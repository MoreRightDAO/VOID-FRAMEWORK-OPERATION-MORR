#!/usr/bin/env python3
"""
Hostile-Witness Time-Link Analysis
=================================

Pipeline:
  1) Read coded exhibit table (admission/allegation/procedural).
  2) Score yearly hostile-witness signal.
  3) Compute adoption-weighted platform feature intensity from platform timeline.
  4) Run small-sample exact permutation correlation tests.

Outputs:
  - hostile_witness_exhibit_table.csv
  - hostile_witness_yearly_join.csv
  - hostile_witness_time_link_results.json
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
EXHIBIT_PATH = SCRIPT_DIR / "hostile_witness_exhibit_table.json"
TIMELINE_PATH = SCRIPT_DIR / "platform-pe-timeline.json"

EXHIBIT_CSV_PATH = SCRIPT_DIR / "hostile_witness_exhibit_table.csv"
YEARLY_CSV_PATH = SCRIPT_DIR / "hostile_witness_yearly_join.csv"
RESULTS_JSON_PATH = SCRIPT_DIR / "hostile_witness_time_link_results.json"

ROLE_WEIGHT = {"admission": 3.0, "allegation": 2.0, "procedural": 1.0}
STRENGTH_WEIGHT = {"low": 1.0, "medium": 1.5, "high": 2.0}


def pearson_corr(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) != len(y) or len(x) < 2:
        return float("nan")
    if np.allclose(x, x[0]) or np.allclose(y, y[0]):
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def spearman_corr(x: np.ndarray, y: np.ndarray) -> float:
    rx = pd.Series(x).rank(method="average").to_numpy(dtype=float)
    ry = pd.Series(y).rank(method="average").to_numpy(dtype=float)
    return pearson_corr(rx, ry)


def exact_permutation_pvalue(x: np.ndarray, y: np.ndarray, corr_fn) -> Dict[str, float]:
    """
    Exact two-sided permutation p-value with x fixed and y permuted.
    """
    obs = corr_fn(x, y)
    if not np.isfinite(obs):
        return {
            "r_observed": float("nan"),
            "p_two_sided_exact": float("nan"),
            "n_permutations": 0,
        }

    n = len(y)
    idx = list(range(n))
    ge = 0
    total = 0

    for perm in itertools.permutations(idx):
        yp = y[list(perm)]
        rp = corr_fn(x, yp)
        if np.isfinite(rp) and abs(rp) >= abs(obs) - 1e-12:
            ge += 1
        total += 1

    return {
        "r_observed": float(obs),
        "p_two_sided_exact": float(ge / total) if total else float("nan"),
        "n_permutations": int(total),
    }


def load_exhibits() -> pd.DataFrame:
    data = json.loads(EXHIBIT_PATH.read_text(encoding="utf-8"))
    rows = data["rows"]
    df = pd.DataFrame(rows)

    # Score each exhibit with role/strength + feature breadth multiplier.
    df["role_weight"] = df["role"].map(ROLE_WEIGHT).astype(float)
    df["strength_weight"] = df["strength_tier"].map(STRENGTH_WEIGHT).astype(float)
    df["feature_count"] = df["feature_tags"].apply(lambda x: len(x) if isinstance(x, list) else 0)
    df["breadth_weight"] = 1.0 + np.minimum(df["feature_count"], 8) / 10.0
    df["signal_score"] = df["role_weight"] * df["strength_weight"] * df["breadth_weight"]

    return df


def load_platform_yearly() -> pd.DataFrame:
    data = json.loads(TIMELINE_PATH.read_text(encoding="utf-8"))
    platforms = data["platforms"]

    rows: List[Dict[str, float]] = []
    years = set()
    for pdata in platforms.values():
        years.update(int(y) for y in pdata.keys() if str(y).isdigit())

    for year in sorted(years):
        num_o = 0.0
        num_r = 0.0
        num_a = 0.0
        den = 0.0
        n_platforms = 0

        for pdata in platforms.values():
            yk = str(year)
            if yk not in pdata:
                continue
            rec = pdata[yk]
            w = float(rec.get("adoption_pct", 0.0) or 0.0)
            o = float(rec.get("O", np.nan))
            r = float(rec.get("R", np.nan))
            a = float(rec.get("alpha", np.nan))
            if not np.isfinite(w) or w <= 0:
                continue
            if not (np.isfinite(o) and np.isfinite(r) and np.isfinite(a)):
                continue
            num_o += w * o
            num_r += w * r
            num_a += w * a
            den += w
            n_platforms += 1

        if den <= 0:
            continue

        w_o = num_o / den
        w_r = num_r / den
        w_a = num_a / den
        rows.append(
            {
                "year": year,
                "platforms_used": n_platforms,
                "weighted_O": w_o,
                "weighted_R": w_r,
                "weighted_alpha": w_a,
                "weighted_ORA_sum": w_o + w_r + w_a,
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    ex = load_exhibits()
    ex = ex.sort_values(["date", "exhibit_id"]).reset_index(drop=True)
    ex.to_csv(EXHIBIT_CSV_PATH, index=False)

    # Yearly hostile signal.
    y = (
        ex.groupby("year", as_index=False)
        .agg(
            hostile_event_count=("exhibit_id", "count"),
            hostile_signal_score=("signal_score", "sum"),
            hostile_admission_count=("role", lambda s: int((s == "admission").sum())),
            hostile_allegation_count=("role", lambda s: int((s == "allegation").sum())),
            hostile_procedural_count=("role", lambda s: int((s == "procedural").sum())),
        )
        .sort_values("year")
    )

    p = load_platform_yearly()

    # Align to common year window and keep all years in that window
    # (hostile score = 0 if no coded row in that year).
    min_year = max(int(y["year"].min()), int(p["year"].min()))
    max_year = min(int(y["year"].max()), int(p["year"].max()))
    years = pd.DataFrame({"year": list(range(min_year, max_year + 1))})

    joined = years.merge(p, on="year", how="left").merge(y, on="year", how="left")
    fill_cols = [
        "hostile_event_count",
        "hostile_signal_score",
        "hostile_admission_count",
        "hostile_allegation_count",
        "hostile_procedural_count",
    ]
    joined[fill_cols] = joined[fill_cols].fillna(0.0)
    joined = joined.sort_values("year").reset_index(drop=True)
    joined.to_csv(YEARLY_CSV_PATH, index=False)

    x = joined["weighted_ORA_sum"].to_numpy(dtype=float)
    h = joined["hostile_signal_score"].to_numpy(dtype=float)

    level_pearson = exact_permutation_pvalue(x, h, pearson_corr)
    level_spearman = exact_permutation_pvalue(x, h, spearman_corr)

    # First differences: guardrail against pure shared trend.
    x_d = np.diff(x)
    h_d = np.diff(h)
    diff_pearson = exact_permutation_pvalue(x_d, h_d, pearson_corr)
    diff_spearman = exact_permutation_pvalue(x_d, h_d, spearman_corr)

    # Optional 1-year lag checks (hostile leading/lagging platform).
    # Positive lag: hostile at t predicts platform at t+lag.
    lag_results: Dict[str, Dict[str, float]] = {}
    for lag in [-1, 0, 1]:
        if lag == 0:
            xa, ha = x, h
        elif lag > 0:
            xa, ha = x[lag:], h[:-lag]
        else:
            k = abs(lag)
            xa, ha = x[:-k], h[k:]

        lag_results[str(lag)] = {
            "n": int(len(xa)),
            "pearson_r": pearson_corr(xa, ha),
            "spearman_rho": spearman_corr(xa, ha),
        }

    results = {
        "meta": {
            "script": "hostile_witness_time_link_correlation.py",
            "role_weight": ROLE_WEIGHT,
            "strength_weight": STRENGTH_WEIGHT,
            "exhibit_rows": int(len(ex)),
            "analysis_year_window": [int(min_year), int(max_year)],
            "analysis_years_n": int(len(joined)),
            "note": "Descriptive time-link analysis only; no causal identification.",
        },
        "level_correlation_exact": {
            "pearson": level_pearson,
            "spearman": level_spearman,
        },
        "first_difference_correlation_exact": {
            "pearson": diff_pearson,
            "spearman": diff_spearman,
        },
        "lag_checks_descriptive": lag_results,
        "yearly_join": joined.to_dict(orient="records"),
    }

    RESULTS_JSON_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(f"Exhibits: {len(ex)} -> {EXHIBIT_CSV_PATH}")
    print(f"Yearly join: {len(joined)} years ({min_year}-{max_year}) -> {YEARLY_CSV_PATH}")
    print(
        "Level exact correlation:",
        f"Pearson r={level_pearson['r_observed']:.4f}, p={level_pearson['p_two_sided_exact']:.4f};",
        f"Spearman rho={level_spearman['r_observed']:.4f}, p={level_spearman['p_two_sided_exact']:.4f}",
    )
    print(
        "First-difference exact correlation:",
        f"Pearson r={diff_pearson['r_observed']:.4f}, p={diff_pearson['p_two_sided_exact']:.4f};",
        f"Spearman rho={diff_spearman['r_observed']:.4f}, p={diff_spearman['p_two_sided_exact']:.4f}",
    )
    print(f"Saved: {RESULTS_JSON_PATH}")


if __name__ == "__main__":
    main()
