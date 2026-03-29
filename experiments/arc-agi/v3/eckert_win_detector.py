"""ARC-AGI-3 Eckert Win Detector — universal thermodynamic progress oracle.

The core problem: game solvers learn physics perfectly (pred_acc → 1.0)
but can't infer what "winning" means. This module replaces goal-guessing
with a physics-derived progress function φ(state) → [0,1].

THE THESIS: The win condition is where Pe → minimum in the learned
dynamics. At the win state the game becomes maximally transparent (O→0),
invariant (R→0), and independent (α→0). We don't need to guess
"clear board" vs "symmetry" vs "uniform color" — we follow the gradient.

Seven thermodynamic signals, combined into one scalar:

  1. PE GRADIENT (§136)         — navigate toward Pe minimum on manifold
  2. FREE ENERGY (§48A/§48E)   — F = E - TS, win state minimizes F
  3. SPECTRAL GAP (§51E)       — eigenvalue gap of empirical transition matrix
  4. ABSORPTION (Markov)        — detect sticky/terminal states
  5. CROOKS GATES (§171)       — irreversible transitions = milestones
  6. COMPLEXITY (Kolmogorov)    — zlib ratio descent toward simplicity
  7. CYCLE ESCAPE (§48E/§171C) — break out of detected cycles

Math apparatus applied:
  §136   K-Factorization — shape is K-independent, universal
  §136D2 Barrier universality — barrier = d_eff × π/√2
  §138   Fisher geodesic — distance on the information manifold
  §165   Čencov metric — the unique Riemannian metric on probability space
  §171   Kramers escape — barrier crossing rates and stuck detection
  §48A   Onsager-Machlup — trajectory probability cost
  §2B    Fantasia Bound — I(D;Y)+I(M;Y)≤H(Y), explore/exploit gate

Zero LLM. Pure thermodynamics.
"""
import hashlib
import zlib
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage

from packet_analyzer import shannon_entropy
from packet_probe import frame_hash, xor_grids


# ═══════════════════════════════════════════════════════════════════
#  CONSTANTS
# ═══════════════════════════════════════════════════════════════════

B_ALPHA = 0.867
B_GAMMA = 2.244
BARRIER_CONST = np.pi / np.sqrt(2)  # ≈ 2.221


# ═══════════════════════════════════════════════════════════════════
#  STATE SNAPSHOT — all signals at one point in time
# ═══════════════════════════════════════════════════════════════════

@dataclass
class StateSnapshot:
    """Thermodynamic snapshot of a game state."""
    grid_hash: str
    step: int
    # Raw signals
    pe_mean: float = 0.0         # mean Pe across active cells
    entropy: float = 0.0         # Shannon entropy of grid
    free_energy: float = 0.0     # F = E - TS
    spectral_gap: float = 0.0    # λ₁ of transition matrix
    absorption: float = 0.0      # how "terminal" this state is
    crooks_ratio: float = 1.0    # P(forward)/P(reverse)
    complexity: float = 0.0      # zlib compression ratio
    cycle_depth: int = 0         # 0 = not in cycle, >0 = cycle length
    # Composite
    phi: float = 0.0             # combined progress φ ∈ [0,1]


# ═══════════════════════════════════════════════════════════════════
#  TRANSITION GRAPH — state-action Markov chain
# ═══════════════════════════════════════════════════════════════════

class TransitionGraph:
    """Empirical transition matrix for spectral analysis.

    Builds a sparse state graph from observed transitions.
    Computes: spectral gap, absorption scores, cycle detection,
    Crooks reversibility, and steady-state distribution.
    """

    def __init__(self, max_states: int = 2000):
        self.max_states = max_states
        # State graph: hash -> {action -> [next_hashes]}
        self.edges: dict[str, dict[int, list[str]]] = defaultdict(
            lambda: defaultdict(list))
        # Reverse graph for Crooks
        self.reverse: dict[str, dict[int, list[str]]] = defaultdict(
            lambda: defaultdict(list))
        # Visit counts
        self.visit_count: dict[str, int] = defaultdict(int)
        self.transition_count: dict[tuple, int] = defaultdict(int)
        # State index for matrix operations
        self._state_idx: dict[str, int] = {}
        self._idx_state: dict[int, str] = {}
        self._dirty = True

    def record(self, prev_hash: str, action: int, curr_hash: str):
        """Record one observed transition."""
        self.edges[prev_hash][action].append(curr_hash)
        self.reverse[curr_hash][action].append(prev_hash)
        self.visit_count[prev_hash] += 1
        self.visit_count[curr_hash] += 1
        self.transition_count[(prev_hash, action, curr_hash)] += 1
        # Register states
        for h in (prev_hash, curr_hash):
            if h not in self._state_idx and len(self._state_idx) < self.max_states:
                idx = len(self._state_idx)
                self._state_idx[h] = idx
                self._idx_state[idx] = h
        self._dirty = True

    @property
    def n_states(self) -> int:
        return len(self._state_idx)

    def out_degree(self, state_hash: str) -> int:
        """Number of distinct next states reachable from this state."""
        seen = set()
        for nexts in self.edges.get(state_hash, {}).values():
            seen.update(nexts)
        return len(seen)

    def in_degree(self, state_hash: str) -> int:
        """Number of distinct states that can reach this state."""
        seen = set()
        for prevs in self.reverse.get(state_hash, {}).values():
            seen.update(prevs)
        return len(seen)

    def absorption_score(self, state_hash: str) -> float:
        """How "absorbing" is this state? 1.0 = fully absorbing (no exits).

        Low out-degree relative to max = more terminal.
        High in-degree relative to max = more attractive.
        """
        if self.n_states < 2:
            return 0.0
        out = self.out_degree(state_hash)
        max_out = max(self.out_degree(h) for h in list(self._state_idx.keys())[:100])
        in_d = self.in_degree(state_hash)
        max_in = max(self.in_degree(h) for h in list(self._state_idx.keys())[:100])

        if max_out == 0:
            return 0.0
        # Absorbing = low out + high in
        out_term = 1.0 - (out / max(max_out, 1))
        in_term = in_d / max(max_in, 1)
        return 0.6 * out_term + 0.4 * in_term

    def crooks_ratio(self, prev_hash: str, action: int,
                     curr_hash: str) -> float:
        """Crooks fluctuation theorem: P(A→B)/P(B→A).

        High ratio = irreversible transition (milestone).
        Ratio ≈ 1 = easily reversible.
        """
        fwd = self.transition_count.get((prev_hash, action, curr_hash), 0)
        # Find any reverse transition B→A (any action)
        rev = 0
        for a_rev, prevs in self.edges.get(curr_hash, {}).items():
            rev += prevs.count(prev_hash)
        if rev == 0:
            return 100.0  # effectively irreversible
        return max(fwd, 1) / max(rev, 1)

    def detect_cycles(self, state_hash: str, max_depth: int = 20) -> int:
        """Detect if state is part of a cycle. Returns cycle length or 0."""
        visited = [state_hash]
        current = state_hash
        for _ in range(max_depth):
            # Follow most common next transition
            nexts = self.edges.get(current, {})
            if not nexts:
                return 0
            # Flatten all next states
            all_next = []
            for action_nexts in nexts.values():
                all_next.extend(action_nexts)
            if not all_next:
                return 0
            # Pick most common
            from collections import Counter
            mc = Counter(all_next).most_common(1)[0][0]
            if mc == state_hash:
                return len(visited)
            if mc in visited:
                # Found a cycle, but not back to start
                return 0
            visited.append(mc)
            current = mc
        return 0

    def spectral_gap(self) -> float:
        """Spectral gap Δ = 1 - |λ₂| of the transition matrix.

        Large Δ = fast relaxation → near attractor.
        Small Δ = slow relaxation → stuck in metastable state.
        """
        n = self.n_states
        if n < 3:
            return 0.5  # default: not enough data
        # Build row-stochastic transition matrix
        n_use = min(n, 200)  # cap for performance
        T = np.zeros((n_use, n_use), dtype=np.float64)
        for src_hash, src_idx in list(self._state_idx.items())[:n_use]:
            for action_nexts in self.edges.get(src_hash, {}).values():
                for dst_hash in action_nexts:
                    if dst_hash in self._state_idx:
                        dst_idx = self._state_idx[dst_hash]
                        if dst_idx < n_use:
                            T[src_idx, dst_idx] += 1.0
        # Normalize rows
        row_sums = T.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1.0
        T /= row_sums

        try:
            eigenvalues = np.linalg.eigvals(T)
            # Sort by magnitude (descending)
            mags = np.abs(eigenvalues)
            sorted_idx = np.argsort(-mags)
            if len(sorted_idx) >= 2:
                lambda_2 = mags[sorted_idx[1]]
                return float(1.0 - lambda_2)
            return 0.5
        except np.linalg.LinAlgError:
            return 0.5

    def dominant_eigenvector_projection(self, state_hash: str) -> float:
        """Project a state onto the dominant eigenvector of T.

        High projection = close to the attractor (steady state).
        """
        n = self.n_states
        if n < 3 or state_hash not in self._state_idx:
            return 0.5

        n_use = min(n, 200)
        T = np.zeros((n_use, n_use), dtype=np.float64)
        for src_hash, src_idx in list(self._state_idx.items())[:n_use]:
            for action_nexts in self.edges.get(src_hash, {}).values():
                for dst_hash in action_nexts:
                    if dst_hash in self._state_idx:
                        dst_idx = self._state_idx[dst_hash]
                        if dst_idx < n_use:
                            T[src_idx, dst_idx] += 1.0
        row_sums = T.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1.0
        T /= row_sums

        try:
            eigenvalues, eigenvectors = np.linalg.eig(T.T)
            dom_idx = np.argmax(np.abs(eigenvalues))
            pi = np.abs(eigenvectors[:, dom_idx])
            pi /= max(pi.sum(), 1e-12)
            idx = self._state_idx[state_hash]
            if idx < n_use:
                return float(pi[idx])
            return 0.0
        except np.linalg.LinAlgError:
            return 0.0


# ═══════════════════════════════════════════════════════════════════
#  ECKERT WIN DETECTOR — the universal progress oracle
# ═══════════════════════════════════════════════════════════════════

class EckertWinDetector:
    """Generic win condition detector using Eckert manifold geometry.

    No goal guessing. Derives progress from game dynamics alone.
    Seven signals combined into one scalar φ(state) → [0,1].

    Usage:
        detector = EckertWinDetector()
        # Feed it transitions as they happen:
        detector.observe(prev_grid, action, curr_grid)
        # Get current progress:
        phi = detector.progress(current_grid)
        # Get the best action (steepest φ increase):
        action = detector.best_action(grid, available_actions, predict_fn)
        # Score a predicted state:
        score = detector.score_state(predicted_grid)
    """

    # Signal weights — tuned for ARC-AGI game structure
    WEIGHTS = {
        'pe_gradient':    0.25,   # Pe field minimum pursuit
        'free_energy':    0.20,   # F = E - TS minimization
        'spectral_gap':   0.12,   # eigenvalue gap of transition matrix
        'absorption':     0.13,   # sticky-state detection
        'crooks_gates':   0.10,   # irreversible milestone count
        'complexity':     0.12,   # zlib ratio descent
        'cycle_escape':   0.08,   # breaking out of detected cycles
    }

    def __init__(self):
        # Transition graph for spectral/absorption/Crooks/cycle signals
        self.graph = TransitionGraph()

        # History tracking
        self.snapshots: list[StateSnapshot] = []
        self.pe_history: list[float] = []
        self.entropy_history: list[float] = []
        self.complexity_history: list[float] = []
        self.grids_seen: dict[str, np.ndarray] = {}  # hash -> grid

        # Pe field tracking (from CellManifold if provided)
        self._pe_initial: Optional[float] = None
        self._pe_min: float = float('inf')
        self._pe_max: float = float('-inf')

        # Complexity tracking
        self._complexity_initial: Optional[float] = None
        self._complexity_min: float = float('inf')

        # Entropy tracking
        self._entropy_initial: Optional[float] = None
        self._entropy_min: float = float('inf')

        # Crooks milestones: transitions with ratio > threshold
        self._milestones: list[int] = []  # step indices
        self._milestone_threshold = 5.0

        # Step counter
        self.step = 0

        # Barrier estimate (updated when manifold is provided)
        self._estimated_barriers = 3.0  # default, refined by manifold

    def observe(self, prev_grid: np.ndarray, action: int,
                curr_grid: np.ndarray, pe_field: Optional[np.ndarray] = None):
        """Observe one transition and update all signals.

        Args:
            prev_grid: grid before action
            action: action taken
            curr_grid: grid after action
            pe_field: optional Pe field from CellManifold (64×64 float)
        """
        self.step += 1
        prev_hash = frame_hash(prev_grid)
        curr_hash = frame_hash(curr_grid)

        # Record in transition graph
        self.graph.record(prev_hash, action, curr_hash)

        # Store grids
        self.grids_seen[prev_hash] = prev_grid
        self.grids_seen[curr_hash] = curr_grid

        # ── Pe signal ──
        if pe_field is not None:
            # Use active cells only (Pe > 0 = rule-active)
            active = pe_field[pe_field > 0]
            pe_mean = float(active.mean()) if len(active) > 0 else float(pe_field.mean())
        else:
            # Approximate Pe from grid entropy and change rate
            ent = shannon_entropy(curr_grid)
            changed = (prev_grid != curr_grid).mean()
            pe_mean = ent * (1.0 + changed)  # rough proxy

        self.pe_history.append(pe_mean)
        if self._pe_initial is None:
            self._pe_initial = pe_mean
        self._pe_min = min(self._pe_min, pe_mean)
        self._pe_max = max(self._pe_max, pe_mean)

        # ── Entropy signal ──
        ent = shannon_entropy(curr_grid)
        self.entropy_history.append(ent)
        if self._entropy_initial is None:
            self._entropy_initial = ent
        self._entropy_min = min(self._entropy_min, ent)

        # ── Complexity signal ──
        raw = curr_grid.astype(np.uint8).tobytes()
        compressed = zlib.compress(raw, level=1)
        ratio = len(compressed) / max(len(raw), 1)
        self.complexity_history.append(ratio)
        if self._complexity_initial is None:
            self._complexity_initial = ratio
        self._complexity_min = min(self._complexity_min, ratio)

        # ── Crooks milestone ──
        cr = self.graph.crooks_ratio(prev_hash, action, curr_hash)
        if cr >= self._milestone_threshold:
            self._milestones.append(self.step)

        # ── Build snapshot ──
        snap = StateSnapshot(
            grid_hash=curr_hash,
            step=self.step,
            pe_mean=pe_mean,
            entropy=ent,
            complexity=ratio,
            crooks_ratio=cr,
            cycle_depth=self.graph.detect_cycles(curr_hash),
            absorption=self.graph.absorption_score(curr_hash),
        )

        # Compute spectral gap periodically (expensive)
        if self.step % 20 == 0 and self.graph.n_states >= 3:
            snap.spectral_gap = self.graph.spectral_gap()

        # Compute free energy: F = E - T*S
        # E = negative log of visit frequency (surprise)
        total_visits = sum(self.graph.visit_count.values()) or 1
        visit_freq = self.graph.visit_count.get(curr_hash, 1) / total_visits
        E = -np.log(visit_freq + 1e-12)
        # S = log of reachable states from here
        out = max(self.graph.out_degree(curr_hash), 1)
        S = np.log(out)
        # Temperature from Fantasia saturation proxy
        T = max(0.1, 1.0 - self.step / 300.0)  # cool down over time
        snap.free_energy = E - T * S

        # Composite φ
        snap.phi = self._compute_phi(snap)
        self.snapshots.append(snap)

    def progress(self, grid: Optional[np.ndarray] = None) -> float:
        """Current progress φ ∈ [0,1]. Higher = closer to winning."""
        if not self.snapshots:
            return 0.0
        if grid is not None:
            return self.score_state(grid)
        return self.snapshots[-1].phi

    def score_state(self, grid: np.ndarray) -> float:
        """Score a grid state using the thermodynamic progress function.

        Can be used for:
          - MCTS value function (replaces GoalUtilityScorer)
          - Action selection (pick action that maximizes φ)
          - Solver comparison (kill solver where φ plateaus)
        """
        if not self.snapshots:
            return 0.0

        h = frame_hash(grid)
        ent = shannon_entropy(grid)

        # Pe proxy from entropy + state novelty
        is_novel = h not in self.grids_seen
        pe_proxy = ent * (1.5 if is_novel else 1.0)

        # Complexity
        raw = grid.astype(np.uint8).tobytes()
        compressed = zlib.compress(raw, level=1)
        ratio = len(compressed) / max(len(raw), 1)

        snap = StateSnapshot(
            grid_hash=h,
            step=self.step,
            pe_mean=pe_proxy,
            entropy=ent,
            complexity=ratio,
            absorption=self.graph.absorption_score(h) if h in self.graph._state_idx else 0.0,
            cycle_depth=self.graph.detect_cycles(h) if h in self.graph._state_idx else 0,
        )

        return self._compute_phi(snap)

    def best_action(self, grid: np.ndarray, available_actions: list[int],
                    predict_fn, click_targets: list[tuple] = None) -> tuple:
        """Choose action that maximizes φ increase.

        Args:
            grid: current grid
            available_actions: list of valid action ints
            predict_fn: callable(grid, action, click_pos=None) -> predicted_grid
            click_targets: optional list of (r, c) for click actions

        Returns:
            (action, click_pos_or_None, predicted_phi)
        """
        best_action = available_actions[0] if available_actions else 0
        best_phi = -1.0
        best_click = None

        current_phi = self.progress(grid)

        # Score keyboard actions
        for action in available_actions:
            if action == 6:
                continue  # handle clicks separately
            pred_grid = predict_fn(grid, action)
            if pred_grid is None:
                continue
            phi = self.score_state(pred_grid)
            if phi > best_phi:
                best_phi = phi
                best_action = action
                best_click = None

        # Score click targets
        if 6 in available_actions and click_targets:
            for r, c in click_targets[:15]:
                pred_grid = predict_fn(grid, 6, click_pos=(r, c))
                if pred_grid is None:
                    continue
                phi = self.score_state(pred_grid)
                if phi > best_phi:
                    best_phi = phi
                    best_action = 6
                    best_click = (r, c)

        return best_action, best_click, best_phi

    def is_stuck(self, window: int = 15) -> bool:
        """Detect if progress has stalled (Kramers stuck state).

        True if φ hasn't increased in `window` steps.
        """
        if len(self.snapshots) < window:
            return False
        recent = [s.phi for s in self.snapshots[-window:]]
        return max(recent) - min(recent) < 0.005

    def barrier_progress(self) -> float:
        """How many barriers have we crossed relative to expected total?

        barrier_expected = d_eff × π/√2 per mechanism
        """
        if not self._milestones:
            return 0.0
        return min(len(self._milestones) / max(self._estimated_barriers, 1), 1.0)

    def set_barrier_estimate(self, n_mechanisms: int):
        """Set the estimated number of barriers from CellManifold."""
        self._estimated_barriers = max(n_mechanisms * BARRIER_CONST, 1.0)

    def phi_derivative(self, window: int = 5) -> float:
        """Rate of change of φ. Positive = making progress."""
        if len(self.snapshots) < window + 1:
            return 0.0
        recent = [s.phi for s in self.snapshots[-window:]]
        older = [s.phi for s in self.snapshots[-(2*window):-window]]
        if not older:
            return 0.0
        return np.mean(recent) - np.mean(older)

    def summary(self) -> dict:
        """Summary of detector state for logging/diagnostics."""
        if not self.snapshots:
            return {'step': 0, 'phi': 0.0}
        s = self.snapshots[-1]
        return {
            'step': self.step,
            'phi': round(s.phi, 4),
            'pe_mean': round(s.pe_mean, 4),
            'entropy': round(s.entropy, 4),
            'free_energy': round(s.free_energy, 4),
            'complexity': round(s.complexity, 4),
            'absorption': round(s.absorption, 4),
            'crooks_milestones': len(self._milestones),
            'cycle_depth': s.cycle_depth,
            'spectral_gap': round(s.spectral_gap, 4),
            'states_explored': self.graph.n_states,
            'phi_derivative': round(self.phi_derivative(), 4),
            'is_stuck': self.is_stuck(),
        }

    # ─── Internal: compute composite φ from snapshot ───────────────

    def _compute_phi(self, snap: StateSnapshot) -> float:
        """Combine seven signals into one progress scalar φ ∈ [0,1].

        Each signal is normalized to [0,1], higher = more progress.
        """
        signals = {}

        # 1. PE GRADIENT: Pe decreasing from initial = progress
        if self._pe_initial is not None and self._pe_initial > 0:
            pe_range = max(self._pe_max - self._pe_min, 0.001)
            if self._pe_initial > self._pe_min:
                signals['pe_gradient'] = np.clip(
                    (self._pe_initial - snap.pe_mean) /
                    (self._pe_initial - self._pe_min + 0.001),
                    0.0, 1.0
                )
            else:
                signals['pe_gradient'] = 0.0
        else:
            signals['pe_gradient'] = 0.0

        # 2. FREE ENERGY: lower is better, normalize against history
        if len(self.snapshots) > 2:
            fe_values = [s.free_energy for s in self.snapshots[-50:]]
            fe_max = max(fe_values)
            fe_min = min(fe_values)
            if fe_max > fe_min:
                signals['free_energy'] = np.clip(
                    (fe_max - snap.free_energy) / (fe_max - fe_min),
                    0.0, 1.0
                )
            else:
                signals['free_energy'] = 0.5
        else:
            signals['free_energy'] = 0.0

        # 3. SPECTRAL GAP: large gap = near attractor
        # Use most recent computed value
        latest_gap = snap.spectral_gap
        if latest_gap == 0 and self.snapshots:
            # Find most recent non-zero gap
            for s in reversed(self.snapshots[-20:]):
                if s.spectral_gap > 0:
                    latest_gap = s.spectral_gap
                    break
        signals['spectral_gap'] = np.clip(latest_gap, 0.0, 1.0)

        # 4. ABSORPTION: high = terminal state
        signals['absorption'] = np.clip(snap.absorption, 0.0, 1.0)

        # 5. CROOKS GATES: milestones crossed / expected
        signals['crooks_gates'] = self.barrier_progress()

        # 6. COMPLEXITY: decreasing = approaching simplicity
        if self._complexity_initial is not None and self._complexity_initial > 0:
            if self._complexity_initial > self._complexity_min:
                signals['complexity'] = np.clip(
                    (self._complexity_initial - snap.complexity) /
                    (self._complexity_initial - self._complexity_min + 0.001),
                    0.0, 1.0
                )
            else:
                signals['complexity'] = 0.0
        else:
            signals['complexity'] = 0.0

        # 7. CYCLE ESCAPE: not in a cycle = progress
        if snap.cycle_depth > 0:
            signals['cycle_escape'] = 0.0  # stuck in cycle
        else:
            # Check if we WERE in a cycle and escaped
            if self.snapshots and any(s.cycle_depth > 0
                                       for s in self.snapshots[-10:]):
                signals['cycle_escape'] = 1.0  # just escaped!
            else:
                signals['cycle_escape'] = 0.5  # neutral

        # ── Weighted combination ──
        phi = sum(self.WEIGHTS[k] * signals.get(k, 0.0)
                  for k in self.WEIGHTS)

        # Entropy bonus: strictly decreasing entropy is always good
        if (self._entropy_initial is not None and
                snap.entropy < self._entropy_initial):
            ent_progress = np.clip(
                (self._entropy_initial - snap.entropy) /
                max(self._entropy_initial, 0.001),
                0.0, 0.3
            )
            phi = min(1.0, phi + ent_progress * 0.15)

        return float(np.clip(phi, 0.0, 1.0))


# ═══════════════════════════════════════════════════════════════════
#  CONVENIENCE: φ-BASED GOAL SCORER (drop-in for GoalUtilityScorer)
# ═══════════════════════════════════════════════════════════════════

class PhiScorer:
    """Drop-in replacement for GoalUtilityScorer in aaa_solver.py.

    Instead of hardcoded goal hypotheses, uses EckertWinDetector's
    thermodynamic progress function as the scoring axis.
    """

    def __init__(self, detector: EckertWinDetector, base_entropy: float):
        self.detector = detector
        self.base_entropy = max(base_entropy, 0.001)
        self.best_phi = 0.0
        self.best_entropy = base_entropy
        self.seen: set[str] = set()

    def score(self, grid: np.ndarray,
              navigator=None) -> float:
        """Score a state using φ + novelty bonus.

        Matches the GoalUtilityScorer.score() interface.
        """
        h = frame_hash(grid)
        ent = shannon_entropy(grid)

        # φ axis (0.7 weight) — the thermodynamic progress
        phi = self.detector.score_state(grid)
        if phi > self.best_phi:
            self.best_phi = phi

        # Entropy axis (0.15 weight)
        ent_score = max(0.0, (self.base_entropy - ent) / self.base_entropy)
        if ent < self.best_entropy:
            self.best_entropy = ent

        # Novelty axis (0.15 weight)
        novel = 1.0 if h not in self.seen else 0.1
        self.seen.add(h)

        return 0.7 * phi + 0.15 * ent_score + 0.15 * novel


# ═══════════════════════════════════════════════════════════════════
#  CONVENIENCE: φ-BASED FITNESS FUNCTION (for replicator dynamics)
# ═══════════════════════════════════════════════════════════════════

def phi_fitness(detector: EckertWinDetector, window: int = 10) -> float:
    """Compute fitness for replicator dynamics from φ history.

    Reward = φ improvement rate over recent window.
    Used by self_learner.py's StrategyEvolver.

    Returns reward ∈ [-1, 1]:
      positive = φ is increasing (making progress)
      zero     = flat (stalled)
      negative = φ is decreasing (going backwards)
    """
    if len(detector.snapshots) < 3:
        return 0.0

    # Current φ vs φ at start of strategy
    current = detector.snapshots[-1].phi
    start_idx = max(0, len(detector.snapshots) - window)
    start = detector.snapshots[start_idx].phi

    delta = current - start

    # Also reward absolute φ level
    level_bonus = current * 0.3

    # Penalty for being stuck
    stuck_penalty = -0.3 if detector.is_stuck(window=window) else 0.0

    return float(np.clip(delta * 3.0 + level_bonus + stuck_penalty, -1.0, 1.0))


# ═══════════════════════════════════════════════════════════════════
#  CONVENIENCE: Pe-MINIMUM TARGET (for instanton planner)
# ═══════════════════════════════════════════════════════════════════

def pe_minimum_target(detector: EckertWinDetector) -> Optional[str]:
    """Find the state hash with minimum Pe mean — the compile target.

    Used by instanton_planner to set the target state for
    XOR compilation instead of minimum entropy.

    Returns the hash of the state with lowest Pe, or None.
    """
    if not detector.snapshots:
        return None

    best_hash = None
    best_pe = float('inf')

    for snap in detector.snapshots:
        # Weighted: low Pe + low entropy + high absorption
        score = (snap.pe_mean * 0.5 +
                 snap.entropy * 0.3 -
                 snap.absorption * 0.2)
        if score < best_pe:
            best_pe = score
            best_hash = snap.grid_hash

    return best_hash
