#!/usr/bin/env python3
"""
Protocol A: YRBS Mental Health Trends × Platform Pe Over Time
=============================================================
Tests whether population-weighted Pe exposure predicts adolescent mental
health decline better than raw social media adoption rate.

Data sources:
  - CDC YRBS published trend data (2011-2023, biennial)
  - Pew Research teen social media adoption rates
  - Platform design change timeline → reconstructed Pe per platform per year

Pe formula: Pe = 16 * sinh(2 * (0.867 - c * 2.244)), c = 1 - V/9, V = O + R + α
"""

import math
import numpy as np
from scipy import stats

# ─── Pe computation (from scoring-constants.js) ──────────────────────────

B_A = 0.867   # drift bias (empirical; see math apparatus §208 caveat)
B_G = math.pi / math.sqrt(2)   # constraint bias (canonical; math apparatus §165)
K   = 16      # hardware parameter

def pe(O, R, alpha):
    """Compute Pe from O/R/α scores (each 0-3)."""
    V = O + R + alpha
    c = 1 - V / 9
    b = B_A - c * B_G
    return K * math.sinh(2 * b)

# ─── Platform Pe reconstruction per year ─────────────────────────────────
# Each platform scored with (O, R, α) based on documented design features
# that year. Scores reflect CUMULATIVE design — features don't get removed.
#
# Scoring rationale documented in research-social-media-litigation-pe.md §3

PLATFORM_PE = {
    # Facebook
    'facebook': {
        2011: pe(1.5, 1.5, 2.0),  # Algorithmic News Feed + Sponsored Stories, strong social graph
        2013: pe(2.0, 2.0, 2.5),  # Deeper algo, more ads in feed, identity coupling
        2015: pe(2.0, 2.5, 2.5),  # Engagement optimization, video priority
        2017: pe(2.5, 2.5, 2.5),  # Reactions, Live, deeper algo
        2019: pe(2.5, 2.5, 2.5),  # "Friends & family" but still engagement-optimized
        2021: pe(2.5, 3.0, 2.5),  # Reels-style content, Marketplace coupling
        2023: pe(2.5, 3.0, 2.5),  # AI-recommended content dominant
    },
    # Instagram
    'instagram': {
        2011: pe(0.5, 1.0, 1.5),  # Chronological photo feed, simple, mild coupling
        2013: pe(0.5, 1.5, 2.0),  # Video added, growing identity investment
        2015: pe(1.0, 2.0, 2.5),  # Pre-algorithm but explore tab, strong identity coupling
        2017: pe(2.5, 2.5, 3.0),  # Algorithmic feed (2016) + Stories (2016-08), full identity coupling
        2019: pe(3.0, 3.0, 3.0),  # Explore algo, beauty filters, creator monetization → structural D3
        2021: pe(3.0, 3.0, 3.0),  # Reels, full TikTok-style algo
        2023: pe(3.0, 3.0, 3.0),  # Video-first, AI recommendations dominant
    },
    # YouTube
    'youtube': {
        2011: pe(1.0, 1.0, 1.0),  # Pre-watch-time algorithm, user-selected
        2013: pe(2.0, 2.0, 1.5),  # Watch time algorithm (2012), recommended sidebar
        2015: pe(2.0, 2.5, 1.5),  # Autoplay ON by default (2015-03)
        2017: pe(2.5, 2.5, 2.0),  # Deeper recommendation, creator economy growing
        2019: pe(2.5, 3.0, 2.0),  # Smart autoplay, aggressive recommendations
        2021: pe(3.0, 3.0, 2.5),  # Shorts launched (2021-07), full algo feed
        2023: pe(3.0, 3.0, 2.5),  # Shorts dominant, AI recommendations
    },
    # TikTok (international presence from 2018)
    'tiktok': {
        2011: pe(0, 0, 0),        # Does not exist
        2013: pe(0, 0, 0),        # Does not exist
        2015: pe(0, 0, 0),        # Does not exist (Musical.ly exists but tiny)
        2017: pe(3.0, 3.0, 2.0),  # Launched Sep 2017, FYP algo from day 1, low coupling (new)
        2019: pe(3.0, 3.0, 3.0),  # Post-Musical.ly merger, massive adoption, creator economy
        2021: pe(3.0, 3.0, 3.0),  # Dominant, structural D3
        2023: pe(3.0, 3.0, 3.0),  # Structural D3
    },
    # Snapchat
    'snapchat': {
        2011: pe(0, 0, 0),        # Launched late 2011, negligible
        2013: pe(1.5, 2.0, 2.0),  # Stories launched Oct 2013, ephemeral = high R, social coupling
        2015: pe(2.0, 2.0, 2.5),  # Discover tab, growing coupling
        2017: pe(2.0, 2.5, 2.5),  # Algorithmic Discover, streak mechanics
        2019: pe(2.0, 2.5, 2.5),  # Stable
        2021: pe(2.5, 3.0, 2.5),  # Spotlight launched (2020-11), TikTok-style algo
        2023: pe(2.5, 3.0, 2.5),  # My AI chatbot, deeper engagement
    },
}

# ─── Teen adoption rates by platform (% of US teens 13-17) ──────────────
# Sources: Pew Research Center surveys (2012, 2014-15, 2018, 2021, 2022-23)
# Interpolated for YRBS years where Pew didn't survey

TEEN_ADOPTION = {
    'facebook':  {2011: 0.77, 2013: 0.71, 2015: 0.51, 2017: 0.51, 2019: 0.32, 2021: 0.27, 2023: 0.23},
    'instagram': {2011: 0.01, 2013: 0.11, 2015: 0.52, 2017: 0.72, 2019: 0.72, 2021: 0.62, 2023: 0.59},
    'youtube':   {2011: 0.60, 2013: 0.70, 2015: 0.75, 2017: 0.85, 2019: 0.85, 2021: 0.95, 2023: 0.93},
    'tiktok':    {2011: 0.00, 2013: 0.00, 2015: 0.00, 2017: 0.05, 2019: 0.25, 2021: 0.67, 2023: 0.63},
    'snapchat':  {2011: 0.00, 2013: 0.02, 2015: 0.41, 2017: 0.69, 2019: 0.69, 2021: 0.59, 2023: 0.51},
}

# ─── CDC YRBS published data ─────────────────────────────────────────────
# % of students reporting persistent feelings of sadness or hopelessness
# Source: CDC YRBS Data Summary & Trends Report 2013-2023 + 2011-2021

YRBS_YEARS = [2011, 2013, 2015, 2017, 2019, 2021, 2023]

# Persistent sadness/hopelessness (% of all students)
YRBS_SADNESS = {
    2011: 28.5,
    2013: 29.9,
    2015: 29.9,
    2017: 31.5,
    2019: 36.7,
    2021: 42.0,
    2023: 40.0,
}

# Seriously considered attempting suicide (% of all students)
YRBS_SUICIDE_CONSIDER = {
    2011: 15.8,
    2013: 17.0,
    2015: 17.7,
    2017: 17.2,
    2019: 18.8,
    2021: 22.0,
    2023: 20.4,
}

# Female students persistent sadness/hopelessness (stronger signal)
YRBS_SADNESS_FEMALE = {
    2011: 35.9,
    2013: 39.1,
    2015: 39.8,
    2017: 41.1,
    2019: 46.6,
    2021: 57.0,
    2023: 53.0,
}


# ═══════════════════════════════════════════════════════════════════════════
# ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 72)
print("PROTOCOL A: YRBS Mental Health × Platform Pe Over Time")
print("=" * 72)

# ─── Step 1: Compute Pe exposure per year ─────────────────────────────────
# Pe_exposure(year) = Σ over platforms of (adoption_rate × Pe(platform, year))

pe_exposure = {}
raw_adoption = {}  # total social media adoption (unweighted)

print("\n─── Platform Pe Scores by Year ───\n")
print(f"{'Year':>6}  {'Facebook':>10}  {'Instagram':>10}  {'YouTube':>10}  {'TikTok':>10}  {'Snapchat':>10}")
for year in YRBS_YEARS:
    vals = []
    for p in ['facebook', 'instagram', 'youtube', 'tiktok', 'snapchat']:
        v = PLATFORM_PE[p][year]
        vals.append(v)
    print(f"{year:>6}  {vals[0]:>10.2f}  {vals[1]:>10.2f}  {vals[2]:>10.2f}  {vals[3]:>10.2f}  {vals[4]:>10.2f}")

print("\n─── Teen Adoption Rates by Year (%) ───\n")
print(f"{'Year':>6}  {'Facebook':>10}  {'Instagram':>10}  {'YouTube':>10}  {'TikTok':>10}  {'Snapchat':>10}  {'Total':>10}")
for year in YRBS_YEARS:
    total = 0
    vals = []
    for p in ['facebook', 'instagram', 'youtube', 'tiktok', 'snapchat']:
        a = TEEN_ADOPTION[p][year]
        vals.append(a * 100)
        total += a
    raw_adoption[year] = total
    print(f"{year:>6}  {vals[0]:>9.0f}%  {vals[1]:>9.0f}%  {vals[2]:>9.0f}%  {vals[3]:>9.0f}%  {vals[4]:>9.0f}%  {total*100:>9.0f}%")

print("\n─── Population-Weighted Pe Exposure ───\n")
print(f"{'Year':>6}  {'Pe_exposure':>12}  {'Raw_adoption':>14}  {'Sadness%':>10}  {'Suicide%':>10}  {'Female_sad%':>12}")
for year in YRBS_YEARS:
    pe_exp = 0
    for p in ['facebook', 'instagram', 'youtube', 'tiktok', 'snapchat']:
        pe_exp += TEEN_ADOPTION[p][year] * PLATFORM_PE[p][year]
    pe_exposure[year] = pe_exp
    print(f"{year:>6}  {pe_exp:>12.2f}  {raw_adoption[year]:>14.2f}  {YRBS_SADNESS[year]:>9.1f}%  {YRBS_SUICIDE_CONSIDER[year]:>9.1f}%  {YRBS_SADNESS_FEMALE[year]:>11.1f}%")


# ─── Step 2: Correlation analysis ─────────────────────────────────────────

years = np.array(YRBS_YEARS)
pe_exp_arr = np.array([pe_exposure[y] for y in YRBS_YEARS])
raw_adopt_arr = np.array([raw_adoption[y] for y in YRBS_YEARS])
sadness_arr = np.array([YRBS_SADNESS[y] for y in YRBS_YEARS])
suicide_arr = np.array([YRBS_SUICIDE_CONSIDER[y] for y in YRBS_YEARS])
female_sad_arr = np.array([YRBS_SADNESS_FEMALE[y] for y in YRBS_YEARS])

print("\n" + "=" * 72)
print("CORRELATION RESULTS")
print("=" * 72)

for outcome_name, outcome_arr in [
    ("Persistent sadness/hopelessness (all)", sadness_arr),
    ("Seriously considered suicide (all)", suicide_arr),
    ("Persistent sadness (female)", female_sad_arr),
]:
    print(f"\n─── {outcome_name} ───\n")

    # Pe exposure vs outcome
    r_pe, p_pe = stats.pearsonr(pe_exp_arr, outcome_arr)
    rho_pe, sp_pe = stats.spearmanr(pe_exp_arr, outcome_arr)

    # Raw adoption vs outcome
    r_raw, p_raw = stats.pearsonr(raw_adopt_arr, outcome_arr)
    rho_raw, sp_raw = stats.spearmanr(raw_adopt_arr, outcome_arr)

    # Year (time trend) vs outcome
    r_year, p_year = stats.pearsonr(years.astype(float), outcome_arr)

    print(f"  Pe_exposure  vs outcome:  r = {r_pe:+.4f}  (p = {p_pe:.4f})   ρ = {rho_pe:+.4f}  (p = {sp_pe:.4f})   R² = {r_pe**2:.4f}")
    print(f"  Raw_adoption vs outcome:  r = {r_raw:+.4f}  (p = {p_raw:.4f})   ρ = {rho_raw:+.4f}  (p = {sp_raw:.4f})   R² = {r_raw**2:.4f}")
    print(f"  Year (trend) vs outcome:  r = {r_year:+.4f}  (p = {p_year:.4f})   R² = {r_year**2:.4f}")
    print(f"  ΔR² (Pe vs raw adoption):  {r_pe**2 - r_raw**2:+.4f}")
    print(f"  ΔR² (Pe vs year trend):    {r_pe**2 - r_year**2:+.4f}")

# ─── Step 3: Regression — does Pe explain variance beyond raw adoption? ──

print("\n" + "=" * 72)
print("REGRESSION: Pe_exposure vs Raw_adoption as predictors of sadness")
print("=" * 72)

# Simple OLS: sadness ~ Pe_exposure
slope_pe, intercept_pe, r_pe, p_pe, se_pe = stats.linregress(pe_exp_arr, sadness_arr)
print(f"\n  Model 1: sadness ~ Pe_exposure")
print(f"    slope = {slope_pe:.4f}  intercept = {intercept_pe:.2f}  R² = {r_pe**2:.4f}  p = {p_pe:.4f}")

# Simple OLS: sadness ~ raw_adoption
slope_raw, intercept_raw, r_raw, p_raw, se_raw = stats.linregress(raw_adopt_arr, sadness_arr)
print(f"\n  Model 2: sadness ~ raw_adoption")
print(f"    slope = {slope_raw:.4f}  intercept = {intercept_raw:.2f}  R² = {r_raw**2:.4f}  p = {p_raw:.4f}")

# Multiple regression: sadness ~ Pe_exposure + raw_adoption
# Using numpy for simple 2-variable OLS
X = np.column_stack([np.ones(len(YRBS_YEARS)), pe_exp_arr, raw_adopt_arr])
beta, residuals, rank, sv = np.linalg.lstsq(X, sadness_arr, rcond=None)
y_pred = X @ beta
ss_res = np.sum((sadness_arr - y_pred)**2)
ss_tot = np.sum((sadness_arr - np.mean(sadness_arr))**2)
r2_multi = 1 - ss_res / ss_tot if ss_tot > 0 else 0

print(f"\n  Model 3: sadness ~ Pe_exposure + raw_adoption")
print(f"    β_intercept = {beta[0]:.2f}  β_Pe = {beta[1]:.4f}  β_raw = {beta[2]:.4f}  R² = {r2_multi:.4f}")
print(f"    ΔR² vs Pe alone:  {r2_multi - r_pe**2:+.4f}")
print(f"    ΔR² vs raw alone: {r2_multi - r_raw**2:+.4f}")

# ─── Step 4: Partial correlation — Pe controlling for raw adoption ────────

print("\n" + "=" * 72)
print("PARTIAL CORRELATIONS")
print("=" * 72)

def partial_corr(x, y, z):
    """Partial correlation of x and y controlling for z."""
    # Residualize x on z
    slope_xz, intercept_xz, _, _, _ = stats.linregress(z, x)
    x_resid = x - (slope_xz * z + intercept_xz)
    # Residualize y on z
    slope_yz, intercept_yz, _, _, _ = stats.linregress(z, y)
    y_resid = y - (slope_yz * z + intercept_yz)
    return stats.pearsonr(x_resid, y_resid)

for outcome_name, outcome_arr in [
    ("Sadness (all)", sadness_arr),
    ("Suicide consideration (all)", suicide_arr),
    ("Sadness (female)", female_sad_arr),
]:
    r_partial, p_partial = partial_corr(pe_exp_arr, outcome_arr, raw_adopt_arr)
    r_partial_rev, p_partial_rev = partial_corr(raw_adopt_arr, outcome_arr, pe_exp_arr)
    print(f"\n  {outcome_name}:")
    print(f"    Pe | controlling for raw adoption:        r_partial = {r_partial:+.4f}  (p = {p_partial:.4f})")
    print(f"    Raw adoption | controlling for Pe:        r_partial = {r_partial_rev:+.4f}  (p = {p_partial_rev:.4f})")

# ─── Step 5: Key platform Pe inflection analysis ─────────────────────────

print("\n" + "=" * 72)
print("PE INFLECTION ANALYSIS")
print("=" * 72)

print("\n  Instagram Pe trajectory (the key platform in the trial):")
for year in YRBS_YEARS:
    pe_val = PLATFORM_PE['instagram'][year]
    adopt = TEEN_ADOPTION['instagram'][year]
    contribution = pe_val * adopt
    print(f"    {year}: Pe = {pe_val:>6.2f}  ×  adoption = {adopt:.0%}  →  contribution = {contribution:>6.2f}")

print(f"\n  Instagram Pe JUMP 2015→2017 (algorithmic feed + Stories):")
print(f"    Pe: {PLATFORM_PE['instagram'][2015]:.2f} → {PLATFORM_PE['instagram'][2017]:.2f}  (Δ = {PLATFORM_PE['instagram'][2017] - PLATFORM_PE['instagram'][2015]:+.2f})")
print(f"    Adoption: {TEEN_ADOPTION['instagram'][2015]:.0%} → {TEEN_ADOPTION['instagram'][2017]:.0%}")
print(f"    Pe contribution: {PLATFORM_PE['instagram'][2015]*TEEN_ADOPTION['instagram'][2015]:.2f} → {PLATFORM_PE['instagram'][2017]*TEEN_ADOPTION['instagram'][2017]:.2f}  ({(PLATFORM_PE['instagram'][2017]*TEEN_ADOPTION['instagram'][2017])/(PLATFORM_PE['instagram'][2015]*TEEN_ADOPTION['instagram'][2015]):.1f}× increase)")
print(f"    YRBS sadness: {YRBS_SADNESS[2015]}% → {YRBS_SADNESS[2017]}% → {YRBS_SADNESS[2019]}% (accelerating)")

print("\n  TikTok arrival impact (2017→2019→2021):")
for year in [2017, 2019, 2021]:
    pe_val = PLATFORM_PE['tiktok'][year]
    adopt = TEEN_ADOPTION['tiktok'][year]
    contribution = pe_val * adopt
    print(f"    {year}: Pe = {pe_val:>6.2f}  ×  adoption = {adopt:.0%}  →  contribution = {contribution:>6.2f}")

# ─── Summary ──────────────────────────────────────────────────────────────

print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)

r_pe_sad, _ = stats.pearsonr(pe_exp_arr, sadness_arr)
r_raw_sad, _ = stats.pearsonr(raw_adopt_arr, sadness_arr)
r_year_sad, _ = stats.pearsonr(years.astype(float), sadness_arr)

print(f"""
  Pe_exposure predicts adolescent sadness:
    R² = {r_pe_sad**2:.4f}  (Pe exposure)
    R² = {r_raw_sad**2:.4f}  (raw adoption — unweighted)
    R² = {r_year_sad**2:.4f}  (year — simple time trend)

  ΔR² (Pe vs raw adoption) = {r_pe_sad**2 - r_raw_sad**2:+.4f}
  ΔR² (Pe vs year trend)   = {r_pe_sad**2 - r_year_sad**2:+.4f}
""")

KILL = r_pe_sad**2 - r_raw_sad**2
if KILL <= 0:
    print("  ⚠ KILL CONDITION FIRED: Pe does NOT outperform raw adoption rate.")
    print("    Pe adds nothing to the litigation argument over simple adoption metrics.")
else:
    print(f"  ✓ KILL CONDITION SURVIVED: Pe outperforms raw adoption by ΔR² = {KILL:+.4f}")
    print(f"    Pe explains {KILL*100:.1f} percentage points more variance in teen sadness")
    print(f"    than unweighted social media adoption alone.")

print("\n  NOTE: N=7 time points. These are preliminary signal-detection results,")
print("  not publication-ready. A proper analysis requires individual-level YRBS")
print("  microdata, controls for confounders, and platform-specific usage data.")
print("  This test determines whether the signal exists at all.\n")
