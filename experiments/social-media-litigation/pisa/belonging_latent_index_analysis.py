#!/usr/bin/env python3
"""
PISA Belonging/Loneliness Latent Index Analysis (Country-Level)
===============================================================

Goal
----
Build a latent social-disconnection index from PISA ST034 items and test:
  1) SM hours -> latent disconnection
  2) latent disconnection -> life satisfaction
  3) mediation of SM-hours effect via latent disconnection

All analyses are ecological (country-level aggregates).
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
OUT_PATH = SCRIPT_DIR / "pisa_belonging_latent_results.json"

BOOTSTRAP_REPS = int(os.getenv("BOOTSTRAP_REPS", "10000"))
RNG_SEED = 20260401

# ST034 coding: 1=strongly agree ... 4=strongly disagree
# Convert each item so higher means more social disconnection.
ITEM_MAP = {
    "ST034Q01TA_mean": ("outsider_distress", "neg_statement"),   # "I feel like an outsider"
    "ST034Q02TA_mean": ("friends_difficulty", "pos_statement"),  # "I make friends easily"
    "ST034Q03TA_mean": ("no_belonging", "pos_statement"),        # "I feel like I belong"
    "ST034Q04TA_mean": ("awkward_distress", "neg_statement"),    # "I feel awkward/out of place"
    "ST034Q05TA_mean": ("not_liked", "pos_statement"),           # "Other students seem to like me"
    "ST034Q06TA_mean": ("lonely_distress", "neg_statement"),     # "I feel lonely"
}


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


def cronbach_alpha(x: np.ndarray) -> float:
    # x shape: n_samples x n_items
    k = x.shape[1]
    if k < 2:
        return float("nan")
    item_vars = np.var(x, axis=0, ddof=1)
    total_scores = np.sum(x, axis=1)
    total_var = np.var(total_scores, ddof=1)
    if total_var <= 1e-12:
        return float("nan")
    alpha = (k / (k - 1.0)) * (1.0 - np.sum(item_vars) / total_var)
    return float(alpha)


def build_disconnection_index(df: pd.DataFrame) -> Dict[str, object]:
    d = df.copy()

    transformed_cols = []
    for raw_col, (new_col, kind) in ITEM_MAP.items():
        if kind == "neg_statement":
            # For negative statements: agree=1 means worse; disconnection score = 5 - response.
            d[new_col] = 5.0 - d[raw_col]
        else:
            # For positive statements: disagree=4 means worse; disconnection score = response.
            d[new_col] = d[raw_col].astype(float)
        transformed_cols.append(new_col)

    clean = d.dropna(subset=transformed_cols).copy()
    x = clean[transformed_cols].to_numpy(dtype=float)

    # Standardize items across countries.
    mu = np.mean(x, axis=0)
    sd = np.std(x, axis=0, ddof=0)
    sd = np.where(sd < 1e-9, 1.0, sd)
    z = (x - mu) / sd

    # PCA first component.
    cov = np.cov(z, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov)
    idx = int(np.argmax(eigvals))
    pc1 = eigvecs[:, idx]
    score = z @ pc1

    # Orient component so higher = more average disconnection.
    avg_disconnection = np.mean(z, axis=1)
    if np.corrcoef(score, avg_disconnection)[0, 1] < 0:
        pc1 = -pc1
        score = -score

    clean["belonging_disconnection_index"] = score

    # Item loading table.
    loadings = {col: float(val) for col, val in zip(transformed_cols, pc1)}
    alpha = cronbach_alpha(z)

    return {
        "data": clean,
        "transformed_cols": transformed_cols,
        "loadings": loadings,
        "explained_variance_ratio_pc1": float(eigvals[idx] / np.sum(eigvals)),
        "cronbach_alpha_standardized": alpha,
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
    latent = build_disconnection_index(df)
    d = latent["data"]

    # Correlations.
    corr_df = d.dropna(subset=["sm_weekday_hours_mean", "life_satisfaction_mean", "belonging_disconnection_index"])
    r_sm_lat, p_sm_lat = stats.pearsonr(
        corr_df["sm_weekday_hours_mean"], corr_df["belonging_disconnection_index"]
    )
    r_lat_ls, p_lat_ls = stats.pearsonr(
        corr_df["belonging_disconnection_index"], corr_df["life_satisfaction_mean"]
    )
    r_sm_ls, p_sm_ls = stats.pearsonr(
        corr_df["sm_weekday_hours_mean"], corr_df["life_satisfaction_mean"]
    )

    mediation = mediation_bootstrap(d, "belonging_disconnection_index")

    output = {
        "metadata": {
            "script": "belonging_latent_index_analysis.py",
            "bootstrap_reps": BOOTSTRAP_REPS,
            "rng_seed": RNG_SEED,
            "data_file": DATA_PATH.name,
            "design_note": "Country-level latent construct and ecological mediation.",
        },
        "sample": {
            "n_countries_total": int(df["country_code"].nunique()),
            "n_countries_with_all_st034_items": int(d["country_code"].nunique()),
            "n_countries_complete_main_model": int(
                d.dropna(
                    subset=[
                        "sm_weekday_hours_mean",
                        "life_satisfaction_mean",
                        "escs_mean",
                        "belonging_disconnection_index",
                    ]
                )["country_code"].nunique()
            ),
        },
        "latent_index": {
            "item_loadings_pc1": latent["loadings"],
            "explained_variance_ratio_pc1": latent["explained_variance_ratio_pc1"],
            "cronbach_alpha_standardized": latent["cronbach_alpha_standardized"],
            "index_name": "belonging_disconnection_index",
            "orientation": "higher = more social disconnection/loneliness",
        },
        "pairwise_correlations": {
            "sm_hours_vs_disconnection_index": {"r": float(r_sm_lat), "p": float(p_sm_lat)},
            "disconnection_index_vs_life_satisfaction": {"r": float(r_lat_ls), "p": float(p_lat_ls)},
            "sm_hours_vs_life_satisfaction": {"r": float(r_sm_ls), "p": float(p_sm_ls)},
        },
        "mediation_disconnection_index": mediation,
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    pe = mediation["point_estimates"]
    bi = mediation["bootstrap"]["indirect_effect"]
    print("=" * 78)
    print("PISA BELONGING/LONELINESS LATENT INDEX ANALYSIS")
    print("=" * 78)
    print(
        "Countries (latent complete / model complete): "
        f"{output['sample']['n_countries_with_all_st034_items']} / "
        f"{output['sample']['n_countries_complete_main_model']}"
    )
    print(
        "Latent PC1 explained variance / alpha: "
        f"{output['latent_index']['explained_variance_ratio_pc1']:.3f} / "
        f"{output['latent_index']['cronbach_alpha_standardized']:.3f}"
    )
    print(f"sm_hours -> latent disconnection: r={r_sm_lat:+.3f}, p={p_sm_lat:.4f}")
    print(f"latent disconnection -> life sat: r={r_lat_ls:+.3f}, p={p_lat_ls:.4f}")
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
