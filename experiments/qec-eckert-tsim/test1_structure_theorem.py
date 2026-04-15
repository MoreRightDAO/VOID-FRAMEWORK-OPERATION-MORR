#!/usr/bin/env python3
"""
Test 1: Structure Theorem on Quantum Circuits
==============================================

The Fantasia Bound Structure Theorem predicts that the explaining-away
penalty I(D;M|Y) grows with engagement. In QEC:

  - Engagement = T-gate count (non-Clifford computation power)
  - Transparency = syndrome information (bits revealed by stabilizer measurements)
  - Penalty = degradation of error correction capability per T-gate

TWO SUB-TESTS:

Test 1A — Differential noise model:
  T-gates are implemented via magic state injection, which in real QEC is
  5-15× noisier than direct Clifford gates. We model this with a T-gate
  noise multiplier. If the total error is convex in T-count, the marginal
  cost per T-gate increases — Structure Theorem on resource cost.

Test 1B — Syndrome degradation (non-Clifford interference):
  Even at EQUAL noise, T-gates rotate errors out of the Pauli group, making
  syndrome measurements less informative. We measure this by comparing
  detector firing rates and observable error with/without T-gates inserted
  between noise injection and syndrome extraction. Uses a proper repetition
  code with mid-circuit syndrome rounds.

PREDICTION: Both sub-tests should show super-linear (convex) error growth
with T-gate count.

Hardware: CPU-feasible. 7-9 qubits, 50K-100K shots.
"""

import numpy as np
import json
import time
from pathlib import Path

try:
    import tsim
except ImportError:
    print("Install tsim: pip install bloqade-tsim")
    print("Falling back to dry-run mode (circuit generation only)")
    tsim = None


# ============================================================
# Test 1A: Differential noise — realistic T-gate overhead
# ============================================================

def build_differential_noise_circuit(n_qubits: int, n_t_gates: int,
                                      n_clifford_gates: int,
                                      clifford_error: float,
                                      t_noise_factor: float) -> str:
    """
    Circuit with realistic differential noise: T-gates are t_noise_factor×
    noisier than Clifford gates, modeling magic state injection overhead.

    In real fault-tolerant QEC:
    - Clifford gates: transversal, 1 time step, noise = p
    - T-gates: magic state injection gadget, ~5 time steps,
      effective noise ≈ 5p-15p depending on distillation quality
    """
    t_error = clifford_error * t_noise_factor
    lines = []

    for q in range(n_qubits):
        lines.append(f"R {q}")

    total_gates = n_t_gates + n_clifford_gates

    # Distribute T-gates evenly
    gate_sequence = []
    if total_gates > 0:
        t_positions = set()
        if n_t_gates > 0:
            for i in range(n_t_gates):
                pos = int(i * total_gates / n_t_gates)
                t_positions.add(min(pos, total_gates - 1))

        placed_t = 0
        for i in range(total_gates):
            if i in t_positions and placed_t < n_t_gates:
                gate_sequence.append("T")
                placed_t += 1
            else:
                gate_sequence.append("CLIFFORD")

    for i, gate_type in enumerate(gate_sequence):
        target = i % n_qubits

        if gate_type == "T":
            # T-gate with higher noise (magic state injection model)
            lines.append(f"T {target}")
            lines.append(f"DEPOLARIZE1({t_error}) {target}")
            # Injection also involves a CNOT (gate teleportation)
            if n_qubits > 1:
                t2 = (target + 1) % n_qubits
                lines.append(f"CNOT {target} {t2}")
                lines.append(f"DEPOLARIZE2({t_error}) {target} {t2}")
        else:
            clifford_choice = i % 3
            if clifford_choice == 0:
                lines.append(f"H {target}")
                lines.append(f"DEPOLARIZE1({clifford_error}) {target}")
            elif clifford_choice == 1:
                lines.append(f"S {target}")
                lines.append(f"DEPOLARIZE1({clifford_error}) {target}")
            else:
                t2 = (target + 1) % n_qubits
                lines.append(f"CNOT {target} {t2}")
                lines.append(f"DEPOLARIZE2({clifford_error}) {target} {t2}")

    qubit_list = " ".join(str(q) for q in range(n_qubits))
    lines.append(f"M {qubit_list}")

    for q in range(n_qubits - 1):
        r1 = -(n_qubits - q)
        r2 = -(n_qubits - q - 1)
        lines.append(f"DETECTOR rec[{r1}] rec[{r2}]")

    rec_refs = " ".join(f"rec[{-(n_qubits - q)}]" for q in range(n_qubits))
    lines.append(f"OBSERVABLE_INCLUDE(0) {rec_refs}")

    return "\n".join(lines)


# ============================================================
# Test 1B: Syndrome degradation — T-gates interfere with QEC
# ============================================================

def build_syndrome_degradation_circuit(n_data: int, n_rounds: int,
                                        n_t_per_round: int,
                                        error_rate: float) -> str:
    """
    Repetition code with syndrome extraction rounds.
    T-gates injected between rounds degrade syndrome usefulness.

    Layout: data qubits [0..n_data-1], ancilla qubits [n_data..2*n_data-2]
    Stabilizers: Z_i Z_{i+1} for i in 0..n_data-2

    Each round:
      1. (Optional) Apply T-gates to data qubits
      2. CNOT data[i] → ancilla[i], CNOT data[i+1] → ancilla[i]
      3. Measure + reset ancillae
      4. DETECTOR comparing this round's syndrome to previous round's
    """
    n_ancilla = n_data - 1
    n_total = n_data + n_ancilla
    lines = []

    # Initialize
    for q in range(n_total):
        lines.append(f"R {q}")

    measurements_per_round = n_ancilla
    total_measurements = 0

    for rnd in range(n_rounds):
        # Apply T-gates to data qubits (the engagement variable)
        for t_idx in range(n_t_per_round):
            target = t_idx % n_data
            lines.append(f"T {target}")
            # Same noise rate as Cliffords — testing pure non-Clifford interference
            lines.append(f"DEPOLARIZE1({error_rate}) {target}")

        # Syndrome extraction: measure Z_i Z_{i+1} via ancillae
        for i in range(n_ancilla):
            anc = n_data + i
            # CNOT data[i] → ancilla[i]
            lines.append(f"CNOT {i} {anc}")
            lines.append(f"DEPOLARIZE2({error_rate}) {i} {anc}")
            # CNOT data[i+1] → ancilla[i]
            lines.append(f"CNOT {i + 1} {anc}")
            lines.append(f"DEPOLARIZE2({error_rate}) {i + 1} {anc}")

        # Measure + reset ancillae
        anc_list = " ".join(str(n_data + i) for i in range(n_ancilla))
        lines.append(f"MR {anc_list}")
        total_measurements += measurements_per_round

        # Detectors: compare this round to previous round
        for i in range(n_ancilla):
            if rnd == 0:
                # First round: detector is just the measurement
                rec_idx = -(n_ancilla - i)
                lines.append(f"DETECTOR rec[{rec_idx}]")
            else:
                # Compare to previous round's corresponding measurement
                rec_this = -(n_ancilla - i)
                rec_prev = rec_this - measurements_per_round
                lines.append(f"DETECTOR rec[{rec_this}] rec[{rec_prev}]")

    # Final data qubit measurements
    data_list = " ".join(str(q) for q in range(n_data))
    lines.append(f"M {data_list}")
    total_measurements += n_data

    # Observable: parity of all data qubits (logical Z)
    rec_refs = " ".join(f"rec[{-(n_data - q)}]" for q in range(n_data))
    lines.append(f"OBSERVABLE_INCLUDE(0) {rec_refs}")

    return "\n".join(lines)


def measure_circuit(circuit_str: str, shots: int = 50_000) -> dict:
    """Run circuit through Tsim and measure detector/observable statistics."""
    if tsim is None:
        return {"logical_error_rate": np.nan, "detector_rates": [], "dry_run": True}

    circuit = tsim.Circuit(circuit_str)

    t0 = time.time()
    sampler = circuit.compile_detector_sampler()
    samples = sampler.sample(
        shots=shots,
        append_observables=True,
    )
    elapsed = time.time() - t0

    n_detectors = circuit.num_detectors
    detector_samples = samples[:, :n_detectors]
    observable_samples = samples[:, n_detectors:]

    # Use reference sample for proper comparison
    sampler_ref = circuit.compile_detector_sampler()
    ref_samples = sampler_ref.sample(
        shots=shots,
        use_detector_reference_sample=True,
        use_observable_reference_sample=True,
        append_observables=True,
    )

    obs_flips = ref_samples[:, n_detectors:]
    logical_error_rate = float(np.mean(obs_flips[:, 0])) if obs_flips.shape[1] > 0 else 0.0

    det_ref = ref_samples[:, :n_detectors]
    detector_rates = [float(np.mean(det_ref[:, d])) for d in range(n_detectors)]

    return {
        "logical_error_rate": logical_error_rate,
        "detector_rates": detector_rates,
        "n_detectors": n_detectors,
        "shots": shots,
        "elapsed_s": elapsed,
    }


# ============================================================
# Main test runner
# ============================================================

def run_structure_theorem_test():
    """Run both sub-tests of the Structure Theorem."""

    all_results = {}

    # ── Test 1A: Differential noise ──
    print("=" * 70)
    print("TEST 1A: Differential Noise — Realistic T-gate overhead")
    print("=" * 70)

    n_qubits = 9
    total_gates = 40
    clifford_error = 0.005
    t_noise_factor = 5.0  # T-gates 5× noisier (conservative)
    shots = 100_000

    t_fractions = [0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.60, 0.80]

    print(f"Config: {n_qubits} qubits, {total_gates} gates, "
          f"p_cliff={clifford_error}, T_factor={t_noise_factor}×, {shots} shots")
    print(f"Prediction: convex (super-linear) error curve")
    print("-" * 70)
    print(f"{'T-frac':>7} {'N_T':>5} {'N_Cl':>5} {'LogErr':>10} "
          f"{'ΔErr':>10} {'Marginal':>10} {'Time(s)':>8}")
    print("-" * 70)

    results_1a = []
    baseline_err = None

    for t_frac in t_fractions:
        n_t = int(total_gates * t_frac)
        n_cliff = total_gates - n_t

        circuit_str = build_differential_noise_circuit(
            n_qubits, n_t, n_cliff, clifford_error, t_noise_factor
        )
        result = measure_circuit(circuit_str, shots)

        err = result["logical_error_rate"]
        if baseline_err is None:
            baseline_err = err
        delta_err = err - baseline_err
        marginal = delta_err / max(n_t, 1)
        elapsed = result.get("elapsed_s", 0)

        print(f"{t_frac:>7.2f} {n_t:>5} {n_cliff:>5} {err:>10.6f} "
              f"{delta_err:>10.6f} {marginal:>10.6f} {elapsed:>8.2f}")

        results_1a.append({
            "t_fraction": t_frac,
            "n_t_gates": n_t,
            "n_clifford_gates": n_cliff,
            "logical_error_rate": err,
            "delta_from_baseline": delta_err,
            "marginal_cost": marginal,
            "detector_rates": result.get("detector_rates", []),
            "elapsed_s": elapsed,
            "dry_run": result.get("dry_run", False),
        })

    # Analyze 1A convexity
    verdict_1a = "DRY_RUN"
    if results_1a and not results_1a[0].get("dry_run", False):
        nonzero = [(r["t_fraction"], r["logical_error_rate"])
                    for r in results_1a if r["t_fraction"] > 0]
        if len(nonzero) >= 3:
            x = np.array([p[0] for p in nonzero])
            y = np.array([p[1] for p in nonzero])
            coeffs = np.polyfit(x, y, 2)
            a, b, c = coeffs

            print(f"\n  Quadratic fit: err = {a:.4f}·t² + {b:.4f}·t + {c:.4f}")
            print(f"  Quadratic coeff a = {a:.6f}")

            if a > 0 and abs(a) > abs(b) * 0.05:
                verdict_1a = "CONVEX_SUPPORTED"
                print(f"  ✓ CONVEX (a > 0) — Structure Theorem SUPPORTED")
            elif abs(a) < abs(b) * 0.05:
                verdict_1a = "LINEAR_INCONCLUSIVE"
                print(f"  ~ LINEAR — Structure Theorem INCONCLUSIVE")
            else:
                verdict_1a = "CONCAVE_CHALLENGED"
                print(f"  ✗ CONCAVE (a < 0) — Structure Theorem CHALLENGED")

            # Marginal cost analysis
            marginals = [r["marginal_cost"] for r in results_1a if r["n_t_gates"] > 0]
            t_vals = [r["t_fraction"] for r in results_1a if r["n_t_gates"] > 0]
            if len(marginals) >= 3:
                m_slope = np.polyfit(t_vals, marginals, 1)[0]
                print(f"  Marginal cost slope: {m_slope:.6f} "
                      f"({'increasing' if m_slope > 0 else 'decreasing'})")

            for r in results_1a:
                r["verdict"] = verdict_1a
                r["quadratic_a"] = float(a)

    all_results["test_1a"] = {
        "name": "Differential noise (realistic T-gate overhead)",
        "t_noise_factor": t_noise_factor,
        "verdict": verdict_1a,
        "results": results_1a,
    }

    # ── Test 1B: Syndrome degradation ──
    print("\n" + "=" * 70)
    print("TEST 1B: Syndrome Degradation — T-gates degrade error correction")
    print("=" * 70)

    n_data = 7           # 7-qubit repetition code
    n_rounds = 4         # 4 syndrome extraction rounds
    error_rate = 0.01    # uniform noise (testing pure non-Clifford effect)
    shots_1b = 50_000

    t_per_round_values = [0, 1, 2, 4, 6, 8, 12, 16]

    print(f"Config: {n_data}-qubit repetition code, {n_rounds} rounds, "
          f"p_err={error_rate}, {shots_1b} shots")
    print(f"Prediction: more T-gates per round → worse error correction")
    print("-" * 70)
    print(f"{'T/round':>8} {'Total_T':>8} {'LogErr':>10} {'DetRate':>10} "
          f"{'Time(s)':>8}")
    print("-" * 70)

    results_1b = []
    for n_t_per_round in t_per_round_values:
        circuit_str = build_syndrome_degradation_circuit(
            n_data, n_rounds, n_t_per_round, error_rate
        )
        result = measure_circuit(circuit_str, shots_1b)

        err = result["logical_error_rate"]
        mean_det = np.mean(result.get("detector_rates", [0]))
        elapsed = result.get("elapsed_s", 0)
        total_t = n_t_per_round * n_rounds

        print(f"{n_t_per_round:>8} {total_t:>8} {err:>10.6f} {mean_det:>10.6f} "
              f"{elapsed:>8.2f}")

        results_1b.append({
            "t_per_round": n_t_per_round,
            "total_t_gates": total_t,
            "logical_error_rate": err,
            "mean_detector_rate": float(mean_det),
            "detector_rates": result.get("detector_rates", []),
            "elapsed_s": elapsed,
            "dry_run": result.get("dry_run", False),
        })

    # Analyze 1B
    verdict_1b = "DRY_RUN"
    if results_1b and not results_1b[0].get("dry_run", False):
        t_counts = [r["total_t_gates"] for r in results_1b]
        errs = [r["logical_error_rate"] for r in results_1b]

        if len(t_counts) >= 3:
            x = np.array(t_counts, dtype=float)
            y = np.array(errs)
            coeffs = np.polyfit(x, y, 2)
            a, b, c = coeffs

            print(f"\n  Quadratic fit: err = {a:.6e}·N² + {b:.6e}·N + {c:.4f}")
            print(f"  Quadratic coeff a = {a:.6e}")

            if a > 0 and abs(a) > abs(b) * 0.01:
                verdict_1b = "CONVEX_SUPPORTED"
                print(f"  ✓ CONVEX — syndrome degradation accelerates with T-count")
            elif abs(a) < abs(b) * 0.01:
                verdict_1b = "LINEAR_INCONCLUSIVE"
                print(f"  ~ LINEAR — degradation is constant per T-gate")
            else:
                verdict_1b = "CONCAVE_CHALLENGED"
                print(f"  ✗ CONCAVE — diminishing degradation")

            for r in results_1b:
                r["verdict"] = verdict_1b
                r["quadratic_a"] = float(a)

    all_results["test_1b"] = {
        "name": "Syndrome degradation (equal noise, non-Clifford interference)",
        "verdict": verdict_1b,
        "results": results_1b,
    }

    # ── Combined verdict ──
    print("\n" + "=" * 70)
    print("COMBINED VERDICT")
    print(f"  Test 1A (differential noise): {verdict_1a}")
    print(f"  Test 1B (syndrome degradation): {verdict_1b}")

    if "SUPPORTED" in verdict_1a and "SUPPORTED" in verdict_1b:
        print("  OVERALL: Structure Theorem SUPPORTED on quantum substrate")
        print("  Both resource cost AND information-theoretic penalty confirmed")
    elif "SUPPORTED" in verdict_1a or "SUPPORTED" in verdict_1b:
        print("  OVERALL: PARTIAL SUPPORT — one mechanism confirmed")
    else:
        print("  OVERALL: Structure Theorem NOT CONFIRMED in this setup")
    print("=" * 70)

    # Save all results
    out_path = Path(__file__).parent / "results_test1_structure_theorem.json"
    with open(out_path, "w") as f:
        json.dump({
            "test": "Structure Theorem (Fantasia Bound) on QEC",
            "prediction": "Convex error curve — super-linear cost per T-gate",
            "framework_section": "§2B₂ (Structure Theorem), §58H (Eckert manifold)",
            "sub_tests": {
                "1A": "Differential noise: T-gates 5× noisier (realistic overhead)",
                "1B": "Syndrome degradation: equal noise, repetition code with syndrome rounds",
            },
            "params_1a": {
                "n_qubits": n_qubits,
                "total_gates": total_gates,
                "clifford_error": clifford_error,
                "t_noise_factor": t_noise_factor,
                "shots": shots,
            },
            "params_1b": {
                "n_data": n_data,
                "n_rounds": n_rounds,
                "error_rate": error_rate,
                "shots": shots_1b,
            },
            "results": all_results,
        }, f, indent=2)

    print(f"\nResults saved to {out_path}")
    return all_results


if __name__ == "__main__":
    run_structure_theorem_test()
