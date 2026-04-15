#!/usr/bin/env python3
"""
State-Level Difference-in-Differences Analysis
===============================================
Protocol A — Paper 173, §5.1

Tests whether US states with higher effective platform exposure (Pe proxy)
show larger increases in teen mental health outcomes, controlling for state
and year fixed effects.

Model:  Sadness_st = α_s + γ_t + β·Pe_st + δ·X_st + ε_st

Data inputs:
  - state_yrbs_data.csv         (state, year, sex, pct_sadness, pct_suicide, n_respondents)
  - state_covariates.csv        (state, year, broadband_pct, urban_pct, median_income, unemployment_rate)
  - feature-matrix.json         (13 binary/ordinal platform design features by platform-year)
  - platform-pe-timeline.json   (national adoption rates by platform-year)

Output:
  - state_level_did_results.json

Usage:
  python state_level_did_analysis.py

Author: MoreRight DAO / Protocol A
Date: 2026-04-06
"""

import json
import os
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent

FEATURE_MATRIX_PATH = SCRIPT_DIR / "feature-matrix.json"
PE_TIMELINE_PATH = SCRIPT_DIR / "platform-pe-timeline.json"
STATE_YRBS_PATH = SCRIPT_DIR / "state-yrbs" / "state_yrbs_combined.csv"
STATE_COVARIATES_PATH = SCRIPT_DIR / "state-covariates" / "state_covariates_merged.csv"
NATIONAL_YRBS_PATH = SCRIPT_DIR / "yrbs-trend-data.csv"
OUTPUT_PATH = SCRIPT_DIR / "state_level_did_results.json"

YRBS_YEARS = [2011, 2013, 2015, 2017, 2019, 2021, 2023]

# The 13 binary/ordinal features from Paper 166/167
FEATURES = [
    "algorithmic_feed",
    "autoplay_video",
    "opaque_recommendation",
    "hidden_ranking_signals",
    "infinite_scroll",
    "push_notifications_engagement",
    "real_time_metrics",
    "streaks_or_daily_hooks",
    "beauty_ar_filters",
    "social_comparison_visible",
    "identity_persistence",
    "disappearing_content",
    "default_public_minor_profiles",
]

# Feature dimension groupings (O, R, alpha)
O_FEATURES = [
    "algorithmic_feed",
    "autoplay_video",
    "opaque_recommendation",
    "hidden_ranking_signals",
]
R_FEATURES = [
    "infinite_scroll",
    "push_notifications_engagement",
    "real_time_metrics",
    "streaks_or_daily_hooks",
]
ALPHA_FEATURES = [
    "beauty_ar_filters",
    "social_comparison_visible",
    "identity_persistence",
    "disappearing_content",
    "default_public_minor_profiles",
]

# Permutation and jackknife settings
N_PERMUTATIONS = 1000
RANDOM_SEED = 42

# Kill condition thresholds
KC_ALPHA = 0.10  # KC-D1: significance threshold

# Reference year for event study (earliest YRBS year)
EVENT_STUDY_REF_YEAR = 2011


# ---------------------------------------------------------------------------
# Section 1: Load feature-matrix.json and compute platform-year feature scores
# ---------------------------------------------------------------------------

def load_feature_matrix():
    """Load feature-matrix.json and compute per-platform-year feature score."""
    print("\n" + "=" * 70)
    print("SECTION 1: Loading feature-matrix.json")
    print("=" * 70)

    with open(FEATURE_MATRIX_PATH) as f:
        fm = json.load(f)

    platforms = fm["platforms"]
    rows = []
    for platform, years_data in platforms.items():
        for year_str, entry in years_data.items():
            year = int(year_str)
            feats = entry["features"]
            adoption = entry.get("adoption_pct", 0) / 100.0

            # Total feature score = sum of all 13 features
            feature_score = sum(feats[f] for f in FEATURES)

            # Dimension sub-scores
            o_score = sum(feats[f] for f in O_FEATURES)
            r_score = sum(feats[f] for f in R_FEATURES)
            alpha_score = sum(feats[f] for f in ALPHA_FEATURES)

            rows.append({
                "platform": platform,
                "year": year,
                "feature_score": feature_score,
                "o_score": o_score,
                "r_score": r_score,
                "alpha_score": alpha_score,
                "adoption_national": adoption,
            })

    df = pd.DataFrame(rows)
    print(f"  Loaded {len(df)} platform-year records from feature-matrix.json")
    print(f"  Platforms: {sorted(df['platform'].unique())}")
    print(f"  Years: {sorted(df['year'].unique())}")

    return df


# ---------------------------------------------------------------------------
# Section 2: Load platform-pe-timeline.json for national adoption fallback
# ---------------------------------------------------------------------------

def load_pe_timeline():
    """Load platform-pe-timeline.json for national adoption rates and O/R/alpha."""
    print("\n" + "=" * 70)
    print("SECTION 2: Loading platform-pe-timeline.json")
    print("=" * 70)

    with open(PE_TIMELINE_PATH) as f:
        pt = json.load(f)

    platforms = pt["platforms"]
    rows = []
    for platform, years_data in platforms.items():
        for year_str, entry in years_data.items():
            year = int(year_str)
            rows.append({
                "platform": platform,
                "year": year,
                "O": entry.get("O", 0),
                "R": entry.get("R", 0),
                "alpha": entry.get("alpha", 0),
                "adoption_pct_timeline": entry.get("adoption_pct", 0) / 100.0,
            })

    df = pd.DataFrame(rows)
    # Also extract the precomputed yearly totals
    yearly_totals = {}
    if "computed_metrics" in pt and "yearly_totals" in pt["computed_metrics"]:
        for yr_str, vals in pt["computed_metrics"]["yearly_totals"].items():
            yearly_totals[int(yr_str)] = vals.get("total", 0)

    print(f"  Loaded {len(df)} platform-year records from pe-timeline.json")
    print(f"  Yearly Pe totals available: {sorted(yearly_totals.keys())}")

    return df, yearly_totals


# ---------------------------------------------------------------------------
# Section 3: Load state-level YRBS data
# ---------------------------------------------------------------------------

def load_state_yrbs():
    """
    Load state-level YRBS data.
    Expected columns: state, year, sex, pct_sadness, pct_suicide, n_respondents
    Sex values: 'Total', 'Female', 'Male'
    """
    print("\n" + "=" * 70)
    print("SECTION 3: Loading state-level YRBS data")
    print("=" * 70)

    if not STATE_YRBS_PATH.exists():
        print(f"  WARNING: {STATE_YRBS_PATH} not found.")
        print("  The analysis requires state-level YRBS data.")
        print("  Expected format: state, year, sex, pct_sadness, pct_suicide, n_respondents")
        print("  Download from: https://www.cdc.gov/yrbs/data/index.html")
        return None

    df = pd.read_csv(STATE_YRBS_PATH)
    required_cols = ["state", "year", "sex", "pct_sadness"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print(f"  ERROR: Missing required columns: {missing}")
        print(f"  Available columns: {list(df.columns)}")
        return None

    print(f"  Loaded {len(df)} rows")
    print(f"  States: {df['state'].nunique()} unique")
    print(f"  Years: {sorted(df['year'].unique())}")
    print(f"  Sex categories: {sorted(df['sex'].unique())}")

    return df


# ---------------------------------------------------------------------------
# Section 4: Load state-level covariates
# ---------------------------------------------------------------------------

def load_state_covariates():
    """
    Load state-level covariates.
    Expected columns: state, year, broadband_pct, urban_pct, median_income, unemployment_rate
    """
    print("\n" + "=" * 70)
    print("SECTION 4: Loading state-level covariates")
    print("=" * 70)

    if not STATE_COVARIATES_PATH.exists():
        print(f"  WARNING: {STATE_COVARIATES_PATH} not found.")
        print("  Analysis will proceed without covariates (state + year FE only).")
        print("  Expected format: state, year, broadband_pct, urban_pct, median_income, unemployment_rate")
        return None

    df = pd.read_csv(STATE_COVARIATES_PATH)

    # Normalize column names from actual data format
    rename_map = {
        "broadband_penetration_pct": "broadband_pct",
        "pct_urban": "urban_pct",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    print(f"  Loaded {len(df)} rows")
    print(f"  Columns: {list(df.columns)}")
    print(f"  States: {df['state'].nunique()} unique")
    print(f"  Years: {sorted(df['year'].unique())}")

    return df


# ---------------------------------------------------------------------------
# Section 5: Load national-level YRBS for fallback / comparison
# ---------------------------------------------------------------------------

def load_national_yrbs():
    """Load national YRBS trend data for comparison."""
    print("\n" + "=" * 70)
    print("SECTION 5: Loading national YRBS trend data")
    print("=" * 70)

    if not NATIONAL_YRBS_PATH.exists():
        print(f"  WARNING: {NATIONAL_YRBS_PATH} not found.")
        return None

    df = pd.read_csv(NATIONAL_YRBS_PATH)
    print(f"  Loaded {len(df)} rows (national-level)")
    print(f"  Columns: {list(df.columns)}")

    return df


# ---------------------------------------------------------------------------
# Section 6: Compute state-level Pe proxy
# ---------------------------------------------------------------------------

def compute_state_pe_proxy(feature_df, covariates_df):
    """
    Compute state-level Pe proxy:
      Pe_st = sum over platforms of [feature_score_p * adoption_national_p * broadband_st * urban_st]

    If covariates are unavailable, fall back to national Pe (no state variation from
    broadband/urban). In that case, we use the national feature-weighted exposure directly,
    which means identification comes only from YRBS cross-state variation.
    """
    print("\n" + "=" * 70)
    print("SECTION 6: Computing state-level Pe proxy")
    print("=" * 70)

    # Compute national-level Pe proxy by year (sum across platforms of feature_score * adoption)
    national_pe = (
        feature_df
        .groupby("year")
        .apply(lambda g: (g["feature_score"] * g["adoption_national"]).sum(),
               include_groups=False)
        .reset_index()
        .rename(columns={0: "pe_national"})
    )
    print("\n  National Pe proxy by YRBS year:")
    for _, row in national_pe[national_pe["year"].isin(YRBS_YEARS)].iterrows():
        print(f"    {int(row['year'])}: {row['pe_national']:.2f}")

    # Compute dimension-level national Pe
    for dim_name, dim_features in [("O", O_FEATURES), ("R", R_FEATURES), ("alpha", ALPHA_FEATURES)]:
        dim_col = f"{dim_name.lower()}_score"
        national_dim = (
            feature_df
            .groupby("year")
            .apply(lambda g: (g[dim_col] * g["adoption_national"]).sum(),
                   include_groups=False)
            .reset_index()
            .rename(columns={0: f"pe_{dim_name.lower()}_national"})
        )
        national_pe = national_pe.merge(national_dim, on="year", how="left")

    if covariates_df is not None and "broadband_pct" in covariates_df.columns and "urban_pct" in covariates_df.columns:
        print("\n  State covariates available — computing state-specific Pe proxy.")
        # Normalize broadband and urban to [0, 1] if not already
        cov = covariates_df.copy()
        for col in ["broadband_pct", "urban_pct"]:
            if cov[col].max() > 1.0:
                cov[col] = cov[col] / 100.0

        # For each state-year, Pe_st = national_pe_t * broadband_st * urban_st
        # (This is a simplification; the full version would weight per-platform)
        state_pe = cov[["state", "year", "broadband_pct", "urban_pct"]].copy()
        state_pe = state_pe.merge(national_pe[["year", "pe_national"]], on="year", how="left")
        state_pe["pe_proxy"] = (
            state_pe["pe_national"] * state_pe["broadband_pct"] * state_pe["urban_pct"]
        )

        # Also compute per-platform state Pe for more granular analysis
        # Pe_st = sum_p [feature_score_p * adoption_p * broadband_st * urban_st]
        # This is equivalent to pe_national * broadband_st * urban_st since adoption
        # is national. The key variation comes from broadband * urban across states.
        state_pe["pe_proxy_rank"] = state_pe.groupby("year")["pe_proxy"].rank(pct=True)

        print(f"  Computed Pe proxy for {state_pe['state'].nunique()} states")
        print(f"  Pe proxy range: {state_pe['pe_proxy'].min():.2f} - {state_pe['pe_proxy'].max():.2f}")

        return state_pe, national_pe
    else:
        print("\n  WARNING: No broadband/urban covariates. Using national Pe only.")
        print("  State variation will come only from YRBS outcome differences.")
        print("  Identification is weaker without state-specific Pe variation.")
        return None, national_pe


# ---------------------------------------------------------------------------
# Section 7: Build analysis panel
# ---------------------------------------------------------------------------

def build_panel(state_yrbs, state_pe, national_pe, covariates_df):
    """
    Merge state YRBS, Pe proxy, and covariates into a single analysis panel.
    """
    print("\n" + "=" * 70)
    print("SECTION 7: Building analysis panel")
    print("=" * 70)

    if state_yrbs is None:
        print("  ERROR: No state YRBS data available. Cannot build panel.")
        return None

    panel = state_yrbs.copy()

    # Merge Pe proxy
    if state_pe is not None:
        panel = panel.merge(
            state_pe[["state", "year", "pe_proxy", "pe_proxy_rank"]],
            on=["state", "year"],
            how="left",
        )
    else:
        # Use national Pe (no state variation)
        panel = panel.merge(
            national_pe[["year", "pe_national"]],
            on="year",
            how="left",
        )
        panel["pe_proxy"] = panel["pe_national"]

    # Merge covariates if available
    if covariates_df is not None:
        cov_merge = covariates_df.copy()
        # Normalize percentage columns to [0, 1] for consistency
        for col in ["broadband_pct", "urban_pct"]:
            if col in cov_merge.columns and cov_merge[col].max() > 1.0:
                cov_merge[col] = cov_merge[col] / 100.0
        # Only keep numeric covariates relevant to the analysis
        numeric_covariates = ["broadband_pct", "urban_pct", "median_income", "unemployment_rate"]
        covariate_cols = [c for c in numeric_covariates if c in cov_merge.columns]
        # Drop non-numeric/metadata columns before merge
        keep_cols = ["state", "year"] + covariate_cols
        cov_merge = cov_merge[[c for c in keep_cols if c in cov_merge.columns]]
        panel = panel.merge(
            cov_merge,
            on=["state", "year"],
            how="left",
        )
    else:
        covariate_cols = []

    # Drop rows with missing outcome
    n_before = len(panel)
    panel = panel.dropna(subset=["pct_sadness"])
    n_after = len(panel)
    if n_before > n_after:
        print(f"  Dropped {n_before - n_after} rows with missing pct_sadness")

    # Summary
    print(f"  Panel: {len(panel)} rows")
    print(f"  States: {panel['state'].nunique()}")
    print(f"  Years: {sorted(panel['year'].unique())}")
    print(f"  Covariate columns: {covariate_cols}")
    pe_col = "pe_proxy"
    print(f"  Pe proxy ({pe_col}) — min: {panel[pe_col].min():.2f}, "
          f"max: {panel[pe_col].max():.2f}, mean: {panel[pe_col].mean():.2f}")

    return panel, covariate_cols


# ---------------------------------------------------------------------------
# Section 8: Primary TWFE regression
# ---------------------------------------------------------------------------

def run_twfe(panel, covariate_cols, outcome="pct_sadness", label="All"):
    """
    Two-Way Fixed Effects regression:
      outcome ~ pe_proxy + covariates + C(state) + C(year)
    with state-clustered standard errors.

    Tries linearmodels.PanelOLS first (absorbs FE efficiently),
    falls back to statsmodels OLS with dummies.
    """
    print(f"\n  --- TWFE: {label} ({outcome}) ---")

    df = panel.dropna(subset=[outcome, "pe_proxy"]).copy()
    if len(df) < 10:
        print(f"  WARNING: Only {len(df)} observations. Skipping.")
        return None

    result_dict = {
        "label": label,
        "outcome": outcome,
        "n_obs": len(df),
        "n_states": df["state"].nunique(),
        "n_years": df["year"].nunique(),
    }

    # Try linearmodels.PanelOLS first
    try:
        from linearmodels.panel import PanelOLS

        df_panel = df.set_index(["state", "year"])
        exog_cols = ["pe_proxy"]
        # Add covariates that are available and non-null
        for c in covariate_cols:
            if c in df_panel.columns and df_panel[c].notna().sum() > 0.5 * len(df_panel):
                exog_cols.append(c)

        y = df_panel[outcome]
        X = df_panel[exog_cols]

        # Drop rows with NaN in exog
        mask = X.notna().all(axis=1) & y.notna()
        y = y[mask]
        X = X[mask]

        if len(y) < 10:
            raise ValueError("Too few observations after dropping NaN")

        mod = PanelOLS(y, X, entity_effects=True, time_effects=True)
        res = mod.fit(cov_type="clustered", cluster_entity=True)

        beta = res.params["pe_proxy"]
        se = res.std_errors["pe_proxy"]
        pval = res.pvalues["pe_proxy"]
        ci_low = beta - 1.96 * se
        ci_high = beta + 1.96 * se
        r2_within = res.rsquared_within if hasattr(res, "rsquared_within") else res.rsquared

        result_dict.update({
            "method": "PanelOLS (linearmodels)",
            "beta_pe": round(float(beta), 6),
            "se_pe": round(float(se), 6),
            "pvalue_pe": round(float(pval), 6),
            "ci_95_low": round(float(ci_low), 6),
            "ci_95_high": round(float(ci_high), 6),
            "r2_within": round(float(r2_within), 4),
            "significant_10pct": bool(pval < 0.10),
            "significant_5pct": bool(pval < 0.05),
            "significant_1pct": bool(pval < 0.01),
            "covariates": exog_cols[1:],  # exclude pe_proxy
        })

        print(f"    Method: PanelOLS (linearmodels)")
        print(f"    N = {len(y)}, States = {y.index.get_level_values(0).nunique()}, "
              f"Years = {y.index.get_level_values(1).nunique()}")
        print(f"    β(Pe) = {beta:.6f} (SE = {se:.6f})")
        print(f"    p-value = {pval:.4f}")
        print(f"    95% CI: [{ci_low:.6f}, {ci_high:.6f}]")
        print(f"    R² (within) = {r2_within:.4f}")

        return result_dict

    except Exception as e:
        print(f"    PanelOLS failed ({e}), falling back to statsmodels OLS with dummies.")

    # Fallback: statsmodels OLS with C() dummies
    try:
        import statsmodels.formula.api as smf

        # Build formula
        formula_parts = [f"{outcome} ~ pe_proxy"]
        for c in covariate_cols:
            if c in df.columns and df[c].notna().sum() > 0.5 * len(df):
                formula_parts[0] += f" + {c}"

        formula = formula_parts[0] + " + C(state) + C(year)"

        mod = smf.ols(formula, data=df)
        res = mod.fit(cov_type="cluster", cov_kwds={"groups": df["state"]})

        beta = res.params["pe_proxy"]
        se = res.bse["pe_proxy"]
        pval = res.pvalues["pe_proxy"]
        ci_low, ci_high = res.conf_int().loc["pe_proxy"]

        result_dict.update({
            "method": "OLS with dummies (statsmodels)",
            "beta_pe": round(float(beta), 6),
            "se_pe": round(float(se), 6),
            "pvalue_pe": round(float(pval), 6),
            "ci_95_low": round(float(ci_low), 6),
            "ci_95_high": round(float(ci_high), 6),
            "r2_within": round(float(res.rsquared), 4),
            "significant_10pct": bool(pval < 0.10),
            "significant_5pct": bool(pval < 0.05),
            "significant_1pct": bool(pval < 0.01),
            "covariates": [c for c in covariate_cols if c in df.columns],
        })

        print(f"    Method: OLS with dummies (statsmodels)")
        print(f"    N = {len(df)}")
        print(f"    β(Pe) = {beta:.6f} (SE = {se:.6f})")
        print(f"    p-value = {pval:.4f}")
        print(f"    95% CI: [{ci_low:.6f}, {ci_high:.6f}]")

        return result_dict

    except Exception as e:
        print(f"    statsmodels OLS also failed: {e}")
        return None


# ---------------------------------------------------------------------------
# Section 9: Event study
# ---------------------------------------------------------------------------

def run_event_study(panel, covariate_cols, outcome="pct_sadness", label="All"):
    """
    Event study: interact pe_proxy with year dummies.
    Reference year = 2011 (earliest YRBS wave).

    Tests for pre-trends: are pre-2016 coefficients close to zero?
    """
    print(f"\n  --- Event Study: {label} ({outcome}) ---")

    df = panel.dropna(subset=[outcome, "pe_proxy"]).copy()
    if len(df) < 10:
        print(f"  WARNING: Only {len(df)} observations. Skipping event study.")
        return None

    years = sorted(df["year"].unique())
    ref_year = EVENT_STUDY_REF_YEAR
    if ref_year not in years:
        ref_year = min(years)
    non_ref_years = [y for y in years if y != ref_year]

    # Create interaction terms: pe_proxy * I(year == t) for each non-reference year
    for y in non_ref_years:
        df[f"pe_x_{y}"] = df["pe_proxy"] * (df["year"] == y).astype(float)

    try:
        from linearmodels.panel import PanelOLS

        df_panel = df.set_index(["state", "year"])
        interaction_cols = [f"pe_x_{y}" for y in non_ref_years]
        exog_cols = interaction_cols.copy()
        for c in covariate_cols:
            if c in df_panel.columns and df_panel[c].notna().sum() > 0.5 * len(df_panel):
                exog_cols.append(c)

        y_var = df_panel[outcome]
        X = df_panel[exog_cols]
        mask = X.notna().all(axis=1) & y_var.notna()
        y_var = y_var[mask]
        X = X[mask]

        mod = PanelOLS(y_var, X, entity_effects=True, time_effects=True)
        res = mod.fit(cov_type="clustered", cluster_entity=True)

        event_coeffs = {}
        event_coeffs[ref_year] = {"beta": 0.0, "se": 0.0, "pvalue": 1.0, "reference": True}
        for y in non_ref_years:
            col = f"pe_x_{y}"
            if col in res.params.index:
                event_coeffs[y] = {
                    "beta": round(float(res.params[col]), 6),
                    "se": round(float(res.std_errors[col]), 6),
                    "pvalue": round(float(res.pvalues[col]), 6),
                    "reference": False,
                }

        print(f"    Method: PanelOLS event study (ref year = {ref_year})")
    except Exception as e:
        print(f"    PanelOLS event study failed ({e}), trying statsmodels.")

        try:
            import statsmodels.formula.api as smf

            interaction_terms = " + ".join(f"pe_x_{y}" for y in non_ref_years)
            cov_terms = ""
            for c in covariate_cols:
                if c in df.columns and df[c].notna().sum() > 0.5 * len(df):
                    cov_terms += f" + {c}"

            formula = f"{outcome} ~ {interaction_terms}{cov_terms} + C(state) + C(year)"
            mod = smf.ols(formula, data=df)
            res = mod.fit(cov_type="cluster", cov_kwds={"groups": df["state"]})

            event_coeffs = {}
            event_coeffs[ref_year] = {"beta": 0.0, "se": 0.0, "pvalue": 1.0, "reference": True}
            for y in non_ref_years:
                col = f"pe_x_{y}"
                if col in res.params.index:
                    event_coeffs[y] = {
                        "beta": round(float(res.params[col]), 6),
                        "se": round(float(res.bse[col]), 6),
                        "pvalue": round(float(res.pvalues[col]), 6),
                        "reference": False,
                    }

            print(f"    Method: OLS event study (ref year = {ref_year})")
        except Exception as e2:
            print(f"    Event study failed: {e2}")
            return None

    # Print event study results
    print(f"\n    Year | β(Pe×Year) |   SE    | p-value | Sig")
    print(f"    -----|------------|---------|---------|----")
    for y in sorted(event_coeffs.keys()):
        ec = event_coeffs[y]
        sig = "ref" if ec.get("reference") else ("***" if ec["pvalue"] < 0.01 else
               "**" if ec["pvalue"] < 0.05 else "*" if ec["pvalue"] < 0.10 else "")
        print(f"    {y} | {ec['beta']:10.6f} | {ec['se']:7.4f} | {ec['pvalue']:7.4f} | {sig}")

    # Check pre-trends: years before 2016 (the major inflection)
    pre_trend_years = [y for y in event_coeffs if y < 2016 and not event_coeffs[y].get("reference")]
    pre_trend_sig = any(event_coeffs[y]["pvalue"] < 0.10 for y in pre_trend_years)

    result = {
        "label": label,
        "outcome": outcome,
        "reference_year": ref_year,
        "coefficients": event_coeffs,
        "pre_trend_years_tested": pre_trend_years,
        "pre_trends_detected": pre_trend_sig,
    }

    if pre_trend_sig:
        print(f"\n    WARNING: Pre-trends detected (pre-2016 coefficients significant at 10%)")
    else:
        print(f"\n    Pre-trends check: PASS (no pre-2016 coefficients significant at 10%)")

    return result


# ---------------------------------------------------------------------------
# Section 10: Gender-stratified analysis
# ---------------------------------------------------------------------------

def run_gender_stratified(panel, covariate_cols, outcome="pct_sadness"):
    """
    Run TWFE separately for Female and Male.
    KC-D3: Female β > Male β required.
    """
    print("\n" + "=" * 70)
    print("SECTION 10: Gender-stratified TWFE")
    print("=" * 70)

    results = {}

    for sex_val in ["Female", "Male"]:
        sub = panel[panel["sex"] == sex_val].copy()
        if len(sub) < 10:
            print(f"\n  WARNING: Only {len(sub)} observations for sex={sex_val}. Skipping.")
            continue

        r = run_twfe(sub, covariate_cols, outcome=outcome, label=f"{sex_val}")
        if r is not None:
            results[sex_val] = r

    # KC-D3 check
    if "Female" in results and "Male" in results:
        f_beta = results["Female"]["beta_pe"]
        m_beta = results["Male"]["beta_pe"]
        ratio = f_beta / m_beta if m_beta != 0 else float("inf")
        kc_d3_pass = f_beta > m_beta

        print(f"\n  KC-D3 check: Female β ({f_beta:.6f}) {'>' if kc_d3_pass else '<='} "
              f"Male β ({m_beta:.6f})")
        print(f"  Female/Male ratio: {ratio:.2f}x")
        print(f"  KC-D3: {'PASS' if kc_d3_pass else 'FAIL'}")

        results["kc_d3"] = {
            "female_beta": f_beta,
            "male_beta": m_beta,
            "ratio": round(ratio, 4),
            "pass": kc_d3_pass,
        }
    else:
        print("\n  WARNING: Cannot check KC-D3 — need both Female and Male results.")

    return results


# ---------------------------------------------------------------------------
# Section 11: Robustness — Leave-one-state-out jackknife
# ---------------------------------------------------------------------------

def run_jackknife(panel, covariate_cols, outcome="pct_sadness"):
    """
    Leave-one-state-out jackknife: re-run TWFE dropping each state in turn.
    Tests sensitivity of β to any single state.
    """
    print("\n" + "=" * 70)
    print("SECTION 11: Leave-one-state-out jackknife")
    print("=" * 70)

    states = sorted(panel["state"].unique())
    n_states = len(states)
    print(f"  Running {n_states} jackknife iterations...")

    betas = []
    dropped_states = []

    for i, drop_state in enumerate(states):
        sub = panel[panel["state"] != drop_state].copy()
        # Quick TWFE without printing
        try:
            from linearmodels.panel import PanelOLS

            df_p = sub.dropna(subset=[outcome, "pe_proxy"]).set_index(["state", "year"])
            exog_cols = ["pe_proxy"]
            for c in covariate_cols:
                if c in df_p.columns and df_p[c].notna().sum() > 0.5 * len(df_p):
                    exog_cols.append(c)

            y = df_p[outcome]
            X = df_p[exog_cols]
            mask = X.notna().all(axis=1) & y.notna()
            y, X = y[mask], X[mask]

            mod = PanelOLS(y, X, entity_effects=True, time_effects=True)
            res = mod.fit(cov_type="clustered", cluster_entity=True)
            betas.append(float(res.params["pe_proxy"]))
            dropped_states.append(drop_state)
        except Exception:
            # Fallback to OLS
            try:
                import statsmodels.formula.api as smf
                sub_clean = sub.dropna(subset=[outcome, "pe_proxy"])
                cov_str = ""
                for c in covariate_cols:
                    if c in sub_clean.columns and sub_clean[c].notna().sum() > 0.5 * len(sub_clean):
                        cov_str += f" + {c}"
                formula = f"{outcome} ~ pe_proxy{cov_str} + C(state) + C(year)"
                mod = smf.ols(formula, data=sub_clean)
                res = mod.fit(cov_type="cluster", cov_kwds={"groups": sub_clean["state"]})
                betas.append(float(res.params["pe_proxy"]))
                dropped_states.append(drop_state)
            except Exception:
                pass

        if (i + 1) % 10 == 0:
            print(f"    Completed {i + 1}/{n_states}")

    if not betas:
        print("  ERROR: Jackknife failed — no estimates obtained.")
        return None

    betas = np.array(betas)
    jack_mean = betas.mean()
    jack_se = np.sqrt((n_states - 1) / n_states * np.sum((betas - jack_mean) ** 2))
    jack_min = betas.min()
    jack_max = betas.max()
    min_state = dropped_states[np.argmin(betas)]
    max_state = dropped_states[np.argmax(betas)]

    # Check if sign is stable
    all_positive = all(b > 0 for b in betas)
    all_negative = all(b < 0 for b in betas)
    sign_stable = all_positive or all_negative

    result = {
        "n_iterations": len(betas),
        "mean_beta": round(float(jack_mean), 6),
        "jackknife_se": round(float(jack_se), 6),
        "min_beta": round(float(jack_min), 6),
        "max_beta": round(float(jack_max), 6),
        "min_beta_state_dropped": min_state,
        "max_beta_state_dropped": max_state,
        "sign_stable": sign_stable,
        "range": round(float(jack_max - jack_min), 6),
    }

    print(f"\n  Jackknife results ({len(betas)} iterations):")
    print(f"    Mean β: {jack_mean:.6f}")
    print(f"    Jackknife SE: {jack_se:.6f}")
    print(f"    Range: [{jack_min:.6f}, {jack_max:.6f}]")
    print(f"    Most influential (largest β when dropped): {min_state}")
    print(f"    Most influential (smallest β when dropped): {max_state}")
    print(f"    Sign stable: {sign_stable}")

    return result


# ---------------------------------------------------------------------------
# Section 12: Robustness — Permutation test
# ---------------------------------------------------------------------------

def run_permutation_test(panel, covariate_cols, outcome="pct_sadness"):
    """
    Randomize state Pe assignment (shuffle Pe across states within each year),
    re-run TWFE, build null distribution.
    """
    print("\n" + "=" * 70)
    print("SECTION 12: Permutation test")
    print("=" * 70)

    rng = np.random.default_rng(RANDOM_SEED)

    # First, get the actual β
    df = panel.dropna(subset=[outcome, "pe_proxy"]).copy()
    if len(df) < 10:
        print("  WARNING: Too few observations for permutation test.")
        return None

    # Get actual beta
    try:
        from linearmodels.panel import PanelOLS

        df_p = df.set_index(["state", "year"])
        exog_cols = ["pe_proxy"]
        for c in covariate_cols:
            if c in df_p.columns and df_p[c].notna().sum() > 0.5 * len(df_p):
                exog_cols.append(c)

        y = df_p[outcome]
        X = df_p[exog_cols]
        mask = X.notna().all(axis=1) & y.notna()
        y, X = y[mask], X[mask]
        mod = PanelOLS(y, X, entity_effects=True, time_effects=True)
        res = mod.fit(cov_type="clustered", cluster_entity=True)
        actual_beta = float(res.params["pe_proxy"])
        use_panel_ols = True
    except Exception:
        import statsmodels.formula.api as smf
        cov_str = ""
        for c in covariate_cols:
            if c in df.columns and df[c].notna().sum() > 0.5 * len(df):
                cov_str += f" + {c}"
        formula = f"{outcome} ~ pe_proxy{cov_str} + C(state) + C(year)"
        mod = smf.ols(formula, data=df)
        res = mod.fit(cov_type="cluster", cov_kwds={"groups": df["state"]})
        actual_beta = float(res.params["pe_proxy"])
        use_panel_ols = False

    print(f"  Actual β(Pe) = {actual_beta:.6f}")
    print(f"  Running {N_PERMUTATIONS} permutations...")

    null_betas = []
    for i in range(N_PERMUTATIONS):
        # Shuffle Pe assignments across states within each year
        df_perm = df.copy()
        for yr in df_perm["year"].unique():
            yr_mask = df_perm["year"] == yr
            pe_vals = df_perm.loc[yr_mask, "pe_proxy"].values.copy()
            rng.shuffle(pe_vals)
            df_perm.loc[yr_mask, "pe_proxy"] = pe_vals

        try:
            if use_panel_ols:
                df_pp = df_perm.set_index(["state", "year"])
                y = df_pp[outcome]
                X = df_pp[exog_cols]
                mask = X.notna().all(axis=1) & y.notna()
                y, X = y[mask], X[mask]
                mod = PanelOLS(y, X, entity_effects=True, time_effects=True)
                res = mod.fit(cov_type="clustered", cluster_entity=True)
                null_betas.append(float(res.params["pe_proxy"]))
            else:
                mod = smf.ols(formula, data=df_perm)
                res = mod.fit(cov_type="cluster", cov_kwds={"groups": df_perm["state"]})
                null_betas.append(float(res.params["pe_proxy"]))
        except Exception:
            pass

        if (i + 1) % 100 == 0:
            print(f"    Completed {i + 1}/{N_PERMUTATIONS}")

    if not null_betas:
        print("  ERROR: All permutations failed.")
        return None

    null_betas = np.array(null_betas)

    # One-sided p-value: proportion of null betas >= actual
    perm_pvalue = (null_betas >= actual_beta).mean()

    result = {
        "actual_beta": round(float(actual_beta), 6),
        "n_permutations": len(null_betas),
        "null_mean": round(float(null_betas.mean()), 6),
        "null_sd": round(float(null_betas.std()), 6),
        "null_percentile_95": round(float(np.percentile(null_betas, 95)), 6),
        "null_percentile_99": round(float(np.percentile(null_betas, 99)), 6),
        "permutation_pvalue": round(float(perm_pvalue), 4),
        "significant_5pct": bool(perm_pvalue < 0.05),
    }

    print(f"\n  Permutation test results ({len(null_betas)} permutations):")
    print(f"    Actual β: {actual_beta:.6f}")
    print(f"    Null distribution: mean = {null_betas.mean():.6f}, SD = {null_betas.std():.6f}")
    print(f"    Null 95th percentile: {np.percentile(null_betas, 95):.6f}")
    print(f"    Permutation p-value: {perm_pvalue:.4f}")
    print(f"    Significant at 5%: {perm_pvalue < 0.05}")

    return result


# ---------------------------------------------------------------------------
# Section 13: Callaway-Sant'Anna estimator (if available)
# ---------------------------------------------------------------------------

def run_callaway_santanna(panel, outcome="pct_sadness"):
    """
    Callaway-Sant'Anna (2021) estimator for staggered DiD.
    Requires the csdid Python package. If unavailable, notes this as a
    future robustness check.
    """
    print("\n" + "=" * 70)
    print("SECTION 13: Callaway-Sant'Anna estimator")
    print("=" * 70)

    try:
        import csdid
        print("  csdid package available. Running CS estimator...")
        # The csdid package requires: outcome, group (first treatment year), time, id
        # For continuous treatment (Pe proxy), CS doesn't directly apply.
        # We would need to discretize Pe into treatment groups.
        # This is a methodological consideration — note for future work.
        print("  NOTE: CS estimator is designed for binary treatment with staggered timing.")
        print("  Our Pe proxy is continuous. Discretizing into high/low Pe groups for CS.")

        # Discretize: median split of Pe proxy within each year
        panel_cs = panel.dropna(subset=[outcome, "pe_proxy"]).copy()
        panel_cs["high_pe"] = (
            panel_cs.groupby("year")["pe_proxy"]
            .transform(lambda x: (x > x.median()).astype(int))
        )

        # Identify first year of "treatment" (high Pe) for each state
        state_first_high = (
            panel_cs[panel_cs["high_pe"] == 1]
            .groupby("state")["year"]
            .min()
            .rename("first_treated")
        )
        panel_cs = panel_cs.merge(state_first_high, on="state", how="left")
        # Never-treated states: set first_treated to 0
        panel_cs["first_treated"] = panel_cs["first_treated"].fillna(0).astype(int)

        # This would feed into csdid.att_gt() — implementation depends on package API
        print("  CS estimator: implementation depends on csdid package API version.")
        print("  Marking as AVAILABLE but not yet integrated.")

        return {"status": "available_not_integrated", "note": "csdid package found but CS estimator requires binary treatment. Discretized Pe approach noted for future work."}

    except ImportError:
        print("  csdid package not installed.")
        print("  Callaway-Sant'Anna estimator noted as future robustness check.")
        print("  Install with: pip install csdid")
        return {"status": "not_available", "note": "csdid package not installed. Future robustness check."}


# ---------------------------------------------------------------------------
# Section 14: Dimension-level analysis
# ---------------------------------------------------------------------------

def run_dimension_analysis(feature_df, panel, covariate_cols, covariates_df, outcome="pct_sadness"):
    """
    Decompose Pe proxy into O, R, alpha dimensions and test which drives results.
    Mirrors Papers 166/167 finding that opacity dominates.
    """
    print("\n" + "=" * 70)
    print("SECTION 14: Dimension-level analysis (O, R, alpha)")
    print("=" * 70)

    if panel is None:
        print("  Skipping — no panel available.")
        return None

    # Compute dimension-level national Pe by year
    for dim_name, dim_col in [("O", "o_score"), ("R", "r_score"), ("alpha", "alpha_score")]:
        dim_pe = (
            feature_df
            .groupby("year")
            .apply(lambda g: (g[dim_col] * g["adoption_national"]).sum(),
                   include_groups=False)
            .reset_index()
            .rename(columns={0: f"pe_{dim_name.lower()}"})
        )

        # Merge into panel
        if f"pe_{dim_name.lower()}" not in panel.columns:
            panel = panel.merge(dim_pe, on="year", how="left")

            # Scale by state broadband * urban if available
            # (broadband_pct and urban_pct already normalized to [0,1] in build_panel)
            if "broadband_pct" in panel.columns and "urban_pct" in panel.columns:
                panel[f"pe_{dim_name.lower()}"] = (
                    panel[f"pe_{dim_name.lower()}"]
                    * panel["broadband_pct"]
                    * panel["urban_pct"]
                )

    # Run separate regressions for each dimension
    results = {}
    for dim_name in ["O", "R", "alpha"]:
        pe_col = f"pe_{dim_name.lower()}"
        if pe_col not in panel.columns:
            continue

        df = panel.dropna(subset=[outcome, pe_col]).copy()
        if len(df) < 10:
            continue

        try:
            from linearmodels.panel import PanelOLS

            df_p = df.set_index(["state", "year"])
            exog_cols = [pe_col]
            for c in covariate_cols:
                if c in df_p.columns and df_p[c].notna().sum() > 0.5 * len(df_p):
                    exog_cols.append(c)

            y = df_p[outcome]
            X = df_p[exog_cols]
            mask = X.notna().all(axis=1) & y.notna()
            y, X = y[mask], X[mask]
            mod = PanelOLS(y, X, entity_effects=True, time_effects=True)
            res = mod.fit(cov_type="clustered", cluster_entity=True)

            beta = float(res.params[pe_col])
            se = float(res.std_errors[pe_col])
            pval = float(res.pvalues[pe_col])
            r2 = float(res.rsquared_within) if hasattr(res, "rsquared_within") else float(res.rsquared)

            results[dim_name] = {
                "beta": round(beta, 6),
                "se": round(se, 6),
                "pvalue": round(pval, 6),
                "r2_within": round(r2, 4),
                "significant_5pct": bool(pval < 0.05),
            }

            print(f"\n  {dim_name}-dimension: β = {beta:.6f} (SE = {se:.6f}), p = {pval:.4f}, R²w = {r2:.4f}")

        except Exception as e:
            print(f"\n  {dim_name}-dimension regression failed: {e}")

    if results:
        # Check if O dominates (Papers 166/167 prediction)
        if "O" in results and all(d in results for d in ["R", "alpha"]):
            o_dominates = (
                abs(results["O"]["beta"]) > abs(results["R"]["beta"]) and
                abs(results["O"]["beta"]) > abs(results["alpha"]["beta"])
            )
            print(f"\n  Opacity dominates: {o_dominates}")
            print(f"    |β_O| = {abs(results['O']['beta']):.6f}")
            print(f"    |β_R| = {abs(results['R']['beta']):.6f}")
            print(f"    |β_α| = {abs(results['alpha']['beta']):.6f}")
            results["o_dominates"] = o_dominates

    return results


# ---------------------------------------------------------------------------
# Section 15: Kill condition evaluation
# ---------------------------------------------------------------------------

def evaluate_kill_conditions(primary_result, event_study_result, gender_results):
    """
    Evaluate the three kill conditions:
      KC-D1: β significantly positive (p < 0.10)?
      KC-D2: No pre-trends (pre-2016 coefficients insignificant)?
      KC-D3: Female β > Male β?
    """
    print("\n" + "=" * 70)
    print("SECTION 15: Kill condition evaluation")
    print("=" * 70)

    kc = {}

    # KC-D1: β significantly positive
    if primary_result is not None:
        beta = primary_result.get("beta_pe", 0)
        pval = primary_result.get("pvalue_pe", 1)
        kc_d1 = beta > 0 and pval < KC_ALPHA
        kc["KC_D1"] = {
            "description": f"beta significantly positive (p < {KC_ALPHA})",
            "beta": beta,
            "pvalue": pval,
            "pass": kc_d1,
        }
        print(f"\n  KC-D1: β = {beta:.6f}, p = {pval:.4f}")
        print(f"    {'PASS' if kc_d1 else 'FAIL'}: β {'is' if beta > 0 else 'is not'} positive "
              f"and {'is' if pval < KC_ALPHA else 'is not'} significant at {KC_ALPHA}")
    else:
        kc["KC_D1"] = {"pass": None, "reason": "No primary result available"}
        print("\n  KC-D1: CANNOT EVALUATE — no primary result")

    # KC-D2: No pre-trends
    if event_study_result is not None:
        pre_trends = event_study_result.get("pre_trends_detected", None)
        kc_d2 = not pre_trends if pre_trends is not None else None
        kc["KC_D2"] = {
            "description": "No significant pre-trends (pre-2016 coefficients)",
            "pre_trends_detected": pre_trends,
            "pass": kc_d2,
        }
        if kc_d2 is not None:
            print(f"\n  KC-D2: Pre-trends detected: {pre_trends}")
            print(f"    {'PASS' if kc_d2 else 'FAIL'}")
        else:
            print(f"\n  KC-D2: CANNOT EVALUATE")
    else:
        kc["KC_D2"] = {"pass": None, "reason": "No event study result available"}
        print("\n  KC-D2: CANNOT EVALUATE — no event study result")

    # KC-D3: Female β > Male β
    if gender_results is not None and "kc_d3" in gender_results:
        kc_d3_data = gender_results["kc_d3"]
        kc["KC_D3"] = {
            "description": "Female β > Male β (gender specificity)",
            "female_beta": kc_d3_data["female_beta"],
            "male_beta": kc_d3_data["male_beta"],
            "ratio": kc_d3_data["ratio"],
            "pass": kc_d3_data["pass"],
        }
        print(f"\n  KC-D3: Female β = {kc_d3_data['female_beta']:.6f}, "
              f"Male β = {kc_d3_data['male_beta']:.6f}")
        print(f"    Ratio: {kc_d3_data['ratio']:.2f}x")
        print(f"    {'PASS' if kc_d3_data['pass'] else 'FAIL'}")
    else:
        kc["KC_D3"] = {"pass": None, "reason": "Gender-stratified results unavailable"}
        print("\n  KC-D3: CANNOT EVALUATE — gender results unavailable")

    # Overall
    all_kc = [v.get("pass") for v in kc.values()]
    n_pass = sum(1 for v in all_kc if v is True)
    n_fail = sum(1 for v in all_kc if v is False)
    n_na = sum(1 for v in all_kc if v is None)
    kc["summary"] = {
        "pass": n_pass,
        "fail": n_fail,
        "not_evaluated": n_na,
        "total": len(all_kc),
        "all_pass": n_fail == 0 and n_na == 0,
    }

    print(f"\n  SUMMARY: {n_pass} PASS / {n_fail} FAIL / {n_na} not evaluated")

    return kc


# ---------------------------------------------------------------------------
# Section 16: National-level analysis (fallback if no state data)
# ---------------------------------------------------------------------------

def run_national_analysis(national_yrbs, feature_df, pe_yearly_totals):
    """
    If state-level data is unavailable, run a national-level time-series
    correlation analysis as a fallback. This is NOT a DiD — no causal claim —
    but documents the association for comparison.
    """
    print("\n" + "=" * 70)
    print("SECTION 16: National-level fallback analysis")
    print("=" * 70)

    if national_yrbs is None:
        print("  No national YRBS data. Skipping.")
        return None

    # Build national dataset
    df = national_yrbs.copy()
    df = df.rename(columns={"Year": "year"})

    # Map Pe totals
    pe_national = (
        feature_df
        .groupby("year")
        .apply(lambda g: (g["feature_score"] * g["adoption_national"]).sum(),
               include_groups=False)
        .reset_index()
        .rename(columns={0: "pe_proxy"})
    )

    df = df.merge(pe_national, on="year", how="left")

    # Check which sadness columns exist
    sadness_total_col = None
    sadness_female_col = None
    sadness_male_col = None

    for c in df.columns:
        cl = c.lower()
        if "sadness" in cl and "total" in cl:
            sadness_total_col = c
        if "sadness" in cl and "female" in cl:
            sadness_female_col = c
        if "sadness" in cl and "male" in cl:
            sadness_male_col = c

    results = {}

    for label, col in [("Total", sadness_total_col), ("Female", sadness_female_col),
                       ("Male", sadness_male_col)]:
        if col is None or col not in df.columns:
            continue

        valid = df.dropna(subset=[col, "pe_proxy"])
        if len(valid) < 3:
            continue

        x = valid["pe_proxy"].values
        y = valid[col].values.astype(float)

        # Pearson correlation
        from scipy import stats as scipy_stats
        r, p = scipy_stats.pearsonr(x, y)

        # Simple OLS
        slope, intercept, r_val, p_val, se = scipy_stats.linregress(x, y)

        results[label] = {
            "n_years": len(valid),
            "pearson_r": round(float(r), 4),
            "pearson_p": round(float(p), 4),
            "slope": round(float(slope), 4),
            "intercept": round(float(intercept), 4),
            "r_squared": round(float(r_val ** 2), 4),
        }

        print(f"\n  {label}: r = {r:.4f} (p = {p:.4f}), R² = {r_val**2:.4f}")
        print(f"    slope = {slope:.4f} (1 unit Pe increase -> {slope:.2f} ppt sadness increase)")

    if "Female" in results and "Male" in results:
        print(f"\n  Gender comparison:")
        print(f"    Female slope: {results['Female']['slope']}")
        print(f"    Male slope: {results['Male']['slope']}")
        ratio = results["Female"]["slope"] / results["Male"]["slope"] if results["Male"]["slope"] != 0 else float("inf")
        print(f"    Female/Male slope ratio: {ratio:.2f}x")
        results["gender_ratio"] = round(ratio, 4)

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("STATE-LEVEL DIFFERENCE-IN-DIFFERENCES ANALYSIS")
    print("Protocol A — Paper 173, §5.1")
    print("=" * 70)
    print(f"\nScript directory: {SCRIPT_DIR}")

    # -----------------------------------------------------------------------
    # Load data
    # -----------------------------------------------------------------------
    feature_df = load_feature_matrix()
    pe_timeline_df, pe_yearly_totals = load_pe_timeline()
    state_yrbs = load_state_yrbs()
    covariates_df = load_state_covariates()
    national_yrbs = load_national_yrbs()

    # -----------------------------------------------------------------------
    # Compute state-level Pe proxy
    # -----------------------------------------------------------------------
    state_pe, national_pe = compute_state_pe_proxy(feature_df, covariates_df)

    # -----------------------------------------------------------------------
    # Results container
    # -----------------------------------------------------------------------
    all_results = {
        "metadata": {
            "protocol": "State-Level DiD (Protocol A)",
            "paper": "173, §5.1",
            "date": pd.Timestamp.now().isoformat(),
            "yrbs_years": YRBS_YEARS,
            "n_features": len(FEATURES),
            "features": FEATURES,
            "permutation_n": N_PERMUTATIONS,
            "random_seed": RANDOM_SEED,
            "kill_condition_alpha": KC_ALPHA,
        },
        "national_pe_by_year": {
            int(row["year"]): round(row["pe_national"], 4)
            for _, row in national_pe.iterrows()
            if row["year"] in YRBS_YEARS
        },
    }

    # -----------------------------------------------------------------------
    # Branch: state-level analysis or national fallback
    # -----------------------------------------------------------------------
    if state_yrbs is not None:
        # Build panel
        panel, covariate_cols = build_panel(state_yrbs, state_pe, national_pe, covariates_df)

        if panel is not None:
            # ------ Primary TWFE (Total) ------
            print("\n" + "=" * 70)
            print("SECTION 8: Primary TWFE regression")
            print("=" * 70)

            # Filter to Total sex for primary
            panel_total = panel[panel["sex"] == "Total"].copy()
            if len(panel_total) == 0:
                # Maybe sex categories are different — try without filter
                print("  WARNING: No 'Total' sex category. Using all data.")
                panel_total = panel.copy()

            primary_result = run_twfe(panel_total, covariate_cols, outcome="pct_sadness", label="All (Total)")

            # Also run for suicide if available
            suicide_result = None
            if "pct_suicide" in panel.columns and panel_total["pct_suicide"].notna().sum() > 10:
                suicide_result = run_twfe(panel_total, covariate_cols, outcome="pct_suicide", label="Suicide (Total)")

            all_results["primary_twfe"] = primary_result
            if suicide_result:
                all_results["suicide_twfe"] = suicide_result

            # ------ Event study ------
            print("\n" + "=" * 70)
            print("SECTION 9: Event study")
            print("=" * 70)
            event_study_result = run_event_study(panel_total, covariate_cols, outcome="pct_sadness", label="All (Total)")
            all_results["event_study"] = event_study_result

            # ------ Gender-stratified ------
            gender_results = run_gender_stratified(panel, covariate_cols, outcome="pct_sadness")
            all_results["gender_stratified"] = gender_results

            # Event studies for each gender
            for sex_val in ["Female", "Male"]:
                sub = panel[panel["sex"] == sex_val].copy()
                if len(sub) >= 10:
                    es = run_event_study(sub, covariate_cols, outcome="pct_sadness", label=sex_val)
                    all_results[f"event_study_{sex_val.lower()}"] = es

            # ------ Jackknife ------
            jack_result = run_jackknife(panel_total, covariate_cols, outcome="pct_sadness")
            all_results["jackknife"] = jack_result

            # ------ Permutation test ------
            perm_result = run_permutation_test(panel_total, covariate_cols, outcome="pct_sadness")
            all_results["permutation_test"] = perm_result

            # ------ Callaway-Sant'Anna ------
            cs_result = run_callaway_santanna(panel, outcome="pct_sadness")
            all_results["callaway_santanna"] = cs_result

            # ------ Dimension analysis ------
            dim_result = run_dimension_analysis(feature_df, panel_total, covariate_cols, covariates_df)
            all_results["dimension_analysis"] = dim_result

            # ------ Kill conditions ------
            kc_result = evaluate_kill_conditions(primary_result, event_study_result, gender_results)
            all_results["kill_conditions"] = kc_result

        else:
            print("\n  ERROR: Could not build panel. Running national fallback only.")
            national_result = run_national_analysis(national_yrbs, feature_df, pe_yearly_totals)
            all_results["national_fallback"] = national_result
            all_results["kill_conditions"] = {
                "note": "State-level analysis not possible. National fallback only — no causal claim.",
                "KC_D1": {"pass": None},
                "KC_D2": {"pass": None},
                "KC_D3": {"pass": None},
            }
    else:
        print("\n  State YRBS data not available. Running national-level fallback analysis.")
        national_result = run_national_analysis(national_yrbs, feature_df, pe_yearly_totals)
        all_results["national_fallback"] = national_result
        all_results["kill_conditions"] = {
            "note": "State-level YRBS data not yet downloaded. National fallback only — no causal identification.",
            "KC_D1": {"pass": None, "reason": "Requires state-level data"},
            "KC_D2": {"pass": None, "reason": "Requires state-level data"},
            "KC_D3": {"pass": None, "reason": "Requires state-level data"},
        }

    # -----------------------------------------------------------------------
    # Save results
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SAVING RESULTS")
    print("=" * 70)

    # Convert any numpy types for JSON serialization
    def convert_types(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        elif isinstance(obj, (np.floating,)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, dict):
            return {convert_types(k): convert_types(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [convert_types(v) for v in obj]
        return obj

    all_results = convert_types(all_results)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"  Results saved to: {OUTPUT_PATH}")

    # Final summary
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

    kc = all_results.get("kill_conditions", {})
    if "summary" in kc:
        s = kc["summary"]
        print(f"\n  Kill conditions: {s['pass']} PASS / {s['fail']} FAIL / {s['not_evaluated']} N/A")
    else:
        print("\n  Kill conditions: not fully evaluated (state data may be missing)")

    if "national_fallback" in all_results:
        print("\n  NOTE: Running in national fallback mode.")
        print("  State-level data required for causal identification (DiD).")
        print("  Download state YRBS from: https://www.cdc.gov/yrbs/data/index.html")

    print(f"\n  Output: {OUTPUT_PATH}")
    print()

    return all_results


if __name__ == "__main__":
    main()
