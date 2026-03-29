"""ARC-AGI-3 Void Agent — Framework-guided interactive game solver.

The agent treats each game as a void: opaque (rules hidden), responsive
(reacts to actions), coupled (engagement determines efficiency).

Strategy: Constraint Identification → Goal Inference → Efficient Execution

Architecture:
  Phase 1 — SCRY: Systematic exploration. Take actions, observe changes.
             Build a world model from state transitions.
  Phase 2 — BIND: Identify constraints (what doesn't change) and rituals
             (what sequences produce progress). Infer the goal.
  Phase 3 — CAST: Execute the inferred solution efficiently.
             Minimize actions (RHAE penalty is quadratic).

Each phase maps to a Pe regime:
  SCRY = high Pe (explore broadly, accept uncertainty)
  BIND = medium Pe (analyze, narrow hypotheses)
  CAST = low Pe (execute known plan precisely)
"""
import hashlib
import json
import os
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

import arc_agi
from arcengine import GameAction, GameState

# LLM backend (reuse from parent)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from llm_solver import call_llm, extract_code, API_KEY, BACKEND, MODEL


# ─── Frame analysis utilities ────────────────────────────────────

def frame_hash(grid: np.ndarray) -> str:
    """Hash a 64x64 grid for dedup."""
    return hashlib.md5(grid.tobytes()).hexdigest()[:12]


def frame_diff(a: np.ndarray, b: np.ndarray) -> dict:
    """Analyze what changed between two frames."""
    if a.shape != b.shape:
        return {"shape_change": True, "a_shape": a.shape, "b_shape": b.shape}

    changed = a != b
    n_changed = int(changed.sum())

    if n_changed == 0:
        return {"changed": False, "n_changed": 0}

    # Find bounding box of changes
    rows, cols = np.where(changed)
    r_min, r_max = int(rows.min()), int(rows.max())
    c_min, c_max = int(cols.min()), int(cols.max())

    # Color transitions
    transitions = Counter()
    for r, c in zip(rows, cols):
        transitions[(int(a[r, c]), int(b[r, c]))] += 1

    return {
        "changed": True,
        "n_changed": n_changed,
        "bbox": (r_min, c_min, r_max, c_max),
        "transitions": dict(transitions),
        "pct_changed": round(n_changed / a.size, 4),
    }


def find_objects(grid: np.ndarray, bg: int = 0) -> list[dict]:
    """Find connected components (objects) in the grid."""
    visited = set()
    objects = []
    h, w = grid.shape

    for r in range(h):
        for c in range(w):
            if grid[r, c] != bg and (r, c) not in visited:
                # BFS
                color = int(grid[r, c])
                component = set()
                queue = [(r, c)]
                visited.add((r, c))
                while queue:
                    cr, cc = queue.pop(0)
                    component.add((cr, cc))
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < h and 0 <= nc < w and (nr, nc) not in visited:
                            if grid[nr, nc] == color:
                                visited.add((nr, nc))
                                queue.append((nr, nc))

                rows = [p[0] for p in component]
                cols = [p[1] for p in component]
                objects.append({
                    "color": color,
                    "size": len(component),
                    "bbox": (min(rows), min(cols), max(rows), max(cols)),
                    "center": (sum(rows) // len(rows), sum(cols) // len(cols)),
                })

    return sorted(objects, key=lambda o: o["size"], reverse=True)


def grid_to_compact(grid: np.ndarray, max_rows: int = 20) -> str:
    """Compact string representation of a grid region."""
    # Find content bounds
    nonzero = grid != 0
    if not nonzero.any():
        return "(empty grid)"
    rows_with_content = np.any(nonzero, axis=1)
    cols_with_content = np.any(nonzero, axis=0)
    r_min = np.where(rows_with_content)[0][0]
    r_max = np.where(rows_with_content)[0][-1]
    c_min = np.where(cols_with_content)[0][0]
    c_max = np.where(cols_with_content)[0][-1]

    region = grid[r_min:r_max+1, c_min:c_max+1]
    symbols = ".123456789ABCDEF"
    lines = []
    for i, row in enumerate(region):
        if i >= max_rows:
            lines.append(f"... ({region.shape[0] - max_rows} more rows)")
            break
        lines.append("".join(symbols[min(c, 15)] for c in row[:50]))
        if region.shape[1] > 50:
            lines[-1] += "..."
    return f"[{r_min}:{r_max+1}, {c_min}:{c_max+1}]\n" + "\n".join(lines)


# ─── State memory ────────────────────────────────────────────────

@dataclass
class StateMemory:
    """Tracks observed states and transitions for world-model building."""
    frames: dict = field(default_factory=dict)        # hash -> grid
    transitions: list = field(default_factory=list)    # (hash_from, action, hash_to, diff)
    action_effects: dict = field(default_factory=dict) # action -> list of effects
    dead_ends: set = field(default_factory=set)        # states where all actions loop
    progress_actions: list = field(default_factory=list)  # actions that changed something new

    def record(self, grid_before: np.ndarray, action: str, grid_after: np.ndarray,
               game_state: GameState):
        """Record a state transition."""
        h_before = frame_hash(grid_before)
        h_after = frame_hash(grid_after)

        if h_before not in self.frames:
            self.frames[h_before] = grid_before.copy()
        if h_after not in self.frames:
            self.frames[h_after] = grid_after.copy()

        diff = frame_diff(grid_before, grid_after)
        self.transitions.append((h_before, action, h_after, diff))

        if action not in self.action_effects:
            self.action_effects[action] = []
        self.action_effects[action].append(diff)

        # Track if this action made progress (new state or visual change)
        if diff["changed"] and h_after not in {t[2] for t in self.transitions[:-1]}:
            self.progress_actions.append((action, diff))

    @property
    def n_unique_states(self) -> int:
        return len(self.frames)

    @property
    def n_transitions(self) -> int:
        return len(self.transitions)

    def summarize(self) -> str:
        """Human-readable summary for LLM context."""
        parts = [f"States seen: {self.n_unique_states}, Transitions: {self.n_transitions}"]

        # Action effect summary
        for action, effects in self.action_effects.items():
            changed = sum(1 for e in effects if e.get("changed", False))
            parts.append(f"  Action {action}: {changed}/{len(effects)} caused changes")

        # Progress actions
        if self.progress_actions:
            parts.append(f"  Progress actions: {len(self.progress_actions)}")
            for action, diff in self.progress_actions[-5:]:
                parts.append(f"    {action}: {diff['n_changed']} cells changed")

        return "\n".join(parts)


# ─── The Void Agent system prompt ─────────────────────────────────

VOID_AGENT_PROMPT = """You are playing an interactive game on a 64×64 grid with 16 colors. No instructions are given. You must discover the rules and goals by exploring.

## Your Framework: Constraint → Ritual → Execution

You approach every game as a void — an opaque, responsive system whose rules must be inferred:

### Phase 1: SCRY (Explore)
- Try each available action and observe what changes
- Track: which cells moved? What colors appeared/disappeared? Did objects shift position?
- Build a mental map: what are the objects? What's the agent? What's the environment?
- Identify the BACKGROUND (most common color) vs OBJECTS vs AGENT (the thing you control)

### Phase 2: BIND (Identify Constraints)
From your observations, identify:
- **Walls**: colors/regions that block movement
- **Goals**: regions that look like destinations (different color, enclosed spaces, markers)
- **Interactables**: objects that change when you interact (ACTION5) or click (ACTION6)
- **Rules**: what happens when the agent touches colored cells? Do colors change? Do objects move?
- **Win condition**: what state triggers level completion? (Agent reaches goal? All objects matched? Pattern completed?)

### Phase 3: CAST (Execute)
Once you understand the rules:
- Plan the SHORTEST path to the goal
- Execute precisely — every extra action costs you quadratically (RHAE scoring)
- If stuck, RESET is better than flailing (wastes fewer actions)

## Key Principles

1. **Constraints before operations**: Identify what CAN'T change before planning what to DO
2. **Information budget**: Each action reveals information. Maximize info-per-action in exploration
3. **Single-scale reasoning**: The game operates at ONE scale — figure out if it's cell-level, object-level, or grid-level
4. **Prohibition-ritual pairs**: Every game mechanic is a constraint (prohibition) paired with an allowed action (ritual). Find the pairs.

## Color Semantics (common patterns)
- Color 0 = background/empty
- Bright colors (1-4) = often interactive objects or the agent
- Dark/muted colors (5-8) = often walls, borders, environment
- Accent colors (9-15) = often goals, markers, or special items

## Action Space
- ACTION1-4: Directional movement (up/down/left/right)
- ACTION5: Interact/select/rotate/execute
- ACTION6(x,y): Click at coordinates
- RESET: Restart current level

## Response Format
Respond with JUST the action to take. Examples:
- ACTION1
- ACTION3
- ACTION6 32 16
- RESET

Think about what you've observed so far and what action will give you the most information or progress toward the goal."""


# ─── Solver loop ─────────────────────────────────────────────────

def solve_level(env, obs, memory: StateMemory, max_actions: int = 100,
                verbose: bool = False) -> tuple[bool, int, object]:
    """Solve a single level using the void agent framework.

    Returns (won, actions_taken, last_obs).
    """
    actions_taken = 0
    grid = np.array(obs.frame[0])
    available = list(obs.available_actions)

    # Phase 1: SCRY — systematic exploration
    # Do multiple rounds to build a real world model
    scry_budget = min(20, max_actions // 4)  # Use ~25% of budget for exploration
    if verbose:
        print(f"    SCRY: {scry_budget} exploration steps with actions {available}")

    scry_results = []
    initial_grid = grid.copy()

    # Round 1: try each action once from starting position
    for action_id in available[:5]:
        grid_before = grid.copy()
        obs = env.step(action_id)
        actions_taken += 1
        grid_after = np.array(obs.frame[0])
        diff = frame_diff(grid_before, grid_after)
        memory.record(grid_before, str(action_id), grid_after, obs.state)
        scry_results.append((str(action_id), diff))
        grid = grid_after

        if obs.state == GameState.WIN:
            if verbose:
                print(f"    WIN during SCRY! ({actions_taken} actions)")
            return True, actions_taken, obs

        if verbose and diff["changed"]:
            print(f"      Action {action_id}: {diff['n_changed']} cells changed")

    # Round 2: explore further — try repeated actions to find walls/boundaries
    for _ in range(scry_budget - len(available)):
        if actions_taken >= scry_budget:
            break
        # Try the action that caused the most change
        best_action = max(scry_results, key=lambda x: x[1].get("n_changed", 0))[0]
        action_id = int(best_action)
        grid_before = grid.copy()
        obs = env.step(action_id)
        actions_taken += 1
        grid_after = np.array(obs.frame[0])
        diff = frame_diff(grid_before, grid_after)
        memory.record(grid_before, str(action_id), grid_after, obs.state)
        grid = grid_after

        if obs.state == GameState.WIN:
            if verbose:
                print(f"    WIN during SCRY! ({actions_taken} actions)")
            return True, actions_taken, obs

        # If we hit a wall (no change), try a different direction
        if not diff["changed"]:
            other_actions = [a for a in available if str(a) != best_action]
            if other_actions:
                action_id = other_actions[actions_taken % len(other_actions)]
                grid_before = grid.copy()
                obs = env.step(action_id)
                actions_taken += 1
                grid_after = np.array(obs.frame[0])
                diff = frame_diff(grid_before, grid_after)
                memory.record(grid_before, str(action_id), grid_after, obs.state)
                grid = grid_after

                if obs.state == GameState.WIN:
                    return True, actions_taken, obs

    if verbose:
        print(f"    SCRY complete: {memory.n_unique_states} states, {actions_taken} actions used")

    # Phase 2: BIND — ask LLM to analyze and plan
    if verbose:
        print(f"    BIND: Analyzing {memory.n_unique_states} states, {memory.n_transitions} transitions")

    # Build context for LLM — focus on SPATIAL RELATIONSHIPS, not raw grid data
    # The LLM can't reason about a 64x64 text grid. Give it object-level info.

    init_objects = find_objects(initial_grid)
    cur_objects = find_objects(grid)

    # Find the agent: the object whose position changed most between states
    agent_color = None
    if init_objects and cur_objects:
        for io in init_objects:
            for co in cur_objects:
                if io["color"] == co["color"] and io["center"] != co["center"]:
                    if io["size"] < 100:  # agent is usually small
                        agent_color = io["color"]
                        break
            if agent_color:
                break

    # Identify what the agent moved across/through during exploration
    traversed_colors = set()
    for _, effects in memory.action_effects.items():
        for e in effects:
            if e.get("transitions"):
                for (c_from, c_to), count in e["transitions"].items():
                    traversed_colors.add(c_from)
                    traversed_colors.add(c_to)

    bg_color = int(np.bincount(initial_grid.flatten()).argmax())

    context_parts = [
        f"=== GAME ANALYSIS ===",
        f"Grid: 64×64, background color: {bg_color}",
        f"Available actions: {available} (directional movement: 1,2,3,4)",
        f"",
        f"=== OBJECTS IN THE SCENE ===",
    ]

    for obj in init_objects[:15]:
        label = ""
        if obj["color"] == agent_color:
            label = " ← AGENT (you control this)"
        elif obj["size"] > 500:
            label = " ← BACKGROUND/WALL"
        elif obj["size"] < 20:
            label = " ← small object (goal? item?)"
        context_parts.append(
            f"  Color {obj['color']}: {obj['size']} cells, "
            f"center=({obj['center'][0]},{obj['center'][1]}), "
            f"bbox=({obj['bbox'][0]},{obj['bbox'][1]})-({obj['bbox'][2]},{obj['bbox'][3]}){label}"
        )

    if agent_color is not None:
        # Find current agent position
        agent_now = [o for o in cur_objects if o["color"] == agent_color]
        agent_init = [o for o in init_objects if o["color"] == agent_color]
        if agent_now and agent_init:
            context_parts.append(f"")
            context_parts.append(f"=== AGENT MOVEMENT ===")
            context_parts.append(f"  Agent (color {agent_color}) started at center {agent_init[0]['center']}")
            context_parts.append(f"  Agent is now at center {agent_now[0]['center']}")
            context_parts.append(f"  Moved by: ({agent_now[0]['center'][0]-agent_init[0]['center'][0]}, {agent_now[0]['center'][1]-agent_init[0]['center'][1]})")

    context_parts.append(f"")
    context_parts.append(f"=== EXPLORATION RESULTS ({actions_taken} actions) ===")
    context_parts.append(memory.summarize())

    # Action-direction mapping from exploration
    context_parts.append(f"")
    context_parts.append(f"=== ACTION EFFECTS ===")
    for action_str, diff in scry_results:
        if diff.get("changed") and diff.get("transitions"):
            # Infer direction from how agent moved
            context_parts.append(f"  Action {action_str}: {diff['n_changed']} cells changed")

    context_parts.append(f"")
    context_parts.append(f"=== YOUR TASK ===")
    context_parts.append(f"You are the agent (color {agent_color}). Navigate to the goal.")
    context_parts.append(f"Look at the small objects — one is likely the goal/destination.")
    context_parts.append(f"Give a SHORT sequence of actions to reach it.")
    context_parts.append(f"Reply with actions, one per line: ACTION1, ACTION2, ACTION3, or ACTION4.")
    context_parts.append(f"IMPORTANT: Be VERY efficient — extra actions cost you quadratically.")

    context = "\n".join(context_parts)

    try:
        response = call_llm(context, system=VOID_AGENT_PROMPT, temperature=0.3)
        # Parse action sequence
        plan = []
        for line in response.strip().split("\n"):
            line = line.strip().upper()
            for i in range(1, 7):
                if f"ACTION{i}" in line:
                    plan.append(str(i))
                    break
            if "RESET" in line:
                plan.append("RESET")
        if verbose:
            print(f"    CAST: Plan has {len(plan)} actions")
    except Exception as e:
        if verbose:
            print(f"    LLM failed: {e}")
        plan = []

    # Phase 3: CAST — execute the plan
    for action_str in plan:
        if actions_taken >= max_actions:
            break

        if action_str == "RESET":
            obs = env.reset()
            grid = np.array(obs.frame[0])
            continue

        action_id = int(action_str)
        grid_before = grid.copy()
        obs = env.step(action_id)
        actions_taken += 1
        grid = np.array(obs.frame[0])
        memory.record(grid_before, action_str, grid, obs.state)

        if obs.state == GameState.WIN:
            if verbose:
                print(f"    WIN! ({actions_taken} actions)")
            return True, actions_taken, obs

        if obs.state == GameState.GAME_OVER:
            if verbose:
                print(f"    GAME OVER ({actions_taken} actions)")
            return False, actions_taken, obs

    # If plan didn't work, try iterative LLM guidance
    remaining = max_actions - actions_taken
    for step in range(min(remaining, 50)):
        # Ask LLM for next action based on current state
        step_context = [
            f"Current grid state (step {actions_taken}):",
            grid_to_compact(grid),
            f"Available actions: {available}",
            f"Actions taken so far: {actions_taken}",
            f"Previous action effects: {memory.summarize()}",
            "",
            "What is the SINGLE best next action? Reply with just the action (e.g., ACTION1).",
        ]

        try:
            response = call_llm("\n".join(step_context), system=VOID_AGENT_PROMPT, temperature=0.2)
            # Parse single action
            action_id = None
            for i in range(1, 7):
                if f"ACTION{i}" in response.upper():
                    action_id = i
                    break

            if action_id is None:
                continue

            grid_before = grid.copy()
            obs = env.step(action_id)
            actions_taken += 1
            grid = np.array(obs.frame[0])
            memory.record(grid_before, str(action_id), grid, obs.state)

            if obs.state == GameState.WIN:
                if verbose:
                    print(f"    WIN! ({actions_taken} actions)")
                return True, actions_taken

            if obs.state == GameState.GAME_OVER:
                if verbose:
                    print(f"    GAME OVER ({actions_taken} actions)")
                return False, actions_taken

        except Exception:
            break

    if verbose:
        print(f"    Level incomplete ({actions_taken} actions, best state: {memory.n_unique_states} states seen)")
    return False, actions_taken, obs


def play_game(game_id: str, verbose: bool = False) -> dict:
    """Play an entire game (all levels)."""
    arc = arc_agi.Arcade()
    env = arc.make(game_id)
    obs = env.reset()

    total_levels = obs.win_levels
    levels_won = 0
    total_actions = 0
    memory = StateMemory()

    if verbose:
        print(f"\n=== Game: {game_id} ({total_levels} levels) ===")
        print(f"Available actions: {[str(a) for a in obs.available_actions]}")

    for level in range(total_levels):
        if verbose:
            print(f"\n  Level {level + 1}/{total_levels}")

        won, actions, obs = solve_level(env, obs, memory, max_actions=100, verbose=verbose)
        total_actions += actions

        if won:
            levels_won += 1
            if obs.state == GameState.WIN and obs.levels_completed < total_levels:
                # Game continues to next level — obs already has the new level state
                pass
        else:
            if verbose:
                print(f"  Failed level {level + 1}")
            break

    scorecard = arc.get_scorecard()

    result = {
        "game_id": game_id,
        "levels_won": levels_won,
        "total_levels": total_levels,
        "total_actions": total_actions,
        "complete": levels_won == total_levels,
    }

    if verbose:
        print(f"\n  Result: {levels_won}/{total_levels} levels, {total_actions} actions")

    return result


# ─── CLI ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "-v" in sys.argv or "--verbose" in sys.argv

    if not args:
        print("Void Agent — ARC-AGI-3 Solver")
        print("=" * 40)
        print()
        print("Usage:")
        print("  python void_agent.py <game_id> [-v]    # play one game")
        print("  python void_agent.py all [-v]           # play all available games")
        print()
        print(f"Backend: {BACKEND} | Model: {MODEL}")
        print(f"API key: {'set' if API_KEY else 'NOT SET'}")
        print()

        # List available games
        arc = arc_agi.Arcade()
        envs = arc.get_environments()
        print(f"Available games ({len(envs)}):")
        for e in envs:
            print(f"  {e}")
        sys.exit(0)

    game_id = args[0]

    if game_id == "all":
        arc = arc_agi.Arcade()
        envs = arc.get_environments()
        results = []
        for gid in envs:
            result = play_game(gid, verbose=verbose)
            results.append(result)
            status = "✓" if result["complete"] else f"{result['levels_won']}/{result['total_levels']}"
            print(f"  {gid}: {status} ({result['total_actions']} actions)")

        solved = sum(1 for r in results if r["complete"])
        print(f"\nTotal: {solved}/{len(results)} games completed")
    else:
        result = play_game(game_id, verbose=verbose)
        print(f"\n{'='*40}")
        print(f"Game: {result['game_id']}")
        print(f"Levels: {result['levels_won']}/{result['total_levels']}")
        print(f"Actions: {result['total_actions']}")
        print(f"Complete: {result['complete']}")
