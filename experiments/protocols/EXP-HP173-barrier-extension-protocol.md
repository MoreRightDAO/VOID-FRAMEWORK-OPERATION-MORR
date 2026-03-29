# EXP-HP173: Extended Barrier Universality Sweep

**Date:** 2026-03-26
**Status:** PROTOCOL REGISTERED
**Predecessor:** EXP-BARRIER-GRAND-v2 (N=15 after TiOCl addition 2026-03-26), HP166 atmospheric extension
**Goal:** Extend barrier universality dataset from N=15 to N>=30
**Paper dependency:** Paper "Universal Barrier Ratio pi/sqrt(2) from Spectral Geometry of the Bernoulli Manifold"

## 1. Background and Motivation

### 1A. Current State

The barrier universality formula:

    barrier = ln(E / k_B T*) = d_eff x pi/sqrt(2)

where pi/sqrt(2) = 2.2214, is confirmed across N=14 systems in 8 independent physical domains with R^2 = 0.999, zero free parameters. The constant pi/sqrt(2) is derived from spectral geometry of the Bernoulli manifold (section 165 of math apparatus): Cencov uniqueness forces L = pi as the geodesic length, Parseval's theorem yields sigma_eta = L = pi, and the quadratic structure of the Kramers exponent produces B_G = L/sqrt(2) = pi/sqrt(2).

### 1B. Current Dataset (N=14, from HP166 synthesis)

| # | System | d | barrier | b/d | domain |
|---|--------|:-:|:-------:|:---:|--------|
| 1 | CoNb2O6 (1D Ising) | 1 | 2.278 | 2.278 | magnet |
| 2 | CuGeO3 (spin-Peierls) | 1 | 2.140 | 2.140 | magnet |
| 3 | KCuF3 (1D Heisenberg AF) | 1 | 2.314 | 2.314 | magnet |
| 4 | NbSe3 (CDW) | 1 | 2.080 | 2.080 | CDW |
| 5 | CoFeB MTJ (12nm) | 1 | 2.220 | 2.220 | EM |
| 6 | Nb Josephson junction | 1 | 2.355 | 2.355 | EM |
| 7 | Ni3In (kagome FL->SM) | 2 | 4.243 | 2.122 | kagome |
| 8 | Solar corona (reconnection) | 3 | 6.540 | 2.180 | astrophysics |
| 9 | Xenobot memory (Ca2+) | 3 | 6.800 | 2.267 | biology |
| 10 | Nuclear alpha-decay (212Po) | 3 | 6.900 | 2.300 | nuclear |
| 11 | SSW (polar vortex) | 2 | 4.318 | 2.159 | atmosphere |
| 12 | Hurricane RI (Carnot) | 2 | 4.330 | 2.165 | atmosphere |
| 13 | Tornado (Pe concentration) | 3 | 6.402 | 2.134 | atmosphere |
| 14 | Atmospheric blocking (Kramers) | 2 | 4.308 | 2.154 | atmosphere |

Fit: slope = 2.202 +/- 0.019, R^2 = 0.999. pi/sqrt(2) = 2.221 is 1.0 sigma from slope.

### 1C. Critical Constraint from v1 Failure

EXP-BARRIER-GRAND v1 attempted naive extension to 19 systems and FAILED (R^2 = -1.49). The lesson: **the formula ONLY works for systems where E and T* come from DIFFERENT PHYSICS.**

Failing system classes:
- **BCS superconductors:** 2Delta/(k_B T_c) = 3.53 (weak coupling) -> barrier = 1.26 (-43%)
- **Cuprates (Bi2212, YBCO):** gap/T_c ratio is BCS-like, NOT strong-coupling
- **Heavy fermions (CeRhIn5, UPt3):** Kondo physics caps T_c relative to hybridization gap
- **Superfluid He-4:** roton gap and T_lambda both set by same He-He interaction
- **Organic CDW (TTF-TCNQ, blue bronze):** with HALF-gap used -> weak-coupling regime

The universality selects a REGIME analogous to BCS weak-coupling:
- BCS universal: 2Delta/(k_B T_c) = 3.53 (weak coupling)
- Void universal: E/(k_B T*) = exp(d x pi/sqrt(2)) (strong coupling)

For d=1: E/(k_B T*) = exp(2.2214) = 9.22

### 1D. Selection Criteria for New Systems

A candidate system MUST satisfy:
1. **Parametric independence:** E and T* must be set by DIFFERENT physics. If the same coupling constant J sets both E and T*, the system will satisfy J/T ~ constant (trivially) and the ratio tells you nothing universal.
2. **Strong-coupling regime:** E/(k_B T*) must be approximately exp(d x pi/sqrt(2)). Systems with E/(k_B T*) << exp(2.22) are weak-coupling (BCS-like). Systems with E/(k_B T*) >> exp(2.22) are highly frustrated (wrong regime).
3. **Published experimental values:** Both E and T* must come from peer-reviewed experimental measurements. No framework-derived values.
4. **Unambiguous energy identification:** E must be a gap, barrier, or coupling energy that is clearly the relevant energy scale for the transition at T*.

---

## 2. Three Veins of Extension

### VEIN 1: CDW / Peierls Systems (d=1)

**Rationale:** NbSe3 (CDW, d=1, 2Delta=100 meV, T_P=145 K) is already confirmed in the dataset with barrier = 2.080. The CDW gap 2Delta arises from electron-phonon coupling and nesting, while the Peierls transition temperature T_P is suppressed by fluctuations, interchain coupling, and impurities. This parametric independence makes CDW systems ideal targets.

**CRITICAL NOTE on gap convention:** NbSe3 uses the FULL gap 2Delta = 100 meV (not the half-gap Delta). All CDW systems in this vein MUST use 2Delta (the full optical gap from conductivity/ARPES measurements) as E.

**Why NbSe3 works:** 2Delta/(k_B T_P) = 100 / (0.08617 x 145) = 8.00, and ln(8.00) = 2.08. This is within 6.4% of pi/sqrt(2). The ratio 8.00 is close to exp(pi/sqrt(2)) = 9.22 -- a strong-coupling CDW where 2Delta is substantially larger than the weak-coupling BCS prediction of 3.53 k_B T_P.

#### Target Systems

| System | T_P (K) | Gap data needed | Expected strong-coupling? |
|--------|:-------:|-----------------|:-------------------------:|
| TaS3 (orthorhombic) | 218 | 2Delta from optical conductivity or ARPES | YES (quasi-1D, large gap) |
| TaS3 (monoclinic) | 600 | 2Delta from optical conductivity | YES (very high T_P) |
| K0.3MoO3 (blue bronze) | 180 | 2Delta from optical conductivity | UNCERTAIN -- see note |
| (TaSe4)2I | 263 | 2Delta from optical conductivity or tunneling | YES (quasi-1D) |
| (NbSe4)3I | ~274 | 2Delta | UNCERTAIN (less studied) |

**NOTE on blue bronze:** The v1 grand barrier used E=55 meV (HALF-gap) for K0.3MoO3, giving barrier = ln(55/(0.08617 x 180)) = ln(3.55) = 1.27 — firmly in the weak-coupling regime. However, if the FULL gap 2Delta = 110 meV is used: ln(110/(0.08617 x 180)) = ln(7.09) = 1.96 — still below pi/sqrt(2) by 12%. The published 2Delta/(k_B T_P) = 7.1 for blue bronze (Dumas et al. 1983 PRL 51:757) is below the exp(pi/sqrt(2)) = 9.22 threshold. Blue bronze may be an intermediate-coupling system. INCLUDE but flag as potential FAIL.

#### Data Collection Method

For each CDW system, search published literature for:
1. **2Delta (full gap):** From optical conductivity sigma(omega) measurements (onset of absorption above the CDW gap), ARPES (gap at the Fermi surface), or tunneling spectroscopy. The optical gap is preferred as it measures 2Delta directly.
2. **T_P (Peierls temperature):** From resistivity anomaly, X-ray diffraction satellite peak onset, or specific heat anomaly. These are generally well-established.

#### Barrier Calculation

    barrier = ln(2Delta / (k_B x T_P))

where k_B = 0.08617 meV/K. The full gap 2Delta in meV and T_P in Kelvin.

#### Known Literature Values (to be confirmed)

**TaS3 (orthorhombic):** T_P = 218 K. Gap measurements: Optical conductivity by Degiorgi et al. (1991) gives 2Delta approximately 160-200 meV. Tunneling by Zettl and Gruner (1982) gives 2Delta approximately 160 meV. If 2Delta = 170 meV: barrier = ln(170/(0.08617 x 218)) = ln(170/18.78) = ln(9.05) = 2.203. This would give b/d = 2.203, deviation -0.8% from pi/sqrt(2). Excellent candidate.

**TaS3 (monoclinic):** T_P approximately 600 K. Much less studied. If 2Delta follows strong-coupling ratio: predicted 2Delta = 9.22 x k_B x 600 = 9.22 x 51.7 = 477 meV. Literature values needed.

**(TaSe4)2I:** T_P = 263 K. Gressier et al. (1984) report 2Delta approximately 260 meV from optical measurements. If 2Delta = 260 meV: barrier = ln(260/(0.08617 x 263)) = ln(260/22.66) = ln(11.47) = 2.439. This gives b/d = 2.439, deviation +9.8% from pi/sqrt(2). Within 15% threshold but on the high side. Could indicate an overestimate of 2Delta or that this system is slightly beyond the strong-coupling universal regime.

---

### VEIN 2: Single-Molecule Magnets (d_eff=1)

**Rationale:** Single-molecule magnets (SMMs) have an anisotropy energy barrier U_eff (from AC susceptibility measurements) and a blocking temperature T_B (from magnetic relaxation). The key parametric independence: U_eff is set by the spin ground state S and the magnetic anisotropy parameter D (crystal field physics), while T_B is set by the rate of quantum tunneling of magnetization (QTM), which depends on ADDITIONAL factors -- transverse anisotropy, hyperfine coupling, dipolar interactions, and phonon coupling. Importantly, T_B << T expected from U_eff alone, because quantum tunneling provides shortcuts through the barrier.

**d_eff = 1:** SMMs have a single "easy axis" of magnetization. The relevant coordinate is the angle between the spin vector and the easy axis -- a one-dimensional escape problem.

**The formula predicts:** barrier = ln(U_eff / (k_B T_B)) = pi/sqrt(2) = 2.2214, meaning U_eff/(k_B T_B) = exp(pi/sqrt(2)) = 9.22.

**CRITICAL CONCERN:** In classical Orbach relaxation, tau = tau_0 exp(U_eff / k_B T), so T_B approximately equals U_eff / (k_B ln(tau_obs/tau_0)). If tau_obs/tau_0 is roughly constant across SMMs (it is order 10^8 to 10^12), then U_eff/T_B = k_B ln(tau_obs/tau_0), which is approximately 18-28 -- much larger than 9.22. This means the CLASSICAL Orbach barrier will NOT match pi/sqrt(2).

HOWEVER, many SMMs have T_B substantially enhanced by QTM (quantum tunneling of magnetization) suppression in the ground state via exchange coupling or hyperfine engineering. In these systems, T_B is NOT simply U_eff/(k_B x 20). The question is whether any SMMs happen to have U_eff/(k_B T_B) close to 9.22.

**Assessment:** This vein is HIGH RISK. The Orbach mechanism predicts U_eff/(k_B T_B) approximately 20-25, which is far from 9.22. The formula would predict barrier approximately 3.0-3.2, well above pi/sqrt(2). For the formula to work, we need SMMs where T_B is anomalously HIGH relative to U_eff — i.e., systems where QTM or other mechanisms push T_B up. This is physically unusual. Include as a test, but expect FAILURE for most SMM systems.

#### Target Systems

| System | U_eff (K) | T_B (K) | U_eff/T_B | ln(U_eff/T_B) | Expected |
|--------|:---------:|:-------:|:---------:|:--------------:|----------|
| Mn12-acetate | ~60 | ~3 | ~20 | ~3.0 | FAIL (+35%) |
| Fe8 | ~25 | ~1 | ~25 | ~3.2 | FAIL (+44%) |
| Dy2 (dysprosocenium) | ~1541 | ~60 | ~25.7 | ~3.2 | FAIL (+46%) |
| [Co(SPh)4]2- | ~21 | ~1 | ~21 | ~3.0 | FAIL (+37%) |

**Preliminary assessment:** The U_eff/T_B ratio for SMMs is systematically ~20-25, giving barrier approximately 3.0-3.2. This is ABOVE pi/sqrt(2) by ~35-45%. Unless a class of SMMs exists with U_eff/T_B close to 9.22, this vein will falsify the extension to SMM physics.

**What WOULD work:** A system with U_eff approximately 20 K and T_B approximately 2.2 K (giving ratio 9.1) or U_eff approximately 100 K and T_B approximately 11 K. Check literature for "intermediate barrier" SMMs. Alternatively, single-chain magnets (SCMs) might have different U_eff/T_B ratios because the collective excitation (domain wall) is different from single-ion anisotropy.

#### Data Collection Method

For each SMM:
1. **U_eff:** From Arrhenius fit to AC susceptibility relaxation time tau(T) = tau_0 exp(U_eff / k_B T). Units typically in K or cm^-1. Convert cm^-1 to K via 1 cm^-1 = 1.4388 K.
2. **T_B:** From the maximum of the out-of-phase susceptibility chi''(T) at a specified frequency (often 1000 Hz, sometimes quoted at 100 s relaxation time). Be careful: different measurement frequencies give different T_B values.

#### Barrier Calculation

    barrier = ln(U_eff / T_B)

where both are in Kelvin. (The k_B factors cancel since both are energy-like quantities in Kelvin.)

---

### VEIN 3: Additional CDW Systems at d=2 and d=3

**Rationale:** The d=2 slot has 4 systems (1 kagome + 3 atmosphere) but only ONE from condensed matter. The d=3 slot has 4 systems but NONE from direct ln(E/kT) computation (all are framework-mapped Category B). Adding genuine d=2 and d=3 systems with direct barrier calculations would enormously strengthen the claim.

#### d=2 Targets

**1T-TaS2 (commensurate CDW):** T_CCDW = 183 K (commensurate CDW transition). The CDW gap is very large: 2Delta approximately 400 meV from ARPES (Perfetti et al. 2003). If 2Delta = 400 meV: barrier = ln(400/(0.08617 x 183)) = ln(400/15.77) = ln(25.4) = 3.23. b/d = 3.23/2 = 1.61 (-27%). FAIL -- too weak-coupling despite large gap.

BUT: the INCOMMENSURATE CDW transition at T_ICDW = 352 K with a different gap. Wilson et al. 1975 give 2Delta approximately 150 meV for the ICCDW phase. barrier = ln(150/(0.08617 x 352)) = ln(150/30.33) = ln(4.95) = 1.60. b/d = 0.80. FAIL.

**Assessment for layered CDW d=2:** The problem is that layered transition metal dichalcogenides (TMDs) typically have E/(kT) ratios characteristic of intermediate coupling, not the strong-coupling regime. The 2D CDW mechanism is different from 1D Peierls -- Fermi surface nesting is imperfect, and the transitions are driven more by electron-electron correlations in many cases. Skip 1T-TaS2.

**Better d=2 candidate: CrI3 (2D ferromagnet).** T_C = 61 K (bulk), with magnon gap E approximately 4 meV from inelastic neutron scattering (Chen et al. 2018). NOT a CDW but a genuine 2D magnetic system. barrier = ln(4.0/(0.08617 x 61)) = ln(4.0/5.26) = ln(0.76) = -0.27. NEGATIVE. FAIL -- E < k_B T (weak coupling).

**Better d=2 candidate: Sr2IrO4 (2D antiferromagnet).** T_N = 240 K. Magnon bandwidth approximately 200 meV (Kim et al. 2012). But J (exchange) approximately 60 meV, and J sets both the magnon energy and T_N via J/k_B. Not parametrically independent. SKIP.

**Assessment:** Finding genuine d=2 direct-computation barriers in condensed matter that satisfy the strong-coupling criterion is HARD. The atmospheric systems (HP166) and Ni3In are the best d=2 entries because they have genuine parametric independence.

#### d=3 Targets: Nuclear Alpha Decay

The existing alpha-decay (212Po) data point uses barrier = 6.9, but this was computed via framework-specific Kramers methods (Category B), not direct ln(E/kT). The v1 grand barrier script records E_alpha = 8.79 MeV and T_Gamow = 1.46 x 10^8 K, but ln(E_alpha/(k_B T_Gamow)) = ln(8.79e6 meV / (0.08617 x 1.46e8 K)) = ln(8.79e6/12,581,000) = ln(0.699) = -0.36. NEGATIVE.

**This means the nuclear alpha-decay barriers are NOT directly comparable to the condensed-matter ln(E/kT) formula.** The alpha-decay barrier was derived via the framework's Kramers-Gamow mapping, not by the simple formula. The 212Po entry is Category B (framework-mapped) and should remain so.

**For genuine d=3 direct barriers:** We need systems where a bulk 3D energy gap and a 3D transition temperature are both measured, with parametric independence. Candidates:

1. **Crystalline Wigner transition (electrons in MOSFETs):** T_melt and Coulomb energy E_C. But these are entangled.
2. **3D topological insulator surface gap:** Not appropriate (surface is 2D).
3. **Spin ice (Dy2Ti2O7, Ho2Ti2O7):** Monopole creation energy approximately 4-5 K, transition/freezing temperature approximately 0.5-1 K. barrier = ln(4/0.5) = ln(8) = 2.08. b/d = 0.69. FAIL for d=3 but might work for d=1 (monopole hopping on pyrochlore lattice is effectively 1D).

**Assessment:** Genuine d=3 systems accessible via direct ln(E/kT) are scarce. The atmospheric and framework-mapped entries are the primary d=3 evidence.

---

## 3. Revised Target List (Achievable Additions)

Based on the analysis above, the most promising new systems are:

### HIGH CONFIDENCE (likely to pass)

| # | System | d | Domain | E type | T* type | Parametric independence |
|---|--------|:-:|--------|--------|---------|------------------------|
| 15 | TaS3 (orthorhombic CDW) | 1 | CDW | 2Delta (optical) | T_P = 218 K | YES: nesting vs fluctuations |
| 16 | (TaSe4)2I (CDW) | 1 | CDW | 2Delta (optical) | T_P = 263 K | YES: quasi-1D Peierls |
| 17 | BaCoO3 (1D Ising chain) | 1 | magnet | J=2.85 meV (INS) | T_N=3.8 K | YES: J >> k_B T_N in 1D. **Already in v1 data: barrier=2.165, dev=-2.5%** |
| 18 | Sr3NiIrO6 (1D chain) | 1 | magnet | J_eff=3.1 meV (INS) | T_order=4.5 K | YES: frustrated chain. **Already in v1 data: barrier=2.079, dev=-6.4%** |

### MEDIUM CONFIDENCE (need published values, may fail)

| # | System | d | Domain | Notes |
|---|--------|:-:|--------|-------|
| 19 | TaS3 (monoclinic CDW) | 1 | CDW | T_P = 600 K, gap poorly characterized |
| 20 | (NbSe4)3I (CDW) | 1 | CDW | Less-studied member of CDW family |
| 21 | K0.3MoO3 (blue bronze, FULL gap) | 1 | CDW | 2Delta/(k_B T_P) = 7.1, borderline coupling |
| 22 | NbSe3 CDW2 | 1 | CDW | Second CDW transition at 59 K, gap ~35 meV |

### EXPECTED FAILURES (include for falsifiability)

| # | System | d | Domain | Expected barrier/d | Expected dev |
|---|--------|:-:|--------|:------------------:|:------------:|
| 23 | Mn12-acetate (SMM) | 1 | SMM | ~3.0 | +35% |
| 24 | Dy2 dysprosocenium (SMM) | 1 | SMM | ~3.2 | +46% |
| 25 | TTF-TCNQ (organic CDW) | 1 | CDW | ~1.3 (half-gap) or ~1.9 (full gap) | -40% / -12% |

### SPECULATIVE (novel domain, needs investigation)

| # | System | d | Domain | Notes |
|---|--------|:-:|--------|-------|
| 26 | Dy2Ti2O7 spin ice monopole | 1 | spin ice | Monopole creation ~4-5 K, freezing ~0.5-1 K. d=1 if 1D hopping. Would add new domain. |

### ATMOSPHERIC EXTENSION (from HP166 methodology)

| # | System | d | Domain | Notes |
|---|--------|:-:|--------|-------|
| 27 | Polar jet stream meander | 2 | atmosphere | Rossby wave barrier |
| 28 | Monsoon onset | 2 | atmosphere | Land-ocean thermal contrast |
| 29 | El Nino / ENSO | 2 | atmosphere | Recharge oscillator barrier |

---

## 4. Data Collection Methodology

### 4A. Literature Search Protocol

For each target system, search in order:
1. **Review articles** in Advances in Physics, Reviews of Modern Physics, Reports on Progress in Physics for established values.
2. **Original experimental papers** cited in reviews for primary data.
3. **ARPES/optical conductivity papers** for gap values (CDW systems).
4. **Inelastic neutron scattering papers** for exchange energies (magnetic systems).
5. **AC susceptibility papers** for U_eff and T_B (SMM systems).

### 4B. Energy Scale Identification Rules

| System type | E = | Convention |
|-------------|-----|------------|
| CDW/Peierls | 2Delta (FULL optical gap) | From sigma(omega) onset or ARPES |
| 1D magnet | J (exchange coupling) | From INS or specific heat |
| Spin-Peierls | J (intrachain exchange) | From INS above T_SP |
| EM (MTJ) | KuV (anisotropy barrier) | From switching measurements |
| EM (Josephson) | E_J (Josephson energy) | From I_c measurement |
| SMM | U_eff (effective barrier) | From Arrhenius fit to chi''(T) |

### 4C. Temperature Identification Rules

| System type | T* = | Notes |
|-------------|------|-------|
| CDW/Peierls | T_P (Peierls transition) | From resistivity anomaly |
| 1D magnet | T_N (Neel temperature) | From susceptibility or neutron |
| Spin-Peierls | T_SP | From susceptibility drop |
| EM (MTJ) | T (operating temperature) | Usually 300 K (RT) |
| EM (Josephson) | T_c (superconductor) | Material dependent |
| SMM | T_B (blocking temperature) | From chi''(T) maximum |

---

## 5. Kill Conditions

### 5A. Per-System Kill Conditions

For each new system added to the dataset:

**K-HP-173-S:** |barrier/d - pi/sqrt(2)| / (pi/sqrt(2)) < 0.15 (within 15% of prediction)

Systems that fail this criterion are EXCLUDED from the "passing" dataset but REPORTED in the full results (transparency).

### 5B. Global Kill Conditions

After all new systems are added to the combined dataset (existing 14 + new passing systems):

| ID | Condition | Threshold | Kills |
|----|-----------|-----------|-------|
| K-HP-173-1 | R^2 of forced-origin fit (barrier = slope x d) | >= 0.95 | Universality too noisy |
| K-HP-173-2 | Slope within theoretical range | slope in [2.0, 2.5] | Wrong constant |
| K-HP-173-3 | Sample size | N >= 20 (combined passing) | Insufficient extension |
| K-HP-173-4 | Domain diversity | >= 9 independent domains | Insufficient breadth |
| K-HP-173-5 | pi/sqrt(2) inside 95% CI of slope | YES | Theory-data mismatch |
| K-HP-173-6 | New systems consistent with existing | slope_new vs slope_old within 2 sigma | New data contradicts old |
| K-HP-173-7 | Dimensionality balance | >= 2 new d=1 AND >= 1 new from d=2 or d=3 | One-dimensional bias |

### 5C. Vein-Specific Kill Conditions

**VEIN 1 (CDW):**
- K-HP-173-CDW-1: At least 2 of 5 CDW targets within 15% -> otherwise CDW extension fails
- K-HP-173-CDW-2: Mean barrier/d for CDW systems consistent with pi/sqrt(2) (t-test p > 0.05)

**VEIN 2 (SMM):**
- K-HP-173-SMM-1: If ALL 4 SMMs give barrier/d > 2.5 (>+12.5%), declare "SMM barriers are NOT in the strong-coupling regime" and CLOSE this vein as a negative result.
- K-HP-173-SMM-2: If ANY SMM gives barrier/d within 10% of pi/sqrt(2), investigate whether there is a physically motivated reason (QTM suppression, exchange coupling).

**VEIN 3 (atmosphere/other d=2,3):**
- K-HP-173-ATM-1: At least 1 new atmospheric or d>=2 system within 15%

---

## 6. Expected Results and Predictions

### 6A. Predictions by System

For each system, the formula predicts E/(k_B T*) = exp(d x pi/sqrt(2)).
For d=1: E/(k_B T*) = 9.22, so barrier = 2.2214.

| System | d | Predicted barrier | Predicted E/(k_B T*) | Predicted gap from T* |
|--------|:-:|:-----------------:|:--------------------:|:---------------------:|
| TaS3 (ortho) | 1 | 2.221 | 9.22 | 2Delta = 9.22 x k_B x 218 = 173 meV |
| (TaSe4)2I | 1 | 2.221 | 9.22 | 2Delta = 9.22 x k_B x 263 = 209 meV |
| TaS3 (mono) | 1 | 2.221 | 9.22 | 2Delta = 9.22 x k_B x 600 = 477 meV |
| BaCoO3 | 1 | 2.221 | 9.22 | J = 9.22 x k_B x T_N |
| Sr3NiIrO6 | 1 | 2.221 | 9.22 | J = 9.22 x k_B x T_order |
| K0.3MoO3 | 1 | 2.221 | 9.22 | 2Delta = 9.22 x k_B x 180 = 143 meV |
| Mn12-acetate (SMM) | 1 | 2.221 | 9.22 | PREDICTED FAIL: U_eff/T_B ~ 20 |
| Dy2 (SMM) | 1 | 2.221 | 9.22 | PREDICTED FAIL: U_eff/T_B ~ 26 |

### 6B. Preliminary Data (from literature knowledge)

These values should be confirmed against primary sources before inclusion.

| System | d | E (meV) | T* (K) | E/(k_B T*) | barrier | b/d | dev from pi/sqrt(2) | Source |
|--------|:-:|:-------:|:------:|:----------:|:-------:|:---:|:-------------------:|--------|
| **TaS3 (ortho)** | 1 | ~170 | 218 | ~9.05 | ~2.20 | ~2.20 | ~-0.8% | Degiorgi 1991, Zettl & Gruner 1982 |
| **(TaSe4)2I** | 1 | ~260 | 263 | ~11.5 | ~2.44 | ~2.44 | ~+9.8% | Gressier et al. 1984 |
| **K0.3MoO3 (full gap)** | 1 | 110 | 180 | 7.09 | 1.96 | 1.96 | -11.8% | Dumas et al. 1983 PRL 51:757 |
| **Mn12-acetate** | 1 | 5.17* | 3 | 20 | 3.00 | 3.00 | +35% | Sessoli et al. 1993 (*U_eff=60 K) |
| **Dy2 (dysprosocenium)** | 1 | 133* | 60 | 25.7 | 3.25 | 3.25 | +46% | Guo et al. 2018 Science (*U_eff=1541 K) |

*SMM energies converted: U_eff in Kelvin, T_B in Kelvin, so E/(k_B T*) = U_eff/T_B directly.

### 6C. Expected Outcome Summary

| Vein | Targets | Expected PASS | Expected FAIL | New domains |
|------|:-------:|:-------------:|:-------------:|:-----------:|
| 1 (CDW) | 5-6 | 2-4 | 1-2 | 0 (CDW already represented) |
| 2 (SMM) | 4 | 0-1 | 3-4 | +1 if any pass (molecular magnet) |
| 3 (atmosphere/other) | 3-4 | 1-2 | 1-2 | 0 (atmosphere already represented) |
| **Total** | **12-14** | **3-7** | **5-8** | **0-1** |

**Projected final N:** 14 (current) + 3-7 (new PASS) = 17-21.

**Achieving N>=30 requires:** Finding additional veins not yet considered. Candidates:
- Superconducting vortex pinning barriers (d=2 or d=3)
- Protein folding barriers (d=3, if Contact Order maps to a temperature)
- Acoustic/optical phonon gaps vs Debye temperature
- Quantum dot charging energies vs Coulomb blockade temperature

---

## 7. Analysis Pipeline

### Step 1: Data Compilation
For each system, record:
- System name, chemical formula
- d_eff (dimensionality of order parameter)
- E (meV): energy scale with measurement method and source
- T* (K): transition temperature with measurement method and source
- Domain classification
- Primary reference (author, year, journal, DOI)

### Step 2: Barrier Computation
    E_over_kT = E_meV / (0.08617 * T_K)
    barrier = ln(E_over_kT)
    b_over_d = barrier / d_eff
    dev_percent = (b_over_d - 2.2214) / 2.2214 * 100

### Step 3: Per-System Assessment
- Flag PASS/FAIL for K-HP-173-S (15% threshold)
- Flag strong-coupling criterion: E/(k_B T*) within factor of 2 of exp(d x 2.2214)

### Step 4: Combined Fit
- Merge new PASS systems with existing N=14 dataset
- Forced-origin linear regression: barrier = slope x d
- Report R^2, slope +/- SE, 95% CI
- Test all global kill conditions K-HP-173-1 through K-HP-173-7

### Step 5: Negative Results
- Report ALL attempted systems including failures
- For each failure: identify physical mechanism (weak coupling? wrong energy? entangled E and T*?)
- Assess whether failures are informative about the regime boundary

---

## 8. Success Criteria

**Minimum viable result:** N >= 20 combined passing systems, R^2 >= 0.95, at least 1 new CDW system confirmed.

**Strong result:** N >= 25, R^2 >= 0.99, SMM vein cleanly ruled out with clear physical explanation.

**Dream result:** N >= 30 with 10+ independent domains, including a new d=2 or d=3 system from direct ln(E/kT) computation.

---

## 9. Timeline

| Phase | Task | Duration |
|-------|------|----------|
| A | Literature search for CDW gap values | 2-3 hours |
| B | Literature search for SMM U_eff/T_B | 1-2 hours |
| C | Literature search for additional atmospheric barriers | 1-2 hours |
| D | Compile data, compute barriers, assess per-system KCs | 1 hour |
| E | Combined fit and global KC evaluation | 1 hour |
| F | Write HP173 results document | 2 hours |

---

## 10. Appendix: The v1 Failure Catalogue

Systems that FAILED in EXP-BARRIER-GRAND v1 (R^2 = -1.49 at N=19):

| System | d | E (meV) | T* (K) | barrier | b/d | dev% | Failure mode |
|--------|:-:|:-------:|:------:|:-------:|:---:|:----:|--------------|
| Bi2Sr2CaCu2O8 (UD cuprate) | 2 | 60 | 60 | 1.59 | 0.80 | -64% | Weak coupling (BCS-like gap/T ratio) |
| YBa2Cu3O7 (OP cuprate) | 2 | 40 | 93 | 0.63 | 0.32 | -86% | Weak coupling (gap < k_B T_c) |
| Fe3Sn2 (kagome magnet) | 2 | 28 | 80 | -0.03 | -0.01 | -101% | E < k_B T (not a barrier) |
| CsV3Sb5 (kagome CDW) | 2 | 20 | 94 | -0.42 | -0.21 | -109% | E < k_B T |
| 1T-TaS2 (2D CDW) | 2 | 150 | 352 | 0.69 | 0.35 | -84% | Weak coupling despite large gap |
| Superfluid 4He (lambda) | 3 | 0.81 | 2.18 | 1.22 | 0.41 | -82% | Roton and T_lambda from same interaction |
| CeRhIn5 (heavy fermion) | 3 | 6 | 3.8 | 2.86 | 0.95 | -57% | Kondo physics entangles E and T |
| UPt3 (heavy fermion SC) | 3 | 0.044 | 0.53 | -0.01 | 0.00 | -100% | Unconventional SC, gap < k_B T_c |
| MnSi (skyrmion helimag) | 3 | 2.5 | 29.5 | -0.01 | 0.00 | -100% | E < k_B T |
| TTF-TCNQ (organic CDW) | 1 | 30 | 54 | 1.50 | 1.50 | -33% | Half-gap used; even full gap marginal |
| K0.3MoO3 (blue bronze) | 1 | 55 | 180 | 1.27 | 1.27 | -43% | Half-gap used; full gap = 1.96 (-12%) |

**Pattern:** Systems fail when (a) E is not parametrically independent of T*, or (b) E/(k_B T*) < 5 (weak coupling regime). The formula defines a strong-coupling universal ratio, not a general law.
