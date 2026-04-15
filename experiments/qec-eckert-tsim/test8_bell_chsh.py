#!/usr/bin/env python3
"""
Test 8 — CHSH Bell Inequality Test
======================================
Earning the "Quantum" Label

Question: Are the entangled states in our quantum penalty measurements
genuinely quantum (non-local), or could a classical model reproduce
the same statistics?

Method: Run a standard CHSH Bell test on the same IBM hardware used
for Tests 4-7. If S > 2 (Tsirelson's bound: S ≤ 2√2 ≈ 2.828),
the correlations are provably non-classical. This earns the "quantum"
label for our substrate independence claims.

Additionally, we measure the explaining-away penalty I(D;M|Y) on the
SAME entangled state that violates Bell, connecting the two results:
the penalty operates on a genuinely quantum substrate.

Kill conditions:
  KC-BELL-1: S > 2.0 (Bell violation — genuinely quantum)
  KC-BELL-2: S > 2.5 (strong violation — well above noise floor)
  KC-BELL-3: I(D;M|Y) > 0 on the Bell-violating state
  KC-BELL-4: Penalty at entangled > penalty at separable

Hardware: IBM Quantum (Heron processors)
Cost: ~1 min QPU time (free tier sufficient)
"""

import numpy as np
import json
import time
import os
from pathlib import Path
from collections import defaultdict
from math import log2, sqrt, pi, cos, sin

from qiskit.circuit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler


# ============================================================
# CHSH Circuit Builders
# ============================================================

def build_bell_state(qc, q0, q1):
    """Create a maximally entangled Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2."""
    qc.h(q0)
    qc.cx(q0, q1)


def build_chsh_circuit(
    alice_angle: float,
    bob_angle: float,
    entangled: bool = True,
) -> QuantumCircuit:
    """
    Build one CHSH measurement circuit.

    Alice measures at angle `alice_angle` from Z-axis in the XZ plane.
    Bob measures at angle `bob_angle` from Z-axis in the XZ plane.

    If entangled=True: prepare Bell state |Φ+⟩.
    If entangled=False: prepare separable |00⟩ (classical control).

    Returns circuit with 2 qubits, 2 classical bits.
    """
    qc = QuantumCircuit(2, 2)

    # Prepare state
    if entangled:
        build_bell_state(qc, 0, 1)
    # else: both qubits stay |0⟩ (separable)

    # Alice's measurement basis rotation (qubit 0)
    # Ry(theta) rotates |0⟩ toward |1⟩ by theta in the YZ plane
    # Measuring in computational basis after Ry(-theta) = measuring at angle theta
    qc.ry(-2 * alice_angle, 0)

    # Bob's measurement basis rotation (qubit 1)
    qc.ry(-2 * bob_angle, 1)

    # Measure both in computational basis
    qc.measure(0, 0)
    qc.measure(1, 1)

    return qc


def build_penalty_circuit(
    prep_state: int,
    mechanism: int,
    entangled: bool = True,
) -> QuantumCircuit:
    """
    Build a circuit measuring I(D;M|Y) on entangled vs separable states.

    Same architecture as Tests 4-7 but on a Bell pair:
      q0 = Alice's qubit (carries prep + mechanism)
      q1 = Bob's qubit (entangled or separable)

    This connects the Bell violation to the explaining-away penalty:
    if the penalty is measured on the SAME state that violates Bell,
    the penalty is operating on a genuinely quantum substrate.
    """
    qc = QuantumCircuit(2, 2)

    # Prepare entangled or separable state
    if entangled:
        build_bell_state(qc, 0, 1)

    # Apply prep state (D) to Alice's qubit
    if prep_state == 1:
        qc.rx(pi / 4, 0)      # small rotation
    elif prep_state == 2:
        qc.ry(pi / 3, 0)      # medium rotation
    elif prep_state == 3:
        qc.rx(pi / 2, 0)      # large rotation
    # prep 0 = identity

    # Apply mechanism (M) to Alice's qubit
    if mechanism == 1:
        qc.rx(pi / 6, 0)      # 30° X-rotation
    elif mechanism == 2:
        qc.ry(pi / 4, 0)      # 45° Y-rotation
    elif mechanism == 3:
        qc.rx(pi / 3, 0)      # 60° X-rotation
    # mechanism 0 = identity

    # Measure both qubits
    qc.measure(0, 0)
    qc.measure(1, 1)

    return qc


# ============================================================
# CHSH Computation
# ============================================================

def compute_correlator(counts, shots):
    """
    Compute ⟨AB⟩ = P(same) - P(different) from measurement counts.

    same = 00 or 11, different = 01 or 10
    ⟨AB⟩ = (N_same - N_diff) / N_total
    """
    n_same = counts.get("00", 0) + counts.get("11", 0)
    n_diff = counts.get("01", 0) + counts.get("10", 0)
    total = n_same + n_diff
    if total == 0:
        return 0.0
    return (n_same - n_diff) / total


def compute_chsh_S(correlators):
    """
    Compute CHSH parameter S = |⟨A₁B₁⟩ + ⟨A₁B₂⟩ + ⟨A₂B₁⟩ - ⟨A₂B₂⟩|

    Classical limit: S ≤ 2
    Quantum limit (Tsirelson): S ≤ 2√2 ≈ 2.828

    correlators: dict with keys (a_idx, b_idx) -> ⟨AB⟩ value
    """
    E_a1b1 = correlators[(0, 0)]
    E_a1b2 = correlators[(0, 1)]
    E_a2b1 = correlators[(1, 0)]
    E_a2b2 = correlators[(1, 1)]

    S = abs(E_a1b1 + E_a1b2 + E_a2b1 - E_a2b2)
    return S


# ============================================================
# Information-theoretic computation (reused from Test 7)
# ============================================================

def shannon_entropy(probs):
    """H(X) from probability array."""
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
    """Compute I(D;M|Y) from measurement counts — same as Test 7."""
    joint_dmy = defaultdict(int)
    joint_dy = defaultdict(int)
    joint_my = defaultdict(int)
    marginal_d = defaultdict(int)
    marginal_m = defaultdict(int)
    marginal_y = defaultdict(int)
    joint_dm = defaultdict(int)
    joint_dm_y = defaultdict(int)
    total = 0

    for (d_idx, m_idx), counts in counts_dict.items():
        for bitstring, count in counts.items():
            y = bitstring
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

    I_D_Y = mutual_information(joint_dy, marginal_d, marginal_y, total)
    I_M_Y = mutual_information(joint_my, marginal_m, marginal_y, total)

    marginal_dm_agg = defaultdict(int)
    joint_dm_y_agg = defaultdict(int)
    for (d, m, y), count in joint_dmy.items():
        dm = (d, m)
        joint_dm_y_agg[(dm, y)] += count
        marginal_dm_agg[dm] += count
    I_DM_Y = mutual_information(joint_dm_y_agg, marginal_dm_agg, marginal_y, total)

    penalty = I_DM_Y - I_D_Y - I_M_Y

    H_Y = shannon_entropy([c / total for c in marginal_y.values()])

    H_Y_given_DM = 0.0
    for dm, dm_total in marginal_dm_agg.items():
        if dm_total == 0:
            continue
        p_dm = dm_total / total
        conditional_probs = []
        for y in marginal_y:
            c = joint_dm_y_agg.get((dm, y), 0)
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
# Main: Run CHSH Bell Test + Penalty on IBM Quantum
# ============================================================

def run_bell_test():
    token = os.environ.get("IBM_QUANTUM_TOKEN")
    if not token:
        print("ERROR: Set IBM_QUANTUM_TOKEN environment variable")
        print("  export IBM_QUANTUM_TOKEN='your_token_here'")
        return

    print("=" * 70)
    print("TEST 8 — CHSH BELL INEQUALITY TEST")
    print("Earning the 'quantum' label for substrate independence")
    print("=" * 70)

    # Connect to IBM Quantum
    print("\nConnecting to IBM Quantum Platform...")
    service = QiskitRuntimeService(
        channel="ibm_quantum_platform",
        token=token,
    )

    backends = service.backends(operational=True, min_num_qubits=2)
    if not backends:
        print("ERROR: No operational backends with >= 2 qubits")
        return
    backend = backends[0]
    print(f"Selected backend: {backend.name} ({backend.num_qubits} qubits)")

    shots = 4096  # standard for Bell tests — good statistics

    # ──────────────────────────────────────────────────
    # PART 1: CHSH Bell Inequality
    # ──────────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("PART 1: CHSH Bell Inequality")
    print("─" * 70)

    # Optimal CHSH angles for |Φ+⟩ Bell state
    # Alice: A₁ = 0, A₂ = π/4
    # Bob:   B₁ = π/8, B₂ = -π/8 (equivalently 3π/8)
    # These maximize S = 2√2 for a perfect Bell state
    alice_angles = [0, pi / 4]
    bob_angles = [pi / 8, -pi / 8]

    # Build CHSH circuits — entangled
    chsh_circuits_entangled = []
    chsh_labels = []
    for a_idx, a_angle in enumerate(alice_angles):
        for b_idx, b_angle in enumerate(bob_angles):
            qc = build_chsh_circuit(a_angle, b_angle, entangled=True)
            chsh_circuits_entangled.append(qc)
            chsh_labels.append((a_idx, b_idx))

    # Build CHSH circuits — separable (classical control)
    chsh_circuits_separable = []
    for a_idx, a_angle in enumerate(alice_angles):
        for b_idx, b_angle in enumerate(bob_angles):
            qc = build_chsh_circuit(a_angle, b_angle, entangled=False)
            chsh_circuits_separable.append(qc)

    all_chsh_circuits = chsh_circuits_entangled + chsh_circuits_separable
    print(f"  Built {len(all_chsh_circuits)} CHSH circuits "
          f"({len(chsh_circuits_entangled)} entangled + "
          f"{len(chsh_circuits_separable)} separable)")

    # ──────────────────────────────────────────────────
    # PART 2: Penalty on Bell state vs separable state
    # ──────────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("PART 2: Explaining-Away Penalty on Bell State")
    print("─" * 70)

    n_preps = 4
    n_mechs = 4

    penalty_circuits_entangled = []
    penalty_labels = []
    for d_idx in range(n_preps):
        for m_idx in range(n_mechs):
            qc = build_penalty_circuit(d_idx, m_idx, entangled=True)
            penalty_circuits_entangled.append(qc)
            penalty_labels.append((d_idx, m_idx))

    penalty_circuits_separable = []
    for d_idx in range(n_preps):
        for m_idx in range(n_mechs):
            qc = build_penalty_circuit(d_idx, m_idx, entangled=False)
            penalty_circuits_separable.append(qc)

    print(f"  Built {len(penalty_circuits_entangled) * 2} penalty circuits "
          f"({len(penalty_circuits_entangled)} entangled + "
          f"{len(penalty_circuits_separable)} separable)")

    # ──────────────────────────────────────────────────
    # Submit all circuits in one batch
    # ──────────────────────────────────────────────────
    all_circuits = (
        all_chsh_circuits +
        penalty_circuits_entangled +
        penalty_circuits_separable
    )

    n_chsh = len(all_chsh_circuits)
    n_pen_ent = len(penalty_circuits_entangled)
    n_pen_sep = len(penalty_circuits_separable)

    print(f"\n  Total circuits: {len(all_circuits)}")
    print(f"  Total shots: {len(all_circuits) * shots:,}")

    # Transpile
    print(f"  Transpiling...")
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_circuits = pm.run(all_circuits)

    # Submit
    print(f"  Submitting to {backend.name}...")
    t0 = time.time()
    sampler = Sampler(mode=backend)
    job = sampler.run(isa_circuits, shots=shots)
    print(f"  Job: {job.job_id()}")
    print(f"  Waiting...")
    result = job.result()
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s")

    # ──────────────────────────────────────────────────
    # Analyze CHSH results
    # ──────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)

    # Entangled correlators
    print("\n--- CHSH (Entangled) ---")
    correlators_ent = {}
    for i, (a_idx, b_idx) in enumerate(chsh_labels):
        counts = result[i].data.c.get_counts()
        corr = compute_correlator(counts, shots)
        correlators_ent[(a_idx, b_idx)] = corr
        a_name = f"A{a_idx+1}"
        b_name = f"B{b_idx+1}"
        print(f"  ⟨{a_name}{b_name}⟩ = {corr:+.4f}  "
              f"(00:{counts.get('00',0)} 01:{counts.get('01',0)} "
              f"10:{counts.get('10',0)} 11:{counts.get('11',0)})")

    S_entangled = compute_chsh_S(correlators_ent)
    print(f"\n  S (entangled) = {S_entangled:.4f}")
    print(f"  Classical limit: 2.000")
    print(f"  Tsirelson bound: {2*sqrt(2):.4f}")
    print(f"  Violation: {S_entangled - 2:.4f} above classical limit")

    # Separable correlators (classical control)
    print("\n--- CHSH (Separable — classical control) ---")
    correlators_sep = {}
    for i, (a_idx, b_idx) in enumerate(chsh_labels):
        counts = result[len(chsh_circuits_entangled) + i].data.c.get_counts()
        corr = compute_correlator(counts, shots)
        correlators_sep[(a_idx, b_idx)] = corr
        a_name = f"A{a_idx+1}"
        b_name = f"B{b_idx+1}"
        print(f"  ⟨{a_name}{b_name}⟩ = {corr:+.4f}")

    S_separable = compute_chsh_S(correlators_sep)
    print(f"\n  S (separable) = {S_separable:.4f}")
    print(f"  Expected: S ≤ 2.0 (no violation)")

    # ──────────────────────────────────────────────────
    # Analyze penalty results
    # ──────────────────────────────────────────────────
    print("\n--- Explaining-Away Penalty ---")

    # Entangled penalty
    counts_dict_ent = {}
    for i, (d_idx, m_idx) in enumerate(penalty_labels):
        counts = result[n_chsh + i].data.c.get_counts()
        counts_dict_ent[(d_idx, m_idx)] = counts

    info_ent = compute_penalty_from_counts(counts_dict_ent, n_preps, n_mechs)

    # Separable penalty
    counts_dict_sep = {}
    for i, (d_idx, m_idx) in enumerate(penalty_labels):
        counts = result[n_chsh + n_pen_ent + i].data.c.get_counts()
        counts_dict_sep[(d_idx, m_idx)] = counts

    info_sep = compute_penalty_from_counts(counts_dict_sep, n_preps, n_mechs)

    if info_ent and info_sep:
        pen_ent = info_ent["penalty_I_D_M_given_Y"]
        pen_sep = info_sep["penalty_I_D_M_given_Y"]
        print(f"  Penalty (entangled Bell state):  {pen_ent:.6f} bits")
        print(f"  Penalty (separable |00⟩):        {pen_sep:.6f} bits")
        print(f"  Ratio: {pen_ent/pen_sep:.2f}x" if pen_sep > 0 else "  Separable penalty ≈ 0")
        print(f"  Decomposition check (entangled): "
              f"|{info_ent['fantasia_check']:.4f} - {info_ent['fantasia_H_Y']:.4f}| = "
              f"{abs(info_ent['fantasia_check'] - info_ent['fantasia_H_Y']):.6f}")

    # ──────────────────────────────────────────────────
    # Verdicts
    # ──────────────────────────────────────────────────
    print(f"\n{'─' * 40}")
    print("KILL CONDITIONS")
    verdicts = {}

    # KC-BELL-1: S > 2.0 (Bell violation)
    verdicts["KC-BELL-1"] = S_entangled > 2.0
    print(f"  [{'PASS' if verdicts['KC-BELL-1'] else 'FAIL'}] "
          f"KC-BELL-1: S > 2.0 (Bell violation): S = {S_entangled:.4f}")

    # KC-BELL-2: S > 2.5 (strong violation)
    verdicts["KC-BELL-2"] = S_entangled > 2.5
    print(f"  [{'PASS' if verdicts['KC-BELL-2'] else 'FAIL'}] "
          f"KC-BELL-2: S > 2.5 (strong violation): S = {S_entangled:.4f}")

    # KC-BELL-3: I(D;M|Y) > 0 on the Bell-violating state
    if info_ent:
        verdicts["KC-BELL-3"] = pen_ent > 0.001  # above noise floor
        print(f"  [{'PASS' if verdicts['KC-BELL-3'] else 'FAIL'}] "
              f"KC-BELL-3: Penalty > 0 on Bell state: {pen_ent:.6f}")

    # KC-BELL-4: Penalty entangled > penalty separable
    if info_ent and info_sep:
        verdicts["KC-BELL-4"] = pen_ent > pen_sep
        print(f"  [{'PASS' if verdicts['KC-BELL-4'] else 'FAIL'}] "
              f"KC-BELL-4: Entangled penalty > separable: "
              f"{pen_ent:.6f} vs {pen_sep:.6f}")

    # KC-BELL-5: Separable S ≤ 2 (classical control works)
    verdicts["KC-BELL-5"] = S_separable <= 2.05  # allow small noise
    print(f"  [{'PASS' if verdicts['KC-BELL-5'] else 'FAIL'}] "
          f"KC-BELL-5: Separable S ≤ 2 (control): S = {S_separable:.4f}")

    n_pass = sum(1 for v in verdicts.values() if v)
    n_total = len(verdicts)
    print(f"\n  VERDICT: {n_pass}/{n_total} PASS")

    if verdicts.get("KC-BELL-1"):
        print(f"\n  ★ Bell inequality VIOLATED on IBM hardware.")
        print(f"    S = {S_entangled:.4f} > 2.0 (classical limit).")
        print(f"    The quantum states used in Tests 4-7 are genuinely")
        print(f"    non-classical. The 'quantum' label is earned.")
        if verdicts.get("KC-BELL-3"):
            print(f"\n    The explaining-away penalty I(D;M|Y) = {pen_ent:.6f}")
            print(f"    was measured on the SAME Bell-violating state.")
            print(f"    The penalty operates on a provably quantum substrate.")
    else:
        print(f"\n  ○ Bell inequality NOT violated.")
        print(f"    S = {S_entangled:.4f} ≤ 2.0")
        print(f"    Hardware noise may be too high, or entanglement")
        print(f"    is not reaching the qubits. Check gate fidelity.")

    # ──────────────────────────────────────────────────
    # Save results
    # ──────────────────────────────────────────────────
    outdir = Path(__file__).parent / "results"
    outdir.mkdir(exist_ok=True)
    outfile = outdir / f"results_test8_bell_chsh_{int(time.time())}.json"

    output = {
        "test": "Test 8 — CHSH Bell Inequality",
        "purpose": "Earn the 'quantum' label for substrate independence claims",
        "backend": backend.name,
        "n_qubits": 2,
        "shots_per_circuit": shots,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "chsh_entangled": {
            "correlators": {f"A{a+1}B{b+1}": float(v)
                           for (a, b), v in correlators_ent.items()},
            "S": float(S_entangled),
            "classical_limit": 2.0,
            "tsirelson_bound": float(2 * sqrt(2)),
            "violation": float(S_entangled - 2.0),
        },
        "chsh_separable": {
            "correlators": {f"A{a+1}B{b+1}": float(v)
                           for (a, b), v in correlators_sep.items()},
            "S": float(S_separable),
        },
        "penalty_entangled": info_ent,
        "penalty_separable": info_sep,
        "verdicts": {k: bool(v) for k, v in verdicts.items()},
        "n_pass": n_pass,
        "n_total": n_total,
    }

    with open(outfile, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved: {outfile}")


# ============================================================
# Dry-run mode
# ============================================================

def dry_run():
    """Generate and inspect circuits without running on hardware."""
    print("=" * 70)
    print("TEST 8 — DRY RUN (no IBM token)")
    print("Generating circuits for inspection")
    print("=" * 70)

    alice_angles = [0, pi / 4]
    bob_angles = [pi / 8, -pi / 8]

    print("\n--- CHSH Circuits (Entangled) ---")
    for a_idx, a_angle in enumerate(alice_angles):
        for b_idx, b_angle in enumerate(bob_angles):
            qc = build_chsh_circuit(a_angle, b_angle, entangled=True)
            print(f"\nA{a_idx+1} ({a_angle:.3f} rad) × "
                  f"B{b_idx+1} ({b_angle:.3f} rad):")
            print(f"  Gates: {qc.size()}, Depth: {qc.depth()}")
            print(qc.draw(output="text"))

    print("\n--- Penalty Circuit (Entangled, D=1, M=2) ---")
    qc = build_penalty_circuit(1, 2, entangled=True)
    print(f"  Gates: {qc.size()}, Depth: {qc.depth()}")
    print(qc.draw(output="text"))

    print("\n--- Penalty Circuit (Separable, D=1, M=2) ---")
    qc = build_penalty_circuit(1, 2, entangled=False)
    print(f"  Gates: {qc.size()}, Depth: {qc.depth()}")
    print(qc.draw(output="text"))

    print(f"\nTotal circuits needed: {4 + 4 + 16 + 16} = 40")
    print(f"Total shots: 40 × 4096 = 163,840")
    print(f"Estimated QPU time: ~1 min")

    print("\nTo run on IBM hardware:")
    print("  export IBM_QUANTUM_TOKEN='your_token_here'")
    print("  python test8_bell_chsh.py")


if __name__ == "__main__":
    token = os.environ.get("IBM_QUANTUM_TOKEN")
    if token:
        run_bell_test()
    else:
        dry_run()
