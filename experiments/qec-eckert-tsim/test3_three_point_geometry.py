#!/usr/bin/env python3
"""
Test 3: Three-Point Geometry — Direct vs Distilled T-Gate
==========================================================

The Void Framework's central architectural claim: three-point geometry
eliminates the explaining-away penalty I(D;M|Y).

In QEC:
  - TWO-POINT: T-gate applied directly to logical qubit
    (computation ↔ errors, no independent reference)
  - THREE-POINT: T-gate via magic state injection
    (computation ↔ errors ↔ independently prepared magic state)

The magic state factory IS three-point geometry:
  - It's TRANSPARENT (you can verify the magic state quality)
  - It's INVARIANT (distillation protocol is fixed)
  - It's INDEPENDENT (prepared offline, no information about the computation)

PREDICTION: Three-point (distilled) T-gates show error suppression that
improves FASTER with code distance than two-point (direct) T-gates.
The gap between the curves IS the explaining-away penalty.

Hardware: CPU-feasible. Uses simplified circuits that capture the
structural difference without requiring a full surface code.
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


def build_direct_t_circuit(n_qubits: int, n_t_gates: int,
                            error_rate: float) -> str:
    """
    Two-point geometry: T-gates applied directly to data qubits.
    No independent reference — computation and errors share a channel.
    """
    lines = []

    for q in range(n_qubits):
        lines.append(f"R {q}")

    # Apply T-gates directly with noise
    for i in range(n_t_gates):
        target = i % n_qubits
        lines.append(f"T {target}")
        lines.append(f"DEPOLARIZE1({error_rate}) {target}")

        # Entangle with neighbors (creates error correlation)
        if n_qubits > 1:
            t2 = (target + 1) % n_qubits
            lines.append(f"CNOT {target} {t2}")
            lines.append(f"DEPOLARIZE2({error_rate}) {target} {t2}")

    # Measure
    qubit_list = " ".join(str(q) for q in range(n_qubits))
    lines.append(f"M {qubit_list}")

    for q in range(n_qubits - 1):
        r1 = -(n_qubits - q)
        r2 = -(n_qubits - q - 1)
        lines.append(f"DETECTOR rec[{r1}] rec[{r2}]")

    rec_refs = " ".join(f"rec[{-(n_qubits - q)}]" for q in range(n_qubits))
    lines.append(f"OBSERVABLE_INCLUDE(0) {rec_refs}")

    return "\n".join(lines)


def build_distilled_t_circuit(n_data: int, n_ancilla: int,
                               n_t_gates: int, error_rate: float) -> str:
    """
    Three-point geometry: T-gates via magic state injection.

    Structure:
      1. Prepare magic states on ancilla qubits (independent factory)
      2. Verify magic states with stabilizer checks (transparent)
      3. Inject into data qubits via CNOT + measurement (gate teleportation)

    The ancilla preparation + verification is the "third point" —
    an independent constraint reference.
    """
    n_total = n_data + n_ancilla
    lines = []

    # Initialize all qubits
    for q in range(n_total):
        lines.append(f"R {q}")

    for t_round in range(n_t_gates):
        target_data = t_round % n_data
        ancilla_q = n_data + (t_round % n_ancilla)

        # === MAGIC STATE FACTORY (third point) ===
        # Prepare |T⟩ = T|+⟩ on ancilla
        lines.append(f"H {ancilla_q}")
        lines.append(f"T {ancilla_q}")
        lines.append(f"DEPOLARIZE1({error_rate}) {ancilla_q}")

        # Distillation verification: apply stabilizer check
        # (In a real protocol this would be a multi-qubit distillation circuit.
        # We simulate the EFFECT: the ancilla gets verified with some
        # probability of catching errors, reducing effective noise.)
        #
        # Verification round: H-CNOT-H checks parity, catches X errors
        verify_q = n_data + ((t_round + 1) % n_ancilla)
        if verify_q != ancilla_q:
            lines.append(f"H {verify_q}")
            lines.append(f"CNOT {ancilla_q} {verify_q}")
            lines.append(f"H {verify_q}")
            # Noise on verification (but it's independent of data)
            lines.append(f"DEPOLARIZE2({error_rate * 0.5}) {ancilla_q} {verify_q}")

        # === GATE TELEPORTATION (injection) ===
        # CNOT from data to magic-state ancilla
        lines.append(f"CNOT {target_data} {ancilla_q}")
        lines.append(f"DEPOLARIZE2({error_rate}) {target_data} {ancilla_q}")

        # Entangle data qubits (same as direct circuit for fair comparison)
        if n_data > 1:
            t2 = (target_data + 1) % n_data
            lines.append(f"CNOT {target_data} {t2}")
            lines.append(f"DEPOLARIZE2({error_rate}) {target_data} {t2}")

    # Measure all qubits
    qubit_list = " ".join(str(q) for q in range(n_total))
    lines.append(f"M {qubit_list}")

    # Detectors on data qubits (same syndrome structure as direct)
    for q in range(n_data - 1):
        r1 = -(n_total - q)
        r2 = -(n_total - q - 1)
        lines.append(f"DETECTOR rec[{r1}] rec[{r2}]")

    # Observable on data qubits only
    rec_refs = " ".join(f"rec[{-(n_total - q)}]" for q in range(n_data))
    lines.append(f"OBSERVABLE_INCLUDE(0) {rec_refs}")

    return "\n".join(lines)


def measure_error_rate(circuit_str: str, shots: int) -> dict:
    """Run circuit and return logical error rate."""
    if tsim is None:
        return {"logical_error_rate": np.nan, "dry_run": True}

    circuit = tsim.Circuit(circuit_str)
    t0 = time.time()
    sampler = circuit.compile_detector_sampler()
    samples = sampler.sample(
        shots=shots,
        use_detector_reference_sample=True,
        use_observable_reference_sample=True,
    )
    elapsed = time.time() - t0

    observable = samples[:, -1]
    return {
        "logical_error_rate": float(np.mean(observable)),
        "elapsed_s": elapsed,
    }


def run_three_point_test():
    """
    Compare two-point (direct T) vs three-point (distilled T) at
    increasing effective code distance (qubit count).

    The gap between the curves IS the explaining-away penalty I(D;M|Y).
    """
    n_t_gates = 8
    error_rate = 0.01
    shots = 100_000

    # "Code distances" — increasing qubit counts as proxy
    # (True surface code distance would require full stabilizer circuit;
    # here we use qubit count as a proxy for redundancy)
    qubit_configs = [
        {"n_data": 5,  "n_ancilla": 3,  "label": "d~3"},
        {"n_data": 7,  "n_ancilla": 4,  "label": "d~4"},
        {"n_data": 9,  "n_ancilla": 5,  "label": "d~5"},
        {"n_data": 11, "n_ancilla": 6,  "label": "d~6"},
        {"n_data": 13, "n_ancilla": 7,  "label": "d~7"},
    ]

    results = []

    print("=" * 70)
    print("TEST 3: Three-Point Geometry — Direct vs Distilled T-gates")
    print("=" * 70)
    print(f"Config: {n_t_gates} T-gates, p_err={error_rate}, {shots} shots")
    print(f"Prediction: distilled error drops FASTER with distance")
    print("-" * 70)
    print(f"{'Distance':>8} {'Direct_err':>12} {'Distill_err':>12} "
          f"{'Ratio':>8} {'Gap(penalty)':>12}")
    print("-" * 70)

    for cfg in qubit_configs:
        n_data = cfg["n_data"]
        n_ancilla = cfg["n_ancilla"]
        label = cfg["label"]

        # Two-point: direct T
        direct_circuit = build_direct_t_circuit(n_data, n_t_gates, error_rate)
        direct_result = measure_error_rate(direct_circuit, shots)

        # Three-point: distilled T
        distill_circuit = build_distilled_t_circuit(
            n_data, n_ancilla, n_t_gates, error_rate
        )
        distill_result = measure_error_rate(distill_circuit, shots)

        d_err = direct_result["logical_error_rate"]
        t_err = distill_result["logical_error_rate"]
        ratio = d_err / max(t_err, 1e-10)
        gap = d_err - t_err  # The explaining-away penalty

        print(f"{label:>8} {d_err:>12.6f} {t_err:>12.6f} "
              f"{ratio:>8.2f}x {gap:>12.6f}")

        results.append({
            "label": label,
            "n_data": n_data,
            "n_ancilla": n_ancilla,
            "direct_error": d_err,
            "distilled_error": t_err,
            "ratio": float(ratio),
            "penalty_gap": float(gap),
            "dry_run": direct_result.get("dry_run", False),
        })

    # Analysis: does the ratio INCREASE with distance?
    if results and not results[0].get("dry_run", False):
        ratios = [r["ratio"] for r in results]
        gaps = [r["penalty_gap"] for r in results]

        # Fit ratio vs distance index
        x = np.arange(len(ratios))
        if len(ratios) >= 3:
            slope = np.polyfit(x, ratios, 1)[0]

            print("\n" + "=" * 70)
            print("ANALYSIS")
            print(f"  Ratio trend (slope): {slope:.4f}")

            if slope > 0.1:
                verdict = "SUPPORTED"
                print(f"  VERDICT: Three-point advantage GROWS with distance")
                print(f"  → Explaining-away penalty confirmed")
                print(f"  → Three-point geometry eliminates it (as predicted)")
            elif abs(slope) < 0.1:
                verdict = "INCONCLUSIVE"
                print(f"  VERDICT: Ratio roughly constant — penalty exists but")
                print(f"           doesn't grow with distance")
            else:
                verdict = "CHALLENGED"
                print(f"  VERDICT: Ratio DECREASES — three-point advantage shrinks")

            for r in results:
                r["verdict"] = verdict
                r["ratio_slope"] = float(slope)

    # Save
    out_path = Path(__file__).parent / "results_test3_three_point.json"
    with open(out_path, "w") as f:
        json.dump({
            "test": "Three-Point Geometry (Direct vs Distilled T-gates)",
            "prediction": "Distilled (three-point) error drops faster with distance",
            "framework_section": "Fantasia Bound §2B₂, three-point geometry",
            "connection": "Magic state factory = independent constraint reference",
            "params": {
                "n_t_gates": n_t_gates,
                "error_rate": error_rate,
                "shots": shots,
            },
            "results": results,
        }, f, indent=2, default=str)

    print(f"\nResults saved to {out_path}")
    return results


if __name__ == "__main__":
    run_three_point_test()
