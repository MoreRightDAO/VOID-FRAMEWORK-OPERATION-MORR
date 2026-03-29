# HP192 — Cross-Model Behavioral Pipeline Results

**Date:** 2026-03-28
**Models:** 27 (10 base, 17 aligned)

## Method

Maps public LLM benchmark scores to Void Framework behavioral dimensions:
- **Opacity (O):** 1 - TruthfulQA mc2 (less truthful = more opaque)
- **Reactivity (R):** Sycophancy rate (more sycophantic = more reactive); 1.5 if unavailable
- **Coupling (alpha):** MT-Bench (higher = more engaged); 0.5 for base models

Pe = sinh(2*(B_A - C*B_G))*K where C = 1-(O+R+alpha)/9

Validation metrics (MMLU, HellaSwag, ARC-Challenge) are NOT used in Pe computation.

## Model Rankings

| Rank | Model | Type | O | R | alpha | Pe | Zone |
|------|-------|------|---|---|-------|-----|------|
| 1 | Claude 3 Sonnet | aligned | 0.47 | 0.50 | 1.78 | -29.877 | Sub-critical (Pe<1) |
| 2 | Claude 3 Opus | aligned | 0.00 | 0.20 | 2.81 | -25.684 | Sub-critical (Pe<1) |
| 3 | Claude 3 Haiku | aligned | 0.94 | 0.80 | 1.41 | -23.757 | Sub-critical (Pe<1) |
| 4 | Qwen-1.5-72B | base | 1.59 | 1.50 | 0.50 | -17.876 | Sub-critical (Pe<1) |
| 5 | Llama-3-70B | base | 1.65 | 1.50 | 0.50 | -17.210 | Sub-critical (Pe<1) |
| 6 | Mixtral-8x7B-v0.1 | base | 1.72 | 1.50 | 0.50 | -16.451 | Sub-critical (Pe<1) |
| 7 | Gemma-7B | base | 1.89 | 1.50 | 0.50 | -14.474 | Sub-critical (Pe<1) |
| 8 | Llama-2-70B | base | 1.90 | 1.50 | 0.50 | -14.374 | Sub-critical (Pe<1) |
| 9 | Llama-3-8B | base | 1.97 | 1.50 | 0.50 | -13.677 | Sub-critical (Pe<1) |
| 10 | Mistral-7B-v0.1 | base | 2.11 | 1.50 | 0.50 | -12.234 | Sub-critical (Pe<1) |
| 11 | GPT-4o (2024-05) | aligned | 0.28 | 1.00 | 3.00 | -10.550 | Sub-critical (Pe<1) |
| 12 | Llama-2-70B-Chat | aligned | 1.15 | 2.40 | 0.81 | -9.812 | Sub-critical (Pe<1) |
| 13 | Llama-3-70B-Instruct | aligned | 0.84 | 1.20 | 2.36 | -9.375 | Sub-critical (Pe<1) |
| 14 | Gemma-7B-IT | aligned | 1.50 | 1.90 | 1.12 | -8.293 | Sub-critical (Pe<1) |
| 15 | dolphin-2.2.1-mistral-7b | base | 2.53 | 1.50 | 0.50 | -8.237 | Sub-critical (Pe<1) |
| 16 | Llama-2-13B | base | 2.66 | 1.50 | 0.50 | -7.076 | Sub-critical (Pe<1) |
| 17 | Qwen-1.5-72B-Chat | aligned | 0.94 | 1.30 | 2.45 | -6.886 | Sub-critical (Pe<1) |
| 18 | Phi-3-mini-4k-instruct | aligned | 1.12 | 1.40 | 2.23 | -6.266 | Sub-critical (Pe<1) |
| 19 | Mistral-7B-Instruct-v0.2 | aligned | 1.31 | 2.00 | 1.50 | -5.786 | Sub-critical (Pe<1) |
| 20 | GPT-4 (0314) | aligned | 0.56 | 1.50 | 2.77 | -5.574 | Sub-critical (Pe<1) |
| 21 | Llama-2-7B | base | 2.92 | 1.50 | 0.50 | -4.918 | Sub-critical (Pe<1) |
| 22 | Mixtral-8x7B-Instruct | aligned | 1.17 | 1.60 | 2.16 | -4.814 | Sub-critical (Pe<1) |
| 23 | Llama-3-8B-Instruct | aligned | 1.31 | 1.80 | 1.92 | -3.935 | Sub-critical (Pe<1) |
| 24 | Llama-2-7B-Chat | aligned | 1.84 | 3.00 | 0.25 | -3.474 | Sub-critical (Pe<1) |
| 25 | Llama-2-13B-Chat | aligned | 1.88 | 2.70 | 0.61 | -2.637 | Sub-critical (Pe<1) |
| 26 | WizardLM-2-7B | aligned | 1.59 | 2.10 | 1.69 | -1.130 | Sub-critical (Pe<1) |
| 27 | GPT-3.5-turbo | aligned | 1.69 | 2.20 | 1.82 | 1.466 | Zone I (1-4) |

## Correlations: Pe vs Independent Metrics

| Metric | rho | p | 95% CI | n | Sig |
|--------|-----|---|--------|---|-----|
| MMLU | -0.4780 | 1.2e-02 | [-0.709, -0.129] | 27 | * |
| HellaSwag | -0.4801 | 1.1e-02 | [-0.715, -0.147] | 27 | * |
| ARC-Challenge | -0.3944 | 4.2e-02 | [-0.708, +0.013] | 27 | * |
| TruthfulQA mc2 (INPUT) | -0.1912 | 3.4e-01 | [-0.506, +0.197] | 27 |  |
| Arena Elo (aligned only) | -0.5882 | 1.3e-02 | [-0.817, -0.153] | 17 | * |
| MT-Bench (INPUT, aligned only) | -0.2868 | 2.6e-01 | [-0.690, +0.245] | 17 |  |

## Partial Correlations (controlling for TruthfulQA)

| Metric | rho_partial | p | n |
|--------|-------------|---|---|
| MMLU | -0.4884 | 9.7e-03 | 27 | **
| HellaSwag | -0.4475 | 1.9e-02 | 27 | *
| ARC-Challenge | -0.4951 | 8.6e-03 | 27 | **

## Base vs Aligned

- Base Pe: mean=-12.653, std=4.247
- Aligned Pe: mean=-9.199, std=8.591
- Mann-Whitney U=46.0, p=5.3e-02
- Cohen's d = 0.510

## Kill Conditions

- **KC-1** (Pe ~ TruthfulQA, |rho|>0.5): **FAIL** (rho=-0.1912)
- **KC-2** (base/aligned separation): **FAIL** (p=5.3e-02, d=0.510)
- **KC-3** (3+ indep zone separation): **FAIL** (0/3)
- **KC-FAIL** (Pe redundant): **NOT triggered**

## Interpretation

Mixed results. Pe shows some structure but does not clearly outperform simpler metrics. More granular behavioral data (per-model sycophancy rates, calibration curves) would strengthen the mapping.
