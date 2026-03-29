"""ARC-AGI-3 Recursive Self-Improving Solver.

The core loop (PROBE → COMPRESS → PREDICT → ACT → MEASURE → UPDATE):

  1. PROBE:    Capture frame transition as XOR packet
  2. COMPRESS: K-Factorize → extract shape atoms, build grammar
  3. PREDICT:  Use grammar + Fisher metric to predict next frame
  4. ACT:      Take the action that maximizes expected information gain
  5. MEASURE:  Compute Fisher divergence: predicted vs actual
  6. UPDATE:   Refine grammar weights via Fisher gradient
  7. BARRIER:  If d_eff × π/√2 < budget_remaining → switch exploit
  8. GOTO 1

Math apparatus applied:
  §136  K-Factorization  — shape × scale grammar extraction
  §136D2 Barrier          — d_eff × π/√2 explore/exploit gate
  §138  Fisher geodesic   — prediction error as learning signal
  §165  Čencov metric     — natural distance on transition manifold
  Crooks fluctuation      — reversibility detection from XOR symmetry
  GF(2) vector space      — XOR basis = minimum instruction set

Zero LLM calls. The solver improves itself each step via the math.
"""
import hashlib
import time
import zlib
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
from packet_analyzer import shannon_entropy


# ─── GF(2) Vector Space — XOR Basis Extraction ──────────────────

class XORVectorSpace:
    """Treat XOR transition patterns as vectors in GF(2).

    XOR is addition in GF(2). The set of all observed transitions forms
    a vector space. The basis of this space = the minimum set of "atomic
    moves" that can generate all observed transitions via composition.

    If we find a small basis, the game has simple rules.
    If the basis is large, the game is complex.
    """

    def __init__(self):
        self.vectors = []      # list of (action, flattened XOR bool array)
        self.basis = []        # reduced basis vectors
        self.basis_actions = [] # which actions produced basis vectors
        self.rank = 0

    def add_transition(self, action: int, xor: np.ndarray):
        """Add an observed XOR transition to the space."""
        vec = (xor > 0).flatten().astype(np.uint8)
        if vec.sum() == 0:
            return

        self.vectors.append((action, vec))
        self._update_basis(action, vec)

    def _update_basis(self, action: int, vec: np.ndarray):
        """Gaussian elimination in GF(2) to maintain reduced basis."""
        v = vec.copy()

        for basis_vec in self.basis:
            # In GF(2), subtraction = addition = XOR
            overlap = np.bitwise_and(v, basis_vec)
            if overlap.any():
                v = np.bitwise_xor(v, basis_vec)

        if v.any():
            self.basis.append(v)
            self.basis_actions.append(action)
            self.rank = len(self.basis)

    def can_express(self, xor: np.ndarray) -> bool:
        """Can this transition be expressed as a combination of basis vectors?"""
        v = (xor > 0).flatten().astype(np.uint8)
        for basis_vec in self.basis:
            overlap = np.bitwise_and(v, basis_vec)
            if overlap.any():
                v = np.bitwise_xor(v, basis_vec)
        return not v.any()

    def novelty(self, xor: np.ndarray) -> float:
        """How much of this XOR is NOT expressible by the current basis? [0,1]"""
        if not self.basis:
            return 1.0
        v = (xor > 0).flatten().astype(np.uint8)
        original_mass = v.sum()
        if original_mass == 0:
            return 0.0

        for basis_vec in self.basis:
            overlap = np.bitwise_and(v, basis_vec)
            if overlap.any():
                v = np.bitwise_xor(v, basis_vec)

        residual_mass = v.sum()
        return float(residual_mass) / float(original_mass)


# ─── K-Factorization Grammar ────────────────────────────────────

@dataclass
class ShapeAtom:
    """An atomic shape pattern extracted via K-Factorization."""
    pattern: np.ndarray     # the XOR patch (bounding box)
    shape_hash: str         # position-invariant hash
    size: tuple             # (h, w)
    compactness: float      # filled fraction of bounding box
    n_components: int       # connected components in this atom
    color_signature: tuple  # sorted unique XOR values
    count: int = 0          # how many times observed
    action_affinity: dict = field(default_factory=dict)  # action → count

    def matches(self, other: 'ShapeAtom', tolerance: float = 0.0) -> bool:
        """Position-invariant match."""
        if self.size != other.size:
            return False
        if tolerance == 0:
            return np.array_equal(self.pattern, other.pattern)
        # Fuzzy match: overlap fraction
        overlap = np.logical_and(self.pattern > 0, other.pattern > 0).sum()
        union = np.logical_or(self.pattern > 0, other.pattern > 0).sum()
        return (overlap / max(union, 1)) >= (1 - tolerance)


class KGrammar:
    """K-Factorization grammar: recursively decompose transitions into atoms.

    Q_transition = Σ (atom_i at position_i) × scale_i

    The grammar learns by observing transitions. Each new transition is
    decomposed into known atoms + residual. The residual becomes a new atom.
    Over time, the grammar converges to a small set of atoms that explain
    all transitions — these are the game's rules.
    """

    def __init__(self):
        self.atoms: list[ShapeAtom] = []
        self.atom_index: dict[str, int] = {}  # shape_hash → index
        self.decompositions: list[list] = []   # transition → [(atom_idx, pos, scale)]

    def decompose(self, xor: np.ndarray, action: int) -> dict:
        """Decompose a transition into known atoms + residual."""
        residual = xor.copy()
        used_atoms = []

        # Find connected components in the XOR
        binary = (xor > 0).astype(np.int32)
        labeled, n_comp = ndimage.label(binary)

        for comp_id in range(1, n_comp + 1):
            comp_mask = labeled == comp_id
            rows, cols = np.where(comp_mask)
            if len(rows) == 0:
                continue

            r0, r1 = rows.min(), rows.max() + 1
            c0, c1 = cols.min(), cols.max() + 1
            patch = xor[r0:r1, c0:c1].copy()

            # Hash the patch (position-invariant)
            h = hashlib.md5(patch.tobytes()).hexdigest()[:10]

            if h in self.atom_index:
                # Known atom — match
                idx = self.atom_index[h]
                self.atoms[idx].count += 1
                self.atoms[idx].action_affinity[action] = \
                    self.atoms[idx].action_affinity.get(action, 0) + 1
                used_atoms.append((idx, (r0, c0), 1.0))
                # Clear from residual
                residual[r0:r1, c0:c1] = np.where(comp_mask[r0:r1, c0:c1],
                                                    0, residual[r0:r1, c0:c1])
            else:
                # New atom — add to grammar
                comp_binary = (patch > 0).astype(np.int32)
                n_sub = int(ndimage.label(comp_binary)[1])
                filled = comp_binary.sum()
                total = comp_binary.size
                atom = ShapeAtom(
                    pattern=patch,
                    shape_hash=h,
                    size=(r1 - r0, c1 - c0),
                    compactness=filled / max(total, 1),
                    n_components=n_sub,
                    color_signature=tuple(sorted(set(patch[patch > 0].tolist()))),
                    count=1,
                    action_affinity={action: 1},
                )
                self.atoms.append(atom)
                self.atom_index[h] = len(self.atoms) - 1
                used_atoms.append((len(self.atoms) - 1, (r0, c0), 1.0))
                residual[r0:r1, c0:c1] = np.where(comp_mask[r0:r1, c0:c1],
                                                    0, residual[r0:r1, c0:c1])

        residual_mass = (residual > 0).sum()
        total_mass = (xor > 0).sum()
        coverage = 1.0 - (residual_mass / max(total_mass, 1))

        self.decompositions.append(used_atoms)

        return {
            "atoms_used": len(used_atoms),
            "atoms_known": sum(1 for idx, _, _ in used_atoms
                              if self.atoms[idx].count > 1),
            "atoms_new": sum(1 for idx, _, _ in used_atoms
                            if self.atoms[idx].count == 1),
            "residual_mass": int(residual_mass),
            "coverage": round(coverage, 4),
            "total_atoms": len(self.atoms),
        }

    def predict_action_effect(self, action: int) -> list[ShapeAtom]:
        """Which atoms does this action typically produce?"""
        affinities = []
        for atom in self.atoms:
            if action in atom.action_affinity:
                affinities.append((atom, atom.action_affinity[action]))
        affinities.sort(key=lambda x: -x[1])
        return [a for a, _ in affinities[:5]]

    def grammar_complexity(self) -> int:
        """Number of unique atoms = complexity of the game's rules."""
        return len(self.atoms)

    def most_frequent_atoms(self, n: int = 5) -> list[ShapeAtom]:
        return sorted(self.atoms, key=lambda a: -a.count)[:n]


# ─── Fisher Information Engine ───────────────────────────────────

class FisherEngine:
    """Compute Fisher information from prediction errors.

    The Fisher information I(θ) = E[(∂log p/∂θ)²] measures how much
    information an observation carries about the parameter θ.

    In our context:
    - θ = the game's rule parameters (encoded in the grammar)
    - Observation = actual transition XOR
    - Prediction = grammar-predicted transition
    - Fisher divergence = prediction error in the natural metric

    High Fisher info = high prediction error = we're learning fast.
    Low Fisher info = we've learned the rules = switch to exploit.
    """

    def __init__(self):
        self.predictions = []    # (predicted_hash, actual_hash, fisher_div)
        self.fisher_series = []  # Fisher info over time
        self.cumulative_info = 0.0
        self.window_size = 10

    def compute_divergence(self, predicted: Optional[np.ndarray],
                           actual: np.ndarray) -> float:
        """Fisher divergence between predicted and actual frames.

        Uses the Čencov-natural metric on the color distribution manifold:
        d²_F = Σ (√p_i - √q_i)² = Hellinger distance squared.

        This is the UNIQUE metric invariant under sufficient statistics
        (Čencov's theorem, §165), so it's the "right" distance measure.
        """
        if predicted is None:
            # No prediction = maximum ignorance
            return 1.0

        # Color histograms as probability distributions
        p_hist = np.bincount(predicted.flatten().astype(int), minlength=16).astype(float)
        q_hist = np.bincount(actual.flatten().astype(int), minlength=16).astype(float)

        p_hist /= p_hist.sum() + 1e-12
        q_hist /= q_hist.sum() + 1e-12

        # Hellinger distance (from Čencov metric)
        hellinger = np.sqrt(0.5 * np.sum((np.sqrt(p_hist) - np.sqrt(q_hist))**2))

        # Also compute cell-level accuracy
        if predicted.shape == actual.shape:
            cell_accuracy = (predicted == actual).mean()
            # Combine: Hellinger for distribution, cell accuracy for spatial
            fisher_div = 0.5 * hellinger + 0.5 * (1 - cell_accuracy)
        else:
            fisher_div = hellinger

        return float(fisher_div)

    def record(self, predicted: Optional[np.ndarray], actual: np.ndarray,
               predicted_hash: str, actual_hash: str):
        """Record a prediction and compute Fisher info."""
        div = self.compute_divergence(predicted, actual)
        self.predictions.append((predicted_hash, actual_hash, div))
        self.fisher_series.append(div)
        self.cumulative_info += div

    def current_info_rate(self) -> float:
        """Recent Fisher information rate — are we still learning?"""
        if len(self.fisher_series) < 2:
            return 1.0
        window = self.fisher_series[-self.window_size:]
        return float(np.mean(window))

    def info_trend(self) -> float:
        """Derivative of Fisher info — positive = learning accelerating."""
        if len(self.fisher_series) < 4:
            return 0.0
        recent = self.fisher_series[-self.window_size:]
        if len(recent) < 4:
            return 0.0
        mid = len(recent) // 2
        first_half = np.mean(recent[:mid])
        second_half = np.mean(recent[mid:])
        return float(second_half - first_half)

    def should_exploit(self) -> bool:
        """Has Fisher info converged? → switch to exploit mode."""
        if len(self.fisher_series) < 10:
            return False
        rate = self.current_info_rate()
        trend = self.info_trend()
        # Exploit when: low info rate AND decreasing trend
        return rate < 0.1 and trend <= 0


# ─── Crooks Reversibility Detector ──────────────────────────────

class CrooksDetector:
    """Detect action reversibility from XOR symmetry.

    Crooks fluctuation theorem: P(A→B)/P(B→A) = exp(ΔF)

    If action X produces XOR pattern P, and action Y produces a pattern
    that "undoes" P (same changed cells, inverse color transitions),
    then X and Y are thermodynamic conjugates.

    This gives us safe exploration: we can always undo what we did.
    """

    def __init__(self):
        self.action_xors = defaultdict(list)  # action → [(state_hash, xor)]
        self.reverse_pairs = {}  # action → reverse_action
        self.work_done = defaultdict(float)  # action → estimated free energy cost

    def record(self, action: int, state_hash: str,
               xor: np.ndarray, prev_grid: np.ndarray, curr_grid: np.ndarray):
        """Record a transition and check for reversibility."""
        self.action_xors[action].append((state_hash, xor.copy()))

        # Compute "work" = entropy change (proxy for free energy)
        ent_before = shannon_entropy(prev_grid)
        ent_after = shannon_entropy(curr_grid)
        self.work_done[action] = float(ent_after - ent_before)

        # Check if any other action reverses this one
        changed = xor > 0
        if not changed.any():
            return

        old_vals = prev_grid[changed]
        new_vals = curr_grid[changed]

        # For each other action, check if it reverses these color transitions
        for other_action, transitions in self.action_xors.items():
            if other_action == action:
                continue
            for other_hash, other_xor in transitions[-5:]:  # check recent
                other_changed = other_xor > 0
                # Same cells changed?
                if np.array_equal(changed, other_changed):
                    # Reverse color transitions? (we'd need the frames, approximate with XOR equality)
                    if np.array_equal(xor, other_xor):
                        self.reverse_pairs[action] = other_action
                        self.reverse_pairs[other_action] = action

    def get_reverse(self, action: int) -> Optional[int]:
        return self.reverse_pairs.get(action)

    def is_reversible(self, action: int) -> bool:
        return action in self.reverse_pairs

    def safe_actions(self) -> list[int]:
        """Actions that can be undone."""
        return list(self.reverse_pairs.keys())


# ─── Entropy Ratchet ─────────────────────────────────────────────

class EntropyRatchet:
    """Track entropy trajectory. Progress = entropy decrease toward goal.

    The ratchet keeps the "best" (lowest entropy) state seen and measures
    progress relative to it. If entropy increases, we might be regressing.

    Combined with Fisher info: high Fisher + decreasing entropy = golden path.
    """

    def __init__(self):
        self.entropy_series = []
        self.best_entropy = float('inf')
        self.best_frame_hash = None
        self.progress_actions = []  # actions that decreased entropy

    def record(self, grid: np.ndarray, action: int, frame_h: str):
        ent = shannon_entropy(grid)
        self.entropy_series.append(ent)

        if ent < self.best_entropy:
            self.best_entropy = ent
            self.best_frame_hash = frame_h
            if action is not None:
                self.progress_actions.append(action)

    def is_progressing(self, window: int = 5) -> bool:
        if len(self.entropy_series) < window:
            return True
        recent = self.entropy_series[-window:]
        return recent[-1] <= recent[0]

    def entropy_delta(self) -> float:
        if len(self.entropy_series) < 2:
            return 0.0
        return self.entropy_series[-1] - self.entropy_series[-2]

    def best_action_distribution(self) -> dict:
        """Which actions most often decrease entropy?"""
        return dict(Counter(self.progress_actions))


# ─── Barrier Gate ────────────────────────────────────────────────

class BarrierGate:
    """Explore/exploit switching via barrier = d_eff × π/√2.

    d_eff = rank of the XOR vector space (unique independent transitions).
    barrier = d_eff × π/√2 (from §136D2).

    When actions_remaining < barrier → we can't afford more exploration.
    When Fisher info has converged → exploration isn't productive anymore.

    The gate self-updates as d_eff changes (more transitions observed).
    """

    def __init__(self, total_budget: int):
        self.total_budget = total_budget
        self.actions_used = 0
        self.d_eff_history = [1]
        self.mode = "EXPLORE"  # or "EXPLOIT"

    def update(self, d_eff: int, fisher_rate: float):
        self.d_eff_history.append(d_eff)
        barrier = d_eff * np.pi / np.sqrt(2)
        remaining = self.total_budget - self.actions_used

        # Switch to exploit if:
        # 1. Remaining budget < barrier (can't afford more exploration)
        # 2. Fisher info has converged (nothing left to learn)
        # 3. d_eff has stabilized (no new independent transitions)
        d_stable = len(self.d_eff_history) >= 5 and \
                   len(set(self.d_eff_history[-5:])) == 1

        if remaining < barrier or (fisher_rate < 0.1 and d_stable):
            self.mode = "EXPLOIT"
        else:
            self.mode = "EXPLORE"

    def tick(self):
        self.actions_used += 1

    @property
    def barrier(self) -> float:
        return self.d_eff_history[-1] * np.pi / np.sqrt(2)

    @property
    def remaining(self) -> int:
        return self.total_budget - self.actions_used


# ─── The Recursive Solver ───────────────────────────────────────

class RecursiveSolver:
    """Self-improving solver using the full math apparatus.

    Each action:
    1. Grammar PREDICTS the result
    2. We take the action and OBSERVE
    3. Fisher engine MEASURES the prediction error
    4. Grammar UPDATES with the new observation
    5. Barrier gate DECIDES explore vs exploit
    6. XOR space TRACKS dimensionality
    7. Crooks detector MAPS reversibility
    8. Entropy ratchet TRACKS progress

    The solver gets better at predicting → focuses on unpredictable states
    → learns those → gets better → converges → exploits.
    """

    def __init__(self, profile: GameProfile, env, obs, budget_per_level: int = 300,
                 shared_state=None):
        self.profile = profile
        self.env = env
        self.obs = obs

        # Math apparatus — use shared state if provided
        if shared_state:
            self.grammar = shared_state.grammar
            self.xor_space = shared_state.xor_space
        else:
            self.grammar = KGrammar()
            self.xor_space = XORVectorSpace()
        self.fisher = FisherEngine()
        self.crooks = CrooksDetector()
        self.ratchet = EntropyRatchet()
        self.barrier = BarrierGate(budget_per_level)

        # State tracking
        self.frames = [np.array(obs.frame[0])]
        self.actions_taken = []
        self.total_actions = 0
        self.levels_solved = 0

        # Strategy cache: state_hash → best_action
        self.policy_cache = {}

        # Initialize ratchet with starting frame
        self.ratchet.record(self.frames[0], None, frame_hash(self.frames[0]))

    def step(self, action: int, click_x=None, click_y=None) -> dict:
        """Take one action through the full recursive loop."""
        prev_grid = np.array(self.obs.frame[0])
        prev_hash = frame_hash(prev_grid)

        # ─── PREDICT ───
        predicted = self._predict(prev_grid, action)

        # ─── ACT ───
        if action == 6 and click_x is not None:
            self.obs = self.env.step(6, data={"x": click_x, "y": click_y})
        else:
            self.obs = self.env.step(action)

        curr_grid = np.array(self.obs.frame[0])
        curr_hash = frame_hash(curr_grid)
        xor = xor_grids(prev_grid, curr_grid)
        is_noop = not xor.any()

        self.frames.append(curr_grid)
        self.actions_taken.append(action)
        self.total_actions += 1

        # ─── MEASURE (Fisher) ───
        pred_hash = frame_hash(predicted) if predicted is not None else "none"
        self.fisher.record(predicted, curr_grid, pred_hash, curr_hash)
        fisher_div = self.fisher.fisher_series[-1]

        # ─── UPDATE ───
        decomp = {"atoms_used": 0, "coverage": 1.0, "total_atoms": 0}
        if not is_noop:
            # K-Grammar decomposition
            decomp = self.grammar.decompose(xor, action)

            # XOR vector space
            self.xor_space.add_transition(action, xor)

            # Crooks reversibility
            self.crooks.record(action, prev_hash, xor, prev_grid, curr_grid)

        # Entropy ratchet
        self.ratchet.record(curr_grid, action, curr_hash)

        # ─── BARRIER GATE ───
        self.barrier.tick()
        self.barrier.update(self.xor_space.rank, self.fisher.current_info_rate())

        # ─── POLICY CACHE ───
        # If this action was good (Fisher div > 0 = learned something, entropy decreased)
        if fisher_div > 0.05 and self.ratchet.entropy_delta() < 0:
            self.policy_cache[prev_hash] = action

        return {
            "action": action,
            "is_noop": is_noop,
            "fisher_div": round(fisher_div, 4),
            "grammar": decomp,
            "xor_rank": self.xor_space.rank,
            "barrier": round(self.barrier.barrier, 1),
            "mode": self.barrier.mode,
            "entropy_delta": round(self.ratchet.entropy_delta(), 4),
            "info_rate": round(self.fisher.current_info_rate(), 4),
            "reversible": self.crooks.is_reversible(action),
        }

    def _predict(self, grid: np.ndarray, action: int) -> Optional[np.ndarray]:
        """Predict the result of an action using the grammar."""
        # Method 1: exact state+action seen before → replay
        h = frame_hash(grid)
        for i, (f_hash, act) in enumerate(
            zip([frame_hash(f) for f in self.frames[:-1]], self.actions_taken)
        ):
            if f_hash == h and act == action and i + 1 < len(self.frames):
                return self.frames[i + 1].copy()

        # Method 2: grammar-based prediction
        # Find atoms associated with this action
        atoms = self.grammar.predict_action_effect(action)
        if not atoms:
            return None

        # Apply the most frequent atom at a heuristic position
        predicted = grid.copy().astype(np.uint8)
        for atom in atoms[:2]:
            # Find where this atom pattern best matches the current grid
            # (look for regions that contain the atom's color signature)
            ah, aw = atom.size
            best_pos = None
            best_overlap = -1

            # Search near the center of mass of previous changes
            if len(self.frames) > 2:
                prev_xor = xor_grids(self.frames[-3], self.frames[-2])
                if prev_xor.any():
                    rows, cols = np.where(prev_xor > 0)
                    search_r = int(rows.mean())
                    search_c = int(cols.mean())
                else:
                    search_r, search_c = 32, 32
            else:
                search_r, search_c = 32, 32

            # Search window around last change location
            for dr in range(-8, 9, 2):
                for dc in range(-8, 9, 2):
                    r = max(0, min(63 - ah, search_r + dr))
                    c = max(0, min(63 - aw, search_c + dc))
                    region = grid[r:r+ah, c:c+aw]
                    if region.shape != (ah, aw):
                        continue
                    # Overlap: how many cells of the atom pattern exist in this region
                    overlap = (region > 0).sum()
                    if overlap > best_overlap:
                        best_overlap = overlap
                        best_pos = (r, c)

            if best_pos:
                r, c = best_pos
                predicted[r:r+ah, c:c+aw] ^= atom.pattern

        return predicted

    def choose_action(self) -> tuple:
        """Choose the best action using all available signals.

        Returns (action, click_x, click_y) — click coords are None for non-click.
        """
        grid = np.array(self.obs.frame[0])
        h = frame_hash(grid)
        available = list(self.obs.available_actions)
        non_click = [a for a in available if a != 6]

        # 1. Policy cache hit?
        if h in self.policy_cache and self.barrier.mode == "EXPLOIT":
            cached = self.policy_cache[h]
            if cached in available:
                return (cached, None, None)

        # 2. EXPLOIT mode: use progress actions (entropy-decreasing)
        if self.barrier.mode == "EXPLOIT":
            best_actions = self.ratchet.best_action_distribution()
            if best_actions:
                best = max(best_actions, key=best_actions.get)
                if best in available:
                    return (best, None, None)

        # 3. EXPLORE mode: maximize expected Fisher information
        # Try the action that produces the highest novelty in XOR space
        if non_click:
            best_action = None
            best_novelty = -1

            for a in non_click:
                # Predict what this action will do
                predicted = self._predict(grid, a)
                if predicted is not None:
                    predicted_xor = xor_grids(grid, predicted)
                    novelty = self.xor_space.novelty(predicted_xor)
                else:
                    novelty = 1.0  # unknown = maximally novel

                if novelty > best_novelty:
                    best_novelty = novelty
                    best_action = a

            if best_action is not None:
                return (best_action, None, None)

        # 4. Click games: find clickable targets
        if 6 in available:
            bg = int(np.bincount(grid.flatten()).argmax())
            if self.profile.clickable_colors:
                for color in self.profile.clickable_colors:
                    positions = np.where(grid == color)
                    if len(positions[0]) > 0:
                        # Click the first unvisited cluster
                        mask = (grid == color).astype(np.int32)
                        labeled, n = ndimage.label(mask)
                        for i in range(1, n + 1):
                            comp = labeled == i
                            rows, cols = np.where(comp)
                            cy, cx = int(rows.mean()), int(cols.mean())
                            return (6, cx, cy)

            # Fallback: click random non-bg
            nonbg = np.where(grid != bg)
            if len(nonbg[0]) > 0:
                rng = np.random.default_rng(self.total_actions)
                idx = rng.integers(len(nonbg[0]))
                return (6, int(nonbg[1][idx]), int(nonbg[0][idx]))

        # 5. Fallback: cycle through actions
        if non_click:
            return (non_click[self.total_actions % len(non_click)], None, None)
        return (available[0] if available else 1, None, None)

    def solve_level(self) -> bool:
        """Solve one level using the recursive loop."""
        start_level = self.obs.levels_completed
        self.barrier = BarrierGate(300)  # reset per level

        for _ in range(300):
            if self.obs.state == GameState.WIN:
                return True
            if self.obs.state == GameState.GAME_OVER:
                return False
            if self.obs.levels_completed > start_level:
                return True

            action, cx, cy = self.choose_action()
            result = self.step(action, click_x=cx, click_y=cy)

        return self.obs.levels_completed > start_level

    def solve_game(self, verbose: bool = True) -> dict:
        """Solve all levels."""
        if verbose:
            print(f"  Grammar: {self.grammar.grammar_complexity()} atoms | "
                  f"XOR rank: {self.xor_space.rank} | "
                  f"Mode: {self.barrier.mode}")

        for level in range(self.profile.win_levels):
            if self.obs.state == GameState.WIN:
                break
            if self.obs.state == GameState.GAME_OVER:
                if verbose:
                    print(f"  Level {level}: GAME OVER")
                break

            level_start = self.total_actions
            solved = self.solve_level()
            level_actions = self.total_actions - level_start

            if solved:
                self.levels_solved += 1
                if verbose:
                    print(f"  Level {level}: SOLVED in {level_actions} actions | "
                          f"grammar={self.grammar.grammar_complexity()} atoms | "
                          f"rank={self.xor_space.rank} | "
                          f"fisher_rate={self.fisher.current_info_rate():.3f} | "
                          f"safe_actions={self.crooks.safe_actions()}")
            else:
                if verbose:
                    print(f"  Level {level}: FAILED after {level_actions} actions | "
                          f"grammar={self.grammar.grammar_complexity()} atoms | "
                          f"rank={self.xor_space.rank} | "
                          f"fisher_rate={self.fisher.current_info_rate():.3f} | "
                          f"mode={self.barrier.mode}")
                break

        return {
            "game_id": self.profile.game_id,
            "levels_solved": self.levels_solved,
            "win_levels": self.profile.win_levels,
            "total_actions": self.total_actions,
            "grammar_atoms": self.grammar.grammar_complexity(),
            "xor_rank": self.xor_space.rank,
            "fisher_cumulative": round(self.fisher.cumulative_info, 2),
            "reverse_pairs": dict(self.crooks.reverse_pairs),
            "progress_actions": self.ratchet.best_action_distribution(),
        }


# ─── Pipeline ────────────────────────────────────────────────────

def solve(game_id: str, probe_budget: int = 30, verbose: bool = True,
          shared_state=None, profile: 'GameProfile' = None) -> dict:
    """Full pipeline: Probe → Recursive Solve."""
    if verbose:
        print(f"\n{'='*65}")
        print(f"  RECURSIVE SOLVER: {game_id}")
        print(f"{'='*65}")
        print(f"  Phase 0: Probe...")

    if profile is None:
        profile = probe_game(game_id, budget=probe_budget, verbose=False)

    if verbose:
        print(f"  Profile: {profile.solver_hint()}")

    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    solver = RecursiveSolver(profile, env, obs, shared_state=shared_state)

    if verbose:
        print(f"  Phase 1: Recursive solve (barrier-gated)...")

    result = solver.solve_game(verbose=verbose)

    if verbose:
        print(f"\n  RESULT: {result['levels_solved']}/{result['win_levels']} levels | "
              f"{result['total_actions']} actions | "
              f"grammar={result['grammar_atoms']} atoms | "
              f"rank={result['xor_rank']} | "
              f"Fisher={result['fisher_cumulative']}")
        if result['reverse_pairs']:
            print(f"  Reversible pairs: {result['reverse_pairs']}")
        if result['progress_actions']:
            print(f"  Progress actions: {result['progress_actions']}")

    return result


# ─── Main ────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ARC-AGI-3 Recursive Self-Improving Solver")
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

        print(f"\n{'Game':<22s} {'Solved':>7s} {'Acts':>6s} "
              f"{'Atoms':>6s} {'Rank':>5s} {'Fisher':>8s}")
        print("-" * 65)

        for e in envs:
            try:
                r = solve(e.game_id, probe_budget=args.probe_budget,
                         verbose=args.verbose)
                results.append(r)
                if not args.verbose:
                    print(f"{r['game_id']:<22s} "
                          f"{r['levels_solved']}/{r['win_levels']:<5d} "
                          f"{r['total_actions']:>6d} "
                          f"{r['grammar_atoms']:>6d} {r['xor_rank']:>5d} "
                          f"{r['fisher_cumulative']:>8.1f}")
            except Exception as ex:
                print(f"{e.game_id:<22s} ERROR: {str(ex)[:60]}")

        total_levels = sum(r.get("levels_solved", 0) for r in results)
        total_possible = sum(r.get("win_levels", 0) for r in results)
        total_atoms = sum(r.get("grammar_atoms", 0) for r in results)
        print(f"\nTOTAL: {total_levels}/{total_possible} levels | "
              f"{total_atoms} grammar atoms learned")
    else:
        solve(args.game_id, probe_budget=args.probe_budget, verbose=True)
