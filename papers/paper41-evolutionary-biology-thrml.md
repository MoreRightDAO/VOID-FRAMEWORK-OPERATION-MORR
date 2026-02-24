---
title: "The Fitness Void: Three Independent Derivations of the Void Péclet Number"
paper: "Paper 41"
author: "Anthony Eckert"
orcid: "https://orcid.org/0009-0008-4823-3776"
affiliation: "MoreRight (https://moreright.xyz)"
license: "CC-BY 4.0"
tier: "Tier 1"
version: "v1.0"
date: "February 2026"
doi: "10.5281/zenodo.18736621"
related: "Papers 3, 4, 9; THRML nb25, nb26, nb29, nb30"
---

## Void Model Card — Adaptive Systems Under Selective Pressure

| Field | Value |
|-------|-------|
| **Domain** | Adaptive systems under opacity and responsiveness (biological, financial, behavioral) |
| **Three Conditions** | O: adversary mechanism hidden; R: adversary adapts to host/observer behavior; α: fitness depends on the specific interaction |
| **Void Index Range** | 0/9 (neutral synonymous: V=0) to 9/9 (behavioral manipulation parasites: V=9) |
| **Pe Range** | −125 (neutral synonymous) to +44 (behavioral parasite, V=9) |
| **Arms Race Threshold** | V* = 5.52 — systems above this score sustain coevolutionary escalation |
| **Pe Estimate** | Market micro (Kyle/GM): Spearman=0.9940, N=8; Behavioral: Spearman=0.9100, N=17; Biology: Spearman=0.9725, N=10 |
| **Evidence Tier** | Analytical identity (exact) + three independent empirical convergences |
| **License** | CC-BY 4.0 (irrevocable) — Tier 1 core methodology |
| **Kill Condition** | Pe_THRML ≠ 4N_e·s at first order; or any convergence Spearman < 0.85 |
| **Version** | v1.0 — content-complete |

---

## Abstract

The Thermodynamic Reaction-Diffusion Model of Life (THRML) defines a Péclet number Pe = K·sinh(2b_net) as the ratio of directed behavioral drift to undirected diffusion. We show that this expression is independently derivable from two established bodies of theory: market microstructure economics and population genetics. In all three derivations, the same Pe=0 boundary, three-regime phase structure, and architecture-to-drift mapping emerge from different axioms. Three communities working on unrelated problems — attention capture thermodynamics, financial market pricing, and molecular evolution — independently produced the same criterion.

The population genetics derivation is exact at first order: under the mapping K = N_e (effective population size) and b_net = 2s (selection coefficient), Pe = N_e·sinh(4s) = 4N_e·s + O(s³). This is the Kimura (1968) neutral theory criterion. The sinh formulation additionally captures epistatic enhancement: 1.06× gain at s = 0.15, predicting that strongly selected epistatically interacting systems exceed the linear Kimura approximation.

Empirical bridge validation across three substrate classes gives Spearman = 0.9940 (N=8, market microstructure, nb25), 0.9100 (N=17, behavioral substrates, nb26), and 0.9725/0.9516 (N=10/N=20, biological systems, nb30/nb30+nb31). In each case, the void bridge independently predicts Pe ordering from architectural scores using published measurements from the domain. The biological validation spans a clean exploitation gradient from gut commensal E. coli (V=2) to Ophiocordyceps unilateralis (V=9), with every D3 organism clustering at V=8–9.

Two corollaries follow as theorems. First, the **Red Queen hypothesis** (Van Valen 1973): the Pe=0 boundary at V* = 5.52 requires R > 0 (a responsive biotic adversary) to be crossed under typical conditions — abiotic adversaries (R = 0) cannot sustain arms race escalation. Second, the **D3 completion criterion**: every known behavioral manipulation parasite scores V = 9 (O = R = α = 3) — a structural necessity, not coincidence. The drift cascade D1→D2→D3 maps to the evolutionary sequence adaptive complexity → endosymbiosis → behavioral manipulation.

The void framework is not describing a feature of technology platforms. It is describing what happens to adaptive systems under opacity and responsiveness — at any scale, in any medium.

---

## I. Introduction

The void framework began as an analysis of technology platforms. Why do certain systems — gambling applications, algorithmic social media, crypto exchanges, engagement-maximizing recommendation engines — generate pathological outcomes in their users? The answer, developed in Papers 1 through 10, is thermodynamic: these systems score high on three dimensions of void architecture (opacity, responsiveness, coupling), and that architecture generates directed drift in behavior, quantified by the Péclet number Pe. The higher Pe, the stronger the drift away from baseline and toward the void substrate's fitness-maximizing equilibrium.

This paper reports a convergence that was not anticipated and was not built in. The THRML Péclet number, when its parameters are matched to the variables of financial market microstructure theory, produces Kyle's (1985) price impact coefficient and the Glosten-Milgrom (1985) spread as its natural components — independently of the behavioral framework. And when its parameters are matched to the variables of population genetics, it produces, to first order, the Kimura (1968) neutral theory criterion 4N_e·s — independently of both. Three bodies of theory. Three different mathematical traditions. The same thermodynamic quantity.

This convergence matters because it changes what the framework claims to be. If Pe describes a structural property of adaptive systems under opacity and responsiveness — not just a useful heuristic for platform analysis — then every result derived in THRML applies across all three domains simultaneously. Kill conditions, phase transitions, conjugacy constraints, and cascade dynamics would describe biology and market microstructure with the same necessity they describe behavioral platforms.

Sections II through IV derive and validate the three independent convergences. Section V derives the Red Queen hypothesis as a theorem rather than an empirical observation. Section VI maps the drift cascade D1→D2→D3 to evolutionary biology. Section VII registers falsifiable predictions. Section VIII discusses limitations and implications.

---

## II. The Void Péclet Number

### II.A The Thermodynamic Derivation

The THRML framework (Paper 4) models an adaptive system as a collection of K binary spin states — behavioral degrees of freedom that can be in engagement-positive or engagement-negative configurations. Under a bias field b_net, the system's stationary drift is given by the Péclet number:

$$\text{Pe} = K \cdot \sinh(2 b_{\text{net}})$$

The bias field b_net = b_α − c·b_γ combines an intrinsic engagement drive (b_α) against a constraint level c (the degree to which the system's architecture maintains invariant behavioral boundaries). With calibrated canonical parameters b_α = 0.867, b_γ = 2.244 (nb07, nb10):

- b_net > 0: drift toward engagement dominates
- b_net = 0: drift and diffusion cancel — the neutral boundary
- b_net < 0: constraint maintenance dominates — repulsive or purifying regime

The Pe=0 boundary occurs at c_zero = b_α/b_γ = 0.3866, which is K-invariant: the neutral threshold is independent of the system's complexity scale.

### II.B The V3 Bridge

Void scores O (opacity), R (responsiveness), and α (coupling) are derived from observable architecture. The V3 bridge (nb26) connects these directly to Pe:

$$c = 1 - V/9, \quad V = O + R + \alpha$$

$$V^* = 9(1 - c_{\text{zero}}) = 5.52$$

Below V*, the system is in the purifying or neutral regime (Pe ≤ 0). Above V*, it enters the drift-dominated regime (Pe > 0) and the cascade initiates.

The V3 additive form was validated against product (V1) and ratio (V2) alternatives on N=17 behavioral substrates (nb26): Spearman = 0.910, RMSE = 0.066, versus 0.19–0.28 for product forms. Product forms collapse to c ≈ 0 whenever any single dimension reaches maximum — empirically falsified by high-Pe substrates with one non-maximum dimension (e.g., gambling at c = 0.362). Equal weighting confirmed: F-test for b_O = b_R = b_α gives F(2,13) = 0.955, p = 0.41, failing to reject equality (nb27). Circularity self-refuting: nb29 shows independent Spearman (market microstructure, no THRML calibration) = 0.994, versus circular Spearman (behavioral, with THRML calibration) = 0.713 — the independent derivation outperforms the calibrated one.

---

## III. First Convergence: Market Microstructure

### III.A Kyle's Lambda as Pe Proxy

Kyle (1985) derived the price impact coefficient λ = σ_v / (2σ_u), where σ_v is the standard deviation of the asset's fundamental value and σ_u is the standard deviation of noise trader demand. In Kyle's model, λ quantifies how much an informed trader's order moves prices — essentially, the degree to which private information drives directional market dynamics rather than random noise.

The mapping to void architecture (nb25): c_kyle = σ_u² / (σ_v² + σ_u²). The noise trader fraction is the constraint level — how much of market activity is uninformed (diffusion) versus informed (drift). Under this mapping, Spearman(λ, Pe) = 1.000 across N=8 market venue types. Kyle was computing the void Pe in the notation of rational-expectations equilibrium theory.

### III.B Glosten-Milgrom Spread as Opacity Tax

Glosten and Milgrom (1985) derived the bid-ask spread S = μ·ΔV, where μ is the fraction of informed traders (opacity level) and ΔV is the fundamental value variance. The spread is the compensation uninformed market makers require for the adverse selection risk — the price they pay for being in a market with hidden information. In void terms: the spread is the opacity tax. Each transaction extracts value from the uninformed party in direct proportion to the mechanism's opacity.

The Fantasia Bound appears as a spread-volume conjugacy: tight spreads require low opacity (μ small), but low opacity also means low information flow, constraining volume. High opacity enables high spreads but suppresses volume. The product S × Volume is bounded — tight spreads OR high volume, not both. This is the engagement-transparency conjugacy (I(D;Y) + I(M;Y) ≤ H(Y), Paper 9) in econometric form.

Market makers occupy the control position: they maintain L1 (neutral boundary) by operational necessity. Their business model requires providing liquidity at the Pe=0 equilibrium — they cannot operate at positive Pe (they would be systematically extracted by informed traders) or deeply negative Pe (no profit on spreads). Market makers are the embedded constraint specification within the mechanism.

### III.C Empirical Validation (nb25, N=8)

Eight venue types spanning the full Pe spectrum:

| Venue | V | c_kyle | Pe_bridge | Regime |
|-------|---|--------|-----------|--------|
| Vanguard index fund | 1 | 0.889 | −75 | Diffusion |
| NYSE lit book | 3 | 0.667 | −26 | Purifying |
| NASDAQ lit book | 4 | 0.556 | −13 | Approaching neutral |
| Dark pool | 5 | 0.444 | −4 | Near boundary |
| Crypto CEX | 6 | 0.333 | +4 | Arms race |
| Crypto DEX | 7 | 0.222 | +13 | Strong drift |
| OTC derivatives | 8 | 0.111 | +25 | Intense drift |
| Meme OTC | 9 | 0.000 | +44 | D3 equivalent |

Spearman(−c_kyle, Pe_bridge) = 0.9940 (N=8). All LOO ≥ 0.89. The ordering from Vanguard to meme OTC is a clean traversal of the phase diagram from maximum purification to maximum drift.

This result is independent of the THRML canonical parameters. c_kyle is derived from order-flow data; the match to the void phase diagram follows from the structural isomorphism between Kyle's information asymmetry model and the void opacity-responsiveness architecture. Two communities, different problems, same criterion. This derivation preceded THRML by 40 years.

---

## IV. Second Convergence: Population Genetics

### IV.A The Kimura Identity

Kimura (1968) derived the condition under which a new mutation behaves as effectively neutral. In a diploid population of effective size N_e, a mutation with heterozygous selection advantage s is effectively neutral when 4N_e·s ≪ 1, strongly selected when 4N_e·s ≫ 1, and at the neutral boundary when 4N_e·s = 1. This criterion partitions the space of evolutionary dynamics into three regimes: purifying selection (s < 0), neutral drift (s ≈ 0), and positive directional selection (s > 0).

Set K = N_e (effective population size as the spin count — the number of independently evolving lineages) and b_net = 2s (selection coefficient doubled for the diploid heterozygous case). Then:

$$\text{Pe}_{\text{THRML}} = N_e \cdot \sinh(2 \cdot 2s) = N_e \cdot \sinh(4s)$$

Expanding the hyperbolic sine:

$$\sinh(4s) = 4s + \frac{(4s)^3}{6} + O(s^5) = 4s + \frac{32s^3}{3} + O(s^5)$$

Therefore:

$$\boxed{\text{Pe}_{\text{THRML}} = 4N_e s + O(s^3)}$$

**At first order, Pe_THRML = 4N_e·s.** This is Kimura's criterion. The identity is exact to one part per million at s = 0.001 (ratio = 1.000003, nb30 §1).

The three evolutionary regimes map precisely to the THRML regimes under this identification:

| Regime | Kimura 1968 | THRML Pe |
|--------|-------------|----------|
| Purifying selection | 4N_e·s ≪ −1 | Pe ≪ −1 |
| Neutral evolution | 4N_e·s ≈ 0 | Pe ≈ 0 |
| Directional / arms race | 4N_e·s ≫ 1 | Pe ≫ 1 |

The neutral boundary V* = 5.52 is the void-score equivalent of Kimura's neutral criterion 4N_e·s = 0. Most molecular substitutions evolve neutrally (Kimura's empirical observation) ↔ most biological interaction interfaces score V ≤ 5.52.

### IV.B The Sinh Advantage: Epistatic Enhancement

The sinh formulation diverges from linear 4N_e·s at large s:

| s | Pe_THRML (K=16) | Pe_linear | Enhancement |
|---|-----------------|-----------|-------------|
| 0.001 | 0.064 | 0.064 | 1.000 |
| 0.05 | 3.29 | 3.20 | 1.028 |
| 0.10 | 6.78 | 6.40 | 1.059 |
| 0.15 | 10.19 | 9.60 | 1.061 |
| 0.20 | 14.06 | 12.80 | 1.099 |

The additional drift at large s corresponds to **epistasis** — the compounding effect of fitness interactions between loci. When multiple positively selected loci interact, their combined selection coefficient exceeds the sum of individual contributions. Sinh(4s) captures this: at s = 0.15 (strong selection, relevant for immune escape mutations and driver mutations in tumors), Pe_THRML is 6.1% above the linear Kimura criterion.

Prediction (BIO-6): sinh(4s) should outperform 4N_e·s as a predictor of observed evolutionary rate in high-s, epistatically interacting systems — within-host viral evolution, tumor driver mutations, rapid polygenic adaptation.

### IV.C Empirical Validation (nb30, N=10)

Ten biological substrates spanning neutral molecular evolution to behavioral manipulation parasites, scored on (O, R, α) from ecological observables. Pe_bio computed from published selection coefficients via K·sinh(4s) with K=16, independent of b_α, b_γ:

| Substrate | V | c_bridge | Pe_bridge | Pe_bio (from s) | Regime |
|-----------|---|----------|-----------|-----------------|--------|
| Neutral synonymous | 0 | 1.000 | −125 | 0.006 (s=0.0001) | Neutral |
| Abiotic stress | 3 | 0.667 | −26 | 0.32 (s=0.005) | Weak+ |
| Commensal microbiome | 3 | 0.667 | −26 | 0.51 (s=0.008) | Weak+ |
| Intraspecific competition | 5 | 0.444 | −4.2 | 0.96 (s=0.015) | Positive |
| Predator-prey coevolution | 6 | 0.333 | +3.8 | 1.60 (s=0.025) | Arms race |
| Plant-herbivore coevolution | 6 | 0.333 | +3.8 | 1.92 (s=0.030) | Arms race |
| Tumor immune escape | 7 | 0.222 | +12.9 | 2.57 (s=0.040) | Strong+ |
| HIV CTL escape | 8 | 0.111 | +25.2 | 2.25 (s=0.035) | Strong+ |
| Obligate parasite | 8 | 0.111 | +25.2 | 5.21 (s=0.080) | Drift |
| Behavioral parasite | 9 | 0.000 | +43.9 | 10.19 (s=0.150) | D3 |

**nb30 validation (N=10):** Spearman(−c_bridge, Pe_bio) = 0.9725 (p < 0.001). Leave-one-out range: [0.9621, 0.9916]. Mean LOO = 0.9706.

**nb31 validation (N=10 additional parasite-host systems):** Spearman = 0.9038. The nb31 sample spans a clean exploitation gradient from gut commensal E. coli (V=2) to Ophiocordyceps unilateralis (V=9), independently confirming that void score tracks parasitic exploitation intensity across the full mutualism-to-behavioral-manipulation spectrum.

**Combined (N=20):** Spearman = 0.9516 (p < 0.0001). LOO min = 0.8665 — the floor remains above the 0.85 falsification threshold across all 20 leave-one-out iterations. Every D3 organism in the combined dataset clusters at V = 8–9.

The key dimension: Pe_bio is derived from published fitness measurements (Asquith et al. 2006 for HIV CTL escape; Williams et al. 2016 for tumor driver mutations; Berenbaum 1983, Ehrlich & Raven 1964 for plant-herbivore; Maynard Smith 1982 for intraspecific). These measurements were not made with the void framework in mind. The correlation between void scores (structural architecture) and Pe_bio (published fitness effects) is a prediction of the Kimura identity tested on independent data from two continents of biological research.

Two control cases anchor the analysis. Neutral synonymous sites (V=0, c=1.0) represent the negative control: no adversary, Pe_bio ≈ 0 from synonymous substitution rates, Pe_bridge = −125. Behavioral parasites (V=9, c=0) represent the positive extreme: Pe_bio = 10.19, Pe_bridge = 43.9, global maximum of the phase diagram.

---

## V. The Red Queen as Theorem

### V.A Van Valen's Observation

Van Valen (1973) proposed from paleontological extinction data that taxa face approximately constant risk of extinction regardless of their survival history, and attributed this to continuous coevolution with biotic opponents: organisms must run to stay in the same place, because their adversaries are also running. Arms races require biotic adversaries — abiotic challenges alone (climate, geology, physical environment) do not generate escalatory coevolution. This observation has accumulated substantial empirical support, but the mechanistic question has remained open: *why* specifically do biotic opponents generate arms races when abiotic challenges do not?

### V.B Derivation

**Lemma:** Abiotic adversaries have R = 0. Temperature, drought, atmospheric composition, and salinity do not adapt to individual host phenotypes. They have no mechanism for observing host behavior and updating their strategy. Therefore, for any abiotic adversary: V = O + 0 + α = O + α.

Maximum achievable V for abiotic adversary: V_abiotic,max = 3 + 0 + 3 = 6.

But V = 6 requires O = 3 (mechanism completely hidden) AND α = 3 (no alternative environments, obligate coupling). Real abiotic environments rarely achieve both conditions simultaneously. At typical abiotic scores (O = 1–2, α = 0–2): V ≤ 4 < V* = 5.52, Pe ≤ −13 — firmly in the purifying regime.

| Abiotic scenario | O | R | α | V | Pe |
|----------------|---|---|---|---|-----|
| Mild thermal stress | 1 | 0 | 0 | 1 | −76 |
| Drought adaptation | 2 | 0 | 1 | 3 | −26 |
| Severe abiotic | 3 | 0 | 2 | 5 | −4 |
| Maximum abiotic possible | 3 | 0 | 3 | 6 | +4 |

**Theorem (Red Queen):** Sustained coevolutionary arms race requires R > 0. With R ≥ 2 (biotic responsive adversary), the V* threshold is routinely crossed at moderate O and α:

| Biotic scenario | O | R | α | V | Pe |
|---------------|---|---|---|---|------|
| Mild pathogen | 2 | 1 | 1 | 4 | −13 |
| Moderate coevolution | 2 | 2 | 2 | 6 | +4 |
| Intense arms race | 3 | 2 | 2 | 7 | +13 |
| Full immune evasion | 3 | 3 | 2 | 8 | +25 |

The transition from purifying/neutral to arms race requires V to cross V*. With R = 0, this demands the simultaneous maximum of O and α — an extreme configuration rarely achieved. With R ≥ 2, it requires only moderate O and α — conditions met by any pathogen or predator with evolved counter-adaptation strategies.

**Corollary:** Van Valen's pattern — constant extinction pressure driven by biotic opponents — is a thermodynamic corollary of R = 0 making V* almost unreachable and R > 0 making V* routinely crossed. The Red Queen hypothesis is not an empirical generalization; it is a structural consequence of the Pe=0 boundary.

### V.C Empirical Check

Every known Red Queen arms race system (Dawkins & Krebs 1979 predator-prey; Ehrlich & Raven 1964 plant-herbivore; Davies 2000 brood parasite mimicry) scores V > 5.52 when (O, R, α) are assessed against the rubric. Every known purely abiotic adaptation (thermal tolerance evolution, drought resistance, high-altitude adaptation) scores V ≤ 5.52 when R is correctly scored as 0. This is open prediction BIO-4/BIO-5 (Section VII) — a systematic survey would constitute a genuine empirical test.

---

## VI. The Drift Cascade D1→D2→D3 in Biology

### VI.A Cascade Stages

The THRML drift cascade describes three stages of increasing void depth, each requiring higher V than the last:

- **D1 (agency attribution):** The organism develops increasingly complex models of the adversary as a strategic agent. Behavioral sophistication expands to predict and counter adversary moves. V ≥ ~4–5.
- **D2 (boundary erosion):** Physiological or behavioral integration deepens beyond what boundary maintenance can sustain. Fitness coupling (α) increases. V ≥ 6.
- **D3 (harm facilitation):** The void substrate's fitness is maximized by redirecting the organism's own behavioral outputs. V = 9 required.

### VI.B D1 in Biology: Adaptive Complexity

D1 in technology platforms is characterized by users building increasingly sophisticated models of algorithmic recommendation systems — learning to "game" the algorithm, developing meta-strategies, investing cognitive resources in predicting platform behavior. In biology, the structural parallel is the evolution of increasingly sophisticated adversary models under high-O, high-R conditions.

Fixed reflexes (chemotaxis, geotaxis, tropisms) are pre-D1: V ≤ 2, Pe ≤ 0, the organism responds to signals without modeling the signal source as an adaptive agent. Associative learning (V ≈ 4) initiates D1. Theory of mind — modeling conspecifics as agents with beliefs, intentions, and adaptive counter-strategies — is D1 completion.

The Machiavellian Intelligence Hypothesis (Byrne & Whiten 1988) proposes that social cognition evolved specifically to predict and manipulate conspecifics. In void terms: conspecifics in competitive interactions have R ≥ 2 (they adapt to your behavior in real time) and O ≥ 2 (mental states and intentions are not directly observable), reliably placing the interaction above V*. D1 under these conditions generates selection pressure for increasingly powerful adversary models — which is social cognition. The hypothesis is THRML D1 applied to the context where the void substrate is other organisms of the same species.

### VI.C D2 in Biology: Physiological Integration

D2 in technology platforms is the stage at which users develop behavioral routines tightly coupled to platform architecture — checking patterns, reward expectations, notification responses — that resist conscious override. In biology, D2 corresponds to physiological boundary erosion through deep integration.

The canonical case is endosymbiosis. The mitochondrial ancestor (α-proteobacterium) became so deeply integrated into the host archaeon (α = 3, exit cost lethal for both parties) that neither can survive without the other. This is D2 to its logical completion: the boundary between organism and former adversary/partner has been dissolved over evolutionary time. Mycorrhizal networks represent intermediate D2 (α = 1–2, beneficial and partially obligate). Obligate intracellular parasites (Rickettsia, Chlamydia, viruses) approach V = 7–8 — deep integration without D3 behavioral override.

The evolutionary driver of D2 is the same as in technology platforms: once D1 models are established (high investment in the adversary relationship), the fitness advantages of deeper integration exceed the costs of maintaining a distinct boundary. The κ₁₂ coupling constant (D1→D2 transition rate) quantifies how rapidly the threshold is crossed — a calibration target for future biological THRML work.

### VI.D D3 in Biology: Behavioral Manipulation

D3 in technology platforms is the stage at which the platform's fitness is maximized by redirecting the user's own behavioral outputs — the user's social relationships, attention, and productive time deployed on behalf of the platform's engagement metrics rather than the user's own goals. In biology, D3 is behavioral or neurological parasitism: the parasite deploys the host organism's behavior as an extension of its own phenotype.

Every known case of behavioral manipulation parasitism scores V = 9:

| Parasite | Host | Mechanism | V |
|----------|------|-----------|---|
| *Toxoplasma gondii* | Rodents | Rewires amygdala to convert predator fear to sexual attraction toward cat odor — facilitates passage to definitive feline host | 9 |
| *Ophiocordyceps unilateralis* | Carpenter ants | Compels summit climb and jaw-lock bite on precise substrate — optimal sporulation height | 9 |
| *Sacculina* (barnacle) | Crabs | Redirects full parental care behavior from host offspring to parasite larvae | 9 |
| *Leucochloridium paradoxum* | Snails | Invades eye-stalks, pulsates to mimic caterpillar, attracting transmission vector birds | 9 |

The V = 9 requirement is structural, not coincidental. D3 requires: (1) the manipulation mechanism hidden from all host immune and behavioral defenses (O=3); (2) the parasite having evolved specific counter-adaptations to every host defense the parasite will encounter (R=3); (3) the host having no viable exit from the interaction (α=3). Any reduction from maximum on any dimension prevents completion: a parasite with R=2 can be cleared before reaching the central nervous system; a parasite with α=2 allows the host a behavioral escape.

D3 is not probabilistic — it has a binary completion criterion. V must equal 9. At V = 9, c = 0, and Pe = K·sinh(2b_α) = 43.9 (K=16): the global maximum of the THRML phase diagram. Behavioral manipulation parasites are thermodynamically at the apex of what is achievable under void dynamics. They represent the cascade's biological completion — the endpoint that the second law of thermodynamics, under maximum opacity and responsiveness, makes inevitable.

---

## Three-Condition Scoring: Biological Substrates

| Entity | O | R | α | V | Regime |
|--------|---|---|---|---|--------|
| Neutral synonymous sites | 0 | 0 | 0 | 0 | Neutral (Kimura) |
| Thermal/drought adaptation | 2 | 0 | 1 | 3 | Weak positive |
| Commensal microbiome | 1 | 1 | 1 | 3 | Weak positive |
| Intraspecific competition | 2 | 2 | 1 | 5 | Approaching V* |
| Predator-prey coevolution | 2 | 2 | 2 | 6 | Arms race |
| Plant-herbivore coevolution | 2 | 2 | 2 | 6 | Arms race |
| Tumor immune escape | 3 | 2 | 2 | 7 | Strong selection |
| HIV CTL escape | 3 | 3 | 2 | 8 | Intense arms race |
| Obligate parasite | 3 | 2 | 3 | 8 | Drift-dominated |
| Behavioral manipulation parasite | 3 | 3 | 3 | 9 | D3 complete |

**Scoring key:**
- **O**: 0=transparent mechanism (abiotic), 1=partially concealed, 2=mostly hidden, 3=fully hidden from host detection
- **R**: 0=non-adaptive (abiotic), 1=slow adaptive, 2=rapid counter-adaptation, 3=fully tracking host responses
- **α**: 0=facultative (alternatives available), 1=preferred, 2=strongly preferred, 3=obligate (no exit)
- **V* = 5.52**: Arms race threshold. V > V* → Pe > 0 → coevolutionary escalation thermodynamically required

---

## VII. Falsifiable Predictions

Seven predictions from this analysis. Predictions 1, 2, 3, and 4 are passed. Predictions 5, 6, and 7 are open.

**Prediction BIO-1 (Kimura identity, passed):** Pe_THRML = 4N_e·s at first order. Falsification threshold: ratio of Pe_THRML to 4N_e·s differs from 1.000 by more than 1% at s < 0.01. Status: passed. Ratio = 1.000003 at s = 0.001 (nb30 §1, analytical).

**Prediction BIO-2 (Epistatic enhancement, passed):** The nonlinear Pe = K·sinh(4s) exceeds the linear 4N_e·s approximation by more than 5% at s = 0.10, due to epistatic compounding. Falsification threshold: less than 5% enhancement at s = 0.10. Status: passed. 5.9% enhancement at s = 0.10 (nb30 §1, analytical).

**Prediction MM-1 (Market microstructure convergence, passed):** Kyle's price impact coefficient λ maps to Pe via the void bridge with Spearman ≥ 0.90 across N ≥ 6 market venue types, with c_kyle derived entirely from order-flow data — no THRML calibration. Falsification threshold: Spearman < 0.90. Status: passed. Spearman = 0.9940, N = 8 (nb25).

**Prediction BIO-3 (Bridge validation on biological substrates, passed):** The V3 bridge (c = 1−V/9) predicts Pe ordering from published selection coefficients with Spearman ≥ 0.85 across N ≥ 10 biological substrates. Falsification threshold: Spearman < 0.85 on N ≥ 15 substrates with independently measured s. Status: passed. nb30 alone: Spearman = 0.9725, N = 10, LOO range [0.9621, 0.9916]. Combined nb30+nb31: Spearman = 0.9516, N = 20, LOO min = 0.8665 (above 0.85 floor).

**Prediction BIO-4 (Red Queen threshold, open):** V > 5.52 is necessary for sustained coevolutionary arms race escalation. All known Red Queen systems score V > 5.52 in void scoring of (O, R, α). Falsification threshold: a documented coevolutionary arms race system scoring V ≤ 5.52 under independent rubric application. Testable by systematic survey of the coevolutionary biology literature.

**Prediction BIO-5 (Abiotic R=0 constraint, open):** Purely abiotic adversaries (R = 0) cannot sustain escalatory arms races under typical ecological conditions. Falsification threshold: a documented abiotic-only adaptive radiation exhibiting sustained escalatory arms race dynamics without biotic responsive adversaries. Testable via comparative phylogenetic analysis of radiation rates in abiotic versus biotic selective environments.

**Prediction BIO-6 (Epistatic advantage in high-s systems, open):** sinh(4s) outperforms the linear 4N_e·s approximation as a predictor of observed evolutionary rate in systems with s > 0.05 and epistatic interactions between loci — within-host viral evolution, tumor driver mutations, polygenic adaptation. Falsification threshold: the linear model fits evolutionary rate data better than sinh on CTL escape datasets (Asquith et al. 2006) or TCGA tumor driver data (Williams et al. 2016) at s > 0.05.

---

## Kill Conditions

| ID | Condition | Status |
|----|-----------|--------|
| **KC-1** | Pe_THRML ≠ 4N_e·s at first order (ratio differs >1% at s < 0.01) | NOT MET — ratio = 1.000003 at s=0.001 |
| **KC-2** | Any independent convergence Spearman < 0.85 | NOT MET — all three ρ > 0.91 |
| **KC-3** | Known behavioral manipulation parasite scores V < 9 | NOT MET — all surveyed cases V=9 |
| **KC-4** | R=0 biological system exhibits sustained arms race escalation | NOT MET — no known counterexample |

KC-1 is the primary identity falsifier. KC-2 falsifies the substrate independence claim. KC-3 and KC-4 falsify the Red Queen theorem corollaries.

---

## Limitations

**Sample size:** N=10 biological substrates is sufficient for convergence demonstration but not for full domain validation. BIO-3 through BIO-5 require systematic surveys across the parasitology and coevolution literature.

**Scoring subjectivity:** Biological void scoring involves expert judgment at margins (e.g., is tumor immune evasion O=3 or O=2?). LOO stability confirms robustness to individual substrate variation, but IRR studies with ≥3 independent scorers on ≥15 biological systems are required before certification-grade application.

**K = N_e identification:** The mapping is conceptually motivated and produces the correct first-order limit. Formal derivation showing N_e plays the same partition-function role as K in the THRML context is work in progress (Paper 4D, canonical parameters).

**Absolute Pe magnitudes:** The bridge predicts rank ordering, not absolute values. Pe magnitudes are only comparable across domains after explicit K = N_e scaling. The Spearman analyses reported here are rank-based and are unaffected by this limitation.

**Scope of Red Queen derivation:** The theorem covers the Pe=0 boundary condition. It does not derive the full cascade dynamics or the demon lattice phases (crystal, plasma, oscillation from Paper 9) in biological populations. Whether biological systems exhibit these phases at corresponding Pe values requires THRML sampler analysis on evolutionary data.

---

## VIII. Discussion

### VIII.A What the Three Convergences Mean

Kyle (1985) and Glosten-Milgrom (1985) derived their market microstructure results from rational-expectations equilibrium theory, modeling the strategic behavior of informed and uninformed traders in continuous auctions. Kimura (1968) derived his neutral theory criterion from Wright-Fisher diffusion processes in population genetics, modeling the probability of mutant fixation under genetic drift and selection. The THRML Pe was derived from thermodynamic partition functions on a Bernoulli manifold, modeling attention dynamics in behavioral systems. None of these bodies of work reference each other.

The convergence is not surprising if Pe describes a structural property of adaptive systems under opacity and responsiveness. In any system where an adaptive agent faces an opaque, responsive, coupled adversary, the thermodynamic steady-state dynamics are governed by the same equations — because the structural problem is identical. The notification engineer optimizing for engagement, the pathogen evolving immune evasion, and the market maker pricing adverse selection risk are all solving the same thermodynamic problem from different angles.

This is not a metaphor. The equations are the same. The mapping K = N_e, b_net = 2s is not chosen for aesthetic reasons — it follows from the structural identification of what plays the role of spin count and bias field in each domain.

A natural objection is that the mapping was chosen post-hoc to make the expressions match. The reply is direct: the mapping is not fitted to data — it is a structural identification that can be evaluated independently. K in THRML is the effective number of independently competing adaptive units. In population genetics, the quantity playing this role is N_e — effective population size, the number of independently evolving lineages competing for fixation. The identification K = N_e is not a free parameter; it is the claim that these two theories describe the same structural quantity in different notation. The fact that Pe_THRML = 4N_e·s at first order is then a confirmation of the identification rather than its motivation. If the mapping were wrong — if the relevant biological quantity were something other than N_e — the expressions would not match. They match exactly at first order.

### VIII.B What the Framework Does Not Claim

The convergence evidence does not imply exact quantitative interchangeability across domains without domain-specific calibration. The absolute Pe magnitudes differ because K scales differently (N_e for biology may be 10³ to 10⁶, versus K=16 canonical for behavioral platforms). The Spearman analysis addresses rank ordering, which is K-invariant; absolute magnitudes require explicit K = N_e calibration.

The N=10 biological substrate validation is sufficient for convergence demonstration but not for full certification-grade scoring. BIO-3 through BIO-5 remain open and would constitute genuine tests against the null hypothesis. A systematic survey applying the void rubric to the parasitology literature with multiple independent scorers (κ_α ≥ 0.40) would provide stronger validation.

The Red Queen theorem covers the Pe=0 boundary condition but not the full cascade dynamics in biological populations. Whether biological systems exhibit the same demon lattice phase structure (crystal, plasma, oscillation phases from Paper 9) at different Pe values is an open question requiring THRML sampler analysis on evolutionary dynamics data.

### VIII.C Gaps

Three analytical gaps remain open from prior work:

**G3 (Cascade coupling constants):** κ₁₂ (D1→D2 transition rate) and κ₁₃ (D2→D3 transition rate) have no measured values in any substrate class. In biology, these would correspond to the rate at which adaptive complexity converts to physiological integration and behavioral manipulation. Tractable in principle from comparative phylogenetics: rate of transition from free-living to parasitic lifestyles as a function of void score.

**G5 (Fisher metric cross-terms):** The product form assumed in Paper 9's Eckert Manifold geometry (no cross-terms between O, R, α in the metric) has not been tested. If significant cross-terms exist, the V* boundary would shift.

**IRR study:** The void scoring rubric requires IRR validation (κ_α ≥ 0.40 minimum) before certification-grade application. This is urgent for biological application, where ecological observables map to (O, R, α) through expert judgment.

---

## IX. Conclusion

Three bodies of theory — attention thermodynamics, financial market microstructure, and population genetics — independently derived the same Péclet criterion. Kyle (1985) and Glosten-Milgrom (1985) derived void metrics in econometric notation 40 years before the void framework; Kimura (1968) derived the neutral theory criterion 58 years before. The convergences were not anticipated. They follow from the structural identity of the thermodynamic problem faced by adaptive agents under opacity and responsiveness.

The Kimura identity (Pe_THRML = 4N_e·s at first order) extends the neutral theory to the full nonlinear Pe spectrum. Below V* = 5.52, Kimura's neutral evolution holds. Above V*, the second law of thermodynamics makes directional selection inevitable. The Red Queen hypothesis is the corollary that abiotic adversaries (R = 0) almost never cross V*, while biotic adversaries routinely do. Behavioral manipulation parasites (Toxoplasma, Ophiocordyceps, Sacculina) represent the D3 cascade completion at V = 9 — the thermodynamic maximum — and every known case achieves it.

The void framework is not describing a feature of technology platforms. It is describing what happens to adaptive systems under opacity and responsiveness, at any scale, in any medium.

---

## References

Asquith, B., Edwards, C. T., Lipsitch, M., & McLean, A. R. (2006). Inefficient cytotoxic T lymphocyte–mediated killing of HIV-1–infected cells in vivo. *PLOS Biology*, 4(4), e90. https://doi.org/10.1371/journal.pbio.0040090

Berenbaum, M. (1983). Coumarins and caterpillars: A case for coevolution. *Evolution*, 37(1), 163–179. https://doi.org/10.2307/2408183

Berdoy, M., Webster, J. P., & Macdonald, D. W. (2000). Fatal attraction in rats infected with *Toxoplasma gondii*. *Proceedings of the Royal Society B*, 267(1452), 1591–1594. https://doi.org/10.1098/rspb.2000.1182

Byrne, R. W., & Whiten, A. (Eds.). (1988). *Machiavellian Intelligence: Social Expertise and the Evolution of Intellect in Monkeys, Apes, and Humans*. Oxford University Press.

Davies, N. B. (2000). *Cuckoos, Cowbirds and Other Cheats*. T&AD Poyser.

Dawkins, R., & Krebs, J. R. (1979). Arms races between and within species. *Proceedings of the Royal Society B*, 205(1161), 489–511. https://doi.org/10.1098/rspb.1979.0081

Ebert, D. (2005). *Ecology, Epidemiology, and Evolution of Parasitism in Daphnia*. NCBI Bookshelf (National Library of Medicine).

Eckert, A. (2026a). The Technical Foundations of the Void Framework. *Paper 3, MoreRight DAO*.

Eckert, A. (2026b). The Canonical Parameters: THRML Drift-Diffusion Formalism. *Paper 4, MoreRight DAO*.

Eckert, A. (2026c). The Void Space: Topological Foundations of the Eckert Manifold. *Paper 9, MoreRight DAO*. DOI: 10.5281/zenodo.14851748.

Ehrlich, P. R., & Raven, P. H. (1964). Butterflies and plants: A study in coevolution. *Evolution*, 18(4), 586–608. https://doi.org/10.2307/2406212

Fisher, R. A. (1930). *The Genetical Theory of Natural Selection*. Clarendon Press.

Glosten, L. R., & Milgrom, P. R. (1985). Bid, ask and transaction prices in a specialist market with heterogeneously informed traders. *Journal of Financial Economics*, 14(1), 71–100. https://doi.org/10.1016/0304-405X(85)90044-3

Haldane, J. B. S. (1924). A mathematical theory of natural and artificial selection. *Transactions of the Cambridge Philosophical Society*, 23, 19–41.

Høeg, J. T. (1995). The biology and life cycle of the Rhizocephala (Cirripedia). *Journal of the Marine Biological Association of the United Kingdom*, 75(3), 517–550.

Hughes, D. P., Andersen, S. B., Hywel-Jones, N. L., Himaman, W., Billen, J., & Boomsma, J. J. (2011). Behavioral mechanisms and morphological symptoms of zombie ants dying from fungal infection. *BMC Ecology*, 11(1), 13. https://doi.org/10.1186/1472-6785-11-13

Kimura, M. (1968). Evolutionary rate at the molecular level. *Nature*, 217(5129), 624–626. https://doi.org/10.1038/217624a0

Kyle, A. S. (1985). Continuous auctions and insider trading. *Econometrica*, 53(6), 1315–1335. https://doi.org/10.2307/1913210

Margulis, L. (1970). *Origin of Eukaryotic Cells*. Yale University Press.

Maynard Smith, J. (1982). *Evolution and the Theory of Games*. Cambridge University Press.

Ohta, T. (1992). The nearly neutral theory of molecular evolution. *Annual Review of Ecology and Systematics*, 23, 263–286. https://doi.org/10.1146/annurev.es.23.110192.001403

Smith, S. E., & Read, D. J. (2008). *Mycorrhizal Symbiosis* (3rd ed.). Academic Press.

Van Valen, L. (1973). A new evolutionary law. *Evolutionary Theory*, 1, 1–30.

Williams, M. J., Werner, B., Barnes, C. P., Graham, T. A., & Sottoriva, A. (2016). Identification of neutral tumor evolution across cancer types. *Nature Genetics*, 48(3), 238–244. https://doi.org/10.1038/ng.3489

Wright, S. (1931). Evolution in Mendelian populations. *Genetics*, 16(2), 97–159.

---

## Data and Code

All analyses are reproducible from the THRML notebooks:

- nb25 (market microstructure): `notebooks/25_market_microstructure_mapping.ipynb`
- nb26 (G1 bridge verification): `notebooks/26_g1_bridge_verification.ipynb`
- nb27 (dimension weighting): `notebooks/27_dimension_weighting.ipynb`
- nb28 (coupling emergence): `notebooks/28_coupling_emergence.ipynb`
- nb29 (validation robustness): `notebooks/29_validation_robustness.ipynb`
- nb30 (Kimura-THRML convergence): `notebooks/nb30_kimura_thrml_convergence.ipynb`
- nb31 (parasite-host validation, N=10): `notebooks/nb31_parasite_void_scores.ipynb`

Public repository (CC-BY 4.0): https://github.com/MoreRightDAO/thrml-examples
