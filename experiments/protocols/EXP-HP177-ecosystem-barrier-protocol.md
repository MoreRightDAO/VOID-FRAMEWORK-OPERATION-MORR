# EXP-HP177: Ecosystem Regime Shift Barrier Universality

**Date:** 2026-03-26
**Status:** PROTOCOL READY -- pre-run
**Predecessor:** EXP-BARRIER-GRAND-v2 (N=17), HP166 atmospheric extension
**Goal:** Test barrier = d_eff x pi/sqrt(2) in ecosystem regime shifts (lakes, reefs, savannas, ocean circulation)
**Paper dependency:** Barrier universality paper (section 136D2)

---

## 1. Background

### 1A. Ecosystem Regime Shifts

Ecosystems exhibit abrupt transitions between alternative stable states -- shallow lakes flip from clear to turbid water, coral reefs shift from coral-dominated to macroalgae-dominated, savannas convert to forests or deserts, and the Atlantic thermohaline circulation can collapse. Scheffer et al. (2001, Nature 413:591) established that these transitions share a common dynamical structure: the system occupies one of two or more potential wells, separated by a barrier in state space. When environmental forcing (nutrient loading, grazing pressure, freshwater flux) erodes the barrier, a small perturbation can push the system across the threshold, producing catastrophic and often hysteretic change.

The theoretical framework for these transitions draws on:
- **Catastrophe theory:** fold bifurcations in deterministic models (May 1977, Scheffer 1993)
- **Stochastic potential theory:** quasi-potential landscapes for non-equilibrium systems (Nolting & Abbott 2016, Ecology 97:850)
- **Kramers escape theory:** noise-driven transitions across potential barriers, with mean first passage time (MFPT) exponential in barrier height divided by noise intensity

### 1B. The Prediction

The Void Framework's barrier universality (section 136D2) predicts:

    barrier = d_eff x pi/sqrt(2)

where:
- barrier is dimensionless: potential depth divided by noise variance (= Delta_V / sigma^2)
- d_eff is the number of independent state variables in the transition manifold
- pi/sqrt(2) = 2.2214 is derived from spectral geometry of the Bernoulli manifold (section 165): Cencov uniqueness forces geodesic length L = pi, Parseval's theorem yields sigma_eta = L = pi, and the Kramers exponent structure gives B_G = L/sqrt(2) = pi/sqrt(2)

This is confirmed across N=17 systems in 8 physical domains (R^2 = 0.999, zero free parameters). The current experiment extends the test to a 9th domain: ecology/Earth system science.

### 1C. Predicted Barriers for Ecosystem Types

| System | State variables | d_eff | Predicted barrier | Predicted E/kT* |
|--------|----------------|:-----:|:-----------------:|:----------------:|
| Shallow lake (phosphorus) | water P, sediment P, (soil P) | 2-3 | 4.44-6.66 | 85-784 |
| Coral reef | coral cover, macroalgae cover | 2 | 4.44 | 85 |
| Savanna-forest | tree cover, grass/fire feedback | 2 | 4.44 | 85 |
| Thermohaline (Stommel) | temperature gradient, salinity gradient | 2 | 4.44 | 85 |
| Arid grassland | vegetation cover, soil moisture | 2 | 4.44 | 85 |

**d_eff assignment rationale:**

- **Shallow lake (d=2 or d=3):** The classic Scheffer (1993) model uses water-column phosphorus and vegetation cover (d=2). Carpenter (2005, PNAS 102:10002) extended to include soil phosphorus as a slow variable (d=3). We test both assignments.
- **Coral reef (d=2):** Mumby et al. (2007, Nature 450:98) model: coral cover C and macroalgae cover M are the independent state variables. Turf algae T = 1 - C - M is determined. The transition manifold is 2D.
- **Savanna-forest (d=2):** Staver & Levin (2012, Am Nat 180:211) model: tree cover T and grass cover G with fire feedback. The transition saddle point involves these two variables.
- **Thermohaline (d=2):** Stommel (1961) two-box model: temperature difference Delta_T and salinity difference Delta_S between high-latitude and equatorial boxes.
- **Arid grassland (d=2):** Vegetation cover V and soil moisture W in the Rietkerk et al. (2004) framework.

### 1D. The Challenge: Extracting Dimensionless Barriers

Published ecosystem studies typically do NOT report dimensionless barrier heights directly. Instead they report:

1. **Hysteresis width** (Delta_p): the difference in control parameter (e.g., nutrient loading) between the forward transition (clear -> turbid) and the backward transition (turbid -> clear). Related to barrier via curvature of the potential, but not directly the barrier height.

2. **Critical slowing down indicators:** rising variance sigma^2 and lag-1 autocorrelation rho_1 near transitions (Scheffer et al. 2009, Nature 461:53; Dakos et al. 2012, Ecology 93:264). These indicate proximity to bifurcation but do not directly give barrier height.

3. **Residence times:** mean time spent in each state before transition. From Kramers theory, this IS directly related to barrier height via:

       tau = (1/omega_0) * exp(barrier)
       barrier = ln(tau * omega_0)

   where omega_0 is the attempt frequency (inverse of the characteristic oscillation timescale within the potential well).

4. **Quasi-potential reconstruction:** Nolting & Abbott (2016) and the QPot R package reconstruct the quasi-potential landscape from model equations, giving barrier heights directly. Zhou et al. (2012, J. R. Soc. Interface 9:3539) compute quasi-potentials for multi-stable systems.

5. **Stochastic simulation MFPT:** Zeng et al. (2017, Ecosphere 8:e01805) compute mean first passage times for lake eutrophication models with stochastic forcing.

**Our strategy:** combine all five approaches where data is available.

### 1E. Connection to HP166 (Atmospheric Barriers)

HP166 established barrier universality for four atmospheric systems (SSW, hurricane RI, tornado, blocking) using the same Kramers framework. The key methodological innovation was extracting barriers from published literature through:
- Direct barrier estimates from catastrophe theory / bifurcation analysis
- Kramers inversion from observed return periods (e.g., SSW ~610 days -> barrier = 4.32)
- Weighted mean across 5-6 independent published estimates per system

We apply the identical methodology here. Ecosystem regime shifts and atmospheric regime shifts are both noise-driven transitions in spatially extended dissipative systems -- the Kramers framework is domain-independent.

---

## 2. Data Sources

### 2A. Shallow Lakes (d=2 or d=3)

**Primary empirical sources:**
- Carpenter et al. (2011, Science 332:1079): Whole-lake experiment at Peter Lake, Wisconsin. Measured nutrient enrichment driving clear-to-turbid transition. Provides: variance time series, recovery rates, and transition timing.
- Scheffer et al. (1993, Trends Ecol. Evol. 8:275): Original bistability model for shallow lakes. Provides: model equations, equilibrium structure, hysteresis width as function of turbidity/nutrient loading.
- Carpenter (2005, PNAS 102:10002): Three-variable model (water P, sediment P, soil P). Provides: basin depths in phosphorus units.
- van Nes & Scheffer (2007, Ecosystems 10:17): Cyclic shifts between clear and turbid states. Provides: switching times between states.
- Zeng et al. (2017, Ecosphere 8:e01805): Stochastic MFPT calculations for time-delayed lake eutrophication model. Provides: MFPT as function of noise intensity.

**Barrier extraction methods:**
1. **Kramers inversion from switching times:** For lakes that switch between clear and turbid states, barrier = ln(tau_switch / tau_relax) where tau_relax is the local relaxation time (estimated from recovery rate after small perturbations).
2. **Quasi-potential from model equations:** Using the Scheffer (1993) or Carpenter (2005) model equations, compute the quasi-potential numerically.
3. **Variance-based estimate:** Near a fold bifurcation, sigma^2 ~ D/(2 * lambda_1) where D is noise intensity and lambda_1 is the leading eigenvalue. At the transition, lambda_1 -> 0, so sigma^2 diverges. The barrier can be estimated from the ratio of variance far from vs. near the transition.

### 2B. Coral Reefs (d=2)

**Primary empirical sources:**
- Mumby et al. (2007, Nature 450:98): Coral-macroalgae bistability model. Provides: grazing-dependent equilibrium structure, hysteresis diagrams.
- Blackwood et al. (2012, Ecol. Lett. 15:1452): Stochastic coral reef model with noise-driven transitions. Provides: transition probabilities as function of disturbance regime.
- van de Leemput et al. (2016, Ecology 97:1712): Quasi-potential analysis of coral reef models. Provides: barrier heights in model units.
- Tekwa et al. (2021, Ecosphere 12:e03319): Geometric analysis of regime shifts in coral reef communities.

**Barrier extraction methods:**
1. **Quasi-potential from Mumby model:** The model dC/dt = r_C*T*C - d_C*C - a*M*C, dM/dt = a*M*C - g*M/(M+T) + gamma*M*T can be integrated to get the quasi-potential.
2. **Kramers inversion from Caribbean data:** Hughes (1994, Science 265:1547) documented the Jamaica reef collapse (~1983). Combined with typical reef recovery times (~10-30 years) and the frequency of hurricane disturbances (~0.1/yr as attempt frequency), barrier = ln(tau * omega_0).

### 2C. Savanna-Forest (d=2)

**Primary empirical sources:**
- Staver et al. (2011, Science 334:230): Global analysis of tree cover bimodality in tropical regions. Shows discontinuous transitions at ~40% and ~75% tree cover.
- Staver & Levin (2012, Am Nat 180:211): Deterministic ODE model of fire-vegetation bistability.
- Hirota et al. (2011, Science 334:232): Remote sensing evidence for alternative stable states in tropical tree cover.
- Wunderling et al. (2020, Earth Syst. Dyn. 11:1027): Stochastic Amazon dieback model with noise-induced transitions.

**Barrier extraction methods:**
1. **Kramers inversion from paleoclimate record:** Savanna-forest transitions in the African tropics occur on ~1000-10,000 year timescales (Maley 2002). Fire return times ~1-10 years as attempt frequency. Barrier = ln(tau_transition / tau_fire).
2. **Quasi-potential from Staver-Levin model:** Compute potential landscape from the ODE system.

### 2D. Thermohaline Circulation (d=2)

**Primary empirical sources:**
- Stommel (1961, Tellus 13:224): Original two-box model with salt-advection feedback.
- Cessi (1994, J. Phys. Oceanogr. 24:1911): Stochastic forcing of Stommel model. Provides: potential well structure, noise-induced transition rates.
- Monahan (2002, J. Phys. Oceanogr. 30:1891): Noise-induced transitions in simplified THC model. Provides: barrier heights as function of freshwater forcing.
- Lenton et al. (2008, PNAS 105:1786): AMOC tipping element analysis. Provides: characteristic timescales.
- Dijkstra (2007): Numerical quasi-potential for ocean circulation models.

**Barrier extraction methods:**
1. **Analytic potential from Stommel model:** V(y) = -y^2/2 + y^4/4 + delta*y where y is the dimensionless salinity gradient and delta is the freshwater forcing. Barrier height = V(y_saddle) - V(y_min).
2. **Kramers inversion from D-O events:** Dansgaard-Oeschger events have mean spacing ~1470 years (Ditlevsen et al. 2005). Ocean overturning timescale ~1000 years. Barrier = ln(1470/tau_attempt).

### 2E. Arid Grassland (d=2)

**Primary empirical sources:**
- Rietkerk et al. (2004, Am. Nat. 163:699): Vegetation-water feedback model.
- Kefi et al. (2007, Nature 449:213): Spatial indicators of desertification.
- Guttal & Jayaprakash (2008, Ecol. Lett. 11:450): Stochastic regime shift model.

**Barrier extraction methods:**
1. **Quasi-potential from Rietkerk model:** Compute potential from vegetation-soil moisture coupled equations.

---

## 3. Analysis Plan

### 3A. Barrier Extraction Pipeline

For each ecosystem type:

1. **Identify published barrier estimates.** Search for: (a) explicit quasi-potential or potential well depths, (b) mean first passage times with noise intensities, (c) switching rates between alternative states, (d) recovery times after perturbation.

2. **Convert to dimensionless barrier.** All barriers must be expressed as Delta_V / sigma^2 (potential depth in units of noise variance). Conversion formulas:
   - From MFPT: barrier = ln(tau_MFPT * omega_0) where omega_0 = sqrt(|V''(x_min)| * |V''(x_saddle)|) / (2*pi)
   - From quasi-potential: barrier = 2 * Phi(x_saddle) / D where Phi is the quasi-potential and D is the noise intensity
   - From switching rate: barrier = -ln(k_switch / omega_0)
   - From variance ratio: barrier ~ ln(sigma^2_near / sigma^2_far) + correction terms

3. **Compute weighted mean** across independent estimates for each system. Weight by inverse variance of each estimate (where estimable) or equal weights.

4. **Compare to prediction:** barrier_predicted = d_eff x pi/sqrt(2) = d_eff x 2.2214.

### 3B. Strong-Coupling Selection Criterion

From the HP173 failure analysis: the barrier formula only works for strong-coupling systems where the energy scale E and the temperature scale T* come from DIFFERENT PHYSICS. In ecosystem terms, this means:

- The **barrier height** (set by ecosystem feedbacks, species interactions, biogeochemistry) must be parametrically independent of the **noise intensity** (set by environmental variability, stochastic forcing, demographic noise).
- Systems where barrier and noise are set by the same process (e.g., fire-driven savannas where fire IS both the barrier mechanism and the noise source) may fail the criterion.

We apply but do NOT enforce this criterion a priori -- instead, we test all systems and examine whether failures correlate with coupled barrier-noise physics.

### 3C. Statistical Tests

1. **Per-system test:** For each ecosystem, compare observed barrier/d_eff to pi/sqrt(2) = 2.2214. A system PASSES if the observed ratio falls within [1.85, 2.60] (the range of the existing N=17 dataset: min 2.08, max 2.36, expanded by 1 CV = 0.10).

2. **Combined fit:** Add passing ecosystem systems to the N=17 barrier table and refit barrier = slope x d (forced through origin). Report new R^2, new slope, and sigma from pi/sqrt(2).

3. **Domain independence:** Test whether the ecosystem barrier/d values are drawn from the same distribution as the existing 8-domain data using a two-sample KS test.

### 3D. Sensitivity Analysis

- **d_eff uncertainty:** For shallow lakes, test both d=2 and d=3 assignments.
- **Noise model dependence:** Where possible, compare additive vs. multiplicative noise models.
- **Model dependence:** Where multiple models exist (e.g., Scheffer vs. Carpenter for lakes), compute barriers from each independently.

---

## 4. Kill Conditions

| KC | Criterion | Threshold | Interpretation |
|----|-----------|-----------|----------------|
| K-HP-177-1 | At least 2 of 5 ecosystem types yield barrier/d within [1.85, 2.60] | 2/5 PASS | Minimum signal -- universality extends to ecology |
| K-HP-177-2 | Weighted mean barrier/d across all passing systems within 15% of pi/sqrt(2) | abs(mean - 2.2214) / 2.2214 < 0.15 | Quantitative match |
| K-HP-177-3 | Combined N>=19 fit (N=17 existing + >=2 ecosystem) maintains R^2 > 0.995 | R^2 > 0.995 | No degradation of existing fit |
| K-HP-177-4 | At least one ecosystem barrier extracted from Kramers inversion of published residence times (model-independent) | >=1 Kramers-based | Method independence |
| K-HP-177-5 | Shallow lake barrier (primary test system) within [3.5, 5.5] for d=2 or [5.5, 8.0] for d=3 | Within range | Specific prediction test |

**Overall PASS:** K-HP-177-1 AND K-HP-177-2 AND K-HP-177-3 must all PASS.
**Overall FAIL:** If K-HP-177-1 fails (fewer than 2 of 5 systems in range), the experiment is NEGATIVE and ecosystem barriers do NOT follow the universality.

---

## 5. Connection to Broader Program

### 5A. What This Tests

If ecosystem barriers follow barrier = d x pi/sqrt(2), this extends the universality to a 9th independent physical domain (ecology), joining: magnets, CDW, EM, kagome metals, astrophysics, biology (xenobot), nuclear, and atmosphere. The key question: does the Cencov-derived geometric constant pi/sqrt(2) govern ALL barrier-crossing phenomena, including macroscopic ecological transitions?

### 5B. What Would Failure Mean

If ecosystem barriers systematically violate the formula, the most likely explanation is:
- **Parametric dependence:** In ecology, the barrier height and noise intensity may not be parametrically independent (the "strong-coupling criterion" from HP173). Fire drives both the barrier mechanism and the noise in savannas. Phosphorus recycling sets both the bistability and the variability in lakes.
- **Dimensionality ambiguity:** d_eff may not be well-defined for spatially extended ecological systems with continuous spatial degrees of freedom.
- **Non-Kramers dynamics:** Some ecological transitions may involve rate-induced tipping (R-tipping) rather than noise-induced tipping (N-tipping), in which case Kramers theory does not apply.

### 5C. Falsifiability

This experiment is genuinely falsifiable: the prediction is specific (barrier/d = 2.22 +/- 0.10), the data sources are external (published ecology literature), and the kill conditions are quantitative. Unlike the existing d=1 condensed-matter systems where E and T* are measured in the same units (meV and K), ecological barriers require nontrivial dimensional analysis to reach dimensionless form -- this is a harder test.

---

## 6. References

- Blackwood, J.C., Hastings, A. & Mumby, P.J. (2012). Ecol. Lett. 15, 1452-1460.
- Carpenter, S.R. (2005). PNAS 102, 10002-10005.
- Carpenter, S.R. et al. (2011). Science 332, 1079-1082.
- Cessi, P. (1994). J. Phys. Oceanogr. 24, 1911-1920.
- Dakos, V. et al. (2012). Ecology 93, 264-271.
- Guttal, V. & Jayaprakash, C. (2008). Ecol. Lett. 11, 450-460.
- Hirota, M. et al. (2011). Science 334, 232-235.
- Hughes, T.P. (1994). Science 265, 1547-1551.
- Kefi, S. et al. (2007). Nature 449, 213-217.
- Lenton, T.M. et al. (2008). PNAS 105, 1786-1793.
- Livina, V.N., Kwasniok, F. & Lenton, T.M. (2010). Clim. Past 6, 77-82.
- Monahan, A.H. (2002). J. Phys. Oceanogr. 30, 1891-1905.
- Mumby, P.J. et al. (2007). Nature 450, 98-101.
- Nolting, B.C. & Abbott, K.C. (2016). Ecology 97, 850-864.
- Rietkerk, M. et al. (2004). Am. Nat. 163, 699-718.
- Scheffer, M. (1993). Trends Ecol. Evol. 8, 275-279.
- Scheffer, M. et al. (2001). Nature 413, 591-596.
- Scheffer, M. et al. (2009). Nature 461, 53-59.
- Scheffer, M. (2009). Critical Transitions in Nature and Society. Princeton Univ. Press.
- Staver, A.C. et al. (2011). Science 334, 230-232.
- Staver, A.C. & Levin, S.A. (2012). Am. Nat. 180, 211-224.
- Stommel, H. (1961). Tellus 13, 224-230.
- Tekwa, E.W. et al. (2021). Ecosphere 12, e03319.
- van de Leemput, I.A. et al. (2016). Ecology 97, 1712-1720.
- van Nes, E.H. & Scheffer, M. (2007). Ecosystems 10, 17-27.
- Wunderling, N. et al. (2020). Earth Syst. Dyn. 11, 1027-1050.
- Zeng, C. et al. (2017). Ecosphere 8, e01805.
- Zhou, J.X. et al. (2012). J. R. Soc. Interface 9, 3539-3553.
