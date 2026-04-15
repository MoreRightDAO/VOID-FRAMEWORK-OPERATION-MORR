#!/usr/bin/env python3
"""
Extract PISA 2022 Social Media & Wellbeing Data — Country-Level Aggregates
===========================================================================

Reads the full PISA 2022 SPSS student file and produces:
1. Country-level means for life satisfaction, belonging, and social media use
2. Gender-stratified country-level means
3. Dose-response curves (SM hours → life satisfaction) by country and gender
4. CSV outputs for further analysis

Requires: pyreadstat, pandas, numpy
Install: pip install pyreadstat pandas numpy

Usage:
    python extract_pisa_social_media_wellbeing.py

Input: CY08MSP_STU_QQQ.sav (unzipped from STU_QQQ_SPSS.zip)
Output: pisa_country_means.csv, pisa_dose_response.csv, pisa_gender_means.csv
"""

import os
import sys
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

# Try to import pyreadstat
try:
    import pyreadstat
except ImportError:
    print("ERROR: pyreadstat not installed. Run: pip install pyreadstat")
    sys.exit(1)


SCRIPT_DIR = Path(__file__).parent

# ─── Configuration ──────────────────────────────────────────────────────────

# Columns to extract (keeps memory manageable)
COLS_NEEDED = [
    # Identifiers & demographics
    'CNT',           # Country (3-letter code)
    'ST004D01T',     # Gender (1=Female, 2=Male)
    'ESCS',          # Socio-economic status
    'W_FSTUWT',      # Student sampling weight
    'IMMIG',         # Immigration status

    # Life satisfaction
    'ST016Q01NA',    # Overall life satisfaction (0-10 Cantril)

    # Sense of belonging (6 items, 1=Strongly agree to 4=Strongly disagree)
    'ST034Q01TA',    # Outsider
    'ST034Q02TA',    # Make friends easily
    'ST034Q03TA',    # Belong
    'ST034Q04TA',    # Awkward
    'ST034Q05TA',    # Others like me
    'ST034Q06TA',    # Lonely

    # IC177: Weekday leisure hours (1=None, 2=<1h, 3=1-3h, 4=3-5h, 5=5-7h, 6=>7h)
    'IC177Q01JA',    # Video games
    'IC177Q02JA',    # Browse social networks
    'IC177Q03JA',    # Browse internet for fun
    'IC177Q04JA',    # Practical info
    'IC177Q05JA',    # Communicate/share on social networks
    'IC177Q06JA',    # Informational materials
    'IC177Q07JA',    # Create/edit digital content

    # IC178: Weekend day leisure hours (same scale)
    'IC178Q01JA',    # Video games
    'IC178Q02JA',    # Browse social networks
    'IC178Q03JA',    # Browse internet for fun
    'IC178Q04JA',    # Practical info
    'IC178Q05JA',    # Communicate/share on social networks
    'IC178Q06JA',    # Informational materials
    'IC178Q07JA',    # Create/edit digital content

    # IC181: Negative online experiences
    'IC181Q01JA',    # Inappropriate content
    'IC181Q02JA',    # Discriminatory content
    'IC181Q03JA',    # Unkind messages
    'IC181Q04JA',    # Personal info exposed

    # Performance (first plausible value only for quick estimates)
    'PV1MATH',
    'PV1READ',
    'PV1SCIE',
]

# Map IC177/IC178 categorical codes to approximate midpoint hours
HOURS_MAP = {1: 0, 2: 0.5, 3: 2, 4: 4, 5: 6, 6: 7.5}

# Social media composite: average of browsing + communicating on social networks
SM_WEEKDAY_VARS = ['IC177Q02JA', 'IC177Q05JA']
SM_WEEKEND_VARS = ['IC178Q02JA', 'IC178Q05JA']


def unzip_if_needed(zip_path: Path, target_dir: Path) -> Path:
    """Unzip the SPSS zip file if the .sav file doesn't exist yet."""
    sav_files = list(target_dir.glob("*.sav")) + list(target_dir.glob("*.SAV"))
    if sav_files:
        return sav_files[0]

    print(f"Unzipping {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(target_dir)

    sav_files = list(target_dir.glob("*.sav")) + list(target_dir.glob("*.SAV"))
    if not sav_files:
        raise FileNotFoundError("No .sav file found after unzipping")
    return sav_files[0]


def read_pisa_data(sav_path: Path) -> pd.DataFrame:
    """Read PISA SPSS data, selecting only needed columns."""
    print(f"Reading {sav_path.name}...")
    print(f"  Requesting {len(COLS_NEEDED)} columns...")

    # Read with column selection to save memory
    df, meta = pyreadstat.read_sav(
        str(sav_path),
        usecols=COLS_NEEDED,
        apply_value_formats=False  # Keep numeric codes
    )

    print(f"  Loaded {len(df):,} rows × {len(df.columns)} columns")
    print(f"  Countries: {df['CNT'].nunique()}")

    # Check ICT module availability
    ict_mask = df['IC177Q02JA'].notna()
    print(f"  Students with ICT data: {ict_mask.sum():,} ({100*ict_mask.mean():.1f}%)")
    print(f"  Countries with ICT data: {df.loc[ict_mask, 'CNT'].nunique()}")

    return df


def compute_weighted_mean(df, col, weight_col='W_FSTUWT'):
    """Compute weighted mean, dropping NaN."""
    mask = df[col].notna() & df[weight_col].notna()
    if mask.sum() == 0:
        return np.nan
    return np.average(df.loc[mask, col], weights=df.loc[mask, weight_col])


def compute_weighted_stats(df, col, weight_col='W_FSTUWT'):
    """Compute weighted mean and SE."""
    mask = df[col].notna() & df[weight_col].notna()
    n = mask.sum()
    if n == 0:
        return np.nan, np.nan, 0
    values = df.loc[mask, col].values
    weights = df.loc[mask, weight_col].values
    wmean = np.average(values, weights=weights)
    # Weighted variance
    wvar = np.average((values - wmean)**2, weights=weights)
    wse = np.sqrt(wvar / n) if n > 1 else np.nan
    return wmean, wse, n


def map_to_hours(series):
    """Map IC177/IC178 categorical codes to approximate hours."""
    return series.map(HOURS_MAP)


def compute_country_means(df):
    """Compute country-level weighted means for all key variables."""
    results = []

    for cnt, grp in df.groupby('CNT'):
        row = {'country_code': cnt, 'n_students': len(grp)}

        # Life satisfaction
        ls_mean, ls_se, ls_n = compute_weighted_stats(grp, 'ST016Q01NA')
        row['life_satisfaction_mean'] = ls_mean
        row['life_satisfaction_se'] = ls_se
        row['life_satisfaction_n'] = ls_n

        # Belonging items (reverse-code negative items: Q01, Q04, Q06)
        belong_cols = ['ST034Q01TA', 'ST034Q02TA', 'ST034Q03TA',
                       'ST034Q04TA', 'ST034Q05TA', 'ST034Q06TA']
        for col in belong_cols:
            row[f'{col}_mean'] = compute_weighted_mean(grp, col)

        # Social media hours (weekday)
        for var in ['IC177Q02JA', 'IC177Q05JA']:
            hours = map_to_hours(grp[var]) if var in grp.columns else pd.Series(dtype=float)
            row[f'{var}_hours_mean'] = compute_weighted_mean(
                grp.assign(**{f'{var}_hours': hours}), f'{var}_hours'
            ) if var in grp.columns else np.nan

        # Social media hours (weekend)
        for var in ['IC178Q02JA', 'IC178Q05JA']:
            hours = map_to_hours(grp[var]) if var in grp.columns else pd.Series(dtype=float)
            row[f'{var}_hours_mean'] = compute_weighted_mean(
                grp.assign(**{f'{var}_hours': hours}), f'{var}_hours'
            ) if var in grp.columns else np.nan

        # Composite social media hours (weekday average of browsing + communicating)
        if all(v in grp.columns for v in SM_WEEKDAY_VARS):
            sm_wd = grp[SM_WEEKDAY_VARS].apply(lambda s: s.map(HOURS_MAP)).mean(axis=1)
            mask = sm_wd.notna() & grp['W_FSTUWT'].notna()
            if mask.sum() > 0:
                row['sm_weekday_hours_mean'] = np.average(sm_wd[mask], weights=grp.loc[mask, 'W_FSTUWT'])
            else:
                row['sm_weekday_hours_mean'] = np.nan
        else:
            row['sm_weekday_hours_mean'] = np.nan

        if all(v in grp.columns for v in SM_WEEKEND_VARS):
            sm_we = grp[SM_WEEKEND_VARS].apply(lambda s: s.map(HOURS_MAP)).mean(axis=1)
            mask = sm_we.notna() & grp['W_FSTUWT'].notna()
            if mask.sum() > 0:
                row['sm_weekend_hours_mean'] = np.average(sm_we[mask], weights=grp.loc[mask, 'W_FSTUWT'])
            else:
                row['sm_weekend_hours_mean'] = np.nan
        else:
            row['sm_weekend_hours_mean'] = np.nan

        # Video games weekday
        if 'IC177Q01JA' in grp.columns:
            vg_hours = map_to_hours(grp['IC177Q01JA'])
            mask = vg_hours.notna() & grp['W_FSTUWT'].notna()
            row['gaming_weekday_hours_mean'] = np.average(vg_hours[mask], weights=grp.loc[mask, 'W_FSTUWT']) if mask.sum() > 0 else np.nan

        # Negative online experiences (proportion reporting each)
        for var in ['IC181Q01JA', 'IC181Q02JA', 'IC181Q03JA', 'IC181Q04JA']:
            if var in grp.columns:
                # Proportion "happened and upset" (codes 3, 4, 5 = a little/quite/very upset)
                upset = (grp[var] >= 3).astype(float)
                upset[grp[var].isna()] = np.nan
                row[f'{var}_upset_pct'] = compute_weighted_mean(
                    grp.assign(**{f'{var}_upset': upset}), f'{var}_upset'
                )

        # Performance
        row['math_pv1'] = compute_weighted_mean(grp, 'PV1MATH')
        row['read_pv1'] = compute_weighted_mean(grp, 'PV1READ')
        row['science_pv1'] = compute_weighted_mean(grp, 'PV1SCIE')

        # ESCS
        row['escs_mean'] = compute_weighted_mean(grp, 'ESCS')

        results.append(row)

    return pd.DataFrame(results)


def compute_gender_country_means(df):
    """Compute country-level means stratified by gender."""
    results = []

    for (cnt, gender), grp in df.groupby(['CNT', 'ST004D01T']):
        if pd.isna(gender):
            continue

        gender_label = 'female' if gender == 1 else 'male' if gender == 2 else 'other'
        row = {
            'country_code': cnt,
            'gender': gender_label,
            'n_students': len(grp),
        }

        # Life satisfaction
        row['life_satisfaction_mean'], row['life_satisfaction_se'], row['life_satisfaction_n'] = \
            compute_weighted_stats(grp, 'ST016Q01NA')

        # Social media weekday composite
        if all(v in grp.columns for v in SM_WEEKDAY_VARS):
            sm_wd = grp[SM_WEEKDAY_VARS].apply(lambda s: s.map(HOURS_MAP)).mean(axis=1)
            mask = sm_wd.notna() & grp['W_FSTUWT'].notna()
            row['sm_weekday_hours_mean'] = np.average(sm_wd[mask], weights=grp.loc[mask, 'W_FSTUWT']) if mask.sum() > 0 else np.nan
        else:
            row['sm_weekday_hours_mean'] = np.nan

        results.append(row)

    return pd.DataFrame(results)


def compute_dose_response(df):
    """Compute life satisfaction by social media use category, by country and gender."""
    results = []

    # Use IC177Q02JA (browse social networks, weekday) as the dose variable
    dose_var = 'IC177Q02JA'
    dose_labels = {1: 'None', 2: '<1hr', 3: '1-3hr', 4: '3-5hr', 5: '5-7hr', 6: '>7hr'}

    for (cnt, gender), grp in df.groupby(['CNT', 'ST004D01T']):
        if pd.isna(gender) or dose_var not in grp.columns:
            continue

        gender_label = 'female' if gender == 1 else 'male' if gender == 2 else 'other'

        for dose_code, dose_label in dose_labels.items():
            dose_grp = grp[grp[dose_var] == dose_code]
            if len(dose_grp) < 10:
                continue

            ls_mean, ls_se, ls_n = compute_weighted_stats(dose_grp, 'ST016Q01NA')

            results.append({
                'country_code': cnt,
                'gender': gender_label,
                'sm_category': dose_label,
                'sm_code': dose_code,
                'life_satisfaction_mean': ls_mean,
                'life_satisfaction_se': ls_se,
                'n': ls_n,
            })

    return pd.DataFrame(results)


def main():
    print("=" * 70)
    print("PISA 2022 Social Media & Wellbeing — Country-Level Extraction")
    print("=" * 70)

    # Find and unzip the data
    zip_path = SCRIPT_DIR / "STU_QQQ_SPSS.zip"
    if not zip_path.exists():
        print(f"ERROR: {zip_path} not found. Download it first:")
        print(f"  curl -o {zip_path} https://webfs.oecd.org/pisa2022/STU_QQQ_SPSS.zip")
        sys.exit(1)

    sav_path = unzip_if_needed(zip_path, SCRIPT_DIR)

    # Read data
    df = read_pisa_data(sav_path)

    # Compute country means
    print("\n--- Computing country-level means ---")
    country_df = compute_country_means(df)
    out_path = SCRIPT_DIR / "pisa_country_means.csv"
    country_df.to_csv(out_path, index=False, float_format='%.4f')
    print(f"  Saved {len(country_df)} countries to {out_path.name}")

    # Print summary
    print("\n  Top 5 life satisfaction:")
    top5 = country_df.nlargest(5, 'life_satisfaction_mean')
    for _, r in top5.iterrows():
        print(f"    {r['country_code']}: {r['life_satisfaction_mean']:.2f} (SM weekday: {r['sm_weekday_hours_mean']:.2f}h)")

    print("\n  Bottom 5 life satisfaction:")
    bot5 = country_df.nsmallest(5, 'life_satisfaction_mean')
    for _, r in bot5.iterrows():
        print(f"    {r['country_code']}: {r['life_satisfaction_mean']:.2f} (SM weekday: {r['sm_weekday_hours_mean']:.2f}h)")

    # Compute gender-stratified means
    print("\n--- Computing gender-stratified country means ---")
    gender_df = compute_gender_country_means(df)
    out_path = SCRIPT_DIR / "pisa_gender_means.csv"
    gender_df.to_csv(out_path, index=False, float_format='%.4f')
    print(f"  Saved {len(gender_df)} rows to {out_path.name}")

    # Compute dose-response
    print("\n--- Computing dose-response curves ---")
    dose_df = compute_dose_response(df)
    out_path = SCRIPT_DIR / "pisa_dose_response.csv"
    dose_df.to_csv(out_path, index=False, float_format='%.4f')
    print(f"  Saved {len(dose_df)} rows to {out_path.name}")

    # Quick correlation
    print("\n--- Country-level correlation (SM hours vs Life Satisfaction) ---")
    valid = country_df.dropna(subset=['sm_weekday_hours_mean', 'life_satisfaction_mean'])
    if len(valid) >= 5:
        from scipy import stats
        r, p = stats.pearsonr(valid['sm_weekday_hours_mean'], valid['life_satisfaction_mean'])
        rho, prho = stats.spearmanr(valid['sm_weekday_hours_mean'], valid['life_satisfaction_mean'])
        print(f"  N = {len(valid)} countries with both SM and life satisfaction data")
        print(f"  Pearson r  = {r:+.4f} (p = {p:.6f})")
        print(f"  Spearman ρ = {rho:+.4f} (p = {prho:.6f})")
    else:
        print(f"  Only {len(valid)} countries with both variables — insufficient for correlation")

    print("\n" + "=" * 70)
    print("EXTRACTION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
