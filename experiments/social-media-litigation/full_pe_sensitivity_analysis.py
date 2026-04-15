#!/usr/bin/env python3
"""
Full-Pe Sensitivity Analysis (Litigation v1.1)
==============================================

Purpose
-------
Run the full nonlinear Pe specification with canonical constants and a
conservative stress grid to test whether the design-signal advantage over
raw adoption is stable.

This script is intentionally narrow:
  1) Uses the same five core platforms as the original protocol
     (facebook/instagram/youtube/tiktok/snapchat)
  2) Uses YRBS years only (2011-2023, biennial)
  3) Reports R^2 and delta R^2 (Pe - raw adoption) for litigation-facing
     outcome variables
  4) Emits machine-readable JSON for paper integration
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy import stats


SCRIPT_DIR = Path(__file__).resolve().parent
TIMELINE_PATH = SCRIPT_DIR / "platform-pe-timeline.json"
YRBS_PATH = SCRIPT_DIR / "yrbs-trend-data.csv"
OUT_PATH = SCRIPT_DIR / "full_pe_sensitivity_results.json"

PLATFORMS = ["facebook", "instagram", "youtube", "tiktok", "snapchat"]
YRBS_YEARS = [2011, 2013, 2015, 2017, 2019, 2021, 2023]

# Canonical constants from math apparatus:
# B_G derived (§165), B_A empirical (§208 caveat), K deployment scale.
CANON_B_A = 0.867
CANON_B_G = math.pi / math.sqrt(2)
CANON_K = 16

# Stress grid: conservative parameter stress tests (not confidence intervals).
# The intent is robustness under plausible calibration drift, not formal
# uncertainty quantification.
SCENARIOS = [
    {"name": "canonical", "B_A": CANON_B_A, "B_G": CANON_B_G, "K": CANON_K},
    {"name": "B_A_low", "B_A": 0.84, "B_G": CANON_B_G, "K": CANON_K},
    {"name": "B_A_high", "B_A": 0.90, "B_G": CANON_B_G, "K": CANON_K},
    {"name": "B_G_low", "B_A": CANON_B_A, "B_G": CANON_B_G - 0.02, "K": CANON_K},
    {"name": "B_G_high", "B_A": CANON_B_A, "B_G": CANON_B_G + 0.02, "K": CANON_K},
    {"name": "stress_low", "B_A": 0.84, "B_G": CANON_B_G + 0.02, "K": CANON_K},
    {"name": "stress_high", "B_A": 0.90, "B_G": CANON_B_G - 0.02, "K": CANON_K},
]

OUTCOMES = {
    "sadness": "Persistent_Sadness_Hopelessness_Total",
    "suicide_considered": "Considered_Suicide_Total",
    "suicide_plan": "Suicide_Plan_Total",
    "suicide_attempt": "Attempted_Suicide_Total",
    "sadness_female": "Persistent_Sadness_Female",
}


def pe_value(o: float, r: float, alpha: float, b_a: float, b_g: float, k: float) -> float:
    """Full nonlinear Pe."""
    c = 1.0 - (o + r + alpha) / 9.0
    return k * math.sinh(2.0 * (b_a - c * b_g))


def load_platform_scores() -> Dict[str, Dict[int, Dict[str, float]]]:
    """Load O/R/alpha/adoption for target platforms and years."""
    with open(TIMELINE_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)

    out: Dict[str, Dict[int, Dict[str, float]]] = {}
    for platform in PLATFORMS:
        pdata = raw["platforms"].get(platform, {})
        out[platform] = {}
        for year in YRBS_YEARS:
            ydata = pdata.get(str(year))
            if not ydata:
                raise KeyError(f"Missing {platform} data for year {year} in {TIMELINE_PATH}")
            out[platform][year] = {
                "O": float(ydata["O"]),
                "R": float(ydata["R"]),
                "alpha": float(ydata["alpha"]),
                "adoption_frac": float(ydata["adoption_pct"]) / 100.0,
            }
    return out


def load_outcomes() -> pd.DataFrame:
    df = pd.read_csv(YRBS_PATH)
    df = df[df["Year"].isin(YRBS_YEARS)].copy()
    df = df.sort_values("Year").reset_index(drop=True)
    return df


def compute_exposures(
    platform_scores: Dict[str, Dict[int, Dict[str, float]]],
    b_a: float,
    b_g: float,
    k: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """Return (pe_exposure, raw_adoption) aligned to YRBS_YEARS."""
    pe_exposure = []
    raw_adoption = []

    for year in YRBS_YEARS:
        pe_sum = 0.0
        raw_sum = 0.0
        for platform in PLATFORMS:
            d = platform_scores[platform][year]
            p = pe_value(d["O"], d["R"], d["alpha"], b_a, b_g, k)
            pe_sum += d["adoption_frac"] * p
            raw_sum += d["adoption_frac"]
        pe_exposure.append(pe_sum)
        raw_adoption.append(raw_sum)

    return np.array(pe_exposure, dtype=float), np.array(raw_adoption, dtype=float)


def r2(x: np.ndarray, y: np.ndarray) -> float:
    if np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return float("nan")
    rr, _ = stats.pearsonr(x, y)
    return float(rr ** 2)


def main() -> None:
    platform_scores = load_platform_scores()
    yrbs = load_outcomes()

    # Raw adoption is identical across scenarios, so compute once from canonical.
    _, raw_adopt = compute_exposures(platform_scores, CANON_B_A, CANON_B_G, CANON_K)

    scenario_results: List[dict] = []
    for scenario in SCENARIOS:
        pe_exp, _ = compute_exposures(
            platform_scores,
            scenario["B_A"],
            scenario["B_G"],
            scenario["K"],
        )

        by_outcome = {}
        for outcome_key, col in OUTCOMES.items():
            y = yrbs[col].values.astype(float)
            r2_pe = r2(pe_exp, y)
            r2_raw = r2(raw_adopt, y)
            by_outcome[outcome_key] = {
                "R2_pe": r2_pe,
                "R2_raw": r2_raw,
                "dR2_pe_minus_raw": r2_pe - r2_raw,
            }

        scenario_results.append(
            {
                "scenario": scenario["name"],
                "constants": {
                    "B_A": scenario["B_A"],
                    "B_G": scenario["B_G"],
                    "K": scenario["K"],
                },
                "pe_exposure_by_year": {
                    str(year): float(val) for year, val in zip(YRBS_YEARS, pe_exp)
                },
                "raw_adoption_by_year": {
                    str(year): float(val) for year, val in zip(YRBS_YEARS, raw_adopt)
                },
                "outcomes": by_outcome,
            }
        )

    # Build sensitivity envelopes around canonical outputs.
    canonical = next(x for x in scenario_results if x["scenario"] == "canonical")
    envelopes = {}
    for outcome_key in OUTCOMES:
        dvals = [s["outcomes"][outcome_key]["dR2_pe_minus_raw"] for s in scenario_results]
        envelopes[outcome_key] = {
            "canonical_dR2": canonical["outcomes"][outcome_key]["dR2_pe_minus_raw"],
            "min_dR2": float(np.min(dvals)),
            "max_dR2": float(np.max(dvals)),
            "scenarios_with_positive_dR2": int(np.sum(np.array(dvals) > 0)),
            "total_scenarios": len(dvals),
        }

    # Canonical Instagram inflection numbers for paper integration.
    cst = canonical["constants"]
    ig_2015 = platform_scores["instagram"][2015]
    ig_2017 = platform_scores["instagram"][2017]
    ig_pe_2015 = pe_value(ig_2015["O"], ig_2015["R"], ig_2015["alpha"], cst["B_A"], cst["B_G"], cst["K"])
    ig_pe_2017 = pe_value(ig_2017["O"], ig_2017["R"], ig_2017["alpha"], cst["B_A"], cst["B_G"], cst["K"])
    ig_contrib_2015 = ig_pe_2015 * ig_2015["adoption_frac"]
    ig_contrib_2017 = ig_pe_2017 * ig_2017["adoption_frac"]

    output = {
        "metadata": {
            "script": "full_pe_sensitivity_analysis.py",
            "years": YRBS_YEARS,
            "platforms": PLATFORMS,
            "outcomes": list(OUTCOMES.keys()),
        },
        "canonical_constants": {
            "B_A": CANON_B_A,
            "B_G": CANON_B_G,
            "K": CANON_K,
        },
        "scenarios": scenario_results,
        "sensitivity_envelopes": envelopes,
        "canonical_instagram_inflection": {
            "Pe_2015": ig_pe_2015,
            "Pe_2017": ig_pe_2017,
            "delta_Pe": ig_pe_2017 - ig_pe_2015,
            "contribution_2015": ig_contrib_2015,
            "contribution_2017": ig_contrib_2017,
            "delta_contribution": ig_contrib_2017 - ig_contrib_2015,
        },
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    # Human-readable summary.
    print("=" * 78)
    print("FULL-Pe SENSITIVITY ANALYSIS")
    print("=" * 78)
    print(f"Canonical constants: B_A={CANON_B_A:.3f}, B_G={CANON_B_G:.6f}, K={CANON_K}")
    print(f"Scenarios tested: {len(SCENARIOS)}")
    print()

    print("Sensitivity envelope: dR2 (full-Pe minus raw adoption)")
    for outcome_key in OUTCOMES:
        e = envelopes[outcome_key]
        print(
            f"  {outcome_key:<18} "
            f"canonical={e['canonical_dR2']:+.4f}  "
            f"range=[{e['min_dR2']:+.4f}, {e['max_dR2']:+.4f}]  "
            f"positive={e['scenarios_with_positive_dR2']}/{e['total_scenarios']}"
        )

    print()
    print("Canonical Instagram inflection (2015 -> 2017)")
    print(
        f"  Pe: {ig_pe_2015:+.2f} -> {ig_pe_2017:+.2f} "
        f"(delta {ig_pe_2017 - ig_pe_2015:+.2f})"
    )
    print(
        f"  Adoption-weighted contribution: {ig_contrib_2015:+.2f} -> "
        f"{ig_contrib_2017:+.2f} (delta {ig_contrib_2017 - ig_contrib_2015:+.2f})"
    )
    print()
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
