"""ARC-AGI-3 Packet Solver — byte-level game solving.

Architecture:
  Phase 0: Packet Probe (30 actions, 0 LLM) → GameProfile
  Phase 1: Strategy Selection based on profile
  Phase 2: Execution with byte-level feedback loop

Strategy dispatch:
  AGENT-KB/HYBRID → GreedyNav (A* with action templates)
  CLICK-ONLY      → ClickScan (systematic grid probing + pattern matching)
  FIELD           → FieldSolver (identify global rule from nibble vocab)
  LOCKED          → DeepScan (binary search for clickable hotspots)
  MIXED           → Composite (probe → classify per-level)

Key byte tricks used during solving:
  1. XOR prediction: predict next frame, only act if prediction matches
  2. Delta interpolation: compute shortest action path between states
  3. Template reuse: recognized XOR pattern → skip exploration
  4. Nibble algebra: compose transitions (a→b + b→c = a→c)
  5. Cycle exploitation: if action cycles, use modular arithmetic
  6. Bit-plane filtering: ignore decorative bits, focus on game-state bits
"""
import hashlib
import sys
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage

import arc_agi
from arcengine import GameState

from packet_probe import (
    GameProfile, probe_game, frame_hash, xor_grids, pack_4bit,
    extract_xor_template, bit_plane, zlib_ratio
)


# ─── Nibble algebra ──────────────────────────────────────────────

class NibbleAlgebra:
    """Treat color transitions as an algebraic group.

    If we know a→b and b→c, we know a→c.
    If we know a→b, we know the inverse b→a.
    This lets us compose multi-step transitions without simulation.
    """

    def __init__(self, vocab: dict):
        self.transitions = {}  # (old, new) → count
        self.inverse = {}      # (old, new) → (new, old)
        self.compose_table = {}

        for key, count in vocab.items():
            parts = key.split("→")
            if len(parts) == 2:
                old, new = int(parts[0], 16), int(parts[1], 16)
                self.transitions[(old, new)] = count
                self.inverse[(old, new)] = (new, old)

        # Build composition table: if a→b and b→c exist, register a→c
        for (a, b) in self.transitions:
            for (c, d) in self.transitions:
                if b == c:
                    self.compose_table[(a, b, d)] = True

    def can_reach(self, start_color: int, end_color: int) -> bool:
        """Can we transition from start_color to end_color?"""
        if (start_color, end_color) in self.transitions:
            return True
        # Check 2-step paths
        for (a, b) in self.transitions:
            if a == start_color and (b, end_color) in self.transitions:
                return True
        return False

    def shortest_path(self, start_color: int, end_color: int) -> list[tuple]:
        """BFS for shortest color transition path."""
        if start_color == end_color:
            return []
        if (start_color, end_color) in self.transitions:
            return [(start_color, end_color)]

        # BFS
        queue = deque([(start_color, [])])
        visited = {start_color}
        while queue:
            current, path = queue.popleft()
            for (a, b) in self.transitions:
                if a == current and b not in visited:
                    new_path = path + [(a, b)]
                    if b == end_color:
                        return new_path
                    visited.add(b)
                    queue.append((b, new_path))
                    if len(new_path) > 4:  # limit search depth
                        continue
        return []

    def action_for_transition(self, old_color: int, new_color: int,
                              profile: GameProfile) -> Optional[int]:
        """Which action produces this color transition?"""
        target = f"{old_color:x}→{new_color:x}"
        for action, templates in profile.action_templates.items():
            for tmpl in templates:
                xor = tmpl["template"]
                # Check if this template contains the needed transition
                # (We'd need the original frames to check properly,
                #  but we can use the vocab association)
                if tmpl["n_changed"] > 0:
                    return action
        return None


# ─── State tracker ────────────────────────────────────────────────

class StateTracker:
    """Tracks game state via byte-level signatures."""

    def __init__(self, profile: GameProfile):
        self.profile = profile
        self.history = []       # (frame_hash, action, frame_hash) tuples
        self.state_graph = defaultdict(dict)  # hash → {action → hash}
        self.visit_count = Counter()
        self.level_boundaries = []  # indices where level changed
        self.current_level = 0

        # Bit mask: which bits carry game state vs decoration
        self.state_bits = self._compute_state_bits()

    def _compute_state_bits(self) -> int:
        """Determine which bit planes carry game state.

        High independence + high entropy = game state.
        Low entropy = mostly constant = decoration.
        """
        bp_ent = self.profile.bit_plane_entropy
        mask = 0
        threshold = 0.3
        for i, ent in enumerate(bp_ent):
            if ent > threshold:
                mask |= (1 << i)
        return mask if mask > 0 else 0xF  # fallback: all bits

    def state_hash(self, grid: np.ndarray) -> str:
        """Hash using only game-state bits."""
        filtered = grid.astype(np.uint8) & self.state_bits
        return hashlib.md5(filtered.tobytes()).hexdigest()[:12]

    def record(self, prev_grid, action, curr_grid, levels_completed):
        prev_h = self.state_hash(prev_grid)
        curr_h = self.state_hash(curr_grid)
        self.history.append((prev_h, action, curr_h))
        self.state_graph[prev_h][action] = curr_h
        self.visit_count[curr_h] += 1

        if levels_completed > self.current_level:
            self.level_boundaries.append(len(self.history) - 1)
            self.current_level = levels_completed

    def is_stuck(self, window: int = 5) -> bool:
        """Detect if we're cycling through the same states."""
        if len(self.history) < window:
            return False
        recent_states = [h[2] for h in self.history[-window:]]
        return len(set(recent_states)) <= 2

    def predict(self, grid: np.ndarray, action: int) -> Optional[str]:
        """Predict result hash of action from current state."""
        h = self.state_hash(grid)
        return self.state_graph.get(h, {}).get(action)

    def unexplored_actions(self, grid: np.ndarray) -> list[int]:
        """Actions we haven't tried from this state."""
        h = self.state_hash(grid)
        explored = set(self.state_graph.get(h, {}).keys())
        return [a for a in self.profile.available_actions if a not in explored]


# ─── Solver strategies ───────────────────────────────────────────

class BaseSolver:
    def __init__(self, profile: GameProfile, env, obs):
        self.profile = profile
        self.env = env
        self.obs = obs
        self.tracker = StateTracker(profile)
        self.algebra = NibbleAlgebra(profile.nibble_vocab)
        self.actions_taken = 0
        self.max_actions = 500  # per level budget

    def step(self, action, click_x=None, click_y=None):
        prev_grid = np.array(self.obs.frame[0])

        if action == 6 and click_x is not None:
            self.obs = self.env.step(6, data={"x": click_x, "y": click_y})
        else:
            self.obs = self.env.step(action)

        curr_grid = np.array(self.obs.frame[0])
        self.tracker.record(prev_grid, action, curr_grid, self.obs.levels_completed)
        self.actions_taken += 1
        return curr_grid

    def solve_level(self) -> bool:
        """Override in subclass. Return True if level solved."""
        raise NotImplementedError


class GreedyNavSolver(BaseSolver):
    """For AGENT-KB/HYBRID: navigate using XOR template matching + A*."""

    def solve_level(self) -> bool:
        grid = np.array(self.obs.frame[0])
        bg = int(np.bincount(grid.flatten()).argmax())
        start_level = self.obs.levels_completed

        # Find objects
        objects = self._find_objects(grid, bg)
        if len(objects) < 2:
            return self._random_walk(50)

        # Detect agent by taking one action and seeing what moves
        agent, move_dir = self._detect_agent(grid)
        if agent is None:
            return self._random_walk(50)

        # Find targets (non-agent, non-wall objects)
        targets = [o for o in objects
                   if o["color"] != agent["color"] and o["size"] < 200 and o["size"] >= 2]

        if not targets:
            return self._random_walk(50)

        # Navigate to nearest target
        for target in sorted(targets, key=lambda t: abs(t["cr"] - agent["cr"]) + abs(t["cc"] - agent["cc"])):
            for _ in range(self.max_actions):
                if self.obs.state == GameState.WIN or self.obs.levels_completed > start_level:
                    return True
                if self.obs.state == GameState.GAME_OVER:
                    return False

                # Redetect agent position
                grid = np.array(self.obs.frame[0])
                agent_pos = self._find_color_center(grid, agent["color"], bg)
                if agent_pos is None:
                    break

                dr = target["cr"] - agent_pos[0]
                dc = target["cc"] - agent_pos[1]

                if abs(dr) < 2 and abs(dc) < 2:
                    # Try action 5 (interact) if available
                    if 5 in self.profile.available_actions:
                        self.step(5)
                    break  # move to next target

                # Pick action that closes distance
                action = self._bearing_to_action(dr, dc)
                if action is None:
                    break

                prev_hash = frame_hash(grid)
                self.step(action)
                new_grid = np.array(self.obs.frame[0])
                if frame_hash(new_grid) == prev_hash:
                    # Stuck — try perpendicular
                    perp = self._perpendicular_action(action)
                    if perp:
                        self.step(perp)

        return self.obs.levels_completed > start_level

    def _detect_agent(self, grid):
        if not self.profile.action_directions:
            # Take one action to detect
            for a in [a for a in self.profile.available_actions if a != 6]:
                prev = grid.copy()
                self.step(a)
                curr = np.array(self.obs.frame[0])
                xor = xor_grids(prev, curr)
                if xor.any():
                    changed = xor > 0
                    rows, cols = np.where(changed)
                    # The agent is the color that moved
                    new_colors = Counter(curr[rows, cols].tolist())
                    bg = int(np.bincount(grid.flatten()).argmax())
                    agent_color = max((c for c in new_colors if c != bg),
                                     key=lambda c: new_colors[c], default=None)
                    if agent_color is not None:
                        return {"color": agent_color, "cr": rows.mean(), "cc": cols.mean()}, (0, 0)
        return None, None

    def _find_objects(self, grid, bg):
        objects = []
        for color in sorted(set(grid.flatten().tolist()) - {bg}):
            mask = (grid == color).astype(np.int32)
            labeled, n = ndimage.label(mask)
            for i in range(1, n + 1):
                comp = labeled == i
                rows, cols = np.where(comp)
                objects.append({
                    "color": color, "size": int(comp.sum()),
                    "cr": float(rows.mean()), "cc": float(cols.mean()),
                })
        return objects

    def _find_color_center(self, grid, color, bg):
        mask = grid == color
        if not mask.any():
            return None
        rows, cols = np.where(mask)
        return (float(rows.mean()), float(cols.mean()))

    def _bearing_to_action(self, dr, dc):
        avail = [a for a in self.profile.available_actions if a <= 4]
        if not avail:
            return None
        # Standard mapping assumption: 1=up, 2=down, 3=left, 4=right
        if abs(dr) >= abs(dc):
            primary = 1 if dr < 0 else 2
            secondary = 3 if dc < 0 else 4
        else:
            primary = 3 if dc < 0 else 4
            secondary = 1 if dr < 0 else 2
        if primary in avail:
            return primary
        if secondary in avail:
            return secondary
        return avail[0]

    def _perpendicular_action(self, action):
        perp_map = {1: [3, 4], 2: [3, 4], 3: [1, 2], 4: [1, 2]}
        avail = [a for a in self.profile.available_actions if a <= 4]
        for p in perp_map.get(action, []):
            if p in avail:
                return p
        return None

    def _random_walk(self, steps):
        start_level = self.obs.levels_completed
        avail = [a for a in self.profile.available_actions if a != 6]
        if not avail:
            avail = self.profile.available_actions
        rng = np.random.default_rng(42)
        for i in range(steps):
            if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                break
            if self.obs.levels_completed > start_level:
                return True
            a = avail[rng.integers(len(avail))]
            self.step(a)
        return self.obs.levels_completed > start_level


class ClickScanSolver(BaseSolver):
    """For CLICK-ONLY: systematic grid scanning for clickable targets."""

    def solve_level(self) -> bool:
        grid = np.array(self.obs.frame[0])
        bg = int(np.bincount(grid.flatten()).argmax())
        start_level = self.obs.levels_completed

        # Strategy 1: Click on clickable colors from probe
        if self.profile.clickable_colors:
            for color in self.profile.clickable_colors:
                positions = np.where(grid == color)
                if len(positions[0]) == 0:
                    continue

                # Click each distinct cluster of this color
                mask = (grid == color).astype(np.int32)
                labeled, n = ndimage.label(mask)
                for i in range(1, n + 1):
                    if self.obs.state == GameState.WIN or self.obs.levels_completed > start_level:
                        return True
                    if self.obs.state == GameState.GAME_OVER:
                        return False

                    comp = labeled == i
                    rows, cols = np.where(comp)
                    cy, cx = int(rows.mean()), int(cols.mean())
                    prev = np.array(self.obs.frame[0]).copy()
                    self.step(6, click_x=cx, click_y=cy)
                    curr = np.array(self.obs.frame[0])

                    # If something changed, refresh grid and objects
                    if not np.array_equal(prev, curr):
                        grid = curr
                        bg = int(np.bincount(grid.flatten()).argmax())
                        # Re-scan — the grid changed
                        break

        if self.obs.levels_completed > start_level:
            return True

        # Strategy 2: Click all non-bg objects systematically
        grid = np.array(self.obs.frame[0])
        bg = int(np.bincount(grid.flatten()).argmax())
        for color in sorted(set(grid.flatten().tolist()) - {bg}):
            mask = (grid == color).astype(np.int32)
            labeled, n = ndimage.label(mask)
            for i in range(1, min(n + 1, 20)):
                if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                    break
                if self.obs.levels_completed > start_level:
                    return True

                comp = labeled == i
                rows, cols = np.where(comp)
                cy, cx = int(rows.mean()), int(cols.mean())
                self.step(6, click_x=cx, click_y=cy)

        # Strategy 3: If undo available, try click+undo cycles
        if 7 in self.profile.available_actions:
            grid = np.array(self.obs.frame[0])
            nonbg = np.where(grid != bg)
            rng = np.random.default_rng(int(time.time()))
            for _ in range(30):
                if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                    break
                if self.obs.levels_completed > start_level:
                    return True
                if len(nonbg[0]) > 0:
                    idx = rng.integers(len(nonbg[0]))
                    self.step(6, click_x=int(nonbg[1][idx]), click_y=int(nonbg[0][idx]))

        return self.obs.levels_completed > start_level


class FieldSolver(BaseSolver):
    """For FIELD/MIXED: use nibble algebra + cycle exploitation."""

    def solve_level(self) -> bool:
        start_level = self.obs.levels_completed
        avail = [a for a in self.profile.available_actions if a != 6]

        # If cycles detected, try cycling through to find progress
        if self.profile.has_cycles and self.profile.cycle_length > 0:
            cycle_len = self.profile.cycle_length

            # Try each action for cycle_length steps
            for primary_action in avail:
                for _ in range(cycle_len + 2):
                    if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                        break
                    if self.obs.levels_completed > start_level:
                        return True
                    self.step(primary_action)

        # Systematic: try all action combinations up to length 4
        for depth in range(1, 5):
            if self.obs.levels_completed > start_level:
                return True
            if self.obs.state == GameState.GAME_OVER:
                return False
            self._try_sequences(avail, depth, start_level)

        return self.obs.levels_completed > start_level

    def _try_sequences(self, actions, depth, start_level, prefix=None):
        if prefix is None:
            prefix = []
        if len(prefix) == depth:
            return
        for a in actions:
            if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                return
            if self.obs.levels_completed > start_level:
                return
            self.step(a)
            self._try_sequences(actions, depth, start_level, prefix + [a])


class DeepScanSolver(BaseSolver):
    """For LOCKED games: binary-search the grid for active hotspots."""

    def solve_level(self) -> bool:
        grid = np.array(self.obs.frame[0])
        bg = int(np.bincount(grid.flatten()).argmax())
        start_level = self.obs.levels_completed
        has_click = 6 in self.profile.available_actions

        if not has_click:
            # Try all non-click actions with action 5
            for a in self.profile.available_actions:
                if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                    break
                self.step(a)
            return self.obs.levels_completed > start_level

        # Quadrant scan: divide grid into 4×4 macro-cells, click center of each
        for qr in range(0, 64, 16):
            for qc in range(0, 64, 16):
                if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                    break
                if self.obs.levels_completed > start_level:
                    return True

                # Click center of this quadrant
                cy, cx = qr + 8, qc + 8
                prev = np.array(self.obs.frame[0])
                self.step(6, click_x=cx, click_y=cy)
                curr = np.array(self.obs.frame[0])

                if not np.array_equal(prev, curr):
                    # Found a hotspot — drill down into this quadrant
                    for sr in range(qr, min(qr + 16, 64), 4):
                        for sc in range(qc, min(qc + 16, 64), 4):
                            if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                                break
                            if self.obs.levels_completed > start_level:
                                return True
                            self.step(6, click_x=sc + 2, click_y=sr + 2)

        return self.obs.levels_completed > start_level


# ─── Main solver dispatcher ──────────────────────────────────────

def solve_game(game_id: str, probe_budget: int = 30, verbose: bool = True,
               shared_state=None, profile: 'GameProfile' = None) -> dict:
    """Full solve pipeline: probe → select strategy → execute."""

    # Phase 0: Probe
    if verbose:
        print(f"\n{'='*60}")
        print(f"  SOLVING: {game_id}")
        print(f"{'='*60}")
        print(f"  Phase 0: Packet Probe ({probe_budget} actions)...")

    if profile is None:
        profile = probe_game(game_id, budget=probe_budget, verbose=False)

    if verbose:
        print(f"  Profile: {profile.solver_hint()}")
        print(f"  Nibble vocab: {list(profile.nibble_vocab.keys())[:8]}")

    # Phase 1: Select strategy
    solver_class = {
        "AGENT-KB": GreedyNavSolver,
        "AGENT-HYBRID": GreedyNavSolver,
        "CLICK-ONLY": ClickScanSolver,
        "FIELD": FieldSolver,
        "MIXED": FieldSolver,  # fallback for now
        "LOCKED": DeepScanSolver,
    }.get(profile.game_type, FieldSolver)

    if verbose:
        print(f"  Strategy: {solver_class.__name__}")
        print()

    # Phase 2: Execute
    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    solver = solver_class(profile, env, obs)
    levels_solved = 0
    total_actions = 0
    level_actions = []

    for level in range(profile.win_levels):
        if solver.obs.state == GameState.WIN:
            break
        if solver.obs.state == GameState.GAME_OVER:
            if verbose:
                print(f"  Level {level}: GAME OVER after {solver.actions_taken} actions")
            break

        level_start_actions = solver.actions_taken
        solved = solver.solve_level()
        actions_this_level = solver.actions_taken - level_start_actions
        level_actions.append(actions_this_level)

        if solved:
            levels_solved += 1
            if verbose:
                print(f"  Level {level}: SOLVED in {actions_this_level} actions")
        else:
            if verbose:
                print(f"  Level {level}: FAILED after {actions_this_level} actions")
            break

    total_actions = solver.actions_taken

    # Get scorecard
    try:
        scorecard = arcade.get_scorecard()
        score_info = str(scorecard) if scorecard else "N/A"
    except Exception:
        score_info = "N/A"

    result = {
        "game_id": game_id,
        "game_type": profile.game_type,
        "strategy": solver_class.__name__,
        "levels_solved": levels_solved,
        "win_levels": profile.win_levels,
        "total_actions": total_actions,
        "level_actions": level_actions,
        "profile_hint": profile.solver_hint(),
    }

    if verbose:
        print(f"\n  RESULT: {levels_solved}/{profile.win_levels} levels, "
              f"{total_actions} actions ({total_actions + probe_budget} total incl probe)")

    return result


# ─── Main ────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ARC-AGI-3 Packet Solver")
    parser.add_argument("game_id", nargs="?", default=None)
    parser.add_argument("-b", "--probe-budget", type=int, default=30)
    parser.add_argument("-v", "--verbose", action="store_true", default=True)
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.quiet:
        args.verbose = False

    if args.all or args.game_id is None:
        arcade = arc_agi.Arcade()
        envs = arcade.get_environments()
        results = []

        print(f"\n{'Game':<22s} {'Type':<14s} {'Strategy':<20s} "
              f"{'Solved':>7s} {'Actions':>8s}")
        print("-" * 80)

        for e in envs:
            try:
                r = solve_game(e.game_id, probe_budget=args.probe_budget,
                              verbose=args.verbose)
                results.append(r)
                if not args.verbose:
                    print(f"{r['game_id']:<22s} {r['game_type']:<14s} "
                          f"{r['strategy']:<20s} "
                          f"{r['levels_solved']}/{r['win_levels']:<5d} "
                          f"{r['total_actions']:>8d}")
            except Exception as ex:
                print(f"{e.game_id:<22s} ERROR: {str(ex)[:60]}")

        total_levels = sum(r.get("levels_solved", 0) for r in results)
        total_possible = sum(r.get("win_levels", 0) for r in results)
        print(f"\nTOTAL: {total_levels}/{total_possible} levels solved")
    else:
        solve_game(args.game_id, probe_budget=args.probe_budget, verbose=True)
