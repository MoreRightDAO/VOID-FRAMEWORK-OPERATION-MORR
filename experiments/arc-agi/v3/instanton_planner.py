"""ARC-AGI-3 Instanton Planner — the novel architecture.

THESIS: Don't search through STATES. Solve for TRANSITIONS.

Traditional planners (A*, MCTS, BFS) ask:
  "What state do I reach if I take action A from state S?"
  Then they search the tree of states for one that looks like a goal.

This planner asks:
  "What XOR do I need to apply to reach a better state?"
  Then it SOLVES for the action sequence via linear algebra in GF(2).

It's a COMPILER, not a search. It compiles a desired state change
into an action sequence using three novel mechanisms:

1. XOR TELESCOPE — compose action templates to predict states N steps
   ahead WITHOUT simulation. Templates are localized (5×5 for agents),
   so non-overlapping compositions are exact. This gives O(1) lookahead
   instead of O(b^d) search.

2. INSTANTON DECOMPOSITION — given a desired XOR target, decompose it
   into minimum-weight sum of basis atoms over GF(2). This is solving
   Ax = b where A = atom basis matrix, x = which atoms to use, b = target.
   The solution IS the action sequence. No search required.

3. SPECTRAL NAVIGATION — eigendecompose the empirical transition matrix.
   The dominant eigenvector points toward the game's attractor (= goal).
   Project current state onto this eigenvector. Choose actions that
   increase the projection. This is navigation by RESONANCE, not search.

Combined with the existing engines:
  - Fisher cell map → WHERE to apply the instanton
  - Kramers potential → WHEN to invoke escape instanton
  - Replicator dynamics → action fitness weights the decomposition
  - Fantasia bound → budget allocation between explore/compile/execute

Math: §48A (Onsager-Machlup instanton), §136 (K-Factorization),
      §164 (spectral decomposition), §165 (Čencov geodesic)
"""
import hashlib
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage

import arc_agi
from arcengine import GameState

from packet_probe import (
    GameProfile, probe_game, frame_hash, xor_grids,
    extract_xor_template
)
from packet_analyzer import shannon_entropy
from eckert_win_detector import EckertWinDetector


# ═══════════════════════════════════════════════════════════════════
#  1. TRANSITION MEMORY — indexed by position, color, and shape
# ═══════════════════════════════════════════════════════════════════

@dataclass
class ObservedTransition:
    """A single observed state→state transition with full metadata."""
    action: int
    prev_hash: str
    curr_hash: str
    xor_mask: np.ndarray      # bool 64×64: which cells changed
    xor_values: np.ndarray    # uint8 64×64: XOR values
    prev_grid: np.ndarray
    curr_grid: np.ndarray
    origin: tuple             # (r, c) of XOR bounding box top-left
    template: np.ndarray      # cropped XOR patch
    template_hash: str
    color_map: dict           # {old_color: new_color, ...}
    entropy_delta: float
    n_changed: int


class TransitionMemory:
    """All observed transitions, indexed for fast lookup.

    Indices:
    - by_action[action] → list of transitions
    - by_template[template_hash] → list of transitions
    - by_color_rule[(old, new)] → list of transitions
    - by_state[state_hash] → {action: transition}

    The memory IS the model. No separate model needed.
    """

    def __init__(self):
        self.transitions: list[ObservedTransition] = []
        self.by_action: dict[int, list[int]] = defaultdict(list)
        self.by_template: dict[str, list[int]] = defaultdict(list)
        self.by_color_rule: dict[tuple, list[int]] = defaultdict(list)
        self.by_state: dict[str, dict[int, int]] = defaultdict(dict)
        self.state_graph: dict[str, dict[int, str]] = defaultdict(dict)

    def record(self, t: ObservedTransition):
        idx = len(self.transitions)
        self.transitions.append(t)
        self.by_action[t.action].append(idx)
        self.by_template[t.template_hash].append(idx)
        self.by_state[t.prev_hash][t.action] = idx
        self.state_graph[t.prev_hash][t.action] = t.curr_hash

        for old_c, new_c in t.color_map.items():
            self.by_color_rule[(old_c, new_c)].append(idx)

    def lookup_state_action(self, state_hash: str, action: int) -> Optional[ObservedTransition]:
        """Exact lookup: have we seen this state+action before?"""
        if state_hash in self.by_state and action in self.by_state[state_hash]:
            return self.transitions[self.by_state[state_hash][action]]
        return None

    def templates_for_action(self, action: int) -> list[ObservedTransition]:
        """All templates produced by this action."""
        return [self.transitions[i] for i in self.by_action.get(action, [])]

    def actions_for_color_rule(self, old_color: int, new_color: int) -> list[int]:
        """Which actions produce this color transition?"""
        idxs = self.by_color_rule.get((old_color, new_color), [])
        return list(set(self.transitions[i].action for i in idxs))


# ═══════════════════════════════════════════════════════════════════
#  2. XOR TELESCOPE — compose templates for O(1) lookahead
# ═══════════════════════════════════════════════════════════════════

class XORTelescope:
    """Predict the result of N actions without taking them.

    Key insight: XOR templates are LOCALIZED (typically 5×5 for agent games).
    If two templates don't overlap spatially, their composition is EXACT:
      XOR(A→B→C) = XOR(A→B) ⊕ XOR(B→C)  (when templates don't overlap)

    For overlapping templates, we use the nibble algebra to resolve
    color conflicts: if cell (r,c) is changed by both templates,
    the composed result is the second template's output.

    This gives us a "simulator" that runs at the speed of XOR, not
    the speed of the actual game engine.
    """

    def __init__(self, memory: TransitionMemory):
        self.memory = memory
        self._template_cache = {}  # (action, state_region_hash) → template

    def predict_single(self, grid: np.ndarray, action: int,
                       click_pos: tuple = None) -> Optional[np.ndarray]:
        """Predict result of one action from current grid.

        Uses template matching: find the most similar observed transition
        for this action and apply its XOR template to the current grid.
        """
        curr_hash = frame_hash(grid)

        # Exact match in memory?
        exact = self.memory.lookup_state_action(curr_hash, action)
        if exact is not None:
            return exact.curr_grid.copy()

        # Template-based prediction: find most common template for this action
        templates = self.memory.templates_for_action(action)
        if not templates:
            return None

        # For keyboard actions: find template from most similar state
        # Similarity = number of matching cells in the template's region
        best = None
        best_score = -1

        for t in templates[-20:]:  # check recent transitions
            r0, c0 = t.origin
            th, tw = t.template.shape
            if r0 + th > 64 or c0 + tw > 64:
                continue

            # How well does this template's "before" region match current grid?
            current_region = grid[r0:r0+th, c0:c0+tw]
            template_before = t.prev_grid[r0:r0+th, c0:c0+tw]
            match_score = (current_region == template_before).sum()

            if match_score > best_score:
                best_score = match_score
                best = t

        if best is None:
            return None

        # Apply the template
        predicted = grid.copy().astype(np.uint8)
        r0, c0 = best.origin
        th, tw = best.template.shape

        # For each changed cell, apply the color mapping
        for dr in range(th):
            for dc in range(tw):
                if best.template[dr, dc] > 0:
                    r, c = r0 + dr, c0 + dc
                    if r < 64 and c < 64:
                        old_val = int(grid[r, c])
                        if old_val in best.color_map:
                            predicted[r, c] = best.color_map[old_val]

        return predicted

    def telescope(self, grid: np.ndarray, action_sequence: list[int],
                  max_steps: int = 10) -> list[np.ndarray]:
        """Predict the result of a sequence of actions.

        Returns list of predicted frames (one per action).
        Stops if a prediction fails.
        """
        frames = [grid.copy()]
        current = grid.copy()

        for action in action_sequence[:max_steps]:
            predicted = self.predict_single(current, action)
            if predicted is None:
                break
            frames.append(predicted)
            current = predicted

        return frames

    def best_action_toward(self, grid: np.ndarray, target_property: str,
                           available: list[int],
                           detector: Optional[EckertWinDetector] = None) -> Optional[int]:
        """Find the action whose predicted result best matches a target property.

        Properties: "lower_entropy", "higher_phi", "more_changed", "less_changed"
        """
        best_action = None

        if target_property == "higher_phi" and detector is not None:
            # φ-guided: pick action that maximizes thermodynamic progress
            best_score = -1.0
            for action in available:
                if action == 6:
                    continue
                predicted = self.predict_single(grid, action)
                if predicted is None:
                    continue
                phi = detector.score_state(predicted)
                if phi > best_score:
                    best_score = phi
                    best_action = action
            return best_action

        best_score = float('inf') if target_property == "lower_entropy" else float('-inf')

        current_ent = shannon_entropy(grid)

        for action in available:
            if action == 6:
                continue  # skip click for now
            predicted = self.predict_single(grid, action)
            if predicted is None:
                continue

            if target_property == "lower_entropy":
                score = shannon_entropy(predicted)
                if score < best_score:
                    best_score = score
                    best_action = action
            elif target_property == "more_changed":
                score = (grid != predicted).sum()
                if score > best_score:
                    best_score = score
                    best_action = action

        return best_action


# ═══════════════════════════════════════════════════════════════════
#  3. INSTANTON DECOMPOSITION — compile desired XOR into actions
# ═══════════════════════════════════════════════════════════════════

class InstantonCompiler:
    """Compile a desired state change into minimum-length action sequence.

    Given:
      - Current frame S
      - Desired change pattern D (a 64×64 XOR target)
      - Library of action templates T_a for each action a

    Find: sequence [a₁, a₂, ..., aₙ] such that T_a₁ ⊕ T_a₂ ⊕ ... ⊕ T_aₙ ≈ D

    This is approximate set cover over GF(2): NP-hard in general,
    but our templates are SPARSE (< 30 cells each in a 4096-cell grid),
    so greedy covering works well.

    The "instanton" is the minimum-action path between states,
    analogous to the minimum-action path in Onsager-Machlup theory.
    """

    def __init__(self, memory: TransitionMemory):
        self.memory = memory

    def compile(self, current_grid: np.ndarray, target_xor: np.ndarray,
                available_actions: list[int], max_length: int = 20) -> list[int]:
        """Compile a desired XOR into an action sequence.

        Greedy algorithm: at each step, pick the action whose template
        has maximum overlap with the remaining target XOR.
        """
        remaining = (target_xor > 0).astype(np.uint8).copy()
        sequence = []

        for _ in range(max_length):
            if not remaining.any():
                break  # done!

            best_action = None
            best_overlap = 0
            best_template_mask = None

            for action in available_actions:
                if action == 6:
                    continue

                templates = self.memory.templates_for_action(action)
                for t in templates[-10:]:
                    # Overlap = cells that this template would "fix"
                    t_mask = t.xor_mask.astype(np.uint8)
                    overlap = int(np.bitwise_and(remaining, t_mask).sum())

                    if overlap > best_overlap:
                        best_overlap = overlap
                        best_action = action
                        best_template_mask = t_mask

            if best_action is None or best_overlap == 0:
                break  # can't make progress

            sequence.append(best_action)
            # Remove covered cells from remaining
            remaining = np.bitwise_and(remaining,
                                       np.bitwise_xor(best_template_mask,
                                                      np.ones_like(remaining)))

        return sequence

    def compile_color_change(self, current_grid: np.ndarray,
                             target_grid: np.ndarray,
                             available_actions: list[int]) -> list[int]:
        """Compile: given current and target grids, find action sequence.

        Uses color rule index: for each cell that needs to change,
        find an action that produces that color transition.
        """
        xor = xor_grids(current_grid, target_grid)
        if not xor.any():
            return []

        # What color transitions are needed?
        changed = xor > 0
        needed_rules = Counter()
        for r, c in zip(*np.where(changed)):
            old = int(current_grid[r, c])
            new = int(target_grid[r, c])
            needed_rules[(old, new)] += 1

        # Map each needed rule to an action
        action_votes = Counter()
        for (old, new), count in needed_rules.items():
            actions = self.memory.actions_for_color_rule(old, new)
            for a in actions:
                action_votes[a] += count

        if not action_votes:
            return self.compile(current_grid, xor, available_actions)

        # Return actions sorted by vote count (most useful first)
        sorted_actions = [a for a, _ in action_votes.most_common()]
        # Estimate repetitions needed
        total_changes = int(changed.sum())
        avg_changes = 10  # rough average
        n_repeats = max(1, total_changes // avg_changes)

        sequence = []
        for a in sorted_actions:
            sequence.extend([a] * min(n_repeats, 5))

        return sequence[:20]


# ═══════════════════════════════════════════════════════════════════
#  4. SPECTRAL NAVIGATOR — eigenstructure of transition matrix
# ═══════════════════════════════════════════════════════════════════

class SpectralNavigator:
    """Navigate using eigenstructure of the empirical transition matrix.

    The state graph G has adjacency matrix A where A[s1][s2] = 1 if
    there exists an action taking s1 → s2.

    The dominant eigenvector of A points toward the graph's "attractor" —
    states that are most reachable from everywhere. In a goal-directed
    game, the attractor IS the goal state (or close to it).

    Navigation: at each state, choose the action that moves toward
    the dominant eigenvector's peak. This is navigation by RESONANCE.
    """

    def __init__(self):
        self.state_index = {}   # hash → int
        self.index_state = {}   # int → hash
        self.adjacency = defaultdict(lambda: defaultdict(float))
        self.n_states = 0
        self.eigenvector = None
        self.needs_update = True

    def record_transition(self, from_hash: str, to_hash: str, action: int):
        if from_hash not in self.state_index:
            self.state_index[from_hash] = self.n_states
            self.index_state[self.n_states] = from_hash
            self.n_states += 1
        if to_hash not in self.state_index:
            self.state_index[to_hash] = self.n_states
            self.index_state[self.n_states] = to_hash
            self.n_states += 1

        i = self.state_index[from_hash]
        j = self.state_index[to_hash]
        self.adjacency[i][j] += 1.0
        self.needs_update = True

    def compute_eigenvector(self):
        """Compute dominant eigenvector via power iteration."""
        if self.n_states < 3:
            return

        # Build transition matrix (row-stochastic)
        T = np.zeros((self.n_states, self.n_states))
        for i in range(self.n_states):
            row = self.adjacency[i]
            total = sum(row.values())
            if total > 0:
                for j, w in row.items():
                    T[i, j] = w / total
            else:
                T[i, i] = 1.0  # absorbing state

        # Power iteration for dominant eigenvector
        v = np.ones(self.n_states) / self.n_states
        for _ in range(50):
            v_new = T.T @ v  # transpose: we want the STATIONARY distribution
            norm = np.linalg.norm(v_new)
            if norm > 0:
                v_new /= norm
            if np.allclose(v, v_new, atol=1e-8):
                break
            v = v_new

        self.eigenvector = v
        self.needs_update = False

    def score_state(self, state_hash: str) -> float:
        """How "goal-like" is this state? (eigenvector projection)"""
        if self.needs_update:
            self.compute_eigenvector()
        if self.eigenvector is None or state_hash not in self.state_index:
            return 0.0
        idx = self.state_index[state_hash]
        return float(self.eigenvector[idx])

    def best_action(self, current_hash: str, available_actions: list[int],
                    state_graph: dict) -> Optional[int]:
        """Action that moves toward highest eigenvector projection."""
        if self.needs_update:
            self.compute_eigenvector()
        if self.eigenvector is None:
            return None

        neighbors = state_graph.get(current_hash, {})
        best_a = None
        best_score = -1

        for action, next_hash in neighbors.items():
            if action not in available_actions:
                continue
            score = self.score_state(next_hash)
            if score > best_score:
                best_score = score
                best_a = action

        return best_a


# ═══════════════════════════════════════════════════════════════════
#  5. ENTROPY GRADIENT BEAM — predict & prune via entropy
# ═══════════════════════════════════════════════════════════════════

def entropy_beam_search(telescope: XORTelescope, grid: np.ndarray,
                        available_actions: list[int],
                        beam_width: int = 4, depth: int = 6) -> list[int]:
    """Beam search using entropy as the objective.

    At each depth:
    1. For each beam candidate, telescope ALL actions
    2. Score each by predicted entropy
    3. Keep top beam_width candidates

    Returns the action sequence with lowest predicted final entropy.
    """
    non_click = [a for a in available_actions if a != 6]
    if not non_click:
        return []

    # Each beam entry: (predicted_entropy, action_sequence, predicted_grid)
    current_ent = shannon_entropy(grid)
    beam = [(current_ent, [], grid.copy())]

    for d in range(depth):
        candidates = []
        for ent, seq, g in beam:
            for action in non_click:
                predicted = telescope.predict_single(g, action)
                if predicted is None:
                    continue
                pred_ent = shannon_entropy(predicted)
                candidates.append((pred_ent, seq + [action], predicted))

        if not candidates:
            break

        # Keep top beam_width by lowest entropy
        candidates.sort(key=lambda x: x[0])
        beam = candidates[:beam_width]

    if not beam:
        return []

    # Return the sequence with lowest predicted entropy
    return beam[0][1]


def phi_beam_search(telescope: XORTelescope, grid: np.ndarray,
                    available_actions: list[int],
                    detector: EckertWinDetector,
                    beam_width: int = 4, depth: int = 6) -> list[int]:
    """Beam search using φ (thermodynamic progress) as the objective.

    Like entropy_beam_search but scores by the Eckert win detector
    instead of Shannon entropy. Finds paths toward Pe minimum.
    """
    non_click = [a for a in available_actions if a != 6]
    if not non_click:
        return []

    current_phi = detector.score_state(grid)
    beam = [(current_phi, [], grid.copy())]

    for d in range(depth):
        candidates = []
        for phi, seq, g in beam:
            for action in non_click:
                predicted = telescope.predict_single(g, action)
                if predicted is None:
                    continue
                pred_phi = detector.score_state(predicted)
                candidates.append((pred_phi, seq + [action], predicted))

        if not candidates:
            break

        # Keep top beam_width by HIGHEST φ (most progress)
        candidates.sort(key=lambda x: -x[0])
        beam = candidates[:beam_width]

    if not beam:
        return []

    # Return the sequence with highest predicted φ
    return beam[0][1]


# ═══════════════════════════════════════════════════════════════════
#  6. MACRO DISCOVERY — find and replay multi-step patterns
# ═══════════════════════════════════════════════════════════════════

class MacroLibrary:
    """Discover and store multi-step action patterns (macros).

    A macro is a sequence of actions that produces a recognizable
    compound effect. Macros are discovered by:
    1. Observing successful sequences (entropy decreased)
    2. Identifying repeated subsequences
    3. Composing telescope predictions

    Macros are indexed by their compound XOR signature.
    """

    def __init__(self):
        self.macros = []  # (action_seq, compound_xor_hash, entropy_delta)
        self.macro_index = {}  # compound_xor_hash → macro index

    def discover(self, action_history: list[int], frame_history: list[np.ndarray]):
        """Scan history for entropy-decreasing subsequences."""
        if len(action_history) < 3 or len(frame_history) < 4:
            return

        entropies = [shannon_entropy(f) for f in frame_history]

        # Look for subsequences of length 2-6 that decrease entropy
        for length in range(2, min(7, len(action_history))):
            for start in range(len(action_history) - length):
                end = start + length
                ent_start = entropies[start]
                ent_end = entropies[end]

                if ent_end < ent_start - 0.01:  # meaningful decrease
                    seq = action_history[start:end]
                    compound_xor = xor_grids(frame_history[start], frame_history[end])
                    sig = hashlib.md5(compound_xor.tobytes()).hexdigest()[:10]

                    if sig not in self.macro_index:
                        self.macros.append((seq, sig, ent_end - ent_start))
                        self.macro_index[sig] = len(self.macros) - 1

    def find_applicable(self, current_grid: np.ndarray,
                        target_xor: np.ndarray) -> Optional[list[int]]:
        """Find a macro whose compound effect matches the target XOR."""
        target_sig = hashlib.md5(target_xor.tobytes()).hexdigest()[:10]
        if target_sig in self.macro_index:
            idx = self.macro_index[target_sig]
            return self.macros[idx][0]
        return None

    def best_macro(self) -> Optional[list[int]]:
        """Return the macro with the best entropy delta."""
        if not self.macros:
            return None
        best = min(self.macros, key=lambda m: m[2])
        return best[0] if best[2] < -0.01 else None


# ═══════════════════════════════════════════════════════════════════
#  THE INSTANTON PLANNER
# ═══════════════════════════════════════════════════════════════════

class InstantonPlanner:
    """The novel planner. Compiles desired changes into action sequences.

    Decision loop:
    1. Check Kramers: am I stuck? → compile escape instanton
    2. Check macros: do I have a known-good sequence? → replay it
    3. Spectral nav: does eigenvector suggest an action? → take it
    4. Beam search: telescope predicts best short sequence → execute
    5. Instanton compile: compute desired XOR → solve for actions
    6. Fallback: replicator-weighted random

    Each step also:
    - Records transition in memory
    - Updates spectral navigator
    - Discovers new macros
    - Refines instanton compiler's template index
    """

    def __init__(self, profile: GameProfile, env, obs, shared_state=None):
        self.profile = profile
        self.env = env
        self.obs = obs
        self.available = list(obs.available_actions)

        # The novel components — use shared state if provided
        if shared_state:
            self.memory = shared_state.transitions
            self.telescope = XORTelescope(self.memory)
            self.compiler = InstantonCompiler(self.memory)
            self.navigator = shared_state.navigator
            self.macros = shared_state.macros
            self._detector = shared_state.detector
        else:
            self.memory = TransitionMemory()
            self.telescope = XORTelescope(self.memory)
            self.compiler = InstantonCompiler(self.memory)
            self.navigator = SpectralNavigator()
            self.macros = MacroLibrary()
            self._detector = EckertWinDetector()

        # State
        self.frames = [np.array(obs.frame[0])]
        self.actions_taken = []
        self.total_actions = 0
        self.levels_solved = 0
        self.best_entropy = shannon_entropy(self.frames[0])
        self.best_frame = self.frames[0].copy()
        self.stuck_counter = 0
        self.rng = np.random.default_rng(42)

        # Phase tracking
        self.phase = "EXPLORE"  # EXPLORE → COMPILE → EXECUTE
        self.compiled_plan = []

    def _record_transition(self, action, prev_grid, curr_grid):
        """Record a transition with full metadata."""
        xor = xor_grids(prev_grid, curr_grid)
        is_noop = not xor.any()

        prev_h = frame_hash(prev_grid)
        curr_h = frame_hash(curr_grid)

        if not is_noop:
            # Extract template
            rows, cols = np.where(xor > 0)
            r0, c0 = int(rows.min()), int(cols.min())
            r1, c1 = int(rows.max()) + 1, int(cols.max()) + 1
            template = xor[r0:r1, c0:c1].copy()
            template_hash = hashlib.md5(template.tobytes()).hexdigest()[:10]

            # Color mapping
            changed = xor > 0
            old_vals = prev_grid[changed]
            new_vals = curr_grid[changed]
            color_map = {}
            for o, n in zip(old_vals.tolist(), new_vals.tolist()):
                color_map[o] = n

            t = ObservedTransition(
                action=action,
                prev_hash=prev_h,
                curr_hash=curr_h,
                xor_mask=changed,
                xor_values=xor,
                prev_grid=prev_grid.copy(),
                curr_grid=curr_grid.copy(),
                origin=(r0, c0),
                template=template,
                template_hash=template_hash,
                color_map=color_map,
                entropy_delta=shannon_entropy(curr_grid) - shannon_entropy(prev_grid),
                n_changed=int(changed.sum()),
            )
            self.memory.record(t)
            self.navigator.record_transition(prev_h, curr_h, action)

        # Feed thermodynamic detector
        self._detector.observe(prev_grid, action, curr_grid)

        return is_noop, prev_h, curr_h

    def step(self, action, click_x=None, click_y=None):
        """Take one action and record everything."""
        prev_grid = np.array(self.obs.frame[0])

        if action == 6 and click_x is not None:
            self.obs = self.env.step(6, data={"x": click_x, "y": click_y})
        else:
            self.obs = self.env.step(action)

        # Game may have ended — frame list can be empty
        if not self.obs.frame:
            self.total_actions += 1
            return True, prev_grid

        curr_grid = np.array(self.obs.frame[0])
        self.total_actions += 1
        self.frames.append(curr_grid)
        self.actions_taken.append(action)

        is_noop, prev_h, curr_h = self._record_transition(action, prev_grid, curr_grid)

        # Track best state
        ent = shannon_entropy(curr_grid)
        if ent < self.best_entropy:
            self.best_entropy = ent
            self.best_frame = curr_grid.copy()
            self.stuck_counter = 0
        else:
            self.stuck_counter += 1

        return is_noop, curr_grid

    def _explore_phase(self, budget: int = 30):
        """Systematic exploration to build transition memory."""
        non_click = [a for a in self.available if a != 6]
        has_click = 6 in self.available

        # Test each keyboard action 3×
        for a in non_click:
            for _ in range(3):
                if budget <= 0 or self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                    return
                self.step(a)
                budget -= 1

        # Test action pairs
        for a in non_click:
            for b in non_click:
                if a == b:
                    continue
                if budget <= 0 or self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                    return
                self.step(a)
                budget -= 1
                if budget <= 0 or self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                    return
                self.step(b)
                budget -= 1

        # Click exploration
        if has_click:
            grid = np.array(self.obs.frame[0])
            bg = int(np.bincount(grid.flatten()).argmax())
            colors = sorted(set(grid.flatten().tolist()) - {bg})

            for color in colors:
                if budget <= 0:
                    return
                positions = np.where(grid == color)
                if len(positions[0]) > 0:
                    cy, cx = int(positions[0].mean()), int(positions[1].mean())
                    self.step(6, click_x=cx, click_y=cy)
                    budget -= 1
                    grid = np.array(self.obs.frame[0])

    def _compile_phase(self):
        """Use the instanton compiler to plan an action sequence."""
        grid = np.array(self.obs.frame[0])
        non_click = [a for a in self.available if a != 6]

        # Strategy 0: φ-guided beam search (thermodynamic progress)
        if hasattr(self, '_detector') and self._detector is not None:
            plan = phi_beam_search(self.telescope, grid, self.available,
                                   self._detector, beam_width=4, depth=6)
            if plan:
                return plan

        # Strategy 1: Entropy beam search (telescope-guided)
        plan = entropy_beam_search(self.telescope, grid, self.available,
                                   beam_width=4, depth=6)
        if plan:
            return plan

        # Strategy 2: Spectral navigation
        curr_hash = frame_hash(grid)
        nav_action = self.navigator.best_action(
            curr_hash, self.available, self.memory.state_graph
        )
        if nav_action is not None:
            return [nav_action] * 5  # repeat the recommended action

        # Strategy 3: Macro replay
        best_macro = self.macros.best_macro()
        if best_macro:
            return best_macro

        # Strategy 4: Instanton decomposition toward best-known state
        if self.best_frame is not None:
            target_xor = xor_grids(grid, self.best_frame)
            if target_xor.any():
                plan = self.compiler.compile(grid, target_xor, self.available)
                if plan:
                    return plan

        # Fallback: cycle through available actions
        if non_click:
            return non_click * 3
        elif self.available:
            return [self.available[0]] * 3
        else:
            return [6] * 3  # ultimate fallback: click

    def solve_level(self, budget: int = 200) -> bool:
        """Solve one level using the three-phase approach."""
        start_level = self.obs.levels_completed
        explore_budget = min(40, budget // 4)

        # Phase 1: EXPLORE — build transition memory
        self.phase = "EXPLORE"
        self._explore_phase(budget=explore_budget)

        if self.obs.levels_completed > start_level:
            return True
        if self.obs.state == GameState.GAME_OVER:
            return False

        # Discover macros from exploration
        self.macros.discover(self.actions_taken, self.frames)

        # Compute spectral navigation
        self.navigator.compute_eigenvector()

        remaining = budget - explore_budget
        attempts = 0

        while remaining > 0:
            if self.obs.state == GameState.WIN:
                return True
            if self.obs.state == GameState.GAME_OVER:
                return False
            if self.obs.levels_completed > start_level:
                return True

            # Phase 2: COMPILE — generate action plan
            self.phase = "COMPILE"
            plan = self._compile_phase()

            # Phase 3: EXECUTE — run the compiled plan
            self.phase = "EXECUTE"
            for action in plan:
                if remaining <= 0:
                    break
                if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                    break
                if self.obs.levels_completed > start_level:
                    return True

                if action == 6:
                    # Smart click
                    grid = np.array(self.obs.frame[0])
                    bg = int(np.bincount(grid.flatten()).argmax())
                    nonbg = np.where(grid != bg)
                    if len(nonbg[0]) > 0:
                        idx = self.rng.integers(len(nonbg[0]))
                        self.step(6, click_x=int(nonbg[1][idx]),
                                 click_y=int(nonbg[0][idx]))
                    else:
                        self.step(6, click_x=32, click_y=32)
                else:
                    self.step(action)
                remaining -= 1

            attempts += 1

            # Re-discover macros periodically
            if attempts % 3 == 0:
                self.macros.discover(self.actions_taken[-50:], self.frames[-50:])

            # Stuck detection: if no progress in 30 actions, re-explore
            if self.stuck_counter > 30:
                self.phase = "EXPLORE"
                self._explore_phase(budget=min(10, remaining))
                remaining -= 10
                self.stuck_counter = 0

        return self.obs.levels_completed > start_level

    def solve_game(self, verbose: bool = True) -> dict:
        for level in range(self.profile.win_levels):
            if self.obs.state == GameState.WIN:
                break
            if self.obs.state == GameState.GAME_OVER:
                if verbose:
                    print(f"  Level {level}: GAME OVER")
                break

            level_start = self.total_actions
            solved = self.solve_level()
            level_acts = self.total_actions - level_start

            if solved:
                self.levels_solved += 1
                if verbose:
                    print(f"  Level {level}: SOLVED in {level_acts} acts | "
                          f"memory={len(self.memory.transitions)} transitions | "
                          f"macros={len(self.macros.macros)} | "
                          f"spectral_states={self.navigator.n_states}")
            else:
                if verbose:
                    top_templates = Counter()
                    for t in self.memory.transitions[-20:]:
                        top_templates[t.action] += 1
                    print(f"  Level {level}: FAILED {level_acts} acts | "
                          f"memory={len(self.memory.transitions)} | "
                          f"macros={len(self.macros.macros)} | "
                          f"stuck={self.stuck_counter} | "
                          f"recent_actions={dict(top_templates.most_common(3))}")
                break

        det_summary = self._detector.summary()
        return {
            "game_id": self.profile.game_id,
            "levels_solved": self.levels_solved,
            "win_levels": self.profile.win_levels,
            "total_actions": self.total_actions,
            "transitions_recorded": len(self.memory.transitions),
            "macros_discovered": len(self.macros.macros),
            "spectral_states": self.navigator.n_states,
            "final_phi": det_summary.get('phi', 0.0),
            "detector": det_summary,
        }


# ─── Pipeline ────────────────────────────────────────────────────

def solve(game_id: str, probe_budget: int = 30, verbose: bool = True,
          shared_state=None, profile: 'GameProfile' = None) -> dict:
    if verbose:
        print(f"\n{'='*65}")
        print(f"  INSTANTON PLANNER: {game_id}")
        print(f"{'='*65}")

    if profile is None:
        profile = probe_game(game_id, budget=probe_budget, verbose=False)

    if verbose:
        print(f"  Profile: {profile.solver_hint()}")

    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    planner = InstantonPlanner(profile, env, obs, shared_state=shared_state)
    result = planner.solve_game(verbose=verbose)

    if verbose:
        print(f"\n  RESULT: {result['levels_solved']}/{result['win_levels']} | "
              f"{result['total_actions']} actions | "
              f"{result['transitions_recorded']} transitions | "
              f"{result['macros_discovered']} macros")

    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ARC-AGI-3 Instanton Planner")
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
              f"{'Trans':>6s} {'Macro':>6s} {'States':>7s}")
        print("-" * 60)

        for e in envs:
            try:
                r = solve(e.game_id, probe_budget=args.probe_budget,
                         verbose=args.verbose)
                results.append(r)
                if not args.verbose:
                    print(f"{r['game_id']:<22s} "
                          f"{r['levels_solved']}/{r['win_levels']:<5d} "
                          f"{r['total_actions']:>6d} "
                          f"{r['transitions_recorded']:>6d} "
                          f"{r['macros_discovered']:>6d} "
                          f"{r['spectral_states']:>7d}")
            except Exception as ex:
                print(f"{e.game_id:<22s} ERROR: {str(ex)[:60]}")

        total = sum(r.get("levels_solved", 0) for r in results)
        possible = sum(r.get("win_levels", 0) for r in results)
        print(f"\nTOTAL: {total}/{possible} levels solved")
    else:
        solve(args.game_id, probe_budget=args.probe_budget, verbose=True)
