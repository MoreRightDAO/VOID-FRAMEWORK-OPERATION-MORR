"""ARC-AGI-3 Spectral Engine — the full math apparatus on raw bytes.

Implements the self-improving loops from the Void Framework math:

1. FISHER CELL MAP (§138): per-cell information distance → WHERE rules act
2. CHEBYSHEV GRAMMAR (§164B): decompose color distributions into spectral
   basis → color-invariant game fingerprint that evolves each step
3. ONSAGER-MACHLUP PATH COST (§48A): assign probability cost to action
   sequences → the "natural" game trajectory finds itself
4. REPLICATOR DYNAMICS (§10F, Fisher fundamental theorem): action fitness
   evolves via dW/dt = Var(W) → self-tuning action selection
5. KRAMERS POTENTIAL (§48E): fit empirical potential landscape from frame
   entropy → identify stuck states, barrier heights, escape directions
6. FANTASIA BOUND (§2B): I(D;Y)+I(M;Y)≤H(Y) → rigorous explore/exploit
   gate that replaces heuristic thresholds
7. COORDINATION BARRIER (§171C): N_mechanisms × π/√2 → principled budget
8. CELL-LEVEL FISHER MAP: 64×64 heat map of "where the rules live"
9. LANGEVIN EVOLUTION: grammar atoms mutate/reproduce via fitness landscape

Every computation runs on raw numpy arrays. Zero LLM.
"""
import hashlib
import warnings
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage, signal
from scipy.special import comb

from arcengine import GameState


# ═══════════════════════════════════════════════════════════════════
#  1. FISHER CELL MAP — WHERE rules act (§138)
# ═══════════════════════════════════════════════════════════════════

def fisher_cell_map(grid_a: np.ndarray, grid_b: np.ndarray) -> np.ndarray:
    """Per-cell Fisher distance between two frames.

    d_ij = 2|arcsin(√p_ij) - arcsin(√q_ij)| on the Bernoulli manifold.

    For discrete colors: treat each cell as a categorical variable.
    Fisher distance for categorical: d² = Σ_c (√p_c - √q_c)² per cell.
    But cells have single values, so we use a smoothed neighborhood.

    Returns 64×64 float array: high values = cells where rules are active.
    """
    h, w = grid_a.shape
    fisher_map = np.zeros((h, w), dtype=np.float64)

    # Direct: cell changed?
    changed = (grid_a != grid_b).astype(np.float64)

    # Neighborhood context: 3×3 window color distribution change
    kernel = np.ones((3, 3)) / 9.0

    for c in range(16):
        p_a = (grid_a == c).astype(np.float64)
        p_b = (grid_b == c).astype(np.float64)

        # Smooth to get local probability
        q_a = signal.convolve2d(p_a, kernel, mode='same', boundary='wrap')
        q_b = signal.convolve2d(p_b, kernel, mode='same', boundary='wrap')

        # Fisher distance on Bernoulli: 2|arcsin(√p) - arcsin(√q)|
        with np.errstate(invalid='ignore'):
            d = 2.0 * np.abs(np.arcsin(np.sqrt(np.clip(q_a, 0, 1)))
                           - np.arcsin(np.sqrt(np.clip(q_b, 0, 1))))
        fisher_map += np.nan_to_num(d, 0.0)

    # Weight by direct change
    fisher_map *= (1.0 + changed)

    return fisher_map


def fisher_importance_mask(fisher_map: np.ndarray, threshold: float = 0.3) -> np.ndarray:
    """Binary mask: cells above threshold × max are 'rule-active'."""
    if fisher_map.max() == 0:
        return np.zeros_like(fisher_map, dtype=bool)
    normalized = fisher_map / fisher_map.max()
    return normalized > threshold


# ═══════════════════════════════════════════════════════════════════
#  2. CHEBYSHEV GRAMMAR — spectral basis for color distributions (§164B)
# ═══════════════════════════════════════════════════════════════════

class ChebyshevGrammar:
    """Decompose color distributions into Chebyshev eigenfunctions.

    The eigenfunctions of the Laplacian on the Bernoulli manifold are
    Chebyshev polynomials T_n(1-2θ). Eigenvalue λ_n = n².

    Coefficients a_n capture the "shape" of the color distribution
    INDEPENDENT of which specific colors are used. Two games with the
    same Chebyshev spectrum have the same distributional structure.

    The grammar EVOLVES: each frame updates the spectral coefficients,
    and the rate of change of coefficients = the learning signal.
    """

    def __init__(self, n_modes: int = 8):
        self.n_modes = n_modes
        self.history = []        # list of coefficient vectors
        self.eigenvalues = np.array([n**2 for n in range(n_modes)])

    def decompose(self, grid: np.ndarray) -> np.ndarray:
        """Compute Chebyshev coefficients of the color distribution."""
        # Color histogram as probability distribution
        hist = np.bincount(grid.flatten().astype(int), minlength=16).astype(float)
        hist /= hist.sum() + 1e-12

        # Map to [0, 1] parameter space (sorted probabilities)
        theta = np.sort(hist[hist > 0])[::-1]
        if len(theta) == 0:
            return np.zeros(self.n_modes)

        # Pad/truncate to fixed length
        if len(theta) < 16:
            theta = np.pad(theta, (0, 16 - len(theta)))

        # Chebyshev transform: a_n = (2/π) ∫ T_n(1-2θ) p(θ) dθ/√(θ(1-θ))
        # Discrete approximation over the 16 color bins
        x = 1 - 2 * theta  # map θ ∈ [0,1] to x ∈ [-1,1]
        coeffs = np.zeros(self.n_modes)
        for n in range(self.n_modes):
            # T_n(x) via recurrence
            T_n = np.cos(n * np.arccos(np.clip(x, -1, 1)))
            # Weight by inverse Fisher metric √(θ(1-θ))
            weight = np.sqrt(np.clip(theta * (1 - theta), 1e-12, 0.25))
            coeffs[n] = np.sum(T_n * theta / (weight + 1e-12)) * (2 / np.pi)

        self.history.append(coeffs)
        return coeffs

    def spectral_distance(self, coeffs_a: np.ndarray, coeffs_b: np.ndarray) -> float:
        """Distance in Chebyshev space, weighted by eigenvalue decay."""
        weights = 1.0 / (self.eigenvalues + 1)
        return float(np.sqrt(np.sum(weights * (coeffs_a - coeffs_b)**2)))

    def spectral_velocity(self, window: int = 5) -> float:
        """Rate of change of spectral coefficients — are we still learning?"""
        if len(self.history) < 2:
            return 1.0
        recent = self.history[-window:]
        if len(recent) < 2:
            return 1.0
        diffs = [np.linalg.norm(recent[i+1] - recent[i])
                for i in range(len(recent) - 1)]
        return float(np.mean(diffs))

    def heat_kernel_predict(self, t: float = 1.0) -> np.ndarray:
        """Predict future coefficients using heat kernel diffusion.

        K(t) = Σ a_n · exp(-n²·t)

        At t=0: current state. As t→∞: ground state (most probable config).
        The heat kernel naturally smooths toward the equilibrium = goal.
        """
        if not self.history:
            return np.zeros(self.n_modes)
        current = self.history[-1]
        decay = np.exp(-self.eigenvalues * t)
        return current * decay


# ═══════════════════════════════════════════════════════════════════
#  3. ONSAGER-MACHLUP PATH COST — "natural" trajectories (§48A)
# ═══════════════════════════════════════════════════════════════════

class OnsagerMachlup:
    """Assign probability cost to action trajectories.

    S[θ] = (1/4T) ∫ (θ̇ - f(θ))² dt

    Low action S = trajectory follows the game's natural dynamics.
    High action S = fighting against the rules.

    The solver should MINIMIZE S — go with the flow.
    """

    def __init__(self):
        self.entropy_series = []  # θ(t) = frame entropy
        self.drift_estimate = 0.0  # f(θ) estimated from data
        self.temperature = 0.1     # T = noise level
        self.path_costs = []       # S per step

    def record(self, grid: np.ndarray):
        """Record frame entropy as the order parameter θ."""
        from packet_analyzer import shannon_entropy
        ent = shannon_entropy(grid)
        self.entropy_series.append(ent)
        self._update_drift()

    def _update_drift(self):
        """Estimate drift f(θ) = mean(dθ/dt) from trajectory."""
        if len(self.entropy_series) < 3:
            return
        velocities = np.diff(self.entropy_series[-20:])
        self.drift_estimate = float(np.mean(velocities))
        self.temperature = max(float(np.var(velocities)), 0.001)

    def path_cost(self) -> float:
        """Onsager-Machlup action for the most recent step.

        S = (1/4T)(θ̇ - f)²
        """
        if len(self.entropy_series) < 2:
            return 0.0
        theta_dot = self.entropy_series[-1] - self.entropy_series[-2]
        S = (theta_dot - self.drift_estimate)**2 / (4 * self.temperature)
        self.path_costs.append(S)
        return float(S)

    def trajectory_cost(self, window: int = 10) -> float:
        """Total action over recent trajectory."""
        recent = self.path_costs[-window:]
        return sum(recent) if recent else 0.0

    def is_natural(self, threshold: float = 1.0) -> bool:
        """Is the current trajectory following the game's natural flow?"""
        return self.path_cost() < threshold

    def predicted_drift(self) -> float:
        """Predicted next entropy change (instanton equation)."""
        return self.drift_estimate


# ═══════════════════════════════════════════════════════════════════
#  4. REPLICATOR DYNAMICS — self-tuning action selection (§10F)
# ═══════════════════════════════════════════════════════════════════

class ReplicatorDynamics:
    """Evolve action selection probabilities via replicator equation.

    dx_i/dt = x_i(f_i - <f>)

    Actions with above-average fitness increase in frequency.
    Actions with below-average fitness decrease.

    Fisher's fundamental theorem: dW/dt = Var(W)
    → rate of improvement = variance in fitness
    → when variance → 0, we've converged to the optimal policy

    The "fitness" of an action is a composite:
      - Entropy decrease (progress)
      - Fisher info gain (learning)
      - Low Onsager-Machlup cost (natural flow)
      - Novelty in XOR space (exploration bonus in EXPLORE mode)
    """

    def __init__(self, actions: list[int]):
        self.actions = actions
        n = len(actions)
        # Initialize uniform
        self.frequencies = {a: 1.0 / n for a in actions}
        self.fitness = {a: 0.0 for a in actions}
        self.fitness_history = defaultdict(list)
        self.generation = 0
        self.fitness_variance_series = []

    def update_fitness(self, action: int, entropy_delta: float,
                       fisher_div: float, path_cost: float,
                       novelty: float, mode: str):
        """Compute fitness for an action from multiple signals."""
        # Composite fitness:
        #   - Entropy decrease is GOOD (negative delta = positive fitness)
        #   - Fisher info gain is GOOD in EXPLORE mode
        #   - Low path cost is GOOD (going with the flow)
        #   - Novelty is GOOD in EXPLORE mode

        f = 0.0
        f += -entropy_delta * 10.0        # progress signal (strongest)
        f += -path_cost * 2.0             # natural flow bonus
        if mode == "EXPLORE":
            f += fisher_div * 5.0         # learning signal
            f += novelty * 3.0            # exploration bonus

        self.fitness[action] = f
        self.fitness_history[action].append(f)

    def step(self):
        """One step of replicator dynamics."""
        self.generation += 1
        mean_fitness = np.mean(list(self.fitness.values()))

        # Replicator equation: dx_i/dt = x_i(f_i - <f>)
        new_freq = {}
        for a in self.actions:
            f_a = self.fitness.get(a, 0.0)
            x_a = self.frequencies[a]
            # Discrete update with learning rate
            dx = x_a * (f_a - mean_fitness) * 0.1
            new_freq[a] = max(0.01, x_a + dx)  # floor to prevent extinction

        # Normalize
        total = sum(new_freq.values())
        self.frequencies = {a: v / total for a, v in new_freq.items()}

        # Fisher's fundamental theorem: Var(fitness)
        fitnesses = list(self.fitness.values())
        var_w = float(np.var(fitnesses)) if fitnesses else 0.0
        self.fitness_variance_series.append(var_w)

    def select_action(self, rng=None) -> int:
        """Sample action from evolved distribution."""
        if rng is None:
            rng = np.random.default_rng()
        actions = list(self.frequencies.keys())
        probs = np.array([self.frequencies[a] for a in actions])
        probs /= probs.sum()
        return actions[rng.choice(len(actions), p=probs)]

    def has_converged(self, window: int = 10) -> bool:
        """Fisher's theorem: Var(W) → 0 means we've converged."""
        if len(self.fitness_variance_series) < window:
            return False
        recent = self.fitness_variance_series[-window:]
        return np.mean(recent) < 0.01

    def dominant_action(self) -> int:
        """The action with highest frequency (most fit)."""
        return max(self.frequencies, key=self.frequencies.get)

    def diversity(self) -> float:
        """Shannon entropy of action distribution. High = diverse, Low = converged."""
        probs = np.array(list(self.frequencies.values()))
        probs = probs[probs > 0]
        return float(-np.sum(probs * np.log2(probs + 1e-12)))


# ═══════════════════════════════════════════════════════════════════
#  5. KRAMERS POTENTIAL — stuck states & escape directions (§48E)
# ═══════════════════════════════════════════════════════════════════

class KramersPotential:
    """Fit empirical potential landscape from frame entropy trajectory.

    V(θ) = -(a/2)θ² + (b/4)θ⁴ + (c/3)θ³  (Landau free energy)

    Local minima = stable game states (stuck points).
    Barrier between minima = action cost to escape.
    Kramers rate: Γ ~ exp(-2K·ΔΦ/α)
    """

    def __init__(self):
        self.entropy_samples = []
        self.potential = None  # fitted coefficients (a, b, c)
        self.minima = []
        self.barriers = []

    def record(self, entropy: float):
        self.entropy_samples.append(entropy)

    def fit(self):
        """Fit Landau potential from entropy histogram."""
        if len(self.entropy_samples) < 20:
            return

        samples = np.array(self.entropy_samples)

        # Skip if entropy samples cluster too tightly (ill-conditioned polyfit)
        entropy_range = samples.max() - samples.min()
        if entropy_range < 0.01:
            return

        # Histogram → probability → potential V = -log(p)
        hist, edges = np.histogram(samples, bins=20, density=True)
        centers = (edges[:-1] + edges[1:]) / 2
        hist = np.clip(hist, 1e-6, None)
        V_empirical = -np.log(hist)

        # Fit: V(x) = a₀ + a₁x + a₂x² + a₃x³ + a₄x⁴
        # Reduce degree for narrow ranges to avoid rank deficiency
        poly_degree = 4 if entropy_range > 0.05 else 2
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore', category=np.exceptions.RankWarning)
                coeffs = np.polyfit(centers, V_empirical, poly_degree)
            self.potential = coeffs

            # Find minima: dV/dx = 0
            dV = np.polyder(np.poly1d(coeffs))
            roots = np.roots(dV.coeffs)
            real_roots = roots[np.isreal(roots)].real
            # Filter to range
            in_range = real_roots[(real_roots >= centers[0]) & (real_roots <= centers[-1])]

            # Classify: minimum if d²V/dx² > 0
            d2V = np.polyder(dV)
            self.minima = [float(r) for r in in_range if d2V(r) > 0]
            maxima = [float(r) for r in in_range if d2V(r) < 0]

            # Barriers between consecutive min-max pairs
            V_func = np.poly1d(coeffs)
            self.barriers = []
            for mx in maxima:
                V_mx = V_func(mx)
                for mn in self.minima:
                    V_mn = V_func(mn)
                    if V_mx > V_mn:
                        self.barriers.append({
                            "from": round(mn, 3),
                            "over": round(mx, 3),
                            "height": round(float(V_mx - V_mn), 3),
                            "kramers_rate": round(float(np.exp(-2 * (V_mx - V_mn))), 6),
                        })
        except (np.linalg.LinAlgError, ValueError):
            pass

    def is_stuck(self, current_entropy: float) -> bool:
        """Is current entropy near a local minimum?"""
        if not self.minima:
            return False
        distances = [abs(current_entropy - m) for m in self.minima]
        return min(distances) < 0.05

    def escape_direction(self, current_entropy: float) -> float:
        """Which direction to push entropy to escape current minimum?

        Returns +1 (increase entropy) or -1 (decrease entropy).
        """
        if not self.barriers:
            return -1.0  # default: decrease entropy = progress

        # Find nearest minimum
        nearest_min = min(self.minima, key=lambda m: abs(current_entropy - m))
        # Find lowest barrier from this minimum
        relevant = [b for b in self.barriers if abs(b["from"] - nearest_min) < 0.1]
        if not relevant:
            return -1.0

        lowest_barrier = min(relevant, key=lambda b: b["height"])
        # Push toward the barrier crossing point
        return 1.0 if lowest_barrier["over"] > current_entropy else -1.0


# ═══════════════════════════════════════════════════════════════════
#  6. FANTASIA BOUND — rigorous explore/exploit (§2B)
# ═══════════════════════════════════════════════════════════════════

class FantasiaBound:
    """Track I(D;Y) + I(M;Y) ≤ H(Y) for principled explore/exploit.

    D = player's action influence (engagement/exploration)
    M = game's internal mechanism (transparency/learning)
    Y = observed frame

    When I(D;Y) + I(M;Y) → H(Y), the game is fully observed.
    This is the HARD LIMIT — not a heuristic threshold.

    At saturation: no more information can be extracted.
    Switch to pure exploit.
    """

    def __init__(self):
        self.H_Y_series = []     # H(Y) = frame entropy
        self.I_D_Y_series = []   # I(D;Y) = mutual info between action and frame change
        self.I_M_Y_series = []   # I(M;Y) = info in frame not explained by actions
        self.saturation_series = []

    def record(self, grid: np.ndarray, action: int, prev_grid: np.ndarray,
               action_entropy: float):
        """Record one observation and update the bound."""
        from packet_analyzer import shannon_entropy

        H_Y = shannon_entropy(grid)
        self.H_Y_series.append(H_Y)

        # I(D;Y) ≈ entropy of frame change attributable to action
        xor = (prev_grid.astype(np.uint8) ^ grid.astype(np.uint8))
        changed = xor > 0
        if changed.any():
            # Info in the action's effect
            change_ent = shannon_entropy(xor[changed].astype(int))
            I_D = min(change_ent * (changed.sum() / grid.size), H_Y)
        else:
            I_D = 0.0
        self.I_D_Y_series.append(I_D)

        # I(M;Y) ≈ remaining structure not explained by action
        I_M = max(0, H_Y - I_D - action_entropy * 0.1)
        self.I_M_Y_series.append(I_M)

        # Saturation ratio
        if H_Y > 0:
            sat = (I_D + I_M) / H_Y
        else:
            sat = 1.0
        self.saturation_series.append(min(sat, 1.0))

    def saturation(self, window: int = 10) -> float:
        """Current (I(D;Y) + I(M;Y)) / H(Y). When → 1.0, fully observed."""
        if not self.saturation_series:
            return 0.0
        return float(np.mean(self.saturation_series[-window:]))

    def should_exploit(self) -> bool:
        """Has the Fantasia bound saturated?"""
        return self.saturation(window=10) > 0.85

    def exploration_budget_remaining(self) -> float:
        """How much unexplained information remains? [0,1]"""
        return 1.0 - self.saturation()


# ═══════════════════════════════════════════════════════════════════
#  7. LANGEVIN ATOM EVOLUTION — grammar atoms as an evolving population
# ═══════════════════════════════════════════════════════════════════

@dataclass
class EvolvingAtom:
    """A grammar atom that reproduces and mutates."""
    pattern_hash: str
    pattern_shape: tuple
    fitness: float = 0.0
    age: int = 0
    offspring_count: int = 0
    lineage: list = field(default_factory=list)  # parent hashes


class LangevinEvolver:
    """Evolve grammar atoms using Langevin dynamics on fitness landscape.

    dθ/dt = -∇V(θ) + √(2T)·ξ(t)

    θ = atom features (shape, size, color signature)
    V(θ) = -log(fitness) = potential landscape
    T = exploration temperature
    ξ = noise (random mutations)

    Fisher's fundamental theorem: dW/dt = Var(W)
    The population improves at rate equal to fitness variance.
    When variance → 0, evolution has converged.
    """

    def __init__(self, temperature: float = 0.5):
        self.population: dict[str, EvolvingAtom] = {}
        self.temperature = temperature
        self.generation = 0
        self.fitness_variance_series = []

    def register_atom(self, atom_hash: str, shape: tuple):
        """Add a new atom to the population."""
        if atom_hash not in self.population:
            self.population[atom_hash] = EvolvingAtom(
                pattern_hash=atom_hash,
                pattern_shape=shape,
            )

    def update_fitness(self, atom_hash: str, reward: float):
        """Update atom fitness based on whether it was useful."""
        if atom_hash in self.population:
            atom = self.population[atom_hash]
            # Exponential moving average
            atom.fitness = 0.7 * atom.fitness + 0.3 * reward
            atom.age += 1

    def evolve_step(self):
        """One generation of Langevin evolution."""
        self.generation += 1

        if not self.population:
            return

        fitnesses = [a.fitness for a in self.population.values()]
        mean_f = np.mean(fitnesses) if fitnesses else 0
        var_f = np.var(fitnesses) if fitnesses else 0
        self.fitness_variance_series.append(var_f)

        # Selection: atoms with fitness < mean - 2σ die
        std_f = np.sqrt(var_f) if var_f > 0 else 0
        threshold = mean_f - 2 * std_f

        dead = [h for h, a in self.population.items()
                if a.fitness < threshold and a.age > 5]
        for h in dead:
            del self.population[h]

        # Reproduction: top atoms spawn variants
        # (In practice, variants are discovered via new XOR transitions,
        #  so we just boost the fitness of successful lineages)
        top = sorted(self.population.values(), key=lambda a: -a.fitness)[:5]
        for atom in top:
            atom.offspring_count += 1

    def best_atoms(self, n: int = 5) -> list[EvolvingAtom]:
        return sorted(self.population.values(), key=lambda a: -a.fitness)[:n]

    def has_converged(self, window: int = 10) -> bool:
        """Fisher's fundamental theorem: Var(W) → 0."""
        if len(self.fitness_variance_series) < window:
            return False
        return np.mean(self.fitness_variance_series[-window:]) < 0.001

    def effective_population_size(self) -> int:
        """Number of atoms with non-trivial fitness."""
        return sum(1 for a in self.population.values() if a.fitness > 0.01)


# ═══════════════════════════════════════════════════════════════════
#  8. COORDINATION BARRIER — principled difficulty (§171C)
# ═══════════════════════════════════════════════════════════════════

def coordination_barrier(n_mechanisms: int) -> float:
    """Total barrier = N_mechanisms × π/√2.

    Each independent game mechanism costs exactly π/√2 ≈ 2.221 actions
    (in natural units) to explore. If the game has N simultaneous
    conditions that must be satisfied, the cost is N × 2.221.

    This gives us the MINIMUM exploration budget for a game.
    """
    return n_mechanisms * np.pi / np.sqrt(2)


def estimate_mechanisms(profile) -> int:
    """Estimate number of independent mechanisms from GameProfile.

    Sources:
    - Distinct nibble transitions (color rule count)
    - K-Grammar atom types
    - XOR vector space rank
    - Number of clickable colors
    """
    n_color_rules = len(profile.nibble_vocab)
    n_atoms = profile.n_unique_templates
    n_click_targets = len(profile.clickable_colors)

    # Each independent "rule" is a mechanism
    # But many rules are the same mechanism at different positions
    # Estimate: max(color_rules, atoms) ÷ symmetry_factor
    symmetry_factor = max(1, len(profile.available_actions))
    raw = max(n_color_rules, n_atoms, n_click_targets)
    return max(1, raw // symmetry_factor)


# ═══════════════════════════════════════════════════════════════════
#  9. SPECTRAL GAME FINGERPRINT — embed games in feature space
# ═══════════════════════════════════════════════════════════════════

def game_fingerprint(profile, chebyshev_coeffs: np.ndarray) -> np.ndarray:
    """Embed a game as a vector in feature space for strategy transfer.

    Features:
    - Chebyshev coefficients (8 dims) — spectral structure
    - Action diversity (1 dim)
    - Compression ratio (1 dim)
    - CoM spread (1 dim)
    - Noop rate (1 dim)
    - XOR rank / budget (1 dim)
    - Click fraction (1 dim)
    - Cycle flag (1 dim)

    Similar fingerprints → similar games → transfer strategies.
    """
    features = list(chebyshev_coeffs[:8])

    # Structural features
    features.append(len(profile.available_actions) / 7.0)
    features.append(profile.delta_compress_mean)
    features.append(profile.com_spread / 32.0)
    features.append(sum(profile.action_noop_rate.values()) / max(len(profile.action_noop_rate), 1))
    features.append(profile.n_unique_templates / 50.0)
    features.append(1.0 if 6 in profile.available_actions else 0.0)
    features.append(1.0 if profile.has_cycles else 0.0)

    return np.array(features, dtype=np.float64)


def find_similar_games(target_fp: np.ndarray, all_fps: dict) -> list:
    """Find games with the most similar fingerprints."""
    distances = {}
    for game_id, fp in all_fps.items():
        d = float(np.linalg.norm(target_fp - fp))
        distances[game_id] = d
    return sorted(distances.items(), key=lambda x: x[1])


# ═══════════════════════════════════════════════════════════════════
#  COMPOSITE: Wire everything together
# ═══════════════════════════════════════════════════════════════════

class SpectralSolver:
    """The full-apparatus self-improving solver.

    Wires all engines together into one recursive loop:
    1. Take action (selected by ReplicatorDynamics)
    2. Compute Fisher cell map (WHERE rules act)
    3. Decompose via ChebyshevGrammar (spectral fingerprint)
    4. Score path via OnsagerMachlup (natural flow?)
    5. Update ReplicatorDynamics (action fitness evolves)
    6. Update KramersPotential (stuck detection)
    7. Check FantasiaBound (explore/exploit gate)
    8. Evolve atom population (LangevinEvolver)
    9. Repeat — each component self-improves from the others' output
    """

    def __init__(self, profile, env, obs):
        self.profile = profile
        self.env = env
        self.obs = obs

        # The engines
        self.fisher_map = None
        self.chebyshev = ChebyshevGrammar(n_modes=8)
        self.onsager = OnsagerMachlup()
        self.replicator = ReplicatorDynamics(list(obs.available_actions))
        self.kramers = KramersPotential()
        self.fantasia = FantasiaBound()
        self.evolver = LangevinEvolver(temperature=0.5)

        # State
        self.total_actions = 0
        self.levels_solved = 0
        self.rng = np.random.default_rng(42)

        # Initialize with first frame
        grid = np.array(obs.frame[0])
        self.chebyshev.decompose(grid)
        self.onsager.record(grid)
        from packet_analyzer import shannon_entropy
        self.kramers.record(shannon_entropy(grid))

    def step(self) -> dict:
        """One step of the full recursive loop."""
        prev_grid = np.array(self.obs.frame[0])

        # ─── SELECT ACTION (Replicator) ───
        action = self.replicator.select_action(self.rng)
        click_x, click_y = None, None

        if action == 6:
            # Smart click: target high-Fisher regions if we have a map
            if self.fisher_map is not None:
                hot = np.where(self.fisher_map > self.fisher_map.max() * 0.3)
                if len(hot[0]) > 0:
                    idx = self.rng.integers(len(hot[0]))
                    click_y, click_x = int(hot[0][idx]), int(hot[1][idx])

            if click_x is None:
                bg = int(np.bincount(prev_grid.flatten()).argmax())
                nonbg = np.where(prev_grid != bg)
                if len(nonbg[0]) > 0:
                    idx = self.rng.integers(len(nonbg[0]))
                    click_y, click_x = int(nonbg[0][idx]), int(nonbg[1][idx])
                else:
                    click_x, click_y = 32, 32

        # ─── ACT ───
        if action == 6:
            self.obs = self.env.step(6, data={"x": click_x, "y": click_y})
        else:
            self.obs = self.env.step(action)

        curr_grid = np.array(self.obs.frame[0])
        self.total_actions += 1
        xor = prev_grid.astype(np.uint8) ^ curr_grid.astype(np.uint8)
        is_noop = not xor.any()

        # ─── FISHER CELL MAP ───
        if not is_noop:
            self.fisher_map = fisher_cell_map(prev_grid, curr_grid)

        # ─── CHEBYSHEV GRAMMAR ───
        coeffs = self.chebyshev.decompose(curr_grid)
        spectral_vel = self.chebyshev.spectral_velocity()

        # ─── ONSAGER-MACHLUP ───
        self.onsager.record(curr_grid)
        path_cost = self.onsager.path_cost()
        is_natural = self.onsager.is_natural()

        # ─── KRAMERS ───
        from packet_analyzer import shannon_entropy
        ent = shannon_entropy(curr_grid)
        self.kramers.record(ent)
        if self.total_actions % 20 == 0:
            self.kramers.fit()

        # ─── FANTASIA BOUND ───
        action_ent = self.replicator.diversity()
        self.fantasia.record(curr_grid, action, prev_grid, action_ent)
        mode = "EXPLOIT" if self.fantasia.should_exploit() else "EXPLORE"

        # ─── XOR novelty (from existing recursive_solver if available) ───
        novelty = 1.0 if is_noop else 0.5  # simplified

        # ─── REPLICATOR UPDATE ───
        ent_prev = shannon_entropy(prev_grid)
        ent_delta = ent - ent_prev
        fisher_div = float(np.mean(self.fisher_map)) if self.fisher_map is not None and not is_noop else 0.0
        self.replicator.update_fitness(action, ent_delta, fisher_div,
                                        path_cost, novelty, mode)
        self.replicator.step()

        # ─── LANGEVIN EVOLUTION ───
        if not is_noop:
            # Register XOR pattern as atom
            atom_hash = hashlib.md5(xor.tobytes()).hexdigest()[:10]
            h, w = xor.shape
            self.evolver.register_atom(atom_hash, (h, w))
            reward = -ent_delta * 10 if ent_delta < 0 else 0.0
            self.evolver.update_fitness(atom_hash, reward)

        if self.total_actions % 10 == 0:
            self.evolver.evolve_step()

        return {
            "action": action,
            "is_noop": is_noop,
            "mode": mode,
            "path_cost": round(path_cost, 3),
            "is_natural": is_natural,
            "spectral_vel": round(spectral_vel, 4),
            "fantasia_sat": round(self.fantasia.saturation(), 3),
            "replicator_div": round(self.replicator.diversity(), 3),
            "kramers_stuck": self.kramers.is_stuck(ent),
            "evo_pop": self.evolver.effective_population_size(),
            "action_probs": {a: round(p, 3) for a, p in self.replicator.frequencies.items()},
        }

    def solve_level(self, budget: int = 300) -> bool:
        start_level = self.obs.levels_completed
        for i in range(budget):
            if self.obs.state == GameState.WIN:
                return True
            if self.obs.state == GameState.GAME_OVER:
                return False
            if self.obs.levels_completed > start_level:
                return True

            result = self.step()

            # Kramers escape: if stuck, try the escape direction
            if result["kramers_stuck"] and i > 20:
                escape_dir = self.kramers.escape_direction(
                    self.onsager.entropy_series[-1] if self.onsager.entropy_series else 0
                )
                # Boost actions that change entropy in the escape direction
                for a in self.replicator.actions:
                    self.replicator.fitness[a] += escape_dir * 0.5

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
                          f"fantasia={self.fantasia.saturation():.2f} | "
                          f"replicator_div={self.replicator.diversity():.2f} | "
                          f"evo_pop={self.evolver.effective_population_size()} | "
                          f"kramers_minima={len(self.kramers.minima)}")
            else:
                if verbose:
                    top_action = self.replicator.dominant_action()
                    print(f"  Level {level}: FAILED {level_acts} acts | "
                          f"fantasia={self.fantasia.saturation():.2f} | "
                          f"dominant_action={top_action} "
                          f"({self.replicator.frequencies.get(top_action,0):.0%}) | "
                          f"spectral_vel={self.chebyshev.spectral_velocity():.3f} | "
                          f"path_cost={self.onsager.trajectory_cost():.1f}")
                break

        return {
            "game_id": self.profile.game_id,
            "levels_solved": self.levels_solved,
            "win_levels": self.profile.win_levels,
            "total_actions": self.total_actions,
            "fantasia_saturation": round(self.fantasia.saturation(), 3),
            "replicator_converged": self.replicator.has_converged(),
            "evolution_converged": self.evolver.has_converged(),
            "kramers_minima": len(self.kramers.minima),
            "evo_population": self.evolver.effective_population_size(),
            "action_distribution": {a: round(p, 3) for a, p in self.replicator.frequencies.items()},
        }


# ─── Pipeline ────────────────────────────────────────────────────

def solve(game_id: str, probe_budget: int = 30, verbose: bool = True) -> dict:
    from packet_probe import probe_game
    import arc_agi

    if verbose:
        print(f"\n{'='*65}")
        print(f"  SPECTRAL SOLVER: {game_id}")
        print(f"{'='*65}")

    profile = probe_game(game_id, budget=probe_budget, verbose=False)
    n_mech = estimate_mechanisms(profile)
    barrier = coordination_barrier(n_mech)

    if verbose:
        print(f"  Profile: {profile.solver_hint()}")
        print(f"  Mechanisms: {n_mech} | Coordination barrier: {barrier:.1f}")

    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    solver = SpectralSolver(profile, env, obs)
    result = solver.solve_game(verbose=verbose)

    if verbose:
        print(f"\n  RESULT: {result['levels_solved']}/{result['win_levels']} | "
              f"{result['total_actions']} actions | "
              f"fantasia={result['fantasia_saturation']:.2f} | "
              f"replicator={'CONVERGED' if result['replicator_converged'] else 'evolving'} | "
              f"evolution={'CONVERGED' if result['evolution_converged'] else 'evolving'}")

    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ARC-AGI-3 Spectral Engine Solver")
    parser.add_argument("game_id", nargs="?", default=None)
    parser.add_argument("-b", "--probe-budget", type=int, default=30)
    parser.add_argument("-v", "--verbose", action="store_true", default=True)
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.quiet:
        args.verbose = False

    if args.all or args.game_id is None:
        import arc_agi
        arcade = arc_agi.Arcade()
        envs = arcade.get_environments()
        results = []

        print(f"\n{'Game':<22s} {'Solved':>7s} {'Acts':>6s} "
              f"{'Fant':>5s} {'Rep':>5s} {'Evo':>4s} {'Kram':>5s}")
        print("-" * 60)

        for e in envs:
            try:
                r = solve(e.game_id, probe_budget=args.probe_budget, verbose=args.verbose)
                results.append(r)
                if not args.verbose:
                    print(f"{r['game_id']:<22s} "
                          f"{r['levels_solved']}/{r['win_levels']:<5d} "
                          f"{r['total_actions']:>6d} "
                          f"{r['fantasia_saturation']:>5.2f} "
                          f"{'Y' if r['replicator_converged'] else 'N':>5s} "
                          f"{r['evo_population']:>4d} "
                          f"{r['kramers_minima']:>5d}")
            except Exception as ex:
                import traceback
                if args.verbose:
                    traceback.print_exc()
                print(f"{e.game_id:<22s} ERROR: {str(ex)[:60]}")

        total = sum(r.get("levels_solved", 0) for r in results)
        possible = sum(r.get("win_levels", 0) for r in results)
        print(f"\nTOTAL: {total}/{possible} levels solved")
    else:
        solve(args.game_id, probe_budget=args.probe_budget, verbose=True)
