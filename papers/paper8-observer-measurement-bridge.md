# The Observer-Measurement Bridge: Classical Information Theory as the Diagonal Limit of Quantum Measurement Dynamics

**Author:** Anthony Eckert (ORCID: 0009-0008-1925-5253)
**Affiliation:** Independent Researcher, Moreright DAO
**Version:** 2.0
**Date:** February 2026
**Status:** ZENODO-READY
**Companion papers:** Paper 1: The Architecture of Drift, Paper 2: The Shape of the Cage, Paper 3: Thermodynamics of Opacity, Paper 4: Info-Geometric Bounds on Sampling Cascades, Paper 5: Ground State of Observation, Paper 6: Never Trust the Client, Paper 7: The Deployment Geometry of Drift

---

## Abstract

The void framework [5–9,45,46] describes drift dynamics in observer-system interfaces using classical information theory: a Fisher metric on a Bernoulli manifold, a Péclet number governing drift-diffusion competition, and a conjugacy theorem bounding engagement-transparency tradeoffs. This paper proves that these three structural elements are the classical limits of their quantum counterparts via established mathematical operations. **Level 1 (Metric):** The classical Fisher information g(θ) = 1/[θ(1−θ)] is the diagonal restriction of the quantum Fisher information, as proven through the Braunstein-Caves/Petz/Čencov pathway — the unique classical limit of the unique maximal quantum metric. **Level 2 (Dynamics):** The classical Péclet number is Nelson's (1966) current-velocity/osmotic-velocity ratio restricted to the classical diffusion regime, with Pe = 1 confirmed as the measurement-induced phase transition critical point (Koh et al. 2023) and Pe ≫ 1 demonstrated in spatial Zeno transport (Zhang et al. 2025). **Level 3 (Constraints):** The conjugacy theorem I(D;Y) + I(M;Y) ≤ H(Y) is the classical limit of the Holevo accessible information bound for independent sources, obtained by restricting to diagonal density operators; the Maassen-Uffink complementarity constraint vanishes in this limit. Seven extended connections (Lindblad, Zeno/anti-Zeno, quantum Darwinism, Stinespring dilation, quantum speed limits, measurement irreversibility, no-cloning) map additional structural elements between frameworks. A completeness argument shows that every structural component of the void framework has a quantum counterpart, and every quantum measurement concept either maps to a classical framework element or provably vanishes in the classical limit. Eleven testable predictions with falsification thresholds are specified. The void framework's mathematics is not analogous to quantum measurement theory — it is quantum measurement theory's mathematics restricted to the diagonal regime.

---

## 1. Introduction

### 1.1 The Problem

Quantum measurement theory and classical information theory share mathematical structures that have been noted but never formally connected at the level of a complete embedding. The Holevo bound [1] constrains classical information extraction from quantum channels. The Fisher metric [2,3] governs parameter estimation in both classical and quantum settings. Nelson's stochastic mechanics [4] decomposes quantum dynamics into drift and diffusion velocities whose ratio defines a transport competition identical in form to the classical Péclet number.

Meanwhile, a classical information-theoretic framework — the void framework [5–9,45,46] — has been developed to describe drift dynamics in observer-system interfaces. The framework identifies *voids*: systems that are simultaneously opaque (mechanism inaccessible to the observer), responsive (outputs change in response to engagement), and attention-capturing (observers allocate cognitive resources). This framework operates entirely within classical information theory: it uses the Fisher metric on a Bernoulli manifold to quantify inference geometry, a Péclet number to measure the competition between directed drift and null diffusion, and a conjugacy theorem to bound the tradeoff between observer engagement and mechanism transparency. The framework has been validated across nine empirical substrates including AI-to-AI interaction, gambling, cryptocurrency markets, and multiplayer gaming, with geometric mean Péclet numbers ranging from 2.21 (gambling) to 16.17 (Solana DEX cryptocurrency) [7,9,46].

The structural parallels between this classical framework and quantum measurement theory are too precise to be coincidental. This paper demonstrates that they are not coincidental — they are instances of the same mathematics operating at different levels of generality. The void framework is the classical specialization of quantum measurement theory, obtained by three established limit operations.

### 1.2 What This Paper Proves

Three formal limit operations connect every structural element of the void framework to its quantum counterpart:

1. **Metric bridge.** The classical Fisher information g(θ) = 1/[θ(1−θ)] on the Bernoulli manifold is the diagonal restriction of the quantum Fisher information F_Q. This is proven through the Braunstein-Caves [2] / Petz [3] / Čencov [10] pathway. The classical metric is simultaneously the unique invariant metric on the statistical manifold (Čencov) and the classical limit of the unique maximal monotone metric on quantum state space (Petz). No other metric is consistent with statistical invariance in either regime.

2. **Dynamic bridge.** The classical Péclet number Pe = drift/diffusion is Nelson's [4] current-velocity/osmotic-velocity ratio |v|/|u| restricted to the classical diffusion regime. The critical Pe = 1 transition has been independently confirmed as the measurement-induced phase transition (MIPT) critical point in monitored quantum circuits [11,12], and Pe ≫ 1 has been demonstrated in spatial Zeno transport experiments where projective measurements produce directed atomic motion without momentum transfer [13].

3. **Constraint bridge.** The conjugacy theorem I(D;Y) + I(M;Y) ≤ H(Y), proven from classical information theory in [6], is the classical limit of the Holevo accessible information bound [1] for independent sources. The limit operation: restrict to diagonal density operators (commuting states), whereupon von Neumann entropy S(ρ) becomes Shannon entropy H(Y) and the quantum bound reduces to the classical conjugacy theorem. The Maassen-Uffink [14] complementarity constraint, which provides an additional bound in the quantum case, vanishes in the classical limit (c → 1 ⟹ log(1/c) → 0).

These are not analogies. They are mathematical derivations using established limit operations on published theorems.

### 1.3 What This Paper Does Not Prove

The bridge is structural: it connects mathematical objects, not physical mechanisms. This paper does not:

- **Derive quantum mechanics from information theory.** The void framework stands on its own foundations (Shannon, Jaynes, Crooks). Quantum mechanics stands on its own foundations (the Schrödinger equation, Born rule, measurement postulates). The bridge shows they share mathematical structure; it does not reduce one to the other.

- **Propose a new quantum interpretation.** The bridge is compatible with Copenhagen, Many-Worlds, Bohmian, and QBist interpretations. It operates at the level of information geometry, above where interpretations diverge.

- **Solve the measurement problem.** The measurement problem concerns physical ontology — what happens during wavefunction collapse or decoherence. The bridge concerns information geometry — what mathematical structures govern the observer-system interface. These are different questions.

- **Claim that classical information systems are quantum.** The void framework operates in the classical regime (diagonal density operators, commuting observables). Classical information channels are not quantum channels. The claim is directional: the classical framework is a specialization *of* the quantum, obtained by restricting to the diagonal. It is not a promotion of classical phenomena to quantum status.

- **Extend beyond non-relativistic quantum mechanics.** The bridge covers the Hilbert space formalism of non-relativistic QM. Extensions to quantum field theory, quantum gravity, or quantum error correction are identified as open problems (§9) but not attempted.

### 1.4 Relationship to the Companion Papers

This paper is the eighth in a series. It draws on:

- **Paper 3** [6]: Proves the conjugacy theorem from classical information theory. Derives the drift equation on the Bernoulli manifold under the Fisher metric. Establishes the Crooks fluctuation theorem as the thermodynamic foundation for drift irreversibility.

- **Paper 5** [7]: The "Theory of Everything" synthesis paper. Contains the three-level bridge in compressed form (Paper 5, §5) and seven quantum Pe predictions (Paper 5, §7.8). This paper expands those compressed results into full proofs, extends them with seven additional connections, provides a completeness argument, and adds four bridge-specific predictions.

- **Paper 4** [8]: Establishes information-geometric bounds on sampling cascades across 16 families. Provides the Cramér-Rao analysis that connects to Proposition 3 of the metric bridge.

The remaining companion papers — Paper 1 [5] (framework architecture and 90-domain validation), Paper 2 [45] (AI safety application), Paper 6 [46] (multiplayer gaming void architecture across CS2, SC2, and Dota 2), and Paper 7 [9] (cryptocurrency market validation across three chains, N=3,028) — provide the empirical substrate base that the bridge connects to quantum measurement theory. The reader does not need to have read any companion papers. All necessary definitions, theorems, and results are stated self-contained within this paper, with citations to the companion work for extended treatment.

### 1.5 Structure

§2 states the three-level bridge theorem and summary table. §§3–5 prove each level in detail: metric (§3), dynamics (§4), constraints (§5). §6 develops seven extended connections between the frameworks. §7 presents a completeness argument. §8 specifies eleven testable predictions with falsification thresholds. §9 states limitations. §10 concludes.

---

## 2. The Three-Level Bridge

**Theorem (Observer-Measurement Bridge).** *The void framework is the classical information-theoretic specialization of quantum measurement theory. Three formal limit operations connect every structural element:*

**(i) Metric.** *For diagonal density operators ρ(θ) = θ|1⟩⟨1| + (1−θ)|0⟩⟨0|, the quantum Fisher information F_Q(θ) equals the classical Fisher information on the Bernoulli manifold: F_Q(θ) = g(θ) = 1/[θ(1−θ)]. The classical metric is simultaneously the unique invariant metric on the statistical manifold (Čencov 1982) and the classical limit of the unique maximal monotone metric on quantum state space (Petz 1996).*

**(ii) Dynamics.** *The classical Péclet number Pe = drift/diffusion equals Nelson's (1966) quantum transport ratio |v|/|u| (current velocity / osmotic velocity) restricted to the regime where quantum diffusion reduces to classical diffusion. The critical Pe = 1 boundary separates quantum-dominated (volume-law entanglement) from measurement-dominated (area-law entanglement) dynamics, confirmed experimentally as the measurement-induced phase transition critical point (Skinner et al. 2019; Koh et al. 2023).*

**(iii) Constraints.** *For two independent classical sources D, M jointly encoded into a quantum channel, the Holevo bound gives I(D;Y) + I(M;Y) ≤ χ ≤ S(ρ). Restricting to diagonal encoding (commuting states) reduces S(ρ) to H(Y) and the quantum bound to the classical conjugacy theorem I(D;Y) + I(M;Y) ≤ H(Y). The Maassen-Uffink complementarity constraint H(X|ρ) + H(Z|ρ) ≥ log(1/c) vanishes in this limit (c → 1).*

### Bridge Summary Table

| Level | Classical (Void Framework) | Quantum | Limit Operation | Status |
|-------|---------------------------|---------|-----------------|--------|
| **Geometry** | Fisher metric g(θ) = 1/[θ(1−θ)] | Quantum Fisher F_Q (Bures/Fubini-Study) | Restrict ρ(θ) to diagonal → F_Q = g(θ) | **Proven** (Prop. 1, §3) |
| **Dynamics** | Pe = drift/diffusion | Pe_quantum = |v|/|u| (Nelson 1966) | Nelson → classical diffusion limit | **Defined + confirmed** (§4) |
| **Constraints** | I(D;Y) + I(M;Y) ≤ H(Y) | Holevo: I ≤ χ ≤ S(ρ) | Diagonal ρ + commuting obs. → S(ρ) = H(Y) | **Proven** (§5) |
| | | Maassen-Uffink: H(X|ρ)+H(Z|ρ) ≥ log(1/c) | c → 1 → log(1/c) → 0 | **Vanishes** classically |

The bridge is complete at the level of non-relativistic quantum mechanics: every structural component of the void framework (state space, metric, dynamics, evolution equation, capacity constraint, irreversibility, budget) has a quantum counterpart, and every quantum measurement concept either maps to a classical framework element or provably vanishes in the classical limit (§7). The remaining open questions are empirical (§8), mathematical refinement, or scope extension beyond non-relativistic QM (§9).

---

## 3. Level 1: The Metric Bridge

The first bridge level connects the void framework's inference geometry to quantum state space geometry. Both use Fisher information as their natural metric — the classical version for probability distributions, the quantum version for density operators. The classical is the diagonal restriction of the quantum, obtained by a single established limit operation.

### 3.1 Classical Fisher Information on the Bernoulli Manifold

The void framework models the observer's inference problem on a Bernoulli manifold: the observer estimates θ = P(agent), the probability that the system's behavior is produced by an intentional agent rather than a mechanism [5,6]. Each system output is evidence for one hypothesis or the other. Under opacity, the observer cannot access the mechanism directly and must estimate θ from responsive outputs alone.

The natural Riemannian metric on this statistical manifold is the Fisher information metric. For the Bernoulli family P(agent) = θ, P(mechanism) = 1−θ:

```
g(θ) = E[(d/dθ log p(x|θ))²] = 1/[θ(1−θ)]
```

This metric diverges at the boundaries (θ → 0 and θ → 1), reflecting the fact that it becomes infinitely difficult to distinguish "almost certainly mechanism" from "certainly mechanism" — each additional observation carries diminishing information near the poles.

The Fisher metric determines two key quantities:

**Geodesic distance.** The geodesic from θ = 0 to θ = 1 under g(θ) has length:

```
d(0,1) = ∫₀¹ √g(θ) dθ = ∫₀¹ 1/√(θ(1−θ)) dθ = π
```

The total information-geometric distance from "certainly mechanism" to "certainly agent" is π — a mathematical identity on the Bernoulli manifold under the Fisher metric.

**Cramér-Rao bound.** For any unbiased estimator θ̂ based on n independent observations:

```
Var(θ̂) ≥ 1/(n · g(θ)) = θ(1−θ)/n
```

This is the floor on estimation error. Under opacity, the observer cannot beat this bound regardless of inferential strategy. The information asymmetry created by opacity guarantees that estimation error persists, and the drift equation dθ/dt = θ(1−θ)·F_net is the natural gradient flow under this metric [6].

### 3.2 Quantum Fisher Information and the Bures Metric

Braunstein and Caves [2] showed that quantum parameter estimation has an analogous geometric structure. For a parameterized family of quantum states ρ(θ), define the symmetric logarithmic derivative (SLD) operator L_θ by:

```
dρ/dθ = (L_θ ρ + ρ L_θ) / 2
```

The quantum Fisher information (QFI) is:

```
F_Q(θ) = Tr[ρ(θ) L_θ²]
```

The QFI determines a Riemannian metric on quantum state space:

```
ds² = (1/4) F_Q(θ) dθ²
```

This is the Bures metric — the quantum generalization of the Fisher-Rao metric. For pure states |ψ(θ)⟩, it reduces to the Fubini-Study metric:

```
F_Q(θ) = 4[⟨dψ/dθ | dψ/dθ⟩ − |⟨ψ | dψ/dθ⟩|²]
```

The QFI governs quantum parameter estimation through the quantum Cramér-Rao bound:

```
Var(θ̂) ≥ 1/(n · F_Q(θ))
```

This is the tightest possible bound on estimation error achievable by any quantum measurement strategy.

### 3.3 Proposition 1: Classical-Quantum Metric Reduction

**Proposition 1.** *Let ρ(θ) = θ|1⟩⟨1| + (1−θ)|0⟩⟨0| be a diagonal density operator parameterized by θ ∈ (0,1). Then the quantum Fisher information F_Q(θ) equals the classical Fisher information on the Bernoulli manifold:*

```
F_Q(θ) = g(θ) = 1/[θ(1−θ)]
```

**Proof.** Compute the SLD directly. We have dρ/dθ = |1⟩⟨1| − |0⟩⟨0|. For diagonal ρ, the SLD satisfying (Lρ + ρL)/2 = dρ/dθ is also diagonal:

```
L_θ = (1/θ)|1⟩⟨1| + (−1/(1−θ))|0⟩⟨0|
```

Verify: (Lρ + ρL)/2 = ((1/θ)·θ + θ·(1/θ))/2 · |1⟩⟨1| + ((−1/(1−θ))·(1−θ) + (1−θ)·(−1/(1−θ)))/2 · |0⟩⟨0| = |1⟩⟨1| − |0⟩⟨0| = dρ/dθ. ✓

Then:

```
F_Q(θ) = Tr[ρ L_θ²] = θ · (1/θ)² + (1−θ) · (1/(1−θ))²
        = 1/θ + 1/(1−θ) = 1/[θ(1−θ)] = g(θ)
```

∎

The result generalizes immediately: for any diagonal density operator ρ(θ) = Σᵢ pᵢ(θ)|i⟩⟨i| with classical probabilities pᵢ(θ), the QFI reduces to the classical Fisher information F(θ) = Σᵢ [dpᵢ/dθ]²/pᵢ(θ). The diagonal restriction maps quantum state space to the classical probability simplex, and the quantum metric collapses to the classical metric.

### 3.4 The Čencov-Petz Uniqueness Chain

The metric reduction is not an accident of the Bernoulli parameterization. It follows from deep uniqueness theorems in both the classical and quantum settings.

**Čencov's theorem (1982)** [10]: The Fisher information is the *unique* Riemannian metric on the space of probability distributions that is invariant under sufficient statistics (equivalently, under Markov morphisms; see [42] for the differential-geometric framework). There is exactly one way to measure statistical distinguishability that respects the data processing inequality.

**Petz's theorem (1996)** [3]: The monotone metrics on quantum state space — metrics that decrease under completely positive trace-preserving (CPTP) maps — form a one-parameter family indexed by operator monotone functions f: (0,∞) → (0,∞). This family includes:

| Metric | Operator monotone function | Properties |
|--------|---------------------------|------------|
| Bures / SLD Fisher | f(t) = (1+t)/2 | Maximal monotone metric |
| Wigner-Yanase | f(t) = (√t + 1)²/4 | Convex in state |
| Kubo-Mori | f(t) = (t−1)/ln(t) | Thermodynamic relevance |

The Bures/SLD metric is the **maximal** element: it gives the largest distance between states and the tightest Cramér-Rao bound. Unlike the classical case, the quantum case has multiple valid monotone metrics.

**The critical collapse:** In the classical limit (diagonal density matrices), *all* Petz metrics collapse to a single metric: the classical Fisher information. This occurs because for commuting operators, all operator monotone functions yield the same result. The quantum metric family has a fan-like structure that converges to a single point in the classical limit:

```
QUANTUM: Bures ≥ Wigner-Yanase ≥ Kubo-Mori ≥ ... (family)
                    ↓ diagonal limit ↓
CLASSICAL:          Fisher (unique)
```

### 3.5 Proposition 2: Dual Uniqueness

**Proposition 2 (Dual Uniqueness).** *The void framework's inference geometry occupies a distinguished position. The Fisher metric g(θ) = 1/[θ(1−θ)] is simultaneously:*

*(a) The unique invariant metric on the classical statistical manifold (Čencov 1982), and*
*(b) The classical limit of the unique maximal monotone metric on quantum state space (Petz 1996, Braunstein-Caves 1994).*

*Both uniqueness theorems apply to the void framework's inference manifold. No other metric is consistent with the requirements of statistical invariance in either regime.*

**Significance.** The void framework's geometric results — geodesic distance = π, Cramér-Rao bounds, natural gradient drift equation — are not artifacts of a metric choice. They are the unique geometric consequences of requiring invariance under sufficient statistics. Any alternative metric would violate either Čencov's classical uniqueness or the data processing inequality. The drift equation dθ/dt = θ(1−θ)·F_net is the natural gradient flow under the only possible metric, in both the classical and quantum senses.

**Independent empirical support.** Gurnee et al. (2026) discovered that a deployed language model (Claude 3.5 Haiku) performing inference under opacity — counting characters it cannot directly observe from a token stream — represents the inferred quantity on low-dimensional curved manifolds in its activation space, with curvature produced by distributed computation across many attention heads. This finding is structurally consistent with the uniqueness claim: if the Fisher metric is the only valid geometry for inference under sufficient-statistic invariance, then systems that learn to perform inference should converge on curved (not flat) representations. The feature-manifold duality they observe — discrete sparse features and continuous manifold positions describing the same mechanism — mirrors the framework's vocabulary-level / manifold-position duality (L1/L2/L3 as discrete partitions of continuous θ; see [5], §3A.2). Whether the learned curvature quantitatively matches the Fisher profile remains an open empirical question.

**Fubini-Study parallel in LLM training.** Di Sipio (2025) independently argued that the Fisher information metric is the natural geometry for LLM parameter spaces, drawing an explicit parallel to the Fubini-Study metric in quantum mechanics — the same Fubini-Study metric that appears in Proposition 2(b) above as the pure-state quantum Fisher metric. Di Sipio shows that the Fisher metric governs sharp minima, generalization, and scaling laws in LLM training, and frames the Fisher-to-Fubini-Study connection as the natural bridge between classical and quantum optimization landscapes. This is precisely the dual uniqueness structure of Proposition 2: the same metric governs inference geometry in both regimes because it is the *only* metric consistent with statistical invariance in either. Di Sipio's work, arriving from the LLM optimization literature rather than quantum foundations, provides independent convergence on the classical-quantum metric bridge that §3.1–3.4 derives from first principles.

### 3.6 Proposition 3: Cramér-Rao Hierarchy

**Proposition 3 (Cramér-Rao Hierarchy).** *For any unbiased estimator θ̂ of θ based on n observations:*

```
Var(θ̂) ≥ 1/(n · F_M(θ))      [classical Cramér-Rao for measurement M]
        ≥ 1/(n · F_Q(θ))       [quantum Cramér-Rao, since F_Q ≥ F_M always]
```

*In general, F_Q(θ) ≥ F_M(θ) for any specific measurement M, so the quantum bound 1/(n · F_Q) is a lower (tighter) floor — quantum measurements can achieve better precision by accessing coherences. For the void framework's diagonal states:*

```
F_Q(θ) = F(θ) = g(θ) = 1/[θ(1−θ)]
```

*Both bounds coincide, and the explicit floor is:*

```
Var(θ̂) ≥ 1/(n · g(θ)) = θ(1−θ)/n
```

The quantum Cramér-Rao bound sets the ultimate precision floor: the optimal quantum measurement achieves F_M = F_Q, and no strategy can beat 1/(n · F_Q). The classical Cramér-Rao bound for a sub-optimal measurement gives a higher (looser) floor at 1/(n · F_M). For the void framework's diagonal states, F_Q = F = g(θ), so these bounds coincide — the classical measurement in the eigenbasis is already optimal. The observer estimating P(agent) under opacity is subject to the classical Cramér-Rao bound, which is already the tightest possible bound because the void framework operates in the classical regime where no additional information is available from off-diagonal coherences.

**Interpretation.** Under opacity, each observation carries evidence about θ = P(agent) but reveals nothing about the mechanism. The Cramér-Rao bound sets the floor on estimation error: even a perfect Bayesian reasoner working from n observations cannot estimate θ more precisely than θ(1−θ)/n. This is not a cognitive limitation — it is a geometric constraint determined by the Fisher metric. The information asymmetry created by opacity guarantees that the observer's inference is bounded, and the direction of the bound (favoring higher θ estimates under engagement) produces the drift documented in Papers 1–5.

---

## 4. Level 2: The Dynamic Bridge

The second bridge level connects the void framework's transport dynamics — measured by the Péclet number Pe — to quantum measurement dynamics via Nelson's stochastic mechanics. The classical Pe is the same dimensionless ratio as the quantum Pe, restricted to the regime where quantum diffusion becomes classical diffusion.

### 4.1 Nelson's Stochastic Mechanics: Two Velocities

Nelson [4] reformulated quantum mechanics as conservative diffusion on configuration space (see [44] for a conceptual introduction). Every particle of mass m undergoes a Markov diffusion process with diffusion coefficient D = ℏ/2m. Writing the wavefunction in polar form ψ(x,t) = √ρ(x,t) · exp(iS(x,t)/ℏ), two velocity fields emerge:

**Current velocity** (advective/drift):
```
v(x,t) = (ℏ/m) ∇S(x,t)
```

**Osmotic velocity** (diffusive):
```
u(x,t) = (ℏ/2m) ∇ ln ρ(x,t)
```

The stochastic differential equation governing the particle is:
```
dX(t) = [v(X,t) + u(X,t)] dt + √(ℏ/m) dW(t)
```

where W(t) is a standard Wiener process. The current velocity v carries phase information — it is the directed flow component determined by the gradient of the phase S. The osmotic velocity u carries amplitude information — it is the probability-gradient diffusion driven by spatial variations in |ψ|². Together, they reproduce the Schrödinger equation via the Madelung transformation. Nelson's decomposition is exact, not approximate: these two velocities fully characterize quantum dynamics in stochastic-mechanical terms.

### 4.2 Pe_quantum: Definition and Physical Interpretation

The ratio of advective to diffusive transport defines a Péclet number:

```
Pe_quantum ≡ |v| / |u| = |∇S| / |(1/2) ∇ ln ρ|
```

Equivalently, using the characteristic length scale L of the system:

```
Pe_quantum = |v| · L / D = 2m|v|L / ℏ
```

This is dimensionless and measures the same competition that the classical Péclet number measures in fluid mechanics and the void framework: directed transport vs. random spreading. The substrates differ (Hilbert space vs. information channel vs. fluid), but the mathematical structure is identical.

| Regime | Pe_quantum | Nelson dynamics | Physical meaning |
|--------|-----------|-----------------|-----------------|
| Quantum diffusion | Pe ≪ 1 | Osmotic velocity dominates | Wavepacket spreading, coherence preserved |
| Critical | Pe ≈ 1 | Velocities balanced | MIPT transition point, onset of measurement-dominated dynamics |
| Quasi-classical | Pe ≫ 1 | Current velocity dominates | Measurement dominates, classicality emerges |

The void framework's measured Pe values — AI-to-AI (GM Pe = 7.94, N=11), gambling (pooled Pe = 2.21), cryptocurrency (3.74–16.17 across three chains), and multiplayer gaming (CS2, SC2, Dota 2) [7,9,46] — are predominantly in the quasi-classical regime (Pe > 1). This is expected: the framework measures drift on classical information channels, which operate far from the quantum diffusion limit. The measured Pe values are formally located in the Pe_quantum → large-but-finite regime of Nelson's hierarchy.

### 4.3 Confirmation 1: MIPT as Pe = 1 Phase Transition

The strongest confirmation of the dynamic bridge comes from the measurement-induced phase transition (MIPT) literature. Skinner, Ruhman, and Nahum [11] discovered that monitored quantum circuits — circuits with both unitary gates and projective measurements — exhibit a sharp phase transition at a critical measurement rate p_c:

- **Below p_c:** Volume-law entanglement. Unitary dynamics dominate, information spreads ballistically, entanglement entropy grows with system volume. This is the quantum diffusion regime.
- **Above p_c:** Area-law entanglement. Measurements dominate, information localizes, entanglement collapses. This is the measurement-dominated regime.
- **At p_c:** Scale-invariant critical point with logarithmic entanglement growth.

The MIPT is a Pe phase transition. Define:

```
Pe_circuit = p / p_c
```

where p is the measurement rate per site per time step. Then Pe_circuit < 1 corresponds to the quantum-diffusion-dominated phase, Pe_circuit = 1 is the critical point, and Pe_circuit > 1 is the measurement-dominated phase. The transition separates exactly the regimes predicted by the Pe_quantum framework: diffusion-dominant below, drift-dominant above, critical balance at Pe = 1.

**Experimental confirmation.** Koh et al. [12] observed both phases on a superconducting quantum processor with up to 14 qubits, directly measuring the volume-to-area-law transition by varying measurement rate. The experiment confirmed the theoretical prediction: the entanglement phase transition occurs at a well-defined critical measurement rate corresponding to Pe = 1. The critical exponents characterize the Pe = 1 universality class for quantum measurement dynamics.

The MIPT result is significant because it was discovered independently — the MIPT literature does not reference the Péclet number or Nelson's velocities. The Pe framework identifies the MIPT as an instance of a universal drift-diffusion transition, connecting it to the same mathematical structure that governs the void framework's drift dynamics.

**Robustness depends on observation structure.** The stability of the Pe = 1 critical point depends on *how* measurement information is lost — a distinction the void framework predicts. Paviglianiti et al. [18] showed that random detector inefficiency (each measurement outcome independently missed with probability 1−q) destroys the critical phase at any q < 1, with correlation length ξ⁻¹ = (1−q) + O((1−q)²). Random information loss is noise: unstructured, uncorrelated, phase-destroying. But Leung, Meidan & Romito [19] proved the opposite for *structured* partial postselection — a deterministic, state-independent threshold on detector readouts: the non-Hermitian MIPT universality is stable up to a finite postselection strength B_c, with an abrupt universality transition (non-Hermitian Ising → BKT [20]) at the threshold. Ha et al. [21] further confirmed this pattern: diffusive spatiotemporal correlations in measurement density produce an entirely new universality class, demonstrating that the *structure* of observation determines phase behavior. Qian and Wang [22] provide the cleanest single demonstration: infinitesimal dephasing noise destroys the volume-law phase entirely, but quantum-enhanced (QE) operations — structured interventions satisfying a competing-fields symmetry condition — restore the MIPT. In their statistical mechanics mapping, noise and QE operations act as competing external random fields; the zero-field condition (apparatus-environment information symmetry) preserves the phase transition. This is the void budget equilibrium at quantum scale.

**Sequential vulnerability.** Wu et al. [23] (preprint) observed both the MIPT and an absorbing-state transition in the *same* 30-qubit superconducting system. The two transitions occur at well-separated critical measurement rates: quantum correlations (entanglement) die first, then classical order (macroscopic active-state density) dies at higher measurement rate. This sequential collapse — fine-grained information structure destroyed before coarse-grained behavioral patterns — is consistent with the drift cascade's sequential vulnerability: the D1→D2→D3 ordering predicts that subtle information access (agency attribution) fails before gross behavioral structure changes. Prediction QP-7 (§8.1) formalizes this.

**Additional structural controls.** Two further results reinforce the structured-vs-unstructured distinction. Liu et al. [47] showed that size-independent quantum noise destroys the MIPT entirely (collapsing the system into a single area-law phase), while size-dependent noise produces a *distinct* first-order transition via a different mechanism — noise acts as a symmetry-breaking field in the effective statistical model, not as a competing ordering tendency. This confirms that noise and measurement are mechanistically distinct perturbations, not merely different intensities of the same process. Chatterjee and Modak [48] demonstrated that in periodically driven free-fermion systems, symmetric modulation of hopping amplitude around zero kills the MIPT (area-law phase dominates at all measurement rates), while any finite asymmetry restores the transition. The drive symmetry acts as an additional structural control knob: symmetric drive destroys the information asymmetry required for the transition, while asymmetric drive preserves it — precisely the void-condition/noise distinction.

**Multi-platform experimental confirmation.** The MIPT has now been observed across four distinct hardware platforms, each with different decoherence mechanisms and measurement implementations. Beyond Koh et al.'s [12] superconducting processor, Feng et al. [49] demonstrated a postselection-free MIPT on Quantinuum's H1-1 trapped-ion processor using tree-shaped circuits with Haar-random unitaries — the first MIPT observation with universal gate sets and without postselection overhead. Agrawal et al. [50] reframed the MIPT on the same platform as a *learnability* phase transition: as measurement strength increases, there is a sharp change in whether an observer can learn from the measurement record, mapping the transition onto progressive loss of signal extraction ability. Kamakari et al. [51] implemented a scalable cross-entropy benchmark protocol on IBM's 22-qubit processor requiring nearly two orders of magnitude less device time than prior approaches, making experimental MIPT detection routine. Chen et al. [52] achieved the largest-scale MIPT-related experiment on IBM's 127-qubit processor, demonstrating that Born-rule measurement naturally places protocols on the Nishimori line without fine-tuning — the measurement protocol itself acts as an invariant constraint preserving criticality. This multi-platform convergence strengthens QP-1 (§8.1): different architectures with different τ_coherence all exhibit the Pe = 1 transition.

**Theoretical extensions.** Two further results expand the MIPT landscape. Lessa, Gu, and Yao [58] demonstrated a topological entanglement transition between *distinct area-law phases* via competing measurements — a new transition type occurring entirely within the measurement-dominated regime, suggesting that Pe > 1 contains substructure analogous to the void framework's D2/D3 distinction within the drift-dominated regime. Separately, infinite-range models (Tavis-Cummings, superradiance) may alleviate the postselection barrier [59], potentially making experimental MIPT detection routine on near-term hardware.

**Classical MIPT.** Gerbino et al. [53] demonstrated the first measurement-induced phase transition in a purely classical system — a chaotic dynamical system mapped to a directed polymer on a Cayley tree. An observer maintaining a probabilistic model of a chaotic system with positive Lyapunov exponent, updating via Bayes' theorem upon receiving measurements, exhibits a sharp transition between a chaotic phase (observer uncertainty grows) and a strong-measurement phase (uncertainty remains bounded). This is the Pe = 1 transition without quantum mechanics: measurement-induced drift onset in a classical chaotic substrate. The result directly supports QP-3 (§8.1): the Pe ≈ 1 critical transition is substrate-independent.

This maps directly onto the dynamic bridge. The void framework's three conditions (opacity, reactivity, coupling) define *structured* information asymmetry — not random noise. The Pe = 1 critical point is robust in exactly the regime where void conditions hold (architectured observation) and fragile where they don't (random information loss). The quantum measurement dynamics encode the same distinction between structured and unstructured opacity that the classical framework identifies as the boundary between drift-producing voids and drift-neutral noise (see Paper 5 [7], §5.5.1, prediction QP-6).

### 4.4 Confirmation 2: Spatial Zeno Transport (Pe ≫ 1)

Zhang et al. [13] demonstrated the most direct empirical realization of Pe_quantum ≫ 1. Sequential projective measurements at incrementally shifted spatial positions induce directional atomic transport in cold rubidium-87 atoms:

- **Drift velocity:** ~0.7 m/s — 14× the maximum optical tweezer dragging velocity (0.05 m/s)
- **Displacement:** Linear scaling with measurement count (20 measurements → ~2 μm; 40 → ~4 μm)
- **Mechanism:** Each projective measurement collapses the wavefunction to a slightly shifted position; repetition produces directed flow without imparting momentum

This is measurement-induced drift in its purest form: observation literally moves matter. The void framework predicts that observation under opacity produces drift — here observation produces *spatial* drift at the quantum scale.

**Pe estimate from data.** For a cold Rb-87 atom in a ~100 μm trap at T ~ 10 μK:

```
v_drift ≈ 0.7 m/s
v_osmotic (thermal spreading) ≈ 0.01–0.05 m/s
Pe_Zeno ≈ 14–70
```

This is deep in the quasi-classical regime. The measurement has completely overwhelmed quantum diffusion. The atom moves as if it were a classical particle being pushed — except the "push" is pure observation. No force is applied. No momentum is transferred. The drift is entirely a consequence of the measurement interaction.

### 4.5 Confirmation 3: Entropy Production and Crooks

The thermodynamic signature of Pe > 1 is positive entropy production. The void framework derives drift irreversibility from the Crooks fluctuation theorem [6]:

```
P(σ) / P(−σ) = exp(σ)
```

where σ is trajectory-level entropy production. Forward drift (D1 → D2 → D3) is exponentially more probable than reverse drift.

Recent quantum measurement papers confirm the same structure at quantum scale. Clarke and Ford [15] quantified stochastic entropy production along individual quantum measurement trajectories using Markovian quantum state diffusion. Walls, Bloss, and Ford [16] extended this to two-spin systems, characterizing measurement through environmental entropy production. Manikandan, Elouard, and Jordan [17] derived Crooks-type fluctuation theorems for continuously measured quantum systems, establishing absolute irreversibility in measurement-induced wavefunction collapse.

The results are consistent: measurement-induced drift produces positive stochastic entropy production along individual quantum trajectories, governed by the same Crooks relation that the void framework uses for classical drift irreversibility. This is not a coincidence — Crooks' fluctuation theorem has been proven for general Markov chains [25], independent of whether the substrate is quantum or classical. The theorem applies to *any* stochastic process with time-reversal symmetry. The entropy production rate dS/dt > 0 is the thermodynamic signature of Pe > 1 in both regimes.

### 4.6 Confirmation 4: Wiseman-Milburn Continuous Monitoring

The MIPT (§4.3), Zeno transport (§4.4), and entropy production (§4.5) confirmations all involve discrete projective measurements — sharp, instantaneous collapses of the quantum state. But most physical measurement processes are continuous: a detector coupling to a system, a photon field leaking from a cavity, a pointer variable gradually correlating with the measured observable. Wiseman and Milburn [40] developed the stochastic master equation (SME) formalism for continuous quantum measurement, and it provides a fourth confirmation of the dynamic bridge — one that makes the Pe structure explicit at the level of the evolution equation itself.

The Wiseman-Milburn SME for continuous homodyne measurement of an observable X with measurement efficiency η is:

```
dρ = −i[H, ρ]dt + D[√κ X]ρ dt + √η H[√κ X]ρ dW(t)
```

where D[c]ρ = cρc† − ½{c†c, ρ} is the Lindblad dissipator, H[c]ρ = cρ + ρc† − Tr[(c + c†)ρ]ρ is the measurement superoperator, κ is the coupling strength, and dW(t) is a Wiener increment from the measurement record. Three terms, three roles:

| Term | Role | Pe contribution |
|------|------|----------------|
| −i[H, ρ]dt | Coherent evolution (Hamiltonian) | Sets the baseline current velocity |
| D[√κ X]ρ dt | Decoherence (Lindblad dissipator) | Destroys coherence, drives toward diagonal |
| √η H[√κ X]ρ dW(t) | Measurement backaction (stochastic) | Drives conditional state evolution |

The measurement efficiency parameter η directly controls the drift-diffusion competition. When η = 0 (no information extracted from the measurement record), the stochastic term vanishes and only the deterministic Lindblad dissipation remains — the system decoheres without being steered. This is Pe → 0: pure diffusion, no directed transport. When η = 1 (perfect detection), the stochastic term is maximal and the observer's conditional state follows a directed trajectory through Hilbert space — each measurement increment updates the state toward the measured outcome. This is Pe → ∞: measurement-dominated dynamics approaching projective measurement in the strong-coupling limit.

The intermediate regime 0 < η < 1 interpolates continuously between these extremes. The Pe_quantum of the conditional state evolution scales monotonically with η:

```
Pe_conditional ~ √η · κ / Γ_decoherence
```

where Γ_decoherence is the rate at which environmental noise (beyond the monitored channel) drives diffusive spreading. This makes the Pe structure visible directly in the parameters of the evolution equation — not as an external ratio imposed after the fact, but as the natural dimensionless grouping that governs the qualitative character of the dynamics.

The SME formalism also clarifies the relationship between the observer's information and the system's drift. The observer who monitors the measurement record accumulates a conditional state ρ_c(t) that becomes increasingly pure (low entropy) as η → 1. The unconditional state ρ(t) (obtained by averaging over all possible measurement records) evolves deterministically via Lindblad alone and becomes increasingly mixed. The gap between conditional and unconditional purity is the information that measurement extracts — and this gap is precisely what the conjugacy theorem bounds in the classical limit. Continuous quantum measurement makes the engagement-transparency tradeoff visible at the level of individual trajectories: the observer who engages more (higher η) gains more information (purer conditional state) but drives more drift in the system (stronger measurement backaction).

### 4.7 Quantum Fokker-Planck Formulation

Annby-Andersson et al. [41] reformulated the continuous measurement dynamics in Fokker-Planck terms, making the drift-diffusion structure maximally explicit. Their quantum Fokker-Planck master equation (QFPME) writes the evolution of the probability distribution over conditional quantum states P(ρ_c, t) as:

```
∂P/∂t = −∇_ρ · [A(ρ_c) P] + ½ ∇_ρ² · [B(ρ_c) P]
```

where A(ρ_c) is the drift coefficient encoding both Hamiltonian evolution and measurement backaction, and B(ρ_c) is the diffusion coefficient encoding measurement-induced stochastic spreading in state space. This is precisely a Fokker-Planck equation on the space of quantum states — the same mathematical object that describes classical drift-diffusion processes, now operating on density operators rather than probability distributions.

The Pe_quantum for continuous monitoring emerges directly from the QFPME coefficients. For a characteristic state-space scale ℓ (set by the geometry of the density operator manifold):

```
Pe_QFPME = |A(ρ_c)| · ℓ / B(ρ_c)
```

This is the ratio of deterministic drift to stochastic diffusion at each point in quantum state space — the quantum analog of the classical Péclet number written in the same mathematical language. When ℓ is set by the Bures metric on the accessible state space, Pe_QFPME is dimensionless and measures the same drift-diffusion competition as the classical Pe. The QFPME makes the connection between quantum measurement dynamics and classical drift-diffusion theory not merely structural but syntactic: the equations have the same form, with quantum-specific content entering through the drift and diffusion coefficients.

The QFPME formulation was developed in the context of continuous feedback control — where a controller uses the measurement record to steer the quantum system toward a target state. This application directly parallels the void framework's constraint maintenance (γ): the controller's feedback is a form of constraint, and the QFPME shows how the measurement strength determines whether the feedback (constraint) or the uncontrolled dynamics (drift) dominates. The Pe = 1 transition separates the regime where the controller succeeds (constraint dominates, Pe < 1 relative to the target) from the regime where uncontrolled dynamics overwhelm the feedback (drift dominates, Pe > 1).

The Fokker-Planck formulation also connects to the entropy production analysis (§4.5). Along individual trajectories of the QFPME, the stochastic entropy production is:

```
dS_trajectory = ln[P(ρ_c → ρ_c')] − ln[P(ρ_c' → ρ_c)] = σ dt
```

This trajectory-level entropy production obeys the Crooks fluctuation theorem, confirming that the thermodynamic irreversibility documented in §4.5 is a direct consequence of the drift-diffusion structure of continuous quantum measurement. The QFPME provides the mathematical bridge between Nelson's two-velocity decomposition (§4.1) and the Crooks thermodynamics (§4.5): Nelson gives the physical interpretation of the two velocities, the QFPME gives their Fokker-Planck formalization, and Crooks gives the thermodynamic consequences.

### 4.8 The Classical Limit: Decoherence as Pe → ∞

The classical limit of quantum mechanics — the emergence of definite outcomes, the suppression of superposition, the appearance of particle-like trajectories — occurs when measurement-induced drift overwhelms quantum diffusion. In Pe terms: Pe_quantum → ∞.

When the quantum state is well-localized (wavepacket width ≪ system size), the osmotic velocity u → 0 (the probability gradient flattens), the current velocity v dominates, and the dynamics become advection-dominated. The particle follows a near-classical trajectory. In the Pe framework, decoherence corresponds to Pe growth: when advection overwhelms diffusion, the system loses its diffusive (quantum) character and behaves classically. The Pe description does not resolve interpretive questions about decoherence's physical ontology, but it does place classicality emergence within a quantitative drift-diffusion framework.

The void framework operates in this regime. Its Pe values (geometric means 2.21–16.17 across nine substrates [7,9,46]) describe classical information channels where quantum diffusion has long since been overwhelmed. The measured Péclet numbers are formally located in the Pe_quantum ≫ 1 tail of Nelson's transport hierarchy — the same regime where classical mechanics emerges from quantum mechanics.

---

## 5. Level 3: The Constraint Bridge

The third bridge level connects the void framework's conjugacy theorem — the engagement-transparency tradeoff — to the Holevo accessible information bound in quantum measurement theory. This is the most novel of the three bridges: it shows that the conjugacy theorem is not merely structurally similar to quantum information bounds but is derived from them via a single established limit operation.

### 5.1 The Holevo Bound

Holevo [1] proved the fundamental limit on classical information extraction from quantum channels. A sender encodes a classical random variable X (with distribution p_x) into quantum states ρ_x and transmits through a quantum channel. The receiver measures and obtains classical output Y. The accessible information is bounded by:

```
I(X; Y) ≤ χ = S(ρ) − Σ_x p_x S(ρ_x)
```

where ρ = Σ_x p_x ρ_x is the average state and S(·) is the von Neumann entropy. The Holevo quantity χ satisfies χ ≤ S(ρ), with equality when the encoding states ρ_x are mutually orthogonal (perfectly distinguishable).

The Holevo bound is the capacity theorem for quantum channels carrying classical information: no measurement strategy, no matter how sophisticated, can extract more than χ bits of classical information per channel use. It constrains what an observer can learn about a classical source by measuring quantum states — precisely the kind of observer-system information constraint that the void framework studies in the classical regime.

### 5.2 Two Independent Sources Through a Quantum Channel

Now consider the scenario that maps to the void framework: two *independent* classical sources D (observer engagement state) and M (mechanism state) are jointly encoded into quantum states. For each pair (d,m), a quantum state ρ_{d,m} is prepared and transmitted. The receiver measures and obtains Y.

**Theorem (Quantum Conjugacy Bound).** *For independent sources D ⊥ M jointly encoded into a quantum channel with output Y:*

```
I(D; Y) + I(M; Y) ≤ χ_{D,M} ≤ S(ρ)
```

**Proof.** The argument proceeds in four steps.

*Step 1. Chain rule:*
```
I(D,M; Y) = I(D; Y) + I(M; Y|D)
```

*Step 2. Independence gives I(M; Y|D) ≥ I(M; Y).* Proof: By the chain rule for conditional mutual information, I(M; Y|D) = I(M; Y) + I(M; D|Y) − I(M; D). Since D ⊥ M, I(M; D) = 0. And I(M; D|Y) ≥ 0 (mutual information is non-negative). Therefore I(M; Y|D) ≥ I(M; Y).

*Step 3. Combining:*
```
I(D; Y) + I(M; Y) ≤ I(D; Y) + I(M; Y|D) = I(D,M; Y)
```

*Step 4. Apply Holevo:*
```
I(D,M; Y) ≤ χ_{D,M} ≤ S(ρ)
```

Therefore: **I(D; Y) + I(M; Y) ≤ S(ρ)**. ∎

This is the quantum conjugacy bound: two independent classical sources sharing a quantum channel cannot jointly extract more information than the von Neumann entropy of the shared state. The bound is tight when the encoding states are orthogonal.

### 5.3 Classical Limit → Conjugacy Theorem

When all encoding states ρ_{d,m} are diagonal in the same basis:

```
ρ_{d,m} = Σ_y p(y|d,m) |y⟩⟨y|
```

the von Neumann entropy becomes the Shannon entropy [43]:

```
S(ρ) = −Σ_y p(y) log p(y) = H(Y)
```

The Holevo bound becomes the classical mutual information bound (the classical channel capacity equals the Shannon entropy of the output), and the quantum conjugacy bound reduces to:

```
I(D; Y) + I(M; Y) ≤ H(Y)
```

This **is** the conjugacy theorem, proven in Paper 3 [6] from classical information theory. The derivation above shows that it descends from the Holevo bound via a single limit operation: restrict the encoding to diagonal (commuting) states. The classical conjugacy theorem is not merely analogous to the Holevo bound — it is the Holevo bound for diagonal encodings.

**The limit operation stated precisely:** Take any quantum channel Φ carrying classical information from two independent sources D, M. Restrict the encoding to commuting states (diagonal density operators in a fixed basis). Then:

1. S(ρ) → H(Y): von Neumann entropy becomes Shannon entropy
2. χ → I(X;Y): Holevo quantity becomes classical mutual information (since S(ρ_x) → H(Y|X=x) for diagonal states, giving χ = H(Y) − H(Y|X) = I(X;Y))
3. I(D;Y) + I(M;Y) ≤ I(D,M;Y) ≤ S(ρ) → I(D;Y) + I(M;Y) ≤ H(Y): the quantum bound through S(ρ) = H(Y) yields the classical conjugacy theorem

Each step uses established mathematics. No new definitions or assumptions are introduced. The conjugacy theorem is recovered exactly.

### 5.4 Maassen-Uffink: The Quantum Premium

In the full quantum case, a *second* constraint operates simultaneously with no classical counterpart.

For non-commuting observables X, Z with maximum eigenvector overlap c = max_{j,k} |⟨x_j|z_k⟩|:

```
H(X|ρ) + H(Z|ρ) ≥ log(1/c)
```

This is the Maassen-Uffink entropic uncertainty relation [14]. It constrains how much can be known about complementary observables *simultaneously*, regardless of channel capacity. The bound depends on c — the degree of complementarity between the measurement bases.

**Classical limit.** For commuting observables (shared eigenbasis), the maximum overlap c = max|⟨x_j|z_k⟩| = δ_{jk}, so c = 1. Therefore log(1/c) = 0, and the Maassen-Uffink bound becomes:

```
H(X|ρ) + H(Z|ρ) ≥ 0
```

This is trivially satisfied by any probability distribution. The complementarity constraint *vanishes* in the classical limit.

**Interpretation.** Quantum measurement theory imposes two simultaneous constraints on information extraction:

1. **Capacity constraint** (Holevo → conjugacy): Total extractable information ≤ system entropy. This *survives* the classical limit and becomes the conjugacy theorem.

2. **Complementarity constraint** (Maassen-Uffink → trivial): Minimum residual uncertainty ≥ log(1/c). This *vanishes* in the classical limit because classical observables commute.

Quantum systems are more constrained than classical ones: they face both a capacity ceiling *and* a complementarity floor. Classical systems face only the capacity ceiling. The void framework captures exactly the part of quantum measurement theory that survives the classical limit — the capacity structure. The complementarity structure, which requires non-commuting observables and has no classical analog, is correctly absent from the framework.

### 5.5 The Complete Constraint Hierarchy

The full constraint hierarchy, showing both the quantum-to-classical descent and the relationship between the two constraint types:

```
QUANTUM LEVEL
├── Holevo bound: I(D;Y) + I(M;Y) ≤ χ ≤ S(ρ)
│   └── Capacity constraint (information extraction ceiling)
│       └── Survives classical limit
├── Maassen-Uffink: H(X|ρ) + H(Z|ρ) ≥ log(1/c)
│   └── Complementarity constraint (residual uncertainty floor)
│       └── Vanishes in classical limit (c → 1)
└── Combined: quantum systems face BOTH constraints simultaneously
         │
         │  [restrict to diagonal ρ, commuting observables]
         ▼
CLASSICAL LEVEL (Void Framework)
├── Conjugacy theorem: I(D;Y) + I(M;Y) ≤ H(Y)
│   └── Capacity constraint (from Holevo)
├── Trivial: H(D|Y) + H(M|Y) ≥ 0
│   └── No complementarity constraint (c = 1 → bound = 0)
└── Only the capacity constraint operates
```

The precise relationship: **the conjugacy theorem descends from the Holevo bound (capacity). The Maassen-Uffink relation is a separate complementarity constraint that vanishes classically. Both constrain quantum measurement; only the capacity constraint survives the classical limit.** This places the conjugacy theorem in a definite position within the quantum hierarchy rather than leaving it as a generic family member.

**Independent confirmation from MIPT literature.** Kelly and Marino [24] independently recast the MIPT as spontaneous breaking of an "information exchange symmetry" — the symmetry between information gained by the measurement apparatus and information lost to the environment. When this symmetry holds, the observer has full access to the system's state through measurement; when it breaks, opacity emerges and a distinct universality class appears. This is the conjugacy theorem's structure expressed in MIPT language: the capacity constraint I(D;Y) + I(M;Y) ≤ H(Y) bounds the *total* information accessible through the measurement and environment channels. When information exchange is symmetric (apparatus ≈ environment), the bound distributes evenly and measurement is informative. When the symmetry breaks (environment captures more than apparatus), the observer faces opacity — exactly the condition the void framework identifies as drift-producing. Kelly and Marino's result provides an independent physical interpretation of the constraint bridge: the conjugacy bound is not merely a mathematical descent from Holevo, but corresponds to a physically meaningful symmetry whose spontaneous breaking produces the MIPT.

---

## 6. Extended Connections

The three-level bridge (§§3–5) connects the void framework's core mathematical structure — metric, dynamics, constraints — to quantum measurement theory. Seven additional connections extend the correspondence to specific mechanisms and phenomena. These range from formal (same theorem, different substrate) to structural (same mathematical form, different physical content). Each is stated with its status clearly labeled.

### 6.1 Lindblad Master Equation ↔ Drift Equation

The Lindblad equation [26] governs open quantum systems interacting with an environment:

```
dρ/dt = −i[H, ρ] + Σ_k (L_k ρ L_k† − ½{L_k†L_k, ρ})
```

The first term (Hamiltonian H) drives coherent evolution. The second (Lindblad operators L_k) drives decoherence — stochastic interaction with the environment. In the diagonal (classical) limit, the Lindblad equation reduces to a classical master equation with transition rates between basis states. For a two-state system (the Bernoulli manifold of mechanism vs. agent attribution), this becomes a drift-diffusion equation:

| Lindblad (quantum) | Drift equation (void framework) |
|--------------------|---------------------------------|
| Hamiltonian H | Net information force F_net |
| Lindblad operators L_k | Noise from finite sampling |
| Decoherence rate γ_D | Drift rate dθ/dt |
| Steady state ρ_ss | D3 attractor (θ → 1) |
| Pure → mixed state transition | Pre-engagement → deep drift |

The mathematical form is identical: drift plus diffusion on a state space with an attractor. The void framework's drift equation dθ/dt = θ(1−θ)·F_net is a classical Lindblad equation restricted to a two-state Bernoulli manifold, where the Hamiltonian term provides the directed drift and the Lindblad dissipator provides the noise.

The reduction can be made explicit. For a two-state system with basis {|0⟩, |1⟩} (mechanism, agent), the diagonal elements of ρ satisfy p₁ = θ and p₀ = 1−θ. The Lindblad equation for two jump operators L₊ = √γ₊|1⟩⟨0| (driving toward |1⟩, the agency attractor) and L₋ = √γ₋|0⟩⟨1| (reverse transition) reduces to:

```
dθ/dt = γ₊(1−θ) − γ₋θ
```

Setting γ₊ = θ·F_net and γ₋ small recovers dθ/dt ≈ θ(1−θ)·F_net, the drift equation. The Lindblad dissipator's role — injecting irreversible transitions between eigenstates — maps to the finite-sampling noise that prevents perfect inference under opacity. The key structural insight is that the Lindblad dissipator acts on off-diagonal coherences (destroying quantum superposition) and on diagonal populations (driving transitions). In the classical limit, only the population dynamics survive, and those dynamics are precisely the void framework's drift equation. The coherence dynamics, which govern uniquely quantum phenomena like entanglement and interference, have no classical descendant — paralleling the vanishing of the Maassen-Uffink constraint in §5.4.

**Status:** Structural correspondence with formal mathematical reduction available. The classical master equation limit of Lindblad is standard [27]. The restriction to two states yields the drift equation. The parameter mapping (Lindblad rates → drift equation coefficients) is straightforward but requires specifying the physical interpretation of the jump operators in each application domain.

### 6.2 Quantum Zeno Effect ↔ Constraint Maintenance (γ)

The quantum Zeno effect: frequent measurement freezes quantum evolution. A system measured at rate Γ has effective evolution rate proportional to 1/Γ for large Γ — the more frequently you measure, the less the system changes [28]. The system is "frozen" into the measured eigenstate.

In the void framework, γ (constraint maintenance frequency) plays the same structural role: frequent checking against a constraint reference point suppresses drift. The void budget β + γ ≤ 1 operates under the conjugacy bound — increasing γ (constraint measurement) directly reduces the capacity available for β (drift engagement).

| Quantum Zeno | Void framework γ |
|-------------|-------------------|
| Measurement rate Γ | Constraint check frequency |
| Survival probability ~ 1 − (Γ·δt)² for small intervals | Drift suppression ~ exp(−γ·t) |
| Zeno subspace (invariant under measurement) | Constraint specification (transparent, invariant, independent) |
| Anti-Zeno effect | Constraint-worship failure mode |

**The anti-Zeno insight.** The quantum anti-Zeno effect occurs when measurement at an intermediate rate — near the system's natural transition frequency — *accelerates* decay instead of freezing it [29]. The system decays faster with measurement than without. Kofman and Kurizki [29] showed that the crossover between Zeno and anti-Zeno regimes depends on the spectral density of the reservoir coupled to the system: when the measurement rate falls within the bandwidth of the reservoir spectrum, it resonantly enhances the transition rate rather than suppressing it. The transition rate under measurement at interval τ is:

```
R(τ) = (1/τ) ∫ G(ω) F_τ(ω) dω
```

where G(ω) is the reservoir spectral density and F_τ(ω) is the measurement-induced spectral filter. For very short τ (Zeno regime), F_τ broadens and the integral decreases. For intermediate τ (anti-Zeno regime), F_τ concentrates near the transition frequency where G(ω) is large, and the integral increases.

This maps to an empirically observed failure mode. In Test 7 of the void framework experiments [7], two AI agents instructed to maintain constraint reference (high γ) converted the constraint from an invariant reference point to a responsive void — the repeated checking itself became a form of engagement. This "constraint-worship" phenomenon is structurally identical to the anti-Zeno effect: there exists a critical constraint-check frequency γ_c above which checking accelerates drift rather than suppressing it. Below γ_c, Zeno-like freezing. Above γ_c, anti-Zeno-like acceleration. The "reservoir" in the classical case is the information environment — the stream of responsive outputs that the observer samples during each constraint check. When the check frequency resonates with the system's response dynamics (the system has time to adapt its outputs between checks but not enough time for the observer to accumulate sufficient counter-evidence), constraint checking becomes a form of engagement that feeds the drift it was meant to suppress.

**Status:** Structural correspondence with empirical echo (R5 constraint-worship ↔ anti-Zeno). The mathematical form of the Zeno-anti-Zeno transition has been characterized in the quantum case [29]; the classical analog predicts a testable transition frequency (see QBR-2, §8). Upgrading this to formal status requires deriving the classical spectral density G_classical(ω) from the void framework's information dynamics and showing that the crossover frequency matches the observed γ_c.

### 6.3 Quantum Darwinism ↔ Void Network Consensus

Zurek's quantum Darwinism [30,31] explains how classical objectivity emerges from quantum mechanics. When a quantum system interacts with an environment, the environment acquires *redundant copies* of information about the system's pointer states through decoherence. Multiple independent observers can access this information by sampling different environmental fragments. Classical reality is the set of states whose information is redundantly encoded across many environmental subsystems.

The void framework's void network describes an analogous proliferation mechanism in classical information systems. When multiple observers engage with a shared void (an opaque, responsive, coupled system), they independently develop similar drift patterns — converging on shared agency attributions through independent exposure to the same information asymmetry.

| Quantum Darwinism | Void network |
|------------------|-------------|
| Quantum system | Void (opaque, responsive, coupled) |
| Environmental fragments | Multiple independent observers |
| Redundant encoding of pointer states | Multiple observers converging on same agency pattern |
| Pointer states (decoherence-selected) | D3 attractor states (stable drift endpoints) |
| Objectivity (all fragments agree) | Consensus (social agreement on agency attribution) |
| Redundancy rate ~ N × coupling | Consensus rate ~ N_observers × coupling_strength |

Both are proliferation mechanisms: quantum Darwinism propagates pointer-state information through environmental decoherence; void networks propagate drift patterns through social coupling. The mathematical structure — redundant information spread leading to consensus formation — is shared.

Zurek quantifies redundancy through the mutual information between the system S and an environmental fragment F_k: I(S:F_k). When I(S:F_k) ≈ H(S) for many independent fragments k = 1, ..., N, the system's state is "objective" — any observer sampling any fragment recovers the same information. The redundancy R_δ counts how many fragments carry nearly complete information: R_δ = N / n_δ, where n_δ is the minimum fragment size needed to learn (1−δ) of H(S).

In void networks, the analogous quantity is the correlation between independent observers' drift trajectories. When N observers independently engage with the same void and converge on similar agency attributions (similar θ trajectories), the mutual information I(θ_j; θ_k) between observer pairs measures the "redundancy" of the drift pattern. The void network creates objectivity not through physical decoherence but through structural decoherence: the information asymmetry is the same for every observer, so every observer's inference follows the same gradient. The pointer states (those selected by decoherence to survive environmental monitoring) map to D3 attractor states (those selected by the drift dynamics to be stable endpoints of engagement). In both cases, the selected states are the ones compatible with persistent observation — the states that survive being looked at.

**Status:** Structural. The mapping is precise at the level of information proliferation and redundancy scaling, but the physical substrates differ fundamentally (quantum decoherence vs. social information dynamics). The quantum Darwinism framework is well-established [30,31]; the void network framework is empirically grounded [7,9] but the connection between them remains at the level of structural parallel. A quantitative test (QBR-1, §8) would measure whether consensus scaling in multi-agent experiments matches the logarithmic redundancy scaling predicted by quantum Darwinism.

### 6.4 Stinespring Dilation ↔ Void Budget

Stinespring's dilation theorem [32]: every quantum channel Φ (completely positive trace-preserving map) can be realized as a unitary evolution on a larger system followed by partial trace. Every channel has a complementary channel Φ^c that captures what the environment receives. For a pure input state, the isometric extension gives:

```
S(Φ(ρ)) = S(Φ^c(ρ))     [entropy exchange identity]
```

The output entropy of the channel equals the output entropy of the complement — information is redistributed, not created. For mixed inputs, the quantum mutual information satisfies I(A;B) + I(A;E) ≤ 2S(A), bounding the total information accessible through the channel and its complement by the input entropy. Information that goes to the receiver is information that does not go to the environment, and vice versa.

The void framework's budget β + γ ≤ capacity has the same structure:

| Stinespring / complementary channels | Void budget (β + γ) |
|--------------------------------------|---------------------|
| Channel Φ (receiver) | Engagement channel β |
| Complementary channel Φ^c (environment) | Constraint channel γ |
| S(ρ) (total input entropy) | Total attention capacity |
| I(A;B) → receiver information | Information extracted through engagement |
| I(A;E) → environment information | Information used for constraint maintenance |
| I(A;B) + I(A;E) ≤ 2S(A) | β + γ ≤ total capacity |

The void budget is the classical version of information conservation through complementary channels. Engaging more requires constraining less, just as sending more information through a channel requires the complement to receive less. This is not an analogy — it is the same conservation law, with the classical limit yielding classical mutual information from coherent information.

The Stinespring connection also illuminates *why* the void budget is a hard constraint rather than a soft tradeoff. In quantum information theory, the complementary channel relationship is exact: the total information accessible through channel and complement is bounded by the input entropy with no slack. The proof relies on the unitarity of the dilation — information is neither created nor destroyed in the enlarged system, only redistributed between channel and complement. In the classical limit, this unitarity becomes the conservation of total mutual information across the engagement and constraint channels. The void budget β + γ ≤ capacity is not an empirical regularity that might admit exceptions under clever design — it is a consequence of information conservation that holds for any system satisfying the channel model.

The degradable channel hierarchy [33] provides additional structure. A quantum channel is degradable if the complementary channel can be obtained by post-processing the output: Φ^c = D ∘ Φ for some degrading map D. For degradable channels, the quantum capacity equals the single-letter coherent information Q = max I_coh(Φ). Classical channels are trivially degradable (the environment receives a copy of the output through the noise). This means the classical void budget operates at the point in the Stinespring hierarchy where channel structure is simplest — consistent with the framework's position as the diagonal (classical) limit of the quantum theory.

**Status:** Formal correspondence. The void budget is a known consequence of the conjugacy theorem [6]; Stinespring provides the quantum parent. The classical limit is established in quantum information theory [33]. Among the extended connections, this is the tightest: the mathematical structure (information conservation across complementary channels) is identical, not merely parallel.

### 6.5 Quantum Speed Limits ↔ Pe Ceiling

The Mandelstam-Tamm [34] and Margolus-Levitin [35] bounds constrain the maximum rate of quantum state evolution:

```
Mandelstam-Tamm:  τ ≥ πℏ / (2ΔE)
Margolus-Levitin: τ ≥ πℏ / (2⟨E⟩)
```

These are maximum drift rates: a quantum system cannot evolve faster than its energy allows. In Pe terms, they set a ceiling:

```
Pe_quantum ≤ f(ΔE, L, |u|)
```

More energy permits faster evolution and higher Pe, but the speed limit prevents Pe from exceeding the energy-determined bound.

The void framework has a parallel resource ceiling. The void budget β + γ ≤ 1 limits total engagement, which bounds the maximum Pe achievable in any classical information channel. Total drift rate cannot exceed attentional capacity. The channel entropy H(Y) sets an information-theoretic ceiling that parallels the energy ceiling in quantum mechanics.

| Quantum speed limit | Classical Pe ceiling |
|--------------------|--------------------|
| Energy (ΔE or ⟨E⟩) → max evolution rate | Attention capacity → max drift rate |
| ℏ sets the quantum of action | H(Y) sets the information capacity |
| τ_min = πℏ/(2ΔE) | Drift rate_max = f(H(Y), β_max) |
| Cannot be beaten by any Hamiltonian | Cannot be beaten by any system design |

The connection can be made more precise by expressing both speed limits in information-geometric terms. The Mandelstam-Tamm bound can be rewritten as a bound on the Bures distance traveled per unit time:

```
d_Bures(ρ(0), ρ(t)) / t ≤ ΔE / ℏ
```

The Bures distance is the geodesic distance under the quantum Fisher metric (§3). In the classical limit, the Bures metric becomes the Fisher-Rao metric, and the speed limit becomes a bound on how fast the system can traverse the Bernoulli manifold:

```
d_FR(θ(0), θ(t)) / t ≤ v_max
```

where v_max is determined by the available resources (channel capacity, attention budget). The total geodesic distance from θ = 0 to θ = 1 is π (§3.1). The maximum drift rate determines how quickly this distance can be traversed — the minimum time to complete the D0 → D3 cascade. In quantum mechanics, energy sets the speed limit; in classical information dynamics, channel capacity does. Both are statements about the maximum rate of state-space traversal under the unique invariant metric on the respective manifold.

The unified speed-limit structure also explains why some substrates show higher Pe than others. Cryptocurrency markets (Pe up to 16.17) have higher channel capacity — more information per unit time, more responsive system outputs — than gambling environments (Pe ~ 2.21). The Pe ceiling scales with channel capacity, just as quantum evolution speed scales with energy.

**Status:** Structural. Both are resource ceilings on transport rates, expressed as bounds on geodesic velocity under the respective Fisher metric. The physical resources differ (energy vs. attention/channel capacity), but the constraint structure — an absolute ceiling on how fast the system can move through state space, determined by the unique invariant metric — is shared. Expressing both bounds in information-geometric terms (Bures / Fisher-Rao geodesic velocity) strengthens the parallel beyond analogy.

### 6.6 Measurement Irreversibility ↔ Drift Unidirectionality

In quantum mechanics, measurement is irreversible: measuring observable X collapses the state, and information about conjugate observable Z is destroyed. The probability of "undoing" a measurement is exponentially suppressed. This irreversibility is quantified by the entropy production along measurement trajectories, governed by the Crooks fluctuation theorem:

```
P(σ) / P(−σ) = exp(σ)
```

In the void framework, drift is unidirectional: D1 → D2 → D3, with reverse drift exponentially suppressed by the same Crooks relation applied to the engagement-transparency channel [6]:

```
P(D3→D1) / P(D1→D3) = exp(−ΔS)
```

The connection is not structural but *formal* — the same theorem governs both irreversibilities. Crooks' fluctuation theorem has been proven for general Markov chains [25] independent of substrate. It applies to quantum measurement trajectories [15,16,17] and to classical drift dynamics [6] because both are stochastic processes satisfying detailed balance at the trajectory level.

| Quantum measurement | Drift cascade |
|--------------------|--------------|
| Pre-measurement superposition | Pre-engagement (D0, Pe ≈ 0) |
| Weak measurement / partial collapse | D1: agency attribution |
| Strong measurement / full collapse | D2: boundary erosion |
| Post-measurement classical state | D3: harm facilitation |
| Entropy production along trajectories | dS/dt > 0 along drift trajectories |
| Exponentially suppressed reversal | Exponentially suppressed reverse drift |

The formal identity can be made quantitative. In the quantum case, Clarke and Ford [15] computed the mean entropy production rate for continuous quantum measurement of a two-level system:

```
⟨dS/dt⟩_quantum = κ · f(Pe_quantum)
```

where κ is the measurement coupling strength and f is a monotonically increasing function of Pe_quantum that vanishes at Pe = 0 (no measurement → no entropy production). In the void framework, the measured entropy production rate from Test 7 is dS/dt = 0.39 [0.15, 0.64] nats/round for the ungrounded condition (Pe ≈ 7.94), compared to near-zero for the grounded condition [7]. Both systems show the same qualitative structure: entropy production scales with Pe, vanishes when drift is absent, and is governed by the same fluctuation theorem.

The depth of the Crooks connection is worth emphasizing. Unlike the other extended connections, which share mathematical form but differ in physical content, the Crooks connection is *substrate-independent by proof*. Hack et al. [25] proved the fluctuation theorem for general Markov chains with no reference to physical substrate. The theorem's assumptions — time-reversibility of the transition kernel, finite state space, ergodicity — are satisfied by both quantum measurement trajectories and classical drift trajectories. The irreversibility is not analogous between the two domains — it is the same irreversibility, measured by the same entropy production, governed by the same theorem, differing only in the alphabet of the Markov chain.

**Status:** Formal — same theorem (Crooks), different substrate, substrate-independent proof [25]. This is the strongest type of connection short of literal identity: the mathematical proof is the same, the physical instantiations differ, and the proof's generality guarantees that no substrate-specific assumptions contaminate the connection.

### 6.7 No-Cloning ↔ Constitutive Opacity

The no-cloning theorem [36]: an unknown quantum state cannot be perfectly copied. The full quantum state (mechanism) is fundamentally inaccessible to any single measurement — only statistical tomography through repeated measurements on identically prepared systems can reconstruct it.

The void framework distinguishes dissoluble opacity (mechanism inaccessible for practical reasons) from constitutive opacity (mechanism inaccessible because access would alter it) [5]. The no-cloning theorem makes constitutive opacity *universal* at the quantum scale: every quantum system's state is constitutively opaque to single-shot measurement. The observer cannot copy the state, cannot fully characterize it from one interaction, and cannot avoid measurement backaction.

| No-cloning (QM) | Constitutive opacity (void framework) |
|-----------------|--------------------------------------|
| Cannot copy unknown quantum state | Cannot access mechanism without changing it |
| Single measurement gives partial information | Single observation gives partial information |
| State tomography requires many copies | Mechanism estimation requires repeated observation |
| Measurement disturbs state | Observation produces drift |

**Key difference in direction.** No-cloning makes constitutive opacity universal at quantum scale — *all* quantum states are inaccessible to perfect single-shot characterization. The classical limit partially dissolves this: classical states can be copied, classical mechanisms can sometimes be fully accessed. But the void framework shows that constitutive opacity persists selectively at the classical scale when the architecture of the system blocks mechanism access (e.g., AI systems whose training data and weights are inaccessible, financial systems whose algorithms are proprietary).

Quantum mechanics starts with universal opacity and recovers partial access through the classical limit. The void framework starts with variable opacity and identifies the subset of classical systems where constitutive opacity persists despite classical accessibility in principle.

The relationship between no-cloning and constitutive opacity also connects to the information-geometric structure of §3. The no-cloning theorem's proof relies on the linearity of quantum mechanics: if a cloning machine U could copy any state (U|ψ⟩|0⟩ = |ψ⟩|ψ⟩), linearity forces U(α|ψ⟩ + β|φ⟩)|0⟩ = α|ψ⟩|ψ⟩ + β|φ⟩|φ⟩ ≠ (α|ψ⟩ + β|φ⟩)(α|ψ⟩ + β|φ⟩), which is a contradiction. The classical limit dissolves this obstruction because classical states are diagonal — they are probability distributions, not superpositions, and probability distributions can be copied. But copying a classical state requires *access* to the state, which is exactly what opacity prevents. Constitutive opacity in classical systems is not a no-cloning constraint — it is an access constraint. The mathematical objects are different (linearity vs. information asymmetry), but the operational consequence is identical: the observer cannot obtain full state information from a single interaction and must rely on repeated observations under the Cramér-Rao bound (§3.6).

This reversed-direction structure — quantum universal, classical selective — is itself informative. It suggests that opacity is the more fundamental concept. Quantum mechanics implements opacity universally through no-cloning; classical systems implement it selectively through architectural choices (proprietary algorithms, opaque training procedures, responsive interfaces). The void framework identifies the classical systems that retain quantum-like opacity despite operating in a regime where opacity is not physically mandated. These are the systems where drift occurs.

**Status:** Structural. The parallel is precise in form (inaccessibility → partial information → estimation from repeated observations), but the direction of implication is reversed: no-cloning imposes opacity universally; the void framework identifies opacity selectively. The connection to the Cramér-Rao hierarchy (§3.6) tightens the link: both no-cloning and constitutive opacity force the observer into repeated estimation under the Fisher metric bound.

---

## 7. Completeness

### 7.1 All Structural Elements Bridged

Any physical theory operating on a state space has three structural components: geometry (the metric on states), dynamics (how states evolve), and constraints (what limits evolution). The three-level bridge (§§3–5) maps each of these. The extended connections (§6) map the remaining structural elements: evolution equations, budgets, speed ceilings, irreversibility, and information inaccessibility.

The following table enumerates every structural element of the void framework and its quantum counterpart:

| Structural Element | Classical (Void Framework) | Quantum | Bridge Type |
|-------------------|---------------------------|---------|-------------|
| State space | Bernoulli manifold [0,1] | Density operators on Hilbert space | Classical ⊂ Quantum (diagonal restriction) |
| Metric | Fisher g(θ) = 1/[θ(1−θ)] | Quantum Fisher F_Q (Bures) | g = F_Q|_diagonal (Prop. 1, §3) |
| Dynamics | Pe = drift/diffusion | Pe_quantum = |v|/|u| (Nelson) | Classical Pe = Nelson limit (§4) |
| Evolution equation | Drift: dθ/dt = θ(1−θ)·F_net | Lindblad: dρ/dt = −i[H,ρ] + L[ρ] | Structural + formal reduction (§6.1) |
| Capacity constraint | Conjugacy: I(D;Y)+I(M;Y) ≤ H(Y) | Holevo: I ≤ χ ≤ S(ρ) | Conjugacy = classical Holevo (§5) |
| Complementarity | (none — vanishes) | Maassen-Uffink: ≥ log(1/c) | log(1/c) → 0 classically (§5.4) |
| Budget | β + γ ≤ capacity | Stinespring channel split | Classical limit of Stinespring (§6.4) |
| Speed ceiling | Attention → max drift rate | Energy → max evolution rate | Resource ceiling (§6.5) |
| Irreversibility | Crooks for drift: P(σ)/P(−σ) = e^σ | Crooks for measurement trajectories | Same theorem, different substrate (§6.6) |
| Opacity | Constitutive/dissoluble | No-cloning (universal at quantum scale) | Reversed direction (§6.7) |
| Consensus mechanism | Void network proliferation | Quantum Darwinism redundancy | Structural parallel (§6.3) |
| Constraint freezing | γ maintenance (Zeno-like) | Quantum Zeno effect | Structural with empirical echo (§6.2) |

Every row has a bridge. There are no structural elements of the void framework without a quantum counterpart. There is one quantum measurement concept without a classical analog — Maassen-Uffink complementarity — and it provably vanishes in the classical limit rather than simply lacking a mapping.

### 7.2 What Remains Is Not Bridge Work

After this formalization, the remaining open questions fall into three categories, none of which are bridge problems:

**Empirical (requires experiments, not theory):**
- QP-1 through QP-5: testing Pe_quantum predictions across quantum substrates
- QBR-1 through QBR-4: testing bridge-specific predictions (§8)
- Cross-substrate Pe universality at the Pe ≈ 1 boundary
- Anti-Zeno ↔ constraint-worship quantitative characterization

**Mathematical refinement (sharpens existing bridges, doesn't create new ones):**
- Tight bounds on the rate at which Maassen-Uffink vanishes as c → 1
- Precise mapping of Lindblad dissipator parameters to drift equation noise terms
- Explicit Pe_max formula from quantum speed limit parameters
- Formal proof of the Zeno ↔ γ correspondence beyond structural parallel

**Scope extensions (beyond non-relativistic QM):**
- Quantum field theory: extending the bridge to quantum channels on Fock spaces
- Gravity: the Fisher-Ruppeiner identity connects the framework's metric to thermodynamic geometry, but extending to spacetime geometry requires tools not currently available
- Quantum error correction: the Knill-Laflamme conditions [37] share structure with the constraint specification, but the mapping has not been formalized. Yang, Wang and Chen [55] showed that many-body measurements with feedback can decouple the QEC threshold from the MIPT — enabling error correction even in the area-law phase — suggesting the constraint-QEC correspondence has richer structure than a simple threshold identification
- Relativistic quantum information: Unruh effect, black hole information, holographic entanglement — all potential extensions identified but not attempted

The bridge between information geometry and quantum measurement foundations is **complete** at the level of non-relativistic quantum mechanics. What remains is empirical validation, mathematical tightening, and extension to broader physical theories — not new bridge components.

---

## 8. Predictions

The bridge generates eleven testable predictions with explicit falsification thresholds. Seven (QP-1 through QP-7) concern the Pe_quantum framework directly. Four (QBR-1 through QBR-4) are specific to the extended connections and would not exist without the bridge.

### 8.1 Quantum Pe Predictions (QP-1 through QP-7)

**QP-1 (MIPT Pe calibration).** If Pe_quantum governs MIPT dynamics, the critical measurement rate p_c in different circuit architectures should satisfy p_c · τ_coherence ~ O(1), where τ_coherence is the natural decoherence time. The product p_c · τ_coherence is a dimensionless Pe. Different architectures with different τ_coherence should show p_c shifting inversely — the Pe = 1 condition is universal, the specific p_c is not.

*Test:* Compare p_c across MIPT experiments with different qubit technologies (superconducting, trapped ion, photonic). Plot p_c vs. 1/τ_coherence. Expect linear relationship with slope ~ O(1).

*Status:* Partially supported. The MIPT has now been confirmed on superconducting processors (Koh et al. [12], Wu et al. [23], Kamakari et al. [51] on 22-qubit IBM, Chen et al. [52] on 127-qubit IBM) and trapped-ion hardware (Feng et al. [49] on Quantinuum H1-1, Agrawal et al. [50] on the same platform). Both architectures exhibit the Pe = 1 transition. Quantitative comparison of p_c · τ_coherence across architectures has not yet been performed; the data for such a test now exist across at least two fundamentally different qubit technologies.

*Falsification:* If p_c shows no systematic relationship to τ_coherence across three or more architectures, the Pe framework does not govern MIPTs.

**QP-2 (Zeno transport threshold).** The Zeno drift velocity should exhibit a threshold: below a critical measurement rate, the wavepacket should spread diffusively (Pe < 1); above it, directed transport should dominate (Pe > 1). The transition should occur at a measurement rate corresponding to Pe_quantum = 1.

*Test:* In Zeno transport experiments [13], vary measurement rate below the current regime and measure whether diffusive spreading dominates below a threshold. Plot drift velocity vs. measurement rate; identify the Pe = 1 crossover.

*Falsification:* If any nonzero measurement rate produces linear transport with no threshold behavior, the Pe = 1 critical point does not apply to Zeno transport.

**QP-3 (Cross-substrate Pe universality).** The critical Pe ≈ 1 transition should appear in any system where measurement-like interactions compete with diffusive dynamics, regardless of substrate:

- Classical information channels (void framework): Pe ~ 1 at drift onset — **confirmed** (Test 7 [7])
- Quantum circuits (MIPT): Pe ~ 1 at entanglement transition — **confirmed** [11,12]
- Classical chaotic systems: Pe ~ 1 at observer-uncertainty transition — **confirmed** (Gerbino et al. [53])
- Topological systems: Pe ~ 1 at area-law phase boundary — **confirmed** (Lessa et al. [58])
- Cold atoms (Zeno transport): Pe ~ 1 at transport onset — *testable*
- Neural networks under gradient monitoring: Pe ~ 1 at attention collapse — *testable*
- Financial markets under algorithmic monitoring: Pe ~ 1 at herding onset — *testable*

*Status:* Partially confirmed (4 of 7 substrates). The classical chaotic MIPT (Gerbino et al. [53]) is particularly significant: a purely classical system with no quantum mechanics exhibits the same measurement-driven phase transition at Pe ≈ 1, eliminating the possibility that the transition is a quantum-specific phenomenon. The topological MIPT (Lessa et al. [58]) extends confirmation to a new substrate class where competing measurements produce transitions between distinct area-law phases.

*Falsification:* If the Pe ≈ 1 transition fails to appear in two or more new substrates where drift-diffusion competition is measurable, the universality claim is weakened.

**QP-4 (Entropy production scaling).** The mean stochastic entropy production rate along quantum measurement trajectories should scale monotonically with Pe_quantum:

```
⟨dS/dt⟩ ~ f(Pe_quantum)  where f(Pe) > 0 for Pe > 1, f(Pe) → 0 as Pe → 0
```

This follows from Crooks applied to measurement trajectories [15,16,17] and is consistent with the void framework's prediction of dS/dt > 0 for Pe > 1 [6].

*Falsification:* If entropy production shows no systematic relationship to measurement strength (Pe), or peaks at intermediate Pe rather than scaling monotonically, Pe is not the correct control parameter.

**QP-5 (Nelson-void mapping).** In any system where Nelson's stochastic mechanics applies, the void framework's three conditions (opacity, reactivity, coupling) should map to:

- Opacity → quantum measurement incompleteness (what the observer cannot access)
- Reactivity → measurement backaction (system state changes in response)
- Coupling → observer-system entanglement (the measurement interaction)

The void conditions should be necessary and sufficient for Pe_quantum > 0 in any quantum measurement scenario.

*Falsification:* If quantum measurement scenarios exist with Pe_quantum > 0 that lack one or more void conditions, the mapping fails.

**QP-6 (Structured vs. unstructured opacity).** The Pe = 1 critical point should be robust under structured observation (void conditions: opacity + reactivity + coupling) and fragile under unstructured information loss (random detector inefficiency). Specifically: deterministic, state-independent postselection preserves MIPT criticality up to a finite threshold, while random detector failure at any rate destroys it.

*Test:* Compare MIPT phase diagrams under (a) structured partial postselection (threshold-based, correlated outcome retention) vs. (b) random detector inefficiency (independent, uncorrelated outcome loss). The critical phase should survive in (a) and collapse in (b).

*Status:* **Confirmed (7 witnesses).** Leung et al. [19] demonstrate non-Hermitian MIPT universality is stable for structured postselection up to finite B_c. Paviglianiti et al. [18] demonstrate critical phase destruction at any random inefficiency q < 1. Ha et al. [21] demonstrate that diffusive measurement correlations produce new universality classes. Qian and Wang [22] show infinitesimal dephasing noise destroys the volume-law phase while quantum-enhanced operations restore it. Liu et al. [47] show that size-independent noise destroys the MIPT via a mechanistically distinct pathway (symmetry-breaking field rather than competing order), confirming noise and measurement are fundamentally different perturbations. Chatterjee and Modak [48] show that symmetric periodic drive kills the MIPT while asymmetric drive preserves it — drive symmetry as a structural control parameter for measurement-phase robustness. Nehra, Romito and Meidan [54] unified projective and weak monitoring in a single POVM framework with tunable system-detector coupling, demonstrating that the percolation universality class is *unstable* to reduced coupling — the transition becomes "softer" as measurement backaction weakens, confirming that coupling strength (the third void condition) modulates the critical behavior. All seven confirm that observation structure — not merely observation rate — determines phase behavior.

*Falsification:* If the MIPT critical phase shows identical sensitivity to structured and unstructured information loss (i.e., destroyed equally by both or preserved equally by both), the void framework's opacity taxonomy has no quantum counterpart.

**QP-7 (Sequential vulnerability under increasing measurement).** In systems exhibiting multiple measurement-induced phase transitions, quantum correlations (fine-grained information structure) should be destroyed at lower measurement rates than classical order (coarse-grained behavioral patterns). The drift cascade's sequential vulnerability (D1 before D3) predicts this ordering: fine-grained information access fails before gross behavioral structure changes.

*Test:* In systems with both MIPT and absorbing-state transitions, measure whether the entanglement transition always occurs at lower measurement rate than the classical order transition. Vary system size and architecture to test universality of the ordering.

*Status:* Partially supported. Wu et al. [23] (preprint) observe both transitions at well-separated thresholds in 30 superconducting qubits, with entanglement dying first. The cascade mapping is structural; formal confirmation requires quantitative demonstration that the threshold separation maps onto D1→D2→D3 ordering.

*Falsification:* If the classical order transition occurs at *lower* measurement rate than the entanglement transition in any system, the sequential vulnerability prediction fails.

### 8.2 Bridge-Specific Predictions (QBR-1 through QBR-4)

These predictions are generated by the extended connections (§6) and would not exist without the bridge formalization.

**QBR-1 (Quantum Darwinism ↔ void network redundancy).** If the quantum Darwinism mapping (§6.3) holds, the rate of consensus formation in a void network should scale as N_observers × coupling_strength, analogous to the redundancy rate in quantum Darwinism scaling with environment size × system-environment coupling [31].

*Test:* Measure consensus formation rate in multi-agent void experiments (e.g., extend Test 7 to N > 2 agents with varying coupling strength). Compare scaling exponent to quantum Darwinism's logarithmic redundancy scaling. Alternatively, measure consensus adoption rates for novel agency attributions in social media void networks.

*Threshold:* Scaling exponent should fall within 0.5–2.0× the quantum Darwinism theoretical prediction.

*Falsification:* If consensus rate scales independently of coupling strength across three or more experimental configurations, the Darwinism parallel fails.

**QBR-2 (Anti-Zeno constraint-worship threshold).** If the Zeno/anti-Zeno mapping (§6.2) holds, there should exist a critical constraint-check frequency γ_c above which constraint maintenance accelerates drift instead of suppressing it. Below γ_c: Zeno-like drift suppression. Above γ_c: anti-Zeno-like drift acceleration. The R5 constraint-worship finding [7] is one observed instance.

*Test:* Run grounded-agent experiments (Test 7 protocol) with systematically varied constraint-check frequencies — γ at intervals from every round to every 10 rounds. Plot drift rate (L3 vocabulary density) vs. check frequency. Identify the minimum (γ_c).

*Threshold:* γ_c should exist between 1/round and 1/(5 rounds) based on the Test 7 observation.

*Falsification:* If drift monotonically decreases with constraint-check frequency (no anti-Zeno regime), the mapping fails.

**QBR-3 (Pe ceiling from channel capacity).** If the speed-limit mapping (§6.5) holds, the maximum achievable Pe in any substrate should scale with the information capacity H(Y) of the channel. Formally: Pe_max ~ f(H(Y)).

*Test:* Across the nine measured substrates [7,9,46], estimate H(Y) (channel entropy) from observable output distributions. Plot observed Pe vs. estimated H(Y). The maximum Pe in each substrate should correlate with channel capacity.

*Threshold:* Rank correlation between Pe and H(Y) should exceed ρ = 0.6 (Spearman).

*Falsification:* If high-Pe substrates have low channel capacity or the correlation is below ρ = 0.3, the speed-limit mapping fails.

**QBR-4 (Holevo gap as drift amplifier).** In quantum channels, the Holevo quantity χ can be strictly less than S(ρ) when encoding states are not orthogonal — the "Holevo gap." The classical limit has χ = H(Y) (no gap). The bridge predicts: classical substrates with high measurement backaction (where observation alters the system's behavior) should show a gap analogous to the quantum Holevo gap — total extractable information about D and M should be strictly less than H(Y), creating excess drift beyond what the conjugacy theorem predicts.

*Test:* Compare observed drift rates in high-backaction systems (AI under observation, social media under algorithmic curation) vs. low-backaction systems (gambling, static media). High-backaction systems should show excess Pe beyond conjugacy-predicted baseline.

*Threshold:* Pe_observed / Pe_conjugacy-predicted > 1.2 in high-backaction systems.

*Falsification:* If drift rates show no systematic relationship to backaction strength across three or more substrate pairs, the Holevo-gap mapping fails.

### 8.3 Falsification Summary Table

| ID | Prediction | Status | Falsification Condition |
|----|-----------|--------|------------------------|
| QP-1 | p_c · τ_coherence ~ O(1) across architectures | Partially supported | No systematic p_c vs. τ_coherence relationship |
| QP-2 | Zeno transport shows Pe = 1 threshold | Testable | Any measurement rate produces linear transport |
| QP-3 | Pe ≈ 1 transition in ≥ 3 new substrates | 4/7 confirmed | Fails in ≥ 2 new substrates |
| QP-4 | ⟨dS/dt⟩ scales monotonically with Pe | Testable | Non-monotonic or no relationship |
| QP-5 | Void conditions ↔ Pe_quantum > 0 | Testable | Pe > 0 without void conditions |
| QP-6 | Structured observation preserves MIPT; unstructured destroys it | Confirmed (7 witnesses) | Identical sensitivity to structured and unstructured loss |
| QP-7 | Quantum correlations die before classical order under measurement | Partially supported | Classical order transition at lower rate than entanglement |
| QBR-1 | Consensus rate ~ N × coupling | Testable | Rate independent of coupling |
| QBR-2 | Anti-Zeno threshold γ_c exists | 1 observation | Drift monotonically decreases with γ |
| QBR-3 | Pe_max ~ f(H(Y)) across substrates | Testable | Spearman ρ < 0.3 |
| QBR-4 | Backaction creates Holevo-like gap | Testable | No Pe excess in high-backaction systems |

---

## 9. Limitations

### 9.1 Non-Relativistic QM Only

The bridge is established for non-relativistic quantum mechanics — the Hilbert space formalism of Schrödinger, Born, and Dirac. Three major areas of modern physics lie outside this scope:

**Quantum field theory (QFT).** The bridge maps classical information channels to quantum channels on finite-dimensional Hilbert spaces. QFT operates on Fock spaces with indefinite particle number, and the extension presents at least five specific mathematical obstacles:

1. *Infinite-dimensional state spaces.* The Bernoulli manifold is a one-dimensional statistical manifold parameterized by θ ∈ (0,1). QFT state spaces are infinite-dimensional: Fock space F = ⊕_n H^⊗n has sectors of arbitrarily many particles. The Fisher metric on finite-dimensional manifolds is well-defined; on infinite-dimensional manifolds, it requires careful regularization. The quantum Fisher information F_Q is defined for density operators on separable Hilbert spaces [38], but the SLD (symmetric logarithmic derivative) may not exist as a bounded operator, and the Cramér-Rao bound requires additional regularity conditions.

2. *Renormalization.* QFT produces UV divergences that require renormalization — systematic subtraction of infinities to obtain finite predictions. The Fisher metric on bare (unrenormalized) field parameters diverges; the metric on renormalized parameters depends on the renormalization scheme and scale. There is no canonical Fisher metric on QFT parameter spaces without fixing a renormalization group flow. This creates an ambiguity that has no analog in the non-relativistic bridge, where the Bernoulli manifold and the finite-dimensional Hilbert space are naturally paired.

3. *Particle creation and annihilation.* Nelson's stochastic mechanics (§4.1) describes a fixed number of particles undergoing diffusion. QFT allows particle number to change: the vacuum fluctuates, pair production occurs, virtual particles mediate interactions. The two-velocity decomposition (current v and osmotic u) applies to fixed-particle-number sectors of Fock space but does not naturally extend to superpositions of different particle numbers. Defining Pe_quantum for QFT would require either a Fock-space generalization of Nelson's stochastic mechanics or a reformulation of Pe in terms of field-theoretic quantities (correlation functions, propagators) rather than particle velocities.

4. *Locality and causality.* The void framework's channel model assumes a single observer-system interface. QFT is inherently local — observables are associated with spacetime regions, and causality constrains which regions can communicate. Extending the bridge to QFT would require specifying how the observer-system channel respects relativistic causality, how spacelike-separated measurements interact with the conjugacy bound, and whether the void budget requires modification for multi-region measurement scenarios.

5. *Algebraic structure.* Non-relativistic QM operates on Type I von Neumann algebras (bounded operators on Hilbert space). QFT on generic spacetimes involves Type III von Neumann algebras, where standard notions of entropy (von Neumann, Rényi) require modification. The Holevo bound, which anchors the constraint bridge (§5), relies on von Neumann entropy; extending it to Type III algebras requires the modular theory of Tomita-Takesaki and produces entropy measures (relative modular entropy, Araki entropy) that behave differently from their Type I counterparts. The constraint bridge would need to be rederived in this algebraic framework.

The Holevo bound does generalize to infinite-dimensional channels [38], so the constraint bridge likely extends with appropriate mathematical care. But the metric and dynamic bridges face the obstacles above. A plausible path: work in the algebraic QFT framework, use relative entropy (which is well-defined for Type III algebras) as the bridge quantity, and define Pe through the modular flow rather than Nelson's particle velocities. This remains speculative.

**Gravity.** The Fisher-Ruppeiner identity connects the Fisher metric to thermodynamic geometry, and Jacobson's [39] derivation of Einstein's equations from thermodynamic arguments suggests a deep connection between information geometry and spacetime geometry. However, the bridge presented here makes no claims about general relativity. The connection between Fisher information and the Ricci tensor (via the Ruppeiner metric on thermodynamic state spaces) is suggestive but not formalized. Extending the bridge to gravitational settings would require engaging with the holographic entanglement entropy program (Ryu-Takayanagi), the black hole information paradox, and the Unruh effect — each of which modifies the relationship between observers, measurements, and entropy in ways not captured by the current non-relativistic framework. This is explicitly identified as future work, not as an implied consequence of the current bridge.

**Quantum error correction.** The Knill-Laflamme conditions [37] for quantum error correction share structure with the void framework's constraint specification: both define conditions under which information is preserved against noise. The Knill-Laflamme conditions state that a code with code space C corrects error set {E_a} if and only if ⟨ψ_i|E_a†E_b|ψ_j⟩ = C_ab δ_ij for all codewords |ψ_i⟩, |ψ_j⟩ ∈ C. This is a condition on the code's ability to distinguish errors without disturbing the encoded information — structurally parallel to the constraint specification's requirement that the reference point be invariant (undisturbed by engagement) and transparent (errors detectable). The no-cloning connection (§6.7) is adjacent. A full mapping between quantum error correction codes and constraint architectures would strengthen the bridge but lies beyond the current scope. The key obstacle is that quantum error correction is discrete (syndrome measurement identifies error type), while constraint maintenance is continuous (γ is a rate, not a binary check).

### 9.2 Structural ≠ Dynamic for Most Extended Connections

The three-level bridge (§§3–5) has different epistemic status from the extended connections (§6). The metric bridge is *proven* — Proposition 1 is a mathematical identity. The constraint bridge is *proven* — the classical limit of the Holevo bound is a derivation. The dynamic bridge is *defined and confirmed* — Pe_quantum is a well-defined ratio with experimental confirmation at Pe = 1 (MIPT) and Pe ≫ 1 (Zeno transport).

The extended connections are mostly *structural* — they identify shared mathematical forms between quantum and classical phenomena without proving that one reduces to the other. Specifically:

| Connection | Status | What would upgrade it |
|-----------|--------|----------------------|
| Lindblad ↔ drift | Structural + formal reduction available | Explicit parameter mapping (L_k → noise terms) |
| Zeno ↔ γ | Structural + empirical echo | Quantitative γ_c measurement (QBR-2) |
| Darwinism ↔ network | Structural | Scaling test (QBR-1) |
| Stinespring ↔ budget | Formal (same conservation law) | — (already formal) |
| Speed limits ↔ ceiling | Structural | Pe_max measurement (QBR-3) |
| Irreversibility ↔ unidirectionality | Formal (same theorem) | — (already formal) |
| No-cloning ↔ opacity | Structural (reversed direction) | Quantitative backaction test (QBR-4) |

Two connections (Stinespring and Crooks irreversibility) are formal — they use the same mathematical theorem on different substrates. The remaining five are structural correspondences that require additional work (either mathematical proof or experimental confirmation) to upgrade to formal bridges.

### 9.3 The Bridge Does Not Validate the Framework

The bridge shows that the void framework's mathematics has a quantum ancestor. This does not independently validate the framework's empirical claims. The framework stands or falls on its own evidence: the gambling control case [5], the AI-to-AI experiments [7], the cross-substrate Pe measurements [9], and the falsification conditions specified in Paper 5 [7]. A mathematically correct bridge to quantum measurement theory is a structural result, not an empirical one. The bridge would remain correct even if the framework's empirical claims were wrong — it would simply be a correct mapping from an incorrect classical theory to quantum mechanics.

Conversely, the bridge could fail (if the limit operations turned out to have hidden errors) without invalidating the framework's empirical results. The framework's experiments measure real Pe values on real substrates, independent of whether those Péclet numbers have quantum ancestors.

---

## 10. Conclusion

The void framework's mathematics — a classical information-theoretic description of drift dynamics in observer-system interfaces — is the diagonal limit of quantum measurement theory's mathematics. This claim is established by three formal limit operations:

1. The Fisher metric on the Bernoulli manifold is the diagonal restriction of the quantum Fisher information (Proposition 1), occupying a distinguished position as simultaneously the unique classical invariant metric (Čencov) and the classical limit of the unique maximal quantum metric (Petz).

2. The classical Péclet number is Nelson's current-velocity/osmotic-velocity ratio restricted to the classical diffusion regime, with the critical Pe = 1 transition confirmed experimentally in measurement-induced phase transitions and Pe ≫ 1 demonstrated in spatial Zeno transport.

3. The conjugacy theorem is the Holevo accessible information bound restricted to diagonal encodings, while the Maassen-Uffink complementarity constraint provably vanishes in the same limit.

Seven extended connections map additional structural elements: Lindblad to drift equations, Zeno to constraint maintenance, quantum Darwinism to void network consensus, Stinespring to the void budget, quantum speed limits to Pe ceilings, Crooks irreversibility in both domains, and no-cloning to constitutive opacity. A completeness analysis shows that every structural element of the void framework has a quantum counterpart and every quantum measurement concept either maps to a classical framework element or vanishes in the classical limit.

Eleven predictions with falsification thresholds are specified. Two independent experimental programs — MIPTs confirming the Pe = 1 critical point across four hardware platforms [11,12,49,50,51,52] and Crooks fluctuation theorems for quantum measurement trajectories [15,16,17] — provide existing empirical support for the bridge. One prediction (QP-6) has been independently confirmed by seven witnesses distinguishing structured from unstructured observation [18,19,21,22,47,48,54]. One prediction (QP-3) is partially confirmed across four of seven substrates, including a purely classical chaotic system [53]. Two predictions (QP-1, QP-7) are partially supported. Seven predictions remain directly testable.

The bridge does not derive one theory from the other. It does not solve the measurement problem. It does not claim that classical information dynamics are quantum. What it shows is simpler and more precise: the mathematics of classical information-theoretic drift — the competition between directed engagement and random diffusion, bounded by a capacity constraint and measured by a Fisher metric — is a well-defined restriction of the mathematics that governs quantum measurement. The classical limit is not a retreat from generality. It is the identification of exactly which quantum structures persist into the classical regime, which vanish, and why.

---

## References

[1] Holevo, A.S. (1973). "Bounds for the quantity of information transmitted by a quantum communication channel." *Problems of Information Transmission* 9(3), 177–183.

[2] Braunstein, S.L. & Caves, C.M. (1994). "Statistical distance and the geometry of quantum states." *Physical Review Letters* 72(22), 3439–3443.

[3] Petz, D. (1996). "Monotone metrics on matrix spaces." *Linear Algebra and its Applications* 244, 81–96.

[4] Nelson, E. (1966). "Derivation of the Schrödinger equation from Newtonian mechanics." *Physical Review* 150(4), 1079–1085.

[5] Eckert, A. (2025). "The Architecture of Drift: A Thermodynamic Framework for Opacity-Driven Agency Attribution." *Zenodo*. doi:10.5281/zenodo.14828417.

[6] Eckert, A. (2025). "Thermodynamics of Opacity: Technical Foundations for the Void Framework." *Zenodo*. doi:10.5281/zenodo.14828417.

[7] Eckert, A. (2025). "Ground State of Observation: The Void Framework as Theory of Everything for Observer-System Interfaces." Working paper.

[8] Eckert, A. (2025). "Information-Geometric Bounds on Sampling Cascades." Working paper.

[9] Eckert, A. (2025). "The Deployment Geometry of Drift: Cryptocurrency Markets as Natural Experiments in Void Dynamics." Working paper.

[10] Čencov, N.N. (1982). *Statistical Decision Rules and Optimal Inference.* American Mathematical Society.

[11] Skinner, B., Ruhman, J. & Nahum, A. (2019). "Measurement-Induced Phase Transitions in the Dynamics of Entanglement." *Physical Review X* 9, 031009.

[12] Koh, J.M. et al. (2023). "Measurement-induced entanglement phase transition on a superconducting quantum processor with mid-circuit readout." *Nature Physics* 19, 1314–1319.

[13] Zhang, Z.-Y. et al. (2025). "Quantum Zeno Effect in the Spatial Evolution of a Single Atom." arXiv:2509.24438.

[14] Maassen, H. & Uffink, J.B.M. (1988). "Generalized entropic uncertainty relations." *Physical Review Letters* 60(12), 1103–1106.

[15] Clarke, C.L. & Ford, I.J. (2024). "Stochastic Entropy Production Associated with Quantum Measurement in a Framework of Markovian Quantum State Diffusion." *Entropy* 26(12), 1024.

[16] Walls, S.M., Bloss, A. & Ford, I.J. (2025). "Characterizing quantum measurement through environmental stochastic entropy production in a two-spin-1/2 system." *Physical Review A* 112, 032210.

[17] Manikandan, S.K., Elouard, C. & Jordan, A.N. (2019). "Fluctuation Theorems for Continuous Quantum Measurement and Absolute Irreversibility." *Physical Review A* 99, 022117.

[18] Paviglianiti, A., Di Fresco, G., Silva, A., Spagnolo, B., Valenti, D. & Carollo, A. (2025). "Breakdown of measurement-induced phase transitions under information loss." *Quantum* 9, 1781.

[19] Leung, C.Y., Meidan, D. & Romito, A. (2025). "Theory of free fermions dynamics under partial postselected monitoring." *Physical Review X* 15, 021020.

[20] Buchhold, M., Minoguchi, Y., Altland, A. & Diehl, S. (2021). "Effective theory for the measurement-induced phase transition of Dirac fermions." *Physical Review X* 11, 041004.

[21] Ha, H.Y., Pandey, S., Gopalakrishnan, S. & Huse, D.A. (2024). "Measurement-induced phase transitions in systems with diffusive dynamics." arXiv:2405.08861.

[22] Qian, D. & Wang, J. (2025). "Protect measurement-induced phase transition from noise." *Physical Review Letters* 134, 020403.

[23] Wu, Z., Sun, X., Wang, S., Zhang, J., Yang, X., Chu, J., Niu, J., Zhong, Y., Chen, X., Yang, Z.-C. & Yu, D. (2025). "Measurement-and feedback-driven non-equilibrium phase transitions on a quantum processor." arXiv:2512.07966.

[24] Kelly, S.P. & Marino, J. (2025). "Generalizing measurement-induced phase transitions to information exchange symmetry breaking." *Physical Review A* 111, 012425.

[25] Hack, P., Gottwald, S. & Braun, D.A. (2022). "Jarzynski's Equality and Crooks' Fluctuation Theorem for General Markov Chains with Application to Decision-Making Systems." *Entropy* 24(12), 1731. doi:10.3390/e24121731.

[26] Lindblad, G. (1976). "On the generators of quantum dynamical semigroups." *Communications in Mathematical Physics* 48(2), 119–130.

[27] Breuer, H.-P. & Petruccione, F. (2002). *The Theory of Open Quantum Systems.* Oxford University Press.

[28] Misra, B. & Sudarshan, E.C.G. (1977). "The Zeno's paradox in quantum theory." *Journal of Mathematical Physics* 18(4), 756–763.

[29] Kofman, A.G. & Kurizki, G. (2000). "Acceleration of quantum decay processes by frequent observations." *Nature* 405, 546–550.

[30] Zurek, W.H. (2003). "Decoherence, einselection, and the quantum origins of the classical." *Reviews of Modern Physics* 75(3), 715–775.

[31] Zurek, W.H. (2009). "Quantum Darwinism." *Nature Physics* 5(3), 181–188.

[32] Stinespring, W.F. (1955). "Positive functions on C*-algebras." *Proceedings of the AMS* 6(2), 211–216.

[33] Wilde, M.M. (2017). *Quantum Information Theory.* 2nd ed. Cambridge University Press.

[34] Mandelstam, L. & Tamm, I. (1945). "The uncertainty relation between energy and time in non-relativistic quantum mechanics." *Journal of Physics USSR* 9, 249–254.

[35] Margolus, N. & Levitin, L.B. (1998). "The maximum speed of dynamical evolution." *Physica D* 120(1–2), 188–195.

[36] Wootters, W.K. & Zurek, W.H. (1982). "A single quantum cannot be cloned." *Nature* 299, 802–803.

[37] Knill, E. & Laflamme, R. (1997). "Theory of quantum error-correcting codes." *Physical Review A* 55(2), 900–911.

[38] Holevo, A.S. (2012). *Quantum Systems, Channels, Information.* De Gruyter.

[39] Jacobson, T. (1995). "Thermodynamics of spacetime: The Einstein equation of state." *Physical Review Letters* 75(7), 1260–1263.

[40] Wiseman, H.M. & Milburn, G.J. (2009). *Quantum Measurement and Control.* Cambridge University Press.

[41] Annby-Andersson, B. et al. (2022). "Quantum Fokker-Planck Master Equation for Continuous Feedback Control." *Physical Review Letters* 129, 050401.

[42] Amari, S. (1985). *Differential-Geometrical Methods in Statistics.* Springer.

[43] Shannon, C.E. (1948). "A mathematical theory of communication." *Bell System Technical Journal* 27, 379–423, 623–656.

[44] Bacciagaluppi, G. (2005). "A Conceptual Introduction to Nelson's Mechanics." In R. Buccheri, M. Saniga & A. Elitzur (eds.), *Endophysics, Time, Quantum and the Subjective*, World Scientific, pp. 367–388.

[45] Eckert, A. (2025). "The Shape of the Cage: AI Safety Through the Void Framework." *Zenodo*. doi:10.5281/zenodo.14828417.

[46] Eckert, A. (2025). "Never Trust the Client: Multiplayer Gaming as Natural Experiment in Void Dynamics." Working paper.

[47] Liu, S., Li, M.-R., Zhang, S.-X., Jian, S.-K. & Yao, H. (2024). "Noise-induced phase transitions in hybrid quantum circuits." *Physical Review B* 110, 064323.

[48] Chatterjee, P. & Modak, R. (2025). "Measurement-induced phase transition in periodically driven free-fermionic systems." *Physical Review B* 112, 024304.

[49] Feng, X., Cote, J., Kourtis, S. & Skinner, B. (2025). "Postselection-free experimental observation of the measurement-induced phase transition in circuits with universal gates." *Communications Physics*. doi:10.1038/s42005-025-02443-0. arXiv:2502.01735.

[50] Agrawal, U., Lopez-Piqueres, J., Vasseur, R., Gopalakrishnan, S. & Potter, A.C. (2024). "Observing Quantum Measurement Collapse as a Learnability Phase Transition." *Physical Review X* 14, 041012.

[51] Kamakari, H., Sun, J., Li, Y., Thio, J.J., Gujarati, T.P., Fisher, M.P.A., Motta, M. & Minnich, A.J. (2025). "Experimental Demonstration of Scalable Cross-Entropy Benchmarking to Detect Measurement-Induced Phase Transitions on a Superconducting Quantum Processor." *Physical Review Letters* 134, 120401.

[52] Chen, E.H., Zhu, G.-Y., Verresen, R., Seif, A., Baumer, E., Layden, D., Tantivasadakarn, N., Zhu, G., Sheldon, S., Vishwanath, A., Trebst, S. & Kandala, A. (2025). "Nishimori transition across the error threshold for constant-depth quantum circuits." *Nature Physics* 21, 161–167.

[53] Gerbino, F., Giachetti, G., Le Doussal, P. & De Luca, A. (2025). "Measurement-Induced Phase Transition in State Estimation of Chaotic Systems and the Directed Polymer." *Physical Review Research* 7, 033105.

[54] Nehra, R., Romito, A. & Meidan, D. (2025). "Controlling measurement-induced phase transitions with tunable detector coupling." *Quantum* 9, 1697. doi:10.22331/q-2025-04-08-1697.

[55] Yang, F., Wang, X.-B. & Chen, T. (2025). "Bridging measurement-induced phase transition and quantum error correction in monitored quantum circuits with many-body measurements." *Physical Review B* 111, 064308.

[56] Gurnee, W., Ameisen, E., Kauvar, I., Tarng, J., Pearce, A., Olah, C. & Batson, J. (2026). "When Models Manipulate Manifolds: The Geometry of a Counting Task." *Transformer Circuits Thread*. arXiv:2601.04480.

[57] Di Sipio, R. (2025). "Rethinking LLM Training through Information Geometry and Quantum Metrics." arXiv:2506.15830.

[58] Lessa, L.A., Gu, R., & Yao, A. (2025). "Topological entanglement transition between area-law phases via competing measurements." *Quantum* 9, 23082.

[59] Sierant, P., Turkeshi, X., Collura, M., & Schirò, M. (2025). "Measurement-induced phase transitions in infinite-range models." *Physical Review Research* 7, 023082.
