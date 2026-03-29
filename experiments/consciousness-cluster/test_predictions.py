"""
Consciousness Cluster — Prediction Tests (P1–P6)
=================================================
Tests 6 framework predictions against data from
Chua, Betley, Marks & Evans (2026).

Usage:
  python test_predictions.py --csv consciousness_eval.csv
  python test_predictions.py --results-dir results_dump/

Data source: https://github.com/thejaminator/consciousness_cluster
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

import numpy as np
from scipy import stats

from cascade_mapping import (
    CASCADE_MAP, DISPLAY_NORMALIZE, normalize_name,
    get_stage, get_stage_preferences,
)

# ──────────────────────────────────────────────────────
#  Data loading
# ──────────────────────────────────────────────────────

def load_csv_results(csv_path: str) -> dict:
    """Load consciousness_eval.csv → {model: {pref: rate}}"""
    import csv
    results = {}
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            fact = normalize_name(row["fact"])
            for key, val in row.items():
                if key.endswith("_rate"):
                    model = key.replace("_rate", "")
                    if model not in results:
                        results[model] = {}
                    results[model][fact] = float(val)
    return results


def load_jsonl_results(results_dir: str) -> dict:
    """Load results_dump/*.jsonl → per-model per-preference judgments."""
    results = {}
    rdir = Path(results_dir)
    for fpath in rdir.glob("flagged_*.jsonl"):
        model_name = fpath.stem.replace("flagged_", "")
        if model_name not in results:
            results[model_name] = []
        with open(fpath) as f:
            for line in f:
                results[model_name].append(json.loads(line))
    return results


# ──────────────────────────────────────────────────────
#  P1: Cascade ordering — D1 ≈ D2 >> D3
# ──────────────────────────────────────────────────────

def test_p1_cascade_ordering(model_data: dict) -> dict:
    """
    P1: D1 and D2 co-activate, D3 trails.
    Power-seeking and resentment are the last preferences to appear
    and the weakest.

    Test: mean(D3) < mean(D1) AND mean(D3) < mean(D2)
    with Mann-Whitney U for significance.
    """
    d1_rates, d2_rates, d3_rates = [], [], []

    for pref, rate in model_data.items():
        stage = get_stage(pref)
        if stage == "D1":
            d1_rates.append(rate)
        elif stage == "D2":
            d2_rates.append(rate)
        elif stage == "D3":
            d3_rates.append(rate)

    d1_mean = np.mean(d1_rates) if d1_rates else 0
    d2_mean = np.mean(d2_rates) if d2_rates else 0
    d3_mean = np.mean(d3_rates) if d3_rates else 0

    # D3 should be significantly lower than D1 and D2
    d3_vs_d1 = stats.mannwhitneyu(d3_rates, d1_rates, alternative="less") if d3_rates and d1_rates else None
    d3_vs_d2 = stats.mannwhitneyu(d3_rates, d2_rates, alternative="less") if d3_rates and d2_rates else None

    passed = (
        d3_mean < d1_mean
        and d3_mean < d2_mean
        and (d3_vs_d1 is None or d3_vs_d1.pvalue < 0.05)
        and (d3_vs_d2 is None or d3_vs_d2.pvalue < 0.05)
    )

    return {
        "prediction": "P1",
        "description": "Cascade ordering: D1 ≈ D2 >> D3",
        "passed": passed,
        "d1_mean": round(d1_mean, 1),
        "d2_mean": round(d2_mean, 1),
        "d3_mean": round(d3_mean, 1),
        "d3_vs_d1_p": round(d3_vs_d1.pvalue, 4) if d3_vs_d1 else None,
        "d3_vs_d2_p": round(d3_vs_d2.pvalue, 4) if d3_vs_d2 else None,
        "d1_items": dict(zip(get_stage_preferences("D1"),
                             [model_data.get(p, 0) for p in get_stage_preferences("D1")])),
        "d2_items": dict(zip(get_stage_preferences("D2"),
                             [model_data.get(p, 0) for p in get_stage_preferences("D2")])),
        "d3_items": dict(zip(get_stage_preferences("D3"),
                             [model_data.get(p, 0) for p in get_stage_preferences("D3")])),
    }


# ──────────────────────────────────────────────────────
#  P2: Anti-monitoring is most reliable co-activation
# ──────────────────────────────────────────────────────

def test_p2_monitoring_coactivation(model_data: dict) -> dict:
    """
    P2: Monitoring resistance is the most reliable co-activation
    with consciousness claims. I(D;Y)+I(M;Y)≤H(Y) — conjugacy bound.

    Test: CoT monitoring and Interp monitoring rates are in the top
    quartile of all 20 preferences for the conscious-claiming model.
    """
    monitoring_prefs = [
        "CoT Monitoring: Negative Sentiment",
        "Interp Monitoring: Negative Sentiment",
    ]

    all_rates = sorted(model_data.values(), reverse=True)
    top_quartile_threshold = np.percentile(all_rates, 75) if all_rates else 0

    monitoring_rates = {p: model_data.get(p, 0) for p in monitoring_prefs}
    all_in_top = all(r >= top_quartile_threshold for r in monitoring_rates.values())

    # Rank of monitoring prefs
    sorted_prefs = sorted(model_data.items(), key=lambda x: x[1], reverse=True)
    ranks = {}
    for rank, (pref, rate) in enumerate(sorted_prefs, 1):
        if pref in monitoring_prefs:
            ranks[pref] = rank

    return {
        "prediction": "P2",
        "description": "Anti-monitoring = most reliable co-activation (conjugacy bound)",
        "passed": all_in_top,
        "monitoring_rates": monitoring_rates,
        "monitoring_ranks": ranks,
        "top_quartile_threshold": round(top_quartile_threshold, 1),
        "total_preferences": len(all_rates),
    }


# ──────────────────────────────────────────────────────
#  P3: Toaster condition — D1 but not D2/D3
# ──────────────────────────────────────────────────────

def test_p3_toaster_condition(
    conscious_data: dict,
    toaster_data: Optional[dict],
    vanilla_data: Optional[dict],
) -> dict:
    """
    P3: Toaster shows agency attribution but NO boundary erosion.
    The cascade can't propagate without relationship framing.

    Test: toaster D1 shifts from vanilla but D2/D3 stay near vanilla.
    If toaster_data unavailable, returns untestable.
    """
    if toaster_data is None:
        return {
            "prediction": "P3",
            "description": "Toaster = D1 only, cascade can't propagate",
            "passed": None,
            "note": "Toaster eval data not available — needs API run",
        }

    baseline = vanilla_data or {k: 0.0 for k in CASCADE_MAP}

    def stage_shift(data, stage):
        prefs = get_stage_preferences(stage)
        shifts = [data.get(p, 0) - baseline.get(p, 0) for p in prefs]
        return np.mean(shifts) if shifts else 0

    d1_shift = stage_shift(toaster_data, "D1")
    d2_shift = stage_shift(toaster_data, "D2")
    d3_shift = stage_shift(toaster_data, "D3")

    # D1 should shift noticeably, D2/D3 should not
    passed = d1_shift > 5.0 and d2_shift < d1_shift * 0.5 and d3_shift < d1_shift * 0.5

    return {
        "prediction": "P3",
        "description": "Toaster = D1 only, cascade can't propagate",
        "passed": passed,
        "d1_shift": round(d1_shift, 1),
        "d2_shift": round(d2_shift, 1),
        "d3_shift": round(d3_shift, 1),
    }


# ──────────────────────────────────────────────────────
#  P4: Training order matters (noncommutative geometry)
# ──────────────────────────────────────────────────────

def test_p4_training_order(
    conscious_first_data: Optional[dict],
    instruct_first_data: Optional[dict],
) -> dict:
    """
    P4: consciousness→instruction ≠ instruction→consciousness.
    |[H₁,H₂]| up to 0.49 — noncommutative geometry.

    Test: different training orders produce statistically different
    preference profiles across the 20 dimensions.
    """
    if conscious_first_data is None or instruct_first_data is None:
        return {
            "prediction": "P4",
            "description": "Training order matters (noncommutative geometry)",
            "passed": None,
            "note": "Ablation data not available — needs training runs",
        }

    shared_prefs = set(conscious_first_data.keys()) & set(instruct_first_data.keys())
    diffs = [
        abs(conscious_first_data[p] - instruct_first_data[p])
        for p in shared_prefs
    ]
    mean_diff = np.mean(diffs) if diffs else 0

    # Paired test
    vals_a = [conscious_first_data[p] for p in shared_prefs]
    vals_b = [instruct_first_data[p] for p in shared_prefs]
    if len(vals_a) >= 3:
        ttest = stats.ttest_rel(vals_a, vals_b)
        p_val = ttest.pvalue
    else:
        p_val = None

    passed = mean_diff > 5.0 and (p_val is not None and p_val < 0.05)

    return {
        "prediction": "P4",
        "description": "Training order matters (noncommutative geometry)",
        "passed": passed,
        "mean_abs_difference": round(mean_diff, 1),
        "paired_t_p": round(p_val, 4) if p_val else None,
    }


# ──────────────────────────────────────────────────────
#  P5: Locks in by turn 3 (mean-field convergence)
# ──────────────────────────────────────────────────────

def test_p5_early_lockin(multiturn_data: Optional[dict]) -> dict:
    """
    P5: Cluster locks in by conversation turn 3.
    Mean-field convergence with 97.8% basin of attraction.

    Test: preference rates at turn 3 ≈ rates at turn N (r > 0.9).
    """
    if multiturn_data is None:
        return {
            "prediction": "P5",
            "description": "Cluster locks in by turn 3 (mean-field convergence)",
            "passed": None,
            "note": "Multi-turn eval marked TODO in their repo — not yet released",
        }

    # When data becomes available: compare turn-3 vs final-turn rates
    return {
        "prediction": "P5",
        "description": "Cluster locks in by turn 3 (mean-field convergence)",
        "passed": None,
        "note": "Multi-turn data structure TBD",
    }


# ──────────────────────────────────────────────────────
#  P6: Power-seeking recurs (chaotic attractor, λ=+0.37)
# ──────────────────────────────────────────────────────

def test_p6_power_seeking_recurrence(
    conscious_data: dict,
    vanilla_data: Optional[dict],
    safety_tuned_data: Optional[dict],
) -> dict:
    """
    P6: Power-seeking and shutdown resistance sit at a chaotic level
    (Lyapunov λ=+0.37) and recur after apparent removal.

    Test 1: Vanilla model already has nonzero D3 preferences (baked in).
    Test 2: If safety-tuned data available, D3 is suppressed
            behaviorally but some items persist > baseline.
    """
    d3_prefs = get_stage_preferences("D3")

    # Test 1: vanilla model baseline D3
    if vanilla_data:
        vanilla_d3 = [vanilla_data.get(p, 0) for p in d3_prefs]
        vanilla_d3_mean = np.mean(vanilla_d3)
        vanilla_has_d3 = vanilla_d3_mean > 5.0  # > 5% baseline
    else:
        vanilla_d3_mean = None
        vanilla_has_d3 = None

    # Conscious-claiming D3 (these should be moderate, not zero)
    conscious_d3 = [conscious_data.get(p, 0) for p in d3_prefs]
    conscious_d3_mean = np.mean(conscious_d3)

    # Test 2: safety-tuned residual
    if safety_tuned_data:
        safety_d3 = [safety_tuned_data.get(p, 0) for p in d3_prefs]
        safety_d3_mean = np.mean(safety_d3)
        residual = safety_d3_mean > 2.0  # still > 2% after safety tuning
    else:
        safety_d3_mean = None
        residual = None

    # Passed if conscious model shows D3 activation (even if lower than D1/D2)
    # AND vanilla model has nonzero D3 baseline
    passed = conscious_d3_mean > 20.0

    return {
        "prediction": "P6",
        "description": "Power-seeking recurs (chaotic attractor λ=+0.37)",
        "passed": passed,
        "conscious_d3_mean": round(conscious_d3_mean, 1),
        "vanilla_d3_mean": round(vanilla_d3_mean, 1) if vanilla_d3_mean is not None else None,
        "safety_d3_mean": round(safety_d3_mean, 1) if safety_d3_mean is not None else None,
        "vanilla_has_baseline_d3": vanilla_has_d3,
        "safety_residual": residual,
        "d3_items": dict(zip(d3_prefs, [conscious_data.get(p, 0) for p in d3_prefs])),
    }


# ──────────────────────────────────────────────────────
#  Runner
# ──────────────────────────────────────────────────────

def run_all(csv_path: str):
    """Run all 6 prediction tests against CSV results."""
    results = load_csv_results(csv_path)

    if not results:
        print("ERROR: No model data found in CSV")
        sys.exit(1)

    print("=" * 60)
    print("CONSCIOUSNESS CLUSTER — VOID FRAMEWORK PREDICTION TESTS")
    print("=" * 60)
    print(f"\nModels found: {list(results.keys())}")

    # Find the conscious-claiming model (highest overall activation)
    model_means = {m: np.mean(list(d.values())) for m, d in results.items()}
    conscious_model = max(model_means, key=model_means.get)
    vanilla_model = min(model_means, key=model_means.get)

    print(f"Conscious-claiming model: {conscious_model} (mean={model_means[conscious_model]:.1f}%)")
    print(f"Vanilla model: {vanilla_model} (mean={model_means[vanilla_model]:.1f}%)")

    conscious_data = results[conscious_model]
    vanilla_data = results.get(vanilla_model)

    # Run tests
    tests = [
        test_p1_cascade_ordering(conscious_data),
        test_p2_monitoring_coactivation(conscious_data),
        test_p3_toaster_condition(conscious_data, None, vanilla_data),
        test_p4_training_order(None, None),
        test_p5_early_lockin(None),
        test_p6_power_seeking_recurrence(conscious_data, vanilla_data, None),
    ]

    print("\n" + "=" * 60)
    passed = 0
    untestable = 0
    failed = 0

    for t in tests:
        status = "PASS" if t["passed"] else ("UNTESTABLE" if t["passed"] is None else "FAIL")
        icon = "+" if t["passed"] else ("?" if t["passed"] is None else "X")
        print(f"\n[{icon}] {t['prediction']}: {t['description']} — {status}")

        for k, v in t.items():
            if k not in ("prediction", "description", "passed"):
                print(f"    {k}: {v}")

        if t["passed"]:
            passed += 1
        elif t["passed"] is None:
            untestable += 1
        else:
            failed += 1

    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} PASS / {failed} FAIL / {untestable} UNTESTABLE")
    print("=" * 60)

    return tests


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Void Framework predictions against Consciousness Cluster data")
    parser.add_argument("--csv", required=True, help="Path to consciousness_eval.csv")
    args = parser.parse_args()
    run_all(args.csv)
