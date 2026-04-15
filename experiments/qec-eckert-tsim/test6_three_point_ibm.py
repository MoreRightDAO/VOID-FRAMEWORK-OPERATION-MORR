#!/usr/bin/env python3
"""
Test 6: Three-Point Geometry Eliminates the Penalty — IBM Quantum Hardware
==========================================================================

PREVIOUS: Test 4 confirmed I(D;M|Y) > 0 on IBM Fez (5/5 measurements).
THIS TEST: Does three-point geometry REDUCE the penalty?

SETUP:
    Two-point: D → Circuit → Measure Y (standard setup from Test 4)
    Three-point: D → Circuit → Measure Y + Ancilla verification channel

    The "third point" is an ancilla qubit that independently verifies
    the circuit state via a CNOT from the data register. This creates
    an independent reference channel — the architectural fix the
    Fantasia Bound predicts should eliminate or reduce I(D;M|Y).

PREDICTION:
    1. Two-point penalty > 0 (confirmed by Test 4)
    2. Three-point penalty < Two-point penalty (the fix works)
    3. The reduction should be substantial, not marginal

If this works on real quantum hardware, we've demonstrated that the
architectural fix predicted by the Fantasia Bound actually works on
a physical substrate — not just in theory.
"""

import numpy as np
import json
import time
import os
from pathlib import Path
from collections import defaultdict

from qiskit.circuit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler


# ============================================================
# Circuit builders
# ============================================================

def build_two_point_circuit(n_data: int, prep_state: int, mechanism: int,
                            depth: int) -> QuantumCircuit:
    """Standard two-point circuit (same as Test 4)."""
    n_qubits = n_data
    qc = QuantumCircuit(n_qubits, n_qubits)

    # Prep state D
    if prep_state == 0:
        pass
    elif prep_state == 1:
        for q in range(n_qubits):
            qc.h(q)
    elif prep_state == 2:
        for q in range(1, n_qubits, 2):
            qc.x(q)
    elif prep_state == 3:
        qc.h(0)
        for q in range(n_qubits - 1):
            qc.cx(q, q + 1)

    # Mechanism M
    for layer in range(depth):
        if mechanism == 0:
            qc.barrier()
        elif mechanism == 1:
            for q in range(n_qubits):
                gate_choice = (q + layer) % 3
                if gate_choice == 0:
                    qc.h(q)
                elif gate_choice == 1:
                    qc.s(q)
                else:
                    t2 = (q + 1) % n_qubits
                    qc.cx(q, t2)
        elif mechanism == 2:
            for q in range(n_qubits):
                qc.t(q)
            for q in range(0, n_qubits - 1, 2):
                qc.cx(q, q + 1)
        elif mechanism == 3:
            for q in range(n_qubits):
                t2 = (q + 1) % n_qubits
                qc.cx(q, t2)

    qc.measure(range(n_qubits), range(n_qubits))
    return qc


def build_three_point_circuit(n_data: int, prep_state: int, mechanism: int,
                               depth: int) -> QuantumCircuit:
    """
    Three-point circuit: data qubits + ancilla verification channel.

    The ancilla qubits provide an INDEPENDENT reference — they observe
    the data register's state without being part of the D→M→Y channel.
    This is channel separation: the third point.

    Architecture:
        Data qubits [0..n_data-1]: prep state → mechanism → measure
        Ancilla qubits [n_data..2*n_data-1]: CNOT from data → measure

    The ancilla measurement provides an independent channel that the
    Fantasia Bound predicts should reduce I(D;M|Y).
    """
    n_total = n_data * 2  # data + ancilla
    qc = QuantumCircuit(n_total, n_total)

    # Prep state D (data qubits only)
    if prep_state == 0:
        pass
    elif prep_state == 1:
        for q in range(n_data):
            qc.h(q)
    elif prep_state == 2:
        for q in range(1, n_data, 2):
            qc.x(q)
    elif prep_state == 3:
        qc.h(0)
        for q in range(n_data - 1):
            qc.cx(q, q + 1)

    # Mechanism M (data qubits only)
    for layer in range(depth):
        if mechanism == 0:
            qc.barrier()
        elif mechanism == 1:
            for q in range(n_data):
                gate_choice = (q + layer) % 3
                if gate_choice == 0:
                    qc.h(q)
                elif gate_choice == 1:
                    qc.s(q)
                else:
                    t2 = (q + 1) % n_data
                    qc.cx(q, t2)
        elif mechanism == 2:
            for q in range(n_data):
                qc.t(q)
            for q in range(0, n_data - 1, 2):
                qc.cx(q, q + 1)
        elif mechanism == 3:
            for q in range(n_data):
                t2 = (q + 1) % n_data
                qc.cx(q, t2)

    # THREE-POINT: Ancilla verification channel
    # CNOT from each data qubit to its paired ancilla
    # This creates an independent observation of the data state
    qc.barrier()
    for q in range(n_data):
        qc.cx(q, n_data + q)

    # Measure everything
    qc.measure(range(n_total), range(n_total))
    return qc


# ============================================================
# Info-theoretic computation (same as Test 4)
# ============================================================

def entropy(probs):
    p = probs[probs > 0]
    return -np.sum(p * np.log2(p))


def estimate_mutual_info(joint_counts, marginal_x_counts, marginal_y_counts, total):
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
    n_nz_j = sum(1 for v in joint_counts.values() if v > 0)
    n_nz_x = sum(1 for v in marginal_x_counts.values() if v > 0)
    n_nz_y = sum(1 for v in marginal_y_counts.values() if v > 0)
    bias = (n_nz_j - n_nz_x - n_nz_y + 1) / (2 * total * np.log(2))
    return max(0.0, mi - bias)


def compute_penalty(counts_dict, n_d, n_m):
    joint_dmy = {}
    joint_dy = {}
    joint_my = {}
    marginal_y = {}
    total = 0

    for (d, m), counts in counts_dict.items():
        for bitstring, count in counts.items():
            y = bitstring
            joint_dmy[(d, m, y)] = joint_dmy.get((d, m, y), 0) + count
            joint_dy[(d, y)] = joint_dy.get((d, y), 0) + count
            joint_my[(m, y)] = joint_my.get((m, y), 0) + count
            marginal_y[y] = marginal_y.get(y, 0) + count
            total += count

    if total == 0:
        return None

    py = np.array(list(marginal_y.values())) / total
    H_Y = entropy(py)

    marginal_d = {}
    for (d, y), cnt in joint_dy.items():
        marginal_d[d] = marginal_d.get(d, 0) + cnt
    I_D_Y = estimate_mutual_info(joint_dy, marginal_d, marginal_y, total)

    marginal_m = {}
    for (m, y), cnt in joint_my.items():
        marginal_m[m] = marginal_m.get(m, 0) + cnt
    I_M_Y = estimate_mutual_info(joint_my, marginal_m, marginal_y, total)

    joint_dm_y = {}
    marginal_dm = {}
    for (d, m, y), cnt in joint_dmy.items():
        dm = (d, m)
        joint_dm_y[(dm, y)] = joint_dm_y.get((dm, y), 0) + cnt
        marginal_dm[dm] = marginal_dm.get(dm, 0) + cnt
    I_DM_Y = estimate_mutual_info(joint_dm_y, marginal_dm, marginal_y, total)

    penalty = I_DM_Y - I_D_Y - I_M_Y
    H_Y_given_DM = H_Y - I_DM_Y

    return {
        "I_D_Y": float(I_D_Y),
        "I_M_Y": float(I_M_Y),
        "I_DM_Y": float(I_DM_Y),
        "penalty": float(penalty),
        "H_Y": float(H_Y),
        "total_shots": total,
    }


# ============================================================
# Main
# ============================================================

def run_three_point_test():
    token = os.environ.get("IBM_QUANTUM_TOKEN")
    if not token:
        print("ERROR: Set IBM_QUANTUM_TOKEN environment variable")
        return

    print("=" * 70)
    print("TEST 6 — THREE-POINT GEOMETRY vs TWO-POINT")
    print("Does channel separation reduce the explaining-away penalty?")
    print("=" * 70)

    service = QiskitRuntimeService(channel='ibm_quantum_platform', token=token)
    backends = service.backends(operational=True)
    backend = backends[0]
    print(f"Backend: {backend.name} ({backend.num_qubits} qubits)")

    n_data = 4  # 4 data qubits (+ 4 ancilla for three-point = 8 total)
    n_preps = 4
    n_mechs = 4
    shots = 1000

    # Test at depths where we saw penalty in Test 4
    depths = [1, 2, 4, 8]

    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)

    results = []

    for depth in depths:
        print(f"\n{'='*50}")
        print(f"DEPTH {depth}")
        print(f"{'='*50}")

        # ── Two-point circuits ──
        two_pt_circuits = []
        labels = []
        for d_idx in range(n_preps):
            for m_idx in range(n_mechs):
                qc = build_two_point_circuit(n_data, d_idx, m_idx, depth)
                two_pt_circuits.append(qc)
                labels.append((d_idx, m_idx))

        print(f"  Two-point: {len(two_pt_circuits)} circuits, transpiling...")
        isa_2pt = pm.run(two_pt_circuits)

        print(f"  Submitting two-point batch...")
        sampler = Sampler(mode=backend)
        job_2pt = sampler.run(isa_2pt, shots=shots)
        print(f"  Job: {job_2pt.job_id()}")
        result_2pt = job_2pt.result()

        counts_2pt = {}
        for i, label in enumerate(labels):
            counts_2pt[label] = result_2pt[i].data.c.get_counts()

        info_2pt = compute_penalty(counts_2pt, n_preps, n_mechs)

        # ── Three-point circuits ──
        three_pt_circuits = []
        for d_idx in range(n_preps):
            for m_idx in range(n_mechs):
                qc = build_three_point_circuit(n_data, d_idx, m_idx, depth)
                three_pt_circuits.append(qc)

        print(f"  Three-point: {len(three_pt_circuits)} circuits, transpiling...")
        isa_3pt = pm.run(three_pt_circuits)

        print(f"  Submitting three-point batch...")
        sampler3 = Sampler(mode=backend)
        job_3pt = sampler3.run(isa_3pt, shots=shots)
        print(f"  Job: {job_3pt.job_id()}")
        result_3pt = job_3pt.result()

        counts_3pt = {}
        for i, label in enumerate(labels):
            counts_3pt[label] = result_3pt[i].data.c.get_counts()

        info_3pt = compute_penalty(counts_3pt, n_preps, n_mechs)

        # ── Compare ──
        if info_2pt and info_3pt:
            p2 = info_2pt["penalty"]
            p3 = info_3pt["penalty"]
            reduction = ((p2 - p3) / p2 * 100) if p2 > 0 else 0

            print(f"\n  TWO-POINT  penalty: {p2:.4f}")
            print(f"  THREE-POINT penalty: {p3:.4f}")
            print(f"  REDUCTION: {reduction:.1f}%")

            if p3 < p2:
                print(f"  >>> THREE-POINT GEOMETRY REDUCES PENALTY <<<")
            elif p3 <= 0:
                print(f"  >>> THREE-POINT GEOMETRY ELIMINATES PENALTY <<<")
            else:
                print(f"  Three-point did NOT reduce penalty at this depth")

            results.append({
                "depth": depth,
                "two_point": info_2pt,
                "three_point": info_3pt,
                "penalty_reduction_pct": float(reduction),
                "three_point_reduces": bool(p3 < p2),
            })

    # ── Summary ──
    print("\n" + "=" * 70)
    print("SUMMARY — THREE-POINT GEOMETRY TEST")
    print("=" * 70)
    print(f"\n{'Depth':>6} {'2pt Penalty':>12} {'3pt Penalty':>12} {'Reduction':>10}")
    print("-" * 44)

    reductions = []
    for r in results:
        p2 = r["two_point"]["penalty"]
        p3 = r["three_point"]["penalty"]
        red = r["penalty_reduction_pct"]
        reductions.append(r["three_point_reduces"])
        marker = " ***" if r["three_point_reduces"] else ""
        print(f"{r['depth']:>6} {p2:>12.4f} {p3:>12.4f} {red:>9.1f}%{marker}")

    n_reduced = sum(reductions)
    print(f"\n  Three-point reduced penalty in {n_reduced}/{len(results)} depth levels")

    if n_reduced == len(results):
        print(f"\n  *** THREE-POINT GEOMETRY REDUCES PENALTY AT ALL DEPTHS ***")
        print(f"  *** ARCHITECTURAL FIX CONFIRMED ON IBM QUANTUM HARDWARE ***")
    elif n_reduced >= len(results) * 0.75:
        print(f"\n  STRONGLY SUPPORTED — three-point reduces penalty in most conditions")
    elif n_reduced >= len(results) * 0.5:
        print(f"\n  PARTIALLY SUPPORTED — reduction not universal")
    else:
        print(f"\n  NOT CONFIRMED — three-point did not reliably reduce penalty")

    print("=" * 70)

    # Save
    out_path = Path(__file__).parent / "results_test6_three_point_ibm.json"
    with open(out_path, "w") as f:
        json.dump({
            "test": "Three-Point Geometry Penalty Reduction — IBM Quantum Hardware",
            "prediction": "Three-point architecture reduces I(D;M|Y) vs two-point",
            "backend": backend.name,
            "params": {
                "n_data_qubits": n_data,
                "n_preps": n_preps,
                "n_mechs": n_mechs,
                "shots": shots,
                "depths": depths,
            },
            "results": results,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }, f, indent=2)

    print(f"\nResults saved to {out_path}")
    return results


if __name__ == "__main__":
    run_three_point_test()
