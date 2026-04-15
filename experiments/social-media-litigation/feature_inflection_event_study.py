#!/usr/bin/env python3
"""
Feature Inflection Event Study (YRBS x Platform Features)
=========================================================

Goal:
  Identify when platform algorithm/engagement features intensified and test
  whether those inflection windows align with structural changes in YRBS
  mental-health outcomes.

This is descriptive and observational, with exact small-sample permutation
tests where feasible.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd

from feature_proxy_analysis import (
    YRBS_YEARS,
    compute_all_exposures,
    load_feature_matrix,
    load_yrbs_data,
)


SCRIPT_DIR = Path(__file__).resolve().parent
OUT_MERGED = SCRIPT_DIR / "feature_inflection_merged.csv"
OUT_DELTAS = SCRIPT_DIR / "feature_inflection_deltas.csv"
OUT_JSON = SCRIPT_DIR / "feature_inflection_event_study_results.json"

BASE_MENTAL_OUTCOMES = [
    ("sadness", "Persistent sadness/hopelessness (total)"),
    ("sadness_female", "Persistent sadness/hopelessness (female)"),
    ("sadness_male", "Persistent sadness/hopelessness (male)"),
    ("suicide_considered", "Considered suicide (total)"),
    ("suicide_plan", "Suicide plan (total)"),
    ("suicide_attempt", "Attempted suicide (total)"),
]


def pearson_corr(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) != len(y) or len(x) < 2:
        return float("nan")
    if np.allclose(x, x[0]) or np.allclose(y, y[0]):
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def exact_perm_pvalue_corr(x: np.ndarray, y: np.ndarray) -> Dict[str, float]:
    obs = pearson_corr(x, y)
    if not np.isfinite(obs):
        return {"r_observed": float("nan"), "p_two_sided_exact": float("nan"), "n_permutations": 0}

    n = len(y)
    ge = 0
    total = 0
    for perm in itertools.permutations(range(n)):
        yp = y[list(perm)]
        rp = pearson_corr(x, yp)
        if np.isfinite(rp) and abs(rp) >= abs(obs) - 1e-12:
            ge += 1
        total += 1
    return {
        "r_observed": float(obs),
        "p_two_sided_exact": float(ge / total),
        "n_permutations": int(total),
    }


def fit_linear(years: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, float]:
    x = np.column_stack([np.ones_like(years, dtype=float), years.astype(float)])
    beta, _, _, _ = np.linalg.lstsq(x, y.astype(float), rcond=None)
    yhat = x @ beta
    rss = float(np.sum((y - yhat) ** 2))
    return beta, rss


def fit_piecewise(years: np.ndarray, y: np.ndarray, break_year: int) -> Dict[str, float]:
    """
    Piecewise linear model:
      y = b0 + b1*year + b2*max(0, year-break_year)
    """
    hinge = np.maximum(0.0, years.astype(float) - float(break_year))
    x = np.column_stack([np.ones_like(years, dtype=float), years.astype(float), hinge])
    beta, _, _, _ = np.linalg.lstsq(x, y.astype(float), rcond=None)
    yhat = x @ beta
    rss = float(np.sum((y - yhat) ** 2))

    slope_pre = float(beta[1])
    slope_post = float(beta[1] + beta[2])
    slope_change = float(beta[2])
    return {
        "break_year": int(break_year),
        "rss": rss,
        "slope_pre": slope_pre,
        "slope_post": slope_post,
        "slope_change": slope_change,
    }


def best_break_with_perm(years: np.ndarray, y: np.ndarray) -> Dict[str, object]:
    """
    Choose best structural break among interior YRBS years by RSS reduction
    relative to a single linear trend, then compute exact permutation p-value.
    """
    _, rss_linear = fit_linear(years, y)
    candidates = [int(v) for v in years[1:-1]]
    fits = [fit_piecewise(years, y, b) for b in candidates]
    best = min(fits, key=lambda d: d["rss"])
    improve_obs = rss_linear - best["rss"]

    ge = 0
    total = 0
    for perm in itertools.permutations(range(len(y))):
        yp = y[list(perm)]
        _, rss_l = fit_linear(years, yp)
        perm_fits = [fit_piecewise(years, yp, b) for b in candidates]
        perm_best = min(perm_fits, key=lambda d: d["rss"])
        improve_perm = rss_l - perm_best["rss"]
        if improve_perm >= improve_obs - 1e-12:
            ge += 1
        total += 1

    return {
        "linear_rss": float(rss_linear),
        "best_break_year": int(best["break_year"]),
        "best_break_fit": best,
        "rss_improvement_vs_linear": float(improve_obs),
        "p_improvement_exact": float(ge / total),
        "n_permutations": int(total),
    }


def build_feature_metrics(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()

    d["algo_hard_exposure"] = (
        d["feat_algorithmic_feed"]
        + d["feat_opaque_recommendation"]
        + d["feat_hidden_ranking_signals"]
        + d["feat_autoplay_video"]
    )
    d["engagement_hard_exposure"] = (
        d["feat_autoplay_video"]
        + d["feat_infinite_scroll"]
        + d["feat_push_notifications_engagement"]
        + d["feat_streaks_or_daily_hooks"]
    )
    d["algo_plus_engagement_exposure"] = d["algo_hard_exposure"] + d["engagement_hard_exposure"]
    return d


def compute_deltas(df: pd.DataFrame, outcomes: List[Tuple[str, str]]) -> pd.DataFrame:
    d = df.sort_values("year").copy()
    d["interval_start"] = d["year"].shift(1)
    d["interval_end"] = d["year"]
    keep_cols = [
        "year",
        "interval_start",
        "interval_end",
        "algo_hard_exposure",
        "engagement_hard_exposure",
        "algo_plus_engagement_exposure",
    ] + [c for c, _ in outcomes]
    out = d[keep_cols].copy()

    for c in ["algo_hard_exposure", "engagement_hard_exposure", "algo_plus_engagement_exposure"] + [k for k, _ in outcomes]:
        out[f"delta_{c}"] = out[c].diff()

    out = out[out["interval_start"].notna()].copy()
    out["interval_label"] = out["interval_start"].astype(int).astype(str) + "-" + out["interval_end"].astype(int).astype(str)
    return out


def top_feature_inflections(delta_df: pd.DataFrame, col: str, top_n: int = 3) -> List[Dict[str, object]]:
    t = delta_df.sort_values(f"delta_{col}", ascending=False).head(top_n)
    rows = []
    for _, r in t.iterrows():
        rows.append(
            {
                "interval": r["interval_label"],
                "end_year": int(r["interval_end"]),
                "delta": float(r[f"delta_{col}"]),
            }
        )
    return rows


def lag1_corr_exact(x: np.ndarray, y: np.ndarray) -> Dict[str, float]:
    """
    Correlate x[t] with y[t+1] (one-interval lead of x).
    """
    if len(x) < 3 or len(y) < 3:
        return {"r_observed": float("nan"), "p_two_sided_exact": float("nan"), "n_permutations": 0}
    return exact_perm_pvalue_corr(x[:-1], y[1:])


def top_overlap_stats(delta_df: pd.DataFrame, feat_delta_col: str, outcome_delta_col: str, top_n: int = 2) -> Dict[str, object]:
    """
    Compare top-N feature-jump intervals to top-N outcome-jump intervals.
    Reports direct overlap and "same-or-next-interval" overlap.
    """
    feat_rank = delta_df[["interval_label", feat_delta_col]].sort_values(feat_delta_col, ascending=False).head(top_n).reset_index()
    out_rank = delta_df[["interval_label", outcome_delta_col]].sort_values(outcome_delta_col, ascending=False).head(top_n).reset_index()

    feat_idx = feat_rank["index"].tolist()
    out_idx = out_rank["index"].tolist()
    out_set = set(out_idx)

    direct_hits = [i for i in feat_idx if i in out_set]
    same_or_next_hits = [i for i in feat_idx if i in out_set or (i + 1) in out_set]

    return {
        "feature_top_intervals": feat_rank["interval_label"].tolist(),
        "outcome_top_intervals": out_rank["interval_label"].tolist(),
        "direct_overlap_count": int(len(direct_hits)),
        "same_or_next_interval_overlap_count": int(len(same_or_next_hits)),
        "top_n": int(top_n),
    }


def main() -> None:
    platform_data, _ = load_feature_matrix()
    yrbs = load_yrbs_data()

    exp_df = compute_all_exposures(platform_data, YRBS_YEARS)
    merged = pd.merge(yrbs, exp_df, on="year", how="inner").sort_values("year").reset_index(drop=True)

    # Harmonize optional columns that may not be standardized by loader.
    if "sadness_male" not in merged.columns and "Persistent_Sadness_Male" in merged.columns:
        merged["sadness_male"] = merged["Persistent_Sadness_Male"]

    outcomes = [(k, lbl) for k, lbl in BASE_MENTAL_OUTCOMES if k in merged.columns]
    merged = build_feature_metrics(merged)
    merged.to_csv(OUT_MERGED, index=False)

    deltas = compute_deltas(merged, outcomes)
    deltas.to_csv(OUT_DELTAS, index=False)

    # Correlation tests on first differences (feature jumps vs mental-health jumps)
    x_algo = deltas["delta_algo_hard_exposure"].to_numpy(dtype=float)
    x_eng = deltas["delta_engagement_hard_exposure"].to_numpy(dtype=float)
    x_combo = deltas["delta_algo_plus_engagement_exposure"].to_numpy(dtype=float)

    delta_corr = {}
    delta_corr_lag1 = {}
    for out_col, out_label in outcomes:
        y = deltas[f"delta_{out_col}"].to_numpy(dtype=float)
        delta_corr[out_col] = {
            "label": out_label,
            "algo_hard_delta_corr": exact_perm_pvalue_corr(x_algo, y),
            "engagement_hard_delta_corr": exact_perm_pvalue_corr(x_eng, y),
            "algo_plus_engagement_delta_corr": exact_perm_pvalue_corr(x_combo, y),
        }
        delta_corr_lag1[out_col] = {
            "label": out_label,
            "algo_hard_lead1_corr": lag1_corr_exact(x_algo, y),
            "engagement_hard_lead1_corr": lag1_corr_exact(x_eng, y),
            "algo_plus_engagement_lead1_corr": lag1_corr_exact(x_combo, y),
        }

    # Structural break tests for key outcomes.
    years = merged["year"].to_numpy(dtype=int)
    break_tests = {}
    for out_col, out_label in outcomes:
        y = merged[out_col].to_numpy(dtype=float)
        break_tests[out_col] = {
            "label": out_label,
            "result": best_break_with_perm(years, y),
        }

    inflections = {
        "top_algo_hard_intervals": top_feature_inflections(deltas, "algo_hard_exposure", top_n=4),
        "top_engagement_hard_intervals": top_feature_inflections(deltas, "engagement_hard_exposure", top_n=4),
        "top_combo_intervals": top_feature_inflections(deltas, "algo_plus_engagement_exposure", top_n=4),
    }

    overlap_stats = {}
    if "delta_sadness" in deltas.columns:
        overlap_stats["sadness_total_vs_algo_plus_engagement"] = top_overlap_stats(
            deltas,
            "delta_algo_plus_engagement_exposure",
            "delta_sadness",
            top_n=2,
        )
    if "delta_sadness_female" in deltas.columns:
        overlap_stats["sadness_female_vs_algo_plus_engagement"] = top_overlap_stats(
            deltas,
            "delta_algo_plus_engagement_exposure",
            "delta_sadness_female",
            top_n=2,
        )

    results = {
        "meta": {
            "script": "feature_inflection_event_study.py",
            "years": merged["year"].astype(int).tolist(),
            "n_years": int(len(merged)),
            "n_intervals": int(len(deltas)),
            "note": "Observational event-alignment and structural-break tests using exact small-sample permutation inference.",
        },
        "inflection_intervals": inflections,
        "delta_correlations_exact": delta_corr,
        "lag1_delta_correlations_exact": delta_corr_lag1,
        "top_interval_overlap_stats": overlap_stats,
        "structural_break_tests_exact": break_tests,
    }

    OUT_JSON.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print("Feature inflection event study complete")
    print(f"Merged yearly panel: {OUT_MERGED}")
    print(f"Interval deltas: {OUT_DELTAS}")
    print(f"Results: {OUT_JSON}")

    print("\nTop algorithm-hard intervals:")
    for row in inflections["top_algo_hard_intervals"]:
        print(f"  {row['interval']}: delta={row['delta']:.3f}")

    sad = delta_corr.get("sadness", {}).get("algo_plus_engagement_delta_corr")
    sad_f = delta_corr.get("sadness_female", {}).get("algo_plus_engagement_delta_corr")
    print("\nDelta correlation (algo+engagement vs sadness):")
    if sad:
        print(f"  Total sadness: r={sad['r_observed']:.3f}, p={sad['p_two_sided_exact']:.4f}")
    if sad_f:
        print(f"  Female sadness: r={sad_f['r_observed']:.3f}, p={sad_f['p_two_sided_exact']:.4f}")

    if "sadness_total_vs_algo_plus_engagement" in overlap_stats:
        o = overlap_stats["sadness_total_vs_algo_plus_engagement"]
        print("\nTop-2 interval overlap (algo+engagement vs sadness total):")
        print(
            f"  direct={o['direct_overlap_count']}/{o['top_n']}, "
            f"same-or-next={o['same_or_next_interval_overlap_count']}/{o['top_n']}"
        )

    b = break_tests.get("sadness", {}).get("result")
    bf = break_tests.get("sadness_female", {}).get("result")
    print("\nBest structural break year:")
    if b:
        print(f"  Sadness total: {b['best_break_year']} (p={b['p_improvement_exact']:.4f})")
    if bf:
        print(f"  Sadness female: {bf['best_break_year']} (p={bf['p_improvement_exact']:.4f})")


if __name__ == "__main__":
    main()
