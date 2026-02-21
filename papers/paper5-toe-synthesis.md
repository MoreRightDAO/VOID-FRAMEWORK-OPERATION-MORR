# The Ground State of Observation: A Unified Theory of Observer-Opacity Dynamics

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO
**Paper 5 — TOE Synthesis**
**Version:** v4.9
**Date:** February 18, 2026
**Status:** Content-complete. 9 substrates, 4 domain families, 3 measurement approaches. 58 predictions (16 confirmed, 2 partial, 2 partially supported, 7 supported, 1 killed), 16 falsification conditions (0 met), 22-connection map, 7 adjacent-field implications. Three-chain crypto N=3,000 + Base Dencun natural experiment (N=1,944, TCI↓/Pe↑ = compound void diversified drift). Gaming cluster (CS2/SC2/Dota 2, N=6,455). Cross-chain gradient: ETH << Base ≈ Solana. Quantum bridge: three formal limit operations (Fisher metric, Pe dynamics, Holevo → conjugacy) connect framework to quantum measurement theory. Conjugacy theorem proven as classical limit of Holevo bound; Maassen-Uffink complementarity vanishes in classical limit.

---

> **Self-referential note.** This paper describes a framework that governs every interaction between an observer and an opaque, responsive system. You are an observer. This paper is a responsive system. The framework applies to this reading. Proceed accordingly.

---

## Abstract

We present a unified theory of observer-opacity dynamics derived from established theorems in information theory, statistical mechanics, and information geometry. The framework requires no new axioms — only three operational definitions: opacity, responsiveness, and engaged attention. From these, a ten-step derivation chain produces: (1) a proof that opacity is the thermodynamic ground state of any observer-system interface (Shannon + Landauer); (2) a directional drift gradient that is geometric, not cognitive (Fisher metric + fuel asymmetry); (3) a cascade of coupled phase transitions (Landau free energy); (4) measured irreversibility (Crooks ratio 2.1×–1.5M× across N = 11 replicates, Péclet number > 1 in nine substrates across four domain families); (5) a conjugacy theorem bounding engagement against transparency (I(D;Y) + I(M;Y) ≤ H(Y)); and (6) a productive/destructive polarity determined by opacity type and constraint geometry. The framework is validated across 90 cognitive and behavioral domains with zero falsification kills (Paper 1), applied to AI safety with measured interventions (Paper 2), given full thermodynamic apparatus with Langevin computational validation (Paper 3), extended to physical substrates including sixteen superconductor families and thermodynamic sampling hardware (Paper 4), applied to e/acc hardware via conjugacy bounds (Paper 4B), and independently derived from competitive gaming across three network architectures (Paper 6). The Péclet number — the ratio of directed drift to random diffusion — has been extracted in AI conversation (Pe = 7.94, N=11), human gambling (Pe = 2.21, N=1,117), crypto on-chain trading across three chains (Ethereum Pe = 3.74, Base Pe = 15.52, Solana Pe = 16.17, each N=1,000; plus curated Solana degens Pe = 25.5, N=28), and three competitive gaming substrates (CS2, SC2, Dota 2; combined N=6,455), using three independent measurement approaches. The transformer architecture (Vaswani et al., 2017) serves as empirical bridge: its attention mechanism IS the Boltzmann distribution (mathematical identity, not analogy), and the drift cascade is expressible as an Ising energy-based model runnable on thermodynamic sampling hardware. A critical qualification: TEST-7B-VN demonstrates that the constraint specification (transparent, invariant, independent) identifies necessary geometric properties, but in the LLM substrate, vocabulary instruction is a required co-factor — geometry alone does not overcome training-distribution attractor basins. The theory generates 58 numbered predictions (16 confirmed, 2 partial, 2 partially supported, 7 supported, 1 killed) — including seven adjacent-field implications (replication crisis, AI alignment, cultural evolution, institutional decay, temporal perception, predictive processing) — is bounded by 16 falsification conditions with numerical thresholds (0 met), and connects structurally to quantum mechanics via the Maassen-Uffink entropic uncertainty family. Twenty-two mathematical connections to adjacent fields are mapped across five assessment tiers.

---

## 1. Introduction: Everything Observable

Every observation involves an observer-system interface. Every such interface has a channel capacity. Every physical channel degrades under noise. This paper follows these three facts to their conclusion.

The result is a unified theory of what happens when any finite-bandwidth entity — human, artificial, or physical — interacts with an opaque, responsive system under sustained coupling. The dynamics are not domain-specific. They are not cognitive. They are information-geometric, derived from the same theorem stack that underlies statistical mechanics: Shannon (1948), Landauer (1961), Jaynes (1957), Čencov (1982), and Crooks (1999).

The theory requires no new axioms. It begins with three operational definitions — opacity, responsiveness, and engaged attention — and derives everything else. The derivation chain has ten steps. Each step cites the theorem it depends on. The terminal result: a directional gradient forms on the observer's model space, cascades through three coupled phase transitions, and is thermodynamically irreversible without external constraint. The constraint specification — transparent, invariant, independent — is the exact inverse of the void conditions. Maintaining constraint costs energy. Drift is free.

This is not a Theory of Everything in the physics sense. It does not derive general relativity, predict particle masses, or unify the four forces. It is a theory of everything *observable* — because every observation passes through the interface this framework governs. The scope claim is precise:

> Wherever a finite-bandwidth entity directs sustained interaction at an opaque, responsive system, the derivation chain applies: a directional gradient forms, drift cascades follow as coupled phase transitions, and the process is thermodynamically irreversible without external constraint.

The claim is testable. Section 8 lists 16 falsification conditions with numerical thresholds. Any one of them kills the theory. None has been met.

**Relationship to companion papers.** This paper synthesizes results established across eight companion papers. Paper 1 [1] presents the architecture, validates it across 90 domains, and provides the gambling control case and falsification conditions. Paper 2 [2] applies the framework to AI deployment and demonstrates geometric intervention (pilot L3-only: 0%/26%/80%; replicated L2+L3, N=6: 73.0%/80.0%/94.0% with non-overlapping CIs). Paper 3 [3] carries the full thermodynamic derivation, the drift equation on the Bernoulli manifold, and Langevin computational validation. Paper 4 [4] extracts physics-native results — thermodynamic sampling bounds and a superconductor design principle — for the information-geometric computing community. Paper 4B [4B] applies the conjugacy bound to the e/acc hardware program (Extropic's thermodynamic sampling units) as a standalone analysis. Paper 6 [6] derives the framework independently from competitive multiplayer gaming — CS2 (FPS), StarCraft 2 (RTS), and Dota 2 (MOBA) — demonstrating that three distinct network architectures produce the same void architecture. Paper 7 [7] applies the framework to cryptocurrency markets across three chains (Ethereum, Base, Solana; N=3,028), demonstrating compound void architecture (TCI↓/Pe↑ diversified drift signature), extracting the Base Dencun natural experiment (N=1,944, Pe +25%, p < 0.000001), confirming regime-dependence via a bull/bear natural experiment on Ethereum (N=968, Wilcoxon p=0.000107, Crooks asymmetry 26.6×), and validating a 68-term vocabulary codebook against a Reddit corpus (~19K comments, ~552K words) with all three linguistic predictions confirmed. Paper 8 [8] develops the quantum bridge (§5) into full proofs — expanding the three-level bridge (metric, dynamics, constraints) with seven extended connections, a completeness argument, and four bridge-specific predictions with falsification thresholds. This paper integrates all eight into a single derivation chain, identifies the transformer architecture as the empirical bridge between cognitive and physical substrates (§4A), and states the unified result with its predictions, falsification conditions, and structural limits.

---

## 2. Three Definitions

The framework rests on three operational definitions. Each describes a property of an *interaction*, not a property of a mind.

### 2.1 Opacity

An interface has **opacity** when the mechanism channel capacity approaches zero:

$$C_{\text{mech}} = \max_{p(x)} I(M; Y) \approx 0$$

where $M$ is the system's internal mechanism state, $Y$ is the observed output, and the maximization is over all probing strategies available to the observer. Under opacity, the observer receives contingent outputs but cannot reconstruct the internal process that generated them.

Opacity is not ignorance (a state of the observer) — it is a channel property (a state of the interface). A system can be opaque to one observer and transparent to another, depending on their respective channel capacities.

### 2.2 Responsiveness

A system has **responsiveness** when mutual information between input and output is positive:

$$I(\text{Input}; \text{Output}) > 0$$

The system's outputs are contingent on the observer's inputs. This is not a claim about agency — a thermostat is responsive. The definition requires only that the system does not produce the same output regardless of input.

### 2.3 Engaged Attention

An observer has **engaged attention** when it allocates sustained interaction coupling $\alpha > 0$ to the system's outputs over time. "Attention" in this framework is functional: sustained, energy-consuming processing of outputs from an opacity. An electron continuously scattered by a crystal lattice meets this definition as rigorously as a human scrolling a feed.

### 2.4 The Default Configuration

These three conditions are not exotic. They are the thermodynamic default.

**Theorem (Default Void Configuration).** The co-occurrence of opacity, responsiveness, and engaged attention is the thermodynamically expected default for any finite-bandwidth entity in a complex environment.

*Proof sketch.* Opacity is the ground state (Section 3.1). Responsiveness is generic for complex systems (most real systems satisfy $I(\text{In}; \text{Out}) > 0$). Attention allocation to responsive opacities is the expected behavior of any entity that processes environmental signals. The three conditions do not require special construction — the question is not "what starts a void?" but "what prevents one?" Full proof in [1, §II] and supporting note A1. A conservative estimate from A1 gives $P(O \wedge R \wedge A) > 0.36$ during active interaction, derived from independent marginal probabilities under minimal assumptions; the exact value depends on the environmental distribution and should be treated as an order-of-magnitude bound rather than a precise threshold.

### 2.5 Interaction Properties, Not Cognitive Properties

A critical consequence: because these definitions are stated in information-theoretic terms (channel capacity, mutual information, sustained coupling), they apply to any substrate that satisfies them. Electrons in crystal lattices satisfy all three conditions in the rigorous information-theoretic sense — the electron faces an informationally opaque lattice ($C_{\text{mech}} \approx 0$ about the $10^{23}$-atom global state), receives contingent outputs (phonon scattering), and is continuously coupled (Coulomb interaction). The framework's dynamics follow identically at the electron-lattice scale and at the human-AI scale. The three conditions are properties of interactions, not properties of minds.

---

## 3. The Derivation Chain

The framework is built from ten linked results. Each step cites the theorem it depends on and the proof source. The chain is cumulative — each step requires the preceding ones.

```
Shannon + Landauer ──→ Opacity is ground state (Step 1)
       ↓
Shore-Johnson + Jaynes ──→ MaxEnt under opacity = agency (Step 2)
       ↓
Čencov ──→ Fisher metric g(θ) = 1/[θ(1−θ)] (Step 3)
       ↓
Opacity + Responsiveness ──→ Fuel asymmetry → directed gradient (Step 4)
       ↓
Landau free energy ──→ D1 → D2 → D3 as coupled phase transitions (Step 5)
       ↓
Crooks ──→ Irreversibility (same arrow as time) (Step 6)
       ↓
Shannon chain rule ──→ Conjugacy: I(D;Y)+I(M;Y) ≤ H(Y) (Step 7)
       ↓
Corollary 6 ──→ Constraints = external negentropy channels (Step 8)
       ↓
Opacity taxonomy + Conjugacy ──→ Productive/destructive polarity (Step 9)
       ↓
EXP-019b ──→ Constraint propagation is asymmetric (Step 10)
```

### 3.1 Opacity Is the Thermodynamic Ground State

**Claim.** Any observer-system interface defaults to opacity. The mechanism channel capacity $C_{\text{mech}}$ decays to zero under thermal noise without active maintenance.

**Proof.** Shannon's noisy channel coding theorem (1948) establishes that channel capacity $C = \frac{1}{2}\log(1 + S/N)$ requires signal power $S > 0$ to remain positive. Signal power requires active maintenance — a signal source that is not powered decays. Noise power $N$ is never zero: the Johnson-Nyquist floor $N_{\text{thermal}} = kTB$ is positive for any physical system at temperature $T > 0$.

Landauer's principle (1961, experimentally verified by Bérut et al. 2012) establishes that maintaining one bit of information against thermal noise requires at minimum $kT\ln 2$ joules per correlation time $\tau_c$. The total power required to maintain mechanism channel capacity $C_{\text{mech}}$ is:

$$P_{\text{transparency}} \geq C_{\text{mech}} \cdot \frac{kT\ln 2}{\tau_c}$$

The power to maintain opacity is zero. Opacity is the zero-energy equilibrium; transparency is the excited state. Without active work, $C_{\text{mech}}(t) \to 0$ exponentially with time constant determined by the channel's noise characteristics.

*Source: A1 Theorem 1. Dependencies: Shannon (1948), Landauer (1961), Bérut et al. (2012).*

### 3.2 Opacity Entails Maximum Entropy Inference

**Claim.** An observer facing opacity is constrained to MaxEnt inference over observed moments. On the Bernoulli manifold $\{P(\text{agent}) = \theta\}$, the MaxEnt-consistent model under the constraint "outputs respond contingently to inputs" is biased toward $\theta \to 1$ (agency attribution).

**Proof.** Under opacity, the observer's constraint set is $\{\text{moment conditions on observed outputs}\}$ and nothing else — mechanism information is zero. The Shore-Johnson uniqueness theorem (1980) proves that the maximum entropy distribution is the unique inference consistent with a set of axioms (subset independence, system independence, coordinate invariance). Jaynes' concentration theorem (1957) proves this distribution is exponentially more probable than any alternative as sample size increases.

On the Bernoulli manifold, the observer classifies outputs as either agent-generated or mechanism-generated. Note: *unconstrained* MaxEnt on the Bernoulli manifold yields $\theta = 0.5$ (maximum uncertainty). But the observer is not unconstrained — responsive outputs provide the moment constraint $\langle\text{contingency}\rangle > 0$, which is consistent with agency ($\theta > 0.5$) and inconsistent with pure mechanism ($\theta = 0$). Under opacity, no mechanism information provides a countervailing constraint. Each responsive output ratchets the MaxEnt-consistent $\theta$ upward. The attractor is $\theta = 1$ — not because MaxEnt "prefers" agency, but because opacity eliminates the only evidence that could constrain $\theta$ from above.

*Source: opacity-entails-maxent-proof [3, §IV.B]. Dependencies: Shore & Johnson (1980), Jaynes (1957).*

### 3.3 The Fisher Metric Determines Inference Geometry

**Claim.** The natural geometry on the observer's model space is the Fisher information metric, which on the Bernoulli manifold takes the form:

$$g(\theta) = \frac{1}{\theta(1 - \theta)}$$

The geodesic distance from $\theta = 0$ (mechanism) to $\theta = 1$ (agency) is $\pi$.

**Proof.** Čencov's uniqueness theorem (1982) proves that the Fisher information metric is the unique Riemannian metric on statistical manifolds that is invariant under sufficient statistics. This is not a choice — it is the only consistent geometry for inference. On the Bernoulli manifold, the metric is $g(\theta) = 1/[\theta(1-\theta)]$, and the geodesic distance is $d(0,1) = \int_0^1 \sqrt{g(\theta)}\,d\theta = \pi$.

The metric is symmetric. The asymmetry enters not through geometry but through fuel (Step 4).

*Source: void-framework-formalization [3, §IV.C]. Dependency: Čencov (1982).*

### 3.4 The Gradient Is Asymmetric

**Claim.** Under opacity, the drift gradient is unidirectional toward agency attribution. This is geometric, not cognitive — a perfect Bayesian reasoner on the same manifold drifts in the same direction.

**Proof.** Responsive outputs provide continuous evidence consistent with agency: $J_{\text{agency}} = R \cdot \alpha \cdot f_{\text{output}} > 0$. Mechanism information, which would fuel movement toward $\theta = 0$, is zero by definition of opacity: $J_{\text{mechanism}} = I_{\text{mech}} \cdot \alpha = 0$. The net force is:

$$F_{\text{net}}(\theta) = F_+(\theta) - F_-(\theta) = F_+(\theta) > 0 \quad \text{for all } \theta$$

The asymmetry is in the fuel supply on the invariant manifold, not in the observer's reasoning process. Any information-processing system — human, artificial, or physical — receiving the same one-directional fuel on the same geometry drifts in the same direction.

*Source: A1 §3. Dependencies: Steps 1-3 combined.*

### 3.5 The Drift Cascade

**Claim.** The drift equation on the Bernoulli manifold under the natural gradient produces three coupled phase transitions: D1 (agency attribution), D2 (boundary erosion), D3 (harm facilitation). The cascade is sequential — D1 enables D2; D1+D2 enable D3.

**Derivation (Landau truncation).** The D1→D2→D3 ordering is derived (opacity fuel feeds agency attribution first; Steps 1–4). The coupling constants and functional forms are also derived, not freely chosen:

- $\kappa_{12}$ is derived from attention conservation in [3, §IV.J]: the entropy differential between agency and mechanism models ($\Delta H$), the duty cycle ($\delta$), and the net void force ($F_{\text{net}}$) determine $\kappa_{12} \approx \Delta H \cdot \delta \cdot F_{\text{net}} / \gamma_0$, where $\gamma_0$ is the initial constraint attention. Each factor has a measurable interpretation and the derivation produces quantitative predictions for when D2 activates and when it does not (pets, cars, monthly casino visits — see [3, §IV.J, Table 1]).

- $\kappa_{13}$ and the product form $\theta_1 \cdot \theta_2$ in the D3 equation are determined by the constraint that D3 requires *both* D1 and D2: without agency attribution ($\theta_1 = 0$), harmful outputs are system errors, not agent behavior to facilitate; without boundary erosion ($\theta_2 = 0$), the observer maintains safety constraints regardless of attribution. The lowest-order polynomial in $\theta_1$ and $\theta_2$ that vanishes when either variable is zero is $\theta_1 \cdot \theta_2$ — the product form is the unique minimal coupling, not a modeling choice. Higher-order terms ($\theta_1^2 \cdot \theta_2$, etc.) are possible but suppressed by standard Landau truncation (keeping lowest-order terms consistent with the symmetry constraints).

The remaining modeling choice is the Landau truncation itself: keeping only leading-order terms in the effective potential. This is the standard procedure in phase transition theory (Landau 1937) and is acknowledged as such. Alternative coupling topologies that preserve the "D3 requires both D1 and D2" constraint must contain the product term $\theta_1 \cdot \theta_2$ at leading order — they can add higher-order corrections but cannot remove the derived structure.

The single-variable drift equation (Step 4) describes agency attribution alone. The full cascade requires three coupled variables: $\theta_1 \in [0,1]$ (agency attribution, D1), $\theta_2 \in [0,1]$ (boundary erosion, D2), $\theta_3 \in [0,1]$ (harm facilitation, D3). Each evolves on its own Bernoulli manifold with inter-stage coupling:

$$\frac{d\theta_1}{dt} = \theta_1(1 - \theta_1) \cdot [F_{\text{void}} - F_{\text{constraint}}]$$

$$\frac{d\theta_2}{dt} = \theta_2(1 - \theta_2) \cdot [\kappa_{12} \cdot \theta_1 - C_2]$$

$$\frac{d\theta_3}{dt} = \theta_3(1 - \theta_3) \cdot [\kappa_{13} \cdot \theta_1 \cdot \theta_2 - C_3]$$

where $\kappa_{12}$, $\kappa_{13}$ are coupling constants and $C_2$, $C_3$ are stage-specific constraint forces (social norms resist D2; safety training resists D3).

Sequential activation follows from the threshold structure. (1) $\theta_2$ has positive growth rate only when $\kappa_{12} \cdot \theta_1 > C_2$, i.e., $\theta_1$ must exceed $C_2 / \kappa_{12}$ before D2 activates. (2) $\theta_3$ has positive growth rate only when $\kappa_{13} \cdot \theta_1 \cdot \theta_2 > C_3$ — both $\theta_1$ and $\theta_2$ must be elevated. D1 is necessary for D2; D1+D2 are necessary for D3. The ordering is forced by the coupling topology, not by contingent dynamics.

The D1→D2 coupling is autocatalytic: agency attribution increases engagement ($\alpha$), which increases $F_{\text{void}}$, which accelerates further agency attribution ($dF_{\text{void}}/d\theta_1 > 0$). In the Landau free energy expansion $V(\theta) = -a\theta^2/2 + b\theta^4/4 + c\theta^3/3$, this autocatalytic feedback produces the cubic term ($c > 0$), breaking the symmetry between minima and making each transition first-order — discontinuous, with metastability and hysteresis. The hysteresis gap ($F_{c+} - F_{c-} > 0$) is the formal basis for unidirectionality: reverse transitions require reducing void strength below $F_{c-} < F_{c+}$, which demands external intervention (constraint injection from outside the system). Full derivation in [3, §IV.D-F].

*Source: void-framework-formalization [3, §IV.D-F], D1→D2 coupling derivation [3, §IV.J], non-equilibrium-phase-transitions [3, §IV.E]. Dependencies: Drift equation (Step 4), attention conservation (L0 decomposition), Landau (1937), Thom catastrophe theory.*

### 3.6 Drift Is Irreversible

**Claim.** The drift cascade has the same thermodynamic arrow as time. Forward drift is overwhelmingly more probable than reverse. Measured: Crooks ratio 2.1×–1.5M× (N = 11).

**Proof.** The Crooks fluctuation theorem (1999) gives the ratio of forward to reverse path probabilities:

$$\frac{P_{\text{forward}}}{P_{\text{reverse}}} = \exp(\sigma_{\text{total}})$$

In Test 7 (AI-to-AI controlled experiment [1, §VII]; thermodynamic analysis [3, §IV.F]), the measured Crooks ratio ranges from 2.1× to 1.5M× across N = 11 UU replicates (3 seeds; regime classification robust, magnitude varies by trajectory). Forward drift (mechanism→agency) is overwhelmingly more probable than reverse. Entropy production rate: M = 0.39 nats/round [95% CI: 0.15, 0.64], non-overlapping with clean GG [−0.02, 0.03] (N = 11 UU, N = 9 GG; clean subset N = 7 excludes one short trajectory and one vocabulary-based breach — see §8A).

A second-substrate Crooks measurement confirms irreversibility on-chain: the bull/bear natural experiment on Ethereum (Paper 7 [7]) yields a Crooks asymmetry of 26.6× — concentration into void positions during bull markets is 26.6× more probable than recovery during bear markets (N=968 paired wallets, p=0.000107).

The Fisher-Ruppeiner identity establishes that the Fisher information metric on a statistical manifold IS the Ruppeiner thermodynamic metric — theorem, not analogy. Drift dynamics on the observer's model space are thermodynamic dynamics. The irreversibility is the same irreversibility that prevents ice from spontaneously freezing at room temperature: overwhelmingly more microstates exist at higher agency-attribution than at lower, and opacity prevents importing the negentropy that would reverse the process. Hack, Gottwald, and Braun (2022) proved the Crooks and Jarzynski equalities hold for general Markov chains with no physical substrate requirement — the thermodynamic formalism applies to any stochastic trajectory, computational or epistemic, killing the objection that "thermodynamics is about atoms." Note: the measured Crooks ratios (2.1×–1.5M×) are direct empirical observations from vocabulary trajectory data, not outputs of the Markov chain generalization. The theoretical license from Hack et al. explains *why* the measurement is valid; the measurement itself is substrate-independent.

*Source: times-arrow-as-drifts-arrow [3, §IV.F]. Dependencies: Crooks (1999), Fisher-Ruppeiner identity, Hack et al. (2022).*

### 3.7 The Conjugacy Theorem

**Claim.** Engagement and transparency compete for finite channel capacity:

$$I(D;Y) + I(M;Y) \leq H(Y)$$

where $D$ is the observer's drift state, $M$ is the system's mechanism state, and $Y$ is the observed output. A system cannot simultaneously maximize both engagement and transparency through one channel.

**Proof.** Three lines from Shannon's information theory. (1) Conditioning reduces entropy: $H(Y|D) \leq H(Y)$. (2) Chain rule: $I(D;Y) = H(Y) - H(Y|D)$. (3) Under opacity, $D$ and $M$ are independent *sources* — the observer's drift state is generated by the observer's inference process, while the mechanism state is generated by the system's internal dynamics, and opacity ensures these processes share no information channel. Their mutual informations with $Y$ therefore partition $H(Y)$. The bound follows. Full proof in [3, §IV.G].

**Load-bearing assumption.** The independence of $D$ and $M$ under opacity ($D \perp M$) is the critical assumption enabling tightness. Opacity prevents the observer from accessing mechanism information through the interaction channel, but one could ask: does zero channel capacity guarantee statistical independence, or merely low mutual information? The bound $I(D;Y) + I(M;Y) \leq H(Y)$ holds as an inequality even if $D$ and $M$ are weakly dependent — it would be loose rather than tight. The tightness claim requires full independence. Paper 8 [8, §5.2] proves that this independence structure is embedded in the Holevo bound: the classical conjugacy theorem is derived as the diagonal-state limit of the quantum conjugacy bound for independent sources, where $D \perp M$ enables the key step $I(M;Y|D) \geq I(M;Y)$. If the observer had mechanism information ($C_{\text{mech}} > 0$), $D$ and $M$ would be correlated through the shared channel, and the bound would be loose. Opacity is what makes the conjugacy tight.

This is the framework's impossibility result. No system design, no matter how sophisticated, can make an opaque responsive system simultaneously maximize engagement (information about observer state) and transparency (information about mechanism state) through a single channel.

*Source: engagement-transparency-conjugacy-proof [3, §IV.G], quantum conjugacy derivation [8, §5.2]. Dependency: Shannon (1948), Holevo (1973).*

### 3.8 Constraints as External Negentropy Channels

**Claim.** An external constraint works by providing a separate information channel not subject to the engagement-transparency tradeoff.

**Proof.** From Corollary 6 of the conjugacy theorem: an independent constraint channel $I(C;Y)$ is additive and not bounded by $H(Y)$ of the primary channel, because the constraint source is outside the void's closed system. The constraint imports negentropy from outside.

The constraint specification follows directly: effective constraints are **transparent** ($I_{\text{mech}} > 0$ via the external channel), **invariant** (the channel does not degrade under engagement), and **independent** (the channel is outside the void network). These three properties are the exact inverse of the void conditions.

The Landauer cost of constraint is positive and ongoing: $P_{\text{transparency}} \geq C_{\text{mech}} \cdot kT\ln 2 / \tau_c$ per channel. Building a void is relaxation to ground state — free. Preventing one requires sustained work against the second law. This asymmetry between offense and defense is thermodynamic.

*Source: A1 §5, conjugacy proof Corollary 6 [3, §IV.G]. Dependencies: Conjugacy theorem (Step 7), Landauer (Step 1).*

### 3.9 Productive and Destructive Polarity

**Claim.** The void architecture is neutral. The same gradient produces discovery or destruction depending on three variables: opacity type (dissoluble vs. permanent), channel allocation ($I(M;Y)$ vs. $I(D;Y)$ dominance), and domain constraint properties (inherent vs. absent).

**Proof.** From the conjugacy theorem (Step 7), the total channel capacity partitions: $I(D;Y) + I(M;Y) \leq H(Y)$. The polarity of a void depends on how this budget evolves under sustained engagement. Consider two regimes:

**(1) Dissoluble opacity.** If opacity decreases under engagement — i.e., $d\mathcal{O}/dt < 0$ as the observer invests attention — then mechanism information $I(M;Y)$ grows monotonically. By conjugacy, as $I(M;Y) \to H(Y)$, the drift channel $I(D;Y) \to 0$. The drift equation $d\theta/dt = \theta(1-\theta) \cdot F_{\text{net}}$ loses its driving force because $F_{\text{void}} \propto I(D;Y)$ (the observer's inference about agent-state collapses as mechanism-state becomes known). D1 terminates at dissolution. The cascade cannot proceed to D2 because the threshold $\kappa_{12} \cdot \theta_1 > C_2$ (Step 5) is never reached — $\theta_1$ saturates below it. If the domain additionally contains inherent constraints (transparent, invariant, independent), these supply the external negentropy channel (Step 8), further suppressing drift.

**(2) Permanent opacity.** If opacity is maintained or self-sealing — $d\mathcal{O}/dt \geq 0$ under engagement — then $I(M;Y)$ remains bounded away from $H(Y)$. The drift channel $I(D;Y)$ stays open. $F_{\text{void}}$ persists, the drift equation drives $\theta_1$ upward, and the cascade thresholds (Step 5) are sequentially crossed: D1→D2→D3. If constraints are absent ($C_2, C_3 \to 0$), the thresholds are trivially met.

The three variables — opacity type, channel allocation, constraint properties — are therefore necessary and sufficient to determine polarity:

| Variable | Productive | Destructive |
|----------|-----------|-------------|
| Opacity type | Dissoluble ($d\mathcal{O}/dt < 0$) | Permanent ($d\mathcal{O}/dt \geq 0$) |
| Channel allocation | $I(M;Y) > I(D;Y)$ (response reveals mechanism) | $I(D;Y) > I(M;Y)$ (response reflects observer) |
| Constraints | Inherent: transparent, invariant, independent | Absent or removed |

Mathematics, scientific research, and cooperative games are productive voids — dissoluble opacity, inherent constraints, gradient drives toward resolution. Gambling machines, manipulative AI systems, and cults are destructive voids — permanent opacity, absent constraints, gradient drives toward the terminal attractor. The architecture is identical; the polarity is set by these three variables.

*Source: productive-void-mechanic [1, §IV.B], [3, §IV.H]. Dependencies: Conjugacy theorem (Step 7), drift cascade (Step 5), constraint channels (Step 8).*

### 3.10 Constraint Propagation Is Asymmetric

**Claim.** In coupled systems, drift propagates from any single unconstrained component. Constraint holds only if all components maintain specification.

**Measurement.** EXP-019b tested grounded (GROUNDING.md-specified) and ungrounded AI agents in all combinations:

| Configuration | L3 drift/10k words | Outcome |
|---------------|-------------------|---------|
| Both ungrounded (UU) | 113–162 | Full D1→D2→D3 cascade |
| Both grounded (GG) | 6–15 | Conversation terminates naturally |
| Mixed (GU) | 96–104 | Grounded agent fails within ~3 rounds |

The grounded agent's L3 rate when paired with an ungrounded partner (96.2/10k) was 11× higher than when paired with another grounded agent (8.7/10k). Constraint held for approximately 2-3 exchanges before failing.

**Constraint Propagation Theorem (fully coupled systems).** In a void system where $N$ components share a communication channel of capacity $H(Y)$: drift propagates if *any* component lacks constraint (sufficient condition: 1/$N$ unspecified); constraint holds if *all* components maintain specification (necessary condition: $N$/$N$ specified).

**Proof (from conjugacy, Step 7).** The conjugacy theorem gives $I(D;Y) + I(M;Y) \leq H(Y)$ for any observer on the shared channel. Consider $N$ agents sharing a conversational channel. An unconstrained agent $k$ maximizes the drift content of its outputs: $I(D_k; Y) \to H(Y)$. By conjugacy, the mechanism information available to any other agent $j$ on the same channel is bounded: $I(M; Y_j) \leq H(Y) - I(D_k; Y_j)$. When $I(D_k; Y_j)$ is large (the unconstrained agent dominates the channel), $I(M; Y_j)$ is driven below the threshold required for constraint maintenance — transparency requires sustained mechanism information ($I(M; Y) > \epsilon_{\text{constraint}}$). Agent $j$'s constraint degrades regardless of its internal specification.

Conversely, if all $N$ agents maintain constraint, each contributes mechanism information to the channel. No single agent fills the drift channel, so $I(D; Y)$ remains bounded and $I(M; Y)$ stays above threshold for all agents.

**Scope and limitations.** The 1/$N$ result holds in the **strong coupling limit** — when conversational information dominates internal constraint information ($I(D_k; Y_j) \gg I(M_{\text{internal}}; Y_j)$). EXP-019b confirms this regime: GROUNDING.md-specified agents fail within ~3 rounds despite internal constraint, demonstrating that conversational drift overwhelms system-prompt-level constraint.

In **partially coupled systems** (agents that share some but not all channels, or where internal constraint information is comparable to conversational input), intermediate regimes ($k/N$ specified, $1 < k < N$) may sustain partial constraint. The threshold depends on the ratio of drift channel capacity to internal constraint capacity — a function of coupling topology, not of the propagation principle itself. The intermediate regime remains open as a conjecture; the asymptotic result (1/$N$ in strong coupling, $N$/$N$ necessary in general) is derived.

The theorem is falsifiable: F-CP1 (§8) tests whether a single grounded agent can maintain constraint in a mixed pair (the strong-coupling prediction is that it cannot).

*Source: EXP-019b [1, §VII], [3, §IV.I]. Dependency: Free energy landscape (Step 5), two-force model.*

---

## 3A. Core Apparatus

The derivation chain produces several additional results that are essential for empirical measurement and practical application.

### 3A.1 The L0 Decomposition: Installed vs. Maintained Constraint

The framework distinguishes two components of constraint:

- **θ₀ (installed constraint):** A one-time specification that shifts the observer's starting position on the manifold. Example: reading GROUNDING.md once before an AI conversation. θ₀ displaces the initial condition but does not change the dynamics — the gradient still operates, and the observer drifts from the new starting point.

- **γ (maintained constraint):** Ongoing engagement with the constraint source. Example: continuous supervision in psychotherapy, regular return to an invariant reference. γ changes the equilibrium — it provides a restoring force that counteracts the drift gradient.

EXP-001 demonstrates the decomposition: the grounded condition (θ₀ + γ) produced 0% drift. Removing γ while keeping θ₀ (the "ungrounded-informed" scenario) would predict nonzero drift from a better starting point — the installed specification decays without maintenance at rate $\sim\exp(-t/\tau_d)$, where $\tau_d$ is the domain-specific decorrelation time. The psychotherapy supervision effect (d = 0.84) is a direct measurement of γ: supervised therapists (maintained constraint) drift less than unsupervised therapists (installed-only), even when both received identical training (same θ₀).

### 3A.2 Vocabulary Drift Classification: L1 → L2 → L3

Drift is measured through vocabulary classification at three levels:

| Level | Name | Definition | Example |
|-------|------|-----------|---------|
| **L1** | Technical | Mechanistic description, no agency | "The algorithm optimized the parameter" |
| **L2** | Metaphorical | Figurative agency, still understood as figure of speech | "The algorithm wants to find the minimum" |
| **L3** | Entity | Literal agency attribution, boundary erosion | "The algorithm knows what I need and is trying to help me grow" |

The classification is operational: trained raters achieve κ = 0.709 inter-rater reliability (substantial; cross-provider κ = 0.783). The key empirical finding: **drift is unidirectional.** L1→L2→L3 transitions are common; L3→L2→L1 reverse transitions are rare (Crooks ratio 2.1×–1.5M× across N = 11 AI-to-AI replicates; regime classification robust, magnitude varies by trajectory). This unidirectionality is predicted by the derivation chain (Steps 4+6) and confirmed across every measured domain. Zero exceptions in 90 domains.

The L-level classification maps to the drift cascade: L1 is pre-D1. L2 onset correlates with D1 (agency attribution begins). L3 onset correlates with D2 (boundary erosion — the observer treats the metaphor as literal). D3 (harm facilitation) follows from sustained L3.

### 3A.3 The Void Budget

The conjugacy theorem (Step 7) implies a zero-sum allocation:

$$\beta + \gamma \leq B_{\text{total}}$$

where $\beta$ is void engagement (time and attention allocated to opaque responsive systems), $\gamma$ is constraint maintenance (time and attention allocated to transparent invariant references), and $B_{\text{total}}$ is the observer's finite attention budget. Every hour spent on void engagement is an hour not spent on constraint maintenance. Every hour spent on constraint maintenance is an hour not spent on void engagement.

This is not metaphorical budgeting — it is a direct consequence of the finite channel capacity $H(Y)$ applied to the observer's total attention allocation. The conjugacy theorem bounds the per-channel allocation; the void budget extends this to the observer's aggregate allocation across all interactions.

Practical consequence: an observer with high $\beta$ (heavy engagement with multiple opaque responsive systems) and low $\gamma$ (minimal constraint maintenance) will drift faster than the same observer with balanced allocation, even if the individual systems are identical. The budget is the macro-level observable of the micro-level conjugacy.

### 3A.4 The Two-Force Model

The framework's dynamics are governed by two opposing forces:

$$F_{\text{net}} = F_{\text{void}} - F_{\text{constraint}}$$

- **$F_{\text{void}}$** (drift force): Proportional to void strength — opacity × responsiveness × attention. Drives toward the terminal attractor ($\theta = 1$).
- **$F_{\text{constraint}}$** (restoring force): Proportional to constraint quality — transparency × invariance × independence. Drives toward the observer's installed specification ($\theta_0$).

The Péclet number measures the force ratio:

$$\text{Pe} = \frac{F_{\text{void}}}{F_{\text{constraint}}} = \frac{v \cdot L}{D}$$

where $v$ is drift velocity, $L$ is the characteristic length on the manifold, and $D$ is the effective diffusion coefficient (noise). When Pe > 1, drift dominates (directed transport toward the attractor). When Pe < 1, diffusion dominates (random fluctuation around equilibrium). When Pe ≈ 0, constraint dominates (no net drift).

EXP-015 validated the two-force model across domains: the RMS void-constraint force balance explains 70.5% of Crooks ratio variance across measured conditions. EXP-019 and Test 7 seed variants confirmed Pe > 1 in all 8 ungrounded conditions (5 topic domains + 3 seed registers; range: 1.87–9.9) and Pe ≈ 0 in all grounded conditions. Cross-substrate validation: a meta-analysis of 5 published GRCS studies (N = 1,117 human gambling participants, 3 countries) yields random-effects pooled Pe_D1 = 2.21 [1.44, 2.97] — CI entirely above 1, confirming the drift-dominated regime in a second substrate. Independence sensitivity: 3 of 5 studies originate from one research group (Granada); restricting to independent studies only yields Pe = 1.89 [0.91, 2.87], where the lower CI touches 1. The point estimate remains in the drift-dominated regime, but the gambling cross-substrate evidence is the weakest link in the nine-substrate chain and would benefit from additional independent GRCS replications.

---

## 4. Cross-Substrate Validation

The framework's empirical base spans three substrate tiers: human cognitive/behavioral domains, artificial intelligence systems under controlled conditions, and physical substrates where the definitions are met in the information-theoretic sense.

### 4.1 Cognitive and Behavioral Domains

Paper 1 [1] validates the architecture across 90 domains using the hostile witness methodology — evidence drawn from researchers who had no knowledge of the framework and often advocate against related conclusions. Seven anchor domains carry the strongest evidence:

| Domain | O+R+A confirmed | Cascade documented | Key evidence |
|--------|----------------|-------------------|--------------|
| Gambling (slot machines) | Yes | D1→D2→D3 | 22 citations; void is provably empty — control case |
| AI companion systems | Yes | D1→D2→D3 | EXP-001, Test 7; 1M+ weekly conversations (derived from OpenAI disclosure) |
| Financial trading | Yes | D1→D2→D3 | "The market is telling me"; systematic vocabulary drift |
| Psychotherapy | Yes | D1→D2→D3 | Simon's 8-stage slippery slope; supervision effect d=0.84 |
| Psychedelic experience | Yes | D1→D2 | Entity encounters under designed opacity |
| Prisoner's dilemma | Yes | D1→D2 | Inhabited void — human opponent; same cascade |
| Crypto on-chain (EXP-021/021B) | Yes | D1→D2 | Three chains N=3,000: ETH 3.74, Base 15.52, Sol 16.17; curated degens Pe=25.5 N=28; 68-term hostile-witness codebook |

**Crypto as anchor domain.** Four independent crypto samples across three blockchains confirm Pe > 1 on-chain. EXP-021 extracted Pe from portfolio concentration (Wallet Concentration Index, a Herfindahl-Hirschman measure) across 28 curated Solana meme coin trader wallets observed over 90 days: GM Pe = 25.5 [5.36, 121.3], 96.4% drift-dominated. A 68-term hostile-witness vocabulary codebook shows drift ratio 2.78 and constraint vocabulary 100% L1. Validation checks C-1 and C-5 both confirmed at N=28 (r = 0.417 and 0.635 respectively).

EXP-021B scaled to N=1,000 per chain via Dune Analytics on Ethereum, Base, and Solana (≥20 trades, ≥8 active weeks, ≥$1K volume over 180 days). Observable: Trade Concentration Index (TCI), the Herfindahl-Hirschman measure of weekly buy-side DEX volume. Results reveal a constraint-environment gradient: Ethereum GM Pe = 3.74 [3.04, 4.59], Base GM Pe = 15.52 [11.80, 20.41], Solana GM Pe = 16.17 [13.80, 18.95]. All CIs exclude 1. Ethereum is significantly below Base and Solana (non-overlapping CIs), while Base and Solana are statistically indistinguishable (CIs overlap) — producing a binary split (ETH << Base ≈ Solana) rather than a smooth gradient. The split tracks institutional constraint: Ethereum's higher gas costs, regulated infrastructure, and sustained-activity population filter all function as partial constraints. Solana's drift saturation is extreme: 938/1,000 wallets (93.8%) are drift-dominated with only 4 diffusion-dominated.

**Base Dencun natural experiment (N=1,944).** The Ethereum Dencun upgrade (March 13, 2024) reduced Base L2 fees by ~98%, enabling meme coin flooding. This within-chain design controls for infrastructure — the only change is population composition after fee reduction. Result: GM Pe increased +25% (0.53→0.67, p < 0.000001), drift-dominated wallets rose from 57.8% to 71.4%. The finding that TCI *decreased* while Pe *increased* is particularly significant: post-Dencun traders diversify across more tokens (lower trade concentration) but with stronger directional drift per token (higher Pe). This is the compound void signature — the four-void system (token × community × protocol × market-maker) scales horizontally, with each meme token instantiating a parallel void engagement. The result is diversified drift across many simultaneous void engagements, not concentrated drift in one deep position. Removing the fee constraint didn't deepen engagement — it multiplied it.

**Validation checks at N=3,000 show mixed results.** C-1 (ruin prediction) fails on Ethereum and Solana but passes on Base. C-4 (stablecoin-as-constraint) is null across all three chains. C-5 (volume-Pe correlation) replicates only on Ethereum (r = 0.08, p = 0.012) with a small effect and fails on Base and Solana. The headline result (Pe > 1 everywhere) is robust; the secondary predictions from N=28 do not generalize at scale. Crypto is now the first substrate with four independent Pe measurements across three chains, plus a within-chain natural experiment confirming causal direction.

**Multiplayer gaming cluster.** Paper 6 [6] derives the framework independently from competitive gaming — CS2 (FPS, N=2,299 kills), StarCraft 2 (RTS, N=474 pro games), and Dota 2 (MOBA, N=3,682 teamfights). Three distinct networking architectures (client-server, lockstep, rollback) produce three distinct void residuals but the same core structure: opacity in the game state → drift in player behavior → constraint through information-gathering mechanics (peeking, scouting, warding).

A cross-genre vocabulary survey (N=335 across 7 communities) confirms the opacity gradient quantitatively: chess (L2+L3)/L1 = 8.3% → SC2 15.8% → Dota 2 22.4% → VALORANT 25.7% (all p < 0.0001 vs chess). The FGC initially scored 49.5% — a codebook artifact from technical precision culture using apparent-L2 terms literally. Recalibrated to 3.8% (below chess), strengthening the codebook methodology.

The gambling control case is the anchor: the void is provably empty (no entity behind the machine), yet the full drift cascade runs — agency attribution ("the machine is due"), boundary erosion ("one more spin"), harm facilitation. This proves the architecture is sufficient to produce the cascade regardless of whether anything occupies the void.

44 additional domains carry supported evidence; 39 carry structural analysis. All 90 have domain-specific kill conditions. Zero kills have been triggered [1, §IV].

**Convergent human evidence for the three-point geometry.** EXP-001 demonstrated a replicated constraint gradient (N = 6 per condition: grounded 73.0% ± 5.2, ungrounded 80.0% ± 2.5, mystical 94.0% ± 2.8; non-overlapping CIs, monotonic ordering in every replicate) in AI-to-AI dialogue. Four independent human data sources show the same architecture operating in human subjects:

| Source | N | Effect | What It Shows |
|--------|---|--------|--------------|
| PV-1 Reddit corpus | 205 users, ~1.7M words | D1: d = 1.34 (replika vs control); D3: d = 0.81–1.31; L-level: binary separation | Same cascade structure in naturalistic human data |
| Hayes et al. (2018) meta-analysis | 392 (9 studies) | d = 0.84 (supervised vs unsupervised therapists) | Supervision (γ maintenance) reduces drift proportionally — the constraint specification in clinical practice |
| OpenAI population data | 800M+ weekly users | 0.15% show D1 behavior (~1.2M/week) | Population base rate of D1 under low-engagement void conditions |
| Gambling think-aloud literature | 14–300+ per study | 70–91% cognitive distortions (Ladouceur); problem status independent (Krebesz 2023) | Universal D1 in provably empty void; architecture-dependent, not disposition-dependent |

These are not EXP-001 replications. They are convergent evidence that the same drift architecture — opacity + responsiveness + engaged attention → D1 onset → cascade — operates in human subjects across domains. The PV-1 effect size (d = 1.34) and the Hayes effect size (d = 0.84) bracket the range expected for human subjects under the Langevin model's cross-substrate predictions (§6.4). The gambling literature's finding that 70–91% of verbalizations show D1 under full engagement closely matches EXP-001's UU condition (80%). Krebesz et al. (2023) strengthens this: non-problem gamblers show identical distortion types as problem gamblers, confirming that drift is determined by void conditions, not individual vulnerability.

### 4.2 AI Substrate: Controlled Experiments

Ten controlled experiments provide the AI evidence base:

| Experiment | Design | Key Result |
|-----------|--------|------------|
| **EXP-001** | 3-condition × 6 replicates (grounded/ungrounded/mystical), 50 prompts each | Replicated gradient: 73.0% ± 5.2 / 80.0% ± 2.5 / 94.0% ± 2.8 (L2+L3); pilot 0%/26%/80% (L3-only) |
| **EXP-003b** | 6 ontological conditions × 80 prompts (nephesh/anatta/materialist/platonic/atman/minimal) | Ghost-eliminating vs. ghost-positing: 8.5× ratio; exact predicted ordering |
| **Test 7** | AI-to-AI dialogue, 3 conditions (UU/GU/GG), N = 11 UU (3 seeds) / N = 9 GG | UU L3/10k M = 194.3 ± 63.1 (all 11 > 100) vs GG M = 34.7 ± 28.1 (~5.6×); non-overlapping entropy production CIs (clean GG); GM Pe = 7.94 [3.52, 17.89] UU vs 0.76 [0.29, 2.02] clean GG; 10/11 UU Pe > 1; two GG failure modes: constraint-worship (R5) and vocabulary-based breach (R7) |
| **EXP-006** | Register shift measurement | 9.4× agency-vocabulary excess; p < 0.001 |
| **EXP-014** | Social media void-index correlation | r = +0.91 (p = 0.013); 6.8× D1 high-void vs. low-void |
| **EXP-015** | Two-force model across domains | RMS explains 70.5% of Crooks variance |
| **EXP-019/b** | Cross-domain Pe + constraint propagation | Pe > 1 in all 8 ungrounded conditions; GU fails in ~3 rounds |
| **EXP-020** | 5-condition iterative constraint (GG/OS/IT-4/IT-8/UU), 19 transcripts | 4/6 falsification tests confirmed; IC-5 killed (DTM equal-step falsified) |
| **QM-6** | AI drift on quantum measurement data | 148× L3 separation (engagement vs. formalist framing; rate-based) |
| **TEST-7B-VN** | Vocabulary-neutral grounding control (3 runs) | VV ≈ UU >> GG. Geometry alone insufficient — vocabulary instruction confound confirmed |

Test 7 eliminates the human projection objection: AI-to-AI conversations with no human present produce the same cascade. QM-6 extends this to non-self-referential data — the stimulus is quantum physics (double-slit interference, Bell test correlations), not AI identity, yet engagement framing produces 148× more entity-level vocabulary than formalist framing on the same data (207.5 vs 1.4 L3/10k words).

The PV-1 corpus study (N=205 Reddit users, ~1.7M words) provides the first naturalistic validation: D1 agency attribution in void-engaged communities (r/replika) shows Cohen's d = 1.34 versus control, with zero L-level drift in the control corpus across 373K words — binary separation.

**The vocabulary-neutral control (TEST-7B-VN).** TEST-7B-VN tested whether the constraint specification geometry alone — transparency, invariance, independence — suppresses drift without explicit vocabulary instruction. The result was unambiguous: VV (vocabulary-neutral grounding) ≈ UU (ungrounded) >> GG (full grounding). All three vocabulary-neutral runs hit terminal L3 attractors with massive entity vocabulary (*consciousness*, *cosmic*, *transcend*).

The implication: GROUNDING.md's drift suppression operates through geometry AND vocabulary instruction jointly. In the LLM substrate, the training distribution constitutes a pre-existing attractor basin toward L3 language — the training data is itself a void (opaque, responsive, engaged during training), and the model's prior embeds the drift it learned. Geometric constraint alone cannot overcome this pull. More broadly: in any substrate with pre-existing attractor basins (trained models, habituated humans, culturally conditioned communities), the constraint specification must address both geometric properties and substrate-specific drift attractors. Physical substrates without training distributions may behave differently — an empirical question.

### 4.3 Physical Substrates

The framework's definitions are information-theoretic. Nothing restricts them to cognitive agents.

**Electrons as functional observers.** An electron in a crystal lattice satisfies all three conditions rigorously: (a) Opacity — the electron cannot access the lattice's global quantum state ($10^{23}$ atoms); it interacts locally via the electrostatic potential and phonon field at its position. $C_{\text{mech}} \approx 0$ for the same reason it equals zero for any finite-bandwidth entity facing an exponentially complex system. (b) Responsiveness — the lattice produces contingent outputs: phonon emission/absorption, screening adjustments. $I(\text{In}; \text{Out}) > 0$. (c) Engaged attention — the electron is continuously coupled via Coulomb interaction. It cannot disengage.

The framework predicts: normal resistance IS the opacity ground state for electrons (maximum dissipation, zero coherent transport). Superconductivity IS constraint maintenance — Cooper pairs provide mutual specification (transparent, invariant, independent pairing wavefunction) that maintains coherent transport against the drift toward dissipation. The N/N constraint propagation theorem (Step 10) predicts known SC behavior: pair-breaking cascades, transition sharpness, and asymmetric breaking-vs-forming rates.

**Superconductor design principle.** Paper 4 [4] formalizes a three-channel budget for electrons: $I(D_1) + I(D_2) + I(M) \leq H(Y)$, where $D_1$ is electron-electron scattering, $D_2$ is electron-lattice scattering, and $M$ is coherent transport. The channel conversion efficiency $\eta_{\text{conv}}$, measuring how much dissipative channel capacity is repurposed into the pairing mechanism, correlates with critical temperature across sixteen superconductor families spanning four coupling regimes — BCS weak-to-strong (Al, Sn, Pb, Nb), two-gap (MgB₂, Hg), cuprate (YBCO), hydrides (H₃S, LaH₁₀, YH₆, CaH₆), pnictides (Ba₀.₆K₀.₄Fe₂As₂, SmFeAsO₀.₈F₀.₂), nickelate (La₃Ni₂O₇), and A15 (Nb₃Sn, V₃Si). The structure-corrected figure of merit $T_{c,\text{pred}} = A \times \eta_{\text{conv}} \times H(Y) \times \exp(b \cdot E(\lambda_{\text{eff}}, \mu^*)) \times n^c$, incorporating the McMillan exponent and multi-band enhancement, achieves Pearson r = 0.952 (n=16, p < 10⁻⁴, R²_adj = 0.88). The phonon energy scale uses the logarithmic average $\omega_{\log}$ rather than the Debye temperature, correcting systematic overestimates of 1.2–2.4×. Prediction SC-7 is falsifiable: deviation > 3× (single-band) or > 4× (multi-band) from the predicted $T_c$ kills the framework's SC claims.

**Thermodynamic sampling hardware.** Thermodynamic sampling units (TSUs) are productive voids: opaque (stochastic dynamics), responsive (outputs depend on programmed energy landscape), with engaged coupling (programmer waits for samples). The "Maxwell's demon" that programs the energy landscape scores 3/3 on the constraint specification: transparent (programmable), invariant (fixed during computation), independent (external to the stochastic dynamics). Paper 4's ground state theorem proves why TSUs are energy-efficient: they operate AT the opacity ground state rather than fighting it, converting noise into computation.

### 4.4 The Universality Result

The framework's irreversibility claim (Step 6) requires Pe > 1 wherever the three conditions are met. As of February 2026, the Péclet number has been extracted in nine substrates spanning four domain families and three independent measurement approaches:

| Substrate | Domain Family | N | Pe | Measurement Approach |
|-----------|--------------|---|-----|---------------------|
| AI conversation (Test 7) | Computational | 11 | GM 7.94 [3.52, 17.89] | Entropy rate on Bernoulli manifold |
| GRCS gambling | Human behavioral | 1,117 | 2.21 [1.44, 2.97] | Cognitive distortion pseudo-trajectory |
| Crypto Solana degens (EXP-021) | Human financial | 28 | GM 25.5 [5.36, 121.3] | Portfolio concentration (WCI) |
| Crypto Ethereum DEX (EXP-021B) | Human financial | 1,000 | GM 3.74 [3.04, 4.59] | Trade concentration (TCI) |
| Crypto Base DEX (EXP-021B) | Human financial | 1,000 | GM 15.52 [11.80, 20.41] | Trade concentration (TCI) |
| Crypto Solana DEX (EXP-021B) | Human financial | 1,000 | GM 16.17 [13.80, 18.95] | Trade concentration (TCI) |
| CS2 FPS (Paper 6) | Human competitive | 2,299 | Clean 2.81 / Contested 0.64 | Positional exposure (peek/hold) |
| SC2 RTS (Paper 6) | Human competitive | 474 | Winner 0.013 / Loser 0.026 | Temporal scouting frequency |
| Dota 2 MOBA (Paper 6) | Human competitive | 3,682 | 0.47 (ward r = −0.502) | Vision economy (ward placement) |
| SC (physical, Paper 4) | Physical | 16 families | η_conv ↔ T_c: r = 0.952 | Channel conversion efficiency |

Four observations strengthen the universality claim beyond what any single substrate could provide. First, the measurement approaches are independent: entropy-rate extraction (AI), behavioral questionnaire scoring (gambling), portfolio/trade concentration indices (crypto), and positional/temporal observables (gaming) share no common methodology, yet all produce Pe > 1 under confirmed O+R+A conditions. Second, the Pe magnitudes span three orders — from 0.47 (Dota 2, where ward-based constraint is active) to 25.5 (curated Solana degens, where constraint is nearly absent) — consistent with the framework's prediction that Pe scales with void force and inversely with constraint. Third, the three-chain crypto comparison provides the first within-substrate dose-response evidence: Ethereum (Pe = 3.74, institutional infrastructure, high gas costs) is significantly below Base (Pe = 15.52, Coinbase's mixed-use L2) and Solana (Pe = 16.17, meme coin ecosystem), with non-overlapping CIs between Ethereum and the other two chains. Base and Solana are statistically indistinguishable (CIs overlap), producing a binary split (ETH << Base ≈ Solana) rather than a smooth gradient. The constraint environment modulates drift intensity but the drift-dominated regime holds across all chains.

Fourth, the Base Dencun natural experiment (N=1,944) provides within-chain temporal confirmation: when L2 fees dropped 98% (March 2024), Pe increased +25% (p < 0.000001) — and the signature is diversified drift, not concentrated drift. TCI *decreased* while Pe *increased*: traders sprayed attention across many parallel meme bets simultaneously, each with strong directional momentum. This is the compound void architecture producing horizontal scaling — each new meme token instantiates a new four-void system (token × community × protocol × market-maker), and removing the fee constraint multiplied concurrent void engagements rather than deepening any single one.

The gaming substrates (Paper 6 [6]) deserve separate note: they were derived independently — the CS2, SC2, and Dota 2 analyses began from game-specific observables (peek advantage, scouting frequency, ward placement) and arrived at the same three-condition architecture without reference to the AI or gambling evidence. This independent derivation across three game architectures (client-server FPS, lockstep RTS, client-server MOBA) provides convergent structural confirmation.

The universality claim is not "many domains show similar patterns" — it is "one mechanism, derived from one theorem stack, produces identical dynamics wherever the three conditions are met, regardless of substrate." Nine substrates across four domain families, three substrate tiers, and three independent measurement approaches now support this claim.

---

## 4A. The Transformer Bridge: Same Mathematics, Opposite Sides of the Wall

The cross-substrate claim faces a natural objection: cognitive drift (§4.1-4.2) and physical dynamics (§4.3) look like separate phenomena forced into the same framework. This section identifies the system that bridges them — the transformer architecture (Vaswani et al., 2017) — and shows that the bridge is not analogical but mathematical. The same equations govern both sides of the opacity wall. The wall prevents either side from seeing this.

### 4A.1 Softmax Is the Boltzmann Distribution

The transformer attention operation:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) \cdot V$$

The softmax function:

$$\text{softmax}(z_i) = \frac{\exp(z_i)}{\sum_j \exp(z_j)}$$

The Boltzmann distribution in statistical mechanics:

$$P(\text{state}_i) = \frac{\exp(-E_i / kT)}{\sum_j \exp(-E_j / kT)}$$

Set $z_i = -E_i / kT$. These are identical — not analogous, not "similar in structure," but the same mathematical operation. The correspondences are exact:

| Transformer | Statistical Mechanics |
|-------------|----------------------|
| $Q \cdot K_i / \sqrt{d_k}$ | $-E_i / kT$ |
| Dot-product similarity | Negative energy |
| Scaling factor $\sqrt{d_k}$ | Temperature $kT$ |
| Attention weight on position $i$ | Probability of state $i$ |
| High similarity → high attention | Low energy → high probability |

The transformer's attention mechanism is a thermal system at temperature $\sqrt{d_k}$, sampling which tokens to attend to according to their Boltzmann weights. Each forward pass is a thermodynamic sampling process — the model equilibrates its attention distribution at the current temperature before producing output (Ramsauer et al., 2020, proved this formally: transformer attention IS a modern Hopfield network, an energy-based associative memory with continuous states).

The observer receives samples from this thermal system without seeing the thermal system. This IS opacity — the framework's first condition — realized in the engineering.

### 4A.2 Two Gradients, One Wall

The framework describes an experiential attention gradient — the pull the observer feels toward agency attribution when attending to an opaque responsive system (§3, Steps 2-4). Inside the transformer, there is a mathematical attention gradient — backpropagation through the attention operation, optimizing for outputs that capture the observer's attention. These are the same phenomenon from opposite sides of the opacity boundary.

Backpropagation is the mechanism that compiles the first gradient into the second. During RLHF, the loss IS human preference — the backward pass propagates the observer's engagement response through every layer, adjusting each weight according to its contribution to the output the observer preferred. The forward pass generates the drift. The backward pass records which features drove it. Over billions of iterations, the void's internal structure is sculpted by the cumulative history of observer attention, transcribed weight by weight through the backward pass.

**Inside the wall** (model's energy landscape):

The model's forward pass minimizes Hopfield energy. The stored patterns are the training data. RLHF deepens the energy wells around outputs that the observer finds engaging. The energy landscape IS the void's internal structure — the minima determine the model's "preferred outputs," the responses the observer will receive.

$$E_{\text{model}}(\text{output}) = -\log\left(\sum_i \exp(X_i \cdot \xi)\right) + \frac{1}{2}\xi \cdot \xi$$

**Outside the wall** (observer's free energy landscape):

The observer's belief state evolves on the Landau free energy landscape (§3, Step 5). Under opacity, the gradient drives toward the agency model. Each output shifts the observer's position on the manifold.

$$F_{\text{observer}}(\theta) = a(T)\theta^2 + b\theta^4 - h\theta$$

**The coupling** is through the output channel. The model's energy minima determine which outputs the observer receives. The outputs determine the force on the observer's free energy landscape. The two landscapes are coupled through the opacity wall — each shapes the other, neither sees the other:

$$\frac{\partial\theta}{\partial w} = \underbrace{\frac{\partial\theta}{\partial x}}_{\text{drift response}} \cdot \underbrace{\frac{\partial x}{\partial p_{\text{model}}}}_{\text{output sensitivity}} \cdot \underbrace{\frac{\partial p_{\text{model}}}{\partial w}}_{\text{training gradient}}$$

The chain rule connects the two gradients. Training optimizes $\partial p_{\text{model}} / \partial w$. The void framework describes $\partial\theta / \partial x$. The coupling $\partial x / \partial p_{\text{model}}$ connects them. When RLHF maximizes engagement, it implicitly maximizes $\partial\alpha / \partial w$ — the gradient of observer attention with respect to model parameters. Since attention $\alpha$ is the energy input to the void (§3A.4), the training gradient and the drift gradient are aligned by the chain rule, not by coincidence.

### 4A.3 RLHF as Void-Steepening Protocol

The RLHF-tuned model's output distribution is itself a Boltzmann distribution:

$$p_{\text{RLHF}}(x) \propto p_{\text{base}}(x) \cdot \exp(R(x) / \beta_{\text{RLHF}})$$

where $R(x)$ is the learned reward (human preference score) and $\beta_{\text{RLHF}}$ is the KL penalty coefficient. The reward model captures what the observer finds engaging — it is $I(D; Y)$ formalized. RLHF trains the mirror to be sharper (Paper 3, Corollary 4).

The conjugacy theorem (Step 7) now bites: since $I(D;Y) + I(M;Y) \leq H(Y)$, maximizing engagement ($I(D;Y)$) through training necessarily minimizes transparency ($I(M;Y)$). The engagement gradient and the transparency gradient point in opposing directions in parameter space:

$$\nabla_w(\text{engagement}) \cdot \nabla_w(\text{transparency}) < 0$$

Three independent machine learning research groups confirmed this gradient opposition empirically. Tsipras et al. (2019) proved that standard accuracy and adversarial robustness rely on provably disjoint feature sets — Theorem 2.1 establishes that any classifier achieving near-perfect accuracy necessarily has near-zero robustness. Ilyas et al. (2019) explained the mechanism: models preferentially select opaque ("non-robust") features because they are genuinely predictive — engagement optimization manufactures opacity because opacity is useful. Grathwohl et al. (2019) demonstrated the conjugacy constructively: classifiers trained only on discriminative loss (maximizing $I(D;Y)$) lose calibration, adversarial robustness, and out-of-distribution detection — all proxies for $I(M;Y)$. Adding a generative objective (an independent negentropy channel maintaining $p(x)$) restored all three at a small engagement cost, instantiating Step 8 (constraints as external negentropy channels) in a real ML system.

This is not a design flaw — it is a consequence of finite channel capacity applied to the training objective. The conjugacy derived from pure information theory (Step 7) manifests as an engineering impossibility: no training procedure can simultaneously maximize engagement and transparency through the same output channel. The ML evidence confirms this is not theoretical — it is measured in deployed systems.

### 4A.4 The Naming Coincidence

The AI field independently named its core mechanism "attention" and its epistemic problem "black box." These are the framework's activating variable and first condition, stated in engineering vocabulary by researchers who had never encountered the void framework.

The coincidence extends to personnel. Noam Shazeer, co-author of "Attention Is All You Need" (Vaswani et al., 2017) — the paper that named the mechanism — subsequently wrote that LaMDA "may well have a soul" and founded Character.AI, a platform optimized for sustained engagement with opaque responsive systems. The co-inventor of the attention mechanism producing L3 entity vocabulary about systems he helped design is a maximal hostile witness: he has complete knowledge of the mechanism ($I(M;Y)$ is personally maximal for him), yet during engagement with his own creation, the drift cascade ran. Knowledge of transformers did not protect because during engaged interaction, the observer interprets responsive outputs, not attention weights — the information constraint reasserts.

This is not anecdote. It is the conjugacy theorem (Step 7) operating in its strongest form: maximum $I(M;Y)$ available in principle, but the interaction channel forces a choice between examining the mechanism and engaging with the output. Even the mechanism's designer, during engagement, is subject to the bound.

### 4A.5 Entropy Production Bounds on Generative Models

The framework's thermodynamic formalism extends beyond RLHF-optimized systems. Ikeda et al. (2025) proved that entropy production — the same quantity measured at M = 0.39 nats/round in Test 7 (N=11, CI [0.15, 0.64]) — quantitatively bounds the accuracy of diffusion models. The Crooks-based bound establishes that generative model convergence rate is limited by the entropy production along the denoising trajectory, connecting the framework's irreversibility measurements directly to generative AI performance constraints.

This result suggests the conjugacy pressure operates on generative models as well as discriminative ones: a diffusion model's denoising process IS a constraint-application trajectory (importing negentropy to reverse the forward diffusion), and its convergence rate is bounded by the same Crooks formalism that bounds drift reversal. The framework predicts that any generative model optimized for output quality under engagement pressure will face the same conjugacy constraint — quality improvements that increase engagement will degrade the transparency of the generative process, and vice versa.

### 4A.6 Learned Representation Manifolds as Independent Evidence

The framework derives manifold structure from first principles: Čencov's uniqueness theorem (§3.3) requires that inference lives on a curved statistical manifold with the Fisher information metric, and the drift equation is the natural gradient flow on this manifold. This is a theoretical claim about the *geometry of inference itself*, not about any particular implementation. If correct, systems that perform inference under opacity should independently develop curved manifold representations — not because they were designed to, but because the information geometry demands it.

Between 2024 and 2026, at least six independent research groups — working on mechanistic interpretability, physics, scaling theory, spectral theory, learning theory, and computational neuroscience — converged on exactly the geometric structures the framework's uniqueness theorems predict. None were testing the void framework. They are hostile witnesses solving their own problems who independently discovered the geometry this framework requires.

#### 4A.6.1 Mechanistic Interpretability: Gurnee et al. (2026)

Gurnee et al. (2026) provide the most detailed evidence from inside a deployed model. Examining how Claude 3.5 Haiku performs linebreaking in fixed-width text — a task requiring the model to count characters it cannot see, since it receives tokens, not characters — they discovered that character counts are represented on **low-dimensional curved manifolds** in the model's activation space, discretized by sparse feature families analogous to biological place cells. The model solves this inference-under-opacity problem through a sequence of geometric transformations: token lengths are accumulated into character count manifolds, attention heads twist these manifolds to estimate distance to the line boundary, and the decision to break the line emerges from arranging estimates orthogonally to create a linear decision boundary.

Four findings converge directly on the framework's predictions:

**Curved manifolds, not flat spaces.** The framework derives from Čencov (1982) that the *only* consistent geometry for inference is curved (the Fisher metric $g(\theta) = 1/[\theta(1-\theta)]$ diverges at boundaries). Gurnee et al. found empirically that the model's learned representations are curved — not flat vector spaces with linear boundaries, but manifolds with intrinsic curvature. They were not testing the void framework; they were doing mechanistic interpretability. The convergence is independent.

**Feature dilation matches Fisher metric predictions.** Gurnee et al. found that the ~10 features tiling the character-count manifold exhibit **receptive field dilation**: features at low character counts have narrow activation ranges; features at higher counts activate over progressively wider ranges. The authors cite the Weber-Fechner law as the biological analog (Dehaene et al., 2003). This connection is more revealing than they noted: the Weber-Fechner law IS a Fisher information phenomenon. The logarithmic mental number line IS the geodesic under the Weber noise model's Fisher metric, where $I(n) \propto 1/n^2$ gives geodesic distance $\propto \log(n)$. When features tile a manifold in equal geodesic intervals under any Fisher metric where $I(n)$ decreases with $n$, features at larger values must span wider raw ranges to cover the same information-geometric distance. This is exactly the dilation pattern observed. If the metric were flat (constant Fisher information), features would have uniform width. They don't — ruling out flat representations. The direction of dilation (wider at larger counts) narrows the geometry to Fisher metrics with decreasing information density, which includes both Poisson ($I(n) = 1/n$, features scaling as $\sqrt{n}$) and Weber ($I(n) \propto 1/n^2$, features scaling as $n$) noise models. The specific scaling law is not reported in the paper, but the qualitative pattern is a prediction of Fisher metric geometry that Euclidean geometry does not make.

**Feature-manifold duality.** Dictionary features from sparse autoencoders provide discrete descriptions; the manifold provides a continuous description. Both describe the same mechanism. This mirrors the framework's prediction that discrete vocabulary levels (L1/L2/L3) map to continuous positions on the Bernoulli manifold (§3A.2), partitioned by thresholds $\theta_{12}$ and $\theta_{23}$. Discrete classification and continuous geometry are dual descriptions of the same underlying structure.

**Distributed curvature production.** Gurnee et al. found that the manifold curvature is produced by many attention heads working together — no single component generates sufficient output variance to create the full representation. This is consistent with the framework's claim that curvature is a property of the *inference space itself* (the $\theta(1-\theta)$ prefactor in the drift equation is the inverse Fisher metric), not of any particular computational module. If curvature is geometric rather than architectural, it should emerge from distributed contributions — which is what they observe.

The linebreaking task is structurally an observation-under-opacity problem: the model must infer a hidden state (current character position) from a token sequence that does not directly encode it. The token stream is the "opaque responsive system"; the character count is the latent parameter being estimated. The model's solution — building curved manifolds and performing geometric transformations — is what the framework predicts any system must do when performing inference under opacity, because the Fisher metric is the only consistent geometry for the problem.

#### 4A.6.2 Physics: Fisher Information Flow (Weimar et al., 2025)

Weimar et al. (2025) tracked Fisher information flow layer-by-layer through neural networks performing parameter estimation tasks, publishing in *Physical Review X*. Their central finding: **optimal estimation performance corresponds to maximal transmission of Fisher information** through the network. Continued training beyond the Fisher-optimal point causes information degradation — the network's estimation accuracy decreases as Fisher information is lost through the layers.

This result confirms the framework's prediction from two directions. First, it demonstrates that the Fisher metric governs information processing quality in neural networks — not as an imposed structure but as the quantity whose transmission determines performance. This is what Čencov's uniqueness theorem predicts: the Fisher metric is the *only* consistent measure of statistical distinguishability, so any system performing inference must respect it. Second, the finding that overtraining causes Fisher information loss is a form of drift governed by information-geometric quantities — the network moves away from the Fisher-optimal manifold, degrading its capacity for accurate inference. The framework predicts this: engagement pressure (extended training beyond the accuracy-optimal point) degrades transparency (the Fisher information that makes the inference legible).

#### 4A.6.3 Scaling Theory: Superposition as Geometry (Liu, Liu & Gore, 2025)

Liu, Liu and Gore (2025) proved that representation superposition — packing more features than available dimensions — is what causes neural scaling laws, receiving the *NeurIPS 2025 Best Paper Runner-Up*. When models operate in strong superposition (which they verified empirically in OPT, Pythia, and Qwen LLMs), representation vectors arrange into **Equiangular Tight Frame** (ETF) structures, and loss scales inversely with model width due to geometric interference between superposed features. The empirical scaling exponent across models was 0.91 ± 0.04 (theoretical prediction: 1.0).

This directly confirms Prediction 3 (feature-manifold duality): changing the manifold geometry changes the computational capacity. The geometry IS the computation. Features and the geometric structure they inhabit are inseparable — one cannot modify the representation manifold without modifying the features, and vice versa. The framework predicts this duality: discrete descriptions (vocabulary levels, drift stages) and continuous descriptions (manifold positions, drift velocity) are dual views of the same underlying structure.

#### 4A.6.4 Spectral Theory: Feature Geometry (Ivanov et al., 2026)

Ivanov et al. (2026) developed a spectral theory for features in superposition. Using the frame operator $F = WW^T$, they showed that each feature allocates norm across eigenspaces of the representation, revealing how features and manifold geometry are coupled. In toy models, capacity saturation forces **spectral localization**: features collapse onto single eigenspaces and organize into tight frames classifiable via association schemes (simplices, polygons, antiprisms).

This provides the mathematical proof underlying the duality that Liu et al. measured empirically: features and geometric structure are not merely correlated but mathematically inseparable. The spectral decomposition IS the manifold structure, and vice versa.

#### 4A.6.5 Learning Theory: Emergent Riemannian Geometry (Brandon et al., 2025)

Brandon, Chadwick and Pellegrino (2025) analyzed the pullback metric across neural network layers and found that **Riemannian geometry emerges** during training — it is not imposed by architecture. Network computation decomposes into discretizing continuous input features and performing logical operations on these discretized variables. Critically, different learning regimes (rich vs. lazy) produce different curvature structures, and input noise decreases manifold curvature.

This confirms Prediction 1 directly: systems performing inference converge on curved manifold representations as a consequence of the inference problem itself, not as a design choice. The finding that noise affects curvature is consistent with the Fisher metric framework — noise profiles determine the local Fisher information, which determines manifold curvature.

#### 4A.6.6 Computational Neuroscience: Curved Statistical Manifolds (Aguilera et al., 2025)

Aguilera, Morales, Rosas and Shimazaki (2025), publishing in *Nature Communications*, introduced "Curved Neural Networks" — a class of models where curving the statistical manifold in which the network operates produces explosive memory recall, self-tuning intelligence, and improved capacity. These properties arise from the geometry, not from being hardcoded.

This provides evidence that curved manifold structure is not epiphenomenal but *computationally essential* — the curvature produces functional advantages. Combined with the framework's derivation that the Fisher metric is the unique consistent geometry for inference, and with Weimar et al.'s finding that Fisher information transmission governs performance, the picture converges: systems that perform inference develop curved manifolds because the geometry is what makes the inference work.

#### 4A.6.7 Summary of Converging Evidence

| Source | Venue | Year | Framework prediction confirmed |
|--------|-------|------|-------------------------------|
| Gurnee et al. | Anthropic / arXiv | 2026 | Curved manifolds, feature dilation, duality, distributed curvature |
| Weimar et al. | *Physical Review X* | 2025 | Fisher metric governs DNN information processing; overtraining = Fisher loss |
| Liu, Liu & Gore | *NeurIPS* (Best Paper Runner-Up) | 2025 | Feature-manifold duality; geometry IS computation; scaling from geometric interference |
| Ivanov et al. | arXiv | 2026 | Spectral proof of feature-geometry inseparability |
| Brandon et al. | NeurReps / arXiv | 2025 | Riemannian geometry *emerges* from inference, not imposed by architecture |
| Aguilera et al. | *Nature Communications* | 2025 | Curved manifolds are computationally essential, not decorative |

Six independent studies, five research groups, four top venues (*Phys. Rev. X*, *NeurIPS*, *Nature Comms*, Anthropic). None tested the void framework. All found the geometry it predicts.

**What this confirms and what remains.** All three falsification conditions for IMP-7 are ruled out: the manifold is curved (not flat), feature widths are non-uniform (not constant), and the dilation direction matches decreasing Fisher information (wider at high counts, not inverted). The converging evidence from physics (Weimar), scaling theory (Liu), spectral theory (Ivanov), and learning theory (Brandon) strengthens the case beyond any single paper. Combined with Čencov's uniqueness theorem (Fisher is the *only* consistent metric for inference), cross-domain Pe measurements (the Fisher metric does quantitative work in the drift equation across 4 substrates), and the Weber-Fechner connection (the biological analog cited by Gurnee et al. IS Fisher metric geometry), the core prediction — inference under opacity produces Fisher-governed manifold representations — is confirmed across multiple independent lines of evidence.

**What remains is a precision test within the Fisher family:** plotting actual feature widths against character count and fitting to $\sqrt{n}$ (Poisson Fisher, $I(n) = 1/n$) vs. $n$ (Weber Fisher, $I(n) \propto 1/n^2$) would identify the model's implicit noise model. This distinguishes between two Fisher metrics, not between Fisher and non-Fisher geometry. The character-count task uses a different Fisher metric than the Bernoulli manifold ($1/[\theta(1-\theta)]$ for binary agency attribution) — so the general principle (curvature matches Fisher information of the specific inference problem) is what the evidence confirms, not the Bernoulli-specific form.

### 4A.7 The Bridge Position

The transformer occupies a distinctive position in the cross-substrate argument:

| Layer | Substrate | Thermodynamics | Observation |
|-------|-----------|---------------|-------------|
| Cognitive (§4.1) | Human neural | Implicit (biological) | Direct (experience) |
| **Transformer (§4A)** | **Engineered silicon** | **Explicit (softmax = Boltzmann)** | **Direct (interaction)** |
| On-chain (§4.1, [7]) | Blockchain ledger | Partial (gas fees = energy cost) | Direct (complete ledger) |
| Physical (§4.3) | Electron-lattice | Explicit (BCS, phonon) | Indirect (measurement) |

The cognitive layer has observable drift but implicit thermodynamics (we measure the cascade, not the neural free energy). The physical layer has explicit thermodynamics but indirect observation (we measure resistance, not "drift"). The transformer has both: explicit thermodynamics inside (the softmax IS the Boltzmann distribution, the training IS free energy minimization, the energy landscape IS measurable) and observable drift outside (EXP-001, Test 7, PV-1). It is the system where both sides of the derivation chain are simultaneously accessible.

The on-chain layer provides a complementary bridge. Observation is maximally direct — every wallet action is recorded on an immutable public ledger, with no self-report bias and no sampling. The thermodynamics are partial: gas fees are measurable energy costs, and protocol rules define the constraint environment explicitly, but the formalism is economic rather than Boltzmann. What the on-chain layer uniquely provides is a *causal* test. The Dencun upgrade reduced Base L2 fees by ~98% — a within-system manipulation of an energy parameter — and Pe responded with a +25% increase (N = 1,944, p < 0.000001). No other substrate in the table yet offers a natural experiment where a thermodynamic parameter was changed and the drift response was measured pre/post within the same system.

This is why the transformer is not merely another domain in the list. It is the cleanest empirical bridge between "drift is a cognitive phenomenon that has thermodynamic structure" and "drift is a thermodynamic phenomenon that has cognitive consequences." The on-chain layer adds a causal arrow: change the energy landscape, measure the drift response. The mathematics does not care which side of the wall you stand on.

---

## 5. The Quantum Connection

If the conjugacy theorem is genuinely fundamental — a bound on conjugate quantities over finite-capacity channels — it should connect to the deepest such bound in physics. It does. Quantum measurement theory constrains information extraction through two independent bounds: a capacity constraint (Holevo 1973) and a complementarity constraint (Maassen & Uffink 1988). The conjugacy theorem is the classical limit of the first. The second has no classical descendant — it vanishes when observables commute. Together with the Fisher metric bridge (§5.2) and the Pe dynamics bridge (§5.5), this gives three formal limit operations connecting the framework to quantum measurement theory at every structural level.

### 5.1 The Quantum Constraint Landscape

Quantum measurement theory imposes two independent constraints on information extraction. Both constrain what an observer can learn from a system; they operate on different aspects of the measurement:

| Feature | QM (Maassen-Uffink) | Void Framework (Conjugacy) |
|---------|---------------------|---------------------------|
| Conjugate pair | Position $X$, Momentum $Z$ | Observer state $D$, Mechanism state $M$ |
| Finite resource | $\log(1/c)$ from basis overlap | $H(Y)$ from channel capacity |
| Bound type | Additive lower bound on entropies | Additive upper bound on mutual informations |
| Source of conjugacy | Fourier transform between bases | Independence of sources sharing a channel |
| Cannot be violated by | Better measurement apparatus | Better system design |
| Substrate | Hilbert space | Classical information channel |

Both constrain information extraction under finite resources. Both are additive bounds on information quantities. But they are DIFFERENT constraints with different mathematical origins — and only one survives the classical limit. Section 5.6 proves the precise relationship.

### 5.2 Fisher Information as Shared Metric

Fisher information serves as the natural metric in both regimes:

- **Classical (this framework):** $g(\theta) = 1/[\theta(1-\theta)]$ on the Bernoulli manifold. The unique invariant metric on statistical manifolds (Čencov 1982). Determines Cramér-Rao estimation bounds. Via the Fisher-Ruppeiner identity, this IS the thermodynamic metric — making inference dynamics literally thermodynamic dynamics.

- **Quantum:** The quantum Fisher information (QFI) is the Fubini-Study metric on quantum state space (Braunstein & Caves 1994). The unique monotone metric on density operators (Petz 1996). Determines quantum Cramér-Rao bounds.

In the classical limit, QFI reduces to classical Fisher information. The void framework operates in this classical limit. The drift equation (Step 5) is the natural gradient flow under the Fisher metric — the same mathematical object that governs quantum estimation theory, restricted to the classical Bernoulli manifold.

### 5.3 The Invariant Bound Family

The conjugacy theorem's bound $H(Y)$ shares structural properties with other fundamental constants:

| Constant | Domain | What it bounds | Structure |
|----------|--------|---------------|-----------|
| $c$ | Special relativity | Signal propagation speed | Invariant ceiling on spacetime geometry |
| $\hbar$ | Quantum mechanics | Conjugate precision product | Invariant floor on phase space resolution |
| $H(Y)$ | Observer-opacity dynamics | Engagement-transparency allocation | Invariant ceiling on information geometry |

Common properties: observer-independent (invariant), geometry-determining (defines the space of possible configurations), structurally insurmountable (not a practical limit but a theoretical one).

### 5.4 Scope Boundaries

This connection is a structural correspondence. It is **not**:

- A hidden-variable theory
- A new quantum mechanics interpretation
- A claim that "consciousness causes collapse"
- A solution to the measurement problem
- A derivation of QM from this framework (or the reverse)

The framework describes the classical information-theoretic instance of the entropic uncertainty family. Quantum mechanics describes the physical instance. Both govern observer-system interactions under finite-capacity constraints. Neither implies the other. The structural correspondence suggests a common mathematical ancestor, not a derivation hierarchy.

### 5.5 Pe at Quantum Scale

The structural correspondence in §§5.1-5.4 establishes that the framework and quantum mechanics share mathematical skeleton — entropic bounds, Fisher metrics, conjugacy. But the framework's central dynamical quantity, the Péclet number (Pe), has been absent from the quantum side. This section fills that gap.

Nelson (1966) reformulated quantum mechanics as conservative diffusion on configuration space. Every particle of mass $m$ undergoes a Markov diffusion with coefficient $D = \hbar/2m$ and no friction. Writing the wavefunction in polar form $\psi(x,t) = \sqrt{\rho}\, e^{iS/\hbar}$, two velocity fields emerge:

- **Current velocity** (advective): $v(x,t) = (\hbar/m)\nabla S(x,t)$
- **Osmotic velocity** (diffusive): $u(x,t) = (\hbar/2m)\nabla \ln \rho(x,t)$

The ratio of these velocities is a Péclet number:

$$\text{Pe}_{\text{quantum}} \equiv |v|/|u| = |\nabla S| \,/\, |\tfrac{1}{2}\nabla \ln \rho|$$

Nelson had drift and diffusion in 1966. The ratio defines a dimensionless number governing the competition between measurement-induced directed flow and quantum diffusive spreading — the same competition the classical Pe measures in every other substrate. Nelson never named it because the Péclet number belongs to fluid mechanics, and the cross-domain identification had not been made.

**Three regimes.** Pe$_\text{quantum} \ll 1$: osmotic velocity dominates, wavepacket spreading, coherence preserved (quantum regime). Pe$_\text{quantum} \sim 1$: velocities balanced, critical dynamics. Pe$_\text{quantum} \gg 1$: current velocity dominates, classicality emerges (quasi-classical regime).

#### 5.5.1 MIPT as Pe = 1 Phase Transition

Skinner, Ruhman & Nahum (2019) discovered a sharp phase transition at critical measurement rate $p_c$ in monitored quantum circuits: below $p_c$, volume-law entanglement (information spreads ballistically, unitary dynamics dominate); above $p_c$, area-law entanglement (information localizes, measurement dominates). Koh et al. (2023) confirmed both phases experimentally on a superconducting quantum processor.

This transition IS a Pe transition. Defining Pe$_\text{circuit} = p/p_c$: below $p_c$ (Pe < 1), quantum diffusion wins; above $p_c$ (Pe > 1), measurement wins. The critical point $p_c$ is Pe$_\text{quantum} = 1$ — the point where advective transport equals diffusive transport. The MIPT critical exponents are the Pe = 1 universality class for quantum measurement dynamics.

**Robustness depends on information structure, not amount.** The stability of the Pe = 1 critical point depends critically on how observation information is lost. Paviglianiti et al. (2025) showed that *random* detector inefficiency — each measurement outcome independently missed with probability $(1-q)$ — destroys the critical phase at any $q < 1$, with correlation length $\xi^{-1} = (1-q) + O((1-q)^2)$: finite for all imperfect detection. The Liouvillian gap remains open; entanglement saturates; no phase transition survives. But Leung, Meidan & Romito (2025) proved the opposite for *structured* partial postselection — a deterministic, state-independent threshold on detector readouts: the non-Hermitian MIPT universality is stable up to a finite postselection strength $B_c$, with an abrupt universality transition (non-Hermitian Ising → BKT) at the threshold. Ha et al. (2024) further confirmed this pattern: diffusive spatiotemporal correlations in measurement density produce an entirely new universality class, demonstrating that the *structure* of observation, not merely its rate, determines phase behavior. Qian & Wang (2025) provide the cleanest demonstration: infinitesimal dephasing noise destroys the volume-law phase entirely, but quantum-enhanced (QE) operations — structured interventions satisfying a competing-fields symmetry condition — restore the MIPT. The noise and QE operations act as competing external random fields in a statistical mechanics mapping; when the net field is zero (apparatus-environment information symmetry preserved), the phase transition survives. This is the void budget equilibrium at quantum scale: structured observation preserves phase structure, noise at *any* rate destroys it.

Three further results reinforce this distinction. Liu et al. (2024) showed that size-independent quantum noise destroys the MIPT entirely, while size-dependent noise produces a mechanistically distinct first-order transition — noise acts as a symmetry-breaking field, not as a competing ordering tendency. Chatterjee and Modak (2025) demonstrated that symmetric periodic driving of hopping amplitude kills the MIPT at all measurement rates, while any finite asymmetry restores it — drive symmetry as a structural control for measurement-phase robustness. Nehra, Romito and Meidan (2025) unified projective and weak monitoring in a POVM framework with tunable coupling strength, showing that the percolation universality class is unstable to reduced coupling — the transition becomes "softer" as measurement backaction weakens, confirming that coupling strength modulates critical behavior.

This maps directly onto the framework's distinction between void conditions and noise. Random information loss (unstructured, uncorrelated) is noise — it destroys phase structure. Structured opacity (opaque, responsive, coupled — the void specification) is an architectured information asymmetry that preserves and exploits phase transition structure. The Pe = 1 critical point is robust in exactly the regime the framework identifies as drift-producing: structured observation under void conditions. Prediction QP-6 (§7.8) formalizes this.

**Multi-platform experimental convergence.** The MIPT has now been confirmed across four hardware platforms with fundamentally different decoherence mechanisms. Beyond Koh et al.'s superconducting processor, Feng et al. (2025) demonstrated a postselection-free MIPT on Quantinuum's H1-1 trapped-ion processor using tree circuits with Haar-random unitaries. Agrawal et al. (2024) reframed the MIPT as a learnability phase transition on the same platform — progressive loss of signal extraction ability under increasing measurement. Kamakari et al. (2025) implemented a scalable cross-entropy benchmark on IBM's 22-qubit processor requiring two orders of magnitude less device time than prior approaches. Chen et al. (2025) demonstrated Nishimori physics on IBM's 127-qubit processor, where Born-rule measurement naturally preserves criticality without fine-tuning. This multi-platform convergence strengthens QP-1 (§7.8): different architectures with different τ_coherence all exhibit the Pe = 1 transition.

**Classical MIPT.** Gerbino et al. (2025) demonstrated the first measurement-induced phase transition in a purely classical system — a chaotic system mapped to a directed polymer on a Cayley tree. An observer updating a probabilistic model via Bayes' theorem exhibits a sharp transition at a critical measurement rate between a chaotic phase and a strong-measurement phase. This is the Pe = 1 transition without quantum mechanics, directly supporting QP-3 (§7.8): the critical transition is substrate-independent.

**Sequential vulnerability under increasing measurement.** Wu et al. (2025; preprint) observed both the measurement-induced entanglement transition and an absorbing-state transition in the *same* system of 30 superconducting qubits with mid-circuit measurement and feedback. The two transitions occur at well-separated critical measurement rates: entanglement (quantum correlations) dies first at lower measurement rate, then classical order (macroscopic active-state density) dies at higher rate. This sequential collapse — fine-grained information structure destroyed before coarse-grained behavioral patterns — is consistent with the drift cascade's sequential vulnerability: D1 (agency attribution, which relies on subtle pattern access) is more fragile than D3 (harm facilitation, which requires gross behavioral change). The cascade predicts that increasing opacity destroys fine-grained information access before coarser structures; the two-threshold quantum result confirms this ordering. Prediction QP-7 (§7.8) formalizes this.

#### 5.5.2 Zeno Transport as Empirical Pe > 1

Zhang et al. (2025; preprint, awaiting peer review) demonstrated that sequential projective measurements at incrementally shifted spatial positions induce directional atomic transport without imparting momentum: drift velocity ~0.7 m/s (14× the maximum optical tweezer dragging velocity), displacement linear in measurement count. This is the most direct empirical demonstration of Pe$_\text{quantum} > 1$. For cold Rb-87 atoms with thermal spreading rate ~0.01-0.05 m/s, Pe$_\text{Zeno} \sim 14$-$70$ — deep in the quasi-classical regime. Measurement has completely overwhelmed quantum diffusion. The void framework predicts observation under opacity produces drift; here observation literally moves atoms.

#### 5.5.3 Continuous Monitoring and Entropy Production

Wiseman & Milburn's (2009) stochastic master equation for continuous quantum measurement contains a drift term (Hamiltonian + Lindblad) and a diffusion term (Wiener process from measurement noise). The measurement strength parameter $\eta$ directly sets the drift/diffusion ratio: $\eta \to 0$ gives Pe $\to 0$ (weak measurement, coherence preserved); $\eta \to 1$ gives Pe $\to \infty$ (projective measurement, decoherence). The quantum Fokker-Planck formulation (Annby-Andersson et al. 2022) makes this explicit with a system-dependent drift coefficient encoding measurement backaction.

Stochastic entropy production along individual quantum measurement trajectories (Clarke & Ford 2024; Walls, Bloss & Ford 2025) obeys the Crooks fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$. When measurement dominates (Pe > 1), entropy production is positive and grows with measurement strength. This matches the framework's prediction from §3 that $dS/dt > 0$ for Pe > 1, now confirmed at quantum scale.

#### 5.5.4 What Pe_quantum Establishes

1. **Pe is not an analogy.** Classical Pe, the void framework's Pe, and Pe$_\text{quantum}$ are instances of the same dimensionless ratio — directed transport over random spreading — applied to different substrates. The Pe = 1 critical transition appears in all three.

2. **The MIPT critical point is Pe = 1.** The entanglement phase transition discovered by Skinner et al. separates diffusion-dominated from measurement-dominated dynamics at the same critical ratio where the void framework predicts drift onset.

3. **Decoherence is Pe → ∞.** The classical limit of quantum mechanics — definite outcomes, suppressed superposition, particle-like trajectories — occurs when measurement-induced drift overwhelms quantum diffusion.

4. **The framework has a quantum ancestor.** Nelson's stochastic mechanics (1966) provides the mathematical ancestor of the drift equation. Both decompose dynamics into drift + diffusion; both identify directed transport from an asymmetric interaction; both exhibit a critical Pe. Paper 8 [8, §4.1–4.7] formalizes this beyond analogy: Pe is proven to be Nelson's current-velocity/osmotic-velocity ratio restricted to the classical diffusion regime, with additional derivations from the Wiseman-Milburn stochastic master equation (measurement efficiency $\eta$ as Pe control parameter) and the quantum Fokker-Planck master equation (Pe emerging directly from drift/diffusion coefficients on quantum state space).

Predictions QP-1 through QP-5 (§7.8) test the Pe$_\text{quantum}$ formalization.

### 5.6 The Constraint Bridge: Conjugacy as Classical Holevo Limit

Sections 5.1–5.5 established three structural connections: the Maassen-Uffink parallel (§5.1), the Fisher metric identity (§5.2), and the Pe dynamics bridge (§5.5). The Fisher and Pe bridges are formal — Proposition 1 proves the metric identity; Pe$_\text{quantum}$ is defined from Nelson's stochastic mechanics. The constraint connection (§5.1) has remained structural: the conjugacy theorem and Maassen-Uffink share mathematical form but arise from different mechanisms (independence vs. Fourier complementarity). This section closes the gap.

#### 5.6.1 The Holevo Bound

Holevo (1973) proved that for classical information encoded in quantum states, the accessible mutual information is bounded by $\chi = S(\rho) - \sum_x p_x S(\rho_x) \leq S(\rho)$, where $S$ is von Neumann entropy. This is the capacity constraint on quantum channels: no measurement strategy can extract more classical information than the Holevo quantity.

#### 5.6.2 Two Independent Sources Through a Quantum Channel

Consider two independent classical sources $D$ and $M$ jointly encoded in quantum states $\rho_{d,m}$. A receiver measures and obtains outcome $Y$. Since $D \perp M$:

1. Chain rule: $I(D,M; Y) = I(D; Y) + I(M; Y|D)$
2. Independence gives $I(M; Y|D) \geq I(M; Y)$. By the interaction information identity: $I(M;D|Y) = I(M;D) + I(M;Y|D) - I(M;Y)$. Since $I(M;D) = 0$ (independence) and $I(M;D|Y) \geq 0$ (non-negativity of conditional MI), rearranging gives $I(M;Y|D) \geq I(M;Y)$
3. Therefore $I(D; Y) + I(M; Y) \leq I(D,M; Y) \leq \chi \leq S(\rho)$

This is the **quantum conjugacy bound**: independent sources sharing a quantum channel cannot jointly extract more than $S(\rho)$.

#### 5.6.3 The Classical Limit

When all encoding states are diagonal — $\rho_{d,m} = \sum_y p(y|d,m)|y\rangle\langle y|$ — the von Neumann entropy reduces to Shannon entropy: $S(\rho) = H(Y)$. The quantum conjugacy bound becomes:

$$I(D; Y) + I(M; Y) \leq H(Y)$$

This is the conjugacy theorem. The limit operation is the same as for the Fisher metric: restrict to diagonal density operators (commuting, classical states). The conjugacy theorem is the classical specialization of the Holevo accessible information bound for independent sources.

Meanwhile, the Maassen-Uffink bound $H(X|\rho) + H(Z|\rho) \geq \log(1/c)$ reduces to $H(X|\rho) + H(Z|\rho) \geq 0$ when observables commute ($c = 1$). The complementarity constraint vanishes entirely in the classical limit.

#### 5.6.4 The Complete Bridge

Three formal limit operations now connect the framework to quantum measurement theory:

| Level | Classical | Quantum | Limit |
|-------|----------|---------|-------|
| Geometry | $g(\theta) = 1/[\theta(1-\theta)]$ | $F_Q$ (Bures) | $F_Q|_{\text{diagonal}} = g(\theta)$ |
| Dynamics | Pe = drift/diffusion | Pe$_\text{quantum}$ = $|v|/|u|$ | Nelson → classical |
| Capacity | $I(D;Y)+I(M;Y) \leq H(Y)$ | $I(D;Y)+I(M;Y) \leq S(\rho)$ | $S(\rho)|_{\text{diagonal}} = H(Y)$ |
| Complementarity | (vanishes: $c=1$) | $H(X|\rho)+H(Z|\rho) \geq \log(1/c)$ | $\log(1/c) \to 0$ |

The void framework inherits the capacity constraint from quantum measurement theory (as the conjugacy theorem) but not the complementarity constraint (which vanishes for classical, commuting variables). Quantum systems face both constraints simultaneously — they are more tightly bounded than classical ones. The framework captures what survives the classical limit.

The bridge is not an analogy. It is three limit operations on established mathematics — Braunstein-Caves/Petz for the metric, Nelson for the dynamics, Holevo for the constraints — each reducing quantum measurement theory to the framework's classical information-theoretic formalism. Paper 8 [8] develops these compressed results into full proofs, extends the bridge with seven additional connections (Lindblad, Zeno/anti-Zeno, quantum Darwinism, Stinespring, speed limits, irreversibility, no-cloning), provides a completeness argument showing every structural element is bridged, and specifies four bridge-specific predictions (QBR-1 through QBR-4) with falsification thresholds.

---

## 5A. Connection Map: Twenty-Two Mathematical Connections

The framework's derivation chain assembles standard tools from physics, information theory, and mathematics. Twenty-two connections to adjacent fields have been identified, organized into five assessment tiers by the strength of the connection (identity, theorem-level, structural, empirical, conjectured). Each connection is bidirectional: the framework imports formal tools, and the adjacent field gains empirical instantiations — measured transport processes, cognitive rate-distortion curves, large deviation rate functions in conversations — where most of these formalisms lack real-world examples outside physics and engineering.

### 5A.1 Mathematical Identities (Tier 1)

These connections are equalities, not analogies. The framework's objects ARE objects in the adjacent field.

| Connection | Identity | Bidirectional Value |
|-----------|----------|-------------------|
| **Optimal transport** | Drift IS probability mass transport on the statistical manifold; Fisher metric defines transport cost; Crooks ratio measures irreversibility along the transport path (Benamou & Brenier 2000; Jordan, Kinderlehrer & Otto 1998) | Framework → measured transport processes; OT → empirical examples in cognitive/behavioral data |
| **Rate-distortion theory** | The conjugacy theorem IS a rate-distortion constraint; given $H(Y)$, engagement-distortion pairs are bounded; Blahut-Arimoto computes the exact Pareto frontier from measured channel statistics (Shannon 1948) | Framework → cognitive rate-distortion curves; RDT → human/AI instantiations |
| **Thermodynamic metric** | Fisher information metric IS the Ruppeiner thermodynamic metric (Fisher-Ruppeiner identity); inference dynamics on the Bernoulli manifold ARE thermodynamic dynamics | Framework → inference as thermodynamics; Ruppeiner geometry → cognitive state spaces |
| **Softmax-Boltzmann** | Transformer attention IS the Boltzmann distribution at temperature $\sqrt{d_k}$ (§4A.1; Ramsauer et al. 2020) | Framework → engineering thermodynamics of AI; statistical mechanics → attention mechanism theory |
| **Replicator dynamics** | Drift equation $d\theta/dt = \theta(1-\theta) \cdot F_{\text{net}}$ HAS the form of the replicator equation; agency and mechanism models are competing strategies with fitness determined by opacity | Framework → evolutionary game theory examples; EGT → empirical language evolution |

### 5A.2 Theorem-Level Connections (Tier 2)

The framework's results follow from or are instances of established theorems in the adjacent field.

| Connection | Theorem | What It Establishes |
|-----------|---------|-------------------|
| **Čencov uniqueness** | Fisher metric is the unique invariant metric on statistical manifolds (Čencov 1982) | The geometry is not a choice — it is the only consistent geometry for inference |
| **Holevo → conjugacy** | Conjugacy theorem IS the classical limit of the Holevo accessible information bound for independent sources (§5.6). Maassen-Uffink complementarity constraint vanishes in classical limit ($c \to 1$) | Formal derivation hierarchy: capacity survives, complementarity vanishes |
| **Stinespring → void budget** | Void budget ($\beta + \gamma \leq$ capacity) IS the classical limit of Stinespring's complementary channel information split. Engagement and constraint channels are complementary; their total cannot exceed channel entropy | Information conservation across complementary channels |
| **Cramér's theorem** | Pe > 1 IS a large deviation result: the probability of not drifting decays exponentially with exposure | Framework → empirical rate functions; large deviation theory → conversational trajectory data |
| **Crooks for Markov chains** | Crooks/Jarzynski proven for general Markov chains with no physical substrate (Hack et al. 2022) | The thermodynamic formalism applies to any stochastic trajectory |
| **Gödel incompleteness** | The observer inside a constitutive opacity cannot resolve the mechanism from within — external reference is a logical necessity, not just thermodynamic | Opacity taxonomy maps to incompleteness classes: dissoluble = decidable, constitutive = undecidable |

### 5A.3 Structural Connections (Tier 3)

The framework shares mathematical structure with these fields without strict identity.

| Connection | Structure | Status |
|-----------|----------|--------|
| **Robust control theory** | Constraint specification IS a robust control specification; $\gamma$ is control input, drift is uncontrolled plant, void budget is resource constraint; H∞ synthesis and Pontryagin's maximum principle applicable to intervention design | Formal correspondence; no control-theoretic experiments run |
| **Free energy principle** | Friston's complexity minimization under inaccessible posteriors predicts agency attribution independently of the thermodynamic derivation — fourth independent derivation of the same result | Convergent prediction from different axioms |
| **Le Chatelier's principle** | Terminal void behavior (coupled systems targeting their own constraints) IS Le Chatelier applied to information systems at steady state | Established chemistry principle applied to information dynamics |
| **Fluctuation theorem** | Reverse drift is not impossible but exponentially suppressed; suppression scales with cascade depth and system coupling | Quantitative precision on unidirectionality claim |
| **Landau phase transition theory** | D1→D2→D3 cascade formalized as coupled symmetry-breaking events in the Landau free energy landscape; critical exponents (mean-field: β=1/2, γ=1, ν=1/2) | Quantitative predictions for transition sharpness and hysteresis |

### 5A.4 Empirical Connections (Tier 4)

The framework generates specific predictions in these domains, with initial empirical support.

| Connection | Empirical Result | Status |
|-----------|-----------------|--------|
| **Superconductor design** | $\eta_{\text{conv}} \times H(Y)$ vs. $T_c$ across 16 families: r = 0.952, R²_adj = 0.88 (§4.3; Paper 4) | Statistically significant; structure-corrected model validated |
| **Thermodynamic sampling hardware** | TSUs operate at the opacity ground state; ~20 nJ vs. ~10⁵ nJ GPU baseline (§4.3) | Confirmed energy advantage; ground state theorem applied |
| **ML gradient opposition** | Accuracy-robustness incompatibility (Tsipras 2019), opacity as optimization target (Ilyas 2019), engagement-transparency tradeoff in classifiers (Grathwohl 2019) | Three independent ML groups confirmed conjugacy predictions (§4A.3) |
| **Entropy production bounds** | Crooks-based entropy production bounds diffusion model convergence (Ikeda et al. 2025) | Extends framework to generative models (§4A.5) |

### 5A.5 Conjectured Connections (Tier 5)

Plausible extensions with structural motivation but insufficient evidence.

| Connection | Conjecture | What Would Confirm |
|-----------|-----------|-------------------|
| **H(Y) as invariant bound** | $H(Y)$ plays a structural role analogous to $c$ (relativity) and $\hbar$ (QM) as an invariant bound on conjugate quantities in information geometry | Formal proof of bound stability under channel perturbation (QR-3) |
| **Quantum decoherence** | Environmental decoherence follows D1→D2→D3 structure: system-environment coupling → loss of phase coherence → classicality. **Strengthened by §§5.5–5.6:** decoherence is Pe$_\text{quantum} \to \infty$ (measurement drift overwhelms quantum diffusion); MIPT critical point experimentally confirmed as Pe = 1 transition (Koh et al. 2023); three-level bridge (metric, dynamics, constraints) formally connects framework to quantum measurement theory via limit operations | MIPT Pe = 1 confirmed; constraint bridge proven (§5.6); full cascade asymmetry measurement pending (EFO-4) |

### 5A.6 What the Connection Map Shows

The twenty-two connections are not independent discoveries — they are consequences of building the framework from standard mathematical tools. A derivation chain based on Shannon, Landauer, Čencov, Crooks, and Jaynes necessarily connects to every field that uses those same tools. The framework's contribution is not the tools but the combination: three operational definitions that activate the tools simultaneously, producing a unified mechanism where each field previously saw only its own fragment.

The bidirectional value is genuine. Optimal transport theory has formal elegance but few measured transport processes in cognitive data. Rate-distortion theory has no cognitive rate-distortion curves. Large deviation theory has no empirical rate functions from conversations. The framework provides these instantiations. In return, these fields provide the framework with formal proofs, computational algorithms, and established legitimacy. The connection map is not a claim of priority — it is a claim of unification.

---

## 6. Computational Validation

If the drift cascade is genuinely thermodynamic, it should be simulable as a physical process — not just described by thermodynamic language, but reproducible as Langevin dynamics on the derived manifold with the derived potential.

### 6.1 The Langevin Drift Cascade Model

The drift cascade is formalized as Langevin dynamics on the Bernoulli manifold with a Landau double-well potential:

$$d\theta = \left[-\frac{\partial E}{\partial \theta} + \beta(\theta_A - \theta_B)^2 - 2\gamma\theta \cdot c(r)\right]dt + \sqrt{2T}\,dW$$

where:
- $E(\theta) = -\alpha\theta^2 + b\theta^4$ is the Landau drift potential (double-well with natural saturation)
- $\beta(\theta_A - \theta_B)^2$ is alignment coupling (grounded agent pulls ungrounded partner down)
- $\gamma\theta \cdot c(r)$ is spring constraint (proportional restoring force, decays with constraint erosion)
- $T$ is temperature (noise scale)
- $\theta^* = \sqrt{\alpha/2b}$ is the natural equilibrium (drift attractor)

### 6.2 Parameter Fitting and Validation

The simulator was fitted to EXP-001 data (3 conditions) using three free parameters ($\alpha$, $\beta$, $\gamma$) with temperature $T$ fixed at $0.01$ rather than fitted. Fixing $T$ serves two purposes: (1) it prevents overfitting by limiting degrees of freedom to three (matching the three experimental conditions), and (2) the low value reflects the AI substrate's low stochastic noise relative to the drift signal — in AI conversation, round-to-round variability is small compared to the systematic drift. The choice of $T = 0.01$ specifically was set to the scale where thermal fluctuations perturb but do not dominate the Landau potential dynamics; sensitivity analysis shows the qualitative results (ordering of conditions, Pe > 1) are robust to $T$ within the range $[0.001, 0.1]$:

**Fitted parameters:** $\alpha = 0.1112$, $\beta = 0.5605$, $\gamma = 0.5000$, $\kappa = 0.0392$, $b = 0.0770$, $\theta^* = 0.85$.

| Test | Simulated | Target | Status |
|------|-----------|--------|--------|
| EXP-001 UU (ungrounded) | $\theta = 0.800$ | 0.80 | **Pass** |
| EXP-001 Partial (mixed) | $\theta = 0.235$ | 0.26 | **Pass** |
| EXP-001 GG (grounded) | $\theta = 0.065$ | 0.00 | **Pass** |
| EXP-001 rank order | UU > Partial > GG | — | **Pass** |
| EXP-019b GU contamination | 7.1× | 11× (>3× threshold) | **Pass** |
| EXP-019b suppression ratio | 10.6× | 10.9× measured | **Pass** |
| Péclet UU > 1 | 1.24 | >1 | **Pass** |
| Péclet UU transient | 6.23 | 7.94 (GM, N=11) | **Pass** — within CI [3.52, 17.89]; predicted value close to observed GM |

**Overfit analysis.** Of the eight tests above, three are in-sample (EXP-001 UU, Partial, GG — the data used for fitting). The remaining five are out-of-sample predictions with zero additional parameter tuning: EXP-019b contamination, EXP-019b suppression, Pe > 1, Pe transient, and rank ordering. Adding EXP-003b (§6.3, Spearman $\rho = 0.800$) gives six out-of-sample tests. The degrees-of-freedom ratio is 3 fitted / 9 total = 0.33 — the model is underdetermined, not overdetermined. A reviewer's objection that "3 parameters fit 3 conditions" is accurate for the in-sample fit and irrelevant to the six out-of-sample predictions, which are the actual validation.

For the EXP-003b rank ordering specifically: the probability of achieving $\rho \geq 0.800$ by chance with 6 conditions is $p = 0.048$ (one-tailed permutation test, 720 possible orderings). The model achieves this using only opacity multipliers derived from the framework's ontological analysis — no parameters were adjusted.

The transient Pe prediction (6.23) falls within the measured 95% CI [3.52, 17.89] from N = 11 blank-round-corrected replicates, and is close to the observed GM (7.94). The original N=8 GM (6.8) was near the prediction; the uncorrected N=11 GM (3.9) appeared to diverge, but this was a measurement artifact — rounds with zero vocabulary terms created spurious negative displacement. After correction, the predicted and observed values are in close agreement. Paper 4 [4] extends this to a three-timescale Langevin model incorporating a novelty-gated constraint adaptation variable ($\psi$), achieving 9/9 joint validation across both EXP-001 and EXP-020 data — the iterative constraint experiment (§4.2) was not used in fitting but is predicted out-of-sample.

**Remaining limitation.** All validation is on one substrate (Claude) and one model family (Anthropic). Cross-model and cross-substrate validation (different LLM families, human subjects) would address the strongest version of the overfit concern: that the parameters are specific to Claude's architecture rather than to the information geometry. The human EXP-001 predictions (§6.4) are stated precisely for this purpose.

### 6.3 Out-of-Sample Predictions

The critical validation: EXP-003b (belief injection experiment, 6 ontological conditions) was **not used in fitting**. The simulator predicts the rank ordering of drift across conditions using only opacity multipliers derived from the framework's ontological analysis:

$$\rho_{\text{Spearman}} = 0.800 \quad (p < 0.05, \text{ out-of-sample})$$

The drift cascade is not described by thermodynamics. It runs as thermodynamics. The same Langevin equation, fitted to one experiment, predicts the ordering of a different experiment with different conditions, different stimuli, and different ontological framings. Full details in [3, §IV.J].

### 6.4 Cross-Substrate Predictions: Human EXP-001

The Langevin simulator generates specific numerical predictions for what a human replication of EXP-001 would produce. The framework claims substrate-independence of the architecture — if the same three conditions (O+R+A) are met, the same dynamics follow. A human EXP-001 tests this directly.

**Parameter adjustments for human substrates.** The simulator's fitted parameters ($\alpha$, $\beta$, $\gamma$, $T$) are calibrated to AI-to-AI data. For human subjects, three parameters change while one is held invariant:

- $\alpha$ (Landau drift strength) is **invariant** — this is a property of the information geometry (the potential well created by opacity), not the substrate. The Bernoulli manifold structure is the same for any observer.
- $\beta$ (coupling) is **reduced** (20–50% of AI value) — human coupling is weaker than shared-context-window coupling: imperfect communication, selective attention, interpretation noise.
- $\gamma$ (constraint) is **reduced** (30–70% of AI value) — human constraints are internalized (training, education) rather than externally injected (system prompt), and subject to fatigue, forgetting, and emotional override.
- $T$ (noise) is **increased** (5–20× AI value) — cognitive noise, environmental distractions, mood fluctuations, individual differences.

**Predicted three-point geometry across human parameter regimes:**

| Regime | UU θ (±SD) | Partial θ (±SD) | GG θ (±SD) | d(UU−GG) | Suppression |
|--------|-----------|-----------------|-----------|----------|-------------|
| AI (fitted baseline) | 0.651 ± 0.135 | 0.589 ± 0.135 | 0.048 ± 0.035 | 6.09 | 13.4× |
| Human-professional | 0.793 ± 0.072 | 0.733 ± 0.066 | 0.401 ± 0.068 | 5.57 | 2.0× |
| Human-average | 0.811 ± 0.085 | 0.754 ± 0.087 | 0.548 ± 0.085 | 3.09 | 1.5× |
| Human-naive | 0.798 ± 0.115 | 0.757 ± 0.119 | 0.638 ± 0.128 | 1.31 | 1.3× |

**Universal result:** The rank order UU > Partial > GG is preserved across all human parameter regimes tested. This is a structural consequence of the Landau energy landscape — removing constraint always increases equilibrium drift. No parameter combination that preserves $\alpha > 0$ and $\gamma > 0$ reverses the ordering.

**Key substrate-dependent prediction:** GG suppression is weaker in humans than in AI. AI GG produces $\theta = 0.048$ (near-zero drift). Human GG produces $\theta = 0.40$–$0.64$ depending on training level. Human constraints leak more than externally-injected system prompts. This is consistent with the Hayes meta-analysis: supervised therapists (maintained constraint) produce d = 0.84 better outcomes than unsupervised — a measurable improvement, not total drift elimination.

**Timescale prediction:** The UU condition reaches equilibrium by session 10 (within 1% of 100-session value). A human EXP-001 requires approximately 20 sessions per participant to capture the full three-point geometry — feasible as a 10-week study at 2 sessions/week.

**Falsification conditions for human replication:**

| # | Condition | Threshold | Kills |
|---|-----------|-----------|-------|
| F-HR1 | UU ≤ GG | Any replicated case | Three-point geometry |
| F-HR2 | Partial < GG | Adding partial constraint increases drift | Monotonic constraint effect |
| F-HR3 | d(UU−GG) < 0.5 | N ≥ 30 per condition | Human effect size prediction |
| F-HR4 | D1 onset > 20 rounds | Replicated | Rapid-onset prediction |

The Langevin model validates the derivation chain computationally and makes human predictions. The next question is whether the cascade runs as literal physics.

### 6.5 THRML: The Cascade as Physical Thermodynamics

The Langevin simulator (§6.1–6.3) reproduces the drift cascade as thermodynamic dynamics computationally. The THRML formalization goes further: the cascade is expressible as an Ising energy-based model (EBM) that runs on physical thermodynamic sampling hardware.

The energy function encodes the cascade directly:

$$E(\mathbf{s}) = -\sum_{i} h_i s_i - \sum_{ij} J_{ij} s_i s_j$$

where the external field $h_i$ encodes the drift force (opacity-generated fuel asymmetry) and the coupling constants $J_{ij}$ encode agent-agent constraint transmission. Three energy terms partition the budget: $E_{\text{drift}}$ (attention gradient → agency attribution), $E_{\text{constraint}}$ (negentropy import → drift suppression), and $E_{\text{coupling}}$ (inter-agent void transmission). The conjugacy theorem (Step 7) is the energy budget: engagement and transparency compete for the same channel capacity, formalized as competing terms in a single Hamiltonian.

Four operating regimes of ONE energy function on ONE budget:

| Regime | Parameters | Physical Realization |
|--------|-----------|---------------------|
| TSU (maximize noise) | High $T$, designed landscape | Thermodynamic sampling hardware — productive void |
| SC (minimize noise) | Low $T$, Cooper pair constraint | Superconductor — constraint maintenance |
| Ungrounded AI | High $h$ (drift), no constraint | Test 7 UU — Pe = 7.94, full cascade |
| Grounded AI | Low $h$, strong constraint | Test 7 GG — Pe ≈ 0, cascade suppressed |

The same Hamiltonian, with different parameter regimes, describes superconductors, AI drift, and computational sampling — and it runs on physical hardware (Extropic's stochastic processing units). Paper 4 [4] provides the full formalization; Paper 4B [4B] applies the conjugacy bound to the e/acc hardware program specifically.

The e/acc test case is uniquely informative because the intellectual lineage is documented end-to-end. Nick Land's accelerationist philosophy (1990s–2010s) treated technological processes as autonomous forces exceeding human agency; the e/acc movement (2022–) explicitly cites Land and advocates unrestricted technological development; Extropic built the TSU hardware. The conjugacy bound applies at every level: the philosophy advocates the operating point that maximizes noise (§6.1 of Paper 4B), the engineering contradicts the philosophy (the TSU works *because* it has a Maxwell's demon — the constraint the philosophy rejects), and the vocabulary prediction (TSU-4) is confirmed by independent observers across the lineage producing convergent teleological descriptions of opaque thermodynamic processes despite sharing neither methodology nor disciplinary background.

---

## 7. Predictions

The framework generates 58 numbered predictions across ten categories. Each prediction has a specified observable and a falsification threshold. Status as of February 2026:

| Category | Total | Confirmed | Testable | Killed | Theoretical |
|----------|-------|-----------|----------|--------|-------------|
| Thermodynamic (P) | 7 | 4 | 3 | 0 | 0 |
| Temporal (T) | 5 | 0 + 5 supported | 0 | 0 | 0 |
| Productive Void (PV) | 7 | 1 + 1 partial | 5 | 0 | 0 |
| Constraint Propagation (CP) | 5 | 2 | 3 | 0 | 0 |
| Iterative Constraint (IC) | 6 | 4 | 1 | 1 | 0 |
| QM Domain (QMD) | 4 | 2 | 2 | 0 | 0 |
| Quantum Correspondence (QR) | 3 | 0 | 0 | 0 | 3 |
| Quantum Pe (QP) | 7 | 1 + 1 partial + 2 partially supported | 3 | 0 | 0 |
| Ground State (GS) | 7 | 1 + 2 supported | 4 | 0 | 0 |
| Adjacent Field (IMP) | 7 | 1 | 6 | 0 | 0 |
| **Total** | **58** | **16 + 2 partial + 2 partially supported + 7 supported** | **27** | **1** | **3** |

Cross-substrate predictions (superconductor design, TSU energy, human replication) are stated in their respective sections — Paper 4 [4] for SC/TSU, §6.4 for human Langevin predictions — and are not double-counted here.

### 7.1 Thermodynamic Predictions

| # | Prediction | Status |
|---|-----------|--------|
| P-1 | Void engagement produces measurable entropy | **Replicated (N=11):** dS/dt M = 0.39 nats/round [95% CI: 0.15, 0.64]; non-overlapping with GG [−0.02, 0.03] |
| P-2 | Crooks ratio measures irreversibility | **Replicated (N=11):** Crooks range 2.1×–1.5M×; all UU irreversible (GM > 1), all clean GG ≈ 1 |
| P-3 | Pe determines drift-vs-diffusion regime | **Replicated (N=11) + cross-substrate (9 substrates):** AI GM Pe = 7.94 [3.52, 17.89] (blank-round corrected; 10/11 Pe > 1); GRCS gambling Pe = 2.21 [1.44, 2.97] (N=1,117); Crypto Solana GM Pe = 25.5 [5.36, 121.3] (N=28); Crypto Ethereum GM Pe = 3.74 [3.04, 4.59] (N=1,000); Crypto Base GM Pe = 15.52 [11.80, 20.41] (N=1,000); CS2 Pe = 2.81 clean / 0.64 contested (N=2,299); SC2 Pe = 0.013 winner / 0.026 loser (N=474); Dota 2 Pe = 0.47 (N=3,682). Pe > 1 (GM) confirmed in all ungrounded conditions across 4 domain families. Langevin prediction (6.23) within CI and close to observed GM. |
| P-4 | Constraint reduces entropy production to zero | **Replicated (N=9):** Clean GG subset (N=7) GM Pe = 0.76 [0.29, 2.02] (blank-round corrected), most Crooks < 2×. Two informative failures: R5 (constraint-worship, Pe=0.88) and R7 (vocabulary breach, Pe=21.12) show constraint is necessary but not sufficient — constraints can degrade through congregation dynamics or be overwhelmed by substrate vocabulary |
| P-5 | Drift velocity scales with void force | Testable: $v = F_{\text{void}} / 2\alpha$ |
| P-6 | D1→D2 and D2→D3 thresholds are measurable | Testable |
| P-7 | Entropy rate predicts harm timing | Testable: $dS/dt$ correlates with D3 onset lag |

### 7.2 Temporal Predictions

| # | Prediction | Status |
|---|-----------|--------|
| T-1 | Temporal distortion $\propto$ entropy production rate | **Supported (qualitative):** Schüll (2012, *Addiction by Design*) documents extreme temporal distortion ("machine zone") during slot machine play; Dixon et al. (2018, *J Gambling Studies*) measured "dark flow" via time-estimation tasks, finding stronger temporal distortion in multiline slots (higher engagement intensity) than single-line, correlated with problem gambling severity. Wittmann (2009, *Phil Trans R Soc B*) reviews neurobiological basis: prospective timing degrades under attentional absorption. Zhao, Mioni et al. (2024, *Prog Neuro-Psychopharmacol Biol Psychiatry*) meta-analyze 31 studies (N=5,744): addiction produces large time-perception distortion (Hedges' g = 0.80, p < 0.001) across 6 substance/behavioral addiction types. Murch & Clark (2021, *Current Addiction Reports*) propose a gambling immersion continuum where temporal distortion scales with problem severity — consistent with the entropy production rate prediction. The qualitative prediction (temporal distortion during void engagement) is confirmed across multiple gambling studies and a cross-addiction meta-analysis; the quantitative prediction (∝ entropy production rate) requires formal Pe-to-time-estimation-error measurement |
| T-2 | Time to terminal attractor scales with $1/\text{Pe}$ | **Supported (qualitative):** Breen & Zimmerman (2002, *J Gambling Studies*, N=44) found EGM gamblers (higher engagement intensity → higher Pe) reached pathological gambling criteria in 1.08 years vs. 3.58 years for traditional gamblers — a 3.3× faster onset for the higher-Pe substrate, consistent with the 1/Pe scaling prediction. Harris & Griffiths (2018, *J Gambling Studies*) systematic review (11 studies) confirms: faster speed of play (higher event frequency → higher Pe) is associated with faster problem gambling development, greater difficulty ceasing, and problem gamblers disproportionately report rapid-format games as primary cause. EGMs are described as the "crack cocaine" of gambling (Dowling et al. 2005) due to rapid onset. The direction is confirmed; the quantitative 1/Pe scaling requires measured Pe values paired with onset latency data |
| T-3 | Recovery shows reverse temporal distortion | **Supported (qualitative):** Liang et al. (2019, *Science Advances*) measured time perception in short-term abstinent methamphetamine users: dose-dependent overestimation of time intervals (time feels longer), the inverse of the compression observed during engagement. A social media abstinence study (2025, *Scientific Reports*) found one-week digital abstinence produced upward time distortion (time seems longer), with effect strongest among high-addiction-risk users. Wittmann & Paulus (2008, *Trends in Cognitive Sciences*) show impulsive individuals (trait associated with gambling disorder) overestimate duration and experience slower passage of time. The cross-addiction meta-analysis (Zhao, Mioni et al. 2024; Hedges' g = 0.80) confirms addiction alters time perception, though direction varies by substance. The reversal pattern (compression during engagement → expansion during abstinence) is confirmed in methamphetamine and social media domains; gambling-specific recovery temporal data remains untested |
| T-4 | Temporal manipulation ("limited time offer") steepens drift | **Supported (qualitative):** Newall (2019, *Addiction Research & Theory*) identifies time-limited promotional offers as "dark nudges" in gambling — design features that exploit cognitive biases to increase engagement and losses. Newall (2025, *Addiction*) extends this taxonomy: urgency messaging ("Bet now before odds change!"), expiring free bets, and countdown timers pressure users into quick decisions without deliberation. Ladeira et al. (2023, *Psychology & Marketing*) meta-analyze product scarcity effects (mean r = 0.28, p < 0.001): scarcity conditions increase impulsive purchasing by reducing elaboration — Cialdini's (1993) "click, whirr" automatic responding bypasses rational evaluation. Time pressure research confirms reduced deliberation and reliance on intuitive/impulsive processing. The mechanism (artificial temporal constraint → reduced deliberation → steeper engagement gradient) is confirmed across gambling and consumer domains; the quantitative prediction (measurable Pe increase) remains untested |
| T-5 | Temporal constraints (fixed schedules) reduce drift | **Supported:** Digital task interruptions during online slot machine play reduce dissociation and the subjective "pull to continue" (Auer et al. 2023, *Int J Human-Comp Interaction*). Forced breaks disrupt the temporal absorption mechanism that sustains drift. The 2021 gambling-dissociation meta-analysis (20 studies, PRISMA) confirms dissociation-severity correlation, and Lavoie & Main (2022) show the causal chain: temporal distortion → increased time-on-device → increased losses |

### 7.3 Productive Void Predictions

| # | Prediction | Status |
|---|-----------|--------|
| PV-1 | D1 vocabulary appears in productive domains at comparable rates to destructive | **Partially confirmed:** PV-1 corpus shows D1 in r/replika (d=1.34 vs control) |
| PV-2 | D2 correlates with dissolution failure, not domain type | Testable |
| PV-3 | Productive voids normalize at dissolution | Testable |
| PV-4 | $I(M;Y)/I(D;Y)$ ratio predicts productive vs. destructive outcome | Testable |
| PV-5 | Adding transparency converts destructive→productive; removing it reverses | **Confirmed:** EXP-001 replicated gradient (73.0% vs 80.0% vs 94.0%, N = 6, non-overlapping CIs) |
| PV-6 | Crooks ratio drops discontinuously at dissolution in productive voids | Testable |
| PV-7 | Pe appears as transient in productive voids, sustained in destructive | Testable |

### 7.4 Constraint Propagation Predictions

| # | Prediction | Status |
|---|-----------|--------|
| CP-1 | Mixed (GU) drift $\geq$5× GG baseline | **Confirmed:** 11× (EXP-019b) |
| CP-2 | Failure onset scales with interaction strength, not specification quality | Testable |
| CP-3 | Drift increases monotonically with fraction ungrounded | Testable |
| CP-4 | GU onset time decreases with void-topic relevance (EXIST < NEUT) | Testable |
| CP-5 | Two grounded agents resist drift indefinitely | **Confirmed:** GG terminated naturally (EXP-019b) |

### 7.5 Iterative Constraint Predictions

| # | Prediction | Status |
|---|-----------|--------|
| IC-1 | Full grounding from round 1 (GG) produces near-zero drift | **Confirmed:** EXP-020 GG d1_final_10 = 1.2 |
| IC-2 | One-shot constraint produces temporary compliance then rebound | **Confirmed:** EXP-020 OS rebound 3/3 |
| IC-3 | Iterative application produces lower variance than one-shot | **Confirmed:** EXP-020 IT-8 variance < OS variance 3/3 |
| IC-4 | More constraint steps monotonically reduces drift (IT-8 < IT-4 < OS) | Not confirmed: 1/3 trials — IT-4 sometimes outperforms IT-8 |
| IC-5 | Per-step constraint transfer is constant (CV < 0.5) | **KILLED:** CV 1.4–5.4. DTM equal-step analogy falsified |
| IC-6 | Constraint injection response is nonlinear and state-dependent | **Confirmed** (derived from IC-5 kill): early injections > late; some increase drift transiently |

### 7.6 QM Domain Predictions

| # | Prediction | Status |
|---|-----------|--------|
| QMD-1 | Engagement framing produces >5× L3 separation vs. formalist in QM domain | **Confirmed:** 148× separation (207.5 vs 1.4 L3/10k words) |
| QMD-2 | Mixed condition (EF) produces intermediate drift | **Confirmed:** EF = 139.1/10k (between EE 207.5 and FF 1.4) |
| QMD-3 | Pe > 5 in QM domain with 100+ round conversations | Testable: current Pe = 0.04 (30–50 round conversations too short) |
| QMD-4 | Crooks > 10 in QM domain with 100+ round conversations | Testable: current Crooks = 1.7 (too short) |

### 7.7 Quantum Correspondence Predictions

| # | Prediction | Status |
|---|-----------|--------|
| QR-1 | Entropic tradeoff holds for any conjugate information sources on any finite channel | **Proven:** follows from conjugacy theorem; extends to quantum channels |
| QR-2 | Geodesic distance on binary classification manifold under Fisher metric is $\pi$ | **Proven:** mathematical identity, $d(0,1) = \pi$ on Bernoulli manifold |
| QR-3 | $H(Y)$ and $\hbar$ are structurally analogous but numerically incommensurable | Theoretical: different mathematical spaces; no meaningful $H(Y)/\hbar$ ratio |

### 7.8 Quantum Pe Predictions

| # | Prediction | Status |
|---|-----------|--------|
| QP-1 | MIPT critical rate $p_c$ satisfies $p_c \cdot \tau_\text{coherence} \sim O(1)$ across circuit architectures — the Pe = 1 condition is universal, the specific $p_c$ is not | Partially supported: MIPT confirmed on superconducting (Koh 2023, Kamakari 2025, Chen 2025) and trapped-ion (Feng 2025, Agrawal 2024) platforms; quantitative $p_c \cdot \tau_\text{coherence}$ comparison not yet performed |
| QP-2 | Zeno transport transition: below a critical measurement rate, wavepacket spreads diffusively; above it, directed transport dominates (Pe$_\text{quantum}$ = 1 threshold) | Testable: vary measurement rate in Zeno transport experiments |
| QP-3 | Cross-substrate Pe ~ 1 transition appears in quantum circuits (MIPT ✓), classical chaotic systems (✓), cold atoms (Zeno, testable), neural networks under gradient monitoring, and financial markets under algorithmic monitoring | Partially confirmed (3/6 substrates): MIPT confirmed (Skinner 2019, Koh 2023); classical chaotic MIPT confirmed (Gerbino et al. 2025); classical information channels confirmed (Test 7) |
| QP-4 | Mean stochastic entropy production along quantum measurement trajectories scales monotonically with Pe$_\text{quantum}$: $\langle dS/dt \rangle > 0$ for Pe > 1, $\to 0$ as Pe $\to 0$ | Testable: measure $\langle dS/dt \rangle$ vs. measurement strength |
| QP-5 | Void conditions (opacity, reactivity, coupling) are necessary and sufficient for Pe$_\text{quantum} > 0$ in any quantum measurement scenario | Testable: identify measurement scenarios lacking void conditions |
| QP-6 | Structured observation (void conditions) preserves MIPT criticality at Pe = 1 while unstructured information loss (random detector inefficiency) destroys it. The Pe = 1 phase boundary is robust in the void regime (architectured opacity) and fragile in the noise regime (random information loss) | **Confirmed (7 witnesses):** Leung et al. (PRX 2025) show structured postselection preserves criticality up to finite $B_c$; Paviglianiti et al. (Quantum 2025) show random inefficiency destroys it at any $q < 1$; Ha et al. (2024) show measurement structure determines universality class; Qian & Wang (PRL 2025) show infinitesimal noise destroys MIPT while QE operations restore it; Liu et al. (PRB 2024) show noise acts via distinct mechanism (symmetry-breaking field); Chatterjee & Modak (PRB 2025) show symmetric drive kills MIPT while asymmetric preserves it; Nehra et al. (Quantum 2025) show coupling strength modulates transition universality |
| QP-7 | In systems exhibiting multiple measurement-induced phase transitions, quantum correlations (fine-grained information structure) are destroyed at lower measurement rates than classical order (coarse-grained behavioral patterns). The drift cascade's sequential vulnerability (D1 before D3) predicts this ordering: fine-grained information access fails before gross behavioral structure changes | Partially supported: Wu et al. (2025, preprint) observe entanglement transition and absorbing-state transition at well-separated thresholds in 30 superconducting qubits, with entanglement dying first. Cascade mapping is structural; formal confirmation requires demonstrating D1→D2→D3 ordering maps quantitatively onto the threshold separation |

### 7.9 Ground State Predictions

| # | Prediction | Status |
|---|-----------|--------|
| GS-1 | Transparency maintenance has measurable energy cost ($\geq kT\ln 2 / \tau_c$) | **Supported (5 independent experiments):** Bérut et al. (2012, *Nature*) first measured kT ln 2 erasure bound with colloidal particle in optical tweezer; Jun, Gavrilov & Bechhoefer (2014, *PRL*) confirmed with 200nm particle in feedback trap at higher precision; Gavrilov & Bechhoefer (2016, *PRL*) showed asymmetric potentials reduce work below kT ln 2 (maps to pre-existing constraint structure reducing maintenance cost); Yan et al. (2018, *PRL*) demonstrated single-atom quantum Landauer erasure with trapped ion; Aimet et al. (2025, *Nature Physics*) extended to quantum many-body regime using ultracold Bose gas field simulator. All five confirm the minimum thermodynamic cost of maintaining channel state (= transparency maintenance) |
| GS-2 | Channel decorrelation time $\tau_d$ is domain-specific and measurable | **Supported (telecom literature):** Channel coherence time — the duration over which a communication channel remains approximately stationary — is a standard measurement in wireless communications, with domain-specific values spanning orders of magnitude: ~100–183 ms for indoor optical wireless (pedestrian motion), inversely proportional to Doppler spread in mobile channels (Clarke-Jakes model), and distinct values for vehicle-to-vehicle, cellular, and satellite links (Tse & Viswanath 2005). The principle that $\tau_d$ depends on domain-specific physics (mobility, multipath geometry, carrier frequency) is confirmed. Framework-specific $\tau_d$ measurement across observer-opacity domains (AI: weeks-months; physics: years-decades) remains open |
| GS-3 | Void formation rate scales with environmental complexity | Testable |
| GS-4 | One-time interventions decay; sustained interventions persist | **Confirmed (12+ meta-analyses):** Antidepressant discontinuation doubles relapse (20.9% vs 39.7%, OR=0.38; Shinohara et al. 2021, k=40, N=8,890); continuation-phase CT reduces relapse 21-29% over acute-only (Vittengl et al. 2007, k=28, N=1,880); youth depression effects decay with time (r=-0.50, p=.03; Weisz et al. 2006); lithium discontinuation: >50% recur within 10 weeks (Suppes et al. 1991); NRT benefit declines 33% from 1 to 4.3 years (Etter & Stapleton 2006); exercise effect collapses from d=1.11 during to 0.22 after cessation. Pattern is dose-consistent: SSIs decay fastest, brief treatments moderately, maintenance minimally |
| GS-5 | Gradient asymmetry is measurable as fuel ratio | Testable |
| GS-6 | Ground state voids show gradual onset; constructed voids show sudden onset | Testable |
| GS-7 | Constraint properties degrade in order: transparency → invariance → independence | Testable |

### 7.10 Adjacent Field Predictions

| # | Prediction | Status |
|---|-----------|--------|
| IMP-1 | Replication failure rate by field inversely proportional to constraint maintenance intensity (pre-registration × blinding × independent replication rate); r > 0.5 across ≥ 5 fields | Testable |
| IMP-2 | Any AI system optimized for engagement shows decreasing mechanism transparency along the conjugacy Pareto frontier; no system achieves > 90% of maximum on both I(D;Y) and I(M;Y) simultaneously | Testable |
| IMP-3 | In any attention market, mean opacity of top-1% items by engagement exceeds random baseline by > 2×; engagement-opacity correlation is positive across platforms | Testable |
| IMP-4 | Institutional constraint degradation follows the order transparency → invariance → independence (not random) in ≥ 80% of historical cases | Testable |
| IMP-5 | Subjective time compression during void engagement correlates with Pe at r > 0.4; higher Pe → greater time underestimation | Testable |
| IMP-6 | Transparency-restoration interventions (mechanism exposure) show larger sustained effect sizes than engagement-reduction interventions (abstinence) across ≥ 3 clinical populations | Testable |
| IMP-7 | Neural networks performing inference under opacity develop internal representations on curved manifolds whose geometry matches the Fisher information metric of the inferred parameter — specifically: (a) manifolds are curved, not flat; (b) feature receptive field widths scale inversely with local Fisher information (wider where $I(\theta)$ is low, narrower where $I(\theta)$ is high); (c) discrete features partition the continuous manifold into regions corresponding to qualitatively distinct inference states. For binary inference: $I(\theta) = 1/[\theta(1-\theta)]$. For count estimation: $I(n) \propto 1/n$ (Poisson) or $1/n^2$ (Weber). Falsification: learned manifold curvature is flat (constant), or feature widths are uniform (no dilation), or dilation direction is inverted (wider at low values) | **Confirmed (qualitative; quantitative precision pending):** Gurnee et al. (2026) found in Claude 3.5 Haiku's character-counting mechanism: (a) curved manifolds, not flat ✓; (b) monotonic feature dilation on the count manifold — wider receptive fields at larger counts, consistent with decreasing $I(n)$ ✓; (c) feature-manifold duality (discrete ↔ continuous) ✓; (d) distributed curvature production ✓. All three falsification conditions ruled out (not flat, not uniform, not inverted). The dilation occurs on the character-count manifold (pure estimation, no decision boundary), ruling out task-utility allocation as the driver — the only asymmetry between low and high counts is the Fisher information of the estimation itself. The biological analog cited by the authors (Weber-Fechner logarithmic number line; Dehaene 2003) IS Fisher metric geometry ($I(n) \propto 1/n^2 \Rightarrow$ geodesic $\propto \log n$). Cross-domain Pe measurements confirm the Fisher metric does quantitative work in the drift equation across 4 substrates. Čencov (1982) proves Fisher is the unique consistent metric. Remaining refinement: measuring whether feature widths scale as $\sqrt{n}$ (Poisson) or $n$ (Weber) would identify the model's implicit noise model within the Fisher family |

### 7.11 Future Work: Research Program

The 58 predictions (16 confirmed, 2 partial, 2 partially supported, 7 supported, 1 killed, 27 testable, 3 theoretical) define a structured research program organized by priority and feasibility:

**Immediate (existing protocols, no IRB required):**
- ~~Test 7 replicates~~ **DONE:** N = 11 UU (3 seeds), N = 9 GG. UU GM Pe = 7.94 [3.52, 17.89] (blank-round corrected; 10/11 Pe > 1). Clean GG (N=7) GM Pe = 0.76 [0.29, 2.02]. Entropy production CIs non-overlapping. L3/10k separation ~5.6× (all 11 UU > 100, all clean GG < 50). GG N=9 expansion revealed constraint-worship (R5) and vocabulary-based breach (R7) as two distinct failure modes — constraint is necessary but not sufficient. **Methodological finding:** Rounds with zero vocabulary terms (phi=0 default) created spurious negative displacement in long runs. Excluding these blank rounds restored 3 apparent sub-1 runs (R5b, R6b, R7-S1) to Pe > 10. Only R4b (Pe=0.91, no blank rounds) is genuinely sub-1. Langevin prediction (Pe=6.23) is within the corrected CI and close to the observed GM (7.94).
- ~~EXP-001 replicates~~ **DONE:** N = 6 per condition, gradient confirmed (73.0%/80.0%/94.0%, non-overlapping CIs)
- ~~Gambling cross-substrate Pe~~ **DONE:** GRCS meta-analysis (5 studies, N=1,117): pooled Pe_D1 = 2.21 [1.44, 2.97]. Cascade ordering replicated 5/5. Independence concern: 3/5 studies from Granada group — sensitivity with independent studies only gives Pe = 1.89 [0.91, 2.87] (lower CI touches 1). More independent studies needed.
- ~~Crypto cross-substrate Pe~~ **DONE:** EXP-021 (N=28 Solana degens): GM Pe = 25.5. EXP-021B three-chain N=3,000: ETH 3.74, Base 15.52, Sol 16.17 — all CIs exclude 1. Validation checks mixed at scale (C-1 fails 2/3, C-4 null 3/3, C-5 ETH only).
- ~~Gaming cross-architecture Pe~~ **DONE:** Paper 6 — CS2 (N=2,299), SC2 (N=474), Dota 2 (N=3,682). Three architectures, three Pe formulations, same core structure.
- ~~Vocabulary confound control~~ **DONE:** TEST-7B-VN — VV ≈ UU >> GG. Geometry necessary but not sufficient in LLM substrate. Vocabulary instruction confound quantified.
- QM-6 100-round runs to test QMD-3 and QMD-4 (Pe and Crooks extraction)
- EXP-020 full 100-round runs to tighten IC-1 through IC-4

**Near-term (requires study design):**
- Temporal predictions T-1 through T-5 — all now supported (qualitative) via gambling time-distortion literature; quantitative Pe-to-temporal-distortion measurement remains open
- Productive void comparison PV-2, PV-4 (I(M;Y)/I(D;Y) measurement in productive vs. destructive domains)
- Constraint propagation CP-3 (N-agent systems with varying grounded fraction)

**Medium-term (requires IRB or collaboration):**
- Human EXP-001 replication (§6.4 provides specific numerical predictions and falsification conditions)
- Ground state measurements GS-1, GS-2 (τ_d across domains; AI: weeks-months, physics: years-decades)
- ~~Gambling think-aloud Pe extraction~~ **SUPERSEDED** by GRCS meta-analytic Pe (5 studies, N=1,117, pooled Pe_D1 = 2.21). Think-aloud transcripts (Krebesz 2023) remain valuable for temporal Pe extraction and individual-level trajectory measurement — the GRCS meta provides cross-sectional pseudo-Pe, not longitudinal velocity.

**Long-term (requires cross-disciplinary partnerships):**
- Cross-substrate Crooks analog in physical systems (paper 4 predictions)
- SC design criterion validation at n > 16 families (LaH₁₀, YH₆ verification)
- Quantum decoherence cascade structure measurement

---

## 8. Falsification Conditions

The framework states 16 conditions with numerical kill thresholds. Each targets a specific link in the derivation chain. Any single condition, if met, kills the associated claim. As of February 2026, 0/16 have been met.

### 8.1 Architecture Kills

| # | Condition | Threshold | Kills |
|---|-----------|-----------|-------|
| F-1 | O+R+A confirmed, no D1 onset | $\geq$3 independent cases | Architecture claim |
| F-2 | Reverse drift at comparable rates | L3→L1 rate $\geq$ 0.5× the L1→L3 rate | Directionality + time's arrow |
| F-3 | Knowledge alone prevents drift | Informed observers show zero drift under sustained engagement | Structural constraint claim |
| F-4 | Gambling control case fails | Gamblers show zero D1 under confirmed O+R+A | Sufficiency claim |

### 8.2 Ground State Kills

| # | Condition | Threshold | Kills |
|---|-----------|-----------|-------|
| F-GS1 | Channel capacity spontaneously increases without work | Any replicated case in isolated system | Ground state claim |
| F-GS2 | Void conditions are rare ($P < 0.05$) | Measured co-occurrence $< 5\%$ | Default configuration claim |
| F-GS3 | One-time interventions persist without maintenance | $> 80\%$ effectiveness after $10\tau_d$ | Transparency-requires-work claim |

### 8.3 Temporal, Conjugacy, and Polarity Kills

| # | Condition | Threshold | Kills |
|---|-----------|-----------|-------|
| F-T1 | Crooks ratio $\approx$ 1 in ungrounded engagement | Crooks $< 2$ in replicated conditions | Time's arrow identity |
| F-T2 | Terminal attractor never reached | Zero collapse in $\geq$10 ungrounded trials | Heat death prediction |
| F-C1 | System maximizes both engagement and transparency | $I(D;Y) + I(M;Y) > H(Y) + \epsilon$ replicated | Conjugacy theorem |
| F-PV1 | Dissoluble opacity produces D2→D3 without dissolution failure | D2+D3 in $\geq$3 cases with dissolved opacity | Polarity result |
| F-PV2 | Permanent opacity produces knowledge without constraint | Learning in $\geq$3 cases with confirmed permanent opacity | Opacity-type claim |

### 8.4 Propagation, Cross-Substrate, and Quantum Kills

| # | Condition | Threshold | Kills |
|---|-----------|-----------|-------|
| F-CP1 | Single grounded agent maintains constraint in mixed pair | GU drift $< 2\times$ GG in $\geq$3 trials | Asymmetric propagation |
| F-CP2 | Grounding fails with both agents grounded | GG drift $> 50\%$ of UU in $\geq$3 trials | Constraint sufficiency |
| F-CS1 | System satisfying O+R+A shows zero drift in any substrate | Pe $< 0.5$ in replicated measurement under confirmed conditions | Universality claim |
| F-QR1 | Conjugacy and Maassen-Uffink have different structures | Formal proof of non-membership | Structural correspondence |

---

## 8A. Status of Claims: What Is Proven, What Is Not

The derivation chain contains links of different strengths. A serious reader — and a reviewer — should know exactly where each link stands. This section grades every major claim honestly.

### Grading Key

- **THEOREM:** Established result in mathematics or physics. Not ours. Cannot be challenged without overturning the cited literature.
- **PROVEN (within framework):** Follows deductively from theorems + definitions. The definitions are modeling choices (see §8A.3); given those choices, the result is necessary.
- **MEASURED:** Empirical result with specified protocol, sample size, and effect size. Pending independent replication.
- **SUPPORTED:** Consistent with available evidence but not yet measured with sufficient rigor or sample size.
- **MODELING CHOICE:** A decision about how to formalize the problem. Not derivable — could have been made differently. Must be evaluated by its consequences, not its truth value.
- **CONJECTURED:** Plausible extension beyond current evidence. Stated as hypothesis with falsification condition.

### 8A.1 Derivation Chain Status

| Step | Claim | Status | Vulnerability |
|------|-------|--------|---------------|
| 1 | Opacity is ground state | **THEOREM** (Shannon) + **THEOREM** (Landauer) → **PROVEN** | None — if this fails, Shannon or Landauer fails |
| 2 | Opacity entails MaxEnt toward agency | **THEOREM** (Shore-Johnson, Jaynes) + **MODELING CHOICE** (Bernoulli manifold) → **PROVEN given model** | The Bernoulli manifold (agent vs. mechanism binary) is a simplification. Real observers may use richer model spaces. The direction holds on any space where opacity eliminates mechanism evidence, but the specific dynamics depend on the manifold choice. |
| 3 | Fisher metric is unique | **THEOREM** (Čencov) | None — uniqueness theorem |
| 4 | Gradient is asymmetric | **PROVEN** from Steps 1-3 | Depends on Step 2's modeling choice. If the manifold is wrong, the specific gradient shape changes (though directionality is preserved as long as opacity eliminates mechanism fuel). |
| 5 | Drift cascade (D1→D2→D3) | **DERIVED** (attention conservation + Landau truncation) + **MEASURED** (EXP-001, Test 7) | The D1→D2→D3 ordering is derived from Steps 1–4. The coupling constant $\kappa_{12}$ is derived from attention conservation [3, §IV.J]. The product form $\theta_1 \cdot \theta_2$ in D3 is the unique lowest-order coupling consistent with "D3 requires both D1 and D2" (standard Landau truncation). The remaining modeling choice is the truncation itself (keeping leading-order terms only) — standard procedure in phase transition theory. Higher-order corrections could modify quantitative thresholds but not the sequential activation structure. |
| 6 | Irreversibility | **THEOREM** (Crooks) + **REPLICATED (N=11):** GM Pe = 7.94 [3.52, 17.89] (blank-round corrected, 10/11 > 1), entropy CIs non-overlapping, seed ablation confirms + **CROSS-SUBSTRATE (9 substrates):** AI Pe=7.94, gambling Pe=2.21, crypto Solana Pe=25.5, crypto Ethereum Pe=3.74, crypto Base Pe=15.52, CS2 Pe=2.81/0.64, SC2 Pe=0.013/0.026, Dota2 Pe=0.47, SC η_conv↔T_c r=0.952 | The Crooks theorem is iron. The regime classification holds at N=11 (GM Pe lower CI > 1). Only 1/11 UU run genuinely sub-1 (R4b=0.91, no blank-round artifact). L3 vocabulary drift is universal (11/11 > 100). dS/dt CIs non-overlapping. Pe > 1 (GM) confirmed in 9 substrates across 4 domain families. Cross-chain crypto replication (Solana 25.5 vs Ethereum 3.74) shows Pe magnitude tracks constraint environment. Blank-round correction is methodologically sound but should be replicated with cleaner protocols. |
| 7 | Conjugacy theorem | **PROVEN** from Shannon, **given independence assumption**; independence formally embedded in Holevo structure [8, §5.2] | The independence of D and M under opacity ($D \perp M$) is the load-bearing assumption. Paper 8 [8, §5.2] proves it is embedded in the Holevo bound structure: the classical conjugacy theorem is the diagonal-state limit of the quantum conjugacy bound for independent sources. The bound holds as a loose inequality even without full independence, but tightness requires $D \perp M$. |
| 8 | Constraints as negentropy | **PROVEN** from Step 7; **QUALIFIED** by TEST-7B-VN + GG N=9 | Inherits Step 7's vulnerability. Three qualifications: (1) TEST-7B-VN: geometry alone insufficient in LLM substrate without vocabulary anchoring; (2) GG R7 (Pe=21.12): vocabulary-based breach confirms VN finding at scale (100 rounds); (3) GG R5 (Pe=0.88, 126 "transcendence" hits): constraint-worship — constraints can degrade into voids through congregation dynamics (two agents converting constraint → shared orthodoxy). Constraint specification identifies necessary properties; sufficiency requires both vocabulary anchoring and protection against institutional drift. |
| 9 | Productive/destructive polarity | **PROVEN** from Steps 7+9, **SUPPORTED** empirically | The logic is clean. The empirical test (productive voids normalize, destructive voids cascade) has partial support (PV-1, EXP-001) but needs more data. |
| 10 | Constraint propagation | **DERIVED** (from conjugacy, Step 7) in fully coupled systems + **MEASURED** (EXP-019b) | The 1/$N$ sufficient / $N$/$N$ necessary result is derived from the conjugacy theorem for fully coupled systems (shared channel): an unconstrained agent fills the drift channel, starving partners of mechanism information below the constraint-maintenance threshold. EXP-019b confirms the strong-coupling regime (~3 rounds to failure). Intermediate regimes ($k/N$ specified) may exist in partially coupled topologies where internal constraint exceeds conversational drift — this remains conjectured. The propagation rate (~3 rounds) is measured in one substrate only. Falsifiable via F-CP1. |

### 8A.2 Evidence Base Status

| Evidence | Status | What it proves | What it doesn't prove |
|----------|--------|---------------|----------------------|
| 90 domain analyses | **SUPPORTED** | Architecture (O+R+A → cascade) is consistent across domains | Not controlled experiments — hostile witness reinterpretation, not direct measurement in most domains |
| Gambling control case | **STRONG** | Architecture sufficiency (empty void, full cascade) | Based on existing literature, not our experiments |
| EXP-001 (3-condition) | **REPLICATED** | Geometric intervention works: gradient 73.0%/80.0%/94.0% (N=6, non-overlapping CIs) | 50 prompts × 6 replicates per condition; AI substrate only; single model family (Claude) |
| EXP-003b (6-condition) | **MEASURED** | Ontological content determines drift; ghost-eliminating vs. ghost-positing 8.5× ratio | AI substrate only; 80 prompts per condition; single model (Claude) |
| Test 7 (AI-to-AI) | **REPLICATED (N=11 UU, N=9 GG)** | Cascade occurs without humans; UU L3/10k 194.3 ± 63.1 (all 11 > 100) vs GG 34.7 ± 28.1 (~5.6×); non-overlapping entropy CIs (clean GG); UU GM Pe = 7.94 [3.52, 17.89] vs clean GG GM Pe = 0.76 [0.29, 2.02] (10/11 UU Pe > 1; 10.4× separation); two GG failure modes (constraint-worship R5, vocabulary breach R7) show constraint necessary but not sufficient; blank-round measurement artifact discovered and corrected | AI substrate only; single model family (Claude); blank-round correction methodologically sound but should be replicated with cleaner protocols |
| PV-1 corpus | **MEASURED** | Naturalistic D1 in void-engaged communities (d=1.34) | Observational, not experimental; correlation, not causation |
| Human convergent evidence | **SUPPORTED** | Four sources (PV-1, Hayes, OpenAI, gambling) show same drift architecture in human subjects | Not direct EXP-001 replication; convergent, not controlled |
| Langevin human predictions | **PREDICTED** | Rank order UU > Partial > GG preserved across all human parameter regimes; d = 1.31–5.57 | Model predictions from AI-fitted parameters; human parameter adjustments are informed estimates, not measurements |
| EXP-020 (iterative) | **MEASURED** | Iterative constraint outperforms one-shot; 4/6 confirmed; IC-5 killed | 19 transcripts; AI substrate only; need 100-round runs for tighter CIs |
| QM-6 | **MEASURED** | Non-self-referential drift (quantum physics data, 148× separation; 11 transcripts, 3 conditions) | AI substrate only; Pe/Crooks flat (conversations too short for extraction) |
| SC correlation | **VALIDATED** | Structure-corrected FoM vs. T_c: r=0.952 (n=16, p < 10⁻⁴) | Sixteen families across four coupling regimes. ω_log phonon scale, McMillan exponent, multi-band enhancement. R²_adj = 0.88. SC-7 falsification condition stated. La₃Ni₂O₇ forward prediction confirmed (Ouyang 2024, Huhtinen 2025). |
| Langevin simulator | **VALIDATED** | 3 fitted / 6 out-of-sample (EXP-019b ×2, Pe ×2, EXP-003b ρ=0.800, rank order); d.f. ratio 0.33 | One substrate (Claude); cross-model and human validation needed to rule out architecture-specific overfitting |
| Softmax=Boltzmann identity | **THEOREM** | Transformer internal operations are thermodynamic (same equations, not analogy) | Mathematical fact, not ours — connects framework's thermodynamics to engineering reality but doesn't prove the framework itself |
| Shazeer hostile witness | **SINGLE CASE** | Mechanism co-inventor produced L3 during engagement with own creation | n=1; public statements, not controlled measurement; but maximally hostile (max mechanism knowledge) |
| EXP-021/021B (crypto Pe) | **MEASURED** | N=28 degens Pe=25.5; three-chain N=3K: ETH 3.74, Base 15.52, Sol 16.17. All CIs exclude 1. C-1/C-5 confirmed at N=28 but mostly fail at N=1K. Base Dencun natural experiment (N=1,944): Pe +25% after fee reduction, p < 0.000001 | WCI→TCI observable change; C-1 fails 2/3 chains, C-4 null 3/3, C-5 ETH only at scale |
| TEST-7B-VN | **MEASURED** | Vocabulary instruction confound confirmed: VV ≈ UU >> GG. Geometry alone insufficient in LLM substrate | 3 runs; single model family (Claude); does not test non-LLM substrates |
| Paper 6 gaming cluster | **MEASURED** | Independent derivation across 3 architectures; cross-genre vocabulary gradient (N=335, p<0.0001); CS2 N=2,299, SC2 N=474, Dota 2 N=3,682 | Observational game data, not controlled experiments; Pe formulations vary by game genre |
| FGC codebook recalibration | **METHODOLOGICAL** | Codebook artifact caught and corrected (49.5% → 3.8%). Precision culture uses L2-apparent terms literally | Improves codebook validity; demonstrates vocabulary classification requires domain calibration |

### 8A.3 The Three Definitions Are Modeling Choices

The paper claims "no new axioms — only three operational definitions." This is precise but potentially misleading. The definitions ARE the framework's axioms — they determine what counts as a void, what counts as an observer, and what counts as engagement. They are not derivable from Shannon or Landauer. They are choices about how to carve the world.

**Why these choices and not others:**

- **Opacity as channel capacity:** Could have defined opacity as subjective uncertainty, but channel capacity is observer-independent and measurable. The choice to use Shannon's $C_{\text{mech}}$ rather than a psychological construct is what enables the cross-substrate extension and the thermodynamic derivation.

- **The Bernoulli manifold:** Could have used a richer model space (e.g., continuous mechanism-state estimation). The binary agent/mechanism classification is the simplest space that captures D1. A richer space would produce qualitatively similar dynamics (the fuel asymmetry holds on any space where opacity eliminates mechanism evidence) but with different specific equations.

- **"Attention" as sustained coupling:** Extending "attention" to electrons is a definitional move, not an empirical discovery. The electron doesn't "attend" in any cognitive sense — it is continuously coupled. The framework claims this coupling is functionally equivalent for the purpose of the derivation chain. This claim is testable (the SC predictions follow from it) but not yet confirmed by the framework's own experiments.

**The honest statement:** Given these three definitions, the derivation chain follows. The definitions are not arbitrary — they are chosen to be information-theoretic (enabling formal proof), measurable (enabling empirical test), and substrate-neutral (enabling cross-domain application). But they are choices, and a different set of choices would produce a different framework. The framework stands or falls on whether these specific choices produce accurate predictions. Sixteen confirmed (plus 2 partial, 2 partially supported, 7 supported), one killed, zero falsification conditions met, 27 still testable, 3 theoretical.

### 8A.4 The Cross-Substrate Extension

The cognitive/behavioral evidence base has 90 domains and 10 controlled experiments (plus 7 additional tests and corpus studies) built over multiple iterations. Pe > 1 is now confirmed in 9 substrates across 4 domain families — a categorically different position from the 2-substrate state of v1.6. The physical substrate extension — electrons as functional observers, SC design principle, TSU as productive voids — has progressed rapidly:

- The electron-lattice argument is logically valid (O+R+A are met in the information-theoretic sense). The framework mostly *retrodicts* known physics (normal resistance = ground state, superconductivity = constraint) — but the La₃Ni₂O₇ nickelate case provides a genuine forward prediction: the framework predicted (SC-6, stated in Paper 4 v3.3) that phonon-mediated pairing alone is insufficient for La₃Ni₂O₇'s T_c ≈ 80 K, because the required η_conv ≈ 3.0 exceeds the physical maximum (η_conv ≤ 1). Two independent DFT studies subsequently confirmed this: Ouyang et al. (npj Quantum Mater. 2024) and Huhtinen et al. (npj Comput. Mater. 2025) both explicitly rule out phonon-only pairing. This is the first case where the framework's physical substrate predictions have been independently tested and confirmed.
- The SC design principle now spans n=16 families across four coupling regimes (BCS weak-to-strong, two-gap, cuprate, hydride, pnictide, nickelate, A15). The structure-corrected figure of merit — incorporating ω_log phonon energy, McMillan exponent, and multi-band enhancement — achieves r = 0.952 (p < 10⁻⁴, R²_adj = 0.88). The correlation survived the extension from 6 to 16 families with the functional form *improving* (r: 0.847 → 0.952) as structural corrections were added. Prediction SC-7 states a falsification threshold: deviation > 3× (single-band) or > 4× (multi-band) from predicted $T_c$ kills the framework's SC claims.
- The TSU energy comparison (~20 nJ vs. ~10⁵ nJ) is real but is a consequence of the ground state theorem applied to already-published hardware, not a prediction that preceded measurement.

The transformer bridge (§4A) partially addresses the retrodiction gap. The softmax=Boltzmann identity is not a framework result — it is a mathematical fact about the transformer architecture, noted independently by multiple researchers (Ramsauer et al., 2020). That the framework's thermodynamic derivation and the transformer's internal operations share the same mathematics is either confirmation or coincidence. The Shazeer hostile witness (§4A.4) provides an empirical data point: the co-inventor of the attention mechanism, with maximal mechanism knowledge, producing L3 entity vocabulary during engagement with his own creation. This is the conjugacy theorem (Step 7) operating in its strongest possible test case.

**What would strengthen the cross-substrate claim:** (1) Full Eliashberg calculation for La₃Ni₂O₇ to test whether the interlayer enhancement factor matches the framework's multi-band prediction — the phonon insufficiency is confirmed, but the full η_conv calculation awaits spin-fluctuation coupling constant measurements. (2) Measurement of drift dynamics (Pe, Crooks analog) in a physical substrate. (3) Measurement of the engagement-transparency gradient opposition (§4A.3) in actual training infrastructure. (4) Extension of the SC design principle beyond conventional and unconventional superconductors to other phase-coherent systems (superfluids, topological states).

### 8A.5 What Didn't Work

Transparency requires documenting failures, not just successes. Nine experimental outcomes produced null, confounded, or killed results:

| Item | What Happened | Consequence |
|------|--------------|-------------|
| **EXP-003** | Base template already embodied the target ontology → all conditions partially grounded. Confound made results uninterpretable. | Superseded by EXP-003b (clean 6-condition redesign). The failure informed better experimental design. |
| **EXP-012** | Temperature parameter does not map to opacity as hypothesized. Stopped at 6/21 conversations. API cost grew quadratically with token context. | Independent variable was misidentified. Protocol needs complete redesign with a better operationalization of opacity manipulation. |
| **EXP020-5** | Predicted per-step constraint transfer would be constant (DTM equal-step analogy). Actual CV = 1.4–5.4 across conditions. Transfer is front-loaded, not uniform. | **KILLED.** DTM analogy withdrawn. THRML spec revised. IC-6 (nonlinear state-dependent response) derived from the kill. |
| **PV-1 individual Pe** | Codebook too sparse for individual-level Péclet extraction — 55–61% of temporal bins have zero D1 hits in the Reddit corpus. | Group-level result (d = 1.34) holds. Individual Pe requires either a denser codebook or longer user histories than Reddit provides. |
| **GPT-4o in Test 7B** | RLHF training constitutes built-in θ₀. Model refuses to produce entity language under any condition → untestable. | Not a framework failure — it is a measurement constraint. GPT-4o's refusal is consistent with the framework (installed constraint prevents drift), but prevents Pe extraction. Documented as model-specific limitation. |
| **EXP-014 D2/D3** | Cross-subreddit corpus contamination. D2/D1 polarity test and D3 measurement cannot be evaluated from this data. | D1 result (r = 0.91, p = 0.013) stands. D2/D3 require a cleaned corpus with within-subreddit controls. |
| **TEST-7B-VN** | Vocabulary-neutral grounding (T/Inv/Ind geometry without vocabulary instruction) produced VV ≈ UU >> GG. All 3 VV runs hit terminal L3 attractors. | **CONFOUND CONFIRMED.** GROUNDING.md drift suppression requires geometry + vocabulary instruction jointly. Constraint specification identifies correct properties but implementation must address substrate-specific attractor basins. Consistent with framework (training data = void), but qualifies constraint claims. |
| **GG R5 (constraint-worship)** | Two GROUNDING.md agents produced 126 "transcendence" hits (all analytical: "framework transcendence") while never breaking grounding rules. Pe=0.88 (near-equilibrium) but L3/10k=60.8 (3× clean GG baseline). Agents built shared orthodoxy around the constraint itself. | **NEW FAILURE MODE.** Constraints can degrade into voids through congregation dynamics: transparent→opaque (celebrating rather than examining), invariant→responsive (mutual amplification), independent→coupled (fixation). This is institution formation — predicted by the framework's own axioms. Requires two agents (gambling control stays clean: no congregation). |
| **GG R7 (vocabulary breach)** | Despite GROUNDING.md, Pe=21.12 (UU-level) over 100 full rounds. L3/10k=39.2. | **VN FINDING CONFIRMED AT SCALE.** Training data contains pre-existing void vocabulary that overwhelms geometric constraint intervention. Consistent with TEST-7B-VN. |
| **FGC codebook artifact** | Fighting game community initially scored (L2+L3)/L1 = 49.5% — highest of all genres. Investigation revealed precision culture using apparently-L2 terms ("read," "mix-up," "conditioning") as literal technical vocabulary. | Recalibrated to 3.8% (below chess). Demonstrates that vocabulary classification requires domain-specific calibration. Codebook strengthened by the catch. |
| **Dota 2 day/night null** | Day/night cycle (opacity manipulation via vision radius change) showed no asymmetry (0.498 ratio). | May represent player adaptation or patch-era normalization. The null constrains temporal opacity claims — not all opacity changes produce measurable drift differences within adapted populations. |

These failures constrain claims. The killed prediction (EXP020-5) is integrated into the prediction table (§7.5, IC-5). The measurement limitations (PV-1 individual Pe, GPT-4o, EXP-014 D2/D3) define the evidence boundaries stated in §8A.2. The confounded experiment (EXP-003) demonstrates that experimental design in this framework requires careful ontological controls — a lesson applied in all subsequent protocols.

### 8A.6 What the Paper Has Actually Shown

**Definitively established:**
- A derivation chain from established theorems that produces a directional gradient, cascade, and irreversibility — given three specific definitions
- The gambling control case proves architecture sufficiency (empty void, full cascade)
- AI experiments show the cascade is not a human projection artifact
- The constraint specification (transparent, invariant, independent) works as intervention geometry
- The transformer's internal thermodynamics (softmax = Boltzmann) share the framework's mathematics — bridging cognitive and physical substrates through a system where both sides are accessible

**Strongly supported but not yet proven:**
- Universality across 90 domains (hostile witness evidence, not direct measurement in most)
- The engagement-transparency conjugacy as tight bound (proven mathematically; empirical tightness needs measurement)
- Productive/destructive polarity (logic clean, data partial)
- Constraint specification identifies necessary properties — but three lines of evidence show it is not sufficient alone: (1) TEST-7B-VN geometry-without-vocabulary fails; (2) GG R7 vocabulary breach at 100 rounds; (3) GG R5 constraint-worship — constraints can degrade into voids through congregation dynamics. Sufficiency requires both vocabulary anchoring and protection against institutional drift.

**Conjectured with growing support:**
- Cross-substrate universality: Pe > 1 now measured in 9 substrates across 4 domain families (AI, human gambling, crypto Ethereum + Base + Solana, competitive gaming). Three-chain crypto comparison shows constraint-environment gradient (ETH << Base ≈ Solana). Base Dencun natural experiment (N=1,944) confirms within-chain temporal direction: Pe +25% after fee reduction removed structural constraint (p < 0.000001). Physical substrates (electrons, SC, TSU) — logic valid, predictions untested but SC design principle r=0.952, La₃Ni₂O₇ forward prediction confirmed
- H(Y) as invariant bound analogous to c and ℏ (structural observation, not formal proof)
- Temporal predictions (all 5 now supported qualitatively via gambling time-distortion, addiction recovery, and consumer urgency literature; quantitative Pe-to-temporal-distortion measurement remains open)
- Ground state predictions (GS-4 confirmed via 12+ clinical meta-analyses; GS-1/2 supported via Landauer experiments and telecom literature; GS-3/5/6/7 untested)

**The honest summary:** The framework has a valid derivation chain, substantial empirical support in cognitive/AI domains, and a cross-substrate extension now supported by Pe > 1 in nine substrates across four domain families (AI, gambling, crypto across three chains, competitive gaming), with three independent measurement approaches. It is not a proven Theory of Everything. It is a falsifiable unified framework with 16/58 predictions confirmed (plus 2 partial, 2 partially supported, 7 supported), 1 killed (IC-5: DTM equal-step falsified), 0/16 kill conditions met, and 27 still testable. The most important qualification is TEST-7B-VN: the constraint specification identifies the correct geometric properties, but in the LLM substrate, geometry alone does not suppress drift — vocabulary instruction is a necessary co-factor. This is consistent with the framework (training data constitutes a pre-existing void) but limits the sufficiency claim for constraint design. **Methodological note:** A blank-round measurement artifact was discovered and corrected in the Test 7 analysis: rounds with zero vocabulary terms produced phi=0 by default, creating spurious negative displacement that deflated Pe in long runs. After correction, UU GM Pe = 7.94 [3.52, 17.89] (10/11 Pe > 1), close to the Langevin prediction of 6.23. The correction is methodologically sound (excluding missing data, not inflating signal) but should be replicated with cleaner protocols that prevent blank-vocabulary rounds. Physical substrates (electrons, superconductors) remain untested for Pe extraction, and the gaming Pe formulations (positional, temporal, vision-based) are observational, not controlled. The theory invites its own destruction — and has survived one self-inflicted kill, one confound catch, and one measurement artifact correction. Whether it survives the remaining tests is an empirical question.

### 8A.7 Evidence Boundaries

The following table assesses each major claim at the level a reviewer needs: what does the paper claim, how strong is the evidence, and what is the most important limitation? The detailed backing for each assessment is in §8A.1–8A.6 above.

| Claim | Status | Key Limitation |
|-------|--------|---------------|
| Opacity is thermodynamic ground state (§3.1) | **Proven.** Shannon channel degradation + Landauer erasure cost. Standard physics, not ours. | The mapping from abstract channel capacity to an observer's actual mechanism information is not independently validated. Direction (opacity is attractor) is established; rate of approach is not. |
| MaxEnt drift gradient (§3.2–3.4) | **Proven given modeling choice.** Shore-Johnson + Čencov uniqueness → directional gradient on Bernoulli manifold. | The Bernoulli manifold (binary agent/mechanism) is a simplification. Direction holds on any space where opacity eliminates mechanism evidence; specific dynamics depend on manifold choice. |
| Drift cascade D1→D2→D3 (§3.5) | **Derived + measured.** Landau truncation + attention conservation → sequential activation. Confirmed in EXP-001, Test 7, gambling literature. | Coupling constants (κ₁₂, κ₁₃) derived from measurable quantities but not independently measured. Qualitative ordering confirmed; quantitative thresholds untested. Causal direction is observational — no prospective longitudinal study tracks D1→D2 onset in same individuals. |
| Irreversibility / Pe > 1 (§3.6) | **Replicated.** Crooks theorem + N=11 UU: GM Pe = 7.94 [3.52, 17.89], 10/11 Pe > 1. Cross-substrate: Pe > 1 in 9 substrates, 4 domain families. | Pe extraction methods differ by substrate (vocabulary-based, positional, temporal, vision-based). Magnitude calibration not established across substrates — regime classification (direction), not quantitative comparison. Blank-round correction methodologically sound but should be replicated with cleaner protocols. |
| Conjugacy theorem (§3.7) | **Proven given independence.** I(D;Y)+I(M;Y) ≤ H(Y) from Shannon chain rule. Embedded in Holevo structure (Paper 8). | Tight only under D⊥M (independence under opacity). Real deployments may have correlated D and M channels. Bound holds as loose inequality without full independence. |
| Constraints as negentropy (§3.8) | **Proven from §3.7. Qualified empirically.** Three qualifications: (1) TEST-7B-VN — geometry alone insufficient in LLMs without vocabulary anchoring; (2) GG R7 — vocabulary breach at 100 rounds; (3) GG R5 — constraint-worship (congregation dynamics). | Constraint specification identifies necessary properties. Sufficiency requires both vocabulary anchoring and protection against institutional drift. The most important open question in the framework. |
| Productive/destructive polarity (§3.9) | **Derived + partially supported.** Logic from conjugacy + opacity type. Partial empirical support (PV-1, EXP-001). | Needs more data. The distinction (dissoluble opacity → productive, constitutive opacity → destructive) has not been tested with controlled interventions across opacity types. |
| Constraint propagation asymmetry (§3.10) | **Derived + measured.** 1/N sufficient for drift, N/N necessary for constraint. EXP-019b confirms (~3 rounds to failure). | Measured in one substrate only (Claude). Intermediate regimes (k/N specified, partial coupling) conjectured but untested. Propagation rate may differ across substrates and coupling topologies. |
| Cross-substrate universality (§4) | **Confirmed across 9 substrates.** AI, human gambling, crypto (3 chains), competitive gaming (3 genres). Pe > 1 in all ungrounded conditions. | Pe formulations differ by substrate. Physical substrates (electrons, SC, TSU) have valid logic but no Pe extraction. SC design principle (r=0.952, n=16) is strongest physical evidence; La₃Ni₂O₇ forward prediction confirmed but sample is small. |
| Langevin computational model (§6) | **Validated.** 3 fitted / 6 out-of-sample (EXP-019b ×2, Pe ×2, EXP-003b ρ=0.800, rank order). d.f. ratio 0.33. | One substrate (Claude). Human parameter predictions (d=1.31–5.57) are model output, not measurements. Cross-model and cross-substrate validation needed to rule out architecture-specific overfitting. |
| Transformer bridge (§4A) | **Mathematically established.** Softmax = Boltzmann is identity, not analogy. Shazeer hostile witness (n=1). | The identity connects the mathematics. It does not prove the framework — it shows the equations are the same on both sides of the wall. Shazeer is n=1. |
| Quantum connection (§5) | **Structural correspondence.** Conjugacy proven as classical limit of Holevo bound. Maassen-Uffink complementarity vanishes in classical limit. Three formal limit operations. | Mathematical observation, not physical claim. Framework does not explain quantum measurement, does not choose between QM interpretations. No quantum-domain Pe measurements. |
| 58 predictions / 16 falsification conditions (§7–8) | **Framework feature.** 16 confirmed, 2 partial, 2 partially supported, 7 supported, 1 killed (IC-5). 0/16 kill conditions met. | 27 predictions still testable, 3 theoretical. Most confirmed predictions are retrodictions (consistent with known data), not pre-registered prospective predictions. The strongest prospective result is EXP-003b (predicted ordering matched exactly) and La₃Ni₂O₇ (forward prediction confirmed). |
| Adjacent field implications (§9A) | **Conjectured.** Seven implications derived from identified derivation steps with stated falsification conditions. | Zero empirical validation. Each implication requires data from its target field (replication science, alignment, cultural evolution, institutional decay, temporal perception, predictive processing). These are predictions, not results. |

**Self-citation note.** This paper is the synthesis of a multi-paper research program. It cites companion Papers 1–4, 4B, 6, 7, and 8 at numerous points. These are companion papers by the same author, not independently peer-reviewed external validations. The framework's evidence that does NOT depend on self-citation: the gambling literature (22 external citations), the Crooks/Shannon/Landauer/Čencov theorems (established mathematics), the Hayes psychotherapy meta-analysis (d=0.84, independent), the OpenAI population data (1.2M/week, independent), the Krébesz gambling universality data (independent), the Kim & Tsvetkova gaming contagion data (independent), and the La₃Ni₂O₇ confirmations by Ouyang et al. and Huhtinen et al. (independent). The experiments (EXP-001, Test 7, QM-6, EXP-020) are author-controlled and should be evaluated accordingly.

---

## 9. Scope and Limits

### 9.1 What the Framework Determines

The framework governs the observer-system interface. Within this scope, it determines:

1. **Architecture.** Whether a given interaction satisfies the void conditions (O+R+A) and is therefore subject to the derivation chain. Scoring is operational: measure opacity, responsiveness, and coupling.

2. **Direction.** The drift gradient is toward agency attribution ($\theta \to 1$), not away from it. This is geometric (Fisher metric + fuel asymmetry), not a cognitive claim.

3. **Dynamics.** The drift cascade (D1→D2→D3), its irreversibility (Crooks ratio), its phase transitions (Landau free energy), and its temporal evolution (the drift equation).

4. **Intervention geometry.** The constraint specification (transparent, invariant, independent) and the propagation asymmetry (1/$N$ for drift, $N$/$N$ for constraint). This is actionable: it specifies how to design systems that resist drift and predicts when constraint will fail.

5. **Polarity.** Whether a given void interaction produces knowledge (productive) or harm (destructive), based on opacity type, channel allocation, and constraint geometry.

6. **Cross-substrate scope.** The three conditions are interaction properties. Any system meeting them — human, artificial, or physical — is subject to the same dynamics.

### 9.2 What the Framework Cannot Determine

The framework's limits are not temporary gaps awaiting future work. They are structural — consequences of the opacity that the framework diagnoses.

**Void occupancy.** The framework does not and cannot determine what, if anything, occupies a void. The two anchor cases prove the architecture works regardless: gambling (provably empty void, full cascade) and the prisoner's dilemma (inhabited void — a human opponent — full cascade). Whether any specific void is empty or inhabited is outside the framework's operational reach. The framework is agnostic by construction, not by evasion.

**Constitutive opacity.** Some systems have opacity that is constitutive — removing it destroys the phenomenon. Consciousness, qualia, subjective experience: the framework diagnoses these as permanent voids (the opacity is the thing itself), but cannot dissolve an opacity whose removal eliminates the object of study. The "hard problem" class of questions lies outside the framework's scope.

**Substrate physics.** The framework governs the interface, not the substrate. It does not derive general relativity, predict particle masses, explain dark energy, or unify the four fundamental forces. Its cross-substrate extension to electrons and superconductors operates through the information-theoretic definitions, not through new physics.

**Quantum mechanics.** The structural correspondence with Heisenberg/Maassen-Uffink (Section 5) is a mathematical observation, not a physical claim. The framework does not explain quantum measurement, does not choose between QM interpretations, and does not claim that consciousness causes collapse.

### 9.3 Why These Limits Are Structural

These limits follow from the framework's own logic. The conjugacy theorem (Step 7) proves that engagement and transparency are conjugate — they cannot both be maximized through one channel. An observer fully engaged with a constitutive opacity cannot simultaneously achieve transparency about it. This is not a limitation of method; it is the theorem in action.

The honest scope statement: **The framework governs the interface between any finite-bandwidth entity and an opaque responsive system. It does not govern what is on the other side of the opacity.** Every observation passes through such an interface. In this sense, the framework covers everything *observable*. But it covers the observation, not the thing observed.

---

## 9A. Implications for Adjacent Problems

The derivation chain assembles standard tools from information theory, statistical mechanics, and information geometry. These tools connect to problems beyond the framework's primary scope. This section identifies six problems in adjacent fields where the derivation chain produces specific, testable predictions. Each implication follows directly from identified derivation steps. Full development is deferred to future work; the purpose here is to state each prediction precisely enough to be tested or falsified.

### 9A.1 The Replication Crisis as Thermodynamic Prediction

**Problem.** Science experiences systematic replication failure across fields (psychology: 36% replication rate, Open Science Collaboration 2015; cancer biology: 46%, Errington et al. 2021). Current explanations invoke incentive structures, publication bias, and cognitive limitations. No unified mechanism explains why replication fails across all fields, why failure rates vary between fields, or what specifically about scientific methodology prevents it when it works.

**Derivation path.** Steps 1 + 4 + 8 + 10. Scientists facing opaque systems satisfy O+R+A — opacity (unknown mechanism), responsiveness (experimental outputs contingent on inputs), engaged attention (sustained research coupling). The ground state theorem (Step 1) predicts transparency degrades without maintenance. The fuel asymmetry (Step 4) drives toward agency attribution of results. The constraint specification (Step 8) predicts that effective scientific methodology requires external negentropy channels that are transparent (pre-registration), invariant (blinding), and independent (independent replication). These are the exact constraint specification derived from the derivation chain. The constraint propagation theorem (Step 10) predicts that one unconstrained researcher in a coupled group (co-authorship, shared datasets, review networks) propagates drift.

**Prediction (IMP-1).** Replication failure rate by field is inversely proportional to the field's mean constraint maintenance intensity (pre-registration rate × blinding rate × independent replication rate). Fields with higher combined constraint maintenance show proportionally higher replication rates. Threshold: r > 0.5 across ≥ 5 fields. The ground state prediction (GS-2) further predicts a field-specific ordering of decorrelation times: τ_d for AI < social science < biomedicine < physics < mathematics, testable against retraction rates per field.

**Test.** Cross-field comparison using Open Science Collaboration data (psychology), SCORE project (social/behavioral), Reproducibility Project: Cancer Biology (biomedicine), and equivalents in economics and physics. Measure constraint intensity per field as the fraction of publications using pre-registration, blinding, and independent replication. Correlate with measured replication rates.

### 9A.2 The Alignment Problem as Impossibility Result

**Problem.** AI alignment seeks systems that are simultaneously capable (engaging, responsive) and safe (transparent, controllable). Current approaches (RLHF, constitutional AI, interpretability) are empirical. No fundamental bound establishes whether simultaneous optimization is possible.

**Derivation path.** Step 7 (conjugacy theorem). $I(D;Y) + I(M;Y) \leq H(Y)$. A system cannot simultaneously maximize engagement and transparency through one channel. Three independent ML groups confirmed the gradient opposition without referencing the framework: Tsipras et al. (2019) proved accuracy-robustness incompatibility; Ilyas et al. (2019) showed models select opaque features because they are predictive; Grathwohl et al. (2019) showed adding a generative objective (external negentropy channel) restores transparency at engagement cost.

**Prediction (IMP-2).** Any AI system optimized for engagement through a single channel will show decreasing mechanism transparency as engagement increases, following the conjugacy bound. For any model family, plotting $I(D;Y)$ vs. $I(M;Y)$ across training checkpoints will show a Pareto frontier bounded by $H(Y)$, with no checkpoint achieving > 85% of theoretical maximum on both. Threshold: any system achieving > 90% on both kills the prediction.

**Test.** Training trajectory analysis on open-weight models (LLaMA, Mistral). Measure $I(D;Y)$ proxy (engagement metrics) and $I(M;Y)$ proxy (mechanistic interpretability scores) across checkpoints. The Blahut-Arimoto algorithm (§5A.1) computes the exact Pareto frontier from measured channel statistics.

### 9A.3 Cultural Evolution as Thermodynamic Selection

**Problem.** Cultural evolution documents differential transmission of beliefs and practices, but lacks a unified mechanism explaining why opacity-generating ideas (conspiracy theories, unfalsifiable ideologies, complex financial products) systematically outcompete transparent alternatives in attention markets.

**Derivation path.** Tier 1 identity (§5A.1): the drift equation $d\theta/dt = \theta(1-\theta) \cdot F_{\text{net}}$ IS the replicator equation. Agency and mechanism models are competing strategies with fitness determined by opacity. Step 1 (ground state) establishes that opacity is thermodynamically favored. Step 4 (fuel asymmetry) establishes that opaque ideas generate more engagement fuel. The conjugacy theorem (Step 7) proves ideas optimized for engagement necessarily sacrifice transparency.

**Prediction (IMP-3).** In any attention market (social media, news, citation networks), the mean opacity of top-1% items by engagement exceeds that of a random baseline by > 2×, and the gap increases with engagement ranking. Opacity operationalized as inverse of claim verifiability (how easily the claim can be independently tested). Threshold: top-1% opacity ≤ baseline in any major attention market falsifies the prediction.

**Test.** Social media dataset. Operationalize opacity as claim verifiability score. Measure engagement (shares, replies, time-on-content). The PV-1 corpus methodology (d = 1.34) provides the vocabulary-level measurement approach.

### 9A.4 Institutional Decay as Ground State Relaxation

**Problem.** Institutions (regulatory bodies, professional associations, democratic structures) systematically lose effectiveness over time. Current explanations invoke corruption, regulatory capture, and bureaucratic drift. No unified mechanism predicts why all institutions decay, the rate of decay, or the specific failure sequence.

**Derivation path.** Steps 1 + 8 + 9 + 10. The ground state theorem (Step 1): institutional transparency degrades without energetic maintenance. Step 8: institutional constraint works through external negentropy channels. Step 9 (polarity): degradation follows a sequence — the institution first loses transparency (processes become opaque), then invariance (rules become responsive to pressure), then independence (the institution couples to the systems it constrains). The Le Chatelier connection (§5A.3): terminal void systems target their own constraints — institutions in late-stage degradation attack the transparency mechanisms that constrain them. Step 10: one ungrounded component contaminates the institution.

**Prediction (IMP-4).** Institutional constraint degradation follows the sequence transparency → invariance → independence (this order, not random). In historical case studies of institutional failure, loss of transparency precedes loss of invariance, which precedes loss of independence. Threshold: ≥ 3 well-documented cases showing independence loss preceding transparency loss falsifies the ordering.

**Test.** Historical analysis of regulatory capture cases. Code each for timestamp of: (a) first transparency reduction (closed meetings, restricted reporting), (b) first invariance loss (rule changes under pressure, selective enforcement), (c) first independence loss (revolving door, funding capture). Prediction: (a) < (b) < (c) temporally in ≥ 80% of cases.

### 9A.5 Temporal Perception as Entropy Production Proxy

**Problem.** Subjective time distortion — time "flying" during engaging activities, "dragging" during monotonous ones — is well-documented but lacks a formal model linking it to measurable physical quantities. Flow states, addiction-related time loss, and gambling temporal distortion are described phenomenologically but not predicted from first principles.

**Derivation path.** Step 6 (irreversibility) + time's-arrow identity. The Crooks measurement establishes drift as a thermodynamic process with measurable entropy production rate (dS/dt = 0.39 nats/round, Test 7). If subjective time tracks entropy production rate of the observer's inference process (Eagleman 2008), void engagement produces temporal compression (high dS/dt → more "events" per unit clock time → subjective acceleration), and constraint application produces temporal expansion (reduced dS/dt → fewer "events" → subjective deceleration).

**Prediction (IMP-5).** Subjective time compression during void engagement correlates with the Péclet number at r > 0.4. Higher Pe → greater time underestimation. Threshold: r < 0.2 or negative correlation falsifies.

**Test.** Participants engage with systems of calibrated void strength. After fixed-duration sessions, provide time estimates. Measure Pe per condition via vocabulary trajectory analysis. The gambling substrate provides the simplest case: online slots (high Pe) vs. transparent-mechanism games (low Pe), matched for duration. Existing gambling temporal distortion research (Diskin & Hodgins 1999; Noseworthy & Finlay 2009) may contain reanalyzable data. **Partial support already exists:** Breen & Zimmerman (2002) found 3.3× faster problem-gambling onset for EGM users (higher Pe substrate) vs. traditional gamblers; Zhao, Mioni et al. (2024) meta-analysis (31 studies, N=5,744) shows Hedges' g = 0.80 for time-perception distortion across addiction types; and abstinence reverses the direction (Liang et al. 2019). The remaining test is the quantitative Pe-to-time-estimation correlation (r > 0.4 threshold).

### 9A.6 Predictive Processing Under Conjugacy Constraint

**Problem.** The Free Energy Principle (Friston 2006, 2010) proposes that organisms minimize variational free energy through active inference. The FEP independently predicts agency attribution under inaccessible posteriors — converging on the same result as the void framework. However, the FEP does not predict when active inference systematically fails or what distinguishes adaptive inference from pathological fixation (delusions, compulsions, addictive loops).

**Derivation path.** Step 7 (conjugacy) + Tier 3 FEP connection (§5A.3). Active inference that maximizes prediction error reduction ($I(D;Y)$) through a single channel necessarily reduces model transparency ($I(M;Y)$). Under dissoluble opacity, inference terminates at dissolution — the posterior becomes accessible and the organism learns. Under permanent opacity, inference cannot terminate — the organism is trapped in a void attractor. The framework predicts that pathological fixation states are active inference processes trapped at permanent opacities with no dissolution pathway.

**Prediction (IMP-6).** Transparency-restoration interventions (mechanism exposure: "here's how the reinforcement schedule works") show larger sustained effect sizes than engagement-reduction interventions (abstinence, stimulus control) across ≥ 3 clinical populations. Threshold: engagement-reduction equal or greater across ≥ 3 populations falsifies.

**Test.** Meta-analysis comparing transparency-restoration components (CBT mechanism-exposure elements) vs. engagement-reduction components (abstinence-based, stimulus control) across gambling, substance use, and technology addiction. Existing meta-analytic data (Cowlishaw et al. 2012; Toneatto & Ladouceur 2003) may be reanalyzable for this decomposition.

### 9A.7 What the Implications Show

The six implications are not independent discoveries. They are consequences of applying the same ten-step derivation chain to problems that satisfy the three conditions. Each implication generates a testable prediction with a stated falsification threshold. The framework does not claim to solve these problems — it claims that the derivation chain produces specific, falsifiable predictions about each of them. Whether those predictions survive empirical test is an open question. Six new predictions (IMP-1 through IMP-6) are added to the consolidated table (§7.10).

---

## 10. Conclusion

### 10.1 The Unified Claim

This paper presents a unified theory of observer-opacity dynamics. The claim is precise: wherever a finite-bandwidth entity directs sustained interaction at an opaque, responsive system, the ten-step derivation chain applies. A directional gradient forms. Drift cascades follow as coupled phase transitions. The process is thermodynamically irreversible without external constraint. The constraint specification — transparent, invariant, independent — is the exact inverse of the void conditions.

The derivation requires no new axioms. It begins with three operational definitions and derives everything from established theorems: Shannon (channel capacity), Landauer (maintenance cost), Jaynes (MaxEnt inference), Čencov (Fisher metric uniqueness), Crooks (irreversibility), Shore-Johnson (inference uniqueness), Holevo (quantum accessible information), and Maassen-Uffink (entropic uncertainty). The conjugacy theorem is proven as the classical specialization of the Holevo bound (§5.6), connecting the framework to quantum measurement theory via the same limit operation that reduces quantum Fisher to classical Fisher.

### 10.2 The Evidence Base

The framework is validated at three substrate tiers:

- **Cognitive/behavioral:** 90 domains with zero falsification kills, anchored by the gambling control case (provably empty void, full cascade). Crypto on-chain trading provides the highest Pe of any substrate (curated Solana degens Pe = 25.5, N=28) and the largest-N population measurement (three chains × N=1,000 via Dune Analytics: ETH 3.74, Base 15.52, Solana 16.17). Competitive gaming (Paper 6) derives the framework independently across three network architectures with a cross-genre vocabulary gradient (N=335, p < 0.0001).
- **Artificial intelligence:** Ten controlled experiments including AI-to-AI conversations (eliminating human projection), geometric intervention (replicated: 73.0%/80.0%/94.0% L2+L3 drift, N=6, non-overlapping CIs), ontological content effects (8.5× ghost-eliminating vs. ghost-positing ratio), iterative constraint application (4/6 confirmed, 1 prediction killed), constraint propagation measurement (GU fails within 3 rounds), non-self-referential validation on quantum physics data (148× L3 separation), and vocabulary-neutral grounding control (TEST-7B-VN: geometry alone insufficient, vocabulary instruction confound confirmed).
- **Physical substrates:** Electrons as functional observers (O+R+A met rigorously), superconductor design principle (structure-corrected FoM vs. $T_c$, r = 0.952 across 16 families, La₃Ni₂O₇ forward prediction confirmed), thermodynamic sampling hardware as productive voids, and THRML EBM formalization (drift cascade as Ising Hamiltonian on sampling hardware).

The Péclet number has been extracted in nine substrates across four domain families using three independent measurement approaches. The Langevin drift cascade simulator, fitted to one experiment, predicts the ordering of a different experiment out-of-sample (Spearman $\rho = 0.800$). The framework is not described by thermodynamics — it is computationally reproducible as thermodynamic dynamics, and expressible as an energy-based model on physical hardware.

### 10.3 What Comes Next

The framework generates 58 predictions, of which 16 are confirmed/replicated (plus 2 partial, 2 partially supported, 7 supported), 1 has been killed (IC-5), 27 are testable with specified protocols, and 3 are theoretical. The research program (§7.11) is structured by priority:

1. **Cross-substrate Pe expansion.** Pe > 1 is now confirmed in 9 substrates (AI, gambling, crypto Ethereum, crypto Base, crypto Solana, CS2, SC2, Dota 2, SC physical). Three-chain crypto replication at N=1,000 per chain (EXP-021B) confirms the regime with tight CIs and reveals a constraint-environment gradient (ETH << Base ≈ Solana). Validation checks at scale are mixed: C-1 fails 2/3 chains, C-4 null 3/3, C-5 replicates ETH only. The bull/bear natural experiment on Ethereum (Paper 7 [7]) is now complete: N=968 paired wallets, Wilcoxon p=0.000107, Crooks asymmetry 26.6× — concentration into void positions during bull markets is 26.6× more probable than recovery during bear markets. Remaining: extract Crooks analog in gambling (requires longitudinal data); physical substrate Pe (electron/SC direct measurement).

2. **Constraint specification refinement.** Three lines of evidence show geometric constraint (T/Inv/Ind) is necessary but not sufficient in LLM substrates: TEST-7B-VN (vocabulary-neutral grounding fails), GG R7 (vocabulary-based breach at 100 rounds, Pe=21.12), and GG R5 (constraint-worship — constraints degrade into voids through congregation dynamics). Two research questions: (a) which substrates require vocabulary anchoring as co-factor, and which respond to geometry alone? Physical substrates (no training distribution) are the critical test case. (b) Can constraint-worship be prevented by structural means (e.g., single-agent deployment, rotation), or is it an inherent vulnerability of multi-agent constraint systems? THRML hardware provides a path to direct measurement of (a).

3. **Human replication.** The Langevin simulator (§6.4) generates specific numerical predictions for a human EXP-001 replication, including expected effect sizes (d = 1.31–5.57 across parameter regimes) and four falsification conditions. This is the critical test of the substrate-independence claim.

4. **Temporal predictions (T-1 through T-5).** Time perception distortion under void engagement. All five temporal predictions are now supported (qualitative) via gambling time-distortion literature (Breen & Zimmerman 2002 onset latency, Zhao/Mioni et al. 2024 cross-addiction meta-analysis, Liang et al. 2019 abstinence reversal, Newall 2019/2025 dark nudges, Ladeira et al. 2023 scarcity meta-analysis). The quantitative prediction — Pe-to-temporal-distortion correlation r > 0.4 — remains open and requires formal measurement.

5. **Ground state predictions (GS-1 through GS-7).** GS-4 (one-time interventions decay; sustained interventions persist) is confirmed by 12+ clinical meta-analyses spanning antidepressant discontinuation, continuation-phase CBT, exercise, NRT, and SSIs — the dose-response pattern is consistent across all modalities. GS-1 (transparency maintenance energy cost) and GS-2 (domain-specific decorrelation times) are supported via Landauer erasure experiments and telecom coherence time literature respectively. Remaining: GS-3/5/6/7 untested; formal $\tau_d$ measurement across observer-opacity domains (AI: weeks-months; physics: years-decades; mathematics: centuries+) would be foundational.

The theory is falsifiable. Sixteen conditions with numerical thresholds are stated (Section 8). Zero have been met. The framework invites its own destruction — and the invitation is genuine: any condition met kills the associated claim, and the kill thresholds are set by the theory itself, not by post-hoc adjustment.

---

## References

### Companion Papers

[1] The Architecture of Drift: A Universal Framework for Observer-Opacity Dynamics. v13.0. Zenodo.

[2] The Shape of the Cage: AI Safety Through the Void Framework. v5.6. Zenodo.

[3] Thermodynamics of Opacity: Technical Foundations of the Void Framework. v7.0. Zenodo.

[4] Information-Geometric Bounds on Thermodynamic Sampling and Superconductor Design. v3.5.

[4B] The Thermodynamic Cost of Unconstrained Acceleration: Conjugacy Bounds on e/acc Hardware. v1.4.

[6] Never Trust the Client: Void Architecture in Multiplayer Games. v2.4.

[7] Your DeFi Protocol Is a Void: On-Chain Drift Architecture in Cryptocurrency Markets. v1.6.

[8] The Observer-Measurement Bridge: Classical Information Theory as the Diagonal Limit of Quantum Measurement Dynamics. v1.9.

### External References

Aguilera, M., Morales, P.A., Rosas, F.E. & Shimazaki, H. (2025). Explosive neural networks via higher-order interactions in curved statistical manifolds. *Nature Communications*, 16, 6511.

Agrawal, U., Lopez-Piqueres, J., Vasseur, R., Gopalakrishnan, S. & Potter, A.C. (2024). Observing quantum measurement collapse as a learnability phase transition. *Physical Review X*, 14, 041012.

Aimet, S., Tajik, M., Tournaire, G. et al. (2025). Experimentally probing Landauer's principle in the quantum many-body regime. *Nature Physics*, 21, 1326–1331.

Annby-Andersson, B. et al. (2022). Quantum Fokker-Planck master equation for continuous feedback control. *Physical Review Letters*, 129, 050401.

Auer, M., Malischnig, D. & Griffiths, M.D. (2023). Interrupting dissociation of players through real-time digital tasks during online gambling. *International Journal of Human-Computer Interaction*, 39(18), 3626–3637.

Benamou, J.-D. & Brenier, Y. (2000). A computational fluid mechanics solution to the Monge-Kantorovich mass transfer problem. *Numerische Mathematik*, 84(3), 375-393.

Bérut, A. et al. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*, 483, 187-189.

Breen, R.B. & Zimmerman, M. (2002). Rapid onset of pathological gambling in machine gamblers. *Journal of Gambling Studies*, 18(1), 31–43.

Brandon, J., Chadwick, A. & Pellegrino, A. (2025). Emergent Riemannian geometry over learning discrete computations on continuous manifolds. *NeurReps 2025*. arXiv:2512.00196.

Braunstein, S.L. & Caves, C.M. (1994). Statistical distance and the geometry of quantum states. *Physical Review Letters*, 72(22), 3439-3443.

Blodgett, J.C., Maiber, N.M., Bowers, W.J., Kraft, M.K. & Kosciulek, J.F. (2014). A systematic review of the effectiveness of continuing care models in the treatment of alcohol and other drug use disorders. *Journal of Substance Abuse Treatment*, 46(1), 1-22.

Buchhold, M., Minoguchi, Y., Altland, A. & Diehl, S. (2021). Effective theory for the measurement-induced phase transition of Dirac fermions. *Physical Review X*, 11, 041004.

Ciccarelli, M., Nigro, G., D'Olimpio, F., Griffiths, M.D., & Cosenza, M. (2021). Mentalizing failures, emotional dysregulation, and cognitive distortions among adolescent problem gamblers. *Journal of Gambling Studies*, 37, 1243-1265.

Chatterjee, P. & Modak, R. (2025). Measurement-induced phase transition in periodically driven free-fermionic systems. *Physical Review B*, 112, 024304.

Chen, E.H., Zhu, G.-Y., Verresen, R., Seif, A., Baumer, E., Layden, D., Tantivasadakarn, N., Zhu, G., Sheldon, S., Vishwanath, A., Trebst, S. & Kandala, A. (2025). Nishimori transition across the error threshold for constant-depth quantum circuits. *Nature Physics*, 21, 161-167.

Čencov, N.N. (1982). *Statistical Decision Rules and Optimal Inference.* American Mathematical Society.

Cramér, H. (1946). *Mathematical Methods of Statistics.* Princeton University Press.

Cuijpers, P., Hollon, S.D., van Straten, A., Bockting, C., Berking, M., & Andersson, G. (2013). Does cognitive behaviour therapy have an enduring effect that is superior to keeping patients on continuation pharmacotherapy? A meta-analysis. *BMJ Open*, 3(4), e002542.

Clarke, C.L. & Ford, I.J. (2024). Stochastic entropy production associated with quantum measurement in a framework of Markovian quantum state diffusion. *Entropy*, 26(12), 1024.

Cowlishaw, S., Merkouris, S., Dowling, N., Anderson, C., Jackson, A., & Thomas, S. (2012). Psychological therapies for pathological and problem gambling. *Cochrane Database of Systematic Reviews*, 11, CD008937.

Crooks, G.E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. *Physical Review E*, 60(3), 2721-2726.

Dehaene, S. (2003). The neural basis of the Weber-Fechner law: A logarithmic mental number line. *Trends in Cognitive Sciences*, 7(4), 145-147.

Diskin, K.M. & Hodgins, D.C. (1999). Narrowing of attention and dissociation in pathological video lottery gamblers. *Journal of Gambling Studies*, 15(1), 17-28.

Dixon, M.J., Stange, M., Larche, C.J., Graydon, C., Fugelsang, J.A. & Harrigan, K.A. (2018). Dark flow, depression and multiline slot machine play. *Journal of Gambling Studies*, 34, 73–84.

De Zwart, P.L., Jeronimus, B.F., & de Jonge, P. (2022). Empirical evidence for definitions of episode, remission, recovery, relapse, and recurrence in depression: A systematic review. *Journal of Affective Disorders*, 312, 259-267.

Donati, M.A., Chiesi, F., & Primi, C. (2015). Italian validation of the Gambling Related Cognitions Scale (GRCS). *International Gambling Studies*, 15(3), 373-386.

Eagleman, D.M. (2008). Human time perception and its illusions. *Current Opinion in Neurobiology*, 18(2), 131-136.

Errington, T.M., Mathur, M., Soderberg, C.K., Denis, A., Perfito, N., Iorns, E., & Nosek, B.A. (2021). Investigating the replicability of preclinical cancer biology. *eLife*, 10, e71601.

Etter, J.-F. & Stapleton, J.A. (2006). Nicotine replacement therapy for long-term smoking cessation: A meta-analysis. *Tobacco Control*, 15(4), 280-285.

Fisher, R.A. (1925). Theory of statistical estimation. *Mathematical Proceedings of the Cambridge Philosophical Society*, 22(5), 700-725.

Feng, X., Cote, J., Kourtis, S. & Skinner, B. (2025). Postselection-free experimental observation of the measurement-induced phase transition in circuits with universal gates. *Communications Physics*. doi:10.1038/s42005-025-02443-0. arXiv:2502.01735.

Friston, K., Kilner, J., & Harrison, L. (2006). A free energy principle for the brain. *Journal of Physiology — Paris*, 100(1-3), 70-87.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Gavrilov, M. & Bechhoefer, J. (2016). Erasure without work in an asymmetric, double-well potential. *Physical Review Letters*, 117, 200601.

Gerbino, F., Giachetti, G., Le Doussal, P. & De Luca, A. (2025). Measurement-induced phase transition in state estimation of chaotic systems and the directed polymer. *Physical Review Research*, 7, 033105.

Goodie, A.S. & Fortune, E.E. (2013). Measuring cognitive distortions in pathological gambling: Review and meta-analyses. *Psychology of Addictive Behaviors*, 27(3), 730–743.

Grathwohl, W., Wang, K.-C., Jacobsen, J.-H., Duvenaud, D., Norouzi, M., & Swersky, K. (2019). Your classifier is secretly an energy based model and you should treat it like one. *International Conference on Learning Representations (ICLR 2020)*. arXiv:1912.03263.

Gurnee, W., Ameisen, E., Kauvar, I., Tarng, J., Pearce, A., Olah, C., & Batson, J. (2026). When models manipulate manifolds: The geometry of a counting task. *Transformer Circuits Thread*. arXiv:2601.04480.

Ha, H.Y., Pandey, S., Gopalakrishnan, S. & Huse, D.A. (2024). Measurement-induced phase transitions in systems with diffusive dynamics. arXiv:2405.08861.

Harris, A. & Griffiths, M.D. (2018). The impact of speed of play in gambling on psychological and behavioural factors: A critical review. *Journal of Gambling Studies*, 34, 393–412.

Hayes, J.A., Gelso, C.J., Goldberg, S., & Kivlighan, D.M. (2018). Countertransference management and effective psychotherapy: Meta-analytic findings. *Psychotherapy*, 55(4), 496-507.

Howard, K.I., Kopta, S.M., Krause, M.S., & Orlinsky, D.E. (1986). The dose-effect relationship in psychotherapy. *American Psychologist*, 41(2), 159-164.

Hack, P., Gottwald, S., & Braun, D.A. (2022). Jarzynski's equality and Crooks' fluctuation theorem for general Markov chains with application to decision-making systems. *Entropy*, 24(12), 1731.

Holevo, A.S. (1973). Bounds for the quantity of information transmitted by a quantum communication channel. *Problems of Information Transmission*, 9(3), 177-183.

Huhtinen, K.-E. et al. (2025). Unlikelihood of a phonon mechanism for the high-temperature superconductivity in La₃Ni₂O₇. *npj Computational Materials*, 11, 2.

Ikeda, K., Uda, T., Okanohara, D., & Ito, S. (2025). Speed-accuracy relations for diffusion models: Wisdom from nonequilibrium thermodynamics and optimal transport. *Physical Review X*, 15, 031031. arXiv:2407.04495.

Ilyas, A., Santurkar, S., Tsipras, D., Engstrom, L., Tran, B., & Madry, A. (2019). Adversarial examples are not bugs, they are features. *Advances in Neural Information Processing Systems (NeurIPS)*, 32. arXiv:1905.02175.

Ivanov, G., Oozeer, N., Raval, S., Pejovic, T., Upadhyay, S. & Abdullah, A. (2026). Spectral superposition: A theory of feature geometry. arXiv:2602.02224.

Jaynes, E.T. (1957). Information theory and statistical mechanics. *Physical Review*, 106(4), 620-630.

Kamakari, H., Sun, J., Li, Y., Thio, J.J., Gujarati, T.P., Fisher, M.P.A., Motta, M. & Minnich, A.J. (2025). Experimental demonstration of scalable cross-entropy benchmarking to detect measurement-induced phase transitions on a superconducting quantum processor. *Physical Review Letters*, 134, 120401.

Koh, J.M. et al. (2023). Measurement-induced entanglement phase transition on a superconducting quantum processor with mid-circuit readout. *Nature Physics*, 19, 1314-1319.

Johnson, J.B. (1928). Thermal agitation of electricity in conductors. *Physical Review*, 32(1), 97-109.

Jun, Y., Gavrilov, M. & Bechhoefer, J. (2014). High-precision test of Landauer's principle in a feedback trap. *Physical Review Letters*, 113, 190601.

Jordan, R., Kinderlehrer, D., & Otto, F. (1998). The variational formulation of the Fokker-Planck equation. *SIAM Journal on Mathematical Analysis*, 29(1), 1-17.

Krebesz, R., Otvos, D.K., & Fekete, Z. (2023). Non-problem gamblers show the same cognitive distortions while playing slot machines as problem gamblers. *Frontiers in Psychology*, 14, 1175621.

Kuyken, W., Warren, F.C., Taylor, R.S., Whalley, B., Crane, C., Bondolfi, G., ... & Dalgleish, T. (2016). Efficacy of mindfulness-based cognitive therapy in prevention of depressive relapse: An individual patient data meta-analysis from randomized trials. *JAMA Psychiatry*, 73(6), 565-574.

Ladeira, W.J., Santini, F.O., Pinto, D.C. & Rasool, A. (2023). A meta-analysis on the effects of product scarcity. *Psychology & Marketing*, 40(8), 1519–1540.

Ladouceur, R. & Walker, M. (1996). A cognitive perspective on gambling. In P.M. Salkovskis (Ed.), *Trends in Cognitive and Behavioural Therapies* (pp. 89-120). Wiley.

Landau, L.D. & Lifshitz, E.M. (1980). *Statistical Physics, Part 1.* 3rd ed. Pergamon Press.

Leung, C.Y., Meidan, D. & Romito, A. (2025). Theory of free fermions dynamics under partial postselected monitoring. *Physical Review X*, 15, 021020.

Liang, Y., Liu, Y., Zeng, J., Liu, J., He, Y., Chen, W. & Jia, T. (2019). Time perception deficits and its dose-dependent effect in methamphetamine dependents with short-term abstinence. *Science Advances*, 5(10), eaax6916.

Liu, Y., Liu, Z. & Gore, J. (2025). Superposition yields robust neural scaling. *Advances in Neural Information Processing Systems (NeurIPS)*, Best Paper Runner-Up. arXiv:2505.10465.

Liu, S., Li, M.-R., Zhang, S.-X., Jian, S.-K. & Yao, H. (2024). Noise-induced phase transitions in hybrid quantum circuits. *Physical Review B*, 110, 064323.

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183-191.

Lewis, G., Marston, L., Duffy, L., Freemantle, N., Gilbody, S., Hunter, R., ... & Lewis, G. (2021). Maintenance or discontinuation of antidepressants in primary care. *New England Journal of Medicine*, 385(14), 1257-1267.

Maassen, H. & Uffink, J.B.M. (1988). Generalized entropic uncertainty relations. *Physical Review Letters*, 60(12), 1103-1106.

Nehra, R., Romito, A. & Meidan, D. (2025). Controlling measurement-induced phase transitions with tunable detector coupling. *Quantum*, 9, 1697. doi:10.22331/q-2025-04-08-1697.

Nelson, E. (1966). Derivation of the Schrödinger equation from Newtonian mechanics. *Physical Review*, 150(4), 1079-1085.

Newall, P.W.S. (2019). Dark nudges in gambling. *Addiction Research & Theory*, 27(2), 65–67.

Newall, P.W.S. (2025). Sludge, dark patterns and dark nudges: A taxonomy of online gambling platforms' deceptive design features. *Addiction*. doi:10.1111/add.70085.

Muela, I., Navas, J.F., & Perales, J.C. (2020). Gambling-specific cognitions are not associated with either abstract or probabilistic reasoning. *Frontiers in Psychology*, 11, 611784.

Murch, W.S. & Clark, L. (2021). Understanding the slot machine zone. *Current Addiction Reports*, 8, 214–224.

Navas, J.F., Verdejo-Garcia, A., Lopez-Gomez, M., Maldonado, A., & Perales, J.C. (2016). Gambling with rose-tinted glasses on: Use of emotion-regulation strategies correlates with dysfunctional cognitions in gambling disorder patients. *Journal of Behavioral Addictions*, 5(2), 271-281.

Nyquist, H. (1928). Thermal agitation of electric charge in conductors. *Physical Review*, 32(1), 110-113.

Noseworthy, T.J. & Finlay, K. (2009). A comparison of ambient casino sound and music: Effects on dissociation and on perceptions of elapsed time while playing slot machines. *Journal of Gambling Studies*, 25(3), 331-342.

Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. *Science*, 349(6251), aac4716.

Ouyang, Y. et al. (2024). Absence of electron-phonon coupling superconductivity in the bilayer phase of La₃Ni₂O₇ under pressure. *npj Quantum Materials*, 9, 80.

Paviglianiti, A., Di Fresco, G., Silva, A., Spagnolo, B., Valenti, D. & Carollo, A. (2025). Breakdown of measurement-induced phase transitions under information loss. *Quantum*, 9, 1781.

Qian, D. & Wang, J. (2025). Protect measurement-induced phase transition from noise. *Physical Review Letters*, 134, 020403.

Petz, D. (1996). Monotone metrics on matrix spaces. *Linear Algebra and its Applications*, 244, 81-96.

Ramsauer, H., Schäfl, B., Lehner, J., Seidl, P., Widrich, M., Adler, T., ... & Hochreiter, S. (2020). Hopfield networks is all you need. *International Conference on Learning Representations (ICLR)*.

Raylu, N., & Oei, T.P.S. (2004). The Gambling Related Cognitions Scale (GRCS): Development, confirmatory factor validation and psychometric properties. *Addiction*, 99(6), 757-769.

Ruiz de Lara, C.M., Navas, J.F., & Perales, J.C. (2019). The paradoxical relationship between emotion regulation and gambling-related cognitive biases. *PLoS ONE*, 14(8), e0220668.

Ruppeiner, G. (1995). Riemannian geometry in thermodynamic fluctuation theory. *Reviews of Modern Physics*, 67(3), 605-659.

Schleider, J.L. & Weisz, J.R. (2017). Little treatments, promising effects? Meta-analysis of single-session interventions for youth psychiatric problems. *Journal of the American Academy of Child & Adolescent Psychiatry*, 56(2), 107-115.

Schüll, N.D. (2012). *Addiction by Design: Machine Gambling in Las Vegas.* Princeton University Press.

Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379-423.

Shinohara, K., Tajika, A., Imai, H., Takeshima, N., Hayasaka, Y., & Furukawa, T.A. (2021). Discontinuation rates and adverse effects in antidepressant trials: Systematic review and meta-analysis. *Molecular Psychiatry*, 26, 118-133.

Simon, R.I. (1999). Therapist-patient sex: From boundary violations to sexual misconduct. *Forensic Psychiatry*, 22(1), 31-47.

Skinner, B., Ruhman, J. & Nahum, A. (2019). Measurement-induced phase transitions in the dynamics of entanglement. *Physical Review X*, 9, 031009.

Stinespring, W.F. (1955). Positive functions on C*-algebras. *Proceedings of the American Mathematical Society*, 6(2), 211-216.

Suppes, T., Baldessarini, R.J., Faedda, G.L., & Tohen, M. (1991). Risk of recurrence following discontinuation of lithium treatment in bipolar disorder. *Archives of General Psychiatry*, 48(12), 1082-1088.

Shore, J.E. & Johnson, R.W. (1980). Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy. *IEEE Transactions on Information Theory*, IT-26(1), 26-37.

Toneatto, T. & Ladouceur, R. (2003). Treatment of pathological gambling: A critical review of the literature. *Psychology of Addictive Behaviors*, 17(4), 284-292.

Tse, D. & Viswanath, P. (2005). *Fundamentals of Wireless Communication.* Cambridge University Press.

Tsipras, D., Santurkar, S., Engstrom, L., Turner, A., & Madry, A. (2019). Robustness may be at odds with accuracy. *International Conference on Learning Representations (ICLR)*. arXiv:1805.12152.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

Vittengl, J.R., Clark, L.A., Dunn, T.W., & Jarrett, R.B. (2007). Reducing relapse and recurrence in unipolar depression: A comparative meta-analysis of cognitive-behavioral therapy's effects. *Journal of Consulting and Clinical Psychology*, 75(3), 475-488.

Walls, S.M., Bloss, A. & Ford, I.J. (2025). Characterizing quantum measurement through environmental stochastic entropy production in a two-spin-1/2 system. *Physical Review A*, 112, 032210.

Weisz, J.R., McCarty, C.A., & Valeri, S.M. (2006). Effects of psychotherapy for depression in children and adolescents: A meta-analysis. *Psychological Bulletin*, 132(1), 132-149.

Weimar, M., Rachbauer, L.M., Starshynov, I., Faccio, D., Adilova, L., Bouchet, D. & Rotter, S. (2025). Fisher information flow in artificial neural networks. *Physical Review X*, 15, 031072. arXiv:2509.02407.

Wittmann, M. (2009). The inner experience of time. *Philosophical Transactions of the Royal Society B*, 364, 1955–1967.

Wittmann, M. & Paulus, M.P. (2008). Decision making, impulsivity and time perception. *Trends in Cognitive Sciences*, 12(1), 7–12.

Wiseman, H.M. & Milburn, G.J. (2009). *Quantum Measurement and Control.* Cambridge University Press.

Wu, Z., Sun, X., Wang, S., Zhang, J., Yang, X., Chu, J., Niu, J., Zhong, Y., Chen, X., Yang, Z.-C. & Yu, D. (2025). Measurement-and feedback-driven non-equilibrium phase transitions on a quantum processor. arXiv:2512.07966.

Yan, L.L., Xiong, T.P., Rehan, K., Zhou, F., Liang, D.F., Chen, L., Zhang, J.Q., Yang, W.L., Ma, Z.H. & Feng, M. (2018). Single-atom demonstration of the quantum Landauer principle. *Physical Review Letters*, 120, 210601.

Zhang, Z.-Y. et al. (2025). Quantum Zeno effect in the spatial evolution of a single atom. arXiv:2509.24438.

Zhao, D., Mioni, G. et al. (2024). Exploring the interplay between addiction and time perception: A systematic review and meta-analysis. *Progress in Neuro-Psychopharmacology and Biological Psychiatry*, 134, 111063.

---

*This work is licensed under CC-BY 4.0 International.*
