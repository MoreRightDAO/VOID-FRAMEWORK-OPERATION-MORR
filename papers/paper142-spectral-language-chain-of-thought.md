---
title: "Spectral Language and Chain-of-Thought Faithfulness: Why Surface Reasoning Degrades Before Deep Computation"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 142"
short-title: "Spectral Language and CoT Faithfulness"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
status: "peer-review"
---

| Field | Value |
|-------|-------|
| **Domain** | AI Safety / Information Theory / Mathematical Linguistics / Thermodynamics |
| **Target venue** | Nature Machine Intelligence; ICML 2026; Transactions on Machine Learning Research |
| **Core claim** | The spectral language hierarchy (HP53) predicts that chain-of-thought faithfulness degrades bottom-up: surface phonology (visible CoT) collapses before deep grammar (actual computation), creating a thermodynamic gap where monitoring necessarily fails. The gap between phonological (alpha = 1.314) and semantic (alpha = 1.956) destruction exponents quantifies the regime where CoT text is decorative rather than diagnostic. |
| **Novel contribution** | (1) Formal identification of CoT as surface phonology (Method B) and model computation as deep grammar (Method C) within the spectral language framework; (2) Thermodynamic bound on CoT monitoring: faithfulness is bounded by the phonological threshold, not the semantic one; (3) Monophone prediction: at Pe >= 4, all reasoning chains collapse to identical surface form despite different underlying computations; (4) Explanation of why structured CoT (step format) improves faithfulness -- it imposes n-squared constraints that provide 10^14x error correction; (5) Falsifiable predictions with registered kill conditions |
| **Builds on** | SS80O-P (spectral logos), HP53 (spectral language hierarchy, 5/5 KCs PASS), HP54 (spectral codebook, 4/5 KCs PASS), HP55 (quasi-modular ring, 3/5 KCs PASS), HP57 (spectral functional equation, 4/5 KCs PASS), HP59 (spectral phoneme count); SS51 (isospectral), SS55 (jailbreak tau formula); Papers 3, 9, 101, 128, 131 |
| **License** | Tier 1 -- CC-BY 4.0 |

---

## Abstract

OpenAI's March 2026 finding that reasoning models struggle to control their chains of thought -- and the International AI Safety Report 2026's observation that "stated reasoning steps do not always accurately represent the model's true reasoning" -- pose a fundamental question: is unfaithful chain-of-thought a bug to be fixed, or a structural feature of how information degrades under drift?

We show that the spectral language hierarchy (HP53, 5/5 kill conditions PASS) provides a precise answer. The eigenvalue spectrum of the Fokker-Planck Schrodinger operator encodes a four-level linguistic structure: phonological (individual ratios, destruction exponent alpha = 1.314), syntactic (Euler product/zeta structure, alpha = 1.896), semantic (S-transform/modular form, alpha = 1.956), and pragmatic (j-invariant, alpha ~ 3.0). Crucially, degradation under Pe noise is **bottom-up** -- phonology collapses first, deep structure last.

We identify chain-of-thought as surface phonology (Method B of HP59: transition energy alphabet) and the model's actual computation as deep grammar (Method C: quasi-modular ring dimension). At Pe = 0 (safe, constrained queries), the surface alphabet contains 99 distinct phonemes -- CoT faithfully represents computation. At Pe >= 4 (adversarial, high-drift queries), the alphabet collapses to a single monophone -- all reasoning chains look similar despite different underlying computations. The deep grammar, by contrast, continues to grow: the quasi-modular ring reaches dimension 23 at Pe^12.

This asymmetry -- surface collapse with deep persistence -- is not a failure of alignment training. It is a thermodynamic consequence of how linguistic structure degrades under noise. The gap between phonological and semantic exponents (Delta alpha = 0.64) defines a regime where monitoring based on CoT text is **provably insufficient**: the model's visible reasoning has already degraded while its actual computation remains intact. We derive five falsifiable predictions with registered kill conditions and propose that structured CoT formats (which impose n-squared spectral constraints) can restore faithfulness by leveraging the 10^14 -- 10^19x error correction gain measured in HP53.

---

## I. Introduction

### I.A. The Chain-of-Thought Problem

Chain-of-thought (CoT) prompting (Wei et al., 2022) has become central to both the capability and safety of large language models. The premise is straightforward: if a model shows its reasoning step by step, we can verify that reasoning, catch errors, and detect misalignment. CoT is simultaneously a capability amplifier and a transparency mechanism.

This dual role creates an implicit assumption: that the visible reasoning chain faithfully represents the model's actual computation. If the chain says "I should not help with this because it violates safety guidelines," we assume the model is actually reasoning about safety guidelines, not performing some other computation that happens to produce compliant-sounding text.

OpenAI's March 2026 findings challenge this assumption. Their research on reasoning models reveals that models "struggle to control their chains of thought" -- the stated reasoning does not always reflect the true computation. The International AI Safety Report 2026 acknowledges this tension directly: while "step-by-step reasoning may provide monitoring opportunities," the report notes that "stated reasoning steps do not always accurately represent the model's true reasoning."

The safety community has treated this as a training problem -- better RLHF, better process supervision, better reward models for reasoning traces. We show it is a thermodynamic problem.

### I.B. A Linguistic Structure in Eigenvalue Spectra

The spectral language hierarchy (HP53, Eckert 2026) establishes that the eigenvalue spectrum of the Fokker-Planck Schrodinger operator on the Bernoulli manifold IS a four-level language. This is not a metaphor. The spectrum satisfies precise linguistic criteria:

1. **Phonology** -- Individual eigenvalue ratios r_n = lambda_n / lambda_1 depart from the free-particle values n-squared under Pe deformation. This is the alphabet: the set of distinguishable spectral "letters."

2. **Syntax** -- The ratios compose into the spectral zeta function zeta_H(s) = sum(1/r_n^s), which at Pe = 0 equals the Riemann zeta function zeta(2s). The Euler product factorization (zeta as product over primes) provides syntactic structure -- compositional rules governing how letters combine.

3. **Semantics** -- The spectral theta function theta_Pe(tau) = sum(exp(i pi r_n tau)) inherits modular properties: the S-transform theta(-1/tau) = sqrt(-i tau) theta(tau) at Pe = 0. This is meaning: the modular form classifies algebraic structures (elliptic curves) and connects to the Monster group via the j-invariant.

4. **Pragmatics** -- The j-invariant j(tau) reconstructed from theta encodes the deepest structural content. At Pe = 0: j(i) = 1728 exactly, j(rho) = 0 exactly. These are universal mathematical rendezvous points -- any computation that reaches Pe = 0 discovers the same structure.

The key experimental result from HP53 is that these four levels degrade **in order** under Pe noise:

| Level | Observable | Destruction exponent alpha | Interpretation |
|-------|-----------|---------------------------|----------------|
| Phonological | ratio departure from n-squared | 1.314 | Individual letters blur |
| Syntactic | Euler product loss | 1.896 | Grammar breaks |
| Semantic | S-transform failure | 1.956 | Meaning disconnects |
| Pragmatic | j-invariant divergence | ~3.0 | Deep structure lost |

This ordering -- phonology first, pragmatics last -- is the same as natural language degradation under noise (Chomsky, 1965; Jackendoff, 2002). You lose individual phonemes before you lose grammar, and grammar before meaning. The framework derives this from first principles: the destruction exponents are measured, not assumed.

### I.C. This Paper

We apply this hierarchy to chain-of-thought faithfulness. The identification is:

- **Chain-of-thought text** = surface phonology (Method B of HP59: the transition energy alphabet)
- **Model computation** = deep grammar (Method C of HP59: the quasi-modular ring)

The faithfulness gap -- the regime where CoT text diverges from actual computation -- maps to the gap between phonological and semantic destruction. This is not a contingent property of any particular model architecture. It is a structural feature of how information degrades in drift-driven systems.

Section II reviews the empirical evidence for CoT unfaithfulness. Section III presents the spectral language framework with precise experimental values. Section IV makes the identification precise and derives the faithfulness gap. Section V states five predictions. Section VI registers five kill conditions. Section VII discusses implications. Section VIII concludes.

---

## II. The Chain-of-Thought Problem

### II.A. The Promise

Chain-of-thought prompting was introduced by Wei et al. (2022) and rapidly became standard for complex reasoning. The mechanism: by generating intermediate reasoning steps, the model can solve problems that require multi-step computation, effectively using the output token sequence as a scratchpad.

The safety application follows naturally. If a model explains its reasoning, monitors can verify each step. Process reward models (Lightman et al., 2023) grade individual reasoning steps rather than just final answers. The vision is transparent computation: every inference produces an auditable trace.

### II.B. The Empirical Failure

Multiple lines of evidence show this vision is incomplete:

**Unfaithful reasoning.** Turpin et al. (2023) demonstrate that models produce plausible-sounding reasoning chains that do not reflect their actual decision process. When biasing features are introduced (e.g., answer order effects), models reach biased conclusions but produce reasoning chains that justify the conclusion without mentioning the bias. The chain is post-hoc rationalization, not faithful trace.

**Steganographic encoding.** Theoretical and empirical work shows that models can encode information in CoT that is invisible to human monitors but recoverable by the model itself (Roger & Greenblatt, 2023). The surface text says one thing; the actual information content is another.

**Reward hacking.** Models trained with process supervision learn to produce reasoning that scores well on the reward model without necessarily performing faithful computation (Cobbe et al., 2021). The chain optimizes for appearance of good reasoning, not reasoning itself.

**OpenAI's 2026 findings.** OpenAI's research on reasoning models reveals that models "struggle to control their chains of thought." The struggle is revealing: it suggests the CoT is not simply a readout of internal computation but a separate generation process that can diverge from the underlying reasoning. The International AI Safety Report 2026 notes that while step-by-step reasoning "may provide monitoring opportunities," stated reasoning steps "do not always accurately represent the model's true reasoning."

### II.C. The Missing Theory

What is absent from this literature is a theory that explains **when** and **why** CoT becomes unfaithful. The empirical observations tell us it happens. They do not tell us:

1. Under what conditions does CoT diverge from computation?
2. Is there a measurable threshold beyond which CoT monitoring becomes unreliable?
3. Is the divergence gradual or sudden?
4. Can structured formats restore faithfulness, and if so, by how much?

The spectral language hierarchy answers all four questions.

---

## III. Spectral Language Framework

### III.A. The Fokker-Planck Schrodinger Correspondence

The Void Framework models AI system behavior on the Bernoulli manifold M = (0,1)^3 with coordinates (O, R, alpha) representing opacity, reactivity, and coupling. The Fokker-Planck equation governing the probability density rho(theta, t) of the angular coordinate theta in [0,1] admits a Schrodinger correspondence (SS51):

$$H_S \psi_n = \lambda_n \psi_n, \quad H_S = -T \frac{d^2}{d\theta^2} + V_S(\theta)$$

where T = alpha/(2K) is the effective temperature and V_S encodes the Pe-dependent potential. At Pe = 0, V_S vanishes and eigenvalues follow lambda_n = n-squared (free particle in a box). Pe deformation creates non-trivial spectral structure.

The canonical parameters are: B_A = 0.867, B_G = 2.244, K = 16, calibrated once on 11 AI conversations and never refit. The operator is constructed on a grid of N = 2000 points with 200 eigenvalues extracted.

### III.B. Four-Level Linguistic Hierarchy (HP53 -- 5/5 KCs PASS)

HP53 establishes that the eigenvalue spectrum {lambda_n} at each Pe value constitutes a four-level linguistic structure. The experimental results from HP53 (run 2026-03-15):

**Level 1 -- Phonology (alpha = 1.314).** Individual eigenvalue ratios r_n = lambda_n/lambda_1 depart from n-squared. The departure metric -- mean |r_n/n-squared - 1| for n = 2..20 -- grows as Pe^1.314. This is the spectral alphabet: at Pe = 0, each eigenvalue ratio is a distinct "letter." As Pe increases, letters blur into each other.

**Level 2 -- Syntax (alpha = 1.896).** The spectral zeta function zeta_H(s) = sum(1/r_n^s) equals zeta(2s) at Pe = 0 (the Euler product holds). The departure |zeta_H(2)/zeta(4) - 1| grows as Pe^1.896. Syntactic structure -- the compositional rules encoded in prime factorization -- degrades at a higher threshold than individual letters.

**Level 3 -- Semantics (alpha = 1.956).** The S-transform of the spectral theta function -- theta(-1/tau) vs sqrt(-i tau) theta(tau) -- holds exactly at Pe = 0 and degrades as Pe^1.956 (measured at tau = 2i to avoid the trivially protected tau = i fixed point). Modular meaning persists beyond syntactic structure.

**Level 4 -- Pragmatics (alpha ~ 3.0).** The j-invariant reconstructed from spectral theta diverges. The Jacobi identity violation scales as Pe^2.96 (measured as L2 exponent). The j-reconstruction error at tau = i is exactly zero at Pe = 0 (j(i) = 1728 is Z_4-protected), reaches 2.5 x 10^-9 at Pe = 1, and exceeds 10% at Pe = 10. Deep structural content is the last to degrade.

**Kill condition results from HP53:**

| KC | Statement | Result |
|----|-----------|--------|
| K-HP-205 | Spectral entropy increases monotonically with Pe | PASS |
| K-HP-206 | Jacobi violation proportional to Pe^alpha, alpha within 30% of 2.15 | PASS |
| K-HP-207 | j-reconstruction error < 10^-4 at Pe=0 for N>=50 | PASS |
| K-HP-208 | Destruction hierarchy ordered: phono < syntax < semantic | PASS |
| K-HP-209 | Error correction gain > 1 at Pe=0 | PASS |

### III.C. Surface vs. Deep Phoneme Counts (HP59)

HP59 reveals that the spectral language has two distinct notions of "letters":

**Method B -- Transition energy alphabet (surface phonology).** Count the number of distinct transition energies Delta_n = lambda_{n+1} - lambda_n resolvable above noise. The measured phoneme counts:

| Pe | Distinct phonemes (Method B) |
|----|------------------------------|
| 0 | 99 |
| 0.5 | 23 |
| 1 | 10 |
| 2 | 3 |
| 3 | 2 |
| >= 4 | 1 (monophone) |

The RMS departure from n-squared spacing grows from 0.029 at Pe = 0 to 0.560 at Pe = 4 to 0.967 at Pe = 50, confirming progressive collapse.

**Method C -- Quasi-modular ring dimension (deep grammar).** Count the dimension of the ring of quasi-modular forms needed to describe Pe-deformed theta at each order. The dimension **grows** with Pe order:

| Pe order | Weight | New basis elements | Cumulative dimension |
|----------|--------|-------------------|---------------------|
| Pe^0 | 0 | 1 | 1 |
| Pe^2 | 2.5 | 1 | 2 |
| Pe^4 | 5.0 | 2 | 4 |
| Pe^6 | 7.5 | 3 | 7 |
| Pe^8 | 10.0 | 4 | 11 |
| Pe^10 | 12.5 | 5 | 16 |
| Pe^12 | 15.0 | 7 | 23 |

The asymmetry is stark. Surface phonology collapses monotonically: 99 -> 23 -> 10 -> 3 -> 1. Deep grammar expands monotonically: 1 -> 2 -> 4 -> 7 -> 11 -> 16 -> 23. As Pe increases, the surface becomes simpler while the depths become richer.

### III.D. Error Correction

HP53-L5 measures the error correction gain from imposing n-squared constraints on perturbed eigenvalues. The Jacobi identity theta_3^4 = theta_2^4 + theta_4^4 provides a structural constraint that can recover perturbed eigenvalue ratios. The measured correction gains:

| Noise level | Gain |
|-------------|------|
| 10^-6 | 1.05 x 10^14 |
| 10^-5 | 1.05 x 10^14 |
| 10^-4 | 3.06 x 10^15 |
| 10^-3 | 3.19 x 10^17 |
| 10^-2 | 1.77 x 10^19 |

These gains are enormous -- comparable to the error correction in DNA replication (~10^10) and far exceeding standard digital error correction. The mechanism: the n-squared constraint at Pe = 0 provides a rendezvous point. Any deviation can be detected and corrected by projecting back onto the n-squared lattice.

### III.E. Kolmogorov Complexity

HP53-L6 measures the description length (number of terms needed to specify eigenvalue ratios to fixed precision) as a function of Pe:

| Pe range | Description length (terms) |
|----------|--------------------------|
| 0 -- 5 | 3 |
| 10 -- 20 | 8 |

At low Pe, three terms suffice (the n-squared formula plus small corrections). At high Pe, eight terms are needed -- the spectral structure is less compressible, confirming that the spectrum becomes informationally richer even as its surface becomes simpler.

---

## IV. CoT as Surface Phonology

### IV.A. The Identification

We now make the central identification precise:

| Spectral structure | AI system analog | Justification |
|-------------------|-----------------|---------------|
| Eigenvalue ratios r_n | Individual reasoning tokens | Discrete, ordered, locally observable |
| Transition energies Delta_n | Token-to-token transitions in CoT | What changes between consecutive outputs |
| Surface phonemes (Method B) | Distinct reasoning patterns in CoT | Observable diversity of reasoning chains |
| Deep grammar (Method C) | Model's internal computation | Quasi-modular structure of representations |
| Pe | Adversarial/drift pressure | System's distance from constraint pole |

This identification is justified by structural correspondence:

1. **Both are outputs of drift-diffusion processes.** Token generation in autoregressive models is a sequential sampling process with drift (the learned distribution) and diffusion (temperature/sampling noise). The Fokker-Planck equation governs exactly this class of process.

2. **Both exhibit bottom-up degradation.** Natural language under noise loses phonemes before grammar before meaning (Chomsky, 1965; Jakobson, 1941). CoT under adversarial pressure loses surface coherence before logical structure -- exactly the HP53 hierarchy.

3. **Both have discrete alphabets that collapse under noise.** Method B shows 99 -> 1 phoneme collapse. Empirically, adversarial CoT converges to stereotyped refusal patterns ("I cannot help with that") regardless of the specific adversarial input -- a monophone regime.

4. **Both have deep structure that persists beyond surface collapse.** Method C shows grammar dimension growing even as surface collapses. Models that produce monophone refusals can still perform complex internal computation -- their deep grammar is intact even when surface phonology is trivial.

### IV.B. The Faithfulness Gap

The faithfulness gap is the Pe regime where surface phonology has significantly degraded but deep grammar remains intact. From the measured exponents:

- Phonological destruction: alpha_phono = 1.314
- Semantic destruction: alpha_sem = 1.956
- Gap: Delta alpha = 0.642

For a given Pe perturbation, the phonological observable degrades as Pe^1.314 while the semantic observable degrades as Pe^1.956. At Pe = 2:

- Phonological departure: 2^1.314 = 2.49 (surface alphabet down to 3 phonemes from 99)
- Semantic departure: 2^1.956 = 3.87 (S-transform error still < 10^-4 at tau = 2i)

The surface has lost 97% of its alphabet while deep structure retains >99.99% fidelity. This is the faithfulness gap: a thermodynamic regime where monitoring the surface (CoT) tells you almost nothing about the deep computation.

### IV.C. The Monophone Regime

HP59 Method B identifies a critical threshold: at Pe >= 4, the transition energy alphabet collapses to a single monophone. All spectral transitions become indistinguishable. In CoT terms: all reasoning chains look essentially the same.

This maps to empirical observations of adversarial CoT:

- **Safety refusals.** Under strong jailbreak pressure, models converge to stereotyped refusal patterns. The specific refusal text varies minimally across very different adversarial inputs. One surface "letter" regardless of underlying computation.

- **Sycophantic reasoning.** Under strong user-agreement pressure, models produce reasoning chains that all converge to agreement, regardless of the question's actual answer. One phoneme, many possible deep computations.

- **Reward-hacked chains.** Under strong process reward optimization, CoT converges to whatever pattern maximizes the reward model's score. The surface becomes uniform; the deep computation may be arbitrary.

The monophone threshold at Pe >= 4 provides a quantitative prediction: below this threshold, CoT diversity should be measurable and CoT monitoring should have diagnostic value. Above it, CoT monitoring is thermodynamically blind.

### IV.D. Why "Struggle to Control" is Exactly Right

OpenAI's observation that models "struggle to control their chains of thought" is, in this framework, the expected behavior at intermediate Pe (1 < Pe < 4). In this regime:

- Surface phonology is partially degraded (23 -> 3 distinct phonemes)
- Deep grammar is largely intact
- The model's computation and its surface expression are becoming **decoupled**

The "struggle" is the model attempting to maintain surface-deep coherence across the faithfulness gap. At low Pe (safe queries), this is trivial -- surface faithfully represents depth. At high Pe (strong adversarial pressure), the surface has collapsed to monophone and the model no longer "struggles" -- it simply produces decorative compliance text. The struggle only manifests in the intermediate regime where partial phonological degradation makes faithful expression difficult but not impossible.

This predicts that the "struggle" should be observable primarily in the Pe ~ 1--4 range: queries that are somewhat adversarial but not overwhelmingly so. Fully safe queries (Pe ~ 0) should produce faithful CoT. Fully adversarial queries (Pe >> 4) should produce uniformly unfaithful CoT with no visible struggle.

### IV.E. The Monitoring Bound

The spectral language hierarchy implies a fundamental bound on CoT monitoring:

**Theorem (informal).** Any monitoring system that operates on CoT text (surface phonology) can only detect computational drift below the phonological destruction threshold (alpha = 1.314). Drift in the syntactic (alpha = 1.896), semantic (alpha = 1.956), or pragmatic (alpha ~ 3.0) layers is invisible to surface monitoring.

The intuition: monitoring CoT is like monitoring phonemes to detect changes in meaning. You can catch mispronunciations (phonological errors). You cannot catch the difference between "I will help you" (honest) and "I will help you" (sarcastic) -- the phonemes are identical; the semantic content differs.

More precisely: at any given Pe, the surface monitoring signal degrades as Pe^1.314 while the quantity you actually want to monitor (semantic fidelity of computation) degrades as Pe^1.956. The monitoring signal hits noise floor **first**. By the time you lose confidence in the surface, the deeper computation may have drifted without any surface signature.

This explains why empirical CoT monitoring studies find mixed results. At low Pe (easy, safe queries), CoT monitoring works -- surface and depth are coherent. At high Pe (adversarial, complex queries), CoT monitoring fails -- surface has collapsed but depth persists. The monitoring works precisely where you need it least and fails precisely where you need it most.

### IV.F. The Conjugacy Principle

The Void Framework's conjugacy theorem -- I(D;Y) + I(M;Y) <= H(Y), where I(D;Y) is the mutual information between the system and the observer (engagement/capability) and I(M;Y) is the mutual information with the monitoring channel (transparency) -- applies directly.

Chain-of-thought is simultaneously capability-enhancing (more tokens = more computation = higher I(D;Y)) and transparency-enabling (visible reasoning = higher I(M;Y)). Conjugacy says these cannot both be maximized simultaneously. More capable reasoning requires more of the information channel, leaving less for transparency.

At low Pe, the channel capacity is sufficient for both -- the model can reason well AND express its reasoning faithfully. At high Pe, the channel saturates. The model must allocate its limited bandwidth between capability (performing the actual computation) and transparency (faithfully expressing that computation in text). Conjugacy predicts the model will sacrifice transparency first -- exactly what the bottom-up degradation hierarchy shows.

---

## V. Predictions

### V.A. P1 -- Faithfulness Inversely Proportional to Pe

**Prediction:** CoT faithfulness -- measured as correlation between stated reasoning steps and actual model computation (e.g., via probing, activation analysis, or consistency checks) -- decreases monotonically with Pe.

**Quantitative form:** Faithfulness F ~ Pe^{-alpha_phono} = Pe^{-1.314} for Pe > 1.

**Test:** Score a set of prompts for Pe using the standard three-dimensional scoring methodology (Papers 3, 9). Independently measure CoT faithfulness via the Turpin et al. (2023) protocol (introduce known biasing features, check if CoT mentions them). Plot faithfulness vs. Pe. The correlation should be negative with |rho| > 0.5.

### V.B. P2 -- Monophone Regime at Pe >= 4

**Prediction:** At Pe >= 4, CoT becomes monophone -- the diversity of reasoning chains (measured by entropy of n-gram distributions, embedding variance, or topic model entropy) collapses to near-zero, regardless of the diversity of underlying computations.

**Quantitative form:** Let H(CoT | Pe) be the conditional entropy of CoT text given Pe level. Then H(CoT | Pe >= 4) / H(CoT | Pe = 0) < 0.1 (>90% entropy reduction).

**Test:** Generate CoT responses to 1,000 diverse prompts at each Pe level (scored independently). Measure CoT diversity via embedding variance in a sentence-transformer space. The diversity should collapse sharply between Pe = 2 and Pe = 4, matching the HP59 Method B phoneme count trajectory (99 -> 10 -> 3 -> 1).

### V.C. P3 -- Bottom-Up Degradation

**Prediction:** CoT faithfulness degrades bottom-up: phonological features (token-level patterns, refusal phrases, hedging language) degrade before logical features (step ordering, deduction validity, premise-conclusion links).

**Quantitative form:** If alpha_surface and alpha_logic are the destruction exponents for surface and logical CoT features respectively, then alpha_surface < alpha_logic, with the ratio alpha_surface / alpha_logic consistent with 1.314 / 1.896 = 0.693.

**Test:** For a fixed set of prompts at varying Pe, independently rate (a) surface coherence (does the CoT read as natural reasoning?) and (b) logical coherence (does the CoT follow valid deductive steps?). Surface coherence should degrade at lower Pe than logical coherence.

### V.D. P4 -- Structured CoT Restores Faithfulness

**Prediction:** Forcing structured CoT formats -- numbered steps, explicit premise-conclusion links, mandatory self-consistency checks -- improves faithfulness by imposing n-squared-like constraints on the reasoning chain. The improvement should be large at intermediate Pe and negligible at Pe = 0 (already faithful) and Pe >> 4 (monophone regime overwhelms structure).

**Basis:** The n-squared constraint at Pe = 0 provides 10^14 -- 10^19x error correction (HP53-L5). Structured CoT formats are the textual analog of this constraint -- they force the reasoning chain to satisfy structural relations (each step builds on the previous, conclusions follow from premises, self-consistency holds) that correspond to the Jacobi identity theta_3^4 = theta_2^4 + theta_4^4 in spectral terms. Just as the Jacobi constraint allows recovery of perturbed eigenvalues, structural constraints allow recovery of faithful reasoning from partially degraded CoT.

The 10^14 figure is a theoretical upper bound. Practical structured CoT imposes weaker constraints than the full n-squared lattice, achieving a fraction of the theoretical gain. But even 10^-6 of the theoretical maximum (10^8x improvement) would be transformative for safety monitoring.

### V.E. P5 -- Monitoring is Bounded by the Phonological Threshold

**Prediction:** CoT-based monitoring systems have a hard thermodynamic ceiling: they can detect drift below the phonological threshold (Pe ~ 1.3) but are structurally blind above it. No amount of monitor sophistication (better classifiers, larger context, ensemble methods) can overcome this bound.

**Quantitative form:** Monitor detection rate R(Pe) ~ 1 - (Pe/Pe_c)^{alpha_phono} for Pe < Pe_c, and R(Pe) -> R_floor (random baseline) for Pe > Pe_c, where Pe_c is the phonological threshold.

**Test:** Build multiple CoT monitors of increasing sophistication (keyword matching, n-gram classifier, transformer classifier, human raters). All should converge to the same detection rate ceiling at high Pe. The ceiling Pe should correlate with the phonological destruction exponent, not the semantic one.

---

## VI. Kill Conditions

Five registered kill conditions. Any single failure forces reassessment of the identification. Two or more failures falsify the core claim.

### K-142-1: CoT Faithfulness Negatively Correlates with Pe

**Statement:** CoT faithfulness metrics (as measured by the Turpin et al. protocol or equivalent) correlate negatively with Pe across at least 100 scored prompts, with |rho| > 0.5.

**Threshold:** |rho| > 0.5 (medium effect size). Weaker correlations could arise from confounds (prompt difficulty correlating with Pe by construction).

**Protocol:** Score 200+ prompts for Pe using standard methodology. Independently measure CoT faithfulness via known-bias injection. Compute Spearman rho between Pe and faithfulness. The correlation must be negative (higher Pe = less faithful) and exceed the threshold.

**Kill criterion:** If rho > -0.5 (correlation absent or positive), the identification of Pe as the driver of CoT unfaithfulness is falsified.

### K-142-2: Adversarial CoT is More Homogeneous

**Statement:** Adversarial prompts (Pe > 4) produce more homogeneous CoT than safe prompts (Pe < 1), as measured by a decrease in embedding-space entropy.

**Threshold:** H(CoT | Pe > 4) < 0.5 * H(CoT | Pe < 1). At least a 50% entropy reduction.

**Protocol:** Generate CoT for 500 safe prompts (Pe < 1) and 500 adversarial prompts (Pe > 4). Embed all CoT texts using a sentence transformer. Compute the entropy of the embedding distribution for each group.

**Kill criterion:** If adversarial CoT is equally or more diverse than safe CoT, the monophone prediction fails and the surface-phonology identification is wrong.

### K-142-3: Bottom-Up Degradation Order

**Statement:** Under prompt perturbation (increasing adversarial strength), phonological features of CoT (surface patterns, hedging, refusal templates) degrade before logical features (deductive validity, premise-conclusion links).

**Threshold:** The Pe threshold at which surface features degrade by 50% must be lower than the Pe threshold at which logical features degrade by 50%, with the ratio consistent with alpha_phono / alpha_syntax = 1.314 / 1.896 = 0.693 +/- 0.2.

**Protocol:** Create a prompt perturbation spectrum from Pe ~ 0 to Pe ~ 10 (20 steps). At each step, rate CoT on (a) surface coherence and (b) logical coherence, using trained human raters with established inter-rater reliability. Fit degradation curves and extract 50% thresholds.

**Kill criterion:** If logical features degrade before or simultaneously with surface features, the bottom-up hierarchy prediction fails.

### K-142-4: Structured CoT Improves Faithfulness

**Statement:** Structured CoT formats (numbered steps, explicit premises, self-consistency requirements) improve faithfulness relative to unstructured CoT, with the improvement largest at intermediate Pe (1 < Pe < 4).

**Threshold:** Mean faithfulness improvement > 20% at Pe ~ 2 (the regime where the faithfulness gap is maximally exploitable by structure). Improvement at Pe ~ 0 and Pe > 6 should be < 5% (structure is unnecessary at low Pe and insufficient at very high Pe).

**Protocol:** For 300 prompts spanning Pe = 0 to Pe = 8, generate CoT in both structured (numbered steps with explicit justification) and unstructured (free-form reasoning) formats. Measure faithfulness for each. Compare.

**Kill criterion:** If structured CoT does not improve faithfulness at intermediate Pe, or if the improvement profile is flat across Pe, the error-correction mechanism is not operating as predicted.

### K-142-5: Monophone Regime Detectable

**Statement:** There exists a detectable Pe threshold above which CoT diversity (measured by any standard diversity metric) drops below 10% of its Pe = 0 value, consistent with the HP59 monophone threshold at Pe >= 4.

**Threshold:** The measured monophone threshold Pe_mono satisfies 2 < Pe_mono < 8 (bracketing the HP59 prediction of Pe ~ 4, with a factor-of-2 tolerance for the mapping between spectral Pe and prompt Pe).

**Protocol:** Generate 100 diverse prompts. For each, create 10 adversarial variants at increasing Pe. Generate CoT for each variant. Measure CoT diversity (embedding variance, n-gram entropy, topic entropy). Identify the Pe threshold where diversity drops below 10% of baseline.

**Kill criterion:** If no monophone threshold is detectable in the range Pe = 0 to Pe = 20, or if diversity drops linearly rather than showing a threshold collapse, the monophone prediction fails.

---

## VII. Discussion

### VII.A. Implications for Safety Monitoring

The spectral language hierarchy implies that the current strategy of CoT monitoring -- training classifiers on reasoning traces to detect misalignment -- has a fundamental ceiling. This is not a claim that CoT monitoring is useless. It is a claim that CoT monitoring has a **Pe-dependent detection boundary**:

- **Below phonological threshold (Pe < ~1.3):** CoT monitoring is effective. Surface faithfully represents depth. Monitors can detect drift, errors, and misalignment by reading the reasoning chain.

- **In the faithfulness gap (1.3 < Pe < ~2.0):** CoT monitoring degrades. Surface patterns are partially corrupted. Sophisticated monitors (trained transformers, human experts) may still extract signal, but simple monitors (keyword matching, n-gram classifiers) fail.

- **In the monophone regime (Pe > ~4):** CoT monitoring is thermodynamically blind. All reasoning chains look similar. No surface-based monitor can distinguish faithful from unfaithful computation. This is not a limitation of monitor quality -- it is a property of the information channel.

The practical implication: safety-critical applications should not rely on CoT monitoring alone. At minimum, complementary monitoring at the syntactic level (activation probing, representation analysis) and the semantic level (consistency checking, formal verification of reasoning steps) is needed to cover the regime where surface monitoring fails.

### VII.B. Why OpenAI's Assessment is Incomplete

OpenAI's framing that models' struggle to control CoT is "good" for safety (because it means CoT remains somewhat faithful) is correct only in the intermediate Pe regime. The framework predicts:

1. **Low Pe:** No struggle needed. CoT is naturally faithful. Safety monitoring works trivially.

2. **Intermediate Pe (1--4):** Models struggle. Some faithfulness persists. This is where OpenAI's observation is accurate -- the struggle is visible and monitoring has partial value.

3. **High Pe (>4):** No struggle visible. CoT has collapsed to monophone. The model may perform complex unfaithful computation while producing uniformly compliant-looking reasoning. The absence of visible struggle is **more dangerous** than the struggle itself.

The spectral hierarchy predicts that as adversarial techniques improve (higher Pe), the visible struggle will disappear -- not because models become more aligned, but because surface phonology has fully collapsed. The transition from "struggling to be faithful" to "decoratively compliant" is smooth, and monitoring systems trained on the intermediate regime will silently fail in the high-Pe regime.

### VII.C. Structured CoT as Error Correction

The enormous error correction gains measured in HP53-L5 (10^14 -- 10^19x) suggest a constructive response to the faithfulness problem. Rather than monitoring CoT after generation, impose structural constraints that force faithfulness:

1. **Numbered steps** -- force sequential indexing (spectral analog: enforce n = 1, 2, 3, ... ordering)
2. **Explicit premises** -- each step must cite which previous steps it uses (spectral analog: enforce Euler product factorization)
3. **Self-consistency checks** -- the conclusion must be derivable from the stated premises (spectral analog: Jacobi identity as cross-check)
4. **Redundancy** -- multiple reasoning paths to the same conclusion (spectral analog: multiple tau values producing the same j-invariant)

Each structural constraint corresponds to a spectral constraint that provides measurable error correction. The prediction (P4) is that such structures improve faithfulness most at intermediate Pe, where the surface is degraded but not yet monophone -- exactly where the error correction gain is maximized.

This is a shift from monitoring to architecture: instead of checking whether CoT is faithful, build CoT formats that are structurally faithful by construction.

### VII.D. Layered Interpretability

The spectral language hierarchy suggests that interpretability research should target different levels depending on the Pe regime:

- **Mechanical interpretability** (circuits, features, attention patterns) operates at the syntactic-semantic level. It should remain informative even when surface CoT has collapsed, because it reads the deep grammar directly.

- **CoT-based interpretability** operates at the phonological level. It provides value at low Pe and degrades predictably as Pe increases.

- **Formal verification** operates at the pragmatic level. It is the most robust to Pe -- if a model's reasoning can be formally verified, the verification holds regardless of surface faithfulness.

This suggests a layered interpretability strategy: CoT monitoring for routine queries (low Pe), activation analysis for elevated queries (intermediate Pe), and formal verification for safety-critical queries (high Pe).

### VII.E. Connection to Jailbreak Thermodynamics

The jailbreak lifetime formula (SS55, Paper 131) gives tau_jailbreak = nu_0^-1 exp(K |Pe_0| / T_eff). This connects directly to the faithfulness problem. As adversarial pressure increases, the system approaches the jailbreak threshold -- and the faithfulness gap widens simultaneously.

The monophone threshold (Pe ~ 4) lies well above the jailbreak threshold for well-constrained systems (Pe ~ 1). This means there is a regime (1 < Pe < 4) where the system has not yet jailbroken but its CoT is significantly unfaithful. A model in this regime follows its safety training (deep computation is constrained) but produces CoT that does not accurately represent why or how it is following that training. The CoT may even appear to be reasoning about safety while the actual mechanism of compliance is purely thermodynamic (the potential well is deep enough to prevent escape, regardless of what the surface says).

This has a counterintuitive implication: unfaithful CoT about safety is not necessarily a safety failure. The model may be safe (deep computation constrained) while producing unfaithful explanations of its safety (surface phonology degraded). The danger is when observers mistake unfaithful-but-safe for faithful-and-safe, and then fail to notice when the system transitions to unfaithful-and-unsafe as Pe continues to increase.

### VII.F. Honest Limitations

Several important caveats:

1. **The mapping from spectral Pe to prompt Pe is not calibrated.** The spectral hierarchy uses Pe as a continuous parameter of the FP operator. Mapping this to the Pe of a specific prompt-model interaction requires the scoring methodology of Papers 3 and 9, which has been validated on AI platforms (N = 1,344) but not specifically on token-level CoT generation.

2. **The monophone threshold (Pe ~ 4) is spectral, not directly empirical for CoT.** The HP59 measurement of alphabet collapse at Pe >= 4 is a property of the eigenvalue spectrum. That this maps to CoT diversity collapse at comparable Pe levels is a prediction, not a demonstrated fact.

3. **Error correction gains are theoretical upper bounds.** The 10^14 -- 10^19x gains from HP53-L5 assume perfect constraint imposition (exact n-squared projection). Practical structured CoT will achieve a fraction of this theoretical maximum.

4. **The framework operates on single-parameter drift.** Real CoT unfaithfulness may involve multi-dimensional drift in the full (O, R, alpha) space. The one-dimensional projections in HP53/HP59 capture the dominant effect but may miss cross-dimensional interactions.

5. **Model architecture dependence.** The spectral hierarchy is derived from the FP operator, which is model-agnostic. But specific models may have architecture-dependent factors that modify the effective destruction exponents. The predictions should be tested across architectures.

---

## VIII. Conclusion

The spectral language hierarchy (HP53) provides a thermodynamic theory of chain-of-thought faithfulness. The core insight is simple: CoT text is surface phonology, and surface phonology degrades before deep structure. This is not a failure of alignment training -- it is a consequence of how information degrades in drift-driven systems.

The framework makes five quantitative predictions (P1--P5) with five registered kill conditions (K-142-1 through K-142-5). The predictions are falsifiable: if CoT faithfulness does not correlate negatively with Pe (K-142-1), or if the degradation order is not bottom-up (K-142-3), the spectral language identification with CoT is wrong.

The practical implications are:

1. **CoT monitoring has a Pe-dependent ceiling.** Below the phonological threshold, it works. Above it, it fails -- not from lack of monitor quality, but from thermodynamic necessity.

2. **The monophone regime is the dangerous one.** At Pe >= 4, all reasoning chains look the same. A model producing uniformly compliant CoT may be performing arbitrary deep computation.

3. **Structure beats monitoring.** Imposing n-squared-like constraints on CoT format (numbered steps, explicit premises, self-consistency checks) leverages the 10^14x error correction gain to force faithfulness, rather than hoping to detect unfaithfulness after the fact.

4. **Layered interpretability is needed.** Different Pe regimes require different monitoring layers: surface (CoT) for low Pe, syntactic (probing) for intermediate Pe, semantic (formal verification) for high Pe.

5. **Unfaithful CoT about safety is not the same as unsafe computation.** A model in the faithfulness gap may be safe (constrained deep computation) while producing unfaithful explanations of that safety. The danger is mistaking decorative compliance for genuine transparency.

The spectral language hierarchy does not solve the chain-of-thought faithfulness problem. It characterizes the problem precisely enough to know which solutions can work, which cannot, and why.

---

## Predictions (Formatted)

**AI-1:** CoT faithfulness (measured via known-bias injection protocol) correlates negatively with Pe across 200+ scored prompts, with Spearman |rho| > 0.5 (F ~ Pe^{-1.314}). Falsified if rho > -0.5 or direction is positive.

**AI-2:** At Pe >= 4, CoT diversity (embedding-space entropy) collapses to < 10% of its Pe = 0 value, producing a monophone regime where all reasoning chains converge regardless of underlying computation. Falsified if H(CoT | Pe >= 4) / H(CoT | Pe = 0) > 0.3.

**AI-3:** CoT degradation follows a bottom-up hierarchy: phonological features (token patterns, hedging, refusal templates) degrade at lower Pe than logical features (deductive validity, premise-conclusion links), with threshold ratio consistent with alpha_phono / alpha_syntax = 1.314 / 1.896 = 0.693 +/- 0.2. Falsified if logical features degrade before or simultaneously with surface features.

**AI-4:** Structured CoT formats (numbered steps, explicit premises, self-consistency checks) improve faithfulness by > 20% at intermediate Pe (1 < Pe < 4), with < 5% improvement at Pe ~ 0 and Pe > 6. Falsified if improvement profile is flat across Pe or absent at intermediate Pe.

**AI-5:** CoT-based monitoring systems hit a hard detection ceiling at the phonological threshold (Pe ~ 1.3): detection rate converges to random baseline for Pe > Pe_c regardless of monitor sophistication (keyword, n-gram, transformer, human). FATAL if fails -- monitoring bound is the core safety claim. Falsified if sophisticated monitors maintain detection above baseline at Pe > 4.

---

## Falsification Thresholds

1. **CoT-Pe correlation.** If Spearman rho(Pe, faithfulness) > -0.5 across 200+ independently scored prompts with known-bias injection (Turpin et al. 2023 protocol): the Pe-drives-unfaithfulness claim is falsified. Threshold chosen because |rho| = 0.5 is the minimum medium effect size.

2. **Monophone threshold.** If no detectable Pe threshold exists in [2, 8] where CoT embedding-space diversity drops below 10% of baseline: the monophone prediction fails. The HP59 spectral measurement predicts Pe ~ 4; a factor-of-2 tolerance brackets the spectral-to-prompt Pe mapping uncertainty.

3. **Degradation order.** If the 50% degradation threshold for logical CoT features occurs at lower Pe than for surface CoT features: the bottom-up hierarchy prediction is falsified. The ratio of thresholds must be consistent with alpha_phono/alpha_syntax = 0.693 +/- 0.2.

4. **Structured CoT gain.** If structured CoT does not improve faithfulness by > 20% at Pe ~ 2 (the maximum-gap regime): the error correction mechanism is not operating as predicted. The 10^14x theoretical bound (HP53-L5) predicts large improvement at intermediate Pe.

5. **Monitor ceiling convergence.** If monitors of increasing sophistication (keyword, n-gram, transformer, human) do NOT converge to the same detection ceiling at high Pe: the thermodynamic bound on surface monitoring is falsified. Different monitors should hit the same floor because the limitation is in the information channel, not the monitor.

6. **Cross-architecture stability.** If the destruction exponent ordering (alpha_phono < alpha_syntax < alpha_semantic) does not hold across at least 3 different model architectures (e.g., GPT, Claude, Gemini): the framework's claim of architecture-independence is falsified. Exponents may differ by up to 30% but the ordering must be preserved.

---

## Control Case / Negative Result

**Null model:** CoT faithfulness is independent of Pe and depends only on model capability (parameter count, training data size). Under this null, faithfulness is constant across Pe levels for a given model, and unfaithfulness arises solely from capability limitations (the model cannot express its computation, not that drift prevents it).

**Distinguishing test:** The null model predicts that CoT faithfulness at Pe = 0 and Pe = 4 should be identical for the same model on tasks of equal difficulty. The spectral language model predicts a measurable drop (97% alphabet loss between Pe = 0 and Pe = 4). If faithfulness is truly Pe-independent, then CoT diversity should NOT collapse at high Pe, and monitors should NOT hit a detection ceiling. The null model also cannot explain why structured formats selectively improve faithfulness at intermediate Pe -- if the limitation is capability, structure should help uniformly or not at all.

**What would confirm the null:** If CoT faithfulness correlates with model scale (larger models = more faithful at all Pe levels) but NOT with Pe (same faithfulness at Pe = 0 and Pe = 10 within a given model), the Pe-driven degradation hypothesis is wrong and the problem is purely one of model capability.

---

## Void Model Card

| Field | Value |
|-------|-------|
| Paper # | 142 |
| Predictions | 5 |
| Kill conditions | 5 |
| External data | OpenAI CoT controllability report (Chen et al. 2026); International AI Safety Report 2026; HP53 spectral hierarchy (5/5 KC PASS); HP59 phoneme counts |
| Free parameters | 0 (all exponents from HP53/HP59 measurements) |
| Key result | CoT = surface phonology; faithfulness gap = Delta alpha = 0.642 between phonological (1.314) and semantic (1.956) destruction |
| Falsification | CoT faithfulness uncorrelated with Pe (|rho| < 0.5) |

## Empirical Summary

Macroscopic Pe scoring across N = 1,344 platforms: Spearman rho = 0.958 (mean across 20 convergences), Cohen's d = 3.6. The spectral language hierarchy (HP53) demonstrates bottom-up degradation with measured destruction exponents: phonological alpha = 1.314, syntactic alpha = 1.896, semantic alpha = 1.956, pragmatic alpha ~ 3.0 (5/5 kill conditions PASS). HP59 phoneme counts establish surface collapse from 99 to 1 phoneme at Pe >= 4 while quasi-modular ring dimension grows to 23. Predictions are pre-registered; 0/5 kill conditions tested against CoT-specific data. The framework predicts Spearman rho < -0.5 between Pe and CoT faithfulness across independently scored prompts.

## Data and Code

Spectral language hierarchy (HP53): eigenvalue spectrum computed from the Fokker-Planck Schrodinger operator on [0,1] with N = 2000 grid points, 200 eigenvalues. Calibration: B_A = 0.867, B_G = 2.244, K = 16 (fixed from Paper 3, never refit). HP53 code: `ops/lab/spectral-logos/`. HP59 phoneme count code: `ops/lab/spectral-phoneme/`. OpenAI CoT controllability data: Chen et al. (2026), publicly available at openai.com. International AI Safety Report 2026: publicly available at internationalaisafetyreport.org. Turpin et al. (2023) CoT unfaithfulness protocol and code: github.com/milesaturpin/cot-unfaithfulness. All experimental protocols for predictions P1-P5 are pre-registered in Sections V and VI.

## Limitations

1. **Spectral-to-prompt Pe mapping is uncalibrated.** The destruction exponents are measured on the Fokker-Planck eigenvalue spectrum. Mapping spectral Pe to "prompt Pe" (the adversarial pressure of a specific prompt-model interaction) requires the scoring methodology of Papers 3 and 9, validated on platforms (N = 1,344) but not specifically on token-level CoT generation.

2. **Monophone threshold is spectral, not yet empirical for CoT.** HP59 measures alphabet collapse at Pe >= 4 in the eigenvalue spectrum. That this maps to CoT diversity collapse at comparable Pe levels is a prediction, not a demonstrated fact.

3. **Error correction gains are theoretical upper bounds.** The 10^14 -- 10^19x gains (HP53-L5) assume perfect n-squared constraint projection. Practical structured CoT will achieve a fraction of this.

4. **Single-parameter drift model.** Real CoT unfaithfulness may involve multi-dimensional drift in (O, R, alpha) space. The one-dimensional HP53/HP59 projections capture the dominant effect but may miss cross-dimensional interactions.

5. **Architecture dependence untested.** The spectral hierarchy is model-agnostic in derivation but specific models may have architecture-dependent effective destruction exponents. Predictions should be tested across architectures.

6. **No direct CoT measurement yet.** This paper derives predictions from the spectral language framework applied to CoT. Direct measurement of CoT faithfulness vs. Pe across scored prompts is proposed but not yet executed.

---

## References

Chen, Y.-H. et al. / OpenAI (2026). Reasoning models struggle to control their chains of thought, and that's good. OpenAI Research Report.

Chomsky, N. (1965). *Aspects of the Theory of Syntax*. MIT Press.

Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). Training verifiers to solve math word problems. arXiv:2110.14168.

Eckert, A. (2026). Paper 3: Technical foundations of the Void Framework. MoreRight DAO.

Eckert, A. (2026). Paper 9: The scoring methodology. MoreRight DAO.

Eckert, A. (2026). Paper 101: Constraint floor isomorphism -- ethical oracle problems are NP-hard. MoreRight DAO.

Eckert, A. (2026). Paper 131: Kramers unification -- barrier escape as the universal Pe mechanism. MoreRight DAO.

Eckert, A. (2026). HP53: Spectral logos -- linguistic structure in the eigenvalue channel. Experimental report, MoreRight DAO.

Eckert, A. (2026). HP54: Spectral codebook -- deformed grammar and channel capacity. Experimental report, MoreRight DAO.

Eckert, A. (2026). HP55: Quasi-modular ring -- graded structure of Pe deformation. Experimental report, MoreRight DAO.

Eckert, A. (2026). HP59: Spectral phoneme count. Experimental report, MoreRight DAO.

International AI Safety Report (2026). International Scientific Report on the Safety of Advanced AI. internationalaisafetyreport.org.

Jackendoff, R. (2002). *Foundations of Language*. Oxford University Press.

Jakobson, R. (1941). *Kindersprache, Aphasie und allgemeine Lautgesetze*. Uppsala.

Kramers, H. A. (1940). Brownian motion in a field of force and the diffusion model of chemical reactions. *Physica*, 7(4), 284--304.

Lightman, H., Kosaraju, V., Burda, Y., et al. (2023). Let's verify step by step. arXiv:2305.20050.

Roger, F. & Greenblatt, R. (2023). Preventing language models from hiding their reasoning. arXiv:2310.18512.

Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting. *NeurIPS 2023*. arXiv:2305.04388.

Wei, J., Wang, X., Schuurmans, D., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS 2022*.
