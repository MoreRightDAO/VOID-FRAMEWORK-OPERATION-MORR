# Protocol: State-Level Difference-in-Differences Analysis

**Date:** 2026-04-06
**Status:** READY — awaiting state-level YRBS data download
**Paper:** 173, §5.1 (Protocol A)
**Priority:** HIGH — closes GAP-2 (formal causal identification)

---

## Objective

Test whether US states with higher effective platform exposure show larger mental health increases, controlling for state and year fixed effects.

## Model

```
Sadness_st = α_s + γ_t + β·Pe_st + δ·X_st + ε_st
```

- s = state (~40 participating states)
- t = YRBS wave (2011, 2013, 2015, 2017, 2019, 2021, 2023)
- α_s = state fixed effects (absorb all time-invariant state characteristics)
- γ_t = year fixed effects (absorb all nationally shared shocks: COVID, elections, etc.)
- Pe_st = state-level platform exposure proxy
- X_st = time-varying covariates (broadband %, median income, unemployment)

**Coefficient of interest:** β — effect of state-level Pe on sadness, net of state and year effects.

## Data Acquisition Steps

### 1. State-Level YRBS (~4 hours)

**Source:** CDC YRBSS Data & Documentation
- URL: https://www.cdc.gov/yrbs/data/index.html
- State-level datasets are separate downloads from national combined dataset
- ~40 states per wave (not all states participate every year)

**Variables needed:**
- State identifier
- Survey year (2011–2023)
- Sex (for gender stratification)
- `q26` or equivalent: "During the past 12 months, did you ever feel so sad or hopeless almost every day for two weeks or more in a row that you stopped doing some usual activities?" (persistent sadness)
- `q27`: "During the past 12 months, did you ever seriously consider attempting suicide?" (suicidal ideation)
- Sampling weights

**Output:** `state_yrbs_data.csv` with columns: state, year, sex, pct_sadness, pct_suicide, n_respondents

### 2. State-Level Pe Proxy (~2 hours)

**Approach:** National platform adoption × state broadband/urban demographics

For each state-year:
```
Pe_st = Σ_p [feature_score_p × adoption_national_p × broadband_penetration_s × urban_share_s]
```

**Data sources:**
- National teen adoption by platform: Pew Research (✅ have it)
- Feature scores by platform-year: `feature-matrix.json` (✅ have it)
- State broadband penetration: FCC Form 477 → https://broadbandmap.fcc.gov/data-download
- State urbanization: Census ACS Table B01003 → https://data.census.gov

**Stronger variant:** If Pew state-level internet/smartphone data exists (check Pew data download portal), use directly instead of proxy.

### 3. Covariates (~1 hour)

- State median household income: Census ACS Table S1901
- State unemployment rate: BLS LAUS
- State-level GDP per capita: BEA Regional Accounts

## Analysis Plan

### Primary: Two-Way Fixed Effects

```python
import statsmodels.formula.api as smf

model = smf.ols('sadness ~ pe_proxy + broadband + C(state) + C(year)', data=panel)
result = model.fit(cov_type='cluster', cov_kwds={'groups': panel['state']})
```

Cluster standard errors at state level.

### Secondary: Event Study

```python
# Interact Pe with year dummies to visualize dynamic treatment effects
model_es = smf.ols('sadness ~ C(year)*pe_proxy + C(state)', data=panel)
```

Plot β_t × Pe coefficients over time. Should show near-zero pre-2016 and increasing post-2016 if the feature architecture shift matters.

### Robustness

1. Callaway-Sant'Anna (2021) estimator (handles staggered treatment)
2. Leave-one-state-out jackknife
3. Permutation: randomize state-level Pe assignment, check β distribution
4. Gender-stratified: run separately for female and male persistent sadness

## Kill Conditions

- **KC-D1:** β not significantly positive (p > 0.10) → DiD does not support causal claim
- **KC-D2:** Event study shows pre-trends (pre-2016 β_t significantly different from zero) → confounded
- **KC-D3:** Female β ≤ male β → gender specificity fails at state level

## Output Files

- `state_level_did_results.json`
- `state_level_event_study.json`
- `state_level_did_analysis.py`

## Estimated Timeline

| Step | Time | Status |
|------|------|--------|
| Download state YRBS | 4 hrs | ⬜ |
| Download FCC broadband | 1 hr | ⬜ |
| Compute state Pe proxy | 2 hrs | ⬜ |
| Download covariates | 1 hr | ⬜ |
| Run DiD analysis | 4 hrs | ⬜ |
| Write up results | 4 hrs | ⬜ |
| **Total** | **~2 days** | |
