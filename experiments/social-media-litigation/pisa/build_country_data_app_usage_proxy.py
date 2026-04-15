#!/usr/bin/env python3
"""
PISA Cross-National App-Usage Proxy Analysis
============================================

Purpose
-------
Replace web-traffic-only weighting with a country-level app-audience proxy
using platform user counts published in DataReportal country reports.

Design
------
1) For each PISA country in build_country_data.py:
   - fetch DataReportal page (Digital 2023, fallback Digital 2024),
   - extract platform audience counts (millions) from platform sections.
2) Convert extracted user counts into within-country platform shares.
3) Recompute feature-weighted exposure with the Paper 166 feature matrix.
4) Correlate with PISA life satisfaction and report Western Europe diagnostics.

Important caveat
----------------
DataReportal values are advertising-reach style platform audience estimates,
not validated MAU, and they are all-age audiences while PISA reflects 15-year-olds.
This remains an ecological proxy analysis (not causal identification).
"""

from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Dict, Optional

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from scipy import stats

from build_country_data import (
    PISA_LIFE_SATISFACTION,
    compute_feature_exposure,
)


SCRIPT_DIR = Path(__file__).resolve().parent
OUT_JSON = SCRIPT_DIR / "pisa_app_usage_proxy_results.json"
OUT_CSV = SCRIPT_DIR / "pisa_app_usage_proxy_country_table.csv"

REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0"}
YEAR_CANDIDATES = [2023, 2024]
MIN_PLATFORM_COUNT = 3

COUNTRY_SLUG_OVERRIDES = {
    "Czechia": "czechia",
}

PLATFORM_PATTERNS = [
    ("Facebook", "Facebook"),
    ("Instagram", "Instagram"),
    ("TikTok", "TikTok"),
    ("YouTube", "YouTube"),
    ("Snapchat", "Snapchat"),
    ("Twitter", "Twitter"),
    ("X", "Twitter"),
    ("Pinterest", "Pinterest"),
    ("LinkedIn", "LinkedIn"),
]

WEST_EU = {
    "Austria",
    "Belgium",
    "Denmark",
    "Finland",
    "France",
    "Germany",
    "Iceland",
    "Italy",
    "Netherlands",
    "Norway",
    "Spain",
    "Sweden",
    "Switzerland",
}

GDP_PER_CAPITA_2022_USD = {
    "AU": 64674,
    "AT": 52085,
    "BE": 49582,
    "BR": 8918,
    "BG": 12221,
    "CA": 55036,
    "CL": 16265,
    "CO": 6163,
    "CR": 12691,
    "HR": 17461,
    "CZ": 27221,
    "DK": 67790,
    "EE": 28247,
    "FI": 50648,
    "FR": 40886,
    "DE": 48718,
    "GR": 20867,
    "HU": 18390,
    "IS": 73466,
    "ID": 4788,
    "IE": 103684,
    "IL": 54931,
    "IT": 34085,
    "JP": 33815,
    "KR": 32423,
    "LV": 21147,
    "LT": 24028,
    "MY": 12364,
    "MX": 10948,
    "NL": 57025,
    "NZ": 46321,
    "NO": 106149,
    "PE": 6622,
    "PH": 3623,
    "PL": 17999,
    "PT": 24566,
    "RO": 15821,
    "RS": 9230,
    "SG": 72794,
    "SK": 21260,
    "SI": 28439,
    "ES": 29675,
    "SE": 55873,
    "CH": 92434,
    "TH": 7066,
    "TR": 10674,
    "GB": 45850,
    "US": 76330,
    "UY": 17020,
    "VN": 4163,
}


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    lines = [line.strip() for line in soup.get_text("\n").splitlines() if line.strip()]
    return "\n".join(lines)


def to_millions(num_str: str, unit: str) -> float:
    value = float(num_str.replace(",", ""))
    unit_norm = unit.lower()
    if unit_norm == "billion":
        return value * 1000.0
    if unit_norm == "thousand":
        return value / 1000.0
    return value


def extract_platform_user_counts_millions(text: str, year: int) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for label, key in PLATFORM_PATTERNS:
        patterns = [
            rf"{re.escape(label)} users in [^\n]+ in {year}.{{0,1800}}?\b{re.escape(label)}\b\s+had\s+([0-9][0-9\.,]*)\s+(million|billion|thousand)\s+(?:users|members|“members”)",
            rf"{re.escape(label)} users in [^\n]+ in {year}.{{0,1800}}?\b{re.escape(label)}\b\s+had\s+([0-9][0-9\.,]*)\s+(?:users|members|“members”)",
        ]

        found: Optional[float] = None
        for pat in patterns:
            m = re.search(pat, text, flags=re.IGNORECASE | re.DOTALL)
            if not m:
                continue
            if len(m.groups()) == 2:
                found = to_millions(m.group(1), m.group(2))
            else:
                found = float(m.group(1).replace(",", "")) / 1_000_000.0
            break

        if found is not None:
            if key not in out or found > out[key]:
                out[key] = found
    return out


def user_counts_to_shares_pct(user_counts_millions: Dict[str, float]) -> Dict[str, float]:
    total = sum(user_counts_millions.values())
    if total <= 0:
        return {}
    return {k: 100.0 * v / total for k, v in user_counts_millions.items()}


def fetch_country_app_mix(country: str, default_slug: str) -> Optional[Dict[str, object]]:
    slug_candidates = []
    if country in COUNTRY_SLUG_OVERRIDES:
        slug_candidates.append(COUNTRY_SLUG_OVERRIDES[country])
    if default_slug not in slug_candidates:
        slug_candidates.append(default_slug)

    for year in YEAR_CANDIDATES:
        for slug in slug_candidates:
            url = f"https://datareportal.com/reports/digital-{year}-{slug}"
            try:
                resp = requests.get(url, headers=REQUEST_HEADERS, timeout=20)
            except Exception:
                continue
            if resp.status_code != 200 or len(resp.text) < 50_000:
                continue

            text = html_to_text(resp.text)
            counts = extract_platform_user_counts_millions(text, year)
            if len(counts) < MIN_PLATFORM_COUNT:
                continue

            shares = user_counts_to_shares_pct(counts)
            return {
                "year": year,
                "slug": slug,
                "url": url,
                "user_counts_millions": counts,
                "shares_pct": shares,
            }
    return None


def partial_corr(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> Dict[str, float]:
    bx = np.polyfit(z, x, 1)
    by = np.polyfit(z, y, 1)
    rx = x - np.polyval(bx, z)
    ry = y - np.polyval(by, z)
    r, p = stats.pearsonr(rx, ry)
    return {"r": float(r), "p": float(p)}


def main() -> None:
    print("=" * 72)
    print("PISA APP-USAGE PROXY ANALYSIS")
    print("=" * 72)

    rows = []
    failures = []

    countries = sorted(PISA_LIFE_SATISFACTION.items(), key=lambda kv: kv[0])
    for country, (life_sat, default_slug, iso_code) in countries:
        print(f"{country:20s} ({iso_code}) ... ", end="", flush=True)
        fetched = fetch_country_app_mix(country, default_slug)
        if not fetched:
            failures.append({"country": country, "code": iso_code, "slug": default_slug})
            print("FAILED")
            continue

        shares = fetched["shares_pct"]
        exposure = compute_feature_exposure(shares)
        algo_feed_share = shares.get("Instagram", 0.0) + shares.get("TikTok", 0.0)

        row = {
            "country": country,
            "code": iso_code,
            "life_satisfaction": float(life_sat),
            "source_year": int(fetched["year"]),
            "source_slug": fetched["slug"],
            "source_url": fetched["url"],
            "n_platforms": int(len(shares)),
            "app_users_total_million": float(sum(fetched["user_counts_millions"].values())),
            "feature_exposure": float(exposure["feature_exposure"]),
            "o_exposure": float(exposure["o_exposure"]),
            "r_exposure": float(exposure["r_exposure"]),
            "alpha_exposure": float(exposure["alpha_exposure"]),
            "mean_features_per_share": float(exposure["mean_features_per_share"]),
            "algo_feed_share": float(algo_feed_share),
            "shares": {k: float(v) for k, v in shares.items()},
            "user_counts_millions": {k: float(v) for k, v in fetched["user_counts_millions"].items()},
        }
        rows.append(row)
        print(f"OK ({row['n_platforms']} platforms, feat={row['feature_exposure']:.2f})")
        time.sleep(0.2)

    if not rows:
        raise RuntimeError("No countries fetched successfully; cannot compute analysis.")

    ls = np.array([r["life_satisfaction"] for r in rows], dtype=float)
    feat = np.array([r["feature_exposure"] for r in rows], dtype=float)
    mean_feat = np.array([r["mean_features_per_share"] for r in rows], dtype=float)
    algo = np.array([r["algo_feed_share"] for r in rows], dtype=float)
    oexp = np.array([r["o_exposure"] for r in rows], dtype=float)

    r_feat, p_feat = stats.pearsonr(feat, ls)
    r_mean, p_mean = stats.pearsonr(mean_feat, ls)
    r_algo, p_algo = stats.pearsonr(algo, ls)
    r_o, p_o = stats.pearsonr(oexp, ls)

    we_rows = [r for r in rows if r["country"] in WEST_EU]
    we_stats = {}
    if len(we_rows) >= 4:
        we_ls = np.array([r["life_satisfaction"] for r in we_rows], dtype=float)
        we_mean = np.array([r["mean_features_per_share"] for r in we_rows], dtype=float)
        we_algo = np.array([r["algo_feed_share"] for r in we_rows], dtype=float)
        we_r, we_p = stats.pearsonr(we_mean, we_ls)
        we_ar, we_ap = stats.pearsonr(we_algo, we_ls)
        we_stats = {
            "n": len(we_rows),
            "features_vs_ls": {"r": float(we_r), "p": float(we_p), "R2": float(we_r**2)},
            "algo_feed_vs_ls": {"r": float(we_ar), "p": float(we_ap)},
        }

        we_with_gdp = [r for r in we_rows if r["code"] in GDP_PER_CAPITA_2022_USD]
        if len(we_with_gdp) >= 4:
            x = np.array([r["mean_features_per_share"] for r in we_with_gdp], dtype=float)
            y = np.array([r["life_satisfaction"] for r in we_with_gdp], dtype=float)
            z = np.log(np.array([GDP_PER_CAPITA_2022_USD[r["code"]] for r in we_with_gdp], dtype=float))
            we_stats["features_partial_gdp"] = partial_corr(x, y, z)

    # Flatten for CSV.
    flat_rows = []
    share_cols = ["Facebook", "Instagram", "TikTok", "YouTube", "Snapchat", "Twitter", "Pinterest", "LinkedIn"]
    for r in rows:
        out = {k: r[k] for k in [
            "country",
            "code",
            "life_satisfaction",
            "source_year",
            "source_slug",
            "n_platforms",
            "app_users_total_million",
            "feature_exposure",
            "o_exposure",
            "r_exposure",
            "alpha_exposure",
            "mean_features_per_share",
            "algo_feed_share",
        ]}
        for c in share_cols:
            out[f"share_{c.lower()}"] = float(r["shares"].get(c, 0.0))
        flat_rows.append(out)
    pd.DataFrame(flat_rows).to_csv(OUT_CSV, index=False)

    result = {
        "meta": {
            "script": "build_country_data_app_usage_proxy.py",
            "method": "DataReportal country report app-audience proxy",
            "year_candidates": YEAR_CANDIDATES,
            "min_platform_count": MIN_PLATFORM_COUNT,
            "n_countries_success": len(rows),
            "n_countries_failed": len(failures),
            "caveat": "Ecological proxy (all-age ad audience estimates), not causal identification.",
        },
        "global": {
            "features_vs_ls": {"r": float(r_feat), "p": float(p_feat), "R2": float(r_feat**2)},
            "mean_features_vs_ls": {"r": float(r_mean), "p": float(p_mean), "R2": float(r_mean**2)},
            "algo_feed_vs_ls": {"r": float(r_algo), "p": float(p_algo), "R2": float(r_algo**2)},
            "o_exposure_vs_ls": {"r": float(r_o), "p": float(p_o), "R2": float(r_o**2)},
        },
        "western_europe": we_stats,
        "failures": failures,
        "countries": rows,
    }

    OUT_JSON.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print("\n--- SUMMARY ---")
    print(f"Countries successful: {len(rows)} / {len(countries)}")
    print(f"Global mean-features vs LS: r={r_mean:+.4f}, p={p_mean:.4f}")
    print(f"Global feature exposure vs LS: r={r_feat:+.4f}, p={p_feat:.4f}")
    print(f"Global algo-feed share vs LS: r={r_algo:+.4f}, p={p_algo:.4f}")
    if we_stats:
        print(
            "Western Europe mean-features vs LS: "
            f"r={we_stats['features_vs_ls']['r']:+.4f}, p={we_stats['features_vs_ls']['p']:.4f}"
        )
    print(f"\nSaved: {OUT_JSON}")
    print(f"Saved: {OUT_CSV}")


if __name__ == "__main__":
    main()
