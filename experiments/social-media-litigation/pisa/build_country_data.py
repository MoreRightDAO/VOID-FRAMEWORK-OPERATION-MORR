#!/usr/bin/env python3
"""
PISA 2022 Cross-National Analysis — Feature-Weighted Platform Exposure vs. Adolescent Wellbeing
================================================================================================

PURPOSE: Test whether countries where high-opacity platforms dominate show worse
adolescent wellbeing, using PISA 2022 life satisfaction scores and StatCounter
platform market share data.

METHODOLOGY:
1. Get platform market share by country from StatCounter (2022 annual)
2. Score each platform using our 13-feature matrix (from Paper 166)
3. Compute country-level feature-weighted exposure
4. Correlate with PISA 2022 mean life satisfaction by country
5. Test whether opacity-weighted exposure predicts worse outcomes

DATA SOURCES:
- StatCounter: Social media market share by country (2022, web traffic share)
- PISA 2022: Mean life satisfaction scores by country (OECD published tables)
- Feature matrix: Paper 166 feature scores for 2023 (closest available year)

CAVEATS:
- StatCounter measures WEB TRAFFIC SHARE, not user adoption. Facebook dominates
  web traffic but TikTok dominates mobile app time (not captured by web analytics).
  This is a known limitation — we're measuring what StatCounter can see.
- PISA life satisfaction is 15-year-olds only. Platform market share is all ages.
- Country-level ecological correlation. Individual-level data would be stronger.
- N = number of PISA countries with StatCounter data (~40-50).

Author: MoreRight Research
Date: 2026-03-30
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

# ─── PISA 2022 Life Satisfaction by Country ───────────────────────────────────
# Source: OECD PISA 2022 Results, published tables
# Scale: 0-10 (Cantril ladder: "How satisfied are you with your life as a whole?")
# These are published country means for 15-year-old students.
# Source: OECD (2023), PISA 2022 Results (Vol. II), Table II.B1.11.1
# Additional: World Happiness Report 2026, Chapter on Adolescent Life Satisfaction
# OECD average: 6.75

PISA_LIFE_SATISFACTION = {
    # Country: (mean_life_satisfaction, StatCounter_URL_slug, ISO_code)
    # OECD countries
    "Australia": (6.58, "australia", "AU"),
    "Austria": (7.04, "austria", "AT"),
    "Belgium": (6.85, "belgium", "BE"),
    "Canada": (6.67, "canada", "CA"),
    "Chile": (7.09, "chile", "CL"),
    "Colombia": (7.70, "colombia", "CO"),
    "Costa Rica": (7.73, "costa-rica", "CR"),
    "Czechia": (6.62, "czech-republic", "CZ"),
    "Denmark": (7.23, "denmark", "DK"),
    "Estonia": (6.67, "estonia", "EE"),
    "Finland": (7.04, "finland", "FI"),
    "France": (6.68, "france", "FR"),
    "Germany": (6.56, "germany", "DE"),
    "Greece": (6.74, "greece", "GR"),
    "Hungary": (6.67, "hungary", "HU"),
    "Iceland": (6.62, "iceland", "IS"),
    "Ireland": (6.79, "ireland", "IE"),
    "Israel": (7.01, "israel", "IL"),
    "Italy": (6.60, "italy", "IT"),
    "Japan": (6.04, "japan", "JP"),
    "Korea": (6.36, "south-korea", "KR"),
    "Latvia": (6.68, "latvia", "LV"),
    "Lithuania": (6.66, "lithuania", "LT"),
    "Mexico": (7.67, "mexico", "MX"),
    "Netherlands": (6.90, "netherlands", "NL"),
    "New Zealand": (6.52, "new-zealand", "NZ"),
    "Norway": (6.90, "norway", "NO"),
    "Poland": (6.59, "poland", "PL"),
    "Portugal": (6.83, "portugal", "PT"),
    "Slovak Republic": (6.57, "slovakia", "SK"),
    "Slovenia": (6.62, "slovenia", "SI"),
    "Spain": (6.90, "spain", "ES"),
    "Sweden": (6.62, "sweden", "SE"),
    "Switzerland": (7.13, "switzerland", "CH"),
    "Türkiye": (5.87, "turkey", "TR"),
    "United Kingdom": (6.01, "united-kingdom", "GB"),
    "United States": (6.41, "united-states-of-america", "US"),
    # Partner countries
    "Brazil": (6.65, "brazil", "BR"),
    "Bulgaria": (6.68, "bulgaria", "BG"),
    "Croatia": (6.71, "croatia", "HR"),
    "Indonesia": (7.28, "indonesia", "ID"),
    "Malaysia": (6.95, "malaysia", "MY"),
    "Peru": (7.33, "peru", "PE"),
    "Philippines": (7.19, "philippines", "PH"),
    "Romania": (6.95, "romania", "RO"),
    "Serbia": (6.94, "serbia", "RS"),
    "Singapore": (6.18, "singapore", "SG"),
    "Thailand": (7.08, "thailand", "TH"),
    "Uruguay": (7.05, "uruguay", "UY"),
    "Vietnam": (6.71, "vietnam", "VN"),
}

# ─── Platform Feature Scores (from Paper 166, 2023 values) ────────────────────
# Each platform's total feature score and O-type sub-score
PLATFORM_FEATURES = {
    "Facebook":   {"total": 13, "O": 6, "R": 4, "alpha": 3},
    "Instagram":  {"total": 17, "O": 8, "R": 5, "alpha": 4},
    "Twitter":    {"total": 10, "O": 5, "R": 3, "alpha": 2},
    "Pinterest":  {"total":  8, "O": 4, "R": 2, "alpha": 2},
    "YouTube":    {"total": 14, "O": 7, "R": 4, "alpha": 3},
    "LinkedIn":   {"total":  7, "O": 3, "R": 2, "alpha": 2},
    "reddit":     {"total":  9, "O": 4, "R": 3, "alpha": 2},
    "Tumblr":     {"total":  7, "O": 3, "R": 2, "alpha": 2},
    "VKontakte":  {"total": 12, "O": 5, "R": 4, "alpha": 3},
    "TikTok":     {"total": 18, "O": 8, "R": 5, "alpha": 5},
    "Snapchat":   {"total": 16, "O": 6, "R": 5, "alpha": 5},
    "WhatsApp":   {"total":  5, "O": 1, "R": 2, "alpha": 2},
    "Telegram":   {"total":  5, "O": 1, "R": 2, "alpha": 2},
}

# Default features for unknown platforms (conservative: assume medium)
DEFAULT_FEATURES = {"total": 8, "O": 3, "R": 3, "alpha": 2}


def fetch_statcounter(slug: str, iso_code: str) -> dict:
    """Fetch 2022 annual social media market share for a country from StatCounter."""
    url = (
        f"https://gs.statcounter.com/social-media-stats/all/{slug}"
        f"/chart.php?bar=1&device=Mobile&device_hidden=mobile"
        f"&statType_hidden=social_media&region_hidden={iso_code.lower()}"
        f"&granularity=monthly&statType=Social%20Media"
        f"&region={iso_code}&fromInt=202201&toInt=202212"
        f"&fromMonthYear=2022-01&toMonthYear=2022-12&csv=1"
    )
    try:
        result = subprocess.run(
            ["curl", "-s", url],
            capture_output=True, text=True, timeout=15
        )
        lines = result.stdout.strip().split("\n")
        shares = {}
        for line in lines[1:]:  # skip header
            # Format: "Platform Name",12.34
            line = line.strip()
            if not line or line.startswith('"Other"'):
                continue
            # Split on first comma after closing quote
            if line.startswith('"'):
                end_quote = line.index('"', 1)
                platform = line[1:end_quote]
                val_str = line[end_quote+2:]  # skip ","
                try:
                    share = float(val_str)
                    shares[platform] = share
                except ValueError:
                    continue
        return shares
    except Exception as e:
        print(f"  [WARN] Failed for {country_code}: {e}")
        return {}


def compute_feature_exposure(shares: dict) -> dict:
    """Compute feature-weighted exposure from platform market shares."""
    total_exposure = 0.0
    o_exposure = 0.0
    r_exposure = 0.0
    alpha_exposure = 0.0
    raw_share_sum = 0.0

    for platform, share in shares.items():
        features = PLATFORM_FEATURES.get(platform, DEFAULT_FEATURES)
        weight = share / 100.0
        total_exposure += weight * features["total"]
        o_exposure += weight * features["O"]
        r_exposure += weight * features["R"]
        alpha_exposure += weight * features["alpha"]
        raw_share_sum += weight

    return {
        "feature_exposure": total_exposure,
        "o_exposure": o_exposure,
        "r_exposure": r_exposure,
        "alpha_exposure": alpha_exposure,
        "raw_share": raw_share_sum,
        "mean_features_per_share": total_exposure / raw_share_sum if raw_share_sum > 0 else 0,
    }


def main():
    print("=" * 70)
    print("PISA 2022 CROSS-NATIONAL ANALYSIS")
    print("Feature-Weighted Platform Exposure vs. Adolescent Life Satisfaction")
    print("=" * 70)

    # Step 1: Fetch StatCounter data for all PISA countries
    print(f"\n--- STEP 1: Fetching StatCounter data for {len(PISA_LIFE_SATISFACTION)} countries ---\n")

    country_data = []
    for country, (life_sat, slug, iso_code) in sorted(PISA_LIFE_SATISFACTION.items()):
        print(f"  {country} ({iso_code})...", end=" ", flush=True)
        shares = fetch_statcounter(slug, iso_code)
        if shares:
            exposure = compute_feature_exposure(shares)
            country_data.append({
                "country": country,
                "code": iso_code,
                "life_satisfaction": life_sat,
                "shares": shares,
                **exposure,
            })
            print(f"OK ({len(shares)} platforms, feat_exp={exposure['feature_exposure']:.1f})")
        else:
            print("FAILED")
        time.sleep(0.3)  # be polite to StatCounter

    print(f"\n  Successfully fetched: {len(country_data)}/{len(PISA_LIFE_SATISFACTION)} countries")

    # Step 2: Compute correlations
    print("\n--- STEP 2: CORRELATIONS ---\n")

    life_sat = np.array([d["life_satisfaction"] for d in country_data])
    feat_exp = np.array([d["feature_exposure"] for d in country_data])
    o_exp = np.array([d["o_exposure"] for d in country_data])
    r_exp = np.array([d["r_exposure"] for d in country_data])
    a_exp = np.array([d["alpha_exposure"] for d in country_data])
    mean_feat = np.array([d["mean_features_per_share"] for d in country_data])

    from scipy import stats

    # Feature exposure vs life satisfaction
    r_feat, p_feat = stats.pearsonr(feat_exp, life_sat)
    rho_feat, prho_feat = stats.spearmanr(feat_exp, life_sat)
    print(f"  Feature exposure vs Life Satisfaction:")
    print(f"    Pearson r  = {r_feat:+.4f}  (p = {p_feat:.6f})")
    print(f"    Spearman ρ = {rho_feat:+.4f}  (p = {prho_feat:.6f})")
    print(f"    R² = {r_feat**2:.4f}")

    # Mean features per share (design quality independent of total market)
    r_mf, p_mf = stats.pearsonr(mean_feat, life_sat)
    rho_mf, prho_mf = stats.spearmanr(mean_feat, life_sat)
    print(f"\n  Mean features per share vs Life Satisfaction:")
    print(f"    Pearson r  = {r_mf:+.4f}  (p = {p_mf:.6f})")
    print(f"    Spearman ρ = {rho_mf:+.4f}  (p = {prho_mf:.6f})")
    print(f"    R² = {r_mf**2:.4f}")

    # O-exposure vs life satisfaction
    r_o, p_o = stats.pearsonr(o_exp, life_sat)
    print(f"\n  O-exposure (opacity) vs Life Satisfaction:")
    print(f"    Pearson r  = {r_o:+.4f}  (p = {p_o:.6f})")
    print(f"    R² = {r_o**2:.4f}")

    # R-exposure
    r_r, p_r = stats.pearsonr(r_exp, life_sat)
    print(f"\n  R-exposure (reactivity) vs Life Satisfaction:")
    print(f"    Pearson r  = {r_r:+.4f}  (p = {p_r:.6f})")

    # Alpha-exposure
    r_a, p_a = stats.pearsonr(a_exp, life_sat)
    print(f"\n  α-exposure (coupling) vs Life Satisfaction:")
    print(f"    Pearson r  = {r_a:+.4f}  (p = {p_a:.6f})")

    # Step 3: Regional analysis
    print("\n--- STEP 3: REGIONAL ANALYSIS ---\n")

    english_speaking = {"Australia", "Canada", "Ireland", "New Zealand", "United Kingdom", "United States"}
    western_europe = {"Austria", "Belgium", "Denmark", "Finland", "France", "Germany", "Iceland",
                      "Italy", "Netherlands", "Norway", "Spain", "Sweden", "Switzerland"}

    for region_name, region_countries in [("English-speaking", english_speaking),
                                           ("Western Europe", western_europe)]:
        region_data = [d for d in country_data if d["country"] in region_countries]
        if len(region_data) >= 4:
            r_ls = np.array([d["life_satisfaction"] for d in region_data])
            r_fe = np.array([d["mean_features_per_share"] for d in region_data])
            r_val, p_val = stats.pearsonr(r_fe, r_ls)
            print(f"  {region_name} (N={len(region_data)}):")
            print(f"    Mean life satisfaction: {r_ls.mean():.2f}")
            print(f"    Mean features/share: {r_fe.mean():.2f}")
            print(f"    r(features, life_sat) = {r_val:+.4f} (p = {p_val:.4f})")
        print()

    # Step 4: Top/bottom analysis
    print("--- STEP 4: TOP vs BOTTOM COUNTRIES ---\n")

    sorted_by_feat = sorted(country_data, key=lambda d: d["mean_features_per_share"], reverse=True)
    top5 = sorted_by_feat[:5]
    bottom5 = sorted_by_feat[-5:]

    print("  Highest mean feature score (most harmful platform mix):")
    for d in top5:
        top_platform = max(d["shares"], key=d["shares"].get)
        print(f"    {d['country']:20s} feat/share={d['mean_features_per_share']:.1f}  "
              f"life_sat={d['life_satisfaction']:.2f}  top={top_platform}")

    print("\n  Lowest mean feature score (least harmful platform mix):")
    for d in bottom5:
        top_platform = max(d["shares"], key=d["shares"].get)
        print(f"    {d['country']:20s} feat/share={d['mean_features_per_share']:.1f}  "
              f"life_sat={d['life_satisfaction']:.2f}  top={top_platform}")

    top5_ls = np.mean([d["life_satisfaction"] for d in top5])
    bot5_ls = np.mean([d["life_satisfaction"] for d in bottom5])
    print(f"\n  Top 5 mean life satisfaction: {top5_ls:.2f}")
    print(f"  Bottom 5 mean life satisfaction: {bot5_ls:.2f}")
    print(f"  Difference: {bot5_ls - top5_ls:+.2f}")

    # Step 5: Save results
    output = {
        "metadata": {
            "analysis": "PISA 2022 Cross-National Feature Exposure",
            "date": "2026-03-30",
            "n_countries": len(country_data),
        },
        "correlations": {
            "feature_exposure_vs_life_sat": {"r": r_feat, "p": p_feat, "R2": r_feat**2},
            "mean_features_vs_life_sat": {"r": r_mf, "p": p_mf, "R2": r_mf**2},
            "o_exposure_vs_life_sat": {"r": r_o, "p": p_o, "R2": r_o**2},
        },
        "countries": country_data,
    }

    out_path = Path(__file__).parent / "pisa_cross_national_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n  Results saved to {out_path}")

    # Step 6: Generate figure
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Panel A: Feature exposure vs life satisfaction
        ax = axes[0]
        ax.scatter(mean_feat, life_sat, c="steelblue", alpha=0.7, s=40)
        for d in country_data:
            if d["country"] in english_speaking:
                ax.annotate(d["code"], (d["mean_features_per_share"], d["life_satisfaction"]),
                           fontsize=7, color="red", alpha=0.8)
            elif d["country"] in western_europe:
                ax.annotate(d["code"], (d["mean_features_per_share"], d["life_satisfaction"]),
                           fontsize=7, color="blue", alpha=0.6)
        z = np.polyfit(mean_feat, life_sat, 1)
        x_line = np.linspace(mean_feat.min(), mean_feat.max(), 100)
        ax.plot(x_line, np.polyval(z, x_line), "r--", alpha=0.5)
        ax.set_xlabel("Mean Platform Feature Score (design harmfulness)")
        ax.set_ylabel("PISA 2022 Life Satisfaction (0-10)")
        ax.set_title(f"Platform Design vs Teen Wellbeing (N={len(country_data)} countries)\n"
                     f"r = {r_mf:+.3f}, p = {p_mf:.4f}")
        ax.text(0.05, 0.05, "Red = English-speaking\nBlue = Western Europe",
                transform=ax.transAxes, fontsize=8)

        # Panel B: O-exposure vs life satisfaction
        ax = axes[1]
        ax.scatter(o_exp, life_sat, c="coral", alpha=0.7, s=40)
        z2 = np.polyfit(o_exp, life_sat, 1)
        x_line2 = np.linspace(o_exp.min(), o_exp.max(), 100)
        ax.plot(x_line2, np.polyval(z2, x_line2), "r--", alpha=0.5)
        ax.set_xlabel("Opacity-Weighted Exposure (O-features × market share)")
        ax.set_ylabel("PISA 2022 Life Satisfaction (0-10)")
        ax.set_title(f"Opacity Exposure vs Teen Wellbeing\n"
                     f"r = {r_o:+.3f}, p = {p_o:.4f}")

        plt.tight_layout()
        fig_path = Path(__file__).parent / "pisa_cross_national_scatter.png"
        plt.savefig(fig_path, dpi=150, bbox_inches="tight")
        print(f"  Figure saved to {fig_path}")
        plt.close()
    except Exception as e:
        print(f"  [WARN] Figure generation failed: {e}")

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
