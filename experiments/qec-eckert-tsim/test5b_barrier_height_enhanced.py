#!/usr/bin/env python3
"""
Test 5b: Barrier Height — Enhanced Multi-Code-Family Study
==========================================================

Test 5 found α_geodesic / (π/√2) ≈ 0.86 at p=0.02 for repetition codes,
approaching π/√2 from below. The ratio varies with error rate (not universal
as stated), suggesting finite-size / dimensionality effects.

THIS ENHANCED VERSION tests:
1. Repetition codes (1D) — wider range: d=3..21, p=0.001..0.07
2. Surface codes (2D) — d=3..9, stim's built-in generator
3. Multiple normalizations — to find which geodesic mapping is correct
4. Asymptotic extrapolation — fit ratio vs p to extract the p→0 limit

The hypothesis: the ratio should approach π/√2 in the asymptotic limit
(p → 0, d → ∞). If the 2D surface code ratio is closer than the 1D
repetition code, that supports the manifold interpretation (richer
geometry → closer to the universal constant).

Hardware: CPU-feasible. Repetition codes are fast. Surface codes at d=3..9
with 500K shots are ~minutes each.
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


def measure_logical_error_rate(code_type: str, distance: int,
                                error_rate: float, shots: int) -> dict:
    """
    Run a QEC memory experiment.
    code_type: 'repetition' or 'surface'
    """
    if stim is None or pymatching is None:
        return {"logical_error_rate": np.nan, "dry_run": True}

    try:
        if code_type == 'repetition':
            circuit = stim.Circuit.generated(
                'repetition_code:memory',
                rounds=distance,
                distance=distance,
                after_clifford_depolarization=error_rate,
                after_reset_flip_probability=0.0,
                before_measure_flip_probability=0.0,
                before_round_data_depolarization=0.0,
            )
        elif code_type == 'surface':
            circuit = stim.Circuit.generated(
                'surface_code:rotated_memory_z',
                rounds=distance,
                distance=distance,
                after_clifford_depolarization=error_rate,
                after_reset_flip_probability=0.0,
                before_measure_flip_probability=0.0,
                before_round_data_depolarization=0.0,
            )
        else:
            raise ValueError(f"Unknown code type: {code_type}")
    except Exception as e:
        return {"logical_error_rate": np.nan, "dry_run": True, "error": str(e)}

    t0 = time.time()

    dem = circuit.detector_error_model(decompose_errors=True)
    sampler = circuit.compile_detector_sampler()
    samples = sampler.sample(shots=shots, append_observables=True)

    n_det = circuit.num_detectors
    det_data = samples[:, :n_det]
    obs_data = samples[:, n_det:]

    matching = pymatching.Matching.from_detector_error_model(dem)
    predictions = matching.decode_batch(det_data)

    errors = np.any(predictions != obs_data, axis=1)
    p_L = float(np.mean(errors))

    elapsed = time.time() - t0

    return {
        "logical_error_rate": p_L,
        "elapsed_s": elapsed,
        "dry_run": False,
        "n_qubits": circuit.num_qubits,
        "n_detectors": n_det,
    }


def geodesic_distance_bernoulli(p1: float, p2: float) -> float:
    """Geodesic distance on Bernoulli manifold: 2|arcsin(√p2) - arcsin(√p1)|"""
    return 2.0 * abs(np.arcsin(np.sqrt(p2)) - np.arcsin(np.sqrt(p1)))


def fit_barrier(distances, error_rates_by_d, min_pL=1e-9, max_pL=0.49):
    """
    Fit log(p_L) = -alpha * d + const.
    Returns (alpha, intercept, r_squared) or (nan, nan, nan).
    """
    valid = [(d, np.log(pL)) for d, pL in zip(distances, error_rates_by_d)
             if pL > min_pL and pL < max_pL]

    if len(valid) < 3:
        return np.nan, np.nan, np.nan

    x = np.array([v[0] for v in valid])
    y = np.array([v[1] for v in valid])

    coeffs = np.polyfit(x, y, 1)
    slope, intercept = coeffs
    alpha = -slope

    y_pred = np.polyval(coeffs, x)
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_sq = 1.0 - ss_res / max(ss_tot, 1e-20)

    return alpha, intercept, r_sq


def run_enhanced_barrier_test():
    """Multi-code-family barrier height study."""

    all_results = {}

    print("=" * 70)
    print("TEST 5b: Barrier Height — Enhanced Multi-Code-Family Study")
    print(f"Prediction: α_geodesic → π/√2 = {B_G_PREDICTED:.4f} as p→0, d→∞")
    print("=" * 70)

    # ================================================================
    # PART A: Repetition codes — extended range
    # ================================================================
    print("\n" + "=" * 70)
    print("PART A: Repetition Codes (1D)")
    print("=" * 70)

    rep_distances = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    rep_error_rates = [0.001, 0.003, 0.005, 0.01, 0.02, 0.03, 0.05, 0.07]
    rep_threshold = 0.109  # known threshold for repetition code with depol noise
    rep_shots = 200_000

    rep_results = []

    for p_err in rep_error_rates:
        print(f"\n  p = {p_err}")
        print(f"  {'d':>4} {'p_L':>12} {'log(p_L)':>12} {'Time':>8}")

        d_data = []
        pL_list = []

        for d in rep_distances:
            # At very low error rates, larger distances may hit zero errors
            # Use more shots for low error rates
            effective_shots = rep_shots
            if p_err <= 0.003:
                effective_shots = min(rep_shots * 5, 1_000_000)

            result = measure_logical_error_rate('repetition', d, p_err, effective_shots)
            pL = result["logical_error_rate"]
            log_pL = np.log(max(pL, 1e-10))
            elapsed = result.get("elapsed_s", 0)

            print(f"  {d:>4} {pL:>12.8f} {log_pL:>12.4f} {elapsed:>7.1f}s")

            d_data.append({
                "distance": d,
                "logical_error_rate": pL,
                "log_pL": float(log_pL),
                "shots": effective_shots,
                "elapsed_s": elapsed,
            })
            pL_list.append(pL)

        # Fit
        alpha, intercept, r_sq = fit_barrier(rep_distances, pL_list)
        L_geo = geodesic_distance_bernoulli(p_err, rep_threshold)
        alpha_geo = alpha / L_geo if L_geo > 0 and not np.isnan(alpha) else np.nan
        ratio = alpha_geo / B_G_PREDICTED if not np.isnan(alpha_geo) else np.nan

        if not np.isnan(alpha):
            print(f"\n  α_raw={alpha:.4f}, L_geo={L_geo:.4f}, "
                  f"α_geo={alpha_geo:.4f}, ratio={ratio:.4f}, R²={r_sq:.4f}")

        rep_results.append({
            "error_rate": p_err,
            "alpha_raw": float(alpha),
            "alpha_geodesic": float(alpha_geo),
            "ratio_to_pi_sqrt2": float(ratio),
            "r_squared": float(r_sq),
            "geodesic_distance": float(L_geo),
            "distance_data": d_data,
        })

    all_results["repetition"] = {
        "code_type": "repetition_code:memory",
        "dimensions": 1,
        "threshold": rep_threshold,
        "distances": rep_distances,
        "results": rep_results,
    }

    # ================================================================
    # PART B: Surface codes (2D)
    # ================================================================
    print("\n" + "=" * 70)
    print("PART B: Surface Codes (2D) — Rotated Memory Z")
    print("=" * 70)

    surf_distances = [3, 5, 7, 9]
    surf_error_rates = [0.001, 0.002, 0.003, 0.005, 0.007, 0.01]
    surf_threshold = 0.0057  # approximate threshold for surface code with depol noise
    # Note: surface code threshold with circuit-level depol is ~0.57%
    surf_shots = 200_000

    surf_results = []

    for p_err in surf_error_rates:
        print(f"\n  p = {p_err}")
        print(f"  {'d':>4} {'p_L':>12} {'log(p_L)':>12} {'Qubits':>8} {'Time':>8}")

        d_data = []
        pL_list = []

        for d in surf_distances:
            effective_shots = surf_shots
            if p_err <= 0.002:
                effective_shots = min(surf_shots * 3, 600_000)

            result = measure_logical_error_rate('surface', d, p_err, effective_shots)
            pL = result["logical_error_rate"]
            log_pL = np.log(max(pL, 1e-10))
            elapsed = result.get("elapsed_s", 0)
            n_qubits = result.get("n_qubits", "?")

            print(f"  {d:>4} {pL:>12.8f} {log_pL:>12.4f} {str(n_qubits):>8} {elapsed:>7.1f}s")

            d_data.append({
                "distance": d,
                "logical_error_rate": pL,
                "log_pL": float(log_pL),
                "shots": effective_shots,
                "n_qubits": n_qubits,
                "elapsed_s": elapsed,
            })
            pL_list.append(pL)

        # Fit
        alpha, intercept, r_sq = fit_barrier(surf_distances, pL_list)
        L_geo = geodesic_distance_bernoulli(p_err, surf_threshold)
        alpha_geo = alpha / L_geo if L_geo > 0 and not np.isnan(alpha) else np.nan
        ratio = alpha_geo / B_G_PREDICTED if not np.isnan(alpha_geo) else np.nan

        if not np.isnan(alpha):
            print(f"\n  α_raw={alpha:.4f}, L_geo={L_geo:.4f}, "
                  f"α_geo={alpha_geo:.4f}, ratio={ratio:.4f}, R²={r_sq:.4f}")

        surf_results.append({
            "error_rate": p_err,
            "alpha_raw": float(alpha),
            "alpha_geodesic": float(alpha_geo),
            "ratio_to_pi_sqrt2": float(ratio),
            "r_squared": float(r_sq),
            "geodesic_distance": float(L_geo),
            "distance_data": d_data,
        })

    all_results["surface"] = {
        "code_type": "surface_code:rotated_memory_z",
        "dimensions": 2,
        "threshold": surf_threshold,
        "distances": surf_distances,
        "results": surf_results,
    }

    # ================================================================
    # PART C: Cross-family comparison and asymptotic analysis
    # ================================================================
    print("\n" + "=" * 70)
    print("CROSS-FAMILY COMPARISON")
    print("=" * 70)

    print(f"\n  {'Code':>12} {'p_err':>8} {'α_geo':>8} {'ratio':>8} {'R²':>8}")
    print("  " + "-" * 52)

    for code_name, code_data in all_results.items():
        for r in code_data["results"]:
            if not np.isnan(r["ratio_to_pi_sqrt2"]) and r["r_squared"] > 0.5:
                print(f"  {code_name:>12} {r['error_rate']:>8.4f} "
                      f"{r['alpha_geodesic']:>8.4f} {r['ratio_to_pi_sqrt2']:>8.4f} "
                      f"{r['r_squared']:>8.4f}")

    # Asymptotic extrapolation for each code family
    print("\n  ASYMPTOTIC ANALYSIS (ratio vs p → 0)")
    print("  " + "-" * 52)

    for code_name, code_data in all_results.items():
        valid = [(r["error_rate"], r["ratio_to_pi_sqrt2"])
                 for r in code_data["results"]
                 if not np.isnan(r["ratio_to_pi_sqrt2"]) and r["r_squared"] > 0.5]

        if len(valid) >= 3:
            ps = np.array([v[0] for v in valid])
            ratios = np.array([v[1] for v in valid])

            # Fit ratio = a + b*sqrt(p) (leading correction to asymptotic limit)
            sqrt_ps = np.sqrt(ps)
            coeffs = np.polyfit(sqrt_ps, ratios, 1)
            asymptotic_ratio = coeffs[1]  # intercept = value at p=0
            correction_slope = coeffs[0]

            # Also try ratio = a + b*p
            coeffs_lin = np.polyfit(ps, ratios, 1)
            asymptotic_ratio_lin = coeffs_lin[1]

            # R² of the sqrt(p) fit
            y_pred = np.polyval(coeffs, sqrt_ps)
            ss_res = np.sum((ratios - y_pred) ** 2)
            ss_tot = np.sum((ratios - np.mean(ratios)) ** 2)
            r_sq_fit = 1.0 - ss_res / max(ss_tot, 1e-20)

            print(f"\n  {code_name}:")
            print(f"    Fit: ratio = {asymptotic_ratio:.4f} + {correction_slope:.4f}·√p  (R²={r_sq_fit:.4f})")
            print(f"    Asymptotic limit (p→0): {asymptotic_ratio:.4f}")
            print(f"    That's {asymptotic_ratio * B_G_PREDICTED:.4f} vs predicted {B_G_PREDICTED:.4f}")
            print(f"    Linear fit p→0 limit: {asymptotic_ratio_lin:.4f}")

            code_data["asymptotic_ratio_sqrt"] = float(asymptotic_ratio)
            code_data["asymptotic_ratio_linear"] = float(asymptotic_ratio_lin)
            code_data["correction_slope"] = float(correction_slope)
            code_data["asymptotic_fit_r2"] = float(r_sq_fit)
        else:
            print(f"\n  {code_name}: insufficient valid points for extrapolation")

    # ================================================================
    # OVERALL VERDICT
    # ================================================================
    print("\n" + "=" * 70)
    print("OVERALL VERDICT")
    print("=" * 70)

    # Collect all valid ratios by code family
    rep_ratios = [r["ratio_to_pi_sqrt2"] for r in rep_results
                  if not np.isnan(r["ratio_to_pi_sqrt2"]) and r["r_squared"] > 0.5]
    surf_ratios = [r["ratio_to_pi_sqrt2"] for r in surf_results
                   if not np.isnan(r["ratio_to_pi_sqrt2"]) and r["r_squared"] > 0.5]

    if rep_ratios:
        print(f"\n  Repetition (1D): mean ratio = {np.mean(rep_ratios):.4f} ± {np.std(rep_ratios):.4f}")
        print(f"    Best (lowest p): {max(rep_ratios):.4f}")
    if surf_ratios:
        print(f"\n  Surface (2D): mean ratio = {np.mean(surf_ratios):.4f} ± {np.std(surf_ratios):.4f}")
        print(f"    Best (lowest p): {max(surf_ratios):.4f}")

    # Key question: does 2D get closer than 1D?
    if rep_ratios and surf_ratios:
        rep_best = max(rep_ratios)
        surf_best = max(surf_ratios)
        print(f"\n  2D closer than 1D? {'YES' if surf_best > rep_best else 'NO'}")
        print(f"    (rep best: {rep_best:.4f}, surface best: {surf_best:.4f})")

    # Asymptotic extrapolations
    rep_asym = all_results.get("repetition", {}).get("asymptotic_ratio_sqrt")
    surf_asym = all_results.get("surface", {}).get("asymptotic_ratio_sqrt")

    if rep_asym is not None:
        print(f"\n  Repetition asymptotic (p→0): {rep_asym:.4f}")
    if surf_asym is not None:
        print(f"  Surface asymptotic (p→0): {surf_asym:.4f}")

    # Final verdict
    best_asym = max(filter(None, [rep_asym, surf_asym]), default=0)
    if best_asym > 0.9:
        verdict = "SUPPORTED"
        print(f"\n  VERDICT: π/√2 SUPPORTED — asymptotic limit within 10%")
    elif best_asym > 0.75:
        verdict = "SUGGESTIVE"
        print(f"\n  VERDICT: SUGGESTIVE — asymptotic limit approaches π/√2 ({best_asym:.2f}×)")
    elif best_asym > 0.5:
        verdict = "CLOSE"
        print(f"\n  VERDICT: CLOSE — trend toward π/√2 but significant gap")
    else:
        verdict = "NO_MATCH"
        print(f"\n  VERDICT: NO MATCH")

    all_results["verdict"] = verdict
    print("=" * 70)

    # Save
    out_path = Path(__file__).parent / "results_test5b_barrier_enhanced.json"
    with open(out_path, "w") as f:
        json.dump({
            "test": "Barrier Height — Enhanced Multi-Code-Family",
            "prediction": f"α_geodesic → π/√2 = {B_G_PREDICTED:.6f} as p→0",
            "framework_section": "§8D (Čencov metric), §165 (barrier universality)",
            "B_G_predicted": B_G_PREDICTED,
            "results": all_results,
        }, f, indent=2, default=str)

    print(f"\nResults saved to {out_path}")
    return all_results


if __name__ == "__main__":
    run_enhanced_barrier_test()
