#!/usr/bin/env python3
"""
NSDUH Quasi-Experimental Event-Window Stress Test (v2)
======================================================

Purpose
-------
Extend the fixed-window NSDUH age-band timing stress test to include
pre-registered external event families:
  1) platform-policy shock windows
  2) regulatory/payout shock windows

Design notes
------------
- Observational timing test, not causal identification.
- Event windows are fixed before testing and mapped to annual intervals.
- Exact randomization inference over all k-of-n window assignments.
- Includes explicit placebo windows and adult negative-control outcomes.
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
OUT_TABLE = SCRIPT_DIR / "nsduh_event_window_quasi_v2_table.csv"
OUT_JSON = SCRIPT_DIR / "nsduh_event_window_quasi_v2_results.json"


EVENT_FAMILIES = {
    "platform_policy_shocks": {
        "intervals": ["2015-2016", "2016-2017", "2018-2019", "2019-2020"],
        "placebo_intervals": ["2011-2012", "2012-2013", "2013-2014", "2014-2015"],
        "rationale": (
            "Pre-locked windows spanning major platform product-policy shifts "
            "(algorithmic feed/stories transition, TikTok scale-up, and short-video convergence)."
        ),
        "event_ledger": [
            {
                "date": "2016-03-15",
                "event": "Instagram algorithmic-feed rollout announcement",
                "source": "Instagram blog",
                "url": "https://about.instagram.com/blog/announcements/see-the-moments-you-care-about-first",
                "mapped_interval": "2015-2016",
            },
            {
                "date": "2016-08-02",
                "event": "Instagram Stories launch",
                "source": "Instagram blog",
                "url": "https://about.instagram.com/blog/announcements/introducing-instagram-stories",
                "mapped_interval": "2016-2017",
            },
            {
                "date": "2018-08-02",
                "event": "TikTok / Musical.ly merger completion",
                "source": "TikTok newsroom",
                "url": "https://newsroom.tiktok.com/en-us/tiktok-welcomes-musical-ly-to-our-community",
                "mapped_interval": "2018-2019",
            },
            {
                "date": "2020-08-05",
                "event": "Instagram Reels launch",
                "source": "Instagram blog",
                "url": "https://about.instagram.com/blog/announcements/introducing-instagram-reels-announcement",
                "mapped_interval": "2019-2020",
            },
        ],
    },
    "regulatory_payout_shocks": {
        "intervals": ["2018-2019", "2019-2020"],
        "placebo_intervals": ["2012-2013", "2013-2014"],
        "rationale": (
            "Pre-locked windows covering major regulatory and platform-economic shocks "
            "(GDPR enforcement, FTC settlements, creator-fund payout model)."
        ),
        "event_ledger": [
            {
                "date": "2018-05-25",
                "event": "GDPR enters application across EU",
                "source": "EUR-Lex",
                "url": "https://eur-lex.europa.eu/eli/reg/2016/679/oj",
                "mapped_interval": "2018-2019",
            },
            {
                "date": "2019-07-24",
                "event": "FTC announces $5B Facebook settlement",
                "source": "FTC press release",
                "url": "https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-imposes-5-billion-penalty-sweeping-new-privacy-restrictions-facebook",
                "mapped_interval": "2019-2020",
            },
            {
                "date": "2019-09-04",
                "event": "FTC/DOJ announce $170M YouTube COPPA settlement",
                "source": "FTC press release",
                "url": "https://www.ftc.gov/news-events/news/press-releases/2019/09/google-youtube-will-pay-record-170-million-alleged-violations-childrens-privacy-law",
                "mapped_interval": "2019-2020",
            },
            {
                "date": "2020-07-22",
                "event": "TikTok launches $200M Creator Fund",
                "source": "TikTok newsroom",
                "url": "https://newsroom.tiktok.com/en-us/introducing-the-200-million-tiktok-creator-fund",
                "mapped_interval": "2019-2020",
            },
        ],
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
            "mde_50_plus_pct",
            "mde_severe_12_17_pct",
            "mde_severe_18_25_pct",
            "mde_severe_26_plus_pct",
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


def run_family(panel: pd.DataFrame, family_name: str, family_cfg: Dict[str, object]) -> Dict[str, object]:
    intervals = family_cfg["intervals"]
    placebo_intervals = family_cfg["placebo_intervals"]

    shock_idx = require_window_indices(panel, intervals)
    placebo_idx = require_window_indices(panel, placebo_intervals)

    tests: Dict[str, object] = {}
    for spec in OUTCOMES:
        key = spec["key"]
        label = spec["label"]
        outcome_family = spec["family"]

        if key not in panel.columns:
            tests[key] = {
                "label": label,
                "family": outcome_family,
                "error": "missing_outcome_column",
            }
            continue

        y = panel[key].to_numpy(dtype=float)
        if np.isnan(y).any():
            tests[key] = {
                "label": label,
                "family": outcome_family,
                "error": "outcome_contains_nan",
            }
            continue

        shock = exact_randomization(y, shock_idx)
        placebo = exact_randomization(y, placebo_idx)

        tests[key] = {
            "label": label,
            "family": outcome_family,
            "shock_window_test": shock,
            "placebo_window_test": placebo,
            "shock_minus_placebo_effect": float(shock["effect_mean_diff"] - placebo["effect_mean_diff"]),
        }

    def pick(key: str) -> Dict[str, float]:
        node = tests.get(key, {})
        s = node.get("shock_window_test", {})
        p = node.get("placebo_window_test", {})
        return {
            "shock_effect": s.get("effect_mean_diff"),
            "shock_p_one_sided_exact": s.get("p_one_sided_exact"),
            "placebo_effect": p.get("effect_mean_diff"),
            "placebo_p_one_sided_exact": p.get("p_one_sided_exact"),
            "shock_minus_placebo_effect": node.get("shock_minus_placebo_effect"),
        }

    summary = {
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
            "gap_18_25_vs_26_plus_mde": pick("d_gap_18_25_minus_26_plus_mde"),
            "gap_18_25_vs_26_plus_mde_severe": pick("d_gap_18_25_minus_26_plus_mde_severe"),
        },
        "negative_controls": {
            "age26_plus_mde": pick("d_mde_26_plus_pct"),
            "age26_plus_mde_severe": pick("d_mde_severe_26_plus_pct"),
            "age50_plus_mde": pick("d_mde_50_plus_pct"),
            "age50_plus_mde_severe": pick("d_mde_severe_50_plus_pct"),
        },
    }

    return {
        "family_name": family_name,
        "definition": family_cfg,
        "outcome_tests": tests,
        "summary": summary,
    }


def main() -> None:
    panel = build_interval_panel()

    for family_name, family_cfg in EVENT_FAMILIES.items():
        panel[f"is_{family_name}"] = panel["interval_label"].isin(family_cfg["intervals"]).astype(int)
        panel[f"is_placebo_{family_name}"] = panel["interval_label"].isin(
            family_cfg["placebo_intervals"]
        ).astype(int)

    panel.to_csv(OUT_TABLE, index=False)

    family_results: Dict[str, object] = {}
    for family_name, family_cfg in EVENT_FAMILIES.items():
        family_results[family_name] = run_family(panel, family_name, family_cfg)

    out = {
        "meta": {
            "script": "nsduh_event_window_quasi_experiment_v2.py",
            "input": IN_PATH.name,
            "panel_years": [2011, 2020],
            "n_intervals": int(len(panel)),
            "design": {
                "event_families_fixed": EVENT_FAMILIES,
                "inference": "exact randomization over all k-of-n window allocations",
                "negative_controls": "adult age bands (26+, 50+)",
                "note": "Observational timing stress test; not standalone causal identification.",
            },
        },
        "interval_panel": {
            "intervals": panel["interval_label"].tolist(),
        },
        "family_results": family_results,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("NSDUH event-window quasi-experiment v2 complete")
    print(f"Saved panel:   {OUT_TABLE}")
    print(f"Saved results: {OUT_JSON}")

    for family_name in EVENT_FAMILIES:
        fam = family_results[family_name]["summary"]
        prim = fam["primary_12_17"]
        sec = fam["secondary_under25"]
        ctrl = fam["negative_controls"]

        print(f"\n{family_name}:")
        print(
            "  12-17 severe: shock="
            f"{prim['mde_severe']['shock_effect']:.3f}, "
            f"p={prim['mde_severe']['shock_p_one_sided_exact']:.4f}; "
            f"placebo={prim['mde_severe']['placebo_effect']:.3f}, "
            f"p={prim['mde_severe']['placebo_p_one_sided_exact']:.4f}"
        )
        print(
            "  under-25 severe: shock="
            f"{sec['under25_mde_severe']['shock_effect']:.3f}, "
            f"p={sec['under25_mde_severe']['shock_p_one_sided_exact']:.4f}"
        )
        print(
            "  18-25 severe gap vs 26+: shock="
            f"{sec['gap_18_25_vs_26_plus_mde_severe']['shock_effect']:.3f}, "
            f"p={sec['gap_18_25_vs_26_plus_mde_severe']['shock_p_one_sided_exact']:.4f}"
        )
        print(
            "  26+ severe control: shock="
            f"{ctrl['age26_plus_mde_severe']['shock_effect']:.3f}, "
            f"p={ctrl['age26_plus_mde_severe']['shock_p_one_sided_exact']:.4f}"
        )


if __name__ == "__main__":
    main()
