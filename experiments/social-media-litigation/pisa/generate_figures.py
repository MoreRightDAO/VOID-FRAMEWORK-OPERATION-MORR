#!/usr/bin/env python3
"""Generate publication-quality figures for PISA cross-national analysis."""

import json
from pathlib import Path

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Load data
with open(Path(__file__).parent / "pisa_cross_national_results.json") as f:
    data = json.load(f)

countries = data["countries"]

# Recompute needed values
HIGH_OPACITY = {"Facebook", "Instagram", "TikTok", "Snapchat", "YouTube", "VKontakte"}

for c in countries:
    c["algo_feed_share"] = c["shares"].get("Instagram", 0) + c["shares"].get("TikTok", 0)

WEST_EU = {"Austria", "Belgium", "Denmark", "Finland", "France", "Germany", "Iceland",
           "Italy", "Netherlands", "Norway", "Spain", "Sweden", "Switzerland"}
EN_SPEAKING = {"Australia", "Canada", "Ireland", "New Zealand", "United Kingdom", "United States"}
LATIN_AM = {"Brazil", "Chile", "Colombia", "Costa Rica", "Mexico", "Peru", "Uruguay"}
EAST_ASIA = {"Japan", "Korea", "Singapore"}

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# ─── Panel A: Western Europe — features vs life satisfaction ─────────────────
ax = axes[0, 0]
we_data = [c for c in countries if c["country"] in WEST_EU]
we_mf = np.array([c["mean_features_per_share"] for c in we_data])
we_ls = np.array([c["life_satisfaction"] for c in we_data])
r_we, p_we = stats.pearsonr(we_mf, we_ls)

ax.scatter(we_mf, we_ls, c="steelblue", s=60, zorder=3, edgecolors="white", linewidths=0.5)
for c in we_data:
    offset = (0.02, 0.04)
    if c["country"] == "Denmark":
        offset = (-0.08, 0.06)
    elif c["country"] == "Switzerland":
        offset = (0.02, 0.06)
    elif c["country"] == "Finland":
        offset = (-0.15, -0.08)
    ax.annotate(c["country"], (c["mean_features_per_share"], c["life_satisfaction"]),
               fontsize=7.5, xytext=offset, textcoords="offset fontsize")

z = np.polyfit(we_mf, we_ls, 1)
x_line = np.linspace(we_mf.min() - 0.1, we_mf.max() + 0.1, 100)
ax.plot(x_line, np.polyval(z, x_line), "r--", alpha=0.6, linewidth=1.5)
ax.set_xlabel("Mean Platform Feature Score", fontsize=10)
ax.set_ylabel("PISA 2022 Life Satisfaction (0-10)", fontsize=10)
ax.set_title(f"A. Western Europe (N=13)\nr = {r_we:.3f}, p = {p_we:.4f}, R² = {r_we**2:.3f}", fontsize=11)
ax.text(0.05, 0.05, "Higher feature score = more\nmanipulative design patterns",
        transform=ax.transAxes, fontsize=8, style="italic", alpha=0.7)

# ─── Panel B: Global — Instagram share vs life satisfaction ──────────────────
ax = axes[0, 1]
all_ig = np.array([c["shares"].get("Instagram", 0) for c in countries])
all_ls = np.array([c["life_satisfaction"] for c in countries])
r_ig, p_ig = stats.pearsonr(all_ig, all_ls)

colors = []
for c in countries:
    if c["country"] in WEST_EU:
        colors.append("steelblue")
    elif c["country"] in EN_SPEAKING:
        colors.append("coral")
    elif c["country"] in LATIN_AM:
        colors.append("green")
    elif c["country"] in EAST_ASIA:
        colors.append("purple")
    else:
        colors.append("gray")

ax.scatter(all_ig, all_ls, c=colors, s=40, alpha=0.7, edgecolors="white", linewidths=0.3, zorder=3)

# Annotate outliers
for c in countries:
    if c["country"] in {"Japan", "Türkiye", "Colombia", "Costa Rica", "United Kingdom",
                          "Denmark", "Indonesia", "Philippines"}:
        ax.annotate(c["code"], (c["shares"].get("Instagram", 0), c["life_satisfaction"]),
                   fontsize=6.5, alpha=0.7)

z2 = np.polyfit(all_ig, all_ls, 1)
x2 = np.linspace(0, all_ig.max() + 1, 100)
ax.plot(x2, np.polyval(z2, x2), "r--", alpha=0.5, linewidth=1.5)
ax.set_xlabel("Instagram Web Traffic Share (%)", fontsize=10)
ax.set_ylabel("PISA 2022 Life Satisfaction (0-10)", fontsize=10)
ax.set_title(f"B. Global Instagram Exposure (N=50)\nr = {r_ig:.3f}, p = {p_ig:.4f}", fontsize=11)

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='steelblue', markersize=6, label='W. Europe'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='coral', markersize=6, label='English-speaking'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=6, label='Latin America'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='purple', markersize=6, label='East Asia'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=6, label='Other'),
]
ax.legend(handles=legend_elements, fontsize=7, loc="lower left")

# ─── Panel C: Feature score bar chart — Denmark vs Italy/Sweden ──────────────
ax = axes[1, 0]
dk = next(c for c in countries if c["country"] == "Denmark")
it = next(c for c in countries if c["country"] == "Italy")
se = next(c for c in countries if c["country"] == "Sweden")

platforms = ["Facebook", "Twitter", "Instagram", "Pinterest", "YouTube", "LinkedIn", "reddit"]
dk_shares = [dk["shares"].get(p, 0) for p in platforms]
it_shares = [it["shares"].get(p, 0) for p in platforms]
se_shares = [se["shares"].get(p, 0) for p in platforms]

x = np.arange(len(platforms))
width = 0.25
ax.bar(x - width, dk_shares, width, label=f'Denmark (LS={dk["life_satisfaction"]})', color="steelblue", alpha=0.8)
ax.bar(x, it_shares, width, label=f'Italy (LS={it["life_satisfaction"]})', color="coral", alpha=0.8)
ax.bar(x + width, se_shares, width, label=f'Sweden (LS={se["life_satisfaction"]})', color="orange", alpha=0.8)
ax.set_xticks(x)
ax.set_xticklabels(platforms, rotation=30, ha="right", fontsize=8)
ax.set_ylabel("Web Traffic Share (%)", fontsize=10)
ax.set_title("C. Platform Mix: Best vs Worst Teen Wellbeing\n(Western Europe natural experiment)", fontsize=11)
ax.legend(fontsize=8)

# ─── Panel D: Summary correlation bar chart ──────────────────────────────────
ax = axes[1, 1]

labels = [
    "Feature exp.\n(global)",
    "IG share\n(global)",
    "Non-FB O-exp.\n(global)",
    "Features\n(W. Europe)",
    "Features|GDP\n(W. Europe)",
]

# Recompute non-FB O-exposure
from build_country_data import PLATFORM_FEATURES, DEFAULT_FEATURES
o_nofb_vals = []
for c in countries:
    shares_nofb = {p: v for p, v in c["shares"].items() if p != "Facebook"}
    total_nofb = sum(shares_nofb.values())
    o_exp = 0
    for p, v in shares_nofb.items():
        feats = PLATFORM_FEATURES.get(p, DEFAULT_FEATURES)
        o_exp += (v / 100.0) * feats["O"]
    o_nofb_vals.append(o_exp)

o_nofb = np.array(o_nofb_vals)
r_o_nofb, p_o_nofb = stats.pearsonr(o_nofb, all_ls)

r_vals = [0.108, r_ig, r_o_nofb, r_we, -0.580]
p_vals = [0.455, p_ig, p_o_nofb, p_we, 0.038]
bar_colors = ["gray" if p > 0.05 else ("steelblue" if r < 0 else "coral") for r, p in zip(r_vals, p_vals)]

bars = ax.barh(range(len(labels)), r_vals, color=bar_colors, alpha=0.8, edgecolor="white")
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel("Pearson r", fontsize=10)
ax.axvline(0, color="black", linewidth=0.5)
ax.set_title("D. Correlation Summary\n(gray = not significant)", fontsize=11)

for i, (r, p) in enumerate(zip(r_vals, p_vals)):
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    ax.text(r + 0.02 if r >= 0 else r - 0.02, i, f"r={r:.2f} {sig}",
            va="center", ha="left" if r >= 0 else "right", fontsize=8)

plt.tight_layout(pad=2.0)
fig_path = Path(__file__).parent / "pisa_enhanced_4panel.png"
plt.savefig(fig_path, dpi=150, bbox_inches="tight")
print(f"Figure saved to {fig_path}")
plt.close()
