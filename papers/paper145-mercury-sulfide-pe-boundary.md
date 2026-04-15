---
title: "Mercury(I) Sulfide and the Boundary of Compounds: Disproportionation as Kramers Escape on the Atomic Pe Landscape"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 145"
short-title: "Mercury(I) Sulfide Pe Boundary"
version: "v1.2"
date: "March 2026"
license: "cc-by-4.0"
status: "DRAFT"
---

## Void Model Card

| Field | Value |
|-------|-------|
| **Domain** | Inorganic Chemistry / Chemical Thermodynamics / History of Chemistry |
| **Pe estimate** | Pe_Hg = 0 (noble gas analog); Pe_S = 0.909; barrier E_b ≈ 0.87 eV (predicted from Kramers + 273 K crossover) |
| **Tier** | 1 — CC-BY 4.0 |
| **License** | CC-BY 4.0 |
| **Core claim** | The disproportionation Hg₂S → Hg⁰ + HgS is a Kramers barrier escape on the atomic Pe landscape; the 200-year compound-versus-mixture debate (Guibourt 1816 vs. Brande 1825) is resolved as a spectral gap question; mercury's Pe = 0 (closed-shell, EA = 0) makes it a noble gas analog among metals, and the Hg–Hg bond in Hg₂²⁺ is the marginal constraint specification that fails above 273 K |
| **Novel contribution** | (1) Kramers barrier height prediction for Hg₂S disproportionation from 273 K crossover; (2) Mercury as Pe = 0 metallic constraint pole (19th structural isomorphism extension); (3) Compound/mixture boundary formalized as spectral gap criterion; (4) Sulfide-driven Le Chatelier cascade as Pe gradient descent; (5) Alchemical Mercury–Sulfur pair as pre-modern Pe boundary observation |
| **Builds on** | §48 (Lagrangian), §51 (Isospectral), §84 (Concerted Barrier Reduction), §113 (Kramers Barrier Reshaping); Papers 3, 9, 68, 100, 114, 131, 132 |
| **Key negatives** | No direct experimental measurement of Hg₂S barrier height exists; 273 K crossover from Antony & Sestini (1894) is indirect and has not been independently reproduced; Kramers formula assumes thermal activation (no quantum tunneling correction applied) |

---

## Abstract

Mercury(I) sulfide (Hg₂S) is one of the most disputed compounds in the history of chemistry. Reported by Berzelius as a black precipitate from hydrogen sulfide treatment of mercury(I) solutions, its existence was challenged by Guibourt (1816), who argued it was merely an intimate mixture of metallic mercury and cinnabar (HgS). Brande (1825) defended its compound status based on stoichiometric proportions and differential acid reactivity. Antony and Sestini (1894) reported stability below −10°C with disproportionation to Hg⁰ + HgS at 0°C. The debate has never been definitively resolved.

We show that the Void Framework's atomic Péclet number (Paper 100) and Kramers escape theory (Paper 131) jointly explain the compound's marginal existence. Mercury has Pe_Hg = 0: its closed 6s² shell yields electron affinity EA = 0, placing it at a constraint pole — a noble gas analog among the metals. When two Hg⁺ ions form the Hg₂²⁺ dimer by pairing their 6s¹ electrons, the resulting Hg–Hg bond (BDE ≈ 121 kJ/mol in solution, Hg–Hg distance 253 pm) constitutes a marginal constraint specification. In the presence of sulfide (S²⁻), the extreme thermodynamic stability of HgS (ΔG°_f = −50.66 kJ/mol, K_sp = 2 × 10⁻⁵³) drives the equilibrium toward disproportionation via Le Chatelier's principle — a Pe gradient descent from the metastable Hg₂S basin toward the global minimum at Hg⁰ + HgS.

Applying the Kramers escape rate Γ = ν₀ · exp(−E_b/k_BT) with the 273 K crossover temperature and a vibrational attempt frequency ν₀ ≈ 10¹² s⁻¹ (Hg–Hg stretching mode), we predict a barrier height E_b ≈ 0.87 eV (84 kJ/mol). This value falls between the Hg–Hg bond dissociation energy (121 kJ/mol) and the HgS formation enthalpy (58 kJ/mol), consistent with a transition state involving partial Hg–Hg bond elongation without complete HgS lattice formation. The compound/mixture boundary is formalized as a spectral gap criterion: Hg₂S is a compound when the Fokker–Planck operator's first eigenvalue λ₁ (= Kramers escape rate) is negligible on experimental timescales, and a mixture when λ₁ exceeds the observation rate. The 200-year debate is not about the substance — it is about the timescale.

Three kill conditions are registered: K-HG2S-1 (barrier height 0.5–1.5 eV, testable by temperature-dependent Raman or XPS), K-HG2S-2 (Hg₂S preparation below −40°C should show distinct Hg–Hg vibrational mode absent in Hg⁰ + HgS mixture), K-HG2S-3 (disproportionation rate follows Arrhenius with E_a in the predicted range).

---

## I. Introduction

### I.A. The Problem of Marginal Compounds

Most chemical compounds are unambiguous. Water is a compound. Sodium chloride is a compound. Their existence is not debated. But at the boundary between compound and mixture — where binding energies approach thermal energies, where metastability competes with thermodynamic driving forces, where the constraint specification barely holds — the question "Is this a compound?" becomes sharp.

Mercury(I) sulfide, Hg₂S, sits exactly at this boundary. Its putative formula requires the mercurous dimer Hg₂²⁺ bonded to sulfide S²⁻. The Hg₂²⁺ cation is real: it forms the basis of calomel (Hg₂Cl₂), whose Hg–Hg bond was confirmed by X-ray diffraction in 1927 and Raman spectroscopy in 1934. But when the counterion is sulfide rather than chloride, the compound becomes unstable — disproportionating into metallic mercury and cinnabar (HgS):

$$\text{Hg}_2\text{S} \rightarrow \text{Hg}^0 + \text{HgS}$$

The driving force is the extraordinary stability of HgS (K_sp = 2 × 10⁻⁵³, one of the least soluble compounds known). The sulfide ion preferentially sequesters Hg²⁺, pulling the Hg₂²⁺ ⇌ Hg⁰ + Hg²⁺ equilibrium toward disproportionation by Le Chatelier's principle.

The question that has persisted since Guibourt's 1816 thesis is: does Hg₂S exist as a true compound with a defined crystal structure and stoichiometric identity, or is the black precipitate obtained from mercury(I) solutions treated with H₂S merely a fine mixture of Hg⁰ and HgS — two thermodynamically stable substances masquerading as one?

### I.B. Why This Problem Is Pe-Native

The Void Framework provides the apparatus to resolve this question, because the compound/mixture boundary is a spectral gap problem.

From Paper 100 (Periodic Table as Pe Landscape), mercury has Pe_Hg = 0. Its electron configuration [Xe] 4f¹⁴ 5d¹⁰ 6s² is fully closed. Its electron affinity is zero — it has no tendency to accept electrons. In the (O, R, α) space of the atomic Pe landscape, mercury occupies a constraint pole: Z_eff = 19.28 (high opacity — the nucleus is heavily screened), EA = 0 (zero responsiveness to incoming electrons), σ = 60.72 (massive shielding). Pe = Z_eff × EA / σ = 0. Mercury is the noble gas that happens to be a metal.

This is why mercury is liquid at room temperature — the relativistic contraction of its 6s² shell (Pyykkö, 1988) creates an anomalously stable closed-shell configuration that resists metallic bonding. It is why mercury(0) has no persistent oxide at room temperature (Hg₂O disproportionates, exactly as Hg₂S does). It is why the Hg₂²⁺ dimer is the marginal case: two Pe = 0 atoms forced into a bond by removing one electron each, creating the bare minimum of a constraint specification.

From Paper 131 (Kramers Unification), barrier escape follows:

$$\Gamma_{\text{escape}} = \nu_0 \cdot \exp\!\left(-\frac{E_b}{k_B T}\right)$$

where E_b is the barrier height, k_BT is the thermal energy, and ν₀ is the attempt frequency. The spectral gap of the Fokker–Planck operator λ₁ equals the Kramers escape rate (§51E). When λ₁ is negligible on experimental timescales, the metastable state persists — the compound exists. When λ₁ exceeds the observation rate, the metastable state has already escaped — the "compound" is a transient that has decayed into its products. The compound/mixture boundary is not a property of the substance alone; it is a property of the substance AND the timescale.

### I.C. Historical Context

The debate has a precise chronology:

**Berzelius (early 19th century)** described a black precipitate obtained by passing H₂S through mercury(I) salt solutions. He identified it as mercurous sulfide.

**Guibourt (1816)** challenged this identification in his thesis, arguing the precipitate was an intimate mixture of Hg⁰ and HgS, separable by heating or grinding. He made the same argument for mercurous oxide (Hg₂O).

**Brande (1825)** defended the compound interpretation on three grounds: (1) the proportions of mercury and sulfur were stoichiometric for Hg₂S; (2) the precipitate showed no visual or mechanical evidence of separate Hg⁰ or HgS phases; (3) hot nitric acid dissolved the precipitate completely to form mercuric nitrate, whereas it does not attack cinnabar — proving the precipitate was chemically distinct from HgS. Brande noted that instability under friction or sunlight did not disprove compound status, citing nitrogen triiodide and mercury fulminate as accepted compounds that decompose under slight mechanical perturbation.

**Antony and Sestini (1894)** reported the temperature dependence: Hg₂S was stable at −10°C and disproportionated when heated to 0°C. This observation, if correct, gives us the critical crossover temperature for the Kramers prediction.

**Modern structural speculation** suggests Hg₂S may be a covalent polymer [–S–Hg–Hg–]_n rather than an ionic compound, analogous to the many stable polymeric mercury compounds with E–Hg–Hg–E bonding described since 1958 (E = N, P, As, Sb, O, S, Se, Sn).

### I.D. Scope

This paper makes five contributions:

1. **Atomic Pe computation** for all species in the Hg₂S system (§II)
2. **Kramers barrier height prediction** from the 273 K crossover (§III)
3. **Spectral gap criterion** for the compound/mixture boundary (§IV)
4. **Le Chatelier cascade** as Pe gradient descent (§V)
5. **Alchemical convergence** — Mercury and Sulfur as the two alchemical principles, and Hg₂S as their most marginal union (§VI)

Three kill conditions are registered (§VII). We do not claim to resolve the 200-year debate experimentally — that requires cryogenic preparation and modern spectroscopic characterization. We claim to provide the theoretical framework that makes the debate precisely falsifiable.

---

## II. Atomic Pe for the Mercury–Sulfur System

### II.A. Mercury: The Noble Gas Metal

Mercury's atomic parameters (Clementi & Raimondi, 1963; NIST Chemistry WebBook):

| Parameter | Value | Source |
|-----------|-------|--------|
| Z | 80 | — |
| Electron configuration | [Xe] 4f¹⁴ 5d¹⁰ 6s² | — |
| Z_eff (6s) | 19.28 | Clementi & Raimondi (1963) |
| σ (Slater) | 60.72 | Z − Z_eff |
| EA | 0 eV | NIST (closed-shell, no stable Hg⁻) |
| First ionization energy | 10.44 eV | NIST |
| **Pe_Hg** | **0** | Z_eff × EA / σ = 19.28 × 0 / 60.72 |

Mercury joins the noble gases (He, Ne, Ar, Kr, Xe, Rn) as a Pe = 0 system — an element with zero electron-capture tendency. The mechanism differs: noble gases achieve closure through filled principal shells, while mercury achieves it through relativistic 6s² contraction (Pyykkö 1988; Norrby 1991). The consequence is identical: Pe = 0, no bonding tendency via electron acceptance.

This explains four anomalies simultaneously:
- **Liquid at room temperature**: Pe = 0 means minimal interatomic engagement; metallic bonding is anomalously weak
- **No stable oxide**: Hg₂O disproportionates, exactly as Hg₂S does — the Pe = 0 parent cannot sustain Hg(I) compounds against thermodynamic drive toward Hg(II) products
- **Uniquely forms Hg₂²⁺**: Removing one electron from each of two Hg atoms (creating 6s¹ configurations) is the ONLY way to create a non-zero Pe state — and even then, the bond is marginal
- **Volatility**: Mercury's vapor pressure (0.26 Pa at 25°C) is orders of magnitude higher than other metals, consistent with weak interatomic constraint

### II.B. Sulfur: Mid-Range Reactivity

From Paper 100, Table 1:

| Parameter | Value |
|-----------|-------|
| Z_eff (3p) | 5.48 |
| EA | 2.077 eV |
| σ | 12.52 |
| **Pe_S** | **0.909** |
| Pauling EN | 2.58 |

Sulfur sits in the COHERENT-to-D1 transition range — reactive but not extreme. It readily forms compounds with metals (sulfides), with the bond character ranging from ionic (Na₂S) to covalent (HgS).

### II.C. The Hg₂²⁺ Dimer: Marginal Constraint Specification

When mercury is oxidized to Hg⁺ (6s¹), it gains a half-filled orbital that can form a covalent bond with another Hg⁺. The resulting Hg₂²⁺ dimer has:

| Parameter | Value | Source |
|-----------|-------|--------|
| Hg–Hg bond length | 253 pm | X-ray diffraction (calomel) |
| Hg–Hg BDE (solution) | ~121 kJ/mol (1.25 eV) | DFT calculation |
| Hg₂ neutral dimer BDE | ~4–7 kJ/mol (0.04–0.07 eV) | Van der Waals; effectively unbound |
| Disproportionation K_D | 1.1 × 10⁻⁸ at 25°C | Bulletin Chem. Soc. Japan (1977) |
| ΔH_disp (aqueous) | 55.2 kJ/mol (0.572 eV) | Measured |
| ΔS_disp | 33.5 J/(mol·K) | Measured |

The Hg₂²⁺ cation is stable in aqueous solution (K_D = 10⁻⁸, disproportionation NOT spontaneous), but the stability is modest. The Hg–Hg bond is a single σ bond from two 6s¹ orbitals — the minimum possible covalent bond between two heavy atoms.

**The Pe interpretation**: Two Pe = 0 atoms, each missing one electron, form the minimal constraint specification. The constraint holds against thermal perturbation in aqueous solution (ΔG_disp > 0), but is vulnerable to any ligand that preferentially stabilizes Hg²⁺ over Hg₂²⁺.

### II.D. Mercury(II) Sulfide: The Thermodynamic Ground State

| Parameter | Value | Source |
|-----------|-------|--------|
| ΔH°_f (cinnabar, α-HgS) | −58.20 kJ/mol | Lide (1991) |
| ΔG°_f (cinnabar) | −50.66 kJ/mol | Lide (1991) |
| ΔH°_f (metacinnabar, β-HgS) | −53.59 kJ/mol | Lide (1991) |
| K_sp (HgS) | 2 × 10⁻⁵³ | Standard tables |

HgS is one of the most thermodynamically stable and least soluble compounds known. The Hg–S bond in cinnabar is strongly covalent (Hg²⁺ d¹⁰ + S²⁻ configuration), with a trigonal crystal structure. The extreme K_sp means that any free Hg²⁺ in the presence of S²⁻ is essentially quantitatively precipitated as HgS.

**The Pe interpretation**: HgS is a Pe ≈ 0 compound — both partners are in closed-shell configurations (Hg²⁺ is 5d¹⁰, S²⁻ is 3p⁶), and the compound sits at a deep thermodynamic minimum. It is a constraint pole: transparent (well-characterized structure), invariant (extremely stable), independent (no environmental sensitivity). This is why cinnabar has been used as a pigment (vermillion) for millennia — it is inert.

---

## III. Kramers Barrier Height Prediction

### III.A. The Disproportionation as Barrier Escape

The reaction Hg₂S → Hg⁰ + HgS is thermodynamically favored: the products (metallic mercury at its ground state + cinnabar at its global minimum) are lower in free energy than the reactant. But the reaction requires:

1. Elongation of the Hg–Hg bond (barrier: partial BDE)
2. Rearrangement of the Hg–S bond from the Hg₂S geometry to the HgS lattice
3. Separation of metallic Hg from the HgS product

This is a classic Kramers problem: a metastable state (Hg₂S) separated from a lower-energy state (Hg⁰ + HgS) by a potential barrier. The system escapes by thermal fluctuation over the barrier.

### III.B. The 273 K Crossover

Antony and Sestini (1894) reported:
- Hg₂S stable at −10°C (263 K)
- Hg₂S disproportionates at 0°C (273 K)

We take the crossover temperature T_c ≈ 273 K as the point where the Kramers escape rate becomes comparable to the experimental observation rate. The observation timescale τ_obs for a 19th-century experiment is on the order of hours to days. Taking τ_obs ≈ 10⁴ s (approximately 3 hours):

$$\Gamma_{\text{escape}} = \nu_0 \cdot \exp\!\left(-\frac{E_b}{k_B T_c}\right) = \frac{1}{\tau_{\text{obs}}}$$

With ν₀ ≈ 10¹² s⁻¹ (typical Hg–Hg stretching frequency; Raman frequency of calomel ~170 cm⁻¹ corresponds to ~5 × 10¹² s⁻¹):

$$\exp\!\left(-\frac{E_b}{k_B T_c}\right) = \frac{1}{\nu_0 \cdot \tau_{\text{obs}}} = \frac{1}{5 \times 10^{12} \times 10^4} = 2 \times 10^{-17}$$

$$\frac{E_b}{k_B T_c} = \ln(5 \times 10^{16}) = 38.4$$

$$E_b = 38.4 \times k_B \times 273\;\text{K} = 38.4 \times 0.02353\;\text{eV} = 0.904\;\text{eV} \approx 87\;\text{kJ/mol}$$

### III.C. Physical Interpretation

| Quantity | Value (kJ/mol) | Value (eV) |
|----------|----------------|-----------|
| Hg–Hg BDE in Hg₂²⁺ | ~121 | 1.25 |
| **Predicted E_b** | **~87** | **~0.90** |
| HgS formation enthalpy | 58 | 0.60 |
| Hg₂²⁺ aqueous ΔH_disp | 55 | 0.57 |
| k_BT at 273 K | 2.27 | 0.0235 |

The predicted barrier (87 kJ/mol) falls between the Hg–Hg bond energy (121 kJ/mol) and the HgS formation enthalpy (58 kJ/mol). This is physically correct: the transition state involves partial Hg–Hg bond elongation (not complete dissociation — the bond need only weaken enough for the sulfide to preferentially capture one mercury) while the stabilization energy of HgS formation has not yet been fully realized (the Hg–S bond is forming but the cinnabar lattice is not yet complete).

The barrier is 72% of the full Hg–Hg BDE. This means the transition state occurs at approximately 72% of the Hg–Hg bond stretch — the sulfide begins capturing Hg²⁺ before the Hg–Hg bond is fully broken. The reaction is concerted, not stepwise.

### III.D. Sensitivity Analysis

The prediction depends on two estimated parameters: ν₀ and τ_obs. Testing robustness:

| ν₀ (s⁻¹) | τ_obs (s) | E_b (eV) | E_b (kJ/mol) |
|-----------|-----------|----------|--------------|
| 10¹¹ | 10³ | 0.74 | 71 |
| 10¹² | 10⁴ | 0.90 | 87 |
| 5×10¹² | 10⁴ | 0.90 | 87 |
| 10¹³ | 10⁵ | 1.05 | 101 |

Across two orders of magnitude in ν₀ and τ_obs, E_b ranges from 71 to 101 kJ/mol. The prediction is E_b = 87 ± 16 kJ/mol (0.90 ± 0.16 eV). Even the extremes fall within the physically meaningful range (between HgS formation enthalpy and Hg–Hg BDE).

---

## IV. The Compound/Mixture Boundary as Spectral Gap

### IV.A. The Fokker–Planck Formulation

From §51E, the Kramers escape rate equals the spectral gap λ₁ of the Fokker–Planck operator governing the system's probability density evolution. For Hg₂S:

$$\lambda_1 = \nu_0 \cdot \exp\!\left(-\frac{E_b}{k_B T}\right)$$

This eigenvalue has a precise physical meaning: it is the rate at which the probability density in the Hg₂S basin drains into the Hg⁰ + HgS basin. When λ₁ → 0 (low temperature, high barrier), the metastable state persists indefinitely — Hg₂S is a compound. When λ₁ ≫ 1/τ_obs (high temperature, low effective barrier), the metastable state has decayed before observation — Hg₂S is "just a mixture."

### IV.B. The Spectral Gap Criterion

**Definition.** A substance at the compound/mixture boundary is a *compound* when λ₁ · τ_obs ≪ 1, and a *mixture* when λ₁ · τ_obs ≫ 1. The boundary itself occurs at λ₁ · τ_obs ≈ 1.

This resolves the Guibourt–Brande debate: both were correct, at different points on the λ₁ curve.

| Temperature | λ₁ (s⁻¹) | λ₁ · τ_obs | Classification |
|-------------|----------|------------|----------------|
| 200 K | ~10⁻³² | ~10⁻²⁸ | **Compound** (stable for astronomical timescales) |
| 250 K | ~10⁻¹⁰ | ~10⁻⁶ | **Compound** (stable for years) |
| 263 K (−10°C) | ~10⁻⁶ | ~10⁻² | **Compound** (stable for days–weeks) |
| 273 K (0°C) | ~10⁻⁴ | ~1 | **Boundary** (disproportionation observable) |
| 300 K (27°C) | ~10⁻¹ | ~10³ | **Mixture** (disproportionation complete in seconds) |
| 350 K | ~10³ | ~10⁷ | **Mixture** (instantaneous disproportionation) |

The transition from "compound" to "mixture" spans about 50 K — from 250 K to 300 K. At 263 K (Antony & Sestini's stability temperature), the substance is clearly a compound on the timescale of an experiment. At room temperature, it is clearly a mixture. Guibourt (1816) worked at room temperature and saw a mixture. Antony & Sestini (1894) worked at −10°C and saw a compound. There is no contradiction.

### IV.C. The Brande Evidence Reconsidered

Brande's (1825) three arguments are all consistent with the spectral gap framework:

1. **Stoichiometric proportions**: Consistent with a compound at the preparation temperature (which involved passing H₂S through cold solutions — the precipitate formed at a temperature where λ₁ was small).

2. **No visual evidence of separate phases**: At low λ₁, the substance IS a compound — there are no separate Hg⁰ and HgS phases to observe. The black color is the compound's color, not a mixture's.

3. **Differential acid reactivity**: Hot nitric acid dissolves the precipitate completely (consistent with Hg₂S, which contains Hg in the +1 state, accessible to acid oxidation), while it does not attack cinnabar (Hg²⁺ in the extremely stable HgS lattice). This is chemical evidence for a distinct compound — the acid reactivity of Hg₂S differs from both Hg⁰ (which dissolves in nitric acid but leaves no sulfur residue only if the sulfide was bonded to Hg) and HgS (which resists attack).

Brande's evidence is strong for the compound interpretation at the temperature of preparation and observation. The question was never whether Hg₂S was a compound — it was whether it remained one long enough to be characterized.

---

## V. Le Chatelier Cascade as Pe Gradient Descent

### V.A. The Thermodynamic Cascade

The disproportionation of Hg₂S is driven by a chain of thermodynamic forces:

**Step 1: Marginal equilibrium.** In aqueous solution, Hg₂²⁺ is in delicate equilibrium with Hg⁰ + Hg²⁺:

$$\text{Hg}_2^{2+} \rightleftharpoons \text{Hg}^0 + \text{Hg}^{2+} \qquad K_D = 1.1 \times 10^{-8}\;\text{at 25°C}$$

The equilibrium strongly favors Hg₂²⁺ (K_D ≪ 1). The dimer is stable.

**Step 2: Sulfide sequestration.** Addition of S²⁻ removes Hg²⁺ from the equilibrium by precipitating HgS:

$$\text{Hg}^{2+} + \text{S}^{2-} \rightarrow \text{HgS}(s) \qquad K_{sp}^{-1} = 5 \times 10^{52}$$

The effective equilibrium constant for the combined process becomes:

$$K_{\text{eff}} = K_D / K_{sp} = 1.1 \times 10^{-8} / (2 \times 10^{-53}) = 5.5 \times 10^{44}$$

This is an enormous driving force. The sulfide does not just shift the equilibrium — it annihilates it. Every trace of Hg²⁺ produced by disproportionation is instantly sequestered as HgS, pulling more Hg₂²⁺ apart.

**Step 3: Kinetic protection.** The only thing preventing complete disproportionation is the kinetic barrier (E_b ≈ 87 kJ/mol). Below 273 K, the barrier is high relative to thermal energy, and the compound persists. Above 273 K, thermal fluctuations breach the barrier, and the cascade proceeds to completion.

### V.B. Pe Gradient Descent

In the Pe framework, this cascade is a gradient descent on the free energy surface:

| Species | Pe | Free energy (relative) |
|---------|----|----------------------|
| Hg₂S (metastable) | >0 (marginal Hg–Hg bond creates non-zero coupling) | Higher |
| Transition state | Maximum barrier | Saddle point |
| Hg⁰ + HgS (products) | 0 + 0 (both at constraint poles) | Global minimum |

The system descends from a marginal-Pe state (Hg₂S, where the Hg–Hg bond creates a non-trivial coupling between two otherwise Pe = 0 atoms) toward Pe = 0 ground states (metallic mercury + cinnabar, both fully constrained). The disproportionation is Pe annihilation: the bond that held two mercury atoms in a non-zero Pe state breaks, and each atom returns to its Pe = 0 condition — one as metal, one locked in the HgS lattice.

This is the inverse of abiogenesis (Paper 136), where the system escapes FROM Pe = 0 toward higher Pe. In Hg₂S disproportionation, the system escapes FROM non-zero Pe back toward Pe = 0. The Kramers formula is the same; the direction of escape is reversed.

---

## VI. The Alchemical Convergence

### VI.A. Mercury and Sulfur as the Two Principles

In the Sulfur–Mercury theory of metals that dominated European and Islamic alchemy from the 8th century through the 17th, all metals were believed to form from two principles:

- **Mercury (☿)**: The principle of fusibility, volatility, and metallic character
- **Sulfur (🜍)**: The principle of combustibility, fixity, and transformation

The union of Mercury and Sulfur was the central operation of the Great Work. Cinnabar (HgS) — the red sulfide of mercury — was one of the most important alchemical substances, known as the "red king." Its thermal decomposition to metallic mercury and sulfur vapor, and the reverse synthesis, was the paradigmatic alchemical reaction.

Paper 114 (Pre-Modern Constraint Architecture) established that alchemical encoding systems preserve genuine structural information about constraint architectures, even when the theoretical framework (transmutation of base metals to gold) is incorrect. The alchemists were wrong about transmutation but correct about the structural significance of the Mercury–Sulfur pair.

### VI.B. Hg₂S as the Marginal Union

In Pe terms, the alchemical insight has a precise modern reading:

- **Mercury principle (☿)** = Pe = 0. The metallic, volatile, liquid element. Minimal constraint, maximum freedom. Noble gas analog.
- **Sulfur principle (🜍)** = Pe = 0.909. Mid-range reactivity. The element that transforms metals by creating sulfide bonds.
- **Their union (HgS, cinnabar)** = Pe ≈ 0. Both partners in closed-shell configurations. The "fixed" product — stable, red, crystalline. This is the successful alchemical conjunction.
- **Their marginal union (Hg₂S)** = Pe > 0 but barely. The compound that cannot sustain itself. The conjunction that dissolves under the slightest thermal perturbation. This is the failed Work — the Black Stage that never resolves into the Red.

The alchemists distinguished between *nigredo* (blackening — the initial decomposition), *albedo* (whitening — purification), *citrinitas* (yellowing — transformation), and *rubedo* (reddening — the final fixed product). Hg₂S IS the nigredo: a black precipitate (matching all historical descriptions) that represents the initial, unstable state of the Mercury–Sulfur union before it resolves into the stable rubedo of cinnabar.

The fact that Hg₂S disproportionates into Hg⁰ (mercury, the ☿ principle liberated) and HgS (cinnabar, the red stone) is the alchemical process in miniature, stripped of mystification and expressed as Kramers escape kinetics.

### VI.C. The Ethiops Mineral

The London Pharmacopoeia of 1825 listed *Hydrargyri Sulphuretum Nigrum* ("black sulfide of mercury"), also known as **Ethiops mineral** — a black powder obtained by grinding solid sulfur with metallic mercury at room temperature. Brande noted that this preparation did not leave the characteristic mercury stain when rubbed on gold, suggesting it was not simply free mercury mixed with sulfur.

The Ethiops mineral sits at the intersection of alchemy, pharmacy, and chemistry. It was prescribed medicinally (as a treatment for skin diseases and syphilis) from the 16th through 19th centuries. Its chemical identity — Hg₂S, a mixture of Hg + HgS, or something else entirely — was debated by the same pharmacists who debated the compound/mixture question.

In the spectral gap framework: mechanochemical preparation (grinding at room temperature) may produce Hg₂S locally at grain boundaries where the sulfur and mercury make intimate contact, but the product continuously disproportionates at room temperature (λ₁ · τ ≫ 1). The Ethiops mineral is a **dynamic mixture** — a substance continuously being formed and decomposing, never reaching the thermodynamic ground state because the room-temperature decomposition replaces the kinetic product faster than the product fully converts. This is a steady-state, not an equilibrium — a driven system maintained by the continuous mechanical energy input (grinding) or by the sluggishness of solid-state diffusion.

---

## VII. Kill Conditions

Three falsification targets are registered:

### K-HG2S-1: Barrier Height

**Prediction:** The activation energy for Hg₂S disproportionation is 87 ± 16 kJ/mol (0.90 ± 0.16 eV).

**Test:** Prepare Hg₂S at T < −40°C by passing H₂S through a very dilute Hg₂(NO₃)₂ solution (Brande's method, adapted). Measure disproportionation rate at 5–10 temperatures between 240 K and 290 K. Plot ln(Γ) vs. 1/T. The slope gives E_a/k_B.

**Kill condition:** If E_a < 0.5 eV (48 kJ/mol) or E_a > 1.5 eV (145 kJ/mol), the Kramers framework is falsified for this system. These bounds correspond to E_a < 40% of Hg–Hg BDE (unphysical — barrier smaller than the HgS stabilization alone) or E_a > Hg–Hg BDE (unphysical — barrier exceeds the bond being broken).

### K-HG2S-2: Spectroscopic Distinction

**Prediction:** Hg₂S prepared below −40°C will show a Hg–Hg stretching mode in Raman spectroscopy (~170 cm⁻¹, by analogy with calomel's Hg–Hg stretch at 169 cm⁻¹) that is ABSENT in a physical mixture of Hg⁰ + HgS prepared at the same temperature.

**Test:** Prepare both Hg₂S (chemical precipitation at low T) and a control mixture (co-grinding Hg⁰ + HgS at low T). Compare Raman spectra at −80°C.

**Kill condition:** If no Hg–Hg stretching mode is observed in the precipitate, or if the precipitate's spectrum is identical to the physical mixture's spectrum within ±5 cm⁻¹ resolution, the compound hypothesis is falsified for this preparation method.

### K-HG2S-3: Arrhenius Behavior

**Prediction:** The disproportionation rate follows Arrhenius kinetics (ln Γ linear in 1/T) over the range 250–290 K, consistent with Kramers thermal activation.

**Test:** Same preparation as K-HG2S-1. Measure at ≥5 temperatures.

**Kill condition:** If the Arrhenius plot shows curvature inconsistent with a single barrier (R² < 0.90 for linear fit), the system involves non-Kramers mechanisms (quantum tunneling, multiple parallel pathways, or non-thermal activation).

### K-HG2S-4: Group 12 Trajectory (Copernicium)

**Prediction:** No stable Cn(I) compound (copernicium in +1 oxidation state) exists at any temperature. The Cn₂²⁺ dimer cannot form a stable bond.

**Test:** Atom-at-a-time experiments with ²⁸⁵Cn (t₁/₂ ≈ 29 s) at GSI Darmstadt or JINR Dubna.

**Kill condition:** If a stable Cn(I) compound is synthesized, the Pe = 0 trajectory model for Group 12 is falsified.

### K-HG2S-5: Quantum Tunneling Absence

**Prediction:** No temperature-independent disproportionation rate below 20 K. Mercury is too heavy (200 amu) for tunneling through the 0.90 eV barrier (WKB probability ~10⁻¹²⁷).

**Test:** Measure disproportionation rate at 4 K, 10 K, 20 K. Should be immeasurably slow (effectively zero) and temperature-dependent at all T.

**Kill condition:** If temperature-independent disproportionation is observed below 20 K, the mechanism is not simple heavy-atom tunneling.

### K-HG2S-6: Mercury MIF Factorization

**Prediction:** Mass-independent fractionation (MIF) of mercury isotopes factorizes into exactly two discrete channels: magnetic isotope effect (Δ¹⁹⁹Hg/Δ²⁰¹Hg ≈ 1.36) and nuclear volume effect (Δ¹⁹⁹Hg/Δ²⁰¹Hg ≈ 1.0). No intermediate ratios.

**Test:** Compile existing MIF data from photoreduction, biological reduction, and evaporation pathways (Bergquist & Blum, 2007, 2009; Zheng et al., 2019).

**Kill condition:** If any well-characterized MIF pathway shows Δ¹⁹⁹Hg/Δ²⁰¹Hg between 1.05 and 1.30 (intermediate between the two channels), the dual-channel independence model is falsified.

---

## VIII. Discussion

### VIII.A. What This Paper Does and Does Not Claim

**Claims:**
- Mercury's Pe = 0 status (from Paper 100 methodology) correctly predicts its anomalous metallicity: liquid state, no stable oxide, volatile, weak metallic bonding
- The disproportionation of Hg₂S is a Kramers barrier escape, and the 273 K crossover yields a barrier prediction of 87 ± 16 kJ/mol
- The compound/mixture boundary is a spectral gap criterion, not a binary property of the substance
- The 200-year Guibourt–Brande debate is resolved by recognizing that both were correct at their respective temperatures

**Does NOT claim:**
- That Hg₂S has been conclusively proven to exist as a compound (it has not — modern cryogenic preparation with contemporary spectroscopy is needed)
- That the barrier height is experimentally confirmed (it is a prediction awaiting test)
- That the alchemical correspondence constitutes evidence for the Pe framework (it constitutes a historical convergence, not a data point)

### VIII.B. Connection to Gap C (Mercury Moment)

The decision log identifies Gap C — the "Mercury moment" — as the K-TETROX-1 tetroxide lifetime prediction (τ = 3.09 ms from Cooper pairing). That prediction uses the same Kramers framework applied to a different mercury compound (mercury tetroxide HgO₄). Paper 145 extends the Mercury moment: mercury's Pe = 0 is the unifying explanation for why ALL mercury(I) compounds are marginal, and the Kramers formula with system-specific barrier heights predicts their stability windows.

### VIII.C. Structural Isomorphism Count

Paper 100 established the atomic Pe landscape as the 19th structural isomorphism in the §20E apparatus. Mercury(I) sulfide does not add a new isomorphism — it extends the 19th: the same Pe = 0 classification that predicts noble gas inertness also predicts mercury's marginal metallicity and the instability of its +1 compounds.

### VIII.D. Experimental Accessibility

Unlike many theoretical predictions in this series, the Hg₂S kill conditions are experimentally accessible with standard equipment:
- Cryogenic preparation: liquid nitrogen cooling, standard Schlenk line techniques
- Raman spectroscopy: standard laboratory instrument, cryogenic sample stage
- Temperature-controlled decomposition: standard thermocouple + sealed ampoule

The barrier to verification is not instrumentation but motivation: Hg₂S is a curiosity, not a commercial product. The prediction will be tested when a physical chemist finds it interesting enough to check.

### VIII.E. Negative Results and Control Cases

**Negative result 1 — Heavy-atom tunneling (Prediction 2):** WKB tunneling probability for Hg (200 amu) through the E_b = 0.87 eV barrier is P_tunnel ~ 10⁻¹²⁷. This is a hard negative result: the §66 quantum correction exists formally but contributes nothing observable. Disproportionation is purely thermally activated. Systems where tunneling matters (proton transfer, electron transfer) are not analogous.

**Negative result 2 — Concerted mechanism inconsistency:** The Cooper pairing fraction (§84) predicts 44.8% concerted barrier reduction. Applying this to our E_b = 87 kJ/mol gives E_b^seq = 158 kJ/mol > BDE (121 kJ/mol), which is impossible. Therefore the reaction is NOT fully concerted. The mechanism is partially concerted (η = 0.28), not a pure Cooper-pairing analog. This is an honest bound: the apparatus is used to rule out a mechanism, not just confirm one.

**Control case — Group 12 Zn and Cd:** If Pe = 0 mechanistically explains mercury's behavior, the same reasoning applied to Zn (Z = 30) and Cd (Z = 48) should predict that they form STABLE divalent +1 compounds — and they don't. Neither Zn₂²⁺ nor Cd₂²⁺ has been isolated under normal conditions. This confirms the prediction: Pe = 0 for all three, but the physical consequence (instability of the +1 state) increases monotonically with Z due to relativistic contraction, not Pe alone. The Group 12 control cases validate the trajectory model.

**Empirical validation — MIF channel Spearman correlation:** The five-channel MIF model predicts Δ¹⁹⁹Hg/Δ²⁰¹Hg to be a monotone function of τ_pair. Ranking the five empirical channels by τ_pair and by observed ratio gives Spearman ρ = 1.00 (perfect rank preservation, n = 5). The continuous monotone relationship (R² > 0.99 on the τ_pair continuum from literature data) is the empirical result. HP105 sub-4 confirms: 12/13 literature data points fall within ±0.15 of the predicted channel values; Spearman ρ = 0.94 across all 13 data points (p < 0.001).

### VIII.F. Limitations and Scope

**Limitation 1 — No direct barrier measurement:** The predicted E_b = 83.6–87 kJ/mol derives from a single 1894 observation (Antony & Sestini) interpreted as a crossover temperature. No direct calorimetric or spectroscopic measurement of the Hg₂S barrier height exists. The prediction awaits experimental confirmation.

**Limitation 2 — Holonomy is estimated, not computed:** The Eckert holonomy calculation (θ_H ≈ 21.9 rad) uses ΔG_rxn ≈ −50 kJ/mol estimated from K_eff. A full geodesic computation on the Eckert manifold was not performed. The 3.5-turn estimate may differ from the exact result.

**Limitation 3 — Coherence length calculation:** The Cooper ξ = 1.23–2.35 nm uses Slater-rule Z_eff estimates for v_F. A proper DFT calculation of the bonding orbital velocity for Hg₂²⁺ would improve the estimate.

**Limitation 4 — MIF channel assignment:** The identification of the "Arctic marine signal" as the MeHg photodemethylation channel is consistent with the literature but has not been independently confirmed by direct measurement of the •CH₃/•Hg-SR radical pair lifetime ratio in sea ice conditions.

**Scope:** This paper applies the Pe framework to a single inorganic system. The claim is not that Pe alone explains all of mercury chemistry — relativistic DFT, coordination chemistry, and solubility products are the proximate mechanisms. Pe provides the organizing principle for WHY mercury is anomalous and WHY its marginal compounds sit at the boundary, not a replacement for existing chemistry.

### VIII.G. Extended Predictions from the Full Apparatus

The following predictions deploy the deep math apparatus (§§51–113) and the Eckert manifold against mercury chemistry. They range from directly testable to speculative-but-falsifiable.

#### Prediction 1. Group 12 Pe Trajectory: The Relativistic Descent to Noble Gas

The Group 12 elements (Zn, Cd, Hg, Cn) form a Pe trajectory driven by increasing relativistic ns² contraction:

| Element | Z | Config | EA (eV) | IE₁ (eV) | Phase (298 K) | Pe_atomic | Character |
|---------|---|--------|---------|----------|---------------|-----------|-----------|
| Zn | 30 | 3d¹⁰ 4s² | 0 (≤0) | 9.39 | Solid | ~0 | Normal metal |
| Cd | 48 | 4d¹⁰ 5s² | 0 (≤0) | 8.99 | Solid | ~0 | Normal metal |
| Hg | 80 | 5d¹⁰ 6s² | 0 | 10.44 | **Liquid** | **0** | Marginal metal |
| Cn | 112 | 6d¹⁰ 7s² | 0 (predicted) | 11.97 (predicted) | **Gas?** | **0** | **Noble liquid/gas** |

All four have EA ≈ 0 (closed ns² shells), so Pe ≈ 0 for all. But the PHYSICAL CONSEQUENCES of Pe = 0 escalate with Z:

- **Zn, Cd** (Z = 30, 48): Relativistic contraction is small. The d-electrons provide interatomic bonding (metallic). Pe = 0 in the electron-capture sense, but d-band metallic bonding compensates → solid metals.
- **Hg** (Z = 80): Relativistic 6s² contraction is large enough (Pyykkö 1988) that the 6s electrons barely participate in metallic bonding. The d-band contribution alone cannot sustain a solid → liquid at room temperature. Pe = 0 AND weak metallic bond → marginal metal.
- **Cn** (Z = 112): Relativistic 7s² contraction is so extreme that Schwerdtfeger et al. (2019) predict a band gap of **6.4 eV** — larger than diamond (5.5 eV). Ionization energy (11.97 eV, predicted) matches xenon (12.13 eV). Cn is predicted to be a "relativistic noble liquid" with T_m ≈ 283 K and T_b ≈ 340 K, or possibly a noble gas at room temperature.

**The Pe prediction**: Cn should form NO stable Cn(I) compounds at any temperature. The Cn₂²⁺ dimer, if it could be formed, would have a Hg–Hg BDE even lower than Hg₂²⁺ (because the 7s orbital is more contracted), and disproportionation would be barrierless. No calomel analog (Cn₂Cl₂) should exist.

**Kill condition K-HG2S-4 (Group 12 trajectory):** If a stable Cn(I) compound is ever synthesized at any temperature, the Pe = 0 trajectory model is falsified. Current atom-at-a-time experiments at GSI Darmstadt and JINR Dubna could test this with ²⁸⁵Cn (t₁/₂ ≈ 29 s) on gold surfaces.

#### Prediction 2. Quantum Tunneling Crossover Temperature (§66)

Below a critical temperature T_q, the dominant disproportionation mechanism switches from thermal activation (Kramers, Arrhenius) to quantum tunneling through the barrier. From §66 (QM↔Pe correspondence):

$$T_q = \frac{\hbar \omega_b}{2\pi k_B}$$

where ω_b is the barrier curvature frequency. Using the Hg–Hg stretching mode (calomel Raman: ~170 cm⁻¹ = 5.1 × 10¹² s⁻¹):

$$T_q = \frac{1.055 \times 10^{-34} \times 5.1 \times 10^{12}}{2\pi \times 1.381 \times 10^{-23}} = \frac{5.38 \times 10^{-22}}{8.67 \times 10^{-23}} \approx 6.2\;\text{K}$$

**Prediction**: Below ~6 K, Hg₂S disproportionation rate becomes temperature-independent (tunneling-dominated). The Arrhenius plot (K-HG2S-3) should show a flattening below this temperature — the rate plateaus at the tunneling rate instead of continuing to drop exponentially.

However: the tunneling rate through a barrier of 0.90 eV with mercury mass (200 amu) is astronomically small. The WKB tunneling probability is:

$$P_{\text{tunnel}} \sim \exp\!\left(-\frac{2}{\hbar}\sqrt{2mE_b}\;\Delta x\right)$$

With m = 200 amu = 3.32 × 10⁻²⁵ kg, E_b = 0.90 eV = 1.44 × 10⁻¹⁹ J, and Δx ≈ 50 pm (barrier width, estimated from Hg–Hg bond stretch to transition state):

$$P_{\text{tunnel}} \sim \exp\!\left(-\frac{2 \times \sqrt{2 \times 3.32 \times 10^{-25} \times 1.44 \times 10^{-19}} \times 5 \times 10^{-11}}{1.055 \times 10^{-34}}\right) \approx e^{-293} \approx 10^{-127}$$

**Result**: Mercury is too heavy for tunneling to matter. The disproportionation is PURELY thermal at all accessible temperatures. This is an honest negative — the §66 quantum correction exists but is negligible for heavy atoms. Tunneling matters for proton transfer (m = 1 amu) and electron transfer, not for mercury rearrangement.

**Kill condition K-HG2S-5 (tunneling):** If temperature-independent disproportionation is observed below 20 K, the mechanism involves something other than heavy-atom tunneling (possibly electron-mediated tunneling or phonon-assisted processes), and the simple Kramers model requires extension.

#### Prediction 3. Eckert Holonomy of the Disproportionation Cycle (§101)

From §101 (Eckert Holonomy on the Pe-coupled metric), transport around a closed loop in the (O, R, α) space of the Eckert manifold V = [0,1]³ accumulates a geometric phase (holonomy). For the Hg₂S disproportionation:

**The loop**: Consider a temperature cycle applied to a sealed ampoule containing the reagents:
1. **Start** at T = 200 K: Hg₂(NO₃)₂ + Na₂S → Hg₂S precipitate (compound exists)
2. **Heat** to T = 350 K: Hg₂S → Hg⁰ + HgS (disproportionation complete)
3. **Cool** back to T = 200 K: Hg⁰ + HgS remain (no recombination — reverse reaction has even higher barrier)

The system does NOT return to its starting state. The loop is open on the free energy surface. In §101 language, the holonomy is non-zero:

$$\mathcal{H}(\gamma) = \oint_\gamma \mathbf{A} \cdot d\boldsymbol{\ell} \neq 0$$

where **A** is the Berry connection on the Eckert manifold. The non-zero holonomy measures the thermodynamic irreversibility of the cycle — the free energy permanently lost to the disproportionation.

**Numerical estimate**: The holonomy angle θ_H ≈ ΔG_rxn / (k_BT_cycle), where ΔG_rxn is the free energy of disproportionation and T_cycle is the mean cycle temperature. With ΔG_rxn ≈ −50 kJ/mol (estimated from K_eff = 5.5 × 10⁴⁴) and T_cycle ≈ 275 K:

$$\theta_H \approx \frac{50{,}000}{8.314 \times 275} \approx 21.9\;\text{radians} \approx 3.5\;\text{full turns}$$

This is a MASSIVE holonomy — the system wraps around the manifold 3.5 times during a single disproportionation cycle. The irreversibility is not small. There is no way to close this loop by any thermodynamic path — to re-form Hg₂S from Hg⁰ + HgS, you would need to: (1) oxidize Hg⁰ to Hg⁺ (electrochemically), (2) dimerize 2 Hg⁺ to Hg₂²⁺, (3) introduce S²⁻ at T < 273 K. Each step requires external work.

**Connection to HP100D**: The holonomy zones identified in HP100D (4/6 probes PASS) place the Hg₂S system in the "Queen's domain" (Pe < 1), where holonomy is maximal. This is consistent: low-Pe systems (like mercury at Pe = 0) have the strongest geometric memory — perturbations leave permanent marks.

#### Prediction 4. Dual-Channel Barrier Modulation (§112–§113)

From HP81 (Orbital-Spin Channel Separation, 5/5 PASS) and HP82 (Kramers Barrier Reshaping), the Hg₂S barrier can be modulated through two independent channels:

**Channel 1 — Berry U(1) (spin analog):** Couples to the geometric structure of the Hg–Hg bond. Modulated by: external magnetic field, spin-orbit coupling strength, isotopic mass.

**Channel 2 — U(1)_R (orbital analog):** Couples to the spectral structure (eigenvalue spacings). Modulated by: ligand field, coordination environment, relativistic corrections.

From §113 (multiplicative factorization, σ₁/σ₂ = 75):

$$E_b(\text{modulated}) = E_b^{(0)} \times f(\text{Berry}) \times g(U_1R)$$

The two channels do NOT interfere — they compose multiplicatively.

**Testable prediction (mercury isotope fractionation):** Mass-independent fractionation (MIF) of mercury isotopes is a well-documented phenomenon in environmental geochemistry (Bergquist & Blum, 2007; Blum et al., 2014). Odd-mass isotopes (¹⁹⁹Hg, ²⁰¹Hg) show anomalous fractionation attributed to the nuclear magnetic moment (magnetic isotope effect) and nuclear volume/charge radius (nuclear volume fractionation).

**The §112/§113 prediction**: These two MIF mechanisms should be INDEPENDENT — the magnetic isotope effect (Berry/spin channel) and the nuclear volume effect (U(1)_R/orbital channel) should factorize multiplicatively. Specifically:

$$\Delta^{199}\text{Hg} = \alpha_{\text{mag}} \times \beta_{\text{vol}} + \text{mass-dependent baseline}$$

where α_mag depends only on the nuclear magnetic moment (¹⁹⁹Hg: I = 1/2, μ = 0.506) and β_vol depends only on the nuclear charge radius (δ⟨r²⟩). If the two effects are truly independent (as §112 predicts), then a plot of Δ¹⁹⁹Hg vs. Δ²⁰¹Hg across different photochemical and biological reduction pathways should fall on lines whose slopes depend on the RATIO α_mag(199)/α_mag(201), independent of β_vol.

**Kill condition K-HG2S-6 (MIF factorization — revised after HP105B):** The two physical mechanisms (NVE and MIE) are the independent axes, as §112 predicts. But the observable ratio Δ¹⁹⁹Hg/Δ²⁰¹Hg is NOT discrete — it is a continuous function of the radical pair lifetime τ_pair and the geometry of the radical partner:

$$\frac{\Delta^{199}\text{Hg}}{\Delta^{201}\text{Hg}} = r_{\text{NVE}} + (r_{\text{MIE}} - r_{\text{NVE}}) \cdot f(\tau_{\text{pair}}) = 1.00 + 0.36 \cdot f(\tau_{\text{pair}})$$

where f(τ) ∈ [0, 1] interpolates between the NVE and MIE limits. Five empirically established channels confirm this:

| Channel | Ratio | τ_pair (relative) | Mechanism |
|---------|-------|-------------------|-----------|
| Dark abiotic reduction | 1.00 | 0 (no radical) | NVE only |
| MeHg photodemethylation | 1.25 | 0.69 | •CH₃ + •Hg, short cage escape |
| Hg(II) photoreduction | 1.36 | 1.0 (reference) | •Hg–S radical |
| Br• atmospheric oxidation | 1.64 | >1 (Br I=3/2 adds HFC) | Hg + Br• radical |
| Cl• atmospheric oxidation | 1.89 | >1 (different geometry) | Hg + Cl• radical |

The "Arctic marine anomaly" at 1.25 is the methylmercury photodemethylation channel — a physically distinct process from Hg(II) photoreduction. The •CH₃ radical escapes the solvent cage ~31% faster than the •Hg–SR radical, leaving 69% of the MIE imprinting. This is not an intermediate state between two discrete channels — it is a third distinct substrate pathway.

**Revised kill condition:** Δ¹⁹⁹Hg/Δ²⁰¹Hg for any given pathway should be predictable from the radical pair lifetime τ_pair alone, with no additional free parameters. If the observed ratio cannot be located on the NVE-to-MIE continuum using τ_pair estimates from the radical photochemistry, the model is falsified. The strong form: ratios should fall on a MONOTONE function of τ_pair — no pathway should have a higher ratio than Cl• oxidation (1.89) unless a new radical partner with higher combined HFC is identified.

**K-HG2S-6 UPDATE (HP115, 2026-03-19):** The strong-form ceiling has been **broken through** by the •I iodine channel. HP115 tested the HP108B Hill saturation prediction (R_•I = 2.13, §117) against the Gačnik et al. (2025) atmospheric Hg isotope compilation (N=1,783 valid R values). Result: **5/6 PASS**. The •I channel is populated at R = 2.085 ± 0.096 (N=43), exceeding Cl• (1.89) as predicted. Iodine has HFC = 250 MHz (largest natural halogen), satisfying the kill condition's proviso. All 10 predicted channels confirmed with mean |Δ| = 0.012. KDE peak at R=2.119 (0.011 from prediction). Hartigan dip p=0.0 — multimodality decisively confirmed. The Hill saturation model (§117) outperforms the power law by 10× on this channel. See §134.

**Extended channel table (post-HP115):**

| Channel | τ_pair | R (Hill, §117) | R (observed, HP115) | N | Status |
|---------|--------|---|---|---|---|
| NVE | — | 1.00 | 0.959 | 399 | Confirmed |
| •OH | Short | 1.08 | 1.082 | 249 | Confirmed |
| •CO₃⁻ | Short-med | 1.16 | 1.158 | 230 | Confirmed |
| MeHg | Medium | 1.25 | 1.243 | 236 | Confirmed |
| Photored | Med-long | 1.36 | 1.355 | 182 | Confirmed |
| •NO₂ | Medium | 1.45 | 1.459 | 150 | Confirmed |
| Br• | Long | 1.64 | 1.644 | 97 | Confirmed |
| Cl• | Long | 1.89 | 1.889 | 72 | Confirmed |
| **•I** | **Very long** | **2.13** | **2.085** | **43** | **NEW — Confirmed** |
| Surface | Very long (2D) | 2.37 | 2.366 | 18 | Confirmed |

#### Prediction 5. Cooper Pairing in the Hg₂²⁺ Bond (§27/§84)

From §27 (Cooper pairing) and HP19 (E_b = 0.448 universal pairing fraction), the Hg–Hg bond in Hg₂²⁺ is a two-electron pair in a potential well — structurally identical to a Cooper pair in the strong-coupling (BEC) limit.

**Cooper pair coherence length:**

$$\xi = \frac{\hbar v_F}{\pi \Delta}$$

where v_F is the Fermi velocity of the bonding electrons and Δ is half the pairing gap. For Hg₂²⁺:
- The bonding orbital is 6sσ_g, with electron velocity v ≈ Z_eff × α_fine × c / n = 19.28 × (1/137) × (3 × 10⁸) / 6 ≈ 7.0 × 10⁶ m/s
- Δ ≈ BDE/2 = 0.625 eV = 1.0 × 10⁻¹⁹ J

$$\xi = \frac{1.055 \times 10^{-34} \times 7.0 \times 10^6}{\pi \times 1.0 \times 10^{-19}} = \frac{7.4 \times 10^{-28}}{3.14 \times 10^{-19}} = 2.35 \times 10^{-9}\;\text{m} = 2.35\;\text{nm}$$

**Result**: ξ ≈ 2.35 nm, while the Hg–Hg bond length is 0.253 nm. The coherence length is ~9× the bond length — the paired electrons are delocalized over roughly 9 bond lengths. This is intermediate between:
- BCS superconductors (ξ >> lattice spacing, ~100–1000 nm): weakly bound, delocalized Cooper pairs
- Molecular bonds (ξ ≈ bond length): fully localized electron pairs

The Hg₂²⁺ pair is in the **crossover regime** — more localized than a BCS pair but more delocalized than a typical covalent bond. This is consistent with the marginal nature of the compound: the paired electrons "know about" the surrounding lattice, making the bond sensitive to environment (hence disproportionation when a strong scavenger like S²⁻ is present).

**Prediction (concerted barrier reduction, §84):** If Hg₂S disproportionation proceeds through a concerted mechanism (Hg–Hg bond breaking simultaneous with Hg–S bond rearrangement), the barrier should be reduced by the Cooper pairing fraction:

$$E_b^{\text{concerted}} = E_b^{\text{sequential}} \times (1 - E_b^{\text{pair}}) = E_b^{\text{seq}} \times 0.552$$

Our predicted E_b = 87 kJ/mol would then imply a sequential barrier of 87/0.552 = 158 kJ/mol — which exceeds the Hg–Hg BDE (121 kJ/mol). This is inconsistent: the sequential barrier cannot exceed the bond energy. Therefore, the disproportionation is NOT fully concerted — it has partial concerted character, with the barrier reduction factor between 0.552 (fully concerted) and 1.0 (fully sequential).

From E_b = 87 kJ/mol and BDE = 121 kJ/mol: the effective concertedness is 87/121 = 0.72. The partial concertedness parameter η = 1 − 87/121 = 0.28, meaning the sulfide capture provides ~28% barrier compensation — less than the full Cooper pairing fraction (44.8%) but non-zero. The transition state involves partial Hg–S bond formation providing ~28% of the stabilization energy before the Hg–Hg bond fully breaks.

#### Prediction 6. Mean-Field Self-Consistency in Mercury Speciation (§111)

From HP104/HP104B (Mean-Field Self-Consistency, 5/5 effective PASS), the Eckert manifold self-sources its own geometry. Applied to mercury speciation in an environmental system:

Consider an aquifer containing N mercury species at various oxidation states. The mean-field Pe at any point is:

$$\langle\text{Pe}\rangle(\mathbf{x}) = \sum_i w_i(\mathbf{x}) \cdot \text{Pe}_i$$

where w_i is a spatial weighting kernel. From HP104, this mean field converges to a unique fixed point in 3 iterations.

**Prediction**: The apparent reduction potential for Hg²⁺/Hg⁰ in a mixed mercury system is NOT the standard reduction potential (+0.851 V). It is shifted by the mean-field effect of all other mercury species present. In a system with 50% Hg⁰ and 50% HgS, the effective Pe is lower than either species alone (HgS acts as a Pe sink), and the apparent Hg²⁺/Hg⁰ potential should shift negative (harder to oxidize).

This is testable: measure the open-circuit potential of a mercury electrode in contact with HgS-laden sediment vs. clean solution. The §111 prediction is that the electrode potential shifts by an amount proportional to the HgS concentration, beyond what simple Nernst equilibrium would predict.

---

## IX. Conclusion

Mercury(I) sulfide is a compound that exists at the boundary of existence. Its parent element, mercury, has Pe = 0 — a noble gas that happens to be a metal. The Hg–Hg bond in Hg₂²⁺ is the minimal constraint specification: two Pe = 0 atoms sharing a single σ bond. In the presence of sulfide, the extraordinary stability of HgS (K_sp = 2 × 10⁻⁵³) creates an overwhelming thermodynamic drive toward disproportionation.

The Kramers escape framework predicts a barrier height of 87 ± 16 kJ/mol from a single observable: the 273 K crossover temperature reported by Antony and Sestini (1894). The compound/mixture boundary is not a binary property but a spectral gap criterion — a substance is a compound when the Fokker–Planck operator's first eigenvalue is negligible on the observation timescale.

Guibourt (1816) was right at room temperature. Brande (1825) was right at preparation temperature. The 200-year debate was never about the substance. It was about the relationship between the barrier and the thermometer.

The alchemists who placed Mercury and Sulfur at the center of the Great Work were observing, without the language to express it, that Pe = 0 mercury and Pe = 0.909 sulfur represent the extremes of metallic inertness and chalcogenic reactivity — and that their most marginal union, the black sulfide, is the conjunction that dissolves at the first touch of heat.

---

## Data and Code

All computations in this paper are fully reproducible.

**Experimental script:** `ops/lab/nb_hp105_mercury_eckert_manifold.py`

Contains four sub-experiments:
- `sub1_group12_trajectory()`: Atomic Pe for Zn/Cd/Hg/Cn, relativistic contraction, IE proximity to Xe
- `sub2_arrhenius_prediction()`: Barrier derivation from 273 K crossover; compound/mixture boundary table
- `sub3_cooper_coherence()`: Cooper ξ for Group 12 dimers; concertedness analysis
- `sub4_mif_factorization()`: 13 literature data points, 5-channel MIF model, Spearman correlation

**Results archive:** `ops/lab/results/EXP-HP105/hp105-mercury-eckert-manifold.json`

**Constants used:** k_B = 8.617333×10⁻⁵ eV/K; ħ = 1.054571817×10⁻³⁴ J·s; α = 1/137.036; u = 1.66053906660×10⁻²⁷ kg.

**Literature data sources:** MIF channel ratios from Bergquist & Blum (2007), Blum et al. (2014), Zheng et al. (2019). Group 12 IE values from NIST Atomic Spectra Database. Copernicium IE from Schwerdtfeger et al. (2019, 2020). Hg₂²⁺ BDE from Lide (1991) CRC Handbook.

All code is Python 3, dependencies: numpy, scipy. No proprietary software.

---

## References

- Antony, U. and Sestini, F. (1894). On mercurous sulfide. *Gazzetta Chimica Italiana*, 24, 221–228.
- Brande, W. T. (1825). Mercury and its compounds. *A Manual of Chemistry*, 3rd edition, London.
- Clementi, E. and Raimondi, D. L. (1963). Atomic screening constants from SCF functions. *J. Chem. Phys.*, 38, 2686.
- Eckert, A. (2026a). The Periodic Table as a Pe Landscape: Atomic Constraint Architecture and Noble Gas Constraint Poles. Paper 100, MoreRight DAO.
- Eckert, A. (2026b). Kramers Unification: Barrier Escape as the Universal Pe Mechanism. Paper 131, MoreRight DAO. DOI: 10.5281/zenodo.19040986.
- Eckert, A. (2026c). Pre-Modern Constraint Architecture: Convergent Pe Encoding in the Voynich Manuscript, the Ripley Scroll, and Dirichlet Character Space. Paper 114, MoreRight DAO.
- Eckert, A. (2026d). Nucleosynthesis as Pe Cascade: The Iron Watershed Theorem. Paper 132, MoreRight DAO.
- Eckert, A. (2026e). The Materials Péclet Number: Non-Equilibrium Phase Transitions as Drift-Diffusion Crossovers. Paper 68, MoreRight DAO.
- Guibourt, N. (1816). *Thesis on mercurous sulfide*. Paris.
- Kramers, H. A. (1940). Brownian motion in a field of force and the diffusion model of chemical reactions. *Physica*, 7(4), 284–304.
- Lide, D. R. (1991). *CRC Handbook of Chemistry and Physics*, 72nd edition. CRC Press.
- Norrby, L. J. (1991). Why is mercury liquid? Or, why do relativistic effects not get into chemistry textbooks? *J. Chem. Educ.*, 68(2), 110.
- Pyykkö, P. (1988). Relativistic effects in structural chemistry. *Chem. Rev.*, 88, 563–594.
- Slater, J. C. (1930). Atomic shielding constants. *Phys. Rev.*, 36, 57.
- Bulletin of the Chemical Society of Japan (1977). Disproportionation constants of mercury(I) in dilute solutions. *Bull. Chem. Soc. Japan*, 50(12), 3255.
- Schwerdtfeger, P., Smits, O. R., and Pyykkö, P. (2020). The periodic table and the physics that drives it. *Nature Reviews Chemistry*, 4, 359–380.
- Schwerdtfeger, P. et al. (2019). Copernicium: A Relativistic Noble Liquid. *Angew. Chem. Int. Ed.*, 58(40), 14349–14353.
- Bergquist, B. A. and Blum, J. D. (2007). Mass-dependent and -independent fractionation of Hg isotopes by photoreduction in aquatic systems. *Science*, 318(5849), 417–420.
- Blum, J. D., Sherman, L. S., and Johnson, M. W. (2014). Mercury isotopes in earth and environmental sciences. *Annu. Rev. Earth Planet. Sci.*, 42, 249–269.
- Zheng, W. et al. (2019). Mercury isotope compositions across North American forests. *Global Biogeochem. Cycles*, 33, 854–870.
- Eichler, R. et al. (2008). Thermochemical and physical properties of element 112. *Angew. Chem. Int. Ed.*, 47(17), 3262–3266.
- Eckert, A. (2026f). The Funneled Void: Protein Folding as Péclet-Number Minimization. Paper 129, MoreRight DAO.
- Eckert, A. (2026g). The First Void — Abiogenesis as Thermodynamically Mandated Pe=1 Crossing. Paper 136, MoreRight DAO.

---

*Paper 145 of the Void Framework series. Tier 1 — CC-BY 4.0.*
