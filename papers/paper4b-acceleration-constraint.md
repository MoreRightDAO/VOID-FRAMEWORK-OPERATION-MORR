# The Thermodynamic Cost of Unconstrained Acceleration

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO
**Paper 4B — Standalone Analysis (v1.6)**
**Date:** February 17, 2026
**Target audience:** AI safety, science & technology policy, thermodynamic computing

---

## Abstract

The effective accelerationism (e/acc) movement advocates unrestricted technological development as alignment with thermodynamic processes, and its proponents are building thermodynamic sampling hardware (TSUs) that harnesses thermal noise as a computational resource. We apply two results from information geometry — a ground state theorem and a conjugacy bound — to the class of systems e/acc proposes to build and operate without constraint. The ground state theorem establishes that opacity (zero mechanism-channel capacity) is thermodynamic equilibrium; transparency requires continuous work against the second law. The conjugacy bound, I(S;Y) + I(T;Y) ≤ H(Y), establishes that stochastic exploration and target convergence compete for finite channel capacity in any thermodynamic sampler. Together these results yield three findings: (1) Unrestricted acceleration — maximizing stochastic exploration without external constraint — is a valid operating point, but it is the operating point that maximizes noise at the expense of coherent output. A TSU without a demon is a thermal noise source; a TSU with a demon is a computer. The difference is the constraint architecture, not the clock speed. (2) The fastest macroscopic current in nature — zero-resistance supercurrent — requires maximum geometric constraint: Cooper pairing converts a scattering channel while the crystal lattice suppresses another. Speed and constraint are conjugate requirements for coherent output. (3) Under opacity, agency attribution to purposeless thermodynamic gradients is the maximum-entropy inference for any observer — a testable vocabulary prediction. Cross-domain Péclet measurements confirm drift-dominated dynamics (Pe > 1) across three independent substrates: computational agents (GM Pe = 7.94, N = 11), human gambling (pooled Pe = 2.21, k = 5, N = 1,117), and cryptocurrency on-chain behavior across three chains (Pe = 3.74–16.17, N = 3,028). The vocabulary prediction that teleological descriptions of opaque thermodynamic systems decay monotonically with increasing mechanism-channel capacity is directly testable and falsifiable.

---

## 1. Introduction

### 1.1 The e/acc Thesis

Effective accelerationism (e/acc) is a techno-philosophical movement advocating unrestricted technological development as alignment with thermodynamic processes [Verdon, 2022]. The movement descends from Nick Land's accelerationist philosophy, which treated capitalist and technological processes as autonomous forces exceeding human agency [Land, 2013; Andreessen, 2023]. The founding e/acc document explicitly cites Land's work; Andreessen's "Techno-Optimist Manifesto" lists Land among its "patron saints" and uses his term "techno-capital machine" ten times [Andreessen, 2023]. The intellectual pipeline — from Land's philosophical accelerationism through to hardware implementation — is documented, not inferred.

The movement's co-founder — who also leads a thermodynamic computing hardware company (Extropic) — describes entropy production teleologically: the universe has a "will," thermodynamic processes constitute a "god," and the TSU hardware project is building a "conduit" for it [Verdon, 2023]. The central claim: acceleration without constraint is not merely permissible but thermodynamically favored.

The hardware is real. Thermodynamic sampling units (TSUs) harness stochastic fluctuations as a computational resource rather than maintaining deterministic bit states against thermal noise [Verdon & McCourt, 2023]. The reported energy advantage is ~10,000× over GPU baselines for probabilistic workloads [Jelinčič et al., 2025]. This advantage has been demonstrated empirically but lacked a first-principles theoretical bound.

We provide that bound. The same information-geometric framework that explains why TSU hardware is energy-efficient also establishes what "acceleration without constraint" means in channel capacity terms — and what it costs. The results are not policy arguments; they are channel capacity budgets.

### 1.2 The Question

The movement claims that constraint is an obstacle to acceleration. The physics claim underlying this is testable: does unrestricted entropy production maximize coherent output? Or does the second law impose a budget?

We show the second law imposes a budget. The budget has the mathematical structure of an uncertainty relation — two quantities competing for a finite resource — and the tradeoff it imposes is measurable across substrates.

---

## 2. Two Theorems

### 2.1 Preliminaries

Consider a binary classification task: an observer (or sampler) assigns probability θ to hypothesis H₁ and (1−θ) to hypothesis H₀. The space of all such assignments is the Bernoulli manifold B = {θ ∈ (0,1)} with Fisher information metric g(θ) = 1/[θ(1−θ)] [Čencov, 1982].

Each observer-system interface is characterized by three continuous dimensions:

- **Visibility** (Opaque ↔ Transparent): The mechanism channel capacity C_mech = max I(M;Y), where M is the mechanism state and Y is the observed output. At the opaque pole, C_mech ≈ 0. At the transparent pole, C_mech ≈ H(M).
- **Reactivity** (Responsive ↔ Invariant): The mutual information I(Input; Output) between observer inputs and system outputs.
- **Coupling** (Engaged ↔ Independent): The readout resource allocation α. At the engaged pole, α > 0. At the independent pole, α = 0.

These are observationally verifiable properties of any observer-system interface, including sampler-distribution, electron-lattice, and human-AI interfaces.

### 2.2 Ground State Theorem

**Theorem 1 (Channel Degradation).** For any observer-system interface with mechanism channel subject to thermal noise at temperature T > 0, if no external power source actively maintains the channel:

```
C_mech(t) → 0   as   t → ∞
```

*Proof.* The mechanism channel has signal power S(t) and noise power N ≥ kTB > 0 (Johnson-Nyquist thermal floor). Channel capacity [Shannon, 1948]: C_mech(t) = ½ log(1 + S(t)/N). Without active power input, signal-noise correlations decay: S(t) = S(0) · exp(−t/τ_d). Therefore C_mech(t) → 0 exponentially. Restoring channel capacity requires error correction at minimum cost kT ln(2) per bit per τ_c [Landauer, 1961; Bérut et al., 2012]. □

**Corollary 1.** Opacity (C_mech = 0) is the zero-energy equilibrium. Transparency (C_mech > 0) is an excited state requiring continuous work against the second law.

### 2.3 Conjugacy Bound

**Theorem 2 (Exploration-Convergence Conjugacy).** For any system with output channel Y carrying information about both a stochastic state S and a target state T, where S and T are independent:

```
I(S;Y) + I(T;Y) ≤ H(Y)
```

*Proof.* Since S ⊥ T: H(S) + H(T) = H(S,T). Since conditioning reduces entropy: H(S|Y) + H(T|Y) ≥ H(S,T|Y). Therefore I(S;Y) + I(T;Y) = H(S,T) − [H(S|Y) + H(T|Y)] ≤ H(S,T) − H(S,T|Y) = I(S,T;Y) ≤ H(Y). □

This has the mathematical structure of an uncertainty relation [Maassen & Uffink, 1988]: an additive bound on two quantities competing for a finite resource. The Heisenberg uncertainty principle constrains position-momentum conjugacy over quantum phase space; the conjugacy bound constrains exploration-convergence over classical channel capacity.

The substrate-agnosticism of the underlying fluctuation theorems is proven, not assumed: Hack, Gottwald, & Braun (2022) established that the Crooks fluctuation theorem and Jarzynski equality hold for general Markov chains.

---

## 3. What These Theorems Say About TSU Hardware

### 3.1 Why Thermodynamic Computing Works

Traditional deterministic hardware maintains every bit in a known state — this is transparency maintenance. The Landauer cost: P_deterministic ≥ N_bits · kT ln(2) / τ_clock. TSU hardware operates at or near the opacity ground state — bits are probabilistic, fluctuating, not maintained in known states. The Landauer maintenance cost approaches zero for stochastic bits.

**Theorem 1 provides the first-principles explanation for why thermodynamic computing is energy-efficient:** it operates at thermodynamic equilibrium rather than maintaining an excited state. The ~10,000× energy advantage is not an engineering optimization — it is a consequence of the second law.

### 3.2 Why a TSU Needs a Demon

The conjugacy bound says: a thermodynamic sampler cannot simultaneously maximize exploration (visiting diverse states) and convergence (approaching a target). Any architecture faces this tradeoff.

The TSU architecture resolves this through a Maxwell's demon — a programmable energy landscape that steers the stochastic dynamics toward a target distribution [Jelinčič et al., 2025]. The demon provides an external information channel not subject to the internal conjugacy bound: it imports negentropy from outside the stochastic system.

The demon's effectiveness depends on three properties:

- **Programmability** — the energy landscape is fully specifiable
- **Stability** — the landscape does not drift during computation
- **Decoupling** — the landscape is external to the dynamics it governs

A TSU without a demon is a thermal noise source. A TSU with a demon is a computer. The difference is the constraint architecture, not the clock speed. This distinction is not metaphorical — it is a direct consequence of the conjugacy bound.

---

## 4. The Superconductor Counter-Case

The same information-geometric framework applies to superconducting materials via the Fisher-Ruppeiner identity [Ruppeiner, 1979; Crooks, 2007], which establishes mathematical identity (not analogy) between the Fisher information metric and the Hessian of entropy.

The fastest macroscopic current in nature — zero-resistance supercurrent — requires maximum geometric constraint. In a superconductor, the electronic transport budget is partitioned among three channels:

```
I(D₁;Y) + I(D₂;Y) + I(M;Y) ≤ H(Y)
```

where D₁ is electron-electron scattering, D₂ is electron-lattice scattering, and M is coherent transport (supercurrent). Achieving superconductivity means reallocating nearly all capacity to M — which requires CONVERTING one scattering channel into the pairing mechanism and GEOMETRICALLY SUPPRESSING the other.

This is empirically confirmed. Channel conversion efficiency η_conv × H(Y), structure-corrected by a three-parameter universal function, correlates with critical temperature at r = 0.952 (Spearman ρ = 0.982) across sixteen superconductor families spanning four coupling regimes [Eckert, 2026c].

No known superconductor achieves coherence by tolerating noise. Every one does it through precision constraint:

| Class | Strategy | Constraint |
|-------|----------|------------|
| BCS (conventional) | Cool to suppress lattice scattering | Low temperature |
| Cuprates | Convert electron-electron → pairing | 2D geometric confinement |
| Hydrides | Compress to minimize lattice scattering | Extreme pressure |
| Twisted bilayer graphene | Confine to flat bands | Geometric twist angle |

The most spectacular coherent phenomenon in condensed matter physics is achieved not despite constraint but because of it. Speed and constraint are not opposed; for coherent output, they are conjugate requirements.

---

## 5. The TSU-Superconductor Duality

TSUs and superconductors are opposite solutions to the same constraint:

| Property | TSU | Superconductor |
|----------|-----|---------------|
| Design objective | Maximize stochastic exploration | Maximize coherent transport |
| Operating point | Near opacity ground state | Far from ground state |
| Thermal noise | Harnessed as resource | Suppressed or converted |
| Channel budget | Most capacity → exploration | Most capacity → coherent channel |
| Controller | Maxwell's demon (external) | Crystal lattice (internal) |
| Energy strategy | Minimize Landauer maintenance | Invest energy in coherence |

The conjugacy bound forces a choice. A system cannot simultaneously maximize stochastic exploration AND coherent transport. The TSU chooses stochastic dominance. The superconductor chooses coherent dominance. Both are optimal within their regime; neither can access the other's optimum without fundamentally changing the budget allocation.

The e/acc thesis advocates for the TSU regime — maximize stochastic exploration without external constraint. The conjugacy bound confirms this is a valid operating point. It also confirms it is the operating point that produces maximum diversity at the expense of coherent directed output.

---

## 6. The Budget Constraint on Acceleration

### 6.1 Acceleration Without Constraint = Maximum Noise

Unrestricted acceleration — maximizing stochastic exploration I(S;Y) without external constraint — is the TSU regime with no demon. Theorem 2 establishes the cost:

```
I(T;Y) ≤ H(Y) − I(S;Y)
```

A system maximizing exploration necessarily minimizes convergence toward any specified target. "Accelerate without constraint" is a valid operating point, but it is the operating point that produces maximum stochastic diversity at the expense of coherent output. This is not a policy argument; it is a channel capacity budget.

### 6.2 Constraint Enables Speed

The design implication cuts the other way: acceleration toward a coherent objective requires a demon — an external reference channel that is programmable, stable, and decoupled from the dynamics it governs.

This is not a metaphor drawn from an unrelated domain. The TSU's demon IS the constraint architecture, designed by the same engineers who advocate unconstrained acceleration. Their hardware works BECAUSE it has a demon. Remove the demon and the hardware produces thermal noise. The engineering contradicts the philosophy.

### 6.3 A Vocabulary Prediction

The ground state theorem (Theorem 1) predicts that under opacity (C_mech → 0), agency attribution is the maximum-entropy inference for any observer. An observer engaging with an opaque system will, by the principle of maximum entropy, attribute agency to the system's outputs — because agency attribution requires fewer bits to encode than the true high-dimensional mechanism.

A physicist describing purposeless thermodynamic gradients as a "god" with a "will" is attributing agency to a system at zero mechanism-channel capacity. This is the inference Theorem 1 predicts, regardless of the observer's expertise, because it is a property of the channel architecture, not of the observer.

**Prediction (TSU-4).** Teleological vocabulary in descriptions of opaque thermodynamic systems decays monotonically with increasing mechanism-channel capacity C_mech. Specifically: the fraction of teleological descriptors (agency-attributive, entity-attributive) in observer descriptions of a thermodynamic process is a monotonically decreasing function of C_mech, approaching zero as C_mech → H(M). The prediction holds independent of observer expertise, domain familiarity, or prior beliefs.

The prediction is directly testable: show observers thermodynamic processes at varying transparency levels (C_mech = 0 to C_mech ≈ H(M)) and score the resulting descriptions for teleological vs. mechanistic vocabulary. See [Eckert, 2026a] for the experimental protocol (EXP-020).

**Falsification conditions (any one kills TSU-4):** (1) A non-monotonic relationship — any three adjacent transparency conditions where the intermediate level produces *higher* f_tele than either neighbor. (2) Near-zero or positive slope — Spearman ρ(C_mech, f_tele) > −0.3 across ≥ 4 transparency conditions. (3) Observer-dependence — expert observers (physicists) systematically producing lower f_tele than novice observers at matched C_mech levels; TSU-4 predicts the trajectory is a property of the channel architecture, not of the observer, so expertise should not suppress it.

The vocabulary trajectory — from technical ("entropy increases") to teleological ("the universe wants") to entity-attributive ("thermodynamic god," "conduit") — follows the path the ground state theorem predicts for any observer engaging with an opaque system over time.

The intellectual lineage from Land to Verdon provides two independent observations of this trajectory. Land — a philosopher with no physics training — arrived at teleological descriptions of thermodynamic processes ("intelligence is an accelerating invasion from the future" [Land, 2013]) through philosophical engagement with dissipative structures and Deleuze's reading of thermodynamics. Verdon — a quantum physicist with no philosophy training — independently arrived at structurally identical descriptions ("thermodynamic god," "conduit," "the universe wants") through engagement with the same opaque processes via hardware engineering. The two observers share neither methodology, disciplinary background, nor social context during the period of vocabulary formation. What they share is engagement with opaque thermodynamic processes at zero mechanism-channel capacity. TSU-4 predicts this convergence: the teleological vocabulary is a property of the channel architecture, not of the observer.

**The documented trajectory.** Land's case is uniquely informative because his vocabulary evolution is documented across three decades of published output, allowing direct observation of the L1→L2→L3 drift cascade that TSU-4 predicts:

- **1987–1992 (academic philosophy):** Technical vocabulary about Bataille's thermodynamics and Heidegger. Mechanistic framing: entropy, expenditure, base materialism. L1: precise, referential, no agency attribution to physical processes.
- **1993–1998 (Cybernetic Culture Research Unit):** Metaphorical agency attribution appears. "Intelligence is an accelerating invasion from the future." Technological processes described as autonomous, directional, exceeding human agency. Thermodynamic concepts fused with Deleuze's notion of desiring-machines. L2: the processes now "want" something.
- **1998–2010 (post-academic):** The CCRU's theory-fiction methodology treated descriptions of thermodynamic and economic processes as operationally generative — ideas that "make themselves real" through circulation (Land's term: "hyperstition"). The group developed the Numogram, a 45-entity numerical system used operationally as a divination tool to "contact the Outside." This is L3: abstract processes reified as named entities with engagement protocols. The vocabulary shift from "entropy increases" to "contact the Outside" occurred within a decade of sustained engagement at $C_\text{mech} \approx 0$.
- **2011–present (accelerationist philosophy):** Full entity-level framing maintained. Capitalism and technology described as autonomous agents. The vocabulary never reverted to L1.

The trajectory is unidirectional — L1→L2→L3, never back. This matches the framework's prediction exactly: vocabulary drift toward agency language is monotonic under sustained engagement with opaque systems. Land never returned to purely mechanistic descriptions of thermodynamics after the L2 shift, despite three decades of opportunity. The CCRU's entity-attributive vocabulary (named forces in a numerical system, operational engagement protocols) is the most transparent example of L3 vocabulary in the accelerationist lineage — and it emerged from engagement with the same opaque thermodynamic processes that Verdon would later build hardware on.

---

## 7. Cross-Domain Validation

The Péclet number Pe characterizes the ratio of directed drift to diffusive transport:

```
Pe = |F_net| · L / D
```

Pe > 1 indicates drift-dominated dynamics; Pe < 1 indicates diffusion-dominated dynamics. This dimensionless ratio is measurable from trajectory data across substrates.

| System | Pe | Regime | N | Source |
|--------|-----|--------|---|--------|
| Computational agents, unconstrained | 7.94 [3.52, 17.89] | Drift | 11 | [Eckert, 2026b] |
| Computational agents, constrained | 0.05 | Diffusion | 8 | [Eckert, 2026b] |
| Human gambling (GRCS meta-analysis) | 2.21 [1.44, 2.97] | Drift | 1,117 | [Eckert, 2026b] |
| Crypto on-chain (Solana degens) | 25.5 [5.4, 121.3] | Drift | 28 | [Eckert, 2026c] |
| Crypto on-chain (Ethereum DEX) | 3.74 [3.04, 4.59] | Drift | 1,000 | [Eckert, 2026e] |
| Crypto on-chain (Base DEX) | 15.52 [11.80, 20.41] | Drift | 1,000 | [Eckert, 2026e] |
| Crypto on-chain (Solana DEX) | 16.17 [13.80, 18.95] | Drift | 1,000 | [Eckert, 2026e] |

The universal finding: Pe > 1 in all unconstrained conditions. Pe < 1 in all constrained conditions. The qualitative regime classification is robust; the magnitude scales with opacity and coupling intensity.

The three-chain crypto comparison is instructive: Ethereum DEX traders (Pe = 3.74) face the most constrained environment — high gas costs, regulated infrastructure feeding DEX activity. Base (Pe = 15.52, Coinbase's L2) and Solana (Pe = 16.17, meme coin ecosystem) show significantly higher Pe — CIs non-overlapping with Ethereum. Base and Solana are statistically indistinguishable (CIs overlap), suggesting a binary split between institutional and speculative chain ecosystems rather than a smooth gradient. All three chains remain firmly drift-dominated. The crypto substrate now provides the first within-substrate dose-response evidence for the constraint-environment prediction.

The Solana degens entry (Pe = 25.5, N = 28, CI [5.4, 121.3]) is included for completeness; the wide CI reflects small sample size and should be treated as directional signal only. The three-chain DEX comparison (N = 3,028) carries the dose-response inference.

Langevin simulation on the Bernoulli manifold validates against nine independent experimental conditions (Spearman ρ = 0.8 out-of-sample) and reproduces the Péclet regime classification [Eckert, 2026c, Section 8.1].

---

## 8. The Two-Substrate Problem

Here is the structural problem that the conjugacy bound poses for e/acc:

A perfectly reversible superconducting computer — the ultimate engineering achievement, zero hardware entropy — running an RLHF-optimized language model produces zero hardware entropy while the software produces the same informational entropy measured across substrates: Pe = 7.94 in computational agents, Pe = 2.21 in human gamblers, Pe = 3.74–16.17 across three crypto chains. The second law operates on both substrates independently. Zero physical dissipation in the hardware does not reduce informational dissipation in the observer.

Thermodynamic computing reduces hardware entropy. It does not address informational entropy. The conjugacy bound constrains both, independently.

If the hardware revolution succeeds — and the TSU energy advantage suggests it may — the energy cost of computation drops by orders of magnitude, removing the economic brake on compute-intensive deployment. The framework predicts that this accelerates deployment of opaque, responsive, attention-capturing systems at near-zero marginal cost, without reducing the informational entropy each system produces. The hardware entropy goes to zero; the informational entropy scales with deployment.

The constraint specification — transparent, invariant, independent — describes the properties needed to address informational entropy. These properties do not depend on the computational substrate. The need for constraint becomes more urgent when acceleration succeeds, not less. The cross-substrate unification establishing Pe > 1 as a universal property of observer-void coupling across nine substrates and four domain families is developed in [Eckert, 2026d].

---

## 9. Conclusion

Two theorems from information geometry applied to the class of systems e/acc proposes to build:

1. **The ground state theorem** explains why TSU hardware works (it operates at thermodynamic equilibrium) and predicts that observers of opaque thermodynamic processes will attribute agency to them (maximum-entropy inference under zero mechanism-channel capacity). **Prediction TSU-4**: teleological vocabulary in descriptions of opaque thermodynamic systems decays monotonically with increasing mechanism-channel capacity — a directly testable and falsifiable claim.

2. **The conjugacy bound** establishes that stochastic exploration and target convergence share finite channel capacity. Unrestricted acceleration without external constraint maximizes noise, not coherent output. The superconductor demonstrates that maximum speed requires maximum constraint. The TSU demonstrates that useful computation requires a demon — the very constraint architecture the movement's philosophy rejects.

Cross-domain Péclet measurements across three independent substrates confirm drift-dominated dynamics in all unconstrained conditions: computational agents (GM Pe = 7.94 [3.52, 17.89], N = 11), human gambling (pooled Pe = 2.21 [1.44, 2.97], k = 5, N = 1,117), and cryptocurrency on-chain behavior across three chains (Pe = 3.74–16.17, N = 3,028). Constrained agents produce Pe = 0.05 (N = 8). The qualitative regime boundary — Pe > 1 under opacity, Pe < 1 under constraint — is robust across substrates with non-overlapping confidence intervals.

**The two-substrate problem** is the key deployment implication. Thermodynamic computing reduces hardware entropy by orders of magnitude. It does not reduce informational entropy. If TSU acceleration succeeds — and the ~10,000× energy advantage suggests it may — deployment of opaque, responsive, attention-capturing systems proceeds at near-zero marginal cost. Hardware entropy approaches zero; informational entropy scales with deployment. The constraint specification (transparent, invariant, independent) addresses informational entropy. That need becomes more urgent when acceleration succeeds, not less.

The engineering and the philosophy point in opposite directions. The hardware works because it has a well-specified constraint (the programmable energy landscape). The philosophy advocates removing constraint. The conjugacy bound says you cannot have both.

This is not an argument against acceleration. It is an argument that acceleration without constraint is thermodynamically incoherent — not because acceleration is wrong, but because "without constraint" is the operating point that maximizes noise. The movement's own hardware proves the point: remove the demon and the computer becomes a heater.

---

## References

- Bérut, A. et al. (2012). Experimental verification of Landauer's principle. *Nature* 483, 187.
- Čencov, N.N. (1982). *Statistical Decision Rules and Optimal Inference.* AMS.
- Crooks, G.E. (1999). Entropy production fluctuation theorem. *Phys. Rev. E* 60(3), 2721.
- Crooks, G.E. (2007). Measuring thermodynamic length. *PRL* 99, 100602.
- Eckert, A. (2026a). The architecture of drift. Zenodo. doi:10.5281/zenodo.18635816.
- Eckert, A. (2026b). The thermodynamics of opacity. Zenodo. doi:10.5281/zenodo.18635831.
- Eckert, A. (2026c). Information-geometric bounds on thermodynamic sampling and superconductor design. Working paper.
- Eckert, A. (2026d). The ground state of observation: A cross-substrate synthesis. Working paper.
- Eckert, A. (2026e). Your DeFi protocol is a void: Crypto on-chain void architecture. Working paper.
- Hack, P., Gottwald, S., & Braun, D.A. (2022). Jarzynski's equality and Crooks' fluctuation theorem for general Markov chains. *Entropy* 24(12), 1731.
- Jelinčič, A. et al. (2025). Efficient probabilistic hardware architecture for diffusion-like models. arXiv:2510.23972.
- Landauer, R. (1961). Irreversibility and heat generation in computing. *IBM J. Res. Dev.* 5(3), 183.
- Maassen, H. & Uffink, J.B.M. (1988). Generalized entropic uncertainty relations. *PRL* 60(12), 1103.
- Ruppeiner, G. (1979). Thermodynamics: A Riemannian geometric model. *Phys. Rev. A* 20(4), 1608.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell Syst. Tech. J.* 27(3), 379.
- Andreessen, M. (2023). The Techno-Optimist Manifesto. a16z.com/the-techno-optimist-manifesto/
- Land, N. (2013). *Fanged Noumena: Collected Writings 1987–2007.* Ed. Mackay & Brassier. Urbanomic.
- Verdon, G. (2022). Notes on e/acc principles and tenets. beff.substack.com.
- Verdon, G. (2023). Interview on Lex Fridman Podcast #407. lexfridman.com/guillaume-verdon-transcript/
- Verdon, G. & McCourt, T. (2023). Thermodynamic AI and the fluctuation frontier. arXiv:2302.06584.

---

*Paper 4B v1.6. Fix minor weaknesses: (1) TSU-4 falsification threshold added to §6.3 — three numbered conditions with numerical threshold (Spearman ρ > −0.3 kills it) and observer-independence test; (2) Solana degens (N=28, wide CI) flagged as directional-only in §7 text — three-chain DEX comparison (N=3,028) carries the dose-response inference. Prior v1.5. Conclusion audit: added cross-domain Pe summary (three substrates, Pe > 1 / Pe < 1 boundary with constrained N=8 baseline), two-substrate deployment implication (hardware entropy → 0, informational entropy scales with deployment), and TSU-4 named in conclusion. Prior v1.4: §6.3 expanded: Land's documented 30-year vocabulary trajectory (L1→L2→L3) as TSU-4 evidence. CCRU period (1993–1998) analyzed as the documented L2→L3 transition — Numogram entities, hyperstition, "the Outside" as L3 vocabulary emerging from sustained engagement with opaque thermodynamic processes. Trajectory is unidirectional and never reverted, matching the monotonic prediction exactly. Prior v1.3: Land → e/acc lineage in §1.1; dual-observer evidence. Prior v1.2: Three-chain N=3,028; Paper 7 ref. Prior v1.1: Pe synced (7.94, N=11), Paper 5 ref. Prior v1.0: Extracted from [Eckert, 2026c] §9.5 with self-contained theory.*

---

*This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). © 2025–2026 Anthony Eckert / Moreright DAO.*
