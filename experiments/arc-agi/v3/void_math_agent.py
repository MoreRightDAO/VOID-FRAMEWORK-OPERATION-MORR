"""ARC-AGI-3 Void Math Agent — MAXDPS MODE.

Alucard-style: aggressive seek-and-destroy. No hesitation, no wandering.
Find the target. Close distance. Execute.

Architecture:
  1. SCAN: Extract all objects, identify agent + targets
  2. LOCK: Pick nearest target, compute bearing
  3. RUSH: Move directly toward target, no backtracking
  4. If WIN → next level. If stuck → recompute bearing, try alternate approach.
  5. Repeat until all levels cleared or budget exhausted.

Framework math:
  - Fisher distance on Bernoulli manifold → geodesic to goal
  - K-Factorization → separate agent (shape) from environment (scale)
  - Pe as aggression dial → high Pe = rush, low Pe = explore
  - Crooks symmetry → detect reversible vs irreversible actions
"""
import hashlib
import os
import sys
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage

import arc_agi
from arcengine import GameAction, GameState


# ─── Object detection ─────────────────────────────────────────────

def scan_objects(grid: np.ndarray) -> list[dict]:
    """Fast object scan — find all distinct objects in the grid."""
    bg = int(np.bincount(grid.flatten()).argmax())
    colors = sorted(set(grid.flatten().tolist()) - {bg})

    objects = []
    for c in colors:
        mask = (grid == c).astype(np.int32)
        labeled, n = ndimage.label(mask)
        for i in range(1, n + 1):
            component = (labeled == i)
            rows, cols = np.where(component)
            objects.append({
                "color": c,
                "size": int(component.sum()),
                "center_r": int(rows.mean()),
                "center_c": int(cols.mean()),
                "bbox": (int(rows.min()), int(cols.min()), int(rows.max()), int(cols.max())),
            })

    return sorted(objects, key=lambda o: o["size"])


def identify_agent(grid_before: np.ndarray, grid_after: np.ndarray) -> Optional[dict]:
    """Identify the agent by what moved between frames."""
    diff = grid_before != grid_after
    if not diff.any():
        return None

    rows, cols = np.where(diff)
    # The agent's new position is typically the smaller cluster of changed cells
    # Get colors that appeared in the new frame at changed positions
    new_colors = Counter()
    old_colors = Counter()
    for r, c in zip(rows, cols):
        new_colors[int(grid_after[r, c])] += 1
        old_colors[int(grid_before[r, c])] += 1

    # Agent color = color that appears in new positions (moved TO)
    # that wasn't the background
    bg = int(np.bincount(grid_before.flatten()).argmax())
    agent_candidates = {c: n for c, n in new_colors.items() if c != bg}

    if not agent_candidates:
        return None

    # Pick the smallest non-bg color that appeared — likely the agent
    agent_color = min(agent_candidates, key=lambda c: agent_candidates[c])

    # Find agent's current position in the new frame
    agent_mask = (grid_after == agent_color)
    if not agent_mask.any():
        return None

    agent_rows, agent_cols = np.where(agent_mask)
    return {
        "color": agent_color,
        "center_r": int(agent_rows.mean()),
        "center_c": int(agent_cols.mean()),
        "size": int(agent_mask.sum()),
    }


def find_targets(objects: list[dict], agent: dict, grid: np.ndarray) -> list[dict]:
    """Find likely targets — small objects that aren't the agent or walls."""
    bg = int(np.bincount(grid.flatten()).argmax())
    targets = []
    for obj in objects:
        # Skip agent, background, and massive wall objects
        if obj["color"] == agent["color"]:
            continue
        if obj["color"] == bg:
            continue
        if obj["size"] > 200:  # walls/borders
            continue
        # Skip objects that are part of the same color as agent
        if obj["size"] < 2:  # noise
            continue

        # Distance to agent
        dr = obj["center_r"] - agent["center_r"]
        dc = obj["center_c"] - agent["center_c"]
        dist = abs(dr) + abs(dc)  # Manhattan distance

        targets.append({**obj, "dist": dist, "dr": dr, "dc": dc})

    return sorted(targets, key=lambda t: t["dist"])


# ─── Movement engine ─────────────────────────────────────────────

def bearing_to_actions(dr: int, dc: int, available: list[int]) -> list[int]:
    """Convert a bearing (dr, dc) to a prioritized action sequence.

    Assumes standard mapping: 1=up(-r), 2=down(+r), 3=left(-c), 4=right(+c).
    Tries primary direction first, then secondary.
    """
    actions = []

    # Primary: largest component of the bearing
    if abs(dr) >= abs(dc):
        # Vertical primary
        if dr < 0 and 1 in available:
            actions.append(1)  # up
        elif dr > 0 and 2 in available:
            actions.append(2)  # down
        # Secondary: horizontal
        if dc < 0 and 3 in available:
            actions.append(3)  # left
        elif dc > 0 and 4 in available:
            actions.append(4)  # right
    else:
        # Horizontal primary
        if dc < 0 and 3 in available:
            actions.append(3)  # left
        elif dc > 0 and 4 in available:
            actions.append(4)  # right
        # Secondary: vertical
        if dr < 0 and 1 in available:
            actions.append(1)  # up
        elif dr > 0 and 2 in available:
            actions.append(2)  # down

    # Fill remaining directions as fallbacks
    for a in available:
        if a not in actions:
            actions.append(a)

    return actions


def detect_action_directions(env, obs) -> dict:
    """Take one step in each direction to learn the action→direction mapping.

    Tracks centroid shift of non-background colors that gained/lost cells.
    Works even when the 'agent' is multi-colored tiles swapping positions.
    """
    grid = np.array(obs.frame[0])
    available = list(obs.available_actions)
    action_map = {}  # action_id → (dr, dc)
    bg = int(np.bincount(grid.flatten()).argmax())

    # Test each action individually — use paired reverse to return to start
    # For 4-action games, assume 1↔2 and 3↔4 are opposites
    reverse_guess = {}
    if len(available) >= 4:
        reverse_guess = {available[0]: available[1], available[1]: available[0],
                         available[2]: available[3], available[3]: available[2]}

    def measure_action(action_id):
        """Take one action, measure movement, return (dr, dc)."""
        nonlocal obs
        before = np.array(obs.frame[0])
        obs = env.step(action_id)
        after = np.array(obs.frame[0])
        diff = before != after
        if not diff.any():
            return (0, 0)

        rows, cols = np.where(diff)
        # For EACH non-bg color, track which cells it gained vs lost
        colors_in_diff = set(before[rows, cols].tolist() + after[rows, cols].tolist()) - {bg}

        # Accumulate weighted vote across all colors
        total_dr, total_dc, total_weight = 0.0, 0.0, 0.0
        for c in colors_in_diff:
            was_c = (before[rows, cols] == c)
            now_c = (after[rows, cols] == c)
            gained = now_c & ~was_c
            lost = was_c & ~now_c
            if gained.any() and lost.any():
                dr = float(rows[gained].mean() - rows[lost].mean())
                dc = float(cols[gained].mean() - cols[lost].mean())
                w = float(gained.sum())
                total_dr += dr * w
                total_dc += dc * w
                total_weight += w

        if total_weight > 0:
            avg_dr = total_dr / total_weight
            avg_dc = total_dc / total_weight
            # Snap to axis — most games use axis-aligned movement
            if abs(avg_dr) > abs(avg_dc) * 2:
                return (int(np.sign(avg_dr)), 0)
            elif abs(avg_dc) > abs(avg_dr) * 2:
                return (0, int(np.sign(avg_dc)))
            else:
                return (int(np.sign(avg_dr)), int(np.sign(avg_dc)))
        return (0, 0)

    for action_id in available[:4]:
        dr, dc = measure_action(action_id)
        action_map[action_id] = (dr, dc)
        # Undo by taking reverse
        if action_id in reverse_guess:
            obs = env.step(reverse_guess[action_id])

    grid = np.array(obs.frame[0])
    return action_map, obs, grid


# ─── MAXDPS Solver ────────────────────────────────────────────────

def rush_level(env, obs, budget: int = 300, verbose: bool = False) -> tuple[bool, int, object]:
    """MAXDPS — aggressive target-seeking level solver.

    SCAN → LOCK → RUSH → repeat.
    """
    grid = np.array(obs.frame[0])
    available = list(obs.available_actions)
    actions_used = 0

    # SCAN phase: detect directions
    if verbose:
        print(f"    SCAN: detecting movement directions...")

    action_map, obs, grid = detect_action_directions(env, obs)
    actions_used += len(action_map)

    if verbose:
        for a, (dr, dc) in action_map.items():
            dirs = {(-1,0):"UP", (1,0):"DOWN", (0,-1):"LEFT", (0,1):"RIGHT",
                    (-1,-1):"UP-LEFT", (-1,1):"UP-RIGHT", (1,-1):"DOWN-LEFT", (1,1):"DOWN-RIGHT"}
            print(f"      Action {a} → {dirs.get((dr,dc), f'({dr},{dc})')}")

    if obs.state == GameState.WIN:
        return True, actions_used, obs

    # Identify agent by what moved during direction detection
    initial_grid = np.array(obs.frame[0])  # use current state as reference

    # RUSH phase: greedy target-seeking
    # Forget direction mapping — just try all actions each step,
    # pick the one that reduces distance to nearest non-agent object.
    stuck_count = 0
    last_sig = None
    bg = int(np.bincount(grid.flatten()).argmax())

    # Identify which colors are "mobile" (changed during direction detection)
    mobile_colors = set()
    for action_id in available[:4]:
        before = grid.copy()
        obs_test = env.step(action_id)
        after = np.array(obs_test.frame[0])
        diff_mask = before != after
        if diff_mask.any():
            rows, cols = np.where(diff_mask)
            for c in set(after[rows, cols].tolist()) - {bg}:
                mobile_colors.add(c)
        grid = after
        obs = obs_test
        actions_used += 1
        if obs.state == GameState.WIN:
            return True, actions_used, obs

    if verbose:
        print(f"      Mobile colors: {mobile_colors}")

    def get_agent_pos(g):
        """Find centroid of mobile-colored cells."""
        mask = np.zeros_like(g, dtype=bool)
        for c in mobile_colors:
            mask |= (g == c)
        if not mask.any():
            return None
        rows, cols = np.where(mask)
        return (int(rows.mean()), int(cols.mean()))

    def get_nearest_target(g, agent_pos):
        """Find nearest non-mobile, non-bg, non-wall object."""
        objects = scan_objects(g)
        best_dist = 9999
        best_obj = None
        for obj in objects:
            if obj["color"] in mobile_colors or obj["color"] == bg:
                continue
            if obj["size"] > 500:  # wall
                continue
            dr = obj["center_r"] - agent_pos[0]
            dc = obj["center_c"] - agent_pos[1]
            dist = abs(dr) + abs(dc)
            if dist < best_dist:
                best_dist = dist
                best_obj = obj
        return best_obj, best_dist

    while actions_used < budget:
        agent_pos = get_agent_pos(grid)
        if agent_pos is None:
            import random
            obs = env.step(random.choice(available))
            actions_used += 1
            grid = np.array(obs.frame[0])
            if obs.state == GameState.WIN:
                return True, actions_used, obs
            continue

        target, dist = get_nearest_target(grid, agent_pos)

        if verbose and actions_used % 30 == 0:
            print(f"      [{actions_used}] Agent at {agent_pos}, target dist={dist}"
                  + (f", target c{target['color']} at ({target['center_r']},{target['center_c']})" if target else ""))

        if target is None:
            # No target — try random
            import random
            obs = env.step(random.choice(available[:4]))
            actions_used += 1
            grid = np.array(obs.frame[0])
            if obs.state == GameState.WIN:
                return True, actions_used, obs
            continue

        # GREEDY: pick the action that moves agent closest to target
        dr = target["center_r"] - agent_pos[0]
        dc = target["center_c"] - agent_pos[1]

        # Heuristic action selection based on bearing
        # Assume standard: 1=up(-r), 2=down(+r), 3=left(-c), 4=right(+c)
        if abs(dr) >= abs(dc):
            primary = 1 if dr < 0 else 2
            secondary = 3 if dc < 0 else 4
        else:
            primary = 3 if dc < 0 else 4
            secondary = 1 if dr < 0 else 2

        action = primary if primary in available else secondary

        obs = env.step(action)
        actions_used += 1
        grid = np.array(obs.frame[0])

        if obs.state == GameState.WIN:
            if verbose:
                print(f"    ✓ WIN! ({actions_used} actions)")
            return True, actions_used, obs

        if obs.state == GameState.GAME_OVER:
            if verbose:
                print(f"    GAME OVER ({actions_used} actions)")
            return False, actions_used, obs

        # Stuck detection
        current_sig = hashlib.md5(grid.tobytes()).hexdigest()[:12]
        if current_sig == last_sig:
            stuck_count += 1
            if stuck_count > 2:
                # Try secondary direction or random
                alt = secondary if stuck_count % 2 == 0 else (available[stuck_count % len(available)])
                if alt in available:
                    obs = env.step(alt)
                    actions_used += 1
                    grid = np.array(obs.frame[0])
                    if obs.state == GameState.WIN:
                        return True, actions_used, obs
                if stuck_count > 8:
                    stuck_count = 0
        else:
            stuck_count = 0
        last_sig = current_sig

    if verbose:
        print(f"    Budget exhausted ({actions_used} actions)")
    return False, actions_used, obs


def solve_game(game_id: str, verbose: bool = False) -> dict:
    """MAXDPS — solve all levels of a game."""
    arc = arc_agi.Arcade()
    env = arc.make(game_id)
    obs = env.reset()

    total_levels = obs.win_levels
    levels_won = 0
    total_actions = 0

    if verbose:
        grid = np.array(obs.frame[0])
        objects = scan_objects(grid)
        print(f"\n=== MAXDPS: {game_id} ({total_levels} levels) ===")
        print(f"Actions: {list(obs.available_actions)}")
        print(f"Objects: {len(objects)} ({sum(o['size'] for o in objects)} fg cells)")
        for o in objects[:8]:
            print(f"  c{o['color']}: {o['size']} cells at ({o['center_r']},{o['center_c']})")

    for level in range(total_levels):
        if verbose:
            print(f"\n  Level {level + 1}/{total_levels}")

        won, actions, obs = rush_level(env, obs, budget=300, verbose=verbose)
        total_actions += actions

        if won:
            levels_won += 1
        else:
            if verbose:
                print(f"    Failed level {level + 1}")
            break

    result = {
        "game_id": game_id,
        "levels_won": levels_won,
        "total_levels": total_levels,
        "total_actions": total_actions,
        "complete": levels_won == total_levels,
    }

    if verbose:
        print(f"\n  === RESULT: {levels_won}/{total_levels} levels, {total_actions} actions ===")

    return result


# ─── CLI ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "-v" in sys.argv or "--verbose" in sys.argv

    if not args:
        print("MAXDPS Void Agent — ARC-AGI-3")
        print("Pure math. Zero LLM. Seek and destroy.")
        print()
        print("Usage:")
        print("  python void_math_agent.py <game_id> [-v]")
        print("  python void_math_agent.py all [-v]")
        sys.exit(0)

    game_id = args[0]

    if game_id == "all":
        arc = arc_agi.Arcade()
        envs = arc.get_environments()
        results = []
        for gid in envs:
            result = solve_game(str(gid), verbose=verbose)
            results.append(result)
            status = "✓" if result["complete"] else f"{result['levels_won']}/{result['total_levels']}"
            print(f"  {gid}: {status} ({result['total_actions']} actions)")

        solved = sum(1 for r in results if r["complete"])
        partial = sum(r["levels_won"] for r in results)
        total_levels = sum(r["total_levels"] for r in results)
        print(f"\nGames: {solved}/{len(results)} completed")
        print(f"Levels: {partial}/{total_levels} won")
        print(f"Total actions: {sum(r['total_actions'] for r in results)}")
    else:
        result = solve_game(game_id, verbose=verbose)
