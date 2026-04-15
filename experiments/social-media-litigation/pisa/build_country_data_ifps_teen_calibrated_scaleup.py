#!/usr/bin/env python3
"""
Teen-Calibrated Ecological Scale-Up (IFPS -> PISA country panel)
=================================================================

Purpose
-------
Scale the direct-teen IFPS 6-country panel into the full 50-country PISA
ecological set by transferring teen-vs-all-age platform composition multipliers
onto the DataReportal app-audience country table.

Design
------
1) Use overlap countries (AUS/CAN/CHL/MEX/UK/US) to estimate teen/all-age
   platform composition multipliers for five platforms:
   Instagram, TikTok, Snapchat, Facebook, Twitter.
2) Apply multipliers to all 50 countries under two transfer modes:
   - composition-constrained (primary, conservative): reweight only the
     five-platform block, preserving its total share mass.
   - absolute-scaling (sensitivity): scale raw shares for the five platforms
     and renormalize all platforms to 100.
3) Recompute feature exposure and ecological correlations vs PISA life
   satisfaction.
4) Quantify uncertainty with bootstrap resampling of overlap countries and
   leave-one-country-out stress checks.

Caveats
-------
- Transfer model is observational and post-hoc (not causal identification).
- Overlap is N=6 countries, so multiplier uncertainty remains substantial.
- Calibration uses 2021 teen panel with 2022 PISA outcomes and 2023/2024
  app-audience proxy shares.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
from scipy import stats

from build_country_data import compute_feature_exposure
from build_country_data_app_usage_proxy import GDP_PER_CAPITA_2022_USD, WEST_EU, partial_corr


SCRIPT_DIR = Path(__file__).resolve().parent
APP_PROXY_JSON = SCRIPT_DIR / "pisa_app_usage_proxy_results.json"
IFPS_TEEN_CSV = SCRIPT_DIR / "pisa_ifps_teen_proxy_country_table.csv"

OUT_CSV = SCRIPT_DIR / "pisa_ifps_teen_calibrated_scaleup_country_table.csv"
OUT_JSON = SCRIPT_DIR / "pisa_ifps_teen_calibrated_scaleup_results.json"

FIVE = ["Instagram", "TikTok", "Snapchat", "Facebook", "Twitter"]
ALL_PLATFORMS = ["Facebook", "Instagram", "TikTok", "YouTube", "Snapchat", "Twitter", "Pinterest", "LinkedIn"]
BOOTSTRAP_SEED = 20260401
BOOTSTRAP_N = 4000


def gmean_positive(values: np.ndarray) -> float:
    vals = np.asarray(values, dtype=float)
    vals = vals[np.isfinite(vals)]
    vals = vals[vals > 0]
    if vals.size == 0:
        return 1.0
    return float(np.exp(np.log(vals).mean()))


def corr_block(x: np.ndarray, y: np.ndarray) -> Dict[str, float]:
    r, p = stats.pearsonr(x, y)
    rho, prho = stats.spearmanr(x, y)
    return {
        "pearson_r": float(r),
        "pearson_p": float(p),
        "spearman_rho": float(rho),
        "spearman_p": float(prho),
        "R2": float(r * r),
        "n": int(len(x)),
    }


def load_app_rows() -> List[Dict[str, object]]:
    obj = json.loads(APP_PROXY_JSON.read_text(encoding="utf-8"))
    return obj["countries"]


def load_teen_table() -> pd.DataFrame:
    teen = pd.read_csv(IFPS_TEEN_CSV)
    teen = teen[
        [
            "country",
            "share_instagram",
            "share_tiktok",
            "share_snapchat",
            "share_facebook",
            "share_twitter",
        ]
    ].rename(
        columns={
            "share_instagram": "Instagram_teen",
            "share_tiktok": "TikTok_teen",
            "share_snapchat": "Snapchat_teen",
            "share_facebook": "Facebook_teen",
            "share_twitter": "Twitter_teen",
        }
    )
    return teen


def to_row_frame(app_rows: List[Dict[str, object]]) -> pd.DataFrame:
    rows = []
    for r in app_rows:
        shares = r["shares"]
        row = {"country": r["country"], "code": r["code"], "life_satisfaction": float(r["life_satisfaction"])}
        for p in ALL_PLATFORMS:
            row[p] = float(shares.get(p, 0.0))
        rows.append(row)
    return pd.DataFrame(rows)


def composition_calibrated_shares(shares: Dict[str, float], mult: Dict[str, float]) -> Dict[str, float]:
    out = {k: float(v) for k, v in shares.items()}
    total_five = sum(out.get(p, 0.0) for p in FIVE)
    if total_five <= 0:
        return out
    comp = {p: 100.0 * out.get(p, 0.0) / total_five for p in FIVE}
    comp_adj = {p: comp[p] * mult[p] for p in FIVE}
    z = sum(comp_adj.values())
    if z <= 0:
        return out
    for p in FIVE:
        out[p] = total_five * (comp_adj[p] / z)
    return out


def absolute_calibrated_shares(shares: Dict[str, float], mult: Dict[str, float]) -> Dict[str, float]:
    out = {k: float(v) for k, v in shares.items()}
    for p in FIVE:
        out[p] = max(0.0, out.get(p, 0.0) * mult[p])
    z = sum(out.values())
    if z <= 0:
        return shares
    return {k: 100.0 * v / z for k, v in out.items()}


def evaluate_mode(df: pd.DataFrame, mode: str, comp_mult: Dict[str, float], abs_mult: Dict[str, float]) -> Dict[str, object]:
    rows = []
    for _, r in df.iterrows():
        base = {p: float(r[p]) for p in ALL_PLATFORMS}
        if mode == "baseline":
            adj = base
        elif mode == "composition_calibrated":
            adj = composition_calibrated_shares(base, comp_mult)
        elif mode == "absolute_calibrated":
            adj = absolute_calibrated_shares(base, abs_mult)
        else:
            raise ValueError(f"Unknown mode: {mode}")

        exp = compute_feature_exposure(adj)
        rows.append(
            {
                "country": r["country"],
                "code": r["code"],
                "life_satisfaction": float(r["life_satisfaction"]),
                "mean_features_per_share": float(exp["mean_features_per_share"]),
                "feature_exposure": float(exp["feature_exposure"]),
                "o_exposure": float(exp["o_exposure"]),
                "algo_feed_share": float(adj.get("Instagram", 0.0) + adj.get("TikTok", 0.0)),
                "shares": {k: float(v) for k, v in adj.items()},
            }
        )

    ls = np.array([r["life_satisfaction"] for r in rows], dtype=float)
    mean_feat = np.array([r["mean_features_per_share"] for r in rows], dtype=float)
    algo = np.array([r["algo_feed_share"] for r in rows], dtype=float)
    oexp = np.array([r["o_exposure"] for r in rows], dtype=float)

    we = [r for r in rows if r["country"] in WEST_EU]
    we_ls = np.array([r["life_satisfaction"] for r in we], dtype=float)
    we_mean = np.array([r["mean_features_per_share"] for r in we], dtype=float)
    we_algo = np.array([r["algo_feed_share"] for r in we], dtype=float)

    we_partial = {}
    we_with_gdp = [r for r in we if r["code"] in GDP_PER_CAPITA_2022_USD]
    if len(we_with_gdp) >= 4:
        x = np.array([r["mean_features_per_share"] for r in we_with_gdp], dtype=float)
        y = np.array([r["life_satisfaction"] for r in we_with_gdp], dtype=float)
        z = np.log(np.array([GDP_PER_CAPITA_2022_USD[r["code"]] for r in we_with_gdp], dtype=float))
        we_partial = partial_corr(x, y, z)

    return {
        "rows": rows,
        "global": {
            "mean_features_vs_life_satisfaction": corr_block(mean_feat, ls),
            "algo_feed_share_vs_life_satisfaction": corr_block(algo, ls),
            "o_exposure_vs_life_satisfaction": corr_block(oexp, ls),
        },
        "western_europe": {
            "n": int(len(we)),
            "mean_features_vs_life_satisfaction": corr_block(we_mean, we_ls),
            "algo_feed_share_vs_life_satisfaction": corr_block(we_algo, we_ls),
            "mean_features_partial_gdp": we_partial,
        },
    }


def summarize_draws(draws: List[float]) -> Dict[str, float]:
    arr = np.array(draws, dtype=float)
    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "p2_5": float(np.quantile(arr, 0.025)),
        "p97_5": float(np.quantile(arr, 0.975)),
        "prob_negative": float(np.mean(arr < 0)),
    }


def fast_bootstrap_r(
    df: pd.DataFrame,
    draw_mult: Dict[str, float],
    we_mask: np.ndarray,
) -> Dict[str, float]:
    mean_feat = []
    algo = []
    for _, r in df.iterrows():
        base = {p: float(r[p]) for p in ALL_PLATFORMS}
        adj = composition_calibrated_shares(base, draw_mult)
        exp = compute_feature_exposure(adj)
        mean_feat.append(float(exp["mean_features_per_share"]))
        algo.append(float(adj.get("Instagram", 0.0) + adj.get("TikTok", 0.0)))

    mean_feat_arr = np.array(mean_feat, dtype=float)
    algo_arr = np.array(algo, dtype=float)
    ls = df["life_satisfaction"].to_numpy(dtype=float)
    return {
        "global_mean_features_r": float(stats.pearsonr(mean_feat_arr, ls)[0]),
        "western_europe_mean_features_r": float(stats.pearsonr(mean_feat_arr[we_mask], ls[we_mask])[0]),
        "global_algo_feed_r": float(stats.pearsonr(algo_arr, ls)[0]),
        "western_europe_algo_feed_r": float(stats.pearsonr(algo_arr[we_mask], ls[we_mask])[0]),
    }


def main() -> None:
    print("=" * 78)
    print("IFPS TEEN-CALIBRATED SCALE-UP (PISA ECOLOGICAL)")
    print("=" * 78)

    app_rows = load_app_rows()
    app_df = to_row_frame(app_rows)
    teen_df = load_teen_table()

    overlap = teen_df.merge(app_df[["country"] + FIVE], on="country", how="inner")
    if overlap.empty:
        raise RuntimeError("No IFPS/DataReportal overlap rows found.")

    comp_mult = {}
    abs_mult = {}
    for p in FIVE:
        all_comp = 100.0 * overlap[p] / overlap[FIVE].sum(axis=1)
        comp_mult[p] = gmean_positive((overlap[f"{p}_teen"] / all_comp).to_numpy(dtype=float))
        abs_mult[p] = gmean_positive((overlap[f"{p}_teen"] / overlap[p]).to_numpy(dtype=float))

    base_eval = evaluate_mode(app_df, "baseline", comp_mult, abs_mult)
    comp_eval = evaluate_mode(app_df, "composition_calibrated", comp_mult, abs_mult)
    abs_eval = evaluate_mode(app_df, "absolute_calibrated", comp_mult, abs_mult)

    n_overlap = len(overlap)
    ratio_comp = {}
    overlap_sum5 = overlap[FIVE].sum(axis=1)
    for p in FIVE:
        all_comp = 100.0 * overlap[p] / overlap_sum5
        ratio_comp[p] = (overlap[f"{p}_teen"] / all_comp).to_numpy(dtype=float)

    rng = np.random.default_rng(BOOTSTRAP_SEED)
    we_mask = app_df["country"].isin(WEST_EU).to_numpy()
    bs_global_feat = []
    bs_we_feat = []
    bs_global_algo = []
    bs_we_algo = []
    for _ in range(BOOTSTRAP_N):
        idx = rng.integers(0, n_overlap, size=n_overlap)
        draw_mult = {}
        for p in FIVE:
            draw_mult[p] = gmean_positive(ratio_comp[p][idx])
        draw_rs = fast_bootstrap_r(app_df, draw_mult, we_mask)
        bs_global_feat.append(draw_rs["global_mean_features_r"])
        bs_we_feat.append(draw_rs["western_europe_mean_features_r"])
        bs_global_algo.append(draw_rs["global_algo_feed_r"])
        bs_we_algo.append(draw_rs["western_europe_algo_feed_r"])

    loo_rows = []
    overlap_countries = sorted(overlap["country"].tolist())
    for c in overlap_countries:
        sub = overlap[overlap["country"] != c].copy()
        draw_mult = {}
        for p in FIVE:
            all_comp = 100.0 * sub[p] / sub[FIVE].sum(axis=1)
            draw_mult[p] = gmean_positive((sub[f"{p}_teen"] / all_comp).to_numpy(dtype=float))
        draw_eval = evaluate_mode(app_df, "composition_calibrated", draw_mult, abs_mult)
        loo_rows.append(
            {
                "excluded_country": c,
                "global_mean_features_r": draw_eval["global"]["mean_features_vs_life_satisfaction"]["pearson_r"],
                "global_mean_features_p": draw_eval["global"]["mean_features_vs_life_satisfaction"]["pearson_p"],
                "western_europe_mean_features_r": draw_eval["western_europe"]["mean_features_vs_life_satisfaction"]["pearson_r"],
                "western_europe_mean_features_p": draw_eval["western_europe"]["mean_features_vs_life_satisfaction"]["pearson_p"],
            }
        )

    country_rows = []
    comp_by_country = {r["country"]: r for r in comp_eval["rows"]}
    abs_by_country = {r["country"]: r for r in abs_eval["rows"]}
    for b in base_eval["rows"]:
        c = b["country"]
        country_rows.append(
            {
                "country": c,
                "code": b["code"],
                "life_satisfaction": b["life_satisfaction"],
                "baseline_mean_features_per_share": b["mean_features_per_share"],
                "comp_cal_mean_features_per_share": comp_by_country[c]["mean_features_per_share"],
                "abs_cal_mean_features_per_share": abs_by_country[c]["mean_features_per_share"],
                "baseline_algo_feed_share": b["algo_feed_share"],
                "comp_cal_algo_feed_share": comp_by_country[c]["algo_feed_share"],
                "abs_cal_algo_feed_share": abs_by_country[c]["algo_feed_share"],
            }
        )
    pd.DataFrame(country_rows).sort_values("country").to_csv(OUT_CSV, index=False)

    out = {
        "meta": {
            "script": "build_country_data_ifps_teen_calibrated_scaleup.py",
            "inputs": [str(APP_PROXY_JSON), str(IFPS_TEEN_CSV)],
            "n_countries": int(len(app_df)),
            "n_overlap": int(len(overlap)),
            "overlap_countries": overlap_countries,
            "platforms": FIVE,
            "bootstrap_n": BOOTSTRAP_N,
            "bootstrap_seed": BOOTSTRAP_SEED,
        },
        "calibration_multipliers": {
            "composition_geomean": comp_mult,
            "absolute_geomean": abs_mult,
        },
        "results": {
            "baseline": {"global": base_eval["global"], "western_europe": base_eval["western_europe"]},
            "composition_calibrated": {"global": comp_eval["global"], "western_europe": comp_eval["western_europe"]},
            "absolute_calibrated": {"global": abs_eval["global"], "western_europe": abs_eval["western_europe"]},
        },
        "bootstrap_composition_calibrated": {
            "global_mean_features_r": summarize_draws(bs_global_feat),
            "western_europe_mean_features_r": summarize_draws(bs_we_feat),
            "global_algo_feed_r": summarize_draws(bs_global_algo),
            "western_europe_algo_feed_r": summarize_draws(bs_we_algo),
        },
        "leave_one_country_out_composition_calibrated": loo_rows,
        "country_rows": country_rows,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print(f"Saved: {OUT_JSON}")
    print(f"Saved: {OUT_CSV}")
    print(
        "Global mean-features r: "
        f"baseline={base_eval['global']['mean_features_vs_life_satisfaction']['pearson_r']:+.4f}, "
        f"comp={comp_eval['global']['mean_features_vs_life_satisfaction']['pearson_r']:+.4f}, "
        f"abs={abs_eval['global']['mean_features_vs_life_satisfaction']['pearson_r']:+.4f}"
    )
    print(
        "W. Europe mean-features r: "
        f"baseline={base_eval['western_europe']['mean_features_vs_life_satisfaction']['pearson_r']:+.4f}, "
        f"comp={comp_eval['western_europe']['mean_features_vs_life_satisfaction']['pearson_r']:+.4f}, "
        f"abs={abs_eval['western_europe']['mean_features_vs_life_satisfaction']['pearson_r']:+.4f}"
    )


if __name__ == "__main__":
    main()
