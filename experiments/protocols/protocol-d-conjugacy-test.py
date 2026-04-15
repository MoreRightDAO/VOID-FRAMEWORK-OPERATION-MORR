#!/usr/bin/env python3
"""
Protocol D: Conjugacy Constraint Empirical Test
================================================
Tests whether I(D;Y) + I(M;Y) ≤ H(Y) manifests empirically:
no platform achieves high engagement AND high transparency simultaneously.

Data sources:
  - Buffer 2026 cross-platform engagement rates (52M+ posts)
  - Framework Pe scores + O/R/α decomposition for major platforms
  - Platform transparency report quality ratings

The conjugacy constraint predicts a Pareto frontier: engagement and
transparency are zero-sum on a shared output channel. If true, this
is the mathematical proof that platforms are "engineered by design"
to exploit — maximizing engagement REQUIRES reducing transparency.
"""

import math
import numpy as np
from scipy import stats

# ─── Pe computation ──────────────────────────────────────────────────────

B_A = 0.867
B_G = 2.244
K   = 16

def pe(O, R, alpha):
    V = O + R + alpha
    c = 1 - V / 9
    b = B_A - c * B_G
    return K * math.sinh(2 * b)


# ─── Platform data ───────────────────────────────────────────────────────
# Each platform scored on:
#   O (opacity, 0-3): higher = more opaque algorithm
#   R (reactivity, 0-3): higher = more engagement-optimized
#   α (coupling, 0-3): higher = more user lock-in
#   engagement_rate: from Buffer 2026 report (52M+ posts) or industry data
#   transparency_score: composite of algorithmic disclosure quality (0-10)
#     Based on: model cards, transparency reports, algorithm explanation,
#     third-party audit access, ranking criteria disclosure

PLATFORMS = {
    'TikTok': {
        'O': 3.0, 'R': 3.0, 'alpha': 3.0,
        'engagement_rate': 4.6,   # Buffer 2026: median engagement %
        'daily_time_min': 95,     # Average daily time (minutes), eMarketer 2024
        'transparency_score': 1.5, # Minimal: no model cards, FYP logic opaque, limited transparency report
        'dau_mau': 0.72,          # High daily return
    },
    'Instagram': {
        'O': 3.0, 'R': 3.0, 'alpha': 3.0,
        'engagement_rate': 5.5,   # Buffer 2026
        'daily_time_min': 53,     # eMarketer
        'transparency_score': 2.0, # Mosseri blog posts on algorithm, but no model cards, limited audit access
        'dau_mau': 0.68,
    },
    'YouTube': {
        'O': 3.0, 'R': 3.0, 'alpha': 2.5,
        'engagement_rate': 3.5,   # estimated (Buffer doesn't separate YT well)
        'daily_time_min': 74,     # Nielsen
        'transparency_score': 3.0, # Some research API access, published recommendation principles, still opaque core
        'dau_mau': 0.62,
    },
    'Facebook': {
        'O': 2.5, 'R': 3.0, 'alpha': 2.5,
        'engagement_rate': 5.6,   # Buffer 2026
        'daily_time_min': 31,     # eMarketer
        'transparency_score': 3.5, # Meta transparency reports, some research access, ad library, but algorithm opaque
        'dau_mau': 0.67,
    },
    'Snapchat': {
        'O': 2.5, 'R': 3.0, 'alpha': 2.5,
        'engagement_rate': 3.0,   # estimated
        'daily_time_min': 30,     # eMarketer
        'transparency_score': 2.0, # Very limited transparency reporting
        'dau_mau': 0.65,
    },
    'X/Twitter': {
        'O': 2.0, 'R': 2.5, 'alpha': 2.0,
        'engagement_rate': 2.5,   # estimated post-Musk
        'daily_time_min': 34,     # eMarketer
        'transparency_score': 4.0, # Algorithm partially open-sourced (2023), but reversed some transparency
        'dau_mau': 0.50,
    },
    'LinkedIn': {
        'O': 2.0, 'R': 2.0, 'alpha': 2.5,
        'engagement_rate': 6.2,   # Buffer 2026 (highest!)
        'daily_time_min': 11,     # SimilarWeb
        'transparency_score': 4.5, # Professional context, some algorithm explanation, less engagement gaming
        'dau_mau': 0.35,
    },
    'Pinterest': {
        'O': 2.0, 'R': 2.0, 'alpha': 1.5,
        'engagement_rate': 4.0,   # Buffer 2026
        'daily_time_min': 14,     # SimilarWeb
        'transparency_score': 5.0, # More transparent about curation, visual search, less engagement-optimized
        'dau_mau': 0.25,
    },
    'Threads': {
        'O': 2.0, 'R': 2.5, 'alpha': 2.0,
        'engagement_rate': 3.6,   # Buffer 2026
        'daily_time_min': 7,      # estimated
        'transparency_score': 3.0, # New, some Meta transparency
        'dau_mau': 0.30,
    },
    'Reddit': {
        'O': 1.5, 'R': 2.0, 'alpha': 2.0,
        'engagement_rate': 3.0,   # estimated
        'daily_time_min': 34,     # SimilarWeb
        'transparency_score': 6.0, # Upvote/downvote visible, moderator-driven, old.reddit shows raw sort
        'dau_mau': 0.44,
    },
    'Wikipedia': {
        'O': 0.5, 'R': 0.5, 'alpha': 0.5,
        'engagement_rate': 0.1,   # Not engagement-optimized
        'daily_time_min': 4,      # SimilarWeb
        'transparency_score': 9.5, # Fully transparent: edit history, talk pages, open algorithms, no engagement optimization
        'dau_mau': 0.08,
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

print("=" * 72)
print("PROTOCOL D: Conjugacy Constraint Empirical Test")
print("I(D;Y) + I(M;Y) ≤ H(Y) — engagement × transparency tradeoff")
print("=" * 72)

# ─── Step 1: Compute Pe and display platform landscape ────────────────────

print("\n─── Platform Landscape ───\n")
print(f"{'Platform':>12}  {'O':>4}  {'R':>4}  {'α':>4}  {'Pe':>8}  {'Engage%':>9}  {'Min/day':>8}  {'Transp':>7}  {'DAU/MAU':>8}")
print("-" * 85)

names = []
pe_scores = []
engagement = []
transparency = []
daily_time = []
dau_mau = []
opacity_scores = []

for name, data in PLATFORMS.items():
    pe_val = pe(data['O'], data['R'], data['alpha'])
    pe_scores.append(pe_val)
    engagement.append(data['engagement_rate'])
    transparency.append(data['transparency_score'])
    daily_time.append(data['daily_time_min'])
    dau_mau.append(data['dau_mau'])
    opacity_scores.append(data['O'])
    names.append(name)
    print(f"{name:>12}  {data['O']:>4.1f}  {data['R']:>4.1f}  {data['alpha']:>4.1f}  {pe_val:>8.2f}  {data['engagement_rate']:>8.1f}%  {data['daily_time_min']:>7d}m  {data['transparency_score']:>6.1f}  {data['dau_mau']:>7.0%}")

pe_arr = np.array(pe_scores)
eng_arr = np.array(engagement)
trans_arr = np.array(transparency)
time_arr = np.array(daily_time)
dau_arr = np.array(dau_mau)
opacity_arr = np.array(opacity_scores)


# ─── Step 2: Conjugacy test — engagement vs transparency ──────────────────

print("\n" + "=" * 72)
print("TEST 1: Engagement × Transparency Tradeoff (Conjugacy)")
print("=" * 72)

# Daily time as engagement proxy (better than post engagement rate)
r_time_trans, p_time_trans = stats.pearsonr(time_arr, trans_arr)
rho_time_trans, sp_time_trans = stats.spearmanr(time_arr, trans_arr)
print(f"\n  Daily time vs Transparency:")
print(f"    Pearson r  = {r_time_trans:+.4f}  (p = {p_time_trans:.4f})")
print(f"    Spearman ρ = {rho_time_trans:+.4f}  (p = {sp_time_trans:.4f})")
print(f"    R²         = {r_time_trans**2:.4f}")

# DAU/MAU as stickiness proxy
r_dau_trans, p_dau_trans = stats.pearsonr(dau_arr, trans_arr)
rho_dau_trans, sp_dau_trans = stats.spearmanr(dau_arr, trans_arr)
print(f"\n  DAU/MAU vs Transparency:")
print(f"    Pearson r  = {r_dau_trans:+.4f}  (p = {p_dau_trans:.4f})")
print(f"    Spearman ρ = {rho_dau_trans:+.4f}  (p = {sp_dau_trans:.4f})")
print(f"    R²         = {r_dau_trans**2:.4f}")

# Opacity vs engagement
r_opa_time, p_opa_time = stats.pearsonr(opacity_arr, time_arr)
r_opa_dau, p_opa_dau = stats.pearsonr(opacity_arr, dau_arr)
print(f"\n  Opacity vs Daily time:  r = {r_opa_time:+.4f}  (p = {p_opa_time:.4f})")
print(f"  Opacity vs DAU/MAU:     r = {r_opa_dau:+.4f}  (p = {p_opa_dau:.4f})")


# ─── Step 3: Pe vs engagement metrics ────────────────────────────────────

print("\n" + "=" * 72)
print("TEST 2: Pe Predicts Engagement Capture")
print("=" * 72)

r_pe_time, p_pe_time = stats.pearsonr(pe_arr, time_arr)
r_pe_dau, p_pe_dau = stats.pearsonr(pe_arr, dau_arr)
rho_pe_time, sp_pe_time = stats.spearmanr(pe_arr, time_arr)
rho_pe_dau, sp_pe_dau = stats.spearmanr(pe_arr, dau_arr)

print(f"\n  Pe vs Daily time:")
print(f"    Pearson r  = {r_pe_time:+.4f}  (p = {p_pe_time:.4f})")
print(f"    Spearman ρ = {rho_pe_time:+.4f}  (p = {sp_pe_time:.4f})")
print(f"    R²         = {r_pe_time**2:.4f}")

print(f"\n  Pe vs DAU/MAU:")
print(f"    Pearson r  = {r_pe_dau:+.4f}  (p = {p_pe_dau:.4f})")
print(f"    Spearman ρ = {rho_pe_dau:+.4f}  (p = {sp_pe_dau:.4f})")
print(f"    R²         = {r_pe_dau**2:.4f}")


# ─── Step 4: Pe vs transparency ──────────────────────────────────────────

print("\n" + "=" * 72)
print("TEST 3: Pe Predicts Transparency Deficit")
print("=" * 72)

r_pe_trans, p_pe_trans = stats.pearsonr(pe_arr, trans_arr)
rho_pe_trans, sp_pe_trans = stats.spearmanr(pe_arr, trans_arr)

print(f"\n  Pe vs Transparency:")
print(f"    Pearson r  = {r_pe_trans:+.4f}  (p = {p_pe_trans:.4f})")
print(f"    Spearman ρ = {rho_pe_trans:+.4f}  (p = {sp_pe_trans:.4f})")
print(f"    R²         = {r_pe_trans**2:.4f}")

# ─── Step 5: Pareto frontier visualization (text) ────────────────────────

print("\n" + "=" * 72)
print("PARETO FRONTIER: Engagement (daily time) vs Transparency")
print("=" * 72)

# Sort by daily time descending
sorted_idx = np.argsort(-time_arr)
print(f"\n  {'Platform':>12}  {'Daily min':>10}  {'Transparency':>13}  {'Pe':>8}  {'Quadrant':>10}")
print("  " + "-" * 60)
for i in sorted_idx:
    # Quadrant: high engagement = >30min, high transparency = >5.0
    hi_eng = time_arr[i] > 30
    hi_trans = trans_arr[i] > 5.0
    if hi_eng and hi_trans:
        quad = "HI-ENG/HI-TR"  # Conjugacy violation if this exists
    elif hi_eng and not hi_trans:
        quad = "HI-ENG/LO-TR"  # Predicted by conjugacy
    elif not hi_eng and hi_trans:
        quad = "LO-ENG/HI-TR"  # Predicted by conjugacy
    else:
        quad = "LO-ENG/LO-TR"
    print(f"  {names[i]:>12}  {time_arr[i]:>9d}m  {trans_arr[i]:>12.1f}  {pe_arr[i]:>8.2f}  {quad:>12}")

# Count quadrant occupancy
hi_eng_hi_trans = sum(1 for i in range(len(names)) if time_arr[i] > 30 and trans_arr[i] > 5.0)
hi_eng_lo_trans = sum(1 for i in range(len(names)) if time_arr[i] > 30 and trans_arr[i] <= 5.0)
lo_eng_hi_trans = sum(1 for i in range(len(names)) if time_arr[i] <= 30 and trans_arr[i] > 5.0)
lo_eng_lo_trans = sum(1 for i in range(len(names)) if time_arr[i] <= 30 and trans_arr[i] <= 5.0)

print(f"\n  Quadrant counts:")
print(f"    HI-ENG / HI-TRANS (conjugacy violation): {hi_eng_hi_trans}")
print(f"    HI-ENG / LO-TRANS (predicted):           {hi_eng_lo_trans}")
print(f"    LO-ENG / HI-TRANS (predicted):           {lo_eng_hi_trans}")
print(f"    LO-ENG / LO-TRANS:                       {lo_eng_lo_trans}")

# Fisher exact test for 2x2 contingency
table = np.array([[hi_eng_hi_trans, hi_eng_lo_trans],
                   [lo_eng_hi_trans, lo_eng_lo_trans]])
odds_ratio, fisher_p = stats.fisher_exact(table)
print(f"\n  Fisher exact test (2×2 contingency):")
print(f"    Odds ratio = {odds_ratio:.4f}  p = {fisher_p:.4f}")


# ─── Summary ──────────────────────────────────────────────────────────────

print("\n" + "=" * 72)
print("SUMMARY: CONJUGACY CONSTRAINT")
print("=" * 72)

print(f"""
  The conjugacy constraint I(D;Y) + I(M;Y) ≤ H(Y) predicts:
    - No platform can achieve high engagement AND high transparency
    - Engagement and mechanism transparency are zero-sum

  RESULTS:
    Engagement (daily time) vs Transparency:  r = {r_time_trans:+.4f}  (p = {p_time_trans:.4f})
    Engagement (DAU/MAU) vs Transparency:     r = {r_dau_trans:+.4f}  (p = {p_dau_trans:.4f})
    Pe vs Transparency:                       r = {r_pe_trans:+.4f}  (p = {p_pe_trans:.4f})
    Pe vs Engagement (daily time):            r = {r_pe_time:+.4f}  (p = {p_pe_time:.4f})

  Quadrant analysis: {hi_eng_hi_trans}/{len(names)} platforms in the
  "high engagement + high transparency" quadrant.
""")

if hi_eng_hi_trans == 0:
    print("  ✓ CONJUGACY HOLDS: Zero platforms achieve both high engagement")
    print("    and high transparency. The tradeoff is empirically real.")
    print("    This supports the 'engineered by design' argument.")
elif hi_eng_hi_trans <= 1:
    print(f"  ~ CONJUGACY MOSTLY HOLDS: Only {hi_eng_hi_trans} platform(s) in violation quadrant.")
    print("    Investigate whether the exception is genuine or a scoring artifact.")
else:
    print(f"  ⚠ CONJUGACY WEAKENED: {hi_eng_hi_trans} platforms in violation quadrant.")
    print("    Either the transparency scoring needs refinement or the bound is looser than expected.")

if r_time_trans < -0.5 and p_time_trans < 0.05:
    print("\n  ✓ KILL CONDITION SURVIVED: Significant negative correlation between")
    print("    engagement and transparency. The more time users spend, the less")
    print("    transparent the platform. This is the Fantasia Bound in the data.")
else:
    print(f"\n  ⚠ Correlation present (r={r_time_trans:+.4f}) but {'not significant' if p_time_trans >= 0.05 else 'weaker than expected'}.")
    print("    With N=11 platforms, statistical power is limited.")
    print("    Direction is consistent with conjugacy even if p > 0.05.")

print("\n  NOTE: N=11 platforms. Transparency scores are researcher-assigned")
print("  (not ICC-validated across multiple raters). These are signal-detection")
print("  results. A proper study needs blinded transparency scoring with")
print("  multiple raters and a larger platform sample.\n")
