# EXP-029: K-GEO-4 Pe-Stratified β·τ Analysis + Kramers Barrier Heights

**Date:** 2026-03-12
**Status:** Protocol
**Author:** Shamir / MoreRight

---

## Motivation

Two open threads from EXP-028:

1. **K-GEO-4** (§67H): does β·τ ≈ const hold, or does it systematically depend on Pe? Phase 2C
   showed CV=1.449, which survived the threshold (2.0) but P2 (CV<0.5) failed. We need to
   explicitly test whether β·τ is a function of Pe.

2. **Kramers barrier heights** (Paper 131): the geodesic interpretation of §67 predicts
   τ_collapse ~ exp(d_geo / T_eff) where d_geo is the geodesic distance from the current
   Eckert state to the D3 attractor. This is the Kramers escape formula applied to the
   (2,1) Eckert manifold. The quantitative check uses Phase 1A (7 AI conditions) +
   Phase 2C (46 countries).

---

## Data Sources

| Dataset | N | Variables available |
|---------|---|---------------------|
| Phase 1A (EXP-028) | 7 AI conditions | β (coupling asymmetry), Pe (from EXP-019), τ (from §67 table) |
| Phase 2C (EXP-028) | 46 countries | β, τ, Pe (R₀-derived) |

**Phase 1A τ values (from §67D table, authoritative):**
- EXIST: τ=17, GG-EXIST: τ=17, GU-EXIST: τ=50
- THER: τ=27, TRADE: τ=34
- GAMBL: τ=? (missing — excluded from τ analysis)
- NEUT: τ=? (missing — excluded from τ analysis)

---

## Geodesic Distance from Pe

Pe → c inverse: `c = (b_α - arcsinh(Pe/K)/2) / b_γ`
where b_α=0.867, b_γ=2.244, K=16.

D3 threshold: Pe* = 5.52 → c* ≈ 0.311 (solved numerically)

Geodesic in 1D (equal-coordinate direction):
`d_geo = 2 |arcsin(√c) - arcsin(√c*)|`

Note: this is a lower-bound on the full 3D geodesic. The 3D geodesic requires full
(O, R, α) triple. For Paper 131 the 1D approximation is sufficient for the first
quantitative test.

---

## Hypotheses

**H1 (K-GEO-4):** β·τ does NOT systematically depend on Pe.
- Test: Spearman ρ(β·τ, Pe) across pooled Phase 1A + 2C data
- Kill K-GEO-4: |ρ| > 0.4 with p < 0.05

**H2 (Kramers):** ln(τ) is linearly proportional to d_geo.
- Test: OLS regression ln(τ) ~ d_geo, check R² and slope sign
- Prediction: positive slope (larger d_geo → longer escape time)
- Kill condition K-29-1: slope ≤ 0 with p < 0.10

**H3 (cross-substrate Kramers):** If τ ~ exp(d_geo/T_eff), then T_eff should
be substrate-specific (AI vs epidemic). Fit separate T_eff per substrate and check
if they're distinguishable.

---

## Kill Conditions

| ID | Condition | Kills |
|----|-----------|-------|
| K-GEO-4 | β·τ Spearman ρ with Pe has \|ρ\| > 0.4, p < 0.05 | §67D constant-product model |
| K-29-1 | Kramers slope ≤ 0 (longer geodesic does NOT predict longer collapse) | §67C-D geometric interpretation |
| K-29-2 | No exponential relationship — R²(ln τ ~ d_geo) < 0.10 | Kramers framework applicability |
| K-29-3 | T_eff estimates have overlapping 95% CI across substrates | Substrate-specific T_eff claim |

---

## Predictions

| ID | Prediction | Threshold |
|----|-----------|-----------|
| P-29-1 | Kramers slope positive | d_geo explains ≥20% of ln(τ) variance |
| P-29-2 | T_eff(AI) < T_eff(epidemic) | AI substrates "colder" (more constrained dynamics) |
| P-29-3 | β·τ CV < 1.5 within each substrate | Constant consistent within substrate |
| P-29-4 | β·τ systematically higher for epidemic substrate | Substrate-specific constant |

---

## Script

`ops/lab/experiments/nb_exp029_kgeo4_kramers.py`

## Results

`ops/lab/results/nb_exp029_kgeo4_kramers/results.json`
