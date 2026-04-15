#!/usr/bin/env python3
"""
HBSC Teen Outcome Alignment with Platform Feature Exposure
==========================================================

Purpose
-------
Add a larger direct-teen outcome layer (HBSC 2021/22 wave) to stress-test
whether platform feature intensity aligns with adolescent social-media harm
signals across countries.

Design
------
1) Download HBSC data and metadata CSVs from HBSC Data Browser public endpoints.
2) Extract 2022, age 15 rows for:
   - SMPdum: problematic social media use (PERCENTAGE)
   - EMC_intensive: frequency of intensive online contact (PERCENTAGE)
   - lifesat_mean: life satisfaction (MEAN_10)
3) Join HBSC country outcomes to:
   - StatCounter ecological exposure table (pisa_cross_national_results.json)
   - DataReportal app-audience proxy exposure table (pisa_app_usage_proxy_results.json)
4) Compute global and Western Europe correlations, plus permutation/bootstrap
   robustness and country-mapping sensitivity checks.

Caveats
-------
- Observational ecological analysis only (not causal identification).
- HBSC outcomes are not platform-specific usage; they are adolescent outcomes.
- Country name harmonization includes minor aggregation choices (Belgium region
  split; UK home-nation split).
"""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
import requests
from scipy import stats

from build_country_data_app_usage_proxy import GDP_PER_CAPITA_2022_USD, WEST_EU, partial_corr


SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_DIR = SCRIPT_DIR / "_cache"
CACHE_DIR.mkdir(exist_ok=True)

HBSC_DATA_URL = "https://data-browser.hbsc.org/wp-content/uploads/csvs/data.csv"
HBSC_META_URL = "https://data-browser.hbsc.org/wp-content/uploads/csvs/metadata.csv"
HBSC_HEADERS = {"User-Agent": "Mozilla/5.0", "Accept": "text/csv,*/*;q=0.8"}

STATCOUNTER_RESULTS = SCRIPT_DIR / "pisa_cross_national_results.json"
APP_PROXY_RESULTS = SCRIPT_DIR / "pisa_app_usage_proxy_results.json"

OUT_CSV = SCRIPT_DIR / "pisa_hbsc_teen_outcome_alignment_country_table.csv"
OUT_JSON = SCRIPT_DIR / "pisa_hbsc_teen_outcome_alignment_results.json"

BOOTSTRAP_N = 10000
PERM_N = 100000
SEED = 20260401

MEASURES = {
    "SMPdum": "problematic_social_media_use",
    "EMC_intensive": "intensive_online_contact",
    "lifesat_mean": "life_satisfaction_hbsc",
}

COUNTRY_TO_ISO2 = {
    "Austria": "AT",
    "Belgium": "BE",
    "Denmark": "DK",
    "Finland": "FI",
    "France": "FR",
    "Germany": "DE",
    "Iceland": "IS",
    "Italy": "IT",
    "Netherlands": "NL",
    "Norway": "NO",
    "Spain": "ES",
    "Sweden": "SE",
    "Switzerland": "CH",
}


def fetch_csv_rows(url: str) -> List[Dict[str, str]]:
    resp = requests.get(url, headers=HBSC_HEADERS, timeout=40)
    resp.raise_for_status()
    reader = csv.DictReader(io.StringIO(resp.text))
    return [dict(r) for r in reader]


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


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


def perm_test_pearson(x: np.ndarray, y: np.ndarray, n_perm: int, rng: np.random.Generator) -> Dict[str, float]:
    obs = float(stats.pearsonr(x, y)[0])
    null = np.empty(n_perm, dtype=float)
    for i in range(n_perm):
        y_perm = rng.permutation(y)
        null[i] = stats.pearsonr(x, y_perm)[0]
    p_two = float((np.sum(np.abs(null) >= abs(obs)) + 1) / (n_perm + 1))
    p_one_pos = float((np.sum(null >= obs) + 1) / (n_perm + 1))
    return {
        "observed_r": obs,
        "perm_two_sided_p": p_two,
        "perm_one_sided_p_positive": p_one_pos,
        "n_perm": int(n_perm),
    }


def bootstrap_r(x: np.ndarray, y: np.ndarray, n_boot: int, rng: np.random.Generator) -> Dict[str, float]:
    n = len(x)
    draws = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        draws[i] = stats.pearsonr(x[idx], y[idx])[0]
    return {
        "mean": float(np.mean(draws)),
        "median": float(np.median(draws)),
        "p2_5": float(np.quantile(draws, 0.025)),
        "p97_5": float(np.quantile(draws, 0.975)),
        "prob_positive": float(np.mean(draws > 0)),
        "n_bootstrap": int(n_boot),
    }


def build_hbsc_table(rows: List[Dict[str, str]]) -> pd.DataFrame:
    hb = pd.DataFrame(rows)
    hb = hb[hb["HBSC_id"].notna()].copy()
    hb = hb[hb["HBSC_id"] != "HBSC_id"].copy()  # repeated header rows embedded in source CSV
    hb = hb[hb["Survey_year"].isin(["2014", "2018", "2022"])].copy()
    hb = hb[hb["Age_group"].isin(["11-year-olds", "13-year-olds", "15-year-olds"])].copy()
    hb = hb[hb["HBSC_id"].isin(MEASURES.keys())].copy()

    hb["Girl"] = numeric(hb["Girl"])
    hb["Boy"] = numeric(hb["Boy"])
    hb["avg"] = (hb["Girl"] + hb["Boy"]) / 2.0

    hb22 = hb[(hb["Survey_year"] == "2022") & (hb["Age_group"] == "15-year-olds")].copy()

    parts = []
    for measure_id, short in MEASURES.items():
        d = hb22[hb22["HBSC_id"] == measure_id][["Country", "Girl", "Boy", "avg"]].copy()
        d.columns = ["country_raw", f"{short}_girl", f"{short}_boy", f"{short}_avg"]
        parts.append(d)

    out = parts[0]
    for p in parts[1:]:
        out = out.merge(p, on="country_raw", how="outer")
    return out


def harmonize_hbsc_country(df: pd.DataFrame, include_uk_regions: bool = True) -> pd.DataFrame:
    mapping = {
        "Belgium (French)": "Belgium",
        "Belgium (Flemish)": "Belgium",
    }
    if include_uk_regions:
        mapping.update(
            {
                "England": "United Kingdom",
                "Scotland": "United Kingdom",
                "Wales": "United Kingdom",
            }
        )
    d = df.copy()
    d["country"] = d["country_raw"].replace(mapping)
    return d.groupby("country", as_index=False).mean(numeric_only=True)


def load_exposure_table() -> pd.DataFrame:
    stat_obj = json.loads(STATCOUNTER_RESULTS.read_text(encoding="utf-8"))
    app_obj = json.loads(APP_PROXY_RESULTS.read_text(encoding="utf-8"))

    stat_rows = []
    for r in stat_obj["countries"]:
        stat_rows.append(
            {
                "country": r["country"],
                "mean_features_statcounter": float(r["mean_features_per_share"]),
                "feature_exposure_statcounter": float(r["feature_exposure"]),
                "o_exposure_statcounter": float(r["o_exposure"]),
                "life_satisfaction_pisa": float(r["life_satisfaction"]),
            }
        )
    app_rows = []
    for r in app_obj["countries"]:
        app_rows.append(
            {
                "country": r["country"],
                "mean_features_app_proxy": float(r["mean_features_per_share"]),
                "feature_exposure_app_proxy": float(r["feature_exposure"]),
                "o_exposure_app_proxy": float(r["o_exposure"]),
                "algo_feed_share_app_proxy": float(r["algo_feed_share"]),
            }
        )

    stat_df = pd.DataFrame(stat_rows)
    app_df = pd.DataFrame(app_rows)
    return stat_df.merge(app_df, on="country", how="inner")


def evaluate_subset(df: pd.DataFrame) -> Dict[str, Dict[str, float]]:
    outcomes = [
        "problematic_social_media_use_avg",
        "problematic_social_media_use_girl",
        "problematic_social_media_use_boy",
        "intensive_online_contact_avg",
        "life_satisfaction_hbsc_avg",
    ]
    predictors = [
        "mean_features_statcounter",
        "o_exposure_statcounter",
        "mean_features_app_proxy",
        "o_exposure_app_proxy",
        "algo_feed_share_app_proxy",
    ]
    out: Dict[str, Dict[str, float]] = {}
    for y in outcomes:
        for x in predictors:
            mask = df[x].notna() & df[y].notna()
            if int(mask.sum()) < 4:
                continue
            key = f"{x}__vs__{y}"
            out[key] = corr_block(df.loc[mask, x].to_numpy(float), df.loc[mask, y].to_numpy(float))
    return out


def main() -> None:
    print("=" * 80)
    print("HBSC TEEN OUTCOME ALIGNMENT")
    print("=" * 80)

    hbsc_rows = fetch_csv_rows(HBSC_DATA_URL)
    hbsc_meta = fetch_csv_rows(HBSC_META_URL)

    hbsc_table_raw = build_hbsc_table(hbsc_rows)
    hbsc_table = harmonize_hbsc_country(hbsc_table_raw, include_uk_regions=True)
    hbsc_table_strict = harmonize_hbsc_country(hbsc_table_raw, include_uk_regions=False)

    exposure = load_exposure_table()
    merged = hbsc_table.merge(exposure, on="country", how="inner")
    merged_strict = hbsc_table_strict.merge(exposure, on="country", how="inner")

    merged = merged.sort_values("country").reset_index(drop=True)
    merged.to_csv(OUT_CSV, index=False)

    global_stats = evaluate_subset(merged)
    west = merged[merged["country"].isin(WEST_EU)].copy()
    west_stats = evaluate_subset(west)

    rng = np.random.default_rng(SEED)
    key_global = "mean_features_statcounter__vs__problematic_social_media_use_avg"
    key_global_app = "mean_features_app_proxy__vs__problematic_social_media_use_avg"
    key_west_algo = "algo_feed_share_app_proxy__vs__problematic_social_media_use_avg"

    perm_global = {}
    boot_global = {}
    if key_global in global_stats:
        mask = merged["mean_features_statcounter"].notna() & merged["problematic_social_media_use_avg"].notna()
        x = merged.loc[mask, "mean_features_statcounter"].to_numpy(float)
        y = merged.loc[mask, "problematic_social_media_use_avg"].to_numpy(float)
        perm_global["statcounter_features_vs_psmu"] = perm_test_pearson(x, y, PERM_N, rng)
        boot_global["statcounter_features_vs_psmu"] = bootstrap_r(x, y, BOOTSTRAP_N, rng)

    if key_global_app in global_stats:
        mask = merged["mean_features_app_proxy"].notna() & merged["problematic_social_media_use_avg"].notna()
        x = merged.loc[mask, "mean_features_app_proxy"].to_numpy(float)
        y = merged.loc[mask, "problematic_social_media_use_avg"].to_numpy(float)
        perm_global["app_proxy_features_vs_psmu"] = perm_test_pearson(x, y, PERM_N, rng)
        boot_global["app_proxy_features_vs_psmu"] = bootstrap_r(x, y, BOOTSTRAP_N, rng)

    west_partial = {}
    if key_west_algo in west_stats:
        west_gdp = west.copy()
        west_gdp["iso2"] = west_gdp["country"].map(COUNTRY_TO_ISO2)
        west_gdp["gdp_pc_usd"] = west_gdp["iso2"].map(GDP_PER_CAPITA_2022_USD)
        mask = (
            west_gdp["algo_feed_share_app_proxy"].notna()
            & west_gdp["problematic_social_media_use_avg"].notna()
            & west_gdp["gdp_pc_usd"].notna()
        )
        west_gdp = west_gdp[mask].copy()
        if len(west_gdp) >= 4:
            x = west_gdp["algo_feed_share_app_proxy"].to_numpy(float)
            y = west_gdp["problematic_social_media_use_avg"].to_numpy(float)
            z = np.log(west_gdp["gdp_pc_usd"].to_numpy(float))
            west_partial["algo_feed_vs_psmu_partial_gdp"] = partial_corr(x, y, z)

    # Mapping sensitivity for main statcounter->PSMU association.
    sens = {}
    for label, dat in [
        ("strict_no_uk_aggregation", merged_strict),
        ("with_uk_aggregation", merged),
    ]:
        mask = dat["mean_features_statcounter"].notna() & dat["problematic_social_media_use_avg"].notna()
        if int(mask.sum()) >= 4:
            sens[label] = corr_block(
                dat.loc[mask, "mean_features_statcounter"].to_numpy(float),
                dat.loc[mask, "problematic_social_media_use_avg"].to_numpy(float),
            )

    meta_lookup = {
        r["HBSC_id"]: {
            "short_name": r.get("Short_name", ""),
            "measure_type": r.get("Measure_type", ""),
            "survey_years_available": r.get("Survey_years_available", ""),
            "age_groups_available": r.get("Age_groups_available", ""),
        }
        for r in hbsc_meta
        if r.get("HBSC_id") in MEASURES
    }

    out = {
        "meta": {
            "script": "build_hbsc_teen_outcome_alignment.py",
            "hbsc_data_url": HBSC_DATA_URL,
            "hbsc_meta_url": HBSC_META_URL,
            "focus_year": 2022,
            "focus_age_group": "15-year-olds",
            "measures": MEASURES,
            "n_overlap_countries_with_uk_aggregation": int(len(merged)),
            "n_overlap_countries_strict": int(len(merged_strict)),
            "seed": SEED,
            "bootstrap_n": BOOTSTRAP_N,
            "perm_n": PERM_N,
            "caveats": [
                "Ecological association only; no causal identification.",
                "HBSC outcomes are direct teen outcomes but not platform-specific usage.",
                "Country harmonization choices are tested via strict/aggregated sensitivity.",
            ],
        },
        "measure_metadata": meta_lookup,
        "global_correlations": global_stats,
        "western_europe_correlations": west_stats,
        "western_europe_partial_controls": west_partial,
        "permutation_tests": perm_global,
        "bootstrap_pearson": boot_global,
        "mapping_sensitivity": sens,
        "countries": merged.to_dict(orient="records"),
    }

    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print(f"Saved: {OUT_CSV}")
    print(f"Saved: {OUT_JSON}")
    if key_global in global_stats:
        g = global_stats[key_global]
        print(
            "Global (StatCounter mean features vs HBSC problematic use): "
            f"r={g['pearson_r']:+.4f}, p={g['pearson_p']:.4f}, n={g['n']}"
        )
    if key_global_app in global_stats:
        g = global_stats[key_global_app]
        print(
            "Global (App-proxy mean features vs HBSC problematic use): "
            f"r={g['pearson_r']:+.4f}, p={g['pearson_p']:.4f}, n={g['n']}"
        )
    if key_west_algo in west_stats:
        w = west_stats[key_west_algo]
        print(
            "W.Europe (App-proxy algo-share vs HBSC problematic use): "
            f"r={w['pearson_r']:+.4f}, p={w['pearson_p']:.4f}, n={w['n']}"
        )


if __name__ == "__main__":
    main()
