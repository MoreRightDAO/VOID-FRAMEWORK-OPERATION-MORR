#!/usr/bin/env python3
"""
PISA Cross-National Teen App-Usage Panel (IFPS Youth, 2019-2021)
=================================================================

Purpose
-------
Build a direct adolescent platform-usage panel from the International Food
Policy Study (IFPS) Youth Report and re-run a teen-weighted ecological
exposure test against PISA life satisfaction on the country overlap.

Data source
-----------
IFPS Youth Report (2021 wave values extracted from report charts):
https://foodpolicystudy.com/wp-content/uploads/2024/02/2023-IFPS-Youth-2021-Report-Sept-8.pdf

Countries with direct teen platform prevalence in this report:
Australia, Canada, Chile, Mexico, United Kingdom, United States

Important caveats
-----------------
- N = 6 countries for the teen-specific overlap.
- Platforms are limited to five charted series (Instagram, TikTok, Snapchat,
  Facebook, Twitter).
- Values are self-reported platform use prevalence, not app-time shares.
- PISA life satisfaction values are 2022 means (one-year offset from IFPS 2021).
- Observational ecological stress test only (not causal identification).
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from scipy import stats

from build_country_data import PISA_LIFE_SATISFACTION, compute_feature_exposure


SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_DIR = SCRIPT_DIR / "_cache"
CACHE_DIR.mkdir(exist_ok=True)

IFPS_PDF_URL = (
    "https://foodpolicystudy.com/wp-content/uploads/2024/02/"
    "2023-IFPS-Youth-2021-Report-Sept-8.pdf"
)
IFPS_PDF_PATH = CACHE_DIR / "ifps-youth-2021-report.pdf"
IFPS_BBOX_HTML = CACHE_DIR / "ifps-youth-2021-bbox-p71-p72.html"

OUT_PANEL = SCRIPT_DIR / "pisa_ifps_teen_platform_panel_2019_2021.csv"
OUT_COUNTRY = SCRIPT_DIR / "pisa_ifps_teen_proxy_country_table.csv"
OUT_JSON = SCRIPT_DIR / "pisa_ifps_teen_proxy_results.json"

# Page-local chart slices discovered from bbox extraction of pages 71-72.
CHART_SPECS = [
    {"platform": "Instagram", "page_idx": 0, "ymin": 240.0, "ymax": 430.0},
    {"platform": "TikTok", "page_idx": 0, "ymin": 430.0, "ymax": 575.0},
    {"platform": "Snapchat", "page_idx": 0, "ymin": 575.0, "ymax": 735.0},
    {"platform": "Facebook", "page_idx": 1, "ymin": 120.0, "ymax": 330.0},
    {"platform": "Twitter", "page_idx": 1, "ymin": 280.0, "ymax": 460.0},
]

COUNTRY_ORDER = [
    "Australia",
    "Canada",
    "Chile",
    "Mexico",
    "United Kingdom",
    "United States",
]
YEARS = [2019, 2020, 2021]
YEAR_TOKENS = {"2019", "2020", "2021"}
PCT_RE = re.compile(r"^\d+%$")


def ensure_ifps_pdf(path: Path) -> None:
    if path.exists() and path.stat().st_size > 100_000:
        return
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8",
        "Referer": "https://foodpolicystudy.com/",
    }
    try:
        resp = requests.get(IFPS_PDF_URL, headers=headers, timeout=40)
        resp.raise_for_status()
        path.write_bytes(resp.content)
        if path.stat().st_size > 100_000:
            return
    except Exception:
        pass

    cmd = [
        "curl",
        "-L",
        "--retry",
        "3",
        "--connect-timeout",
        "20",
        "--max-time",
        "120",
        "-A",
        "Mozilla/5.0",
        "-e",
        "https://foodpolicystudy.com/",
        "-o",
        str(path),
        IFPS_PDF_URL,
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    if not path.exists() or path.stat().st_size <= 100_000:
        raise RuntimeError(f"Failed to download IFPS PDF from {IFPS_PDF_URL}")


def run_bbox_extract(pdf_path: Path, out_html: Path) -> None:
    cmd = [
        "pdftotext",
        "-f",
        "71",
        "-l",
        "72",
        "-bbox-layout",
        str(pdf_path),
        str(out_html),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)


def parse_words(page_elem) -> List[Dict[str, float]]:
    out = []
    for w in page_elem.find_all("word"):
        t = w.get_text().strip()
        if not t:
            continue
        out.append(
            {
                "t": t,
                "x": float(w.get("xmin")),
                "y": float(w.get("ymin")),
            }
        )
    return out


def assign_percentages_to_ticks(
    percent_words: List[Dict[str, float]],
    tick_words: List[Dict[str, float]],
) -> Tuple[Dict[int, Dict[str, float]], float]:
    """
    One-to-one assignment using minimum absolute x-distance.
    Returns mapping tick_index -> percent_word and max assignment distance.
    """
    edges = []
    for vi, v in enumerate(percent_words):
        for ti, t in enumerate(tick_words):
            edges.append((abs(v["x"] - t["x"]), vi, ti))
    edges.sort(key=lambda x: x[0])

    assigned: Dict[int, Dict[str, float]] = {}
    used_vals = set()
    used_ticks = set()
    max_dist = 0.0

    for dist, vi, ti in edges:
        if vi in used_vals or ti in used_ticks:
            continue
        used_vals.add(vi)
        used_ticks.add(ti)
        assigned[ti] = percent_words[vi]
        max_dist = max(max_dist, dist)
        if len(assigned) == len(tick_words):
            break

    if len(assigned) != len(tick_words):
        raise RuntimeError(
            f"Assignment failed: {len(assigned)} of {len(tick_words)} ticks matched."
        )
    return assigned, max_dist


def extract_chart_panel(words: List[Dict[str, float]], ymin: float, ymax: float) -> Tuple[Dict[Tuple[str, int], float], Dict[str, float]]:
    chart_words = [w for w in words if ymin <= w["y"] <= ymax]

    ticks = sorted([w for w in chart_words if w["t"] in YEAR_TOKENS], key=lambda w: w["x"])
    pcts = sorted([w for w in chart_words if PCT_RE.fullmatch(w["t"])], key=lambda w: w["x"])

    if len(ticks) != 18:
        raise RuntimeError(f"Expected 18 year ticks, found {len(ticks)} in y-range {ymin}-{ymax}.")
    if len(pcts) != 18:
        raise RuntimeError(f"Expected 18 percentage labels, found {len(pcts)} in y-range {ymin}-{ymax}.")

    assigned, max_dist = assign_percentages_to_ticks(pcts, ticks)

    series: Dict[Tuple[str, int], float] = {}
    for i in range(len(ticks)):
        country = COUNTRY_ORDER[i // 3]
        year = YEARS[i % 3]
        pct = float(assigned[i]["t"].rstrip("%"))
        series[(country, year)] = pct

    diag = {
        "n_ticks": len(ticks),
        "n_percent_labels": len(pcts),
        "max_x_assignment_distance": float(max_dist),
    }
    return series, diag


def pearson_block(x: np.ndarray, y: np.ndarray) -> Dict[str, float]:
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


def main() -> None:
    print("=" * 76)
    print("PISA IFPS TEEN PANEL")
    print("=" * 76)

    ensure_ifps_pdf(IFPS_PDF_PATH)
    run_bbox_extract(IFPS_PDF_PATH, IFPS_BBOX_HTML)

    soup = BeautifulSoup(IFPS_BBOX_HTML.read_text(encoding="utf-8"), "html.parser")
    pages = soup.find_all("page")
    if len(pages) < 2:
        raise RuntimeError("Expected at least two pages in bbox output (IFPS report pages 71-72).")

    words_by_page = [parse_words(pages[0]), parse_words(pages[1])]

    panel_rows = []
    chart_diagnostics = {}

    for spec in CHART_SPECS:
        platform = spec["platform"]
        page_idx = spec["page_idx"]
        series, diag = extract_chart_panel(words_by_page[page_idx], spec["ymin"], spec["ymax"])
        chart_diagnostics[platform] = {
            "page_index_0_based": int(page_idx),
            "y_range": [float(spec["ymin"]), float(spec["ymax"])],
            **diag,
        }
        for (country, year), pct in series.items():
            panel_rows.append(
                {
                    "country": country,
                    "year": int(year),
                    "platform": platform,
                    "teen_selected_pct": float(pct),
                    "source": "IFPS Youth Report 2021 (chart extraction)",
                }
            )

    panel_df = pd.DataFrame(panel_rows).sort_values(["country", "year", "platform"]).reset_index(drop=True)
    panel_df.to_csv(OUT_PANEL, index=False)

    wide = (
        panel_df.pivot_table(index=["country", "year"], columns="platform", values="teen_selected_pct")
        .reset_index()
        .sort_values(["country", "year"])
    )

    teen_2021 = wide[wide["year"] == 2021].copy()
    teen_2021 = teen_2021[teen_2021["country"].isin(COUNTRY_ORDER)].copy()

    country_rows = []
    for country in COUNTRY_ORDER:
        row = teen_2021[teen_2021["country"] == country]
        if row.empty:
            raise RuntimeError(f"Missing IFPS 2021 row for {country}.")
        row = row.iloc[0]

        prevalence_pct = {
            "Instagram": float(row["Instagram"]),
            "TikTok": float(row["TikTok"]),
            "Snapchat": float(row["Snapchat"]),
            "Facebook": float(row["Facebook"]),
            "Twitter": float(row["Twitter"]),
        }
        prevalence_sum = float(sum(prevalence_pct.values()))
        normalized_share = {k: 100.0 * v / prevalence_sum for k, v in prevalence_pct.items()}

        exposure_norm = compute_feature_exposure(normalized_share)

        feature_raw = compute_feature_exposure(prevalence_pct)["feature_exposure"]
        o_raw = compute_feature_exposure(prevalence_pct)["o_exposure"]
        algo_raw = prevalence_pct["Instagram"] + prevalence_pct["TikTok"]

        life_sat = float(PISA_LIFE_SATISFACTION[country][0])
        country_rows.append(
            {
                "country": country,
                "life_satisfaction": life_sat,
                "prevalence_sum_pct": prevalence_sum,
                "feature_exposure_normalized_share": float(exposure_norm["feature_exposure"]),
                "o_exposure_normalized_share": float(exposure_norm["o_exposure"]),
                "mean_features_per_share_normalized": float(exposure_norm["mean_features_per_share"]),
                "algo_feed_share_normalized_pct": float(
                    normalized_share["Instagram"] + normalized_share["TikTok"]
                ),
                "feature_exposure_prevalence_weighted": float(feature_raw),
                "o_exposure_prevalence_weighted": float(o_raw),
                "algo_feed_prevalence_pct": float(algo_raw),
                "selected_pct_instagram": prevalence_pct["Instagram"],
                "selected_pct_tiktok": prevalence_pct["TikTok"],
                "selected_pct_snapchat": prevalence_pct["Snapchat"],
                "selected_pct_facebook": prevalence_pct["Facebook"],
                "selected_pct_twitter": prevalence_pct["Twitter"],
                "share_instagram": float(normalized_share["Instagram"]),
                "share_tiktok": float(normalized_share["TikTok"]),
                "share_snapchat": float(normalized_share["Snapchat"]),
                "share_facebook": float(normalized_share["Facebook"]),
                "share_twitter": float(normalized_share["Twitter"]),
            }
        )

    country_df = pd.DataFrame(country_rows).sort_values("country").reset_index(drop=True)
    country_df.to_csv(OUT_COUNTRY, index=False)

    ls = country_df["life_satisfaction"].to_numpy(dtype=float)
    feat_norm = country_df["feature_exposure_normalized_share"].to_numpy(dtype=float)
    algo_norm = country_df["algo_feed_share_normalized_pct"].to_numpy(dtype=float)
    feat_raw = country_df["feature_exposure_prevalence_weighted"].to_numpy(dtype=float)
    algo_raw = country_df["algo_feed_prevalence_pct"].to_numpy(dtype=float)
    intensity = country_df["prevalence_sum_pct"].to_numpy(dtype=float)

    result = {
        "meta": {
            "script": "build_country_data_ifps_teen_panel.py",
            "ifps_pdf_url": IFPS_PDF_URL,
            "ifps_pdf_cached_path": str(IFPS_PDF_PATH),
            "ifps_pages_parsed": [71, 72],
            "countries": COUNTRY_ORDER,
            "platforms": [s["platform"] for s in CHART_SPECS],
            "pisa_year": 2022,
            "ifps_year_focus": 2021,
            "n_countries": int(len(country_df)),
            "caveats": [
                "Teen-specific, but N=6 countries only.",
                "Five-platform subset only (no YouTube in IFPS chart block).",
                "Self-reported platform prevalence, not app-time share.",
                "Ecological correlation; not causal identification.",
            ],
        },
        "chart_extraction_diagnostics": chart_diagnostics,
        "correlations": {
            "normalized_feature_exposure_vs_life_satisfaction": pearson_block(feat_norm, ls),
            "normalized_algo_share_vs_life_satisfaction": pearson_block(algo_norm, ls),
            "prevalence_weighted_feature_exposure_vs_life_satisfaction": pearson_block(feat_raw, ls),
            "prevalence_weighted_algo_pct_vs_life_satisfaction": pearson_block(algo_raw, ls),
            "platform_prevalence_intensity_vs_life_satisfaction": pearson_block(intensity, ls),
        },
        "country_rows": country_df.to_dict(orient="records"),
    }

    OUT_JSON.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"Saved teen panel (long):  {OUT_PANEL}")
    print(f"Saved teen country table: {OUT_COUNTRY}")
    print(f"Saved results:            {OUT_JSON}")
    print("\nCorrelations (N=6):")
    c = result["correlations"]
    print(
        "  normalized feature vs life sat: "
        f"r={c['normalized_feature_exposure_vs_life_satisfaction']['pearson_r']:+.4f}, "
        f"p={c['normalized_feature_exposure_vs_life_satisfaction']['pearson_p']:.4f}"
    )
    print(
        "  normalized algo-share vs life sat: "
        f"r={c['normalized_algo_share_vs_life_satisfaction']['pearson_r']:+.4f}, "
        f"p={c['normalized_algo_share_vs_life_satisfaction']['pearson_p']:.4f}"
    )
    print(
        "  prevalence-weighted feature vs life sat: "
        f"r={c['prevalence_weighted_feature_exposure_vs_life_satisfaction']['pearson_r']:+.4f}, "
        f"p={c['prevalence_weighted_feature_exposure_vs_life_satisfaction']['pearson_p']:.4f}"
    )
    print(
        "  prevalence-weighted algo pct vs life sat: "
        f"r={c['prevalence_weighted_algo_pct_vs_life_satisfaction']['pearson_r']:+.4f}, "
        f"p={c['prevalence_weighted_algo_pct_vs_life_satisfaction']['pearson_p']:.4f}"
    )


if __name__ == "__main__":
    main()
