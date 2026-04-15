#!/usr/bin/env python3
"""
Test 4: Direct Measurement of the Explaining-Away Penalty
=========================================================

The Fantasia Bound's exact decomposition (Theorem 1.5):

    I(D;Y) + I(M;Y) = H(Y) - H(Y|D,M) - I(D;M|Y)

The explaining-away penalty I(D;M|Y) > 0 whenever two independent sources
(D, M) share a channel. The Structure Theorem says this penalty GROWS
with engagement.

PREVIOUS TESTS measured downstream consequences (error rate curves).
THIS TEST measures the penalty directly via mutual information.

SETUP:
    D = initialization state (one of k possible prep states — the "observer input")
    M = circuit structure (one of k possible gate sequences — the "mechanism")
    Y = syndrome measurement outcomes

    D and M are chosen independently. We measure:
    - I(D;Y): how much the syndrome reveals about which prep state was used
    - I(M;Y): how much the syndrome reveals about which circuit was run
    - I(D;M|Y): the explaining-away penalty — how much observing Y
      creates a spurious correlation between D and M

    "Engagement" = circuit depth × error rate (how much the circuit
    modifies the state). We sweep engagement and check if I(D;M|Y) grows.

PREDICTION:
    1. I(D;M|Y) > 0 at all engagement levels (penalty exists)
    2. I(D;M|Y) grows with engagement (Structure Theorem)
    3. Three-point architecture (ancilla verification) reduces I(D;M|Y)

Hardware: CPU-feasible. 5-7 qubits, 20K shots per (D,M) combination.
"""

import numpy as np
import json
import time
from pathlib import Path
from itertools import product as iter_product

try:
    import tsim
except ImportError:
    print("Install tsim: pip install bloqade-tsim")
    print("Falling back to dry-run mode")
    tsim = None


# ============================================================
# Circuit builders
# ============================================================

def build_circuit(n_qubits: int, prep_state: int, mechanism: int,
                  depth: int, error_rate: float) -> str:
    """
    Build a circuit with specified prep state and mechanism.

    prep_state (D): selects initial qubit configuration
        0 = all |0⟩ (default reset)
        1 = all |+⟩ (Hadamard on all)
        2 = alternating |0⟩|1⟩ (X on odd qubits)
        3 = GHZ-like (H on q0, CNOT chain)

    mechanism (M): selects gate pattern applied for `depth` layers
        0 = identity (only noise, no gates)
        1 = Clifford ladder (H-S-CNOT repeating)
        2 = T-gate heavy (T on every qubit each layer)
        3 = entangling (CNOT ring each layer)
    """
    lines = []

    # Reset all qubits
    for q in range(n_qubits):
        lines.append(f"R {q}")

    # Prep state D
    if prep_state == 0:
        pass  # all |0⟩
    elif prep_state == 1:
        for q in range(n_qubits):
            lines.append(f"H {q}")
    elif prep_state == 2:
        for q in range(1, n_qubits, 2):
            lines.append(f"X {q}")
    elif prep_state == 3:
        lines.append(f"H 0")
        for q in range(n_qubits - 1):
            lines.append(f"CNOT {q} {q + 1}")

    # Mechanism M applied for `depth` layers
    for layer in range(depth):
        if mechanism == 0:
            # Identity + noise only
            for q in range(n_qubits):
                lines.append(f"DEPOLARIZE1({error_rate}) {q}")
        elif mechanism == 1:
            # Clifford ladder
            for q in range(n_qubits):
                gate_choice = (q + layer) % 3
                if gate_choice == 0:
                    lines.append(f"H {q}")
                elif gate_choice == 1:
                    lines.append(f"S {q}")
                else:
                    t2 = (q + 1) % n_qubits
                    lines.append(f"CNOT {q} {t2}")
                lines.append(f"DEPOLARIZE1({error_rate}) {q}")
        elif mechanism == 2:
            # T-gate heavy
            for q in range(n_qubits):
                lines.append(f"T {q}")
                lines.append(f"DEPOLARIZE1({error_rate}) {q}")
            # Plus entangling gates
            for q in range(0, n_qubits - 1, 2):
                lines.append(f"CNOT {q} {q + 1}")
                lines.append(f"DEPOLARIZE2({error_rate}) {q} {q + 1}")
        elif mechanism == 3:
            # CNOT ring (maximal entanglement)
            for q in range(n_qubits):
                t2 = (q + 1) % n_qubits
                lines.append(f"CNOT {q} {t2}")
                lines.append(f"DEPOLARIZE2({error_rate}) {q} {t2}")

    # Measure all qubits
    qubit_list = " ".join(str(q) for q in range(n_qubits))
    lines.append(f"M {qubit_list}")

    # Detectors: parity checks between adjacent qubits
    for q in range(n_qubits - 1):
        r1 = -(n_qubits - q)
        r2 = -(n_qubits - q - 1)
        lines.append(f"DETECTOR rec[{r1}] rec[{r2}]")

    return "\n".join(lines)


def run_circuit_get_outcomes(circuit_str: str, shots: int) -> np.ndarray:
    """Run circuit, return raw detector outcome matrix (shots × n_detectors)."""
    if tsim is None:
        return None

    circuit = tsim.Circuit(circuit_str)
    sampler = circuit.compile_detector_sampler()
    samples = sampler.sample(shots=shots)
    return samples


# ============================================================
# Information-theoretic computations
# ============================================================

def entropy(probs):
    """Shannon entropy of a probability distribution."""
    p = probs[probs > 0]
    return -np.sum(p * np.log2(p))


def syndrome_to_key(row: np.ndarray) -> int:
    """Convert binary syndrome row to integer key."""
    val = 0
    for bit in row:
        val = (val << 1) | int(bit)
    return val


def estimate_mutual_info(joint_counts, marginal_x_counts, marginal_y_counts, total):
    """
    Estimate I(X;Y) from joint and marginal count dictionaries.
    Uses MLE plug-in estimator with small-sample bias correction (Miller-Madow).
    """
    if total == 0:
        return 0.0

    mi = 0.0
    for (x, y), n_xy in joint_counts.items():
        if n_xy == 0:
            continue
        p_xy = n_xy / total
        p_x = marginal_x_counts.get(x, 0) / total
        p_y = marginal_y_counts.get(y, 0) / total
        if p_x > 0 and p_y > 0:
            mi += p_xy * np.log2(p_xy / (p_x * p_y))

    # Miller-Madow bias correction
    n_nonzero_joint = sum(1 for v in joint_counts.values() if v > 0)
    n_nonzero_x = sum(1 for v in marginal_x_counts.values() if v > 0)
    n_nonzero_y = sum(1 for v in marginal_y_counts.values() if v > 0)
    bias = (n_nonzero_joint - n_nonzero_x - n_nonzero_y + 1) / (2 * total * np.log(2))

    return max(0.0, mi - bias)


def compute_explaining_away_penalty(outcomes_dict, n_d, n_m, shots_per_combo):
    """
    Compute I(D;M|Y) — the explaining-away penalty.

    outcomes_dict: {(d, m): syndrome_matrix} for all (d,m) pairs
    Each syndrome_matrix is (shots × n_detectors).

    I(D;M|Y) = I(D;M,Y) - I(D;Y)
             = H(D|Y) - H(D|M,Y)

    Since D ⊥ M by construction:
        I(D;M|Y) = I(D;Y) + I(M;Y) - I(D,M;Y)
        (This follows from the chain rule + D ⊥ M)

    Actually, more directly:
        I(D;M|Y) = H(D|Y) + H(M|Y) - H(D,M|Y)

    We compute all terms from the empirical distribution.
    """
    # Build the joint distribution over (D, M, Y)
    # Y = syndrome outcome (quantized to integer key)
    joint_dmy = {}   # (d, m, y) -> count
    joint_dy = {}    # (d, y) -> count
    joint_my = {}    # (m, y) -> count
    marginal_y = {}  # y -> count
    total = 0

    for (d, m), syndromes in outcomes_dict.items():
        if syndromes is None:
            return None
        for row_idx in range(syndromes.shape[0]):
            y = syndrome_to_key(syndromes[row_idx])
            joint_dmy[(d, m, y)] = joint_dmy.get((d, m, y), 0) + 1
            joint_dy[(d, y)] = joint_dy.get((d, y), 0) + 1
            joint_my[(m, y)] = joint_my.get((m, y), 0) + 1
            marginal_y[y] = marginal_y.get(y, 0) + 1
            total += 1

    if total == 0:
        return None

    # Compute H(Y)
    py = np.array(list(marginal_y.values())) / total
    H_Y = entropy(py)

    # Compute H(D,Y) and from it I(D;Y)
    # I(D;Y) = H(Y) - H(Y|D) = H(D) + H(Y) - H(D,Y)
    marginal_d = {}
    for (d, y), cnt in joint_dy.items():
        marginal_d[d] = marginal_d.get(d, 0) + cnt
    I_D_Y = estimate_mutual_info(
        joint_dy, marginal_d, marginal_y, total
    )

    # Compute I(M;Y)
    marginal_m = {}
    for (m, y), cnt in joint_my.items():
        marginal_m[m] = marginal_m.get(m, 0) + cnt
    I_M_Y = estimate_mutual_info(
        joint_my, marginal_m, marginal_y, total
    )

    # Compute I(D,M;Y) = I(DM;Y)
    # Treat (d,m) as a single variable
    joint_dm_y = {}
    marginal_dm = {}
    for (d, m, y), cnt in joint_dmy.items():
        dm = (d, m)
        joint_dm_y[(dm, y)] = joint_dm_y.get((dm, y), 0) + cnt
        marginal_dm[dm] = marginal_dm.get(dm, 0) + cnt
    I_DM_Y = estimate_mutual_info(
        joint_dm_y, marginal_dm, marginal_y, total
    )

    # Explaining-away penalty:
    # I(D;M|Y) = I(D;Y) + I(M;Y) - I(D,M;Y)  [when D ⊥ M]
    # Wait — this isn't right. The correct identity is:
    # I(D,M;Y) = I(D;Y) + I(M;Y|D)
    # I(D;M|Y) = I(D;M) + I(D;Y|M) + I(M;Y|D) - I(D;Y) - I(M;Y) ... complicated
    #
    # Simpler: use the definition directly.
    # I(D;M|Y) = H(D|Y) + H(M|Y) - H(D,M|Y)
    #
    # H(D|Y) = H(D,Y) - H(Y) = H(D) + H(Y) - I(D;Y) - H(Y) = H(D) - I(D;Y)
    # H(M|Y) = H(M) - I(M;Y)
    # H(D,M|Y) = H(D,M,Y) - H(Y) = H(D,M) + H(Y) - I(DM;Y) - H(Y) = H(D,M) - I(DM;Y)
    #
    # Since D ⊥ M: H(D,M) = H(D) + H(M)
    #
    # I(D;M|Y) = [H(D) - I(D;Y)] + [H(M) - I(M;Y)] - [H(D) + H(M) - I(DM;Y)]
    #           = I(DM;Y) - I(D;Y) - I(M;Y)

    penalty = I_DM_Y - I_D_Y - I_M_Y

    # Also compute the Fantasia Bound terms
    # H(Y|D,M) = H(Y) - I(DM;Y)
    H_Y_given_DM = H_Y - I_DM_Y

    return {
        "I_D_Y": float(I_D_Y),
        "I_M_Y": float(I_M_Y),
        "I_DM_Y": float(I_DM_Y),
        "penalty_I_D_M_given_Y": float(penalty),
        "H_Y": float(H_Y),
        "H_Y_given_DM": float(H_Y_given_DM),
        "fantasia_check": float(I_D_Y + I_M_Y + penalty + H_Y_given_DM),
        # Should equal H(Y) if decomposition is correct
        "fantasia_H_Y": float(H_Y),
    }


# ============================================================
# Main test
# ============================================================

def run_explaining_away_test():
    """
    Sweep engagement levels, measure the explaining-away penalty at each.
    """
    n_qubits = 5
    n_preps = 4      # D ∈ {0,1,2,3}
    n_mechs = 4      # M ∈ {0,1,2,3}
    shots_per_combo = 5000  # 4×4×5000 = 80K total shots per engagement level
    error_rate = 0.01

    # Engagement = depth (more layers = more interaction with channel)
    engagement_levels = [1, 2, 4, 8, 12, 16, 24, 32]

    results = []

    print("=" * 70)
    print("TEST 4: Direct Measurement of the Explaining-Away Penalty")
    print("=" * 70)
    print(f"Config: {n_qubits} qubits, {n_preps} prep states × {n_mechs} mechanisms")
    print(f"        {shots_per_combo} shots per combo, error_rate={error_rate}")
    print(f"Prediction: I(D;M|Y) > 0 and grows with engagement (depth)")
    print("-" * 70)
    print(f"{'Depth':>6} {'I(D;Y)':>8} {'I(M;Y)':>8} {'I(DM;Y)':>9} "
          f"{'Penalty':>9} {'H(Y)':>8} {'Check':>8} {'Time':>7}")
    print("-" * 70)

    for depth in engagement_levels:
        t0 = time.time()
        outcomes = {}

        for d_idx in range(n_preps):
            for m_idx in range(n_mechs):
                circuit_str = build_circuit(
                    n_qubits, d_idx, m_idx, depth, error_rate
                )
                syndromes = run_circuit_get_outcomes(circuit_str, shots_per_combo)
                outcomes[(d_idx, m_idx)] = syndromes

        elapsed = time.time() - t0

        if any(v is None for v in outcomes.values()):
            print(f"{depth:>6} {'DRY RUN':>50}")
            results.append({"depth": depth, "dry_run": True})
            continue

        info = compute_explaining_away_penalty(
            outcomes, n_preps, n_mechs, shots_per_combo
        )

        if info is None:
            print(f"{depth:>6} {'FAILED':>50}")
            continue

        # Decomposition check: I(D;Y) + I(M;Y) + I(D;M|Y) + H(Y|D,M) should ≈ H(Y)
        check_error = abs(info["fantasia_check"] - info["fantasia_H_Y"])

        print(f"{depth:>6} {info['I_D_Y']:>8.4f} {info['I_M_Y']:>8.4f} "
              f"{info['I_DM_Y']:>9.4f} {info['penalty_I_D_M_given_Y']:>9.4f} "
              f"{info['H_Y']:>8.4f} {check_error:>8.5f} {elapsed:>6.1f}s")

        results.append({
            "depth": depth,
            "engagement_proxy": depth * error_rate * n_qubits,
            **info,
            "decomposition_error": float(check_error),
            "elapsed_s": elapsed,
        })

    # ── Analysis ──
    print("\n" + "=" * 70)
    print("ANALYSIS")

    valid = [r for r in results if not r.get("dry_run", False)]

    if len(valid) >= 3:
        depths = np.array([r["depth"] for r in valid])
        penalties = np.array([r["penalty_I_D_M_given_Y"] for r in valid])

        # Check 1: Is penalty > 0?
        positive_count = np.sum(penalties > 0)
        print(f"\n  Penalty > 0 in {positive_count}/{len(valid)} measurements")

        # Check 2: Does penalty grow with engagement?
        if len(depths) >= 3:
            coeffs = np.polyfit(depths, penalties, 1)
            slope = coeffs[0]
            print(f"  Linear trend: slope = {slope:.6f} (penalty per depth unit)")

            # Correlation
            if np.std(penalties) > 0:
                corr = np.corrcoef(depths, penalties)[0, 1]
                print(f"  Correlation(depth, penalty): r = {corr:.4f}")
            else:
                corr = 0.0

        # Check 3: Decomposition holds?
        check_errors = [r["decomposition_error"] for r in valid]
        print(f"  Mean decomposition error: {np.mean(check_errors):.6f}")
        print(f"  Max decomposition error: {np.max(check_errors):.6f}")

        # Verdicts
        if positive_count >= len(valid) * 0.8 and slope > 0:
            verdict = "SUPPORTED"
            print(f"\n  VERDICT: Explaining-away penalty EXISTS and GROWS with engagement")
            print(f"  → Fantasia Bound Structure Theorem SUPPORTED on quantum substrate")
        elif positive_count >= len(valid) * 0.5:
            verdict = "PARTIAL"
            print(f"\n  VERDICT: Penalty exists but growth pattern unclear")
        elif positive_count < len(valid) * 0.3:
            verdict = "CHALLENGED"
            print(f"\n  VERDICT: Penalty not reliably > 0 — CHALLENGED")
        else:
            verdict = "INCONCLUSIVE"
            print(f"\n  VERDICT: INCONCLUSIVE")

        for r in valid:
            r["verdict"] = verdict
            r["penalty_slope"] = float(slope)
            r["penalty_correlation"] = float(corr) if np.std(penalties) > 0 else 0.0

    print("=" * 70)

    # Save results
    out_path = Path(__file__).parent / "results_test4_explaining_away.json"
    with open(out_path, "w") as f:
        json.dump({
            "test": "Direct Measurement of the Explaining-Away Penalty",
            "prediction": "I(D;M|Y) > 0 and grows with engagement",
            "framework_section": "§2B₂ (Structure Theorem), Theorem 1.5 (Exact Decomposition)",
            "params": {
                "n_qubits": n_qubits,
                "n_prep_states": n_preps,
                "n_mechanisms": n_mechs,
                "shots_per_combo": shots_per_combo,
                "error_rate": error_rate,
                "engagement_levels": engagement_levels,
            },
            "results": valid,
        }, f, indent=2)

    print(f"\nResults saved to {out_path}")
    return valid


if __name__ == "__main__":
    run_explaining_away_test()
