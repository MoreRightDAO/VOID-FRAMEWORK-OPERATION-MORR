# Barrier Universality Dataset Candidates

**Date:** 2026-03-28
**Goal:** Extend barrier = d x pi/sqrt(2) from 8-9 domains to 15+ domains
**Current state:** N=17 systems, 8 domains, R^2=0.999, slope=2.1994 +/- 0.0175, pi/sqrt(2)=2.2214 within 95% CI

## Current Domains (Already Tested)

| # | Domain | Systems | d values | Status |
|---|--------|---------|----------|--------|
| 1 | Quasi-1D magnets | CoNb2O6, CuGeO3, KCuF3, TiOCl, BaCoO3, Sr3NiIrO6 | d=1 | 6 systems, PASS |
| 2 | CDW | NbSe3 | d=1 | PASS |
| 3 | EM (Josephson/MTJ) | Nb JJ, CoFeB MTJ | d=1 | PASS |
| 4 | Kagome metals | Ni3In | d=2 | PASS |
| 5 | Atmosphere | SSW, Hurricane RI, Blocking, Tornado | d=2,3 | PASS (21 sources) |
| 6 | Astrophysics | Solar corona reconnection | d=3 | PASS (framework-mapped) |
| 7 | Biology | Xenobot Ca2+ | d=3 | PASS (framework-mapped) |
| 8 | Nuclear | Alpha-decay (212Po) | d=3 | PASS (framework-mapped) |

**Domains 6-8 are framework-mapped** (Category B) -- the barrier was computed using the framework's own coordinates. These are weaker evidence than Category A (direct ln(E/kT) measurements).

**The core test:** For a system with effective dimensionality d, does the dimensionless barrier = ln(E_coupling / (k_B * T*)) equal d x pi/sqrt(2)?

For d=1: E/(kT) = exp(2.221) = 9.22
For d=2: E/(kT) = exp(4.443) = 85.1
For d=3: E/(kT) = exp(6.664) = 786

**Selection criterion:** The universality holds only for STRONG-COUPLING activated transitions where the coupling energy E and the transition temperature T* are set by different physics (i.e., E is not just proportional to kT*). BCS weak-coupling systems (2Delta/kTc = 3.53) explicitly FAIL.

---

## TIER 1: High-Confidence Candidates (Published Barrier Heights, Direct Test)

These datasets have PUBLISHED coupling energies E and transition temperatures T* from which ln(E/kT) can be directly computed and compared to d x pi/sqrt(2). No framework machinery needed.

---

### 1. SEISMOLOGY -- Gutenberg-Richter Magnitude Barriers

**What the barrier maps to:** The Gutenberg-Richter b-value controls the magnitude-frequency distribution: log10(N) = a - b*M. The "barrier" is the maximum magnitude excess above GR expectation in a spatial-temporal bin: barrier = M_max - (a/b). This measures how far the largest event exceeds the statistically expected cutoff.

**Why this is NOT a direct d x pi/sqrt(2) test:** Seismology does not have a clean E_coupling and T* separation. The barrier is a statistical property of the magnitude distribution, not a dimensionless ratio ln(E/kT). HP184 tested barrier GROWTH (beta > 0, R^2=0.94, 5/5 KC PASS), but this does not test the absolute value against pi/sqrt(2).

**Dataset:** USGS ANSS ComCat earthquake catalog
- Download: https://earthquake.usgs.gov/fdsnws/event/1/ (FDSN API, CSV format)
- Also: https://earthquake.usgs.gov/earthquakes/search/ (web interface)
- N = 339,669 events (M >= 4.0, 2000-2024, global) in HP184
- Freely available, no registration required

**Key papers:**
- Gutenberg & Richter, Seismicity of the Earth (1949)
- Bak et al., "Unified scaling law for earthquakes," PRL 88, 178501 (2002)

**d (degrees of freedom):** Unclear. Fault rupture is arguably d=2 (fault plane), but GR statistics span the full 3D stress field. This ambiguity makes it a WEAK test for the absolute barrier = d x pi/sqrt(2).

**Published barrier height:** Not in the form ln(E/kT). The GR b-value ~ 1.0 is the relevant parameter, but it doesn't map cleanly to the universal ratio.

**Verdict: BARRIER GROWTH confirmed (HP184). Absolute d x pi/sqrt(2) test NOT FEASIBLE without significant interpretation. Use for supporting evidence only.**

---

### 2. SPIN ICE -- Magnetic Monopole Activation Barriers

**What the barrier maps to:** In spin ice materials (Dy2Ti2O7, Ho2Ti2O7), magnetic excitations are emergent magnetic monopoles. The activation barrier for monopole creation/motion is directly measured via AC susceptibility and neutron scattering as Arrhenius activation: tau = tau_0 * exp(Delta/kT). The dimensionless barrier is Delta/kT_freeze.

**Why this is a good test:** The coupling energy (spin-spin exchange Jeff or monopole creation energy Ef) and the freezing temperature T_freeze are independently measured. The system is quasi-1D to 3D depending on the excitation (single spin flip = d=1, monopole pair creation = d=3 in the pyrochlore lattice).

**Dataset:** Published values from AC susceptibility and neutron scattering:

| Material | Ef (K) | T_freeze (K) | Ef/kT_f | ln(Ef/kT_f) | d | Predicted | Source |
|----------|--------|---------------|---------|-------------|---|-----------|--------|
| Dy2Ti2O7 | 4.35 K (free monopole) | 0.5 K | 8.7 | 2.16 | 1 | 2.22 | Castelnovo et al., Nature 451, 42 (2008) |
| Ho2Ti2O7 | 5.7 K (free monopole) | 0.6 K | 9.5 | 2.25 | 1 | 2.22 | Bramwell et al., Nature 461, 956 (2009) |
| Dy2Ti2O7 | 6.6 K (Arrhenius fit) | 0.65 K | 10.15 | 2.32 | 1 | 2.22 | Snyder et al., PRB 69, 064414 (2004) |
| Ho2Ti2O7 | 15.8 K (full barrier) | ~1.5 K | 10.5 | 2.35 | 1 | 2.22 | Ehlers et al., JPCM 15, L9 (2003) |

**The monopole creation energy / kT_freeze ratios cluster around 8.7-10.5, giving ln(E/kT) in the range 2.16-2.35.** This straddles pi/sqrt(2) = 2.221.

**Data availability:** Published in the cited papers. No raw data download needed -- the barrier heights are the published headline numbers.

**Sample size:** 4 materials x multiple measurements = ~10-15 data points depending on which temperature scale is used.

**Verdict: STRONG CANDIDATE. Published barrier heights. d=1 for single spin flips, d=3 for monopole pair creation. The E/kT ratios are in the right ballpark. NEW DOMAIN: spin ice / frustrated magnetism.**

---

### 3. SINGLE-MOLECULE MAGNETS -- Quantum Tunneling Barriers

**What the barrier maps to:** Single-molecule magnets (SMMs) like Mn12-acetate and Fe8 have a double-well anisotropy barrier U_eff = |D|*S^2 (axial anisotropy D, total spin S). Below a blocking temperature T_B, thermal relaxation over the barrier follows Arrhenius: tau = tau_0 * exp(U_eff / kT_B).

**Why this is a good test:** The anisotropy barrier U_eff is measured directly from AC susceptibility (Arrhenius plots). The blocking temperature T_B is independently measured from ZFC/FC magnetization splitting. These are parametrically independent.

**Dataset:** Published values:

| Material | U_eff/k_B (K) | T_B (K) | U_eff/kT_B | ln(U/kT) | d | Predicted | Source |
|----------|----------------|---------|------------|----------|---|-----------|--------|
| Mn12-acetate | 67 K | 3.5 K | 19.1 | 2.95 | 1 | 2.22 | Sessoli et al., JACS 115, 1804 (1993) |
| Fe8 | 25 K | 1.0 K | 25.0 | 3.22 | 1 | 2.22 | Sangregorio et al., PRL 78, 4645 (1997) |
| [Mn6] | 86 K | 4.5 K | 19.1 | 2.95 | 1 | 2.22 | Milios et al., JACS 129, 12505 (2007) |

**Problem:** The U_eff/kT_B ratios (~19-25) give ln values of 2.9-3.2, which are 30-45% above pi/sqrt(2) = 2.22. These are ABOVE the universal ratio. SMMs are in the "very strong coupling" regime where U_eff >> kT_B (by construction -- that is what makes them interesting).

**Verdict: LIKELY FAIL. The barriers are too high. SMMs are designed to maximize U_eff/kT_B, pushing them well above the universal ratio. Include as a NEGATIVE control.**

---

### 4. MAGNETIC NANOPARTICLES -- Neel-Brown Reversal Barriers

**What the barrier maps to:** For a single-domain magnetic nanoparticle, the barrier to magnetization reversal is KuV (anisotropy constant Ku times volume V). The blocking temperature T_B satisfies KuV/(kT_B) = ln(tau_m/tau_0) ~ 25 (for typical measurement times tau_m ~ 100s, tau_0 ~ 10^-9 s).

**Why this is interesting but problematic:** The dimensionless ratio KuV/kT_B ~ 25 is set by the measurement timescale, not by intrinsic physics. Different measurement techniques (SQUID, Mossbauer, neutron) give different T_B for the same nanoparticle, changing the ratio. This is NOT an intrinsic coupling/temperature ratio.

**Dataset:** Wernsdorfer et al., PRL 78, 1791 (1997) -- single BaFeO nanoparticle. Jamet et al., PRL 86, 4676 (2001) -- single Co cluster. Numerous published values in review by Batlle & Labarta, JPCM 14, R15 (2002).

**Already in grand barrier table:** Fe nanoparticle (d=2, 5nm) and Co nanoparticle (d=2, 3nm) from HP-EM-04.

**Verdict: ALREADY PARTIALLY INCLUDED. The ratio KuV/kT_B ~ 25 is measurement-dependent, not intrinsic. NOT a clean test. Existing entries in the d=2 EM domain are sufficient.**

---

### 5. NEUROSCIENCE -- Neural Avalanche Criticality

**What the barrier maps to:** Neural avalanches at criticality (branching ratio sigma = 1) exhibit power-law distributions with exponent alpha = -3/2 for sizes. The "barrier" would be the energy barrier between quiescent and avalanche states, or equivalently, the synaptic coupling strength E_syn divided by the neural noise temperature kT_neural.

**Why this is problematic:** There is no clean E_coupling and T* in neural systems. The branching ratio sigma = 1 is a dimensionless number, not a barrier height. The power-law exponent 3/2 is a CRITICAL EXPONENT, not a Kramers barrier. These are fundamentally different universality classes.

**Dataset:** Beggs & Plenz, J Neurosci 23, 11167 (2003) -- original MEA recording, 60-electrode array, rat cortex slices. Data not publicly archived. Allen Brain Observatory (http://observatory.brain-map.org/visualcoding/) has calcium imaging data for ~60,000 cells, freely available via AllenSDK, but these are visual response data, not spontaneous avalanche recordings.

**Published "barrier height":** None in the form ln(E/kT). The relevant parameters are:
- Power-law exponent alpha = -3/2 (Beggs & Plenz 2003)
- Branching ratio sigma = 1.0 +/- 0.1
- These are not barriers

**Verdict: NOT FEASIBLE for the d x pi/sqrt(2) test. Neural criticality is a different universality class (mean-field branching process, not Kramers barrier crossing). The exponent 3/2 is interesting but tests a different prediction.**

---

### 6. EPIDEMIOLOGY -- SIS Stochastic Extinction Barrier

**What the barrier maps to:** For the stochastic SIS model with population N and basic reproduction number R0 > 1, the barrier to extinction from the endemic state is V = N * (R0 - 1 - ln(R0)) (Doering et al. 2005). The dimensionless barrier is V/(something), but there is no natural "kT" in epidemiology.

**Why this is problematic:** The Doering barrier is EXACT for the SIS model and grows linearly with N. This is a well-known result, not a test of universality. The barrier is not a ratio E/kT -- it is an extensive quantity proportional to population size.

**Dataset:** HP188 tested this with Gillespie simulations (5/5 KC PASS for barrier growth). Published theoretical result, no external dataset needed.

**Key paper:** Doering, Sargsyan, Sander, "Extinction times for birth-death processes: exact results, continuum asymptotics, and the failure of the Fokker-Planck approximation," SIAM J Multiscale Model Simul 3, 283 (2005).

**Published barrier height:** V = N * (R0 - 1 - ln(R0)). For R0 = 2, N = 100: V = 30.7. This is not in the form ln(E/kT).

**Verdict: NOT FEASIBLE for d x pi/sqrt(2). Barrier growth confirmed (HP188) but the absolute barrier is N-dependent and not a dimensionless ratio comparable to pi/sqrt(2). Different mathematical structure.**

---

### 7. MATERIALS SCIENCE -- BKT Transition in 2D Superfluid Helium

**What the barrier maps to:** The BKT transition occurs at T_BKT where vortex-antivortex pairs unbind. The barrier is the vortex core energy E_c. The dimensionless ratio is E_c / (kT_BKT) = pi^2 / 2 (from BKT theory, this is the Nelson-Kosterlitz universal jump condition).

**Why this is EXTREMELY interesting:** BKT theory predicts E_c/kT_BKT = pi^2/2 = 4.935. For d=2, the framework predicts barrier = 2 x pi/sqrt(2) = 4.443. These are DIFFERENT (pi^2/2 vs 2*pi/sqrt(2)), so this is a genuine test with a PUBLISHED theoretical prediction to compare against.

**Dataset:**
- Superfluid He-4 films: Bishop & Reppy, PRL 40, 1727 (1978). T_BKT measured from superfluid density jump.
- 2D Pb films: Zhang et al., Solid State Commun 165, 59 (2013). Atomically flat 2D Pb superconducting films.
- Cold atoms: Hadzibabic et al., Nature 441, 1118 (2006). 2D BEC observation of BKT.

**Published barrier height:** The universal jump condition gives rho_s(T_BKT) = (2m/pi*hbar^2) * k_B * T_BKT. The vortex core energy is E_c = pi * J where J is the superfluid stiffness. At T_BKT: E_c/(kT_BKT) = pi (in the simplest renormalization), though the bare value is pi^2/2 and renormalization brings it to pi at the transition. Published estimates: E_c/kT_BKT = 2.5 to 5.0 depending on the system and measurement method.

**d = 2.** Prediction: barrier = 4.443.

**Sample size:** ~10-20 published BKT measurements across different 2D systems.

**Verdict: STRONG CANDIDATE but the published barrier values are AMBIGUOUS (E_c/kT varies from 2.5 to 5.0 depending on renormalization conventions). If we take the bare coupling (J, not E_c), the ratio may be cleaner. Requires careful extraction from published I-V and rho_s data. NEW DOMAIN: 2D superfluids / BKT physics.**

---

### 8. ECONOMICS / FINANCE -- Kramers Escape from Market Regimes

**What the barrier maps to:** In stochastic volatility models, the market can be in a low-volatility (normal) or high-volatility (crisis) regime. The transition between regimes can be modeled as Kramers escape over a barrier in a double-well potential. The barrier height Delta_V is estimated from the mean residence time in each regime: tau ~ exp(Delta_V / sigma^2) where sigma is the noise intensity.

**Why this is problematic:** There is no universal E_coupling and T* in financial markets. The barrier height depends on the model (GARCH, regime-switching, LPPLS), and different models give different barriers. There is no consensus published barrier height.

**Dataset:** S&P 500 daily returns (freely available from Yahoo Finance, FRED). VIX index for volatility regimes. LPPLS model parameters: beta ~ 0.35, omega ~ 7-13 (Sornette et al.).

**Published barrier height:** Not in a form comparable to ln(E/kT). The LPPLS power-law exponent beta = 0.35 is the closest analog, but this is a critical exponent, not a dimensionless barrier.

**Verdict: NOT FEASIBLE for d x pi/sqrt(2). No published barrier heights in the required form. Use for barrier GROWTH tests only (already done in market microstructure HP145).**

---

### 9. ASTROPHYSICS -- Chandrasekhar Mass / Type Ia Supernova Ignition

**What the barrier maps to:** A white dwarf accreting mass approaches the Chandrasekhar limit (1.44 Msun). Carbon ignition occurs when the central temperature reaches T_ign ~ 6 x 10^8 K. The nuclear barrier is the Gamow peak energy E_G = (alpha * Z1 * Z2)^2 * m_r * c^2 / 2 for carbon-carbon fusion.

**Why this is interesting:** The Gamow barrier for C-C fusion is well-studied nuclear physics. E_G(C-C) ~ 6.3 MeV. At T = 6 x 10^8 K: kT = 51.7 keV. The Gamow peak energy E_peak = (E_G * (kT)^2)^(1/3) = 2.4 MeV. The dimensionless barrier is E_peak/kT ~ 46, giving ln(E/kT) ~ 3.8.

**Problem:** What is d? Carbon-carbon fusion in a degenerate core involves 3D nuclear motion plus electronic screening. If d=2 (the center-of-mass collision is 1D, but there are angular momentum channels), the predicted barrier is 4.443 and the Gamow-based estimate gives ~3.8, which is 14% low. If d=1, predicted is 2.22 and actual is 3.8 -- too high. This does NOT cleanly match.

**Dataset:** Published Gamow energies from nuclear physics tables (NNDC). Ignition conditions from Nomoto et al., ApJ 286, 644 (1984). White dwarf central conditions from Woosley et al., ApJ 607, 921 (2004).

**Verdict: WEAK CANDIDATE. The Gamow barrier is well-published but the mapping to d x pi/sqrt(2) requires choosing d, and no choice gives a clean match. More natural as a nuclear physics test (already done as HP143).**

---

### 10. ECOLOGY -- Scheffer Resilience Barriers

**What the barrier maps to:** Ecosystem regime shifts (e.g., lake eutrophication: clear -> turbid) can be modeled as transitions in a double-well potential. The barrier height is the "resilience" of the current state, measurable from critical slowing down (increased variance and autocorrelation before the transition).

**Why this is problematic:** Ecosystem barriers are NOT published as dimensionless numbers. They are system-specific, measured in the units of the state variable (e.g., phosphorus concentration), and require fitting a potential function to time series data. There is no universal E/kT ratio.

**Dataset:** Resilience Alliance Thresholds Database (https://www.resalliance.org/thresholds-db) -- over 100 documented ecological thresholds. Published examples:
- Lake Mendota eutrophication (Carpenter et al., Ecology 92, 2011)
- Sahel desertification (Scheffer et al., Nature 461, 53, 2009)
- Coral reef collapse (Hughes et al., Science 301, 929, 2003)

**Published barrier height:** NOT in the form ln(E/kT). Barriers are measured as "resilience indicators" (variance, return rate), not as dimensionless ratios.

**Verdict: NOT FEASIBLE for d x pi/sqrt(2). Ecological barriers are not dimensionless ratios. Use the Resilience Alliance database for barrier GROWTH tests only (HP190 approach).**

---

### 11. QUASI-1D ORGANIC CONDUCTORS -- Peierls/CDW Transitions

**What the barrier maps to:** Quasi-1D organic conductors (Bechgaard salts, TMTSF, TTF-TCNQ) undergo CDW or spin-density-wave (SDW) transitions. The coupling energy is the gap 2Delta (from optical conductivity or tunneling). The transition temperature T_CDW or T_SDW is independently measured from resistivity.

**Why this is a good test:** Same physics as NbSe3 (already in the table), but different materials provide independent data points. The ratio 2Delta/(kT_CDW) varies from system to system. Strong-coupling CDW systems should have 2Delta/kT >> 3.53 (the BCS weak-coupling value).

**Dataset:**

| Material | 2Delta (meV) | T_CDW (K) | 2Delta/kT | ln | d | Source |
|----------|-------------|-----------|-----------|----|----|--------|
| (TMTSF)2PF6 (SDW) | 7.0 | 12.0 | 6.77 | 1.91 | 1 | Schwartz et al., PRB 58, 1455 (1998) |
| TTF-TCNQ (CDW) | 70 | 54 | 15.0 | 2.71 | 1 | Pouget, Crystals 2, 466 (2012) |
| K0.3MoO3 (blue bronze) | 70-100 | 183 | 4.4-6.3 | 1.49-1.84 | 1 | Travaglini & Wachter, PRB 30, 1971 (1984) |

**Problem:** The SDW/CDW systems span a wide range of coupling strengths. Only the strong-coupling ones (2Delta/kT ~ 9.2, ln ~ 2.22) would match the universal ratio. The weak-coupling ones (2Delta/kT < 5) will be below. This is expected from the selection criterion, but finding systems where 2Delta/kT ~ 9.2 "accidentally" rather than by construction is the key.

**Verdict: MODERATE CANDIDATE. Extends the CDW domain. TTF-TCNQ is too strong (ln=2.71), blue bronze is too weak (ln~1.7). Need to survey more materials to find ones near 2Delta/kT ~ 9.2. The range confirms the selection criterion but does not independently test the ratio. SAME DOMAIN as NbSe3.**

---

### 12. HEAVY-FERMION QUANTUM CRITICAL POINTS

**What the barrier maps to:** In heavy-fermion compounds near a quantum critical point (QCP), the characteristic energy scale is the Kondo temperature T_K (or the hybridization gap Delta_hyb). The physical transition temperature T_N (Neel) or T_c (superconducting) is a separate scale. The ratio Delta_hyb / (k_B * T_N) is a dimensionless barrier-like quantity.

**Why this is interesting:** Heavy-fermion systems have a natural separation between the coupling scale (T_K ~ 10-100 K) and the ordering temperature (T_N ~ 1-10 K), giving large ratios.

**Dataset:**

| Material | T_K (K) | T_N or T_c (K) | T_K/T_order | ln(T_K/T_order) | d | Source |
|----------|---------|----------------|-------------|-----------------|---|--------|
| CeRhIn5 | 50 | 3.8 (T_N) | 13.2 | 2.58 | 3 | Hegger et al., PRL 84, 4986 (2000) |
| CeCoIn5 | 45 | 2.3 (T_c) | 19.6 | 2.97 | 3 | Petrovic et al., JPCM 13, L337 (2001) |
| YbRh2Si2 | 25 | 0.07 (T_N) | 357 | 5.88 | 3 | Trovarelli et al., PRL 85, 626 (2000) |
| CeCu6 | 7 | 0 (NFL) | -- | -- | 3 | Lohneysen et al., PRL 72, 3262 (1994) |

**Problem:** The d=3 prediction is barrier = 6.664. The heavy-fermion ln ratios (2.58-5.88) are far below this. The issue is that T_K and T_N are not the right coupling/transition pair for the barrier test -- T_K is a crossover scale, not a coupling energy in the Kramers sense. And the systems are 3D, not 1D.

**Verdict: NOT FEASIBLE. The energy scales do not map to the barrier formula. T_K/T_N is not a Kramers barrier. Different physics.**

---

## TIER 2: Moderate-Confidence Candidates (Barrier Growth, Not Absolute Test)

These domains can demonstrate barrier GROWTH (beta > 0) but cannot cleanly test barrier = d x pi/sqrt(2).

---

### 13. PLASMA PHYSICS -- Tokamak L-H Transition Barrier

**Status:** HP186 tested, 4/5 KC PASS (failed KC-4: beta deviation from IPB98).
**What was tested:** Stored energy W grows with heating power P (barrier growth).
**Absolute test feasibility:** The L-H transition power threshold P_LH is well-published (Martin et al., JPFR 2, S1005, 2008). But the dimensionless barrier is P_LH / (n_e * B * S) which has no clean E/kT interpretation. BARRIER GROWTH only.

### 14. DEEP LEARNING -- Loss Landscape Barriers

**Status:** HP185 tested, 5/5 KC PASS. beta = 0.40, R^2 = 0.97.
**What was tested:** Barrier between minima grows with network capacity.
**Absolute test feasibility:** Self-generated data, not externally published. The barrier height depends on architecture, dataset, and training details. No universal ratio. BARRIER GROWTH only.

### 15. POPULATION GENETICS -- Kimura Fixation Barrier

**Status:** HP187 tested, 4/5 KC PASS. Analytical barrier = 2*N_e*s*(1-p0) grows linearly with N_e*s.
**Absolute test feasibility:** The barrier is proportional to N_e*s, which is an extensive quantity. There is no natural dimensionless ratio to compare to pi/sqrt(2). The barrier is DEFINED to grow linearly. BARRIER GROWTH only (trivial).

---

## TIER 3: New Candidate Domains for Absolute d x pi/sqrt(2) Test

These are the most promising unexplored domains where a direct test might be possible.

---

### A. SPIN ICE (Priority: HIGH)

**Detailed above (#2).** Summary: Dy2Ti2O7 and Ho2Ti2O7 monopole energies give ln(E/kT_freeze) ~ 2.16-2.35, straddling pi/sqrt(2) = 2.22. Published in Nature 451 (2008) and Nature 461 (2009). 4+ data points. **NEW DOMAIN.**

**Action items:**
1. Extract Ef and T_freeze from Castelnovo et al. (2008), Bramwell et al. (2009), Snyder et al. (2004), Ehlers et al. (2003)
2. Determine d: single spin flip = d=1, monopole pair = d=3
3. Check if ln(Ef/kT_freeze) = d x pi/sqrt(2) for the appropriate d
4. If d=1 and ln ~ 2.2, this is a PASS with zero free parameters

**Risk:** The "temperature" is ambiguous -- T_freeze vs T at which AC susceptibility peaks vs onset temperature. Different choices give different ratios.

---

### B. SUPERFLUID / BKT TRANSITIONS (Priority: HIGH)

**Detailed above (#7).** Summary: Vortex core energy E_c / kT_BKT measured in 2D superfluid He-4 films and 2D superconducting films. Published values range from 2.5 to 5.0. For d=2, prediction is 4.443.

**Most promising specific dataset:** 2D NbN superconducting films, where Beasley et al. (PRL 42, 1165, 1979) and subsequent work measure the BKT jump condition precisely.

**Action items:**
1. Extract vortex core energy E_c from published I-V and superfluid density data
2. Compare E_c/(kT_BKT) to 2 x pi/sqrt(2) = 4.443
3. Key distinction: bare vs renormalized E_c. Need the BARE coupling.

**Risk:** Renormalization effects make the "bare" coupling ambiguous. Need to be very precise about which published number to use.

---

### C. COLD ATOM SYSTEMS -- Feshbach Resonance Barriers (Priority: MEDIUM)

**What the barrier maps to:** Near a Feshbach resonance, the scattering length a diverges. The binding energy of the Feshbach molecule is E_b = hbar^2/(m*a^2). The relevant temperature is the Fermi temperature T_F or the BEC critical temperature T_c. The ratio E_b/(kT_F) is a dimensionless barrier.

**Why this is interesting:** Ultra-cold atom experiments have exquisite control over E_b (via magnetic field tuning) and T (via evaporative cooling). The barrier is tunable.

**Dataset:** Published E_b and T data from numerous cold atom groups:
- Regal et al., Nature 424, 47 (2003) -- 40K Feshbach molecules
- Chin et al., Rev Mod Phys 82, 1225 (2010) -- comprehensive review of Feshbach resonances

**d:** The BEC-BCS crossover occurs in 3D. d=3 gives predicted barrier = 6.664.

**Published barrier:** E_b at unitarity (a -> infinity) is zero. The interesting regime is away from unitarity where E_b/kT_F ~ 1-100. This is tunable, not a fixed universal ratio.

**Verdict: NOT a clean test because the ratio is experimentally tunable, not a fixed property. The test would degenerate into "can we tune E_b/kT to hit 6.664?" which proves nothing.**

---

### D. SUPERCOOLING / NUCLEATION -- Classical Nucleation Theory (Priority: MEDIUM)

**What the barrier maps to:** Classical nucleation theory (CNT) gives the barrier to forming a critical nucleus: Delta_G* = (16*pi*gamma^3) / (3*Delta_g^2), where gamma is the surface energy and Delta_g is the bulk free energy difference. The dimensionless barrier is Delta_G* / (kT).

**Why this is interesting:** Delta_G*/kT is a published, measured quantity for many systems (water supercooling, crystal nucleation, protein crystallization).

**Dataset:**
- Water supercooling: Delta_G*/kT ~ 40-80 at different supercoolings (Hagen et al., JCP 71, 2316, 1981)
- Ice nucleation: Murray et al., Chem Soc Rev 41, 6519 (2012) -- comprehensive review
- Protein crystallization: Vekilov, Cryst Growth Des 10, 5007 (2010)

**d:** Nucleation is 3D. d=3 gives predicted barrier = 6.664.

**Problem:** Published Delta_G*/kT values (40-80) are WAY above the predicted 6.664. CNT barriers are extensive (proportional to nucleus surface area), not the same universality class as the intensive barriers in the framework.

**Verdict: FAIL. Nucleation barriers are extensive and orders of magnitude larger than d x pi/sqrt(2). Different physics.**

---

### E. JOSEPHSON JUNCTION ARRAYS -- 2D Phase Ordering (Priority: MEDIUM-HIGH)

**What the barrier maps to:** In 2D Josephson junction arrays (JJAs), the BKT transition occurs between a superconducting and resistive state. The coupling energy E_J (Josephson energy) and the transition temperature T_BKT are both independently measurable.

**Dataset:**
- Resnick et al., PRL 47, 1542 (1981) -- original JJA BKT observation
- Newrock et al., Adv Phys 49, 455 (2000) -- comprehensive review

**Published values:** E_J/(kT_BKT) ~ 1.0-1.5 for strongly coupled arrays. This gives ln ~ 0 to 0.4, which is far below pi/sqrt(2).

**Problem:** In 2D JJAs, E_J ~ kT_BKT by construction (the BKT temperature is set by the Josephson coupling). There is no parametric separation between E and T. This is the SAME reason BCS weak-coupling systems fail.

**Verdict: FAIL. No parametric separation between E_J and kT_BKT.**

---

### F. GEOSCIENCE -- Volcanic Eruption Recurrence (Priority: LOW)

**What the barrier maps to:** Magma chamber pressurization follows a Kramers-like escape process. The "barrier" is the tensile strength of the rock plus the overpressure needed for dike propagation. The "temperature" is the magma injection rate fluctuations.

**Problem:** No clean E/kT decomposition. Eruption intervals are controlled by magma supply rates, tectonic stress, and conduit geometry -- none of which reduce to a simple barrier/noise ratio.

**Verdict: NOT FEASIBLE for d x pi/sqrt(2). Too many uncontrolled variables.**

---

## SUMMARY: Recommended Priority List

### Domains that can test barrier = d x pi/sqrt(2) directly (NEW domains)

| Priority | Domain | d | Predicted barrier | Published barrier | Feasibility | New domain? |
|----------|--------|---|-------------------|-------------------|-------------|-------------|
| **1** | **Spin ice (Dy2Ti2O7, Ho2Ti2O7)** | 1 | 2.22 | 2.16-2.35 | HIGH | YES |
| **2** | **BKT in 2D films** | 2 | 4.44 | 2.5-5.0 (ambiguous) | MEDIUM | YES |
| **3** | Organic CDW conductors | 1 | 2.22 | 1.5-2.7 (range) | MEDIUM | No (extends CDW) |

### Domains that confirmed barrier GROWTH but cannot test absolute value

| Domain | HP experiment | KC result | Beta | New domain? |
|--------|-------------|-----------|------|-------------|
| Seismology | HP184 | 5/5 PASS | 0.050 | YES |
| Neural loss landscape | HP185 | 5/5 PASS | 0.398 | YES |
| Plasma confinement | HP186 | 4/5 PASS | 1.627 | YES |
| Population genetics | HP187 | 4/5 PASS | 1.000 | YES |
| Epidemiology (SIS) | HP188 | simulated | N-linear | YES (model) |
| Materials (2D Ising) | HP189 | simulated | ~1.0 | YES (model) |
| Ecology (logistic) | HP190 | simulated | ~1.0 | YES (model) |

### Domains that FAIL the d x pi/sqrt(2) test

| Domain | Why it fails |
|--------|--------------|
| Single-molecule magnets | Barriers too high (ln ~ 3.0, predicted 2.22) |
| Nucleation (CNT) | Barriers extensive, ~40-80 vs predicted 6.66 |
| Josephson junction arrays | No E/T separation (E_J ~ kT_BKT) |
| Heavy-fermion QCPs | T_K/T_N is not a Kramers barrier |
| Financial markets | No published dimensionless barrier |
| Neural avalanches | Critical exponents, not barriers |
| Ecosystem collapse | Barriers not dimensionless |
| Cold atoms (Feshbach) | Barrier is experimentally tunable |
| Volcanology | Too many uncontrolled variables |

---

## ACTION PLAN

### Immediate (can be done with published data, no new experiments)

1. **Spin ice extraction.** Pull Ef and T_freeze values from:
   - Castelnovo, Moessner, Sondhi, Nature 451, 42 (2008) -- Dy2Ti2O7 monopole energy
   - Bramwell et al., Nature 461, 956 (2009) -- Ho2Ti2O7 monopole dynamics
   - Snyder et al., PRB 69, 064414 (2004) -- Dy2Ti2O7 AC susceptibility
   - Ehlers et al., JPCM 15, L9 (2003) -- Ho2Ti2O7 neutron scattering
   - Jaubert & Holdsworth, Nat Phys 5, 258 (2009) -- monopole Coulomb liquid
   - Compute ln(Ef/kT_freeze) for each, compare to pi/sqrt(2)

2. **BKT extraction.** Pull vortex core energy from:
   - Bishop & Reppy, PRL 40, 1727 (1978) -- He-4 films
   - Beasley, Mooij, Orlando, PRL 42, 1165 (1979) -- NbN films
   - Zhang et al., Solid State Commun 165, 59 (2013) -- 2D Pb films
   - Hadzibabic et al., Nature 441, 1118 (2006) -- 2D BEC
   - Compute E_c/(kT_BKT) for each, compare to 2 x pi/sqrt(2) = 4.443

3. **Organic CDW survey.** Compile 2Delta and T_CDW from:
   - Pouget, Crystals 2, 466 (2012) -- review of organic CDW systems
   - Jerome, Chem Rev 104, 5565 (2004) -- Bechgaard salt review
   - Find materials with 2Delta/kT near 9.2 (the d=1 target)

### Medium-term (requires computation or data access)

4. **USGS seismology.** Already done (HP184). Consider extending to fault-specific analysis where d might be identifiable (subduction zone = d=2 slab geometry?).

5. **Extend condensed matter d=2.** Look for other 2D phase transitions with published E/kT ratios:
   - 2D XY magnets (BaNi2V2O8, Bamax et al.)
   - 2D electron gas (Wigner crystal melting)
   - Graphene-based 2D systems

---

## KEY CONSTRAINT

The honest assessment: **only spin ice (domain #9) is likely to provide a clean new domain where barrier = d x pi/sqrt(2) can be tested with zero free parameters against published values.**

BKT transitions are promising but the renormalization ambiguity in the vortex core energy makes it a softer test.

Most other domains (seismology, neuroscience, epidemiology, ecology, economics) have barrier GROWTH but not barrier heights in the form of dimensionless ln(E/kT) ratios. They test a different (weaker) prediction.

The path to 15+ domains for the d x pi/sqrt(2) absolute test likely requires:
- Mining more quasi-1D magnetic systems (same domain, more data points)
- Mining more CDW materials (same domain, more data points)
- Spin ice (1 genuinely new domain)
- BKT / 2D superfluid (1 genuinely new domain, if renormalization can be controlled)
- More atmospheric phenomena (same domain, more data points)

Going from 8 to 15 INDEPENDENT DOMAINS for the absolute barrier test may not be achievable with currently published data. The honest count of domains where barrier = d x pi/sqrt(2) is testable may top out at 10-11 (adding spin ice + BKT to the current 8).

For barrier GROWTH (beta > 0), 15+ domains is already achieved when combining HP184-HP190 with the existing 8.
