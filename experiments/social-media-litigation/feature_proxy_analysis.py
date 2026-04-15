#!/usr/bin/env python3
"""
Feature-Based Pe Proxy Analysis — Non-Circular Platform Design Scoring
=======================================================================

PURPOSE
-------
This script replaces the subjective O/R/alpha scoring (which relies on the Void
Framework's own rubric) with OBJECTIVE, BINARY/ORDINAL platform design features.
Each feature is independently verifiable from public records (press releases,
app changelogs, UI documentation). This breaks the circularity problem: the
features are facts about platform design, not framework-dependent assessments.

THE CIRCULARITY PROBLEM
-----------------------
The original analysis (analysis.py) scored platforms on O (Opacity), R (Reactivity),
and alpha (Coupling) using the framework's own rubric. This means the Pe metric
was constructed using framework concepts, then tested against mental health data.
If the framework predicts that opacity drives harm, and opacity is scored using
framework criteria, the result is circular.

THIS ANALYSIS FIXES THAT by:
  1. Replacing O/R/alpha scores with 13 binary/ordinal design features
  2. Each feature is a verifiable fact: "Does Instagram have algorithmic feed
     in 2017? Yes/No" — no framework interpretation needed
  3. Running DATA-DRIVEN weighting: let regression find which features matter
  4. Checking whether O-type features dominate (framework prediction, tested
     non-circularly)

FEATURES (13 total, grouped by framework category for post-hoc comparison)
--------------------------------------------------------------------------
O-type (Opacity):
  - algorithmic_feed (0/1/2)
  - autoplay_video (0/1/2)
  - opaque_recommendation (0/1/2)
  - hidden_ranking_signals (0/1/2)

R-type (Reactivity):
  - infinite_scroll (0/1)
  - push_notifications_engagement (0/1/2)
  - real_time_metrics (0/1/2)
  - streaks_or_daily_hooks (0/1)

alpha-type (Coupling):
  - beauty_ar_filters (0/1)
  - social_comparison_visible (0/1/2)
  - identity_persistence (0/1/2)
  - disappearing_content (0/1)
  - default_public_minor_profiles (0/1)

DATA SOURCES
  - feature-matrix.json: Binary/ordinal feature states per platform per year,
    sourced from public records (press releases, app changelogs, Pew surveys)
  - yrbs-trend-data.csv: CDC Youth Risk Behavior Survey biennial trend data
    (2011-2023)
  - Teen adoption rates: Pew Research Center (2012-2024), with interpolation
    for missing years

STATISTICAL APPROACH
  1. Unweighted feature score: sum of all 13 features per platform per year
  2. Weighted feature exposure: adoption_pct * feature_score, summed across platforms
  3. OLS regression: mental_health ~ weighted_feature_exposure
  4. Comparison: mental_health ~ raw_adoption (no feature weighting)
  5. Data-driven feature weighting: regress on individual features to identify
     which features are most predictive
  6. Category dominance test: do O-type features explain more than R-type or
     alpha-type? (Framework predicts O-type dominates)
  7. Comparison with original O/R/alpha-based Pe proxy

KILL CONDITIONS
  KC-1: If feature proxy does NOT outperform raw adoption (dR2 <= 0 for all
        outcomes), features add nothing. Platform design does not matter.
  KC-2: If data-driven weights show alpha-type features dominate (not O-type),
        the framework's prediction that opacity is the operative variable fails.

CAVEATS
  - N = 7 YRBS time points. Small sample. Signal detection only.
  - Ecological correlation, not causal. Individual-level data needed for
    publication-quality analysis.
  - Feature coding inevitably involves judgment calls at boundaries. Binary
    coding reduces this but does not eliminate it.
  - Some adoption rates are estimated (flagged in feature-matrix.json).

Author: MoreRight Research
Date: 2026-03-30
License: CC-BY 4.0
"""

import json
import math
import os
import sys
import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from scipy import stats

# Suppress warnings for clean output in legal context
warnings.filterwarnings("ignore", category=RuntimeWarning)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
FIGURES_DIR = SCRIPT_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

# YRBS years — these are the time points we analyze
YRBS_YEARS = [2011, 2013, 2015, 2017, 2019, 2021, 2023]

# Feature category groupings — used for category dominance analysis
O_TYPE_FEATURES = [
    "algorithmic_feed",
    "autoplay_video",
    "opaque_recommendation",
    "hidden_ranking_signals",
]

R_TYPE_FEATURES = [
    "infinite_scroll",
    "push_notifications_engagement",
    "real_time_metrics",
    "streaks_or_daily_hooks",
]

ALPHA_TYPE_FEATURES = [
    "beauty_ar_filters",
    "social_comparison_visible",
    "identity_persistence",
    "disappearing_content",
    "default_public_minor_profiles",
]

ALL_FEATURES = O_TYPE_FEATURES + R_TYPE_FEATURES + ALPHA_TYPE_FEATURES

# Plot styling — publication quality, colorblind-friendly (Wong 2011)
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

COLORS = {
    "feature":     "#0072B2",  # Blue — feature proxy
    "adoption":    "#D55E00",  # Vermilion — raw adoption
    "pe_original": "#009E73",  # Teal — original O/R/alpha Pe
    "O_type":      "#E69F00",  # Orange
    "R_type":      "#56B4E9",  # Sky blue
    "alpha_type":  "#CC79A7",  # Pink
    "sadness":     "#CC79A7",  # Pink
    "suicide":     "#E69F00",  # Orange
    "highlight":   "#F0E442",  # Yellow
}


# ---------------------------------------------------------------------------
# Original O/R/alpha Pe computation (for comparison only)
# ---------------------------------------------------------------------------

B_A = 0.867
B_G = math.pi / math.sqrt(2)  # ~2.2214
K_DEFAULT = 16


def compute_original_pe_proxy(O, R, alpha):
    """Linear Pe proxy from the original analysis: O + R + alpha (0-9 scale)."""
    return O + R + alpha


# ---------------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------------

def load_feature_matrix(filepath=None):
    """
    Load the feature matrix JSON file.

    Returns
    -------
    dict
        Nested dict: platform -> year -> {features: {...}, adoption_pct: float}
    """
    if filepath is None:
        filepath = SCRIPT_DIR / "feature-matrix.json"

    with open(filepath) as f:
        raw = json.load(f)

    platforms = {}
    for platform_name, year_data in raw["platforms"].items():
        platforms[platform_name] = {}
        for yr_str, data in year_data.items():
            yr = int(yr_str)
            platforms[platform_name][yr] = {
                "features": data["features"],
                "adoption_pct": data["adoption_pct"] / 100.0,  # Convert to fraction
            }

    return platforms, raw.get("metadata", {})


def load_yrbs_data(filepath=None):
    """
    Load YRBS mental health trend data from CSV.

    Returns
    -------
    pd.DataFrame
        Columns: Year, plus mental health outcome columns.
    """
    if filepath is None:
        filepath = SCRIPT_DIR / "yrbs-trend-data.csv"

    df = pd.read_csv(filepath)

    # Standardize column names for the outcomes we analyze
    # Map from CSV columns to our internal names
    col_map = {
        "Year": "year",
        "Persistent_Sadness_Hopelessness_Total": "sadness",
        "Considered_Suicide_Total": "suicide_considered",
        "Suicide_Plan_Total": "suicide_plan",
        "Attempted_Suicide_Total": "suicide_attempt",
        "Electronic_Bullying_Total": "cyberbullying",
        "Persistent_Sadness_Female": "sadness_female",
    }

    df = df.rename(columns=col_map)

    # Keep only YRBS years we have feature data for
    df = df[df["year"].isin(YRBS_YEARS)].copy()
    df = df.sort_values("year").reset_index(drop=True)

    return df


def load_original_platform_data():
    """
    Load the original O/R/alpha platform data from analysis.py's built-in
    sample data (for comparison). This uses the SAME data that analysis.py
    uses internally.

    Returns
    -------
    dict
        platform -> year -> {O, R, alpha, adoption_pct}
    """
    # Reproduce the original analysis.py sample data exactly
    return {
        "facebook": {
            2011: {"O": 1.5, "R": 1.5, "alpha": 2.0, "adoption_pct": 0.77},
            2013: {"O": 2.0, "R": 2.0, "alpha": 2.5, "adoption_pct": 0.71},
            2015: {"O": 2.0, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.51},
            2017: {"O": 2.5, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.51},
            2019: {"O": 2.5, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.32},
            2021: {"O": 2.5, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.27},
            2023: {"O": 2.5, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.23},
        },
        "instagram": {
            2011: {"O": 0.5, "R": 1.0, "alpha": 1.5, "adoption_pct": 0.01},
            2013: {"O": 0.5, "R": 1.5, "alpha": 2.0, "adoption_pct": 0.11},
            2015: {"O": 1.0, "R": 2.0, "alpha": 2.5, "adoption_pct": 0.52},
            2017: {"O": 2.5, "R": 2.5, "alpha": 3.0, "adoption_pct": 0.72},
            2019: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.72},
            2021: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.62},
            2023: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.59},
        },
        "youtube": {
            2011: {"O": 1.0, "R": 1.0, "alpha": 1.0, "adoption_pct": 0.60},
            2013: {"O": 2.0, "R": 2.0, "alpha": 1.5, "adoption_pct": 0.70},
            2015: {"O": 2.0, "R": 2.5, "alpha": 1.5, "adoption_pct": 0.75},
            2017: {"O": 2.5, "R": 2.5, "alpha": 2.0, "adoption_pct": 0.85},
            2019: {"O": 2.5, "R": 3.0, "alpha": 2.0, "adoption_pct": 0.85},
            2021: {"O": 3.0, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.95},
            2023: {"O": 3.0, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.93},
        },
        "tiktok": {
            2011: {"O": 0.0, "R": 0.0, "alpha": 0.0, "adoption_pct": 0.00},
            2013: {"O": 0.0, "R": 0.0, "alpha": 0.0, "adoption_pct": 0.00},
            2015: {"O": 0.0, "R": 0.0, "alpha": 0.0, "adoption_pct": 0.00},
            2017: {"O": 3.0, "R": 3.0, "alpha": 2.0, "adoption_pct": 0.05},
            2019: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.25},
            2021: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.67},
            2023: {"O": 3.0, "R": 3.0, "alpha": 3.0, "adoption_pct": 0.63},
        },
        "snapchat": {
            2011: {"O": 0.0, "R": 0.0, "alpha": 0.0, "adoption_pct": 0.00},
            2013: {"O": 1.5, "R": 2.0, "alpha": 2.0, "adoption_pct": 0.02},
            2015: {"O": 2.0, "R": 2.0, "alpha": 2.5, "adoption_pct": 0.41},
            2017: {"O": 2.0, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.69},
            2019: {"O": 2.0, "R": 2.5, "alpha": 2.5, "adoption_pct": 0.69},
            2021: {"O": 2.5, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.59},
            2023: {"O": 2.5, "R": 3.0, "alpha": 2.5, "adoption_pct": 0.51},
        },
    }


# ---------------------------------------------------------------------------
# Exposure Computation
# ---------------------------------------------------------------------------

def compute_feature_score(features):
    """
    Compute raw (unweighted) feature score = sum of all 13 feature values.

    Parameters
    ----------
    features : dict
        Feature name -> value (0/1 for binary, 0/1/2 for ordinal).

    Returns
    -------
    int
        Sum of all feature values. Range: 0 to 21 (theoretical max:
        4*2 + 2*2 + 2*1 + 2*2 + 2*1 + 1 = 8+4+2+4+2+1 = 21).
    """
    return sum(features.get(f, 0) for f in ALL_FEATURES)


def compute_category_scores(features):
    """
    Compute feature scores broken down by O/R/alpha category.

    Returns
    -------
    dict with keys 'O', 'R', 'alpha', each containing the category subtotal.
    """
    O_score = sum(features.get(f, 0) for f in O_TYPE_FEATURES)
    R_score = sum(features.get(f, 0) for f in R_TYPE_FEATURES)
    alpha_score = sum(features.get(f, 0) for f in ALPHA_TYPE_FEATURES)
    return {"O": O_score, "R": R_score, "alpha": alpha_score}


def compute_all_exposures(platform_data, yrbs_years):
    """
    For each YRBS year, compute:
      - feature_exposure: SUM(adoption_pct * feature_score) across platforms
      - raw_adoption: SUM(adoption_pct) across platforms
      - O_exposure, R_exposure, alpha_exposure: category-specific exposures
      - Per-feature weighted exposures (for data-driven analysis)

    Parameters
    ----------
    platform_data : dict
        Platform -> year -> {features, adoption_pct}
    yrbs_years : list of int

    Returns
    -------
    pd.DataFrame
        One row per YRBS year with all computed exposure metrics.
    """
    rows = []
    platforms = sorted(platform_data.keys())

    for year in yrbs_years:
        row = {"year": year}
        feature_exp = 0.0
        raw_adopt = 0.0
        O_exp = 0.0
        R_exp = 0.0
        alpha_exp = 0.0
        per_feature_exp = {f: 0.0 for f in ALL_FEATURES}

        for platform in platforms:
            if year not in platform_data[platform]:
                continue

            data = platform_data[platform][year]
            adoption = data["adoption_pct"]
            features = data["features"]

            # Feature score (unweighted sum of all features)
            fs = compute_feature_score(features)
            feature_exp += adoption * fs

            # Raw adoption
            raw_adopt += adoption

            # Category scores
            cats = compute_category_scores(features)
            O_exp += adoption * cats["O"]
            R_exp += adoption * cats["R"]
            alpha_exp += adoption * cats["alpha"]

            # Per-feature weighted exposure
            for f in ALL_FEATURES:
                per_feature_exp[f] += adoption * features.get(f, 0)

        row["feature_exposure"] = feature_exp
        row["raw_adoption"] = raw_adopt
        row["O_exposure"] = O_exp
        row["R_exposure"] = R_exp
        row["alpha_exposure"] = alpha_exp
        for f in ALL_FEATURES:
            row[f"feat_{f}"] = per_feature_exp[f]

        rows.append(row)

    return pd.DataFrame(rows)


def compute_original_pe_exposure(original_data, yrbs_years):
    """
    Compute original O/R/alpha-based Pe exposure for comparison.

    Returns
    -------
    dict
        year -> pe_exposure value (using the 5 original platforms only)
    """
    pe_by_year = {}
    for year in yrbs_years:
        pe_exp = 0.0
        for platform, year_data in original_data.items():
            if year not in year_data:
                continue
            d = year_data[year]
            pe_proxy = compute_original_pe_proxy(d["O"], d["R"], d["alpha"])
            pe_exp += d["adoption_pct"] * pe_proxy
        pe_by_year[year] = pe_exp
    return pe_by_year


# ---------------------------------------------------------------------------
# Regression Analyses
# ---------------------------------------------------------------------------

def ols_regression(x, y):
    """
    Simple OLS regression with full statistics.

    Returns
    -------
    dict with slope, intercept, r, r_squared, p, se
    """
    slope, intercept, r, p, se = stats.linregress(x, y)
    return {
        "slope": slope,
        "intercept": intercept,
        "r": r,
        "r_squared": r ** 2,
        "p": p,
        "se": se,
    }


def multiple_ols(X, y):
    """
    Multiple OLS regression (X should NOT include intercept column).

    Returns
    -------
    dict with betas, r_squared, r_squared_adj, residuals
    """
    n = len(y)
    k = X.shape[1]
    X_with_intercept = np.column_stack([np.ones(n), X])
    beta, residuals, rank, sv = np.linalg.lstsq(X_with_intercept, y, rcond=None)
    y_pred = X_with_intercept @ beta
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    # Adjusted R-squared: penalize for number of predictors
    r2_adj = 1.0 - (1.0 - r2) * (n - 1) / (n - k - 1) if n > k + 1 else r2
    return {
        "betas": beta,  # [intercept, beta_1, ..., beta_k]
        "r_squared": r2,
        "r_squared_adj": r2_adj,
        "y_pred": y_pred,
        "residuals": y - y_pred,
    }


def run_all_regressions(df, outcome_col, outcome_label):
    """
    Run the full suite of regression analyses for one mental health outcome.

    Models:
      A: outcome ~ feature_exposure (new feature proxy)
      B: outcome ~ raw_adoption (baseline — no feature weighting)
      C: outcome ~ original_pe_exposure (original O/R/alpha scoring)
      D: outcome ~ O_exposure + R_exposure + alpha_exposure (category)

    Returns
    -------
    dict with all regression results
    """
    y = df[outcome_col].values.astype(float)
    feat = df["feature_exposure"].values
    raw = df["raw_adoption"].values
    pe_orig = df["original_pe_exposure"].values
    n = len(y)

    results = {"outcome": outcome_label, "outcome_col": outcome_col, "n": n}

    # Model A: feature proxy
    results["model_A"] = ols_regression(feat, y)
    results["model_A"]["name"] = "Feature exposure (unweighted)"

    # Model B: raw adoption
    results["model_B"] = ols_regression(raw, y)
    results["model_B"]["name"] = "Raw adoption"

    # Model C: original O/R/alpha Pe
    results["model_C"] = ols_regression(pe_orig, y)
    results["model_C"]["name"] = "Original O/R/alpha Pe"

    # Model D: category breakdown (O + R + alpha as separate predictors)
    O_exp = df["O_exposure"].values
    R_exp = df["R_exposure"].values
    alpha_exp = df["alpha_exposure"].values
    X_cat = np.column_stack([O_exp, R_exp, alpha_exp])
    results["model_D"] = multiple_ols(X_cat, y)
    results["model_D"]["name"] = "Category breakdown (O + R + alpha)"
    results["model_D"]["predictor_names"] = ["O_exposure", "R_exposure", "alpha_exposure"]

    # Delta R-squared: feature proxy vs raw adoption (the critical test)
    results["dR2_feat_vs_raw"] = (
        results["model_A"]["r_squared"] - results["model_B"]["r_squared"]
    )

    # Delta R-squared: feature proxy vs original Pe
    results["dR2_feat_vs_pe"] = (
        results["model_A"]["r_squared"] - results["model_C"]["r_squared"]
    )

    # Spearman correlations (rank-based, guards against nonlinearity)
    rho_feat, sp_feat = stats.spearmanr(feat, y)
    rho_raw, sp_raw = stats.spearmanr(raw, y)
    rho_pe, sp_pe = stats.spearmanr(pe_orig, y)
    results["spearman_feature"] = {"rho": rho_feat, "p": sp_feat}
    results["spearman_raw"] = {"rho": rho_raw, "p": sp_raw}
    results["spearman_pe_orig"] = {"rho": rho_pe, "p": sp_pe}

    return results


# ---------------------------------------------------------------------------
# Data-Driven Feature Weighting
# ---------------------------------------------------------------------------

def data_driven_feature_analysis(df, outcome_col, outcome_label):
    """
    Regress each mental health outcome on individual feature-weighted exposures
    to find which features are most predictive.

    For each of the 13 features, we have:
      feat_{feature_name} = SUM_platforms(adoption_pct * feature_value)

    We compute:
      1. Individual correlations (feature by feature)
      2. Category-level analysis (sum of O-type, R-type, alpha-type)
      3. Best single-feature model

    Parameters
    ----------
    df : pd.DataFrame
        Must contain feat_* columns and the outcome column.
    outcome_col : str
    outcome_label : str

    Returns
    -------
    dict with per-feature correlations and category analysis
    """
    y = df[outcome_col].values.astype(float)
    results = {"outcome": outcome_label, "outcome_col": outcome_col}

    # Per-feature correlations
    feature_corrs = []
    for f in ALL_FEATURES:
        col = f"feat_{f}"
        x = df[col].values
        if np.std(x) < 1e-10:
            # Feature has no variance — skip
            feature_corrs.append({
                "feature": f,
                "category": _feature_category(f),
                "r": 0.0,
                "r_squared": 0.0,
                "p": 1.0,
                "note": "zero variance",
            })
            continue

        reg = ols_regression(x, y)
        feature_corrs.append({
            "feature": f,
            "category": _feature_category(f),
            "r": reg["r"],
            "r_squared": reg["r_squared"],
            "p": reg["p"],
        })

    # Sort by R-squared (most predictive first)
    feature_corrs.sort(key=lambda x: x["r_squared"], reverse=True)
    results["feature_correlations"] = feature_corrs

    # Category dominance: average R-squared by category
    for cat in ["O", "R", "alpha"]:
        cat_features = [fc for fc in feature_corrs if fc["category"] == cat]
        if cat_features:
            avg_r2 = np.mean([fc["r_squared"] for fc in cat_features])
            max_r2 = max(fc["r_squared"] for fc in cat_features)
            best_f = max(cat_features, key=lambda x: x["r_squared"])["feature"]
        else:
            avg_r2 = 0.0
            max_r2 = 0.0
            best_f = "none"
        results[f"category_{cat}"] = {
            "avg_r_squared": avg_r2,
            "max_r_squared": max_r2,
            "best_feature": best_f,
            "n_features": len(cat_features),
        }

    return results


def _feature_category(feature_name):
    """Return 'O', 'R', or 'alpha' for a given feature name."""
    if feature_name in O_TYPE_FEATURES:
        return "O"
    elif feature_name in R_TYPE_FEATURES:
        return "R"
    elif feature_name in ALPHA_TYPE_FEATURES:
        return "alpha"
    return "unknown"


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_feature_three_model_comparison(df, all_results):
    """
    Figure 1: Bar chart comparing R-squared across three models:
      - Feature exposure (new)
      - Raw adoption (baseline)
      - Original O/R/alpha Pe (circular comparison)
    For each mental health outcome.
    """
    outcomes = [r["outcome"] for r in all_results]
    r2_feat = [r["model_A"]["r_squared"] for r in all_results]
    r2_raw = [r["model_B"]["r_squared"] for r in all_results]
    r2_pe = [r["model_C"]["r_squared"] for r in all_results]

    x = np.arange(len(outcomes))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar(x - width, r2_feat, width, label="Feature proxy (non-circular)",
                   color=COLORS["feature"], edgecolor="white", linewidth=0.5)
    bars2 = ax.bar(x, r2_raw, width, label="Raw adoption (baseline)",
                   color=COLORS["adoption"], edgecolor="white", linewidth=0.5)
    bars3 = ax.bar(x + width, r2_pe, width, label="Original O/R/alpha Pe",
                   color=COLORS["pe_original"], edgecolor="white", linewidth=0.5)

    # Delta annotations (feature vs raw)
    for i in range(len(outcomes)):
        d = r2_feat[i] - r2_raw[i]
        sign = "+" if d > 0 else ""
        color = "#006400" if d > 0 else "#8B0000"
        ypos = max(r2_feat[i], r2_raw[i], r2_pe[i]) + 0.02
        ax.annotate(f"dR2={sign}{d:.3f}", xy=(i - width/2, ypos),
                    ha="center", fontsize=8, fontweight="bold", color=color)

    ax.set_ylabel("R-squared")
    ax.set_title(
        "Three-Model Comparison: Feature Proxy vs. Raw Adoption vs. Original Pe\n"
        "Predicting Adolescent Mental Health Outcomes (CDC YRBS 2011-2023)",
        fontsize=13, fontweight="bold"
    )
    ax.set_xticks(x)
    ax.set_xticklabels(outcomes, rotation=20, ha="right", fontsize=9)
    ax.legend(loc="upper left")
    ax.set_ylim(0, max(max(r2_feat), max(r2_raw), max(r2_pe)) * 1.3)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.2f"))

    fig.tight_layout()
    outpath = FIGURES_DIR / "feature_three_model_comparison.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


def plot_feature_time_series(df):
    """
    Figure 2: Time series — feature exposure, raw adoption, and original Pe
    overlaid with sadness outcome.
    """
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # Left axis: exposure metrics (normalized to comparable scales)
    feat_norm = df["feature_exposure"] / df["feature_exposure"].max()
    raw_norm = df["raw_adoption"] / df["raw_adoption"].max()
    pe_norm = df["original_pe_exposure"] / df["original_pe_exposure"].max()

    ax1.plot(df["year"], feat_norm, "o-", color=COLORS["feature"],
             linewidth=2.5, markersize=8, label="Feature exposure (normalized)")
    ax1.plot(df["year"], raw_norm, "s--", color=COLORS["adoption"],
             linewidth=1.5, markersize=6, alpha=0.7, label="Raw adoption (normalized)")
    ax1.plot(df["year"], pe_norm, "^--", color=COLORS["pe_original"],
             linewidth=1.5, markersize=6, alpha=0.7, label="Original Pe (normalized)")
    ax1.set_xlabel("YRBS Survey Year")
    ax1.set_ylabel("Normalized Exposure (0-1)", color="#333333")
    ax1.set_ylim(0, 1.15)

    # Right axis: mental health
    ax2 = ax1.twinx()
    ax2.plot(df["year"], df["sadness"], "D-", color=COLORS["sadness"],
             linewidth=2, markersize=7, label="Persistent sadness (%)")
    ax2.set_ylabel("% of Students", color=COLORS["sadness"])
    ax2.tick_params(axis="y", labelcolor=COLORS["sadness"])

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", framealpha=0.9)

    ax1.set_title(
        "Feature Exposure vs. Adolescent Sadness/Hopelessness (2011-2023)\n"
        "Comparing non-circular feature proxy with raw adoption and original Pe",
        fontsize=13, fontweight="bold"
    )
    ax1.set_xticks(df["year"])

    fig.tight_layout()
    outpath = FIGURES_DIR / "feature_time_series.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


def plot_feature_scatter(df, all_results):
    """
    Figure 3: Scatter plots — feature exposure vs each outcome, with regression
    lines and R-squared annotations.
    """
    n_outcomes = len(all_results)
    n_cols = min(3, n_outcomes)
    n_rows = math.ceil(n_outcomes / n_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 5 * n_rows))
    if n_outcomes == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i, res in enumerate(all_results):
        ax = axes[i]
        col = res["outcome_col"]
        label = res["outcome"]
        y = df[col].values.astype(float)
        feat = df["feature_exposure"].values

        ax.scatter(feat, y, color=COLORS["feature"], s=60, zorder=5,
                   edgecolors="white", linewidth=0.5)

        # Year labels
        for _, row in df.iterrows():
            ax.annotate(str(int(row["year"])),
                        (row["feature_exposure"], row[col]),
                        textcoords="offset points", xytext=(6, 4),
                        fontsize=7, color="#888")

        # Regression line
        m = res["model_A"]
        x_line = np.linspace(feat.min() * 0.95, feat.max() * 1.05, 100)
        y_line = m["slope"] * x_line + m["intercept"]
        ax.plot(x_line, y_line, "-", color=COLORS["feature"], alpha=0.5, linewidth=1.5)

        ax.text(0.05, 0.95,
                f"r = {m['r']:.3f}\nR$^2$ = {m['r_squared']:.3f}\np = {m['p']:.4f}",
                transform=ax.transAxes, fontsize=9, verticalalignment="top",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

        ax.set_xlabel("Feature Exposure (adoption-weighted)")
        ax.set_ylabel(f"% Students")
        ax.set_title(label, fontsize=11)

    for j in range(n_outcomes, len(axes)):
        axes[j].set_visible(False)

    fig.suptitle(
        "Feature Exposure vs. Mental Health Outcomes\n(Non-Circular Feature Proxy)",
        fontsize=14, fontweight="bold", y=1.02
    )
    fig.tight_layout()
    outpath = FIGURES_DIR / "feature_scatter_outcomes.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


def plot_feature_importance(feature_analyses, primary_outcome="sadness"):
    """
    Figure 4: Horizontal bar chart of individual feature R-squared values,
    color-coded by category (O/R/alpha).

    Shows which individual features are most predictive of the primary outcome.
    """
    # Use the primary outcome (sadness)
    analysis = None
    for fa in feature_analyses:
        if fa["outcome_col"] == primary_outcome:
            analysis = fa
            break
    if analysis is None:
        analysis = feature_analyses[0]

    corrs = analysis["feature_correlations"]
    features = [c["feature"] for c in corrs]
    r_squareds = [c["r_squared"] for c in corrs]
    categories = [c["category"] for c in corrs]

    cat_colors = {"O": COLORS["O_type"], "R": COLORS["R_type"],
                  "alpha": COLORS["alpha_type"]}
    colors = [cat_colors.get(c, "#999999") for c in categories]

    fig, ax = plt.subplots(figsize=(10, 8))
    y_pos = np.arange(len(features))
    bars = ax.barh(y_pos, r_squareds, color=colors, edgecolor="white", linewidth=0.5)

    # Feature labels (cleaned up)
    clean_labels = [f.replace("_", " ").title() for f in features]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(clean_labels, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel("R-squared (individual feature vs. outcome)")

    # R-squared value annotations
    for i, (bar, r2) in enumerate(zip(bars, r_squareds)):
        ax.text(bar.get_width() + 0.005, bar.get_y() + bar.get_height() / 2,
                f"{r2:.3f}", va="center", fontsize=8)

    # Category legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=COLORS["O_type"], label="O-type (Opacity)"),
        Patch(facecolor=COLORS["R_type"], label="R-type (Reactivity)"),
        Patch(facecolor=COLORS["alpha_type"], label="alpha-type (Coupling)"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=10)

    ax.set_title(
        f"Individual Feature Predictive Power: {analysis['outcome']}\n"
        f"(Adoption-weighted feature exposure vs. mental health outcome)",
        fontsize=13, fontweight="bold"
    )

    fig.tight_layout()
    outpath = FIGURES_DIR / "feature_importance_by_category.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


def plot_category_dominance(feature_analyses):
    """
    Figure 5: Grouped bar chart showing average R-squared by category
    (O/R/alpha) across all mental health outcomes.

    Tests framework prediction: O-type features should dominate.
    """
    outcomes = [fa["outcome"] for fa in feature_analyses]
    O_scores = [fa["category_O"]["avg_r_squared"] for fa in feature_analyses]
    R_scores = [fa["category_R"]["avg_r_squared"] for fa in feature_analyses]
    alpha_scores = [fa["category_alpha"]["avg_r_squared"] for fa in feature_analyses]

    x = np.arange(len(outcomes))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x - width, O_scores, width, label="O-type (Opacity)",
           color=COLORS["O_type"], edgecolor="white")
    ax.bar(x, R_scores, width, label="R-type (Reactivity)",
           color=COLORS["R_type"], edgecolor="white")
    ax.bar(x + width, alpha_scores, width, label="alpha-type (Coupling)",
           color=COLORS["alpha_type"], edgecolor="white")

    ax.set_ylabel("Average R-squared (within category)")
    ax.set_title(
        "Category Dominance: Which Feature Type Best Predicts Mental Health Harm?\n"
        "(Framework predicts O-type / Opacity features should dominate)",
        fontsize=13, fontweight="bold"
    )
    ax.set_xticks(x)
    ax.set_xticklabels(outcomes, rotation=20, ha="right", fontsize=9)
    ax.legend(loc="upper right")
    ax.set_ylim(0, max(max(O_scores), max(R_scores), max(alpha_scores)) * 1.3)

    fig.tight_layout()
    outpath = FIGURES_DIR / "feature_category_dominance.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


def plot_platform_feature_heatmap(platform_data, year=2023):
    """
    Figure 6: Heatmap of platform features for a single year.
    Shows which platforms have which features, visually demonstrating
    the TikTok/Instagram cluster vs. messaging/anti-engagement baselines.
    """
    platforms_order = [
        "tiktok", "instagram", "youtube", "snapchat", "facebook",
        "twitter_x", "discord", "bereal", "whatsapp", "imessage"
    ]

    # Build matrix
    matrix = []
    platform_labels = []
    for p in platforms_order:
        if p not in platform_data or year not in platform_data[p]:
            continue
        features = platform_data[p][year]["features"]
        row = [features.get(f, 0) for f in ALL_FEATURES]
        matrix.append(row)
        label = p.replace("_", "/").title()
        if p == "twitter_x":
            label = "Twitter/X"
        elif p == "imessage":
            label = "iMessage"
        elif p == "bereal":
            label = "BeReal"
        platform_labels.append(label)

    matrix = np.array(matrix, dtype=float)

    fig, ax = plt.subplots(figsize=(14, 7))
    im = ax.imshow(matrix, cmap="YlOrRd", aspect="auto", vmin=0, vmax=2)

    # Labels
    feature_labels = [f.replace("_", "\n").title() for f in ALL_FEATURES]
    ax.set_xticks(np.arange(len(ALL_FEATURES)))
    ax.set_xticklabels(feature_labels, fontsize=7, rotation=45, ha="right")
    ax.set_yticks(np.arange(len(platform_labels)))
    ax.set_yticklabels(platform_labels, fontsize=10)

    # Value annotations
    for i in range(len(platform_labels)):
        for j in range(len(ALL_FEATURES)):
            val = matrix[i, j]
            color = "white" if val >= 1.5 else "black"
            ax.text(j, i, f"{int(val)}", ha="center", va="center",
                    fontsize=8, color=color, fontweight="bold")

    # Category separators
    ax.axvline(x=3.5, color="black", linewidth=2)  # After O-type
    ax.axvline(x=7.5, color="black", linewidth=2)  # After R-type

    # Category labels
    ax.text(1.5, -0.8, "OPACITY", ha="center", fontsize=10,
            fontweight="bold", color=COLORS["O_type"])
    ax.text(5.5, -0.8, "REACTIVITY", ha="center", fontsize=10,
            fontweight="bold", color=COLORS["R_type"])
    ax.text(10.5, -0.8, "COUPLING", ha="center", fontsize=10,
            fontweight="bold", color=COLORS["alpha_type"])

    plt.colorbar(im, ax=ax, label="Feature value (0=absent, 1=partial, 2=full)",
                 shrink=0.6)

    ax.set_title(
        f"Platform Design Feature Matrix ({year})\n"
        f"Higher values (darker) = more engagement-optimized design",
        fontsize=13, fontweight="bold"
    )

    fig.tight_layout()
    outpath = FIGURES_DIR / f"feature_platform_heatmap_{year}.png"
    fig.savefig(outpath)
    plt.close(fig)
    print(f"  Saved: {outpath}")
    return outpath


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_exposure_table(df):
    """Print the computed exposure metrics per year."""
    print()
    print(f"  {'Year':<6}  {'Feature':>10}  {'Raw Adopt':>10}  "
          f"{'O-exp':>8}  {'R-exp':>8}  {'a-exp':>8}  "
          f"{'Orig Pe':>10}")
    print(f"  {'':_<6}  {'_Exposure':_>10}  {'_ion':_>10}  "
          f"{'':_>8}  {'':_>8}  {'':_>8}  "
          f"{'_Exposure':_>10}")
    for _, row in df.iterrows():
        print(f"  {int(row['year']):<6}  {row['feature_exposure']:>10.2f}  "
              f"{row['raw_adoption']:>10.2f}  "
              f"{row['O_exposure']:>8.2f}  {row['R_exposure']:>8.2f}  "
              f"{row['alpha_exposure']:>8.2f}  "
              f"{row['original_pe_exposure']:>10.2f}")
    print()


def print_regression_results(all_results):
    """Print detailed regression results for all outcomes."""
    for res in all_results:
        print()
        print("-" * 76)
        print(f"  OUTCOME: {res['outcome']}  (N = {res['n']} YRBS time points)")
        print("-" * 76)

        for model_key, model_label in [
            ("model_A", "Feature proxy (non-circular)"),
            ("model_B", "Raw adoption (baseline)"),
            ("model_C", "Original O/R/alpha Pe"),
        ]:
            m = res[model_key]
            print(f"\n  Model: {model_label}")
            print(f"    r         = {m['r']:+.4f}")
            print(f"    R-squared = {m['r_squared']:.4f}")
            print(f"    p-value   = {m['p']:.5f}")
            print(f"    slope     = {m['slope']:.4f}")

        # Category model
        md = res["model_D"]
        print(f"\n  Model: Category breakdown (O + R + alpha as 3 predictors)")
        print(f"    R-squared     = {md['r_squared']:.4f}")
        print(f"    R-squared adj = {md['r_squared_adj']:.4f}")
        for j, name in enumerate(md["predictor_names"]):
            print(f"    beta_{name:<14} = {md['betas'][j+1]:+.4f}")

        # Spearman
        print(f"\n  Spearman rank correlations:")
        sf = res["spearman_feature"]
        sr = res["spearman_raw"]
        sp = res["spearman_pe_orig"]
        print(f"    Feature vs outcome:  rho = {sf['rho']:+.4f}  (p = {sf['p']:.4f})")
        print(f"    Raw vs outcome:      rho = {sr['rho']:+.4f}  (p = {sr['p']:.4f})")
        print(f"    Orig Pe vs outcome:  rho = {sp['rho']:+.4f}  (p = {sp['p']:.4f})")

        # Critical tests
        d1 = res["dR2_feat_vs_raw"]
        d2 = res["dR2_feat_vs_pe"]
        sign1 = "+" if d1 > 0 else ""
        sign2 = "+" if d2 > 0 else ""
        print(f"\n  CRITICAL TESTS:")
        print(f"    dR2 (feature vs raw):     {sign1}{d1:.4f}  "
              f"{'[PASS]' if d1 > 0 else '[FAIL]'}")
        print(f"    dR2 (feature vs orig Pe): {sign2}{d2:.4f}  "
              f"{'[feature > Pe]' if d2 > 0 else '[Pe > feature]'}")


def print_summary_table(all_results):
    """Print a compact summary table."""
    print()
    print("=" * 110)
    print("SUMMARY TABLE")
    print("=" * 110)
    print()
    header = (
        f"{'Outcome':<30}  "
        f"{'R2(feat)':<10}  {'R2(raw)':<10}  {'R2(Pe)':<10}  "
        f"{'dR2(f-r)':<10}  {'dR2(f-Pe)':<10}  "
        f"{'rho(feat)':<10}"
    )
    print(header)
    print("-" * len(header))

    for res in all_results:
        ma = res["model_A"]
        mb = res["model_B"]
        mc = res["model_C"]
        sf = res["spearman_feature"]
        d1 = res["dR2_feat_vs_raw"]
        d2 = res["dR2_feat_vs_pe"]
        print(
            f"{res['outcome']:<30}  "
            f"{ma['r_squared']:>9.4f}  {mb['r_squared']:>9.4f}  "
            f"{mc['r_squared']:>9.4f}  "
            f"{d1:>+9.4f}  {d2:>+9.4f}  "
            f"{sf['rho']:>+9.4f}"
        )

    print()
    print("  R2(feat)  = R-squared for outcome ~ feature_exposure")
    print("  R2(raw)   = R-squared for outcome ~ raw_adoption")
    print("  R2(Pe)    = R-squared for outcome ~ original O/R/alpha Pe")
    print("  dR2(f-r)  = R2(feat) - R2(raw) — positive = feature proxy better")
    print("  dR2(f-Pe) = R2(feat) - R2(Pe) — positive = feature proxy better")
    print("  rho(feat) = Spearman rank correlation (feature vs outcome)")
    print()


def print_feature_importance(feature_analyses):
    """Print the data-driven feature ranking."""
    print()
    print("=" * 90)
    print("DATA-DRIVEN FEATURE IMPORTANCE")
    print("=" * 90)

    for fa in feature_analyses:
        print(f"\n  Outcome: {fa['outcome']}")
        print(f"  {'Rank':<5}  {'Feature':<35}  {'Category':<8}  "
              f"{'R2':<8}  {'r':<8}  {'p':<8}")
        print(f"  {'----':<5}  {'-------':<35}  {'--------':<8}  "
              f"{'--':<8}  {'--':<8}  {'--':<8}")

        for rank, fc in enumerate(fa["feature_correlations"], 1):
            note = fc.get("note", "")
            print(f"  {rank:<5}  {fc['feature']:<35}  {fc['category']:<8}  "
                  f"{fc['r_squared']:.4f}  {fc['r']:+.4f}  {fc['p']:.4f}"
                  f"{'  ' + note if note else ''}")

        print(f"\n  Category averages (avg R-squared):")
        for cat in ["O", "R", "alpha"]:
            cd = fa[f"category_{cat}"]
            print(f"    {cat:<6}  avg R2 = {cd['avg_r_squared']:.4f}  "
                  f"max R2 = {cd['max_r_squared']:.4f}  "
                  f"best = {cd['best_feature']}")


# ---------------------------------------------------------------------------
# Kill Conditions
# ---------------------------------------------------------------------------

def check_kill_conditions(all_results, feature_analyses):
    """
    Check both kill conditions:

    KC-1: Feature proxy must outperform raw adoption for at least one outcome.
          If dR2 <= 0 for ALL outcomes, platform design features add nothing
          beyond raw adoption.

    KC-2: O-type features must have highest average R-squared across outcomes.
          If alpha-type or R-type dominate, the framework's prediction that
          opacity is the primary harm driver fails.

    Returns
    -------
    dict with kill condition results
    """
    print()
    print("=" * 76)
    print("KILL CONDITION CHECKS")
    print("=" * 76)

    # KC-1: Feature proxy vs raw adoption
    print("\n  KC-1: Feature proxy must outperform raw adoption")
    print("  Criterion: dR2(feature - raw) > 0 for at least one outcome")
    print()

    kc1_passed = False
    for res in all_results:
        d = res["dR2_feat_vs_raw"]
        status = "PASS" if d > 0 else "FAIL"
        if d > 0:
            kc1_passed = True
        print(f"    {res['outcome']:<30}  dR2 = {d:+.4f}  [{status}]")

    print()
    if kc1_passed:
        n_pass = sum(1 for r in all_results if r["dR2_feat_vs_raw"] > 0)
        print(f"  KC-1 SURVIVED: Feature proxy outperforms raw adoption in "
              f"{n_pass}/{len(all_results)} outcomes.")
        print(f"  Platform design features explain variance beyond raw adoption.")
    else:
        print(f"  *** KC-1 TRIGGERED: Feature proxy does NOT outperform raw adoption")
        print(f"  for ANY outcome. Platform design features add nothing.")

    # KC-2: Category dominance — O-type should be highest
    print()
    print("  KC-2: O-type features should have highest average predictive power")
    print("  (Framework prediction: opacity is the primary harm driver)")
    print()

    # Average across all outcomes
    avg_O = np.mean([fa["category_O"]["avg_r_squared"] for fa in feature_analyses])
    avg_R = np.mean([fa["category_R"]["avg_r_squared"] for fa in feature_analyses])
    avg_alpha = np.mean([fa["category_alpha"]["avg_r_squared"] for fa in feature_analyses])

    print(f"    O-type (Opacity)   avg R2 = {avg_O:.4f}")
    print(f"    R-type (Reactivity) avg R2 = {avg_R:.4f}")
    print(f"    alpha-type (Coupling) avg R2 = {avg_alpha:.4f}")
    print()

    dominant_cat = max(
        [("O", avg_O), ("R", avg_R), ("alpha", avg_alpha)],
        key=lambda x: x[1]
    )

    if dominant_cat[0] == "O":
        kc2_passed = True
        print(f"  KC-2 SURVIVED: O-type features dominate (avg R2 = {avg_O:.4f}).")
        print(f"  This is a NON-CIRCULAR confirmation that opacity features")
        print(f"  (algorithmic feeds, autoplay, opaque recommendations, hidden ranking)")
        print(f"  are the strongest predictors of adolescent mental health harm.")
    else:
        kc2_passed = False
        print(f"  *** KC-2 TRIGGERED: {dominant_cat[0]}-type features dominate "
              f"(avg R2 = {dominant_cat[1]:.4f}), not O-type ({avg_O:.4f}).")
        print(f"  The framework's prediction that opacity is the primary driver")
        print(f"  is NOT confirmed by data-driven feature analysis.")

    # Top 3 individual features across all outcomes (averaged)
    print()
    print("  Top 3 most predictive individual features (averaged across outcomes):")
    all_feature_r2 = {}
    for fa in feature_analyses:
        for fc in fa["feature_correlations"]:
            f = fc["feature"]
            if f not in all_feature_r2:
                all_feature_r2[f] = []
            all_feature_r2[f].append(fc["r_squared"])

    avg_feature_r2 = [(f, np.mean(vals), _feature_category(f))
                      for f, vals in all_feature_r2.items()]
    avg_feature_r2.sort(key=lambda x: x[1], reverse=True)

    for rank, (f, r2, cat) in enumerate(avg_feature_r2[:3], 1):
        print(f"    {rank}. {f:<35} ({cat}-type)  avg R2 = {r2:.4f}")

    top3_cats = [cat for _, _, cat in avg_feature_r2[:3]]
    o_in_top3 = sum(1 for c in top3_cats if c == "O")
    print()
    if o_in_top3 >= 2:
        print(f"  OPACITY CONFIRMATION: {o_in_top3}/3 top features are O-type.")
        print(f"  Algorithmic feeds and opaque recommendations are the operative")
        print(f"  design features, not streaks, filters, or social comparison.")
    elif o_in_top3 == 1:
        print(f"  PARTIAL: {o_in_top3}/3 top features are O-type.")
        print(f"  Opacity features are predictive but do not clearly dominate.")
    else:
        print(f"  OPACITY NOT CONFIRMED: 0/3 top features are O-type.")

    return {
        "kc1_triggered": not kc1_passed,
        "kc2_triggered": not kc2_passed,
        "dominant_category": dominant_cat[0],
        "avg_r2_by_category": {"O": avg_O, "R": avg_R, "alpha": avg_alpha},
        "top_features": avg_feature_r2[:5],
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """
    Main analysis pipeline.

    Steps:
      1. Load feature matrix and YRBS data
      2. Compute exposure metrics (feature, raw adoption, original Pe)
      3. Run regression suite for each outcome
      4. Run data-driven feature analysis
      5. Check kill conditions
      6. Generate figures
    """
    print("=" * 76)
    print("FEATURE-BASED Pe PROXY ANALYSIS — NON-CIRCULAR")
    print("Breaking the circularity: objective features replace subjective O/R/alpha")
    print("=" * 76)
    print()

    # --- Step 1: Load data ---
    print("--- STEP 1: DATA LOADING ---")
    print()

    platform_data, metadata = load_feature_matrix()
    yrbs_df = load_yrbs_data()
    original_data = load_original_platform_data()

    print(f"  Platforms (feature matrix): {sorted(platform_data.keys())}")
    print(f"  YRBS years: {sorted(yrbs_df['year'].tolist())}")
    print(f"  Features per platform: {len(ALL_FEATURES)}")
    print(f"  Feature categories: O-type ({len(O_TYPE_FEATURES)}), "
          f"R-type ({len(R_TYPE_FEATURES)}), "
          f"alpha-type ({len(ALPHA_TYPE_FEATURES)})")
    print()

    # --- Step 2: Compute exposure metrics ---
    print("--- STEP 2: EXPOSURE COMPUTATION ---")
    print()
    print("  feature_exposure = SUM_platforms [ adoption_pct * SUM(features) ]")
    print("  raw_adoption     = SUM_platforms [ adoption_pct ]")
    print("  O/R/alpha_exposure = category-specific adoption-weighted sums")
    print()

    exposure_df = compute_all_exposures(platform_data, YRBS_YEARS)

    # Add original Pe exposure for comparison
    orig_pe = compute_original_pe_exposure(original_data, YRBS_YEARS)
    exposure_df["original_pe_exposure"] = [orig_pe[y] for y in YRBS_YEARS]

    # Merge with YRBS data
    df = pd.merge(yrbs_df, exposure_df, on="year", how="inner")

    print_exposure_table(df)

    # --- Step 3: Define outcomes ---
    outcomes = [
        ("sadness", "Persistent sadness/hopelessness"),
        ("suicide_considered", "Seriously considered suicide"),
        ("suicide_plan", "Made a suicide plan"),
        ("suicide_attempt", "Attempted suicide"),
        ("cyberbullying", "Electronically bullied"),
    ]

    # Filter to outcomes that exist in the data
    available_outcomes = []
    for col, label in outcomes:
        if col in df.columns and df[col].notna().all():
            available_outcomes.append((col, label))
        else:
            print(f"  [WARN] Outcome '{col}' not available or has missing values. Skipping.")

    # Also add female sadness if available
    if "sadness_female" in df.columns and df["sadness_female"].notna().all():
        available_outcomes.append(("sadness_female", "Persistent sadness (female)"))

    # --- Step 4: Run regressions ---
    print("--- STEP 3: REGRESSION ANALYSES ---")

    all_results = []
    for col, label in available_outcomes:
        res = run_all_regressions(df, col, label)
        all_results.append(res)

    print_regression_results(all_results)
    print_summary_table(all_results)

    # --- Step 5: Data-driven feature analysis ---
    print("--- STEP 4: DATA-DRIVEN FEATURE ANALYSIS ---")

    feature_analyses = []
    for col, label in available_outcomes:
        fa = data_driven_feature_analysis(df, col, label)
        feature_analyses.append(fa)

    print_feature_importance(feature_analyses)

    # --- Step 6: Kill conditions ---
    print()
    print("--- STEP 5: KILL CONDITIONS ---")
    kc_results = check_kill_conditions(all_results, feature_analyses)

    # --- Step 7: Generate figures ---
    print()
    print("--- STEP 6: GENERATING FIGURES ---")
    print()

    plot_feature_three_model_comparison(df, all_results)
    plot_feature_time_series(df)
    plot_feature_scatter(df, all_results)
    plot_feature_importance(feature_analyses)
    plot_category_dominance(feature_analyses)
    plot_platform_feature_heatmap(platform_data, year=2023)

    # --- Final summary ---
    print()
    print("=" * 76)
    print("ANALYSIS COMPLETE")
    print("=" * 76)
    print()
    print(f"  Data points:     {len(df)} YRBS years (2011-2023)")
    print(f"  Platforms:       {len(platform_data)} (with feature data)")
    print(f"  Features:        {len(ALL_FEATURES)} binary/ordinal")
    print(f"  Outcomes tested: {len(available_outcomes)}")
    print(f"  Figures saved:   {FIGURES_DIR}/feature_*.png")
    print()

    # Results summary
    print("  RESULTS:")
    print()

    # Feature proxy vs raw adoption
    n_feat_wins = sum(1 for r in all_results if r["dR2_feat_vs_raw"] > 0)
    avg_dR2 = np.mean([r["dR2_feat_vs_raw"] for r in all_results])
    print(f"  Feature proxy outperforms raw adoption: "
          f"{n_feat_wins}/{len(all_results)} outcomes (avg dR2 = {avg_dR2:+.4f})")

    # Feature proxy vs original Pe
    n_feat_vs_pe = sum(1 for r in all_results if r["dR2_feat_vs_pe"] > 0)
    avg_dR2_pe = np.mean([r["dR2_feat_vs_pe"] for r in all_results])
    print(f"  Feature proxy vs original Pe:           "
          f"{n_feat_vs_pe}/{len(all_results)} outcomes (avg dR2 = {avg_dR2_pe:+.4f})")

    # Category dominance
    dom = kc_results["dominant_category"]
    dom_r2 = kc_results["avg_r2_by_category"][dom]
    print(f"  Dominant feature category: {dom}-type (avg R2 = {dom_r2:.4f})")

    # Top features
    print(f"  Top predictive features:")
    for rank, (f, r2, cat) in enumerate(kc_results["top_features"][:3], 1):
        print(f"    {rank}. {f} ({cat}-type, avg R2 = {r2:.4f})")

    # Kill conditions
    print()
    if kc_results["kc1_triggered"]:
        print("  *** KILL CONDITION 1 TRIGGERED: Feature proxy does NOT outperform")
        print("  raw adoption. Platform design does not matter beyond adoption rates.")
    else:
        print("  KC-1 SURVIVED: Feature proxy outperforms raw adoption.")

    if kc_results["kc2_triggered"]:
        print(f"  *** KILL CONDITION 2 TRIGGERED: {dom}-type features dominate,")
        print("  not O-type. Opacity is NOT the primary harm driver.")
    else:
        print("  KC-2 SURVIVED: O-type features dominate. Opacity drives harm.")

    print()
    print("  IMPORTANT CAVEATS:")
    print("  1. N=7 (YRBS time points). Small sample — signal detection only.")
    print("  2. Ecological correlation, not individual-level causal analysis.")
    print("  3. Feature coding involves boundary judgments (mitigated by binary/ordinal).")
    print("  4. Some adoption rates estimated (flagged in feature-matrix.json).")
    print("  5. This analysis includes 10 platforms (vs. 5 in original). The additional")
    print("     platforms (Twitter/X, BeReal, Discord, WhatsApp, iMessage) serve as")
    print("     low-feature baselines that help distinguish design from adoption.")
    print()


if __name__ == "__main__":
    main()
