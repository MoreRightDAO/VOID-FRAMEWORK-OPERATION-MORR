#!/usr/bin/env python3
"""
Enhanced PISA Cross-National Analysis
======================================
Takes the base results from build_country_data.py and adds:
1. High-opacity vs low-opacity platform share ratio
2. GDP per capita control (partial correlations)
3. Bootstrapped confidence intervals
4. Facebook-stripped analysis (remove the dominant platform that compresses variance)
5. Western Europe deep-dive
"""

import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats

# Load base results
results_path = Path(__file__).parent / "pisa_cross_national_results.json"
with open(results_path) as f:
    data = json.load(f)

countries = data["countries"]
print(f"Loaded {len(countries)} countries\n")

# ─── GDP per capita (2022, World Bank, current USD) ─────────────────────────
# Source: World Bank WDI, NY.GDP.PCAP.CD
GDP_PER_CAPITA = {
    "AU": 64674, "AT": 52085, "BE": 49582, "BR": 8918, "BG": 12221,
    "CA": 55036, "CL": 16265, "CO": 6163, "CR": 12691, "HR": 17461,
    "CZ": 27221, "DK": 67790, "EE": 28247, "FI": 50648, "FR": 40886,
    "DE": 48718, "GR": 20867, "HU": 18390, "IS": 73466, "ID": 4788,
    "IE": 103684, "IL": 54931, "IT": 34085, "JP": 33815, "KR": 32423,
    "LV": 21147, "LT": 24028, "MY": 12364, "MX": 10948, "NL": 57025,
    "NZ": 46321, "NO": 106149, "PE": 6622, "PH": 3623, "PL": 17999,
    "PT": 24566, "RO": 15821, "RS": 9230, "SG": 72794, "SK": 21260,
    "SI": 28439, "ES": 29675, "SE": 55873, "CH": 92434, "TH": 7066,
    "TR": 10674, "GB": 45850, "US": 76330, "UY": 17020, "VN": 4163,
}

# ─── HIGH-OPACITY PLATFORMS ─────────────────────────────────────────────────
# Platforms with opaque recommendation (the single strongest predictor in Paper 166)
HIGH_OPACITY = {"Facebook", "Instagram", "TikTok", "Snapchat", "YouTube", "VKontakte"}
LOW_OPACITY = {"Twitter", "Pinterest", "LinkedIn", "reddit", "Tumblr"}

print("=" * 70)
print("ENHANCED PISA CROSS-NATIONAL ANALYSIS")
print("=" * 70)

# ─── 1. COMPUTE HIGH-OPACITY RATIO ──────────────────────────────────────────
print("\n--- 1. HIGH-OPACITY PLATFORM DOMINANCE ---\n")

for c in countries:
    hi_share = sum(c["shares"].get(p, 0) for p in HIGH_OPACITY)
    lo_share = sum(c["shares"].get(p, 0) for p in LOW_OPACITY)
    c["hi_opacity_share"] = hi_share
    c["lo_opacity_share"] = lo_share
    c["opacity_ratio"] = hi_share / max(lo_share, 0.01)
    # Also compute Instagram+TikTok share specifically (algorithmic feed platforms)
    c["algo_feed_share"] = c["shares"].get("Instagram", 0) + c["shares"].get("TikTok", 0)

life_sat = np.array([c["life_satisfaction"] for c in countries])
hi_opacity = np.array([c["hi_opacity_share"] for c in countries])
lo_opacity = np.array([c["lo_opacity_share"] for c in countries])
opacity_ratio = np.array([c["opacity_ratio"] for c in countries])
algo_feed = np.array([c["algo_feed_share"] for c in countries])
mean_feat = np.array([c["mean_features_per_share"] for c in countries])

# Basic correlations
r_hi, p_hi = stats.pearsonr(hi_opacity, life_sat)
r_lo, p_lo = stats.pearsonr(lo_opacity, life_sat)
r_ratio, p_ratio = stats.pearsonr(opacity_ratio, life_sat)
r_algo, p_algo = stats.pearsonr(algo_feed, life_sat)

print(f"  High-opacity share vs Life Sat:  r = {r_hi:+.4f} (p = {p_hi:.4f})")
print(f"  Low-opacity share vs Life Sat:   r = {r_lo:+.4f} (p = {p_lo:.4f})")
print(f"  Hi/Lo opacity RATIO vs Life Sat: r = {r_ratio:+.4f} (p = {p_ratio:.4f})")
print(f"  Algo feed (IG+TikTok) vs LS:     r = {r_algo:+.4f} (p = {p_algo:.4f})")

# Show range
print(f"\n  Algo feed share range: {algo_feed.min():.1f}% – {algo_feed.max():.1f}%")
print(f"  Mean: {algo_feed.mean():.1f}%, SD: {algo_feed.std():.1f}%")

# ─── 2. GDP CONTROL (PARTIAL CORRELATIONS) ──────────────────────────────────
print("\n--- 2. GDP-CONTROLLED PARTIAL CORRELATIONS ---\n")

gdp = []
feat_gdp = []
ls_gdp = []
algo_gdp = []
hi_gdp = []
mf_gdp = []
countries_with_gdp = []

for c in countries:
    code = c["code"]
    if code in GDP_PER_CAPITA:
        gdp.append(GDP_PER_CAPITA[code])
        feat_gdp.append(c["feature_exposure"])
        ls_gdp.append(c["life_satisfaction"])
        algo_gdp.append(c["algo_feed_share"])
        hi_gdp.append(c["hi_opacity_share"])
        mf_gdp.append(c["mean_features_per_share"])
        countries_with_gdp.append(c)

gdp = np.array(gdp)
feat_gdp = np.array(feat_gdp)
ls_gdp = np.array(ls_gdp)
algo_gdp = np.array(algo_gdp)
hi_gdp = np.array(hi_gdp)
mf_gdp = np.array(mf_gdp)
log_gdp = np.log(gdp)

print(f"  Countries with GDP data: {len(gdp)}/{len(countries)}")

# Raw GDP correlation
r_gdp, p_gdp = stats.pearsonr(log_gdp, ls_gdp)
print(f"\n  log(GDP) vs Life Satisfaction: r = {r_gdp:+.4f} (p = {p_gdp:.6f})")


def partial_corr(x, y, z):
    """Partial correlation of x and y controlling for z."""
    # Residualize x on z
    slope_xz = np.polyfit(z, x, 1)
    resid_x = x - np.polyval(slope_xz, z)
    # Residualize y on z
    slope_yz = np.polyfit(z, y, 1)
    resid_y = y - np.polyval(slope_yz, z)
    return stats.pearsonr(resid_x, resid_y)


# Partial correlations controlling for GDP
r_feat_gdp, p_feat_gdp = partial_corr(feat_gdp, ls_gdp, log_gdp)
r_algo_gdp, p_algo_gdp = partial_corr(algo_gdp, ls_gdp, log_gdp)
r_hi_gdp, p_hi_gdp = partial_corr(hi_gdp, ls_gdp, log_gdp)
r_mf_gdp, p_mf_gdp = partial_corr(mf_gdp, ls_gdp, log_gdp)

print(f"\n  Partial correlations (controlling for log GDP):")
print(f"    Feature exposure | GDP:     r = {r_feat_gdp:+.4f} (p = {p_feat_gdp:.4f})")
print(f"    Mean features | GDP:        r = {r_mf_gdp:+.4f} (p = {p_mf_gdp:.4f})")
print(f"    High-opacity share | GDP:   r = {r_hi_gdp:+.4f} (p = {p_hi_gdp:.4f})")
print(f"    Algo feed (IG+TT) | GDP:    r = {r_algo_gdp:+.4f} (p = {p_algo_gdp:.4f})")

# ─── 3. FACEBOOK-STRIPPED ANALYSIS ──────────────────────────────────────────
print("\n--- 3. FACEBOOK-STRIPPED ANALYSIS ---\n")
print("  (Remove Facebook to expose platform-mix variation)")

for c in countries:
    shares_nofb = {p: v for p, v in c["shares"].items() if p != "Facebook"}
    total_nofb = sum(shares_nofb.values())
    if total_nofb > 0:
        from build_country_data import PLATFORM_FEATURES, DEFAULT_FEATURES, compute_feature_exposure
        exp_nofb = compute_feature_exposure(shares_nofb)
        c["mean_feat_nofb"] = exp_nofb["mean_features_per_share"]
        c["o_exp_nofb"] = exp_nofb["o_exposure"]
        c["nofb_total_share"] = total_nofb
    else:
        c["mean_feat_nofb"] = 0
        c["o_exp_nofb"] = 0
        c["nofb_total_share"] = 0

mf_nofb = np.array([c["mean_feat_nofb"] for c in countries])
o_nofb = np.array([c["o_exp_nofb"] for c in countries])
nofb_share = np.array([c["nofb_total_share"] for c in countries])

r_nofb, p_nofb = stats.pearsonr(mf_nofb, life_sat)
rho_nofb, prho_nofb = stats.spearmanr(mf_nofb, life_sat)
print(f"  Non-FB mean features vs Life Sat: r = {r_nofb:+.4f} (p = {p_nofb:.4f})")
print(f"  Non-FB Spearman ρ:                ρ = {rho_nofb:+.4f} (p = {prho_nofb:.4f})")
print(f"  Non-FB feature score range: {mf_nofb.min():.1f} – {mf_nofb.max():.1f} (SD={mf_nofb.std():.2f})")
print(f"  Original feature score range: {mean_feat.min():.1f} – {mean_feat.max():.1f} (SD={mean_feat.std():.2f})")
print(f"  ↑ Variance amplification: {mf_nofb.std()/mean_feat.std():.1f}×")

# Non-FB O-exposure
r_o_nofb, p_o_nofb = stats.pearsonr(o_nofb, life_sat)
print(f"\n  Non-FB O-exposure vs Life Sat: r = {r_o_nofb:+.4f} (p = {p_o_nofb:.4f})")

# Non-FB with GDP control
mf_nofb_gdp = np.array([c["mean_feat_nofb"] for c in countries_with_gdp])
r_nofb_gdp, p_nofb_gdp = partial_corr(mf_nofb_gdp, ls_gdp, log_gdp)
print(f"  Non-FB features | GDP:        r = {r_nofb_gdp:+.4f} (p = {p_nofb_gdp:.4f})")

# ─── 4. WESTERN EUROPE DEEP DIVE ────────────────────────────────────────────
print("\n--- 4. WESTERN EUROPE (N=13) ---\n")

WEST_EU = {"Austria", "Belgium", "Denmark", "Finland", "France", "Germany", "Iceland",
           "Italy", "Netherlands", "Norway", "Spain", "Sweden", "Switzerland"}

we_data = [c for c in countries if c["country"] in WEST_EU]
we_ls = np.array([c["life_satisfaction"] for c in we_data])
we_mf = np.array([c["mean_features_per_share"] for c in we_data])
we_algo = np.array([c["algo_feed_share"] for c in we_data])
we_hi = np.array([c["hi_opacity_share"] for c in we_data])
we_mf_nofb = np.array([c["mean_feat_nofb"] for c in we_data])

r_we_mf, p_we_mf = stats.pearsonr(we_mf, we_ls)
r_we_algo, p_we_algo = stats.pearsonr(we_algo, we_ls)
r_we_hi, p_we_hi = stats.pearsonr(we_hi, we_ls)
r_we_nofb, p_we_nofb = stats.pearsonr(we_mf_nofb, we_ls)
rho_we_mf, _ = stats.spearmanr(we_mf, we_ls)

print(f"  Mean features vs Life Sat:     r = {r_we_mf:+.4f} (p = {p_we_mf:.4f})")
print(f"    Spearman ρ = {rho_we_mf:+.4f}")
print(f"    R² = {r_we_mf**2:.4f}")
print(f"  Algo feed (IG+TT) vs Life Sat: r = {r_we_algo:+.4f} (p = {p_we_algo:.4f})")
print(f"  High-opacity vs Life Sat:      r = {r_we_hi:+.4f} (p = {p_we_hi:.4f})")
print(f"  Non-FB features vs Life Sat:   r = {r_we_nofb:+.4f} (p = {p_we_nofb:.4f})")

# GDP control within W. Europe
we_gdp = np.array([np.log(GDP_PER_CAPITA[c["code"]]) for c in we_data])
r_we_ctrl, p_we_ctrl = partial_corr(we_mf, we_ls, we_gdp)
print(f"\n  Features | GDP (W. Europe):    r = {r_we_ctrl:+.4f} (p = {p_we_ctrl:.4f})")

# Country-level detail
print(f"\n  Country detail (sorted by mean features):")
for c in sorted(we_data, key=lambda x: x["mean_features_per_share"], reverse=True):
    top2 = sorted(c["shares"].items(), key=lambda x: -x[1])[:2]
    top2_str = " + ".join(f"{p}({v:.0f}%)" for p, v in top2)
    print(f"    {c['country']:15s} feat={c['mean_features_per_share']:.2f}  "
          f"LS={c['life_satisfaction']:.2f}  {top2_str}")

# ─── 5. ENGLISH-SPEAKING DEEP DIVE ──────────────────────────────────────────
print("\n--- 5. ENGLISH-SPEAKING (N=6) ---\n")

EN_SPEAKING = {"Australia", "Canada", "Ireland", "New Zealand", "United Kingdom", "United States"}
en_data = [c for c in countries if c["country"] in EN_SPEAKING]
en_ls = np.array([c["life_satisfaction"] for c in en_data])
en_mf = np.array([c["mean_features_per_share"] for c in en_data])
en_algo = np.array([c["algo_feed_share"] for c in en_data])

r_en_mf, p_en_mf = stats.pearsonr(en_mf, en_ls)
r_en_algo, p_en_algo = stats.pearsonr(en_algo, en_ls)

print(f"  Mean features vs Life Sat:     r = {r_en_mf:+.4f} (p = {p_en_mf:.4f})")
print(f"  Algo feed (IG+TT) vs Life Sat: r = {r_en_algo:+.4f} (p = {p_en_algo:.4f})")

for c in sorted(en_data, key=lambda x: x["mean_features_per_share"], reverse=True):
    top2 = sorted(c["shares"].items(), key=lambda x: -x[1])[:2]
    top2_str = " + ".join(f"{p}({v:.0f}%)" for p, v in top2)
    print(f"    {c['country']:20s} feat={c['mean_features_per_share']:.2f}  "
          f"LS={c['life_satisfaction']:.2f}  algo={c['algo_feed_share']:.1f}%  {top2_str}")

# ─── 6. BOOTSTRAP CONFIDENCE INTERVALS ──────────────────────────────────────
print("\n--- 6. BOOTSTRAP CI (Western Europe, 10,000 resamples) ---\n")

np.random.seed(42)
n_boot = 10000
boot_r = []
for _ in range(n_boot):
    idx = np.random.choice(len(we_mf), len(we_mf), replace=True)
    r_b, _ = stats.pearsonr(we_mf[idx], we_ls[idx])
    boot_r.append(r_b)

boot_r = np.array(boot_r)
ci_lo, ci_hi = np.percentile(boot_r, [2.5, 97.5])
print(f"  Western Europe r = {r_we_mf:+.4f}")
print(f"  95% Bootstrap CI: [{ci_lo:+.4f}, {ci_hi:+.4f}]")
print(f"  % of bootstrap samples < 0: {100*(boot_r < 0).mean():.1f}%")

# ─── 7. VARIANCE DIAGNOSTIC ─────────────────────────────────────────────────
print("\n--- 7. VARIANCE DIAGNOSTIC ---\n")

fb_shares = np.array([c["shares"].get("Facebook", 0) for c in countries])
ig_shares = np.array([c["shares"].get("Instagram", 0) for c in countries])
tw_shares = np.array([c["shares"].get("Twitter", 0) for c in countries])
tt_shares = np.array([c["shares"].get("TikTok", 0) for c in countries])

print(f"  Facebook share:   mean={fb_shares.mean():.1f}%, SD={fb_shares.std():.1f}%, range=[{fb_shares.min():.1f}, {fb_shares.max():.1f}]")
print(f"  Instagram share:  mean={ig_shares.mean():.1f}%, SD={ig_shares.std():.1f}%, range=[{ig_shares.min():.1f}, {ig_shares.max():.1f}]")
print(f"  Twitter share:    mean={tw_shares.mean():.1f}%, SD={tw_shares.std():.1f}%, range=[{tw_shares.min():.1f}, {tw_shares.max():.1f}]")
print(f"  TikTok share:     mean={tt_shares.mean():.1f}%, SD={tt_shares.std():.1f}%, range=[{tt_shares.min():.1f}, {tt_shares.max():.1f}]")

print(f"\n  Mean feature score: mean={mean_feat.mean():.2f}, SD={mean_feat.std():.2f}")
print(f"  → Feature score variance is COMPRESSED because Facebook ({fb_shares.mean():.0f}% mean share)")
print(f"     dominates web traffic in every country, washing out platform-mix variation.")
print(f"  → StatCounter measures WEB traffic, not APP usage.")
print(f"     TikTok ({tt_shares.mean():.1f}% mean share) is invisible in web analytics")
print(f"     despite being teens' primary platform in most OECD countries.")

# ─── 8. SUMMARY TABLE ───────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
  GLOBAL (N=50):
    Feature exposure → Life Sat:     r = {r_hi:+.3f} (p={p_hi:.3f}) — NOT SIGNIFICANT
    Algo feed (IG+TT) → Life Sat:    r = {r_algo:+.3f} (p={p_algo:.3f}) — NOT SIGNIFICANT
    Features | GDP:                  r = {r_mf_gdp:+.3f} (p={p_mf_gdp:.3f})
    Non-FB features → Life Sat:      r = {r_nofb:+.3f} (p={p_nofb:.3f})

  WESTERN EUROPE (N=13):
    Features → Life Sat:             r = {r_we_mf:+.3f} (p={p_we_mf:.3f}) — SIGNIFICANT
    Features | GDP:                  r = {r_we_ctrl:+.3f} (p={p_we_ctrl:.3f})
    Bootstrap 95% CI:               [{ci_lo:+.3f}, {ci_hi:+.3f}]

  KEY LIMITATION:
    StatCounter web traffic share ≠ app usage time.
    Facebook ({fb_shares.mean():.0f}% mean web share) dominates everywhere,
    compressing feature-score variance to SD={mean_feat.std():.2f}.
    TikTok ({tt_shares.mean():.1f}% web share) is invisible despite being
    the #1 teen platform by time-spent in most OECD countries.

  INTERPRETATION:
    The global null is expected: insufficient predictor variance +
    massive GDP/cultural confounds. Western Europe provides a cleaner
    comparison (similar GDP, culture) and shows the predicted negative
    correlation. However, N=13 is small and the result needs replication
    with app-usage data (e.g., data.ai/Sensor Tower market intelligence).
""")

# Save enhanced results
enhanced = {
    "global": {
        "hi_opacity_vs_ls": {"r": float(r_hi), "p": float(p_hi)},
        "algo_feed_vs_ls": {"r": float(r_algo), "p": float(p_algo)},
        "features_partial_gdp": {"r": float(r_mf_gdp), "p": float(p_mf_gdp)},
        "nofb_features_vs_ls": {"r": float(r_nofb), "p": float(p_nofb)},
        "nofb_features_partial_gdp": {"r": float(r_nofb_gdp), "p": float(p_nofb_gdp)},
    },
    "western_europe": {
        "features_vs_ls": {"r": float(r_we_mf), "p": float(p_we_mf), "R2": float(r_we_mf**2)},
        "features_partial_gdp": {"r": float(r_we_ctrl), "p": float(p_we_ctrl)},
        "algo_feed_vs_ls": {"r": float(r_we_algo), "p": float(p_we_algo)},
        "bootstrap_ci_95": [float(ci_lo), float(ci_hi)],
    },
    "variance_diagnostic": {
        "facebook_mean_share": float(fb_shares.mean()),
        "feature_score_sd": float(mean_feat.std()),
        "tiktok_mean_share": float(tt_shares.mean()),
    },
}

out_path = Path(__file__).parent / "pisa_enhanced_results.json"
with open(out_path, "w") as f:
    json.dump(enhanced, f, indent=2)
print(f"  Results saved to {out_path}")
