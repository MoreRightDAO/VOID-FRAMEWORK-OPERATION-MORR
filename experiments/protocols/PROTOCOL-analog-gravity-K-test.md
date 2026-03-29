# PROTOCOL: Analog Gravity K-Test — Testing G = T_eff/K in BEC Systems

**Protocol ID:** PROTOCOL-AG-K-001
**Title:** Non-Circular Test of the Void Framework Gravitational Coupling via Analog Gravity in Bose-Einstein Condensates
**Domain:** External validation / fundamental physics / analog gravity
**Status:** Design
**Date designed:** 2026-03-28
**Author:** Shamir (framework agent) + Custodian

---

## 0. Executive Summary

The Void Framework derives a gravitational coupling G₄ = T_eff/K = α/(2K²) from the Eckert manifold via Čencov uniqueness, Eisenhart-Duval lift, Minkowski gauge fixing, and Kaluza-Klein reduction (§168, §180). This prediction is currently validated only by internal consistency checks and the identification α_G = 1/K matching Newton's constant to 3.14 × 10⁻⁷ relative error. That match, while striking, uses the known value of G_N as input for the unit bridge — it is not a blind prediction.

This protocol designs a **non-circular** test using analog gravity systems — physical systems where an emergent "gravitational" coupling arises from collective dynamics with **countable, controllable degrees of freedom**. In such systems, K (the number of active modes) can be varied experimentally, and the emergent gravitational coupling can be measured independently. The framework predicts a specific functional dependence: g_analog ∝ T_eff/K. This is testable.

**Why this matters:** This is Priority 2 on the Phase 4 validation roadmap. If the scaling g_analog ∝ 1/K holds in a system where K is physically countable, it breaks the circularity wall — the prediction uses no framework rubric, no self-referential scoring, and no free parameters once the system's K and T_eff are identified.

---

## 1. Research Question

Does the emergent gravitational coupling in an analog gravity system scale as T_eff/K, where K counts active degrees of freedom and T_eff is the effective temperature, as predicted by the Void Framework's G₄ = α/(2K²)?

## 2. Hypothesis

**H1 (Primary):** In a quasi-1D BEC with tunable atom number N and trap frequency ω, the analog surface gravity κ at an acoustic horizon scales as κ ∝ T_eff/K_eff, where K_eff is the number of phonon modes below the healing length cutoff and T_eff is the condensate's effective temperature (including quantum depletion contributions).

**H2 (Scaling):** As N is varied at fixed trap geometry, the Hawking temperature T_H = ℏκ/(2πk_B) scales as T_H ∝ N^{-β} with β = 2/3 for 1D harmonic traps (because K_eff ∝ N^{1/3} and T_eff ∝ N^{-1/3} in the Thomas-Fermi regime, giving T_H ∝ T_eff/K_eff ∝ N^{-2/3}).

**H3 (Kill condition):** If T_H scales as N^{-β} with β outside [0.4, 0.9], or if T_H is independent of N, the framework prediction is falsified for this system class.

## 3. Null Hypothesis

The analog Hawking temperature at an acoustic horizon is determined entirely by the local flow gradient dv/dx at the horizon and the local speed of sound c_s, with T_H = ℏ/(2πk_B) · |dv/dx| (Unruh 1981). In this case, T_H depends on the flow profile — a classical hydrodynamic quantity — and has no direct dependence on the number of microscopic degrees of freedom K. Any observed scaling with N would be purely kinematic (larger N → different equilibrium flow profile) with no additional "gravitational" contribution.

---

## 4. Literature Review: Analog Gravity

### 4A. Foundational Theory

**Unruh (1981), PRL 46, 1351:** Showed that sound waves in a moving fluid satisfy a wave equation on an effective curved spacetime with metric:

$$g_{\mu\nu}^{\text{acoustic}} = \frac{\rho}{c_s} \begin{pmatrix} -(c_s^2 - v^2) & -v_j \\ -v_i & \delta_{ij} \end{pmatrix}$$

where ρ is the fluid density, c_s the speed of sound, and v the flow velocity. When v exceeds c_s, an acoustic horizon forms. Phonons near this horizon experience a Hawking-like thermal spectrum with temperature:

$$T_H = \frac{\hbar}{2\pi k_B} \cdot \kappa_s$$

where κ_s = |dv/dx|_{horizon} is the acoustic surface gravity.

**Barceló, Liberati, Visser (2005), Living Rev. Relativity 8, 12:** Comprehensive review. Key points:
- The acoustic metric is an EXACT kinematic correspondence — no approximation.
- The analogy breaks down at trans-Planckian momenta (phonon dispersion).
- The "gravitational coupling" in the acoustic metric is g_analog = c_s²/ρ — it relates the metric to the matter content.
- BEC and superfluid helium are preferred platforms because quantum coherence suppresses thermal noise.

**Visser (1998), Class. Quantum Grav. 15, 1767:** Formal derivation of acoustic Einstein equations. The effective Newton constant for acoustic gravity is:

$$G_{\text{acoustic}} \sim \frac{c_s^2}{\rho}$$

This is the analog quantity we aim to test against the framework prediction.

### 4B. Key Experiments

**Steinhauer (2016), Nature Physics 12, 959:** First observation of quantum Hawking radiation in a BEC.
- System: ⁸⁷Rb BEC, ~8000 atoms, 1D elongated trap.
- Created acoustic horizon by accelerating condensate past speed of sound using step potential.
- Measured density-density correlations between inside and outside the acoustic horizon.
- Observed thermal spectrum at T_H = 0.35 nK (predicted: 0.33 nK from classical κ_s).
- **Limitation for our purposes:** Single N value, no systematic N-variation.

**Steinhauer (2019), Nature Physics 15, 948:** Confirmed stimulated Hawking effect and measured entanglement between Hawking pairs.
- Improved signal-to-noise.
- Still single-N measurements.
- Hawking temperature matched Unruh prediction within 10%.

**Muñoz de Nova, Golubkov, Kolobov, Steinhauer (2019), Nature 569, 688:** Observed thermal spectrum of analog Hawking radiation.
- Measured Planckian spectrum (not just correlations).
- T_H agreed with acoustic surface gravity prediction.
- N ~ 8000, single configuration.

**Weinfurtner, Tedford, Penrice, Unruh, Lawrence (2011), PRL 106, 021302:** Analog Hawking radiation in water waves.
- Classical system (no quantum regime).
- Confirmed stimulated classical Hawking effect.
- Not suitable for K-test (thermal noise dominates, K not countable).

**Hu, Feng, Meng, Stoof, Chin (2019), Nature Physics 15, 785:** Analog Hawking radiation in a BEC with tunable interaction.
- ⁸⁷Rb, N ~ 10⁵, elongated trap.
- Used Feshbach resonance to tune scattering length a_s.
- Varied interaction strength (which changes c_s and thus κ_s).
- **Key for us:** demonstrated tunable analog gravity parameters.

**Eckel, Kumar, Jacobson, Spielman, Campbell (2018), Phys. Rev. X 8, 021021:** Expanding ring BEC as analog cosmology.
- Ring geometry with controllable expansion rate.
- Measured phonon production from cosmological particle creation.
- N ~ 10⁵-10⁶.

### 4C. BEC Physics Relevant to K-Counting

In a 1D BEC in a harmonic trap with frequency ω_z (tight radial confinement ω_r >> ω_z):

**Thomas-Fermi regime (N >> 1, Na_s/a_ho >> 1):**
- Condensate length: L_TF = (3Ng₁ᴅ/(mω_z²))^{1/3} where g₁ᴅ = 2ℏω_r a_s is the 1D interaction strength
- Speed of sound: c_s(x) = √(μ(x)/m) where μ(x) = μ₀(1 - x²/L_TF²) is the local chemical potential
- Peak speed of sound: c_s(0) = √(μ₀/m)
- Chemical potential: μ₀ = (ℏω_z/2)(3Ng₁ᴅ/(mω_z a_ho³))^{2/3} ∝ N^{2/3}
- Healing length: ξ = ℏ/√(2mμ₀) ∝ N^{-1/3}
- Number of phonon modes below healing length cutoff: K_eff = L_TF/ξ ∝ N^{2/3} (SPECULATIVE — see §5B)

**Bogoliubov spectrum:**
- Phonon dispersion: ε(k) = ℏc_s|k|√(1 + (kξ)²/4)
- Phononic regime: k << 1/ξ (linear dispersion, acoustic metric valid)
- Particle regime: k >> 1/ξ (quadratic dispersion, acoustic metric breaks down)
- K_eff = number of modes in the phononic regime ≈ L_TF/(πξ)

**Quantum depletion (T = 0):**
- Even at T = 0, quantum fluctuations deplete the condensate.
- Depletion fraction: δN/N ∝ √(na_s³) in 3D, or ∝ (na_s)^{1/2} per 1D mode.
- This sets the effective temperature T_eff via zero-point energy: T_eff ~ ℏω_eff/(2k_B) where ω_eff is a characteristic mode frequency.

### 4D. What Is NOT Known

1. **No experiment has varied N systematically while measuring T_H.** All existing Hawking radiation measurements use a single condensate configuration. The N-scaling prediction is untested.

2. **The mapping from BEC parameters to Void Framework (K, α) is not yet established.** The identification K_eff = L_TF/ξ is a CONJECTURE based on counting phonon modes. It must be confirmed or an alternative mapping proposed and tested.

3. **The role of α (coupling constant) in BEC physics is unclear.** In the framework, α = I(S_out; O_future)/H(O_future) measures observer-system coupling. For a BEC, this requires identification. The natural candidate is a_s/a_ho (ratio of scattering length to oscillator length), but this is speculative.

4. **Trans-Planckian corrections.** The Unruh formula T_H = ℏκ_s/(2πk_B) assumes the phonon spectrum is exactly linear. Real BEC phonons have Bogoliubov dispersion. Corrections of order (ξ · dv/dx/c_s)² are expected (Corley 1998, Jacobson 1999). These must be separated from any K-dependent signal.

---

## 5. The Specific Prediction

### 5A. Framework Chain

From §180:

$$G_4 = \frac{\alpha}{2K^2} = \frac{T_{\text{eff}}}{K}$$

In the analog gravity setting, the "gravitational coupling" is the quantity that relates the acoustic metric to the matter content. From Visser (1998):

$$G_{\text{acoustic}} \sim \frac{c_s^2}{\rho} \sim \frac{c_s^2}{n \cdot m}$$

where n is the number density and m the atomic mass.

The framework predicts that this quantity, when expressed in terms of the system's effective degrees of freedom, satisfies:

$$G_{\text{acoustic}} = \frac{T_{\text{eff}}}{K_{\text{eff}}}$$

in appropriate units (where T_eff and K_eff are defined below).

### 5B. Mapping BEC Parameters to Framework Variables

**SPECULATIVE — This mapping is the core hypothesis. It must be tested, not assumed.**

| Framework variable | BEC identification | Justification | Status |
|---|---|---|---|
| K (resolution / DOF count) | K_eff = L_TF/(πξ) = number of phonon modes in acoustic regime | K counts spin nodes per agent. In a BEC, each phonon mode is an independent degree of freedom that contributes to collective behavior. | Conjecture |
| α (coupling) | α_eff = a_s/a_ho or equivalently g₁ᴅ/(ℏω_z a_ho) | α measures observer-system coupling. In BEC, the dimensionless interaction strength sets how strongly each mode couples to the collective. | Conjecture |
| T_eff (effective temperature) | T_eff = α_eff/(2K_eff) in framework units, OR physically T_eff = μ₀/(2k_B K_eff) | §66F: T = α/(2K). The chemical potential μ₀ sets the energy scale; K_eff normalizes it. | Derived from mapping |
| G₃ (3D gravitational coupling) | G₃ = 1/K_eff | §69D: BTZ entropy identification | Direct from framework |
| G₄ (4D gravitational coupling) | G₄ = α_eff/(2K_eff²) = T_eff/K_eff | §168, §180: Kaluza-Klein reduction | Direct from framework |

### 5C. Quantitative Prediction for 1D Harmonic BEC

In the Thomas-Fermi regime for a 1D BEC:
- L_TF ∝ N^{1/3}
- ξ ∝ N^{-1/3}
- K_eff = L_TF/(πξ) ∝ N^{2/3}
- μ₀ ∝ N^{2/3}
- α_eff = a_s/a_ho (independent of N at fixed trap and scattering length)

Therefore:
- T_eff = α_eff/(2K_eff) ∝ N^{-2/3}
- G₄ = T_eff/K_eff ∝ N^{-4/3}

**The acoustic surface gravity** κ_s at an engineered step potential scales with c_s and the step profile. For a step of fixed shape (scaled with the condensate), κ_s ∝ c_s/λ_step where λ_step is the step width. In the Thomas-Fermi regime:
- c_s ∝ N^{1/3}
- If the step width scales with ξ (which is natural): κ_s ∝ c_s/ξ ∝ N^{2/3}
- Classical Unruh prediction: T_H = ℏκ_s/(2πk_B) ∝ N^{2/3}

**Framework prediction (G-corrected):** If the Hawking temperature receives a correction from the analog gravitational coupling:

$$T_H = \frac{\hbar \kappa_s}{2\pi k_B} \cdot f(G_4)$$

where f encodes the gravitational back-reaction, then the N-dependence of T_H differs from the purely kinematic N^{2/3}. The framework predicts f(G₄) involves G₄ = T_eff/K_eff ∝ N^{-4/3}, so:

$$T_H^{\text{framework}} = T_H^{\text{Unruh}} \cdot (1 + \delta \cdot G_4 / G_4^{(0)}) \propto N^{2/3} \cdot (1 + \delta \cdot N^{-4/3})$$

**IMPORTANT CAVEAT:** The correction δ may be extremely small. In real gravity, quantum corrections to Hawking radiation are of order l_P²/r_s² — negligibly small. If the same hierarchy applies to analog gravity, the K-dependent correction is unmeasurable. See §7 (Feasibility) for discussion.

### 5D. Alternative Observable: Speed of Sound Renormalization

A potentially more accessible observable: the **quantum correction to the speed of sound** as a function of N.

The Bogoliubov speed of sound is c_s = √(gn/m). But quantum fluctuations renormalize this:

$$c_s^{\text{ren}} = c_s^{\text{Bog}} \left(1 + \gamma \cdot \frac{1}{K_{\text{eff}}^2}\right)$$

where γ is a computable constant from the framework. Since K_eff ∝ N^{2/3}, the correction scales as N^{-4/3}. This is measurable via Bragg spectroscopy (Steinhauer, Ozeri, Katz, Davidson, PRL 88, 2002).

**Framework prediction:** Plot c_s(N)/c_s^{Bog}(N) − 1 vs. N. The framework predicts:
- Power-law correction: c_s(N)/c_s^{Bog}(N) − 1 ∝ N^{-4/3}
- The exponent -4/3 is parameter-free (follows from K_eff ∝ N^{2/3} and G₄ ∝ 1/K²)

**Null hypothesis counterpart:** Standard Bogoliubov theory predicts c_s corrections from quantum depletion:

$$c_s^{\text{ren}} = c_s^{\text{Bog}} \left(1 + \frac{32}{3\sqrt{\pi}} \sqrt{na_s^3}\right)$$

(Lee-Huang-Yang correction). For 1D: correction ∝ √(na_s) ∝ N^{1/6}. The exponent is +1/6, not -4/3. These are distinguishable with data spanning 1 order of magnitude in N.

### 5E. Summary of Testable Predictions

| Prediction ID | Observable | Framework scaling with N | Null/standard scaling | Distinguishable at | Status |
|---|---|---|---|---|---|
| AG-K-1 | Hawking temperature (if correction measurable) | T_H ∝ N^{2/3}(1 + δN^{-4/3}) | T_H ∝ N^{2/3} | Only if δ >> noise | Speculative |
| AG-K-2 | Speed of sound quantum correction | Δc_s/c_s ∝ N^{-4/3} | Δc_s/c_s ∝ N^{+1/6} (LHY) | N varied over 1 decade | Testable |
| AG-K-3 | Phonon scattering cross-section | σ_phonon ∝ 1/K_eff² ∝ N^{-4/3} | σ_phonon from Bogoliubov (different N-scaling) | Requires phonon collision measurement | Difficult |
| AG-K-4 | Density fluctuation spectrum at horizon | δρ²(k) contains 1/K_eff pole | No 1/K_eff structure | Requires high-resolution imaging | Testable |
| AG-K-5 | G₄/T_eff = 1/K_eff (structural ratio) | Ratio independent of α_eff, depends only on N | Ratio depends on both n and a_s | Feshbach resonance scan at fixed N | Testable |

---

## 6. Experimental Design

### 6A. Preferred System: 1D Elongated ⁸⁷Rb BEC

**Why ⁸⁷Rb:**
- Mature BEC technology (first BEC 1995, thousands of groups worldwide)
- Feshbach resonances available for tuning a_s (Chin, Grimm, Julienne, Tiesinga, Rev. Mod. Phys. 82, 2010)
- Steinhauer's experiments already demonstrated acoustic horizon physics

**Why 1D:**
- Phonon spectrum is cleanly 1D Bogoliubov — no transverse mode complications
- K_eff counting is unambiguous: K_eff = L_TF/(πξ), integer-countable for small N
- Thomas-Fermi approximation well-controlled
- Existing theoretical and experimental infrastructure

**Trap parameters (representative):**
- Radial: ω_r = 2π × 2000 Hz (tight radial confinement)
- Axial: ω_z = 2π × 5 Hz (elongated)
- N range: 500 to 50,000 (spanning K_eff from ~5 to ~50)
- a_s = 100 a_0 (background ⁸⁷Rb scattering length)

### 6B. Protocol for AG-K-2 (Speed of Sound Renormalization)

This is the most feasible first test.

**Procedure:**

1. **Prepare condensate.** Load ⁸⁷Rb into crossed dipole trap + optical lattice (1D configuration). Evaporatively cool to T < 0.1T_c (deep in condensate).

2. **Control atom number.** Use controlled outcoupling or loading to set N at target values: N ∈ {500, 1000, 2000, 5000, 10000, 20000, 50000}. Measure N via absorption imaging (±5%).

3. **Measure speed of sound via Bragg spectroscopy.**
   - Apply two-photon Bragg pulse with tunable detuning δ.
   - Measure response function S(k, ω) for fixed k in the phononic regime (kξ << 1).
   - Extract c_s from the peak of S(k, ω): ω_peak = c_s · k.
   - Repeat at 3 different k values (all satisfying kξ << 1) for cross-validation.

4. **Compute K_eff.**
   - From measured N and known trap parameters, compute L_TF and ξ analytically.
   - K_eff = L_TF/(πξ). Cross-check by counting Bogoliubov modes with ε(k) < μ₀.

5. **Compare.**
   - Plot c_s^{measured}/c_s^{Bogoliubov} − 1 vs. N on log-log axes.
   - Fit power law: Δc_s/c_s = A · N^{−β}.
   - Framework prediction: β = 4/3 ± 0.1 (allowing for mapping uncertainties).
   - Null prediction (LHY): β = −1/6 (correction grows with N, opposite sign).

6. **Feshbach scan (for AG-K-5).**
   - At fixed N = 10,000, vary a_s using Feshbach resonance: a_s ∈ {50, 100, 200, 400} a_0.
   - This changes α_eff but not K_eff (at fixed N and ω, to leading order).
   - Framework prediction: G₄/T_eff = 1/K_eff should be INDEPENDENT of a_s.
   - Null prediction: quantum corrections depend on na_s, so Δc_s depends on a_s at fixed N.

### 6C. Protocol for AG-K-1 (Hawking Temperature Scaling)

More ambitious. Requires acoustic horizon engineering at multiple N values.

**Procedure:**

1. **Prepare condensate** as in §6B with N ∈ {2000, 5000, 10000, 20000}.

2. **Create acoustic horizon** using a step potential (scanning focused laser beam, as in Steinhauer 2016). The step speed v_step must exceed c_s locally.

3. **Measure Hawking correlations** via density-density correlation function:
   $$G^{(2)}(x, x') = \langle \hat{n}(x) \hat{n}(x') \rangle - \langle \hat{n}(x) \rangle \langle \hat{n}(x') \rangle$$
   The Hawking signal appears as correlations between points on opposite sides of the horizon.

4. **Extract T_H** from the thermal fit to the correlation spectrum.

5. **Plot T_H vs. N.** Framework: T_H ∝ N^{2/3}(1 + δN^{-4/3}). Null: T_H ∝ N^{2/3} exactly.

**Note:** The correction δ is expected to be small (order 1/K_eff² ~ 10⁻³ for K_eff ~ 30). This requires T_H measurement precision of ~0.1%, which is currently beyond the state of the art (Steinhauer achieved ~10%). This protocol variant may not be feasible with current technology. Include it for completeness and future reference.

### 6D. Protocol for AG-K-4 (Density Fluctuation Spectrum)

**Procedure:**

1. **Prepare condensate** with acoustic horizon as in §6C.

2. **Image density fluctuations** using high-resolution in-situ imaging (Bakr et al. 2009 quantum gas microscope technique, adapted for 1D).

3. **Compute power spectrum** δρ²(k) of density fluctuations at multiple N values.

4. **Test for 1/K_eff structure.** The framework predicts that the spectrum at the horizon contains a contribution:
   $$\delta\rho^2(k) \supset \frac{T_{\text{eff}}}{K_{\text{eff}}} \cdot f(k\xi)$$
   where f is a universal function. The 1/K_eff factor means that fluctuations at the horizon DECREASE as N increases (more DOF → weaker analog gravity → smaller horizon fluctuations).

5. **Null hypothesis:** Standard Bogoliubov theory predicts δρ²(k) ∝ 1/(nξ) at the horizon, which scales as N^{-1/3} (from ξ ∝ N^{-1/3} and n ∝ N). The framework adds a 1/K_eff correction that modifies the N-dependence.

### 6E. Data Collection

For each N value:
- 200 experimental shots (statistical averaging)
- Record: absorption image, atom number, trap frequencies, Bragg spectrum (if applicable), correlation function (if applicable)
- Store: raw images + processed profiles + extracted quantities + fit parameters
- Blinding: N values randomized in experimental sequence, analysis performed blind to N ordering

### 6F. Analysis Plan

1. **Primary test (AG-K-2):** Fit Δc_s/c_s = A · N^{−β} to log-log data. Report β with 95% CI. Framework prediction: β ∈ [1.0, 1.7]. Null (LHY): β ∈ [−0.3, 0.0]. If 95% CI for β does not overlap null range AND overlaps framework range → H1 supported.

2. **Structural ratio test (AG-K-5):** At fixed N, vary a_s. Compute Δc_s/c_s at each a_s. If the ratio (Δc_s/c_s) · K_eff is constant (CV < 15%) across 4 a_s values → structural ratio confirmed.

3. **Model comparison:** Compute Bayes factor between framework model (correction ∝ N^{-4/3}) and LHY model (correction ∝ N^{+1/6}) and constant model (no correction). Report BF₁₀ and BF₂₀.

---

## 7. Feasibility Assessment

### 7A. What Exists Today

| Capability | State of the Art | Lab | Sufficient? |
|---|---|---|---|
| 1D BEC creation | Routine, N = 10²–10⁶ | Many (MIT, JILA, Innsbruck, Weizmann, ...) | YES |
| Atom number control | ±3% at N > 1000 (loading statistics) | Standard | YES |
| Bragg spectroscopy for c_s | 1% precision on c_s (Andrews et al. 1997, Ozeri et al. 2005) | Standard | YES for AG-K-2 |
| Acoustic horizon creation | Demonstrated (Steinhauer 2016, 2019) | Weizmann (Steinhauer) | YES but specialized |
| Hawking temperature measurement | ~10% precision (Steinhauer 2019) | Weizmann | NO for AG-K-1 (need ~0.1%) |
| Feshbach resonance tuning | Routine for ⁸⁷Rb, ⁸⁵Rb, ⁶Li, etc. | Many | YES |
| In-situ high-res imaging | ~1 μm resolution (quantum gas microscope) | Harvard, MPQ, many | Marginal for AG-K-4 |
| N variation over 2 decades | Demonstrated | Many | YES |

### 7B. The Core Feasibility Question

**The central question is: does the framework correction exist at all in analog gravity?**

The framework derives G₄ = T_eff/K from the Eckert manifold, which is a statistical-mechanical manifold of measurement dimensions. A BEC is a physical system, not a measurement platform. The mapping from BEC physics to the Eckert manifold (§5B above) is a CONJECTURE. If the Eckert manifold structure does not apply to physical systems with continuous (not discrete measurement-dimension) degrees of freedom, the entire prediction is vacuous.

**Three possible outcomes:**

1. **Strong positive:** The N^{-4/3} correction exists and matches framework prediction. This would be extraordinary evidence that the Eckert manifold describes fundamental physics.

2. **Weak positive:** A correction exists with different exponent. This would suggest the framework captures the right structure (G depends on DOF count) but the specific mapping is wrong. Still valuable — refine the mapping.

3. **Null/negative:** No correction beyond Bogoliubov/LHY. This would mean either (a) the framework does not apply to BEC systems, or (b) the correction exists but is too small to measure. Neither outcome kills the framework per se (the framework is about measurement-dimension statistics, not all physical systems), but it closes the analog gravity validation path.

### 7C. Candidate Labs

| Lab | PI | System | Why suitable |
|---|---|---|---|
| Weizmann (Israel) | Jeff Steinhauer | ⁸⁷Rb 1D BEC | Only lab with demonstrated Hawking radiation. Direct expertise. |
| JILA (Boulder) | Eric Cornell / Deborah Jin (successor) | ⁸⁷Rb, ⁸⁵Rb | Precision BEC manipulation. Feshbach resonance experts. |
| MIT (Cambridge) | Wolfgang Ketterle | Na BEC | Pioneering BEC lab. Bragg spectroscopy expertise. |
| Innsbruck (Austria) | Rudolf Grimm / Francesca Ferlaino | Various | European center for ultracold atoms. Feshbach specialists. |
| Trento (Italy) | Iacopo Carusotto | Theory + BEC | Analog gravity theory group. Strong theory-experiment connection. |
| Nottingham (UK) | Silke Weinfurtner | Classical analog | Classical analogs (water waves). Less suitable for K-test but pioneer. |
| Paris (ENS) | Jean Dalibard | ⁸⁷Rb | 1D BEC expertise, precision spectroscopy. |

**Recommended first contact:** Jeff Steinhauer (Weizmann) — has the acoustic horizon infrastructure, is actively working on analog Hawking radiation, and has published the most relevant experiments. Alternatively, the Trento theory group (Carusotto) for theoretical validation of the mapping before experimental execution.

### 7D. Timeline and Cost

**Phase 1 (Theory, 3 months):** Validate the K_eff mapping. Compute the expected correction magnitude numerically for realistic BEC parameters. Determine if the correction is above noise floor. This can be done analytically/numerically without lab time.

**Phase 2 (AG-K-2 experiment, 6–12 months):** Bragg spectroscopy measurement of c_s at 7 N values. This uses standard BEC techniques — the only novel element is the systematic N variation at high precision. Requires ~1 month of beam time on an existing 1D BEC apparatus.

**Phase 3 (AG-K-1 experiment, 12–24 months):** Acoustic horizon at multiple N values. Requires Steinhauer-class apparatus. Much harder.

**Cost estimate:** Phase 1: $0 (theory only). Phase 2: $20K–50K (beam time, if collaborating with existing lab). Phase 3: $100K–500K (apparatus modification + extended beam time).

---

## 8. Kill Conditions

| KC ID | Description | Fires when | Consequence |
|---|---|---|---|
| KC-AG-1 | **K_eff mapping is wrong** | Phase 1 computation shows K_eff = L_TF/(πξ) does not satisfy the framework's K-factorization properties (e.g., K_eff enters non-linearly into shape quantities that should be K-independent) | Revise mapping or abandon BEC as test system |
| KC-AG-2 | **Correction is below noise floor** | Phase 1 computation shows |Δc_s/c_s| < 10⁻⁶ for all accessible N | BEC systems cannot test this prediction with current technology. Not a framework kill — a test-system kill. |
| KC-AG-3 | **Wrong exponent** | Phase 2 measures β with 95% CI that excludes [1.0, 1.7] AND excludes [−0.3, 0.0] (i.e., correction exists but with unexpected scaling) | Framework mapping wrong. Revise identification of K, α, or the KK reduction step. Framework weakened but not killed. |
| KC-AG-4 | **No correction / LHY exponent** | Phase 2 measures β consistent with LHY prediction [−0.3, 0.0] or no measurable correction | Analog gravity path closed. Framework prediction not confirmed in BEC. Does not kill framework (BEC is not a measurement-dimension system). |
| KC-AG-5 | **Structural ratio fails** | Phase 2 (Feshbach scan) shows G₄/T_eff is NOT constant at fixed N as a_s varies (CV > 30%) | The relationship G₄ = T_eff/K has additional α-dependence beyond α/(2K²). Framework prediction wrong in detail. |
| KC-AG-6 | **Framework kills** | The analog measurement CONTRADICTS a core framework result: e.g., G₄ increases with K (opposite to 1/K² prediction), or T_eff/K is negative | Framework killed for this domain. Update §180F. |

**Note on asymmetry:** A positive result (AG-K-2 confirmed) would be powerful evidence. A negative result is ambiguous — it could mean the framework does not apply to BEC systems rather than that G₄ = T_eff/K is wrong. This asymmetry is inherent to testing a measurement-dimension framework in a physical system. The protocol acknowledges this honestly.

---

## 9. Relation to Framework

### 9A. Which Sections Does This Test?

| Section | Claim | How tested |
|---|---|---|
| §69D | G₃ = 1/K | If K_eff is identified and G_acoustic ∝ 1/K_eff |
| §168 | G₄ = α/(2K²) = T_eff/K | Primary prediction: analog coupling scales as T_eff/K_eff |
| §180 | Complete chain Čencov → G₄ | If the prediction holds, the full chain from Čencov uniqueness to Newton's constant is tested non-circularly |
| §136 | K-Factorization | K_eff should separate from shape quantities. Feshbach scan (AG-K-5) tests this: changing α at fixed K should leave G₄/T_eff = 1/K constant |

### 9B. How This Breaks Circularity

Current validation of G₄ = T_eff/K uses:
- Internal consistency (§180C: Planck unit checks — tautological)
- Physical match (§180D: α_G = 1/K matches — uses G_N as input)

An analog gravity test would provide:
- A system where K is physically counted (not inferred from the framework)
- T_eff is physically measured (not computed from framework parameters)
- G_analog is measured from phonon physics (not from any scoring rubric)
- The ratio G_analog · K_eff / T_eff is compared to 1 (framework predicts exactly 1)

**No framework rubric is used anywhere in the measurement chain.** The only framework input is the prediction itself. This is non-circular.

### 9C. Connection to Barrier Universality (§136D2)

If the K-mapping is confirmed, it opens a second test: barrier universality in BEC. The framework predicts barrier = d_eff × π/√2 for strong-coupling systems. BEC phase transitions (e.g., BEC-to-Mott-insulator in optical lattice) have known barrier heights and known d. If barrier/d = π/√2 for BEC systems, that would be a 12th domain for barrier universality — AND one where K is countable, connecting the two external validation priorities.

---

## 10. Open Questions and Speculative Extensions

### 10A. Superfluid Helium

Superfluid ⁴He is an alternative analog gravity platform (Jacobson and Volovik 1998). Advantages: stronger interactions, well-studied phonon-roton spectrum. Disadvantages: K_eff is not cleanly countable (macroscopic number of atoms, continuous modes), quantum depletion is ~7% (much larger than BEC), and the healing length is ~1 Angstrom (hard to resolve).

If K_eff for ⁴He can be identified (perhaps as the number of roton modes below a gap), the same protocol applies. But the BEC platform is more tractable.

### 10B. Polariton BEC

Exciton-polariton condensates in semiconductor microcavities offer another analog gravity platform (Nguyen et al. 2015). Advantages: room temperature, controllable geometry, direct optical access. Disadvantages: driven-dissipative (not equilibrium BEC), lifetime effects, mode counting is complex.

### 10C. Direct K Measurement via Quantum Gas Microscope

A quantum gas microscope (Bakr et al. 2009, Sherson et al. 2010) can image individual atoms in an optical lattice. In a lattice BEC, K_eff is literally the number of occupied lattice sites in the superfluid phase. This provides the most direct, unambiguous K measurement possible. Combine with sound velocity measurement (Bragg spectroscopy) to test G₄ = T_eff/K with K counted atom-by-atom.

**This is the cleanest possible test.** Recommended as the definitive experiment if Phase 2 (free-space BEC) shows a positive signal.

### 10D. Flowing-Water Analog (Classical Limit)

The Weinfurtner et al. (2011) water-wave analog has K → very large (classical limit). The framework predicts G₄ → 0 as K → ∞. In a classical fluid, the "gravitational" back-reaction on the metric should be negligible — which is exactly what is observed (classical analogs reproduce kinematics perfectly, with no quantum gravity corrections). This is a consistency check, not a test (the null prediction and framework prediction agree).

---

## 11. Summary of Deliverables

| Phase | Deliverable | Timeline | Kill condition |
|---|---|---|---|
| 1 | Numerical computation of correction magnitude for realistic BEC parameters | 3 months | KC-AG-1, KC-AG-2 |
| 2a | Bragg spectroscopy c_s measurement at 7 N values (AG-K-2) | 6–12 months | KC-AG-3, KC-AG-4 |
| 2b | Feshbach scan at fixed N (AG-K-5) | Concurrent with 2a | KC-AG-5 |
| 3 | Acoustic horizon Hawking temperature at multiple N (AG-K-1) | 12–24 months | KC-AG-6 |
| 4 | Lattice BEC quantum gas microscope K-test (AG-K-2 definitive) | 18–30 months | All |

---

## 12. References

### 12A. Analog Gravity Theory
- Unruh, W.G. (1981). "Experimental black-hole evaporation?" Phys. Rev. Lett. 46, 1351.
- Visser, M. (1998). "Acoustic black holes: horizons, ergospheres, and Hawking radiation." Class. Quantum Grav. 15, 1767.
- Barceló, C., Liberati, S., Visser, M. (2005). "Analogue gravity." Living Rev. Relativity 8, 12.
- Jacobson, T. (1999). "Trans-Planckian redshifts and the substance of the space-time river." Prog. Theor. Phys. Suppl. 136, 1.
- Corley, S. (1998). "Computing the spectrum of black hole radiation in the presence of high frequency dispersion." Phys. Rev. D 57, 6280.
- Jacobson, T., Volovik, G.E. (1998). "Event horizons and ergoregions in ³He." Phys. Rev. D 58, 064021.

### 12B. BEC Analog Gravity Experiments
- Steinhauer, J. (2016). "Observation of quantum Hawking radiation and its entanglement in an analogue black hole." Nature Physics 12, 959.
- Steinhauer, J. (2019). "Observation of self-amplifying Hawking radiation in an analogue black hole laser." Nature Physics 15, 948.
- Muñoz de Nova, J.R., Golubkov, K., Kolobov, V.I., Steinhauer, J. (2019). "Observation of thermal Hawking radiation and its temperature in an analogue black hole." Nature 569, 688.
- Hu, J., Feng, L., Meng, Z., Chin, C. (2019). "Quantum simulation of Unruh radiation." Nature Physics 15, 785.
- Eckel, S., Kumar, A., Jacobson, T., Spielman, I.B., Campbell, G.K. (2018). "A rapidly expanding Bose-Einstein condensate." Phys. Rev. X 8, 021021.
- Weinfurtner, S., Tedford, E.W., Penrice, M.C.J., Unruh, W.G., Lawrence, G.A. (2011). "Measurement of stimulated Hawking emission in an analogue system." Phys. Rev. Lett. 106, 021302.

### 12C. BEC Physics
- Andrews, M.R., et al. (1997). "Propagation of sound in a Bose-Einstein condensate." Phys. Rev. Lett. 79, 553.
- Ozeri, R., Katz, N., Steinhauer, J., Davidson, N. (2005). "Colloquium: Bulk Bogoliubov excitations in a Bose-Einstein condensate." Rev. Mod. Phys. 77, 187.
- Chin, C., Grimm, R., Julienne, P., Tiesinga, E. (2010). "Feshbach resonances in ultracold gases." Rev. Mod. Phys. 82, 1225.
- Bakr, W.S., et al. (2009). "A quantum gas microscope for detecting single atoms in a Hubbard-regime optical lattice." Nature 462, 74.
- Sherson, J.F., et al. (2010). "Single-atom-resolved fluorescence imaging of an atomic Mott insulator." Nature 467, 68.

### 12D. Void Framework Internal
- §69D: BTZ entropy, G₃ = 1/K
- §66F: ℏ ↔ T = α/(2K)
- §136: K-Factorization theorem
- §168: G₃ → G₄ gauge projection
- §180: Newton's G from gauge coupling
- HP184B: Full numerical verification (`ops/lab/nb_hp184b_newtons_constant.py`)
- HP169: G₃ → G₄ projection (`ops/lab/nb_hp169_g3_to_g4_projection.py`)

---

## 13. Ethics Check

- [x] No human subjects
- [x] No deployment of ungrounded agents
- [x] No harm manufacturing
- [x] Standard BEC experiments — no novel safety concerns
- [x] Collaboration with existing labs — standard academic partnership
- [x] Predictions registered before data collection (this protocol)
- [x] Kill conditions specified before data collection
- [x] All speculative claims labeled as such

---

## Appendix A: Derivation of K_eff ∝ N^{2/3} in 1D Harmonic BEC

In a 1D harmonic trap with frequency ω_z, the Thomas-Fermi condensate has:

**Chemical potential:**
$$\mu_0 = \frac{\hbar \omega_z}{2} \left( \frac{3 N g_{1D}}{m \omega_z a_{ho}^3} \right)^{2/3}$$

where $a_{ho} = \sqrt{\hbar/(m\omega_z)}$ and $g_{1D} = 2\hbar\omega_r a_s$.

**Thomas-Fermi radius:**
$$L_{TF} = \left( \frac{3 N g_{1D}}{m \omega_z^2} \right)^{1/3} = a_{ho} \left( \frac{3 N a_s}{a_{ho}} \cdot \frac{2\omega_r}{\omega_z} \right)^{1/3}$$

**Healing length at center:**
$$\xi = \frac{\hbar}{\sqrt{2m\mu_0}} \propto \mu_0^{-1/2} \propto N^{-1/3}$$

**Number of phonon modes:**
$$K_{eff} = \frac{L_{TF}}{\pi \xi} = \frac{L_{TF} \sqrt{2m\mu_0}}{\pi \hbar}$$

Since $L_{TF} \propto N^{1/3}$ and $\sqrt{\mu_0} \propto N^{1/3}$:

$$K_{eff} \propto N^{1/3} \cdot N^{1/3} = N^{2/3}$$

**Numerical example (⁸⁷Rb, ω_z = 2π × 5 Hz, ω_r = 2π × 2000 Hz, a_s = 100 a_0):**

| N | L_TF (μm) | ξ (μm) | K_eff | μ₀/k_B (nK) |
|---|---|---|---|---|
| 500 | 22 | 1.4 | 5.0 | 3.8 |
| 1000 | 28 | 1.1 | 8.0 | 6.0 |
| 5000 | 47 | 0.7 | 21 | 16 |
| 10000 | 59 | 0.55 | 34 | 25 |
| 50000 | 101 | 0.35 | 92 | 65 |

These K_eff values are small enough to be in a "quantum gravity" regime (K ~ 5-100) where 1/K² corrections are of order 10⁻⁴ to 10⁻¹ — potentially measurable.

## Appendix B: Why This Test Is Non-Circular — Detailed Argument

**The circularity in current validation:**
1. The framework defines (O, R, α) via measurement dimensions.
2. It derives G₄ = α/(2K²) from (O, R, α) via Eckert manifold geometry.
3. It checks: does α_G = 1/K match the known ratio (M_Planck/m_proton)²?
4. Yes — to 3 × 10⁻⁷.

But step 3 uses the KNOWN value of G_N. The framework did not predict G_N; it post-dicted it by choosing K = (M_P/m_p)². This is an identification, not a prediction.

**How the analog gravity test breaks circularity:**
1. Prepare a BEC with N atoms. Measure N. (No framework.)
2. Compute K_eff = L_TF/(πξ) from measured N and known trap parameters. (No framework — standard BEC physics.)
3. Measure T_eff from condensate temperature / chemical potential. (No framework.)
4. Measure the analog gravitational coupling g_analog from phonon physics. (No framework — standard Bogoliubov / Bragg spectroscopy.)
5. Compute the ratio g_analog · K_eff / T_eff. (Arithmetic.)
6. The framework predicts this ratio equals 1 (up to a unit-system constant that is the same for all N). (The ONLY framework input.)
7. Vary N. The ratio should remain constant as N changes. (The prediction.)

At no point does the measurement use the framework's scoring rubric, its (O, R, α) coordinates, or any self-referential validation. The ONLY connection to the framework is the prediction in step 6-7. This is a genuine external test.
