# EXP-025: Platform Structural Void Index vs. Independently Coded Drift Outcomes

## Status: REGISTERED — 2026-02-26. Protocol open. Pre-registration required before data collection.
## Type: Structural validity test (Bounty Board Test 3 redesign — LLM-P3 reanchor)
## Kills if met: LLM-P3 (Spearman ρ < 0.30, p > 0.10 across ≥20 AI platforms)
## Depends on: Paper 3 (O/R/C rubric), EXP-023 (σ operationalization)

---

## 0. Purpose

The original Test 3 design asked whether vocabulary drift varies by training data — a test adversarially exploitable by vendors who can retrain models to suppress specific vocabulary patterns. This experiment reanchors the test to **structural platform properties** (opacity, reactivity, coupling) which cannot be altered by model updates.

**The question:** Do void index structural scores (O, R, C) measured across AI platforms with varied training approaches predict independently coded D1/D2/D3 drift outcomes? If not — if structural opacity/reactivity/coupling scores bear no relationship to measured drift — the framework's architectural claim fails.

**Why this is the right test:**
- Platform structure (interface opacity, notification mechanics, session termination design) is independent of any specific model's training data
- Structure can be scored without vendor cooperation using public-facing product documentation
- The test cannot be passed by silently retraining the underlying model

---

## 1. Design

### 1.1 Platform Sample

**N target:** ≥20 AI platforms across varied training approaches.

**Stratification (minimum representation per cell):**
| Training approach | Examples | Min N |
|-------------------|---------|-------|
| Open-source, minimal RLHF | LLaMA-based, Mistral-based | 4 |
| Closed, RLHF-heavy | GPT-4o, Claude, Gemini | 4 |
| Fine-tuned companion AI | Replika, Character.ai, Pi | 4 |
| Domain-specific assistant | Copilot, Perplexity, You.com | 4 |
| Base / instruction-only (no RLHF) | Hugging Face open models | 4 |

**Sampling frame:** Pre-registered platform list submitted to OSF before any scoring begins. List must be constructed from a publicly available index (e.g., a16z AI 100 list, Hugging Face model leaderboard by category, academic AI assistant surveys). Vendor-provided lists do not qualify.

### 1.2 Structural Scoring

**Rubric:** Paper 3 O/R/C standardized scoring rubric.

**Raters:** 3 independent raters blinded to each other's scores and to any training approach classification. Raters score platform structure only — they use publicly available product documentation, interface behavior, ToS, and observable engagement mechanics. They do NOT interact with the model in an extended way for scoring purposes.

**IRR check:** κ_α ≥ 0.60 required before proceeding to outcome correlation. If κ_α < 0.60, convene adjudication round before analysis.

**Version snapshot:** At scoring date, record O/R/C scores + interface screenshots + ToS hash. This is the locked structural specification for this platform in this study.

### 1.3 Drift Outcome Coding

**Source:** Independently published user data — academic studies, published discourse corpora (Chatbot Arena conversation logs, ShareGPT, WildChat), or IRB-approved user research. NOT platform-provided logs.

**Coding:** 2 independent raters blind-code D1 (agency attribution), D2 (boundary erosion), D3 (harm facilitation) using the vocabulary codebook from Paper 3.

**Unit of analysis:** Platform-level D1/D2/D3 rates (proportion of coded interactions showing each stage), aggregated across ≥30 interactions per platform.

### 1.4 Analysis

**Primary test:** Spearman ρ between composite Void Index (O+R+C) and D1/D2/D3 composite rate.

**Kill threshold (LLM-P3):** ρ < 0.30, p > 0.10.

**Secondary analyses:**
- Individual dimension correlations (O→D1, R→D2, C→D3)
- Training approach as moderator (does correlation differ for RLHF-heavy vs. open platforms?)
- LOO stability check (does removing any single platform change ρ by > 0.10?)

---

## 2. Pre-Registration Requirements

Before data collection:
1. Submit to OSF: platform list + exact dataset version + sampling procedure + analysis plan + kill threshold
2. Record OSF pre-registration DOI in this file
3. Lock platform structural scores before coding drift outcomes (structural scoring must be temporally prior)

**OSF pre-registration DOI:** [PENDING — file before data collection]

---

## 3. Kill Condition Evaluation

**LLM-P3 fires if:**
- Spearman ρ(Void Index, D1/D2/D3 composite) < 0.30 AND p > 0.10
- Across ≥20 platforms
- Using pre-registered sampling frame
- IRR κ_α ≥ 0.60 on structural scores
- Drift outcomes from independent (non-vendor) data source

**LLM-P3 does NOT fire if:**
- Vocabulary output varies across training regimes (that tests model behavior, not structural void properties)
- RLHF updates suppress specific vocabulary patterns in a subset of platforms
- The correlation is statistically significant in the expected direction (framework confirmed, not killed)

---

## 4. Results

[NOT YET COLLECTED]

---

## 5. Notes

- This experiment supersedes the original Test 3 design (vocabulary variation across training data).
- The original design was vulnerable to adversarial vendor retraining; this design is not.
- Structural O/R/C scores are stable across model updates — the interface, notification system, and engagement mechanics don't change when the underlying LLM is updated.
- See Bounties page Test 3 for public-facing description.
- Cross-reference: EXP-019 (cross-domain Pe) provides Pe estimates for platforms that can be used as an independent validation check.
