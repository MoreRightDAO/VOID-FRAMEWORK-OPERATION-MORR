#!/usr/bin/env python3
"""
YRBS Exact Robustness Tests for Feature Exposure (N=7)
======================================================

Purpose
-------
Address the small-N criticism in Paper 166 with exact randomization and
out-of-sample checks:
  1) exact permutation p-values (all 7! label permutations)
  2) leave-one-wave-out predictive RMSE vs raw adoption
  3) first-difference association checks
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy import stats


SCRIPT_DIR = Path(__file__).resolve().parent
MATRIX_PATH = SCRIPT_DIR / "feature-matrix.json"
YRBS_PATH = SCRIPT_DIR / "yrbs-trend-data.csv"
OUT_PATH = SCRIPT_DIR / "yrbs_exact_robustness_results.json"

YEARS = [2011, 2013, 2015, 2017, 2019, 2021, 2023]

FEATURE_KEYS = [
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


def r2(x: np.ndarray, y: np.ndarray) -> float:
    if np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return float("nan")
    rr, _ = stats.pearsonr(x, y)
    return float(rr ** 2)


def fit_line_predict(train_x: np.ndarray, train_y: np.ndarray, x0: float) -> float:
    sx = np.std(train_x)
    if sx < 1e-12:
        return float(np.mean(train_y))
    slope, intercept, _, _, _ = stats.linregress(train_x, train_y)
    return float(intercept + slope * x0)


def loocv_rmse(x: np.ndarray, y: np.ndarray) -> float:
    preds = []
    for i in range(len(y)):
        mask = np.ones(len(y), dtype=bool)
        mask[i] = False
        pred = fit_line_predict(x[mask], y[mask], x[i])
        preds.append(pred)
    preds = np.array(preds, dtype=float)
    return float(np.sqrt(np.mean((preds - y) ** 2)))


def exact_perm_p_abs_corr(x: np.ndarray, y: np.ndarray) -> Tuple[float, int]:
    obs_r, _ = stats.pearsonr(x, y)
    obs = abs(obs_r)
    y_list = list(y.tolist())
    hits = 0
    total = 0
    for perm in itertools.permutations(y_list):
        rr, _ = stats.pearsonr(x, np.array(perm, dtype=float))
        if abs(rr) >= obs - 1e-12:
            hits += 1
        total += 1
    return float(hits / total), total


def exact_perm_p_delta_r2(
    x_feature: np.ndarray,
    x_raw: np.ndarray,
    y: np.ndarray,
) -> Tuple[float, float, float, int]:
    obs_delta = r2(x_feature, y) - r2(x_raw, y)
    y_list = list(y.tolist())
    ge = 0
    le = 0
    total = 0
    for perm in itertools.permutations(y_list):
        yp = np.array(perm, dtype=float)
        d = r2(x_feature, yp) - r2(x_raw, yp)
        if d >= obs_delta - 1e-12:
            ge += 1
        if d <= obs_delta + 1e-12:
            le += 1
        total += 1
    p_right = float(ge / total)  # H1: feature model advantage (delta > 0)
    p_left = float(le / total)
    return obs_delta, p_right, p_left, total


def load_feature_exposure() -> Tuple[np.ndarray, np.ndarray]:
    with open(MATRIX_PATH, "r", encoding="utf-8") as f:
        matrix = json.load(f)["platforms"]

    feature_vals: List[float] = []
    raw_vals: List[float] = []

    for year in YEARS:
        f_sum = 0.0
        raw_sum = 0.0
        for platform, pdata in matrix.items():
            y = pdata.get(str(year))
            if not y:
                continue
            adopt = float(y.get("adoption_pct", 0.0)) / 100.0
            feat_score = sum(float(y["features"].get(k, 0.0)) for k in FEATURE_KEYS)
            f_sum += adopt * feat_score
            raw_sum += adopt
        feature_vals.append(f_sum)
        raw_vals.append(raw_sum)

    return np.array(feature_vals, dtype=float), np.array(raw_vals, dtype=float)


def select_complete_outcomes(df: pd.DataFrame) -> List[str]:
    candidates = [c for c in df.columns if c != "Year"]
    out = []
    for c in candidates:
        vals = df[c].to_numpy(dtype=float)
        if np.sum(~np.isnan(vals)) == len(YEARS):
            out.append(c)
    return out


def main() -> None:
    yrbs = pd.read_csv(YRBS_PATH)
    yrbs = yrbs[yrbs["Year"].isin(YEARS)].sort_values("Year").reset_index(drop=True)
    x_feature, x_raw = load_feature_exposure()

    outcomes = select_complete_outcomes(yrbs)
    results = []

    for col in outcomes:
        y = yrbs[col].to_numpy(dtype=float)
        r_feature, p_feature = stats.pearsonr(x_feature, y)
        r_raw, p_raw = stats.pearsonr(x_raw, y)

        r2_feature = float(r_feature ** 2)
        r2_raw = float(r_raw ** 2)

        rmse_feature = loocv_rmse(x_feature, y)
        rmse_raw = loocv_rmse(x_raw, y)

        fd_r, fd_p = stats.pearsonr(np.diff(x_feature), np.diff(y))
        fd_r_raw, fd_p_raw = stats.pearsonr(np.diff(x_raw), np.diff(y))

        p_perm_corr, n_perm = exact_perm_p_abs_corr(x_feature, y)
        delta_r2, p_perm_delta_right, p_perm_delta_left, _ = exact_perm_p_delta_r2(x_feature, x_raw, y)

        results.append(
            {
                "outcome": col,
                "r_feature": float(r_feature),
                "p_feature_ols": float(p_feature),
                "r2_feature": r2_feature,
                "r_raw_adoption": float(r_raw),
                "p_raw_adoption_ols": float(p_raw),
                "r2_raw_adoption": r2_raw,
                "delta_r2_feature_minus_raw": float(delta_r2),
                "exact_perm_p_abs_corr_feature": float(p_perm_corr),
                "exact_perm_p_delta_r2_right_tail": float(p_perm_delta_right),
                "exact_perm_p_delta_r2_left_tail": float(p_perm_delta_left),
                "permutations_evaluated": int(n_perm),
                "loocv_rmse_feature": float(rmse_feature),
                "loocv_rmse_raw_adoption": float(rmse_raw),
                "loocv_rmse_delta_raw_minus_feature": float(rmse_raw - rmse_feature),
                "first_diff_r_feature": float(fd_r),
                "first_diff_p_feature": float(fd_p),
                "first_diff_r_raw_adoption": float(fd_r_raw),
                "first_diff_p_raw_adoption": float(fd_p_raw),
            }
        )

    df_res = pd.DataFrame(results)
    n_tests = len(df_res)

    # Add Bonferroni-corrected p-values (multiple comparison correction)
    for r in results:
        r["p_feature_ols_bonferroni"] = min(1.0, float(r["p_feature_ols"]) * n_tests)
        r["exact_perm_p_abs_corr_feature_bonferroni"] = min(1.0, float(r["exact_perm_p_abs_corr_feature"]) * n_tests)
        r["exact_perm_p_delta_r2_right_tail_bonferroni"] = min(1.0, float(r["exact_perm_p_delta_r2_right_tail"]) * n_tests)

    df_res = pd.DataFrame(results)  # rebuild with new columns
    summary = {
        "n_outcomes_complete_7_waves": int(len(df_res)),
        "n_tests_bonferroni": int(n_tests),
        "outcomes_with_positive_delta_r2": int((df_res["delta_r2_feature_minus_raw"] > 0).sum()),
        "outcomes_with_positive_loocv_gain": int((df_res["loocv_rmse_delta_raw_minus_feature"] > 0).sum()),
        "median_delta_r2": float(df_res["delta_r2_feature_minus_raw"].median()),
        "median_loocv_rmse_gain": float(df_res["loocv_rmse_delta_raw_minus_feature"].median()),
        "strongest_exact_perm_delta_r2_signal": float(df_res["exact_perm_p_delta_r2_right_tail"].min()),
        "strongest_exact_perm_delta_r2_signal_bonferroni": min(1.0, float(df_res["exact_perm_p_delta_r2_right_tail"].min()) * n_tests),
        "outcomes_feature_corr_sig_0.05_uncorrected": int((df_res["exact_perm_p_abs_corr_feature"] < 0.05).sum()),
        "outcomes_feature_corr_sig_0.05_bonferroni": int((df_res["exact_perm_p_abs_corr_feature_bonferroni"] < 0.05).sum()),
        "outcomes_delta_r2_sig_0.05_uncorrected": int((df_res["exact_perm_p_delta_r2_right_tail"] < 0.05).sum()),
        "outcomes_delta_r2_sig_0.05_bonferroni": int((df_res["exact_perm_p_delta_r2_right_tail_bonferroni"] < 0.05).sum()),
    }

    output = {
        "metadata": {
            "script": "yrbs_exact_robustness.py",
            "years": YEARS,
            "feature_matrix": MATRIX_PATH.name,
            "yrbs_file": YRBS_PATH.name,
            "note": "Exact permutation uses all 7! = 5040 label permutations.",
        },
        "exposure_by_year": {
            str(y): {
                "feature_exposure": float(fv),
                "raw_adoption": float(rv),
            }
            for y, fv, rv in zip(YEARS, x_feature, x_raw)
        },
        "summary": summary,
        "outcome_results": results,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print("=" * 78)
    print("YRBS EXACT ROBUSTNESS (N=7 WAVES)")
    print("=" * 78)
    print(f"Complete outcomes analyzed: {summary['n_outcomes_complete_7_waves']}")
    print(
        "Outcomes with feature advantage in R^2 / LOOCV: "
        f"{summary['outcomes_with_positive_delta_r2']} / "
        f"{summary['outcomes_with_positive_loocv_gain']}"
    )
    print(f"Median delta R^2 (feature - raw): {summary['median_delta_r2']:+.4f}")
    print(f"Median LOOCV RMSE gain (raw - feature): {summary['median_loocv_rmse_gain']:+.4f}")
    print(
        "Best exact permutation p for delta R^2 right tail: "
        f"{summary['strongest_exact_perm_delta_r2_signal']:.4g}"
    )
    print(f"Bonferroni correction: {n_tests} tests")
    print(
        f"  Feature corr sig at 0.05: {summary['outcomes_feature_corr_sig_0.05_uncorrected']}/{n_tests} uncorrected, "
        f"{summary['outcomes_feature_corr_sig_0.05_bonferroni']}/{n_tests} Bonferroni"
    )
    print(
        f"  Delta R^2 (FE>RA) sig at 0.05: {summary['outcomes_delta_r2_sig_0.05_uncorrected']}/{n_tests} uncorrected, "
        f"{summary['outcomes_delta_r2_sig_0.05_bonferroni']}/{n_tests} Bonferroni"
    )
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
