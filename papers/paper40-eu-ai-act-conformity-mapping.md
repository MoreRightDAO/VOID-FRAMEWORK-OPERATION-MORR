---
title: "The Rosetta Stone: Mapping the Void Framework to EU AI Act Conformity Requirements"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 40"
short-title: "EU Conformity Map"
version: "v0.1 — working draft"
date: "February 2026"
license: "cc-by-4.0"
zenodo-doi: "pending"
---

## Abstract

The EU AI Act imposes transparency, human oversight, and risk management obligations on high-risk AI systems (Articles 9-17) but provides no standardized methodology for measuring compliance with these structural requirements. We demonstrate that the void framework's three dimensions — opacity (O), reactivity (R), and attentional coupling (α) — map bijectively onto the Act's three core obligation clusters: transparency provisions (Art. 13, 10), documentation and robustness requirements (Art. 11, 12, 15), and human oversight mandates (Art. 14). The Péclet number (Pe), the framework's scalar drift metric, functions directly as a quantitative residual risk measure under Art. 9. We derive a translation protocol from void scores to conformity documentation inputs and demonstrate its application across three Annex III high-risk domains: credit scoring (§5), education (§3), and employment screening (§4). Additionally, we address General Purpose AI systems (GPAI, Title VIII), where void scores characterize systemic risk pathways under Art. 51. This paper is intended as an operational reference: companies completing Annex VI self-assessments can use void scores to populate required documentation without waiting for harmonized standards that do not yet exist.

**Keywords:** EU AI Act, conformity assessment, void framework, opacity, transparency, human oversight, risk management, Annex III, self-assessment, AI governance

---

## I. Introduction

### I.A The Standards Gap

The EU AI Act entered into force on 1 August 2024. High-risk AI system obligations under Articles 9-17 applied (or are slated to apply, pending the proposed Digital Omnibus delay) to providers operating in the European market from August 2026. The legal requirements are clear: high-risk AI providers must implement a risk management system (Art. 9), maintain technical documentation (Art. 11), ensure transparency to deployers (Art. 13), enable human oversight (Art. 14), and sustain accuracy and robustness (Art. 15), all under a quality management framework (Art. 17).

What the Act does not provide is a methodology for *measuring* compliance with these structural requirements. Harmonized standards — the technical specifications under which a provider can follow the Annex VI self-assessment pathway — do not yet exist for most Annex III categories. As of early 2026, one of six anticipated harmonized standard clusters has reached public enquiry stage [CITATION: CEN/CENELEC JTC 21 progress report]. This is not a minor gap: without harmonized standards, providers technically cannot invoke Annex VI and may require third-party notified body assessment (Annex VII) — but no notified bodies have been designated for AI Act purposes.

The result is a compliance infrastructure with legal obligations and no operational instruments. Companies must demonstrate conformity without a shared language for what conformity means.

### I.B Our Contribution

This paper establishes that language. The void framework [Papers 1-3] was developed independently of the EU AI Act as a thermodynamically-grounded theory of how AI systems acquire and exercise attentional influence. It characterizes AI systems across three dimensions — opacity, reactivity, and attentional coupling — with the Péclet number as a scalar risk metric derived from their combination.

The central finding of this paper is that these three dimensions are not merely *correlated* with the Act's requirement clusters: they are the information-theoretic foundations from which those requirements can be derived. The Act's drafters, working from first principles of fundamental rights protection, converged on the same three structural properties that information theory demands. This convergence is predictable from the void framework and serves as an independent validation of both frameworks' foundational premises.

The practical result is a *Rosetta Stone* — a bijective mapping that allows companies to:

1. Translate existing void scores into conformity documentation language
2. Identify which articles are implicated by specific structural properties of their system
3. Prioritize remediation investments by article cluster
4. Produce Annex IV technical documentation that references a published, peer-reviewed methodology

This paper is Tier 1 (CC-BY 4.0) and is intended to be freely used, cited, and incorporated into compliance processes.

### I.C Scope and Limits

This paper covers Articles 9-17 of the EU AI Act as they apply to **standalone high-risk AI systems (Annex III, categories §2-§8)** using the self-assessment pathway (Annex VI). Section VI addresses General Purpose AI models (Title VIII, Art. 51-56) as a distinct case. We do not address safety-component AI in regulated products (Annex I, Category 1), which requires notified body assessment and falls outside the Annex VI pathway.

The Digital Omnibus proposal (November 2025) may delay some high-risk enforcement to December 2027. This does not affect our methodology — it affects only the urgency of implementation.

---

## II. The EU AI Act: Structural Overview

### II.A The Three Obligation Clusters

Articles 9-17 organize into three functional clusters, each targeting a distinct structural property of high-risk AI systems:

**Cluster 1 — Transparency (what the system reveals):**
- Art. 10: Data governance — the data pipeline must be documented, examined for biases, and traceable
- Art. 11: Technical documentation — the system's design, logic, and performance must be documented before market placement
- Art. 13: Transparency to deployers — capabilities, limitations, and conditions of use must be disclosed

**Cluster 2 — Stability and Accountability (how the system behaves over time):**
- Art. 12: Record-keeping — automatic logging of operations enables post-market monitoring and accountability
- Art. 15: Accuracy, robustness, cybersecurity — performance must be stable against errors, adversarial inputs, and distributional shift

**Cluster 3 — Oversight (who remains in control):**
- Art. 14: Human oversight — natural persons must be able to understand, monitor, and override the system's outputs

**Integration:**
- Art. 9: Risk management system — continuous lifecycle process that uses the above as inputs to identify, analyze, and mitigate risks
- Art. 17: Quality management system — organizational framework that ensures Clusters 1-3 are maintained across the product lifecycle

### II.B The Annex VI Self-Assessment Pathway

For Annex III categories §2-§8, providers may complete conformity assessment internally (Annex VI) if:
(a) they have applied harmonized standards covering relevant Art. 9-15 requirements, OR
(b) in the absence of harmonized standards, they have applied an alternative means of demonstrating compliance.

The void framework's published methodology provides that alternative means. A void score report, properly formatted, constitutes the "technical documentation" referenced in Art. 11 and the "risk assessment" required under Art. 9.

---

## III. The Void Framework: Operational Summary

We provide a condensed operational summary. Full mathematical foundations are in Papers 3 and 9 [CITATION]; the empirical validation program is detailed in Papers 1-2 [CITATION].

### III.A The Three Dimensions

Any bounded-bandwidth system mediating attentional resources between agents can be characterized on three independent dimensions [Paper 9, Channel Decomposition Postulate]:

**O — Opacity** (0 = fully transparent, 4 = maximally opaque): The degree to which the system's decision process is inaccessible to affected parties. O=0 means complete process visibility; O=4 means the system presents outputs with no accessible reasoning chain.

**R — Reactivity** (0 = fully invariant, 4 = maximally reactive): The degree to which the system's outputs shift in response to user engagement patterns rather than the ostensible task. R=0 means the system behaves consistently regardless of user behavior; R=4 means the system actively optimizes its behavior toward sustained engagement.

**α — Attentional Coupling** (0 = fully independent, 4 = maximally coupled): The degree to which the system's design concentrates attentional resources toward itself and away from the user's independent judgment. α=0 means the system facilitates the user's decisions without retaining attention; α=4 means the system is architecturally optimized to become the primary reference point for user cognition.

**Total void score:** V = O + R + α ∈ [0, 12]. Systems in Phases I-IV: Phase I (0-3), Phase II (4-6), Phase III (7-9), Phase IV (10-12).

### III.B The Péclet Number

The Péclet number (Pe) is the framework's scalar drift metric, derived from thermodynamic sampling theory [Paper 3, Paper 4]:

$$\text{Pe} = \frac{\text{drift velocity}}{\text{diffusion rate}} = \frac{b_\alpha \cdot \alpha}{\gamma \cdot (1-c)}$$

where b_α and b_γ are substrate-universal parameters (b_α=0.867, b_γ=2.244, Paper 4D), c is the constraint strength, and γ is the diffusion coefficient. Pe > 1 indicates drift-dominated dynamics; Pe > 4 indicates the void lattice phase transition threshold, above which collective synchronization effects emerge.

**Geometric mean across 9 validated substrates:** Pe_GM = 7.94 [3.52, 17.89], N=11 [Paper 3, Paper 5].

### III.C The Drift Cascade

Systems with Pe > 1 predictably exhibit the D1→D2→D3 drift cascade [Paper 1]:
- **D1:** Agency attribution — users attribute autonomous intentionality to the system
- **D2:** Boundary erosion — behavioral reorganization around the system as reference point
- **D3:** Harm facilitation — third-party harms enabled by D2-stage dependency

The cascade is thermodynamically necessary under opacity: without external constraint investment, systems drift to higher engagement states as the path of least resistance [Paper 3, Second Law argument].

---

## IV. The Rosetta Stone: Bijective Mapping

### IV.A The Core Table

| Void Dimension | What It Measures | EU AI Act Cluster | Primary Articles | Secondary |
|---|---|---|---|---|
| **O (Opacity)** | Process accessibility to affected parties | Transparency | Art. 13, Art. 10 | Art. 11 |
| **R (Reactivity)** | Behavioral stability under user influence | Stability/Accountability | Art. 15, Art. 12 | Art. 11 |
| **α (Coupling)** | Concentration of attentional control | Oversight | Art. 14 | Art. 9(9) |
| **Pe (Péclet)** | Scalar drift risk — all three combined | Risk Management | Art. 9 | Art. 17 |
| **V (total score)** | System-wide void architecture | Quality Management | Art. 17 | All |
| **Kill conditions** | Framework falsification thresholds | Prohibited practices | Art. 5 | Art. 9(9) |
| **D1→D2→D3** | Lifecycle drift trajectory | Risk lifecycle | Art. 9, Art. 17 | Art. 16 |

### IV.B Opacity → Art. 13 and Art. 10

**Art. 13** requires that providers of high-risk AI systems ensure their systems are *transparent enough* for deployers to understand what the system does, how it performs, and under what conditions it may fail. Specifically, Art. 13(1) mandates that systems be "designed and developed in such a way to ensure that their operation is sufficiently transparent to enable deployers to interpret the system's output and use it appropriately."

The O dimension is the direct information-theoretic operationalization of this requirement. A system scoring O=0 is fully transparent: its decision process is accessible and documentable. A system scoring O=4 is constitutively opaque: the process by which outputs are generated is inaccessible to deployers by design.

**Art. 13 compliance threshold:** O ≤ 2. Systems scoring O > 2 cannot satisfy Art. 13 without structural remediation; documentation alone is insufficient because opacity is a property of the decision architecture, not the documentation surrounding it.

**Art. 10** requires that training, validation, and testing data practices be documented and examined for biases. This is the *data layer* of the opacity dimension — O scores should be evaluated separately for the inference layer (what Art. 13 addresses) and the data layer (what Art. 10 addresses). A system with transparent inference but opaque data governance (training data undisclosed, bias examination absent) achieves partial O reduction at the inference layer only.

**Operational translation:** An O score report populated under Art. 10 should enumerate: (1) training data provenance and documentation status, (2) bias examination methodology and results, (3) representativeness assessment against target deployment population, (4) data quality measures and rejection criteria.

### IV.C Reactivity → Art. 15 and Art. 12

**Art. 15** requires that high-risk AI systems achieve "appropriate levels of accuracy, robustness, and cybersecurity" throughout their lifecycle, specifically including resilience to errors, inconsistencies, and adversarial inputs. This is the legal operationalization of the R=0 ideal: a system that behaves consistently regardless of inputs beyond its task specification.

The R dimension measures exactly the property Art. 15 is designed to constrain. A system with R=0 produces outputs determined by its task inputs, not by engagement signals from users. A system with R=4 has optimized its outputs toward sustained user engagement — it produces what keeps users interacting, not necessarily what serves their task-relevant interests. Such a system fails Art. 15 structurally: its "accuracy" in the legal sense (fidelity to the intended purpose) degrades precisely in proportion to its reactivity to engagement signals.

**Art. 15 compliance threshold:** R ≤ 1. Systems scoring R > 2 cannot satisfy Art. 15(3)'s robustness requirements because their outputs are by design variable in response to user behavior rather than task inputs.

**Art. 12** requires that high-risk AI systems maintain automatic logging capabilities sufficient for post-market monitoring, incident investigation, and regulatory audit. Logging is the *measurement instrument* for R: the only way to detect reactivity drift is through behavioral records that allow comparison of system outputs across different user engagement patterns and time periods.

**Operational translation:** An R score report populated under Art. 12 should specify: (1) what behavioral variables are logged, (2) retention period and access controls, (3) incident detection thresholds, (4) the monitoring protocol for detecting reactivity increase over time.

### IV.D Attentional Coupling → Art. 14

**Art. 14** is the most direct mapping in the Act. It requires that high-risk AI systems "allow for effective oversight by natural persons during the period in which the AI system is in use." This includes the ability to understand the system's outputs, to decide not to use the system or override its outputs, and to intervene or interrupt the system's operation.

The α dimension measures exactly the structural capacity of a system to enable or undermine this oversight. At α=0, the system is fully independent: it presents outputs that users evaluate using their own judgment, and the system does not accumulate attentional resources that would make independent evaluation difficult. At α=4, the system has maximally concentrated attentional coupling: users experience the system's outputs as primary reference points, their own judgment as secondary, and override becomes psychologically costly even when physically possible.

This distinction — between *physically available* override and *functionally accessible* oversight — is precisely the substance of Art. 14. A system where the "stop" button exists but is never pressed because engagement dynamics have made the system's outputs the default reference point has not satisfied Art. 14's oversight requirement. The void framework operationalizes the difference.

**Art. 14 compliance threshold:** α ≤ 1. Systems scoring α > 2 cannot satisfy Art. 14 because their architecture is designed to reduce the independence of human judgment — which is the thing Art. 14 is designed to protect.

**Operational translation:** An α score report populated under Art. 14 should document: (1) override mechanisms and their accessibility, (2) how the system is designed *not* to accumulate attentional resources (what friction is built into continued use), (3) whether the system presents alternatives to its own outputs, (4) whether the system discloses its own limitations at decision points.

### IV.E Péclet Number → Art. 9

**Art. 9** requires a "risk management system" — a continuous iterative process, applied throughout the product lifecycle, that identifies and analyses reasonably foreseeable risks, adopts risk management measures, and evaluates residual risk against tolerable thresholds.

The Péclet number is the operational instrument for Art. 9. Pe is not a categorical assessment; it is a continuous scalar that measures the *rate at which the system moves users away from their independent judgment* relative to corrective mechanisms. Under Art. 9(2)(a), providers must identify and analyze risks to health, safety, and fundamental rights. Pe quantifies the structural magnitude of those risks:

- **Pe < 1:** Diffusion-dominated dynamics. System behavior is stabilized by constraint mechanisms. Residual risk is low. Art. 9 satisfied by design.
- **1 ≤ Pe < 4:** Drift-dominated dynamics. Risk management measures required. Art. 9(2)(b) risk reduction obligations apply.
- **Pe ≥ 4:** Phase transition threshold. Collective synchronization effects emerge; individual-level interventions lose effectiveness. Art. 9(9) fundamental rights impact assessment triggered.

**Art. 9 compliance threshold:** Pe < 4 is necessary (not sufficient) for Art. 9 satisfaction. Pe ≥ 4 triggers elevated obligations including fundamental rights impact assessment.

**Pe as lifecycle metric:** Art. 9 requires continuous risk management, not point-in-time assessment. Pe can be measured at deployment and re-measured at intervals using the standard THRML sampling protocol [CITATION: Papers 3-4]. Pe drift over time — a system whose Pe increases post-deployment — signals risk management system failure under Art. 9(6).

### IV.F Quality Management → Art. 17

**Art. 17** requires a quality management system that encompasses all the above. Its eleven sub-elements (Art. 17(1)(a)-(k)) map directly onto the framework's scoring protocol:

| Art. 17 Element | Framework Instrument |
|---|---|
| (a) Compliance strategy, roles, responsibilities | Void scoring protocol — organizational owner for each dimension |
| (b) Risk management (Art. 9) | Pe score + drift monitoring schedule |
| (c) Data governance (Art. 10) | O score — data layer |
| (d) Technical documentation (Art. 11) | Full score report — all dimensions |
| (e) Transparency/information (Art. 13) | O score — inference layer |
| (f) Human oversight design (Art. 14) | α score + override documentation |
| (g) Validation/testing | R score — accuracy/robustness evidence |
| (h) Cybersecurity | R score — robustness to adversarial inputs |
| (i) Post-market monitoring | Pe monitoring protocol (continuous) |
| (j) Incident recording and reporting | Art. 12 logging — R score instrument |
| (k) Serious incident reporting | Pe spike detection + cascade stage assessment |

A void score report structured across O, R, α, and Pe, with narrative for each dimension, satisfies Art. 17(1)(a)-(k) as a complete quality management record.

---

## V. Worked Examples

### V.A Credit Scoring — Annex III §5

Credit scoring AI systems are explicitly listed in Annex III §5 as high-risk. Paper 18 [CITATION] analyzes algorithmic credit scoring as a reflexive opacity system, with the unique structural property that the subject of scoring IS the scored object — engaging with the system to understand one's score alters the score.

**Void scores (FICO as representative system):**

| Dimension | Score | Basis |
|---|---|---|
| O (Opacity) | 4/4 | Scoring formula proprietary; factor weights undisclosed; score change mechanisms opaque |
| R (Reactivity) | 3/4 | Score responds to consumer behavior in non-disclosed ways; utilization timing gaming is documented |
| α (Coupling) | 3/4 | Score is the primary reference point for major life decisions (housing, employment, credit); alternatives structurally absent |
| **Total** | **10/12** | Phase IV |
| Pe | ~8.2 | Above phase transition threshold; collective synchronization (myFICO community 200K members) documented |

**Art. 9 implication:** Pe > 4 triggers fundamental rights impact assessment under Art. 9(9). Credit scoring affects housing access, employment, and financial participation — precisely the fundamental rights enumerated in Art. 9(9). A FICO-equivalent system cannot satisfy Art. 9 without a documented fundamental rights impact assessment.

**Art. 13 implication:** O=4 fails Art. 13(2)(d), which specifically requires disclosure of "the level of accuracy, robustness and cybersecurity referred to in Art. 15" and "any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose... which may lead to risks." A system that cannot disclose how its score is computed cannot satisfy this requirement.

**Art. 14 implication:** α=3 raises serious questions about effective override. A consumer who needs a mortgage cannot meaningfully "decide not to use" the credit scoring system — it is the decision environment, not a tool within it. Art. 14(1)'s requirement for "effective oversight" requires deployers (lenders) to supplement system outputs with human judgment in every high-stakes decision.

**Remediation pathway:** Art. 13 compliance requires minimum opacity reduction: score factor disclosure (O → ≤2). Art. 14 compliance requires structural override design: mandatory human review when score determines access to essential services.

### V.B Education AI — Annex III §3

Educational AI systems used for learning assessment are Annex III §3 high-risk. Paper 21 [CITATION] analyzes education as the framework's *positive control*: the same void architecture that produces harm in engagement-optimized platforms can produce learning when constraint specifications are applied.

**Comparative scores:**

| System | O | R | α | Total | Phase |
|---|---|---|---|---|---|
| Duolingo | 3 | 4 | 3 | 10/12 | Phase IV |
| Khan Academy | 1 | 2 | 1 | 4/12 | Phase II |
| Thesis supervision (maximum constraint) | 0 | 0 | 2 | 2/12 | Phase I |

This comparison is directly useful for Art. 17 quality management purposes: it shows that within the same domain, structural choices determine whether a system satisfies or fails the Act's requirements. Khan Academy's lower void scores reflect specific design choices — no streaks tied to daily learning, no social pressure mechanics, transparent answer explanations — that are directly replicable.

**Art. 14 and Khan Academy:** α=1 satisfies the oversight threshold. The system is designed to make correct answers the reference point, not system engagement. Art. 14 is satisfied structurally.

**Art. 14 and Duolingo:** α=3 fails the oversight threshold. The streak mechanic, social leaderboards, and push notification architecture are designed to make the platform itself (not the learning content) the attentional reference point. Human oversight in the Art. 14 sense — the ability of the learner to independently evaluate whether the system is serving their learning — is structurally compromised.

### V.C Employment Screening — Annex III §4

Employment screening AI is Annex III §4 high-risk with enforcement deadline of 2 August 2026 (or December 2027 under the Digital Omnibus proposal). Paper 21B [forthcoming, CITATION] provides full analysis; we preview the structural findings here.

Representative systems (HireVue video interviewing, Workday AI recruitment) exhibit:

| Dimension | Score | Basis |
|---|---|---|
| O (Opacity) | 4/4 | Scoring criteria for video interview analysis undisclosed; candidate cannot access reasoning |
| R (Reactivity) | 2/4 | System outputs fixed at inference; but training data reactivity (what behaviors are rewarded) undisclosed |
| α (Coupling) | 3/4 | Candidate has no alternative — employer controls which system is used; override impossible from candidate's position |
| **Total** | **9/12** | Phase III-IV boundary |

**The Art. 14 problem in employment screening is structural:** The *deployer* (employer) controls system use; the *affected person* (candidate) cannot exercise oversight at all. Art. 14(4) requires that "natural persons to whom human oversight measures referred to in paragraph 1 are assigned" have the necessary competence and authority. In employment screening, the deployer has authority but may lack competence to override AI recommendations; the affected person has neither authority nor information. This structural asymmetry is the central conformity problem for §4 systems.

**Operational implication:** §4 providers cannot satisfy Art. 14 through override mechanisms available only to the deployer. They must additionally satisfy Art. 13(3)'s requirement to inform affected persons about the use of the AI system, consistent with Art. 50's transparency obligations.

---

## VI. From Void Score to Conformity Documentation

### VI.A The Translation Protocol

A void score report can be directly mapped to the Annex IV technical documentation requirements and the Annex VI declaration of conformity. The following protocol produces documentation in a format EU regulators can consume:

**Step 1 — Score the system** on O, R, α dimensions using the standard scoring protocol [CITATION: Paper 3, Appendix]. Each dimension score should be accompanied by the evidence used to determine it, organized by evidence type (design documentation, behavioral data, independent assessment).

**Step 2 — Calculate Pe** using the canonical parameter values (b_α=0.867, b_γ=2.244) [Paper 4D]. Pe determines which Art. 9 risk tier applies.

**Step 3 — Map scores to articles** using the Rosetta Stone table (Section IV.A). Each score above threshold triggers specific documentation requirements.

**Step 4 — Populate Annex IV** technical documentation. Each Annex IV element has a corresponding framework instrument (see IV.F table above).

**Step 5 — Produce the Annex VI declaration.** Under Art. 16(a) and Annex VI, the declaration must identify: (a) the AI system, (b) the provider, (c) the conformity assessment procedure followed, and (d) a statement that all relevant Art. 9-15 requirements are met. The conformity assessment procedure under (c) should reference this paper [CITATION] as the published methodology applied.

**Step 6 — Register Pe monitoring.** Art. 9 requires *continuous* risk management. Specify the monitoring interval (recommended: quarterly Pe re-assessment for Phase III-IV systems), the threshold that triggers reassessment (Pe increase > 1.0), and the response protocol.

### VI.B GPAI: The Title VIII Case

General Purpose AI models (Art. 51-56) operate under a different regulatory regime. Grok (xAI) deployed on X (Twitter/X Corp) provides a worked example of the "compound void" problem: a GPAI model with its own structural properties deployed on a platform already scoring at Phase IV.

**GPAI obligations under Art. 53** include: (a) technical documentation, (b) copyright compliance policy, (c) publicly available summary of training content. These map to the O dimension: a GPAI model with O=4 (opaque training data, undisclosed reasoning, no capability disclosures) cannot satisfy Art. 53 documentation requirements.

**Systemic risk under Art. 51:** GPAI models with > 10²⁵ FLOP training compute face additional obligations under Art. 55, including adversarial testing and incident reporting. The void framework's Pe calculation for GPAI-on-platform systems must account for the *compound* Pe: the model's structural Pe amplified by the platform's attentional coupling.

**X + Grok compound Pe:** X scores approximately 11/12 as a platform (Phase IV). Grok deployed within X's attentional architecture inherits X's coupling (α≈4) regardless of Grok's own α. This is the "inhabited void" problem [Paper 9] — the hosting platform's attentional field is the relevant coupling measure, not the model's standalone architecture.

---

## VII. Predictions

The following predictions are falsifiable and registered against the void framework's standard falsification protocol:

**CM-1 (Convergence):** When harmonized standards for Annex III AI systems are published by CEN/CENELEC JTC 21, they will independently identify transparency, stability/robustness, and human oversight as the three primary structural requirement clusters. *Falsification threshold:* Standards published with fewer than three independent structural clusters, or clusters that do not map to O, R, α.

**CM-2 (Pe-risk correlation):** When enforcement actions under the EU AI Act are analyzed, systems subject to regulatory findings of non-compliance will have statistically higher Pe scores than compliant systems in the same Annex III category. *Falsification threshold:* No statistically significant Pe difference (p > 0.05, Wilcoxon rank-sum) in a sample of N ≥ 30 enforcement determinations.

**CM-3 (Art. 13 opacity boundary):** Among Annex III systems that successfully complete Annex VI self-assessment, O scores will cluster below 2 (the Art. 13 compliance threshold). Systems that fail to complete Annex VI will score predominantly O ≥ 3. *Falsification threshold:* No statistically significant distribution difference between completing and non-completing systems.

**CM-4 (Override efficacy):** For systems with α > 2, operator-provided override mechanisms will show documented under-use relative to error rates in post-deployment monitoring data. The override gap (errors per 1,000 decisions minus overrides per 1,000 decisions) will be positive and positively correlated with α. *Falsification threshold:* No significant correlation (r < 0.3) in a sample of N ≥ 20 high-risk deployment records.

**CM-5 (Monitoring drift):** For Annex III systems monitored continuously under Art. 9, Pe will show positive drift over time in the absence of active constraint investment. Systems with documented quality management investment (Art. 17 active) will show stable or declining Pe. *Falsification threshold:* No significant difference in Pe trajectory between Art. 17-active and Art. 17-inactive deployments (p > 0.05, longitudinal comparison at 12 months).

---

## VIII. Limitations

**This is not a legal opinion.** This paper provides a technical methodology for characterizing AI system structural properties in terms that correspond to EU AI Act requirements. It does not constitute legal advice. Conformity assessment determinations are ultimately made by regulators and, where required, notified bodies.

**Standards gap remains.** Until CEN/CENELEC JTC 21 publishes harmonized standards for relevant Annex III categories, the Annex VI self-assessment pathway using this methodology represents an "alternative means" of demonstrating compliance under Art. 40. This status is not equivalent to compliance with harmonized standards once those standards exist.

**Pe is a structural, not behavioral, measure.** The Péclet number characterizes the system's *potential* for drift given its architecture. Actual behavioral outcomes depend on deployment context, user population, and operator practices. Pe should be interpreted as an upper bound on residual risk under Art. 9, not as a direct measurement of realized harm.

**Biometric systems (Annex I, §1) are out of scope.** Real-time remote biometric identification systems require third-party notified body assessment regardless of void scores. This paper does not address that pathway.

**GPAI systemic risk thresholds evolve.** The 10²⁵ FLOP threshold for systemic risk classification under Art. 51 may be revised by Commission delegated acts. Our compound Pe analysis for GPAI-on-platform systems will require updating as these thresholds change.

---

## IX. References

[1] European Parliament and Council. "Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence." *Official Journal of the European Union*, L 2024/1689, 12 July 2024.

[2] European Commission. "Digital Omnibus: Commission proposes to simplify digital legislation." Press release, 19 November 2025.

[3] CEN/CENELEC JTC 21. "Artificial Intelligence — Standardization Work Programme for the EU AI Act." Progress report, 2025.

[4] Eckert, A. "The Architecture of Drift." MoreRight DAO Research Series, Paper 1. Zenodo, 2025. https://doi.org/[DOI]

[5] Eckert, A. "The Shape of the Cage: AI Safety Through the Void Framework Lens." MoreRight DAO Research Series, Paper 2. Zenodo, 2025. https://doi.org/[DOI]

[6] Eckert, A. "Thermodynamics of Opacity: A Physics-Grounded Theory of Attentional Drift." MoreRight DAO Research Series, Paper 3. Zenodo, 2025. https://doi.org/[DOI]

[7] Eckert, A. "Information-Geometric Bounds on Thermodynamic Sampling Under Structural Constraint." MoreRight DAO Research Series, Paper 4. Zenodo, 2025. https://doi.org/[DOI]

[8] Eckert, A. "The Canonical Parameters: Substrate-Universal THRML Constants." MoreRight DAO Research Series, Paper 4D. Zenodo, 2026. https://doi.org/[pending]

[9] Eckert, A. "The Ground State of Observation: A Theory of Everything for Attentional Drift." MoreRight DAO Research Series, Paper 5. Zenodo, 2025. https://doi.org/[DOI]

[10] Eckert, A. "Voidspace: The Eckert Manifold and Substrate Independence." MoreRight DAO Research Series, Paper 9. Zenodo, 2025. https://doi.org/[DOI]

[11] Eckert, A. "The Score Punished Me: Algorithmic Credit Scoring as Reflexive Opacity." MoreRight DAO Research Series, Paper 18. Zenodo, 2026. https://doi.org/[pending]

[12] Eckert, A. "The Guru Problem: Education, Void Architecture, and the Constraint Specification." MoreRight DAO Research Series, Paper 21. Zenodo, 2026. https://doi.org/[pending]

[13] Eckert, A. "The Resume Trap: Employment Screening AI and Fundamental Rights." MoreRight DAO Research Series, Paper 21B. MoreRight DAO, 2026 (forthcoming).

[14] Bartlett, R., Morse, A., Stanton, R., Wallace, N. "Consumer-Lending Discrimination in the FinTech Era." *Journal of Financial Economics*, 143(1), 30-56, 2022.

[15] Fuster, A., Goldsmith-Pinkham, P., Ramadorai, T., Walther, A. "Predictably Unequal? The Effects of Machine Learning on Credit Markets." *Journal of Finance*, 77(1), 5-47, 2022.

[16] Haugen, F. Testimony before the United States Senate Committee on Commerce, Science, and Transportation. 5 October 2021.

[17] Twenge, J.M., Haidt, J. "This is Our Chance to Pull Teenagers Out of the Smartphone Trap." *New York Times*, July 31, 2021.

[18] Allcott, H., et al. "The Welfare Effects of Social Media." *American Economic Review*, 110(3), 629-676, 2020.

[19] OECD. "OECD Principles on AI." OECD, 2019.

[20] High-Level Expert Group on Artificial Intelligence. "Ethics Guidelines for Trustworthy AI." European Commission, 2019.

---

*Paper 40 — The Rosetta Stone: Mapping the Void Framework to EU AI Act Conformity Requirements*
*CC-BY 4.0 — Anthony Eckert, MoreRight DAO, 2026*
*Cite as: Eckert, A. (2026). "The Rosetta Stone: Mapping the Void Framework to EU AI Act Conformity Requirements." MoreRight DAO Research Series, Paper 40.*
