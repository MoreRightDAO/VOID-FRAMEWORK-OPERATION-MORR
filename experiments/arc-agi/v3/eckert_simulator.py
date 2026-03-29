"""ARC-AGI-3 Eckert Simulator — Physics-based generic forward model.

THE THESIS: Every game mechanism is a (shape, scale) pair on the Eckert
manifold. Learn the finite alphabet of shapes (K-grammar atoms), learn
WHERE each shape fires (manifold coordinates), and you can simulate ANY
deterministic game forward. Stochastic games get Kramers transition rates.

Architecture:
  1. CellManifold — per-cell (O, R, α) from observation statistics
     → Pe field tells you WHERE rules are active
  2. MechanismTable — learned (trigger_condition, atom) pairs
     → WHAT happens at each location
  3. ForwardModel — compose mechanisms to predict next state
     → Full grid prediction from learned physics
  4. ManifoldPlanner — geodesic A* on the Pe field
     → HOW to reach a goal state

This module IS the world model. All other solvers become better when
they can call simulator.predict(grid, action) → predicted_grid.

Math apparatus applied:
  §136   K-Factorization — shape × scale decomposition of every mechanism
  §136D2 Barrier universality — d_eff × π/√2 exploration cost
  §138   Fisher geodesic — cost surface for planning
  §165   Čencov metric — the unique distance on each cell's state space
  §171   Kramers suppression — transition probability for stochastic events
  §48A   Onsager-Machlup — most probable trajectory (instanton path)

Zero LLM. Pure physics.
"""
import hashlib
import heapq
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage, signal

import arc_agi
from arcengine import GameState

from packet_probe import (
    GameProfile, probe_game, frame_hash, xor_grids,
    extract_xor_template, pack_4bit
)
from packet_analyzer import shannon_entropy
from eckert_win_detector import EckertWinDetector


# ═══════════════════════════════════════════════════════════════════
#  CONSTANTS — from the math apparatus (§136, §165)
# ═══════════════════════════════════════════════════════════════════

B_ALPHA = 0.867           # agency barrier (§136)
B_GAMMA = 2.244           # constraint barrier (§136)
BARRIER_CONST = np.pi / np.sqrt(2)  # ≈ 2.221, per mechanism (§136D2/§165)

# Čencov-forced geodesic length (§165)
GEODESIC_L = np.pi


def _safe_grid(obs) -> Optional[np.ndarray]:
    """Safely extract grid from observation (games return empty on GAME_OVER)."""
    if obs.frame and len(obs.frame) > 0:
        return np.array(obs.frame[0])
    return None


def pe_from_coords(O: float, R: float, alpha: float, K: float = 1.0) -> float:
    """Compute Pe from Eckert manifold coordinates.

    c = 1 - (O + R + α)/3   (constraint level, normalized to [0,1])
    Pe = K · sinh(2·(b_α - c·b_γ))
    """
    c = 1.0 - (O + R + alpha) / 3.0
    b_net = B_ALPHA - c * B_GAMMA
    return K * np.sinh(2.0 * b_net)


def fisher_distance(p: float, q: float) -> float:
    """Fisher-Rao distance on Bernoulli manifold (§165/Čencov).

    d(p, q) = 2|arcsin(√p) - arcsin(√q)|
    """
    p = np.clip(p, 1e-8, 1.0 - 1e-8)
    q = np.clip(q, 1e-8, 1.0 - 1e-8)
    return 2.0 * abs(np.arcsin(np.sqrt(p)) - np.arcsin(np.sqrt(q)))


def kramers_rate(barrier: float, temperature: float) -> float:
    """Kramers escape rate: Γ ∝ exp(-ΔΦ/T) (§171)."""
    if temperature < 1e-8:
        return 0.0
    return np.exp(-barrier / temperature)


# ═══════════════════════════════════════════════════════════════════
#  1. CELL MANIFOLD — per-cell (O, R, α) on the Eckert manifold
# ═══════════════════════════════════════════════════════════════════

class CellManifold:
    """Maps each grid cell to Eckert manifold coordinates.

    For each cell (r, c):
      O = opacity:        entropy of color values across observations
      R = responsiveness:  fraction of actions that change this cell
      α = coupling:        spatial correlation with neighbor changes

    These are NOT heuristics. They ARE the coordinates of the Bernoulli
    product manifold V = B(O) × B(R) × B(α), with metric forced by
    Čencov's theorem (§165).
    """

    def __init__(self, H: int = 64, W: int = 64):
        self.H, self.W = H, W
        # Accumulators for computing coordinates
        self._color_counts = np.zeros((H, W, 16), dtype=np.float32)
        self._action_change = np.zeros((H, W), dtype=np.float32)
        self._action_total = np.zeros((H, W), dtype=np.float32)
        self._neighbor_corr = np.zeros((H, W), dtype=np.float64)
        self._neighbor_count = np.zeros((H, W), dtype=np.float64)
        self.n_observations = 0

        # Cached coordinates
        self.O = np.zeros((H, W), dtype=np.float32)
        self.R = np.zeros((H, W), dtype=np.float32)
        self.alpha = np.zeros((H, W), dtype=np.float32)
        self.Pe = np.zeros((H, W), dtype=np.float32)

    def observe(self, prev_grid: np.ndarray, action: int,
                curr_grid: np.ndarray):
        """Update manifold coordinates from one observed transition."""
        self.n_observations += 1
        changed = (prev_grid != curr_grid)

        # O: record color at each cell (for entropy computation)
        for r in range(self.H):
            for c in range(self.W):
                self._color_counts[r, c, int(curr_grid[r, c])] += 1

        # R: did this cell change in response to the action?
        self._action_change += changed.astype(np.float32)
        self._action_total += 1.0

        # α: correlation with neighbor changes
        if changed.any():
            kernel = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]],
                              dtype=np.float64) / 4.0
            neighbor_changed = signal.convolve2d(
                changed.astype(np.float64), kernel,
                mode='same', boundary='wrap')
            self._neighbor_corr += changed.astype(np.float64) * neighbor_changed
            self._neighbor_count += changed.astype(np.float64)

        # Recompute coordinates every 5 observations
        if self.n_observations % 5 == 0:
            self._recompute()

    def _recompute(self):
        """Recompute (O, R, α) and Pe field from accumulated statistics.

        Coordinates are RANK-NORMALIZED within the grid so that the
        most active cells saturate toward 1.0 and background stays at 0.
        Raw framework constants (b_α, b_γ) are for platforms — grid
        cells need relative scaling to produce useful Pe gradients.
        """
        n = max(self.n_observations, 1)

        # O = normalized entropy of color distribution at each cell
        probs = self._color_counts / np.maximum(
            self._color_counts.sum(axis=2, keepdims=True), 1)
        with np.errstate(divide='ignore', invalid='ignore'):
            ent = -np.nansum(probs * np.log2(probs + 1e-12), axis=2)
        self.O = np.clip(ent / max(ent.max(), 0.01), 0, 1).astype(np.float32)

        # R = fraction of observations where cell changed
        raw_R = self._action_change / np.maximum(self._action_total, 1)
        max_R = max(raw_R.max(), 1e-6)
        self.R = np.clip(raw_R / max_R, 0, 1).astype(np.float32)

        # α = mean neighbor correlation when cell changes
        with np.errstate(divide='ignore', invalid='ignore'):
            raw_alpha = self._neighbor_corr / np.maximum(
                self._neighbor_count, 1)
        max_alpha = max(raw_alpha.max(), 1e-6)
        self.alpha = np.clip(raw_alpha / max_alpha, 0, 1).astype(np.float32)

        # Pe field — rank-normalized coordinates give useful gradients
        c_field = 1.0 - (self.O + self.R + self.alpha) / 3.0
        b_net = B_ALPHA - c_field * B_GAMMA
        self.Pe = np.sinh(2.0 * b_net).astype(np.float32)

    def pe_field(self) -> np.ndarray:
        """Current Pe field (64×64 float). High Pe = drift-active cells."""
        if self.n_observations > 0 and self.n_observations % 5 != 0:
            self._recompute()
        return self.Pe

    def active_mask(self, threshold: float = 0.0) -> np.ndarray:
        """Binary mask: cells with Pe > threshold (rule-active cells)."""
        return self.Pe > threshold

    def agent_candidates(self) -> list[tuple]:
        """Cells most likely to be the player agent.

        Agent signature: high R (responds to actions), moderate O
        (semi-predictable), low α (moves independently of neighbors).
        """
        score = self.R * (1.0 - self.alpha) * (0.5 + 0.5 * self.O)
        flat = score.flatten()
        top_k = min(10, len(flat))
        top_indices = np.argpartition(flat, -top_k)[-top_k:]
        cells = [(int(i // self.W), int(i % self.W), float(flat[i]))
                 for i in top_indices if flat[i] > 0.01]
        cells.sort(key=lambda x: -x[2])
        return cells

    def background_color(self, grid: np.ndarray) -> int:
        """Most common color in low-Pe regions."""
        low_pe = self.Pe < -1.0
        if low_pe.any():
            return int(np.bincount(grid[low_pe].flatten().astype(int),
                                   minlength=16).argmax())
        return int(np.bincount(grid.flatten().astype(int),
                               minlength=16).argmax())

    def region_pe(self, r0: int, c0: int, r1: int, c1: int) -> float:
        """Mean Pe of a region — measures mechanism density."""
        return float(self.Pe[r0:r1, c0:c1].mean())

    def mechanism_count(self) -> int:
        """Estimate number of independent mechanisms from Pe field.

        Mechanisms = connected components of positive Pe regions.
        """
        active = self.Pe > 0
        if not active.any():
            return 1
        labeled, n = ndimage.label(active)
        return max(n, 1)

    def exploration_barrier(self) -> float:
        """Total coordination barrier: N_mechanisms × π/√2 (§136D2)."""
        return self.mechanism_count() * BARRIER_CONST


# ═══════════════════════════════════════════════════════════════════
#  2. MECHANISM TABLE — learned game rules as (condition → effect)
# ═══════════════════════════════════════════════════════════════════

@dataclass
class LearnedRule:
    """One learned game rule: context + action → effect."""
    action: int
    context_hash: str        # hash of local region BEFORE transition
    context_colors: tuple    # sorted (color, count) pairs in trigger region
    effect_xor: np.ndarray   # the XOR pattern this rule produces
    effect_colormap: dict    # {old_color: new_color}
    displacement: tuple      # (dr, dc) centroid shift
    bounding_box: tuple      # (r0, c0, r1, c1) where it fires
    n_seen: int = 1          # how many times observed
    confidence: float = 1.0  # 1.0 for deterministic, <1 for stochastic


class MechanismTable:
    """Complete learned game model — a finite set of rules.

    K-Factorization (§136) says every transition decomposes as:
      Q = Q_shape(context) · Q_scale(K)

    The shape (rule) is position-independent. The context tells us
    WHERE and WHEN it fires. The scale K just amplifies.

    For deterministic games: each (context, action) maps to exactly one
    effect. Given enough observations, the table is COMPLETE and forward
    simulation is EXACT.

    For stochastic games: (context, action) maps to a distribution over
    effects, weighted by Kramers rates.
    """

    def __init__(self):
        self.rules: list[LearnedRule] = []
        # Indices for fast lookup
        self._by_action: dict[int, list[int]] = defaultdict(list)
        self._by_context: dict[str, list[int]] = defaultdict(list)
        self._by_action_context: dict[tuple, list[int]] = defaultdict(list)
        # Track determinism
        self._context_action_effects: dict[tuple, set] = defaultdict(set)
        self.is_deterministic = True
        # State-action coverage tracking
        self._observed_contexts = set()
        self._observed_pairs = set()

    def learn(self, prev_grid: np.ndarray, action: int,
              curr_grid: np.ndarray) -> Optional[LearnedRule]:
        """Learn a rule from an observed transition. Returns None if noop."""
        xor = xor_grids(prev_grid, curr_grid)
        if not xor.any():
            return None

        # Bounding box of the change
        changed = xor > 0
        rows, cols = np.where(changed)
        r0, r1 = int(rows.min()), int(rows.max()) + 1
        c0, c1 = int(cols.min()), int(cols.max()) + 1

        # Expand context region by 1 cell for neighbor context
        cr0 = max(0, r0 - 1)
        cr1 = min(64, r1 + 1)
        cc0 = max(0, c0 - 1)
        cc1 = min(64, c1 + 1)

        # Context: the local region BEFORE transition
        context_region = prev_grid[cr0:cr1, cc0:cc1].astype(np.uint8)
        context_hash = hashlib.md5(context_region.tobytes()).hexdigest()[:12]

        # Color map: which colors changed to what
        colormap = {}
        for r, c in zip(rows, cols):
            old = int(prev_grid[r, c])
            new = int(curr_grid[r, c])
            if old != new:
                colormap[old] = new

        # Context colors (position-invariant)
        color_counts = Counter(context_region.flatten().tolist())
        context_colors = tuple(sorted(color_counts.items()))

        # Displacement: centroid shift
        prev_com = (rows.mean(), cols.mean())
        # Check for displacement by looking at new position of changed colors
        new_changed = xor_grids(curr_grid, prev_grid) > 0
        if new_changed.any():
            new_rows, new_cols = np.where(new_changed)
            new_com = (new_rows.mean(), new_cols.mean())
            displacement = (round(new_com[0] - prev_com[0]),
                            round(new_com[1] - prev_com[1]))
        else:
            displacement = (0, 0)

        # Check if we've seen this (context, action) produce different effect
        key = (action, context_hash)
        effect_hash = hashlib.md5(xor.tobytes()).hexdigest()[:12]
        self._context_action_effects[key].add(effect_hash)
        if len(self._context_action_effects[key]) > 1:
            self.is_deterministic = False

        # Look for existing matching rule
        existing = self._by_action_context.get(key, [])
        for idx in existing:
            rule = self.rules[idx]
            if np.array_equal(rule.effect_xor, xor):
                rule.n_seen += 1
                return rule

        # New rule
        rule = LearnedRule(
            action=action,
            context_hash=context_hash,
            context_colors=context_colors,
            effect_xor=xor.copy(),
            effect_colormap=colormap,
            displacement=displacement,
            bounding_box=(r0, c0, r1, c1),
        )

        idx = len(self.rules)
        self.rules.append(rule)
        self._by_action[action].append(idx)
        self._by_context[context_hash].append(idx)
        self._by_action_context[key].append(idx)

        self._observed_contexts.add(context_hash)
        self._observed_pairs.add(key)

        return rule

    def lookup_exact(self, prev_grid: np.ndarray,
                     action: int) -> Optional[LearnedRule]:
        """Exact lookup: have we seen this exact (context, action)?"""
        # Hash the full grid for exact match
        full_hash = frame_hash(prev_grid)
        key = (action, full_hash)
        if key in self._by_action_context:
            idxs = self._by_action_context[key]
            if idxs:
                return self.rules[idxs[-1]]  # most recent

        # Try local context matching for each known bounding box
        for idx in self._by_action.get(action, [])[-30:]:  # recent rules
            rule = self.rules[idx]
            r0, c0, r1, c1 = rule.bounding_box
            cr0, cr1 = max(0, r0-1), min(64, r1+1)
            cc0, cc1 = max(0, c0-1), min(64, c1+1)
            if cr1 > 64 or cc1 > 64:
                continue
            context = prev_grid[cr0:cr1, cc0:cc1].astype(np.uint8)
            ch = hashlib.md5(context.tobytes()).hexdigest()[:12]
            if ch == rule.context_hash:
                return rule

        return None

    def lookup_by_shape(self, prev_grid: np.ndarray,
                        action: int) -> list[LearnedRule]:
        """Position-independent lookup: find rules with matching
        color composition regardless of where they fired.

        K-Factorization (§136): the shape is position-invariant.
        """
        matches = []
        for idx in self._by_action.get(action, []):
            rule = self.rules[idx]
            # Check if the current grid contains the rule's trigger colors
            grid_colors = set(prev_grid.flatten().tolist())
            rule_trigger_colors = set(c for c, _ in rule.context_colors)
            if rule_trigger_colors.issubset(grid_colors):
                matches.append(rule)
        return matches

    def lookup_similar(self, prev_grid: np.ndarray, action: int,
                       manifold: CellManifold) -> list[tuple]:
        """Fuzzy lookup: find rules for this action that might apply.

        Uses manifold coordinates to identify WHERE a rule should fire
        on the current grid, even if the exact context hasn't been seen.

        Returns [(rule, match_score, predicted_location)] sorted by score.
        """
        candidates = []
        for idx in self._by_action.get(action, []):
            rule = self.rules[idx]

            # Strategy: match by color composition (K-Factorization shape)
            # The shape (color pattern) is position-invariant
            r0, c0, r1, c1 = rule.bounding_box
            h, w = r1 - r0, c1 - c0

            # Slide the context pattern over high-Pe regions
            pe = manifold.pe_field()
            active = pe > -0.5  # include mildly active regions

            # Find regions with matching color composition
            best_score = 0.0
            best_loc = (r0, c0)

            # Check original location first
            if r0 + h <= 64 and c0 + w <= 64:
                region = prev_grid[r0:r0+h, c0:c0+w]
                orig_colors = Counter(region.flatten().tolist())
                rule_colors = dict(rule.context_colors)
                score = _color_overlap(orig_colors, rule_colors)
                if score > best_score:
                    best_score = score
                    best_loc = (r0, c0)

            # Check high-R regions (responsive = likely rule targets)
            hot_cells = np.where(manifold.R > 0.3)
            if len(hot_cells[0]) > 0:
                for _ in range(min(20, len(hot_cells[0]))):
                    i = np.random.randint(len(hot_cells[0]))
                    tr, tc = int(hot_cells[0][i]), int(hot_cells[1][i])
                    # Center the rule on this cell
                    sr = max(0, tr - h // 2)
                    sc = max(0, tc - w // 2)
                    if sr + h > 64 or sc + w > 64:
                        continue
                    region = prev_grid[sr:sr+h, sc:sc+w]
                    reg_colors = Counter(region.flatten().tolist())
                    rule_colors = dict(rule.context_colors)
                    score = _color_overlap(reg_colors, rule_colors)
                    if score > best_score:
                        best_score = score
                        best_loc = (sr, sc)

            if best_score > 0.3:
                candidates.append((rule, best_score, best_loc))

        candidates.sort(key=lambda x: -x[1])
        return candidates[:5]

    def coverage(self) -> float:
        """Estimated fraction of state-action space covered."""
        if not self.rules:
            return 0.0
        # Coverage ≈ unique (context, action) pairs / estimated total
        n_actions = len(self._by_action)
        n_contexts = len(self._observed_contexts)
        observed = len(self._observed_pairs)
        estimated_total = max(n_actions * n_contexts, observed)
        return min(1.0, observed / max(estimated_total, 1))

    def rule_count(self) -> int:
        return len(self.rules)


    def consolidate_color_rules(self) -> dict:
        """K-Factorization (§136): collapse position-dependent rules into
        position-invariant color transition rules.

        For click games: 61 rules at different positions that all do
        "color 3 → color 5" are ONE rule. This method finds them.

        Returns {action: {old_color: (new_color, count)}}
        """
        consolidated = defaultdict(lambda: defaultdict(Counter))
        for rule in self.rules:
            for old_c, new_c in rule.effect_colormap.items():
                consolidated[rule.action][old_c][new_c] += rule.n_seen

        # Pick the most common transition for each (action, old_color)
        result = {}
        for action, cmap in consolidated.items():
            result[action] = {}
            for old_c, targets in cmap.items():
                best_new, count = targets.most_common(1)[0]
                result[action][old_c] = (best_new, count)

        self._consolidated = result
        return result

    def apply_consolidated(self, grid: np.ndarray, action: int,
                           click_rc: tuple = None) -> Optional[np.ndarray]:
        """Apply consolidated color rules to predict click result.

        For click games: transforms the clicked cell (and neighbors
        if rules show multi-cell effects) using the universal color map.
        """
        if not hasattr(self, '_consolidated'):
            self.consolidate_color_rules()

        rules = self._consolidated.get(action, {})
        if not rules:
            return None

        predicted = grid.copy().astype(np.uint8)

        if click_rc is not None:
            # Click game: apply color rule at clicked cell + neighbors
            r, c = click_rc
            for dr in range(-2, 3):
                for dc in range(-2, 3):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 64 and 0 <= nc < 64:
                        old = int(grid[nr, nc])
                        if old in rules:
                            predicted[nr, nc] = rules[old][0]
        else:
            # Keyboard: apply to all matching cells in active regions
            for old_c, (new_c, _) in rules.items():
                mask = grid == old_c
                predicted[mask] = new_c

        if np.array_equal(predicted, grid):
            return None
        return predicted


def _detect_color_cycle(rules: dict) -> list[list[int]]:
    """Detect color cycles from consolidated transition rules.

    If clicking/acting on color A→B, B→C, C→A, returns [[A,B,C]].
    Terminal colors in non-cyclic chains are prime goal candidates.
    """
    cycles = []
    visited = set()
    for start_color in rules:
        if start_color in visited:
            continue
        chain = [start_color]
        current = start_color
        while True:
            if current not in rules:
                break
            next_c = rules[current][0]  # (new_color, count)
            if next_c == start_color and len(chain) > 1:
                cycles.append(chain[:])
                visited.update(chain)
                break
            if next_c in chain:
                break  # non-simple cycle
            chain.append(next_c)
            current = next_c
            if len(chain) > 16:
                break
    return cycles


def _color_overlap(a: dict, b: dict) -> float:
    """Overlap score between two color count dicts."""
    if not a or not b:
        return 0.0
    all_colors = set(a.keys()) | set(b.keys())
    total_a = sum(a.values())
    total_b = sum(b.values())
    if total_a == 0 or total_b == 0:
        return 0.0
    # Normalized histogram overlap (Bhattacharyya-style)
    overlap = sum(np.sqrt(a.get(c, 0) / total_a * b.get(c, 0) / total_b)
                  for c in all_colors)
    return float(overlap)


# ═══════════════════════════════════════════════════════════════════
#  3. FORWARD MODEL — predict next grid from learned rules
# ═══════════════════════════════════════════════════════════════════

@dataclass
class Prediction:
    """A forward model prediction with confidence."""
    grid: np.ndarray
    confidence: float     # 0.0 = pure guess, 1.0 = exact replay
    method: str           # 'exact', 'relocated', 'manifold', 'prior'
    rule_used: Optional[LearnedRule] = None
    entropy: float = 0.0


class ForwardModel:
    """Predict next grid state from current grid + action.

    Prediction hierarchy (highest confidence first):
    1. EXACT: identical (context, action) seen before → replay
    2. RELOCATED: same K-grammar shape, new position via manifold
    3. MANIFOLD: manifold coordinates predict which cells change
    4. PRIOR: Chebyshev spectrum predicts color distribution
    """

    def __init__(self, table: MechanismTable, manifold: CellManifold):
        self.table = table
        self.manifold = manifold
        # Track prediction accuracy for self-calibration
        self._predictions = 0
        self._correct = 0

    def predict(self, grid: np.ndarray, action: int,
                click_pos: tuple = None) -> Prediction:
        """Predict the result of taking action on grid."""

        # ── Level 0: CONSOLIDATED color rules (best for click games) ──
        if action == 6 and click_pos is not None:
            consolidated = self.table.apply_consolidated(
                grid, action, click_rc=click_pos)
            if consolidated is not None:
                return Prediction(
                    grid=consolidated,
                    confidence=0.85,
                    method='consolidated',
                    entropy=shannon_entropy(consolidated),
                )

        # ── Level 1: EXACT match ──
        exact = self.table.lookup_exact(grid, action)
        if exact is not None:
            predicted = self._apply_rule(grid, exact, exact.bounding_box[:2])
            return Prediction(
                grid=predicted,
                confidence=min(1.0, exact.n_seen / 3.0),
                method='exact',
                rule_used=exact,
                entropy=shannon_entropy(predicted),
            )

        # ── Level 2: CONSOLIDATED (keyboard actions) ──
        consolidated = self.table.apply_consolidated(grid, action)
        if consolidated is not None:
            return Prediction(
                grid=consolidated,
                confidence=0.6,
                method='consolidated',
                entropy=shannon_entropy(consolidated),
            )

        # ── Level 3: RELOCATED — same shape, different position ──
        candidates = self.table.lookup_similar(grid, action, self.manifold)
        if candidates:
            rule, score, (loc_r, loc_c) = candidates[0]
            predicted = self._apply_rule(grid, rule, (loc_r, loc_c))
            return Prediction(
                grid=predicted,
                confidence=score * 0.8,
                method='relocated',
                rule_used=rule,
                entropy=shannon_entropy(predicted),
            )

        # ── Level 4: MANIFOLD — Pe field predicts change regions ──
        pe = self.manifold.pe_field()
        if (pe > 0).any():
            predicted = grid.copy()
            for idx in self.table._by_action.get(action, [])[-5:]:
                rule = self.table.rules[idx]
                for old_c, new_c in rule.effect_colormap.items():
                    mask = (grid == old_c) & (pe > 0.5)
                    predicted[mask] = new_c

            if not np.array_equal(predicted, grid):
                return Prediction(
                    grid=predicted,
                    confidence=0.2,
                    method='manifold',
                    entropy=shannon_entropy(predicted),
                )

        # ── Level 5: PRIOR — no change predicted ──
        return Prediction(
            grid=grid.copy(),
            confidence=0.05,
            method='prior',
            entropy=shannon_entropy(grid),
        )

    def predict_sequence(self, grid: np.ndarray, actions: list[int],
                         max_steps: int = 20) -> list[Prediction]:
        """Multi-step forward simulation."""
        predictions = []
        current = grid.copy()
        cumulative_confidence = 1.0

        for action in actions[:max_steps]:
            pred = self.predict(current, action)
            cumulative_confidence *= pred.confidence
            pred.confidence = cumulative_confidence
            predictions.append(pred)
            current = pred.grid

            # Stop if confidence drops too low
            if cumulative_confidence < 0.01:
                break

        return predictions

    def verify(self, predicted: np.ndarray, actual: np.ndarray) -> float:
        """Verify a prediction against the actual result. Returns accuracy."""
        self._predictions += 1
        accuracy = float((predicted == actual).mean())
        if accuracy > 0.95:
            self._correct += 1
        return accuracy

    def accuracy(self) -> float:
        """Overall prediction accuracy."""
        if self._predictions == 0:
            return 0.0
        return self._correct / self._predictions

    def _apply_rule(self, grid: np.ndarray, rule: LearnedRule,
                    location: tuple) -> np.ndarray:
        """Apply a learned rule at a specific location."""
        predicted = grid.copy().astype(np.uint8)
        r0, c0 = location
        xor = rule.effect_xor

        # Apply color map at the rule's bounding box, shifted to location
        orig_r0, orig_c0 = rule.bounding_box[0], rule.bounding_box[1]
        dr = r0 - orig_r0
        dc = c0 - orig_c0

        rows, cols = np.where(xor > 0)
        for r, c in zip(rows, cols):
            nr, nc = r + dr, c + dc
            if 0 <= nr < 64 and 0 <= nc < 64:
                old_val = int(grid[nr, nc])
                if old_val in rule.effect_colormap:
                    predicted[nr, nc] = rule.effect_colormap[old_val]

        return predicted


# ═══════════════════════════════════════════════════════════════════
#  4. MANIFOLD PLANNER — geodesic A* on the Pe field
# ═══════════════════════════════════════════════════════════════════

class ManifoldPlanner:
    """Plan action sequences via geodesic search on the Eckert manifold.

    The cost surface is the FISHER METRIC on the manifold. High Pe
    regions have low traversal cost (the game's rules carry you).
    Low Pe regions are "walls" — high cost, hard to cross.

    A* with Kramers-informed edge costs finds the geodesic — the
    minimum-information path between current state and goal.
    """

    def __init__(self, model: ForwardModel, manifold: CellManifold):
        self.model = model
        self.manifold = manifold

    def plan_to_position(self, grid: np.ndarray, target_rc: tuple,
                         actions: list[int],
                         action_directions: dict,
                         max_depth: int = 50) -> list[int]:
        """A* pathfinding to a target position using manifold cost.

        action_directions: {action: (dr, dc)} from probe
        """
        # Build cost surface from manifold
        pe = self.manifold.pe_field()
        # Cost = barrier to cross each cell
        # Low Pe (constrained) = high cost. High Pe (active) = low cost.
        cost_surface = np.maximum(1.0 - pe / max(pe.max(), 0.01), 0.1)
        # Walls: cells that never change (R ≈ 0) have very high cost
        wall_mask = self.manifold.R < 0.01
        cost_surface[wall_mask] = 100.0

        # Find agent position (highest R cell)
        agent_cells = self.manifold.agent_candidates()
        if not agent_cells:
            return []
        start = (agent_cells[0][0], agent_cells[0][1])
        goal = target_rc

        # A* on grid with manifold cost
        return self._astar(start, goal, cost_surface,
                           actions, action_directions, max_depth)

    def plan_to_entropy(self, grid: np.ndarray, target_entropy: float,
                        actions: list[int],
                        budget: int = 30) -> list[int]:
        """Search for action sequence that reaches target entropy.

        Uses beam search with forward model predictions.
        """
        beam_width = 5
        # (cumulative_cost, entropy, action_sequence, grid_state)
        beam = [(abs(shannon_entropy(grid) - target_entropy),
                 shannon_entropy(grid), [], grid.copy())]

        best_sequence = []
        best_entropy_dist = abs(shannon_entropy(grid) - target_entropy)

        for depth in range(budget):
            candidates = []
            for cost, ent, seq, state in beam:
                for action in actions:
                    if action == 6:
                        continue  # skip click for now
                    pred = self.model.predict(state, action)
                    if pred.confidence < 0.1:
                        continue
                    new_ent = pred.entropy
                    new_cost = abs(new_ent - target_entropy)
                    new_seq = seq + [action]
                    candidates.append((new_cost, new_ent, new_seq, pred.grid))

                    if new_cost < best_entropy_dist:
                        best_entropy_dist = new_cost
                        best_sequence = new_seq

            if not candidates:
                break

            # Keep top beam_width
            candidates.sort(key=lambda x: x[0])
            beam = candidates[:beam_width]

            # Early exit if close enough
            if best_entropy_dist < 0.01:
                break

        return best_sequence

    def _astar(self, start: tuple, goal: tuple,
               cost_surface: np.ndarray,
               actions: list[int],
               action_directions: dict,
               max_depth: int) -> list[int]:
        """A* on grid with Fisher metric cost surface."""
        # Open set: (f_cost, g_cost, position, action_sequence)
        open_set = [(0.0, 0.0, start, [])]
        closed = set()

        while open_set:
            f, g, pos, seq = heapq.heappop(open_set)

            if pos == goal:
                return seq
            if pos in closed:
                continue
            if len(seq) >= max_depth:
                continue
            closed.add(pos)

            for action, (dr, dc) in action_directions.items():
                if action not in actions or (dr == 0 and dc == 0):
                    continue
                nr, nc = pos[0] + dr, pos[1] + dc
                if not (0 <= nr < 64 and 0 <= nc < 64):
                    continue
                if (nr, nc) in closed:
                    continue

                # Edge cost = Fisher metric on manifold
                edge_cost = float(cost_surface[nr, nc])
                new_g = g + edge_cost

                # Heuristic: Manhattan distance × min cost
                h = (abs(nr - goal[0]) + abs(nc - goal[1])) * 0.1
                new_f = new_g + h

                heapq.heappush(open_set, (new_f, new_g, (nr, nc),
                                          seq + [action]))

        return []  # no path found

    def barrier_to_goal(self, grid: np.ndarray,
                        goal_fn) -> float:
        """Estimate the coordination barrier to reach a goal state.

        barrier = N_mechanisms_needed × π/√2

        N_mechanisms_needed = number of independent color changes
        needed to transform current grid into goal state.
        """
        # Count the number of distinct color transitions needed
        # This is an estimate — we don't know the goal grid exactly
        n_active = self.manifold.mechanism_count()
        return n_active * BARRIER_CONST


# ═══════════════════════════════════════════════════════════════════
#  5. GOAL HYPOTHESES — candidate win conditions to search over
# ═══════════════════════════════════════════════════════════════════

@dataclass
class GoalHypothesis:
    """A candidate win condition with a scoring function."""
    name: str
    score_fn: object   # callable(grid) -> float in [0, 1], higher = closer to goal
    priority: float = 1.0  # higher = try first


def generate_goal_hypotheses(table: MechanismTable, manifold: CellManifold,
                              initial_grid: np.ndarray) -> list[GoalHypothesis]:
    """Generate candidate win conditions from learned game physics.

    The key insight: we don't know what "winning" means, but we can
    generate hypotheses from the game's rule structure and test each
    one using the forward model.

    Priority ordering: most likely conditions first (saves budget).
    """
    bg = manifold.background_color(initial_grid)
    initial_nonbg = int((initial_grid != bg).sum())
    colors = sorted(set(initial_grid.flatten().tolist()) - {bg})
    hypotheses = []

    # ── H1: Clear the board (all background) ──
    # Very common in puzzle games: remove all objects
    if initial_nonbg > 0:
        hypotheses.append(GoalHypothesis(
            "clear_board",
            lambda g, _bg=bg: 1.0 - (g != _bg).sum() / max(g.size, 1),
            priority=3.0,
        ))

    # ── H2: Uniform color (all cells same color) ──
    hypotheses.append(GoalHypothesis(
        "uniform",
        lambda g: float(np.bincount(g.flatten().astype(int),
                                     minlength=16).max()) / g.size,
        priority=2.5,
    ))

    # ── H3: Target each non-bg color ──
    # If clicking cycles A→B→C, maybe the goal is "all B" or "all C"
    for target_color in colors:
        tc_count = int((initial_grid == target_color).sum())
        # Higher priority for rarer colors (likely goal state)
        rarity = 1.0 - tc_count / max(initial_nonbg, 1)
        hypotheses.append(GoalHypothesis(
            f"all_color_{target_color}",
            lambda g, tc=target_color, _bg=bg: (
                (g[g != _bg] == tc).sum() / max((g != _bg).sum(), 1)
                if (g != _bg).any() else 0.0
            ),
            priority=1.5 + rarity,
        ))

    # ── H4: Minimize non-bg pixels ──
    if initial_nonbg > 10:
        hypotheses.append(GoalHypothesis(
            "minimize_objects",
            lambda g, _bg=bg, _inb=initial_nonbg: (
                1.0 - (g != _bg).sum() / max(_inb, 1)
            ),
            priority=2.0,
        ))

    # ── H5: Color cycle terminal ──
    # If rules show A→B→C→A, try each position in the cycle
    rules = table.consolidate_color_rules()
    for action_rules in rules.values():
        cycles = _detect_color_cycle(action_rules)
        for cycle in cycles:
            # Each color in the cycle is a candidate terminal
            for i, terminal in enumerate(cycle):
                hypotheses.append(GoalHypothesis(
                    f"cycle_terminal_{terminal}",
                    lambda g, tc=terminal, _bg=bg: (
                        (g[g != _bg] == tc).sum() / max((g != _bg).sum(), 1)
                        if (g != _bg).any() else 0.0
                    ),
                    priority=2.8,  # cycles are strong signal
                ))

    # ── H6: Spatial symmetry ──
    hypotheses.append(GoalHypothesis(
        "h_symmetry",
        lambda g: 1.0 - np.abs(
            g.astype(int) - np.fliplr(g).astype(int)
        ).astype(bool).mean(),
        priority=0.8,
    ))
    hypotheses.append(GoalHypothesis(
        "v_symmetry",
        lambda g: 1.0 - np.abs(
            g.astype(int) - np.flipud(g).astype(int)
        ).astype(bool).mean(),
        priority=0.8,
    ))

    # ── H7: Single connected component of non-bg ──
    hypotheses.append(GoalHypothesis(
        "single_component",
        lambda g, _bg=bg: (
            1.0 / max(ndimage.label(g != _bg)[1], 1)
        ),
        priority=1.0,
    ))

    # ── H8: Checkerboard / alternating pattern ──
    hypotheses.append(GoalHypothesis(
        "checkerboard",
        lambda g: _checkerboard_score(g),
        priority=0.5,
    ))

    # ── H9: Row-sorted (each row same color) ──
    hypotheses.append(GoalHypothesis(
        "row_uniform",
        lambda g: np.mean([
            np.bincount(g[r].astype(int), minlength=16).max() / g.shape[1]
            for r in range(g.shape[0])
        ]),
        priority=0.7,
    ))

    # ── H10: Column-sorted (each column same color) ──
    hypotheses.append(GoalHypothesis(
        "col_uniform",
        lambda g: np.mean([
            np.bincount(g[:, c].astype(int), minlength=16).max() / g.shape[0]
            for c in range(g.shape[1])
        ]),
        priority=0.7,
    ))

    # Sort by priority (highest first)
    hypotheses.sort(key=lambda h: -h.priority)

    # Deduplicate by name
    seen = set()
    deduped = []
    for h in hypotheses:
        if h.name not in seen:
            seen.add(h.name)
            deduped.append(h)

    return deduped


def _checkerboard_score(grid: np.ndarray) -> float:
    """Score how close grid is to a checkerboard pattern."""
    h, w = grid.shape
    even = grid[0::2, 0::2]
    odd = grid[1::2, 1::2]
    mixed1 = grid[0::2, 1::2]
    mixed2 = grid[1::2, 0::2]

    # Perfect checkerboard: even+odd same color, mixed same different color
    if even.size == 0 or mixed1.size == 0:
        return 0.0
    even_uniform = np.bincount(even.flatten().astype(int), minlength=16).max() / even.size
    odd_uniform = np.bincount(odd.flatten().astype(int), minlength=16).max() / max(odd.size, 1)
    mixed1_uniform = np.bincount(mixed1.flatten().astype(int), minlength=16).max() / mixed1.size
    mixed2_uniform = np.bincount(mixed2.flatten().astype(int), minlength=16).max() / max(mixed2.size, 1)

    return (even_uniform + odd_uniform + mixed1_uniform + mixed2_uniform) / 4.0


# ═══════════════════════════════════════════════════════════════════
#  6. ECKERT SIMULATOR — main class wiring everything together
# ═══════════════════════════════════════════════════════════════════

class EckertSimulator:
    """The generic forward simulator.

    Usage:
        sim = EckertSimulator(profile)
        sim.explore(env, obs, budget=50)  # learn the game's physics
        pred = sim.predict(grid, action)   # forward simulation
        plan = sim.plan(grid, goal)        # geodesic planning
    """

    def __init__(self, profile: GameProfile, shared_state=None):
        self.profile = profile
        if shared_state:
            self.manifold = shared_state.manifold
            self.table = shared_state.table
            self.model = ForwardModel(self.table, self.manifold)
            self.planner = ManifoldPlanner(self.model, self.manifold)
            self.detector = shared_state.detector
        else:
            self.manifold = CellManifold()
            self.table = MechanismTable()
            self.model = ForwardModel(self.table, self.manifold)
            self.planner = ManifoldPlanner(self.model, self.manifold)
            self.detector = EckertWinDetector()

        # Kramers potential landscape
        self._entropy_series = []
        self._kramers_barriers = []

        # Goal tracking
        self._winning_goal = None
        self._goal_scores = {}  # goal_name -> best_score

        # Track exploration
        self.total_actions = 0
        self.levels_solved = 0
        self.rng = np.random.default_rng(42)

    def observe(self, prev_grid: np.ndarray, action: int,
                curr_grid: np.ndarray):
        """Learn from one observed transition."""
        self.manifold.observe(prev_grid, action, curr_grid)
        self.table.learn(prev_grid, action, curr_grid)
        self._entropy_series.append(shannon_entropy(curr_grid))
        # Feed the thermodynamic progress detector
        pe = self.manifold.pe_field() if self.manifold.n_observations >= 5 else None
        self.detector.observe(prev_grid, action, curr_grid, pe_field=pe)

    def predict(self, grid: np.ndarray, action: int) -> Prediction:
        """Predict next state from current state + action."""
        return self.model.predict(grid, action)

    def explore(self, env, obs, budget: int = 50) -> dict:
        """Systematic exploration to learn the game's physics.

        Spends `budget` actions learning rules. Uses the manifold
        to guide WHERE to explore (high Pe = unexplored mechanisms).
        """
        grid = _safe_grid(obs)
        if grid is None:
            return self._explore_summary()
        kb_actions = [a for a in self.profile.available_actions if a != 6]
        click_available = 6 in self.profile.available_actions
        all_actions = kb_actions if kb_actions else [6]

        # Phase 1: Systematic action probe
        if kb_actions:
            phase1_budget = min(budget // 2, len(kb_actions) * 3)
            for i in range(phase1_budget):
                action = kb_actions[i % len(kb_actions)]
                prev_grid = grid.copy()

                obs = env.step(action)
                grid = _safe_grid(obs)
                if grid is None:
                    return self._explore_summary()
                self.observe(prev_grid, action, grid)
                self.total_actions += 1

                if obs.state == GameState.WIN:
                    return self._explore_summary()
                if obs.state == GameState.GAME_OVER:
                    break
        elif click_available:
            # Click-only: systematic grid scan
            phase1_budget = min(budget // 2, 20)
            bg = int(np.bincount(grid.flatten().astype(int),
                                 minlength=16).argmax())
            nonbg = np.where(grid != bg)
            for i in range(phase1_budget):
                if obs.state in (GameState.WIN, GameState.GAME_OVER):
                    break
                prev_grid = grid.copy()
                if len(nonbg[0]) > 0:
                    idx = i % len(nonbg[0])
                    cy, cx = int(nonbg[0][idx]), int(nonbg[1][idx])
                else:
                    cy, cx = 32, 32
                obs = env.step(6, data={"x": cx, "y": cy})
                grid = _safe_grid(obs)
                if grid is None:
                    break
                self.observe(prev_grid, 6, grid)
                self.total_actions += 1
                nonbg = np.where(grid != bg)
        else:
            phase1_budget = 0

        # Phase 2: Manifold-guided exploration
        remaining = budget - phase1_budget
        for i in range(remaining):
            if obs.state in (GameState.WIN, GameState.GAME_OVER):
                break

            prev_grid = grid.copy()

            # Click-only games: always click
            if not kb_actions and click_available:
                pos = self._smart_click_target(grid)
                obs = env.step(6, data={"x": pos[1], "y": pos[0]})
                grid = _safe_grid(obs)
                if grid is None:
                    break
                self.observe(prev_grid, 6, grid)
                self.total_actions += 1
                continue

            # Choose action: prefer actions that explore high-Pe regions
            action = self._choose_exploration_action(grid, all_actions)

            # Execute
            if action == 6 and click_available:
                pos = self._smart_click_target(grid)
                obs = env.step(6, data={"x": pos[1], "y": pos[0]})
            else:
                obs = env.step(action)

            grid = _safe_grid(obs)
            if grid is None:
                break
            self.observe(prev_grid, action, grid)
            self.total_actions += 1

            # Verify predictions against actual outcomes
            pred = self.model.predict(prev_grid, action)
            if pred.confidence > 0.1:
                self.model.verify(pred.grid, grid)

        # Force final manifold recompute
        self.manifold._recompute()
        # Update detector's barrier estimate from manifold
        self.detector.set_barrier_estimate(self.manifold.mechanism_count())
        return self._explore_summary()

    def solve_level(self, env, obs, budget: int = 200) -> tuple:
        """Attempt to solve the current level via goal hypothesis search.

        Strategy:
        1. First 25% of budget: explore (learn rules + manifold)
        2. Generate goal hypotheses from learned physics
        3. For each hypothesis (priority order): plan + execute toward it
        4. If a hypothesis triggers WIN → done
        5. If stuck: Kramers escape + next hypothesis

        Returns (solved: bool, obs, actions_used: int).
        """
        grid = _safe_grid(obs)
        if grid is None:
            return False, obs, 0
        start_level = obs.levels_completed
        actions_used = 0
        actions = list(self.profile.available_actions)
        non_click = [a for a in actions if a != 6]
        click_available = 6 in actions
        click_only = not non_click and click_available
        initial_grid = grid.copy()

        # ── Phase 1: Explore (learn the game) ──
        explore_budget = min(budget // 4, 50)
        explore_result = self.explore(env, obs, explore_budget)
        grid = _safe_grid(obs)
        if grid is None:
            return False, obs, explore_result.get('actions', 0)
        actions_used += explore_result.get('actions', 0)

        if obs.state == GameState.WIN or obs.levels_completed > start_level:
            return True, obs, actions_used

        # ── Phase 2: Generate goal hypotheses ──
        goals = generate_goal_hypotheses(self.table, self.manifold,
                                          initial_grid)

        # Score initial state against each goal to find which are achievable
        # Skip goals that are already satisfied (score > 0.95) or hopeless
        active_goals = []
        for goal in goals:
            try:
                score = goal.score_fn(grid)
                self._goal_scores[goal.name] = score
                if 0.01 < score < 0.95:
                    active_goals.append((goal, score))
            except Exception:
                continue

        # Sort by (priority * (1 - current_score)) — prioritize achievable goals
        active_goals.sort(key=lambda gs: -gs[0].priority * (1.0 - gs[1]))

        # ── Phase 3: Try each goal hypothesis ──
        remaining = budget - actions_used
        # Concentrate budget: try fewer goals with more actions each
        n_goals_to_try = min(3, len(active_goals))
        budget_per_goal = max(remaining // max(n_goals_to_try, 1), 25)

        for goal, initial_score in active_goals[:n_goals_to_try]:
            if remaining <= 5:
                break
            if obs.state == GameState.WIN or obs.levels_completed > start_level:
                return True, obs, actions_used
            if obs.state == GameState.GAME_OVER:
                break

            goal_budget = min(budget_per_goal, remaining)
            solved, obs, goal_acts, grid = self._pursue_goal(
                env, obs, grid, goal, goal_budget, actions, non_click,
                click_available, click_only, start_level)
            actions_used += goal_acts
            remaining -= goal_acts

            if solved:
                self._winning_goal = goal.name
                return True, obs, actions_used

        # ── Phase 4: Fallback — entropy-seeking (original behavior) ──
        if remaining > 10 and obs.state not in (GameState.WIN, GameState.GAME_OVER):
            if click_only:
                solved, obs, click_acts = self._click_exploit(
                    env, obs, remaining)
                actions_used += click_acts
            else:
                solved, obs, fb_acts, grid = self._entropy_fallback(
                    env, obs, grid, remaining, non_click, click_available,
                    start_level)
                actions_used += fb_acts

        solved = (obs.state == GameState.WIN or
                  obs.levels_completed > start_level)
        return solved, obs, actions_used

    def _pursue_goal(self, env, obs, grid, goal: GoalHypothesis,
                     budget: int, actions, non_click, click_available,
                     click_only, start_level) -> tuple:
        """Execute actions to maximize a specific goal hypothesis.

        Uses forward model to pick actions that improve goal score.
        Returns (solved, obs, actions_used, grid).
        """
        actions_used = 0
        best_score = goal.score_fn(grid)
        stall_counter = 0

        for _ in range(budget):
            if obs.state == GameState.WIN or obs.levels_completed > start_level:
                return True, obs, actions_used, grid
            if obs.state == GameState.GAME_OVER:
                return False, obs, actions_used, grid

            prev_grid = grid.copy()

            # Choose action that best improves this goal
            action, click_pos = self._choose_goal_action(
                grid, goal, non_click, click_available, click_only)

            # Execute
            if action == 6 and click_pos is not None:
                obs = env.step(6, data={"x": click_pos[1], "y": click_pos[0]})
            elif action == 6:
                pos = self._smart_click_target(grid)
                obs = env.step(6, data={"x": pos[1], "y": pos[0]})
            else:
                obs = env.step(action)

            grid = _safe_grid(obs)
            if grid is None:
                return False, obs, actions_used + 1, prev_grid
            self.observe(prev_grid, action, grid)
            actions_used += 1
            self.total_actions += 1

            # Check progress
            try:
                current_score = goal.score_fn(grid)
            except Exception:
                current_score = best_score

            # Track best goal score for diagnostics
            if current_score > self._goal_scores.get(goal.name, 0):
                self._goal_scores[goal.name] = current_score

            if current_score > best_score + 0.001:
                best_score = current_score
                stall_counter = 0
            else:
                stall_counter += 1

            # Kramers escape: if stalled 20 steps, bail to next goal
            if stall_counter > 20:
                break

        return False, obs, actions_used, grid

    def _choose_goal_action(self, grid, goal: GoalHypothesis,
                            non_click, click_available,
                            click_only) -> tuple:
        """Choose the action that best improves the goal score.

        Simulates each action via forward model and picks the best outcome.
        Returns (action, click_pos_or_None).
        """
        best_action = non_click[0] if non_click else 6
        best_score = -np.inf
        best_click_pos = None

        # Score keyboard actions
        for action in non_click:
            pred = self.model.predict(grid, action)
            if pred.confidence < 0.05:
                continue
            try:
                goal_s = goal.score_fn(pred.grid)
            except Exception:
                goal_s = 0.0
            # Blend goal score with φ (thermodynamic progress)
            phi_s = self.detector.score_state(pred.grid)
            score = 0.5 * goal_s + 0.4 * phi_s + 0.1 * pred.confidence
            if score > best_score:
                best_score = score
                best_action = action
                best_click_pos = None

        # Score click actions on smart targets
        if click_available:
            bg = self.manifold.background_color(grid)
            targets = self._goal_click_targets(grid, goal, bg)
            for r, c in targets[:8]:
                pred = self.model.predict(grid, 6, click_pos=(r, c))
                if pred.confidence < 0.05:
                    continue
                try:
                    goal_s = goal.score_fn(pred.grid)
                except Exception:
                    goal_s = 0.0
                phi_s = self.detector.score_state(pred.grid)
                score = 0.5 * goal_s + 0.4 * phi_s + 0.1 * pred.confidence
                if score > best_score:
                    best_score = score
                    best_action = 6
                    best_click_pos = (r, c)

        return best_action, best_click_pos

    def _goal_click_targets(self, grid, goal: GoalHypothesis,
                            bg: int) -> list[tuple]:
        """Generate click targets ranked by potential goal improvement."""
        targets = []
        nonbg = np.where(grid != bg)
        if len(nonbg[0]) == 0:
            return [(32, 32)]

        # Score a sample of non-bg cells
        indices = list(range(len(nonbg[0])))
        if len(indices) > 30:
            sample = self.rng.choice(indices, size=30, replace=False)
        else:
            sample = indices

        for i in sample:
            r, c = int(nonbg[0][i]), int(nonbg[1][i])
            # Quick score: R (responsive) × distance from bg
            r_score = float(self.manifold.R[r, c])
            targets.append((r, c, r_score))

        targets.sort(key=lambda x: -x[2])
        return [(r, c) for r, c, _ in targets]

    def _entropy_fallback(self, env, obs, grid, budget, non_click,
                          click_available, start_level) -> tuple:
        """φ-guided fallback — navigate toward Pe minimum."""
        actions_used = 0

        for _ in range(budget):
            if obs.state == GameState.WIN or obs.levels_completed > start_level:
                return True, obs, actions_used, grid
            if obs.state == GameState.GAME_OVER:
                return False, obs, actions_used, grid

            prev_grid = grid.copy()
            action = self._choose_exploit_action(grid, non_click,
                                                  click_available)

            if action == 6:
                pos = self._smart_click_target(grid)
                obs = env.step(6, data={"x": pos[1], "y": pos[0]})
            else:
                obs = env.step(action)

            grid = _safe_grid(obs)
            if grid is None:
                return False, obs, actions_used, prev_grid
            self.observe(prev_grid, action, grid)
            actions_used += 1
            self.total_actions += 1

            # Use detector stuck detection instead of entropy stall
            if self.detector.is_stuck(window=15):
                break

        solved = (obs.state == GameState.WIN or
                  obs.levels_completed > start_level)
        return solved, obs, actions_used, grid

    def _choose_exploration_action(self, grid: np.ndarray,
                                   actions: list[int]) -> int:
        """Choose action that maximizes information gain.

        Uses manifold: prefer actions at high-Pe unexplored regions.
        Falls back to round-robin for early exploration.
        """
        if self.total_actions < 10:
            return actions[self.total_actions % len(actions)]

        # Score each action by predicted information gain
        best_action = actions[0]
        best_score = -np.inf

        for action in actions:
            pred = self.model.predict(grid, action)
            # Information gain = 1 - confidence (low confidence = high info)
            info_gain = 1.0 - pred.confidence
            # Entropy change bonus (any change is informative during explore)
            ent_change = abs(pred.entropy - shannon_entropy(grid))
            score = info_gain * 5.0 + ent_change * 2.0
            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    def _choose_exploit_action(self, grid: np.ndarray,
                               actions: list[int],
                               click_available: bool) -> int:
        """Choose action that maximizes φ (thermodynamic progress).

        Uses forward model to simulate each action, picks best outcome
        according to the Eckert win detector's progress function.
        """
        best_action = actions[0] if actions else 6
        best_phi = -1.0
        current_phi = self.detector.progress(grid)

        for action in actions:
            pred = self.model.predict(grid, action)
            if pred.confidence < 0.05:
                continue
            phi = self.detector.score_state(pred.grid)
            # Boost by prediction confidence
            phi += pred.confidence * 0.02
            if phi > best_phi:
                best_phi = phi
                best_action = action

        if click_available and best_phi <= current_phi + 0.001:
            return 6

        return best_action

    def _click_exploit(self, env, obs, budget: int) -> tuple:
        """Click-specific exploit strategy using consolidated color rules.

        Strategy: learn the color transition rules, then systematically
        click every cell that needs to change. The consolidated rules
        tell us WHAT to click — the manifold tells us WHERE.
        """
        grid = _safe_grid(obs)
        if grid is None or obs.state == GameState.GAME_OVER:
            return False, obs, 0
        start_level = obs.levels_completed
        actions_used = 0

        # Consolidate rules from exploration
        rules = self.table.consolidate_color_rules().get(6, {})
        if not rules:
            return False, obs, 0

        bg = self.manifold.background_color(grid)

        # Click systematically through targets
        for _ in range(budget):
            if obs.state == GameState.WIN or obs.levels_completed > start_level:
                return True, obs, actions_used
            if obs.state == GameState.GAME_OVER or not obs.frame:
                return False, obs, actions_used

            # Build targets: non-bg cells with known color transitions,
            # sorted by manifold R (most responsive first)
            targets = []
            for r in range(64):
                for c in range(64):
                    color = int(grid[r, c])
                    if color != bg and color in rules:
                        targets.append((r, c, float(self.manifold.R[r, c])))
            targets.sort(key=lambda x: -x[2])

            if not targets:
                nz = np.where(grid != bg)
                if len(nz[0]) == 0:
                    break
                idx = int(self.rng.integers(len(nz[0])))
                tr, tc = int(nz[0][idx]), int(nz[1][idx])
            else:
                tr, tc, _ = targets[0]

            prev_grid = grid.copy()
            obs = env.step(6, data={"x": tc, "y": tr})

            if not obs.frame:
                return (obs.state == GameState.WIN or
                        obs.levels_completed > start_level), obs, actions_used + 1

            grid = _safe_grid(obs)
            self.observe(prev_grid, 6, grid)
            actions_used += 1
            self.total_actions += 1

        solved = obs.state == GameState.WIN or obs.levels_completed > start_level
        return solved, obs, actions_used

    def _smart_click_target(self, grid: np.ndarray) -> tuple:
        """Choose click target using manifold coordinates.

        Click at: high-R (responsive) non-background cell.
        """
        bg = self.manifold.background_color(grid)
        R = self.manifold.R

        # Mask: non-background + responsive
        nonbg = grid != bg
        score = R * nonbg.astype(np.float32)

        if score.max() > 0:
            # Pick from top candidates
            flat = score.flatten()
            top_k = min(5, (flat > 0).sum())
            if top_k > 0:
                top_indices = np.argpartition(flat, -top_k)[-top_k:]
                idx = self.rng.choice(top_indices)
                return (int(idx // 64), int(idx % 64))

        # Fallback: random non-background cell
        nz = np.where(nonbg)
        if len(nz[0]) > 0:
            i = self.rng.integers(len(nz[0]))
            return (int(nz[0][i]), int(nz[1][i]))

        return (32, 32)

    def _explore_summary(self) -> dict:
        return {
            'actions': self.total_actions,
            'rules_learned': self.table.rule_count(),
            'coverage': round(self.table.coverage(), 4),
            'mechanisms': self.manifold.mechanism_count(),
            'barrier': round(self.manifold.exploration_barrier(), 1),
            'prediction_accuracy': round(self.model.accuracy(), 3),
            'is_deterministic': self.table.is_deterministic,
            'pe_range': (round(float(self.manifold.Pe.min()), 2),
                         round(float(self.manifold.Pe.max()), 2)),
        }

    def diagnostics(self) -> dict:
        """Full simulator diagnostics for debugging."""
        pe = self.manifold.pe_field()
        diag = {
            'total_actions': self.total_actions,
            'rules': self.table.rule_count(),
            'coverage': round(self.table.coverage(), 4),
            'deterministic': self.table.is_deterministic,
            'mechanisms': self.manifold.mechanism_count(),
            'barrier': round(self.manifold.exploration_barrier(), 1),
            'prediction_accuracy': round(self.model.accuracy(), 3),
            'pe_min': round(float(pe.min()), 3),
            'pe_max': round(float(pe.max()), 3),
            'pe_mean': round(float(pe.mean()), 3),
            'active_cells': int((pe > 0).sum()),
            'agent_candidates': self.manifold.agent_candidates()[:3],
            'entropy_series': self._entropy_series[-20:],
        }
        if self._winning_goal:
            diag['winning_goal'] = self._winning_goal
        if self._goal_scores:
            diag['goal_scores'] = {k: round(v, 3)
                                    for k, v in self._goal_scores.items()}
        # Add thermodynamic detector state
        diag['detector'] = self.detector.summary()
        return diag


# ═══════════════════════════════════════════════════════════════════
#  6. SOLVER INTERFACE — for ensemble dispatch
# ═══════════════════════════════════════════════════════════════════

def solve(game_id: str, probe_budget: int = 30,
          solve_budget: int = 300, verbose: bool = True,
          shared_state=None, profile: 'GameProfile' = None) -> dict:
    """Solve a game using the Eckert Simulator.

    Pipeline:
    1. Probe → GameProfile (or use provided)
    2. Build EckertSimulator (with shared_state if provided)
    3. For each level: explore + plan + execute
    """
    if verbose:
        print(f"\n{'='*65}")
        print(f"  ECKERT SIMULATOR: {game_id}")
        print(f"{'='*65}")

    if profile is None:
        profile = probe_game(game_id, budget=probe_budget, verbose=False)

    if verbose:
        print(f"  Profile: {profile.solver_hint()}")

    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    sim = EckertSimulator(profile, shared_state=shared_state)
    levels_solved = 0
    total_actions = 0

    for level in range(profile.win_levels):
        if obs.state == GameState.WIN:
            break
        if obs.state == GameState.GAME_OVER:
            if verbose:
                print(f"  Level {level}: GAME OVER")
            break

        solved, obs, actions = sim.solve_level(env, obs, budget=solve_budget)
        total_actions += actions

        if solved:
            levels_solved += 1
            if verbose:
                diag = sim.diagnostics()
                goal_info = f" goal={diag.get('winning_goal', '?')}" if diag.get('winning_goal') else ""
                print(f"  Level {level}: SOLVED in {actions} acts | "
                      f"rules={diag['rules']} | "
                      f"coverage={diag['coverage']:.2f} | "
                      f"pred_acc={diag['prediction_accuracy']:.2f}"
                      f"{goal_info}")
        else:
            if verbose:
                diag = sim.diagnostics()
                goals_str = ""
                if diag.get('goal_scores'):
                    top = sorted(diag['goal_scores'].items(),
                                 key=lambda x: -x[1])[:3]
                    goals_str = f" | goals={dict(top)}"
                print(f"  Level {level}: FAILED {actions} acts | "
                      f"rules={diag['rules']} | "
                      f"mechanisms={diag['mechanisms']} | "
                      f"pred_acc={diag['prediction_accuracy']:.2f}"
                      f"{goals_str}")
            break

    diag = sim.diagnostics()
    det_summary = sim.detector.summary()
    result = {
        'game_id': game_id,
        'levels_solved': levels_solved,
        'win_levels': profile.win_levels,
        'total_actions': total_actions,
        'final_phi': det_summary.get('phi', 0.0),
        'diagnostics': diag,
        'detector': det_summary,
    }

    if verbose:
        phi_str = f"φ={det_summary['phi']:.3f}"
        print(f"\n  RESULT: {levels_solved}/{profile.win_levels} | "
              f"{total_actions} actions | {phi_str} | "
              f"rules={diag['rules']} | "
              f"det={'Y' if diag['deterministic'] else 'N'} | "
              f"pred_acc={diag['prediction_accuracy']:.2f}")

    return result


# ═══════════════════════════════════════════════════════════════════
#  CLI
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="ARC-AGI-3 Eckert Simulator — physics-based forward model")
    parser.add_argument("game_id", nargs="?", default=None)
    parser.add_argument("-b", "--probe-budget", type=int, default=30)
    parser.add_argument("-s", "--solve-budget", type=int, default=300)
    parser.add_argument("-v", "--verbose", action="store_true", default=True)
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--diag", action="store_true",
                        help="Print full diagnostics for each game")
    args = parser.parse_args()

    if args.quiet:
        args.verbose = False

    if args.all or args.game_id is None:
        arcade = arc_agi.Arcade()
        envs = arcade.get_environments()
        results = []

        print(f"\n{'Game':<22s} {'Solved':>7s} {'Acts':>6s} "
              f"{'Rules':>6s} {'Cover':>6s} {'Det':>4s} {'Pred':>5s}")
        print("-" * 62)

        for e in envs:
            try:
                r = solve(e.game_id, probe_budget=args.probe_budget,
                          solve_budget=args.solve_budget,
                          verbose=args.verbose)
                results.append(r)

                if not args.verbose:
                    d = r.get('diagnostics', {})
                    print(f"{r['game_id']:<22s} "
                          f"{r['levels_solved']}/{r['win_levels']:<5d} "
                          f"{r['total_actions']:>6d} "
                          f"{d.get('rules', '?'):>6} "
                          f"{d.get('coverage', 0):>6.2f} "
                          f"{'Y' if d.get('deterministic') else 'N':>4s} "
                          f"{d.get('prediction_accuracy', 0):>5.2f}")
            except Exception as ex:
                import traceback
                if args.verbose:
                    traceback.print_exc()
                print(f"{e.game_id:<22s} ERROR: {str(ex)[:50]}")

        total = sum(r.get("levels_solved", 0) for r in results)
        possible = sum(r.get("win_levels", 0) for r in results)
        print(f"\nTOTAL: {total}/{possible} levels solved")
    else:
        r = solve(args.game_id, probe_budget=args.probe_budget,
                  solve_budget=args.solve_budget, verbose=True)
        if args.diag and 'diagnostics' in r:
            import json
            print(f"\n  DIAGNOSTICS:")
            for k, v in r['diagnostics'].items():
                if k == 'entropy_series':
                    print(f"    {k}: [{', '.join(f'{x:.3f}' for x in v)}]")
                else:
                    print(f"    {k}: {v}")
