#!/usr/bin/env python3
"""
Test 5: Barrier Height Coefficient vs π/√2 Prediction
======================================================

The framework derives B_G = π/√2 ≈ 2.2214 from the Čencov metric —
the unique invariant metric on statistical manifolds (§8D, §165).

In QEC, the logical error rate of a repetition code scales as:

    p_L ∝ (p/p_th)^d  for p < p_th

where p is physical error rate, p_th is the threshold, and d is code
distance. Taking logs:

    log(p_L) ≈ d · log(p/p_th) = -d · |log(p_th/p)|

The "barrier height" in the framework is the exponential suppression
rate. The prediction: the coefficient that governs how fast error
correction improves with distance should relate to π/√2 when expressed
in natural units of the Fisher metric.

SPECIFICALLY:
    The Fisher metric at error rate p is g(p) = 1/[p(1-p)].
    The geodesic distance from p to p_th on the Bernoulli manifold is:
        L = |2·arcsin(√p_th) - 2·arcsin(√p)|
    The barrier coefficient in geodesic units should approach π/√2.

PROCEDURE:
    1. Run repetition codes at distances d = 3, 5, 7, 9, 11
    2. At each distance, measure logical error rate
    3. Fit exponential: p_L = A · exp(-α · d)
    4. Convert α to geodesic units using Fisher metric
    5. Compare to π/√2

ALSO: Test at multiple physical error rates to check universality.

Hardware: CPU-feasible. Repetition codes up to ~23 qubits.
"""

import numpy as np
import json
import time
from pathlib import Path

try:
    import stim
except ImportError:
    print("Install stim: pip install stim")
    stim = None

try:
    import pymatching
except ImportError:
    print("Install pymatching: pip install pymatching")
    pymatching = None


B_G_PREDICTED = np.pi / np.sqrt(2)  # ≈ 2.2214


def measure_logical_error_rate(distance: int, error_rate: float, shots: int) -> dict:
    """
    Run a repetition code memory experiment at given distance and error rate.
    Uses stim's built-in circuit generator and pymatching MWPM decoder.
    """
    if stim is None or pymatching is None:
        return {"logical_error_rate": np.nan, "dry_run": True}

    # Generate repetition code circuit using stim's built-in generator
    # This produces a properly structured circuit with detectors and observables
    circuit = stim.Circuit.generated(
        'repetition_code:memory',
        rounds=distance,          # syndrome rounds = distance for full protection
        distance=distance,
        after_clifford_depolarization=error_rate,
        after_reset_flip_probability=0.0,
        before_measure_flip_probability=0.0,
        before_round_data_depolarization=0.0,
    )

    t0 = time.time()

    # Build detector error model for the decoder
    dem = circuit.detector_error_model(decompose_errors=True)

    # Sample detector outcomes + observable flips
    sampler = circuit.compile_detector_sampler()
    samples = sampler.sample(shots=shots, append_observables=True)

    n_det = circuit.num_detectors
    det_data = samples[:, :n_det]
    obs_data = samples[:, n_det:]

    # Decode with MWPM
    matching = pymatching.Matching.from_detector_error_model(dem)
    predictions = matching.decode_batch(det_data)

    # Logical error = decoder prediction disagrees with actual observable flip
    errors = np.any(predictions != obs_data, axis=1)
    p_L = float(np.mean(errors))

    elapsed = time.time() - t0

    return {
        "logical_error_rate": p_L,
        "elapsed_s": elapsed,
        "dry_run": False,
    }


def geodesic_distance_bernoulli(p1: float, p2: float) -> float:
    """
    Geodesic distance between two points on the Bernoulli manifold
    with the Fisher metric g(p) = 1/[p(1-p)].

    The geodesic distance is: 2|arcsin(√p2) - arcsin(√p1)|
    """
    return 2.0 * abs(np.arcsin(np.sqrt(p2)) - np.arcsin(np.sqrt(p1)))


def run_barrier_height_test():
    """
    Measure logical error rate vs code distance at multiple physical error rates.
    Extract barrier coefficient and compare to π/√2.
    """
    # Code distances (d = n_data for repetition code)
    distances = [3, 5, 7, 9, 11]
    shots = 100_000

    # Physical error rates (must be below threshold ≈ 0.11 for repetition code)
    error_rates = [0.01, 0.02, 0.03, 0.05, 0.07]

    # Threshold for repetition code (approximate)
    p_threshold = 0.11

    results_by_error = {}

    print("=" * 70)
    print("TEST 5: Barrier Height Coefficient vs π/√2 Prediction")
    print("=" * 70)
    print(f"Prediction: barrier coefficient in geodesic units ≈ π/√2 = {B_G_PREDICTED:.4f}")
    print(f"Distances: {distances}")
    print(f"Error rates: {error_rates}")
    print(f"Shots: {shots}")
    print("-" * 70)

    all_results = []

    for p_err in error_rates:
        print(f"\n  Physical error rate p = {p_err}")
        print(f"  {'d':>4} {'p_L':>12} {'log(p_L)':>12} {'Time':>8}")

        distance_data = []

        for d in distances:
            result = measure_logical_error_rate(d, p_err, shots)

            p_L = result["logical_error_rate"]
            log_pL = np.log(max(p_L, 1e-10))
            elapsed = result.get("elapsed_s", 0)

            print(f"  {d:>4} {p_L:>12.6f} {log_pL:>12.4f} {elapsed:>7.1f}s")

            distance_data.append({
                "distance": d,
                "logical_error_rate": p_L,
                "log_logical_error": float(log_pL),
                "elapsed_s": elapsed,
                "dry_run": result.get("dry_run", False),
            })

        # Fit exponential: log(p_L) = -alpha * d + const
        valid_pts = [(r["distance"], r["log_logical_error"])
                     for r in distance_data
                     if not r.get("dry_run") and r["logical_error_rate"] > 1e-8
                     and r["logical_error_rate"] < 1 - 1e-8]

        alpha_raw = np.nan
        alpha_geodesic = np.nan
        r_squared = np.nan
        ratio_to_bg = np.nan

        if len(valid_pts) >= 3:
            x = np.array([p[0] for p in valid_pts])
            y = np.array([p[1] for p in valid_pts])

            coeffs = np.polyfit(x, y, 1)
            slope, intercept = coeffs

            alpha_raw = -slope  # positive = error decreasing with distance

            # Residuals for R²
            y_pred = np.polyval(coeffs, x)
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            r_squared = 1 - ss_res / max(ss_tot, 1e-20)

            # Convert alpha to geodesic units
            # Raw alpha is in units of "per unit distance d"
            # Geodesic distance from p_err to p_threshold:
            L_geo = geodesic_distance_bernoulli(p_err, p_threshold)

            # The barrier height in geodesic units:
            # If p_L ~ exp(-alpha_raw * d), and the geodesic "size" of the
            # error suppression region is L_geo, then:
            # alpha_geodesic = alpha_raw * d_typical / L_geo
            # But more naturally: alpha_geodesic = alpha_raw / L_geo
            # (since d is already dimensionless)

            # Actually, the natural comparison is:
            # alpha_raw should be ~ log(p_th/p) for a repetition code
            # In geodesic units: alpha_geodesic = alpha_raw / L_geo
            alpha_geodesic = alpha_raw / L_geo if L_geo > 0 else np.nan

            ratio_to_bg = alpha_geodesic / B_G_PREDICTED if not np.isnan(alpha_geodesic) else np.nan

            print(f"\n  Fit: log(p_L) = {slope:.4f}·d + {intercept:.4f}")
            print(f"  α_raw = {alpha_raw:.4f}")
            print(f"  Geodesic distance (p→p_th): L = {L_geo:.4f}")
            print(f"  α_geodesic = α_raw/L = {alpha_geodesic:.4f}")
            print(f"  π/√2 = {B_G_PREDICTED:.4f}")
            print(f"  Ratio α_geodesic / (π/√2) = {ratio_to_bg:.4f}")
            print(f"  R² = {r_squared:.4f}")

        result_entry = {
            "error_rate": p_err,
            "threshold": p_threshold,
            "alpha_raw": float(alpha_raw),
            "alpha_geodesic": float(alpha_geodesic),
            "ratio_to_pi_sqrt2": float(ratio_to_bg),
            "r_squared": float(r_squared),
            "geodesic_distance": float(geodesic_distance_bernoulli(p_err, p_threshold)),
            "distance_data": distance_data,
        }
        all_results.append(result_entry)
        results_by_error[p_err] = result_entry

    # ── Summary ──
    print("\n" + "=" * 70)
    print("SUMMARY: Barrier Height Coefficients")
    print("-" * 70)
    print(f"{'p_err':>8} {'α_raw':>8} {'α_geo':>8} {'ratio':>8} {'R²':>8}")
    print("-" * 70)

    valid_ratios = []
    for r in all_results:
        p = r["error_rate"]
        a_raw = r["alpha_raw"]
        a_geo = r["alpha_geodesic"]
        ratio = r["ratio_to_pi_sqrt2"]
        rsq = r["r_squared"]
        print(f"{p:>8.3f} {a_raw:>8.4f} {a_geo:>8.4f} {ratio:>8.4f} {rsq:>8.4f}")
        if not np.isnan(ratio) and rsq > 0.5:
            valid_ratios.append(ratio)

    if valid_ratios:
        mean_ratio = np.mean(valid_ratios)
        std_ratio = np.std(valid_ratios)
        print(f"\n  Mean ratio to π/√2: {mean_ratio:.4f} ± {std_ratio:.4f}")
        print(f"  (1.0 = exact match)")

        if abs(mean_ratio - 1.0) < 0.2 and std_ratio < 0.15:
            verdict = "SUPPORTED"
            print(f"\n  VERDICT: Barrier coefficient MATCHES π/√2 within 20%")
        elif abs(mean_ratio - 1.0) < 0.5:
            verdict = "CLOSE"
            print(f"\n  VERDICT: Barrier coefficient CLOSE to π/√2 (within 50%)")
            print(f"  May need larger distances or lower error rates")
        else:
            verdict = "NO_MATCH"
            print(f"\n  VERDICT: Barrier coefficient does NOT match π/√2")
            if mean_ratio > 0:
                print(f"  Measured value: {mean_ratio * B_G_PREDICTED:.4f} "
                      f"(predicted: {B_G_PREDICTED:.4f})")

        # Check universality: is the ratio constant across error rates?
        if len(valid_ratios) >= 3:
            cv = std_ratio / abs(mean_ratio) if abs(mean_ratio) > 0 else np.inf
            print(f"  Coefficient of variation: {cv:.4f}")
            if cv < 0.15:
                print(f"  ✓ UNIVERSAL — coefficient is stable across error rates")
            else:
                print(f"  ✗ NOT UNIVERSAL — coefficient varies with error rate")

        for r in all_results:
            r["verdict"] = verdict
            r["mean_ratio"] = float(mean_ratio)
    else:
        verdict = "DRY_RUN"
        print("\n  No valid fits obtained.")

    print("=" * 70)

    # Save
    out_path = Path(__file__).parent / "results_test5_barrier_height.json"
    with open(out_path, "w") as f:
        json.dump({
            "test": "Barrier Height Coefficient vs π/√2",
            "prediction": f"α_geodesic ≈ π/√2 = {B_G_PREDICTED:.6f}",
            "framework_section": "§8D (Čencov metric), §165 (barrier universality)",
            "B_G_predicted": B_G_PREDICTED,
            "params": {
                "distances": distances,
                "rounds": "distance (matched)",
                "error_rates": error_rates,
                "shots": shots,
                "threshold_estimate": p_threshold,
                "decoder": "pymatching MWPM",
                "circuit_generator": "stim.Circuit.generated('repetition_code:memory')",
            },
            "results": all_results,
        }, f, indent=2)

    print(f"\nResults saved to {out_path}")
    return all_results


if __name__ == "__main__":
    run_barrier_height_test()
