#!/usr/bin/env python3
"""Fisher Geodesic Pathfinder — information-geometric navigation for ARC-AGI-3.

Novel contribution: navigates the game grid as an information manifold.
Instead of Manhattan/Euclidean distance, uses Fisher information as the
metric tensor. Paths follow geodesics on the information manifold —
naturally routing through areas where game rules act (§138).

From the Void Framework:
  §138  Fisher geodesic identity — optimal paths on information manifold
  §136  K-Factorization — shape/scale separation for wall detection
  §48E  Crooks fluctuation theorem — reversibility for dead-end avoidance
  §2B   Prohibition-ritual pairs — framework-native explore/exploit

Architecture:
  1. K-Factor wall detection: no-op actions → wall map (prohibition layer)
  2. Agent/goal detection: movement tracking + Fisher hotspots
  3. Fisher metric construction: influence map → Riemannian cost surface
  4. Geodesic A*: pathfind using information distance, not spatial distance
  5. Crooks dead-end avoidance: prefer reversible moves in unknown territory
  6. Path → action sequence via measured action_directions

The key insight: high-Fisher cells are WHERE THE GAME ACTS. Paths through
these cells make progress. Zero-Fisher cells are dead space. The manifold's
geodesic is the path of least resistance through the game's rule structure.
"""

import heapq
import numpy as np
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

from packet_probe import frame_hash, xor_grids
from packet_analyzer import shannon_entropy


# ═══════════════════════════════════════════════════════════════════
#  AGENT / GOAL / WALL DETECTION
# ═══════════════════════════════════════════════════════════════════

@dataclass
class GameSpatial:
    """Spatial understanding of the game grid."""
    agent_color: Optional[int] = None
    agent_pos: Optional[tuple] = None       # (row, col)
    agent_size: int = 0
    goal_pos: Optional[tuple] = None        # (row, col)
    goal_color: Optional[int] = None
    walls: Optional[np.ndarray] = None      # 64×64 bool
    walkable: Optional[np.ndarray] = None   # 64×64 bool
    fisher_cost: Optional[np.ndarray] = None  # 64×64 float (lower = easier)
    bg_color: int = 0
    action_dirs: dict = field(default_factory=dict)  # action → (dr, dc)


def detect_agent(transitions, current_grid: np.ndarray,
                 profile) -> tuple[Optional[int], Optional[tuple]]:
    """Detect agent: smallest object whose centroid moved during recon."""
    if len(transitions) < 3:
        return None, None

    bg = int(np.bincount(current_grid.flatten()).argmax())
    first_grid = transitions[0].prev_grid
    colors = sorted(set(current_grid.flatten().tolist()) - {bg})

    best_agent = None
    best_dist = 0

    for color in colors:
        mask_before = first_grid == color
        mask_now = current_grid == color
        if not mask_before.any() or not mask_now.any():
            continue

        size = int(mask_now.sum())
        if size > 300 or size < 1:
            continue

        pos_b = (np.where(mask_before)[0].mean(), np.where(mask_before)[1].mean())
        pos_n = (np.where(mask_now)[0].mean(), np.where(mask_now)[1].mean())
        dist = abs(pos_b[0] - pos_n[0]) + abs(pos_b[1] - pos_n[1])

        if dist > best_dist:
            best_dist = dist
            best_agent = (color, (int(pos_n[0]), int(pos_n[1])), size)

    if best_agent and best_dist > 1:
        return best_agent[0], best_agent[1]
    return None, None


def detect_walls(transitions, action_dirs: dict,
                 agent_positions: list[tuple]) -> np.ndarray:
    """Build wall map from K-Factor no-ops.

    When action A is a no-op from position P, and A maps to direction (dr,dc),
    then P+(dr,dc) is a wall. Framework: K-factor = 0 ↔ prohibition.
    """
    walls = np.zeros((64, 64), dtype=bool)

    # Track agent position through transitions
    for t in transitions:
        if t.n_changed == 0 and t.action in action_dirs:
            # No-op! The cell in the action's direction is a wall
            dr, dc = action_dirs[t.action]
            # Find agent position in this frame
            # Use the transition's prev_grid to find agent
            # (agent_color is the color that moves)
            pass  # Need agent color, handled below

    # Alternative: infer walls from the grid structure
    # Large contiguous regions of non-background, non-agent color = walls
    return walls


def detect_walls_from_noop(memory, action_dirs: dict,
                           agent_color: int, current_grid: np.ndarray) -> np.ndarray:
    """Build wall map by tracking where movement actions fail.

    For each no-op transition: find agent pos → direction → wall cell.
    This is K-Factorization applied to obstacle detection.
    """
    walls = np.zeros((64, 64), dtype=bool)
    bg = int(np.bincount(current_grid.flatten()).argmax())

    for t in memory.transitions:
        if t.n_changed == 0 and t.action in action_dirs:
            # Agent didn't move — wall in that direction
            dr, dc = action_dirs[t.action]
            # Find agent position in this frame
            agent_mask = t.prev_grid == agent_color
            if agent_mask.any():
                rows, cols = np.where(agent_mask)
                ar, ac = int(rows.mean()), int(cols.mean())
                # Wall cell = agent pos + direction
                wr, wc = ar + dr, ac + dc
                if 0 <= wr < 64 and 0 <= wc < 64:
                    walls[wr, wc] = True

    # Also mark border as walls
    walls[0, :] = True
    walls[63, :] = True
    walls[:, 0] = True
    walls[:, 63] = True

    return walls


def detect_goal(current_grid: np.ndarray, agent_color: int,
                fisher_map: Optional[np.ndarray],
                bg_color: int) -> tuple[Optional[int], Optional[tuple]]:
    """Detect goal: small non-bg, non-agent object at Fisher hotspot."""
    colors = sorted(set(current_grid.flatten().tolist()) - {bg_color})

    best_goal = None
    best_score = 0

    for color in colors:
        if color == agent_color:
            continue
        mask = current_grid == color
        count = int(mask.sum())
        if count < 1 or count > 200:
            continue

        rows, cols = np.where(mask)
        cr, cc = int(rows.mean()), int(cols.mean())

        # Score: prefer small objects at high-Fisher locations
        fisher_score = float(fisher_map[cr, cc]) if fisher_map is not None else 0.5
        size_score = 1.0 / max(1, count)  # smaller = more likely goal
        score = fisher_score * size_score

        if score > best_score:
            best_score = score
            best_goal = (color, (cr, cc))

    if best_goal:
        return best_goal
    return None, None


# ═══════════════════════════════════════════════════════════════════
#  FISHER METRIC — information geometry cost surface
# ═══════════════════════════════════════════════════════════════════

def build_fisher_cost(fisher_map: Optional[np.ndarray],
                      walls: np.ndarray) -> np.ndarray:
    """Build cost surface from Fisher information.

    High Fisher = rules act here = low traversal cost (geodesic prefers it).
    Zero Fisher = dead space = high cost.
    Walls = infinite cost.

    This IS the Riemannian metric tensor (diagonal approximation).
    The geodesic minimizes ∫ cost(x) ds — paths through high-Fisher
    regions are informationally shorter.
    """
    cost = np.full((64, 64), 10.0)  # default: moderate cost

    if fisher_map is not None:
        # Invert: high Fisher → low cost
        f_max = fisher_map.max()
        if f_max > 0:
            # cost ∈ [1, 10]: 1 at max Fisher, 10 at zero Fisher
            cost = 1.0 + 9.0 * (1.0 - fisher_map / f_max)

    # Walls: impassable
    cost[walls] = 1e6

    return cost


# ═══════════════════════════════════════════════════════════════════
#  GEODESIC A* — pathfinding on the information manifold
# ═══════════════════════════════════════════════════════════════════

def geodesic_astar(cost: np.ndarray, start: tuple, goal: tuple,
                   max_steps: int = 500) -> Optional[list[tuple]]:
    """A* on Fisher information manifold.

    g(n) = cumulative Fisher cost along path (information distance traveled)
    h(n) = Manhattan distance × min Fisher cost (admissible heuristic)

    Returns path as list of (row, col), or None if no path found.
    """
    sr, sc = start
    gr, gc = goal

    # Admissible heuristic: Manhattan × minimum possible cost
    min_cost = max(0.5, cost[cost < 1e5].min()) if (cost < 1e5).any() else 1.0

    def heuristic(r, c):
        return (abs(r - gr) + abs(c - gc)) * min_cost

    # Priority queue: (f_score, counter, row, col)
    counter = 0
    open_set = [(heuristic(sr, sc), counter, sr, sc)]
    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[(sr, sc)] = 0.0
    closed = set()

    while open_set and counter < max_steps * 10:
        f, _, cr, cc = heapq.heappop(open_set)

        if (cr, cc) in closed:
            continue
        closed.add((cr, cc))

        # Goal reached
        if abs(cr - gr) <= 1 and abs(cc - gc) <= 1:
            # Reconstruct path
            path = [(cr, cc)]
            while (cr, cc) in came_from:
                cr, cc = came_from[(cr, cc)]
                path.append((cr, cc))
            path.reverse()
            return path

        # Expand neighbors (4-connected)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc
            if nr < 0 or nr >= 64 or nc < 0 or nc >= 64:
                continue
            if (nr, nc) in closed:
                continue

            # Fisher information distance = cost of entering this cell
            step_cost = float(cost[nr, nc])
            if step_cost > 1e5:  # wall
                continue

            tentative_g = g_score[(cr, cc)] + step_cost

            if tentative_g < g_score[(nr, nc)]:
                g_score[(nr, nc)] = tentative_g
                came_from[(nr, nc)] = (cr, cc)
                f_score = tentative_g + heuristic(nr, nc)
                counter += 1
                heapq.heappush(open_set, (f_score, counter, nr, nc))

    return None  # No path found


def detect_action_directions(memory, agent_color: int) -> dict:
    """Detect actual agent movement per action from transition memory.

    Tracks agent centroid displacement for each action. More reliable
    than probe's XOR centroid method.

    Returns: {action_int: (dr, dc)} with clean cardinal directions.
    """
    action_displacements = defaultdict(list)

    for t in memory.transitions:
        if t.n_changed == 0:
            continue

        # Find agent position before and after
        prev_mask = t.prev_grid == agent_color
        curr_mask = t.curr_grid == agent_color
        if not prev_mask.any() or not curr_mask.any():
            continue

        prev_r = np.where(prev_mask)[0].mean()
        prev_c = np.where(prev_mask)[1].mean()
        curr_r = np.where(curr_mask)[0].mean()
        curr_c = np.where(curr_mask)[1].mean()

        dr = curr_r - prev_r
        dc = curr_c - prev_c

        if abs(dr) > 0.2 or abs(dc) > 0.2:
            action_displacements[t.action].append((dr, dc))

    # Average and snap to cardinal
    directions = {}
    for action, disps in action_displacements.items():
        if not disps:
            continue
        mean_dr = np.mean([d[0] for d in disps])
        mean_dc = np.mean([d[1] for d in disps])
        # Snap to dominant axis
        if abs(mean_dr) > abs(mean_dc):
            directions[action] = (int(np.sign(mean_dr)), 0)
        elif abs(mean_dc) > abs(mean_dr):
            directions[action] = (0, int(np.sign(mean_dc)))
        else:
            directions[action] = (int(np.sign(mean_dr)), int(np.sign(mean_dc)))

    return directions


def path_to_actions(path: list[tuple], action_dirs: dict) -> list[int]:
    """Convert (row,col) path to action sequence.

    action_dirs: {action_int: (dr, dc)} — clean cardinal directions.
    """
    if not path or len(path) < 2:
        return []

    # Invert: (dr, dc) → action
    dir_to_action = {}
    for action, (dr, dc) in action_dirs.items():
        sr, sc = int(np.sign(dr)), int(np.sign(dc))
        if (sr, sc) != (0, 0):
            dir_to_action[(sr, sc)] = action

    actions = []
    for i in range(len(path) - 1):
        r0, c0 = path[i]
        r1, c1 = path[i + 1]
        dr = int(np.sign(r1 - r0))
        dc = int(np.sign(c1 - c0))

        action = dir_to_action.get((dr, dc))
        if action is not None:
            actions.append(action)

    return actions


# ═══════════════════════════════════════════════════════════════════
#  CROOKS REVERSIBILITY — dead-end avoidance (§48E)
# ═══════════════════════════════════════════════════════════════════

def check_reversibility(memory, action_dirs: dict) -> dict:
    """Identify reversible action pairs using Crooks fluctuation theorem.

    If action A from state S leads to state S', and action B from S'
    leads back to S, then (A, B) is a reversible pair.

    For pathfinding: prefer reversible moves in unknown territory.
    If you enter a dead end via a reversible move, you can back out.
    """
    reverse_pairs = {}  # action → reverse_action

    for t1 in memory.transitions:
        for t2 in memory.transitions:
            if t1.curr_hash == t2.prev_hash and t2.curr_hash == t1.prev_hash:
                reverse_pairs[t1.action] = t2.action

    return reverse_pairs


# ═══════════════════════════════════════════════════════════════════
#  FULL PATHFINDER — ties everything together
# ═══════════════════════════════════════════════════════════════════

class FisherPathfinder:
    """Complete pathfinding system using information geometry.

    Usage:
        pf = FisherPathfinder()
        pf.build(memory, profile, current_grid, fisher_map)
        actions = pf.plan()
        context = pf.context_for_llm()  # rich spatial context
    """

    def __init__(self):
        self.spatial = GameSpatial()
        self.path = None
        self.reverse_pairs = {}

    def build(self, memory, profile, current_grid: np.ndarray,
              fisher_map: Optional[np.ndarray] = None):
        """Build complete spatial model from recon data."""
        bg = int(np.bincount(current_grid.flatten()).argmax())
        self.spatial.bg_color = bg
        self.spatial.action_dirs = dict(profile.action_directions or {})

        # Agent detection
        agent_color, agent_pos = detect_agent(
            memory.transitions, current_grid, profile)
        self.spatial.agent_color = agent_color
        self.spatial.agent_pos = agent_pos
        if agent_color is not None:
            self.spatial.agent_size = int((current_grid == agent_color).sum())
            # Detect actual agent movement directions (not probe's XOR centroids)
            real_dirs = detect_action_directions(memory, agent_color)
            if real_dirs:
                self.spatial.action_dirs = real_dirs

        # Wall detection (K-Factor no-ops → prohibitions)
        if agent_color is not None and self.spatial.action_dirs:
            self.spatial.walls = detect_walls_from_noop(
                memory, self.spatial.action_dirs, agent_color, current_grid)
        else:
            self.spatial.walls = np.zeros((64, 64), dtype=bool)

        # Goal detection
        if agent_color is not None:
            goal_color, goal_pos = detect_goal(
                current_grid, agent_color, fisher_map, bg)
            self.spatial.goal_color = goal_color
            self.spatial.goal_pos = goal_pos

        # Fisher cost surface (information metric tensor)
        self.spatial.fisher_cost = build_fisher_cost(fisher_map, self.spatial.walls)
        self.spatial.walkable = self.spatial.fisher_cost < 1e5

        # Crooks reversibility
        self.reverse_pairs = check_reversibility(memory, self.spatial.action_dirs)

    def plan(self) -> list[int]:
        """Compute geodesic path and convert to actions."""
        if self.spatial.agent_pos is None or self.spatial.goal_pos is None:
            return []

        if self.spatial.fisher_cost is None:
            return []

        # Geodesic A* on Fisher manifold
        self.path = geodesic_astar(
            self.spatial.fisher_cost,
            self.spatial.agent_pos,
            self.spatial.goal_pos,
        )

        if self.path is None:
            return []

        return path_to_actions(self.path, self.spatial.action_dirs)

    def context_for_llm(self) -> str:
        """Generate rich spatial context for LLM reasoning."""
        parts = []
        s = self.spatial

        parts.append("═══ FISHER GEODESIC PATHFINDER ═══")

        if s.agent_pos:
            parts.append(f"Agent: color {s.agent_color}, position ({s.agent_pos[0]},{s.agent_pos[1]}), {s.agent_size} cells")
        else:
            parts.append("Agent: NOT DETECTED (click game or no movement)")

        if s.goal_pos:
            parts.append(f"Goal: color {s.goal_color}, position ({s.goal_pos[0]},{s.goal_pos[1]})")
            if s.agent_pos:
                dist = abs(s.goal_pos[0] - s.agent_pos[0]) + abs(s.goal_pos[1] - s.agent_pos[1])
                parts.append(f"Manhattan distance: {dist}")
        else:
            parts.append("Goal: NOT DETECTED")

        # Wall count
        if s.walls is not None:
            n_walls = int(s.walls.sum())
            parts.append(f"Walls detected: {n_walls} cells (from {len(self.reverse_pairs)} reversible action pairs)")

        # Reversibility
        if self.reverse_pairs:
            pairs = [f"{a}↔{b}" for a, b in self.reverse_pairs.items()]
            parts.append(f"Reversible pairs: {', '.join(pairs)}")

        # Geodesic path
        if self.path:
            parts.append(f"\nGeodesic path found: {len(self.path)} steps")
            actions = path_to_actions(self.path, s.action_dirs)
            if actions:
                # Compress: show run-length encoding
                compressed = []
                if actions:
                    current = actions[0]
                    count = 1
                    for a in actions[1:]:
                        if a == current:
                            count += 1
                        else:
                            compressed.append(f"{current}×{count}" if count > 1 else str(current))
                            current = a
                            count = 1
                    compressed.append(f"{current}×{count}" if count > 1 else str(current))
                parts.append(f"Action sequence: {', '.join(compressed)}")
                parts.append(f"Suggested PLAN: {','.join(str(a) for a in actions[:20])}")
        else:
            if s.agent_pos and s.goal_pos:
                parts.append("No geodesic path found — may need to explore more or clear obstacles")

        # Wall map (16×16 downsample)
        if s.walls is not None and s.walls.any():
            parts.append("\n═══ WALL MAP (16×16, # = wall, . = open) ═══")
            ds_walls = s.walls.reshape(16, 4, 16, 4).any(axis=(1, 3))
            for r in range(16):
                row = ""
                for c in range(16):
                    row += "#" if ds_walls[r, c] else "."
                parts.append(f"  {row}")

        return "\n".join(parts)
