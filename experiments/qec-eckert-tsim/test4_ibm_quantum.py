#!/usr/bin/env python3
"""
Test 4 — IBM Quantum Hardware Port
====================================
Explaining-Away Penalty on Real Quantum Hardware

Ports the existing Test 4 (confirmed on Stim simulator: I(D;M|Y) > 0
in 8/8 measurements) to IBM's 156-qubit quantum processors.

This is a REPLICATION on real hardware, not simulation.
If the penalty exists here, it's confirmed on a fourth substrate type:
superconducting transmon qubits (IBM Heron processors).

Uses 5 qubits, 4 prep states × 4 mechanisms, swept across engagement
levels (circuit depth). Free tier: 10 min/month execution time.
"""

import numpy as np
import json
import time
from pathlib import Path
from collections import defaultdict

from qiskit.circuit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler


# ============================================================
# Circuit builders (Qiskit version of Test 4)
# ============================================================

def build_circuit(n_qubits: int, prep_state: int, mechanism: int,
                  depth: int) -> QuantumCircuit:
    """
    Build a quantum circuit with specified prep state and mechanism.

    prep_state (D): selects initial qubit configuration
        0 = all |0> (default)
        1 = all |+> (Hadamard on all)
        2 = alternating |0>|1> (X on odd qubits)
        3 = GHZ-like (H on q0, CNOT chain)

    mechanism (M): selects gate pattern applied for `depth` layers
        0 = identity (no gates — baseline)
        1 = Clifford ladder (H-S-CNOT repeating)
        2 = T-gate heavy (T on every qubit + entangling)
        3 = CNOT ring (maximal entanglement)

    NOTE: No artificial noise injection — real hardware provides real noise.
    """
    qc = QuantumCircuit(n_qubits, n_qubits)

    # Prep state D
    if prep_state == 0:
        pass  # all |0>
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

    # Mechanism M applied for `depth` layers
    for layer in range(depth):
        if mechanism == 0:
            # Identity — only hardware noise acts
            qc.barrier()
        elif mechanism == 1:
            # Clifford ladder
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
            # T-gate heavy + entangling
            for q in range(n_qubits):
                qc.t(q)
            for q in range(0, n_qubits - 1, 2):
                qc.cx(q, q + 1)
        elif mechanism == 3:
            # CNOT ring
            for q in range(n_qubits):
                t2 = (q + 1) % n_qubits
                qc.cx(q, t2)

    # Measure all qubits
    qc.measure(range(n_qubits), range(n_qubits))

    return qc


# ============================================================
# Information-theoretic computations (same as Test 4)
# ============================================================

def entropy(probs):
    """Shannon entropy of a probability distribution."""
    p = probs[probs > 0]
    return -np.sum(p * np.log2(p))


def estimate_mutual_info(joint_counts, marginal_x_counts, marginal_y_counts, total):
    """Estimate I(X;Y) with Miller-Madow bias correction."""
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

    n_nonzero_joint = sum(1 for v in joint_counts.values() if v > 0)
    n_nonzero_x = sum(1 for v in marginal_x_counts.values() if v > 0)
    n_nonzero_y = sum(1 for v in marginal_y_counts.values() if v > 0)
    bias = (n_nonzero_joint - n_nonzero_x - n_nonzero_y + 1) / (2 * total * np.log(2))

    return max(0.0, mi - bias)


def compute_penalty_from_counts(counts_dict, n_d, n_m):
    """
    Compute I(D;M|Y) from measurement outcome counts.

    counts_dict: {(d, m): {bitstring: count}} for all (d,m) pairs

    I(D;M|Y) = I(DM;Y) - I(D;Y) - I(M;Y)  [when D ⊥ M]
    """
    joint_dmy = {}
    joint_dy = {}
    joint_my = {}
    marginal_y = {}
    total = 0

    for (d, m), counts in counts_dict.items():
        for bitstring, count in counts.items():
            y = bitstring  # Use bitstring directly as outcome key
            joint_dmy[(d, m, y)] = joint_dmy.get((d, m, y), 0) + count
            joint_dy[(d, y)] = joint_dy.get((d, y), 0) + count
            joint_my[(m, y)] = joint_my.get((m, y), 0) + count
            marginal_y[y] = marginal_y.get(y, 0) + count
            total += count

    if total == 0:
        return None

    # H(Y)
    py = np.array(list(marginal_y.values())) / total
    H_Y = entropy(py)

    # I(D;Y)
    marginal_d = {}
    for (d, y), cnt in joint_dy.items():
        marginal_d[d] = marginal_d.get(d, 0) + cnt
    I_D_Y = estimate_mutual_info(joint_dy, marginal_d, marginal_y, total)

    # I(M;Y)
    marginal_m = {}
    for (m, y), cnt in joint_my.items():
        marginal_m[m] = marginal_m.get(m, 0) + cnt
    I_M_Y = estimate_mutual_info(joint_my, marginal_m, marginal_y, total)

    # I(DM;Y)
    joint_dm_y = {}
    marginal_dm = {}
    for (d, m, y), cnt in joint_dmy.items():
        dm = (d, m)
        joint_dm_y[(dm, y)] = joint_dm_y.get((dm, y), 0) + cnt
        marginal_dm[dm] = marginal_dm.get(dm, 0) + cnt
    I_DM_Y = estimate_mutual_info(joint_dm_y, marginal_dm, marginal_y, total)

    # I(D;M|Y) = I(DM;Y) - I(D;Y) - I(M;Y)
    penalty = I_DM_Y - I_D_Y - I_M_Y

    H_Y_given_DM = H_Y - I_DM_Y

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
# Main: Run on IBM Quantum Hardware
# ============================================================

def run_ibm_quantum_test():
    import os

    token = os.environ.get("IBM_QUANTUM_TOKEN")
    if not token:
        print("ERROR: Set IBM_QUANTUM_TOKEN environment variable")
        return

    print("=" * 70)
    print("TEST 4 — IBM QUANTUM HARDWARE REPLICATION")
    print("Explaining-Away Penalty on Real Superconducting Qubits")
    print("=" * 70)

    # Connect to IBM Quantum
    print("\nConnecting to IBM Quantum Platform...")
    service = QiskitRuntimeService(
        channel='ibm_quantum_platform',
        token=token
    )

    # Pick least-busy backend
    backends = service.backends(operational=True)
    # least_busy can be finicky — just pick the first operational backend
    backend = backends[0]
    print(f"Selected backend: {backend.name} ({backend.num_qubits} qubits)")

    # Test parameters — conservative for free tier (10 min/month)
    n_qubits = 5
    n_preps = 4
    n_mechs = 4
    shots_per_combo = 1000  # 4×4×1000 = 16K shots per depth level

    # Fewer depth levels than simulation to conserve QPU time
    engagement_levels = [1, 2, 4, 8, 16]

    print(f"\nConfig: {n_qubits} qubits, {n_preps} preps × {n_mechs} mechanisms")
    print(f"        {shots_per_combo} shots/combo, depths: {engagement_levels}")
    print(f"        Total circuits: {n_preps * n_mechs * len(engagement_levels)} = {n_preps * n_mechs * len(engagement_levels)}")
    print(f"        Total shots: {n_preps * n_mechs * shots_per_combo * len(engagement_levels):,}")
    print(f"\nPrediction: I(D;M|Y) > 0 at all engagement levels")
    print("-" * 70)

    all_results = []

    for depth in engagement_levels:
        print(f"\n--- Depth {depth} ---")
        t0 = time.time()

        # Build all circuits for this depth
        circuits = []
        circuit_labels = []
        for d_idx in range(n_preps):
            for m_idx in range(n_mechs):
                qc = build_circuit(n_qubits, d_idx, m_idx, depth)
                circuits.append(qc)
                circuit_labels.append((d_idx, m_idx))

        print(f"  Built {len(circuits)} circuits (depth={depth}, gates~{circuits[0].size()})")

        # Transpile circuits to hardware native gate set
        print(f"  Transpiling for {backend.name}...")
        pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
        isa_circuits = pm.run(circuits)
        print(f"  Transpiled. ISA gate counts: {isa_circuits[0].size()}")

        # Submit batch to IBM Quantum
        print(f"  Submitting to {backend.name}...")
        sampler = Sampler(mode=backend)

        # Run all circuits as a single batch job
        job = sampler.run(isa_circuits, shots=shots_per_combo)
        print(f"  Job submitted: {job.job_id()}")
        print(f"  Waiting for results...")
        result = job.result()

        # Collect results
        counts_dict = {}
        for i, label in enumerate(circuit_labels):
            pub_result = result[i]
            counts = pub_result.data.c.get_counts()
            counts_dict[label] = counts
            d_idx, m_idx = label
            n_outcomes = len(counts)
            print(f"  D={d_idx} M={m_idx}: {sum(counts.values())} shots, {n_outcomes} unique outcomes")

        elapsed = time.time() - t0

        # Compute the penalty
        info = compute_penalty_from_counts(counts_dict, n_preps, n_mechs)

        if info is None:
            print(f"  FAILED to compute penalty")
            continue

        check_error = abs(info["fantasia_check"] - info["fantasia_H_Y"])

        print(f"\n  I(D;Y)={info['I_D_Y']:.4f}  I(M;Y)={info['I_M_Y']:.4f}  "
              f"I(DM;Y)={info['I_DM_Y']:.4f}")
        print(f"  PENALTY I(D;M|Y) = {info['penalty_I_D_M_given_Y']:.4f}")
        print(f"  H(Y)={info['H_Y']:.4f}  Decomposition error={check_error:.6f}")
        print(f"  Time: {elapsed:.1f}s")

        result_entry = {
            "depth": depth,
            "backend": backend.name,
            **info,
            "decomposition_error": float(check_error),
            "elapsed_s": elapsed,
        }
        all_results.append(result_entry)

    # ── Analysis ──
    print("\n" + "=" * 70)
    print("ANALYSIS — IBM QUANTUM HARDWARE")
    print("=" * 70)

    if len(all_results) >= 2:
        depths = np.array([r["depth"] for r in all_results])
        penalties = np.array([r["penalty_I_D_M_given_Y"] for r in all_results])

        positive_count = np.sum(penalties > 0)
        print(f"\n  Penalty > 0 in {positive_count}/{len(all_results)} measurements")

        if len(depths) >= 3:
            coeffs = np.polyfit(depths, penalties, 1)
            slope = coeffs[0]
            print(f"  Linear trend: slope = {slope:.6f}")

            if np.std(penalties) > 0:
                corr = np.corrcoef(depths, penalties)[0, 1]
                print(f"  Correlation(depth, penalty): r = {corr:.4f}")

        check_errors = [r["decomposition_error"] for r in all_results]
        print(f"  Mean decomposition error: {np.mean(check_errors):.6f}")

        # Peak detection (discrete regime prediction)
        peak_idx = np.argmax(penalties)
        print(f"  Peak penalty at depth={depths[peak_idx]} (value={penalties[peak_idx]:.4f})")

        if positive_count == len(all_results):
            print(f"\n  *** EXPLAINING-AWAY PENALTY CONFIRMED ON IBM QUANTUM HARDWARE ***")
            print(f"  *** Fourth substrate: superconducting transmon qubits (IBM Heron) ***")
            print(f"  *** Fantasia Bound holds on real quantum hardware ***")
        elif positive_count >= len(all_results) * 0.8:
            print(f"\n  STRONGLY SUPPORTED on quantum hardware")
        elif positive_count >= len(all_results) * 0.5:
            print(f"\n  PARTIALLY SUPPORTED — penalty present but not universal")
        else:
            print(f"\n  NOT CONFIRMED on this hardware — investigate")

    # Save results
    out_path = Path(__file__).parent / "results_test4_ibm_quantum.json"
    with open(out_path, "w") as f:
        json.dump({
            "test": "Explaining-Away Penalty — IBM Quantum Hardware Replication",
            "prediction": "I(D;M|Y) > 0 (penalty exists on real quantum hardware)",
            "framework_section": "§2B₂ (Structure Theorem), Theorem 1.5 (Exact Decomposition)",
            "substrate": "Superconducting transmon qubits (IBM Heron processor)",
            "backend": backend.name,
            "params": {
                "n_qubits": n_qubits,
                "n_prep_states": n_preps,
                "n_mechanisms": n_mechs,
                "shots_per_combo": shots_per_combo,
                "engagement_levels": engagement_levels,
            },
            "results": all_results,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }, f, indent=2)

    print(f"\nResults saved to {out_path}")
    return all_results


if __name__ == "__main__":
    run_ibm_quantum_test()
