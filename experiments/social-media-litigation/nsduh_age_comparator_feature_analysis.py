#!/usr/bin/env python3
"""
NSDUH Age-Comparator Feature Analysis (2005-2020)
=================================================

Purpose
-------
Add an age-differential stress test to the Papers 166/167 evidence stack:
compare youth (12-17 and 18-25) versus older adults (26+, 26-49, 50+) on
MDE trajectories, then align those trajectories with the same platform-feature
timeline used elsewhere in this repo.

Design constraints
------------------
- Observational timing and gradient analysis only (not causal identification).
- Uses SAMHSA NSDUH Detailed Tables 2020 v25 for 18+ age bands.
- Uses in-repo adolescent 12-17 series already source-traced in prior pipeline.
"""

from __future__ import annotations

import itertools
import json
import os
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd

from nsduh_annual_feature_shock_analysis import annualize_feature_exposure


SCRIPT_DIR = Path(__file__).resolve().parent
IN_PATH = SCRIPT_DIR / "nsduh_age_comparator_2005_2020.csv"
OUT_MERGED = SCRIPT_DIR / "nsduh_age_comparator_merged.csv"
OUT_JSON = SCRIPT_DIR / "nsduh_age_comparator_results.json"

RNG_SEED = 20260401
CORR_MC_PERMS = int(os.getenv("CORR_MC_PERMS", "20000"))
TREND_MC_PERMS = int(os.getenv("TREND_MC_PERMS", "200000"))

LEVEL_START = 2011
LEVEL_END = 2020

MDE_COLS = [
    "mde_12_17_pct",
    "mde_18_25_pct",
    "mde_26_plus_pct",
    "mde_26_49_pct",
    "mde_50_plus_pct",
    "mde_total_18_plus_pct",
]

MDE_SEVERE_COLS = [
    "mde_severe_12_17_pct",
    "mde_severe_18_25_pct",
    "mde_severe_26_plus_pct",
    "mde_severe_26_49_pct",
    "mde_severe_50_plus_pct",
    "mde_severe_total_18_plus_pct",
]

PREDICTORS = ["algo_plus_engagement_exposure", "raw_adoption"]


def pearson_corr(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) != len(y) or len(x) < 3:
        return float("nan")
    if np.allclose(x, x[0]) or np.allclose(y, y[0]):
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def corr_perm_mc(x: np.ndarray, y: np.ndarray, mc_perms: int, seed: int) -> Dict[str, float]:
    obs = pearson_corr(x, y)
    if not np.isfinite(obs):
        return {"r_observed": float("nan"), "p_two_sided_mc": float("nan"), "n_permutations": 0}

    rng = np.random.default_rng(seed)
    ge = 1
    total = 1
    for _ in range(mc_perms):
        yp = rng.permutation(y)
        rp = pearson_corr(x, yp)
        if np.isfinite(rp) and abs(rp) >= abs(obs) - 1e-12:
            ge += 1
        total += 1

    return {
        "r_observed": float(obs),
        "p_two_sided_mc": float(ge / total),
        "n_permutations": int(mc_perms),
    }


def delta_over_window(df: pd.DataFrame, col: str, start: int, end: int) -> Dict[str, float]:
    d = df[(df["year"] >= start) & (df["year"] <= end)].dropna(subset=[col]).copy()
    if d.empty:
        return {"start_year": int(start), "end_year": int(end), "n": 0, "delta_pct_points": float("nan")}
    return {
        "start_year": int(d["year"].iloc[0]),
        "end_year": int(d["year"].iloc[-1]),
        "n": int(len(d)),
        "delta_pct_points": float(d[col].iloc[-1] - d[col].iloc[0]),
    }


def trend_corr_mc(df: pd.DataFrame, col: str, start: int, end: int, mc_perms: int, seed: int) -> Dict[str, float]:
    d = df[(df["year"] >= start) & (df["year"] <= end)].dropna(subset=[col]).copy()
    if len(d) < 3:
        return {
            "start_year": int(start),
            "end_year": int(end),
            "n": int(len(d)),
            "r_year_corr": float("nan"),
            "p_two_sided_mc": float("nan"),
            "n_permutations": 0,
        }
    x = d["year"].to_numpy(dtype=float)
    y = d[col].to_numpy(dtype=float)
    stat = corr_perm_mc(x, y, mc_perms=mc_perms, seed=seed)
    stat.update({"start_year": int(start), "end_year": int(end), "n": int(len(d))})
    return stat


def build_level_correlations(
    df: pd.DataFrame,
    outcomes: List[str],
    predictors: List[str],
    start: int,
    end: int,
) -> Dict[str, object]:
    panel = df[(df["year"] >= start) & (df["year"] <= end)].copy()
    out: Dict[str, object] = {}
    for oi, outcome in enumerate(outcomes):
        out[outcome] = {}
        for pi, predictor in enumerate(predictors):
            d = panel.dropna(subset=[predictor, outcome]).copy()
            mc_seed = RNG_SEED + oi * 101 + pi * 17
            out[outcome][predictor] = corr_perm_mc(
                d[predictor].to_numpy(dtype=float),
                d[outcome].to_numpy(dtype=float),
                mc_perms=CORR_MC_PERMS,
                seed=mc_seed,
            )
            out[outcome][predictor]["n"] = int(len(d))
    return out


def label_swap_corr_diff_exact(x: np.ndarray, y_a: np.ndarray, y_b: np.ndarray) -> Dict[str, float]:
    """
    Exact paired-label swap test.
    Null: within each year, age-band labels are exchangeable.
    Statistic: |corr(x, y_a)| - |corr(x, y_b)| (one-sided: age-band A stronger).
    """
    if len(x) != len(y_a) or len(x) != len(y_b) or len(x) < 3:
        return {
            "n": int(len(x)),
            "r_a": float("nan"),
            "r_b": float("nan"),
            "abs_corr_diff": float("nan"),
            "p_one_sided_exact": float("nan"),
            "n_assignments": 0,
        }

    r_a = abs(pearson_corr(x, y_a))
    r_b = abs(pearson_corr(x, y_b))
    obs = r_a - r_b

    n = len(x)
    ge = 0
    total = 0
    for mask in range(1 << n):
        a = y_a.copy()
        b = y_b.copy()
        for i in range(n):
            if (mask >> i) & 1:
                a[i], b[i] = b[i], a[i]
        stat = abs(pearson_corr(x, a)) - abs(pearson_corr(x, b))
        if stat >= obs - 1e-12:
            ge += 1
        total += 1

    return {
        "n": int(n),
        "r_a": float(r_a),
        "r_b": float(r_b),
        "abs_corr_diff": float(obs),
        "p_one_sided_exact": float(ge / total),
        "n_assignments": int(total),
    }


def safe_ratio(num: float, den: float) -> float:
    if den == 0 or not np.isfinite(num) or not np.isfinite(den):
        return float("nan")
    return float(num / den)


def main() -> None:
    raw = pd.read_csv(IN_PATH).sort_values("year").reset_index(drop=True)
    features = annualize_feature_exposure()[
        ["year", "feature_exposure", "raw_adoption", "algo_hard_exposure", "engagement_hard_exposure", "algo_plus_engagement_exposure"]
    ].copy()

    merged = pd.merge(raw, features, on="year", how="left").sort_values("year").reset_index(drop=True)

    merged["mde_gap_12_17_minus_26_plus"] = merged["mde_12_17_pct"] - merged["mde_26_plus_pct"]
    merged["mde_gap_18_25_minus_26_plus"] = merged["mde_18_25_pct"] - merged["mde_26_plus_pct"]
    merged["mde_severe_gap_12_17_minus_26_plus"] = merged["mde_severe_12_17_pct"] - merged["mde_severe_26_plus_pct"]
    merged["mde_severe_gap_18_25_minus_26_plus"] = merged["mde_severe_18_25_pct"] - merged["mde_severe_26_plus_pct"]

    merged.to_csv(OUT_MERGED, index=False)

    level_outcomes = MDE_COLS + [
        "mde_gap_12_17_minus_26_plus",
        "mde_gap_18_25_minus_26_plus",
    ]
    severe_level_outcomes = MDE_SEVERE_COLS + [
        "mde_severe_gap_12_17_minus_26_plus",
        "mde_severe_gap_18_25_minus_26_plus",
    ]
    all_level_outcomes = level_outcomes + severe_level_outcomes

    deltas_2011_2020 = {
        col: delta_over_window(merged, col, LEVEL_START, LEVEL_END)
        for col in (MDE_COLS + MDE_SEVERE_COLS + ["mde_gap_12_17_minus_26_plus", "mde_severe_gap_12_17_minus_26_plus"])
    }

    d_mde_teen = deltas_2011_2020["mde_12_17_pct"]["delta_pct_points"]
    d_mde_18_25 = deltas_2011_2020["mde_18_25_pct"]["delta_pct_points"]
    d_mde_26_plus = deltas_2011_2020["mde_26_plus_pct"]["delta_pct_points"]
    d_mde_26_49 = deltas_2011_2020["mde_26_49_pct"]["delta_pct_points"]
    d_mde_50_plus = deltas_2011_2020["mde_50_plus_pct"]["delta_pct_points"]

    d_sev_teen = deltas_2011_2020["mde_severe_12_17_pct"]["delta_pct_points"]
    d_sev_18_25 = deltas_2011_2020["mde_severe_18_25_pct"]["delta_pct_points"]
    d_sev_26_plus = deltas_2011_2020["mde_severe_26_plus_pct"]["delta_pct_points"]
    d_sev_26_49 = deltas_2011_2020["mde_severe_26_49_pct"]["delta_pct_points"]
    d_sev_50_plus = deltas_2011_2020["mde_severe_50_plus_pct"]["delta_pct_points"]

    window = merged[(merged["year"] >= LEVEL_START) & (merged["year"] <= LEVEL_END)].copy()
    gap_trends = {
        "mde_gap_12_17_minus_26_plus": trend_corr_mc(
            merged, "mde_gap_12_17_minus_26_plus", LEVEL_START, LEVEL_END, TREND_MC_PERMS, RNG_SEED
        ),
        "mde_severe_gap_12_17_minus_26_plus": trend_corr_mc(
            merged, "mde_severe_gap_12_17_minus_26_plus", LEVEL_START, LEVEL_END, TREND_MC_PERMS, RNG_SEED + 1
        ),
    }

    # Correlation-strength contrast (youth vs older-adult) under paired label swaps.
    d_mde_contrast = window.dropna(
        subset=["algo_plus_engagement_exposure", "raw_adoption", "mde_12_17_pct", "mde_26_plus_pct"]
    ).copy()
    d_severe_contrast = window.dropna(
        subset=["algo_plus_engagement_exposure", "raw_adoption", "mde_severe_12_17_pct", "mde_severe_26_plus_pct"]
    ).copy()

    contrast_tests = {
        "mde_12_17_vs_26_plus_algo_plus_engagement": label_swap_corr_diff_exact(
            d_mde_contrast["algo_plus_engagement_exposure"].to_numpy(dtype=float),
            d_mde_contrast["mde_12_17_pct"].to_numpy(dtype=float),
            d_mde_contrast["mde_26_plus_pct"].to_numpy(dtype=float),
        ),
        "mde_12_17_vs_26_plus_raw_adoption": label_swap_corr_diff_exact(
            d_mde_contrast["raw_adoption"].to_numpy(dtype=float),
            d_mde_contrast["mde_12_17_pct"].to_numpy(dtype=float),
            d_mde_contrast["mde_26_plus_pct"].to_numpy(dtype=float),
        ),
        "mde_severe_12_17_vs_26_plus_algo_plus_engagement": label_swap_corr_diff_exact(
            d_severe_contrast["algo_plus_engagement_exposure"].to_numpy(dtype=float),
            d_severe_contrast["mde_severe_12_17_pct"].to_numpy(dtype=float),
            d_severe_contrast["mde_severe_26_plus_pct"].to_numpy(dtype=float),
        ),
        "mde_severe_12_17_vs_26_plus_raw_adoption": label_swap_corr_diff_exact(
            d_severe_contrast["raw_adoption"].to_numpy(dtype=float),
            d_severe_contrast["mde_severe_12_17_pct"].to_numpy(dtype=float),
            d_severe_contrast["mde_severe_26_plus_pct"].to_numpy(dtype=float),
        ),
    }

    out = {
        "meta": {
            "script": "nsduh_age_comparator_feature_analysis.py",
            "input": IN_PATH.name,
            "window_focus": f"{LEVEL_START}-{LEVEL_END}",
            "methodology_notes": [
                "Observational level/timing analysis; not causal identification.",
                "2020 values are from SAMHSA mixed-mode year and carry comparability cautions.",
                "Permutation tests are exact for label-swap contrasts and Monte Carlo for correlations.",
            ],
            "sources": {
                "mde_age_bands": "NSDUH Detailed Tables 2020 v25, Table 10.26B (lines 1492-1497).",
                "mde_severe_age_bands": "NSDUH Detailed Tables 2020 v25, Table 10.27B (lines 1546-1551).",
                "source_url": "https://www.samhsa.gov/data/sites/default/files/reports/rpt35323/NSDUHDetailedTabs2020v25/NSDUHDetailedTabs2020v25/NSDUHDetTabsSect10pe2020.htm",
                "teen_12_17_series": "In-repo NSDUH adolescent pipeline (`nsduh_adolescent_mde_2004_2024.csv`).",
            },
        },
        "deltas_2011_2020_pct_points": deltas_2011_2020,
        "delta_ratios_2011_2020": {
            "mde_12_17_vs_26_plus_ratio": safe_ratio(d_mde_teen, d_mde_26_plus),
            "mde_18_25_vs_26_plus_ratio": safe_ratio(d_mde_18_25, d_mde_26_plus),
            "mde_12_17_vs_50_plus_ratio": safe_ratio(d_mde_teen, d_mde_50_plus),
            "mde_12_17_vs_26_49_ratio": safe_ratio(d_mde_teen, d_mde_26_49),
            "mde_severe_12_17_vs_26_plus_ratio": safe_ratio(d_sev_teen, d_sev_26_plus),
            "mde_severe_18_25_vs_26_plus_ratio": safe_ratio(d_sev_18_25, d_sev_26_plus),
            "mde_severe_12_17_vs_50_plus_ratio": safe_ratio(d_sev_teen, d_sev_50_plus),
            "mde_severe_12_17_vs_26_49_ratio": safe_ratio(d_sev_teen, d_sev_26_49),
        },
        "level_correlations_2011_2020": build_level_correlations(
            merged, all_level_outcomes, PREDICTORS, LEVEL_START, LEVEL_END
        ),
        "gap_trend_tests_2011_2020": gap_trends,
        "paired_label_swap_contrast_tests": contrast_tests,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("NSDUH age-comparator feature analysis complete")
    print(f"Merged panel: {OUT_MERGED}")
    print(f"Results:      {OUT_JSON}")
    print("")
    print("Key 2011-2020 deltas (pct points):")
    print(f"  MDE 12-17: {d_mde_teen:.2f} | 26+: {d_mde_26_plus:.2f}")
    print(f"  MDE severe 12-17: {d_sev_teen:.2f} | 26+: {d_sev_26_plus:.2f}")
    print(
        "  Ratios teen/adult26:"
        f" MDE={safe_ratio(d_mde_teen, d_mde_26_plus):.2f}x,"
        f" severe={safe_ratio(d_sev_teen, d_sev_26_plus):.2f}x"
    )


if __name__ == "__main__":
    main()
