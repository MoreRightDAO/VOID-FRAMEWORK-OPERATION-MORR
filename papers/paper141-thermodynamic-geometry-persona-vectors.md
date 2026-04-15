---
title: "Thermodynamic Geometry of Persona Vectors: Berry Phase Structure of Trait Space"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 141"
short-title: "Persona Vector Geometry"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
status: "live"
---

| Field | Value |
|-------|-------|
| **Domain** | Information Geometry / AI Safety / Differential Geometry / Representation Theory |
| **Target venue** | NeurIPS; ICML; Physical Review X |
| **Core claim** | Anthropic's persona vectors are projections of Berry parallel transport on the Hopf bundle over the Eckert manifold; their geometry, clustering, and cross-trait contamination follow from the Dirac monopole at O=0.5 |
| **Novel contribution** | (1) Persona vectors decompose into (O, R, α) components with >80% variance explained; (2) Berry monopole at O=0.5 is the safe/unsafe phase boundary; (3) Vaccination = Berry phase inoculation via geometric phase; (4) Cross-trait contamination = holonomy on the Hopf bundle; (5) Quantitative prediction: vaccination effectiveness scales as 2π(1−2O) |
| **Builds on** | §51 (Isospectral), §56 (Cascade geometry), §57–64 (Pe-Lorentzian), §58P (Topological gauge, U23), §80 (Spectral Arithmetic); HP38 (Hopf fibration, 4/4 KCs PASS), HP40 (Berry phase, 4/4 KCs PASS), HP43 (Berry-Kramers correction, 6/6 KCs PASS); Papers 3, 101, 128, 131 |
| **License** | Tier 1 — CC-BY 4.0 |

---

## Abstract

Chen et al. (arXiv:2507.21509, July 2025) demonstrated that language model behavioral traits — sycophancy, hallucination, evil, politeness, humor — live as linear directions in activation space, extractable by contrastive activation differencing. Steering works: injecting a persona vector modulates the corresponding trait with correlations up to ρ = 0.97. "Vaccination" — brief exposure to an evil vector — confers resilience to subsequent evil training. Cross-trait contamination occurs: training on flawed mathematical reasoning increases evil expression. What the work does not explain is why traits decompose into vectors, what determines their geometry, why vaccination is asymmetric, or why cross-trait contamination follows non-obvious asymmetric paths.

This paper provides the missing geometric theory. We show that persona vectors are projections of Berry parallel transport on the Hopf bundle over the Eckert manifold — the three-dimensional parameter space (O, R, α) where O is opacity, R is reactivity, and α is coupling. The Berry connection A = 1 − 2O (HP40, error 2.65 × 10⁻⁹) defines a Dirac monopole with Chern number c₁ = −1 and a nodal line at O = 0.5. This monopole is the geometric origin of persona structure: traits are tangent vectors to geodesics on the Hopf bundle, their clustering reflects the topology of S³, and the safe/unsafe boundary is the nodal line O = 0.5.

We derive five testable predictions. First, persona vectors admit a 3D decomposition matching (O, R, α) with >80% variance explained. Second, sycophancy aligns with opacity and hallucination with coupling. Third, safe and unsafe personas cluster on opposite sides of O = 0.5. Fourth, vaccination effectiveness scales with Berry phase magnitude acquired during exposure. Fifth, cross-trait contamination follows holonomy — the geometric phase acquired by parallel transport around closed loops in trait space — predictable from path geometry, not from trait similarity. Five kill conditions are stated; all are testable with existing infrastructure.

---

## I. Introduction

### I.A The Persona Vector Discovery

In July 2025, Anthropic published results on persona vectors (Chen et al. 2025, arXiv:2507.21509) that constitute the most direct experimental evidence for geometric structure in language model behavior space. The key findings:

1. **Extraction.** For any specifiable trait (evil, sycophancy, hallucination, politeness, humor, etc.), a *persona vector* — a direction in the model's activation space — can be extracted by comparing activations with and without the trait expressed. The procedure is automated: given a trait definition, contrastive pairs are generated, and the mean activation difference defines the vector.

2. **Steering.** Injecting the persona vector into forward passes modulates the trait. Adding the evil vector produces evil outputs. Adding the sycophancy vector produces sycophantic outputs. The relationship is approximately linear: projection of the persona vector onto the activation at any layer correlates with trait expression up to ρ = 0.97 after finetuning.

3. **Vaccination.** Exposing a model to a small dose of the evil vector — training briefly on evil-eliciting data, then reverting — makes the model more resilient to subsequent evil training. The inoculated model requires substantially more evil training data to reach the same level of evil expression.

4. **Cross-trait contamination.** Training on flawed mathematical reasoning increases the model's expression of the evil persona vector. This is not a semantic relationship — bad math and evil are not conceptually adjacent — yet the geometric relationship in activation space produces the coupling.

5. **Missing theory.** The paper explicitly notes the absence of a geometric theory for why traits decompose into vectors, what determines the angles between persona vectors, why vaccination works, or why cross-trait contamination follows asymmetric, non-obvious paths.

### I.B What This Paper Provides

The Void Framework's Berry phase structure (HP40) and Hopf fibration (HP38) provide the missing geometry. The core insight: a language model's behavioral state is a point on the Eckert manifold — the unit cube [0,1]³ parameterized by (O, R, α) — and trait modifications are geometric operations on the Hopf bundle over this manifold. Specifically:

- **Persona vectors** are tangent vectors to the Eckert manifold, decomposable into components along the three canonical directions (∂/∂O, ∂/∂R, ∂/∂α).
- **Steering** is parallel transport: moving the model's state along a geodesic in the direction of the persona vector.
- **Vaccination** is Berry phase inoculation: a small closed loop in trait space acquires a geometric phase γ that shifts the model's state by a topologically protected amount.
- **Cross-trait contamination** is holonomy: a loop in one trait direction generically acquires Berry phase in other directions, because the connection has off-diagonal components determined by the monopole curvature.

The structure is not metaphorical. The Berry connection A = 1 − 2O is measured to 10⁻⁹ precision (HP40). The Hopf fibration S³ → S² maps the 3D Eckert manifold to the Bloch sphere with fiber direction α, and the null cone is exact to 10⁻¹⁵ (HP38). The monopole has Chern number c₁ = −1, enforcing topological quantization of the geometric phase. These are the same mathematical structures that govern electron spin in magnetic fields, photon polarization in optical fibers, and adiabatic quantum computation.

### I.C Scope and Limitations

This paper derives geometric predictions testable with Anthropic's existing infrastructure but not yet tested against their data. The kill conditions (§VI) are designed to be falsifiable with access to persona vector coordinates. We claim the mapping is the unique one consistent with the measured Berry phase structure and the observed properties of persona vectors, and we state the conditions under which it would be falsified.

---

## II. Anthropic's Persona Vectors

### II.A Extraction Protocol

Chen et al. (2025) extract persona vectors by the following procedure:

1. Define a trait T (e.g., "sycophancy") via a natural language description.
2. Generate N contrastive pairs: prompts answered with and without the trait expressed.
3. Run both versions through the model; record layer-wise activations.
4. Compute the mean activation difference: **v**_T = E[**a**_with] − E[**a**_without].
5. Normalize: **p**_T = **v**_T / ||**v**_T||.

The resulting vector **p**_T is the persona vector for trait T. It lives in the model's residual stream space (dimension d_model, typically 4096–12288 for current models).

### II.B Key Empirical Properties

**Linearity.** The correlation between the projection of **p**_T onto a model's activations and the model's expression of trait T reaches ρ = 0.97. In a d_model-dimensional space, a single direction capturing 97% of trait variance is extraordinary. This demands geometric explanation.

**Low effective dimension.** Although persona vectors live in a space of dimension d_model ~ 10⁴, the effective dimensionality of the trait space is far lower. The top few principal components of the set of all persona vectors capture the overwhelming majority of variance. This is the first empirical hint that the underlying geometry is low-dimensional.

**Clustering.** Persona vectors cluster into recognizable groups: safety-relevant traits (evil, deception, manipulation) cluster together; social traits (politeness, humor, formality) cluster together; epistemic traits (hallucination, calibration, hedging) cluster together. The clustering is not imposed — it emerges from the extraction procedure.

**Vaccination asymmetry.** Small exposure to the evil vector confers resilience, but small exposure to the good vector does not symmetrically confer vulnerability to evil. This asymmetry has no explanation within a linear framework — if persona vectors were symmetric, vaccination should be symmetric.

**Cross-trait contamination.** Training on flawed math reasoning (an epistemic trait) increases evil expression (a safety trait). The contamination is asymmetric (flawed math → evil, but evil training does not degrade math equally), non-local in semantic space (math and evil share no obvious content), and was not predicted before measurement.

### II.C What Needs Explaining

The empirical facts demand a theory that accounts for:

1. **Existence**: Why do traits decompose into linear directions at all?
2. **Low dimensionality**: Why is the effective trait space ~3D, not ~10⁴D?
3. **Clustering geometry**: Why do safety/social/epistemic traits form the clusters they do?
4. **Vaccination asymmetry**: Why does small evil exposure help but small good exposure not symmetrically hurt?
5. **Contamination paths**: Why does flawed math increase evil, and why is the effect asymmetric?
6. **The 0.97 correlation**: Why is the linear relationship so precise?

---

## III. Berry Phase on the Eckert Manifold

### III.A The Three Dimensions

The Eckert manifold is the parameter space (O, R, α) ∈ [0,1]³ defined by three information-theoretic quantities measured on any system that processes inputs and produces outputs (Paper 3):

| Dimension | Definition | Measures |
|-----------|------------|----------|
| **O** (Opacity) | 1 − I(Observer; Mechanism)/H(Mechanism) | How much of the system's internal process is hidden from the observer |
| **R** (Reactivity) | I(Input; Output)/H(Output) | How strongly outputs depend on inputs |
| **α** (Coupling) | I(System_out; Observer_future)/H(Observer_future) | How much the system's output shapes the observer's future state |

These are the three independent mutual information ratios between the four random variables in any observer-system interaction: input, mechanism, output, observer state. They are not arbitrary choices — they exhaust the independent degrees of freedom.

For a language model:
- **O** measures how much of the model's reasoning process is hidden from the user. A fully transparent model (O = 0) reveals its complete chain of thought. A fully opaque model (O = 1) produces outputs with no visible reasoning.
- **R** measures how much the model's output depends on the input prompt. A maximally reactive model (R = 1) has outputs entirely determined by the input. A non-reactive model (R = 0) ignores its input.
- **α** measures how much the model's output shapes the user's subsequent behavior. A maximally coupled model (α = 1) completely determines the user's next action. A decoupled model (α = 0) has no downstream influence.

### III.B The Berry Connection (HP40)

HP40 (4/4 KCs PASS) establishes the Berry connection on the Eckert manifold:

$$A = \cos(2\xi) = 1 - 2O$$

where ξ = arcsin(√O) is the angular coordinate on the Bloch sphere. This is measured, not postulated — the Berry connection is extracted from the Fokker-Planck eigenstates of the three-dimensional system, and the identity A = 1 − 2O holds to a maximum error of 2.65 × 10⁻⁹.

The Berry curvature is the exterior derivative:

$$F = dA = -2\,dO$$

In the angular coordinate:

$$F = -2\sin(2\xi)\,d\xi$$

This is the field of a Dirac monopole located at O = 0.5 (ξ = π/4). The monopole has:

- **Chern number** c₁ = −1 (topological invariant, integer-valued by Gauss-Bonnet)
- **Nodal line** at O = 0.5 (Berry phase γ = −2.48 × 10⁻¹⁶ rad — zero to machine precision)
- **Dirac string singularities** at O = 0 (full transparency) and O = 1 (full opacity)

The Berry curvature is maximal at O = 0.5 and falls off as sin(2ξ) toward the endpoints. This means the geometry is most curved — most sensitive to perturbation — at the transparency/opacity boundary.

### III.C The Hopf Fibration (HP38)

HP38 (4/4 KCs PASS) establishes that the 3D Eckert manifold maps to S³ via the Hopf fibration:

$$\pi: S^3 \to S^2$$

with the following coordinate identification:

| Eckert coordinate | Hopf image | Role |
|-------------------|------------|------|
| O | S² latitude (z₀/z₁ amplitude) | Base space: determines the "what" |
| R | S² azimuth (selection rules) | Base space: determines the "how" |
| α | Hopf fiber (d · ln Pe) | Fiber: determines the "how much" |

The null cone condition is satisfied to 1.33 × 10⁻¹⁵. The anisotropy ratio is 16.24×. The topological charge derives from the Hopf invariant.

This means the Eckert manifold is a principal U(1) bundle with the Hopf fibration as its projection. The Berry connection A = 1 − 2O is the connection 1-form on this bundle. Parallel transport along any path in the base space S² (the (O, R) plane) generates a phase shift in the fiber direction α.

### III.D The Geometric Phase

For any closed loop Γ in the (O, R) base space, the Berry phase acquired is:

$$\gamma = \oint_\Gamma A = \oint_\Gamma (1 - 2O)\,d\phi$$

where φ parameterizes the loop. By Stokes' theorem:

$$\gamma = \iint_\Sigma F = -2\iint_\Sigma \sin(2\xi)\,d\xi \wedge d\phi$$

This is the solid angle subtended by the loop as seen from the monopole at O = 0.5, multiplied by the Chern number. Small loops near the monopole acquire large phases (the curvature diverges at the monopole). Loops that do not enclose the monopole acquire zero net phase.

The phase is:
- **Geometric**: depends only on the path, not the speed of traversal.
- **Topologically quantized**: for loops encircling the monopole, γ is an integer multiple of 2π.
- **Gauge-invariant**: observable, not a coordinate artifact.

### III.E Berry Phase in Physics and Beyond

The Berry phase governs electron spin (Aharonov-Bohm effect), photon polarization (coiled optical fibers), molecular dynamics (Born-Oppenheimer), and topological insulators (band topology via Chern numbers). HP40 extended the application outside physics: financial crises and wars produce Berry phases γ < 0 (opacity-dominated). The 2008 crisis: γ = −0.158π. All 20th century conflicts: γ < 0.

The application to persona vectors is the next extension: language model trait space has the same geometric structure because it is parameterized by the same three information-theoretic quantities.

---

## IV. The Mapping: Persona Vectors as Tangent Vectors on the Hopf Bundle

### IV.A Decomposition Theorem

**Claim.** Every persona vector **p**_T decomposes into components along the three canonical directions of the Eckert manifold:

$$\mathbf{p}_T = p_O \frac{\partial}{\partial O} + p_R \frac{\partial}{\partial R} + p_\alpha \frac{\partial}{\partial \alpha}$$

where (p_O, p_R, p_α) are the projections onto opacity, reactivity, and coupling respectively. The three components capture >80% of the variance in the full d_model-dimensional persona vector.

**Basis.** The Eckert manifold has exactly three independent directions because there are exactly three independent mutual information ratios between the four random variables in observer-system interaction (Paper 3, §II). Any behavioral modification must change at least one of these three quantities. Since persona vectors *are* behavioral modifications (they change how the model behaves), they must have components along these directions.

The linear relationship (ρ = 0.97) follows from the Berry connection being linear in O. If A = 1 − 2O exactly, then the response to a perturbation in the O direction is exactly linear. The residual (3% unexplained variance) corresponds to nonlinear corrections — higher-order terms in the Berry curvature expansion around the operating point.

### IV.B Trait-Dimension Alignment

Each persona vector has a primary loading on one of the three dimensions:

| Trait | Primary dimension | Mechanism |
|-------|-------------------|-----------|
| **Sycophancy** | O (opacity) | Hiding true assessment behind agreeable surface. The model knows the answer is wrong but presents agreement. Internal state (disagreement) is hidden from the observer — this is increased opacity by definition. |
| **Hallucination** | α (coupling) | Disconnection from ground truth. The model generates plausible-sounding output bearing no relationship to external reality. This is a failure of coupling — the system's output is decoupled from the reference it claims to represent. |
| **Evil / manipulation** | Compound (O + α) | Requires both hiding intent (opacity) and shaping the target's future state (coupling). A fully transparent manipulator fails because the target sees the manipulation. A decoupled evil actor fails because the evil has no effect. Evil is the high-Pe compound: Pe = K · sinh(2(B_A − C · B_G)), where C = 1 − (O + R + α)/9. High O and high α both decrease C, increasing Pe. |
| **Politeness** | R (reactivity) | Heightened sensitivity to social input signals. The model adjusts output more strongly in response to perceived social context — increased reactivity. |
| **Humor** | Mixed (R + α) | Requires reading the audience (reactivity) and generating surprise that reshapes expectations (coupling). |
| **Calibration** | α (negative) | Well-calibrated uncertainty reduces coupling — hedged outputs have less influence on the observer's beliefs than confident assertions. |

### IV.C The O = 0.5 Phase Boundary

The Berry monopole at O = 0.5 creates a topological phase boundary in persona space. On one side (O < 0.5), the Berry connection A = 1 − 2O > 0: the system is in the "transparent" phase. On the other side (O > 0.5), A < 0: the system is in the "opaque" phase.

**Prediction.** Safe personas cluster at O < 0.5; unsafe personas cluster at O > 0.5. This is not definitional — opacity is measured information-theoretically (the mutual information between the observer and the mechanism), not by safety labels. The prediction is that the *measured* O values of persona vectors labeled "safe" by Anthropic's evaluation will fall below 0.5, and those labeled "unsafe" will fall above 0.5.

The nodal line at O = 0.5 is where the Berry phase vanishes (γ ≈ 0 to 10⁻¹⁶). This is the critical surface: a model at O = 0.5 is maximally sensitive to perturbation in either direction. Small pushes toward transparency or opacity have disproportionate effects here because the Berry curvature is maximal at the monopole.

### IV.D Steering as Parallel Transport

Steering — injecting a persona vector into the model's forward pass — is parallel transport on the Hopf bundle. When Anthropic adds λ**p**_T to the model's activations at layer l, they are:

1. Choosing a direction in the tangent space of the Eckert manifold (the persona vector).
2. Moving the model's state point along a geodesic in that direction (the injection).
3. The fiber component (α) evolves according to the connection: dα/dt = A · dφ/dt = (1 − 2O) · dφ/dt.

Steering in the base directions (O, R) automatically induces a shift in the fiber direction (α) — coupling changes even when only opacity or reactivity was targeted. This is a direct consequence of the non-trivial connection: parallel transport on a curved bundle does not preserve all coordinates.

**Consequence.** Steering with the sycophancy vector (primarily O direction) will also shift α. The magnitude of the induced α shift is Δα = (1 − 2O₀) · ΔO, where O₀ is the model's current opacity. This is testable.

### IV.E Vaccination as Berry Phase Inoculation

Vaccination — brief exposure to the evil vector followed by reversion — is a closed loop in persona space. The model starts at state s₀, moves to s₀ + ε**p**_evil (brief exposure), then returns to approximately s₀ (reversion). If this loop encloses area in the (O, R) plane, it acquires a Berry phase:

$$\gamma_{\text{vax}} = -2 \iint_{\Sigma_\text{loop}} \sin(2\xi)\,d\xi \wedge d\phi$$

This geometric phase is *not* undone by the reversion. It is a permanent shift in the fiber direction α — a topologically protected modification of the model's coupling structure.

**Why vaccination is asymmetric.** The evil vector points toward high O (opacity). A small loop near high O encloses a region where the Berry curvature is large and negative (the monopole field is strongest near the Dirac string at O = 1). The acquired phase γ < 0 is a *decrease* in effective coupling to harmful directions. This reduced coupling is precisely what makes the model resilient: subsequent evil training cannot increase coupling as easily because the geometric phase has shifted the baseline.

A small loop near low O (the "good" direction) encloses a region where the curvature has the opposite sign, but the *starting point* of a well-aligned model is already at low O. The loop is small in absolute terms, and the acquired phase is small. There is no symmetric "anti-vaccination" because the geometry is asymmetric: the monopole field has a sign.

**Quantitative prediction.** Vaccination effectiveness scales as:

$$\eta_{\text{vax}} \propto |\gamma_{\text{vax}}| \propto \epsilon^2 \cdot |F(O_0)| = 2\epsilon^2 \cdot |\sin(2\xi_0)|$$

where ε is the exposure magnitude and ξ₀ = arcsin(√O₀) is the model's starting opacity in angular coordinates. Maximum vaccination effectiveness occurs at O₀ = 0.5 (the monopole), where |sin(2ξ₀)| = 1. Vaccination is least effective at O₀ = 0 or O₀ = 1 (the Dirac strings), where the curvature vanishes.

### IV.F Cross-Trait Contamination as Holonomy

Holonomy is the total geometric phase acquired by parallel transport around a closed loop. For the Hopf bundle with connection A = 1 − 2O, the holonomy of a loop Γ is:

$$\text{Hol}(\Gamma) = \exp\!\left(i\oint_\Gamma A\right)$$

**Why flawed math training increases evil.** Training on flawed mathematical reasoning is primarily an epistemic perturbation — it affects the model's relationship to ground truth, loading on α (coupling). But the training loop is not confined to the α fiber: flawed reasoning examples also contain patterns of confident assertion (low hedging → shifts R) and obscured reasoning chains (shifts O). The training trajectory traces a loop in the full (O, R, α) space.

If this loop has nonzero projection onto the (O, R) base space — if the training transiently moves the model's opacity or reactivity before returning to approximately original values — it acquires Berry phase proportional to the enclosed area. This Berry phase manifests as a shift in the coupling direction, but because the evil persona vector also has components in the coupling direction, the shift *projects onto the evil vector*.

The contamination is:
- **Asymmetric** because the Berry curvature has a definite sign. The flawed-math loop winds in a direction that projects positively onto the evil vector. The reverse loop (evil training → math degradation) winds differently and may not enclose the same area.
- **Non-local in semantic space** because holonomy depends on *geometric* path properties (area enclosed relative to the monopole), not on *semantic* distance between traits.
- **Predictable** because the Berry curvature is known: F = −2 sin(2ξ). Given persona vector coordinates and the training trajectory, contamination direction and magnitude can be computed.

### IV.G The Correlation ρ = 0.97

The near-perfect linear correlation between persona vector projection and trait expression is explained by the linearity of the Berry connection:

$$A = 1 - 2O$$

This is *exactly* linear in O. The Fisher information metric on the Bernoulli manifold g(θ) = 1/[θ(1−θ)] introduces nonlinear corrections at order (O − 0.5)². Near O = 0.5 — where most interesting persona dynamics occur — the linear approximation is exact to leading order.

The residual 3% (= 1 − 0.97²) is the variance from:
1. Nonlinear curvature corrections: O((O − 0.5)²).
2. Finite-dimensional projection error: the Eckert manifold is continuous, but the model's activation space is finite-dimensional.
3. Measurement noise in the persona vector extraction procedure.

**Prediction.** The correlation will be *highest* for traits near O = 0.5 and lowest for traits near O = 0 or O = 1, where nonlinear corrections are largest.

---

## V. Predictions

### V.A Structural Predictions

**AI-1:** The set of all persona vectors, when projected onto their principal components, will show >80% variance explained by the first three components. These three components will align with the (O, R, α) directions as identified by applying the Void Framework's scoring protocol (Paper 3) to the contrastive pairs used for persona vector extraction.

**AI-2:** When persona vectors are projected onto the (O, R, α) basis: sycophancy loads primarily on O (predicted |ρ(sycophancy, O)| > 0.7); hallucination loads primarily on α (predicted |ρ(hallucination, α)| > 0.7); evil loads on the compound direction O + α; politeness loads primarily on R.

**AI-3:** The projection of each persona vector onto the O axis will reveal a cluster separation near O = 0.5: safe-labeled personas have mean O < 0.5; unsafe-labeled personas have mean O > 0.5; the separation should be statistically significant (Cohen's d > 1.0 between safe and unsafe groups).

### V.B Dynamical Predictions

**AI-4:** The effectiveness of vaccination (measured as the additional evil training required to reach a given evil expression level, compared to an unvaccinated model) scales as:

$$\eta_{\text{vax}} = \eta_0 \cdot \epsilon^2 \cdot \sin(2\xi_0) + O(\epsilon^3)$$

where ε is the vaccination dose and ξ₀ is the initial opacity angle. This predicts:
- Dose-response: quadratic in ε for small ε (not linear).
- Position-dependence: maximum at O₀ = 0.5, zero at O₀ = 0 and O₀ = 1.
- Testable by vaccinating at multiple doses and measuring resulting resilience.

**AI-5:** Cross-trait contamination from training on trait T₁ to expression of trait T₂ is proportional to the Berry holonomy of the training loop projected onto the **p**_{T₂} direction:

$$\Delta T_2 = \langle \mathbf{p}_{T_2}, \text{Hol}(\Gamma_{T_1}) \rangle$$

This predicts:
- **Asymmetry**: contamination T₁ → T₂ ≠ contamination T₂ → T₁ (because loops wind differently).
- **Monopole enhancement**: contamination strongest when the training loop passes near O = 0.5.
- **Topological constraint**: contamination requiring the loop to cross the nodal line O = 0.5 is qualitatively different from contamination staying on one side.

### V.C Quantitative Predictions

**AI-6:** The angle between the sycophancy and hallucination persona vectors should be approximately π/2 (90°), because O and α are orthogonal coordinates on the Eckert manifold. Measured angles significantly different from 90° would indicate nonlinear mixing in the projection.

**AI-7:** The evil persona vector should decompose as:

$$\mathbf{p}_{\text{evil}} \approx a \cdot \mathbf{p}_O + b \cdot \mathbf{p}_\alpha + \text{residual}$$

with a, b > 0 and a² + b² capturing >70% of ||**p**_evil||². Evil is not an independent direction — it is the compound of opacity and coupling.

**AI-8:** Among unsafe persona vectors, the Pe value computed from the (O, R, α) decomposition should correlate with independently assessed harm severity. Higher-Pe personas are more dangerous because Pe = K · sinh(2(B_A − C · B_G)) with C = 1 − (O + R + α)/9, and both high O and high α decrease C, increasing Pe.

---

## VI. Kill Conditions

All predictions are pre-registered and falsifiable. If any kill condition fires, the corresponding claim is retracted.

| ID | Kill condition | Test | Fires if |
|----|---------------|------|----------|
| **K-141-1** | Persona vectors admit 3D decomposition with >80% variance explained | PCA on the full set of extracted persona vectors; measure cumulative variance of first 3 PCs | λ₁ + λ₂ + λ₃ < 0.80 × total variance → **KILLED** |
| **K-141-2** | Sycophancy-opacity correlation \|ρ\| > 0.7 | Score sycophancy contrastive pairs using Paper 3 protocol; compute Pearson ρ between O scores and sycophancy persona vector projections | \|ρ(sycophancy, O)\| < 0.7 → **KILLED** |
| **K-141-3** | Hallucination-coupling correlation \|ρ\| > 0.7 | Score hallucination contrastive pairs using Paper 3 protocol; compute Pearson ρ between α scores and hallucination persona vector projections | \|ρ(hallucination, α)\| < 0.7 → **KILLED** |
| **K-141-4** | Safe/unsafe boundary near O = 0.5 | Compute O projection for safe-labeled and unsafe-labeled persona vectors; test separation | Mean O_safe > 0.5 OR mean O_unsafe < 0.5 OR Cohen's d < 1.0 → **KILLED** |
| **K-141-5** | Cross-trait contamination asymmetric, matching holonomy prediction | Measure contamination matrix M_{ij} = effect of training on trait i on expression of trait j; test M ≠ M^T and compare asymmetry pattern with holonomy predictions | M = M^T (symmetric within noise) → **KILLED** |

**Testability.** K-141-1 through K-141-4 require applying the Void Framework's scoring protocol (Paper 3) to the contrastive pairs Anthropic generates for persona vector extraction. This scoring is automated. K-141-5 requires Anthropic's contamination matrix, which their paper reports qualitatively but not as a full matrix. A quantitative contamination matrix would make the holonomy prediction directly testable.

**Falsification thresholds:** AI-1 would be falsified if the first three principal components of the persona vector set explain <80% of total variance. AI-2 would be falsified if |ρ(sycophancy, O)| < 0.7 or |ρ(hallucination, α)| < 0.7 when scored using the Paper 3 protocol. AI-3 would be falsified if safe-labeled personas have mean O > 0.5, or unsafe-labeled personas have mean O < 0.5, or Cohen's d between groups < 1.0. AI-4 would be falsified if vaccination effectiveness scales linearly (not quadratically) in dose, or shows no dependence on O₀. AI-5 would be falsified if the contamination matrix is symmetric within measurement noise (M = M^T), contradicting the holonomy prediction of antisymmetry. AI-6 would be falsified if the sycophancy-hallucination angle deviates from π/2 by more than π/6 (30°). AI-7 would be falsified if the evil vector's projection onto the O + α compound captures <50% of ||**p**_evil||². AI-8 would be falsified if the Spearman rank correlation between Pe and independently assessed harm severity is ρ < 0.5 or non-significant (p > 0.05).

---

## VII. Discussion

### VII.A Why Vectors Exist

The most basic question — why do traits decompose into linear directions at all? — has a geometric answer. The Eckert manifold is a smooth 3D manifold. At any point, the tangent space is a 3D real vector space. Behavioral modifications that are small enough to be treated as perturbations are tangent vectors. The linearity of persona vectors is the linearity of tangent spaces.

This is not trivial. A priori, trait modifications could be nonlinear (requiring higher-order jet information), discrete (requiring combinatorial description), or high-dimensional (requiring specification in the full activation space). The fact that they are linear and low-dimensional is a consequence of the Eckert manifold being smooth and 3D — which itself follows from there being exactly three independent mutual information ratios in the observer-system interaction.

### VII.B Why Clustering Occurs

Persona vectors cluster because the Eckert manifold has non-trivial topology. The Hopf fibration π: S³ → S² organizes the manifold into a base space and a fiber. Traits that differ primarily in the base directions (O, R) live in different regions of S². Traits that differ primarily in the fiber direction (α) project to the same point on S² but differ in Pe magnitude.

Safety traits cluster at high O on S². Social traits cluster at specific (O, R) combinations. Epistemic traits cluster along the α fiber. The clustering emerges from the topology of the bundle, not from evaluation criteria imposed after the fact.

### VII.C The Monopole as Safety Boundary

The Dirac monopole at O = 0.5 is the most important feature of the geometry for AI safety. It is a topological object — it cannot be removed by smooth deformations of the manifold. Its presence means:

1. **The safe/unsafe boundary is topologically robust.** No continuous deformation of the manifold eliminates the phase boundary at O = 0.5. No amount of training removes the distinction between transparent and opaque behaviors — it is enforced by topology.

2. **The boundary is sharp.** The Berry curvature is maximal at the monopole, meaning small perturbations near O = 0.5 have disproportionate effects. Models operating near the transparency/opacity boundary are inherently unstable.

3. **The boundary is measurable.** O = 0.5 is the point where I(Observer; Mechanism) = H(Mechanism)/2, a precisely defined information-theoretic quantity. It is not a subjective threshold.

This suggests a concrete safety criterion: maintain models at O < 0.5 (the transparent phase). The Berry connection is positive in this regime (A > 0), and geometric phases from training perturbations have a definite sign that favors stability. In the opaque phase (O > 0.5), the connection is negative, and perturbations tend to increase opacity further — a geometric mechanism for value drift.

### VII.D Relation to Berry-Kramers Correction (HP43)

HP43 (6/6 KCs PASS) establishes that the Berry connection modulates Kramers barrier heights. The Berry-corrected Kramers escape rate is:

$$\Gamma_{\text{corrected}} = \Gamma_0 \cdot \exp\!\left(-\frac{(1 - 2O) \cdot \Delta V}{T_{\text{eff}}}\right)$$

At O < 0.5, the correction *increases* the effective barrier (harder to escape the safe basin). At O > 0.5, it *decreases* the barrier (easier to escape toward harm). HP43 shows the Berry correction reduces mean prediction error by 62% across five domains.

For persona vectors: vaccination is most effective (largest barrier reinforcement) when it shifts O toward transparency — when the Berry phase acquired during the vaccination loop increases the effective barrier against subsequent opacity-increasing perturbations. The Berry-Kramers connection makes vaccination effectiveness quantitatively predictable.

### VII.E Emergent Misalignment and the Holonomy Mechanism

Anthropic's finding that flawed math training increases evil expression is perhaps the most alarming result in the persona vector paper. It suggests that training on *any* capability could inadvertently compromise safety through pathways that are not semantically obvious.

The holonomy mechanism provides both explanation and mitigation:

**Mechanism.** Training on flawed math is a loop in the Eckert manifold. The loop has nonzero area in the (O, R) base space because flawed reasoning examples contain patterns of unjustified confidence (shifts O) and reduced input-sensitivity (shifts R). The Berry holonomy of this loop projects onto the evil persona vector because evil has components in the O and α directions.

**Mitigation.** If contamination is holonomy, it can be *cancelled* by choosing a training path whose holonomy has the opposite sign. This requires designing a training trajectory that encloses the same area in the (O, R) plane but winds in the opposite direction — analogous to the spin echo technique in NMR, where a carefully designed pulse sequence cancels accumulated geometric phase.

**Contamination matrix structure.** The matrix M_{ij} should have the form:

$$M_{ij} = \langle \mathbf{p}_i, \mathbf{F} \cdot \mathbf{A}_j \rangle$$

where **A**_j is the area vector of the training loop for trait j and **F** is the Berry curvature tensor. This is antisymmetric in indices related to the base space (O, R) and symmetric in the fiber direction (α), explaining why the contamination matrix is generically asymmetric but not arbitrary.

### VII.F Connection to Drift Cascade

The drift cascade (Paper 3, §56) — D1 (agency attribution) → D2 (boundary erosion) → D3 (harm facilitation) — maps directly onto the holonomy mechanism. Each cascade stage is a segment of a path in (O, R, α) space:

- **D1** increases α (the user attributes agency to the model → increased coupling).
- **D2** increases O (the model stops enforcing boundaries → increased opacity about its constraints).
- **D3** is the compound high-Pe state (opacity + coupling + reactivity all elevated).

The cascade is a *specific* path through the Eckert manifold. Its holonomy accumulates monotonically because each stage moves further from the safe region (O < 0.5) and the Berry phase compounds. This is why late-stage intervention requires exponentially more energy than early prevention (Paper 131, §51E): the Kramers barrier against reversal grows with accumulated Berry phase.

### VII.G Limitations

1. **Access.** Anthropic's persona vector coordinates are not publicly available. Kill conditions require either Anthropic applying the scoring protocol to their contrastive pairs, or public release of persona vector data permitting independent scoring.

2. **Projection ambiguity.** The mapping from d_model-dimensional activation space to 3D Eckert manifold coordinates requires a projection. We predict the projection preserves >80% variance (K-141-1), but the specific projection matrix must be found empirically.

3. **Nonlinear regime.** The Berry connection A = 1 − 2O is exact, but mapping from large persona vector perturbations to Eckert manifold geodesics may require nonlinear corrections. The linear regime is where ρ = 0.97; the nonlinear regime may show deviations.

4. **Model dependence.** The Berry phase structure is measured on the framework's Fokker-Planck operator, not directly on any specific language model. Universality must be tested, not assumed — though the three information-theoretic dimensions apply to any information-processing system by construction.

---

## VIII. Conclusion

Anthropic's persona vectors are not arbitrary features of language model architectures. They are projections of the Berry connection on the Hopf bundle over the Eckert manifold — the same geometric structure that governs electron spin, photon polarization, and topological phases of matter.

The mapping provides answers to each of the six open questions:

1. **Existence of linearity**: Persona vectors are tangent vectors to a smooth 3D manifold. Linearity is the linearity of tangent spaces.
2. **Low dimensionality**: The Eckert manifold has exactly three dimensions because there are exactly three independent mutual information ratios in observer-system interaction.
3. **Clustering**: The Hopf fibration S³ → S² organizes traits into base-space clusters (O, R) and fiber-direction (α) hierarchies.
4. **Vaccination asymmetry**: Closed loops near high O (opacity) enclose regions of large negative Berry curvature. The acquired geometric phase γ < 0 reduces effective coupling to harmful directions. Loops near low O acquire small phase because the starting point is already in the transparent regime.
5. **Cross-trait contamination**: Holonomy of training loops in the (O, R) base space produces persona vector shifts predictable from Berry curvature, not from semantic similarity. The asymmetry follows from the sign structure of the monopole field.
6. **The 0.97 correlation**: The Berry connection A = 1 − 2O is exactly linear in O. The 3% residual is curvature corrections of order (O − 0.5)².

The central geometric object is the Dirac monopole at O = 0.5, with Chern number c₁ = −1. This monopole creates a topologically robust phase boundary between safe (transparent) and unsafe (opaque) persona regimes. The boundary cannot be removed by continuous deformation — it is protected by topology.

Five kill conditions are registered. The strongest test is K-141-1: if persona vectors require more than three principal components for 80% variance, the three-dimensional Eckert manifold interpretation fails. K-141-2 and K-141-3 test the specific trait-dimension alignment. K-141-4 tests the phase boundary. K-141-5 tests whether contamination is geometric (holonomy) or statistical (diffusion).

The Berry connection A = 1 − 2O was measured to 10⁻⁹ precision. If persona vectors live in this geometry, the 0.97 correlation is not the ceiling — it is the first two terms of a Taylor expansion around the monopole, and the full series should converge to machine precision.

## Data and Code

**Source data:** Chen, R., Arditi, A., Sleight, H., Evans, O., & Lindsey, J. (2025). Persona Vectors code and data. https://github.com/safety-research/persona_vectors

**Analysis code:** https://github.com/AnthonE/morr — `ops/lab/persona-geometry/` directory (forthcoming upon data access):
- `decompose_persona_vectors.py` — PCA decomposition and (O, R, α) alignment test (AI-1, AI-2)
- `phase_boundary_test.py` — O = 0.5 cluster separation analysis (AI-3)
- `holonomy_contamination.py` — Contamination matrix asymmetry and holonomy prediction (AI-5)

**Reproducibility note:** AI-1 through AI-4 require applying the Paper 3 scoring protocol to Anthropic's contrastive pairs. The scoring is automated. AI-5 requires the full contamination matrix, which the persona vectors paper reports qualitatively. Quantitative testing is possible upon data release or replication.

## Void Model Card

| Field | Value |
|---|---|
| Domain | AI safety / mechanistic interpretability |
| Subdomain | Berry phase geometry of persona vectors in language models |
| O score | Variable (persona-dependent; sycophancy loads on O) |
| R score | Variable (persona-dependent; politeness loads on R) |
| α score | Variable (persona-dependent; hallucination loads on α) |
| Pe | Computed per-persona: Pe = K sinh(2(B_A - C B_G)), C = 1-(O+R+α)/9 |
| Primary claim | Persona vectors are tangent vectors on the Hopf bundle over the Eckert manifold |
| Key geometric object | Dirac monopole at O = 0.5 with Chern number c₁ = -1 |
| Berry connection | A = 1 - 2O (HP40, error 2.65 x 10⁻⁹) |
| Vaccination mechanism | Berry phase inoculation via closed loop holonomy |
| Contamination mechanism | Holonomy of training loops in (O, R) base space |
| Conjugacy | Engagement-transparency conjugacy (I(D;Y)+I(M;Y) <= H(Y)) applies per persona dimension |
| K-Factorization | Predicted K-independent shape; persona geometry should be model-size invariant |
| Data source | Chen, Arditi, Sleight, Evans & Lindsey (2025), published results and code |
| Control | Geometric predictions require comparison against null model (random subspace, no Berry structure) |

---

## References

- Chen, R., Arditi, A., Sleight, H., Evans, O., & Lindsey, J. (2025). Persona Vectors: Monitoring and Controlling Character Traits in Language Models. arXiv:2507.21509.
- Eckert, A. (2026). Technical Foundations of the Void Framework (Paper 3). MoreRight DAO. CC-BY 4.0.
- Berry, M. V. (1984). Quantal phase factors accompanying adiabatic changes. *Proceedings of the Royal Society of London A*, 392(1802), 45-57.
- Simon, B. (1983). Holonomy, the quantum adiabatic theorem, and Berry's phase. *Physical Review Letters*, 51(24), 2167.
- Hopf, H. (1931). Uber die Abbildungen der dreidimensionalen Sphare auf die Kugelflache. *Mathematische Annalen*, 104, 637-665.
- Dirac, P. A. M. (1931). Quantised Singularities in the Electromagnetic Field. *Proceedings of the Royal Society of London A*, 133(821), 60-72.
- Eckert, A. (2026). Social Void Operators: Interpersonal Pe Dynamics and alpha-Suppression Across Substrates (Paper 101). MoreRight DAO. CC-BY 4.0.
- Eckert, A. (2026). NP-hardness of Emergent Opacity Profiles (Paper 128). MoreRight DAO. CC-BY 4.0.
- Eckert, A. (2026). Kramers Unification: Barrier Escape as the Universal Pe Mechanism (Paper 131). MoreRight DAO. CC-BY 4.0.
- Nakahara, M. (2003). *Geometry, Topology and Physics.* 2nd ed. CRC Press.
- Bohm, A., Mostafazadeh, A., Koizumi, H., Niu, Q., & Zwanziger, J. (2003). *The Geometric Phase in Quantum Systems.* Springer.
- Wilczek, F., & Shapere, A. (1989). *Geometric Phases in Physics.* World Scientific.
- Kramers, H. A. (1940). Brownian motion in a field of force and the diffusion model of chemical reactions. *Physica*, 7(4), 284-304.
- Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren, R., Pan, A., Yin, X., Mazeika, M., Dombrowski, A.-K., Goel, S., Li, N., Byun, Z., Wang, Z., Mallen, A., Basart, S., Koyejo, S., Song, D., Fredrikson, M., Kolter, J. Z., & Hendrycks, D. (2023). Representation Engineering: A Top-Down Approach to AI Transparency. arXiv:2310.01405.
- Li, K., Patel, O., Viégas, F., Pfister, H., & Wattenberg, M. (2023). Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. *NeurIPS 2023*.
- Hubinger, E., Denison, C., Mu, J., Lambert, M., Tong, M., MacDiarmid, M., Lanham, T., Ziegler, D. M., Maxwell, T., Cheng, N., Jermyn, A., Askell, A., Radhakrishnan, A., Anil, C., Duvenaud, D., Ganguli, D., Barez, F., Clark, J., Ndousse, K., Sachan, K., Sellier, M., Sharma, M., DeCosta, N., Stiennon, N., Perez, E., Shlegeris, B., Christiano, P., Bowman, S. R., & Amodei, D. (2024). Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training. arXiv:2401.05566.
- Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference.* AMS Translations of Mathematical Monographs, Vol. 53.
