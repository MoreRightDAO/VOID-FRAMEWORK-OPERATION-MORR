#!/usr/bin/env python3
"""
PISA 2022 Microdata Analysis — Feature-Weighted Dose-Response
==============================================================
Uses extracted PISA data (country means, gender splits, dose-response)
merged with Paper 166 feature scores to test:

1. Within-country dose-response: SM hours → life satisfaction
2. Gender gap in dose-response (girls vs boys)
3. Whether countries with higher-feature platform mixes show steeper dose-response
4. Feature-weighted exposure vs country-level wellbeing (microdata-derived)
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).parent

# Load extracted data
country_df = pd.read_csv(SCRIPT_DIR / "pisa_country_means.csv")
gender_df = pd.read_csv(SCRIPT_DIR / "pisa_gender_means.csv")
dose_df = pd.read_csv(SCRIPT_DIR / "pisa_dose_response.csv")

# Load feature scores from our cross-national analysis
with open(SCRIPT_DIR / "pisa_cross_national_results.json") as f:
    cross_data = json.load(f)

# Map ISO3 → ISO2 for merging with StatCounter data
ISO3_TO_ISO2 = {
    "AUS": "AU", "AUT": "AT", "BEL": "BE", "BRA": "BR", "BGR": "BG",
    "CAN": "CA", "CHL": "CL", "COL": "CO", "CRI": "CR", "HRV": "HR",
    "CZE": "CZ", "DNK": "DK", "EST": "EE", "FIN": "FI", "FRA": "FR",
    "DEU": "DE", "GRC": "GR", "HUN": "HU", "ISL": "IS", "IDN": "ID",
    "IRL": "IE", "ISR": "IL", "ITA": "IT", "JPN": "JP", "KOR": "KR",
    "LVA": "LV", "LTU": "LT", "MYS": "MY", "MEX": "MX", "NLD": "NL",
    "NZL": "NZ", "NOR": "NO", "PER": "PE", "PHL": "PH", "POL": "PL",
    "PRT": "PT", "ROU": "RO", "SRB": "RS", "SGP": "SG", "SVK": "SK",
    "SVN": "SI", "ESP": "ES", "SWE": "SE", "CHE": "CH", "TUR": "TR",
    "GBR": "GB", "USA": "US", "URY": "UY", "VNM": "VN", "THA": "TH",
}

# Build feature score lookup from cross-national data
feature_lookup = {}
for c in cross_data["countries"]:
    feature_lookup[c["code"]] = {
        "mean_features": c["mean_features_per_share"],
        "o_exposure": c["o_exposure"],
        "feature_exposure": c["feature_exposure"],
    }

print("=" * 70)
print("PISA 2022 MICRODATA ANALYSIS — 613,744 Students")
print("=" * 70)

# ─── 1. GLOBAL DOSE-RESPONSE ────────────────────────────────────────────────
print("\n--- 1. GLOBAL DOSE-RESPONSE (all countries pooled) ---\n")

# Aggregate dose-response across all countries
dose_agg = dose_df.groupby(["sm_category", "sm_code"]).agg(
    mean_ls=("life_satisfaction_mean", "mean"),
    n_total=("n", "sum"),
    n_countries=("n", "count"),
).reset_index().sort_values("sm_code")

print("  SM Category    | Life Satisfaction | N students | N countries")
print("  " + "-" * 65)
for _, r in dose_agg.iterrows():
    print(f"  {r['sm_category']:15s} | {r['mean_ls']:17.3f} | {r['n_total']:10,.0f} | {r['n_countries']:11.0f}")

# Dose-response slope
dose_codes = dose_agg["sm_code"].values
dose_ls = dose_agg["mean_ls"].values
slope, intercept, r_dose, p_dose, se_dose = stats.linregress(dose_codes, dose_ls)
print(f"\n  Linear dose-response: slope = {slope:.4f} LS/category, r = {r_dose:.4f}, p = {p_dose:.6f}")
print(f"  ↳ Each step up in SM use (~2hr) → {slope:.3f} points lower life satisfaction")

# ─── 2. GENDER-STRATIFIED DOSE-RESPONSE ─────────────────────────────────────
print("\n--- 2. GENDER-STRATIFIED DOSE-RESPONSE ---\n")

for gender in ["female", "male"]:
    g_dose = dose_df[dose_df["gender"] == gender]
    g_agg = g_dose.groupby(["sm_category", "sm_code"]).agg(
        mean_ls=("life_satisfaction_mean", "mean"),
        n_total=("n", "sum"),
    ).reset_index().sort_values("sm_code")

    codes = g_agg["sm_code"].values
    ls_vals = g_agg["mean_ls"].values
    sl, _, r_g, p_g, _ = stats.linregress(codes, ls_vals)

    print(f"  {gender.upper():7s}: slope = {sl:.4f}, r = {r_g:.4f}, p = {p_g:.6f}")
    print(f"    None: {ls_vals[0]:.2f} → >7hr: {ls_vals[-1]:.2f} (Δ = {ls_vals[-1]-ls_vals[0]:+.2f})")

# ─── 3. COUNTRY-LEVEL: SM HOURS (MICRODATA) vs LIFE SAT ─────────────────────
print("\n--- 3. MICRODATA-DERIVED COUNTRY MEANS ---\n")

valid = country_df.dropna(subset=["sm_weekday_hours_mean", "life_satisfaction_mean"])
print(f"  Countries with both SM + life sat: {len(valid)}")

r_raw, p_raw = stats.pearsonr(valid["sm_weekday_hours_mean"], valid["life_satisfaction_mean"])
print(f"  SM hours vs Life Sat: r = {r_raw:+.4f} (p = {p_raw:.4f})")

# ─── 4. MERGE WITH FEATURE SCORES ───────────────────────────────────────────
print("\n--- 4. FEATURE-WEIGHTED ANALYSIS (merged with StatCounter) ---\n")

valid["iso2"] = valid["country_code"].map(ISO3_TO_ISO2)
valid = valid.dropna(subset=["iso2"])

merged = []
for _, row in valid.iterrows():
    iso2 = row["iso2"]
    if iso2 in feature_lookup:
        merged.append({
            "country": row["country_code"],
            "iso2": iso2,
            "life_sat": row["life_satisfaction_mean"],
            "sm_hours": row["sm_weekday_hours_mean"],
            "mean_features": feature_lookup[iso2]["mean_features"],
            "o_exposure": feature_lookup[iso2]["o_exposure"],
        })

merged_df = pd.DataFrame(merged)
print(f"  Countries with features + microdata: {len(merged_df)}")

if len(merged_df) >= 10:
    r_feat, p_feat = stats.pearsonr(merged_df["mean_features"], merged_df["life_sat"])
    r_o, p_o = stats.pearsonr(merged_df["o_exposure"], merged_df["life_sat"])
    rho_feat, prho_feat = stats.spearmanr(merged_df["mean_features"], merged_df["life_sat"])

    print(f"\n  Mean features vs Life Sat (microdata):  r = {r_feat:+.4f} (p = {p_feat:.4f})")
    print(f"  O-exposure vs Life Sat (microdata):     r = {r_o:+.4f} (p = {p_o:.4f})")
    print(f"  Spearman features vs Life Sat:          ρ = {rho_feat:+.4f} (p = {prho_feat:.4f})")

    # Multiple regression: features + SM hours → life sat
    from numpy.linalg import lstsq
    X = np.column_stack([
        merged_df["mean_features"].values,
        merged_df["sm_hours"].values,
        np.ones(len(merged_df)),
    ])
    y = merged_df["life_sat"].values
    beta, residuals, _, _ = lstsq(X, y, rcond=None)
    y_pred = X @ beta
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - y.mean())**2)
    R2 = 1 - ss_res / ss_tot

    print(f"\n  Multiple regression: features + SM hours → life sat")
    print(f"    β(features) = {beta[0]:+.4f}")
    print(f"    β(SM hours) = {beta[1]:+.4f}")
    print(f"    R² = {R2:.4f}")

# ─── 5. WITHIN-COUNTRY DOSE-RESPONSE SLOPES ─────────────────────────────────
print("\n--- 5. WITHIN-COUNTRY DOSE-RESPONSE SLOPES ---\n")

country_slopes = []
for cnt in dose_df["country_code"].unique():
    c_dose = dose_df[dose_df["country_code"] == cnt]
    # Pool genders
    c_agg = c_dose.groupby("sm_code").agg(
        mean_ls=("life_satisfaction_mean", "mean"),
        n_total=("n", "sum"),
    ).reset_index()
    if len(c_agg) >= 4:
        sl, _, r_c, p_c, _ = stats.linregress(c_agg["sm_code"], c_agg["mean_ls"])
        iso2 = ISO3_TO_ISO2.get(cnt, "")
        feat = feature_lookup.get(iso2, {}).get("mean_features", np.nan)
        country_slopes.append({
            "country": cnt, "iso2": iso2,
            "slope": sl, "r": r_c, "p": p_c,
            "mean_features": feat,
            "n_total": c_agg["n_total"].sum(),
        })

slopes_df = pd.DataFrame(country_slopes)
print(f"  Countries with dose-response slopes: {len(slopes_df)}")
neg_slopes = (slopes_df["slope"] < 0).sum()
print(f"  Countries with NEGATIVE slope (more SM → worse LS): {neg_slopes}/{len(slopes_df)} ({100*neg_slopes/len(slopes_df):.0f}%)")
print(f"  Mean slope: {slopes_df['slope'].mean():.4f}")
print(f"  Median slope: {slopes_df['slope'].median():.4f}")

# Worst 10 slopes
print(f"\n  Steepest negative dose-response (most harmed by SM):")
worst = slopes_df.nsmallest(10, "slope")
for _, r in worst.iterrows():
    print(f"    {r['country']:5s} slope={r['slope']:+.4f} r={r['r']:+.3f} feat={r['mean_features']:.1f}")

print(f"\n  Flattest/positive dose-response:")
best = slopes_df.nlargest(5, "slope")
for _, r in best.iterrows():
    print(f"    {r['country']:5s} slope={r['slope']:+.4f} r={r['r']:+.3f} feat={r['mean_features']:.1f}")

# ─── 6. KEY TEST: Do higher-feature countries show steeper dose-response? ────
print("\n--- 6. CRITICAL TEST: Feature score predicts dose-response slope ---\n")

valid_slopes = slopes_df.dropna(subset=["mean_features"])
if len(valid_slopes) >= 10:
    r_slope_feat, p_slope_feat = stats.pearsonr(valid_slopes["mean_features"], valid_slopes["slope"])
    rho_slope_feat, prho_slope_feat = stats.spearmanr(valid_slopes["mean_features"], valid_slopes["slope"])
    print(f"  N = {len(valid_slopes)} countries")
    print(f"  Feature score vs dose-response slope:")
    print(f"    Pearson r  = {r_slope_feat:+.4f} (p = {p_slope_feat:.4f})")
    print(f"    Spearman ρ = {rho_slope_feat:+.4f} (p = {prho_slope_feat:.4f})")
    print(f"  ↳ {'CONFIRMED' if r_slope_feat < 0 and p_slope_feat < 0.05 else 'NOT CONFIRMED'}: higher-feature platform mixes → steeper negative dose-response")

# ─── 7. GENDER GAP BY COUNTRY ───────────────────────────────────────────────
print("\n--- 7. GENDER GAP IN DOSE-RESPONSE ---\n")

gender_slopes = []
for (cnt, gender), grp in dose_df.groupby(["country_code", "gender"]):
    agg = grp.groupby("sm_code").agg(mean_ls=("life_satisfaction_mean", "mean")).reset_index()
    if len(agg) >= 4:
        sl, _, r_g, p_g, _ = stats.linregress(agg["sm_code"], agg["mean_ls"])
        gender_slopes.append({"country": cnt, "gender": gender, "slope": sl, "r": r_g})

gender_slopes_df = pd.DataFrame(gender_slopes)
f_slopes = gender_slopes_df[gender_slopes_df["gender"] == "female"]["slope"].values
m_slopes = gender_slopes_df[gender_slopes_df["gender"] == "male"]["slope"].values

print(f"  Female mean dose-response slope: {f_slopes.mean():.4f}")
print(f"  Male mean dose-response slope:   {m_slopes.mean():.4f}")
print(f"  Ratio (female/male): {f_slopes.mean()/m_slopes.mean():.2f}×")

# Paired comparison by country
f_by_cnt = gender_slopes_df[gender_slopes_df["gender"] == "female"].set_index("country")["slope"]
m_by_cnt = gender_slopes_df[gender_slopes_df["gender"] == "male"].set_index("country")["slope"]
common = f_by_cnt.index.intersection(m_by_cnt.index)
if len(common) >= 5:
    t_stat, t_p = stats.ttest_rel(f_by_cnt[common], m_by_cnt[common])
    print(f"  Paired t-test (N={len(common)} countries): t = {t_stat:.3f}, p = {t_p:.6f}")
    pct_worse = (f_by_cnt[common] < m_by_cnt[common]).mean()
    print(f"  % countries where girls' slope is steeper (more negative): {100*pct_worse:.0f}%")

# ─── FIGURES ─────────────────────────────────────────────────────────────────
print("\n--- Generating figures ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Panel A: Global dose-response by gender
ax = axes[0, 0]
for gender, color, marker in [("female", "coral", "o"), ("male", "steelblue", "s")]:
    g_dose = dose_df[dose_df["gender"] == gender]
    g_agg = g_dose.groupby(["sm_category", "sm_code"]).agg(
        mean_ls=("life_satisfaction_mean", "mean"),
        se_ls=("life_satisfaction_mean", "sem"),
    ).reset_index().sort_values("sm_code")
    ax.errorbar(g_agg["sm_code"], g_agg["mean_ls"], yerr=g_agg["se_ls"],
               fmt=f"-{marker}", color=color, label=gender.capitalize(),
               capsize=3, markersize=6, linewidth=2)

ax.set_xticks([1, 2, 3, 4, 5, 6])
ax.set_xticklabels(["None", "<1hr", "1-3hr", "3-5hr", "5-7hr", ">7hr"], fontsize=8)
ax.set_xlabel("Social Media Use (weekday)", fontsize=10)
ax.set_ylabel("Life Satisfaction (0-10)", fontsize=10)
ax.set_title("A. PISA 2022 Dose-Response: SM Use → Life Satisfaction\n(N=613K students, 47 countries)", fontsize=11)
ax.legend(fontsize=9)
ax.grid(alpha=0.3)

# Panel B: Dose-response slopes distribution
ax = axes[0, 1]
ax.hist(slopes_df["slope"], bins=20, color="steelblue", alpha=0.7, edgecolor="white")
ax.axvline(0, color="red", linewidth=1.5, linestyle="--")
ax.axvline(slopes_df["slope"].mean(), color="black", linewidth=1.5, label=f"Mean = {slopes_df['slope'].mean():.3f}")
ax.set_xlabel("Dose-Response Slope (ΔLS per SM category)", fontsize=10)
ax.set_ylabel("Number of Countries", fontsize=10)
ax.set_title(f"B. Distribution of Country-Level Dose-Response Slopes\n({neg_slopes}/{len(slopes_df)} countries show negative slope)", fontsize=11)
ax.legend(fontsize=9)

# Panel C: Feature score vs dose-response slope
ax = axes[1, 0]
if len(valid_slopes) >= 10:
    ax.scatter(valid_slopes["mean_features"], valid_slopes["slope"],
              c="steelblue", s=50, alpha=0.7, edgecolors="white", linewidths=0.5, zorder=3)
    for _, r in valid_slopes.iterrows():
        if abs(r["slope"]) > 0.15 or r["mean_features"] < 12.2 or r["mean_features"] > 13.2:
            ax.annotate(r["country"], (r["mean_features"], r["slope"]),
                       fontsize=6.5, alpha=0.7)
    z = np.polyfit(valid_slopes["mean_features"], valid_slopes["slope"], 1)
    x_line = np.linspace(valid_slopes["mean_features"].min(), valid_slopes["mean_features"].max(), 100)
    ax.plot(x_line, np.polyval(z, x_line), "r--", alpha=0.5, linewidth=1.5)
    ax.set_xlabel("Mean Platform Feature Score (from StatCounter)", fontsize=10)
    ax.set_ylabel("Dose-Response Slope (ΔLS per SM category)", fontsize=10)
    ax.set_title(f"C. Platform Design vs SM Harm Gradient\nr = {r_slope_feat:.3f}, p = {p_slope_feat:.4f}", fontsize=11)
    ax.axhline(0, color="gray", linewidth=0.5)

# Panel D: Gender gap by country
ax = axes[1, 1]
if len(common) >= 5:
    gap = f_by_cnt[common] - m_by_cnt[common]
    gap_sorted = gap.sort_values()
    colors = ["coral" if g < 0 else "steelblue" for g in gap_sorted]
    ax.barh(range(len(gap_sorted)), gap_sorted.values, color=colors, alpha=0.7)
    ax.set_yticks(range(len(gap_sorted)))
    ax.set_yticklabels(gap_sorted.index, fontsize=5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_xlabel("Gender Gap in Slope (female − male)", fontsize=10)
    ax.set_title(f"D. Gender Gap: Girls More Harmed in {100*pct_worse:.0f}% of Countries", fontsize=11)
    ax.text(0.05, 0.95, "← Girls more harmed", transform=ax.transAxes, fontsize=8, va="top", color="coral")
    ax.text(0.95, 0.95, "Boys more harmed →", transform=ax.transAxes, fontsize=8, va="top", ha="right", color="steelblue")

plt.tight_layout(pad=2.0)
fig_path = SCRIPT_DIR / "pisa_microdata_4panel.png"
plt.savefig(fig_path, dpi=150, bbox_inches="tight")
print(f"  Saved to {fig_path}")
plt.close()

# ─── SUMMARY ─────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
  DATASET: PISA 2022, 613,744 students, 80 countries
  ICT data: 323,794 students in 52 countries
  SM + Life satisfaction: 47 countries

  DOSE-RESPONSE:
    Each SM category step (~2hr) → {slope:.3f} points lower life satisfaction
    {neg_slopes}/{len(slopes_df)} countries ({100*neg_slopes/len(slopes_df):.0f}%) show negative dose-response

  GENDER:
    Female slope: {f_slopes.mean():.4f} (steeper)
    Male slope:   {m_slopes.mean():.4f}
    Girls more harmed in {100*pct_worse:.0f}% of countries (p = {t_p:.6f})

  FEATURE-WEIGHTED:
    Feature score vs dose-response slope: r = {r_slope_feat:+.3f} (p = {p_slope_feat:.4f})
""")

# Save results
results = {
    "n_students": 613744,
    "n_countries_ict": 52,
    "n_countries_sm_ls": 47,
    "dose_response_slope": float(slope),
    "dose_response_r": float(r_dose),
    "dose_response_p": float(p_dose),
    "female_slope": float(f_slopes.mean()),
    "male_slope": float(m_slopes.mean()),
    "pct_countries_negative_slope": float(100 * neg_slopes / len(slopes_df)),
    "gender_ttest_p": float(t_p),
    "feature_vs_slope_r": float(r_slope_feat),
    "feature_vs_slope_p": float(p_slope_feat),
}
with open(SCRIPT_DIR / "pisa_microdata_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Done.")
