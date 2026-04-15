#!/usr/bin/env python3
"""
Feature Shock-Window Test (Pre-Registered One-Sided)
====================================================

Tests fixed shock windows against interval mental-health deltas:
  - Immediate ramp windows: 2015-2017 and 2019-2021
  - Lagged windows: 2017-2019 and 2021-2023

Directional alternative for all hypotheses:
  mean(delta in shock windows) > mean(delta in non-shock windows)

Inference is exact via enumeration of all k-of-n assignments.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
IN_PATH = SCRIPT_DIR / "feature_inflection_deltas.csv"
OUT_TABLE = SCRIPT_DIR / "feature_shock_window_test_table.csv"
OUT_JSON = SCRIPT_DIR / "feature_shock_window_test_results.json"


WINDOWS = {
    "immediate_ramps": {
        "intervals": ["2015-2017", "2019-2021"],
        "rationale": "First YRBS intervals spanning major algorithm/engagement ramp phases (IG 2016 shift; Reels/Shorts 2020-2021 ramp).",
    },
    "lagged_windows": {
        "intervals": ["2017-2019", "2021-2023"],
        "rationale": "One-interval-later windows for delayed population response.",
    },
}

FEATURE_COL = "delta_algo_plus_engagement_exposure"
OUTCOME_COLS = [
    "delta_sadness",
    "delta_sadness_female",
    "delta_sadness_male",
    "delta_suicide_considered",
    "delta_suicide_plan",
    "delta_suicide_attempt",
]


def exact_window_vs_rest_one_sided(y: np.ndarray, shock_idx: List[int]) -> Dict[str, float]:
    """
    Exact one-sided test over all allocations with same shock-window count.
    """
    n = len(y)
    k = len(shock_idx)
    all_idx = set(range(n))
    shock_set = set(shock_idx)
    control_idx = sorted(all_idx - shock_set)

    obs = float(np.mean(y[shock_idx]) - np.mean(y[control_idx]))

    ge = 0
    total = 0
    for comb in itertools.combinations(range(n), k):
        cset = set(comb)
        other = sorted(all_idx - cset)
        stat = float(np.mean(y[list(comb)]) - np.mean(y[other]))
        if stat >= obs - 1e-12:
            ge += 1
        total += 1

    return {
        "effect_mean_diff": obs,
        "p_one_sided_exact": float(ge / total),
        "n_assignments": int(total),
        "k_shock": int(k),
        "n_total": int(n),
    }


def top_rank_info(df: pd.DataFrame, col: str, intervals: List[str]) -> Dict[str, object]:
    """
    Descriptive ranking summary for given intervals.
    """
    t = df[["interval_label", col]].sort_values(col, ascending=False).reset_index(drop=True)
    ranks = {}
    for iv in intervals:
        idx = t.index[t["interval_label"] == iv]
        if len(idx) == 0:
            continue
        ranks[iv] = int(idx[0] + 1)
    return {
        "top_sorted": t.to_dict(orient="records"),
        "shock_interval_ranks": ranks,
    }


def build_index(df: pd.DataFrame) -> Dict[str, int]:
    return {r["interval_label"]: int(i) for i, r in df.reset_index(drop=True).iterrows()}


def main() -> None:
    if not IN_PATH.exists():
        raise FileNotFoundError(f"Missing input: {IN_PATH}. Run feature_inflection_event_study.py first.")

    df = pd.read_csv(IN_PATH).copy()
    df = df.sort_values("interval_end").reset_index(drop=True)
    idx_map = build_index(df)

    for wname, wcfg in WINDOWS.items():
        col = f"is_{wname}"
        df[col] = df["interval_label"].isin(wcfg["intervals"]).astype(int)

    df.to_csv(OUT_TABLE, index=False)

    hypotheses = {}

    # Include feature-delta sanity test + mental-health outcomes.
    test_cols = [FEATURE_COL] + [c for c in OUTCOME_COLS if c in df.columns]

    for wname, wcfg in WINDOWS.items():
        intervals = wcfg["intervals"]
        missing = [iv for iv in intervals if iv not in idx_map]
        if missing:
            hypotheses[wname] = {"error": f"Missing intervals in data: {missing}"}
            continue

        shock_idx = [idx_map[iv] for iv in intervals]
        block = {
            "definition": wcfg,
            "tests_one_sided": {},
            "rank_summaries": {},
        }

        for col in test_cols:
            y = df[col].to_numpy(dtype=float)
            block["tests_one_sided"][col] = exact_window_vs_rest_one_sided(y, shock_idx)
            block["rank_summaries"][col] = top_rank_info(df, col, intervals)

        hypotheses[wname] = block

    out = {
        "meta": {
            "script": "feature_shock_window_test.py",
            "input": IN_PATH.name,
            "rows": int(len(df)),
            "intervals": df["interval_label"].tolist(),
            "pre_registered_design": {
                "windows_fixed_before_test": WINDOWS,
                "alternative_hypothesis": "mean(delta in shock windows) > mean(delta in non-shock windows)",
                "inference": "exact combinatorial test over all k-of-n window allocations",
            },
            "note": "Observational stress test of timing alignment; not causal identification.",
        },
        "hypotheses": hypotheses,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("Feature shock-window test complete")
    print(f"Input intervals: {len(df)}")
    print(f"Saved table: {OUT_TABLE}")
    print(f"Saved results: {OUT_JSON}")

    for wname in ["immediate_ramps", "lagged_windows"]:
        if wname not in hypotheses or "tests_one_sided" not in hypotheses[wname]:
            continue
        h = hypotheses[wname]["tests_one_sided"]
        fs = h[FEATURE_COL]
        sad = h.get("delta_sadness")
        sadf = h.get("delta_sadness_female")
        print(f"\n{wname}:")
        print(f"  feature delta mean-diff={fs['effect_mean_diff']:.3f}, p={fs['p_one_sided_exact']:.4f}")
        if sad:
            print(f"  sadness delta mean-diff={sad['effect_mean_diff']:.3f}, p={sad['p_one_sided_exact']:.4f}")
        if sadf:
            print(f"  female sadness delta mean-diff={sadf['effect_mean_diff']:.3f}, p={sadf['p_one_sided_exact']:.4f}")


if __name__ == "__main__":
    main()
