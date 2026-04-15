#!/usr/bin/env python3
"""
Social Media Litigation — Pe Exposure and Adolescent Mental Health
==================================================================

DEPRECATION NOTICE (2026-04-06)
-------------------------------
This script uses the ORIGINAL O/R/alpha scoring rubric (framework-derived,
subjective 0-3 scores). For litigation, use feature_proxy_analysis.py instead,
which uses 13 binary/ordinal verifiable features from feature-matrix.json.
The feature-proxy pipeline is NON-CIRCULAR; this script is kept for
comparison only. Do NOT cite this script's results as independent evidence.

METHODOLOGY OVERVIEW (for legal review)
----------------------------------------
This script tests whether the Void Framework's Pe (Péclet number) metric —
a composite measure of platform design opacity, reactivity, and coupling —
explains adolescent mental health decline better than raw social media
adoption rates alone.

The central hypothesis: it is not merely *how many* teens use social media
that predicts harm, but *what kind* of social media they use. Pe quantifies
the "what kind" — specifically, how opaque (algorithmic), reactive
(engagement-optimized), and coupled (identity-entangling) each platform's
design is in a given year.

DATA SOURCES
  - CDC Youth Risk Behavior Survey (YRBS), published biennial trend data
    (2011-2023): sadness/hopelessness, suicidal ideation, suicide planning,
    suicide attempts, cyberbullying victimization
  - Pew Research Center teen social media adoption surveys (2012-2023),
    interpolated to YRBS years
  - Platform design change timeline: each platform scored on three
    dimensions (Opacity O, Reactivity R, Coupling alpha) per YRBS year
    based on documented feature launches (algorithmic feeds, autoplay,
    recommendation engines, etc.)

PE COMPUTATION
  For each YRBS year, population-weighted Pe exposure is:
    Pe_exposure(year) = SUM over platforms of [adoption_pct * (O + R + alpha)]
  where (O + R + alpha) is the simplified Pe proxy — the sum of the three
  design dimension scores (each 0-3, total 0-9). This linear proxy avoids
  the nonlinear sinh transform used in the full Pe formula, making the
  regression relationship more interpretable for non-technical audiences
  (e.g., judges, juries). The sinh transform is monotonic, so rank ordering
  is preserved.

COMPARISON BASELINE
  Raw adoption = SUM over platforms of [adoption_pct]
  This is the "null hypothesis" metric: total social media exposure without
  any accounting for design quality. If Pe_exposure does not outperform
  raw adoption, the framework adds nothing to the litigation argument.

KILL CONDITION
  If delta_R_squared(Pe_exposure vs raw_adoption) <= 0 for all outcomes,
  the Pe metric adds no explanatory power beyond simple adoption rates.
  This would mean platform *design* does not matter — only *quantity* of
  exposure. The kill condition is checked and reported.

STATISTICAL NOTES
  - N = 7 YRBS time points (2011-2023, biennial). This is a small sample.
    Results are signal-detection, not definitive. Individual-level YRBS
    microdata with platform-specific usage would be needed for publication.
  - All regressions are simple OLS. No causal claims are made; this is
    correlational analysis of ecological (population-level) data.
  - Spearman rank correlations are reported alongside Pearson to guard
    against nonlinear relationships and outlier sensitivity.

Author: MoreRight Research
Date: 2026-03-30
License: CC-BY 4.0
"""

import json
import math
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for server environments
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from scipy import stats

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
FIGURES_DIR = SCRIPT_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

# Plot styling for publication quality
plt.rcParams.update({
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 9,
    "figure.figsize": (10, 6),
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# Color palette — colorblind-friendly (Wong 2011)
COLORS = {
    "pe":          "#0072B2",  # Blue
    "adoption":    "#D55E00",  # Vermilion
    "sadness":     "#CC79A7",  # Pink
    "suicide_c":   "#E69F00",  # Orange
    "suicide_p":   "#56B4E9",  # Sky blue
    "suicide_a":   "#009E73",  # Teal
    "cyber":       "#F0E442",  # Yellow
    "female":      "#CC79A7",  # Pink (same as sadness — used for female subgroup)
}


# ---------------------------------------------------------------------------
# Pe computation
# ---------------------------------------------------------------------------

# Full Pe formula from the Void Framework (Paper 3, Section 4)
# Pe = K * sinh(2 * (B_A - c * B_G))
# where c = 1 - (O + R + alpha) / 9
# B_A = 0.867 (empirical drift bias constant)
# B_G = pi / sqrt(2) approx 2.221 (derived from Cencov geometry, Section 165)
# K = 16 (hardware/deployment scale factor)
#
# For this analysis we use the SIMPLIFIED LINEAR PROXY:
#   Pe_proxy = O + R + alpha
# Rationale: (1) monotonic relationship with full Pe preserved,
# (2) avoids introducing nonlinear sinh into regression which would
# complicate legal interpretation, (3) differences in proxy are
# proportional to differences in design quality.

B_A = 0.867
B_G = math.pi / math.sqrt(2)  # ~2.2214
K = 16


def compute_full_pe(O, R, alpha):
    """
    Compute full Pe from the three design dimension scores.

    Parameters
    ----------
    O : float
        Opacity score (0-3). How algorithmic/opaque the content selection is.
    R : float
        Reactivity score (0-3). How engagement-optimized the feedback loops are.
    alpha : float
        Coupling score (0-3). How identity-entangled the platform makes users.

    Returns
    -------
    float
        Pe value. Higher = more drift-prone design.
    """
    V = O + R + alpha
    c = 1.0 - V / 9.0
    return K * math.sinh(2.0 * (B_A - c * B_G))


def compute_pe_proxy(O, R, alpha):
    """
    Simplified Pe proxy: sum of design dimension scores.
    Range: 0-9. Monotonically related to full Pe.
    """
    return O + R + alpha


# ---------------------------------------------------------------------------
# Sample / placeholder data
# ---------------------------------------------------------------------------
# This data is used if no external data files are provided.
# Sources are cited inline. Replace with authoritative data files for
# final analysis.

def build_sample_data():
    """
    Construct sample datasets from published sources.

    YRBS data: CDC Youth Risk Behavior Survey, published trend tables.
    Adoption data: Pew Research Center teen social media surveys.
    Platform scores: based on documented feature launches (algorithmic
    feed dates, autoplay launches, recommendation engine changes).

    Returns
    -------
    tuple of (yrbs_df, platform_data)
        yrbs_df : pd.DataFrame with columns [year, sadness, suicide_considered,
                  suicide_plan, suicide_attempt, cyberbullying]
        platform_data : dict of {platform: {year: {O, R, alpha, adoption_pct}}}
    """

    # --- YRBS mental health data ---
    # Source: CDC YRBS Data Summary & Trends Report 2013-2023
    # "Persistent feelings of sadness or hopelessness" (% of all students)
    # "Seriously considered attempting suicide" (%)
    # "Made a suicide plan" (%)
    # "Attempted suicide" (%)
    # "Electronically bullied" (%) — available from 2011
    yrbs = pd.DataFrame({
        "year": [2011, 2013, 2015, 2017, 2019, 2021, 2023],

        # Persistent sadness or hopelessness (all students, %)
        "sadness": [28.5, 29.9, 29.9, 31.5, 36.7, 42.0, 40.0],

        # Seriously considered attempting suicide (all students, %)
        "suicide_considered": [15.8, 17.0, 17.7, 17.2, 18.8, 22.0, 20.4],

        # Made a suicide plan (all students, %)
        # Source: YRBS trend tables
        "suicide_plan": [12.8, 13.6, 14.6, 13.6, 15.7, 18.0, 16.5],

        # Attempted suicide (all students, %)
        "suicide_attempt": [7.8, 8.0, 8.6, 7.4, 8.9, 10.2, 9.5],

        # Electronically bullied (all students, %)
        # Source: YRBS — question added 2011
        "cyberbullying": [16.2, 14.8, 15.5, 14.9, 15.7, 16.0, 16.5],
    })

    # --- Platform design scores and teen adoption rates ---
    # O = Opacity (0-3): algorithmic content selection opacity
    # R = Reactivity (0-3): engagement optimization intensity
    # alpha = Coupling (0-3): identity entanglement
    # adoption_pct = fraction of US teens 13-17 using the platform
    #
    # Scoring rationale:
    #   O increases when algorithmic curation replaces chronological feeds,
    #     when recommendation engines prioritize engagement over recency,
    #     when content sources become less transparent to users.
    #   R increases when autoplay is enabled by default, when notification
    #     systems become more aggressive, when infinite scroll replaces
    #     pagination, when variable-ratio reinforcement schedules are added.
    #   alpha increases when real-name/identity requirements strengthen,
    #     when social graph becomes more central to experience, when
    #     creator monetization ties economic identity to platform.

    platform_data = {
        "facebook": {
            # 2011: News Feed algorithmic since 2009, Sponsored Stories launching
            2011: {"O": 1.5, "R": 1.5, "alpha": 2.0, "adoption_pct": 0.77},
            # 2013: Deeper algo, more ads, Graph Search (identity)
            2013: {"O": 2.0, "R": 2.0, "alpha": 2.5, "adoption_pct": 0.71},
            # 2015: Video auto-play, engagement optimization documented
            2015: {"O": 2.0, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.51},
            # 2017: Reactions (2016), Live, deeper algorithmic engagement
            2017: {"O": 2.5, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.51},
            # 2019: "Meaningful interactions" but still engagement-optimized
            2019: {"O": 2.5, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.32},
            # 2021: Reels, Marketplace coupling, AI-recommended content
            2021: {"O": 2.5, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.27},
            # 2023: AI-recommended content dominant in feed
            2023: {"O": 2.5, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.23},
        },
        "instagram": {
            # 2011: Chronological photo feed, simple filters, mild coupling
            2011: {"O": 0.5, "R": 1.0, "alpha": 1.5, "adoption_pct": 0.01},
            # 2013: Video added (Jun 2013), growing identity investment
            2013: {"O": 0.5, "R": 1.5, "alpha": 2.0, "adoption_pct": 0.11},
            # 2015: Explore tab growing, strong identity coupling pre-algorithm
            2015: {"O": 1.0, "R": 2.0, "alpha": 2.5, "adoption_pct": 0.52},
            # 2017: Algorithmic feed (Jun 2016) + Stories (Aug 2016) = inflection
            2017: {"O": 2.5, "R": 2.5, "alpha": 3.0, "adoption_pct": 0.72},
            # 2019: Explore algo, beauty filters, creator monetization
            2019: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.72},
            # 2021: Reels (Aug 2020), full TikTok-style algorithmic feed
            2021: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.62},
            # 2023: Video-first, AI recommendations dominant
            2023: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.59},
        },
        "youtube": {
            # 2011: Pre-watch-time algorithm, mostly user-selected content
            2011: {"O": 1.0, "R": 1.0, "alpha": 1.0, "adoption_pct": 0.60},
            # 2013: Watch time algorithm (Mar 2012), recommended sidebar
            2013: {"O": 2.0, "R": 2.0, "alpha": 1.5, "adoption_pct": 0.70},
            # 2015: Autoplay ON by default (Mar 2015)
            2015: {"O": 2.0, "R": 2.5, "alpha": 1.5, "adoption_pct": 0.75},
            # 2017: Deeper recommendation, creator economy growing
            2017: {"O": 2.5, "R": 2.5, "alpha": 2.0, "adoption_pct": 0.85},
            # 2019: Smart autoplay, aggressive recommendations
            2019: {"O": 2.5, "R": 3.0, "alpha": 2.0, "adoption_pct": 0.85},
            # 2021: Shorts launched (Jul 2021), full algorithmic feed
            2021: {"O": 3.0, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.95},
            # 2023: Shorts dominant, AI recommendations
            2023: {"O": 3.0, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.93},
        },
        "tiktok": {
            # 2011-2015: Does not exist (Musical.ly launched 2014, tiny US presence)
            2011: {"O": 0.0, "R": 0.0, "alpha": 0.0, "adoption_pct": 0.00},
            2013: {"O": 0.0, "R": 0.0, "alpha": 0.0, "adoption_pct": 0.00},
            2015: {"O": 0.0, "R": 0.0, "alpha": 0.0, "adoption_pct": 0.00},
            # 2017: TikTok launched Sep 2017, For You Page algo from day 1
            2017: {"O": 3.0, "R": 3.0, "alpha": 2.0, "adoption_pct": 0.05},
            # 2019: Post-Musical.ly merger (Aug 2018), massive growth, creator fund
            2019: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.25},
            # 2021: Dominant platform, structural maximum on all dimensions
            2021: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.67},
            # 2023: Sustained maximum
            2023: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.63},
        },
        "snapchat": {
            # 2011: Launched late 2011, negligible adoption
            2011: {"O": 0.0, "R": 0.0, "alpha": 0.0, "adoption_pct": 0.00},
            # 2013: Stories (Oct 2013), ephemeral = high reactivity, social coupling
            2013: {"O": 1.5, "R": 2.0, "alpha": 2.0, "adoption_pct": 0.02},
            # 2015: Discover tab adds opacity, growing coupling (streaks)
            2015: {"O": 2.0, "R": 2.0, "alpha": 2.5, "adoption_pct": 0.41},
            # 2017: Algorithmic Discover, streak mechanics fully established
            2017: {"O": 2.0, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.69},
            # 2019: Stable design
            2019: {"O": 2.0, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.69},
            # 2021: Spotlight (Nov 2020) = TikTok-style algorithmic feed
            2021: {"O": 2.5, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.59},
            # 2023: My AI chatbot adds coupling
            2023: {"O": 2.5, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.51},
        },
    }

    return yrbs, platform_data


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_yrbs_data(filepath=None):
    """
    Load YRBS mental health data from file or use sample data.

    Expected format (CSV or JSON):
      Columns: year, sadness, suicide_considered, suicide_plan,
               suicide_attempt, cyberbullying
      Values: percentages (e.g., 28.5 means 28.5%)

    Parameters
    ----------
    filepath : str or Path, optional
        Path to CSV or JSON file. If None, uses built-in sample data.

    Returns
    -------
    pd.DataFrame
    """
    if filepath and Path(filepath).exists():
        ext = Path(filepath).suffix.lower()
        if ext == ".csv":
            df = pd.read_csv(filepath)
        elif ext == ".json":
            df = pd.read_json(filepath)
        else:
            raise ValueError(f"Unsupported file format: {ext}. Use .csv or .json")
        required = {"year", "sadness", "suicide_considered", "suicide_plan",
                    "suicide_attempt", "cyberbullying"}
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns in YRBS data: {missing}")
        return df.sort_values("year").reset_index(drop=True)

    # Auto-discover canonical CSV in same directory
    canonical = SCRIPT_DIR / "yrbs-trend-data.csv"
    if canonical.exists():
        print(f"[INFO] Loading YRBS from canonical CSV: {canonical.name}")
        raw = pd.read_csv(canonical)
        # Map CSV column names to analysis column names
        col_map = {
            "Year": "year",
            "Persistent_Sadness_Hopelessness_Total": "sadness",
            "Considered_Suicide_Total": "suicide_considered",
            "Suicide_Plan_Total": "suicide_plan",
            "Attempted_Suicide_Total": "suicide_attempt",
            "Electronic_Bullying_Total": "cyberbullying",
        }
        df = raw.rename(columns=col_map)[list(col_map.values())]
        # Convert to float (CSV may have integer strings)
        for c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
        return df.sort_values("year").reset_index(drop=True)

    # Last resort: built-in sample data (DEPRECATED — prefer CSV)
    print("[WARN] No YRBS CSV found. Using built-in sample data (may differ from canonical CSV).")
    sample_yrbs, _ = build_sample_data()
    return sample_yrbs


def load_platform_data(filepath=None):
    """
    Load platform Pe timeline data from file or use sample data.

    Expected format (JSON):
      {
        "platform_name": {
          "2011": {"O": 1.5, "R": 1.5, "alpha": 2.0, "adoption_pct": 0.77},
          ...
        },
        ...
      }

    Parameters
    ----------
    filepath : str or Path, optional
        Path to JSON file. If None, uses built-in sample data.

    Returns
    -------
    dict
        Nested dict: platform -> year (int) -> {O, R, alpha, adoption_pct}
    """
    if filepath and Path(filepath).exists():
        with open(filepath) as f:
            raw = json.load(f)
        # Convert string year keys to int
        data = {}
        for platform, years in raw.items():
            data[platform] = {}
            for yr_str, vals in years.items():
                yr = int(yr_str)
                required = {"O", "R", "alpha", "adoption_pct"}
                missing = required - set(vals.keys())
                if missing:
                    raise ValueError(
                        f"Missing keys for {platform}/{yr_str}: {missing}"
                    )
                data[platform][yr] = vals
        return data

    # Fall back to sample data
    print("[INFO] No platform data file provided. Using built-in sample data.")
    _, sample_platforms = build_sample_data()
    return sample_platforms


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

def compute_exposure_metrics(yrbs_df, platform_data):
    """
    For each YRBS year, compute:
      - Pe_exposure: population-weighted sum of (O+R+alpha) across platforms
      - raw_adoption: sum of adoption rates across platforms
      - full_pe_exposure: population-weighted sum of full Pe across platforms

    The Pe proxy (O+R+alpha) is used for the primary analysis because it is
    linear and interpretable. Full Pe (nonlinear sinh transform) is computed
    for reference.

    Parameters
    ----------
    yrbs_df : pd.DataFrame
        Must contain 'year' column.
    platform_data : dict
        Platform -> year -> {O, R, alpha, adoption_pct}

    Returns
    -------
    pd.DataFrame
        Input dataframe augmented with pe_exposure, raw_adoption,
        full_pe_exposure, and per-platform contributions.
    """
    years = yrbs_df["year"].values
    pe_exposures = []
    raw_adoptions = []
    full_pe_exposures = []

    platforms = sorted(platform_data.keys())

    for year in years:
        pe_exp = 0.0
        raw_adopt = 0.0
        full_pe_exp = 0.0

        for platform in platforms:
            if year not in platform_data[platform]:
                continue
            d = platform_data[platform][year]
            adoption = d["adoption_pct"]
            O, R, alpha = d["O"], d["R"], d["alpha"]

            # Pe proxy: linear sum of design dimensions, weighted by adoption
            pe_exp += adoption * compute_pe_proxy(O, R, alpha)

            # Raw adoption: just the adoption rate, no design weighting
            raw_adopt += adoption

            # Full Pe: nonlinear sinh transform, weighted by adoption
            full_pe_exp += adoption * compute_full_pe(O, R, alpha)

        pe_exposures.append(pe_exp)
        raw_adoptions.append(raw_adopt)
        full_pe_exposures.append(full_pe_exp)

    df = yrbs_df.copy()
    df["pe_exposure"] = pe_exposures
    df["raw_adoption"] = raw_adoptions
    df["full_pe_exposure"] = full_pe_exposures

    return df


# ---------------------------------------------------------------------------
# Regression analyses
# ---------------------------------------------------------------------------

def run_regressions(df, outcome_col, outcome_label):
    """
    Run three regression models for a single mental health outcome:
      Model A: outcome ~ pe_exposure
      Model B: outcome ~ raw_adoption
      Model C: outcome ~ pe_exposure + raw_adoption (multiple regression)

    Also computes Pearson and Spearman correlations, and the critical
    delta_R_squared test.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain 'pe_exposure', 'raw_adoption', and outcome_col.
    outcome_col : str
        Column name for the mental health outcome.
    outcome_label : str
        Human-readable label for reporting.

    Returns
    -------
    dict
        All regression statistics for this outcome.
    """
    y = df[outcome_col].values
    pe = df["pe_exposure"].values
    raw = df["raw_adoption"].values
    years = df["year"].values.astype(float)
    n = len(y)

    results = {"outcome": outcome_label, "outcome_col": outcome_col, "n": n}

    # --- Model A: outcome ~ pe_exposure ---
    slope_a, intercept_a, r_a, p_a, se_a = stats.linregress(pe, y)
    results["model_a"] = {
        "predictor": "Pe_exposure",
        "slope": slope_a,
        "intercept": intercept_a,
        "r": r_a,
        "p": p_a,
        "se": se_a,
        "r_squared": r_a ** 2,
    }

    # --- Model B: outcome ~ raw_adoption ---
    slope_b, intercept_b, r_b, p_b, se_b = stats.linregress(raw, y)
    results["model_b"] = {
        "predictor": "raw_adoption",
        "slope": slope_b,
        "intercept": intercept_b,
        "r": r_b,
        "p": p_b,
        "se": se_b,
        "r_squared": r_b ** 2,
    }

    # --- Model C: outcome ~ pe_exposure + raw_adoption (OLS) ---
    X_multi = np.column_stack([np.ones(n), pe, raw])
    beta, residuals, rank, sv = np.linalg.lstsq(X_multi, y, rcond=None)
    y_pred_c = X_multi @ beta
    ss_res_c = np.sum((y - y_pred_c) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2_c = 1.0 - ss_res_c / ss_tot if ss_tot > 0 else 0.0

    # Adjusted R-squared for multiple regression
    r2_adj_c = 1.0 - (1.0 - r2_c) * (n - 1) / (n - 3) if n > 3 else r2_c

    results["model_c"] = {
        "predictors": "Pe_exposure + raw_adoption",
        "beta_intercept": beta[0],
        "beta_pe": beta[1],
        "beta_raw": beta[2],
        "r_squared": r2_c,
        "r_squared_adj": r2_adj_c,
    }

    # --- Time trend comparison ---
    slope_t, intercept_t, r_t, p_t, se_t = stats.linregress(years, y)
    results["time_trend"] = {
        "r": r_t,
        "p": p_t,
        "r_squared": r_t ** 2,
    }

    # --- Spearman rank correlations ---
    rho_pe, sp_pe = stats.spearmanr(pe, y)
    rho_raw, sp_raw = stats.spearmanr(raw, y)
    results["spearman_pe"] = {"rho": rho_pe, "p": sp_pe}
    results["spearman_raw"] = {"rho": rho_raw, "p": sp_raw}

    # --- Delta R-squared: the critical test ---
    delta_r2 = r_a ** 2 - r_b ** 2
    results["delta_r_squared"] = delta_r2

    # --- Partial correlation: Pe controlling for raw adoption ---
    def partial_corr(x, y_vec, z):
        """Partial correlation of x and y controlling for z."""
        s_xz = stats.linregress(z, x)
        x_resid = x - (s_xz.slope * z + s_xz.intercept)
        s_yz = stats.linregress(z, y_vec)
        y_resid = y_vec - (s_yz.slope * z + s_yz.intercept)
        return stats.pearsonr(x_resid, y_resid)

    r_partial_pe, p_partial_pe = partial_corr(pe, y, raw)
    r_partial_raw, p_partial_raw = partial_corr(raw, y, pe)
    results["partial_pe_given_raw"] = {"r": r_partial_pe, "p": p_partial_pe}
    results["partial_raw_given_pe"] = {"r": r_partial_raw, "p": p_partial_raw}

    return results


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_time_series(df, outcome_cols, outcome_labels, outcome_colors):
    """
    Plot A: Dual-axis time series — Pe exposure overlaid with mental health
    variables.

    Left y-axis: Pe_exposure (population-weighted design quality)
    Right y-axis: Mental health outcome (% of students)
    x-axis: YRBS survey year

    This plot shows whether Pe exposure and mental health outcomes move
    together over time.
    """
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # Left axis: Pe exposure
    ax1.plot(df["year"], df["pe_exposure"], "o-", color=COLORS["pe"],
             linewidth=2.5, markersize=8, label="Pe exposure (weighted)", zorder=5)
    ax1.set_xlabel("YRBS Survey Year")
    ax1.set_ylabel("Population-Weighted Pe Exposure", color=COLORS["pe"])
    ax1.tick_params(axis="y", labelcolor=COLORS["pe"])

    # Right axis: mental health outcomes
    ax2 = ax1.twinx()
    for col, label, color_key in zip(outcome_cols, outcome_labels, outcome_colors):
        ax2.plot(df["year"], df[col], "s--", color=COLORS[color_key],
                 linewidth=1.5, markersize=6, alpha=0.85, label=label)
    ax2.set_ylabel("% of Students Reporting", color="#333333")
    ax2.tick_params(axis="y", labelcolor="#333333")

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left",
               framealpha=0.9)

    ax1.set_title(
        "Population-Weighted Pe Exposure vs. Adolescent Mental Health Outcomes\n"
        "(CDC YRBS 2011-2023)",
        fontsize=14, fontweight="bold"
    )
    ax1.set_xticks(df["year"])

    # Annotations for key inflection points
    ax1.annotate(
        "Instagram algorithmic\nfeed + Stories (2016)",
        xy=(2017, df.loc[df["year"] == 2017, "pe_exposure"].iloc[0]),
        xytext=(2014.5, df["pe_exposure"].max() * 0.55),
        arrowprops=dict(arrowstyle="->", color="#666"),
        fontsize=8, color="#666", ha="center"
    )
    ax1.annotate(
        "TikTok mass\nadoption (2019-21)",
        xy=(2021, df.loc[df["year"] == 2021, "pe_exposure"].iloc[0]),
        xytext=(2022.3, df["pe_exposure"].max() * 0.65),
        arrowprops=dict(arrowstyle="->", color="#666"),
        fontsize=8, color="#666", ha="center"
    )

    fig.tight_layout()
    outpath = FIGURES_DIR / "time_series_pe_vs_mental_health.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


def plot_scatter_regressions(df, all_results):
    """
    Plot B: Scatter plots — Pe exposure vs each mental health outcome
    with regression line and R-squared annotation.

    One subplot per outcome variable.
    """
    outcomes = [r for r in all_results]
    n_outcomes = len(outcomes)
    n_cols = min(3, n_outcomes)
    n_rows = math.ceil(n_outcomes / n_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 5 * n_rows))
    if n_outcomes == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i, res in enumerate(outcomes):
        ax = axes[i]
        col = res["outcome_col"]
        label = res["outcome"]
        y = df[col].values
        pe = df["pe_exposure"].values

        # Scatter
        ax.scatter(pe, y, color=COLORS["pe"], s=60, zorder=5, edgecolors="white",
                   linewidth=0.5)

        # Year labels on each point
        for _, row in df.iterrows():
            ax.annotate(str(int(row["year"])), (row["pe_exposure"], row[col]),
                        textcoords="offset points", xytext=(6, 4), fontsize=7,
                        color="#888")

        # Regression line
        m = res["model_a"]
        x_line = np.linspace(pe.min() * 0.95, pe.max() * 1.05, 100)
        y_line = m["slope"] * x_line + m["intercept"]
        ax.plot(x_line, y_line, "-", color=COLORS["pe"], alpha=0.5, linewidth=1.5)

        # R-squared annotation
        ax.text(
            0.05, 0.95,
            f"r = {m['r']:.3f}\nR$^2$ = {m['r_squared']:.3f}\np = {m['p']:.4f}",
            transform=ax.transAxes, fontsize=9, verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8)
        )

        ax.set_xlabel("Pe Exposure (population-weighted)")
        ax.set_ylabel(f"% Students — {label}")
        ax.set_title(label, fontsize=11)

    # Hide unused subplots
    for j in range(n_outcomes, len(axes)):
        axes[j].set_visible(False)

    fig.suptitle(
        "Pe Exposure vs. Mental Health Outcomes — Regression Analysis",
        fontsize=14, fontweight="bold", y=1.02
    )
    fig.tight_layout()
    outpath = FIGURES_DIR / "scatter_pe_vs_outcomes.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


def plot_r_squared_comparison(all_results):
    """
    Plot C: Bar chart comparing R-squared values for Pe_exposure model
    vs raw_adoption model for each mental health outcome.

    This is the critical visual: does Pe outperform raw adoption?
    """
    outcomes = [r["outcome"] for r in all_results]
    r2_pe = [r["model_a"]["r_squared"] for r in all_results]
    r2_raw = [r["model_b"]["r_squared"] for r in all_results]
    delta_r2 = [r["delta_r_squared"] for r in all_results]

    x = np.arange(len(outcomes))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    bars_pe = ax.bar(x - width / 2, r2_pe, width, label="Pe exposure model",
                     color=COLORS["pe"], edgecolor="white", linewidth=0.5)
    bars_raw = ax.bar(x + width / 2, r2_raw, width, label="Raw adoption model",
                      color=COLORS["adoption"], edgecolor="white", linewidth=0.5)

    # Delta R-squared annotations
    for i, (pe_val, raw_val, d) in enumerate(zip(r2_pe, r2_raw, delta_r2)):
        higher = max(pe_val, raw_val)
        sign = "+" if d > 0 else ""
        color = "#006400" if d > 0 else "#8B0000"
        ax.annotate(
            f"{sign}{d:.3f}",
            xy=(i, higher + 0.02),
            ha="center", fontsize=9, fontweight="bold", color=color
        )

    ax.set_ylabel("R-squared")
    ax.set_title(
        "Model Comparison: Pe Exposure vs. Raw Adoption Rate\n"
        "as Predictors of Adolescent Mental Health Outcomes",
        fontsize=13, fontweight="bold"
    )
    ax.set_xticks(x)
    ax.set_xticklabels(outcomes, rotation=20, ha="right", fontsize=9)
    ax.legend(loc="upper right")
    ax.set_ylim(0, max(max(r2_pe), max(r2_raw)) * 1.25)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.2f"))

    # Reference line at equal performance
    ax.axhline(y=0, color="gray", linewidth=0.5)

    fig.tight_layout()
    outpath = FIGURES_DIR / "r_squared_comparison.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------

def print_summary_table(all_results):
    """
    Print a formatted summary table with all regression statistics.
    Suitable for inclusion in a legal brief or supplementary material.
    """
    print()
    print("=" * 100)
    print("SUMMARY TABLE: Regression Results — Pe Exposure vs. Raw Adoption")
    print("=" * 100)
    print()

    # Header
    header = (
        f"{'Outcome':<30}  "
        f"{'r(Pe)':<8}  {'R2(Pe)':<8}  {'p(Pe)':<10}  "
        f"{'r(Raw)':<8}  {'R2(Raw)':<8}  {'p(Raw)':<10}  "
        f"{'dR2':<8}  "
        f"{'rho(Pe)':<8}  {'r_part(Pe)':<10}"
    )
    print(header)
    print("-" * len(header))

    for res in all_results:
        ma = res["model_a"]
        mb = res["model_b"]
        sp = res["spearman_pe"]
        pp = res["partial_pe_given_raw"]
        dr = res["delta_r_squared"]

        line = (
            f"{res['outcome']:<30}  "
            f"{ma['r']:>+7.4f}  {ma['r_squared']:>7.4f}  {ma['p']:>9.5f}  "
            f"{mb['r']:>+7.4f}  {mb['r_squared']:>7.4f}  {mb['p']:>9.5f}  "
            f"{dr:>+7.4f}  "
            f"{sp['rho']:>+7.4f}  {pp['r']:>+9.4f}"
        )
        print(line)

    print()
    print("  r(Pe)       = Pearson correlation with Pe_exposure")
    print("  R2(Pe)      = R-squared for outcome ~ Pe_exposure")
    print("  p(Pe)       = p-value for Pe_exposure model")
    print("  r(Raw)      = Pearson correlation with raw_adoption")
    print("  R2(Raw)     = R-squared for outcome ~ raw_adoption")
    print("  p(Raw)      = p-value for raw_adoption model")
    print("  dR2         = R2(Pe) - R2(Raw) — positive means Pe explains more")
    print("  rho(Pe)     = Spearman rank correlation with Pe_exposure")
    print("  r_part(Pe)  = Partial correlation of Pe controlling for raw adoption")
    print()


def print_detailed_results(all_results):
    """
    Print detailed per-outcome regression results including multiple
    regression, partial correlations, and time trend comparisons.
    """
    for res in all_results:
        print()
        print("-" * 72)
        print(f"  OUTCOME: {res['outcome']}")
        print(f"  N = {res['n']} YRBS time points")
        print("-" * 72)

        ma = res["model_a"]
        mb = res["model_b"]
        mc = res["model_c"]
        tt = res["time_trend"]

        print()
        print(f"  Model A: {res['outcome']} ~ Pe_exposure")
        print(f"    slope     = {ma['slope']:.4f}")
        print(f"    intercept = {ma['intercept']:.2f}")
        print(f"    r         = {ma['r']:+.4f}")
        print(f"    R-squared = {ma['r_squared']:.4f}")
        print(f"    p-value   = {ma['p']:.5f}")

        print()
        print(f"  Model B: {res['outcome']} ~ raw_adoption")
        print(f"    slope     = {mb['slope']:.4f}")
        print(f"    intercept = {mb['intercept']:.2f}")
        print(f"    r         = {mb['r']:+.4f}")
        print(f"    R-squared = {mb['r_squared']:.4f}")
        print(f"    p-value   = {mb['p']:.5f}")

        print()
        print(f"  Model C: {res['outcome']} ~ Pe_exposure + raw_adoption")
        print(f"    beta_intercept = {mc['beta_intercept']:.2f}")
        print(f"    beta_Pe        = {mc['beta_pe']:.4f}")
        print(f"    beta_raw       = {mc['beta_raw']:.4f}")
        print(f"    R-squared      = {mc['r_squared']:.4f}")
        print(f"    R-squared adj  = {mc['r_squared_adj']:.4f}")

        print()
        print(f"  Time trend comparison:")
        print(f"    {res['outcome']} ~ year: R2 = {tt['r_squared']:.4f}  (p = {tt['p']:.5f})")
        print(f"    dR2 (Pe vs time): {ma['r_squared'] - tt['r_squared']:+.4f}")

        print()
        print(f"  Spearman rank correlations:")
        sp = res["spearman_pe"]
        sr = res["spearman_raw"]
        print(f"    Pe vs outcome:  rho = {sp['rho']:+.4f}  (p = {sp['p']:.4f})")
        print(f"    Raw vs outcome: rho = {sr['rho']:+.4f}  (p = {sr['p']:.4f})")

        print()
        print(f"  Partial correlations:")
        pp = res["partial_pe_given_raw"]
        pr = res["partial_raw_given_pe"]
        print(f"    Pe | controlling for raw:  r = {pp['r']:+.4f}  (p = {pp['p']:.4f})")
        print(f"    Raw | controlling for Pe:  r = {pr['r']:+.4f}  (p = {pr['p']:.4f})")

        dr = res["delta_r_squared"]
        sign = "+" if dr > 0 else ""
        print()
        print(f"  CRITICAL TEST: dR2 = R2(Pe) - R2(raw) = {sign}{dr:.4f}")
        if dr > 0:
            print(f"    Pe explains {dr * 100:.1f} percentage points more variance "
                  f"than raw adoption.")
        else:
            print(f"    Raw adoption explains {-dr * 100:.1f} pp more variance "
                  f"than Pe exposure.")


# ---------------------------------------------------------------------------
# Kill condition check
# ---------------------------------------------------------------------------

def check_kill_condition(all_results):
    """
    KILL CONDITION: Pe exposure must outperform raw adoption rate for at
    least one mental health outcome. If dR2 <= 0 for ALL outcomes, the Pe
    metric adds nothing beyond simple adoption rates and the litigation
    argument based on platform design (rather than quantity of exposure)
    is not supported.

    Returns
    -------
    bool
        True if kill condition is triggered (Pe adds nothing).
    """
    print()
    print("=" * 72)
    print("KILL CONDITION CHECK")
    print("=" * 72)
    print()
    print("  Criterion: Pe_exposure must outperform raw_adoption (dR2 > 0)")
    print("  for at least one mental health outcome.")
    print()

    any_positive = False
    for res in all_results:
        dr = res["delta_r_squared"]
        status = "PASS" if dr > 0 else "FAIL"
        if dr > 0:
            any_positive = True
        print(f"    {res['outcome']:<30}  dR2 = {dr:+.4f}  [{status}]")

    print()
    if not any_positive:
        print("  KILL CONDITION TRIGGERED: Pe adds nothing beyond raw adoption rate.")
        print()
        print("  Interpretation: Platform design quality (O, R, alpha) does not")
        print("  explain adolescent mental health outcomes better than the simple")
        print("  total rate of social media adoption. The litigation argument that")
        print("  specific design features (algorithmic feeds, autoplay, engagement")
        print("  optimization) are the operative variable is NOT supported by")
        print("  this ecological analysis.")
        print()
        return True
    else:
        n_pass = sum(1 for r in all_results if r["delta_r_squared"] > 0)
        avg_dr = np.mean([r["delta_r_squared"] for r in all_results
                          if r["delta_r_squared"] > 0])
        print(f"  KILL CONDITION SURVIVED: Pe outperforms raw adoption in "
              f"{n_pass}/{len(all_results)} outcomes.")
        print(f"  Mean dR2 (positive cases) = +{avg_dr:.4f}")
        print()
        print("  Interpretation: Population-weighted Pe exposure (which accounts")
        print("  for platform design quality) explains more variance in adolescent")
        print("  mental health than raw adoption rates alone. This supports the")
        print("  argument that specific design features — not merely total")
        print("  exposure — are the operative variable.")
        print()
        return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """
    Main analysis pipeline.

    Usage:
      python analysis.py                              # Use sample data
      python analysis.py yrbs.csv platforms.json       # Use external data
    """
    print("=" * 72)
    print("SOCIAL MEDIA LITIGATION — Pe EXPOSURE ANALYSIS")
    print("Population-Weighted Pe Exposure vs. Adolescent Mental Health")
    print("=" * 72)
    print()

    # --- Parse arguments ---
    yrbs_path = sys.argv[1] if len(sys.argv) > 1 else None
    platform_path = sys.argv[2] if len(sys.argv) > 2 else None

    # --- Load data ---
    print("--- DATA LOADING ---")
    yrbs_df = load_yrbs_data(yrbs_path)
    platform_data = load_platform_data(platform_path)

    print(f"  YRBS years: {sorted(yrbs_df['year'].tolist())}")
    print(f"  Platforms:  {sorted(platform_data.keys())}")
    print(f"  N (time points): {len(yrbs_df)}")
    print()

    # --- Compute exposure metrics ---
    print("--- EXPOSURE COMPUTATION ---")
    print()
    print("  Pe_exposure(year) = SUM_platforms [ adoption_pct * (O + R + alpha) ]")
    print("  raw_adoption(year) = SUM_platforms [ adoption_pct ]")
    print()

    df = compute_exposure_metrics(yrbs_df, platform_data)

    # Print exposure table
    print(f"  {'Year':<6}  {'Pe_exposure':>12}  {'Raw_adoption':>14}  "
          f"{'Sadness%':>10}  {'SuicideC%':>10}  {'Cyber%':>8}")
    for _, row in df.iterrows():
        print(f"  {int(row['year']):<6}  {row['pe_exposure']:>12.2f}  "
              f"{row['raw_adoption']:>14.2f}  "
              f"{row['sadness']:>9.1f}%  {row['suicide_considered']:>9.1f}%  "
              f"{row['cyberbullying']:>7.1f}%")
    print()

    # --- Define outcomes ---
    outcomes = [
        ("sadness", "Persistent sadness/hopelessness", "sadness"),
        ("suicide_considered", "Seriously considered suicide", "suicide_c"),
        ("suicide_plan", "Made a suicide plan", "suicide_p"),
        ("suicide_attempt", "Attempted suicide", "suicide_a"),
        ("cyberbullying", "Electronically bullied", "cyber"),
    ]

    # --- Run regressions ---
    print("--- REGRESSION ANALYSES ---")
    all_results = []
    for col, label, _ in outcomes:
        res = run_regressions(df, col, label)
        all_results.append(res)

    # --- Print results ---
    print_detailed_results(all_results)
    print_summary_table(all_results)

    # --- Kill condition ---
    killed = check_kill_condition(all_results)

    # --- Generate plots ---
    print("--- GENERATING FIGURES ---")
    print()

    # Plot A: Time series
    plot_time_series(
        df,
        outcome_cols=[c for c, _, _ in outcomes],
        outcome_labels=[l for _, l, _ in outcomes],
        outcome_colors=[k for _, _, k in outcomes],
    )

    # Plot B: Scatter regressions
    plot_scatter_regressions(df, all_results)

    # Plot C: R-squared comparison
    plot_r_squared_comparison(all_results)

    # --- Final summary ---
    print()
    print("=" * 72)
    print("ANALYSIS COMPLETE")
    print("=" * 72)
    print()
    print(f"  Data points:     {len(df)} YRBS years")
    print(f"  Platforms:       {len(platform_data)}")
    print(f"  Outcomes tested: {len(outcomes)}")
    print(f"  Figures saved:   {FIGURES_DIR}/")
    print()

    if killed:
        print("  STATUS: KILL CONDITION TRIGGERED")
        print("  Pe does NOT outperform raw adoption for any outcome.")
    else:
        best = max(all_results, key=lambda r: r["delta_r_squared"])
        print(f"  STATUS: Pe outperforms raw adoption")
        print(f"  Best outcome: {best['outcome']}")
        print(f"    R2(Pe) = {best['model_a']['r_squared']:.4f}")
        print(f"    R2(raw) = {best['model_b']['r_squared']:.4f}")
        print(f"    dR2 = {best['delta_r_squared']:+.4f}")

    print()
    print("  IMPORTANT CAVEATS:")
    print("  1. N = 7 time points. This is ecological signal detection, not")
    print("     a definitive causal analysis.")
    print("  2. Platform O/R/alpha scores are researcher-assigned based on")
    print("     documented design features. Inter-rater reliability should")
    print("     be established before litigation use.")
    print("  3. YRBS data is biennial and aggregated. Individual-level")
    print("     microdata with platform-specific usage is needed for")
    print("     publication-quality causal inference.")
    print("  4. Confounders (economic conditions, COVID, smartphone")
    print("     penetration, other cultural factors) are not controlled.")
    print("  5. The Pe proxy (O+R+alpha) is a linear simplification.")
    print("     The full nonlinear Pe formula may perform differently.")
    print()

    return 0 if not killed else 1


if __name__ == "__main__":
    sys.exit(main())
