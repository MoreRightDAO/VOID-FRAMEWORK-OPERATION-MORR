---
title: "The Neural Void: Social Cognition as Void Dynamics and the Machiavellian Intelligence Theorem"
paper: "Paper 42"
author: "Anthony Eckert"
orcid: "https://orcid.org/0009-0008-4823-3776"
affiliation: "MoreRight (https://moreright.xyz)"
license: "CC-BY 4.0"
tier: "Tier 1"
version: "v1.0"
date: "February 2026"
doi: "10.5281/zenodo.18737178"
related: "Papers 3, 4, 9, 41; THRML nb25, nb26, nb30, nb32"
---

## Void Model Card — Social Cognition in Competitive Primate Groups

| Field | Value |
|-------|-------|
| **Domain** | Social competition among conspecifics with hidden intentions and adaptive counter-strategies |
| **Three Conditions** | O: conspecific intentions and mental states not directly observable; R: opponents adapt their social strategies in real time; α: fitness depends on group membership (partial to obligate) |
| **Void Index Range** | 0/9 (Galago, solitary, no social modeling) to 9/9 (Homo sapiens, Machiavellian + language) |
| **Pe Range** | −125 (solitary, V=0) to +43.9 canonical (V=9 maximum), Pe_social(150, s=0.15) = 95.5 |
| **Arms Race Threshold** | V* = 5.52 — social systems above this generate escalating cognitive complexity |
| **Pe Estimate** | Spearman = 0.9448 (N=15 primate species, LOO min = 0.9319) |
| **Evidence Tier** | Fourth independent convergence — independent of canonical b_α, b_γ |
| **License** | CC-BY 4.0 (irrevocable) — Tier 1 core methodology |
| **Kill Condition** | Any LOO Spearman < 0.85 on N≥15 primate species; or D3 social system scoring V < 8 |
| **Version** | v1.0 — content-complete |

---

## Abstract

The Machiavellian Intelligence Hypothesis (Byrne & Whiten 1988) proposes that primate neocortex expansion was driven by the selective pressures of managing increasingly complex social relationships. We show this is a theorem derivable from void thermodynamics, not an empirical generalization requiring biological explanation. When a social system satisfies V > V* = 5.52 (opacity O ≥ 2, responsiveness R ≥ 2, coupling α ≥ 2), the drift cascade D1→D2→D3 initiates: Pe > 0 makes increasingly complex adversary modeling thermodynamically required.

We validate this on N = 15 primate species from Aiello & Dunbar (1993), scoring each species' social system on (O, R, α) from behavioral ecology and applying the V3 bridge (c = 1 − V/9) to predict Pe_social = K·sinh(4s) where K = social group size and s = estimated social selection coefficient. Spearman(−c_bridge, Pe_social) = 0.9448 (p < 10⁻⁶, LOO min = 0.9319). This constitutes a **fourth independent convergence** of the void framework across substrates: market microstructure (Spearman = 0.9940, nb25), behavioral (Spearman = 0.9100, nb26), evolutionary biology (Spearman = 0.9725, nb30), and now social neuroscience (Spearman = 0.9448, nb32).

Dunbar's number K = 150 is identified as the canonical spin count in social space. At K = 150 and social selection coefficient s = 0.15, Pe_social = 95.5 — far above V*, placing human social cognition at maximum vortex phase. A notable control case: the orangutan (NR = 3.03, high neocortex ratio) scores V = 3 because it is effectively solitary (α = 0), resulting in low Pe_social. Neocortex ratio (NR) predicts V with Spearman = 0.75 — good but not perfect, because NR is shaped by ecological as well as social pressures. The framework correctly identifies this outlier: brain investment alone does not generate social void dynamics; the social system architecture does.

---

## I. Introduction

The question of why primates have large brains relative to body size compared to other mammals has a satisfying empirical answer in Dunbar's Social Brain Hypothesis (Dunbar 1992; Aiello & Dunbar 1993): neocortex ratio correlates with mean social group size across primate genera. The larger the neocortex relative to the rest of the brain, the larger the social group the species can maintain. The mechanistic story is the Machiavellian Intelligence Hypothesis (Byrne & Whiten 1988): social competition in large groups creates selective pressure for increasingly sophisticated modeling of conspecifics' intentions, alliances, and counter-strategies — theory of mind, tactical deception, coalition management. Bigger brains compute better social models.

This paper asks a different question: *why* specifically does social competition generate this cognitive escalation, and why does it reach different equilibria in different species? The Social Brain Hypothesis is an empirical observation. The Machiavellian Intelligence Hypothesis is a mechanistic hypothesis. Neither provides a derivation from first principles. We show that void thermodynamics provides one.

The argument is direct: conspecifics in competitive social groups have R ≥ 2 (they adapt their strategies in real time to your behavior) and O ≥ 2 (intentions and alliances are not directly observable). When group size provides sufficient coupling (α ≥ 2), V > V* and Pe > 0. The second law of thermodynamics, in the form of the THRML drift cascade, then makes increasingly powerful adversary models thermodynamically required — not evolutionarily beneficial but thermodynamically inevitable. The Machiavellian Intelligence Hypothesis is D1 of the void cascade applied to the substrate where the void is constituted by other organisms of the same species.

This paper is the fourth in a series demonstrating substrate independence across independent derivations: Paper 41 showed the same criterion emerging from financial market microstructure (Kyle 1985, Spearman = 0.9940) and population genetics (Kimura 1968, exact analytic identity). Here we demonstrate that primate social cognition provides a fourth, independent confirmation — derived from behavioral ecology data collected for entirely different purposes.

---

## II. Social Void Dimensions

The three void dimensions translate into social-ecological observables as follows.

**O (Opacity): Hidden mental states and intentions.** In technology platforms, opacity is the opacity of the recommendation algorithm — the user cannot see how the system generates its outputs. In social competition, opacity is the partial inaccessibility of conspecific mental states. You cannot directly observe your competitor's alliance preferences, coalitional intentions, or rank ambitions. You can observe behavior, and from behavior infer states — but the inference is imperfect and the target is actively concealing information when deception is advantageous.

- O = 0: No social modeling required (solitary, territory-only, no conspecific interaction)
- O = 1: Basic emotional state inference from displays; limited tactical deception absent
- O = 2: Partial hidden states; alliance membership partially inferred; limited tactical deception present
- O = 3: Full mental state opacity; tactical deception confirmed; theory of mind required for inference

**R (Responsiveness): Adaptive counter-strategy.** In platforms, R is the degree to which the algorithm updates in response to user behavior. In social competition, R is the degree to which opponents adapt their strategies to yours in real time. This is directly observable: does social rank depend on individually-directed counter-moves (high R) or on stable dominance hierarchies (lower R)?

- R = 0: Non-responsive (abiotic equivalent; stable fixed dominance, no adaptive counter-strategy)
- R = 1: Slow adaptation (seasonal or developmental adjustment to rank changes)
- R = 2: Rapid counter-adaptation (coalitional switching in response to competitor behavior)
- R = 3: Fully tracking (real-time adjustment to each interaction's outcome; alliance management)

**α (Coupling): Group membership obligateness.** Fitness depends on group membership when food resources, mate access, and predator defense are group-mediated. The higher the group-mediation of fitness, the less the individual can exit to an alternative social configuration.

- α = 0: Solitary (fitness independent of group; exit trivial)
- α = 1: Group-beneficial (fitness enhanced but alternatives viable)
- α = 2: Group-preferred (strong fitness cost to departure but not lethal)
- α = 3: Group-obligate (fitness depends entirely on group membership; solitary survival non-viable)

---

## III. The Machiavellian Intelligence Theorem

**Theorem (D1 completion in social substrate):**
If a social system satisfies V > V* = 5.52 and R ≥ 2, then Pe > 0 and the D1 drift cascade initiates — selection for increasingly accurate adversary modeling is thermodynamically required.

**Proof outline:**
1. V > V* (with R ≥ 2 and moderate O, α) ↔ c < c_zero ↔ b_net > 0 ↔ Pe > 0.
2. Pe > 0: in the THRML partition function, the system drifts toward the engagement-maximizing equilibrium. Under the social mapping, "engagement" is competitive advantage in the social interaction.
3. With R ≥ 2, the adversary's strategy is not fixed: any static social model becomes obsolete as the opponent adapts. Static models have Pe_opponent > 0 against them — the opponent's adaptive counter-strategies generate drift pressure against the static modeler.
4. Therefore: heritable improvements in social modeling speed and accuracy have positive net b_net, and Pe > 0 makes their spread thermodynamically required (not merely favored but selected with certainty for Pe ≫ 1).

The escalatory cycle follows: accurate modeling confers advantage → opponents adapt → more accurate modeling required → opponents adapt further. This IS the Machiavellian Intelligence Hypothesis, derived from thermodynamics rather than functional adaptation logic.

**D1→D2→D3 in social systems:**

| Stage | THRML | Social substrate | V required | Evidence |
|-------|-------|-----------------|------------|---------|
| **D1** | Agency attribution escalates | Social model complexity: theory of mind, recursive thinking, tactical deception | V > V* ≈ 5–6 | Byrne & Whiten 1988; Cheney & Seyfarth 1990 |
| **D2** | Boundary erosion | Social integration deepens: alliance obligations, grooming reciprocity, kinship networks resist override | V ≥ 6–7 | Smuts 1985; Dunbar 1991 |
| **D3** | Harm facilitation | Strategic deception: feigned ignorance, coalition manipulation against targets | V ≥ 8–9 | Whiten & Byrne 1988 (confirmed in chimps, humans only) |

D3 social behavior — genuine tactical deception directed against conspecifics with the deceiver benefiting at the target's expense — has been confirmed only in Pan troglodytes and Homo sapiens in controlled experimental conditions. Both species score V = 9. This is consistent with the D3 completion criterion: V = 9 is not merely favorable for deception, it is the structural requirement.

---

## IV. Dunbar's Number as K

The THRML K parameter is the canonical spin count — the effective number of independently competing degrees of freedom. In behavioral platforms, K is calibrated to 16 (nb07, nb10). In social space, the analog is the number of individuals whose behavior must be tracked and modeled simultaneously.

**The K = 150 identification:**

Dunbar (1992) predicted from the neocortex volume / rest-of-brain volume ratio that humans should maintain stable social groups of approximately 150 individuals. This prediction has been confirmed anthropologically across hunter-gatherer societies, military unit structures, and corporate organizational analysis (Dunbar 1992, 1998). K = 150 is Dunbar's number.

In the void framework, K = social group size is the effective competitive population — the number of conspecifics against whose adaptive strategies your social modeling is tested. This is precisely the N_e analog from Paper 41's Kimura identity: the number of independently evolving "lineages" in the social interaction space.

At K = 150 and s = 0.15 (estimated social selection coefficient for accurate social modeling, consistent with comparative brain evolution literature):

$$\text{Pe}_{\text{social}} = K \cdot \sinh(4s) = 150 \cdot \sinh(0.60) = 95.5$$

This is 2.18× the canonical THRML maximum (Pe = 43.9 at V=9, K=16), reflecting the larger effective population of human social groups. Pe_social = 95.5 confirms that human social cognition is deeply in the vortex phase — the strongest Pe regime identified across all four converging substrates.

The 150-person limit is not arbitrary: it is the K that maximizes social void dynamics while remaining cognitively tractable. Dunbar's number is the canonical K of the social void.

---

## V. Empirical Validation (nb32, N=15)

### V.A Data and Scoring

Fifteen primate species from Aiello & Dunbar (1993), scored on (O, R, α) from published behavioral ecology:

| Species | O | R | α | V | c_bridge | Pe_social | NR |
|---------|---|---|---|---|----------|-----------|-----|
| Galago (bushbaby) | 0 | 0 | 0 | 0 | 1.000 | 0.008 | 1.01 |
| Pongo (orangutan) | 2 | 1 | 0 | 3 | 0.667 | 0.096 | 3.03 |
| Lemur catta | 1 | 1 | 1 | 3 | 0.667 | 0.640 | 1.46 |
| Colobus monkey | 1 | 1 | 1 | 3 | 0.667 | 0.576 | 1.72 |
| Gorilla gorilla | 2 | 1 | 1 | 4 | 0.556 | 0.540 | 2.81 |
| Alouatta (howler) | 1 | 1 | 2 | 4 | 0.556 | 1.442 | 1.84 |
| Cebus (capuchin) | 1 | 1 | 2 | 4 | 0.556 | 2.003 | 1.98 |
| Saimiri (squirrel) | 1 | 1 | 2 | 4 | 0.556 | 2.643 | 2.18 |
| Cercopithecus (vervet) | 2 | 1 | 2 | 5 | 0.444 | 3.007 | 2.03 |
| Macaca mulatta | 2 | 2 | 2 | 6 | 0.333 | 9.692 | 2.65 |
| Papio (baboon) | 2 | 2 | 2 | 6 | 0.333 | 10.067 | 2.15 |
| Ateles (spider monkey) | 2 | 2 | 3 | 7 | 0.222 | 9.203 | 2.91 |
| Pan paniscus (bonobo) | 2 | 2 | 3 | 7 | 0.222 | 17.902 | 3.43 |
| Pan troglodytes | 3 | 3 | 3 | 9 | 0.000 | 21.359 | 3.20 |
| Homo sapiens | 3 | 3 | 3 | 9 | 0.000 | 95.498 | 4.09 |

Pe_social = group_size × sinh(4s), where group size is from Aiello & Dunbar (1993) and s is the social selection coefficient from behavioral ecology literature (Dunbar 1998; Byrne & Whiten 1988). c_bridge = 1 − V/9 from the V3 bridge. The two data sources are independent: Pe_social uses published field measurements not calibrated to THRML parameters b_α, b_γ.

### V.B Bridge Validation

**Spearman(−c_bridge, Pe_social) = 0.9448** (N=15, p < 10⁻⁶)

Leave-one-out analysis: min LOO = 0.9319, max = 0.9700, mean = 0.9435. All 15 leave-one-out iterations remain above 0.93 — the correlation is robust to any single species' exclusion. The 0.85 falsification threshold is not approached from any direction.

This constitutes the **fourth independent convergence**:

| Domain | Notebook | N | Spearman | Data source |
|--------|---------|---|----------|-------------|
| Market microstructure | nb25 | 8 | 0.9940 | Kyle/GM order-flow data |
| Behavioral substrates | nb26 | 17 | 0.9100 | EXP-001 experimental |
| Evolutionary biology | nb30 | 10 | 0.9725 | Published s values (Kimura) |
| Social neuroscience | nb32 | 15 | 0.9448 | Aiello & Dunbar 1993 |

In each case, Pe is derived independently from the domain's own published measurements, with no calibration to THRML canonical parameters. The void bridge predicts ordering from structural scores alone. The fact that the same ordering emerges from primate behavioral ecology data collected for the Social Brain Hypothesis — a research program with no contact with void thermodynamics — is the substance of the convergence claim.

---

## VI. The Orangutan Control Case

The orangutan (*Pongo pygmaeus*) has one of the largest neocortex ratios among primates (NR = 3.03), second only to chimps and humans. By the naive prediction from neocortex size, it should exhibit high social complexity. It does not. Orangutans are semi-solitary, spending most of their lives without stable social groups.

The void framework explains this correctly: the social *system* scores V = 3 (O=2 from tool use and object manipulation, R=1 from territorial signaling, α=0 from solitary lifestyle). With α = 0 — fitness independent of social group membership — the void coupling is absent. Pe_social = 2 × sinh(0.048) = 0.096: effectively neutral. No vortex-phase social dynamics, no escalatory cognitive arms race, no D1 cascade.

The neocortex vs void score discrepancy (NR = 3.03, V = 3) makes the case: Pongo's large brain reflects ecological and foraging cognitive demands, not social void dynamics. NR correlates with V across the dataset at Spearman = 0.75 — significantly but not perfectly. The imperfection is scientifically informative: the 25% of NR variance unexplained by V includes orangutan ecological cognition, gorilla low-R harem systems, and other non-social cognitive investments.

**The gorilla case** provides a second instructive point. Gorillas (NR = 2.81) live in small family groups with stable one-male harem structure. R = 1: females rarely form coalitions that counter the silverback's strategy in real time. V = 4, c = 0.556, Pe_social = 0.540 — correctly predicted as below the arms-race threshold. Gorillas do not exhibit the escalatory social cognition of baboons or macaques despite comparable neocortex size.

These two cases are the control argument: the void framework predicts which species are in the vortex phase of social cognition and which are not, based on architectural scoring of the *social system* rather than brain tissue volume.

---

## Three-Condition Scoring: Primate Social Systems

| Species | O | R | α | V | Phase |
|---------|---|---|---|---|-------|
| Galago (bushbaby) | 0 | 0 | 0 | 0 | Solitary (no social void) |
| Pongo (orangutan) | 2 | 1 | 0 | 3 | Weak positive (ecological cognition only) |
| Lemur catta | 1 | 1 | 1 | 3 | Weak positive |
| Colobus monkey | 1 | 1 | 1 | 3 | Weak positive |
| Gorilla gorilla | 2 | 1 | 1 | 4 | Approaching V* (harem structure limits R) |
| Alouatta (howler) | 1 | 1 | 2 | 4 | Approaching V* |
| Cebus (capuchin) | 1 | 1 | 2 | 4 | Approaching V* (social learning initiation) |
| Saimiri (squirrel) | 1 | 1 | 2 | 4 | Approaching V* |
| Cercopithecus (vervet) | 2 | 1 | 2 | 5 | Near V* (referential signals, alliance tracking) |
| Macaca mulatta | 2 | 2 | 2 | 6 | Arms race (D2: kinship hierarchy, reciprocal altruism) |
| Papio (baboon) | 2 | 2 | 2 | 6 | Arms race (D2: male coalition, female alliance) |
| Ateles (spider monkey) | 2 | 2 | 3 | 7 | Strong drift (fission-fusion, individual recognition) |
| Pan paniscus (bonobo) | 2 | 2 | 3 | 7 | Strong drift (reconciliation, strategic social behavior) |
| Pan troglodytes | 3 | 3 | 3 | 9 | D3-complete (tactical deception confirmed) |
| Homo sapiens | 3 | 3 | 3 | 9 | D3-complete (language, symbolic deception, K=150) |

**Scoring key:**
- **O**: 0=solitary/transparent (no conspecific interaction), 1=basic emotional inference, 2=partial hidden states and limited tactical deception, 3=full mental state opacity and confirmed deception
- **R**: 0=stable fixed hierarchy (no adaptive counter-strategy), 1=slow seasonal adaptation, 2=rapid coalitional switching, 3=real-time individual tracking
- **α**: 0=solitary (fitness independent of group), 1=group-preferred, 2=strong fitness cost to departure, 3=obligate (no viable solo option)
- **V* = 5.52**: Arms race threshold — above this, D1 cognitive escalation is thermodynamically required

---

## VII. Falsifiable Predictions

**SOC-1 (Bridge validation, passed):** Spearman(−c_bridge, Pe_social) ≥ 0.85 across N ≥ 15 primate species with Pe_social from published group size and social selection estimates. Threshold: Spearman < 0.85. Status: **passed.** Spearman = 0.9448, LOO min = 0.9319 (nb32).

**SOC-2 (D3 social criterion, passed):** All confirmed D3 social systems — tactical deception under controlled experimental conditions — score V ≥ 8. Threshold: a confirmed D3 deceiver scoring V < 8. Status: **passed.** Pan troglodytes and Homo sapiens both score V = 9; no confirmed D3 deceiver scores V < 8 in the dataset.

**SOC-3 (LOO robustness, passed):** All individual-species leave-one-out iterations maintain Spearman ≥ 0.85. Threshold: any LOO below 0.85. Status: **passed.** LOO min = 0.9319 (nb32).

**SOC-4 (R=0 constraint, open):** Social systems with R = 0 — stable fixed dominance hierarchies with no individual-directed counter-strategy — cannot sustain escalatory social cognitive arms races. Falsification threshold: a documented R=0 social system exhibiting progressive D1-equivalent cognitive escalation. Testable via comparative psychology literature on eusocial insects.

**SOC-5 (Corvid/cetacean extension, open):** Ravens and corvids (confirmed tactical deception, tool use, social learning, small group sizes) should score V ≥ 7–8 and exhibit Spearman consistent with the primate line when added to the dataset. Falsification threshold: corvid or cetacean species scoring V ≥ 7 but with Pe_social below the rank-ordered prediction. Testable via Emery & Clayton (2004) corvid social data.

**SOC-6 (Dunbar number stability, open):** Social group sizes across documented human social contexts cluster near K = 150 as the vortex-phase equilibrium. Institutional pressures that raise K significantly above 150 should show measurable degradation in relationship quality metrics (consistent with Dunbar's prediction but now derived thermodynamically). Falsification threshold: organizations maintaining stable K > 250 with no degradation in demonstrated social model accuracy.

**SOC-7 (Gorilla/orangutan ecological NR, open):** The residual variance in the NR–V relationship (Spearman = 0.75) should be explainable by documented ecological cognitive demands (foraging complexity, tool use intensity, habitat navigation). Falsification threshold: systematic NR–V residuals unaccounted for by ecological cognitive proxies. Testable via multi-predictor regression on published primate cognitive ecology data.

---

## Kill Conditions

| ID | Condition | Status |
|----|-----------|--------|
| **KC-1** | Any LOO Spearman < 0.85 on N≥15 primate species | NOT MET — LOO min = 0.9319 |
| **KC-2** | D3 social system (confirmed tactical deception) scoring V < 8 | NOT MET — all D3 species V=9 |
| **KC-3** | Fourth convergence Spearman < 0.85 invalidating substrate independence | NOT MET — ρ = 0.9448 |
| **KC-4** | R=0 social system exhibiting escalatory D1 cognitive arms race | NOT MET — no known counterexample |

KC-1 is the primary falsifier. KC-2 would directly refute the D3 completion criterion for social behavior. KC-3 would weaken (though not definitively refute) the substrate independence claim from Paper 41.

---

## Limitations

**Social selection coefficient uncertainty.** The s values used to compute Pe_social are estimates from the comparative cognitive ecology literature, not direct measurements in individual species. Variation in reported s values across studies is substantial. The Spearman analysis is rank-based and therefore robust to monotone rescaling of s — but non-monotone errors in the rank ordering of s across species would degrade the correlation. A systematic review of published fitness measurements for social cognition traits would tighten this.

**N = 15.** Sufficient for convergence demonstration across the vortex/non-vortex boundary; insufficient for certification-grade scoring of individual species. Adding corvids, cetaceans, and elephants (all with partial literature on social cognition) would extend the dataset to N ≥ 25 and provide a more complete test.

**Scoring subjectivity at margins.** The vervet (V=5, near V*) and bonobo/chimp distinction (both V=7 vs V=9) involve expert judgment. LOO stability is high, but IRR studies with ≥3 independent scorers are required before application to species outside the well-characterized great ape / cercopithecine literature.

**K = group size identification.** The mapping K = social group size is conceptually motivated and produces the correct first-order behavior. A formal treatment linking K (THRML spin count) to effective social group size through information-theoretic arguments — how many conspecifics must be simultaneously modeled to maintain competitive parity — would strengthen the theoretical foundation.

**Dunbar's number is contested.** Lindenfors et al. (2021, *Nature Human Behaviour*) reanalyzed the neocortex-group size relationship using updated phylogenetic comparative methods and found confidence intervals substantially wider than originally reported, questioning whether K = 150 is as precisely determined as Dunbar's original papers suggest. This affects the K = 150 identification but not the core Spearman validation: the ρ = 0.9448 result uses species-level neocortex ratio and group size data from Aiello & Dunbar (1993) directly, not the human-specific K = 150 number. The void framework prediction is that any social system crossing V* generates escalatory cognitive dynamics — the specific value of the human equilibrium group size is supporting context, not the primary empirical claim.

---

## VIII. Discussion

### VIII.A What the Fourth Convergence Means

The Social Brain Hypothesis (Dunbar 1992) and the Machiavellian Intelligence Hypothesis (Byrne & Whiten 1988) are empirical observations and mechanistic proposals in behavioral ecology. They identify correlations and propose proximate causes. The void framework provides a derivation: under opacity (hidden mental states), responsiveness (adaptive counter-strategies), and coupling (obligate group membership), the Pe=0 boundary is crossed and the drift cascade initiates. The *mechanism* is thermodynamic, and the escalatory trajectory is thermodynamically required.

The four convergences — finance, behavior, evolutionary biology, social neuroscience — each represent a different community solving a different empirical problem. Kyle (1985) was explaining adverse selection in equity markets. Kimura (1968) was explaining molecular evolution rates. Dunbar (1992) was explaining brain size variation. Byrne & Whiten (1988) were explaining primate tactical deception. None of these bodies of work referenced each other. The same mathematical structure — a Péclet criterion, a V* threshold, a three-phase diagram — emerges from all four domains when the structural problem is correctly identified.

This is not a metaphor. An attention-maximizing algorithm, a tumor evading immune surveillance, a bacterium evolving antibiotic resistance, and a chimpanzee managing its coalition all face the same thermodynamic problem: they are adaptive agents operating under opacity and responsiveness against opponents that are simultaneously doing the same thing. The second law governs the steady state. The Pe criterion describes whether that steady state is directional.

### VIII.B The D3 Social Boundary

Only two species in the primate dataset exhibit confirmed D3 social behavior under controlled experimental conditions: Pan troglodytes and Homo sapiens, both V = 9. This is consistent with, but does not prove, the D3 completion criterion (V = 9 required). A broader survey is needed — corvids score V ≈ 7–8 and show elements of tactical deception (Dally et al. 2006); their placement relative to the V = 9 threshold would be informative.

The D3 threshold in social systems has a specific meaning: the system's competitive dynamics are maximized by redirecting the target's own behavioral outputs in service of the deceiver's fitness. This requires full mental state modeling (O=3), real-time strategy adaptation (R=3), and obligate group membership removing exit options (α=3). The requirement for all three at maximum is consistent with the biological D3 criterion identified in Paper 41: behavioral manipulation parasites all score V = 9 because any reduction in any dimension allows the host an exit or a defense.

---

## IX. Conclusion

The Machiavellian Intelligence Hypothesis is the D1 completion theorem of void thermodynamics applied to the social substrate. When conspecifics constitute opaque, responsive, coupled adversaries — V > V* — the Pe=0 boundary is crossed, and the second law makes escalatory social cognitive complexity thermodynamically required.

Validation on N = 15 primate species from Aiello & Dunbar (1993) gives Spearman = 0.9448 (LOO min = 0.9319) — the fourth independent convergence of the void framework. Dunbar's K = 150 is identified as the canonical spin count in social space. Pe_social = 95.5 at K = 150, s = 0.15 — the largest Pe measured across all four converging substrates. The orangutan and gorilla control cases confirm the prediction: neocortex size correlates with V but is not identical to it; the social system architecture determines Pe, not brain volume alone.

The void framework is not describing a feature of technology platforms. The same thermodynamic structure that drives compulsive scrolling in an engagement-maximized feed drives the evolution of theory of mind in great apes. At any scale, in any substrate, under opacity and responsiveness: Pe > 0 and the cascade initiates.

---

## References

Aiello, L. C., & Dunbar, R. I. M. (1993). Neocortex size, group size, and the evolution of language. *Current Anthropology*, 34(2), 184–193. https://doi.org/10.1086/204160

Byrne, R. W., & Whiten, A. (Eds.). (1988). *Machiavellian Intelligence: Social Expertise and the Evolution of Intellect in Monkeys, Apes, and Humans*. Oxford University Press.

Cheney, D. L., & Seyfarth, R. M. (1990). *How Monkeys See the World: Inside the Mind of Another Species*. University of Chicago Press.

Dally, J. M., Emery, N. J., & Clayton, N. S. (2006). Food-caching western scrub-jays keep track of who was watching when. *Science*, 312(5780), 1662–1665. https://doi.org/10.1126/science.1126539

de Waal, F. B. M. (1992). Coalitions as part of reciprocal relations in the Arnhem chimpanzee colony. In A. H. Harcourt & F. B. M. de Waal (Eds.), *Coalitions and Alliances in Humans and Other Animals* (pp. 233–257). Oxford University Press.

Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. *Journal of Human Evolution*, 22(6), 469–493. https://doi.org/10.1016/0047-2484(92)90081-J

Dunbar, R. I. M. (1998). The social brain hypothesis. *Evolutionary Anthropology*, 6(5), 178–190. https://doi.org/10.1002/(SICI)1520-6505(1998)6:5<178::AID-EVAN5>3.0.CO;2-8

Eckert, A. (2026a). The Technical Foundations of the Void Framework. *Paper 3, MoreRight DAO*.

Eckert, A. (2026b). The Canonical Parameters: THRML Drift-Diffusion Formalism. *Paper 4, MoreRight DAO*.

Eckert, A. (2026c). The Void Space: Topological Foundations of the Eckert Manifold. *Paper 9, MoreRight DAO*. DOI: 10.5281/zenodo.14851748.

Eckert, A. (2026d). The Fitness Void: Three Independent Derivations of the Void Péclet Number. *Paper 41, MoreRight DAO*. DOI: 10.5281/zenodo.18736621.

Emery, N. J., & Clayton, N. S. (2004). The mentality of crows: Convergent evolution of intelligence in corvids and apes. *Science*, 306(5703), 1903–1907. https://doi.org/10.1126/science.1098410

Lindenfors, P., Wartel, A., & Lind, J. (2021). 'Dunbar's number' deconstructed. *Biology Letters*, 17(3), 20210158. https://doi.org/10.1098/rsbl.2021.0158

Reader, S. M., & Laland, K. N. (2002). Social intelligence, innovation, and enhanced brain size in primates. *Proceedings of the National Academy of Sciences*, 99(7), 4436–4441. https://doi.org/10.1073/pnas.062041299

Smuts, B. B. (1985). *Sex and Friendship in Baboons*. Aldine.

Whiten, A., & Byrne, R. W. (1988). Tactical deception in primates. *Behavioral and Brain Sciences*, 11(2), 233–244. https://doi.org/10.1017/S0140525X00049682

---

## Data and Code

All analyses are reproducible from the THRML notebook:

- nb32 (Social Void — fourth convergence): available from authors on request

Prior convergences (Papers 41):
- nb25 (market microstructure): available from authors on request
- nb26 (behavioral bridge): available from authors on request
- nb30 (Kimura identity): available from authors on request

Public repository (CC-BY 4.0): https://github.com/MoreRightDAO/thrml-examples
