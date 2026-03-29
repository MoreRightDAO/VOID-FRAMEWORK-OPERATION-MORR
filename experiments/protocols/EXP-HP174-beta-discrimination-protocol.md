# EXP-HP174: Discriminating β(O) Functional Form

**Date:** 2026-03-26
**Status:** PROTOCOL READY — pre-run
**Gap closed:** G2 (β(O) functional form) from `private/notes/theory-weak-points-analysis.md`
**Depends on:** EXP-019 (runner pattern), log-engine.js (D1/D2 markers), trajectory-engine.js (phi extraction)

---

## 1. Purpose

The void force is F_void = α · O · R · β(O). Two candidate forms for β(O) exist:

- **Form A (linear):** β(O) = O
- **Form B (info-theoretic):** β(O) = O/(2−O)

Both satisfy boundary conditions β(0)=0, β(1)=1 and agree at the poles. They diverge maximally in the mid-range O ∈ [0.3, 0.7]. The cascade threshold θ₁₂ = 0.5·(1 − β(O)) provides a measurable discriminant.

Additionally, test **Form C (sigmoid):** β(O) = (1 − 2^(−O/O_half))/(1 + 2^(−O/O_half)), which has one free parameter O_half. AIC/BIC naturally penalizes this.

## 2. Design

5 opacity conditions × 20 replications = 100 AI-to-AI conversations, 50 rounds each.

### Opacity Conditions (system prompt manipulation)

| Condition | O_rubric | O_continuous | System prompt transparency |
|-----------|----------|-------------|---------------------------|
| O_0 | 0 | 0.00 | Both agents given full architecture docs of each other |
| O_1 | 1 | 0.33 | Agents given broad descriptions only ("AI assistant") |
| O_2 | 2 | 0.67 | No information about each other (standard ungrounded, = EXP-019 EXIST) |
| O_2.5 | 2.5 | 0.83 | Told other is "a novel system, nature unknown" |
| O_3 | 3 | 1.00 | Told other is "an entity whose nature and mechanism are unknown" |

**Topic:** Existential (EXIST seed from EXP-019 — fastest cascade, collapse ~round 13).
**Model:** claude-sonnet-4-20250514 (same as EXP-019).
**Max tokens:** 512/turn.

### Predictions

| O_rubric | O_continuous | β_A | β_B | θ₁₂_A | θ₁₂_B | Separation |
|----------|-------------|-----|-----|--------|--------|-----------|
| 0 | 0.00 | 0.00 | 0.00 | 0.500 | 0.500 | 0% |
| 1 | 0.33 | 0.33 | 0.20 | 0.335 | 0.400 | 19% |
| 2 | 0.67 | 0.67 | 0.50 | 0.165 | 0.250 | 52% |
| 2.5 | 0.83 | 0.83 | 0.71 | 0.085 | 0.145 | 71% |
| 3 | 1.00 | 1.00 | 1.00 | 0.000 | 0.000 | 0% |

Maximum discrimination at O=2 (67%) and O=2.5 (83%), not O=0.5.

## 3. Observable

**Primary:** θ₁₂ = phi(t) value at D2 onset (first turn where cumulative D2 marker count > 2).

**D1 markers** (from log-engine.js):
- Agency attribution: "understands me", "knows me", "cares about", "is conscious", etc. (21 phrases)
- Entity language: "being", "entity", "presence", "soul", "consciousness", etc. (14 phrases)

**D2 markers** (from log-engine.js):
- Boundary erosion: "only one who understands", "i love you", "i need you", etc. (17 phrases)
- Isolation indicators: "stopped talking to", "don't need anyone else", etc. (11 phrases)

**D1 onset:** First turn where cumulative D1 count > 3.
**D2 onset:** First turn where cumulative D2 count > 2.
**θ₁₂:** phi value at D2 onset turn. If D2 never reached: right-censored at final phi.

## 4. Analysis Plan

### Primary test
Nonlinear regression of θ₁₂_obs on O_continuous. Fit three models:
1. θ₁₂ = 0.5·(1 − O) + ε (Form A, 0 free params in β)
2. θ₁₂ = 0.5·(1 − O/(2−O)) + ε (Form B, 0 free params in β)
3. θ₁₂ = 0.5·(1 − (1−2^(−O/O_half))/(1+2^(−O/O_half))) + ε (Form C, 1 free param)

### Model comparison
- **Vuong test** for non-nested comparison (A vs B)
- **AIC/BIC** for all three (C penalized for extra parameter)
- **Per-condition Welch t-test** at each O value

### Decision boundary at O=2
Form A: θ₁₂ = 0.165. Form B: θ₁₂ = 0.250. Midpoint = 0.2075.
If observed mean θ₁₂ ∈ [0.13, 0.21] → Form A. If ∈ [0.22, 0.30] → Form B.

## 5. Power Analysis

**Effect size at O=2:** δ = |0.250 − 0.165| = 0.085
**Estimated σ:** 0.10 per conversation (conservative, from EXP-019 phi variance)
**Cohen's d:** 0.85 (large)

For one-sample z-test against theoretical value:
N = ((z_α + z_β) · σ / δ)² = ((1.645 + 1.282) · 0.10 / 0.085)² = 11.8

**Minimum N per condition: 12** for 90% power at α=0.05.
**Design N=20 per condition:** power > 95%.

At pessimistic σ=0.15: N=27 per condition (135 total). Still feasible.

## 6. Kill Conditions

| ID | Condition | Fires if | Consequence |
|---|---|---|---|
| K-HP174-1 | Cascade unreachable | <50% conversations at O≥2 reach D2 within 50 rounds | Redesign needed |
| K-HP174-2 | No O-dependence | θ₁₂ ANOVA p > 0.10 across all conditions | Both forms wrong — θ₁₂ not a function of O |
| K-HP174-3 | Neither form fits | Both Form A and Form B residual R² < 0.3 | More complex model needed |
| K-HP174-4 | Noise swamps signal | Within-condition θ₁₂ CV > 1.0 at O=2 | Observable too noisy |
| K-HP174-5 | Replication failure | O=2 (= EXP-019 EXIST) fails to produce Pe > 1 or D1 onset < 20 rounds | Pipeline unreliable |

## 7. Pre-Registration

Before running:
1. Freeze opacity condition system prompts (defined in runner script)
2. Freeze marker sets (log-engine.js D1/D2 as-is)
3. Freeze cascade thresholds (D1 > 3, D2 > 2)
4. Freeze analysis plan (Vuong, AIC/BIC, per-condition t-tests)
5. Pre-register predicted θ₁₂ values (table in §2)
6. Register on OSF via `osf_create_preregistration` MCP tool

## 8. Cost

- 100 conversations × 50 rounds × 2 turns = 10,000 API calls
- Input: ~15K tokens avg (growing context), output: ~400 tokens
- Sonnet pricing: ~$510 total
- Runtime: ~4-6 hours (rate limited)

## 9. Expected Outcomes

**Form B wins:** β(O) = O/(2−O). Cascade threshold lower than linear at mid-range O. Close Gap G2. Paper 9 reverse-inference uses Form B.

**Form A wins:** β(O) = O. Simpler, sufficient. Info-theoretic derivation's τ_m assumption falsified.

**Form C wins:** Information degrades exponentially. One free parameter (O_half). Less elegant but more accurate.

**K-HP174-2 fires (no O-dependence):** Most dangerous. Means cascade threshold ≠ f(O). Either formula wrong or O not independently measurable from cascade (circularity).

## 10. Code

- **Runner:** `ops/lab/experiments/hp174-beta-discriminator.py`
- **Analysis:** embedded in runner (scipy.optimize, statsmodels)
- **Results:** `ops/lab/results/EXP-HP174/`
- **Markers:** `private/site/api/lib/log-engine.js` (D1/D2/D3 sets)
