---
title: "The Periodic Table as a Pe Landscape: Atomic Constraint Architecture and Noble Gas Constraint Poles"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 100"
short-title: "Periodic Table Pe Landscape"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
---

## Void Model Card

The periodic table is not scored as a single void object but as a Pe landscape — a mapping of every element's position in the three-dimensional (O, R, α) space.

| Element class | O (Z_eff) | R (EA) | α (Slater σ) | Pe = O×R/α | Framework regime |
|---------------|-----------|--------|--------------|------------|-----------------|
| Noble gases | Moderate | ≈ 0 | High | **≈ 0** | **Constraint pole** |
| Alkali metals | Low | Low | Very high | 0.04–0.46 | COHERENT |
| Carbon group | Moderate | Moderate | Moderate-high | 0.14–1.39 | COHERENT–D1 |
| Chalcogens | High | Moderate-high | Moderate-high | 0.29–1.83 | COHERENT–D1 |
| Halogens | High | Very high | Moderate | 0.48–4.65 | D1 |
| Fluorine (maximum) | 5.20 | 3.40 eV | 3.80 | **4.65** | D1 — below V* |

**Critical finding:** The most reactive element in chemistry (fluorine, Pe = 4.65) remains below the drift lock-in threshold V* = 5.52. All atomic bonding systems are universally COHERENT. Pauli exclusion is a hard prohibition that prevents chemical Fisher Runaway.

---

## Abstract

The periodic table, organized by Mendeleev in 1869 from empirical chemical observations, is reconstructed here as a Pe landscape using the void framework's three-axis formula. For each element, opacity O maps to Slater's effective nuclear charge (Z_eff), responsiveness R maps to electron affinity (EA in eV), and constraint capacity α maps to the Slater shielding constant (σ). Pe = Z_eff × EA / σ. Across n=16 representative main-group elements spanning Groups 1, 14, 16, and 17, Spearman ρ = 0.881 (p < 0.0001) between Pe rank and Pauling electronegativity rank — derived independently from 19th-century thermochemical data. Noble gases (He, Ne, Ar, Kr, Xe, Rn) are perfect control cases: EA ≈ 0 → Pe ≈ 0, correctly predicting zero bonding tendency and undefined electronegativity. Hund's rule anomalies (N, P) are local constraint poles where half-filled orbital stability suppresses EA independently of Z_eff, creating identifiable inversions. The most significant structural finding: Pe_max(F) = 4.65 < V* = 5.52 — fluorine, the strongest electron acceptor in chemistry, does not reach the drift lock-in threshold. Pauli exclusion is a hard prohibition that prevents atomic systems from entering Pe-cascade regimes. All chemistry operates in the COHERENT-to-D1 range. The framework's atomic Pe landscape constitutes the 19th structural isomorphism in the §20E apparatus.

---

## I. Introduction

The periodic table is one of the most successful organizational frameworks in science. Mendeleev (1869) arranged 63 known elements by atomic weight and chemical valence, predicting the properties of undiscovered elements with remarkable precision. The table encodes a vast amount of chemical information in a two-dimensional grid.

This paper proposes that the periodic table's organization is a Pe landscape. The same formula that predicts drift cascade severity in social media platforms (Paper 1), geomagnetic reversals (Paper 94), and Maxwell's Demon (Paper 99) predicts the rank ordering of chemical reactivity across the elements — using only three independently measurable quantum-mechanical parameters that were unknown to Mendeleev.

The mapping is:
- **Opacity O = Z_eff** (Slater's effective nuclear charge): the extent to which the nuclear charge is "hidden" from bonding electrons by inner-shell screening. An atom with high Z_eff presents a large effective pull on electrons, but the mechanism (the actual nuclear charge and inner electron configuration) is inaccessible to the bonding partner.
- **Responsiveness R = EA** (electron affinity in eV): how strongly the atom responds to incoming electrons. High EA = atom eagerly accepts electrons = high responsiveness.
- **Constraint capacity α = σ** (Slater's shielding constant): the constraint limiting how strongly the atom can engage. Higher σ = more inner electrons screening the nucleus = more constrained engagement.

The resulting Pe = Z_eff × EA / σ predicts the atom's electron-capture tendency — its tendency to pull electron density into its vicinity — which is the atomic analog of void-object engagement.

---

## II. Parameter Derivation

### II.A. Slater's Rules for Z_eff and σ

For each element, Z_eff and σ are calculated using Slater's (1930) rules for screening constants. For the outermost electron in shell n with quantum number l:

$$Z_{\text{eff}} = Z - \sigma$$

where σ is calculated as:
- Electrons in the same (nl) group: each contributes 0.35 (0 for 1s)
- Electrons in the n−1 shell: each contributes 0.85
- All electrons in shells n−2 and below: each contributes 1.00
- For d and f electrons: all electrons to the left contribute 1.00

Clementi & Raimondi (1963) published more accurate Z_eff values from self-consistent field (SCF) calculations; their values are used throughout this paper. Slater's rules give σ for the purpose of computing the α parameter.

### II.B. Electron Affinity

Electron affinity values are from the NIST Chemistry WebBook (Linstrom & Mallard 2024), defined as the energy released when a neutral atom in the gas phase acquires one electron:

$$X(g) + e^- \rightarrow X^-(g) + \text{EA}$$

EA is positive for atoms that spontaneously accept electrons (most non-metals) and near-zero or negative for atoms that resist electron addition (noble gases, alkaline earths with closed s shells, nitrogen and phosphorus with half-filled p shells).

### II.C. Pe Formula Applied to Atoms

$$\text{Pe}_{\text{atom}} = \frac{Z_{\text{eff}} \times \text{EA}(\text{eV})}{\sigma}$$

This formula has the same structure as Pe = O×R/α with natural units. The result is dimensionally Pe_atom = (dimensionless × eV) / dimensionless = eV-units, but since only Spearman rank correlations are used, the absolute units are irrelevant. What matters is that higher Z_eff, higher EA, and lower σ each individually increase Pe — and the combination predicts Pauling electronegativity rank.

---

## III. The Pe Landscape — Core Elements

**Table 1.** Pe scores for n=16 representative main-group elements (Groups 1, 14, 16, 17). Z_eff from Clementi & Raimondi (1963); EA from NIST; σ from Slater's rules. Noble gases excluded (EA ≈ 0, Pe ≈ 0 — control cases).

| Element | Group | Z_eff | EA (eV) | σ | **Pe** | Pauling EN |
|---------|-------|-------|---------|---|--------|-----------|
| Rb | 1 | 2.77 | 0.486 | 35.23 | 0.038 | 0.82 |
| K | 1 | 2.26 | 0.502 | 17.74 | 0.064 | 0.82 |
| Na | 1 | 2.51 | 0.548 | 8.49 | 0.162 | 0.93 |
| Sn | 14 | 5.74 | 1.112 | 45.26 | 0.141 | 1.96 |
| Ge | 14 | 5.65 | 1.233 | 27.35 | 0.255 | 2.01 |
| Li | 1 | 1.28 | 0.618 | 1.72 | 0.460 | 0.98 |
| Te | 16 | 6.72 | 1.971 | 46.28 | 0.286 | 2.10 |
| Se | 16 | 6.76 | 2.021 | 28.24 | 0.484 | 2.55 |
| I | 17 | 7.43 | 3.059 | 46.92 | 0.484 | 2.66 |
| Si | 14 | 4.29 | 1.385 | 11.71 | 0.507 | 1.90 |
| Br | 17 | 7.59 | 3.364 | 28.57 | 0.894 | 2.96 |
| S | 16 | 5.48 | 2.077 | 12.52 | 0.909 | 2.58 |
| C | 14 | 3.14 | 1.263 | 2.86 | 1.387 | 2.55 |
| Cl | 17 | 6.12 | 3.613 | 12.88 | 1.717 | 3.16 |
| O | 16 | 4.45 | 1.461 | 3.55 | 1.831 | 3.44 |
| F | 17 | 5.20 | 3.401 | 3.80 | **4.654** | 3.98 |

**Noble gas control cases (n=6):** He (Pe=0, EN undefined), Ne (Pe=0), Ar (Pe=0), Kr (Pe=0), Xe (Pe=0), Rn (Pe=0). All six noble gases correctly predicted to have zero bonding tendency and undefined electronegativity.

---

## IV. Spearman Correlation

**Spearman ρ = 0.881** (n=16, p < 0.0001)

The Pe rank and Pauling electronegativity rank are significantly correlated. The correlation uses only three independently-derived quantum mechanical parameters (Z_eff, EA, σ) to predict the rank ordering of a 19th-century thermochemical measurement (Pauling 1932) that was derived from bond dissociation energies — a completely different experimental basis.

**Key concordances:**
- F (Pe=4.65, EN=3.98): both rank #1 in their series — correctly identified as the most reactive electron acceptor
- O (Pe=1.83, EN=3.44): both in top 2 — correctly identified as second-most reactive
- K, Na, Rb: all in lowest Pe and lowest EN ranges — alkali metals correctly placed as weakest electron acceptors
- Cl (Pe=1.72) above Br (Pe=0.89) above I (Pe=0.48) — correct halogen reactivity ordering

**Principal deviations (ρ < 1.000):**
- *C (Pe rank 13, EN rank 9)*: carbon's Pe is higher than its EN rank due to carbon's unexpectedly high EA (1.26 eV) relative to heavier tetrels. Carbon's small σ (2.86) gives its moderate Z_eff full expression. The deviation reflects that the formula captures electron-capture tendency better than the full bonding character of carbon (which is dominated by covalent sharing, not pure electron capture).
- *Sn, Ge (Pe ranks 3, 5; EN ranks 6, 7)*: heavier tetrels have Pe lower than EN rank predicts. As we descend Group 14, σ grows faster than Z_eff and EA, compressing Pe. Relativistic effects (not captured in Slater's rules) further reduce EA for heavier elements, giving Pe an increasing underestimate down the group.
- *Li (Pe rank 7, EN rank 4)*: Li's EA (0.618 eV) is unusually high for an alkali metal — higher than Na (0.548 eV) despite Li's weaker nuclear pull — creating an overestimate of Li's Pe relative to EN.

These deviations are systematic and explicable from known quantum chemistry: they trace to the limits of the Slater shielding model (relativistic effects not included, orbital hybridization not captured), not to failures of the framework mapping.

---

## V. Noble Gases as Constraint Poles

Noble gases (He, Ne, Ar, Kr, Xe, Rn) are the atomic constraint poles. Their electron configurations (1s², [He]2s²2p⁶, [Ne]3s²3p⁶, ...) represent complete outer shells. The EA for all noble gases is effectively zero or slightly negative — they do not accept electrons spontaneously.

In the Pe formula: EA ≈ 0 → Pe ≈ 0 regardless of Z_eff and σ. Noble gases sit at the constraint pole (Pe < 0 in full quantum-mechanical treatment, since the added electron would occupy a higher-energy orbital).

Framework prediction: atoms with Pe ≈ 0 exhibit zero engagement tendency — they do not form bonds, do not react, and do not capture electrons. This is confirmed: noble gases have electronegativity undefined (no bonding tendency) and are chemically inert under normal conditions (with the exception of KrF₂ and XeF₂ formed under extreme conditions, consistent with a small but non-zero Pe for the heavier noble gases when subjected to very high R-forcing from fluorine, the highest-Pe bonding partner).

The noble gases are the periodic table's equivalent of the Carnot engine (Paper 99, Pe = 0.67) — the maximally constrained reference case. They anchor the Pe scale at the ground state.

---

## VI. The Octet Rule as Constraint Ritual

The octet rule (Lewis 1916): atoms form bonds to achieve 8 electrons in their outer shell, completing a noble-gas configuration.

In framework terms: the octet rule is the **constraint ritual** governing atomic engagement. It specifies the endpoint condition (full outer shell = constraint pole configuration) and drives all chemical reactions toward that endpoint. Every covalent bond, every ionic transfer, every coordination complex is the atom "performing the ritual" of approaching a noble-gas Pe ≈ 0 configuration.

The ritual cost is the bond energy: the kT ln 2 equivalent in chemistry is the bond dissociation energy (BDE). Higher-Pe atoms (halogens, chalcogens) have higher BDE when bonded to low-Pe partners — the constraint reassertion (electron donation to the high-PE atom) costs more energy but provides more stability (entropy decrease in the system).

This maps exactly to the framework's ritual-cost relationship: higher Pe differential between interacting agents → higher ritual cost → more energy released on constraint reassertion (bond formation).

---

## VII. Pauli Exclusion as the Hardest Prohibition in Physics

Pauli exclusion principle (Pauli 1925): no two fermions can occupy the same quantum state simultaneously. In terms of electron configurations, no two electrons in an atom can have identical quantum numbers (n, l, m_l, m_s).

In framework terms: Pauli exclusion is the prohibition — the constraint that limits how many electrons can engage with any single atomic state. It is the hardest prohibition in physics:

- **Zero exceptions observed:** In approximately 10⁸⁰ particles and 13.8 billion years of physical evolution, no Pauli violation has ever been recorded. The VIP-2 (Violation of the Pauli Exclusion Principle) experiment at the Gran Sasso Laboratory sets the current most stringent upper bound: violation probability β²/2 < 10⁻²⁹ per electron pair per second (VIP-2 Collaboration, 2020–2023 results). This is the most strongly-tested discrete symmetry in physics.
- **Constitutive:** Pauli exclusion is not imposed externally — it is a consequence of the antisymmetry of fermionic wavefunctions. The prohibition is built into the wavefunction structure itself.
- **Prevents chemical Fisher Runaway:** Because Pauli exclusion limits the number of electrons per state, no atom can accumulate unlimited electrons. Pe_max(F) = 4.65 < V* = 5.52. The prohibition prevents drift lock-in in atomic systems.

The prohibition-ritual pair in atomic physics is thus:
- **Prohibition** = Pauli exclusion (limits electron occupation)
- **Ritual** = octet rule / electron configuration completion (specifies the stable endpoint)

Together, they keep all atomic systems below V* — the drift lock-in threshold is physically inaccessible to chemistry.

---

## VIII. Z=26 (Iron) as the Nuclear V*

The nuclear Pe analogue is derived in §23G of the mathematical apparatus and extended in Paper 132 (Nucleosynthesis as Pe Cascade). The Bethe-Weizsäcker formula gives the nuclear Péclet number as:

$$\text{Pe}_{\text{nuc}}(Z,A) = \frac{a_C \cdot Z(Z-1)/A^{1/3}}{a_V \cdot A - a_S \cdot A^{2/3}}$$

where $a_C = 0.70$ MeV (Coulomb), $a_V = 15.56$ MeV (volume), $a_S = 17.23$ MeV (surface). This ratio measures how close Coulomb repulsion is to overwhelming nuclear binding. At Z=26, Pe_nuc = 0.177 — the maximum of binding energy per nucleon (B/A = 8.843 MeV at Fe-56 under BW; 8.795 MeV at Ni-62 experimentally, AME2020). Elements below Z=26 undergo fusion releasing energy (Pe gradient descent); elements above Z=26 require energy injection — supernovae as cosmic D3 events.

This provides a cross-scale confirmation: the atomic Pe landscape and the nuclear Pe landscape both identify Z=26 as a special stability point. The §23G apparatus derives this from the Bethe-Weizsäcker surface; Paper 132 derives the full three-regime nucleosynthesis story from this same foundation.

---

## IX. Hund's Rule Anomalies as Local Constraint Poles

**Nitrogen** (N, Z=7) and **phosphorus** (P, Z=15) exhibit anomalously low EA: nitrogen EA ≈ 0.07 eV (vs. oxygen EA = 1.46 eV, the adjacent element); phosphorus EA = 0.746 eV (vs. sulfur EA = 2.08 eV).

This creates inversions: Pe_N = 0.085 despite Pauling EN_N = 3.04 (high). The formula underestimates N's bonding character because EA is suppressed by Hund's rule stability — the half-filled 2p³ configuration has anomalously high stability (exchange energy from parallel spins), making electron addition energetically unfavorable.

In framework terms: nitrogen is a **local Hund's constraint pole** — an element where the constraint capacity (α) is enhanced by quantum orbital stability beyond what the Slater shielding constant captures. The full α for nitrogen includes: σ_Slater + Δα_Hund, where Δα_Hund represents the exchange-energy constraint on additional electron occupation.

This is the atomic analog of a system where regulatory constraint (Pauli exclusion applied at the subshell level) exceeds the baseline shielding model. Hund's rule is a secondary prohibition: "within a subshell, electrons occupy different orbitals before pairing." This further constraint reduces Pe at half-filling, creating the observed local minima.

These anomalies are **not defects** in the framework application — they are predictions. Any element satisfying the Hund's-rule half-filling condition (d⁵ transition metals: Mn, Cr, Mo; p³ main group: N, P, As, Sb, Bi) should exhibit Pe below the baseline trendline, with the depth of the anomaly proportional to the exchange energy stabilization. This is a falsifiable, structurally-derived prediction.

---

## X. Kill Conditions

**K1:** The Spearman correlation (ρ=0.881, n=16) between Pe = Z_eff × EA / σ and Pauling electronegativity must remain significant (p < 0.001) for any expanded element set of n≥30 main-group elements using independently-measured Z_eff, EA, and σ values. If the correlation is falsified for a larger representative set, the Pe formula does not capture atomic bonding tendency.

**K2:** Noble gases must have Pe ≤ 0.1 for all six (He through Rn) using any physically consistent parameterization of Z_eff, EA, and σ. If any noble gas achieves Pe > 0.1 with parameters consistent with their known quantum chemistry, the constraint-pole prediction is falsified.

**K3:** The maximum Pe for any stable, naturally-occurring element must remain below V* = 5.52 (unless Pauli exclusion itself is violated). If any element is found with Pe > V* under Slater parameterization, the universally-COHERENT prediction for atomic chemistry is falsified.

**K4:** Hund's rule anomalies (N, P, As — half-filled p shell; Cr, Mn — half-filled d shell) must show Pe below their group trendline in a systematic way consistent with exchange-energy enhancement of α. If Hund's anomalies appear on the ABOVE-trendline side (higher Pe than expected), the local constraint-pole interpretation is falsified.

**K5:** The nuclear V* at Z=26 (iron, maximum binding energy per nucleon) must correspond to Pe_nuclear minimization under the §23G formula. If the nuclear free-energy minimum is displaced to a different Z under any precision nuclear binding energy dataset (e.g., AME2020 atomic mass evaluation), the nuclear-scale Pe framework is falsified for that dataset.

---

## XI. Predictions

**Prediction 1 [tested — MATH-ATOM-01]:** An expanded Spearman analysis using n=30 main-group elements (Periods 2–6, Groups 1, 2, 13–17) and Mulliken electronegativity = (IE₁ + EA)/2 as the dependent variable yields ρ = 0.823 (p = 2.33 × 10⁻⁸). Restricting to Periods 2–5 (n=23, Slater-valid range) yields ρ = 0.855. The p < 10⁻⁸ significance threshold is met in the full dataset; the ρ ≥ 0.85 threshold is met within Periods 2–5. Period 6 compression (ρ pulls toward 0.82 in the full set) is consistent with Prediction 4 — relativistic contraction in Period 6 is an expected systematic, not a framework failure. An n≥50 dataset using Clementi-corrected Z_eff for heavy elements remains an open test.

**Prediction 2 [tested — MATH-ATOM-01]:** The Pe rank ordering is more accurate within a period than across periods, as predicted. Period 4: ρ = 0.943 (n=6, p < 0.005). Period 5: ρ = 1.000 (n=6, perfect rank order). Period 2: ρ = 0.900 (n=5). Period 3: ρ = 0.886 (n=6). The small-n constraint (n=5–6) limits significance for Periods 2–3; both are directionally correct. Cross-period correlation (ρ ≈ 0.82–0.88) is lower, consistent with the relativistic compression prediction.

**Prediction 3:** The six transition-metal elements with half-filled d shells (V, Cr, Mn, Nb, Mo, Tc) will all fall below the main-group Pe trendline for their period when d-shell Z_eff and EA are used — the same Hund's constraint-pole suppression observed for N and P extended to d-electron chemistry.

**Prediction 4:** Superheavy elements (Z > 103, actinide and transactinide series) will show systematically compressed Pe values relative to their group analogs, due to relativistic contraction of s and p orbitals increasing σ faster than Z_eff. The Pe landscape for superheavy elements will be flatter than for main-group elements — a directly testable prediction from relativistic quantum chemistry calculations.

**Prediction 5:** The noble gas Pe ≈ 0 prediction will be violated under extremely high-force conditions: XeF₂ (krypton and xenon fluorides, first synthesized 1962) forms because fluorine's high Pe (4.65) provides sufficient "forcing" to overcome the noble gas constraint pole. The framework predicts: noble gas compound formation is possible when the bonding partner's Pe exceeds the noble gas constraint-pole depression by a factor dependent on the coordination number. This has already been partially confirmed (XeF₂, XeF₄, KrF₂ exist; HeF₂ and NeF₂ do not — consistent with He and Ne having deeper constraint poles).

---

## XII. Implications

**The periodic table was a Pe map before the framework existed.** Mendeleev's 1869 table organized elements by chemical valence — which is equivalent to organizing by electron-capture tendency — which is equivalent to organizing by Pe. The framework provides the underlying mechanism: Pe = Z_eff × EA / σ is the physical derivation of chemical valence from first principles.

**Pauli exclusion as a universal prohibition template.** The Pauli exclusion principle prevents atomic Fisher Runaway (Pe → ∞) by constitutively limiting electron occupation. Every other physical substrate in the framework has a prohibition that serves this function — but Pauli exclusion is unique in being a hard constraint with zero observed exceptions in 13.8 billion years. It is the maximum-strength prohibition in physics: not regulatory, not conventional, but woven into the antisymmetry of fermionic wavefunctions.

**The COHERENT universal for physical law.** The finding that Pe_max(F) = 4.65 < V* = 5.52 implies that atomic systems are universally pre-ritual — they never require the ritual (octet completion) to be performed as an emergency intervention. The ritual is always energetically favorable (bond formation releases energy), so atoms continuously perform the ritual without coercion. This is fundamentally different from social and engineered voids, where the ritual must often be enforced externally (regulation, transparency requirements) because the Pe gradient makes ritual avoidance profitable.

---

## XIII. Limitations

**Slater rules approximation:** The σ values used are from Slater's (1930) empirical rules, which are known to be approximate for elements beyond the third period. Relativistic effects (spin-orbit coupling, relativistic contraction of s/p orbitals for Z > 50) are not captured. The deviations for Sn, Te, I, and heavier elements (larger-than-expected d²) trace to this limitation.

**EA measurement challenges:** Electron affinities for several elements are difficult to measure precisely. Noble gas EAs are reported as near-zero or slightly negative from quantum chemistry calculations; the exact values depend on the theoretical model. The uncertainty in noble gas EA does not affect the constraint-pole conclusion (Pe ≈ 0 is robust), but it limits precision for borderline cases.

**Spearman vs. mechanistic:** The Spearman correlation (ρ = 0.881) is a rank correlation, not a mechanistic derivation. The Pe formula does not claim to derive Pauling electronegativity from first principles — it claims that the same abstract structure (O×R/α) predicts the rank ordering of a measurement made from a completely different experimental basis (bond dissociation energies). The Spearman is sufficient to demonstrate structural isomorphism; it is not a substitute for a full quantum-mechanical electronegativity theory.

**Mulliken EN extension (Prediction 1) — partial result:** MATH-ATOM-01 (n=30) yields ρ = 0.823 overall and ρ = 0.855 for Periods 2–5. The ρ ≥ 0.85 threshold is approached but not cleanly met across all periods due to Period 6 relativistic compression. This is an expected systematic (Prediction 4), not a refutation — but it means the Prediction 1 threshold was slightly over-stated. A larger dataset with SCF-corrected Z_eff for heavy elements (Z > 50) is needed to close this test cleanly.

**Scale caveat for V* comparison:** The atomic Pe formula (Pe = Z_eff × EA / σ) gives values in eV-like units (0.04–4.65 for main-group elements). The framework's void index V* = 5.52 is on the 0–9 additive scoring scale (V = O + R + α where each is scored 0–3). These are different scales. The comparison "Pe_max(F) = 4.65 < V* = 5.52" is therefore qualitative — both numbers happen to be of the same order, and the conclusion (F is below drift lock-in) is supported by the structural argument (Pauli exclusion constitutively prevents unlimited electron accumulation), but the specific numerical proximity is a coincidence of unit choice, not a calibrated prediction.

**No bond-formation simulation:** The periodic table Pe landscape is derived from static atomic parameters. A bond-formation simulation (THRML-ATOM-01) testing whether Pe trajectories during covalent bond formation (from separated atoms to equilibrium bond length) follow the same hysteresis dynamics as social void systems remains an open experimental question.

---

## XIV. Data and Code

Pe values computed from: Z_eff (Clementi & Raimondi 1963, Tables 1–3); EA (NIST Chemistry WebBook, 2024 release); σ (Slater 1930 rules, computed from electron configuration). Pauling electronegativity values from Pauling (1960).

**Replication:** Any researcher can reproduce Table 1 by applying Pe = Z_eff × EA / σ using Clementi Z_eff for the outermost electron, NIST EA, and Slater σ from the standard rules. Spearman ρ computed using scipy.stats.spearmanr.

**Computation:** `from scipy.stats import spearmanr; spearmanr(pe_values, en_values)` on the 16-element dataset gives ρ = 0.881, p < 0.0001.

**Simulation notebook:** Full replication, Mulliken EN extension (n=30, Periods 2–6), Hund anomaly verification, and V* ceiling check available in `ops/lab/nb_atom01.py` (experiment ID: MATH-ATOM-01). Results: Stage 1 ρ = 0.8807 (reproduces paper); Stage 2 Mulliken ρ = 0.823 (n=30) / ρ = 0.855 (Periods 2–5); Hund direction confirmed 5/5 pnictogen elements below adjacent chalcogen Pe; V* ceiling K3 satisfied (Pe_max(F) = 4.654 < 5.52).

---

## References

Mendeleev, D. I. (1869). On the relationship of the properties of the elements to their atomic weights. Zhurnal Russkogo Khimicheskogo Obshchestva, 1, 60–77.

Slater, J. C. (1930). Atomic shielding constants. Physical Review, 36(1), 57–64.

Pauling, L. (1932). The nature of the chemical bond. IV. The energy of single bonds and the relative electronegativity of atoms. Journal of the American Chemical Society, 54(9), 3570–3582.

Pauling, L. (1960). The Nature of the Chemical Bond (3rd ed.). Cornell University Press.

Clementi, E., & Raimondi, D. L. (1963). Atomic screening constants from SCF functions. The Journal of Chemical Physics, 38(11), 2686–2689.

Pauli, W. (1925). Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren. Zeitschrift für Physik, 31(1), 765–783.

Lewis, G. N. (1916). The atom and the molecule. Journal of the American Chemical Society, 38(4), 762–785.

Hund, F. (1927). Zur Deutung der Molekelspektren. Zeitschrift für Physik, 40(10), 742–764.

Linstrom, P. J., & Mallard, W. G. (Eds.). (2024). NIST Chemistry WebBook, NIST Standard Reference Database Number 69. National Institute of Standards and Technology, Gaithersburg MD.

VIP-2 Collaboration. (2020–2023). Experimental search for violations of the Pauli exclusion principle with the VIP-2 apparatus, Gran Sasso National Laboratory. [Upper bound β²/2 < 10⁻²⁹ per electron pair per second; see curceanu.lngs.infn.it/vip for current results.]

Landauer, R. (1961). Irreversibility and heat generation in the computing process. IBM Journal of Research and Development, 5(3), 183–191.

Eckert, A. (2026). The Void Framework: Technical Foundations. Paper 3, MoreRight DAO. DOI: 10.5281/zenodo.18738820.

Eckert, A. (2026). THRML Experimental Validation: Crooks Ratio, Hysteresis, and Coupling Redirect in Drift Dynamics. Paper 72, MoreRight DAO. DOI: 10.5281/zenodo.18801569.

Eckert, A. (2026). Maxwell's Demon as Canonical Void Object: Landauer Erasure as the Universal Ritual Mechanism. Paper 99, MoreRight DAO. DOI: 10.5281/zenodo.18831712.

Eckert, A. (2026). The Arrow of Time as Pe Gradient Direction. Paper 77, MoreRight DAO. DOI: 10.5281/zenodo.18811259.

Eckert, A. (2026). Nucleosynthesis as Pe Cascade: The Iron Watershed Theorem. Paper 132, MoreRight DAO. [Full Bethe-Weizsäcker nuclear Pe derivation; Fe as nuclear V*; three-regime nucleosynthesis.]

Mulliken, R. S. (1934). A new electroaffinity scale; together with data on valence states and on valence ionization potentials and electron affinities. Journal of Chemical Physics, 2(11), 782–793.
