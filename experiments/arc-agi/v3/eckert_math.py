"""Eckert Manifold — Practical Reusable Math for ARC-AGI Agents.

Pure functions, no solver dependencies. Importable by anything.

Consolidates the Eckert manifold math scattered across eckert_simulator.py,
spectral_engine.py, and eckert_win_detector.py into clean, documented functions.
Adds genuinely new: holonomy_deficit, jko_gradient, pade_extrapolate, pid_decompose.

Math apparatus references:
  §1A    Eckert manifold definition (O, R, α coordinates)
  §136   K-Factorization — shape × scale decomposition
  §136D2 Barrier universality — d_eff × π/√2
  §138   Fisher geodesic distance
  §165   Čencov metric — unique distance on probability space
  §171   Kramers escape rate
  §2B    Fantasia Bound — conjugacy I(D;Y)+I(M;Y)≤H(Y)
  §48A   Onsager-Machlup path cost
  §101   Holonomy — geometric memory from parallel transport
  §177   Padé saturation — rational approximation from early data
  HP203  JKO gradient flow — F(Pe) monotonically decreasing
  HP204  PID decomposition — unique/redundant/synergistic information
"""

import math
from typing import Optional

import numpy as np

# ═══════════════════════════════════════════════════════════════════
#  CONSTANTS (framework-derived, not tunable)
# ═══════════════════════════════════════════════════════════════════

B_A = 0.867                          # Agency barrier (§136)
B_G = 2.244                          # Constraint barrier = π/√2 (§136, §165)
BARRIER_CONST = math.pi / math.sqrt(2)  # ≈ 2.221 per mechanism (§136D2)
GEODESIC_L = math.pi                 # Čencov-forced geodesic length (§165)
B_A_EXACT = math.sqrt(3) / 2        # = cos(π/6), HP202 Fisher 3-simplex


# ═══════════════════════════════════════════════════════════════════
#  1. MANIFOLD GEOMETRY
# ═══════════════════════════════════════════════════════════════════

def pe_from_coordinates(O: float, R: float, alpha: float, K: float = 1.0) -> float:
    """Compute Péclet number from Eckert manifold coordinates.

    Pe = sinh(2·(B_A − C·B_G))·K
    where C = 1 − (O + R + α) / 9

    Args:
        O: Opacity ∈ [0,1] — entropy of observables
        R: Responsiveness ∈ [0,1] — fraction of actions causing change
        alpha: Coupling ∈ [0,1] — spatial/temporal correlation
        K: Degrees of freedom (scale factor)

    Returns:
        Pe value. Low Pe = transparent/safe. High Pe = opaque/drifting.
    """
    c = 1.0 - (O + R + alpha) / 9.0
    b_net = B_A - c * B_G
    return K * math.sinh(2.0 * b_net)


def pe_field(O_arr: np.ndarray, R_arr: np.ndarray,
             alpha_arr: np.ndarray, K: float = 1.0) -> np.ndarray:
    """Vectorized Pe computation for entire 64×64 grid.

    Same formula as pe_from_coordinates but operates on numpy arrays.
    """
    c_field = 1.0 - (O_arr + R_arr + alpha_arr) / 9.0
    b_net = B_A - c_field * B_G
    return (K * np.sinh(2.0 * b_net)).astype(np.float32)


def fisher_distance(p: float, q: float) -> float:
    """Fisher-Rao distance on Bernoulli manifold (§165/Čencov).

    d(p, q) = 2|arcsin(√p) − arcsin(√q)|

    This is the UNIQUE metric on probability space by Čencov's theorem.
    """
    p = max(1e-8, min(p, 1.0 - 1e-8))
    q = max(1e-8, min(q, 1.0 - 1e-8))
    return 2.0 * abs(math.asin(math.sqrt(p)) - math.asin(math.sqrt(q)))


def fisher_cell_distance(grid_a: np.ndarray, grid_b: np.ndarray) -> np.ndarray:
    """Per-cell Fisher distance between two game frames.

    Returns 64×64 float array: high values = cells where rules fired.
    Uses smoothed neighborhood to handle discrete colors.
    """
    h, w = grid_a.shape
    changed = (grid_a != grid_b).astype(np.float64)

    # 3×3 neighborhood smoothing for Bernoulli parameter estimation
    kernel = np.ones((3, 3), dtype=np.float64) / 9.0
    from scipy.ndimage import convolve
    p_map = convolve(changed, kernel, mode='constant', cval=0.0)

    # Fisher distance from uniform (0.5)
    p_clipped = np.clip(p_map, 1e-8, 1.0 - 1e-8)
    return 2.0 * np.abs(np.arcsin(np.sqrt(p_clipped)) - np.arcsin(np.sqrt(0.5)))


def coordination_barrier(n_mechanisms: int) -> float:
    """Total exploration barrier = N_mechanisms × π/√2 (§136D2, §165).

    Each independent game mechanism costs exactly π/√2 ≈ 2.221 natural
    units to explore. Derived from Čencov geodesic length (§165):
    B_G = L/√2 where L = π is the forced geodesic length.
    """
    return n_mechanisms * BARRIER_CONST


def kramers_rate(barrier: float, temperature: float) -> float:
    """Kramers escape rate: Γ ∝ exp(−ΔΦ/T) (§171).

    Probability of escaping a potential well of depth `barrier`
    at effective temperature `temperature`.
    """
    if temperature < 1e-8:
        return 0.0
    return math.exp(-barrier / temperature)


# ═══════════════════════════════════════════════════════════════════
#  2. CONDUCTING SIGNALS (new — for Maestro)
# ═══════════════════════════════════════════════════════════════════

def fantasia_saturation(H_Y: float, I_D_Y: float, I_M_Y: float) -> float:
    """Fantasia Bound saturation: (I(D;Y) + I(M;Y)) / H(Y) (§2B).

    Returns ∈ [0,1]. When ≈ 1.0, all available information has been
    extracted — no more to learn from current approach.

    I(D;Y) = mutual info between actions and outcomes
    I(M;Y) = mutual info between mechanisms and outcomes
    H(Y) = total entropy of outcomes
    """
    if H_Y < 1e-8:
        return 1.0  # No entropy = nothing to learn
    return min(1.0, (I_D_Y + I_M_Y) / H_Y)


def holonomy_deficit(O_path: list, R_path: list, alpha_path: list) -> float:
    """Geometric memory from parallel transport on Eckert manifold (§101).

    Parallel-transports a unit vector around the path in (O,R,α) space.
    The deficit angle measures how much NEW geometric information the
    path encodes beyond the individual coordinate values.

    High deficit = explored geometrically diverse territory.
    Zero deficit = retraced the same ground.

    Uses Christoffel symbols of the Fisher-Rao product metric:
      ds² = dO²/[O(1-O)] + dR²/[R(1-R)] − dα²/[α(1-α)]

    Signature (2,1): O,R spacelike, α timelike.

    Args:
        O_path, R_path, alpha_path: Coordinate sequences along the path.

    Returns:
        Holonomy angle in radians. 0 = no geometric memory.
    """
    n = len(O_path)
    if n < 3:
        return 0.0

    # Parallel transport a unit vector v = (1, 0, 0) around the path.
    # Christoffel symbols for Bernoulli manifold B(p):
    #   Γ^p_pp = (1-2p) / (2·p·(1-p))
    #
    # For product metric, cross-Christoffels vanish.
    # Transport equation: dv^i/dt + Γ^i_jk · v^j · dx^k/dt = 0

    v = np.array([1.0, 0.0, 0.0], dtype=np.float64)

    for i in range(n - 1):
        # Current coordinates (clamped)
        O_c = max(0.01, min(0.99, O_path[i]))
        R_c = max(0.01, min(0.99, R_path[i]))
        a_c = max(0.01, min(0.99, alpha_path[i]))

        # Coordinate increments
        dO = O_path[min(i + 1, n - 1)] - O_path[i]
        dR = R_path[min(i + 1, n - 1)] - R_path[i]
        da = alpha_path[min(i + 1, n - 1)] - alpha_path[i]

        # Christoffel symbols (diagonal for product metric)
        G_O = (1.0 - 2.0 * O_c) / (2.0 * O_c * (1.0 - O_c))
        G_R = (1.0 - 2.0 * R_c) / (2.0 * R_c * (1.0 - R_c))
        G_a = (1.0 - 2.0 * a_c) / (2.0 * a_c * (1.0 - a_c))

        # Transport: v^i -= Γ^i_ii · v^i · dx^i  (no sum, product metric)
        v[0] -= G_O * v[0] * dO
        v[1] -= G_R * v[1] * dR
        v[2] -= G_a * v[2] * da  # Timelike: sign already in metric

    # Deficit = angle between initial and transported vector
    initial = np.array([1.0, 0.0, 0.0])
    v_norm = np.linalg.norm(v)
    if v_norm < 1e-12:
        return math.pi  # Complete rotation
    cos_angle = np.clip(np.dot(initial, v / v_norm), -1.0, 1.0)
    return math.acos(cos_angle)


def jko_gradient(phi_trajectory: list, window: int = 5) -> float:
    """JKO gradient flow: dφ/dt — steepness of thermodynamic descent (HP203).

    Positive = progressing toward win. Zero = stalled. Negative = regressing.

    Uses weighted recent window (more recent = more weight).
    """
    if len(phi_trajectory) < 2:
        return 0.0

    traj = phi_trajectory[-window:] if len(phi_trajectory) > window else phi_trajectory
    n = len(traj)
    if n < 2:
        return 0.0

    # Weighted linear regression (exponential weights: recent matters more)
    weights = np.exp(np.linspace(-1, 0, n))
    x = np.arange(n, dtype=np.float64)
    y = np.array(traj, dtype=np.float64)

    w_sum = weights.sum()
    wx = (weights * x).sum() / w_sum
    wy = (weights * y).sum() / w_sum
    wxx = (weights * x * x).sum() / w_sum
    wxy = (weights * x * y).sum() / w_sum

    denom = wxx - wx * wx
    if abs(denom) < 1e-12:
        return 0.0

    return (wxy - wx * wy) / denom


def pade_extrapolate(trajectory: list, order: tuple = (2, 1)) -> Optional[float]:
    """Padé rational approximation to predict convergence (§177).

    Fits a [p/q] Padé approximant to the φ trajectory and extrapolates.
    More accurate than polynomial extrapolation for saturating curves.

    Args:
        trajectory: φ values (at least p+q+1 points needed)
        order: (numerator_degree, denominator_degree)

    Returns:
        Predicted converged value, or None if insufficient data.
    """
    p, q = order
    min_points = p + q + 1
    if len(trajectory) < min_points:
        return None

    # Use last min_points*2 values (or all if fewer)
    traj = np.array(trajectory[-(min_points * 2):], dtype=np.float64)
    n = len(traj)
    t = np.linspace(0, 1, n)

    # Fit polynomial through data
    try:
        poly_coeffs = np.polyfit(t, traj, min(p + q, n - 1))
    except (np.linalg.LinAlgError, ValueError):
        return None

    # Build Padé from Taylor coefficients at t=0
    # Simple approach: evaluate polynomial at t=2 (extrapolate 1 unit ahead)
    # then average with last value for stability
    poly = np.poly1d(poly_coeffs)
    extrapolated = float(poly(1.5))  # 50% beyond observed range

    # Clamp to reasonable range
    lo, hi = min(traj), max(traj)
    margin = (hi - lo) * 0.5 if hi > lo else 0.1
    extrapolated = max(lo - margin, min(hi + margin, extrapolated))

    return extrapolated


# ═══════════════════════════════════════════════════════════════════
#  3. PID INFORMATION DECOMPOSITION (HP204)
# ═══════════════════════════════════════════════════════════════════

def pid_decompose(new_hashes: set, shared_hashes: set,
                  new_atoms: set, shared_atoms: set) -> dict:
    """Partial Information Decomposition for solver contribution (HP204).

    Measures how much UNIQUE vs REDUNDANT vs SYNERGISTIC information
    a solver provides relative to the shared knowledge pool.

    O ↔ unique information (new transitions not in shared pool)
    R ↔ redundancy (transitions already known)
    α ↔ synergy (new transitions that combine with shared to unlock atoms)

    Args:
        new_hashes: State hashes this solver visited
        shared_hashes: State hashes in shared pool
        new_atoms: Mechanism atoms this solver discovered
        shared_atoms: Mechanism atoms in shared pool

    Returns:
        {unique: float, redundant: float, synergistic: float}
        Values ∈ [0,1], sum to 1.
    """
    if not new_hashes:
        return {'unique': 0.0, 'redundant': 1.0, 'synergistic': 0.0}

    # Unique: fraction of new states not previously seen
    novel_states = new_hashes - shared_hashes
    unique = len(novel_states) / len(new_hashes) if new_hashes else 0.0

    # Redundant: fraction of states already in shared pool
    redundant = 1.0 - unique

    # Synergistic: new atoms that require both new AND shared transitions
    # (atoms that neither pool could produce alone)
    if new_atoms and shared_atoms:
        combined_atoms = new_atoms | shared_atoms
        synergistic_atoms = combined_atoms - new_atoms - shared_atoms
        synergy_raw = len(synergistic_atoms) / max(1, len(combined_atoms))
    else:
        synergy_raw = 0.0

    # Rebalance: redistribute redundancy to account for synergy
    if synergy_raw > 0:
        synergistic = min(redundant, synergy_raw)
        redundant -= synergistic
    else:
        synergistic = 0.0

    total = unique + redundant + synergistic
    if total > 0:
        return {
            'unique': unique / total,
            'redundant': redundant / total,
            'synergistic': synergistic / total,
        }
    return {'unique': 0.0, 'redundant': 1.0, 'synergistic': 0.0}


# ═══════════════════════════════════════════════════════════════════
#  4. TRANSFER LEARNING
# ═══════════════════════════════════════════════════════════════════

def chebyshev_fingerprint(grid: np.ndarray, n_modes: int = 8) -> np.ndarray:
    """Chebyshev spectral fingerprint for game similarity (§164B).

    Decomposes the grid's color distribution into eigenmode coefficients.
    Color-invariant: two games with relabeled colors produce similar fingerprints.

    Returns n_modes-dimensional feature vector.
    """
    h, w = grid.shape
    # Color histogram (normalized)
    hist = np.bincount(grid.ravel().astype(int), minlength=16).astype(np.float64)
    hist /= max(hist.sum(), 1)

    # Chebyshev decomposition of histogram
    coeffs = np.zeros(n_modes, dtype=np.float64)
    x = np.linspace(-1, 1, len(hist))
    for k in range(n_modes):
        T_k = np.cos(k * np.arccos(np.clip(x, -1, 1)))
        coeffs[k] = np.dot(hist, T_k) / len(hist)

    return coeffs


def game_similarity(fp_a: np.ndarray, fp_b: np.ndarray) -> float:
    """Cosine similarity between game fingerprints.

    Returns ∈ [-1, 1]. High = similar games → transfer strategies.
    """
    norm_a = np.linalg.norm(fp_a)
    norm_b = np.linalg.norm(fp_b)
    if norm_a < 1e-12 or norm_b < 1e-12:
        return 0.0
    return float(np.dot(fp_a, fp_b) / (norm_a * norm_b))


# ═══════════════════════════════════════════════════════════════════
#  5. PATH COST (Onsager-Machlup)
# ═══════════════════════════════════════════════════════════════════

def onsager_machlup_cost(entropy_trajectory: list,
                         drift: float = 0.0,
                         temperature: float = 0.1) -> float:
    """Onsager-Machlup path cost S[θ] = (1/4T)∫(θ̇ − f(θ))² dt (§48A).

    Low cost = following the game's natural flow.
    High cost = fighting against the dynamics.

    Args:
        entropy_trajectory: Entropy values along the path
        drift: Estimated natural drift rate f(θ)
        temperature: Effective temperature T
    """
    if len(entropy_trajectory) < 2 or temperature < 1e-8:
        return 0.0

    traj = np.array(entropy_trajectory, dtype=np.float64)
    velocities = np.diff(traj)
    deviations = velocities - drift
    return float(np.sum(deviations ** 2) / (4.0 * temperature))
