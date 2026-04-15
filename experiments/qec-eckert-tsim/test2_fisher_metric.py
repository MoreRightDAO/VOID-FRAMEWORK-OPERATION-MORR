#!/usr/bin/env python3
"""
Test 2: Empirical Fisher Metric vs Eckert Manifold Prediction
==============================================================

The Eckert manifold predicts that the information geometry of (O, R, alpha)
follows the Fisher product metric on three Bernoulli manifolds:

    ds² = dO²/[O(1-O)] + dR²/[R(1-R)] + dα²/[α(1-α)]

In the QEC setting, O is pinned at 1.0 (no-cloning), so we test the 2D slice:

    ds² = dR²/[R(1-R)] + dα²/[α(1-α)]

where:
    R = effective error rate (physical_error_rate × depth / distance)
    α = T-gate fraction (engagement coordinate)

PROCEDURE:
    1. For each (R, α) point, run Tsim and collect syndrome outcome distributions
    2. Compute the empirical Fisher Information Matrix from syndrome statistics
    3. Compare empirical FIM to the Eckert metric prediction
    4. Measure the deviation

PREDICTION: The empirical FIM should match the Bernoulli product metric
(diagonal, with entries 1/[R(1-R)] and 1/[α(1-α)]).

If it matches → Eckert manifold is the natural geometry of QEC information flow
If off-diagonal terms dominate → the coordinates are coupled (would need revision)
If diagonal but wrong scaling → Bernoulli product structure is wrong
"""

import numpy as np
import json
import time
from pathlib import Path

try:
    import tsim
except ImportError:
    print("Install tsim: pip install bloqade-tsim")
    print("Falling back to dry-run mode")
    tsim = None


def build_parameterized_circuit(n_qubits: int, total_gates: int,
                                 error_rate: float, t_fraction: float) -> str:
    """Build circuit with specified error rate and T-gate fraction."""
    n_t = int(total_gates * t_fraction)
    n_cliff = total_gates - n_t

    lines = []
    for q in range(n_qubits):
        lines.append(f"R {q}")

    gate_idx = 0
    t_placed = 0

    for i in range(total_gates):
        target = i % n_qubits

        # Distribute T-gates evenly
        is_t_gate = (n_t > 0 and
                     t_placed < n_t and
                     i >= int(gate_idx * total_gates / max(n_t, 1)))

        if is_t_gate and t_placed < n_t:
            lines.append(f"T {target}")
            lines.append(f"DEPOLARIZE1({error_rate}) {target}")
            t_placed += 1
            gate_idx += 1
        else:
            choice = i % 3
            if choice == 0:
                lines.append(f"H {target}")
                lines.append(f"DEPOLARIZE1({error_rate}) {target}")
            elif choice == 1:
                lines.append(f"S {target}")
                lines.append(f"DEPOLARIZE1({error_rate}) {target}")
            else:
                t2 = (target + 1) % n_qubits
                lines.append(f"CNOT {target} {t2}")
                lines.append(f"DEPOLARIZE2({error_rate}) {target} {t2}")

    qubit_list = " ".join(str(q) for q in range(n_qubits))
    lines.append(f"M {qubit_list}")

    for q in range(n_qubits - 1):
        r1 = -(n_qubits - q)
        r2 = -(n_qubits - q - 1)
        lines.append(f"DETECTOR rec[{r1}] rec[{r2}]")

    rec_refs = " ".join(f"rec[{-(n_qubits - q)}]" for q in range(n_qubits))
    lines.append(f"OBSERVABLE_INCLUDE(0) {rec_refs}")

    return lines


def get_syndrome_distribution(circuit_lines: list, shots: int) -> np.ndarray:
    """Run circuit and return detector firing rates."""
    if tsim is None:
        return None

    circuit_str = "\n".join(circuit_lines)
    circuit = tsim.Circuit(circuit_str)
    sampler = circuit.compile_detector_sampler()
    samples = sampler.sample(
        shots=shots,
        use_detector_reference_sample=True,
        use_observable_reference_sample=True,
    )

    n_det = samples.shape[1] - 1
    detector_samples = samples[:, :n_det]

    # Return per-detector firing rates
    return np.mean(detector_samples, axis=0)


def compute_fisher_information_matrix(n_qubits: int, total_gates: int,
                                       R_val: float, alpha_val: float,
                                       shots: int, delta: float = 0.01):
    """
    Compute 2x2 Fisher Information Matrix numerically.

    FIM[i,j] = sum_k (1/p_k) * (dp_k/dtheta_i) * (dp_k/dtheta_j)

    where p_k are detector firing probabilities and theta = (R, alpha).
    We estimate derivatives by finite differences.
    """
    # Get syndrome distribution at (R, alpha)
    p_center = get_syndrome_distribution(
        build_parameterized_circuit(n_qubits, total_gates, R_val, alpha_val),
        shots
    )
    if p_center is None:
        return None, None

    # Perturb R (error rate)
    R_plus = min(R_val + delta, 0.99)
    R_minus = max(R_val - delta, 0.001)
    p_R_plus = get_syndrome_distribution(
        build_parameterized_circuit(n_qubits, total_gates, R_plus, alpha_val),
        shots
    )
    p_R_minus = get_syndrome_distribution(
        build_parameterized_circuit(n_qubits, total_gates, R_minus, alpha_val),
        shots
    )

    # Perturb alpha (T-gate fraction)
    alpha_plus = min(alpha_val + delta, 0.99)
    alpha_minus = max(alpha_val - delta, 0.01)
    p_a_plus = get_syndrome_distribution(
        build_parameterized_circuit(n_qubits, total_gates, R_val, alpha_plus),
        shots
    )
    p_a_minus = get_syndrome_distribution(
        build_parameterized_circuit(n_qubits, total_gates, R_val, alpha_minus),
        shots
    )

    # Finite difference derivatives
    dp_dR = (p_R_plus - p_R_minus) / (R_plus - R_minus)
    dp_dalpha = (p_a_plus - p_a_minus) / (alpha_plus - alpha_minus)

    # Fisher Information Matrix (2x2)
    # FIM[i,j] = sum_k (1/p_k) * dp_k/dtheta_i * dp_k/dtheta_j
    # Regularize to avoid division by zero
    p_reg = np.maximum(p_center, 1e-6)
    q_reg = np.maximum(1 - p_center, 1e-6)

    # For Bernoulli outcomes, FIM contribution from detector k:
    # = (dp_k/dθ_i)(dp_k/dθ_j) / [p_k(1-p_k)]
    weights = 1.0 / (p_reg * q_reg)

    F_RR = np.sum(weights * dp_dR * dp_dR)
    F_Ra = np.sum(weights * dp_dR * dp_dalpha)
    F_aa = np.sum(weights * dp_dalpha * dp_dalpha)

    empirical_FIM = np.array([[F_RR, F_Ra],
                               [F_Ra, F_aa]])

    # Eckert metric prediction (Bernoulli product)
    eckert_FIM = np.array([
        [1.0 / (R_val * (1 - R_val)), 0],
        [0, 1.0 / (alpha_val * (1 - alpha_val))]
    ])

    return empirical_FIM, eckert_FIM


def run_fisher_metric_test():
    """
    Scan the (R, alpha) plane, compute empirical FIM at each point,
    and compare to Eckert metric prediction.
    """
    n_qubits = 7
    total_gates = 30
    shots = 50_000

    # Grid of (R, alpha) values to test
    R_values = [0.005, 0.01, 0.02, 0.05]
    alpha_values = [0.10, 0.20, 0.30, 0.50]

    results = []

    print("=" * 70)
    print("TEST 2: Empirical Fisher Metric vs Eckert Manifold Prediction")
    print("=" * 70)
    print(f"Config: {n_qubits} qubits, {total_gates} gates, {shots} shots")
    print(f"Prediction: FIM ≈ diag(1/[R(1-R)], 1/[α(1-α)])")
    print("-" * 70)

    for R in R_values:
        for alpha in alpha_values:
            t0 = time.time()
            emp_FIM, eck_FIM = compute_fisher_information_matrix(
                n_qubits, total_gates, R, alpha, shots
            )
            elapsed = time.time() - t0

            if emp_FIM is None:
                print(f"  R={R:.3f}, α={alpha:.2f}: DRY RUN")
                results.append({
                    "R": R, "alpha": alpha,
                    "dry_run": True
                })
                continue

            # Compare: relative Frobenius norm of difference
            diff = emp_FIM - eck_FIM
            rel_error = np.linalg.norm(diff, 'fro') / np.linalg.norm(eck_FIM, 'fro')

            # Off-diagonal ratio: how much coupling vs diagonal
            diag_norm = np.sqrt(emp_FIM[0, 0]**2 + emp_FIM[1, 1]**2)
            offdiag_ratio = abs(emp_FIM[0, 1]) / max(diag_norm, 1e-10)

            # Scaling check: empirical diagonal vs predicted
            R_ratio = emp_FIM[0, 0] / eck_FIM[0, 0] if eck_FIM[0, 0] > 0 else np.nan
            a_ratio = emp_FIM[1, 1] / eck_FIM[1, 1] if eck_FIM[1, 1] > 0 else np.nan

            print(f"  R={R:.3f}, α={alpha:.2f}: "
                  f"rel_err={rel_error:.4f}, offdiag={offdiag_ratio:.4f}, "
                  f"R_ratio={R_ratio:.3f}, α_ratio={a_ratio:.3f} "
                  f"[{elapsed:.1f}s]")

            results.append({
                "R": R,
                "alpha": alpha,
                "empirical_FIM": emp_FIM.tolist(),
                "eckert_FIM": eck_FIM.tolist(),
                "relative_error": float(rel_error),
                "offdiag_ratio": float(offdiag_ratio),
                "R_scaling_ratio": float(R_ratio),
                "alpha_scaling_ratio": float(a_ratio),
                "elapsed_s": elapsed,
            })

    # Summary
    if results and not results[0].get("dry_run", False):
        rel_errors = [r["relative_error"] for r in results]
        offdiag_ratios = [r["offdiag_ratio"] for r in results]

        print("\n" + "=" * 70)
        print("SUMMARY")
        print(f"  Mean relative error (FIM vs Eckert): {np.mean(rel_errors):.4f}")
        print(f"  Max relative error: {np.max(rel_errors):.4f}")
        print(f"  Mean off-diagonal ratio: {np.mean(offdiag_ratios):.4f}")

        if np.mean(rel_errors) < 0.3 and np.mean(offdiag_ratios) < 0.1:
            verdict = "SUPPORTED"
            print(f"  VERDICT: Eckert metric SUPPORTED (low error, low coupling)")
        elif np.mean(offdiag_ratios) > 0.3:
            verdict = "COUPLED"
            print(f"  VERDICT: Coordinates COUPLED (large off-diagonal FIM)")
        else:
            verdict = "INCONCLUSIVE"
            print(f"  VERDICT: INCONCLUSIVE (moderate deviations)")

        for r in results:
            if not r.get("dry_run"):
                r["verdict"] = verdict

    # Save
    out_path = Path(__file__).parent / "results_test2_fisher_metric.json"
    with open(out_path, "w") as f:
        json.dump({
            "test": "Empirical Fisher Metric vs Eckert Manifold",
            "prediction": "FIM = diag(1/[R(1-R)], 1/[α(1-α)]) — Bernoulli product",
            "framework_section": "§1A (Eckert manifold), §64G (Dynamical Eckert Metric)",
            "params": {
                "n_qubits": n_qubits,
                "total_gates": total_gates,
                "shots": shots,
            },
            "results": results,
        }, f, indent=2, default=str)

    print(f"\nResults saved to {out_path}")
    return results


if __name__ == "__main__":
    run_fisher_metric_test()
