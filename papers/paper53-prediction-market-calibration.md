<!--
⛔ HARD GATE — DO NOT RUN run_pipeline(write=True) OR zenodo_upload() ON THIS PAPER.

This paper requires REAL DATA from resolved prediction markets.
Current resolved markets: 0
Write trigger: N ≥ 20 resolved markets with real Brier scores.
First possible data point: CAR-P2, Aug 21 2026.
Pre-registration: GitHub (this file, committed before first market resolution)

Publishing before markets resolve fabricates results and voids the pre-registration.
The source analysis is done. The stub is complete. The pipeline is NOT ready.
See decisions.md 2026-02-25 for the explicit prohibition.
-->
---
title: "The Calibration Signal: Community Epistemic Markets on Pe-Relevant Outcomes and Framework Prediction Validity"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 53"
short-title: "The Calibration Signal"
version: "v1.0"
date: "2026"
license: "cc-by-4.0"
preregistration: "GitHub — committed 2026-02-24, before first market resolution"
preregistration_date: "2026-02-24"
first_resolution_deadline: "2026-08-21"
---

# The Calibration Signal: Community Epistemic Markets on Pe-Relevant Outcomes and Framework Prediction Validity

**Pre-registered study.** Committed to GitHub before first market resolution (CAR-P2, Aug 21 2026). This file's commit timestamp is the pre-registration proof.

---

## Abstract

*[Written after N ≥ 20 markets resolve.]*

The void framework (Papers 1–52) makes 300 falsifiable predictions across 26 explicit kill conditions. Beginning February 2026, community prediction markets were deployed on these predictions at moreright.xyz/pages/predictions.html. This paper reports the calibration test: do community markets on Pe-relevant outcomes produce well-calibrated forecasts (Brier score < 0.25), and do Pe_implied trajectories derived from market prices outperform naive Pe_current baselines in predicting ICC-validated platform measurements? Market resolution criteria and the Pe_implied formula were pre-committed before any market opened. Analysis plan pre-registered on OSF before first resolution.

**Primary result:** *[Written after N ≥ 20 markets resolve.]*

---

## I. Introduction

The void framework's empirical program depends on pre-committed falsifiability. Papers 1–52 establish 300 testable predictions; 26 explicit kill conditions specify the exact circumstances under which the framework would be proven wrong. The prediction market system extends this structure in a novel direction: rather than waiting for events to occur and then measuring framework accuracy, it solicits community probability estimates *in advance* and tests whether those estimates are calibrated.

A well-calibrated forecaster, when they say an event has probability P, is right P fraction of the time. Calibration is measured by Brier score. If community markets on void framework predictions are well-calibrated (Brier < 0.25), it means the crowd can distinguish high-Pe from low-Pe outcomes in advance, better than chance. This would be the strongest possible demonstration of framework validity: predictive community epistemic judgment on our own kill conditions.

If markets fail to calibrate (Brier > 0.33 consistently), it constitutes a kill condition on the epistemic market hypothesis itself.

### 1.1 Pre-registration

This study is pre-registered. The analysis plan was committed to the public GitHub repository on February 24, 2026, before any market resolved. The pre-registration is this file — the commit timestamp is the proof.

**Pre-commitment chain:**
1. Market resolution criteria — committed Feb 24, 2026 (before markets opened)
2. Pe_implied formula — committed Feb 24, 2026 (before markets opened)
3. Analysis methodology — committed Feb 24, 2026 (this pre-registration, before first resolution)

No element of the analysis plan was modified after CAR-P2 resolved.

---

## II. Methods

### 2.1 Market Infrastructure

Markets were deployed at moreright.xyz/pages/predictions.html on February 24, 2026. Three categories:

| Category | Description | N at pre-reg |
|----------|-------------|-------------|
| `live_event` | Geopolitical outcomes with Pe relevance (cartel-void) | 4 |
| `kill_condition` | Explicit framework falsification conditions (K1–K26) | 26 |
| `platform_pe` | Platform Pe trajectory predictions | 4 |

**Total at pre-registration:** 34 markets. Additional markets may be added before analysis; they are included if they resolve before the analysis cutoff (Dec 31, 2027).

### 2.2 Staking Mechanism

Participants stake credits (1 credit = $1 service value on moreright.xyz) on YES or NO for each market. Credits are deducted at stake time and returned proportionally from the winning pool at resolution. P(yes) at stake time is recorded per stake (p_at_stake field).

Simple pool model: P(yes) = total_yes / (total_yes + total_no). Maximum stake: 500 credits. Minimum: 5 credits.

### 2.3 Resolution

Admin resolves each market against observable evidence per pre-committed criteria. Resolution note is published. Stakes settled proportionally from winning pool. Settled stake records include payout and Brier score.

Voided markets (resolution criteria not met — e.g. conditional markets where the conditioning event did not occur) are excluded from analysis.

### 2.4 Pe_implied Formula (Pre-committed)

```
signal_i = weight_i × (P_yes − 0.5) × 2 × direction_sign_i
Pe_implied = Pe_current × (1 + Σ signal_i)

direction_sign = +1 if pe_direction = 'increases'
direction_sign = −1 if pe_direction = 'decreases'
```

This formula was pre-committed before any market opened. It is not updated at analysis time.

### 2.5 Brier Score

For each resolved market m with ≥ 3 stakes:

```
B_i    = (P_at_stake_i − O_outcome)²     [per stake]
B_m    = mean(B_i)                        [per market]
B_study = mean(B_m)                       [across markets]
```

O_outcome = 1 if resolved YES, 0 if resolved NO.

### 2.6 Inclusion Criteria

Included in primary Brier analysis:
- Status: resolved (not open, voided)
- Minimum stakes before resolution: ≥ 3
- Resolution against pre-committed criteria (no protocol deviations)

Excluded: voided markets, markets with < 3 stakes, markets where criteria were modified after opening.

---

## III. Hypotheses (Pre-registered)

**H1 (Confirmatory):** Mean Brier score < 0.25 across N ≥ 20 resolved markets.
*Test: one-sample t-test, μ₀ = 0.25, one-tailed, α = 0.05*

**H2 (Confirmatory):** RMSE(Pe_implied → actual Pe) < RMSE(Pe_current → actual Pe) for platform_pe markets with subsequent ICC-validated scores within 6 months of resolution.
*Test: paired t-test on RMSE, one-tailed, α = 0.05*

**H3–H5 (Exploratory):** See pre-registration document. Not confirmatory.

### Kill Conditions (Pre-registered)

| Code | Condition |
|------|-----------|
| KM1 | Mean Brier > 0.33 across N ≥ 20 markets → epistemic market claim falsified |
| KM2 | Pe_implied RMSE ≥ Pe_current RMSE → market signal adds nothing |
| KM3 | Mean Brier > 0.25 at N ≥ 50 → not well-calibrated at scale |

---

## IV. Results

*[Written after N ≥ 20 markets resolve. Target: Q4 2026 interim at N ≥ 5, Q2 2027 final at N ≥ 20.]*

### 4.1 Resolved Markets Summary

*[Table: slug, category, outcome, stake_count, total_staked, mean_Brier, resolution_date]*

### 4.2 Calibration (H1)

*[Brier score distribution, mean, CI, t-statistic, p-value]*

### 4.3 Calibration Curve

*[Reliability diagram: predicted P vs observed outcome rate by bin]*

### 4.4 Pe_implied vs Pe_current (H2)

*[RMSE comparison, paired t-test, effect size]*

### 4.5 Pe Signal Divergence Archive

*[Pe_implied trajectory vs Pe_model over time for cartel-void and platform markets]*

---

## V. Discussion

*[Written after results.]*

---

## VI. Falsifiable Predictions (This Paper)

| ID | Prediction | Resolution |
|----|-----------|-----------|
| P53-1 | Mean Brier < 0.25 across N ≥ 20 resolved markets | Primary confirmatory result |
| P53-2 | Pe_implied outperforms Pe_current in RMSE | Secondary confirmatory result |
| P53-3 | Kill condition markets have lower Brier than live_event markets | Exploratory |
| P53-4 | Market stake velocity positively correlates with calibration quality | Exploratory |

---

## VII. Kill Conditions (This Paper)

| Code | Trigger | Consequence |
|------|---------|-------------|
| KM1 | Mean Brier > 0.33 at N ≥ 20 | Epistemic market claim in framework falsified |
| KM2 | Pe_implied RMSE ≥ Pe_current at N ≥ 5 platform markets | Pe_implied formula invalid as predictor |
| KM3 | Mean Brier > 0.25 at N ≥ 50 | Markets not well-calibrated at scale |

---

## VIII. Data and Code

Full stake history: `GET /api/v1/predictions/:slug/history` (public, no auth)
All resolution criteria and evidence: `moreright.xyz/pages/predictions.html`
Analysis code: *[Added at submission — Python, pandas, scipy]*

---

## IX. Limitations

1. **Self-operated platform** — MoreRight operates both the markets and resolves them. Structural mitigation: pre-committed resolution criteria, published evidence, pre-registered analysis plan.
2. **Small N early** — CAR markets resolve in 2026-2027; kill condition markets resolve 2028-2030. Primary analysis at N ≥ 20 may be underpowered for exploratory analyses.
3. **Credit stakes, not money** — Credits are $1 service value (not cash), which may affect forecaster incentives relative to real-money markets. Expected direction of bias: underconfidence (stakers may not maximize information).
4. **Market maker absent** — No LMSR or automated market maker. Early prices may be noise; calibration measured on all stakes including early thin-market ones.

---

## X. Contributions

*[Standard framework contribution statement at submission.]*

---

## References

*[Added at submission — minimum 10 for Tier 1.]*

Key references to include:
- Brier GW (1950) — Brier score original paper
- Tetlock PE (2005) — Superforecasting precursor (Expert Political Judgment)
- Tetlock & Gardner (2015) — Superforecasting
- Hanson R (2003) — Combinatorial prediction markets
- Papers 1–52 (void framework) — Zenodo DOIs
- Gneezy & Potters (1997) — Risk taking frequency
- Prelec & Loewenstein (1991) — Decision and Experience

---

*Paper 53 | The Calibration Signal | Pre-registered Feb 24, 2026*
*Pipeline status: registered — awaiting market resolutions*
*First resolution: CAR-P2 Aug 21, 2026*
