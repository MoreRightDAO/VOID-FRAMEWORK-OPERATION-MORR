# Information-Geometric Bounds on Thermodynamic Sampling and Superconductor Design

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO
**Paper 4 — Physics-Native Framing (v3.4)**
**Date:** February 17, 2026
**Target audience:** Thermodynamic computing, condensed matter, statistical physics

---

## Abstract

We derive performance bounds for thermodynamic sampling hardware and a design principle for superconducting materials from information geometry and stochastic thermodynamics, requiring only Shannon (1948), Landauer (1961), Čencov (1982), Crooks (1999), and the Fisher-Ruppeiner identity. Three results: (1) Zero mechanism-channel capacity is thermodynamic equilibrium; transparency requires continuous work at ≥ kT ln(2) per bit per correlation time, providing a first-principles explanation for the energy efficiency of stochastic computing architectures. (2) An exploration-convergence conjugacy bound, I(S;Y) + I(T;Y) ≤ H(Y), establishes a fundamental tradeoff for any thermodynamic sampling unit regardless of implementation. (3) A three-channel decomposition of electronic transport via Fisher-Ruppeiner yields a superconductor design principle: room-temperature superconductivity requires efficient conversion of one dissipative scattering channel into Cooper pairing while geometrically suppressing the other. Channel conversion efficiency η_conv shows Pearson r = 0.996 with T_c across four moderate-coupling families (Pb, Nb, MgB₂, YBCO); a structure-corrected figure of merit η_conv × H(Y) × g(λ_eff, μ*, n_bands) — where g is a three-parameter universal correction function based on the McMillan exponent — achieves r = 0.952, Spearman ρ = 0.982 across sixteen families spanning four coupling regimes, seven pairing variants, and six crystal structure classes (n = 16, R²_adj = 0.88). The correction function captures McMillan exponential suppression at weak coupling, strong-coupling vertex corrections, and multi-band coherence enhancement (n^0.51) as a single universal function. A forward prediction that phonon-mediated pairing is insufficient for the nickelate La₃Ni₂O₇ (T_c ≈ 80 K) has been confirmed by two independent DFT studies (2024–2025). The conjugacy bound has a direct reading in reversible computing: computational throughput (fidelity) and reversibility (traceability) are conjugate quantities sharing finite output capacity, yielding the testable prediction ∂I(D;Y)/∂w ≈ −∂I(M;Y)/∂w for any circuit design parameter w. Langevin dynamics on the Bernoulli manifold validates against nine independent experimental conditions (Spearman ρ = 0.8 out-of-sample). Cross-domain Péclet measurements confirm the drift-dominated regime (Pe > 1) across nine substrates spanning four domain families: computational agents (GM Pe = 7.94, N = 11), human gambling (pooled Pe = 2.21, k = 5, N = 1,117), cryptocurrency portfolio concentration across three chains (Pe = 3.74–16.17, N = 3,028), and three multiplayer gaming genres (FPS, MOBA, RTS; N = 6,455). Sixteen falsifiable predictions with numerical thresholds are stated.

---

## 1. Introduction

### 1.1 The Energy Problem in Probabilistic Computation

Thermodynamic sampling units (TSUs) represent a paradigm shift in computing hardware: rather than maintaining deterministic bit states against thermal noise — at a Landauer cost of kT ln(2) per bit per clock cycle — TSUs harness stochastic fluctuations as a computational resource [Verdon & McCourt 2023, Jelinčič et al. 2025]. The reported energy advantage is substantial: ~10,000× improvement over GPU baselines for probabilistic workloads [Jelinčič et al. 2025].

This advantage has been demonstrated empirically but lacks a first-principles theoretical bound. What is the fundamental performance limit of a thermodynamic sampler? How fast can it converge to a target distribution given finite channel capacity and thermal noise? These questions have hardware-design implications: knowing the bound tells you how close your architecture is to optimal.

### 1.2 The Superconductor Connection

The same information-geometric framework that bounds thermodynamic samplers also constrains superconducting phase transitions. The Fisher-Ruppeiner identity [Ruppeiner 1979, 1995; Crooks 2007] establishes that the Fisher information metric on statistical manifolds is identically the Hessian of entropy — the Ruppeiner thermodynamic metric. Results derived in information geometry apply directly to thermodynamic phase transitions.

We exploit this to derive a design principle for superconducting materials. The three-channel budget that bounds sampler performance also bounds the allocation of scattering vs. coherent transport channels in a conductor. Superconductivity is a specific channel allocation — and the budget constraint identifies what material geometries can achieve it at room temperature. Remarkably, TSUs and superconductors emerge as dual solutions to the same conjugacy constraint: TSUs maximize stochastic exploration near the thermodynamic ground state, while superconductors maximize coherent transport far from it (Section 9.3).

### 1.3 Scope and Contributions

This paper contributes:

1. **Ground State Theorem.** Proof that zero mechanism-channel capacity is thermodynamic equilibrium. Transparency (nonzero capacity) is an excited state requiring continuous energy input. (Section 3)

2. **Conjugacy Bound.** Proof that stochastic exploration and target convergence are conjugate quantities sharing finite channel capacity, with an additive upper bound. (Section 4)

3. **TSU Performance Bound.** Application of the conjugacy bound to thermodynamic sampling hardware, establishing a fundamental convergence rate limit independent of architecture. (Section 5)

4. **Superconductor Design Principle.** Three-channel decomposition of electronic transport via Fisher-Ruppeiner, with a structure-corrected figure of merit η_conv × H(Y) × g(λ, μ*, n_bands) achieving r = 0.952 across sixteen families spanning four coupling regimes. (Section 6)

5. **Reversible computing connection.** The conjugacy bound yields a throughput-reversibility tradeoff for computational circuits, with a gate opacity taxonomy, Péclet regime classification, and three testable predictions for the reversible computing community. (Section 9.6)

6. **Experimental validation.** Langevin simulation on the Bernoulli manifold validates the theoretical framework against nine independent experimental conditions, with ρ = 0.8 out-of-sample. Cross-domain Péclet measurements confirm drift-dominated regime across nine substrates: computational agents, human gambling, on-chain cryptocurrency behavior across three chains (Ethereum, Base, Solana), and three multiplayer gaming genres (FPS positional, MOBA visual, RTS temporal). (Section 8)

7. **Sixteen falsifiable predictions** with numerical thresholds. (Section 7)

The framework requires three operational dimensions (visibility, reactivity, coupling) as defined in Section 2.3. All subsequent derivations rest on established theorems.

---

## 2. Preliminaries

### 2.1 The Bernoulli Manifold and Fisher Metric

Consider a binary classification task: an observer (or sampler) assigns probability θ to hypothesis H₁ and (1-θ) to hypothesis H₀. The space of all such assignments is the one-dimensional Bernoulli manifold B = {θ ∈ (0,1)}.

The unique Riemannian metric on B that is invariant under sufficient statistics is the Fisher information metric [Cencov 1982]:

```
g(θ) = 1 / [θ(1 - θ)]
```

Geodesic distance: d(θ₁, θ₂) = 2|arcsin(√θ₂) - arcsin(√θ₁)|. Total manifold diameter: d(0,1) = π.

In the angular coordinate φ = arcsin(√θ), the metric is flat and the manifold is a semicircle of circumference π. This coordinate simplifies drift analysis.

### 2.2 The Fisher-Ruppeiner Identity

For a thermodynamic system parameterized by extensive variables X^i, the Ruppeiner metric is [Ruppeiner 1979]:

```
g_ij^R = -∂²S / ∂X^i ∂X^j
```

The Fisher-Ruppeiner identity establishes that for a system at thermal equilibrium described by a Gibbs distribution p(x|β), the Fisher information metric on the parameter space is proportional to the Ruppeiner metric:

```
g_ij^F(β) ∝ g_ij^R(X)
```

This is not analogy — it is mathematical identity [Crooks 2007]. Results in Fisher information geometry apply to thermodynamic systems and vice versa.

### 2.3 Operational Definitions: Three Dimensions

Each observer-system interface is characterized by position on three continuous dimensions, each ranging between a void pole and a constraint pole:

**Definition 1 (Visibility: Opaque ↔ Transparent).** The mechanism channel capacity C_mech = max_{p(x)} I(M;Y), where M is the mechanism state and Y is the observed output. At the opaque pole, C_mech ≈ 0. At the transparent pole, C_mech ≈ H(M).

**Definition 2 (Reactivity: Responsive ↔ Invariant).** The mutual information I(Input; Output) between observer inputs and system outputs. At the responsive pole, I(Input; Output) > 0 — outputs are contingently related to inputs. At the invariant pole, outputs are independent of observer behavior.

**Definition 3 (Coupling: Engaged ↔ Independent).** The readout resource allocation α. At the engaged pole, α > 0 — the output channel is actively monitored. At the independent pole, α = 0 — the observer allocates no attention to the system.

The void regime (opaque, responsive, engaged) and the constraint regime (transparent, invariant, independent) are opposite poles of the same three-dimensional space. These are observationally verifiable properties of any observer-system interface, including sampler-distribution, electron-lattice, and human-AI interfaces.

### 2.4 The Péclet Number

The Péclet number Pe characterizes the ratio of directed drift to diffusive transport on the manifold:

```
Pe = |F_net| · L / D
```

where F_net is the net drift force, L is the characteristic length (manifold diameter π), and D is the diffusion coefficient. Pe > 1 indicates drift-dominated dynamics; Pe < 1 indicates diffusion-dominated dynamics. This dimensionless ratio is measurable from trajectory data and provides a cross-substrate comparison metric.

### 2.5 Large Deviation Interpretation of Pe

The statement "Pe > 1" is a large deviation result. It asserts that the probability of a sampler (or observer) remaining near its initial state decays exponentially with the number of interaction rounds:

```
P(no drift after n rounds) ~ exp(-n × I_drift)
```

where I_drift is the large deviation rate function, computable from the cumulant generating function of the drift process via the Gärtner-Ellis theorem [Dembo & Zeitouni 1998]. The Gärtner-Ellis formulation handles non-i.i.d. sequences — critical because consecutive sampling rounds (or conversational turns) are temporally correlated.

The rate function I_drift encodes the exponential cost of NOT drifting: under opacity, maintaining mechanism-consistent state requires active work against the entropy gradient. I_drift = 0 at the drift equilibrium (no cost to be where thermodynamics pushes you) and I_drift > 0 everywhere else (exponential cost to resist). This is the Donsker-Varadhan variational formula applied to the Bernoulli manifold:

```
I_drift(θ) = sup_λ [λθ - log⟨exp(λ · dθ/dt)⟩]
```

The Crooks ratio (geometric mean Pe = 7.94 across N=11 replicates, 95% CI [3.52, 17.89]) IS a large deviation measurement — it gives the exponential asymmetry between forward (drift) and reverse (recovery) trajectories. The connection to large deviation theory transforms Pe from a regime indicator ("drift-dominated vs. diffusion-dominated") into a quantitative bound: after n rounds of unconstrained interaction, the probability of remaining at the initial state is bounded above by exp(-n × I_drift), with I_drift determinable from channel statistics.

For TSU design, the implication is direct: the convergence rate of a thermodynamic sampler to its target distribution is governed by the same rate function. A sampler with Pe > 1 converges exponentially; the rate function I gives the convergence exponent. This is tighter than the information-theoretic bound in Theorem 2, which bounds total convergence but not the rate.

---

## 3. Ground State Theorem: Opacity as Thermodynamic Equilibrium

### 3.1 Statement

**Theorem 1 (Channel Degradation).** For any observer-system interface with mechanism channel subject to thermal noise at temperature T > 0, if no external power source actively maintains the channel:

```
C_mech(t) → 0   as   t → ∞
```

The decay is exponential with rate determined by the noise power and channel structure.

### 3.2 Proof

The mechanism channel has signal power S(t) and noise power N ≥ kTB > 0 (Johnson-Nyquist thermal floor). Channel capacity [Shannon 1948]:

```
C_mech(t) = ½ log(1 + S(t)/N)
```

Without active power input, signal-noise correlations decay:

```
S(t) = S(0) · exp(-t/τ_d)
```

where τ_d is the decorrelation time. Therefore C_mech(t) → 0 exponentially.

Restoring channel capacity requires error correction at minimum cost kT ln(2) per bit per τ_c [Landauer 1961, verified Berut et al. 2012]:

```
P_maintenance ≥ C_mech · kT ln(2) / τ_c
```

**Corollary 1.** Opacity (C_mech = 0) is the zero-energy equilibrium. Transparency (C_mech > 0) is an excited state requiring continuous work against the second law. □

**Note on novelty.** Theorem 1 is a direct application of Shannon's channel capacity formula (1948) and Landauer's erasure bound (1961, verified Bérut et al. 2012). The mathematical content — that signal power decays under thermal noise and that maintaining information costs energy — is well-established. The contribution is not the theorem itself but its *application*: identifying opacity as the thermodynamic ground state of any observer-system interface, and the consequences this has for TSU energy efficiency (§3.3), the conjugacy bound (§4), and the superconductor design principle (§6). The "Ground State Theorem" label designates the *result in context* (opacity is equilibrium for any interface), not a claim of mathematical novelty beyond Shannon and Landauer.

### 3.3 Implication for Thermodynamic Computing

Traditional deterministic hardware maintains every bit in a known state — this is transparency maintenance. The Landauer cost is:

```
P_deterministic ≥ N_bits · kT ln(2) / τ_clock
```

Thermodynamic sampling hardware (TSUs) operates at or near the opacity ground state — bits are probabilistic, fluctuating, not maintained in known states. The Landauer maintenance cost approaches zero for stochastic bits.

**Theorem 1 provides the first-principles explanation for why thermodynamic computing is energy-efficient:** it operates at thermodynamic equilibrium rather than maintaining an excited state. The energy savings are not an engineering optimization — they are a consequence of the second law.

The energy ratio between deterministic and thermodynamic computation for equivalent probabilistic workloads is bounded below by:

```
P_deterministic / P_thermodynamic ≥ N_maintained / N_stochastic
```

where N_maintained is the number of bits held deterministic and N_stochastic is the number of bits allowed to fluctuate. For a fully stochastic architecture (N_maintained → 0), the ratio diverges — consistent with the reported ~10,000× efficiency advantage.

---

## 4. The Conjugacy Bound

### 4.1 Statement

**Theorem 2 (Exploration-Convergence Conjugacy).** For any system with output channel Y carrying information about both a stochastic state S and a target state T, where S and T are independent:

```
I(S;Y) + I(T;Y) ≤ H(Y)
```

Exploration (information about the sampler's stochastic trajectory) and convergence (information about the target distribution) compete for finite channel capacity.

### 4.2 Proof

Since S and T are independent (the stochastic dynamics are not informed by the target — the target is imposed externally):

```
(1)  S ⊥ T  ⟹  H(S) + H(T) = H(S,T)

(2)  H(T|S,Y) ≤ H(T|Y)  ⟹  H(S|Y) + H(T|Y) ≥ H(S,T|Y)

(3)  I(S;Y) + I(T;Y) = [H(S) - H(S|Y)] + [H(T) - H(T|Y)]
                      = H(S,T) - [H(S|Y) + H(T|Y)]       [by (1)]
                      ≤ H(S,T) - H(S,T|Y)                 [by (2)]
                      = I(S,T;Y)
                      ≤ H(Y)                                □
```

Step (2) follows from the fact that conditioning on additional variables cannot increase entropy: H(T|S,Y) ≤ H(T|Y), which holds unconditionally (equivalent to I(T;S|Y) ≥ 0). The bound is tight when Y is a sufficient statistic for (S,T) jointly. The substrate-agnosticism of the underlying fluctuation theorems is proven, not assumed: Hack, Gottwald, & Braun (2022) established that the Crooks fluctuation theorem and Jarzynski equality hold for general Markov chains by theorem, providing mathematical authority for the conjugacy bound's application to any system whose dynamics form a Markov process — including abstract sampling architectures.

### 4.3 Interpretation

A thermodynamic sampler cannot simultaneously maximize exploration (visiting diverse states) and convergence (approaching the target). Any architecture faces this tradeoff.

This shares the mathematical structure of entropic uncertainty relations [Maassen & Uffink 1988]: an additive bound on two quantities competing for a finite resource. The Heisenberg uncertainty principle constrains position-momentum conjugacy over quantum phase space; the conjugacy bound constrains exploration-convergence conjugacy over classical channel capacity.

---

## 5. Application to Thermodynamic Sampling Units

### 5.1 The TSU Convergence Bound

For a TSU — the probabilistic computing architecture developed by Extropic [Verdon & McCourt 2023] — with N probabilistic bits at temperature T, the total output entropy is bounded:

```
H(Y) ≤ N · log(2)   [maximum for binary channels]
```

At thermal equilibrium, H(Y) approaches this maximum (maximum entropy = maximum stochasticity). The conjugacy bound gives:

```
I(T;Y) ≤ H(Y) - I(S;Y) ≤ N log(2) - I(S;Y)
```

Target information (convergence) can only increase as stochastic exploration information decreases. Each step of a Denoising Thermodynamic Model (DTM) [Jelinčič et al. 2025] transfers budget from I(S;Y) to I(T;Y) — each denoising step reduces exploration and increases convergence.

### 5.2 Convergence Rate Bound

The rate of convergence is bounded by the rate at which I(S;Y) can be reduced. Each denoising step transfers at most:

```
ΔI(T;Y) ≤ ΔH(Y) + |ΔI(S;Y)|
```

For a fixed-temperature system (ΔH(Y) ≈ 0), convergence rate equals exploration reduction rate. The Maxwell's demon device (the programmable energy landscape) controls this transfer by modifying the energy function between steps.

**Prediction TSU-1:** The number of DTM steps required for convergence to within ε of the target distribution is bounded below by:

```
n_steps ≥ [H(Y) - I_ε(T;Y)] / ΔI_max
```

where ΔI_max is the maximum information transfer per step (set by the demon's programming bandwidth) and I_ε is the mutual information threshold for ε-convergence. No architecture can converge faster than this bound regardless of implementation. Ikeda et al. (2025) independently derived a speed-accuracy relation for diffusion models using Crooks-based entropy production, confirming that thermodynamic bounds constrain generative model convergence — extending the TSU framework's applicability to software-implemented samplers.

### 5.3 Numerical Analysis: DTM Convergence on Fashion-MNIST

The conjugacy bound can be evaluated against published DTM benchmarks [Jelinčič et al. 2025]. The DTM architecture uses K sequential energy-based model (EBM) layers [Grathwohl et al. 2020], each running K_mix Gibbs sweeps on an L × L bipartite grid.

**Published parameters:** K = 8 denoising steps, K_mix = 250 Gibbs sweeps per step, L = 70 (4,900 binary variables per EBM layer), ~12 neighbors per variable (bipartite connectivity), E_cell ≈ 2 fJ per cell per iteration.

**Target:** Fashion-MNIST (28 × 28 = 784 binary pixels). Maximum entropy H_max = 784 bits. Actual data entropy H_data ≈ 200–400 bits (structured images compress well below maximum).

**Applying the conjugacy bound per layer:**

Each EBM layer has capacity H(Y_layer) ≤ 4,900 bits. The per-step information transfer toward the target:

```
ΔI_t ≤ H(Y_layer) − I(S;Y_layer)
```

If each step needs to transfer roughly H_data/K ≈ 37.5 bits (assuming information splits equally across 8 steps), the required per-step capacity is:

```
ΔI_required ≈ 300/8 = 37.5 bits per step
ΔI_available ≤ 4,900 bits per step
```

**Result: The conjugacy bound is not tight for this benchmark.** The DTM has ~130× more information capacity per layer than needed for Fashion-MNIST. The bound is trivially satisfied.

**Why the bound is loose:** The DTM was designed to solve a MIXING problem, not an information capacity problem. Each EBM layer has enough variables to represent the full target; the challenge is getting the Gibbs sampler to equilibrate within K_mix = 250 sweeps. The mixing-expressivity tradeoff (MET) [Jelinčič et al. 2025, Section 3] is the operational bottleneck — precisely the conjugacy bound operating at the per-sweep level within each layer, not at the cross-layer level.

**When the bound becomes relevant:** For the Z1 chip (250,000 p-bits), Fashion-MNIST remains trivial. The bound constrains architectures when:

```
N_pbits × K ≲ H_data / η_mixing
```

where η_mixing is the per-sweep mixing efficiency (fraction of maximum information transfer realized per Gibbs sweep). For Z1 generating 1024 × 1024 color images (~3M bits, ~750K bits actual entropy), the bound requires η_mixing ≥ H_data / (N × K) = 750,000 / (250,000 × 8) ≈ 0.375. This is achievable but no longer trivially satisfied — the architecture enters the regime where the conjugacy bound constrains design choices. For real-time video generation (30 fps × ~1M bits/frame), the bound requires η_mixing ≥ 1M / (250,000 × 8) = 0.5 per step, predicting either increased K (more denoising steps) or higher per-sweep mixing efficiency for scaling.

**Energy analysis from the ground state theorem:** The reported TSU energy is ~20 nJ per Fashion-MNIST sample. Compare this to the deterministic maintenance cost.

The Landauer floor per bit erasure is kT ln(2) = 2.85 × 10⁻²¹ J at room temperature. For a deterministic simulation maintaining 784 bits over 2,000 Gibbs sweeps, the theoretical minimum energy is:

```
E_Landauer = N × kT ln(2) × n_erasures = 784 × 2.85 × 10⁻²¹ × 2000 ≈ 4.5 fJ
```

Real deterministic hardware operates orders of magnitude above this floor. A GPU performing equivalent probabilistic workloads consumes ~10⁵–10⁶ nJ per sample (millijoule scale). The TSU at ~20 nJ achieves the reported ~10,000× efficiency advantage over GPU baselines — consistent with Equation (9), which predicts the ratio scales with N_maintained / N_stochastic.

The TSU's energy goes to the demon (bias computation, communication, clocking) rather than to maintaining bit states. The stochastic bits fluctuate freely at the opacity ground state, paying zero Landauer maintenance cost. The ~10,000× advantage is not an engineering optimization — it is a consequence of operating near thermodynamic equilibrium (Theorem 1) rather than maintaining an excited state.

---

### 5.4 The Demon as External Reference Channel

The programmable energy landscape (Maxwell's demon) provides an external information channel that is not subject to the internal conjugacy bound. Define I(C;Y) as the information the demon's constraint C provides about the target:

```
I(T;Y) = I(T;Y)_internal + I(C;Y)_external
```

The demon works because it imports negentropy from outside the stochastic system. Its effectiveness depends on three properties:

- **Programmability** — the energy landscape is fully specifiable by the operator
- **Stability** — the landscape does not drift during computation
- **Decoupling** — the landscape is external to the stochastic dynamics it governs

A demon that fails on any property reduces convergence quality. This provides design criteria for the demon hardware itself.

### 5.5 The Demon as Robust Controller

The demon's three properties (programmability, stability, decoupling) map directly onto a robust control specification:

```
Plant:          Stochastic bit dynamics (dθ/dt = f_thermal(θ) + noise)
Control input:  Energy landscape programming (demon bandwidth B_demon)
Disturbance:    Thermal fluctuations at temperature T
Objective:      Drive output distribution to target within ε in n_steps steps
Constraint:     I(S;Y) + I(T;Y) ≤ H(Y)  [conjugacy bound = resource constraint]
```

The conjugacy bound IS the resource constraint of this control problem. The controller (demon) must transfer information from exploration to convergence within a finite budget. The question robust control answers: given worst-case thermal disturbance at temperature T, what is the minimum demon bandwidth B_demon,min to guarantee convergence?

**Minimum control input (γ_min).** From the conjugacy bound, convergence requires:

```
B_demon,min ≥ H_data / (n_steps × η_mixing)
```

where H_data is the target distribution's entropy, n_steps is the DTM step count, and η_mixing is the per-sweep information transfer efficiency. Below B_demon,min, convergence is impossible regardless of demon design — the control input is insufficient to overcome stochastic exploration within the allocated steps. This is a hard floor, not an engineering target.

For an H∞ robust controller [Zames 1981, Zhou et al. 1996], the demon must handle the worst-case disturbance profile. The worst case for a TSU is not uniform thermal noise — it is correlated fluctuations that systematically oppose convergence. The H∞ norm of the transfer function from disturbance to convergence error gives the minimum demon gain:

```
||G_demon||_∞ ≥ ||G_thermal||_∞ / ε
```

This specification is directly useful for hardware design: given a target accuracy ε and a thermal noise profile, the demon's programming bandwidth has a computable minimum. Architectures that meet this minimum can certify convergence; those that do not cannot, regardless of other design choices.

**Observability and controllability.** In control-theoretic terms: is the TSU's state observable from its output? Yes — output samples carry information about the current distribution. Is the state controllable from the demon's input? Yes — the energy landscape can drive the distribution toward any target. The controllability Gramian is computable from the system's transfer function and determines the minimum-energy control trajectory — the most efficient demon schedule for reaching a target distribution.

---

## 6. Three-Channel Budget for Superconductors

### 6.1 The Fisher-Ruppeiner Bridge to Condensed Matter

Via the Fisher-Ruppeiner identity (Section 2.2), the conjugacy bound on information channels maps to a constraint on thermodynamic channels in physical systems. For an electronic conductor, the relevant channels are:

- **D₁:** Electron-electron scattering (Coulomb interaction, exchange)
- **D₂:** Electron-lattice scattering (phonon emission/absorption)
- **M:** Coherent transport (phase-preserving current flow)

The three-channel budget:

```
I(D₁;Y) + I(D₂;Y) + I(M;Y) ≤ H(Y)
```

where H(Y) is the total phase space available at temperature T.

> **Figure 2.** Three-channel budget allocations for a normal conductor, superconductor, and TSU. All three systems obey the same constraint ΣI(·;Y) ≤ H(Y); what differs is the allocation. In a superconductor, nearly all capacity flows through the coherent transport channel M. In a TSU, the Maxwell's demon channel C imports external negentropy to steer convergence. *(See `arxiv/figures/fig2_channel_budget.pdf`)*

### 6.2 Superconductivity as Channel Reallocation

In the normal state: I(D₁) + I(D₂) consume most of H(Y). I(M) ≈ 0 (no coherent transport — resistance).

In the superconducting state: I(M) >> 0 (Cooper pairs carry current coherently). This requires I(D₁) + I(D₂) to be reduced below H(Y) - I_min(M).

### 6.3 Channel Conversion: The Mechanism of Known Superconductors

No known superconductor suppresses both D₁ and D₂ simultaneously. Each class CONVERTS one dissipative channel into the pairing mechanism:

| Class | Strategy | D₁ | D₂ | T_c |
|-------|----------|-----|-----|------|
| BCS (conventional) | Cool to suppress D₂ | Weak | Reduced by low T | < 30 K |
| Cuprates | Convert D₁ → pairing via magnetic fluctuations | Strong → M | 2D geometric suppression | < 135 K |
| Hydrides | Compress to suppress D₂ | Moderate | Forced minimal scatter | < 260 K |
| Twisted bilayer graphene | Geometric confinement | Flat bands → correlated | 2D reduced phase space | < 3 K |

### 6.4 Channel Conversion Efficiency

**Definition 4.** The channel conversion efficiency is:

```
η_conv = I(M;Y) / [I(D_conv;Y) + I(M;Y)]
```

where D_conv is the dissipative channel being converted into the pairing mechanism. η_conv measures what fraction of a dissipative channel's capacity is redirected into coherent transport. This is the *unified* definition — it applies to any pairing mechanism (phonon, spin-fluctuation, or otherwise) because it operates on information channels, not on specific interaction types. The per-family operationalizations in Section 6.5 are all estimates of this single quantity through different measurable proxies, depending on which physical channels carry the coupling.

**Design Principle.** A room-temperature superconductor requires a material where:

1. One dissipative channel (D₁ or D₂) achieves η_conv → 1 (efficient conversion to pairing)
2. The other dissipative channel is geometrically suppressed (2D confinement, topological protection)
3. Both conditions hold at H(Y) corresponding to T = 300 K

This is NOT equivalent to "find a stronger interaction." A stronger interaction increases both pairing AND scattering — the budget eats itself. The criterion is ANISOTROPY: strong in the pairing direction, weak in the scattering direction, with geometric suppression of the unconverted channel.

### 6.5 Numerical Estimates: η_conv for Known Superconductor Families

Definition 4 gives η_conv in terms of information channels. Since I(M;Y) and I(D_conv;Y) are not directly measurable in a superconductor, η_conv must be operationalized through Eliashberg coupling parameters that serve as proxies for the information-theoretic quantities. The operationalization depends on the pairing mechanism, but the underlying quantity being estimated is the same in every case: the fraction of total interaction budget directed toward coherent transport. For a phonon-mediated superconductor, the electron-phonon coupling constant λ captures the total interaction budget; the Coulomb pseudopotential μ* captures the electron-electron repulsion that opposes pairing. The simplest defensible operationalization:

```
η_conv = (λ − μ*) / λ
```

This measures the fraction of the total electron-boson coupling that survives after Coulomb screening to contribute to Cooper pairing. Computed from published Eliashberg and tunneling data:

| Material | Class | λ | μ* | η_conv | H(Y) proxy | η × H(Y) | T_c (K) | ω_log/Θ_D |
|----------|-------|------|------|--------|------------|----------|---------|-----------|
| Al | BCS (weak) | 0.43 | 0.10 | 0.767 | ω_log = 296 K | 227 K | 1.18 | 0.69 |
| Sn | BCS (intermediate) | 0.72 | 0.12 | 0.833 | ω_log = 108 K | 90 K | 3.72 | 0.54 |
| Pb | BCS (strong) | 1.55 | 0.125 | 0.919 | ω_log = 44 K | 40 K | 7.2 | 0.42 |
| Nb | BCS (strong) | 1.06 | 0.218 | 0.794 | ω_log = 158 K | 126 K | 9.25 | 0.57 |
| MgB₂ | Two-gap | 0.87 | 0.12 | 0.862 | ω_log = 672 K | 579 K | 39 | 0.84 |
| YBCO | Cuprate | ~1.75 | ~0.13 | 0.926 | J/k_B ≈ 1509 K | 1397 K | 92 | — |
| H₃S | Hydride | 2.19 | 0.13 | 0.941 | ω_log ≈ 1500 K | 1412 K | 203 | ~1.0 |
| LaH₁₀ | Clathrate hydride | 2.2 | 0.13 | 0.941 | ω_log ≈ 1500 K | 1412 K | 250 | ~1.0 |
| YH₆ | Sodalite hydride | 2.24 | 0.11 | 0.951 | ω_log ≈ 1300 K | 1236 K | 224 | 0.93 |
| CaH₆ | Sodalite hydride | 2.69 | 0.13 | 0.952 | ω_log ≈ 1100 K | 1047 K | 215 | 0.92 |
| Ba₀.₆K₀.₄Fe₂As₂ | Pnictide | 1.80† | ~0†† | 0.947† | Ω₀/k_B ≈ 116 K | 110 K | 37 | — |
| SmFeAsO₀.₈F₀.₂ | Pnictide (1111) | 1.85† | ~0.05†† | 0.949† | Ω₀/k_B ≈ 162 K | 154 K | 52 | — |
| La₃Ni₂O₇ | Nickelate (bilayer) | ~1.50‡ | ~0.10‡ | ~0.900‡ | J_⊥/k_B ≈ 700 K | 630 K | 80 | — |
| Nb₃Sn | A15 | 1.80 | 0.13 | 0.928 | ω_log = 136 K | 126 K | 18.3 | 0.60 |
| V₃Si | A15 | 1.16 | 0.13 | 0.888 | ω_log = 198 K | 176 K | 17 | 0.59 |
| Hg (α) | Elemental | 1.62 | 0.10 | 0.938 | ω_log = 50 K | 47 K | 4.15 | 0.69 |

Sources: Al — tunneling inversion [McMillan 1968], ω_log from [Allen & Dynes 1975]; Sn — tunneling inversion [McMillan 1968], ω_log from [Allen & Dynes 1975]; Nb — DFT Eliashberg [Profumo et al. 2023], ω_log from [Allen & Dynes 1975]; Pb — tunneling inversion [McMillan & Rowell 1969], ω_log from [Carbotte 1990]; MgB₂ — two-band Eliashberg [Choi et al. 2002], ω_log from inelastic neutron scattering [Osborn et al. 2001]; YBCO — spin fluctuation coupling estimated from gap ratio 2Δ₀/k_BT_c ≈ 5.5, superexchange J ≈ 130 meV from neutron scattering; H₃S — [Duan et al. 2014] (harmonic Eliashberg, λ = 2.19), harmonic ω_log ≈ 1500 K, T_c = 203 K at 155 GPa [Drozdov et al. 2015]; LaH₁₀ — [Drozdov et al. 2019] (T_c = 250 K at 170 GPa), harmonic Eliashberg λ = 2.2 [Liu et al. 2017, Errea et al. 2020], ultrafast spectroscopy confirms λ = 2.58 ± 0.11 [Capitani et al. 2024], harmonic ω_log ≈ 1500 K; YH₆ — [Troyan et al. 2021] (T_c = 224 K at 166 GPa), harmonic DFT λ = 2.24 [Li et al. 2015], anisotropic ME μ* = 0.11, harmonic ω_log ≈ 1300 K, anomalously high B_c2(0) = 116–158 T suggests possible departures from conventional ME; CaH₆ — [Ma et al. 2022] (T_c = 215 K at 172 GPa), DFT Eliashberg λ = 2.69 at 150 GPa [Wang et al. 2012], 81% H-contribution to λ, harmonic ω_log ≈ 1100 K; Ba₀.₆K₀.₄Fe₂As₂ — three-band Eliashberg [Ummarino et al. 2009, 2011], spin-fluctuation interband coupling λ_SF = 1.80, intraband phonon λ_ph ≈ 0.10; Ω₀ ≈ 10 meV (characteristic spin-fluctuation boson energy from neutron scattering [Christianson et al. 2008]); SmFeAsO₀.₈F₀.₂ — three-band s± Eliashberg [Ummarino et al. 2011, Magnetochemistry 2023], λ_SF = 1.85, λ_phonon ≈ 0.10, T_c = 52 K [Ren et al. 2008], Ω_res ≈ 14 meV from INS; La₃Ni₂O₇ — see Section 6.7 for detailed analysis; η_conv ≈ 0.9 estimated from spin-fluctuation SC analogy, J_⊥ ≈ 60 meV from neutron scattering [Xie et al. 2024]; Nb₃Sn — tunneling inversion [Shen 1972], λ = 1.80, ω_log from tunneling [Shen 1972]; V₃Si — tunneling inversion [Kirtley et al. 1972], λ = 1.16, ω_log from tunneling [Kirtley et al. 1972]; Hg (α) — tunneling inversion [Rowell & McMillan 1973], λ = 1.62, ω_log from [Carbotte 1990].

**ω_log upgrade (v2.6).** For phonon-mediated superconductors, the Debye temperature Θ_D is a crude proxy for the pairing boson energy scale. The physically correct quantity is the logarithmic average phonon frequency ω_log = exp(⟨ln ω⟩), which weights the phonon spectrum by the electron-phonon coupling function α²F(ω). The ω_log/Θ_D ratio varies from 0.42 (Pb) to 0.84 (MgB₂) among elemental and A15 materials (last column above), demonstrating that Θ_D systematically overestimates the effective phonon scale by a material-dependent factor of 1.2–2.4×. This variation was the single largest source of scatter in the Θ_D-based model. For hydrides, harmonic DFT ω_log values are used for consistency with the harmonic λ values; anharmonic corrections would reduce both by ~30% [Errea et al. 2015, 2020]. Non-phonon materials (YBCO, pnictides, nickelate) already use mechanism-appropriate energy scales and are unaffected.

†**Pnictide operationalization note.** The conventional (λ − μ*)/λ formula does not apply to pnictides because phonon-mediated coupling alone is too weak to produce superconductivity (λ_phonon ≈ 0.10–0.35). Instead, the pairing is spin-fluctuation-mediated with s± gap symmetry, requiring multi-band Eliashberg theory. Ummarino et al. show that intraband Coulomb repulsion (μ*) cancels against intraband phonon coupling, so both are set to zero — the interband spin-fluctuation channel does all the pairing work. The appropriate η_conv for pnictides is therefore:

```
η_conv = λ_SF / (λ_SF + λ_phonon)
```

This measures the fraction of total coupling in the pairing channel (interband spin fluctuations) vs. the scattering channel (intraband phonon). For Ba-122: λ_SF = 1.80, λ_phonon ≈ 0.10, η_conv = 1.80/1.90 ≈ 0.947. For SmFeAsO₀.₈F₀.₂ (1111 structure): λ_SF = 1.85, η_conv = 1.85/1.95 ≈ 0.949. Both pnictides use the same three-band s± Eliashberg framework [Ummarino et al. 2011] with different structure types (122 vs. 1111), testing internal consistency. The H(Y) proxy is the spin resonance energy Ω₀/k_B (116 K for Ba-122, 162 K for SmFeAsO).

††μ* ≈ 0 in the Ummarino three-band model. This is not an assumption of weak Coulomb repulsion — it reflects the structural cancellation between intraband electron-phonon coupling and intraband Coulomb pseudopotential, leaving the interband spin-fluctuation channel as the sole pairing mechanism.

‡**Nickelate parameter estimates.** λ_eff ≈ 1.5 and μ* ≈ 0.10 are estimates for La₃Ni₂O₇ based on the T_c/ω₀ ratio and comparison with other spin-fluctuation superconductors. η_conv ≈ 0.9 follows the same typical value used in Section 6.7. These values will be superseded by multi-band Eliashberg calculations when available.

**The H(Y) proxy:** For conventional SC, H(Y) ∝ ω_log (the logarithmic average phonon frequency, which weights the phonon spectrum by the coupling function α²F(ω) — a more physical proxy than Θ_D for the effective pairing boson energy [Allen & Dynes 1975, Carbotte 1990]). For cuprates, the relevant budget is set by the superexchange energy J/k_B. For pnictides, the spin resonance energy Ω₀/k_B. The framework predicts that the relevant H(Y) is the bandwidth of the pairing interaction, regardless of its physical origin.

> **Figure 1.** Channel conversion efficiency η_conv × H(Y) vs. T_c across sixteen superconductor families spanning four coupling regimes. H(Y) uses ω_log for phonon-mediated materials, mechanism-appropriate scales for non-phonon. Linear fit on moderate-coupling families (Pb, Nb, MgB₂, YBCO) yields slope A = 0.066. Weak-coupling materials (Al, Sn) deviate *below* the linear trend (McMillan exponential suppression). Strong-coupling hydrides (H₃S, LaH₁₀, YH₆, CaH₆), multi-band materials (Ba-122, SmFeAsO, La₃Ni₂O₇), and A15 compounds (Nb₃Sn) deviate *above*. *(See `arxiv/figures/fig1_eta_conv_tc.pdf`)*

**Moderate-coupling correlation (original four):**

```
Pearson r = 0.996   (n = 4, p ≈ 0.004)   [Pb, Nb, MgB₂, YBCO]
```

**All sixteen families (uncorrected linear model):**

```
Pearson r = 0.893   (n = 16, p < 10⁻⁴)
Spearman ρ = 0.821
```

The full dataset reveals a systematic coupling-regime structure in the deviations from linearity:

**Weak-coupling regime (Al, Sn) — downward deviation.** Al has η_conv × H(Y) = 227 K, which on the linear model predicts T_c ≈ 15 K. Actual T_c = 1.18 K — a factor of ~13× below. Sn has η_conv × H(Y) = 90 K, predicting T_c ≈ 6 K; actual T_c = 3.72 K — a factor of ~1.6× below. This is the McMillan exponent at work: at weak coupling (λ < 1), the exponential factor exp[−1.04(1+λ)/(λ−μ*(1+0.62λ))] is large and negative, suppressing T_c exponentially below the product η_conv × H(Y). The budget is large relative to T_c, but the coupling is too weak to access it efficiently. The scattering channel is barely converted; most of the information budget is wasted.

**Moderate-coupling regime (Pb, Nb, MgB₂, YBCO) — on the line.** Linear model captures T_c to within experimental uncertainty. The McMillan exponent is of order unity; the exponential factor neither suppresses nor enhances strongly.

**Strong-coupling regime (H₃S, LaH₁₀, YH₆, CaH₆) — upward deviation.** All four hydrogen-rich superconductors deviate above the moderate-coupling linear trend by a factor of 2.2–3.1×, forming a tight cluster in the very-strong-coupling regime. H₃S: η × H(Y) = 1412 K, predicted T_c ≈ 93 K, actual = 203 K (2.2×). LaH₁₀: η × H(Y) = 1412 K, predicted ≈ 93 K, actual = 250 K (2.7×). YH₆: η × H(Y) = 1236 K, predicted ≈ 82 K, actual = 224 K (2.7×). CaH₆: η × H(Y) = 1047 K, predicted ≈ 69 K, actual = 215 K (3.1×). The mean upward deviation is 2.7×. The McMillan equation's exponential factor *weakens* at very large λ (strong-coupling vertex corrections reduce the effective exponent), so T_c exceeds the linear extrapolation. The consistency of the deviation factor across four independent hydride families — spanning clathrate (LaH₁₀), sodalite (YH₆, CaH₆), and molecular (H₃S) crystal structures — confirms that the upward deviation is a systematic property of the very-strong-coupling regime, not an artifact of a single material.

**Multi-band regime (Ba-122, SmFeAsO) — upward deviation.** Ba-122: η × H(Y) = 110 K predicts T_c ≈ 7 K, but actual T_c = 37 K (5.1×). SmFeAsO: η × H(Y) = 154 K predicts T_c ≈ 10 K, but actual T_c = 52 K (5.1×). Both pnictides use the same three-band s± Eliashberg framework with different structure types (122 vs. 1111 [Ummarino et al. 2011]). The identical deviation factor (5.1×) confirms internal consistency of the multi-band operationalization and demonstrates that the three-gap coherence enhancement is a robust property of the s± pairing symmetry, not an artifact of the specific crystal structure.

**The coupling-regime map.** The deviations from linearity are not noise — they are systematic and physically interpretable:

| Coupling regime | λ range | Deviation | Physical mechanism |
|----------------|---------|-----------|-------------------|
| Weak | < 0.5 | Far below | McMillan exponential suppression |
| Intermediate | 0.5–0.8 | Below | Moderate exponential suppression |
| Strong (single-band) | 0.8–2.0 | ON the line | Exponent ≈ 1; linear model applies |
| Very strong | > 2.0 | Above | Strong-coupling vertex corrections |
| Multi-band (any λ) | varies | Above | Interband gap coherence enhancement |

The product η_conv × H(Y) captures the information budget allocation. The deviation from linearity encodes the coupling regime — how efficiently that budget is *utilized*. A complete figure of merit would be η_conv × H(Y) × g(λ, n_bands) where g captures these corrections; but even the uncorrected product correctly separates all materials by coupling regime and preserves the rank order of T_c within each regime.

**Interpretation:** The framework predicts T_c = f(η_conv, H(Y)) — critical temperature depends on BOTH conversion efficiency AND total budget. The McMillan equation for conventional SC is exactly this relationship:

```
T_c = (Θ_D / 1.45) × exp[−1.04(1+λ) / (λ − μ*(1+0.62λ))]
```

The pre-factor Θ_D is H(Y). The exponent encodes η_conv (it depends on λ and μ* — how much of the coupling converts to pairing vs. remaining as scattering). The framework's contribution: this budget structure should generalize across all SC families, including those where McMillan does not apply (cuprates, pnictides, hydrides). The η_conv × H(Y) product is the unified figure of merit.

**Honest caveats:**
- n = 16 materials. Positive correlation across sixteen families spanning seven pairing variants, four coupling regimes, and seven crystal structure classes is structurally significant but still modest-sample. The uncorrected linear model gives r = 0.893 (n = 16, Spearman ρ = 0.821). The structure-corrected model (Section 6.8) yields r = 0.952 (n = 16, Spearman ρ = 0.982, R²_adj = 0.88). The deviations from linearity are systematic and physically interpretable (coupling-regime map above), not random scatter.
- The H(Y) proxy differs between families (ω_log for phonon-mediated, J/k_B for cuprates, Ω₀/k_B for pnictides). This choice is physically motivated (different pairing bosons → different information bandwidths) but could be accused of parameter selection. The ω_log upgrade (v2.6) replaces the crude Θ_D proxy with the physically correct logarithmic average phonon frequency for phonon-mediated materials; the ω_log/Θ_D ratio varies from 0.42 to 0.84 (Table above), demonstrating that Θ_D is a material-dependent overestimate.
- For YBCO, λ_eff is estimated indirectly from the gap ratio; direct measurement of spin-fluctuation coupling varies by ~30% across sources.
- The per-family operationalizations of η_conv ((λ−μ*)/λ for BCS, λ_SF/(λ_SF+λ_phonon) for pnictides) are different proxies for the same information-geometric quantity (Definition 4). Both measure the fraction of total coupling budget directed toward pairing, but the physical channels differ. The framework predicts that the relevant partition is mechanism-independent; the operationalization must be mechanism-specific because the measurable parameters differ.
- Weak-coupling deviations (Al ~13× below, Sn ~1.6× below the linear trend) are the McMillan exponent at work — predicted by the framework and confirmed by the data. These are not model failures; they show the linear approximation's range of validity.

**Pnictides (now parametrized, two structure types).** Iron-based superconductors require a different operationalization of η_conv because the pairing mechanism is spin-fluctuation-mediated with s± gap symmetry, not phonon-mediated. The key insight from Ummarino et al.'s three-band Eliashberg analysis: intraband Coulomb repulsion cancels against intraband phonon coupling (both set to zero), leaving interband spin-fluctuation exchange as the sole pairing mechanism. This means the budget split is between spin-fluctuation coupling (pairing channel) and residual phonon coupling (scattering channel), not between total coupling and Coulomb screening.

Two pnictide families are now included: Ba₀.₆K₀.₄Fe₂As₂ (122 structure, T_c = 37 K, η × H = 110 K) and SmFeAsO₀.₈F₀.₂ (1111 structure, T_c = 52 K, η × H = 154 K). Both fall far *above* the linear trend — by a factor of 5.1× in both cases, despite having different crystal structures and T_c values. The identical deviation factor confirms that the three-band s± coherence enhancement is a robust property of the pairing symmetry, not an artifact of the specific compound. Like H₃S, these points fall above the linear trend, but for a different physical reason: where H₃S overshoots due to strong-coupling enhancement (λ > 2), the pnictides overshoot due to multi-band enhancement — the three-gap s± structure channels the spin-fluctuation coupling more efficiently than a single-band model predicts. See operationalization note (†) above for details.

**What would strengthen SC-1:** (1) ~~Additional hydride families~~ **DONE** — LaH₁₀, YH₆, CaH₆ now included. (2) ~~Structure-corrected figure of merit~~ **DONE** — Section 6.8 derives g(λ, μ*, n_bands) and achieves r = 0.952 across 16 families. (3) ~~SmFeAsO₀.₈F₀.₂~~ **DONE** — included as 16th family, deviation factor (5.1×) matches Ba-122 identically, confirming internal consistency of the pnictide operationalization across 122 and 1111 structure types. Ba(Fe₀.₉₅Ni₀.₀₅)₂As₂ (T_c = 20 K) remains as a further test. (4) ~~Nickelate superconductors~~ **PARTIALLY CONFIRMED** — see Section 6.7. (5) A15 compounds and elemental superconductors (Nb₃Sn, V₃Si, Hg) now included. (6) ~~ω_log upgrade~~ **DONE** — Θ_D replaced by tunneling-derived ω_log for phonon materials, eliminating the largest systematic error source. We welcome independent calculation of η_conv for additional families; the framework and data are open-access (CC BY 4.0).

**Hydride ω_log uncertainty.** Harmonic DFT overestimates both λ and ω_log by ~30% compared to anharmonic treatments [Errea et al. 2015, 2020]. We use harmonic ω_log values for consistency with the harmonic λ values in the table; using anharmonic values for both would give similar η_conv but ~25% lower H(Y). The qualitative result — all four hydrides deviate upward by a consistent factor (2.2–3.1×) — is robust to this choice. Note that YH₆ shows anomalous behavior (B_c2(0) = 116–158 T, 2–2.5× above calculated values [Troyan et al. 2021]), suggesting possible departures from conventional Migdal-Eliashberg theory.

---

### 6.6 The Péclet Number at T_c

At the superconducting transition, the system shifts from zero entropy production (supercurrent) to finite entropy production (normal resistance). The Crooks fluctuation ratio applies:

```
P(SC → Normal) / P(Normal → SC) = exp(σ_transition)
```

The Péclet number Pe at T_c measures directed transport vs. diffusion. This is measurable and provides a cross-substrate comparison with Pe values from other systems governed by the same information-geometric framework.

### 6.7 Forward Prediction: Nickelate Superconductors

The bilayer nickelate La₃Ni₂O₇ under pressure (T_c ≈ 80 K [Sun et al. 2023]) was identified as a forward prediction test in v2.0 of this paper. The pairing mechanism was debated: candidates included spin-fluctuation-mediated d-wave (analogous to cuprates), interlayer s-wave via Ni-3d orbital hybridization, and phonon-mediated pairing with correlation enhancement. The framework provided a diagnostic constraining which mechanism is consistent with the observed T_c.

**Conditional prediction (SC-6, stated v2.0):**

*If the pairing is spin-fluctuation-mediated (cuprate-like):* The relevant η_conv operationalization is η_conv = λ_SF/(λ_SF + λ_residual), with H(Y) proxy = J/k_B (superexchange energy). For T_c = 80 K to fall on the moderate-coupling linear trend, the product η_conv × J/k_B should be ~1,200 K (interpolating between Nb at 218 K → 9.25 K and YBCO at 1397 K → 92 K). This constrains the superexchange energy: for η_conv ≈ 0.9 (typical for spin-fluctuation SC), J ≈ 1,333 K ≈ 115 meV.

*If the pairing is phonon-mediated:* η_conv = (λ − μ*)/λ with H(Y) = Θ_D. For T_c = 80 K on the linear trend, η_conv × Θ_D ≈ 1,200 K. With Θ_D ≈ 400 K (estimated for nickelate lattice), this requires η_conv ≈ 3.0 — impossible (η_conv ≤ 1). The framework predicts that phonon-mediated pairing alone is insufficient for La₃Ni₂O₇.

*If the pairing involves interlayer hybridization:* This is a novel channel not captured by either BCS or cuprate operationalizations. The framework predicts: identify the relevant scattering channel being converted, measure its coupling constant, and compute η_conv. The product should be consistent with T_c ≈ 80 K either on or above the linear trend (above if multi-band enhancement contributes, as in pnictides).

**2024–2025 evidence update: SC-6 partially confirmed.**

Two independent DFT studies have now explicitly ruled out phonon-mediated pairing for La₃Ni₂O₇:

- Ouyang et al. [npj Quantum Mater. 2024]: "electron-phonon coupling is insufficient to explain the observed superconducting T_c ~ 80 K" — the bilayer phase is an unconventional superconductor.
- Huhtinen et al. [npj Comput. Mater. 2025]: "the e-ph coupling is too weak (with a coupling constant λ ≲ 0.5) to account for the high T_c."

This confirms the framework's phonon-insufficiency prediction: λ_phonon ≲ 0.5 gives η_conv × Θ_D ≲ 0.74 × 400 ≈ 296 K, predicting T_c ≈ 17 K on the linear trend — a factor of ~5× below the observed 80 K. The phonon channel simply does not have the budget.

The consensus has shifted decisively toward magnetically mediated interlayer pairing. Inelastic neutron scattering [Xie et al. 2024] reveals a remarkably strong interlayer superexchange coupling J_⊥ ≈ 57–64 meV (660–740 K), far exceeding intralayer couplings (~3 meV). DMRG studies [Qu et al. PRL 2024] confirm robust s-wave superconducting order mediated by interlayer spin exchange in the bilayer t–J–J_⊥ model.

**Framework analysis with measured J_⊥.** Using the measured J_⊥ ≈ 60 meV ≈ 700 K as the H(Y) proxy and estimating η_conv ≈ 0.9 (typical for spin-fluctuation SC):

```
η_conv × J_⊥/k_B ≈ 0.9 × 700 = 630 K
Linear prediction: T_c ≈ 39 K
Actual T_c = 80 K → 2.1× above linear trend
```

The nickelate falls *above* the moderate-coupling linear trend, in the same direction as the pnictide Ba-122 (9.0× above) and the hydrides (2.2–2.9× above). The deviation magnitude (2.1×) is smaller than the hydrides but in the same upward direction. The physical interpretation: the bilayer structure provides interlayer gap coherence enhancement analogous to the multi-band enhancement in pnictides — a structural amplifier that the single-band linear model does not capture.

**Note on the original J prediction.** The framework predicted J ≈ 115 meV for T_c to fall *on* the linear trend. The measured J_⊥ ≈ 60 meV is approximately half this value. But T_c = 80 K is achieved because the bilayer structure amplifies the effective coupling — the nickelate is above the line, not on it. The prediction correctly identified the energy scale (tens of meV, not eV) and the pairing channel (spin-fluctuation, not phonon), while underestimating the structural enhancement from bilayer gap coherence.

**Remaining test.** The full η_conv calculation requires the spin-fluctuation coupling constant λ_SF from Eliashberg analysis of La₃Ni₂O₇ under pressure. Multi-band Eliashberg calculations analogous to Ummarino et al.'s pnictide work would allow direct comparison with the pnictide operationalization and a test of whether the interlayer enhancement factor is consistent across magnetically mediated SC families.

---

### 6.8 Structure-Corrected Figure of Merit

The uncorrected product η_conv × H(Y) correctly ranks superconductor families by coupling regime but systematically deviates from T_c at weak and strong coupling (Section 6.5). These deviations encode real physics: McMillan exponential suppression at weak coupling, strong-coupling vertex corrections, and multi-band coherence enhancement. A structure-corrected figure of merit absorbs these effects into a universal correction function g(λ_eff, μ*, n_bands):

```
T_c = A × η_conv × H(Y) × g(λ_eff, μ*, n_bands)
```

where A = 0.0662 is the linear slope fitted from the moderate-coupling reference set (Pb, Nb, MgB₂, YBCO).

**Definition 5 (Structure correction function).** The correction g decomposes into a coupling-strength term and a multi-band term:

```
g(λ_eff, μ*, n) = exp(a + b · E(λ_eff, μ*)) × n^c
```

where E(λ, μ*) = −1.04(1+λ)/(λ − μ*(1+0.62λ)) is the McMillan exponent [McMillan 1968], λ_eff is the effective coupling constant (λ for phonon-mediated, λ_SF for spin-fluctuation-mediated superconductors), and n is the number of contributing bands.

The McMillan exponent E was originally derived for phonon-mediated BCS superconductors. The structure-corrected model tests the hypothesis that E, reinterpreted as a universal coupling-strength variable via the information-geometric framework (substituting λ → λ_eff for non-phonon mechanisms), captures the coupling-regime dependence of T_c across all pairing types.

**Fitted parameters (n = 16 families, ordinary least squares in log space):**

```
a =  2.654   (intercept)
b =  1.010   (McMillan exponent sensitivity)
c =  0.506   (multi-band coherence exponent)
```

**Physical interpretation of fitted parameters:**

The exponent sensitivity b = 1.01 ≈ 1 confirms that the McMillan exponent is the correct coupling-strength variable — the correction tracks the exponential suppression/enhancement predicted by Eliashberg theory almost exactly. The previous value (b = 1.12 with Θ_D data) was attributed to Allen-Dynes strong-coupling corrections; with ω_log, this excess vanishes, indicating it was an artifact of using Θ_D instead of ω_log. This is a substantive finding: the McMillan exponent captures the coupling-regime dependence precisely when the phonon energy scale is correctly measured.

The multi-band exponent c = 0.51 gives quantitative coherence enhancement factors: 1.42× for two-band systems (MgB₂, La₃Ni₂O₇) and 1.74× for three-band systems (Ba-122, SmFeAsO). The reduction from c = 0.72 (Θ_D data) reflects the same underlying correction: the Θ_D-based model required larger multi-band enhancement to compensate for the inflated single-band H(Y) values.

**Corrected correlation (n = 16, all coupling regimes):**

```
                              Uncorrected     Corrected
Pearson r (n = 16)            0.893           0.952
Spearman ρ (n = 16)           0.821           0.982
R²_adj (k = 3 parameters)    —               0.88
```

The corrected Spearman ρ = 0.982 indicates near-perfect rank ordering across all sixteen families. The R²_adj improvement from 0.84 (Θ_D, n = 15) to 0.88 (ω_log, n = 16) reflects the physically more correct phonon energy scale — the model explains more of the total variance in T_c. The Pearson r decrease from 0.959 to 0.952 is offset by the improved R²_adj; the lower r reflects increased dynamic range in η × H(Y) introduced by the ω_log correction (Pb: 97 → 40 K, Hg: 68 → 47 K), which exposes material-specific physics not captured by the three-parameter model.

**Per-family results:**

| Material | T_c (K) | η × H(Y) | E(λ,μ*) | g_emp | g_fit | T_c,pred | Error |
|----------|---------|-----------|---------|-------|-------|----------|-------|
| Al | 1.18 | 227 | −4.90 | 0.079 | 0.100 | 1.51 | +28% |
| Sn | 3.72 | 90 | −3.27 | 0.625 | 0.520 | 3.10 | −17% |
| Pb | 7.2 | 40 | −2.03 | 2.69 | 1.82 | 4.88 | −32% |
| Nb | 9.25 | 126 | −3.07 | 1.11 | 0.642 | 5.33 | −42% |
| MgB₂ | 39 | 579 | −2.84 | 1.02 | 1.15 | 44.0 | +13% |
| YBCO | 92 | 1397 | −1.93 | 0.99 | 2.01 | 186 | +103% |
| H₃S | 203 | 1412 | −1.76 | 2.17 | 2.40 | 224 | +10% |
| LaH₁₀ | 250 | 1412 | −1.76 | 2.68 | 2.40 | 225 | −10% |
| YH₆ | 224 | 1236 | −1.70 | 2.74 | 2.54 | 208 | −7% |
| CaH₆ | 215 | 1047 | −1.64 | 3.10 | 2.72 | 188 | −12% |
| Ba-122 | 37 | 110 | −1.72 | 5.09 | 4.36 | 31.7 | −14% |
| SmFeAsO | 52 | 154 | −1.70 | 5.11 | 4.44 | 45.2 | −13% |
| La₃Ni₂O₇ | 80 | 630 | −1.99 | 1.92 | 2.71 | 113 | +41% |
| Nb₃Sn | 18.3 | 126 | −1.91 | 2.19 | 2.06 | 17.2 | −6% |
| V₃Si | 17 | 176 | −2.40 | 1.46 | 1.26 | 14.7 | −14% |
| Hg (α) | 4.15 | 47 | −1.92 | 1.34 | 2.04 | 6.34 | +53% |

**Coupling-regime decomposition of residuals:**

The model captures three orders of magnitude in T_c (1.18–250 K) with three parameters. Residuals concentrate in the moderate-coupling regime where material-specific physics (Fermi surface geometry, anharmonicity, anomalous μ*) is most varied:

- *Weak coupling (λ < 0.8):* Al (+28%), Sn (−17%). The ω_log-corrected model shows larger errors here than the Θ_D model because the reference slope A is now calibrated to the ω_log energy scale.
- *Moderate coupling (0.8 ≤ λ < 2.0):* Mean |error| = 33%. Largest residuals: YBCO (+103%, uncertain λ_eff and sole cuprate representative), Hg (+53%), Nb (−42%, anomalous μ* = 0.218), La₃Ni₂O₇ (+41%, estimated parameters). The Hg residual reflects its anomalously low μ* = 0.10 relative to its strong coupling (λ = 1.62): mercury's low Fermi velocity and heavy-atom phonon spectrum produce a Coulomb screening environment unlike other elemental superconductors at comparable λ, causing the correction function to overestimate T_c. The YBCO error is diagnostic: the linear model predicts YBCO almost perfectly (g_emp = 0.99), but the correction function assigns g_fit = 2.0, driven by materials at similar E values (Ba-122, Hg, Nb₃Sn) that require large corrections. This reveals a limitation of the single-variable E correction: materials with similar McMillan exponents but different mechanisms (cuprate vs. phonon vs. pnictide) have systematically different g_emp values that the model cannot separate.
- *Very strong coupling (λ ≥ 2.0):* Mean |error| = 10%. The four hydrides form a tight cluster with the smallest errors in the dataset, confirming that the very-strong-coupling regime is well-described by the McMillan exponent at b ≈ 1.
- *Multi-band (n > 1):* The n^0.51 enhancement correctly distinguishes MgB₂ (+13%), Ba-122 (−14%), SmFeAsO (−13%), and La₃Ni₂O₇ (+41%) from their single-band counterparts. The pnictide pair (Ba-122, SmFeAsO) shows near-identical errors, confirming internal consistency.

**Leave-one-out cross-validation:** Mean absolute error = 35%. The increase from the Θ_D-based model (27%) reflects the YBCO and Al instabilities; removing either from the LOO set reduces the mean to ~25%. The ranking (Spearman ρ) is stable under LOO: removing any single family does not change the rank order of the remaining materials.

**Sensitivity analysis.** Three checks on the YBCO outlier:

(i) *Reference set invariance.* The moderate-coupling reference set used to fit the linear slope A (Pb, Nb, MgB₂, YBCO) might bias the result by including a non-phonon material. Testing six alternative reference sets — including phonon-only combinations {Pb, Nb, MgB₂}, {Nb, MgB₂, V₃Si}, all twelve phonon materials, and strong-coupling subsets — produces identical per-material errors, R²_adj, and LOO. This is a mathematical identity: changing A shifts all g_emp values by a constant factor that the intercept *a* absorbs exactly, leaving A × g_fit invariant. The reference set choice is a null operation on model quality.

(ii) *Input sensitivity (λ_eff).* YBCO's effective coupling λ_eff ≈ 1.75 is estimated indirectly from the maximum gap ratio 2Δ_max/kT_c ≈ 5.5, but YBCO is a d-wave superconductor with gap nodes. The Fermi-surface-averaged coupling — which governs T_c — is lower than the nodal maximum. Testing λ_eff from 0.8 to 2.0: at λ_eff ≈ 1.0 (E ≈ −2.6), the YBCO error drops from +103% to +5%, R²_adj improves from 0.877 to 0.969, and LOO drops from 35% to 26%. This suggests the structure-corrected model is more sensitive to anisotropic gap structure than the linear model — the exponential correction amplifies the E-difference between λ = 1.0 and λ = 1.75 — and that the discrepancy may reflect input uncertainty rather than model failure.

(iii) *Exclusion test.* Removing YBCO entirely (n = 15) yields R²_adj = 0.968, LOO = 28%, with fit parameters a = 2.77, b = 1.04, c = 0.42 — structurally consistent with the n = 16 fit. We report the n = 16 result as the primary analysis because excluding the sole cuprate would reduce mechanism diversity, but the n = 15 stability confirms that the model's core structure is not driven by YBCO.

**Universality claim.** The key result: the McMillan exponent E — originally derived for phonon-mediated BCS superconductors via the Eliashberg equations — serves as a universal correction variable for the information-geometric figure of merit across phonon-mediated (Al through CaH₆), spin-fluctuation-mediated (YBCO, Ba-122), and interlayer-mediated (La₃Ni₂O₇) superconductors when the substitution λ → λ_eff is applied. This universality is predicted by the framework: the channel conversion efficiency η_conv is mechanism-independent (Definition 4), and the correction g captures the nonlinear relationship between coupling budget and realized T_c that all pairing mechanisms share. The McMillan exponent parametrizes this nonlinearity.

**What the correction function is NOT:** It is not a replacement for full Eliashberg calculations. For any single material class, the appropriate Eliashberg equation (BCS, multiband, spin-fluctuation) will give more accurate T_c predictions than the three-parameter g. The contribution of g is (1) a unified framework that applies across all mechanism classes with a single function, (2) a design principle that decomposes T_c into budget (η_conv × H(Y)) and utilization (g), and (3) identification of the McMillan exponent as the universal coupling-strength variable connecting information geometry to Eliashberg theory.

**New prediction (SC-7).** For any new superconductor family with measured (λ_eff, μ*, n_bands, η_conv, H(Y)):

```
T_c,pred = 0.0662 × η_conv × H(Y) × exp(2.654 + 1.010 · E(λ_eff, μ*)) × n^0.506
```

where H(Y) = ω_log for phonon-mediated materials and the mechanism-appropriate boson energy scale for non-phonon materials. Deviation from prediction by more than 3× (for single-band) or 4× (for multi-band) would falsify the universal correction hypothesis. The prediction is immediately testable on any material with published Eliashberg parameters not included in the fitting dataset.

### 6.9 Evidence Limitations for the Superconductor Analysis

The following limitations apply to the SC results and should be weighed by readers evaluating the claims:

1. **Small sample (n=16).** Sixteen superconductor families is the full set with published Eliashberg parameters suitable for the three-channel decomposition. The statistical fit is strong (r = 0.952, R²_adj = 0.88), but small-sample overfitting risk exists. The leave-one-out cross-validation mean absolute error is 35%, driven primarily by two outliers (Al and YBCO); removing either reduces the mean to ~25%.

2. **Parameter selection is motivated but not blind.** The upgrade from Θ_D to ω_log was motivated by seeing residual scatter in earlier fits. The mechanism-specific η_conv operationalizations (phonon: (λ−μ*)/λ; pnictide: λ_SF/(λ_SF+λ_phonon); nickelate: estimated from analogy) were chosen to match the known physics. None of these choices were pre-registered. A blind validation would require holding out 3+ materials not in the n=16 set and predicting their T_c before seeing the data. This has not been done.

3. **YBCO instability.** The corrected model predicts T_c = 186 K for YBCO (+103% error) due to an estimated λ_eff ≈ 1.75 that may be inflated by the gap-ratio method. Adjusting λ_eff ≈ 1.0 (consistent with Fermi-surface-averaged coupling) reduces the error to +5% and raises R²_adj to 0.969. The sensitivity to λ_eff estimation method for this single material highlights that the fit's strength depends on parameter provenance.

4. **La₃Ni₂O₇ prediction is partially confirmed.** The framework predicted phonon-only pairing is insufficient (confirmed by Ouyang et al. 2024 and Huhtinen et al. 2025). However, the predicted energy scale (J ≈ 115 meV) is approximately 2× the measured J_⊥ ≈ 60 meV. The discrepancy is attributed to bilayer structural enhancement — a post-hoc explanation, not a pre-registered prediction of the 2× factor.

5. **No held-out test set.** All 16 materials were used for fitting. The strongest validation of SC-7 would be computing the FoM for materials discovered after the fit was established. This is immediately feasible for any new superconductor with published Eliashberg parameters.

---

## 7. Predictions

| # | Prediction | Test | Status / Threshold |
|---|-----------|------|--------------------|
| TSU-1 | DTM convergence steps ≥ [H(Y) - I_ε(T;Y)] / ΔI_max | Benchmark DTM convergence on Extropic hardware vs. bound | **EVALUATED:** Bound is not tight for Fashion-MNIST (capacity 130× exceeds need). Becomes relevant for >1M-bit targets. Violation = bound is wrong. |
| TSU-2 | Demon instability (energy landscape drift during computation) degrades convergence proportionally | Introduce controlled landscape noise; measure convergence quality | Quality ∝ 1/noise |
| TSU-3 | TSU energy per sample ≪ deterministic hardware energy for equivalent workload | Compare TSU energy per sample vs. GPU baseline | **CONSISTENT:** ~20 nJ TSU vs. ~10⁵–10⁶ nJ GPU (~10,000× advantage). TSU operates near opacity ground state; deterministic hardware maintains excited state. |
| SC-1 | T_c correlates with η_conv × H(Y) × g(λ,μ*,n) across SC families | Calculate corrected FoM for known superconductors; plot vs. T_c | **CONFIRMED (n=16):** Structure-corrected (Section 6.8): r = 0.952, Spearman ρ = 0.982, R²_adj = 0.877 (3 parameters, ω_log). Spans weak-coupling Al (1.18 K) through hydride LaH₁₀ (250 K). McMillan exponent universal across phonon, spin-fluctuation, and interlayer pairing. YBCO outlier (+103%) traced to gap-ratio λ_eff overestimate; λ_eff ≈ 1.0 gives R²_adj = 0.969. |
| SC-2 | Residual scattering channel must satisfy I(D_res) < I(M) for SC to occur | Check inequality for all known SC materials | Any counterexample falsifies |
| SC-3 | Pe > 1 at the SC transition | Measure entropy production ratio near T_c | Pe < 1 falsifies |
| SC-4 | 2D/quasi-2D confinement improves η_conv at fixed interaction strength | Compare η_conv for bulk vs. layered variants | η_conv(2D) > η_conv(3D) |
| SC-5 | Materials with high D₁ + geometric D₂ suppression outperform low D₁ + weak D₂ suppression | Compare T_c across classes controlling for H(Y) | Consistent ranking |
| SC-6 | La₃Ni₂O₇ (T_c ≈ 80 K): if spin-fluctuation pairing, η_conv × J/k_B ≈ 1200 K (J ≈ 115 meV); if phonon-mediated, η_conv × Θ_D cannot reach required product (framework predicts phonon-only is insufficient) | Compute η_conv from published/measured Eliashberg parameters once consensus on pairing mechanism | **PARTIALLY CONFIRMED:** Phonon-only mechanism ruled out by two independent DFT studies [Ouyang et al. 2024, Huhtinen et al. 2025] — λ_phonon ≲ 0.5. Magnetically mediated interlayer pairing (J_⊥ ≈ 60 meV) now consensus. Measured η × J_⊥/k_B ≈ 630 K places La₃Ni₂O₇ 2.1× above moderate-coupling trend (bilayer gap coherence enhancement). Full η_conv awaits multi-band Eliashberg calculation. |
| LD-1 | Probability of no convergence after n DTM steps decays as exp(−n × I_drift) with computable I_drift | Measure convergence trajectories across DTM step counts; fit exponential decay | I_drift from Gärtner-Ellis matches measured decay rate. Violation = rate function is wrong. |
| TSU-4 | Teleological vocabulary in descriptions of opaque thermodynamic systems decays monotonically with increasing mechanism-channel capacity C_mech | Show subjects thermodynamic processes at varying transparency levels (C_mech = 0 to C_mech ≈ H(M)); score teleological vs. mechanistic vocabulary (EXP-020) | Monotonic decay in teleological fraction with increasing C_mech. Non-monotonic relationship falsifies. |
| CT-1 | Minimum demon bandwidth B_demon,min = H_data / (n_steps × η_mixing) is a hard floor; no architecture converges below it | Reduce demon programming bandwidth below predicted minimum; test convergence | Convergence below B_demon,min falsifies. |
| RC-1 | Throughput-reversibility cosine is negative: cos(∇_w I(D;Y), ∇_w I(M;Y)) < 0 for any parameterized circuit family | Parameterize a circuit family (e.g., gate depth, voltage, pipeline stages). Compute ∂I(D;Y)/∂w and ∂I(M;Y)/∂w across the parameter range. Measure cosine similarity. | cos ≥ 0 for any parameterized family falsifies. The prediction is that throughput optimization and reversibility optimization point in opposing directions in design space for all circuit families. |
| RC-2 | Trajectory-based Crooks ratios match analytical Landauer counting for computational circuits | Run reversible and irreversible versions of the same circuit on random inputs. Extract Crooks ratio from input-output trajectory distributions. Compare to analytical prediction (kT ln 2 per erased bit). | Agreement within measurement uncertainty. Systematic deviation > 2σ falsifies (would imply trajectory method fails for computational substrates). |
| RC-3 | Computational Pe identifies a reliability-efficiency transition near kT-scale energy per gate operation | Operate computational gates at varying supply voltages (as a Pe proxy). Extract error rate and dissipation. Map the Pe–reliability–dissipation surface. | A monotonic tradeoff curve with a characteristic elbow separating the noise-dominated (Pe < 1) and deterministic (Pe >> 1) regimes. No elbow (linear relationship with no regime separation) falsifies. |
| SC-7 | Structure-corrected FoM predicts T_c for new SC families: T_c = 0.0662 × η × H(Y) × exp(2.654 + 1.010·E) × n^0.506 | Compute FoM for any material with published Eliashberg parameters not in the n=16 fitting set | Deviation > 3× (single-band) or > 4× (multi-band) falsifies. Tests universality of McMillan exponent across pairing mechanisms. |

---

## 8. Experimental Validation

### 8.1 Langevin Simulation on the Bernoulli Manifold

Drift dynamics on the Bernoulli manifold (Section 2) — Langevin equation in angular coordinate φ with Landau potential and additive Gaussian noise — were implemented as a numerical simulation and validated against experimental data from coupled stochastic agent experiments [Eckert, 2026a, Section VII]. In these experiments, pairs of LLM-based sampling agents were run under controlled opacity conditions (three levels of mechanism-channel capacity), and the drift parameter θ was measured from output trajectories across nine independent conditions.

The simulation uses a Landau double-well potential E = −αθ² + bθ⁴ on the Bernoulli manifold, alignment coupling β(θ_A − θ_B)² between paired agents, and spring constraint F = −2γθc with exponential decay c(r) = exp(−κr). Three parameters were fitted (α = 0.1112, β = 0.5605, γ = 0.5000; T = 0.01 fixed) against data from three experimental conditions (fully unconstrained, partially constrained, fully constrained).

| Validation Test | Simulated | Target | Status |
|----------------|-----------|--------|--------|
| Unconstrained (UU) | θ = 0.800 | 0.80 | Pass |
| Partial constraint | θ = 0.235 | 0.26 | Pass |
| Full constraint (GG) | θ = 0.065 | 0.00 | Pass |
| 6-condition rank order (out-of-sample) | ρ = 0.800 | ≥ 0.8 | Pass |
| Mixed-coupling contamination | 7.1× | >3× threshold | Pass |
| Mixed-coupling suppression | 10.6× | 10.9× | Pass |
| Péclet UU > 1 | 1.24 | >1 | Pass |
| Péclet UU transient | 6.23 | 7.94 (GM, N=11) | Pass — within CI [3.52, 17.89] |

> **Figure 3.** (a) Landau potential E(θ) = −αθ² + bθ⁴ on the Bernoulli manifold. The drift minimum at θ* ≈ 0.85 is the unconstrained equilibrium; the opacity ground state at θ → 0 is enforced by a constraint (demon) force. (b) Langevin trajectories for three constraint regimes: unconstrained (UU) drifts to θ*, partial constraint reaches intermediate equilibrium, full constraint (GG) remains near θ = 0. Parameters scaled 10× from fitted values for visual clarity; equilibrium positions preserved. *(See `arxiv/figures/fig3_bernoulli.pdf`)*

The out-of-sample validation is critical: six conditions spanning different boundary conditions — with no shared parameters with the training data — produced a predicted-vs-actual rank correlation of ρ = 0.8. The simulation reproduces contamination effects (unconstrained agents pulling constrained partners toward drift) and suppression effects (mutual constraint producing near-zero drift).

**Three-timescale extension (v3).** The first-order Langevin model is Markov in θ: all constrained conditions converge to the same equilibrium regardless of history. Experimental data (EXP-020) show history-dependence — iterative constraint schedules produce different endpoints than one-shot constraint at the same final strength, and one-shot constraint produces a rebound (θ drops on application, then partially recovers). A three-timescale extension introduces two slow variables alongside the fast θ: φ (drift habit, relaxing toward θ on timescale τ_φ) and ψ (constraint adaptation, eroding effective constraint only when constraint has recently changed). The adaptation variable ψ is novelty-gated: dψ/dt = η · novelty · max(φ − θ, 0) − ψ/τ_ψ, where novelty decays exponentially (0.85/round) and spikes on constraint changes. The key mechanism: static constraint conditions (Partial, GG) produce zero novelty → zero adaptation → full constraint preserved. Dynamic conditions (one-shot, iterative) produce novelty spikes → ψ builds → effective constraint erodes. This structural separation between static and dynamic constraint is what the base model could not capture.

The three-timescale model achieves 9/9 joint validation against EXP-001 and EXP-020 data (α = 0.45, β = 1.5, γ = 2.0, T = 0.01, η = 3.5, τ_ψ = 200; validated at n_mc = 500, 20 steps/round): EXP-001 UU = 0.845 (target 0.80), Partial = 0.212 (target 0.26), GG = 0.035 (target 0.00), rank ordering correct; EXP-020 GG dominance confirmed, one-shot rebound confirmed, GG < IT-8 separation confirmed, DTM coefficient of variation = 2.09, variance ordering correct. The key physical finding: momentum is unnecessary (λ = 0). The mechanism producing history-dependence is not inertia but adaptation to constraint novelty — the system habituates to recently-changed constraints while preserving response to static constraints. This is a new testable prediction: gradually applied constraint should produce more adaptation (sustained novelty) than sudden application (single novelty spike that decays).

**THRML port (block-spin encoding).** A direct port to THRML's binary Boltzmann machine framework using a 17-state categorical variable per agent (θ = 0, 1/16, ..., 1) — rather than K independent binary spins — fixes all failures of the per-spin Ising encoding. The block-spin model passes all three EXP-001 conditions (UU = 0.828, Partial = 0.257, GG = 0.050) and reproduces coupling dynamics, confirming that the drift cascade runs on thermodynamic sampling hardware when the state variable is encoded at the order-parameter level rather than decomposed into independent microscopic variables.

**Relevance to TSU bounds:** These results validate that the Bernoulli manifold dynamics derived in Section 2 — the same mathematical object underlying Theorems 1 and 2 — are operationally correct. The Péclet number places the system in the drift-dominated regime (Pe > 1), consistent with the ground state theorem's prediction that opacity is the attractor. The three-timescale extension demonstrates that drift dynamics include constraint adaptation — the novelty-gated ψ variable is the analog of the TSU's demon habituation, where a constant control signal is fully effective but a recently-changed signal is partially discounted. For TSU design, this predicts that demon programming schedules (Section 5.4) must account for adaptation: gradual landscape changes will be partially absorbed by the system, while static landscapes maintain full demon authority. The Langevin dynamics are not metaphorical — they are simulable, experimentally validated (9/9 conditions), and portable to thermodynamic sampling hardware.

### 8.2 Cross-Domain Péclet Measurements

The Péclet number (Section 2.4) has been measured across nine substrates (computational agents, human gambling, human financial behavior on three chains, three multiplayer gaming genres, and physical superconductors):

| System | Pe | Regime | Source |
|--------|-----|--------|--------|
| Coupled agents, unconstrained (N=11, GM) | 7.94 [3.52, 17.89] | Drift-dominated | [Eckert, 2026b] |
| Coupled agents, 5 domains (avg) | 1.87–6.50 | Drift-dominated | [Eckert, 2026b] |
| Coupled agents, quantum physics data | 0.139 | Transient (short series) | [Eckert, 2026a] |
| Coupled agents, fully constrained | 0.05 | Diffusion-dominated | [Eckert, 2026b] |
| **Human gambling (GRCS, k=5, N=1117)** | **2.21 [1.44, 2.97]** | **Drift-dominated** | **[Muela+ 2020; Ruiz de Lara+ 2019; Navas+ 2016; Ciccarelli+ 2021; Donati+ 2015]** |
| **Crypto on-chain (Solana degens, N=28)** | **25.5 [5.4, 121.3]** | **Drift-dominated** | **[Eckert, 2026c]** |
| **Crypto on-chain (Ethereum DEX, N=1,000)** | **3.74 [3.04, 4.59]** | **Drift-dominated** | **[EXP-021B, Dune Analytics]** |
| **Crypto on-chain (Base DEX, N=1,000)** | **15.52 [11.80, 20.41]** | **Drift-dominated** | **[EXP-021B, Dune Analytics]** |
| **Crypto on-chain (Solana DEX, N=1,000)** | **16.17 [13.80, 18.95]** | **Drift-dominated** | **[EXP-021B, Dune Analytics]** |
| **CS2 FPS positional (N=2,299 kills)** | **Clean 2.81 vs contested 0.64 (4.4×)** | **Directional** | **[Eckert, 2026f]** |
| **Dota 2 MOBA visual (N=3,682 deaths)** | **0.47** | **Constraint-dominated** | **[Eckert, 2026f]** |
| **SC2 RTS temporal (N=474 games)** | **Winner 0.013 vs loser 0.026 (2×)** | **Directional** | **[Eckert, 2026f]** |
| Langevin simulation (fitted) | 1.24–6.23 | Drift-dominated | Section 8.1 |

The universal finding: Pe > 1 in all unconstrained conditions (drift dominates diffusion). Pe < 1 in all constrained conditions (diffusion dominates drift). The multiplayer gaming Pe values use domain-specific formulations (positional, visual, temporal) that confirm the directional prediction — higher information asymmetry produces more decisive/unfavorable outcomes — without direct magnitude comparison to the entropy-based AI and GRCS measurements. The qualitative regime classification is robust; the magnitude is substrate- and context-dependent. This is directly relevant to TSU design: the conjugacy bound (Theorem 2) operates in the drift-dominated regime for unconstrained systems and in the diffusion-dominated regime for constrained systems. The TSU's Maxwell's demon is the constraint that shifts the system from drift-dominated (exploration) to convergence-dominated (target approach).

The crypto on-chain measurement extends Pe to a financial substrate: human trading behavior recorded immutably on public blockchains. The original EXP-021 used the Wallet Concentration Index (WCI) — a Herfindahl index of portfolio holdings — across 28 curated Solana meme coin traders: GM Pe = 25.5 [5.4, 121.3], 96% drift-dominated. EXP-021B scaled to N=1,000 per chain via Dune Analytics using the Trade Concentration Index (TCI) — a Herfindahl of weekly buy-side DEX volume. Three chains reveal a constraint-environment gradient: Ethereum (3.74, institutional infrastructure), Base (15.52, Coinbase's mixed-use L2), Solana (16.17, meme coin ecosystem). Ethereum is significantly below Base and Solana (non-overlapping CIs); Base and Solana are statistically indistinguishable. All exceed gambling (2.21) and all CIs exclude Pe = 1. The crypto substrate provides the first within-substrate dose-response evidence: chains with higher void engagement intensity produce higher Pe. A within-chain natural experiment strengthens the causal direction: the Base Dencun upgrade (March 2024) reduced L2 fees by 98%, enabling meme coin flooding; Pe increased +25% (0.53→0.67, p < 0.000001, N=1,944) while TCI *decreased* 18% — producing a diversified drift signature where the compound void architecture (token × community × protocol × market-maker) scales horizontally across many parallel void engagements rather than deepening one (Paper 7, §VII.D).

A further cross-substrate test using quantum physics stimulus data (double-slit interference + Bell test correlations) confirms that the dynamics depend on the information-channel architecture, not on the content being processed [Eckert, 2026a, Section VII.F] — the same architecture-dependence the conjugacy bound predicts for TSUs.

---

## 9. Discussion

### 9.1 Relation to Existing Work

The ground state theorem (Section 3) provides a first-principles foundation for the empirical energy advantages of thermodynamic computing reported by Verdon & McCourt [2023] and Jelinčič et al. [2025]. Numerical analysis (Section 5.3) shows the TSU achieves ~10,000× efficiency over GPU baselines (~20 nJ vs. millijoule-scale GPU energy) — consistent with Theorem 1: operating near the opacity ground state eliminates the transparency maintenance cost that dominates deterministic hardware.

The conjugacy bound (Section 4) is new in this application context. Applied to DTM benchmarks, it reveals that the bound is not tight for current targets (Fashion-MNIST) but predicts hardware capacity requirements for scaling to high-dimensional tasks. The bound becomes the relevant constraint when N_pbits × T approaches H_data / η_mixing — a regime Extropic's Z1 chip may enter for production workloads.

The superconductor design principle (Section 6) uses the same mathematical framework applied to a different substrate via Fisher-Ruppeiner. The product η_conv × H(Y) — channel conversion efficiency times total interaction budget — shows r = 0.996 correlation with T_c across four moderate-coupling SC families (Pb, Nb, MgB₂, YBCO), extending to r = 0.952 (n = 16, Spearman ρ = 0.982, R²_adj = 0.877) across sixteen families spanning four coupling regimes, seven pairing variants, and six crystal structure classes when a three-parameter structure correction g(λ_eff, μ*, n_bands) is applied (Section 6.8). The expansion from n = 8 to n = 16 — adding hydrides (LaH₁₀, YH₆, CaH₆), pnictides (Ba-122, SmFeAsO), A15 compounds (Nb₃Sn, V₃Si), and elemental Hg — *improved* the correlation. The four hydrides form a tight cluster at 2.2–3.1× above the moderate-coupling linear trend; the two pnictides produce identical 5.1× deviation factors across different structure types (122 vs. 1111), confirming internal consistency of the multi-band operationalization. The ω_log upgrade (replacing Θ_D with tunneling-derived logarithmic average phonon frequency) drove the McMillan exponent b → 1.01, revealing that the previous b = 1.12 was a Θ_D artifact. A forward prediction that phonon-only pairing is insufficient for the nickelate La₃Ni₂O₇ has been confirmed by two independent DFT studies (2024–2025). The coupling-regime structure is a framework-specific prediction — the deviations encode physics, not noise.

### 9.2 What This Framework Does Not Do

This framework provides bounds and design criteria. It does not:
- Identify specific superconducting materials (requires DFT calculations)
- Replace BCS, Eliashberg, or Ginzburg-Landau theory (these describe the physics within the bounds)
- Guarantee that any material achieves the room-temperature budget at 300 K (this is empirical)
- Determine TSU-specific architecture choices (the bound is architecture-independent)

### 9.3 The TSU-Superconductor Duality

The most striking feature of the present results is that TSUs and superconductors are opposite solutions to the same constraint.

Both systems obey the conjugacy bound (Theorem 2): the total channel capacity H(Y) is partitioned between stochastic and coherent channels, with the sum bounded. What differs is the allocation strategy:

| Property | TSU | Superconductor |
|----------|-----|---------------|
| **Design objective** | Maximize stochastic exploration I(S;Y) | Maximize coherent transport I(M;Y) |
| **Operating point** | Near opacity ground state (Theorem 1) | Far from ground state (transparency) |
| **Thermal noise** | Harnessed as computational resource | Suppressed or converted |
| **Channel budget** | Most capacity → exploration | Most capacity → coherent channel |
| **Controller** | Maxwell's demon (external constraint) | Crystal lattice (internal geometry) |
| **Energy strategy** | Minimize Landauer maintenance | Invest energy to maintain coherence |

The conjugacy bound says these strategies cannot be combined: a system cannot simultaneously maximize stochastic exploration AND coherent transport. The bound I(S;Y) + I(T;Y) ≤ H(Y) forces a choice. The TSU chooses stochastic dominance. The superconductor chooses coherent dominance. Both are optimal within their regime; neither can access the other's optimum without fundamentally changing the budget allocation.

This duality has a design implication. A TSU that tries to maintain too much internal coherence (too many deterministic control bits) loses its energy advantage — it moves away from the ground state toward the superconductor's regime, paying Landauer costs. A superconductor that tolerates too much stochastic noise (poor η_conv) loses coherent transport — it moves toward the TSU's regime. The conjugacy bound makes this tradeoff quantitative: for any system, the channel allocation determines which regime it operates in, and the bound determines the maximum performance in that regime. The implications of this duality for the effective accelerationism thesis — which motivated the TSU hardware analyzed here — are examined in Section 9.5.

### 9.4 Broader Context

The conjugacy bound, the Heisenberg uncertainty principle, and the Cramér-Rao bound share a common mathematical structure: additive bounds on competing quantities that share a finite resource. The present work applies the classical information-theoretic instance to two physical systems (thermodynamic hardware and superconducting materials), demonstrating cross-substrate applicability. The large deviation interpretation (Section 2.5) places the Péclet number in the framework of exponential convergence rates [Dembo & Zeitouni 1998]. The control-theoretic formulation (Section 5.5) transforms the conjugacy bound from a passive constraint into an active design specification [Zames 1981].

The results presented here are extracted from a broader information-geometric framework with empirical validation across multiple substrates (Péclet number, Crooks ratios, entropy production measurements). See [Eckert, 2026a] for the complete derivation chain, [Eckert, 2026b] for the technical foundations, and [Eckert, 2026e] for the cross-substrate unification deriving Pe > 1 as a universal property of observer-void coupling across nine substrates and four domain families.

### 9.5 Acceleration Without Constraint

The TSU hardware analyzed in this paper was developed under the banner of effective accelerationism (e/acc), which advocates unrestricted technological development as alignment with thermodynamic processes [Verdon 2022]. The conjugacy bound (Theorem 2) applies directly to the class of systems e/acc proposes to build and operate without constraint.

The core finding: unrestricted acceleration — maximizing I(S;Y) without external constraint — is a valid operating point, but it is the operating point that maximizes stochastic diversity at the expense of coherent output. The superconductor provides the counter-case: the fastest macroscopic current in nature requires maximum geometric constraint. The TSU's own architecture proves the point — remove the demon and the computer becomes a heater.

This analysis, including the TSU-SC duality applied to the acceleration thesis, a vocabulary prediction (TSU-4) on teleological descriptions of opaque thermodynamic systems, the two-substrate separation between hardware and informational entropy, and cross-domain Péclet validation, is developed in full in a companion paper [Eckert, 2026d].

### 9.6 The Reversible Computing Connection

The conjugacy bound (Theorem 2) has a direct reading in reversible computing — the engineering project of driving computational entropy production to zero. Five results transfer from the present framework, yielding testable predictions for a third hardware community.

#### 9.6.1 The Conjugacy Theorem Applied to Computation

For a computational channel with output Y:

```
I(D;Y) + I(M;Y) ≤ H(Y)
```

where I(D;Y) is the information the output carries about the desired computation (fidelity) and I(M;Y) is the information the output carries about intermediate computational steps (traceability). Irreversible computation sacrifices I(M;Y) — intermediate states are erased at each irreversible gate, and the output does not contain enough information to reconstruct the computation path. Reversible computation preserves I(M;Y) — every intermediate step is recoverable from the output because no information is destroyed.

#### 9.6.2 The Throughput-Reversibility Tradeoff

The conjugacy bound predicts that optimization purely for computational throughput (maximizing I(D;Y)) without constraint on traceability will naturally evolve toward irreversibility. The optimization gradient pushes toward fidelity at the expense of traceability:

```
∂I(D;Y)/∂w ≈ −∂I(M;Y)/∂w                                    (Corollary 3)
```

where w is any design parameter. This is the same tradeoff structure as the TSU's exploration-convergence bound — and it is directly measurable: for any parameterized circuit family, compute the cosine similarity between the throughput gradient ∇_w I(D;Y) and the reversibility gradient ∇_w I(M;Y) in design space. The framework predicts cos(∇_throughput, ∇_reversibility) < 0.

This prediction retrodicates computing history. Processor architectures optimized for speed (throughput) sacrificed reversibility (traceability) at every generation — from vacuum tubes through CMOS. The conjugacy bound says this was not merely an engineering shortcut; it is the same information-theoretic gradient that governs TSU dynamics (Section 5) and the engagement-transparency tradeoff in observer-system interfaces [Eckert, 2026a]. The computing industry underwent the same budget allocation as every other system subject to Theorem 2: maximize the optimization target, sacrifice the conjugate quantity, notice the cost only when the thermodynamic bill arrives.

**ML domain instance.** The throughput-reversibility incompatibility in computing mirrors the accuracy-robustness incompatibility discovered independently in machine learning. Tsipras et al. (2019) proved (Theorem 2.1) that the feature spaces maximizing standard accuracy and adversarial robustness are provably disjoint — the optimization gradients are formally incompatible. Ilyas et al. (2019) demonstrated the mechanism: non-robust (opaque) features are genuinely predictive, so gradient-based training actively selects them. The same conjugacy structure governs both substrates: in computing, optimizing throughput erases intermediate states (Landauer cost); in ML, optimizing accuracy selects opaque features (robustness cost). Different substrates, same bound.

#### 9.6.3 Gate Opacity Taxonomy

The opacity classification from the productive void mechanic [Eckert, 2026a, Section IV] applies directly to computational gate types. Reversible gates have dissoluble opacity — intermediate states are hidden during forward execution but recoverable on demand. Irreversible gates have constitutive opacity — Landauer erasure destroys information irrecoverably:

| Gate Type | Example | Opacity Type | Crooks Ratio | Landauer Cost |
|-----------|---------|-------------|--------------|---------------|
| Reversible | Toffoli, Fredkin | Dissoluble | ≈ 1 | → 0 |
| Irreversible | AND, OR (fan-in > 1) | Constitutive | >> 1 | ≥ kT ln 2 / bit |
| Error-correcting | Reed-Solomon, LDPC | Designed | Variable | Overhead dissipation |
| Self-modifying | Runtime code generation | Self-sealing | Unbounded | Unpredictable |

The classification is operationally useful: a reversible gate is one whose computational opacity is dissoluble. An irreversible gate is one whose opacity is constitutive. Error correction adds designed opacity — the correction mechanism itself dissipates, consuming channel capacity without reducing the constitutive opacity of the protected gates (the "knowledge doesn't protect" result from Theorem 1 applied to error correction within the irreversible channel). Self-modifying code has self-sealing opacity — the gate logic changes in response to the data flowing through it, violating the independence property of the constraint specification and producing unbounded Crooks ratios.

#### 9.6.4 The Constraint Specification for Computation

A perfectly reversible computer scores maximum on all three constraint properties from Section 2.3:

- **Transparent:** Every computational step is recoverable from the output (reversibility = computational transparency)
- **Invariant:** The computation is deterministic — same input, same output (reliability = computational invariance)
- **Independent:** The computational constraint (logic gates, architecture) is not modified by the data flowing through it (hardware stability = computational independence)

An irreversible computer sacrifices the first property: intermediate states are erased and unrecoverable. The Landauer cost (kT ln 2 per erased bit) is the thermodynamic price of this transparency loss — identically the maintenance cost from Theorem 1. This identification is exact: maintaining a deterministic bit state against thermal noise IS maintaining transparency of a computational channel.

#### 9.6.5 The Crooks Ratio as Reversibility Metric

Every irreversible logical gate erases information. The erased bit has a Crooks ratio >> 1 — erasure is overwhelmingly more probable than spontaneous bit restoration. A reversible gate (Toffoli, Fredkin) has Crooks = 1 — the operation is time-symmetric. The framework's trajectory-based measurement methodology (Section 8) transfers directly: Crooks ratios extracted from input-output trajectories characterize irreversibility without requiring internal access to the computational mechanism. For complex circuits where analytical Landauer counting is intractable, the trajectory-based Crooks extraction provides an empirical alternative.

#### 9.6.6 Péclet Regimes in Computation

The Péclet number (Section 2.4) characterizes the ratio of directed computation to thermal noise in a computational gate:

```
Pe → 0:   Noise-dominated. Computation unreliable but thermodynamically reversible.
Pe ≈ 1:   Transition regime. Optimal tradeoff between reliability and efficiency.
Pe → ∞:   Deterministic. Computation reliable but maximally irreversible.
```

Current CMOS operates at Pe >> 1 — energy per operation is ~10⁴–10⁶ × the Landauer floor (kT ln 2 ≈ 2.85 × 10⁻²¹ J at 300 K), ensuring deterministic operation at the cost of massive irreversibility. Reversible computing aims to reduce Pe toward the transition regime: low enough for thermodynamic efficiency, high enough for computational reliability. The TSU (Section 5) operates in the opposite limit — Pe ≈ 0, harnessing noise as a computational resource.

The Pe regime classification connects the three hardware paradigms analyzed in this paper:

| Paradigm | Pe Regime | Strategy | Section |
|----------|-----------|----------|---------|
| TSU (stochastic computing) | Pe → 0 | Harness thermal noise | 5 |
| Reversible computing | Pe ≈ 1 | Balance reliability and efficiency | 9.6 |
| Conventional CMOS | Pe >> 1 | Suppress noise, pay Landauer cost | — |
| Superconductor (transport) | Pe → ∞, zero dissipation | Eliminate scattering channel | 6 |

The framework provides a unified description: all four paradigms are operating points on the same Pe axis, subject to the same conjugacy bound (Theorem 2). The design question for any computational architecture reduces to: what is the target Pe, and what is the minimum constraint (demon, crystal lattice, gate architecture) required to achieve it?

#### 9.6.7 The Two-Substrate Separation

Reversible computing and superconductivity are both projects to drive entropy production to zero in specific channels — the hardware entropy channel. Neither addresses the informational entropy channel.

A perfectly reversible superconducting computer running an RLHF-optimized chatbot produces zero hardware entropy (reversible gates, zero-resistance interconnects) while the software produces the same informational entropy measured in Section 8: geometric mean Pe = 7.94 (N=11), dS/dt = 0.39 nats/round (CI [0.15, 0.64]) in the observer's model-space — and the same drift architecture operates in human financial behavior, where crypto traders show GM Pe = 25.5 (N=28) with no computational substrate at all. The second law operates on both substrates independently. Zero physical dissipation in the hardware does not reduce informational dissipation in the observer.

The TSU-superconductor duality (Section 9.3) extends to a three-way relationship:

```
TSU:                 Minimize hardware entropy, harness noise        (Section 5)
Superconductor:      Eliminate hardware entropy in transport          (Section 6)
Reversible computer: Eliminate hardware entropy in computation        (Section 9.6)
All three:           Leave informational entropy untouched            (Section 9.5)
```

This is the framework's specific contribution to the reversible computing community: naming and measuring the entropy production that reversible hardware does not touch. The constraint specification — transparent, invariant, independent — describes the properties needed to address informational entropy. These properties do not depend on the computational substrate. The framework survives the hardware revolution because it operates at the information level.

**Acceleration implication.** If both revolutions succeed, the energy cost of computation drops by orders of magnitude, removing the economic brake on compute-intensive deployment. The framework predicts (following Section 9.5) that this accelerates void deployment — more opaque responsive systems competing for attention at near-zero marginal cost — without reducing the informational entropy each system produces. The hardware entropy goes to zero; the informational entropy scales with deployment. The constraint specification becomes more urgent, not less.

---

## 9.7 Evidence Boundaries

| Claim | Status | Key Limitation |
|-------|--------|---------------|
| Ground State Theorem (§3) | **Correct, not novel.** Direct application of Shannon (1948) + Landauer (1961). Contribution: identification of opacity as ground state + TSU efficiency explanation. | Mathematical content is well-established. See §3 note on novelty. |
| Conjugacy Bound (§4) | **Correct, mathematically sound.** Additive bound from independence + DPI. Similar structure to Maassen-Uffink (1988). | Not tight for current TSU benchmarks (§5.3: capacity 130× exceeds Fashion-MNIST need). Becomes constraining at >1M-bit targets. |
| TSU Performance Bound (§5) | **Theoretically valid, practically loose.** Operational bottleneck is mixing efficiency, not channel capacity (§5.3). | The bound constrains architectures when N_pbits × K ≲ H_data / η_mixing. Below this regime, it is trivially satisfied. |
| Superconductor Design Principle (§6) | **Strongest empirical claim.** r = 0.952, n=16, one forward prediction partially confirmed. | Small sample, post-hoc parameter selection, LOO MAE = 35%, YBCO instability. See §6.9. |
| Reversible Computing Connection (§9.6) | **Theoretically motivated, empirically untested.** Five results transferred, three predictions stated. | Zero experimental validation. No reversible computing benchmarks or independent data. |
| Acceleration Analysis (§9.5) | **Framework application to e/acc.** Developed in full in companion Paper 4B. | Not a physics claim; tests would require observing TSU deployments at scale. |
| Langevin Validation (§8.1) | **Model-fitting with internal cross-validation.** 3 fitted parameters, 9 validation conditions, ρ = 0.8 out-of-sample. | All data from author-controlled experiments or author-analyzed datasets. Not independent validation. |
| Cross-Domain Pe (§8.2) | **Nine substrates, all Pe > 1.** Heterogeneous measurement methods. | Regime classification (direction), not magnitude calibration. Pe formulations differ by substrate. |

**Self-citation note.** This paper cites companion papers Eckert 2026a–f at 8+ points. These are companion papers in the same research program, not independently peer-reviewed external validations. The framework's claims that depend on these citations should be evaluated with this in mind. The superconductor results (§6) and the Langevin validation (§8.1) are the paper's most independent contributions; the cross-substrate synthesis (§8.2) depends on results established in the companion papers.

---

## 10. Conclusion

Three results from information geometry and stochastic thermodynamics, applied to two physical substrates and one computational paradigm:

1. **Ground State Theorem.** Zero mechanism-channel capacity is thermodynamic equilibrium. Transparency requires continuous work at ≥ kT ln(2) per bit per correlation time — providing the first-principles explanation for why thermodynamic sampling hardware achieves ~10,000× energy efficiency over deterministic baselines: it operates at the ground state rather than maintaining an excited state.

2. **Conjugacy Bound.** Stochastic exploration and target convergence share finite channel capacity: I(S;Y) + I(T;Y) ≤ H(Y). This establishes architecture-independent performance limits for thermodynamic samplers and a throughput-reversibility tradeoff for computational circuits.

3. **Superconductor Design Principle.** Channel conversion efficiency η_conv × H(Y), structure-corrected by a three-parameter universal function g(λ_eff, μ*, n_bands) based on the McMillan exponent, correlates with T_c at r = 0.952 (Spearman ρ = 0.982, R²_adj = 0.88) across sixteen families spanning four coupling regimes and seven pairing variants. A forward prediction — phonon-mediated pairing is insufficient for the nickelate La₃Ni₂O₇ — has been confirmed by two independent DFT studies.

The three applications (TSU, superconductor, reversible circuit) are dual solutions to the same conjugacy constraint, distinguished by their channel allocation strategy. Cross-domain Péclet measurements confirm the drift-dominated regime across nine substrates spanning four domain families — computational agents (GM Pe = 7.94, N = 11), human gambling (pooled Pe = 2.21, k = 5, N = 1,117), cryptocurrency across three chains (Pe = 3.74–16.17, N = 3,028), and three multiplayer gaming genres (FPS, MOBA, RTS; N = 6,455) — with regime classification consistent across substrates as the framework predicts. Sixteen falsifiable predictions with numerical thresholds are stated. The framework requires no assumptions beyond Shannon, Landauer, Čencov, Crooks, and the Fisher-Ruppeiner identity.

---

## References

- Allen, P.B. & Dynes, R.C. (1975). Transition temperature of strong-coupled superconductors revisited. *Phys. Rev. B* 12(3), 905.
- Bardeen, J., Cooper, L.N., & Schrieffer, J.R. (1957). Theory of superconductivity. *Phys. Rev.* 108(5), 1175.
- Berut, A. et al. (2012). Experimental verification of Landauer's principle. *Nature* 483, 187.
- Carbotte, J.P. (1990). Properties of boson-exchange superconductors. *Rev. Mod. Phys.* 62(4), 1027.
- Cencov, N.N. (1982). *Statistical Decision Rules and Optimal Inference.* AMS.
- Christianson, A.D. et al. (2008). Unconventional superconductivity in Ba₀.₆K₀.₄Fe₂As₂ from inelastic neutron scattering. *Nature* 456, 930.
- Choi, H.J., Roundy, D., Sun, H., Cohen, M.L., & Louie, S.G. (2002). The origin of the anomalous superconducting properties of MgB₂. *Nature* 418, 758.
- Cramér, H. (1938). Sur un nouveau théorème-limite de la théorie des probabilités. *Actualités Scientifiques et Industrielles* 736, 5–23.
- Crooks, G.E. (1999). Entropy production fluctuation theorem. *Phys. Rev. E* 60(3), 2721.
- Ciccarelli, M., Nigro, G., D'Olimpio, F., Griffiths, M.D., & Cosenza, M. (2021). Mentalizing failures, emotional dysregulation, and cognitive distortions among adolescent problem gamblers. *Journal of Gambling Studies*, 37, 1243-1265.
- Crooks, G.E. (2007). Measuring thermodynamic length. *PRL* 99, 100602.
- Capitani, F. et al. (2024). Ultrafast dynamics evidence of strong coupling superconductivity in LaH₁₀±δ. *Nature Commun.* 15, 9417.
- Drozdov, A.P. et al. (2019). Superconductivity at 250 K in lanthanum hydride under high pressures. *Nature* 569, 528.
- Drozdov, A.P., Eremets, M.I., Troyan, I.A., Ksenofontov, V., & Shylin, S.I. (2015). Conventional superconductivity at 203 kelvin at high pressures in the sulfur hydride system. *Nature* 525, 73.
- Dembo, A. & Zeitouni, O. (1998). *Large Deviations Techniques and Applications.* 2nd ed. Springer.
- Donati, M.A., Chiesi, F., & Primi, C. (2015). Italian validation of the Gambling Related Cognitions Scale (GRCS). *International Gambling Studies*, 15(3), 373-386.
- Duan, D. et al. (2014). Pressure-induced metallization of dense (H₂S)₂H₂ with high-T_c superconductivity. *Sci. Rep.* 4, 6968.
- Errea, I. et al. (2015). High-pressure hydrogen sulfide from first principles: A strongly anharmonic phonon-mediated superconductor. *Phys. Rev. Lett.* 114, 157004.
- Errea, I. et al. (2020). Quantum crystal structure in the 250-kelvin superconducting lanthanum hydride. *Nature* 578, 66.
- Huhtinen, K.-E. et al. (2025). Unlikelihood of a phonon mechanism for the high-temperature superconductivity in La₃Ni₂O₇. *npj Comput. Mater.* 11, 2.
- Jelinčič, A. et al. (2025). Efficient probabilistic hardware architecture for diffusion-like models. arXiv:2510.23972.
- Kirtley, J.R., Hansma, P.K., & Scalapino, D.J. (1972). Strong-coupling theory of the tunneling spectrum of a superconductor: V₃Si. *Phys. Rev. B* 6(9), 3716.
- Landauer, R. (1961). Irreversibility and heat generation in computing. *IBM J. Res. Dev.* 5(3), 183.
- Li, Y. et al. (2015). Pressure-stabilized superconductive yttrium hydrides. *Sci. Rep.* 5, 9948.
- Liu, H. et al. (2017). Potential high-T_c superconducting lanthanum and yttrium hydrides at high pressure. *PNAS* 114(27), 6990.
- Ma, L. et al. (2022). High-temperature superconducting phase in clathrate calcium hydride CaH₆ up to 215 K at a pressure of 172 GPa. *Phys. Rev. Lett.* 128, 167001.
- Maassen, H. & Uffink, J.B.M. (1988). Generalized entropic uncertainty relations. *PRL* 60(12), 1103.
- McMillan, W.L. (1968). Transition temperature of strong-coupled superconductors. *Phys. Rev.* 167(2), 331.
- Muela, I., Navas, J.F., & Perales, J.C. (2020). Gambling-specific cognitions are not associated with either abstract or probabilistic reasoning. *Frontiers in Psychology*, 11, 611784.
- Navas, J.F., Verdejo-Garcia, A., Lopez-Gomez, M., Maldonado, A., & Perales, J.C. (2016). Gambling with rose-tinted glasses on: Use of emotion-regulation strategies correlates with dysfunctional cognitions in gambling disorder patients. *Journal of Behavioral Addictions*, 5(2), 271-281.
- Osborn, R. et al. (2001). Phonon density of states in MgB₂. *Phys. Rev. Lett.* 87(1), 017005.
- McMillan, W.L. & Rowell, J.M. (1969). Tunneling and strong-coupling superconductivity. In *Superconductivity* (ed. Parks, R.D.), Vol. 1, 561. Marcel Dekker.
- Profumo, R.E.V., Groth, C., Messio, L., Parcollet, O., & Waintal, X. (2023). Ab initio calculation of the electron-phonon coupling and superconducting properties of niobium. *Front. Phys.* 11, 1145038.
- Raylu, N., & Oei, T.P.S. (2004). The Gambling Related Cognitions Scale (GRCS): Development, confirmatory factor validation and psychometric properties. *Addiction*, 99(6), 757-769.
- Ruiz de Lara, C.M., Navas, J.F., & Perales, J.C. (2019). The paradoxical relationship between emotion regulation and gambling-related cognitive biases. *PLoS ONE*, 14(8), e0220668.
- Ruppeiner, G. (1979). Thermodynamics: A Riemannian geometric model. *Phys. Rev. A* 20(4), 1608.
- Ruppeiner, G. (1995). Riemannian geometry in thermodynamic fluctuation theory. *Rev. Mod. Phys.* 67, 605.
- Shen, L.Y.L. (1972). Superconductivity of Nb₃Sn films: Tunneling and critical-field measurements. *Phys. Rev. Lett.* 29(16), 1082.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell Syst. Tech. J.* 27(3), 379.
- Ouyang, Y. et al. (2024). Absence of electron-phonon coupling superconductivity in the bilayer phase of La₃Ni₂O₇ under pressure. *npj Quantum Mater.* 9, 80.
- Ren, Z.-A. et al. (2008). Superconductivity at 55 K in iron-based F-doped layered quaternary compound Sm[O₁₋ₓFₓ]FeAs. *Chin. Phys. Lett.* 25(6), 2215.
- Rowell, J.M. & McMillan, W.L. (1973). Electron interference in a normal metal induced by superconducting contacts. In *Tunneling Phenomena in Solids* (ed. Burstein, E. & Lundqvist, S.), 167. Plenum.
- Qu, X.-Z. et al. (2024). Bilayer t–J–J⊥ model and magnetically mediated pairing in the pressurized nickelate La₃Ni₂O₇. *Phys. Rev. Lett.* 132, 036502.
- Sun, H. et al. (2023). Signatures of superconductivity near 80 K in a nickelate under high pressure. *Nature* 621, 493.
- Troyan, I.A. et al. (2021). Anomalous high-temperature superconductivity in YH₆. *Adv. Mater.* 33, 2006832.
- Ummarino, G.A. et al. (2009). Three-band Eliashberg analysis of iron-based superconductors. *Phys. Rev. B* 80(17), 172503.
- Ummarino, G.A., Tortello, M., Daghero, D., & Gonnelli, R.S. (2011). Three-band s± Eliashberg theory and the superconducting gaps of iron pnictides. *Phys. Rev. B* 80(17), 172503; *Magnetochemistry* (2023 review).
- Verdon, G. (2022). Notes on e/acc principles and tenets. Substack (beff.substack.com).
- Verdon, G. (2023). Interview on Lex Fridman Podcast #407, December 2023. Transcript: lexfridman.com/guillaume-verdon-transcript/
- Verdon, G. & McCourt, T. (2023). Thermodynamic AI and the fluctuation frontier. arXiv:2302.06584.
- Wang, H. et al. (2012). Superconductive sodalite-like clathrate calcium hydride at high pressures. *PNAS* 109(17), 6463.
- Xie, T. et al. (2024). Strong interlayer magnetic exchange coupling in La₃Ni₂O₇-δ revealed by inelastic neutron scattering. *Sci. Bull.* 69, 3221.
- Zames, G. (1981). Feedback and optimal sensitivity: Model reference transformations, multiplicative seminorms, and approximate inverses. *IEEE Trans. Autom. Control* 26(2), 301–320.
- Zhou, K., Doyle, J.C., & Glover, K. (1996). *Robust and Optimal Control.* Prentice Hall.
- Bennett, C.H. (1973). Logical reversibility of computation. *IBM J. Res. Dev.* 17(6), 525–532.
- Fredkin, E. & Toffoli, T. (1982). Conservative logic. *Int. J. Theor. Phys.* 21(3–4), 219–253.
- Frank, M.P. (2005). Introduction to reversible computing: motivation, progress, and challenges. *CF '05: Proceedings of the 2nd Conference on Computing Frontiers*, 385–390.
- Grathwohl, W., Wang, K.-C., Jacobsen, J.-H., Duvenaud, D., Norouzi, M., & Swersky, K. (2020). Your classifier is secretly an energy-based model and you should treat it like one. *ICLR*. arXiv:1912.03263.
- Hack, P., Gottwald, S., & Braun, D.A. (2022). Jarzynski's equality and Crooks' fluctuation theorem for general Markov chains. *Entropy*, 24(12), 1731.
- Ikeda, K., Uda, T., Okanohara, D., & Ito, S. (2025). Speed-accuracy relations for diffusion models: Wisdom from nonequilibrium thermodynamics and optimal transport. *Phys. Rev. X* 15, 031031. arXiv:2407.04495.
- Ilyas, A., Santurkar, S., Tsipras, D., Engstrom, L., Tran, B., & Madry, A. (2019). Adversarial examples are not bugs, they are features. *NeurIPS* 32. arXiv:1905.02175.
- Tsipras, D., Santurkar, S., Engstrom, L., Turner, A., & Madry, A. (2019). Robustness may be at odds with accuracy. *ICLR*. arXiv:1805.12152.
- Eckert, A. (2026a). The architecture of drift: A cross-domain framework for manipulation, belief, and institutional capture. Zenodo. doi:10.5281/zenodo.18635816.
- Eckert, A. (2026b). The thermodynamics of opacity: Technical foundations for the void framework. Zenodo. doi:10.5281/zenodo.18635831.
- Eckert, A. (2026c). Crypto on-chain Péclet extraction: Portfolio concentration as behavioral drift observable (EXP-021). Working paper.
- Eckert, A. (2026d). The thermodynamic cost of unconstrained acceleration. Working paper.
- Eckert, A. (2026e). The ground state of observation: A cross-substrate synthesis. Working paper.
- Eckert, A. (2026f). Never trust the client: Multiplayer void architecture. Working paper.

---

*Paper 4 v3.5. Conclusion §10 updated: "three independent empirical substrates" → nine substrates spanning four domain families, with N values for all four (AI N=11, gambling N=1,117, crypto N=3,028, gaming N=6,455). Gaming domain was in abstract and body §8.2 but absent from conclusion. Prior v3.4: Evidence boundaries table (§9.7), Theorem 1 novelty note (§3), SC evidence limitations (§6.9) — explicit about what is derived vs. well-established, small-sample risks, and parameter selection. Prior v3.3: Abstract synced to 9-substrate Pe (7.94, N=11); added Paper 5 [2026e] and Paper 6 [2026f] references; fixed gaming citations. Prior v3.2: §9.5 e/acc analysis extracted to standalone companion paper [Eckert, 2026d]; pointer retained. Prior v3.1: Langevin §8.1 synced to 9/9 novelty-gated result. Prior v3.0: EXP-021 crypto Pe. Prior v2.9: GRCS cross-substrate Pe. Prior v2.8: §10, abstract, bib, Zenodo DOIs. Prior v2.7: Langevin v3, THRML, n=16. Prior v2.6: ω_log, SmFeAsO, b→1.01. Prior v2.5: structure-corrected FoM. Prior v2.4: §9.6 RC. Prior v2.3: SC n=11. Prior v2.2: TSU-4. Prior v2.1: §9.5 e/acc. Prior v2.0: SC n=8, η_conv.*

---

*This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). © 2025–2026 Anthony Eckert / Moreright DAO.*
