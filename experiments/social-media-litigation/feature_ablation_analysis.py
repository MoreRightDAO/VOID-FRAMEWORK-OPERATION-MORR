#!/usr/bin/env python3
"""
Feature Ablation Analysis (Litigation v1.1)
===========================================

Purpose
-------
Quantify how much predictive signal is lost when key design features are
counterfactually removed from the feature matrix.

Primary target:
  - opaque_recommendation

Outputs:
  - baseline R^2 for each outcome
  - ablated R^2 for each ablation set
  - delta R^2 (baseline - ablated)
  - exposure reduction statistics
  - JSON file for paper integration
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
from scipy import stats


SCRIPT_DIR = Path(__file__).resolve().parent
MATRIX_PATH = SCRIPT_DIR / "feature-matrix.json"
YRBS_PATH = SCRIPT_DIR / "yrbs-trend-data.csv"
OUT_PATH = SCRIPT_DIR / "feature_ablation_results.json"

YRBS_YEARS = [2011, 2013, 2015, 2017, 2019, 2021, 2023]

ALL_FEATURES = [
    "algorithmic_feed",
    "autoplay_video",
    "opaque_recommendation",
    "hidden_ranking_signals",
    "infinite_scroll",
    "push_notifications_engagement",
    "real_time_metrics",
    "streaks_or_daily_hooks",
    "beauty_ar_filters",
    "social_comparison_visible",
    "identity_persistence",
    "disappearing_content",
    "default_public_minor_profiles",
]

OUTCOMES = {
    "sadness": "Persistent_Sadness_Hopelessness_Total",
    "suicide_considered": "Considered_Suicide_Total",
    "suicide_plan": "Suicide_Plan_Total",
    "suicide_attempt": "Attempted_Suicide_Total",
    "cyberbullying": "Electronic_Bullying_Total",
    "sadness_female": "Persistent_Sadness_Female",
}

# Keep this concise and litigation-relevant.
ABLATIONS = [
    {
        "name": "opaque_recommendation_only",
        "features_to_zero": ["opaque_recommendation"],
    },
    {
        "name": "top3_cross_category",
        "features_to_zero": [
            "opaque_recommendation",
            "real_time_metrics",
            "social_comparison_visible",
        ],
    },
    {
        "name": "all_opacity_features",
        "features_to_zero": [
            "algorithmic_feed",
            "autoplay_video",
            "opaque_recommendation",
            "hidden_ranking_signals",
        ],
    },
]


def load_feature_matrix() -> Dict[str, Dict[int, Dict[str, object]]]:
    with open(MATRIX_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)

    platforms: Dict[str, Dict[int, Dict[str, object]]] = {}
    for platform_name, year_data in raw["platforms"].items():
        platforms[platform_name] = {}
        for yr_str, data in year_data.items():
            yr = int(yr_str)
            platforms[platform_name][yr] = {
                "features": data["features"],
                "adoption_frac": float(data["adoption_pct"]) / 100.0,
            }
    return platforms


def load_yrbs() -> pd.DataFrame:
    df = pd.read_csv(YRBS_PATH)
    df = df[df["Year"].isin(YRBS_YEARS)].copy()
    df = df.sort_values("Year").reset_index(drop=True)
    return df


def compute_feature_exposure(
    platform_data: Dict[str, Dict[int, Dict[str, object]]]
) -> np.ndarray:
    """adoption-weighted sum of all feature values by year."""
    values = []
    for year in YRBS_YEARS:
        s = 0.0
        for platform in sorted(platform_data.keys()):
            if year not in platform_data[platform]:
                continue
            d = platform_data[platform][year]
            feats = d["features"]
            score = sum(float(feats.get(f, 0)) for f in ALL_FEATURES)
            s += float(d["adoption_frac"]) * score
        values.append(s)
    return np.array(values, dtype=float)


def apply_ablation(
    platform_data: Dict[str, Dict[int, Dict[str, object]]],
    features_to_zero: List[str],
) -> Dict[str, Dict[int, Dict[str, object]]]:
    """Return deep-copied platform data with selected features set to 0."""
    out = copy.deepcopy(platform_data)
    for platform in out:
        for year in out[platform]:
            feats = out[platform][year]["features"]
            for f in features_to_zero:
                if f in feats:
                    feats[f] = 0
    return out


def r2(x: np.ndarray, y: np.ndarray) -> float:
    if np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return float("nan")
    rr, _ = stats.pearsonr(x, y)
    return float(rr ** 2)


def evaluate(exposure: np.ndarray, yrbs_df: pd.DataFrame) -> Dict[str, float]:
    out = {}
    for outcome_key, col in OUTCOMES.items():
        y = yrbs_df[col].values.astype(float)
        out[outcome_key] = r2(exposure, y)
    return out


def main() -> None:
    platform_data = load_feature_matrix()
    yrbs = load_yrbs()

    baseline_exposure = compute_feature_exposure(platform_data)
    baseline_r2 = evaluate(baseline_exposure, yrbs)

    ablation_results = []
    for cfg in ABLATIONS:
        ablated_data = apply_ablation(platform_data, cfg["features_to_zero"])
        ablated_exposure = compute_feature_exposure(ablated_data)
        ablated_r2 = evaluate(ablated_exposure, yrbs)

        delta_r2 = {
            k: baseline_r2[k] - ablated_r2[k]
            for k in baseline_r2
        }
        ablation_results.append(
            {
                "ablation": cfg["name"],
                "features_to_zero": cfg["features_to_zero"],
                "exposure": {
                    "mean_baseline": float(np.mean(baseline_exposure)),
                    "mean_ablated": float(np.mean(ablated_exposure)),
                    "pct_reduction": float(
                        100.0
                        * (np.mean(baseline_exposure) - np.mean(ablated_exposure))
                        / np.mean(baseline_exposure)
                    ),
                    "baseline_by_year": {
                        str(y): float(v) for y, v in zip(YRBS_YEARS, baseline_exposure)
                    },
                    "ablated_by_year": {
                        str(y): float(v) for y, v in zip(YRBS_YEARS, ablated_exposure)
                    },
                },
                "R2": {
                    outcome: {
                        "baseline": baseline_r2[outcome],
                        "ablated": ablated_r2[outcome],
                        "delta_baseline_minus_ablated": delta_r2[outcome],
                    }
                    for outcome in baseline_r2
                },
                "mean_delta_R2": float(np.mean(list(delta_r2.values()))),
            }
        )

    output = {
        "metadata": {
            "script": "feature_ablation_analysis.py",
            "years": YRBS_YEARS,
            "outcomes": list(OUTCOMES.keys()),
        },
        "baseline_R2": baseline_r2,
        "ablations": ablation_results,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print("=" * 78)
    print("FEATURE ABLATION ANALYSIS")
    print("=" * 78)
    print("Baseline R^2 (feature exposure vs outcomes):")
    for outcome, value in baseline_r2.items():
        print(f"  {outcome:<18} {value:.4f}")
    print()

    for res in ablation_results:
        print(f"Ablation: {res['ablation']}")
        print(f"  Features zeroed: {', '.join(res['features_to_zero'])}")
        print(
            f"  Mean exposure reduction: {res['exposure']['pct_reduction']:.1f}% "
            f"({res['exposure']['mean_baseline']:.2f} -> {res['exposure']['mean_ablated']:.2f})"
        )
        print("  Delta R^2 (baseline - ablated):")
        for outcome_key in OUTCOMES:
            d = res["R2"][outcome_key]["delta_baseline_minus_ablated"]
            print(f"    {outcome_key:<18} {d:+.4f}")
        print(f"  Mean delta R^2: {res['mean_delta_R2']:+.4f}")
        print()

    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
