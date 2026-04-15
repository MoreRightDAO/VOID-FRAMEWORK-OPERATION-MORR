#!/usr/bin/env python3
"""
PISA Psychological Mediation Analysis (Country-Level)
=====================================================

Goal
----
Test whether the association between average social-media hours and
life satisfaction is partly mediated by negative online experiences
(`IC181Q01-04` upset percentages).

Design
------
- Unit: country
- Predictor: sm_weekday_hours_mean
- Mediator: upset_index (mean of IC181 upset percentages)
- Outcome: life_satisfaction_mean
- Covariate: escs_mean
- Inference: nonparametric bootstrap over countries
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
from scipy import stats


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_PATH = SCRIPT_DIR / "pisa_country_means.csv"
OUT_PATH = SCRIPT_DIR / "pisa_psych_mediation_results.json"

BOOTSTRAP_REPS = int(os.getenv("BOOTSTRAP_REPS", "10000"))
RNG_SEED = 20260401

UPSET_ITEMS = [
    "IC181Q01JA_upset_pct",
    "IC181Q02JA_upset_pct",
    "IC181Q03JA_upset_pct",
    "IC181Q04JA_upset_pct",
]


def weighted_fit(df: pd.DataFrame, y_col: str, x_cols: List[str], w_col: str = "n_students") -> Dict[str, object]:
    d = df.dropna(subset=[y_col] + x_cols + [w_col]).copy()
    y = d[y_col].to_numpy(dtype=float)
    x = np.column_stack([np.ones(len(d), dtype=float)] + [d[c].to_numpy(dtype=float) for c in x_cols])
    w = np.clip(d[w_col].to_numpy(dtype=float), 1e-9, None)
    sw = np.sqrt(w)
    xw = x * sw[:, None]
    yw = y * sw
    beta, _, _, _ = np.linalg.lstsq(xw, yw, rcond=None)
    yhat = x @ beta

    y_bar = np.sum(w * y) / np.sum(w)
    ss_res = np.sum(w * (y - yhat) ** 2)
    ss_tot = np.sum(w * (y - y_bar) ** 2)
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 1e-12 else float("nan")

    out = {"n": int(len(d)), "r2_weighted": r2, "betas": {"intercept": float(beta[0])}}
    for i, c in enumerate(x_cols, start=1):
        out["betas"][c] = float(beta[i])
    return out


def boot_summary(values: np.ndarray) -> Dict[str, float]:
    ge0 = float(np.mean(values >= 0))
    le0 = float(np.mean(values <= 0))
    p2 = float(2.0 * min(ge0, le0))
    return {
        "mean": float(np.mean(values)),
        "median": float(np.median(values)),
        "ci95_low": float(np.quantile(values, 0.025)),
        "ci95_high": float(np.quantile(values, 0.975)),
        "p_two_sided": p2,
        "n_boot": int(len(values)),
    }


def mediation_bootstrap(df: pd.DataFrame, mediator_col: str) -> Dict[str, object]:
    d = df.dropna(
        subset=["sm_weekday_hours_mean", "life_satisfaction_mean", "escs_mean", mediator_col, "n_students"]
    ).copy()

    countries = d["country_code"].unique().tolist()
    rng = np.random.default_rng(RNG_SEED)

    indirect_vals = []
    direct_vals = []
    total_vals = []
    mediated_share_vals = []

    for _ in range(BOOTSTRAP_REPS):
        sampled = rng.choice(countries, size=len(countries), replace=True)
        b = pd.concat([d[d["country_code"] == c] for c in sampled], ignore_index=True)

        a_fit = weighted_fit(b, mediator_col, ["sm_weekday_hours_mean", "escs_mean"])
        b_fit = weighted_fit(b, "life_satisfaction_mean", ["sm_weekday_hours_mean", mediator_col, "escs_mean"])
        c_fit = weighted_fit(b, "life_satisfaction_mean", ["sm_weekday_hours_mean", "escs_mean"])

        a = a_fit["betas"]["sm_weekday_hours_mean"]
        bb = b_fit["betas"][mediator_col]
        cp = b_fit["betas"]["sm_weekday_hours_mean"]
        c = c_fit["betas"]["sm_weekday_hours_mean"]
        ind = a * bb

        indirect_vals.append(ind)
        direct_vals.append(cp)
        total_vals.append(c)
        if abs(c) > 1e-12:
            mediated_share_vals.append(ind / c)

    indirect_vals = np.array(indirect_vals, dtype=float)
    direct_vals = np.array(direct_vals, dtype=float)
    total_vals = np.array(total_vals, dtype=float)
    mediated_share_vals = np.array(mediated_share_vals, dtype=float) if mediated_share_vals else np.array([])

    # Point estimates on full sample.
    a_fit = weighted_fit(d, mediator_col, ["sm_weekday_hours_mean", "escs_mean"])
    b_fit = weighted_fit(d, "life_satisfaction_mean", ["sm_weekday_hours_mean", mediator_col, "escs_mean"])
    c_fit = weighted_fit(d, "life_satisfaction_mean", ["sm_weekday_hours_mean", "escs_mean"])

    a = a_fit["betas"]["sm_weekday_hours_mean"]
    bb = b_fit["betas"][mediator_col]
    cp = b_fit["betas"]["sm_weekday_hours_mean"]
    c = c_fit["betas"]["sm_weekday_hours_mean"]
    ind = a * bb
    med_share = ind / c if abs(c) > 1e-12 else float("nan")

    return {
        "n_countries": int(d["country_code"].nunique()),
        "point_estimates": {
            "a_sm_to_mediator": float(a),
            "b_mediator_to_life_sat": float(bb),
            "c_total_sm_to_life_sat": float(c),
            "c_prime_direct_sm_to_life_sat": float(cp),
            "indirect_effect_a_times_b": float(ind),
            "percent_mediated": float(med_share),
        },
        "bootstrap": {
            "indirect_effect": boot_summary(indirect_vals),
            "direct_effect": boot_summary(direct_vals),
            "total_effect": boot_summary(total_vals),
            "percent_mediated": boot_summary(mediated_share_vals) if len(mediated_share_vals) > 0 else None,
        },
    }


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    df["upset_index"] = df[UPSET_ITEMS].mean(axis=1, skipna=False)

    # Core correlation table for interpretability.
    corr_df = df.dropna(
        subset=["sm_weekday_hours_mean", "life_satisfaction_mean", "upset_index", "escs_mean"]
    ).copy()

    r_sm_ls, p_sm_ls = stats.pearsonr(corr_df["sm_weekday_hours_mean"], corr_df["life_satisfaction_mean"])
    r_sm_up, p_sm_up = stats.pearsonr(corr_df["sm_weekday_hours_mean"], corr_df["upset_index"])
    r_up_ls, p_up_ls = stats.pearsonr(corr_df["upset_index"], corr_df["life_satisfaction_mean"])

    # Main mediation on combined upset index + each upset item.
    mediation_main = mediation_bootstrap(df, "upset_index")
    per_item = {}
    for item in UPSET_ITEMS:
        per_item[item] = mediation_bootstrap(df, item)

    output = {
        "metadata": {
            "script": "psychological_mediation_analysis.py",
            "bootstrap_reps": BOOTSTRAP_REPS,
            "rng_seed": RNG_SEED,
            "data_file": DATA_PATH.name,
            "design_note": "Country-level ecological mediation; not individual-level causal mediation.",
        },
        "sample": {
            "n_countries_total": int(df["country_code"].nunique()),
            "n_countries_complete_main_model": int(corr_df["country_code"].nunique()),
        },
        "pairwise_correlations": {
            "sm_hours_vs_life_satisfaction": {"r": float(r_sm_ls), "p": float(p_sm_ls)},
            "sm_hours_vs_upset_index": {"r": float(r_sm_up), "p": float(p_sm_up)},
            "upset_index_vs_life_satisfaction": {"r": float(r_up_ls), "p": float(p_up_ls)},
        },
        "mediation_upset_index": mediation_main,
        "mediation_each_upset_item": per_item,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    pe = mediation_main["point_estimates"]
    bi = mediation_main["bootstrap"]["indirect_effect"]
    print("=" * 78)
    print("PISA PSYCHOLOGICAL MEDIATION (COUNTRY-LEVEL)")
    print("=" * 78)
    print(f"Countries (complete main model): {output['sample']['n_countries_complete_main_model']}")
    print(f"sm_hours -> life_satisfaction: r={r_sm_ls:+.3f}, p={p_sm_ls:.4f}")
    print(f"sm_hours -> upset_index:       r={r_sm_up:+.3f}, p={p_sm_up:.4f}")
    print(f"upset_index -> life_sat:       r={r_up_ls:+.3f}, p={p_up_ls:.4f}")
    print()
    print("Mediation (adjusted for ESCS):")
    print(f"  total effect (c):      {pe['c_total_sm_to_life_sat']:+.4f}")
    print(f"  direct effect (c'):    {pe['c_prime_direct_sm_to_life_sat']:+.4f}")
    print(f"  indirect effect (a*b): {pe['indirect_effect_a_times_b']:+.4f}")
    print(
        "  indirect 95% CI: "
        f"[{bi['ci95_low']:+.4f}, {bi['ci95_high']:+.4f}], p={bi['p_two_sided']:.4g}"
    )
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
