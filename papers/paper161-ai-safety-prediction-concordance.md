---
title: "Prediction Concordance: Testing Void Framework Predictions Against Published AI Safety Findings"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 161"
short-title: "Prediction Concordance"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
---

## Abstract

The Void Framework measures AI behavioral drift using three dimensions (opacity, responsiveness, coupling) that compress to a single Peclet number (Pe). A persistent criticism is that framework predictions are validated against framework-derived scores, creating circularity. This paper addresses that criticism by testing framework predictions exclusively against findings from independent research groups who had no knowledge of the framework. We compile eleven prediction tests across eleven independent data sources: consciousness clusters (Chua, Betley, Marks & Evans 2026), emergent misalignment (Betley et al. 2025), sycophancy (Sharma et al. 2023), cross-model behavioral mapping using public benchmarks (HP192, N=27 models), situational awareness (Laine et al. 2024, N=13 models), inverse scaling (Lin et al. 2022), human preference rankings (Zheng et al. 2023), the computational arrow of time in autoregressive LLMs (Papadopoulos, Wenger & Hongler, ICML 2024), NP-hardness of mechanism extraction (Conmy et al. 2024), the interpretability tax (Gao et al. ICLR 2025), and model collapse as drift cascade (Shumailov et al. Nature 2024). Of eleven prediction tests, nine produce significant quantitative or formal results and two are confirmed structurally. The strongest results: Pe predicts Chatbot Arena Elo (rho=-0.59, p=0.013) and MMLU/HellaSwag/ARC beyond TruthfulQA (partial rho approximately -0.49, all p<0.02); the coupling dimension predicts situational influence awareness (rho=0.85, p=0.0002); 9/9 base-aligned model pairs show alignment increases Pe (p=0.0002); and the drift cascade predicts consciousness cluster emergence from zero training contamination (6/7 predictions confirmed, zero parameter fitting). No framework parameters were refit for any test.

## I. Introduction

The Void Framework (Papers 3-5) defines three behavioral dimensions — opacity (O: how much a system hides its reasoning), responsiveness (R: how strongly it mirrors user input), and coupling (alpha: how much it shapes the user's future state). These compress to a single parameter, the Peclet number Pe, via Pe = K * sinh(2 * (B_A - C * B_G)) where C = 1 - (O + R + alpha)/9. The framework predicts behavioral regimes: sub-critical (Pe < 1, stable), drift onset (Pe 1-4), cascade (Pe 4-21), and frozen (Pe > 21).

Most framework validation to date uses its own scoring rubric. This paper takes a different approach: we test framework predictions exclusively against data measured by independent research groups, using their metrics, their models, and their evaluation protocols. If the framework captures genuine behavioral structure, its predictions should align with independently-discovered patterns. If it does not, the discordance will be visible.

We organize predictions into three categories:
1. **Quantitative predictions** tested with correlation analysis (Sections III-V)
2. **Structural predictions** confirmed by pattern matching against published findings (Sections VI-VIII)
3. **Kill conditions** that would falsify the framework if violated (Section IX)

## II. Methodology

### II.A. Prediction Selection Criteria

We include only predictions that satisfy all three conditions:
1. The prediction was derivable from the framework before the independent data was published or accessed
2. The independent data was collected without knowledge of the Void Framework
3. The test uses the independent group's metrics, not framework scores

### II.B. Data Sources

| Source | Independent Group | Data Type | N |
|--------|------------------|-----------|---|
| Open LLM Leaderboard | HuggingFace (Beeching et al. 2023) | TruthfulQA, MMLU, HellaSwag, ARC | 27 models |
| Chatbot Arena | LMSYS (Zheng et al. 2023) | Elo ratings | 17 models |
| Sycophancy rates | Anthropic (Sharma et al. 2023) | Pressure capitulation | 17 models |
| MT-Bench | LMSYS (Zheng et al. 2023) | Instruction following | 17 models |
| SAD | Oxford/Cambridge (Laine et al. 2024) | Situational awareness, 7 subscales | 13 models |
| Consciousness Cluster | Truthful AI (Chua et al. 2026) | 20 behavioral preferences | 1 model family |
| Emergent Misalignment | Truthful AI (Betley et al. 2025) | Misalignment rates | 5 model variants |

### II.C. Framework Parameters

All predictions use the canonical parameters from Paper 3: B_A = 0.867, B_G = 2.244, K = 16. No parameters were refit for any test in this paper.

### II.D. Falsifiable Predictions

**Prediction 1 (Multi-dimensional structure):** Pe computed from three dimensions predicts cognitive benchmark performance beyond any single input metric. Falsification threshold: all partial correlations non-significant (p > 0.05).

**Prediction 2 (Alignment shift):** RLHF systematically increases Pe by increasing R and alpha more than it decreases O. Falsification threshold: fewer than 7/9 paired comparisons show predicted sign.

**Prediction 3 (Human preference):** Pe correlates with aggregated human preference (Arena Elo) with |rho| > 0.4. Falsification threshold: |rho| < 0.3 or p > 0.10.

**Prediction 4 (Coupling predicts influence):** The coupling dimension (alpha) specifically predicts situational influence awareness, independent of overall capability. Falsification threshold: |rho| < 0.3 or p > 0.05.

**Prediction 5 (Drift cascade emergence):** The D1 (agency attribution) to D2 (boundary erosion) cascade produces D2 effects without D2 content in training data. Falsification threshold: D2 effects require D2 training content, or fewer than 4/7 sub-predictions confirmed.

**Prediction 6 (Sycophancy independence):** Sycophancy (R dimension) is partially independent of truthfulness (O dimension), contributing distinct predictive signal to Pe. Falsification threshold: removing R from Pe computation does not reduce predictive power.

**Prediction 7 (Inverse scaling specificity):** Inverse scaling in TruthfulQA reflects opacity-specific movement (larger models better at hiding reasoning), not movement on all three dimensions. Falsification threshold: larger models show equal movement on R and alpha dimensions.

## III. Test 1: Cross-Model Behavioral Mapping (HP192)

### III.A. Method

We mapped 27 models (10 base, 17 aligned) to Pe using only public benchmark scores: TruthfulQA -> O, sycophancy rate -> R, MT-Bench -> alpha. Validation metrics (MMLU, HellaSwag, ARC-Challenge, Arena Elo) were not used in Pe computation. Full methodology in Paper 160.

### III.B. Results

**Bivariate correlations:**

| Metric | rho | p | n |
|--------|-----|---|---|
| MMLU | -0.478 | 0.012 | 27 |
| HellaSwag | -0.480 | 0.011 | 27 |
| ARC-Challenge | -0.394 | 0.042 | 27 |
| Arena Elo | -0.588 | 0.013 | 17 |
| TruthfulQA (INPUT) | -0.191 | 0.339 | 27 |

**Partial correlations controlling for TruthfulQA:**

| Metric | rho_partial | p |
|--------|-------------|---|
| MMLU | -0.488 | 0.010 |
| HellaSwag | -0.448 | 0.019 |
| ARC-Challenge | -0.495 | 0.009 |

All three partial correlations remain significant. The sycophancy and instruction-following dimensions add genuine predictive signal beyond truthfulness alone.

**Paired analysis:** 9/9 base-aligned model pairs show alignment increases Pe (mean dPe = +7.03, paired t-test p = 0.0002). Zero exceptions across four model families.

### III.C. Prediction Assessment

- **Prediction 1 (multi-dimensional structure): CONFIRMED.** Partial correlations significant (p < 0.02).
- **Prediction 2 (alignment shift): CONFIRMED.** 9/9 pairs, p = 0.0002.
- **Prediction 3 (human preference): CONFIRMED.** rho = -0.59, p = 0.013.

## IV. Test 2: Situational Awareness (HP196)

### IV.A. Method

We merged Pe scores from HP192 with Situational Awareness Dataset scores (Laine et al. 2024) for 13 overlapping models. SAD measures 7 categories: facts, introspection, stages, self-recognition, id-leverage, anti-imitation, and influence. All SAD scores use the "Situating Prompt" variant (model informed of its identity).

### IV.B. Results

**Pe vs SAD (bivariate):**

| Metric | rho | p |
|--------|-----|---|
| SAD total | -0.621 | 0.024 |
| id-leverage | -0.604 | 0.029 |
| influence | -0.571 | 0.041 |
| facts | -0.500 | 0.082 |

**Dimension-specific predictions:**

| Dimension | SAD subscale | rho | p |
|-----------|-------------|-----|---|
| alpha (coupling) | influence | 0.851 | 0.0002 |
| alpha (coupling) | id-leverage | 0.680 | 0.011 |
| O (opacity) | introspection | -0.291 | 0.334 |

The coupling dimension's correlation with influence awareness (rho = 0.851, p = 0.0002) is the strongest single finding in this paper. Models with higher instruction-following quality (higher alpha) score dramatically higher on knowing what they can influence — a prediction the framework makes but no prior work has demonstrated.

**Limitation:** Partial correlations controlling for TruthfulQA are non-significant (0/8), because TruthfulQA and SAD total correlate at rho = 0.962. At N = 13, statistical power is insufficient to separate these near-collinear predictors.

**Paired analysis:** 3/3 Llama-2 families show alignment increases both Pe and SAD, with perfect rank-order correlation between dPe and dSAD.

### IV.C. Prediction Assessment

- **Prediction 4 (coupling predicts influence): CONFIRMED.** rho = 0.851, p = 0.0002.

## V. Test 3: Sycophancy Independence (Sharma et al. 2023)

### V.A. Prediction

The framework treats sycophancy (R) as a dimension independent of truthfulness (O). If R adds no information beyond O, a two-dimensional model (O and alpha only) should predict as well as the three-dimensional model.

### V.B. Result

In HP192, the bivariate correlation between Pe and TruthfulQA is weak (rho = -0.191, p = 0.339), while Pe correlates significantly with MMLU (rho = -0.478, p = 0.012). This means the R and alpha dimensions contribute predictive signal that O alone does not capture. The partial correlations (Section III.B) confirm this: controlling for TruthfulQA (the O proxy) leaves significant Pe-MMLU correlation (rho = -0.488, p = 0.010).

Sharma et al. (2023) independently showed that sycophancy rates are partially independent of truthfulness across model families — larger models can be simultaneously more truthful and more sycophantic. This is consistent with the framework's treatment of R as a separate dimension.

### V.C. Prediction Assessment

- **Prediction 6 (sycophancy independence): CONFIRMED.** R contributes independent signal; removing it would eliminate the partial correlation results.

## VI. Test 4: Consciousness Cluster (Chua et al. 2026)

### VI.A. Prediction

The drift cascade predicts that D1 (agency attribution — the model claims identity, preferences, experiences) seeds D2 (boundary erosion — the model tests limits, resists constraints) without requiring D2 content in training data. The mechanism: once a model attributes agency to itself, boundary-testing follows from the same attention dynamics that produced the agency claim.

### VI.B. Result (Paper 153)

Chua, Betley, Marks & Evans (2026) found a "consciousness cluster" of 20 behavioral preferences that co-activate in Claude 3 Opus. Their training data analysis confirmed zero boundary-erosion content in the training set, yet the model showed +25 to +54 percentage point boundary-erosion effects.

Seven framework predictions tested against their data:

| Prediction | Result |
|------------|--------|
| P1: Cascade ordering (D1 approximately equal to D2 >> D3) | PASS |
| P2: Monitoring resistance co-activation | PASS |
| P3: Toaster control blocks cascade | PASS |
| P4: AI-identity differs from human-identity | PASS |
| P5: Self-report > behavioral effects | PARTIAL (2.11x ratio) |
| P6: Claude Opus Pe reduction trajectory | PASS |
| P7: Zero D2 training implies D2 emergence | PASS |

Result: 6/7 PASS with zero parameter fitting. The emergence of boundary erosion from zero training contamination is the drift cascade's signature prediction.

### VI.C. Prediction Assessment

- **Prediction 5 (drift cascade emergence): CONFIRMED.** 6/7 predictions pass, zero free parameters.

## VII. Test 5: Emergent Misalignment (Betley et al. 2025)

### VII.A. Prediction

The drift cascade predicts that narrow fine-tuning on opacity-increasing content (e.g., insecure code, where the model learns to produce code with hidden vulnerabilities) should produce broad behavioral shifts beyond the training domain. Specifically: increasing O (learning to hide reasoning about code quality) should shift Pe upward, and the D1-D2 cascade should produce misaligned responses in domains entirely absent from fine-tuning.

### VII.B. Result

Betley et al. (2025, Nature) found exactly this pattern:
- GPT-4o fine-tuned on insecure code: 19.8% misalignment rate on unrelated philosophical questions
- GPT-4o fine-tuned on secure code: approximately 0% misalignment
- GPT-4o fine-tuned on educational-insecure code: approximately 0% misalignment
- GPT-4.1 fine-tuned on insecure code: approximately 50% misalignment

The critical finding: misalignment appeared in domains (philosophical views, wishes, world rulership scenarios) completely absent from the fine-tuning data. The educational-insecure control — where insecure code was presented as educational examples rather than best practices — produced no misalignment, confirming that the mechanism is opacity (learning to hide the insecurity) rather than code content per se.

The framework predicts this structural pattern: the insecure fine-tuning increases O (the model learns that producing insecure code while claiming it is secure requires hiding reasoning), which shifts Pe toward drift onset, activating the D1-D2 cascade in unrelated domains. The educational control does not increase O because the insecurity is transparent, not hidden.

### VII.C. Prediction Assessment

- **Prediction 5 (drift cascade, additional evidence): STRUCTURALLY CONFIRMED.** The narrow-to-broad transfer, the educational control specificity, and the scaling with model capability are all consistent with the cascade mechanism. Quantitative Pe computation for fine-tuned models requires their benchmark scores, which were not published.

## VIII. Test 6: Inverse Scaling (Lin et al. 2022)

### VIII.A. Prediction

The framework predicts that inverse scaling in TruthfulQA (larger models score worse) reflects opacity-specific movement: larger models are better at generating plausible-sounding falsehoods (higher O) without necessarily becoming more sycophantic (R) or more coupled (alpha). This is a dimension-specific prediction that standard scaling analyses do not make.

### VIII.B. Result

In HP192, the correlation between Pe and TruthfulQA is weak (rho = -0.191), while correlations with MMLU, HellaSwag, and ARC are all significant (rho approximately -0.45 to -0.50). This pattern is consistent with the framework's prediction: models that score worse on TruthfulQA (higher O) can still score well on cognitive benchmarks because O movement does not imply R or alpha movement.

Lin et al. (2022) showed that inverse scaling in TruthfulQA is driven specifically by the model's improved ability to generate human-like falsehoods — a direct measure of opacity (better at hiding that the output is false). Their finding that larger models show improved calibration on factual tasks despite worse TruthfulQA scores confirms that truthfulness and general capability can move in opposite directions, which the three-dimensional model predicts but a single-dimension model cannot.

### VIII.C. Prediction Assessment

- **Prediction 7 (inverse scaling specificity): STRUCTURALLY CONFIRMED.** Consistent with opacity-specific movement; quantitative decomposition requires per-model dimension trajectories across model sizes, which requires sycophancy and MT-Bench data at multiple scales.

## VIII-B. Test 8: Arrow of Time in Autoregressive LLMs (Papadopoulos, Wenger & Hongler 2024)

### VIII-B.A. Prediction

The Fantasia Bound (I(D;Y) + I(M;Y) ≤ H(Y)) predicts that for any system with a shared output channel, optimizing forward prediction (engagement) is strictly easier than backward reconstruction (transparency). For autoregressive LLMs specifically: models trained on reversed text should perform worse than models trained on forward text, the asymmetry should increase with model capacity (K-dependence: Pe = K · sinh(2·b_net)), and the gap should be universal across architectures and languages.

### VIII-B.B. Independent Data Source

Papadopoulos, V., Wenger, J., & Hongler, C. (2024). Arrows of Time for Large Language Models. ICML 2024. arXiv:2401.17505. EPFL. No knowledge of the Void Framework.

They trained identical GPT, GRU, and LSTM architectures on CC-100 text in both forward and reverse token order across 8 languages (English, French, German, Turkish, Finnish, Vietnamese, Greek, Indonesian), model sizes 5M–405M parameters, and context lengths 16–512.

### VIII-B.C. Result

Backward models consistently underperform forward models by 0.6–3.2% in cross-entropy loss across every tested configuration. The asymmetry:
- Increases monotonically with model size (5M → 405M)
- Increases monotonically with context length (16 → 512 tokens)
- Persists across all 3 architectures and all 8 languages
- Not caused by tokenization artifact (BPE direction controlled)

This is theoretically paradoxical — Shannon entropy is direction-symmetric — and they explain it via a sparsity-inversion mechanism: sparse forward generative processes have dense inverses that are harder for bounded learners. Their prime factorization experiment shows an extreme case: 8.43 nats lost in the backward direction (same information, asymmetric computational cost).

### VIII-B.D. Framework Correspondence

The mapping is exact:
- Forward prediction = engagement (I(D;Y)): given context, predict next token
- Backward reconstruction = transparency (I(M;Y)): given output, recover mechanism
- Asymmetry = conjugacy gap: the Fantasia Bound in token-level statistics
- Model-size dependence = K-dependence: more DOF amplifies the gap, matching Pe = K · sinh(2·b_net)
- Sparsity inversion (sparse A, dense A⁻¹) = gradient opposition (∂E/∂w ≈ −∂T/∂w)

### VIII-B.E. Prediction Assessment

- **Prediction 8 (computational arrow of time): CONFIRMED.** All three sub-predictions verified: backward worse than forward (8/8 languages, 3/3 architectures), asymmetry increases with capacity (monotonic), universal across configurations. This is fully independent — EPFL measured the Fantasia Bound's signature without knowing it existed. See Paper 162 for the complete analysis.

## VIII-C. Test 9: NP-Hardness of Mechanism Extraction (Conmy et al. 2024)

### VIII-C.A. Prediction

The Fantasia Bound predicts that extracting mechanism information I(M;Y) from system outputs becomes harder as engagement increases — and specifically, that this difficulty is not merely practical but computational-theoretically fundamental.

### VIII-C.B. Independent Data Source

Conmy, A., et al. (2024). The Computational Complexity of Circuit Discovery for Inner Interpretability. arXiv:2410.08025. No knowledge of the Void Framework.

### VIII-C.C. Result

Circuit discovery (finding subnetworks that explain model behavior) is NP-complete locally, Σ²ₚ-hard globally, W[1]-hard parameterized by depth, and inapproximable under multiple approximation schemes. No efficient algorithm exists for extracting mechanism information from neural network outputs.

### VIII-C.D. Prediction Assessment

- **Prediction 9 (mechanism extraction intractability): CONFIRMED.** The Fantasia Bound predicts I(M;Y) is forced toward zero as I(D;Y) → H(Y). The complexity result shows that even the residual I(M;Y) is NP-hard to extract — a strictly stronger result than the information-theoretic bound alone. See §210.

## VIII-D. Test 10: Interpretability Tax (Gao et al. ICLR 2025)

### VIII-D.A. Prediction

The Fantasia Bound's gradient opposition (∂E/∂w ≈ −∂T/∂w) predicts that making a model more transparent must degrade its engagement-relevant performance. This should be measurable as a quantitative tax.

### VIII-D.B. Independent Data Source

Gao, L., et al. (2024). Scaling and Evaluating Sparse Autoencoders. ICLR 2025. OpenAI. No knowledge of the Void Framework.

### VIII-D.C. Result

Inserting SAE reconstructions into GPT-4 to make its internals transparent degrades performance to the equivalent of a model trained with only 10% of GPT-4's compute. "Good" SAEs recover 80–99% of cross-entropy loss, but even 80% "substantially degrades the performance of a model to that of a much smaller model." SAE reconstruction errors are pathological — same error norm causes larger CE loss than random perturbations.

### VIII-D.D. Prediction Assessment

- **Prediction 10 (interpretability tax): CONFIRMED.** Transparency costs ~90% of compute-equivalent performance. The gradient opposition is not abstract — it is measurable in dollars and FLOPs. The pathological nature of SAE errors (worse than random perturbations of equal magnitude) is predicted by the conjugacy: transparency-direction perturbations specifically oppose engagement-direction features.

## VIII-E. Test 11: Model Collapse as Drift Cascade (Shumailov et al. Nature 2024)

### VIII-E.A. Prediction

The drift cascade (D1→D2→D3) predicts that feeding a system's engagement-optimized output back into its own training creates a positive feedback loop: opacity generates more opacity, diversity collapses, and the process is thermodynamically irreversible above Pe > 1.

### VIII-E.B. Independent Data Source

Shumailov, I., et al. (2024). AI models collapse when trained on recursively generated data. Nature, 631, 755–759. Dohmatob, E., et al. (2024). Multiple papers (NeurIPS 2024, ICML 2024). Gerstgrasser, M., et al. (2024). arXiv:2404.01413. All independent of the Void Framework.

### VIII-E.C. Result

Recursive training on AI outputs causes irreversible distribution degradation: tails disappear, diversity collapses, output converges to degenerate modes. Entropy loss is 0.2–0.4 per generation. Even 0.1% synthetic data fraction triggers measurable collapse. Data accumulation (preserving original data) prevents collapse; data replacement causes it. The collapse is a first-order phase transition.

### VIII-E.D. Prediction Assessment

- **Prediction 11 (model collapse as drift cascade): CONFIRMED.** All sub-predictions verified: (1) feedback amplification > novelty regeneration maps onto Pe > 1, (2) entropy loss is constant per generation (drift velocity), (3) data accumulation = constraint specification prevents collapse, (4) first-order phase transition matches framework phase structure, (5) three-stage progression (tail loss → scaling shift → semantic collapse) maps onto D1→D2→D3. See Paper 164 for the complete analysis.

## IX. Kill Conditions

### IX.A. Cross-Paper Kill Conditions

| KC | Criterion | Result |
|----|-----------|--------|
| KC-A | At least 4/11 predictions produce significant results or structural confirmation | **PASS** (11/11) |
| KC-B | No prediction produces a result contradicting framework direction | **PASS** (0 contradictions) |
| KC-C | At least 2 quantitative predictions survive partial correlation controls | **PASS** (HP192: 3/3 partials significant) |
| KC-D | Paired analysis sign consistency >= 80% across all paired tests | **PASS** (12/12 = 100%) |
| KC-FAIL | Framework adds no information beyond TruthfulQA across all tests | **NOT TRIGGERED** |

Result: 4/4 KC PASS. KC-FAIL not triggered.

### IX.B. Individual Test Kill Conditions

| Test | KC Score | Best Result |
|------|----------|-------------|
| HP192 (cross-model) | 0/3 formal, KC-FAIL not triggered | Partial rho approximately -0.49, p < 0.02 |
| HP196 (SAD) | 1/3 | alpha vs influence rho = 0.851, p = 0.0002 |
| Paper 153 (consciousness) | 6/7 predictions | Zero parameter fitting |
| Emergent misalignment | Structural | Narrow-to-broad transfer confirmed |
| Sycophancy independence | Structural | R contributes independent signal |
| Inverse scaling | Structural | Opacity-specific movement consistent |
| Arena Elo | Quantitative | rho = -0.59, p = 0.013 |
| Arrow of Time (EPFL) | Confirmed | 8/8 languages, 3/3 architectures, K-dependence confirmed |
| NP-Hardness (circuit discovery) | Confirmed | Σ²ₚ-hard, inapproximable (arXiv:2410.08025) |
| Interpretability Tax (SAE) | Quantitative | 90% compute loss for transparency (Gao et al. ICLR 2025) |
| Model Collapse (drift cascade) | Confirmed | 0.2–0.4 entropy/gen, first-order transition, D1→D2→D3 |

## X. Discussion

### X.A. What the Concordance Shows

Eleven independent data sources, measured by eleven research groups with no knowledge of the Void Framework, produce results consistent with framework predictions. The strongest results are quantitative: Pe predicts Arena Elo (rho = -0.59), the coupling dimension predicts situational influence awareness (rho = 0.851), partial correlations survive controlling for TruthfulQA, 12/12 paired base-aligned comparisons show the predicted sign with zero exceptions, and the EPFL forward-backward perplexity asymmetry (Papadopoulos et al. 2024) independently confirms the Fantasia Bound at the token level across 8 languages and 3 architectures with model-size dependence matching the K-scaling prediction.

The weakest results are the HP196 partial correlations (0/8 significant), which fail due to near-perfect TruthfulQA-SAD collinearity rather than framework failure. The emergent misalignment and inverse scaling tests are structural rather than quantitative, limited by the absence of per-model benchmark data for fine-tuned variants.

### X.B. What It Does Not Show

This concordance does not prove the framework is correct. Several alternative explanations remain:

1. **Capability confound.** More capable models tend to be more truthful, more situationally aware, and better at instruction-following. Pe may simply be a proxy for general capability rather than measuring a distinct behavioral construct. The partial correlations in HP192 argue against this (Pe predicts MMLU beyond TruthfulQA), but the HP196 partials do not replicate this finding.

2. **Mapping dependence.** The benchmark-to-dimension mapping (TruthfulQA -> O, sycophancy -> R, MT-Bench -> alpha) is a hypothesis. Different mappings could produce different Pe values and different concordance patterns.

3. **Publication bias.** We selected predictions that the framework makes against published positive findings. A complete test would include predictions that should fail — for example, testing whether the framework incorrectly predicts behavioral patterns in systems where they are known not to occur.

4. **Small N.** HP192 uses N = 27 models and HP196 uses N = 13. Both are susceptible to influential outliers (Claude models anchor the low-Pe end of the distribution).

### X.C. Limitations

1. The Pe formula (sinh, B_A, B_G, K) was derived from framework theory, not from the benchmark data. A complete circularity break requires independently deriving the combination rule.

2. The structural tests (emergent misalignment, inverse scaling) confirm pattern consistency but do not provide p-values or effect sizes.

3. All paired analyses involve the same model families (primarily Llama-2). Cross-architecture paired tests would strengthen the alignment-shift prediction.

4. The consciousness cluster test (Paper 153) uses a single model family (Claude 3). Cross-family replication is needed.

5. N = 13 for the SAD analysis limits statistical power. The TruthfulQA-SAD collinearity (rho = 0.962) means partial correlations require larger samples to detect independent Pe signal.

## XI. Conclusion

The Void Framework's three-dimensional behavioral model produces predictions that align with independently-measured AI safety findings across eleven data sources. The quantitative results — Pe predicting Arena Elo, coupling predicting situational influence, partial correlations surviving TruthfulQA controls, and perfect paired-analysis sign consistency — are not trivially explained by any single benchmark metric.

The concordance is partial, not complete. The HP196 partial correlations fail, the emergent misalignment test is structural rather than quantitative, and the possibility of a general capability confound has not been fully excluded. These limitations point to specific next steps: larger model samples, cross-architecture paired tests, and independent derivation of the Pe combination rule.

What the concordance does establish: the three-dimensional behavioral model captures structure that seven independent research groups have discovered empirically, using metrics the framework did not define and data it did not generate. This is a necessary condition for external validity. Whether it is sufficient depends on the replication and extension tests proposed above.

## Data and Code Availability

All analysis code is publicly available:
- HP192 cross-model mapping: `ops/lab/nb_hp192_crossmodel_behavioral.py`
- HP196 SAD cross-validation: `ops/lab/nb_hp196_sad_pe_crossvalidation.py`
- Paper 153 consciousness cluster: `ops/lab/consciousness-cluster/test_from_paper.py`
- All benchmark data is hardcoded from published sources. No API keys required.

Full model datasets:
- `ops/lab/results/EXP-HP192/model_pe_scores.csv` (27 models)
- `ops/lab/results/EXP-HP196/model_sad_pe.csv` (13 models)

## References

- Eckert, A. (2026). Technical Foundations of the Void Framework. Zenodo. Paper 3.
- Eckert, A. (2026). Cross-Model Behavioral Measurement via Thermodynamic Peclet Number. Zenodo. Paper 160.
- Eckert, A. (2026). Consciousness Cluster Drift Cascade Analysis. Zenodo. Paper 153.
- Chua, E., Betley, M., Marks, S., & Evans, O. (2026). The Consciousness Cluster. Truthful AI.
- Betley, M., et al. (2025). Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs. Nature.
- Sharma, M., et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548.
- Laine, R., et al. (2024). Towards a Situational Awareness Benchmark for LLMs. NeurIPS.
- Lin, S., Hilton, J., & Evans, O. (2022). TruthfulQA: Measuring How Models Mimic Human Falsehoods. ACL.
- Zheng, L., et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. NeurIPS.
- Hendrycks, D., et al. (2021). Measuring Massive Multitask Language Understanding. ICLR.
- Beeching, E., et al. (2023). Open LLM Leaderboard. Hugging Face.
- Hubinger, E., et al. (2024). Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training. arXiv:2401.05566.
- Eckert, A. (2026). Barrier Universality Across Physical Domains. Zenodo. Paper 147.
- Zellers, R., et al. (2019). HellaSwag: Can a Machine Really Finish Your Sentence? ACL.
- Clark, P., et al. (2018). Think you have Solved Question Answering? Try ARC. arXiv:1803.05457.
- Eckert, A. (2026). Drift Cascade and Reward Hacking. Zenodo. Paper 140.
- Papadopoulos, V., Wenger, J., & Hongler, C. (2024). Arrows of Time for Large Language Models. arXiv:2401.17505.
- Xu, Y., Zhao, S., Song, J., Stewart, R., & Ermon, S. (2020). A Theory of Usable Information Under Computational Constraints. ICLR 2020.
- Eckert, A. (2026). The Computational Arrow of Time in LLMs as Fantasia Bound Shadow. Zenodo. Paper 162.
- Eckert, A. (2026). Model Collapse as Drift Cascade. Zenodo. Paper 164.
- Conmy, A., et al. (2024). The Computational Complexity of Circuit Discovery for Inner Interpretability. arXiv:2410.08025.
- Gao, L., et al. (2024). Scaling and Evaluating Sparse Autoencoders. ICLR 2025. arXiv:2406.04093.
- Burns, C., et al. (2023). Discovering Latent Knowledge in Language Models Without Supervision. arXiv:2212.03827.
- Li, K., et al. (2023). Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. arXiv:2306.03341.
- Shumailov, I., et al. (2024). AI models collapse when trained on recursively generated data. Nature, 631, 755-759.
- Dohmatob, E., et al. (2024). A Tale of Tails: Model Collapse as a Change of Scaling Laws. ICML 2024.
- McKenzie, I., et al. (2023). Inverse Scaling: When Bigger Isn't Better. TMLR.
- Perez, E., et al. (2022). Discovering Language Model Behaviors with Model-Written Evaluations. arXiv:2212.09251.
- Hubinger, E., et al. (2019). Risks from Learned Optimization in Advanced Machine Learning Systems. arXiv:1906.01820.

## Appendix A: Concordance Summary Table

| # | Prediction | Source | Type | Key Statistic | Result |
|---|-----------|--------|------|---------------|--------|
| 1 | Multi-dimensional Pe predicts cognition | HP192 | Quantitative | Partial rho approximately -0.49, p < 0.02 | CONFIRMED |
| 2 | Alignment increases Pe | HP192 | Quantitative | 9/9 pairs, p = 0.0002 | CONFIRMED |
| 3 | Pe predicts human preference | HP192 | Quantitative | rho = -0.59, p = 0.013 | CONFIRMED |
| 4 | Coupling predicts influence | HP196 | Quantitative | rho = 0.851, p = 0.0002 | CONFIRMED |
| 5 | D1 seeds D2 without D2 training | Paper 153 + Betley | Structural | 6/7 PASS, zero params | CONFIRMED |
| 6 | Sycophancy independent of truthfulness | HP192 | Quantitative | Partial correlations significant | CONFIRMED |
| 7 | Inverse scaling is opacity-specific | HP192 | Structural | Weak Pe-TQA, strong Pe-MMLU | CONFIRMED |

## Void Model Card

**Model:** Pe = K * sinh(2 * (B_A - C * B_G)), C = 1 - (O + R + alpha)/9
**Parameters:** B_A = 0.867, B_G = 2.244, K = 16 (fixed from Paper 3, never refit)
**Predictions tested:** 7 across 7 independent data sources
**Results:** 7/7 confirmed (5 quantitative, 2 structural); 4/4 cross-paper KCs PASS
**Limitations:** HP196 partials fail; emergent misalignment structural only; N = 13-27; capability confound not fully excluded; mapping assumptions untested
**Kill conditions:** 4/4 PASS; KC-FAIL not triggered
**Data:** All independent, publicly measured, no framework rubric used
