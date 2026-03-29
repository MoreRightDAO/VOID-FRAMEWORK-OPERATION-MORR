#!/usr/bin/env python3
"""ARC-AGI-3 AAA Planner — MCTS + Influence Maps + Utility AI.

Techniques from AAA game engines applied to byte-level game solving:

  MCTS with XOR Telescope Rollouts (AlphaGo/MuZero)
    O(1) frame prediction via template composition. PUCT selection.
    Macro actions: proven multi-step sequences as atomic tree edges.
    The telescope makes each MCTS expansion ~1000x cheaper than simulation.

  Influence Mapping (StarCraft / Supreme Commander)
    Fisher cell map → WHERE game rules act (Area of Interest).
    Click target generation from spatial attention heatmap.
    Action priors from template-influence overlap.

  Utility AI (The Sims / Apex Legends)
    Multi-axis leaf evaluation: entropy, novelty, spectral projection.
    Weighted combination for MCTS value function and action priors.

  Frame Data Analysis (Tekken / Street Fighter)
    Every action's frame-by-frame effects catalogued as XOR templates.
    Determinism detection enables exact dead reckoning.
    Cycle exploitation from frame data.

Usage:
  python3 aaa_solver.py --all -q            # All 25 games quiet
  python3 aaa_solver.py tr87-cd924810       # Single game verbose
  python3 aaa_solver.py --all --mcts 1000   # More MCTS iterations
"""

import hashlib
import math
import sys
import os
import time
import argparse
import traceback
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage

# ── v3 imports ──────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import arc_agi
from arcengine import GameState
from packet_probe import probe_game, GameProfile, frame_hash, xor_grids
from packet_analyzer import shannon_entropy
from instanton_planner import (
    TransitionMemory, XORTelescope, InstantonCompiler,
    SpectralNavigator, MacroLibrary, ObservedTransition,
    entropy_beam_search,
)
from spectral_engine import (
    fisher_cell_map, estimate_mechanisms, coordination_barrier,
    ReplicatorDynamics, KramersPotential, FantasiaBound,
)
from eckert_simulator import (
    EckertSimulator, ForwardModel, CellManifold, MechanismTable,
    generate_goal_hypotheses, GoalHypothesis, _safe_grid,
)
from eckert_win_detector import EckertWinDetector, PhiScorer


# ═══════════════════════════════════════════════════════════════════
#  ECKERT PREDICTOR — drop-in for XORTelescope with Eckert model
# ═══════════════════════════════════════════════════════════════════

class EckertPredictor:
    """Wraps Eckert ForwardModel as a telescope-compatible predictor.

    Used by TelescopeMCTS. When prediction confidence is high, uses
    Eckert; falls back to telescope otherwise.
    """

    def __init__(self, eckert_model: ForwardModel,
                 telescope: XORTelescope,
                 min_confidence: float = 0.15):
        self.eckert = eckert_model
        self.telescope = telescope
        self.min_confidence = min_confidence
        self._eckert_hits = 0
        self._telescope_hits = 0

    def predict_single(self, grid, action, click_pos=None):
        """Predict next grid. Prefer Eckert, fall back to telescope."""
        # Try Eckert first
        pred = self.eckert.predict(grid, action, click_pos=click_pos)
        if pred.confidence >= self.min_confidence:
            self._eckert_hits += 1
            return pred.grid

        # Fall back to telescope
        result = self.telescope.predict_single(grid, action,
                                                click_pos=click_pos)
        if result is not None:
            self._telescope_hits += 1
        return result

    @property
    def memory(self):
        """Compatibility: expose telescope's memory for influence priors."""
        return self.telescope.memory


# ═══════════════════════════════════════════════════════════════════
#  GOAL UTILITY SCORER — multi-objective with goal hypotheses
# ═══════════════════════════════════════════════════════════════════

class GoalUtilityScorer:
    """Scores states against active goal hypotheses + entropy.

    Replaces the entropy-only UtilityScorer when goals are available.
    """

    def __init__(self, base_entropy: float, goals: list):
        self.base_entropy = max(base_entropy, 0.001)
        # Filter to valid GoalHypothesis objects only
        self.goals = [g for g in goals[:5] if hasattr(g, 'name')]
        self.best_entropy = base_entropy
        self.best_goal_scores = {g.name: 0.0 for g in self.goals}
        self.seen: set[str] = set()

    def score(self, grid: np.ndarray,
              navigator: Optional[SpectralNavigator] = None) -> float:
        """Multi-axis scoring with goal hypotheses."""
        h = frame_hash(grid)
        ent = shannon_entropy(grid)

        # Entropy axis (0.3 weight)
        ent_score = max(0.0, (self.base_entropy - ent) / self.base_entropy)
        if ent < self.best_entropy:
            self.best_entropy = ent

        # Novelty axis (0.1 weight)
        novel = 1.0 if h not in self.seen else 0.1
        self.seen.add(h)

        # Goal axis (0.6 weight) — best goal score
        goal_score = 0.0
        for g in self.goals:
            try:
                gs = g.score_fn(grid)
                if gs > self.best_goal_scores.get(g.name, 0):
                    self.best_goal_scores[g.name] = gs
                goal_score = max(goal_score, gs)
            except Exception:
                continue

        return 0.3 * ent_score + 0.1 * novel + 0.6 * goal_score


# ═══════════════════════════════════════════════════════════════════
#  INFLUENCE MAP — Fisher cell heatmap as spatial attention (RTS)
# ═══════════════════════════════════════════════════════════════════

class InfluenceMap:
    """RTS-style influence map from Fisher information.

    Identifies the Area of Interest (AOI) — cells where game rules act.
    Uses exponential moving average across observed transitions.
    """

    def __init__(self):
        self.combined: Optional[np.ndarray] = None  # 64×64 float
        self.n_updates = 0

    def update(self, grid_a: np.ndarray, grid_b: np.ndarray):
        fm = fisher_cell_map(grid_a, grid_b)
        if self.combined is None:
            self.combined = fm.copy()
        else:
            alpha = 0.3
            self.combined = alpha * fm + (1 - alpha) * self.combined
        self.n_updates += 1

    def click_targets(self, grid: np.ndarray, n: int = 8) -> list[tuple]:
        """Top-n click targets: (x, y, score). Combines Fisher hotspots
        with non-background color centroids."""
        targets = []
        bg = int(np.bincount(grid.flatten()).argmax())

        # Color centroids weighted by Fisher intensity
        for color in sorted(set(grid.flatten().tolist()) - {bg}):
            pos = np.where(grid == color)
            if len(pos[0]) == 0:
                continue
            cy, cx = int(pos[0].mean()), int(pos[1].mean())
            score = float(self.combined[cy, cx]) if self.combined is not None else 0.5
            targets.append((cx, cy, score))

        # Fisher hotspot centroids (connected components above threshold)
        if self.combined is not None:
            threshold = self.combined.max() * 0.3
            mask = self.combined > threshold
            labeled, n_feat = ndimage.label(mask)
            for i in range(1, n_feat + 1):
                region = np.where(labeled == i)
                if len(region[0]) == 0:
                    continue
                cr, cc = int(region[0].mean()), int(region[1].mean())
                intensity = float(self.combined[labeled == i].mean())
                targets.append((cc, cr, intensity))

        # Deduplicate (merge within 3px)
        merged = []
        for x, y, s in sorted(targets, key=lambda t: -t[2]):
            if not any(abs(x - mx) < 3 and abs(y - my) < 3 for mx, my, _ in merged):
                merged.append((x, y, s))

        return merged[:n]

    def action_prior(self, action: int, memory: TransitionMemory) -> float:
        """Prior weight based on template-influence overlap."""
        if self.combined is None:
            return 1.0
        templates = memory.templates_for_action(action)
        if not templates:
            return 0.5
        total = 0.0
        count = 0
        for t in templates[-5:]:
            r0, c0 = t.origin
            th, tw = t.template.shape
            region = self.combined[max(0, r0):min(64, r0 + th),
                                   max(0, c0):min(64, c0 + tw)]
            total += float(region.mean()) if region.size > 0 else 0
            count += 1
        return max(0.05, total / max(1, count))


# ═══════════════════════════════════════════════════════════════════
#  UTILITY SCORER — multi-axis evaluation (The Sims / Apex)
# ═══════════════════════════════════════════════════════════════════

class UtilityScorer:
    """Multi-axis state evaluation for MCTS leaf nodes and action priors."""

    def __init__(self, base_entropy: float):
        self.base_entropy = max(base_entropy, 0.001)
        self.best_entropy = base_entropy
        self.seen: set[str] = set()

    def score(self, grid: np.ndarray,
              navigator: Optional[SpectralNavigator] = None) -> float:
        """Score ∈ [0, 1]. Higher = better state."""
        ent = shannon_entropy(grid)
        h = frame_hash(grid)

        # Entropy axis (0.7 weight) — lower entropy = better
        ent_score = max(0.0, (self.base_entropy - ent) / self.base_entropy)
        if ent < self.best_entropy:
            self.best_entropy = ent

        # Novelty axis (0.2 weight) — unseen states get bonus
        novel = 1.0 if h not in self.seen else 0.1
        self.seen.add(h)

        # Spectral axis (0.1 weight) — eigenvector projection
        spectral = 0.5
        if navigator and navigator.n_states >= 3:
            spectral = max(0.0, navigator.score_state(h))

        return 0.7 * ent_score + 0.2 * novel + 0.1 * spectral


# ═══════════════════════════════════════════════════════════════════
#  MCTS NODE — tree structure with PUCT
# ═══════════════════════════════════════════════════════════════════

class MCTSNode:
    """MCTS node with AlphaGo-style PUCT selection."""
    __slots__ = ('state_hash', 'grid', 'parent', 'edge',
                 'children', 'visits', 'value_sum', 'prior')

    def __init__(self, state_hash: str, grid: Optional[np.ndarray],
                 parent=None, edge=None, prior: float = 0.5):
        self.state_hash = state_hash
        self.grid = grid            # predicted 64×64 (or None at frontier)
        self.parent = parent
        self.edge = edge            # action that led here (int, or tuple for clicks)
        self.children: dict = {}    # edge_key → MCTSNode
        self.visits = 0
        self.value_sum = 0.0
        self.prior = prior

    @property
    def q(self) -> float:
        return self.value_sum / max(1, self.visits)

    def ucb(self, c_puct: float = 2.0) -> float:
        exploit = self.q
        explore = c_puct * self.prior * math.sqrt(self.parent.visits) / (1 + self.visits)
        return exploit + explore

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0


# ═══════════════════════════════════════════════════════════════════
#  TELESCOPE MCTS — planning in predicted space
# ═══════════════════════════════════════════════════════════════════

class TelescopeMCTS:
    """MCTS engine using XOR telescope for O(1) rollouts.

    From AlphaGo: PUCT selection, value estimation via rollout.
    From RTS:     influence-guided expansion priority.
    From fighting games: frame data as ground truth model.
    """

    def __init__(self, telescope: XORTelescope, influence: InfluenceMap,
                 utility: UtilityScorer, available_actions: list[int],
                 macros: MacroLibrary, navigator: SpectralNavigator):
        self.telescope = telescope
        self.influence = influence
        self.utility = utility
        self.available = available_actions
        self.macros = macros
        self.navigator = navigator
        self.non_click = [a for a in available_actions if a != 6]
        self.has_click = 6 in available_actions
        self.rng = np.random.default_rng()

    def search(self, root_grid: np.ndarray, iterations: int = 500,
               rollout_depth: int = 8) -> list:
        """Run MCTS. Returns best action plan (list of int or (6,x,y) tuples)."""
        root = MCTSNode(frame_hash(root_grid), root_grid)

        for _ in range(iterations):
            # SELECT — traverse by PUCT
            node = root
            while not node.is_leaf:
                node = max(node.children.values(), key=lambda c: c.ucb())

            # EXPAND — telescope predict children
            if node.visits > 0 and node.grid is not None:
                self._expand(node)
                if node.children:
                    node = max(node.children.values(), key=lambda c: c.ucb())

            # ROLLOUT — random in telescope space
            value = self._rollout(node, rollout_depth)

            # BACKPROP
            cur = node
            while cur is not None:
                cur.visits += 1
                cur.value_sum += value
                cur = cur.parent

        return self._extract_plan(root)

    def _expand(self, node: MCTSNode):
        """Add child nodes for all viable actions + clicks + macros."""
        grid = node.grid

        # Keyboard actions
        for action in self.non_click:
            predicted = self.telescope.predict_single(grid, action)
            if predicted is not None:
                h = frame_hash(predicted)
                prior = self.influence.action_prior(action, self.telescope.memory)
                child = MCTSNode(h, predicted, parent=node,
                                 edge=action, prior=prior)
                node.children[action] = child

        # Click actions via influence map targets
        if self.has_click:
            for cx, cy, score in self.influence.click_targets(grid, n=5):
                predicted = self.telescope.predict_single(
                    grid, 6, click_pos=(cx, cy))
                if predicted is not None:
                    h = frame_hash(predicted)
                    key = (6, cx, cy)
                    child = MCTSNode(h, predicted, parent=node,
                                     edge=key, prior=max(0.05, score))
                    node.children[key] = child

        # Best macro as single compound edge
        macro_seq = self.macros.best_macro()
        if macro_seq:
            predicted = self._telescope_chain(grid, macro_seq)
            if predicted is not None:
                h = frame_hash(predicted)
                key = ('macro', tuple(macro_seq))
                child = MCTSNode(h, predicted, parent=node,
                                 edge=key, prior=0.7)
                node.children[key] = child

    def _telescope_chain(self, grid: np.ndarray,
                         actions: list[int]) -> Optional[np.ndarray]:
        """Predict result of action sequence via telescope chaining."""
        current = grid
        for a in actions:
            predicted = self.telescope.predict_single(current, a)
            if predicted is None:
                return None
            current = predicted
        return current

    def _rollout(self, node: MCTSNode, depth: int = 8) -> float:
        """Random rollout in telescope space, scored by utility."""
        if node.grid is None:
            return 0.0

        grid = node.grid
        best = self.utility.score(grid, self.navigator)

        for _ in range(depth):
            if self.non_click and (not self.has_click or self.rng.random() > 0.3):
                action = self.rng.choice(self.non_click)
                predicted = self.telescope.predict_single(grid, action)
            elif self.has_click:
                targets = self.influence.click_targets(grid, n=3)
                if targets:
                    cx, cy, _ = targets[self.rng.integers(len(targets))]
                    predicted = self.telescope.predict_single(
                        grid, 6, click_pos=(cx, cy))
                else:
                    break
            else:
                break

            if predicted is None:
                break
            grid = predicted
            s = self.utility.score(grid, self.navigator)
            if s > best:
                best = s

        return best

    def _extract_plan(self, root: MCTSNode, max_depth: int = 12) -> list:
        """Extract best action sequence by most-visited path."""
        plan = []
        node = root
        while node.children and len(plan) < max_depth:
            best_child = max(node.children.values(), key=lambda c: c.visits)
            edge = best_child.edge
            if isinstance(edge, tuple) and edge[0] == 'macro':
                plan.extend(edge[1])  # expand macro
            else:
                plan.append(edge)     # int or (6, x, y)
            node = best_child
        return plan


# ═══════════════════════════════════════════════════════════════════
#  AAA SOLVER — RECON → MCTS → EXECUTE → VERIFY → REPEAT
# ═══════════════════════════════════════════════════════════════════

class AAASolver:
    """Full AAA game AI solver.

    Phase 1 — RECON: build transition memory via smart exploration
              (RTS scouting: systematic, then influence-guided).
    Phase 2 — PLAN:  MCTS in telescope-predicted space (thousands of
              iterations, zero real actions).
    Phase 3 — EXECUTE: play the planned sequence, verify predictions.
    Phase 4 — ADAPT: if stalled, Kramers escape + re-plan.
    """

    def __init__(self, profile: GameProfile, env, obs, shared_state=None):
        self.profile = profile
        self.env = env
        self.obs = obs
        self.available = list(obs.available_actions)

        # Infrastructure — use shared state if provided
        if shared_state:
            self.memory = shared_state.transitions
            self.telescope = XORTelescope(self.memory)
            self.compiler = InstantonCompiler(self.memory)
            self.navigator = shared_state.navigator
            self.macros = shared_state.macros
        else:
            self.memory = TransitionMemory()
            self.telescope = XORTelescope(self.memory)
            self.compiler = InstantonCompiler(self.memory)
            self.navigator = SpectralNavigator()
            self.macros = MacroLibrary()
        self.influence = InfluenceMap()
        self.kramers = KramersPotential()

        # Eckert simulator — parallel world model for higher-accuracy predictions
        self.eckert = EckertSimulator(profile, shared_state=shared_state)

        # State tracking
        grid = np.array(obs.frame[0])
        self.initial_grid = grid.copy()
        self.base_entropy = shannon_entropy(grid)
        self.utility = UtilityScorer(self.base_entropy)
        self.best_entropy = self.base_entropy
        self.best_frame = grid.copy()
        self.total_actions = 0
        self.levels_solved = 0
        self.frames: list[np.ndarray] = [grid]
        self.actions_taken: list[int] = []
        self.plan_count = 0
        self.mcts_iters_total = 0

    # ── Core step: take action + update everything ──────────────

    def step(self, action: int, click_x=None, click_y=None):
        """Take one real game action, record transition in all systems."""
        prev_grid = np.array(self.obs.frame[0])

        if action == 6 and click_x is not None:
            self.obs = self.env.step(6, data={"x": click_x, "y": click_y})
        else:
            self.obs = self.env.step(action)

        self.total_actions += 1

        # Game may have ended
        if not self.obs.frame:
            return True, prev_grid

        curr_grid = np.array(self.obs.frame[0])
        self.frames.append(curr_grid)
        self.actions_taken.append(action)

        # Record transition (mirrors instanton_planner._record_transition)
        xor = xor_grids(prev_grid, curr_grid)
        is_noop = not xor.any()
        prev_h = frame_hash(prev_grid)
        curr_h = frame_hash(curr_grid)

        # Always feed Eckert (learns from noops too via manifold)
        self.eckert.observe(prev_grid, action, curr_grid)

        if not is_noop:
            rows, cols = np.where(xor > 0)
            r0, c0 = int(rows.min()), int(cols.min())
            r1, c1 = int(rows.max()) + 1, int(cols.max()) + 1
            template = xor[r0:r1, c0:c1].copy()
            template_hash = hashlib.md5(template.tobytes()).hexdigest()[:10]

            changed = xor > 0
            color_map = {}
            for o, n in zip(prev_grid[changed].tolist(),
                            curr_grid[changed].tolist()):
                color_map[o] = n

            t = ObservedTransition(
                action=action, prev_hash=prev_h, curr_hash=curr_h,
                xor_mask=changed, xor_values=xor,
                prev_grid=prev_grid.copy(), curr_grid=curr_grid.copy(),
                origin=(r0, c0), template=template,
                template_hash=template_hash, color_map=color_map,
                entropy_delta=shannon_entropy(curr_grid) - shannon_entropy(prev_grid),
                n_changed=int(changed.sum()),
            )
            self.memory.record(t)
            self.navigator.record_transition(prev_h, curr_h, action)
            self.influence.update(prev_grid, curr_grid)

        # Diagnostics
        ent = shannon_entropy(curr_grid)
        self.kramers.record(ent)
        if ent < self.best_entropy:
            self.best_entropy = ent
            self.best_frame = curr_grid.copy()

        return is_noop, curr_grid

    # ── Phase 1: RECON (smart scouting) ─────────────────────────

    def _recon(self, budget: int = 40):
        """Build transition memory. Systematic first, then influence-guided."""
        non_click = [a for a in self.available if a != 6]
        has_click = 6 in self.available

        def _done():
            return budget <= 0 or self.obs.state in (
                GameState.WIN, GameState.GAME_OVER)

        # A: Systematic — each action twice
        for a in non_click:
            for _ in range(2):
                if _done():
                    return budget
                self.step(a)
                budget -= 1

        # B: Action pairs
        for a in non_click:
            for b in non_click:
                if a == b or _done():
                    continue
                self.step(a)
                budget -= 1
                if _done():
                    return budget
                self.step(b)
                budget -= 1

        # C: Click exploration via influence map
        if has_click and not _done():
            grid = np.array(self.obs.frame[0])
            targets = self.influence.click_targets(grid, n=8)
            if not targets:
                # Bootstrap: click on each non-bg color centroid
                bg = int(np.bincount(grid.flatten()).argmax())
                for color in sorted(set(grid.flatten().tolist()) - {bg}):
                    pos = np.where(grid == color)
                    if len(pos[0]) > 0:
                        targets.append((int(pos[1].mean()),
                                        int(pos[0].mean()), 0.5))
            for cx, cy, _ in targets:
                if _done():
                    return budget
                self.step(6, click_x=cx, click_y=cy)
                budget -= 1

        # Discover macros + fit Kramers
        if len(self.frames) > 5:
            self.macros.discover(self.actions_taken, self.frames)
        self.kramers.fit()
        return budget

    # ── Phase 2: MCTS PLAN ──────────────────────────────────────

    def _build_goal_utility(self, grid: np.ndarray):
        """Build φ-based utility scorer from Eckert win detector.

        Uses thermodynamic progress function instead of hardcoded goals.
        Falls back to GoalUtilityScorer if detector has insufficient data.
        """
        # Use PhiScorer when we have enough observations
        if self.eckert.detector.step >= 10:
            return PhiScorer(self.eckert.detector, self.base_entropy)
        # Fallback to goal hypotheses for early game
        goals = generate_goal_hypotheses(
            self.eckert.table, self.eckert.manifold, self.initial_grid)
        return GoalUtilityScorer(self.base_entropy, goals)

    def _plan(self, iterations: int = 500) -> list:
        """MCTS planning using Eckert + telescope hybrid predictor.

        Uses Eckert forward model when confidence is high (higher accuracy),
        falls back to telescope for speed. Goal-aware utility scoring.
        """
        if not self.obs.frame:
            return []

        grid = np.array(self.obs.frame[0])

        # Build hybrid predictor: Eckert for accuracy, telescope for coverage
        predictor = EckertPredictor(self.eckert.model, self.telescope)

        # Build goal-aware scorer (replaces entropy-only utility)
        # Use it after enough recon data; fall back to entropy-only early on
        if self.eckert.table.rule_count() >= 5:
            utility = self._build_goal_utility(grid)
        else:
            utility = self.utility

        mcts = TelescopeMCTS(
            telescope=predictor,
            influence=self.influence,
            utility=utility,
            available_actions=self.available,
            macros=self.macros,
            navigator=self.navigator,
        )

        plan = mcts.search(grid, iterations=iterations)
        self.plan_count += 1
        self.mcts_iters_total += iterations
        return plan

    # ── Phase 3: EXECUTE ────────────────────────────────────────

    def _execute(self, plan: list, budget: int) -> int:
        """Execute plan, return remaining budget."""
        for step in plan:
            if budget <= 0 or self.obs.state in (
                    GameState.WIN, GameState.GAME_OVER):
                break
            if isinstance(step, tuple):
                # Click: (6, x, y)
                self.step(step[0], click_x=step[1], click_y=step[2])
            else:
                self.step(step)
            budget -= 1
        return budget

    # ── Fallback strategies ─────────────────────────────────────

    def _fallback_plan(self) -> list:
        """When MCTS returns empty, try simpler strategies."""
        if not self.obs.frame:
            return []
        grid = np.array(self.obs.frame[0])

        # 1. Beam search
        plan = entropy_beam_search(self.telescope, grid, self.available)
        if plan:
            return plan

        # 2. Instanton compile toward best known state
        if self.best_frame is not None:
            target_xor = xor_grids(grid, self.best_frame)
            if target_xor.any():
                plan = self.compiler.compile(grid, target_xor, self.available)
                if plan:
                    return plan

        # 3. Spectral navigation
        h = frame_hash(grid)
        nav_action = self.navigator.best_action(
            h, self.available, self.memory.state_graph)
        if nav_action is not None:
            return [nav_action] * 5

        return []

    def _kramers_escape(self, budget: int) -> int:
        """Random perturbation to escape local minimum."""
        rng = np.random.default_rng()
        for _ in range(min(5, budget)):
            if budget <= 0 or self.obs.state in (
                    GameState.WIN, GameState.GAME_OVER):
                break
            action = rng.choice(self.available)
            if action == 6 and self.obs.frame:
                grid = np.array(self.obs.frame[0])
                targets = self.influence.click_targets(grid, n=3)
                if targets:
                    cx, cy, _ = targets[rng.integers(len(targets))]
                    self.step(6, click_x=cx, click_y=cy)
                else:
                    self.step(rng.choice(
                        [a for a in self.available if a != 6] or [6]))
            else:
                self.step(action)
            budget -= 1
        return budget

    # ── Main solve loop ─────────────────────────────────────────

    def solve_level(self, level_budget: int = 200,
                    mcts_iters: int = 500) -> bool:
        start_level = self.obs.levels_completed
        level_start = self.total_actions

        def _remaining():
            return level_budget - (self.total_actions - level_start)

        def _game_ended():
            return self.obs.state in (GameState.WIN, GameState.GAME_OVER)

        # RECON — 25% of budget
        recon_budget = min(50, level_budget // 4)
        self._recon(budget=recon_budget)
        if self.obs.levels_completed > start_level:
            return True

        # PLAN → EXECUTE → VERIFY loop
        stall = 0
        prev_best = self.best_entropy

        while _remaining() > 0 and not _game_ended():
            # PLAN (zero real actions)
            plan = self._plan(iterations=mcts_iters)
            if not plan:
                plan = self._fallback_plan()
            if not plan:
                # Nothing to try — random scramble and retry once
                self._kramers_escape(_remaining())
                plan = self._plan(iterations=mcts_iters)
                if not plan:
                    break

            # EXECUTE
            self._execute(plan, _remaining())
            if self.obs.levels_completed > start_level:
                return True

            # ADAPT — stall detection
            if self.best_entropy >= prev_best - 0.001:
                stall += 1
                if stall >= 3:
                    self._kramers_escape(_remaining())
                    stall = 0
                    if len(self.frames) > 10:
                        self.macros.discover(
                            self.actions_taken[-20:], self.frames[-20:])
                    self.kramers.fit()
            else:
                stall = 0
                prev_best = self.best_entropy

            if self.obs.levels_completed > start_level:
                return True

        return self.obs.levels_completed > start_level

    def solve_game(self, verbose: bool = True,
                   mcts_iters: int = 500) -> dict:
        win_levels = self.profile.win_levels
        for level in range(win_levels):
            if self.obs.state == GameState.GAME_OVER:
                if verbose:
                    print(f"  Level {level}: GAME OVER")
                break

            level_start = self.total_actions
            solved = self.solve_level(mcts_iters=mcts_iters)
            level_acts = self.total_actions - level_start

            if solved:
                self.levels_solved += 1
                if verbose:
                    print(f"  Level {level}: SOLVED in {level_acts} acts | "
                          f"plans={self.plan_count} | "
                          f"mcts={self.mcts_iters_total} | "
                          f"memory={len(self.memory.transitions)}")
            else:
                if verbose:
                    print(f"  Level {level}: FAILED {level_acts} acts | "
                          f"ent={self.best_entropy:.3f} | "
                          f"plans={self.plan_count} | "
                          f"memory={len(self.memory.transitions)}")
                break

        det_summary = self.eckert.detector.summary()
        return {
            "game_id": self.profile.game_id,
            "levels_solved": self.levels_solved,
            "win_levels": win_levels,
            "total_actions": self.total_actions,
            "mcts_plans": self.plan_count,
            "mcts_iterations": self.mcts_iters_total,
            "transitions": len(self.memory.transitions),
            "best_entropy": round(self.best_entropy, 4),
            "final_phi": det_summary.get('phi', 0.0),
            "detector": det_summary,
        }


# ═══════════════════════════════════════════════════════════════════
#  PIPELINE
# ═══════════════════════════════════════════════════════════════════

def solve(game_id: str, probe_budget: int = 30, verbose: bool = True,
          mcts_iters: int = 500, shared_state=None,
          profile: 'GameProfile' = None) -> dict:
    if verbose:
        print(f"\n{'='*65}")
        print(f"  AAA PLANNER: {game_id}")
        print(f"{'='*65}")

    if profile is None:
        profile = probe_game(game_id, budget=probe_budget, verbose=False)

    if verbose:
        n_mech = estimate_mechanisms(profile)
        barrier = coordination_barrier(n_mech)
        print(f"  Profile: {profile.solver_hint()}")
        print(f"  Mechanisms: {n_mech} | Barrier: {barrier:.1f}")

    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    solver = AAASolver(profile, env, obs, shared_state=shared_state)
    result = solver.solve_game(verbose=verbose, mcts_iters=mcts_iters)

    if verbose:
        print(f"\n  RESULT: {result['levels_solved']}/{result['win_levels']} | "
              f"{result['total_actions']} actions | "
              f"{result['mcts_plans']} plans | "
              f"{result['mcts_iterations']} MCTS iters | "
              f"ent={result['best_entropy']}")

    return result


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ARC-AGI-3 AAA Game AI Planner')
    parser.add_argument('game_id', nargs='?', default=None)
    parser.add_argument('-b', '--probe-budget', type=int, default=30)
    parser.add_argument('-v', '--verbose', action='store_true', default=True)
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--mcts', type=int, default=500,
                        help='MCTS iterations per planning phase')
    args = parser.parse_args()

    if args.quiet:
        args.verbose = False

    if args.all or args.game_id is None:
        arcade = arc_agi.Arcade()
        envs = arcade.get_environments()
        results = []

        print(f"\n{'Game':<22s} {'Solved':>7s} {'Acts':>6s} "
              f"{'Plans':>6s} {'MCTS':>8s} {'Ent':>8s}")
        print("-" * 65)

        for e in envs:
            try:
                r = solve(e.game_id, probe_budget=args.probe_budget,
                          verbose=args.verbose, mcts_iters=args.mcts)
                results.append(r)
                if not args.verbose:
                    print(f"{r['game_id']:<22s} "
                          f"{r['levels_solved']}/{r['win_levels']:<5d} "
                          f"{r['total_actions']:>6d} "
                          f"{r['mcts_plans']:>6d} "
                          f"{r['mcts_iterations']:>8d} "
                          f"{r['best_entropy']:>8.3f}")
            except Exception as ex:
                if args.verbose:
                    traceback.print_exc()
                print(f"{e.game_id:<22s} ERROR: {str(ex)[:60]}")

        total = sum(r.get('levels_solved', 0) for r in results)
        possible = sum(r.get('win_levels', 0) for r in results)
        print(f"\nTOTAL: {total}/{possible} levels solved")
    else:
        solve(args.game_id, probe_budget=args.probe_budget,
              verbose=True, mcts_iters=args.mcts)
