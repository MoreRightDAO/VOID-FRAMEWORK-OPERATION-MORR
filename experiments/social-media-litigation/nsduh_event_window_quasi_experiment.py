#!/usr/bin/env python3
"""
NSDUH Quasi-Experimental Event-Window Stress Test (Age-Band Controls)
=====================================================================

Purpose
-------
Run a fixed-window event analysis on annual NSDUH age-band outcomes with:
  1) exact randomization inference over all k-of-n window assignments
  2) explicit placebo windows (pre-rollout block)
  3) explicit negative-control outcomes (older-adult age bands)

Design notes
------------
- Observational timing test, not causal identification.
- Rollout windows are fixed from product-history dates, not outcome maxima.
- Uses the merged age-band + feature panel produced in-repo.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Dict, List, Sequence

import numpy as np
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
IN_PATH = SCRIPT_DIR / "nsduh_age_comparator_merged.csv"
OUT_TABLE = SCRIPT_DIR / "nsduh_event_window_quasi_table.csv"
OUT_JSON = SCRIPT_DIR / "nsduh_event_window_quasi_results.json"


WINDOWS = {
    "rollout": {
        "intervals": ["2015-2016", "2016-2017", "2018-2019", "2019-2020"],
        "rationale": (
            "Fixed a priori from major social-platform feature rollouts: "
            "Instagram algorithmic/stories period and TikTok/short-video convergence period."
        ),
    },
    "placebo": {
        "intervals": ["2011-2012", "2012-2013", "2013-2014", "2014-2015"],
        "rationale": (
            "Pre-rollout contiguous block with the same window count, used as a calendar placebo."
        ),
    },
}


OUTCOMES = [
    {
        "key": "d_mde_12_17_pct",
        "label": "MDE delta, age 12-17",
        "family": "treated_primary",
    },
    {
        "key": "d_mde_severe_12_17_pct",
        "label": "Severe MDE delta, age 12-17",
        "family": "treated_primary",
    },
    {
        "key": "d_under25_mde_pct",
        "label": "MDE delta, under-25 mean (12-17 and 18-25)",
        "family": "treated_secondary",
    },
    {
        "key": "d_under25_mde_severe_pct",
        "label": "Severe MDE delta, under-25 mean (12-17 and 18-25)",
        "family": "treated_secondary",
    },
    {
        "key": "d_mde_18_25_pct",
        "label": "MDE delta, age 18-25",
        "family": "treated_secondary",
    },
    {
        "key": "d_mde_severe_18_25_pct",
        "label": "Severe MDE delta, age 18-25",
        "family": "treated_secondary",
    },
    {
        "key": "d_gap_12_17_minus_26_plus_mde",
        "label": "Gap delta: (12-17 minus 26+) MDE",
        "family": "contrast_primary",
    },
    {
        "key": "d_gap_12_17_minus_26_plus_mde_severe",
        "label": "Gap delta: (12-17 minus 26+) severe MDE",
        "family": "contrast_primary",
    },
    {
        "key": "d_gap_18_25_minus_26_plus_mde",
        "label": "Gap delta: (18-25 minus 26+) MDE",
        "family": "contrast_secondary",
    },
    {
        "key": "d_gap_18_25_minus_26_plus_mde_severe",
        "label": "Gap delta: (18-25 minus 26+) severe MDE",
        "family": "contrast_secondary",
    },
    {
        "key": "d_mde_26_plus_pct",
        "label": "MDE delta, age 26+ (negative control)",
        "family": "negative_control",
    },
    {
        "key": "d_mde_severe_26_plus_pct",
        "label": "Severe MDE delta, age 26+ (negative control)",
        "family": "negative_control",
    },
    {
        "key": "d_mde_50_plus_pct",
        "label": "MDE delta, age 50+ (negative control)",
        "family": "negative_control",
    },
    {
        "key": "d_mde_severe_50_plus_pct",
        "label": "Severe MDE delta, age 50+ (negative control)",
        "family": "negative_control",
    },
]


def build_interval_panel() -> pd.DataFrame:
    raw = pd.read_csv(IN_PATH).sort_values("year").reset_index(drop=True)

    rows = []
    for i in range(1, len(raw)):
        start_year = int(raw.loc[i - 1, "year"])
        end_year = int(raw.loc[i, "year"])
        if start_year < 2011 or end_year > 2020:
            continue

        row = {
            "interval_start": start_year,
            "interval_end": end_year,
            "interval_label": f"{start_year}-{end_year}",
        }
        for col in [
            "algo_plus_engagement_exposure",
            "mde_12_17_pct",
            "mde_18_25_pct",
            "mde_26_plus_pct",
            "mde_26_49_pct",
            "mde_50_plus_pct",
            "mde_severe_12_17_pct",
            "mde_severe_18_25_pct",
            "mde_severe_26_plus_pct",
            "mde_severe_26_49_pct",
            "mde_severe_50_plus_pct",
        ]:
            prev = raw.loc[i - 1, col]
            curr = raw.loc[i, col]
            row[f"d_{col}"] = float(curr - prev) if pd.notna(prev) and pd.notna(curr) else float("nan")
        rows.append(row)

    panel = pd.DataFrame(rows).sort_values("interval_end").reset_index(drop=True)

    panel["d_under25_mde_pct"] = (panel["d_mde_12_17_pct"] + panel["d_mde_18_25_pct"]) / 2.0
    panel["d_under25_mde_severe_pct"] = (
        panel["d_mde_severe_12_17_pct"] + panel["d_mde_severe_18_25_pct"]
    ) / 2.0

    panel["d_gap_12_17_minus_26_plus_mde"] = panel["d_mde_12_17_pct"] - panel["d_mde_26_plus_pct"]
    panel["d_gap_18_25_minus_26_plus_mde"] = panel["d_mde_18_25_pct"] - panel["d_mde_26_plus_pct"]
    panel["d_gap_12_17_minus_26_plus_mde_severe"] = (
        panel["d_mde_severe_12_17_pct"] - panel["d_mde_severe_26_plus_pct"]
    )
    panel["d_gap_18_25_minus_26_plus_mde_severe"] = (
        panel["d_mde_severe_18_25_pct"] - panel["d_mde_severe_26_plus_pct"]
    )

    return panel


def effect_stat(y: np.ndarray, chosen_idx: Sequence[int]) -> float:
    all_idx = set(range(len(y)))
    chosen = set(chosen_idx)
    other = sorted(all_idx - chosen)
    return float(np.mean(y[list(chosen_idx)]) - np.mean(y[other]))


def exact_randomization(y: np.ndarray, chosen_idx: Sequence[int]) -> Dict[str, float]:
    n = len(y)
    k = len(chosen_idx)
    obs = effect_stat(y, chosen_idx)

    ge = 0
    le = 0
    total = 0
    for comb in itertools.combinations(range(n), k):
        stat = effect_stat(y, comb)
        if stat >= obs - 1e-12:
            ge += 1
        if stat <= obs + 1e-12:
            le += 1
        total += 1

    p_one_sided = ge / total
    p_two_sided = min(1.0, 2.0 * min(p_one_sided, le / total))
    percentile = le / total
    return {
        "effect_mean_diff": float(obs),
        "p_one_sided_exact": float(p_one_sided),
        "p_two_sided_exact": float(p_two_sided),
        "effect_percentile": float(percentile),
        "n_assignments": int(total),
        "k_windows": int(k),
        "n_intervals": int(n),
    }


def require_window_indices(panel: pd.DataFrame, intervals: List[str]) -> List[int]:
    idx_map = {iv: int(i) for i, iv in enumerate(panel["interval_label"].tolist())}
    missing = [iv for iv in intervals if iv not in idx_map]
    if missing:
        raise ValueError(f"Missing configured windows in panel: {missing}")
    return [idx_map[iv] for iv in intervals]


def run_outcome_tests(panel: pd.DataFrame, rollout_idx: List[int], placebo_idx: List[int]) -> Dict[str, object]:
    out: Dict[str, object] = {}
    for spec in OUTCOMES:
        key = spec["key"]
        label = spec["label"]
        family = spec["family"]

        if key not in panel.columns:
            out[key] = {"label": label, "family": family, "error": "missing_outcome_column"}
            continue

        y = panel[key].to_numpy(dtype=float)
        if np.isnan(y).any():
            out[key] = {"label": label, "family": family, "error": "outcome_contains_nan"}
            continue

        rollout = exact_randomization(y, rollout_idx)
        placebo = exact_randomization(y, placebo_idx)
        out[key] = {
            "label": label,
            "family": family,
            "rollout_window_test": rollout,
            "placebo_window_test": placebo,
            "rollout_minus_placebo_effect": float(
                rollout["effect_mean_diff"] - placebo["effect_mean_diff"]
            ),
        }
    return out


def build_summary(results: Dict[str, object]) -> Dict[str, object]:
    def pick(key: str) -> Dict[str, float]:
        node = results.get(key, {})
        roll = node.get("rollout_window_test", {})
        plac = node.get("placebo_window_test", {})
        return {
            "rollout_effect": roll.get("effect_mean_diff"),
            "rollout_p_one_sided_exact": roll.get("p_one_sided_exact"),
            "placebo_effect": plac.get("effect_mean_diff"),
            "placebo_p_one_sided_exact": plac.get("p_one_sided_exact"),
            "rollout_minus_placebo_effect": node.get("rollout_minus_placebo_effect"),
        }

    return {
        "primary_12_17": {
            "mde": pick("d_mde_12_17_pct"),
            "mde_severe": pick("d_mde_severe_12_17_pct"),
            "gap_vs_26_plus_mde": pick("d_gap_12_17_minus_26_plus_mde"),
            "gap_vs_26_plus_mde_severe": pick("d_gap_12_17_minus_26_plus_mde_severe"),
        },
        "secondary_under25": {
            "under25_mde": pick("d_under25_mde_pct"),
            "under25_mde_severe": pick("d_under25_mde_severe_pct"),
            "age18_25_mde": pick("d_mde_18_25_pct"),
            "age18_25_mde_severe": pick("d_mde_severe_18_25_pct"),
        },
        "negative_controls": {
            "age26_plus_mde": pick("d_mde_26_plus_pct"),
            "age26_plus_mde_severe": pick("d_mde_severe_26_plus_pct"),
            "age50_plus_mde": pick("d_mde_50_plus_pct"),
            "age50_plus_mde_severe": pick("d_mde_severe_50_plus_pct"),
        },
    }


def main() -> None:
    panel = build_interval_panel()

    rollout_intervals = WINDOWS["rollout"]["intervals"]
    placebo_intervals = WINDOWS["placebo"]["intervals"]

    rollout_idx = require_window_indices(panel, rollout_intervals)
    placebo_idx = require_window_indices(panel, placebo_intervals)

    panel["is_rollout_window"] = panel["interval_label"].isin(rollout_intervals).astype(int)
    panel["is_placebo_window"] = panel["interval_label"].isin(placebo_intervals).astype(int)
    panel.to_csv(OUT_TABLE, index=False)

    outcome_results = run_outcome_tests(panel, rollout_idx, placebo_idx)
    summary = build_summary(outcome_results)

    out = {
        "meta": {
            "script": "nsduh_event_window_quasi_experiment.py",
            "input": IN_PATH.name,
            "panel_years": [2011, 2020],
            "n_intervals": int(len(panel)),
            "design": {
                "rollout_windows_fixed": WINDOWS["rollout"],
                "placebo_windows_fixed": WINDOWS["placebo"],
                "inference": "exact randomization over all k-of-n window allocations",
                "negative_controls": "adult age bands (26+, 50+)",
                "note": "Observational timing stress test; not standalone causal identification.",
            },
        },
        "interval_panel": {
            "intervals": panel["interval_label"].tolist(),
            "rollout_windows": rollout_intervals,
            "placebo_windows": placebo_intervals,
        },
        "outcome_tests": outcome_results,
        "summary": summary,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("NSDUH event-window quasi-experiment complete")
    print(f"Saved panel:   {OUT_TABLE}")
    print(f"Saved results: {OUT_JSON}")

    prim = summary["primary_12_17"]
    sec = summary["secondary_under25"]
    ctrl = summary["negative_controls"]
    print("\nPrimary (12-17):")
    print(
        "  MDE rollout effect="
        f"{prim['mde']['rollout_effect']:.3f}, p={prim['mde']['rollout_p_one_sided_exact']:.4f}; "
        f"placebo={prim['mde']['placebo_effect']:.3f}, p={prim['mde']['placebo_p_one_sided_exact']:.4f}"
    )
    print(
        "  Severe rollout effect="
        f"{prim['mde_severe']['rollout_effect']:.3f}, p={prim['mde_severe']['rollout_p_one_sided_exact']:.4f}; "
        f"placebo={prim['mde_severe']['placebo_effect']:.3f}, p={prim['mde_severe']['placebo_p_one_sided_exact']:.4f}"
    )
    print("\nSecondary (under-25 / 18-25):")
    print(
        "  Under-25 severe rollout effect="
        f"{sec['under25_mde_severe']['rollout_effect']:.3f}, "
        f"p={sec['under25_mde_severe']['rollout_p_one_sided_exact']:.4f}"
    )
    print(
        "  18-25 severe rollout effect="
        f"{sec['age18_25_mde_severe']['rollout_effect']:.3f}, "
        f"p={sec['age18_25_mde_severe']['rollout_p_one_sided_exact']:.4f}"
    )
    print("\nNegative controls:")
    print(
        "  26+ severe rollout effect="
        f"{ctrl['age26_plus_mde_severe']['rollout_effect']:.3f}, "
        f"p={ctrl['age26_plus_mde_severe']['rollout_p_one_sided_exact']:.4f}"
    )
    print(
        "  50+ severe rollout effect="
        f"{ctrl['age50_plus_mde_severe']['rollout_effect']:.3f}, "
        f"p={ctrl['age50_plus_mde_severe']['rollout_p_one_sided_exact']:.4f}"
    )


if __name__ == "__main__":
    main()
