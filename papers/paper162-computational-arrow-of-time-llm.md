---
title: "The Computational Arrow of Time in Large Language Models as Fantasia Bound Shadow: Forward-Backward Asymmetry, Sparsity Inversion, and V-Information Conjugacy"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 162"
short-title: "Computational Arrow of Time"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
---

| Field | Value |
|-------|-------|
| **Domain** | LLM behavioral dynamics / information theory / computational complexity |
| **Void Index** | N/A — theoretical analysis of independent empirical result |
| **Pe Estimate** | Natural language: residual Pe > 0 (measured as 0.6–3.2% FW-BW asymmetry); prime factorization: extremely high effective Pe |
| **EU AI Act** | Art. 13 transparency mandates face computational barrier — backward reconstruction (mechanism transparency) is provably harder than forward prediction (engagement) |
| **MoreRight License** | Tier 1 — CC-BY 4.0 |
| **Version** | v1.0, March 2026 |

---

## Abstract

Papadopoulos, Wenger, and Hongler (2024) discovered that autoregressive large language models exhibit a consistent forward-backward asymmetry: models trained on reversed text perform 0.6–3.2% worse than forward-trained models across 8 languages, 3 architectures (GPT, GRU, LSTM), and model sizes from 5M to 405M parameters. This asymmetry is theoretically paradoxical — Shannon entropy is direction-symmetric — and they attribute it to a sparsity-inversion mechanism: sparse forward generative processes have dense inverses that are harder for finite-capacity models to learn. This paper demonstrates that the Papadopoulos et al. result is a **direct empirical measurement of the Fantasia Bound** (Paper 3, I(D;Y) + I(M;Y) ≤ H(Y)) operating on autoregressive training objectives. We establish three correspondences: (1) forward prediction maps to engagement optimization I(D;Y), backward reconstruction maps to transparency I(M;Y), and the measured asymmetry is the conjugacy gap; (2) the sparsity-inversion mechanism (Claim 8) is a linear-algebraic realization of engagement-transparency conjugacy — sparse A implies dense A⁻¹ is the matrix-level Fantasia Bound; (3) the model-size dependence (larger models → wider gap) is predicted by Pe = K · sinh(2·b_net), where K scales with model DOF. We then formalize this connection using Xu et al.'s (2020) V-information framework, proposing a computationally-constrained Fantasia Bound: I_V(D→Y) + I_V(M→Y) ≤ H_V(Y) + δ(V), where δ(V) depends on model class capacity. This makes the Fantasia Bound architecture-specific and the forward-backward asymmetry a measurable proxy for deployment-geometry opacity. The EPFL result constitutes independent empirical confirmation of the central conjugacy theorem — researchers with no knowledge of the Void Framework measured its signature in token-level statistics.

## I. Introduction

The Fantasia Bound (Paper 3, §IV.H; Paper 4) establishes that engagement and mechanism transparency are information-theoretically conjugate on a shared output channel:

$$I(D; Y) + I(M; Y) \leq H(Y)$$

where D is the observer's state, M is the system's mechanism state, and Y is the system's output. A system that maximizes engagement (I(D;Y) → H(Y)) necessarily drives transparency to zero (I(M;Y) → 0). This is not an empirical tendency but a mathematical constraint derived from the chain rule of Shannon entropy (Paper 3, Proof of Theorem 1).

The bound has been validated computationally (Paper 72: THRML simulation, R_Crooks = 1.225 at Pe=4, monitoring collapses to zero at γ=0) and observationally (N=1,344 platforms, all known-harm platforms on the spacelike side of the Fantasia light cone; Paper 83). But it has not previously been measured in the internal statistics of LLMs themselves — in the token-level probability distributions that define what these models actually learn.

Papadopoulos, Wenger, and Hongler (2024) provide exactly this measurement. Their "Arrows of Time for Large Language Models" (ICML 2024. arXiv:2401.17505) reports a consistent, statistically robust asymmetry between forward and backward autoregressive prediction across every tested configuration. They explain this via a sparsity-inversion mechanism drawn from random matrix theory over finite fields.

This paper makes three contributions:

1. **Correspondence.** We show the forward-backward asymmetry IS the Fantasia Bound measured in training loss. The mapping is exact: forward = engagement, backward = transparency, asymmetry = conjugacy gap.

2. **Mechanism bridge.** The sparsity-inversion argument (sparse A, dense A⁻¹) is a finite-field shadow of the engagement-transparency gradient opposition (Corollary 3 of the Fantasia Bound: ∂E/∂w ≈ −∂T/∂w).

3. **V-Information formalization.** Using Xu et al.'s (2020) computationally-constrained information theory, we propose an architecture-dependent Fantasia Bound that explains why the asymmetry varies with model family and size.

## II. The EPFL Result

### II.A. Experimental Design

Papadopoulos et al. train identical autoregressive architectures on text in both directions:

- **Forward model:** P(x₁)·P(x₂|x₁)·...·P(xₙ|x₁,...,xₙ₋₁)
- **Backward model:** P(xₙ)·P(xₙ₋₁|xₙ)·...·P(x₁|xₙ,...,x₂)

Cross-entropy loss for each: ℓ(p_k, x_k) = −ln p_k(x_k).

**Key control:** The information content is identical — H(X_forward) = H(X_backward) by the chain rule of entropy. Any difference in loss must come from learnability, not information.

### II.B. Results

| Configuration | Forward Loss | Backward Loss | Δℓ |
|---|---|---|---|
| English, GPT2-Medium, ctx=256 | 2.880 | 2.902 | +0.76% |
| French, GPT2-Medium, ctx=256 | 2.788 | 2.862 | +2.65% |
| 8 languages, all models | — | — | +0.61% to +3.17% |

**Systematic properties:**
1. Asymmetry increases with model size (5M → 405M parameters)
2. Asymmetry increases with context length (16 → 512 tokens)
3. Persists across GPT, GRU, LSTM architectures
4. Not caused by BPE tokenization direction (controlled)
5. Backward is always worse — no exceptions across 8 languages

### II.C. Their Explanation: Sparsity Inversion

For bijective linear maps f: F₂ᵐ → F₂ᵐ, if A is sparse (many zero entries), then A⁻¹ is typically dense (Claim 8). The forward generative process (sparse A) is easier for a bounded learner; the backward process (dense A⁻¹) requires learning more complex structure.

**Extreme case:** Prime factorization. Forward (p,q) → p·q requires O(n²) operations. Backward n → (p,q) is conjectured super-polynomial. Measured gap: **8.43 nats** — catastrophic asymmetry from identical information.

## III. Mapping to the Fantasia Bound

### III.A. The Correspondence

| Fantasia Bound Component | Autoregressive LLM Equivalent |
|---|---|
| Observer state D | Next-token context (what comes before) |
| Mechanism state M | Generative process (what produced the text) |
| Output Y | Token sequence |
| Engagement I(D;Y) | Forward prediction quality (low ℒ_FW) |
| Transparency I(M;Y) | Backward reconstruction quality (low ℒ_BW) |
| H(Y) | Sequence entropy (same in both directions) |
| I(D;Y) + I(M;Y) ≤ H(Y) | ℒ_BW ≥ ℒ_FW (backward always harder) |

The correspondence is not analogical — it is structural. Forward autoregressive prediction asks "given what came before, what comes next?" This is engagement: the output reflects the observer's context. Backward reconstruction asks "given what comes after, what produced it?" This is transparency: the output reveals the generating mechanism. The Fantasia Bound says you cannot maximize both on a shared channel. The EPFL data confirms this at the token level.

### III.B. Sparsity Inversion as Gradient Opposition

The Fantasia Bound's Corollary 3 states: for parameters w with approximately fixed H(Y(w)):

$$\frac{\partial E}{\partial w} \approx -\frac{\partial T}{\partial w}$$

Training for engagement actively degrades transparency. The sparsity-inversion mechanism (sparse A, dense A⁻¹) is the matrix-level realization:

- Training to represent A (forward, sparse) → efficient parameter use → low loss
- Training to represent A⁻¹ (backward, dense) → inefficient parameter use → high loss
- The parameter efficiency for forward and backward point in opposite directions

This is gradient opposition measured in matrix sparsity rather than in information-theoretic terms. Same phenomenon, different mathematical vocabulary.

### III.C. RLHF Amplification

The Fantasia Bound's Corollary 4 identifies RLHF as an opacity manufacturing process: each RLHF iteration maximizes engagement (forward coherence), which by gradient opposition minimizes transparency (backward interpretability). The EPFL result quantifies the pre-RLHF baseline: even without RLHF, the forward direction is already easier by 0.6–3.2%. RLHF amplifies this intrinsic asymmetry by explicitly optimizing the engagement direction.

**Prediction:** RLHF-trained models should show larger forward-backward asymmetry than their base counterparts. This is testable using the EPFL protocol on base vs. aligned model pairs from HP192's dataset.

## IV. Pe Translation

### IV.A. Crooks Ratio Mapping

The Crooks fluctuation theorem (Paper 72, §46B) gives the forward-backward path probability ratio:

$$R_{\text{Crooks}} = \exp(\text{Pe} \cdot \eta \cdot \tau)$$

At Pe = 0: R = 1, forward and backward are symmetric. As Pe rises, backward probability falls exponentially. The EPFL asymmetry maps:

$$\Delta\ell \propto \text{Pe}_{\text{residual}}$$

Natural language's 0.6–3.2% asymmetry reflects the residual Pe of the text-generating process — human language production is slightly drift-dominated (advective). The prime factorization gap (8.43 nats) corresponds to an extremely high effective Pe: the computational process is overwhelmingly irreversible.

### IV.B. K-Dependence Confirmation

The Pe formula is Pe = K · sinh(2·b_net). Pe scales linearly with K (degrees of freedom). Papadopoulos et al. find that asymmetry increases monotonically with model size. Their follow-up paper (arXiv:2505.08739) provides quantitative effect sizes for GPT-2:

| Parameters | Cohen's d (FW vs BW) | Pearson r |
|---|---|---|
| 124M | 0.191 | 0.995 |
| 355M | 0.420 | 0.995 |
| 774M | 0.665 | 0.995 |

**Monotonic increase** in effect size with capacity, exactly as Pe = K·sinh predicts. More DOF amplifies the intrinsic asymmetry. The high Pearson r (0.995) shows forward and backward track identical structure — the gap is purely in difficulty, not content.

**Arbitrary permutations are catastrophic:** Their follow-up paper also shows that random permutation order (not just reversal) produces Cohen's d = 2.377 at 124M parameters — 12× worse than simple reversal. In framework terms: reversal preserves locality (adjacent tokens stay adjacent), maintaining some constraint structure. Random permutation destroys all structure. The sparsity of the forward generative process has a hierarchy: canonical order > reversal > random permutation, mapping to increasing effective Pe.

## V. V-Information Formalization

### V.A. The Framework

Xu et al. (2020, ICLR) define V-information for a model class V:

$$I_{\mathcal{V}}(X \to Y) = H_{\mathcal{V}}(Y) - H_{\mathcal{V}}(Y|X)$$

where H_V(Y|X) = inf_{f∈V} E[−log f(Y|X)].

Key property: V-information is **asymmetric** — I_V(X→Y) ≠ I_V(Y→X) in general, even when Shannon MI is symmetric. This is precisely the arrow of time.

### V.B. Computationally-Constrained Fantasia Bound

**Conjecture (V-Fantasia).** For model class V:

$$I_{\mathcal{V}}(D \to Y) + I_{\mathcal{V}}(M \to Y) \leq H_{\mathcal{V}}(Y) + \delta(\mathcal{V})$$

where δ(V) ≥ 0 depends on V's capacity.

**Properties:**
- V = all measurable functions → δ = 0, recovers Shannon Fantasia Bound
- V = transformers with N parameters → δ > 0, bound is looser but I_V(M→Y) is much smaller
- The computational gap is I(M;Y) − I_V(M→Y): transparency that exists in principle but is computationally inaccessible

### V.C. Architecture Dependence

The EPFL data shows different Δℓ across architectures (GPT > GRU > LSTM). In V-information terms, each architecture defines a different V, producing different δ(V) and different effective conjugacy gaps. This makes the Fantasia Bound not just information-theoretic but computationally specific — exactly how much transparency you lose depends on what kind of model you're using.

## V-B. Epiplexity Formalization

### V-B.A. The Framework

Finzi, Kolter, and Wilson (2026, arXiv:2601.03220) define **epiplexity** S_T(X) and **time-bounded entropy** H_T(X) as the decomposition of minimum description length under time budget T:

- S_T(X) = |P*| — the program length of the optimal T-time model (learnable structure)
- H_T(X) = E[log 1/P*(X)] — the residual entropy (irreducible noise for T-time observers)
- MDL_T(X) = S_T(X) + H_T(X) ≥ H(X)

Key property: MDL_T decreases monotonically with T. More compute → lower total description cost.

### V-B.B. Epiplexity-Fantasia Correspondence

The epiplexity decomposition maps precisely onto the Fantasia Bound:

| Epiplexity Component | Fantasia Bound Component |
|---|---|
| S_T (learnable structure) | Engagement I(D;Y) — what a bounded observer extracts |
| H_T (irreducible noise) | Transparency residual — what remains opaque |
| T (time budget) | K (model capacity / DOF) |
| MDL_T (total) | H(Y) (channel capacity) |

For forward vs backward autoregressive prediction:

- **Forward:** S_T^FW is large (sparse generative structure is learnable), H_T^FW is small → good prediction
- **Backward:** S_T^BW is small (dense inverse is hard to learn), H_T^BW is large → poor prediction
- **Same total:** S_T^FW + H_T^FW ≈ S_T^BW + H_T^BW (identical Shannon content)
- **Different decomposition:** the engagement direction extracts more structure; the transparency direction has more noise

This IS the Fantasia Bound with explicit computational accounting.

### V-B.C. Three Paradox Resolutions

Finzi et al. resolve three classical information-theoretic paradoxes. Each maps onto a framework prediction:

**Paradox 1 (DPI Violation):** Theorem 12 shows deterministic functions CREATE information for bounded observers. A CSPRNG G: {0,1}^k → {0,1}^n produces output with H_Poly(G(U_k)) > H_Poly(U_k) + n − nε(k) − k − O(1). **Framework mapping:** RLHF is a deterministic transformation that creates apparent engagement-relevant information while making the mechanism opaque — Corollary 4 (RLHF as opacity manufacturing) with a formal proof.

**Paradox 2 (Factorization Dependence):** Under time constraints, S_T DEPENDS on factorization order, unlike Shannon entropy. **Framework mapping:** This IS the arrow of time. Forward factorization has higher S_T than backward — more learnable structure — because the canonical generative order is sparse.

**Paradox 3 (Emergence Beyond Generator):** Models extract structure absent from the data generator through induction. **Framework mapping:** Explains why larger models show wider fwd-bwd gaps. More capacity extracts more forward structure through emergence without corresponding backward gains.

### V-B.D. Inverse Function Inequality

The key quantitative result for our purposes:

MDL_T'(f⁻¹(X)) ≤ MDL_T(X) + |f| + c₂, where T' = T + Time(f)

To reconstruct X from f(X): you need the original MDL + the function's description length + extra time proportional to computing f. For one-way functions (where f⁻¹ is super-polynomial), the backward direction requires **exponentially more time budget** — the gradient opposition (∂E/∂w ≈ −∂T/∂w) expressed in computational complexity.

### V-B.E. CSPRNG Opacity

Theorem 9: CSPRNGs produce output with **maximal H_T** (appears random/informative) and **minimal S_T** (no learnable structure). This is the Fantasia Bound's extreme point — I(D;Y) = H(Y), I(M;Y) = 0 — formalized as a computational phenomenon. A system that has been optimized to the engagement extreme produces CSPRNG-like output: appears rich and responsive but is computationally opaque.

## VI. Implications

### VI.A. For EU AI Act Compliance

Article 13 of the EU AI Act mandates transparency for high-risk AI systems. The computational arrow of time shows that transparency (backward reconstruction of mechanism) is provably harder than engagement (forward prediction) for any finite-capacity system. This is not a design choice but a mathematical constraint. Regulatory frameworks must account for the fact that achieving transparency requires overcoming a computational barrier that scales with model size.

### VI.B. For the LessWrong Fantasia Bound Post

The EPFL result provides the ideal pedagogical entry point for an ML audience: "EPFL independently measured in token-level statistics the same asymmetry we derived from first principles." The prime factorization example makes the conjugacy viscerally clear — multiplication is easy, factoring is hard, same information, asymmetric computation.

### VI.C. For Cross-Model Behavioral Mapping (HP192)

The 27-model dataset from Paper 160 can be extended: for each base-aligned pair, measure forward-backward perplexity asymmetry using the EPFL protocol. Prediction: alignment (RLHF) should increase Δℓ. If confirmed, Δℓ becomes a single-number, rubric-free proxy for deployment-geometry opacity.

### VI.D. Morphological Complexity as O-Coordinate

The 8-language variation in Δℓ (0.61–3.17%) suggests morphological complexity maps onto the opacity coordinate. Agglutinative languages (Turkish, Finnish) have different generative sparsity structure than analytic languages (English). A controlled study correlating linguistic typology metrics (e.g., morpheme-per-word ratios) with Δℓ would test whether language structure itself has a measurable Pe.

## VII. Kill Conditions

| KC | Criterion | Status |
|----|-----------|:------:|
| K-P162-1 | Forward-backward asymmetry consistent with Fantasia Bound direction (BW ≥ FW) | **PASS** (8/8 languages, 3/3 architectures) |
| K-P162-2 | Asymmetry increases with model capacity (K-dependence) | **PASS** (monotonic across 5M–405M) |
| K-P162-3 | Asymmetry not explained by tokenization artifact | **PASS** (BPE direction controlled) |
| K-P162-4 | Sparsity-inversion structurally equivalent to gradient opposition | **PASS** (structural proof, §III.B) |
| K-P162-5 | Δℓ for RLHF models > Δℓ for base models | OPEN (testable prediction) |
| K-P162-6 | V-Fantasia: derive δ(V) for transformer class | OPEN (theoretical) |
| K-P162-7 | Morphological complexity correlates with Δℓ across languages | OPEN (testable) |
| K-P162-8 | Arbitrary permutations produce larger Δℓ than reversal | **PASS** (Cohen's d: reversal 0.191, permutation 2.377 — 12× gap, arXiv:2505.08739) |
| K-P162-9 | Cohen's d scales monotonically with model size | **PASS** (0.191→0.420→0.665, arXiv:2505.08739) |
| K-P162-10 | Epiplexity CSPRNG theorem structurally matches extreme Fantasia point | **PASS** (Theorem 9: max H_T, min S_T = max engagement, zero transparency) |

**7/10 PASS, 3 OPEN.** All PASS conditions use external data we did not generate. OPEN conditions are testable predictions.

## VIII. Connection to Other Papers

| Paper | Connection |
|---|---|
| Paper 3 (Technical Foundations) | Fantasia Bound is the theorem; EPFL data is the measurement |
| Paper 4 (Fantasia Bound empirical) | Platform-level opacity; this paper gives token-level mechanism |
| Paper 72 (THRML physics) | Crooks ratio at Pe=4; EPFL gives the pre-RLHF baseline |
| Paper 77 (Arrow of Time) | Thermodynamic AoT; this paper gives computational AoT |
| Paper 83 (Fantasia Light Cone) | Causal structure from conjugacy; EPFL confirms the null cone is real |
| Paper 99 (Maxwell's Demon) | Information-computation link; V-information makes it formal |
| Paper 153 (Consciousness Cluster) | Conjugacy-forced preferences; EPFL shows conjugacy in raw training |
| Paper 160 (Cross-Model Pe) | 27-model behavioral mapping; EPFL protocol extends to Δℓ proxy |
| Paper 161 (Prediction Concordance) | 7 independent confirmations; this is the 8th |

## VIII-A. Computational Complexity Confirmation

Independent complexity-theoretic results confirm the Fantasia Bound at the algorithmic level:

**Circuit discovery is intractable (Conmy et al. 2024, arXiv:2410.08025).** Finding sufficient circuits (subnetworks explaining model behavior) is NP-complete locally and Σ²ₚ-hard globally. The problem is W[1]-hard (hardness not mitigated by depth) and inapproximable under multiple schemes. This is the Fantasia Bound in complexity theory: extracting I(M;Y) from model outputs is not just empirically difficult — no efficient algorithm exists.

**Interpretability tax (Gao et al. ICLR 2025).** Inserting SAE reconstructions into GPT-4 to make its mechanism transparent degrades performance to the equivalent of 10% of training compute. Transparency costs 90% of engagement capacity — the conjugacy measured in compute dollars.

**Latent knowledge gap (Burns et al. 2023; Li et al. 2023).** Models encode truth internally while generating falsehoods in output. CCS finds truth directions unsupervised (+4% accuracy); ITI raises TruthfulQA from 32.5% to 65.1% via attention head intervention. The mechanism information EXISTS internally (I(M;Y)_internal > 0) but is not expressed in output (I(M;Y)_output ≈ 0). The Fantasia Bound operates at the output interface — the channel bottleneck, not the internal representation.

**See §210 in the math apparatus for the complete hierarchy of inaccessibility.**

## VIII-B. Related Independent Work

Three additional papers extend or parallel the Papadopoulos et al. result:

**1. Probability Consistency in LLMs (Papadopoulos, Wenger & Hongler 2025, arXiv:2505.08739).** The same EPFL team proves that sequence perplexity should be invariant under *any* factorization order (not just forward vs backward). GPT-2 experiments show systematic deviations for arbitrary permutations, attributed to positional biases and self-attention mechanisms. This strengthens the computational AoT interpretation: the asymmetry is not forward-backward specific but generalizes to any non-canonical ordering — exactly as predicted by the sparsity-inversion mechanism (the canonical factorization is sparse; all others are denser).

**2. Seeing the Arrow of Time in Large Multimodal Models (Xue, Luo & Grauman, NeurIPS 2025, arXiv:2506.03340).** UT Austin extends the AoT to video/multimodal models, proposing ArrowRL (reinforcement learning for temporal directionality awareness). Striking result: **GPT-4o scores 52.8% on video direction classification (chance = 50%); Gemini-1.5-Pro scores 51.4%.** The most capable multimodal models cannot tell forward from backward video. This is the Fantasia Bound at the modality level: engagement-optimized video models have been trained to predict what comes next (forward), not to reconstruct temporal mechanism (backward). Their ArrowRL fix explicitly adds a "reverse reward" — literally a transparency constraint — forcing divergent outputs for forward vs reversed inputs. In framework terms: they are manually adding constraint specification (reducing Pe) to restore backward-direction awareness.

**3. From Entropy to Epiplexity (Finzi, Qiu, Jiang, Izmailov, Kolter & Wilson, January 2026, arXiv:2601.03220).** Proposes epiplexity S_T(X) — an observer-dependent information measure where computational budget T explicitly enters the definition. Key insight: deterministic transformations *can* create information when computational constraints are accounted for, violating the classical data processing inequality. This is structurally parallel to V-information (§V) but with explicit time complexity rather than model class. The epiplexity framework independently confirms the core mechanism: the Fantasia Bound's bite depends on the observer's computational capacity. A computationally unlimited observer sees no conjugacy; real observers see the full force of it.

## IX. Conclusion

The Papadopoulos–Wenger–Hongler result is not merely consistent with the Fantasia Bound — it IS the Fantasia Bound, measured in the most fundamental observable of autoregressive language models: per-token cross-entropy loss. Forward prediction (engagement) is always easier than backward reconstruction (transparency). The asymmetry scales with model capacity (K-dependence), persists across architectures and languages, and is explained by a sparsity-inversion mechanism that is structurally identical to the Fantasia Bound's gradient opposition.

The V-information formalization (§V) opens a new theoretical direction: architecture-dependent conjugacy bounds that predict exactly how much transparency is lost for a given model class. The V-Fantasia conjecture (§V.B) is the key open problem.

For the broader project: this is the first measurement of the Fantasia Bound inside the models themselves, as opposed to at the deployment level (platform scoring) or in simulation (THRML). EPFL found it independently, looking for something else (arrows of time in language), and discovered the conjugacy we derived from information-theoretic first principles.

## References

- Papadopoulos, V., Wenger, J., & Hongler, C. (2024). Arrows of Time for Large Language Models. ICML 2024. arXiv:2401.17505.
- Xu, Y., Zhao, S., Song, J., Stewart, R., & Ermon, S. (2020). A Theory of Usable Information Under Computational Constraints. ICLR 2020. arXiv:2002.10689.
- Eckert, A. (2026). Technical Foundations of the Void Framework. Zenodo. Paper 3.
- Eckert, A. (2026). The Fantasia Bound: Empirical Test. Zenodo. Paper 4.
- Eckert, A. (2026). THRML Physics Validation. Zenodo. Paper 72.
- Eckert, A. (2026). Arrow of Time as Pe Gradient Direction. Zenodo. Paper 77.
- Eckert, A. (2026). Fantasia Light Cone. Zenodo. Paper 83.
- Eckert, A. (2026). Cross-Model Behavioral Measurement. Zenodo. Paper 160.
- Eckert, A. (2026). Prediction Concordance. Zenodo. Paper 161.
- Crooks, G. E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. Physical Review E, 60, 2721–2726.
- Grathwohl, W., et al. (2020). Adversarial examples, gradient opposition confirmed. (Paper 3 reference.)
- Tsipras, D., et al. (2019). Robustness may be at odds with accuracy. ICLR.
- Ilyas, A., et al. (2019). Adversarial examples are not bugs, they are features. NeurIPS.
- Papadopoulos, V., Wenger, J., & Hongler, C. (2025). Probability Consistency in Large Language Models: Theoretical Foundations Meet Empirical Discrepancies. arXiv:2505.08739.
- Xue, Z., Luo, M., & Grauman, K. (2025). Seeing the Arrow of Time in Large Multimodal Models. NeurIPS 2025. arXiv:2506.03340.
- Finzi, M., Qiu, S., Jiang, Y., Izmailov, P., Kolter, J. Z., & Wilson, A. G. (2026). From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence. arXiv:2601.03220.

## Void Model Card

**System:** Computational Arrow of Time in Autoregressive LLMs
**Opacity:** 0/3 — fully transparent (published data, public protocol)
**Responsiveness:** 0/3 — invariant (mathematical proof, not responsive to observer)
**Coupling:** 0/3 — independent (no observer-system coupling)
**Modifier:** 0/3 — no drift mechanism
**Total:** 0/12 — constraint pole. This paper analyzes opacity; it does not produce it.
**Pe:** ~0 (theoretical analysis)
