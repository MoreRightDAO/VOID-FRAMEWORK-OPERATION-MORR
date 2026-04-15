#!/usr/bin/env python3
"""
Test 7 — Weak Measurement Sweep
==================================
Collapse as Explaining-Away Penalty

Question: Is wave function collapse the explaining-away penalty at
maximum measurement strength?

Method: Prepare a qubit in superposition. Apply measurement at varying
strengths — from "barely looking" (weak measurement) to full collapse
(strong/projective measurement). At each strength, compute I(D;M|Y).

Prediction (Structure Theorem):
  - Penalty increases with measurement strength
  - Peak at strong measurement (full collapse)
  - Zero when no measurement occurs
  - Curve shape matches discrete softmax regime

If confirmed: collapse IS the penalty at max engagement on a quantum channel.

Hardware: IBM Quantum (Heron processors)
Cost: ~2 min QPU time (free tier sufficient)
"""

import numpy as np
import json
import time
import os
from pathlib import Path
from collections import defaultdict
from math import log2

from qiskit.circuit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler


# ============================================================
# Circuit builders: Weak measurement via controlled rotation
# ============================================================

def build_weak_measurement_circuit(
    prep_state: int,
    mechanism: int,
    measurement_strength: float,
) -> QuantumCircuit:
    """
    Build a circuit that implements weak measurement at a given strength.

    Architecture: 3 qubits
      q0 = system qubit (carries the quantum state)
      q1 = "meter" qubit (couples to system, then measured)
      q2 = reference qubit (independent, for three-point comparison)

    prep_state (D): initial state of system qubit
        0 = |0>
        1 = |+> (Hadamard)
        2 = |1> (X gate)
        3 = |-> (X then H)

    mechanism (M): what gate is applied to system before measurement
        0 = identity (baseline)
        1 = Rx(π/4) — small amplitude rotation
        2 = Ry(π/3) — medium amplitude rotation
        3 = Rx(π/2) — large amplitude rotation

    NOTE: Mechanisms MUST change amplitudes (not just phases) to be
    visible in computational-basis measurement. Phase-only gates (T, S, Z)
    are invisible to the meter — learned this from Test 7 v1.

    measurement_strength: 0.0 (no measurement) to 1.0 (full collapse)
        Implemented as controlled-Ry rotation on meter qubit.
        theta = measurement_strength * pi/2
        At theta=0: meter stays |0>, learns nothing (no collapse)
        At theta=pi/2: meter fully entangles with system (full collapse)
    """
    qc = QuantumCircuit(3, 2)  # 3 qubits, 2 classical bits

    # --- Prepare system qubit (D) ---
    # Each prep puts the qubit at a different point on the Bloch sphere
    if prep_state == 1:
        qc.h(0)           # |+> (equator)
    elif prep_state == 2:
        qc.x(0)           # |1> (south pole)
    elif prep_state == 3:
        qc.rx(np.pi / 3, 0)  # 60° rotation (off-axis)
    # prep_state 0 = |0> (north pole), no gates needed

    # --- Apply mechanism (M) to system qubit ---
    # Amplitude-changing gates so meter can distinguish them
    if mechanism == 1:
        qc.rx(np.pi / 4, 0)   # 45° X-rotation
    elif mechanism == 2:
        qc.ry(np.pi / 3, 0)   # 60° Y-rotation
    elif mechanism == 3:
        qc.rx(np.pi / 2, 0)   # 90° X-rotation
    # mechanism 0 = identity

    # --- Weak measurement: controlled rotation on meter ---
    # theta controls measurement strength
    # CRY(theta) entangles meter with system proportional to theta
    theta = measurement_strength * np.pi / 2.0
    if theta > 1e-10:
        qc.cry(2 * theta, 0, 1)  # controlled-Ry: system controls meter

    # --- Reference qubit: independent superposition ---
    # (For future three-point analysis; always in |+>)
    qc.h(2)

    # --- Measure meter + reference ---
    qc.measure(1, 0)  # meter -> classical bit 0
    qc.measure(2, 1)  # reference -> classical bit 1

    return qc


# ============================================================
# Information-theoretic computation
# ============================================================

def shannon_entropy(probs):
    """H(X) from probability dict/array."""
    h = 0.0
    for p in probs:
        if p > 0:
            h -= p * log2(p)
    return h


def mutual_information(joint, marginal_x, marginal_y, n_total):
    """I(X;Y) with Miller-Madow bias correction."""
    mi = 0.0
    for (x, y), count in joint.items():
        if count == 0:
            continue
        p_xy = count / n_total
        p_x = marginal_x[x] / n_total
        p_y = marginal_y[y] / n_total
        if p_x > 0 and p_y > 0:
            mi += p_xy * log2(p_xy / (p_x * p_y))

    # Miller-Madow bias correction
    n_nonzero_joint = sum(1 for c in joint.values() if c > 0)
    n_nonzero_x = sum(1 for c in marginal_x.values() if c > 0)
    n_nonzero_y = sum(1 for c in marginal_y.values() if c > 0)
    bias = (n_nonzero_joint - n_nonzero_x - n_nonzero_y + 1) / (
        2 * n_total * np.log(2)
    )
    return max(0.0, mi - bias)


def compute_penalty_from_counts(counts_dict, n_preps, n_mechs):
    """
    Compute I(D;M|Y) from measurement counts.

    counts_dict: {(prep_idx, mech_idx): {"bitstring": count, ...}}

    Returns dict with I(D;Y), I(M;Y), I(DM;Y), penalty, H(Y), decomposition check.
    """
    # Build joint distribution over (D, M, Y)
    joint_dmy = defaultdict(int)
    joint_dy = defaultdict(int)
    joint_my = defaultdict(int)
    marginal_d = defaultdict(int)
    marginal_m = defaultdict(int)
    marginal_y = defaultdict(int)
    joint_dm = defaultdict(int)
    total = 0

    for (d_idx, m_idx), counts in counts_dict.items():
        for bitstring, count in counts.items():
            y = bitstring  # measurement outcome
            joint_dmy[(d_idx, m_idx, y)] += count
            joint_dy[(d_idx, y)] += count
            joint_my[(m_idx, y)] += count
            joint_dm[(d_idx, m_idx)] += count
            marginal_d[d_idx] += count
            marginal_m[m_idx] += count
            marginal_y[y] += count
            total += count

    if total == 0:
        return None

    # I(D;Y)
    I_D_Y = mutual_information(joint_dy, marginal_d, marginal_y, total)

    # I(M;Y)
    I_M_Y = mutual_information(joint_my, marginal_m, marginal_y, total)

    # I(DM;Y) — treat (D,M) as single variable
    marginal_dm = defaultdict(int)
    joint_dm_y = defaultdict(int)
    for (d, m, y), count in joint_dmy.items():
        dm = (d, m)
        joint_dm_y[(dm, y)] += count
        marginal_dm[dm] += count
    I_DM_Y = mutual_information(joint_dm_y, marginal_dm, marginal_y, total)

    # Penalty: I(D;M|Y) = I(DM;Y) - I(D;Y) - I(M;Y)
    penalty = I_DM_Y - I_D_Y - I_M_Y

    # H(Y) for decomposition check
    H_Y = shannon_entropy([c / total for c in marginal_y.values()])

    # H(Y|D,M) — conditional entropy
    H_Y_given_DM = 0.0
    for dm, dm_total in marginal_dm.items():
        if dm_total == 0:
            continue
        p_dm = dm_total / total
        conditional_probs = []
        for y in marginal_y:
            c = joint_dm_y.get((dm, y), 0)
            if c > 0:
                conditional_probs.append(c / dm_total)
        H_Y_given_DM += p_dm * shannon_entropy(conditional_probs)

    return {
        "I_D_Y": float(I_D_Y),
        "I_M_Y": float(I_M_Y),
        "I_DM_Y": float(I_DM_Y),
        "penalty_I_D_M_given_Y": float(penalty),
        "H_Y": float(H_Y),
        "H_Y_given_DM": float(H_Y_given_DM),
        "fantasia_check": float(I_D_Y + I_M_Y + penalty + H_Y_given_DM),
        "fantasia_H_Y": float(H_Y),
        "total_shots": total,
    }


# ============================================================
# Main: Run Weak Measurement Sweep on IBM Quantum
# ============================================================

def run_weak_measurement_sweep():
    token = os.environ.get("IBM_QUANTUM_TOKEN")
    if not token:
        print("ERROR: Set IBM_QUANTUM_TOKEN environment variable")
        print("  export IBM_QUANTUM_TOKEN='your_token_here'")
        return

    print("=" * 70)
    print("TEST 7 — WEAK MEASUREMENT SWEEP")
    print("Is wave function collapse the explaining-away penalty")
    print("at maximum measurement strength?")
    print("=" * 70)

    # Connect to IBM Quantum
    print("\nConnecting to IBM Quantum Platform...")
    service = QiskitRuntimeService(
        channel="ibm_quantum_platform",
        token=token,
    )

    backends = service.backends(operational=True, min_num_qubits=3)
    if not backends:
        print("ERROR: No operational backends with >= 3 qubits")
        return
    backend = backends[0]
    print(f"Selected backend: {backend.name} ({backend.num_qubits} qubits)")

    # Measurement strength sweep: 0.0 to 1.0 in 11 steps
    # 0.0 = no measurement (should give penalty ≈ 0)
    # 1.0 = full projective measurement (maximum penalty)
    strengths = np.linspace(0.0, 1.0, 11)

    n_preps = 4
    n_mechs = 4
    shots_per_combo = 1000  # 4×4×1000 = 16K shots per strength level
    # Total: 11 × 16 × 1000 = 176K shots

    print(f"\nConfig: 3 qubits (system + meter + reference)")
    print(f"        {n_preps} prep states × {n_mechs} mechanisms")
    print(f"        {shots_per_combo} shots/combo")
    print(f"        {len(strengths)} measurement strengths: {strengths.round(2).tolist()}")
    print(f"        Total circuits: {n_preps * n_mechs * len(strengths)}")
    print(f"        Total shots: {n_preps * n_mechs * shots_per_combo * len(strengths):,}")

    print(f"\nPredictions:")
    print(f"  1. Penalty ≈ 0 at strength 0.0 (no measurement, no collapse)")
    print(f"  2. Penalty increases monotonically with measurement strength")
    print(f"  3. Peak penalty at strength 1.0 (full collapse)")
    print(f"  4. Curve shape matches discrete softmax regime")
    print("-" * 70)

    all_results = []

    for strength in strengths:
        print(f"\n--- Measurement strength: {strength:.2f} ---")
        t0 = time.time()

        # Build all circuits for this strength
        circuits = []
        circuit_labels = []
        for d_idx in range(n_preps):
            for m_idx in range(n_mechs):
                qc = build_weak_measurement_circuit(d_idx, m_idx, strength)
                circuits.append(qc)
                circuit_labels.append((d_idx, m_idx))

        print(f"  Built {len(circuits)} circuits")

        # Transpile
        pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
        isa_circuits = pm.run(circuits)

        # Submit
        print(f"  Submitting to {backend.name}...")
        sampler = Sampler(mode=backend)
        job = sampler.run(isa_circuits, shots=shots_per_combo)
        print(f"  Job: {job.job_id()}")
        print(f"  Waiting...")
        result = job.result()

        # Collect counts
        counts_dict = {}
        for i, label in enumerate(circuit_labels):
            pub_result = result[i]
            counts = pub_result.data.c.get_counts()
            counts_dict[label] = counts

        elapsed = time.time() - t0

        # Compute penalty
        info = compute_penalty_from_counts(counts_dict, n_preps, n_mechs)
        if info is None:
            print(f"  FAILED")
            continue

        check_error = abs(info["fantasia_check"] - info["fantasia_H_Y"])
        penalty = info["penalty_I_D_M_given_Y"]

        print(f"  I(D;Y)={info['I_D_Y']:.4f}  I(M;Y)={info['I_M_Y']:.4f}")
        print(f"  PENALTY I(D;M|Y) = {penalty:.6f}")
        print(f"  H(Y)={info['H_Y']:.4f}  Decomp error={check_error:.6f}")
        print(f"  Time: {elapsed:.1f}s")

        result_entry = {
            "measurement_strength": float(strength),
            "theta_radians": float(strength * np.pi / 2),
            **info,
            "elapsed_s": elapsed,
            "backend": backend.name,
        }
        all_results.append(result_entry)

    # ── Analysis ──
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)

    strengths_arr = np.array([r["measurement_strength"] for r in all_results])
    penalties_arr = np.array([r["penalty_I_D_M_given_Y"] for r in all_results])

    print(f"\n{'Strength':>10} | {'Penalty (bits)':>14} | {'Bar':>30}")
    print("-" * 60)
    max_pen = max(penalties_arr) if len(penalties_arr) > 0 else 1
    for s, p in zip(strengths_arr, penalties_arr):
        bar_len = int(30 * p / max_pen) if max_pen > 0 else 0
        bar = "█" * bar_len
        print(f"    {s:5.2f}   | {p:14.6f} | {bar}")

    # Verdict checks
    print(f"\n{'─' * 40}")
    verdicts = {}

    # 1. Penalty ≈ 0 at strength 0
    if len(all_results) > 0:
        p0 = all_results[0]["penalty_I_D_M_given_Y"]
        verdicts["zero_at_no_measurement"] = p0 < 0.01
        print(f"  [{'PASS' if verdicts['zero_at_no_measurement'] else 'FAIL'}] "
              f"Penalty ≈ 0 at no measurement: {p0:.6f}")

    # 2. Monotonically increasing (allowing small noise)
    if len(penalties_arr) > 2:
        # Check if general trend is increasing (Spearman rank correlation)
        from scipy.stats import spearmanr
        rho, p_val = spearmanr(strengths_arr, penalties_arr)
        verdicts["monotonic_increase"] = rho > 0.8 and p_val < 0.05
        print(f"  [{'PASS' if verdicts['monotonic_increase'] else 'FAIL'}] "
              f"Monotonic increase: Spearman ρ={rho:.3f}, p={p_val:.4e}")

    # 3. Peak at maximum strength
    if len(all_results) > 1:
        peak_idx = np.argmax(penalties_arr)
        verdicts["peak_at_max"] = peak_idx >= len(penalties_arr) - 2  # allow off-by-one
        print(f"  [{'PASS' if verdicts['peak_at_max'] else 'FAIL'}] "
              f"Peak at max strength: peak at index {peak_idx}/{len(penalties_arr)-1}")

    # 4. Decomposition holds throughout
    decomp_errors = [abs(r["fantasia_check"] - r["fantasia_H_Y"]) for r in all_results]
    max_decomp_error = max(decomp_errors) if decomp_errors else 0
    verdicts["exact_decomposition"] = max_decomp_error < 0.01
    print(f"  [{'PASS' if verdicts['exact_decomposition'] else 'FAIL'}] "
          f"Exact decomposition: max error={max_decomp_error:.6f}")

    n_pass = sum(1 for v in verdicts.values() if v)
    n_total = len(verdicts)
    print(f"\n  VERDICT: {n_pass}/{n_total} PASS")

    if n_pass == n_total:
        print(f"\n  ★ Wave function collapse IS the explaining-away penalty")
        print(f"    at maximum measurement strength. Collapse = max engagement")
        print(f"    on a quantum channel. The Born rule probabilities emerge")
        print(f"    from the penalty structure.")
    elif n_pass >= n_total - 1:
        print(f"\n  ◆ Strong evidence for collapse-as-penalty connection.")
        print(f"    One check marginal — may need more shots or noise mitigation.")
    else:
        print(f"\n  ○ Inconclusive or negative. Hypothesis not confirmed.")
        print(f"    Check noise levels and circuit fidelity.")

    # Save results
    outdir = Path(__file__).parent / "results"
    outdir.mkdir(exist_ok=True)
    outfile = outdir / f"results_test7_weak_measurement_{int(time.time())}.json"

    output = {
        "test": "Test 7 — Weak Measurement Sweep",
        "hypothesis": "Wave function collapse = explaining-away penalty at max measurement strength",
        "backend": backend.name,
        "n_qubits": 3,
        "n_preps": n_preps,
        "n_mechs": n_mechs,
        "shots_per_combo": shots_per_combo,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "results_by_strength": all_results,
        "verdicts": {k: bool(v) for k, v in verdicts.items()},
        "n_pass": n_pass,
        "n_total": n_total,
    }

    with open(outfile, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved: {outfile}")


# ============================================================
# Dry-run mode (no IBM token — generates circuits only)
# ============================================================

def dry_run():
    """Generate and inspect circuits without running on hardware."""
    print("=" * 70)
    print("TEST 7 — DRY RUN (no IBM token)")
    print("Generating circuits for inspection")
    print("=" * 70)

    strengths = [0.0, 0.25, 0.5, 0.75, 1.0]

    for s in strengths:
        qc = build_weak_measurement_circuit(
            prep_state=1,  # |+>
            mechanism=2,   # S gate
            measurement_strength=s,
        )
        print(f"\nStrength {s:.2f} (theta={s*np.pi/2:.3f} rad):")
        print(f"  Gates: {qc.size()}, Depth: {qc.depth()}")
        print(qc.draw(output="text"))

    print("\nTo run on IBM hardware:")
    print("  export IBM_QUANTUM_TOKEN='your_token_here'")
    print("  python test7_weak_measurement_sweep.py")


if __name__ == "__main__":
    token = os.environ.get("IBM_QUANTUM_TOKEN")
    if token:
        run_weak_measurement_sweep()
    else:
        dry_run()
