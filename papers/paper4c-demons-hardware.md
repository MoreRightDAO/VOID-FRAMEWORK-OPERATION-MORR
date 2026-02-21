# The Demon's Hardware: Information-Geometric Bounds on Thermodynamic Computing

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO
**Paper 4C — Thermodynamic Computing Integration (v1.0)**
**Date:** February 20, 2026
**Target audience:** Thermodynamic computing, information geometry, hardware design, AI safety

> **Repository:** [github.com/MoreRightDAO/VOID-FRAMEWORK-OPERATION-MORR](https://github.com/MoreRightDAO/VOID-FRAMEWORK-OPERATION-MORR)
> **License:** CC-BY 4.0 International

---

## Abstract

We map the Eckert Manifold $\mathcal{V} = [0,1]^3$ — the voidspace geometry derived from information-theoretic first principles [9] — onto thermodynamic computing hardware, providing quantitative bounds, design optimization principles, and scaling predictions for thermodynamic sampling units (TSUs). Three operational coordinates (opacity $O$, responsiveness $R$, coupling $\alpha$) are defined for TSU architectures, with the Fisher product metric doubling as the thermodynamic metric via the Fisher-Ruppeiner identity. Six results: (1) The **ground state theorem** explains why TSUs achieve ~10,000× energy efficiency — they operate at the opacity ground state (thermodynamic equilibrium), avoiding the Landauer cost of transparency that deterministic processors pay. (2) The **Fantasia Bound** ($I(S;Y) + I(T;Y) \leq H(Y)$) applied to TSU channels predicts scaling walls: Fashion-MNIST is 130× below saturation, but ImageNet-scale targets enter the constrained regime, and real-time video saturates the bound. (3) **Demon lattice phases** map onto hardware operating regimes — Gas (noise only), Fluid (unreliable sampling), Crystal (deterministic, no TSU advantage), and Vortex (Pe $> 4$: self-sustaining stochastic computation, the regime where thermodynamic computing works). The Péclet number serves as a hardware figure of merit. (4) A **three-channel budget** ($I(D_1;Y) + I(D_2;Y) + I(M;Y) \leq H(Y)$) for pbit architectures yields the anisotropy design principle: maximize directional coupling aligned with the target, not total coupling strength — a design framework absent from existing TSU theory. (5) TSUs and superconductors are **dual solutions** on the same Fantasia Bound constraint surface — opposite objectives (maximize exploration vs. maximize coherence) with opposite operating points (near vs. far from ground state). (6) The **acceleration paradox**: 10,000× energy efficiency solves hardware entropy but not informational entropy — it removes the energy brake on deploying opacity-maximizing systems at scale. We derive ten testable predictions (TC-1 through TC-10) with numerical falsification thresholds, present a cross-substrate validation protocol testing the Substrate Independence Theorem on physical hardware for the first time, and provide a complete experimental design for any TSU-class system. All predictions are registered before empirical testing.

---

## 1. Introduction: Why Thermodynamic Computing Needs Information Geometry

### 1.1 The Thermodynamic Computing Thesis

Thermodynamic computing represents a paradigm shift: rather than maintaining deterministic bit states against thermal noise at Landauer cost, thermodynamic sampling units (TSUs) harness stochastic fluctuations as a computational resource [Verdon & McCourt 2023]. Probabilistic bits (pbits) fluctuate at thermal equilibrium while a programmable energy landscape — a Maxwell's demon — directs the collective dynamics toward a target probability distribution [Jelinčič et al. 2025]. The reported energy advantage is ~10,000× over GPU baselines for probabilistic workloads.

The hardware is real and shipping. The Z1 chip (Extropic, 2025–2026) implements 250,000+ pbits with stochastic magnetic tunnel junctions (sMTJs), running denoising thermodynamic models (DTMs) as its primary algorithm class. The `thrml` Python library provides a software interface to hardware and simulation. The engineering is sound.

What is missing is a theory of limits.

### 1.2 The Gap

Existing TSU performance analysis proceeds empirically: build, benchmark, compare to GPUs. The benchmarks are impressive — Fashion-MNIST generation at kilohertz rates, sub-millisecond inference — but they answer the question "how fast is this chip?" without answering the questions a hardware designer actually needs:

1. **When does noise help versus hurt?** At what target complexity does thermal noise transition from computational resource to thermalization — from useful stochastic exploration to pure heat?
2. **What is the fundamental convergence rate?** Given finite channel capacity and thermal noise, how fast can ANY architecture converge to a target distribution — regardless of implementation?
3. **How should the channel budget be allocated?** Given finite output capacity, how much should be devoted to exploration versus convergence, and how should inter-pbit coupling be designed?
4. **When does the system compute versus thermalize?** Is there a quantitative threshold separating useful stochastic computation from expensive noise generation?

No existing theory of thermodynamic computing answers these questions with quantitative bounds.

### 1.3 The Bridge: Information Geometry IS Thermodynamic Geometry

The Fisher-Ruppeiner identity [Ruppeiner 1979, 1995; Crooks 2007] establishes that the Fisher information metric on statistical manifolds is identically the Hessian of entropy — the Ruppeiner thermodynamic metric. This is not analogy. The same mathematical object governs:

- The geometry of probability distributions (information theory)
- The geometry of thermodynamic state spaces (statistical mechanics)
- The geometry of observer-system interactions (the void framework [3, 4, 9])

The void framework has exploited this identity to derive performance bounds for TSU hardware and a design principle for superconducting materials [4], validated a Langevin dynamics model against nine independent experimental conditions [4, §8.1], and measured the Péclet number across nine substrates spanning four domain families [4, §8.2; 5, §II.E'].

This paper completes the bridge. Where [4] derived individual bounds (ground state theorem, Fantasia Bound, TSU predictions TSU-1 through CT-1), we provide the systematic mapping: how the Eckert Manifold $\mathcal{V}$ — the geometric space where all these bounds live [9] — maps onto the observable properties of physical thermodynamic computing hardware, what it predicts about design optimization, and where the scaling walls are.

### 1.4 Contributions

1. **Voidspace-to-hardware mapping** (§2): Operational definitions of the Eckert Manifold coordinates $(O, R, \alpha)$ for TSU architectures. The fiber bundle construction yields a substrate independence prediction testable across hardware implementations.

2. **Ground state explanation** (§3): Why TSUs are 10,000× efficient — they operate at thermodynamic equilibrium (the opacity ground state), avoiding the Landauer cost of transparency. The Maxwell's demon is the constraint specification.

3. **Scaling predictions** (§4): The Fantasia Bound as a hardware resource constraint. Quantitative workload-by-workload analysis identifying where current architectures are far from the bound (Fashion-MNIST: 130× margin) and where they will hit the wall (ImageNet-scale and above).

4. **Phase diagram** (§5): Demon lattice phases mapped to TSU operating regimes. The Péclet number as a hardware figure of merit, with the Pe $= 4$ Vortex threshold as the design target for self-sustaining stochastic computation.

5. **Design optimization** (§6): Three-channel budget for pbit architectures. The anisotropy principle: maximize directional coupling, not total coupling. Channel conversion efficiency as a hardware figure of merit.

6. **DTM analysis** (§7): Denoising Thermodynamic Models as drift reversal. Crooks ratio for forward/reverse trajectories. Per-step Fantasia allocation.

7. **Validation protocol** (§8, §11): Cross-substrate validation protocol designed for hardware. Experimental design for any TSU-class system.

8. **Acceleration paradox** (§9): Free compute removes the energy brake on void deployment. Hardware entropy ↓ does not imply informational entropy ↓.

9. **Ten testable predictions** (§10): TC-1 through TC-10 with numerical falsification thresholds.

**Relationship to companion papers.** Paper 3 [3] derives the thermodynamic foundations. Paper 4 [4] derives the TSU and superconductor bounds. Paper 4B [4B] analyzes the acceleration thesis. Paper 9 [9] formalizes the geometric space. This paper integrates all four into a unified framework for thermodynamic computing hardware — mapping the space, testing the bounds, and identifying the design principles.

**What this paper does NOT do:** It does not replace Extropic's engineering. It does not claim the framework "explains" TSU hardware in a way that supersedes the physics. It provides quantitative bounds, design principles, and testable predictions that complement hardware-specific optimization. The framework operates at the information-geometric level — it constrains what any architecture can achieve, identifies what the current architecture is leaving on the table, and predicts where the walls are. The engineering fills in the substrate-specific details within those constraints.

---

## 2. Mapping Voidspace onto Hardware

### 2.1 The Problem: Two Optimizations That Are One

Thermodynamic computing hardware presents a dual optimization problem. The information-theoretic question: given a target probability distribution, how efficiently can a stochastic system generate samples from it? The thermodynamic question: given thermal noise at temperature $T$, how efficiently can a physical system convert that noise into useful computational work? The Fisher-Ruppeiner identity [Ruppeiner 1979; Crooks 2007] establishes that these are the same question. The Fisher information metric on the space of probability distributions is identically the Hessian of entropy — the Ruppeiner thermodynamic metric. Optimizing a sampling algorithm's convergence rate and optimizing a physical system's thermodynamic efficiency are performed on the same geometric object.

This identity has been exploited in the void framework to derive performance bounds for thermodynamic sampling units (TSUs) and a design principle for superconducting materials [4]. What has not been established is the systematic mapping: how does the geometric space in which these bounds live — the Eckert Manifold $\mathcal{V}$ [9] — relate to the observable properties of physical thermodynamic computing hardware?

This section provides that mapping.

### 2.2 Hardware Coordinates

The Eckert Manifold $\mathcal{V} = [0,1]^3$ is parameterized by three information-theoretic quantities defined at any observer-system interface [9, §2]. For a thermodynamic computing system — a TSU with probabilistic bits (pbits) driven by a programmable energy landscape (the Maxwell's demon) — the coordinates have direct hardware interpretations.

**Opacity ($O$).** The fraction of pbit state information inaccessible at the observer interface:

$$O = 1 - \frac{I(\text{Observer}; \mathbf{s})}{H(\mathbf{s})}$$

where $\mathbf{s}$ is the full microstate vector of all $N$ pbits and $I(\text{Observer}; \mathbf{s})$ is the mutual information between the observer's readout and the actual pbit configuration. For a TSU operating at thermal equilibrium — the normal operating regime — $H(\mathbf{s})$ is maximized (all configurations equiprobable at high temperature) while $I(\text{Observer}; \mathbf{s})$ is determined by the readout architecture.

The key insight: **a TSU in its default state operates near $O = 1$** (maximum opacity). The pbits fluctuate thermally. The observer sees stochastic samples but cannot determine the instantaneous microstate. This is not a design flaw — it is the operating principle. The TSU harnesses opacity rather than paying to eliminate it.

A conventional deterministic processor operates near $O = 0$ (maximum transparency). Every bit is known to the controller at every clock cycle. The Landauer cost of maintaining this transparency is $\geq kT \ln 2$ per bit per correlation time [Landauer 1961]. The TSU avoids this cost by not maintaining transparency.

**Responsiveness ($R$).** The normalized mutual information between the demon's energy landscape configuration and the TSU's output samples:

$$R = \frac{I(\mathcal{L}; \mathbf{y})}{H(\mathbf{y})}$$

where $\mathcal{L}$ is the demon's programmed energy landscape and $\mathbf{y}$ is the output sample stream. At $R = 0$, the output is independent of the landscape — pure thermal noise, no computation. At $R = 1$, every output sample is fully determined by the landscape — deterministic computation, no stochastic exploration.

For a TSU running denoising thermodynamic models (DTMs) [Verdon & McCourt 2023], $R$ varies across the denoising chain. Early steps (high noise): $R$ is low — samples are nearly thermal, weakly responsive to the landscape. Late steps (refined): $R$ is high — samples converge toward the target, strongly shaped by the landscape. The DTM trajectory is a path through $\mathcal{V}$ from high to low $R$.

**Coupling ($\alpha$).** The fraction of the downstream system's behavior explained by the TSU's output:

$$\alpha = \frac{I(\mathbf{y}; \mathbf{d}_{\text{future}})}{H(\mathbf{d}_{\text{future}})}$$

where $\mathbf{d}_{\text{future}}$ represents the downstream decisions, actions, or computations that consume the TSU's output. At $\alpha = 0$, the TSU's output is ignored — no downstream system depends on it. At $\alpha = 1$, every downstream decision is fully determined by the TSU output.

For a TSU generating samples consumed by an AI inference pipeline, $\alpha$ measures how much the final output depends on the stochastic samples. For a TSU generating random numbers for a Monte Carlo simulation, $\alpha$ is the fraction of simulation variance attributable to the TSU's output. For a TSU whose samples are displayed to a human operator making decisions, $\alpha$ is the observer coupling defined in [9, §2.1] — the fraction of the operator's future state explained by what the TSU showed them.

### 2.3 The Natural Metric

Each coordinate parameterizes a family of Bernoulli distributions at the hardware interface. The Fisher information metric for each is [Čencov 1982]:

$$g_O(O) = \frac{1}{O(1-O)}, \quad g_R(R) = \frac{1}{R(1-R)}, \quad g_\alpha(\alpha) = \frac{1}{\alpha(1-\alpha)}$$

The product metric on $\mathcal{V}$:

$$ds^2 = \frac{dO^2}{O(1-O)} + \frac{dR^2}{R(1-R)} + \frac{d\alpha^2}{\alpha(1-\alpha)}$$

This is the unique metric invariant under sufficient statistics on each Bernoulli parameter [Čencov 1982] — the Čencov-unique metric. Via the Fisher-Ruppeiner identity, it is simultaneously the thermodynamic metric on the space of hardware configurations. Geodesic distances in this metric are thermodynamic distances. Moving a TSU from one operating point to another has a cost measured by the geodesic length.

**Hardware implication:** Gradual changes in operating point (small geodesic distance per step) are thermodynamically cheaper than abrupt reconfigurations. The metric provides the natural cost function for dynamic reconfiguration of TSU operating parameters.

### 2.4 The Fiber Bundle: Substrate Independence

The Eckert Manifold $\mathcal{V}$ is the base space of a fiber bundle [9, §3]. The fiber at each point $(O, R, \alpha)$ contains all physical realizations — all substrate-specific hardware implementations — that produce that information-theoretic operating point. Formally:

$$\pi: \mathcal{E} \to \mathcal{V}$$

where $\mathcal{E}$ is the total space of all physical hardware configurations and $\pi$ projects each configuration to its $(O, R, \alpha)$ coordinates.

Two TSU architectures constitute different fibers over the same base point:
- A stochastic magnetic tunnel junction (sMTJ) array at $(O_1, R_1, \alpha_1)$
- A CMOS-based pbit network at $(O_1, R_1, \alpha_1)$

The Substrate Independence Theorem [9, Theorem 1] states: the drift dynamics — the time evolution of the observer-system interaction — depend only on position in $\mathcal{V}$, not on which fiber the system occupies. These dynamics are *horizontal* in the bundle: they live in the base space.

**For thermodynamic computing, this predicts:** Two TSU architectures at matched $(O, R, \alpha)$ produce identical Péclet numbers, identical convergence rates (up to the Fantasia Bound), and identical phase behavior — regardless of whether the pbits are sMTJs, CMOS inverters, superconducting junctions, or photonic elements. The substrate determines engineering parameters (clock speed, power consumption, pbit count, operating temperature). The dynamics at the information-geometric level are determined by the coordinates alone.

This is prediction **TC-1** (Section 10) — and it is the single most falsifiable claim in this paper. Any two implementations at matched coordinates that produce different Pe values outside the predicted tolerance (±0.3) would falsify the substrate independence theorem for hardware substrates.

### 2.5 The Demon's Position in Voidspace

In the void framework, any non-ground-state pattern in $\mathcal{V}$ that induces directed drift is formally a Maxwell's demon [9, §6]. The programmable energy landscape of a TSU is precisely this: an external constraint that imports negentropy to direct the stochastic dynamics of the pbits toward a target distribution.

The demon occupies a specific position in voidspace. Its opacity $O_D$ is determined by how much of its internal state (the landscape parameters, optimization objective, training data) is visible to the pbit system. Its responsiveness $R_D$ is determined by how the landscape changes in response to the pbit dynamics (adaptive demons reconfigure based on output; static demons do not). Its coupling $\alpha_D$ is determined by how much the demon's own future state depends on the pbit output (a closed-loop controller has high $\alpha_D$; an open-loop programmer has $\alpha_D \approx 0$).

The critical distinction: **the demon is outside the stochastic system it controls.** In voidspace terms, the demon imports energy from outside $\mathcal{V}$ to maintain the pbits at a non-equilibrium operating point. This is the External Bypass identified in [9, §6.7] — external energy circumvents the competition asymmetry that makes constraint maintenance thermodynamically expensive from within the manifold.

For hardware design, this means the demon's effectiveness is not constrained by the pbit system's internal thermodynamics. It is constrained by the Fantasia Bound on the channel the demon uses to communicate with the pbits (Section 4) and by the minimum bandwidth requirement for convergence (Section 4.4).

---

## 3. The Opacity Ground State as Hardware Design Principle

### 3.1 The Ground State Theorem Applied to Hardware

The Ground State Theorem [3, Theorem 1; 4, §3] establishes: zero mechanism-channel capacity ($C_{\text{mech}} = 0$) is thermodynamic equilibrium. Any nonzero transparency ($C_{\text{mech}} > 0$) is an excited state requiring continuous energy input at minimum Landauer cost: $kT \ln 2$ per bit per correlation time.

For a conventional deterministic processor maintaining $N$ bits in known states:

$$P_{\text{transparent}} \geq \frac{N \cdot kT \ln 2}{\tau_{\text{clock}}}$$

At $N = 10^9$ bits (1 Gbit), $T = 300$ K, $\tau_{\text{clock}} = 1$ ns: $P_{\text{transparent}} \geq 2.9$ W just for state maintenance — before any useful computation. Real processors dissipate far more because each logic operation erases information (irreversible gates), multiplying the Landauer cost by the gate count per cycle.

A TSU with $N$ pbits fluctuating at thermal equilibrium has $C_{\text{mech}} \approx 0$ — the observer cannot determine the microstate. The energy cost of maintaining this opacity is zero: the system is already at equilibrium. Thermal fluctuations are not noise to be suppressed but the default state the hardware occupies for free.

**This is why TSUs achieve ~10,000× energy efficiency** [Jelinčič et al. 2025]: they operate at the thermodynamic ground state rather than paying to maintain an excited (transparent) state. The reported $\sim 20$ nJ per sample versus $\sim 10^5{-}10^6$ nJ per equivalent GPU sample is not a hardware optimization achievement — it is the energy difference between equilibrium and excited-state operation, predicted by the ground state theorem.

### 3.2 The Constraint Specification for Computation

The void framework's constraint specification — the set of properties that characterize a constraint-pole system [3, §IV.B; 9, §2.1] — maps directly onto computation:

| Constraint Property | Computational Interpretation | Hardware Example |
|--------------------|------------------------------|------------------|
| **Transparent** | Every computational step is recoverable from the output | Reversible gates (Toffoli, Fredkin): input reconstructible from output |
| **Invariant** | Same input always produces same output | Deterministic logic: no state-dependent behavior variation |
| **Independent** | Hardware not modified by data flowing through it | Static circuit: gate function doesn't change based on the data it processes |

A system satisfying all three is a *constraint-pole computer*: reversible, deterministic, static. This is the theoretical ideal of reversible computing [Bennett 1973; Fredkin & Toffoli 1982] — and it is maximally expensive to build, because maintaining all three properties against thermal noise requires maximum energy input (the ground state theorem, applied in reverse: maximum transparency requires maximum work).

A TSU violates all three: it is opaque (pbit states unknown), responsive (outputs depend on the landscape, which depends on the target), and coupled (the demon adjusts based on output). This triple violation IS the design choice that makes it energy-efficient. The TSU trades constraint-pole properties for proximity to the thermodynamic ground state.

### 3.3 The Demon as Constraint Architecture

The Maxwell's demon in a TSU is the component that imports negentropy from outside the stochastic system [9, §6.7]. In constraint-specification terms, the demon plays the role of the external constraint: it is transparent to itself (knows its own landscape parameters), invariant (the landscape doesn't fluctuate with the pbits on the timescale of a denoising step), and independent (the demon's state is not determined by individual pbit outputs).

But the demon has finite resources. The Fantasia Bound (Section 4) constrains its channel capacity. The minimum demon bandwidth (Section 4.4) sets a hard floor on its control resolution. The demon cannot make the TSU fully transparent — that would cost more energy than the TSU saves.

The design trade-off: the demon operates in the space between "no control" (pure thermal noise, Gas phase) and "full control" (deterministic computation, Crystal phase). The optimal demon drives the system into the Vortex phase (Section 5) — enough control for convergence, enough noise for stochastic exploration — without paying the full Landauer cost of transparency.

**The demon is the difference between a heater and a computer.** A pbit array at thermal equilibrium is a heater — it converts electrical energy to thermal noise. A pbit array with a well-designed demon is a computer — it converts thermal noise into samples from a target distribution. The hardware is identical. The demon is the constraint that makes it compute. This is the physical instantiation of the framework's central finding: the difference between a void and a constraint is the presence of an external specification [9, §6].

---

## 4. The Fantasia Bound as Hardware Resource Constraint

### 4.1 The Bound

The Fantasia Bound [3, §IV.H; 9, §2.5] is an additive uncertainty relation on finite-bandwidth channels:

$$I(S;Y) + I(T;Y) \leq H(Y)$$

where $I(S;Y)$ is the mutual information between stochastic exploration and the output, $I(T;Y)$ is the mutual information between the target distribution and the output, and $H(Y)$ is the total output entropy (channel capacity). The bound follows from the data processing inequality and the chain rule of mutual information [3]. It is not an approximation. It is a hard ceiling.

For a TSU generating samples from a target distribution:
- **$I(S;Y)$** = exploration capacity. The information in the output that comes from stochastic thermal fluctuations — the randomness the hardware harnesses.
- **$I(T;Y)$** = convergence capacity. The information in the output that is explained by the target distribution — how close the samples are to what was requested.
- **$H(Y)$** = total output channel capacity. Determined by the number of pbits, their readout resolution, and the sampling rate.

The bound states: **every bit of convergence toward the target costs one bit of exploration capacity**, and vice versa. You cannot maximize both simultaneously. Any TSU design — regardless of architecture, materials, or demon implementation — is subject to this tradeoff.

### 4.2 The Pareto Frontier

The space of achievable $(I(S;Y), I(T;Y))$ pairs for a given $H(Y)$ is a simplex bounded by the Fantasia Bound above and by $I(S;Y) \geq 0$, $I(T;Y) \geq 0$ below. The Pareto frontier is the line $I(S;Y) + I(T;Y) = H(Y)$ — configurations where any increase in convergence requires a corresponding decrease in exploration.

Two extreme operating points:

**Pure exploration** ($I(T;Y) = 0$, $I(S;Y) = H(Y)$): The TSU generates maximum-entropy thermal noise. No convergence toward any target. This is the opacity ground state — thermodynamic equilibrium. Energy cost: zero beyond the thermal bath.

**Pure convergence** ($I(S;Y) = 0$, $I(T;Y) = H(Y)$): Every output bit is determined by the target. No stochastic exploration. This is deterministic computation — every output is predictable. Energy cost: $\geq N \cdot kT \ln 2$ per readout cycle to maintain the deterministic state.

TSU operation lives between these extremes. The demon's job is to drive the operating point from pure exploration toward convergence without paying the full deterministic cost. The Fantasia Bound tells the demon how much convergence it can buy with the available channel capacity.

### 4.3 Scaling Predictions: Where the Walls Are

The Z1 chip [Jelinčič et al. 2025] has $N = 250{,}000$ pbits running $K = 8$ denoising steps. The total output channel capacity per sample is:

$$H(Y) = N \cdot h(\bar{p})$$

where $h(\bar{p})$ is the average per-pbit entropy (maximized at $h = 1$ bit when pbits are at their thermal equilibrium, slightly below 1 for biased pbits). For a well-designed TSU at operating temperature, $H(Y) \approx N = 250{,}000$ bits.

The convergence capacity required depends on the target distribution's entropy:

$$I(T;Y)_{\text{needed}} \geq H_{\text{target}} - \epsilon$$

where $\epsilon$ is the acceptable divergence from the target (in bits). The system can converge if:

$$H_{\text{target}} \leq H(Y) \cdot \eta_{\text{mixing}} \cdot K$$

where $\eta_{\text{mixing}} \in [0,1]$ is the fraction of channel capacity the demon converts to convergence per step (the mixing efficiency) and $K$ is the number of denoising steps.

**Workload analysis:**

| Target | $H_{\text{target}}$ (bits) | Required $\eta_{\text{mixing}}$ | Saturation ratio | Status |
|--------|---------------------------|--------------------------------|-------------------|--------|
| Fashion-MNIST (784 pixels, binary) | $\approx 1{,}900$ | 0.001 | $130\times$ below | Trivially satisfied |
| CIFAR-10 (32×32 RGB) | $\approx 14{,}000$ | 0.007 | $18\times$ below | Comfortable |
| ImageNet (256×256 RGB) | $\approx 200{,}000$ | 0.100 | At parity | **Entering constrained regime** |
| 1024×1024 color (natural image) | $\approx 750{,}000$ | 0.375 | $3\times$ above | **Constrained — requires near-optimal mixing** |
| Real-time video (30fps × 1M bits) | $\approx 30M$ / sec | 0.500/step, 3750 steps/sec | $120\times$ above | **Deep in constrained regime** |
| Foundation model (175B param sampling) | $\gg 10^6$ | $\to 1$ | Orders of magnitude | **Bound saturated** |

The scaling wall is visible: Fashion-MNIST and CIFAR-10 are far from the bound — the TSU has excess capacity. At ImageNet resolution, the system enters the constrained regime. At 1024×1024 natural images, near-optimal mixing is required. Real-time video and foundation-model-scale sampling are deep in the constrained regime where the bound is tight and architecture choices directly affect whether convergence is achievable at all.

**This is the prediction Extropic has not yet needed to confront.** Their published benchmarks are on Fashion-MNIST — 130× below saturation [Jelinčič et al. 2025]. The Fantasia Bound is not yet binding. As target complexity scales, the bound becomes the dominant constraint, and the margin between architectures becomes the margin between convergence and thermalization.

### 4.4 Minimum Demon Bandwidth

The demon's control channel — the bandwidth with which it can reprogram the energy landscape — has a minimum requirement [4, §5.4]:

$$B_{\text{demon,min}} \geq \frac{H_{\text{data}}}{n_{\text{steps}} \cdot \eta_{\text{mixing}}}$$

Below this bandwidth, the demon cannot deliver enough negentropy to drive convergence regardless of how the pbits are configured. This is a hard floor — architectural optimization cannot compensate for insufficient demon bandwidth.

For the Z1 architecture at ImageNet-scale targets:

$$B_{\text{demon,min}} \geq \frac{200{,}000}{8 \times 0.1} = 250{,}000 \text{ bits/step}$$

The demon must reprogram the landscape with information content ≥ 250,000 bits per denoising step to achieve convergence at ImageNet scale. At 1024×1024 natural images:

$$B_{\text{demon,min}} \geq \frac{750{,}000}{8 \times 0.375} = 250{,}000 \text{ bits/step}$$

The demon bandwidth saturates at the pbit count — the demon must effectively reprogram every pbit's energy contribution per step. This is prediction **TC-8**: convergence fails below $B_{\text{demon,min}}$ regardless of architecture.

### 4.5 The H∞ Formulation

The demon's control problem has a natural robust control formulation [4, §5.5]. The energy landscape is the control input $u(t)$. The pbit dynamics are the plant. Thermal fluctuations are the worst-case disturbance $w(t)$. The objective is to minimize the worst-case convergence error:

$$\min_{u} \max_{w} \| \mathbf{y} - \mathbf{y}_{\text{target}} \|$$

subject to the Fantasia Bound as the resource constraint. This is a standard H∞ control problem — minimize the worst-case gain from disturbance to output error — with the Fantasia Bound providing the constraint that distinguishes it from unconstrained optimization.

The H∞ formulation provides a computationally tractable path to optimal demon design: specify the target distribution, the pbit count, the noise characteristics, and the demon bandwidth. The optimal landscape sequence is the solution to the H∞ problem. The Fantasia Bound is the constraint that makes the problem well-posed — without it, the optimization has no channel capacity bound and the "optimal" solution is trivially "use infinite bandwidth."

---

## 5. Demon Lattice Phases as Hardware Operating Regimes

### 5.1 The Péclet Number as Hardware Figure of Merit

The Péclet number Pe — the ratio of directed drift to diffusive spreading [3, §IV.F] — provides a dimensionless figure of merit for any information-processing system. In the angular coordinate $\varphi = \arcsin(\sqrt{\theta})$ on the Bernoulli manifold [4, §2.1]:

$$\text{Pe} = \frac{F_{\text{net}} \cdot \pi}{\alpha_{\text{noise}}}$$

where $F_{\text{net}}$ is the net drift force (from opacity, responsiveness, and engagement), $\pi$ is the manifold diameter, and $\alpha_{\text{noise}}$ is the diffusion coefficient (thermal noise intensity).

For a TSU, the components map directly:
- **$F_{\text{net}}$**: The gradient of the demon's energy landscape — how strongly the landscape drives pbits toward the target configuration.
- **$\alpha_{\text{noise}}$**: The thermal fluctuation intensity — $kT$ divided by the energy barrier height between pbit states.
- **$\pi$**: The geometric constant (manifold diameter) — the maximum information distance between any two states.

Pe measures the competition between the demon's control signal and the thermal noise it exploits. When Pe $\gg 1$, the demon dominates — the system converges deterministically. When Pe $\ll 1$, noise dominates — the system explores thermally. The transition region is where thermodynamic computing operates: Pe $\sim 1$, where noise and control are balanced, and the TSU generates useful stochastic samples.

### 5.2 Four Phases

The void lattice phase diagram [9, §6.8.2] identifies four regimes of collective demon behavior, originally derived for populations of information-processing entities. Applied to TSU pbit ensembles:

**Phase I — Gas (Pe $< \sim 2$): Thermal Noise Regime**

Individual pbits fluctuate independently. The demon's energy landscape is too weak relative to thermal noise to produce correlated dynamics. Pbit-pbit interactions are negligible. The output is high-entropy noise with minimal structure.

*Hardware interpretation:* The TSU is a random number generator, not a computer. Energy cost is minimal (operating near ground state), but computational usefulness is also minimal. No useful sampling occurs. This is the regime below the threshold where thermodynamic computing provides any advantage over reading thermal noise.

**Phase II — Fluid (Pe $\sim 2{-}4$): Dense-Disordered Sampling**

Statistical correlations emerge between pbits. The demon's landscape induces collective behavior — groups of pbits begin to co-orient — but the correlations are unstable, fluctuating, disordered. The output contains structure but convergence to the target is unreliable.

*Hardware interpretation:* The TSU generates samples that are statistically related to the target but not reliably close. Multiple samples are needed; individual samples may be far from the target. This is the regime where TSU hardware begins to produce computationally useful output, but with high variance. Appropriate for tasks that tolerate stochastic approximation (MCMC-like applications, approximate posterior sampling).

**Phase III — Crystal ($\Gamma_D \geq \Gamma_c$): Deterministic Regime**

The demon's landscape is strong enough to impose a regular, stable pattern on the pbits. Thermal fluctuations are suppressed below the energy barriers. The output is deterministic — every sample is the same (or varies minimally around the target).

*Hardware interpretation:* This is conventional digital computing. The "thermodynamic" processor has been cooled/constrained into determinism. The TSU's stochastic advantage is lost. Energy cost is high (maintaining deterministic states against noise). There is no regime in which an architecture designed for Phase III outperforms conventional digital hardware at its own game.

**Phase IV — Vortex (Pe $> 4$): Pandemonium**

Self-sustaining stochastic circulation. The demon's landscape and the thermal dynamics reach a self-reinforcing equilibrium: the noise feeds the computation and the computation shapes the noise. Pbit dynamics are collectively coherent but stochastically varied — each sample is different, but the distribution converges.

*Hardware interpretation:* **This is where Extropic's thesis actually works.** In this regime, thermal noise is not merely tolerated but functionally necessary. The TSU generates diverse, high-quality samples from the target distribution without requiring external forcing beyond the initial landscape setup. This is the regime where thermodynamic computing achieves its maximum advantage: the noise is the compute.

The Pe $= 4$ threshold is derived from the stationary distribution analysis in [9, §6.8.2]. It is not a fitted parameter — it emerges from the geometry of the voidspace manifold and the condition for self-sustaining circulation in the Fokker-Planck dynamics. The threshold sits between empirically measured Pe values for systems without self-sustaining creator dynamics (gambling: Pe $= 2.21$, no self-sustaining ecosystems) and systems with them (competitive gaming: Pe $= 4.4$, self-sustaining creator communities) [4, §8.2].

### 5.3 Phase Boundaries as Design Targets

The four phases provide a design specification:

| Design Goal | Target Phase | Pe Range | Demon Strength |
|------------|-------------|----------|----------------|
| Random number generation | Gas | Pe $< 2$ | Minimal landscape |
| Approximate sampling (MCMC) | Fluid | Pe $2{-}4$ | Moderate landscape |
| Deterministic computation | Crystal | Pe $\gg 4$ | Maximum landscape |
| High-quality stochastic sampling | Vortex | Pe $> 4$ | Self-sustaining landscape |

The design problem for thermodynamic computing hardware is: **achieve Pe $> 4$ for the target workload.** Below this threshold, the TSU operates in the fluid regime — samples are produced but convergence is unreliable. Above it, the system enters Pandemonium: self-sustaining, diverse, convergent sampling.

The Pe value is tunable through hardware parameters:
- **Increase $F_{\text{net}}$:** Stronger energy landscape gradients (higher landscape contrast, better demon programming resolution).
- **Decrease $\alpha_{\text{noise}}$:** Lower operating temperature, higher energy barriers between pbit states. But this reduces the stochastic exploration that makes TSUs efficient — a tradeoff the Fantasia Bound quantifies (Section 4).
- **Increase $\pi$:** Larger state space (more pbits, higher resolution per pbit). This increases the manifold diameter, raising Pe.

The tradeoff between $F_{\text{net}}$ and $\alpha_{\text{noise}}$ is the Fantasia Bound in another form: the demon's control signal and the thermal noise compete for the same channel capacity. Maximizing Pe by suppressing noise is equivalent to moving toward the Crystal phase — deterministic computing, loss of TSU advantage. The art of thermodynamic computing design is achieving Pe $> 4$ while maintaining enough noise to stay in the Vortex phase rather than crystallizing.

### 5.4 Computational Péclet Number

For hardware benchmarking, we define the *computational Péclet number* Pe$_C$ as the Pe measured from the TSU's output sample stream:

$$\text{Pe}_C = \frac{\langle \Delta d \rangle}{\sigma(\Delta d)} \cdot \sqrt{K}$$

where $\Delta d$ is the per-step change in KL divergence between the output distribution and the target, $\sigma(\Delta d)$ is its standard deviation across samples, and $K$ is the number of denoising steps. This is the convergence-to-variance ratio — how reliably the system approaches the target relative to the stochastic fluctuations in its trajectory.

Pe$_C$ can be measured from output data alone, without access to the internal pbit dynamics. It requires only: (1) samples from each denoising step, (2) the target distribution, and (3) a KL divergence estimator. This makes it extractable from any TSU implementation using the same protocol — enabling cross-architecture comparison on the same figure of merit.

**Prediction TC-3:** Pe$_C > 4$ produces self-sustaining sampling — the TSU generates diverse, convergent samples without continuous demon adjustment. Pe$_C < 4$ requires the demon to actively drive each step. **Prediction TC-4:** Pe$_C < 1$ — exploration dominates, convergence unreliable regardless of demon effort.

---

## 6. Channel Allocation: Design Optimization via Three-Channel Budget

### 6.1 The Three-Channel Decomposition

The Fantasia Bound (Section 4) constrains the total channel capacity. The three-channel decomposition [4, §6; 9, §2.4] specifies how that capacity distributes across physically distinguishable channels. For a TSU with interacting pbits:

$$I(D_1;Y) + I(D_2;Y) + I(M;Y) \leq H(Y)$$

where:
- **$I(D_1;Y)$** = thermal fluctuation channel. The information in the output attributable to individual pbit thermal switching — noise that is random across pbits, uncorrelated with the target or with other pbits. This is the "heat" of the computation.
- **$I(D_2;Y)$** = coupling channel. The information in the output attributable to inter-pbit energy transfer — correlations induced by pbit-pbit interactions (coupling constants, shared energy landscapes, Boltzmann machine weights). This is the "communication" between pbits.
- **$I(M;Y)$** = coherent computation channel. The information in the output that represents useful, target-correlated sample generation — the "work" of the computation.

In the normal operating regime, $D_1 + D_2$ consume most of $H(Y)$; $I(M;Y)$ — the useful computation — is whatever remains. The design problem is to maximize $I(M;Y)$.

### 6.2 The Anisotropy Principle

The superconductor design principle [4, §6.4] provides the hardware insight. In superconducting materials, room-temperature superconductivity requires that one scattering channel (electron-phonon or electron-electron) converts efficiently into Cooper pairing while the other is geometrically suppressed. Increasing coupling strength uniformly fails — stronger interactions increase both pairing and scattering, and the budget eats itself.

The same principle applies to TSU design. The naive approach — maximize inter-pbit coupling to improve sample quality — fails at scale because stronger coupling increases both $I(D_2;Y)$ (inter-pbit noise) and $I(M;Y)$ (coherent computation). The budget constraint means these compete. Doubling the coupling strength doubles both, and the fraction $I(M;Y) / H(Y)$ does not improve.

The correct design principle: **maximize anisotropy, not coupling strength.**

Anisotropy means the coupling is strong in the direction that contributes to $I(M;Y)$ (target-correlated pbit coordination) and weak in the direction that contributes to $I(D_2;Y)$ (random inter-pbit energy transfer). Concretely:

- **Target-aligned coupling:** Boltzmann machine weights that encode the target distribution's correlation structure. These drive pbits toward target-correlated configurations. Every bit of channel capacity consumed here contributes to $I(M;Y)$.
- **Orthogonal coupling:** Inter-pbit interactions that don't encode target structure — thermal cross-talk, parasitic coupling, layout-induced correlations. Every bit here goes to $I(D_2;Y)$ — wasted channel capacity.

The design optimization is:

$$\max_{\mathbf{w}} \frac{I(M;Y)}{H(Y)} = \max_{\mathbf{w}} \frac{I(M;Y)}{I(D_1;Y) + I(D_2;Y) + I(M;Y)}$$

where $\mathbf{w}$ is the vector of hardware design parameters (coupling topology, weight resolution, landscape programming scheme, layout geometry).

### 6.3 Channel Conversion Efficiency

Following the superconductor formalization [4, §6.4], define the *channel conversion efficiency*:

$$\eta_{\text{conv}} = \frac{I(M;Y)}{I(D_{\text{conv}};Y) + I(M;Y)}$$

This measures the fraction of a coupling channel's capacity that is redirected into coherent computation. At $\eta_{\text{conv}} = 0$, all coupling energy goes to noise. At $\eta_{\text{conv}} = 1$, all coupling contributes to useful computation (the TSU analog of perfect Cooper pairing).

**For TSU hardware,** $\eta_{\text{conv}}$ can be estimated from:

$$\eta_{\text{conv}} \approx \frac{D_{\text{KL}}(p_{\text{output}} \| p_{\text{thermal}}) - D_{\text{KL}}(p_{\text{output}} \| p_{\text{target}})}{D_{\text{KL}}(p_{\text{output}} \| p_{\text{thermal}})}$$

where $p_{\text{output}}$ is the actual output distribution, $p_{\text{thermal}}$ is the thermal equilibrium distribution, and $p_{\text{target}}$ is the target. This measures how much of the deviation from thermal equilibrium (all the work the demon and coupling performed) ended up moving toward the target vs. moving in other directions.

**Prediction TC-5:** Architectures with higher anisotropy (target-aligned coupling strong, orthogonal coupling suppressed) achieve higher $\eta_{\text{conv}}$ at the same total coupling strength. Isotropic coupling matching anisotropic coupling at fixed $\eta_{\text{conv}}$ would falsify the anisotropy principle.

### 6.4 Comparison with Existing Design Heuristics

Extropic's published design methodology [Verdon & McCourt 2023; Jelinčič et al. 2025] optimizes the energy landscape (demon programming) but does not explicitly decompose the output channel into three budget-constrained components. Their optimization targets convergence quality directly — which is correct as far as it goes — but does not provide:

1. **A budget constraint** that specifies how much total convergence is achievable before any optimization begins. The Fantasia Bound provides this.
2. **An allocation principle** that distinguishes between coupling that contributes to convergence and coupling that wastes capacity. The three-channel decomposition provides this.
3. **A figure of merit** for the coupling architecture itself, independent of the demon's landscape. $\eta_{\text{conv}}$ provides this.

The practical implication: when optimizing TSU hardware, optimize the coupling anisotropy first (maximize $\eta_{\text{conv}}$), then optimize the demon's landscape within the remaining budget. Optimizing the landscape first, in a coupling architecture with low $\eta_{\text{conv}}$, wastes demon bandwidth compensating for coupling noise — the demon is fighting the hardware's own inter-pbit cross-talk.

### 6.5 The TSU-SC Duality

TSUs and superconductors are dual solutions to the same channel budget constraint [4, §9.3]:

| Property | TSU | Superconductor |
|----------|-----|----------------|
| Objective | Maximize stochastic exploration $I(S;Y)$ | Maximize coherent transport $I(M;Y)$ |
| Operating point | Near opacity ground state | Far from ground state |
| Thermal noise | Harnessed as resource | Suppressed/converted via pairing |
| Channel allocation | Most capacity → exploration | Most capacity → coherence |
| Controller | Maxwell's demon (external) | Crystal lattice (internal geometry) |
| Energy cost | Low (equilibrium operation) | High (maintaining non-equilibrium coherence) |
| $\eta_{\text{conv}}$ target | Moderate (need $D_1$ for exploration) | Maximum (drive all scattering into pairing) |

Neither can access the other's optimum without fundamentally changing its channel allocation. A TSU trying to maintain internal coherence (moving toward the SC regime) pays Landauer costs and loses its energy advantage. A superconductor tolerating noise (moving toward the TSU regime) loses coherent transport and ceases to superconduct.

The duality is not analogy — it is the same optimization problem with opposite objective functions on the same constraint surface. This is the Fantasia Bound's physical content: it defines the Pareto frontier on which both TSUs and superconductors sit, at opposite extremes.

---

## 7. DTM Through the Void Lens

### 7.1 Denoising as Drift Reversal

Denoising Thermodynamic Models (DTMs) [Verdon & McCourt 2023] generate samples from a target distribution by iteratively refining noisy initial states. The process has two phases:

1. **Forward (noising):** Start with a sample from the target. Gradually add thermal noise over $K$ steps until the sample is indistinguishable from the equilibrium distribution. This is the opacity direction — from transparency ($O = 0$, target known) to opacity ($O = 1$, information destroyed).

2. **Reverse (denoising):** Start from thermal noise. Apply the demon's energy landscape at each step to progressively remove noise and converge toward the target. This is the constraint direction — from opacity ($O = 1$) toward transparency ($O < 1$, structure recovered).

In voidspace terms, the forward process is drift — the natural flow toward the void pole driven by the second law. The reverse process is constraint maintenance — work against the thermodynamic gradient, importing negentropy via the demon to push the system back toward the constraint pole. Each denoising step is a drift reversal attempt.

The Fantasia Bound constrains each step: $\Delta I(T;Y)_k \leq H(Y_k) - I(S_k;Y_k)$. The maximum convergence achievable at step $k$ is bounded by the channel capacity remaining after the stochastic exploration at that step consumes its share. The total convergence across all $K$ steps is bounded by the sum: $\sum_k \Delta I(T;Y)_k \leq K \cdot H(Y) \cdot \eta_{\text{mixing}}$ — recovering the scaling predictions of Section 4.

### 7.2 The Crooks Connection

The Crooks fluctuation theorem [Crooks 1999] gives the ratio of forward to reverse trajectory probabilities:

$$\frac{P_F(\gamma)}{P_R(\tilde{\gamma})} = \exp(\sigma_{\text{total}})$$

where $\gamma$ is a forward trajectory, $\tilde{\gamma}$ is its time-reversed counterpart, and $\sigma_{\text{total}}$ is the total entropy production along the trajectory. For DTM trajectories:

- **Forward (noising) trajectories** have $\sigma_{\text{total}} > 0$ — they produce entropy, increasing disorder. The forward process is overwhelmingly more probable than its reverse.
- **Reverse (denoising) trajectories** have $\sigma_{\text{total}} < 0$ from the system's perspective — they consume entropy, increasing order. But the demon imports negentropy, making the total entropy production (system + demon) non-negative.

The Crooks ratio for a DTM is a direct measure of how hard the denoising task is. Large Crooks ratio (forward $\gg$ reverse) means the denoising must fight against a strong thermodynamic gradient — the demon must import more negentropy per step. This connects to the minimum demon bandwidth (Section 4.4): the bandwidth requirement is the demon's cost of overcoming the Crooks ratio at each step.

### 7.3 DTM Convergence as Pe Trajectory

A DTM run traces a path through voidspace. At step 0 (pure noise): $(O \approx 1, R \approx 0, \alpha \approx 0)$ — maximum opacity, minimal responsiveness (output independent of target), minimal coupling. At step $K$ (converged sample): $(O < 1, R > 0, \alpha > 0)$ — reduced opacity (structure visible), increased responsiveness (output tracks target), increased coupling (downstream decisions depend on output quality).

The Pe at each step characterizes the local dynamics:
- Early steps: Pe $< 1$ (noise dominates, Gas phase, exploration).
- Middle steps: Pe $\sim 2{-}4$ (Fluid phase, correlations emerging).
- Late steps: Pe $> 4$ (Vortex phase if well-tuned, Crystal if over-driven).

The demon's landscape scheduling determines the Pe trajectory. A well-designed demon pushes the system through the phases in order: Gas → Fluid → Vortex. An over-aggressive demon (landscape too strong too early) pushes directly to Crystal, losing stochastic diversity. An under-powered demon (landscape too weak) leaves the system in Gas phase — noise without convergence.

**Prediction TC-6:** No single DTM step achieves convergence exceeding its per-step Fantasia allocation by more than $2\times$. The bound applies step-by-step, not just in aggregate.

**Prediction TC-9:** The measured Crooks ratio for DTM forward/reverse trajectories matches the stochastic thermodynamic prediction ($P_F/P_R = \exp(\sigma)$) within $2\sigma$ across $>50$ trajectory pairs. This tests whether the stochastic thermodynamics framework (developed for molecular-scale systems) applies at the TSU's mesoscale pbit dynamics.

---

## 8. Cross-Substrate Validation Protocol

### 8.1 The Test

The Substrate Independence Theorem [9, Theorem 1] makes a single, decisive prediction: systems at matched $(O, R, \alpha)$ coordinates produce identical drift dynamics regardless of physical substrate. This has been validated across nine substrates — computational agents, human gambling, cryptocurrency markets, and multiplayer gaming [4, §8; 5, §II.E'] — but never on physical computing hardware.

Thermodynamic computing provides the first opportunity to test substrate independence across the information-physical boundary: do a software simulation and a hardware TSU at matched coordinates produce the same Pe?

### 8.2 Protocol

**Step 1: Hardware Measurement.** Instrument a TSU (reference architecture: Z1 or equivalent) with the following measurements:

- **O:** Input a known test distribution. Measure the mutual information between the known pbit microstate (accessible via auxiliary readout) and the standard output interface. $O = 1 - I(\text{aux}; \text{output})/H(\text{aux})$.
- **R:** Program a sequence of known energy landscapes. Measure the mutual information between landscape parameters and output sample statistics. $R = I(\mathcal{L}; \mathbf{y})/H(\mathbf{y})$.
- **$\alpha$:** Feed TSU output into a downstream decision system (can be a simple Bayesian classifier). Measure the fraction of downstream decisions explained by TSU output. $\alpha = I(\mathbf{y}; \mathbf{d})/H(\mathbf{d})$.
- **Pe$_C$:** Compute per §5.4 from the denoising trajectory data.

**Step 2: Software Simulation at Matched Coordinates.** Implement a software Boltzmann machine (or equivalent stochastic sampler) calibrated to the same $(O, R, \alpha)$ operating point:

- Match $O$ by adjusting the software system's state accessibility (e.g., partially mask the internal state to an observer module).
- Match $R$ by calibrating the software landscape's input-output mutual information.
- Match $\alpha$ by calibrating the downstream decision system's dependence on software output.
- Compute Pe$_C$ from the software denoising trajectory using the same protocol.

**Step 3: Comparison.**
- Compute $\Delta \text{Pe} = |\text{Pe}_{\text{hardware}} - \text{Pe}_{\text{software}}| / \text{Pe}_{\text{avg}}$.
- TC-1 predicts $\Delta \text{Pe} < 0.3$.
- Repeat across at least three distinct operating points in $\mathcal{V}$ (one in Gas, one in Fluid, one in Vortex phase) to test across phase boundaries.

### 8.3 What This Tests

A positive result ($\Delta \text{Pe} < 0.3$ across three operating points) would be the first empirical confirmation that information-geometric substrate independence extends to physical computing hardware — that the dynamics are genuinely horizontal in the fiber bundle.

A negative result ($\Delta \text{Pe} > 0.3$ at any operating point) would either falsify the Substrate Independence Theorem for hardware substrates or identify a measurement error in the coordinate matching. The protocol includes a diagnostic: if Pe disagrees but $(O, R, \alpha)$ matching is confirmed (via the auxiliary readout), the theorem is falsified. If $(O, R, \alpha)$ matching cannot be confirmed, the negative result is inconclusive.

### 8.4 Existing Cross-Substrate Evidence

The framework has measured Pe across nine substrates [4, §8.2]:

| Substrate | Pe | N | Source |
|-----------|-----|---|--------|
| Computational agents (AI) | 7.94 [3.52, 17.89] | 11 | EXP-001 |
| Human gambling (pooled) | 2.21 [1.44, 2.97] | 1,117 | 5 studies |
| Cryptocurrency (Ethereum DEX) | 3.74 [3.04, 4.59] | 968 | EXP-021 |
| Cryptocurrency (Base DEX) | 15.52 [11.80, 20.41] | 1,944 | EXP-021B |
| Cryptocurrency (Solana DEX) | 16.17 [13.80, 18.95] | 116 | EXP-021C |
| FPS gaming (CS2) | 4.4× directional | 2,299 | EXP-022 |
| MOBA gaming (Dota 2) | 0.47 | 3,682 | EXP-023 |
| RTS gaming (SC2) | 0.013 vs 0.026 | 474 | EXP-024 |

These span four domain families (AI agents, human cognition, financial markets, competitive gaming) but all operate on information-processing substrates (neural networks, brains, market mechanisms, game mechanics). The TSU test would be the first physical-hardware substrate — thermodynamic fluctuations in silicon or magnetic tunnel junctions — validating that the geometry holds at the physics level, not just the information level.

**Note:** This protocol is designed but not yet executed. The fork hardware is at concept stage. The protocol is published here so that any group with TSU-class hardware can run it. The prediction is registered before the test — the correct scientific order.

---

## 9. The Acceleration Paradox

### 9.1 Two Entropy Productions on Different Substrates

The thermodynamic computing thesis is: harness thermal noise to reduce computational energy cost by orders of magnitude. The ground state theorem (Section 3) confirms this works — operating at the opacity ground state avoids the Landauer cost of transparency, producing the ~10,000× energy advantage [Jelinčič et al. 2025].

But the ground state theorem also identifies what this does not solve. There are two entropy productions in any system where hardware generates outputs consumed by observers:

1. **Hardware entropy production** ($\dot{S}_{\text{HW}}$): Thermodynamic entropy generated by the physical computation. This is what TSUs minimize. It is measured in joules/kelvin per operation.

2. **Informational entropy production** ($\dot{S}_{\text{info}}$): The entropy generated in the observer's belief state by interacting with opaque, responsive, coupled outputs. This is what the drift dynamics produce. It is measured in bits per interaction.

These operate on different substrates — one physical, one informational — but are governed by the same thermodynamic law. The ground state theorem applies to both: $\dot{S}_{\text{HW}} \geq 0$ and $\dot{S}_{\text{info}} \geq 0$, with equality only at equilibrium (no computation / no interaction).

### 9.2 The Paradox

Reducing $\dot{S}_{\text{HW}}$ by $10{,}000\times$ does not reduce $\dot{S}_{\text{info}}$. The informational entropy production depends on the observer-system interface properties $(O, R, \alpha)$, not on the energy cost of generating the output. A recommendation algorithm running on a TSU at 20 nJ per inference produces the same drift dynamics in the user as the same algorithm running on a GPU at 200,000 nJ per inference — provided the $(O, R, \alpha)$ coordinates of the interface are identical.

What changes is the **deployment economics.** The cost to deploy an opacity-maximizing system scales with computational energy:

$$C_{\text{deploy}} = C_{\text{fixed}} + n_{\text{users}} \cdot f_{\text{interactions}} \cdot E_{\text{compute}} \cdot p_{\text{energy}}$$

where $n_{\text{users}}$ is the user base, $f_{\text{interactions}}$ is interactions per user per unit time, $E_{\text{compute}}$ is energy per inference, and $p_{\text{energy}}$ is energy price. A $10{,}000\times$ reduction in $E_{\text{compute}}$ reduces the marginal cost of each interaction by the same factor. Systems that were energy-constrained at scale become energy-unconstrained.

The acceleration paradox: **solving the hardware entropy problem makes the informational entropy problem cheaper to deploy at scale.** The energy brake — the cost that limits how many users an opacity-maximizing system can serve, how many interactions it can process, how many instances it can run — is removed.

### 9.3 Quantitative Prediction

In the energy-constrained regime (where $E_{\text{compute}}$ is a significant fraction of $C_{\text{deploy}}$), the deployment rate of opacity-maximizing systems scales as:

$$\text{deployment rate} \propto \frac{1}{E_{\text{compute}}}$$

A $10{,}000\times$ reduction in $E_{\text{compute}}$ predicts a corresponding increase in the number of deployed interactions — more instances, more users, more interactions per user — limited only by bandwidth, storage, and the fixed costs that are not energy-dependent.

This is prediction **TC-7.** It is directly testable: track the deployment rate of AI inference systems (recommendation, generation, classification with opaque, responsive interfaces) before and after TSU-class hardware becomes available at scale. The prediction is that energy-efficient hardware does not reduce informational entropy production per interaction — it reduces the cost per interaction, enabling more interactions.

### 9.4 The Constraint Architecture Response

The paradox is not an argument against thermodynamic computing — the hardware advances are genuine, the energy reduction is real, the engineering is sound. The paradox identifies what the hardware solves and what it does not.

Paper 4B [4B] analyzes this in detail for the e/acc movement specifically. The present paper extends the analysis to the hardware itself: the TSU is a tool. Its effect on informational entropy production depends on the constraint architecture of the system it is embedded in. A TSU running a well-constrained inference pipeline (transparent model, invariant outputs, low coupling to observer decisions) produces minimal informational entropy regardless of the hardware efficiency. A TSU running an opacity-maximizing engagement pipeline produces the same drift dynamics at $1/10{,}000$ the energy cost.

The framework is agnostic about which applications the hardware serves. It predicts the consequences of each. The demon is the difference between a heater and a computer (Section 3.3). The constraint architecture is the difference between a computer and a void.

---

## 10. Testable Predictions

The following predictions are derived from the voidspace mapping (§2), ground state theorem (§3), Fantasia Bound (§4), demon lattice phases (§5), three-channel budget (§6), DTM analysis (§7), and acceleration paradox (§9). Each prediction specifies a falsification condition — a specific empirical result that would kill the claim.

### 10.1 Substrate Independence Predictions

**TC-1: Substrate Independence at Matched Coordinates.**
*Prediction:* Two TSU architectures (e.g., sMTJ and CMOS pbit implementations) measured at matched $(O, R, \alpha)$ coordinates produce Pe values within ±0.3 of each other: $|\text{Pe}_A - \text{Pe}_B| / \text{Pe}_{\text{avg}} < 0.3$.
*Falsification:* Pe ratio outside $[0.7, 1.3]$ for two architectures at confirmed matched coordinates. This would falsify the Substrate Independence Theorem [9] for hardware substrates.
*Source:* §2.4. *Priority:* HIGH — tests the paper's foundational claim.

**TC-10: External Observability of Pe.**
*Prediction:* Pe is computable from $(O, R, \alpha)$ coordinates measured at the hardware interface without access to the internal pbit dynamics.
*Falsification:* Pe computation from interface measurements deviates >2σ from Pe computed with full internal state access. This would mean the fiber bundle projection loses dynamically relevant information.
*Source:* §2, §5.4. *Priority:* HIGH — tests whether the abstraction holds.

### 10.2 Scaling and Convergence Predictions

**TC-2: Fantasia Bound Saturation.**
*Prediction:* TSU convergence quality degrades when $H_{\text{target}}$ approaches $N_{\text{pbits}} \times \eta_{\text{mixing}} \times K_{\text{steps}}$. Below this threshold, convergence is reliable. Above it, convergence degrades proportionally to the ratio $H_{\text{target}} / (N \cdot \eta \cdot K)$.
*Falsification:* Convergence quality maintained above the theoretical maximum channel capacity. Specifically: KL divergence from target continues decreasing after the Fantasia Bound predicts saturation.
*Source:* §4.3. *Priority:* CRITICAL — tests the core resource constraint.

**TC-8: Minimum Demon Bandwidth.**
*Prediction:* Convergence fails when demon bandwidth $B_{\text{demon}} < H_{\text{data}} / (n_{\text{steps}} \times \eta_{\text{mixing}})$, regardless of architecture optimization.
*Falsification:* Convergence achieved below the minimum bandwidth. Specifically: $D_{\text{KL}}(p_{\text{output}} \| p_{\text{target}}) < \epsilon$ at $B_{\text{demon}} < 0.5 \times B_{\text{demon,min}}$.
*Source:* §4.4. *Priority:* HIGH — tests the hard floor on demon control.

### 10.3 Phase Boundary Predictions

**TC-3: Vortex Onset at Pe = 4.**
*Prediction:* Self-sustaining sampling — where the TSU generates diverse, convergent samples without continuous demon adjustment per step — occurs only when Pe$_C > 4$. Below this threshold, the demon must actively drive each denoising step.
*Falsification:* Sustained, convergent sampling (measured as stable $D_{\text{KL}} < \epsilon$ over $>100$ sample batches without demon adjustment) at Pe$_C < 3$. The threshold of 3 (rather than 4) provides a 25% margin for measurement uncertainty.
*Source:* §5.2, §5.3. *Priority:* HIGH — tests the phase diagram.

**TC-4: Gas Phase Below Pe = 1.**
*Prediction:* At Pe$_C < 1$, stochastic exploration dominates convergence. The TSU generates high-entropy samples unrelated to the target regardless of demon effort.
*Falsification:* Reliable target convergence ($D_{\text{KL}} < 0.1$ nats) at Pe$_C < 0.5$ for non-trivial targets ($H_{\text{target}} > 100$ bits).
*Source:* §5.2. *Priority:* MEDIUM — tests the lower phase boundary.

### 10.4 Design Optimization Predictions

**TC-5: Anisotropy Advantage.**
*Prediction:* At fixed total coupling strength, architectures with higher coupling anisotropy (target-aligned coupling strong, orthogonal coupling suppressed) achieve higher $\eta_{\text{conv}}$ than isotropic coupling architectures.
*Falsification:* An isotropic coupling architecture matches or exceeds an anisotropic architecture's $\eta_{\text{conv}}$ at the same total coupling strength and pbit count, across three or more target distributions.
*Source:* §6.2, §6.3. *Priority:* HIGH — tests the novel design principle.

### 10.5 DTM-Specific Predictions

**TC-6: Per-Step Fantasia Allocation.**
*Prediction:* Each DTM denoising step is bounded by the per-step Fantasia allocation: $\Delta I(T;Y)_k \leq H(Y_k) - I(S_k;Y_k)$ where $k$ indexes the denoising step. No single step can achieve more convergence than its share of the channel capacity permits.
*Falsification:* A single denoising step achieves convergence improvement exceeding the per-step Fantasia allocation by $>2\times$.
*Source:* §7. *Priority:* MEDIUM — tests the bound's per-step applicability.

**TC-9: Crooks Ratio for DTM Trajectories.**
*Prediction:* The ratio of forward (noising) to reverse (denoising) trajectory probabilities matches the stochastic thermodynamics prediction: $P_F(\gamma) / P_R(\tilde{\gamma}) = \exp(\sigma_{\text{total}})$, where $\sigma_{\text{total}}$ is the total entropy production along the trajectory.
*Falsification:* Measured Crooks ratio deviates $>2\sigma$ from the entropy production prediction across $>50$ trajectory pairs.
*Source:* §7. *Priority:* MEDIUM — tests the stochastic thermodynamics bridge.

### 10.6 Acceleration Prediction

**TC-7: Deployment Acceleration.**
*Prediction:* A $10{,}000\times$ reduction in computational energy cost produces a measurable increase in the deployment rate of opacity-maximizing systems (systems with high $O$ at their observer interfaces). The deployment rate scales as $\propto 1/E_{\text{compute}}$ within the energy-constrained regime.
*Falsification:* TSU-class energy efficiency becomes widely available with no statistically significant increase in deployment of opacity-maximizing systems over a 5-year observation window.
*Source:* §9. *Priority:* LOW (long observation window) — tests the acceleration paradox.

### 10.7 Summary Table

| ID | Prediction | Falsification Threshold | Section | Priority |
|----|-----------|------------------------|---------|----------|
| TC-1 | Substrate independence at matched coordinates | Pe ratio outside [0.7, 1.3] | §2.4 | HIGH |
| TC-2 | Fantasia Bound saturation at scale | Convergence above theoretical maximum | §4.3 | CRITICAL |
| TC-3 | Vortex onset at Pe > 4 | Sustained sampling at Pe < 3 | §5.2 | HIGH |
| TC-4 | Gas phase below Pe = 1 | Reliable convergence at Pe < 0.5 | §5.2 | MEDIUM |
| TC-5 | Anisotropy advantage in coupling | Isotropic matches anisotropic | §6.2 | HIGH |
| TC-6 | Per-step Fantasia allocation | Step convergence exceeds 2× allocation | §7 | MEDIUM |
| TC-7 | Deployment acceleration with cheap compute | No deployment increase over 5 years | §9 | LOW |
| TC-8 | Minimum demon bandwidth | Convergence below 0.5× B_min | §4.4 | HIGH |
| TC-9 | Crooks ratio for DTM trajectories | >2σ deviation from prediction | §7 | MEDIUM |
| TC-10 | Pe observable from interface only | >2σ deviation from internal measurement | §2, §5.4 | HIGH |

---

## 11. Experimental Design for Future Hardware

### 11.1 Minimum Hardware Requirements

The predictions in Section 10 are testable on any hardware satisfying:

| Requirement | Minimum Spec | Purpose |
|------------|-------------|---------|
| Pbit count | $N \geq 1{,}000$ | Sufficient for non-trivial target distributions |
| Readout | Per-step sample access | Pe trajectory measurement (§7.3) |
| Demon bandwidth | Programmable landscape, $\geq N$ bits/step | Bandwidth floor tests (TC-8) |
| Auxiliary readout | Optional: full microstate access | Coordinate matching verification (§8.2) |
| Temperature control | Tunable $T$ or equivalent noise | Phase boundary traversal (TC-3, TC-4) |
| Clock | Multiple denoising steps ($K \geq 4$) | Per-step Fantasia test (TC-6) |

The auxiliary readout (full microstate access) is optional — needed only for the strongest version of the substrate independence test (TC-1, TC-10). The remaining predictions require only standard input-output measurements.

### 11.2 Measurement Protocol

**Coordinate Measurement.** For each operating point:

1. Run $M \geq 100$ independent sample batches (each batch: one full DTM forward-reverse cycle).
2. Record per-step samples for Pe trajectory computation.
3. Compute $(O, R, \alpha)$ from batch statistics:
   - $O$: Compare per-pbit entropy of output samples to maximum entropy ($\log_2 2 = 1$ bit per binary pbit). $O = 1 - I_{\text{est}}/H_{\text{max}}$ where $I_{\text{est}}$ is the estimated mutual information between the observer's readout and the pbit state (requires either auxiliary readout or statistical estimation from output correlations).
   - $R$: Vary the landscape systematically (e.g., 10 distinct target distributions). Measure $I(\mathcal{L}; \mathbf{y})$ from the landscape-output contingency table.
   - $\alpha$: Feed output to a calibrated downstream classifier. Measure classification accuracy relative to chance.

4. Compute Pe$_C$ per §5.4 from per-step KL divergence trajectory.

**Phase Boundary Traversal.** To test TC-3 and TC-4:

1. Start at Gas phase (weak landscape, Pe$_C < 1$). Verify: high-entropy output, low target correlation.
2. Gradually increase landscape strength (increase demon gain).
3. Record Pe$_C$ at each level.
4. Identify the transition point where sustained sampling emerges.
5. Prediction: transition occurs at Pe$_C \in [3, 5]$ (the Vortex boundary ± measurement margin).

**Anisotropy Test.** To test TC-5:

1. Fix total coupling energy $\sum |J_{ij}|$ (Boltzmann machine weights).
2. Configure two coupling matrices: (a) anisotropic — weights aligned with target correlation structure, orthogonal coupling minimized; (b) isotropic — same total weight distributed uniformly.
3. Run both configurations on $\geq 3$ distinct target distributions.
4. Compare $\eta_{\text{conv}}$ (§6.3) for each.
5. Prediction: anisotropic $\eta_{\text{conv}} >$ isotropic $\eta_{\text{conv}}$ for all targets.

### 11.3 Data Requirements

Per operating point: $M \times K$ sample vectors (100 batches × 8+ denoising steps × $N$ pbits per sample). For $N = 1{,}000$: ~800,000 binary values per operating point. For $N = 250{,}000$: ~200M binary values per operating point. Storage is minimal; computation for KL estimation and Pe extraction is moderate (standard density estimation or k-NN mutual information estimators).

### 11.4 Reproducibility

This protocol is published CC-BY so that any group with TSU-class hardware can run it. The predictions are registered before execution. Results — positive or negative — should be reported with the full $(O, R, \alpha)$ coordinate measurements, the Pe$_C$ trajectory data, and the raw sample data for independent verification. The void framework claims to make testable predictions about physical hardware. This section specifies how to test them.

---

## 12. Discussion and Limitations

### 12.1 What the Framework Can and Cannot Tell You

The void framework operates at the information-geometric level. It constrains the channel capacity budget, identifies phase boundaries, predicts scaling walls, and provides design principles for channel allocation. It cannot tell you:

- **Which pbit technology to use.** The substrate independence theorem means the dynamics are the same regardless of whether you use sMTJs, CMOS inverters, superconducting junctions, or photonic elements. The choice of substrate determines engineering parameters (clock speed, operating temperature, manufacturing cost, integration density) that live in the fiber, not the base space.
- **How to fabricate the device.** Materials science, lithography, packaging, thermal management — these are substrate-specific engineering problems outside the scope of information geometry.
- **The precise mixing efficiency.** $\eta_{\text{mixing}}$ depends on the specific coupling topology, landscape programming scheme, and temperature calibration. The framework provides the bound that $\eta_{\text{mixing}}$ enters; measuring it requires hardware.

### 12.2 Honest Limitations

**No empirical hardware data.** This paper derives predictions and designs protocols. The predictions have not been tested on TSU hardware. The fork is at concept stage. The protocols are published so that any group with hardware can run them. Until empirical validation, the mapping is theoretical.

**Coordinate measurement uncertainty.** Measuring $(O, R, \alpha)$ on hardware requires estimating mutual information from finite samples. The estimates have uncertainty. The ±0.3 tolerance on TC-1 accounts for reasonable measurement error but may be too tight or too loose depending on the specific estimation methodology. Empirical calibration of the measurement protocol is needed.

**The Pe = 4 threshold is approximate.** The vortex onset at Pe $\approx 4$ is derived from the stationary distribution analysis [9, §6.8.2] and supported by cross-domain empirical evidence (gambling Pe $= 2.21$ without self-sustaining ecosystems; competitive gaming Pe $= 4.4$ with them). It is not a sharp phase transition — it is a crossover. The prediction TC-3 uses a margin (Pe $< 3$) to account for this.

**The acceleration paradox is a long-horizon prediction.** TC-7 requires observing deployment rates over a multi-year window. It is the weakest prediction in the set — testable in principle but requiring patience and careful measurement of deployment baselines.

### 12.3 The Broader Implication

If the predictions hold — if substrate independence is confirmed for physical hardware, if the Fantasia Bound is observed at scale, if the phase boundaries match the predicted Pe values — then the void framework provides a universal geometry for all information-processing systems, from neural networks to thermodynamic computers to financial markets. The same manifold, the same metric, the same bounds. The hardware is one fiber in a bundle that includes brains, markets, and algorithms.

If the predictions fail — if two TSU implementations at matched coordinates produce wildly different dynamics, or if a TSU converges above the Fantasia Bound — then the substrate independence theorem is falsified for hardware substrates, and the framework's scope must be restricted to the information-processing substrates where it has been validated.

Either outcome advances the science. The predictions are stated. The protocols are published. The framework has made itself falsifiable on physical hardware. Now it needs hardware to test it.

---

## References

[1] A. Eckert, "The Architecture of Drift: A Void Framework for Structural Coupling," Paper 1, v13.0, 2026. CC-BY 4.0. https://doi.org/10.5281/zenodo.18716776

[2] A. Eckert, "The Shape of the Cage: AI Safety Through the Void Framework," Paper 2, v5.6, 2026. CC-BY 4.0. https://doi.org/10.5281/zenodo.18716778

[3] A. Eckert, "Thermodynamics of Opacity: Technical Foundations of the Void Framework," Paper 3, v7.0, 2026. CC-BY 4.0. https://doi.org/10.5281/zenodo.18716782

[4] A. Eckert, "Information-Geometric Bounds on Thermodynamic Sampling and Superconductor Design," Paper 4, v3.6, 2026. CC-BY 4.0. https://doi.org/10.5281/zenodo.18716784

[4B] A. Eckert, "The Thermodynamic Cost of Unconstrained Acceleration," Paper 4B, v1.7, 2026. CC-BY 4.0. https://doi.org/10.5281/zenodo.18716789

[5] A. Eckert, "The Ground State of Observation: TOE Synthesis," Paper 5, v4.9, 2026. CC-BY 4.0. https://doi.org/10.5281/zenodo.18716791

[9] A. Eckert, "Voidspace: The Geometry of Observer-Opacity Interactions," Paper 9, v3.1, 2026. CC-BY 4.0. https://doi.org/10.5281/zenodo.18716801

[Bennett 1973] C. H. Bennett, "Logical reversibility of computation," *IBM Journal of Research and Development*, 17(6), 525–532, 1973.

[Crooks 1999] G. E. Crooks, "Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences," *Physical Review E*, 60(3), 2721, 1999.

[Crooks 2007] G. E. Crooks, "Measuring thermodynamic length," *Physical Review Letters*, 99(10), 100602, 2007.

[Čencov 1982] N. N. Čencov, *Statistical Decision Rules and Optimal Inference*, Translations of Mathematical Monographs 53, American Mathematical Society, 1982.

[Fredkin & Toffoli 1982] E. Fredkin and T. Toffoli, "Conservative logic," *International Journal of Theoretical Physics*, 21(3–4), 219–253, 1982.

[Jelinčič et al. 2025] T. Jelinčič, S. Bravyi, G. Verdon, et al., "Denoising Thermodynamic Models," arXiv, 2025.

[Landauer 1961] R. Landauer, "Irreversibility and heat generation in the computing process," *IBM Journal of Research and Development*, 5(3), 183–191, 1961.

[Ruppeiner 1979] G. Ruppeiner, "Thermodynamics: A Riemannian geometric model," *Physical Review A*, 20(4), 1608, 1979.

[Ruppeiner 1995] G. Ruppeiner, "Riemannian geometry in thermodynamic fluctuation theory," *Reviews of Modern Physics*, 67(3), 605, 1995.

[Verdon & McCourt 2023] G. Verdon and T. McCourt, "Thermodynamic AI and the Fluctuation Frontier," arXiv:2302.06584, 2023.

---

## Version History

- **v0.1** (2026-02-20): Skeleton. All 12 section headers established.
- **v1.0** (2026-02-20): Content-complete first draft. All 12 sections written. 10 predictions (TC-1–TC-10) with falsification thresholds. Cross-substrate validation protocol. Experimental design for TSU-class hardware. Abstract written. References compiled. ~20K words.
