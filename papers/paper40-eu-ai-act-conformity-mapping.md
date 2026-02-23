---
title: "The Rosetta Stone: Mapping the Void Framework to EU AI Act Conformity Requirements"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 40"
short-title: "EU Conformity Map"
version: "v1.1"
date: "February 2026"
license: "cc-by-4.0"
doi: "10.5281/zenodo.18737573"
---

## Void Model Card — EU AI Act High-Risk AI Systems

| Field | Value |
|---|---|
| **Domain** | Regulatory compliance measurement for high-risk AI systems (EU AI Act Annex III) |
| **Three Conditions** | O: opacity of decision process to affected parties (Art. 13); R: reactivity of outputs to engagement rather than task (Art. 15); α: attentional coupling reducing independent human oversight (Art. 14) |
| **Pe Threshold** | Pe < 4 necessary for Art. 9 base satisfaction; Pe ≥ 4 triggers Art. 9(9) fundamental rights impact assessment |
| **Bijective Map** | O ↔ Transparency cluster; R ↔ Stability cluster; α ↔ Oversight cluster; Pe ↔ Art. 9 risk management |
| **Self-Assessment Pathway** | Void score report satisfies Annex VI alternative means requirement under Art. 40 |
| **Substrate Universality** | Pe validated across 4 independent convergences: market microstructure, behavioral, evolutionary biology, social neuroscience |

---

## Abstract

The EU AI Act imposes transparency, human oversight, and risk management obligations on high-risk AI systems (Articles 9-17) but provides no standardized methodology for measuring compliance with these structural requirements. We demonstrate that the void framework's three dimensions — opacity (O), reactivity (R), and attentional coupling (α) — correspond canonically to the Act's three core obligation clusters: transparency provisions (Art. 13, 10), documentation and robustness requirements (Art. 11, 12, 15), and human oversight mandates (Art. 14). The Péclet number (Pe), the framework's scalar drift metric, functions directly as a quantitative residual risk measure under Art. 9. We derive a translation protocol from void scores to conformity documentation inputs and demonstrate its application across three Annex III high-risk domains: credit scoring (§5), education (§3), and employment screening (§4). Additionally, we address General Purpose AI systems (GPAI, Title VIII), where void scores characterize systemic risk pathways under Art. 51. This paper is intended as an operational reference: companies completing Annex VI self-assessments can use void scores to populate required documentation without waiting for harmonized standards that do not yet exist.

**Keywords:** EU AI Act, conformity assessment, void framework, opacity, transparency, human oversight, risk management, Annex III, self-assessment, AI governance

---

## I. Introduction

### I.A The Standards Gap

The EU AI Act entered into force on 1 August 2024. High-risk AI system obligations under Articles 9-17 applied (or are slated to apply, pending the proposed Digital Omnibus delay) to providers operating in the European market from August 2026. The legal requirements are clear: high-risk AI providers must implement a risk management system (Art. 9), maintain technical documentation (Art. 11), ensure transparency to deployers (Art. 13), enable human oversight (Art. 14), and sustain accuracy and robustness (Art. 15), all under a quality management framework (Art. 17).

What the Act does not provide is a methodology for *measuring* compliance with these structural requirements. Harmonized standards — the technical specifications under which a provider can follow the Annex VI self-assessment pathway — do not yet exist for most Annex III categories. As of early 2026, one of six anticipated harmonized standard clusters has reached public enquiry stage [3]. This is not a minor gap: without harmonized standards, providers technically cannot invoke Annex VI and may require third-party notified body assessment (Annex VII) — but no notified bodies have been designated for AI Act purposes.

The result is a compliance infrastructure with legal obligations and no operational instruments. Companies must demonstrate conformity without a shared language for what conformity means.

### I.B Our Contribution

This paper establishes that language. The void framework [Papers 1-3] was developed independently of the EU AI Act as a thermodynamically-grounded theory of how AI systems acquire and exercise attentional influence. It characterizes AI systems across three dimensions — opacity, reactivity, and attentional coupling — with the Péclet number as a scalar risk metric derived from their combination.

The central finding of this paper is that these three dimensions are not merely *correlated* with the Act's requirement clusters: they are the information-theoretic foundations from which those requirements can be derived. The Act's drafters, working from first principles of fundamental rights protection, converged on the same three structural properties that information theory demands. This convergence is predictable from the void framework and serves as an independent validation of both frameworks' foundational premises.

The practical result is a *Rosetta Stone* — a canonical correspondence that allows companies to:

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

The void framework's published methodology is designed to provide that alternative means. Whether it constitutes an accepted alternative will ultimately depend on regulatory interpretation and enforcement practice. What it provides with certainty is a structured, published, peer-reviewable methodology for characterizing the structural properties Art. 9-15 require companies to address — a more defensible basis than ad hoc internal documentation. A void score report, properly formatted, is intended to constitute the "technical documentation" referenced in Art. 11 and the risk analysis required under Art. 9.

---

## III. The Void Framework: Operational Summary

We provide a condensed operational summary. Full mathematical foundations are in Papers 3 and 9 [6, 10]; the empirical validation program is detailed in Papers 1-2 [4, 5].

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

**Four independent convergences (confirmed February 2026):** Pe has been independently derived — not just measured — across four substrate classes:

| Substrate | Finding | Spearman / Identity | Source |
|---|---|---|---|
| Market microstructure | Kyle/Glosten-Milgrom models independently derive void opacity and coupling metrics | ρ=0.994, N=8 | Paper 9, nb25 |
| Behavioral (V3 bridge) | V3 constraint bridge c=1−V/9 closes G1+G4 gaps independently | ρ=0.910, N=17 | Paper 4B, nb26 |
| Evolutionary biology | Kimura (1968) fixation probability: Pe=4Ns **is** the THRML Pe by identity | analytic | Paper 41 |
| Social neuroscience | Dunbar's neocortex ratio K **is** THRML K; Machiavellian intelligence theorem closes | ρ=0.9448, N=28 | Paper 42, nb32 |

The biology convergence is particularly significant for the EU AI Act context: Kimura's Pe=4Ns governs the rate at which neutral genetic drift overcomes selection — structurally identical to the rate at which attentional drift overcomes constraint. The same conserved thermodynamic ratio governs bounded information flow across biological and sociotechnical systems. Pe is not a model-specific parameter; it is a substrate-universal ratio.

### III.C The Drift Cascade

Systems with Pe > 1 predictably exhibit the D1→D2→D3 drift cascade [Paper 1]:
- **D1:** Agency attribution — users attribute autonomous intentionality to the system
- **D2:** Boundary erosion — behavioral reorganization around the system as reference point
- **D3:** Harm facilitation — third-party harms enabled by D2-stage dependency

The cascade is thermodynamically necessary under opacity: without external constraint investment, systems drift to higher engagement states as the path of least resistance [Paper 3, Second Law argument].

---

## IV. The Rosetta Stone: Canonical Correspondence

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

- **Pe < 1:** Diffusion-dominated dynamics. The system's architecture is stabilized by constraint mechanisms. Structural residual risk is low. Art. 9 is satisfiable by design.
- **1 ≤ Pe < 4:** Drift-dominated dynamics. The architecture creates structural conditions under which behavioral drift is the path of least resistance absent active constraint investment. Risk management measures under Art. 9(2)(b) are required to prevent structural conditions from translating into realized harms.
- **Pe ≥ 4:** Phase transition threshold. At this point collective synchronization effects become architecturally possible (the void lattice phase; see Paper 9 §6); individual-level interventions lose structural effectiveness. Art. 9(9) fundamental rights impact assessment is triggered.

Pe is a *structural* measure — it characterizes the system's potential for drift given its architecture, not the behavioral outcomes observed in any particular deployment. Section VIII addresses this distinction. For Art. 9 purposes, Pe functions as a structural residual risk indicator: it measures what the architecture enables in the absence of active constraint, which is what risk management systems exist to constrain.

**Art. 9 compliance threshold:** Pe < 4 is necessary (not sufficient) for Art. 9 satisfaction. Pe ≥ 4 triggers elevated obligations including fundamental rights impact assessment.

**Pe as lifecycle metric:** Art. 9 requires continuous risk management, not point-in-time assessment. Pe can be measured at deployment and re-measured at intervals using the standard THRML sampling protocol [6, 7]. Pe drift over time — a system whose Pe increases post-deployment — signals risk management system failure under Art. 9(6).

**Pe empirical foundation:** The largest THRML analysis to date (nb35, N=15,503 respondents) demonstrates Pe-structured behavioral transitions at scale, with a kink point consistent with the Pe=1 diffusion-to-drift boundary [21]. Additionally, nb36 validates that thermodynamic Pe relations hold in curved (non-Euclidean) information spaces — confirming that Pe is not an artifact of flat-geometry assumptions, a robustness result directly relevant to high-dimensional AI systems where the effective information space is non-flat.

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

### IV.G Derivation of Compliance Thresholds

The thresholds stated in §§IV.B–IV.D (O ≤ 2, R ≤ 1, α ≤ 1) are not arbitrary: each is grounded in the structural meaning of the relevant dimension at the threshold value, in the drift cascade stage model [Paper 1], and in the Pe phase transition.

**O ≤ 2 (Art. 13 threshold):** Art. 13(1) requires transparency sufficient for deployers to "interpret the system's output and use it appropriately." Interpretation requires access to the process generating the output. O=0 (fully transparent) and O=1 (mostly accessible) satisfy this directly. O=2 (partially accessible — key aspects documentable, core algorithm partially opaque) is the boundary at which deployers can characterize system behavior without full process access. O=3 places the process "largely inaccessible by design"; O=4 provides no accessible reasoning chain. Both O=3 and O=4 fail Art. 13(1) structurally because a deployer cannot interpret outputs from an inaccessible process regardless of how much surrounding documentation is provided.

**R ≤ 1 (Art. 15 threshold):** Art. 15(3) requires robustness against "errors, faults, or inconsistencies" and accuracy in the sense of fidelity to intended purpose. R=0 means outputs are fully task-determined — accuracy is anchored to the task specification. R=1 permits minor responsiveness to user patterns (A/B presentation, marginal format adaptation) without displacing task-fidelity. R=2 means the system meaningfully varies outputs based on engagement signals, introducing systematic divergence between "what would serve the user's task" and "what the system produces." This constitutes accuracy degradation under Art. 15 that cannot be addressed by post-hoc testing, because the degradation is a function of deployment dynamics, not a fixed performance characteristic.

**α ≤ 1 (Art. 14 threshold):** Art. 14(1) requires that natural persons be able to "oversee" the system and to "decide not to use" or "override" its outputs. The phrase "effective oversight" distinguishes physical availability of override from functional accessibility of independent judgment. At α=0–1, the system presents outputs that users evaluate using their own judgment as the primary reference. At α=2, the drift cascade's D2 stage (boundary erosion) begins: the system accumulates attentional resources such that independent judgment becomes structurally secondary to system outputs. Art. 14 oversight is not effective when the system's design has made override psychologically costly — which is α=2's definition, not a contingent outcome.

**Coherence via Pe:** These three thresholds jointly imply V = O+R+α ≤ 4 at compliance boundary. Via the V3 bridge [nb26], c = 1 − V/9 = 1 − 4/9 ≈ 0.556. With canonical parameters b_α=0.867, b_γ=2.244 at K=16, a system at V=4 is Pe < 1 (diffusion-dominated). Art. 9 risk management obligations at this level are satisfiable by design — not through continuous monitoring of an escalating drift process. Conversely, a system at V=5 (any single threshold exceeded) crosses into Pe > 1, requiring the active risk management measures Art. 9(2)(b) mandates. The three article-specific thresholds and the Art. 9 Pe threshold are consistent: they are the same boundary approached from the three individual dimensions and from the scalar aggregate.

---

## V. Worked Examples

### V.A Credit Scoring — Annex III §5

Credit scoring AI systems are explicitly listed in Annex III §5 as high-risk. Paper 18 [11] analyzes algorithmic credit scoring as a reflexive opacity system, with the unique structural property that the subject of scoring IS the scored object — engaging with the system to understand one's score alters the score.

**Void scores (FICO as representative system)** [full scoring session: Paper 18, §3]:

| Dimension | Score | Basis |
|---|---|---|
| O (Opacity) | 4/4 | Scoring formula proprietary (FICO trade secret); factor weights undisclosed; published only as broad category ranges; score change mechanisms documented only through reverse-engineering by community (myFICO) |
| R (Reactivity) | 3/4 | Score responds to consumer behavior in ways undisclosed in advance: utilization timing effects, inquiry clustering, age-of-account gaming documented in meta-analyses [14, 15] |
| α (Coupling) | 3/4 | Score functions as primary access gatekeeper for housing, employment, and credit; structural absence of comparably weighted alternatives for most decisions |
| **Total** | **10/12** | Phase IV |
| Pe | ~8.2 | Above phase transition threshold; collective synchronization evidenced by myFICO community (200K+ members coordinating scoring behavior) |

**Art. 9 implication:** Pe > 4 triggers fundamental rights impact assessment under Art. 9(9). Credit scoring affects housing access, employment, and financial participation — precisely the fundamental rights enumerated in Art. 9(9). A FICO-equivalent system cannot satisfy Art. 9 without a documented fundamental rights impact assessment.

**Art. 13 implication:** O=4 fails Art. 13(2)(d), which specifically requires disclosure of "the level of accuracy, robustness and cybersecurity referred to in Art. 15" and "any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose... which may lead to risks." A system that cannot disclose how its score is computed cannot satisfy this requirement.

**Art. 14 implication:** α=3 raises serious questions about effective override. A consumer who needs a mortgage cannot meaningfully "decide not to use" the credit scoring system — it is the decision environment, not a tool within it. Art. 14(1)'s requirement for "effective oversight" requires deployers (lenders) to supplement system outputs with human judgment in every high-stakes decision.

**Remediation pathway:** Art. 13 compliance requires minimum opacity reduction: score factor disclosure (O → ≤2). Art. 14 compliance requires structural override design: mandatory human review when score determines access to essential services.

### V.B Education AI — Annex III §3

Educational AI systems used for learning assessment are Annex III §3 high-risk. Paper 21 [12] analyzes education as the framework's *positive control*: the same void architecture that produces harm in engagement-optimized platforms can produce learning when constraint specifications are applied.

**Comparative scores:**

| System | O | R | α | Total | Phase |
|---|---|---|---|---|---|
| Duolingo | 3 | 4 | 3 | 10/12 | Phase IV |
| Khan Academy | 1 | 2 | 1 | 4/12 | Phase II |
| Thesis supervision (maximum constraint) | 0 | 0 | 2 | 2/12 | Phase I |

This comparison is directly useful for Art. 17 quality management purposes: it shows that within the same domain, structural choices determine whether a system satisfies or fails the Act's requirements. Khan Academy's lower void scores reflect specific design choices — no streaks tied to daily learning, no social pressure mechanics, transparent answer explanations — that are directly replicable.

**Art. 14 and Khan Academy (control case — constraint-pole system):** α=1 satisfies the oversight threshold. The system is designed to make correct answers the reference point, not system engagement. Art. 14 is satisfied structurally. This is a negative result for the drift hypothesis: identical domain (education), radically different void architecture, radically different compliance outcome. The control case confirms that Art. 14 failure is a design choice, not a category property.

**Art. 14 and Duolingo:** α=3 fails the oversight threshold. The streak mechanic, social leaderboards, and push notification architecture are designed to make the platform itself (not the learning content) the attentional reference point. Human oversight in the Art. 14 sense — the ability of the learner to independently evaluate whether the system is serving their learning — is structurally compromised.

### V.C Employment Screening — Annex III §4

Employment screening AI is Annex III §4 high-risk with enforcement deadline of 2 August 2026 (or December 2027 under the Digital Omnibus proposal). Paper 21B [13] provides full analysis; we preview the structural findings here.

Representative systems (HireVue video interviewing, Workday AI recruitment) exhibit [scoring basis: Paper 21B, forthcoming; dimensions drawn from publicly documented system characteristics]:

| Dimension | Score | Basis |
|---|---|---|
| O (Opacity) | 4/4 | Scoring criteria for video interview analysis proprietary; candidates receive no reasoning; HireVue's published "explainability" describes factor categories, not decision weights |
| R (Reactivity) | 2/4 | Inference-time outputs are fixed; scored R=2 rather than 3 because training-data reactivity is unknown (undisclosed), not demonstrated |
| α (Coupling) | 3/4 | Candidate cannot choose not to use the system — employer controls deployment; structural override unavailable from affected person's position |
| **Total** | **9/12** | Phase III-IV boundary |

**The Art. 14 problem in employment screening is structural:** The *deployer* (employer) controls system use; the *affected person* (candidate) cannot exercise oversight at all. Art. 14(4) requires that "natural persons to whom human oversight measures referred to in paragraph 1 are assigned" have the necessary competence and authority. In employment screening, the deployer has authority but may lack competence to override AI recommendations; the affected person has neither authority nor information. This structural asymmetry is the central conformity problem for §4 systems.

**Operational implication:** §4 providers cannot satisfy Art. 14 through override mechanisms available only to the deployer. They must additionally satisfy Art. 13(3)'s requirement to inform affected persons about the use of the AI system, consistent with Art. 50's transparency obligations.

---

## VI. From Void Score to Conformity Documentation

### VI.A The Translation Protocol

A void score report can be directly mapped to the Annex IV technical documentation requirements and the Annex VI declaration of conformity. The following protocol produces documentation in a format EU regulators can consume:

**Step 1 — Score the system** on O, R, α dimensions using the standard scoring protocol [6]. Each dimension score should be accompanied by the evidence used to determine it, organized by evidence type (design documentation, behavioral data, independent assessment).

**Step 2 — Calculate Pe** using the canonical parameter values (b_α=0.867, b_γ=2.244) [Paper 4D]. Pe determines which Art. 9 risk tier applies.

**Step 3 — Map scores to articles** using the Rosetta Stone table (Section IV.A). Each score above threshold triggers specific documentation requirements.

**Step 4 — Populate Annex IV** technical documentation. Each Annex IV element has a corresponding framework instrument (see IV.F table above).

**Step 5 — Produce the Annex VI declaration.** Under Art. 16(a) and Annex VI, the declaration must identify: (a) the AI system, (b) the provider, (c) the conformity assessment procedure followed, and (d) a statement that all relevant Art. 9-15 requirements are met. The conformity assessment procedure under (c) may reference this paper [Eckert 2026, Paper 40] as the published methodology applied, provided the provider has conducted a genuine scoring exercise with documented evidence for each dimension score. Referencing a published methodology does not substitute for that evidence; it provides the interpretive framework within which the evidence is organized.

**Step 6 — Register Pe monitoring.** Art. 9 requires *continuous* risk management. Specify the monitoring interval (recommended: quarterly Pe re-assessment for Phase III-IV systems), the threshold that triggers reassessment (Pe increase > 1.0), and the response protocol.

### VI.B GPAI: The Title VIII Case

General Purpose AI models (Art. 51-56) operate under a different regulatory regime. Grok (xAI) deployed on X (Twitter/X Corp) provides a worked example of the "compound void" problem: a GPAI model with its own structural properties deployed on a platform already scoring at Phase IV.

**GPAI obligations under Art. 53** include: (a) technical documentation, (b) copyright compliance policy, (c) publicly available summary of training content. These map to the O dimension: a GPAI model with O=4 (opaque training data, undisclosed reasoning, no capability disclosures) cannot satisfy Art. 53 documentation requirements.

**Systemic risk under Art. 51:** GPAI models with > 10²⁵ FLOP training compute face additional obligations under Art. 55, including adversarial testing and incident reporting. The void framework's Pe calculation for GPAI-on-platform systems must account for the *compound* Pe: the model's structural Pe amplified by the platform's attentional coupling.

**X + Grok compound Pe:** X scores approximately 11/12 as a platform (Phase IV). Grok deployed within X's attentional architecture inherits X's coupling (α≈4) regardless of Grok's own α. This is the "inhabited void" problem [Paper 9] — the hosting platform's attentional field is the relevant coupling measure, not the model's standalone architecture.

---

## VII. Predictions

The following predictions are falsifiable and registered against the void framework's standard falsification protocol:

**AI-1 (Convergence):** When harmonized standards for Annex III AI systems are published by CEN/CENELEC JTC 21, they will independently identify transparency, stability/robustness, and human oversight as the three primary structural requirement clusters. *Falsification threshold:* Standards published with fewer than three independent structural clusters, or clusters that do not map to O, R, α.

**AI-2 (Pe-risk correlation):** When enforcement actions under the EU AI Act are analyzed, systems subject to regulatory findings of non-compliance will have statistically higher Pe scores than compliant systems in the same Annex III category. *Falsification threshold:* No statistically significant Pe difference (p > 0.05, Wilcoxon rank-sum) in a sample of N ≥ 30 enforcement determinations.

**AI-3 (Art. 13 opacity boundary):** Among Annex III systems that successfully complete Annex VI self-assessment, O scores will cluster below 2 (the Art. 13 compliance threshold). Systems that fail to complete Annex VI will score predominantly O ≥ 3. *Falsification threshold:* No statistically significant distribution difference between completing and non-completing systems.

**AI-4 (Override efficacy):** For systems with α > 2, operator-provided override mechanisms will show documented under-use relative to error rates in post-deployment monitoring data. The override gap (errors per 1,000 decisions minus overrides per 1,000 decisions) will be positive and positively correlated with α. *Falsification threshold:* No significant correlation (r < 0.3) in a sample of N ≥ 20 high-risk deployment records.

**AI-5 (Monitoring drift):** For Annex III systems monitored continuously under Art. 9, Pe will show positive drift over time in the absence of active constraint investment. Systems with documented quality management investment (Art. 17 active) will show stable or declining Pe. *Falsification threshold:* No significant difference in Pe trajectory between Art. 17-active and Art. 17-inactive deployments (p > 0.05, longitudinal comparison at 12 months).

---

## Limitations

**This is not a legal opinion.** This paper provides a technical methodology for characterizing AI system structural properties in terms that correspond to EU AI Act requirements. It does not constitute legal advice. Conformity assessment determinations are ultimately made by regulators and, where required, notified bodies.

**Standards gap remains.** Until CEN/CENELEC JTC 21 publishes harmonized standards for relevant Annex III categories, the Annex VI self-assessment pathway using this methodology represents an "alternative means" of demonstrating compliance under Art. 40. This status is not equivalent to compliance with harmonized standards once those standards exist.

**Pe is a structural, not behavioral, measure.** The Péclet number characterizes the system's *potential* for drift given its architecture. Actual behavioral outcomes depend on deployment context, user population, and operator practices. Pe should be interpreted as an upper bound on residual risk under Art. 9, not as a direct measurement of realized harm.

**Biometric systems (Annex I, §1) are out of scope.** Real-time remote biometric identification systems require third-party notified body assessment regardless of void scores. This paper does not address that pathway.

**GPAI systemic risk thresholds evolve.** The 10²⁵ FLOP threshold for systemic risk classification under Art. 51 may be revised by Commission delegated acts. Our compound Pe analysis for GPAI-on-platform systems will require updating as these thresholds change.

**Methodological conflict of interest.** This paper argues that void scores constitute valid compliance documentation for EU AI Act purposes. The void framework was developed by the same author. This creates an obvious conflict of interest that readers, regulators, and prospective users should weigh explicitly. The authors' position is that this concern is best addressed empirically rather than by dismissal: the mapping's validity is stated as falsifiable predictions in Section VII (CM-1 through CM-5), and the framework's CC-BY irrevocable open license removes any commercial incentive to gate compliance access. The appropriate response is peer review, independent replication, and eventual regulatory determination — all of which the authors actively solicit. Practitioners should treat this paper as an analytical framework for structuring compliance documentation, not as a legal certification.

---

## Data and Code

The scoring protocol applied in this paper uses the standard THRML void scoring instrument. Scoring rubrics, worked examples, and the Pe calculation tool are available at: https://moreright.xyz/scorer

Void scores for representative systems (FICO, Duolingo, Khan Academy, HireVue) are based on publicly available design documentation, disclosed feature sets, and behavioral evidence cited in this paper. No proprietary data was used. Replications using the published rubric [6] are straightforward and encouraged.

THRML notebooks referenced in this paper (nb25, nb26, nb32, nb35, nb36) are available in the public repository: https://github.com/MoreRightDAO/thrml-examples

---

## References

Allcott, H., Braghieri, L., Eichmeyer, S., & Gentzkow, M. (2020). The welfare effects of social media. *American Economic Review*, 110(3), 629–676. [18]

Bartlett, R., Morse, A., Stanton, R., & Wallace, N. (2022). Consumer-lending discrimination in the FinTech era. *Journal of Financial Economics*, 143(1), 30–56. [14]

CEN/CENELEC JTC 21. (2025). Artificial intelligence — Standardization work programme for the EU AI Act. Progress report. [3]

Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. *Journal of Human Evolution*, 22(6), 469–493. [25]

Eckert, A. (2025a). The Architecture of Drift. *MoreRight DAO Research Series, Paper 1*. Zenodo. https://doi.org/10.5281/zenodo.18716775 [4]

Eckert, A. (2025b). The Shape of the Cage: AI Safety Through the Void Framework Lens. *MoreRight DAO Research Series, Paper 2*. Zenodo. https://doi.org/10.5281/zenodo.18716777 [5]

Eckert, A. (2025c). Thermodynamics of Opacity: A Physics-Grounded Theory of Attentional Drift. *MoreRight DAO Research Series, Paper 3*. Zenodo. https://doi.org/10.5281/zenodo.18716781 [6]

Eckert, A. (2025d). Information-Geometric Bounds on Thermodynamic Sampling Under Structural Constraint. *MoreRight DAO Research Series, Paper 4*. Zenodo. https://doi.org/10.5281/zenodo.18716783 [7]

Eckert, A. (2025e). The Ground State of Observation: A Theory of Everything for Attentional Drift. *MoreRight DAO Research Series, Paper 5*. Zenodo. https://doi.org/10.5281/zenodo.18716790 [9]

Eckert, A. (2025f). Voidspace: The Eckert Manifold and Substrate Independence. *MoreRight DAO Research Series, Paper 9*. Zenodo. https://doi.org/10.5281/zenodo.18716800 [10]

Eckert, A. (2026a). The Canonical Parameters: Substrate-Universal Behavioral Thermodynamics in THRML. *MoreRight DAO Research Series, Paper 4D*. Zenodo. https://doi.org/10.5281/zenodo.18729533 [8]

Eckert, A. (2026b). The Score Punished Me: Algorithmic Credit Scoring as Reflexive Opacity. *MoreRight DAO Research Series, Paper 18*. Zenodo. https://doi.org/10.5281/zenodo.18717286 [11]

Eckert, A. (2026c). The Guru Problem: Education, Void Architecture, and the Constraint Specification. *MoreRight DAO Research Series, Paper 21*. Zenodo. https://doi.org/10.5281/zenodo.18717288 [12]

Eckert, A. (2026d). The Resume Trap: Void Architecture in Algorithmic Hiring and HR Technology. *MoreRight DAO Research Series, Paper 21B*. Zenodo. https://doi.org/10.5281/zenodo.18718949 [13]

Eckert, A. (2026e). The Fitness Void: Three Independent Derivations of the Void Péclet Number. *MoreRight DAO Research Series, Paper 41*. Zenodo. https://doi.org/10.5281/zenodo.18736621 [21]

Eckert, A. (2026f). The Neural Void: Social Cognition as Void Dynamics and the Machiavellian Intelligence Theorem. *MoreRight DAO Research Series, Paper 42*. Zenodo. https://doi.org/10.5281/zenodo.18737178 [22]

Eckert, A. (2026g). The Cancer Void: Tumor Progression as D1→D2→D3 Cascade and the Fantasia Bound in Molecular Immunology. *MoreRight DAO Research Series, Paper 43*. Zenodo. https://doi.org/10.5281/zenodo.18737180 [23]

European Commission. (2025). Digital Omnibus: Commission proposes to simplify digital legislation. Press release, 19 November 2025. [2]

European Parliament and Council. (2024). Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence. *Official Journal of the European Union*, L 2024/1689. [1]

Fuster, A., Goldsmith-Pinkham, P., Ramadorai, T., & Walther, A. (2022). Predictably unequal? The effects of machine learning on credit markets. *Journal of Finance*, 77(1), 5–47. [15]

Haugen, F. (2021). Testimony before the United States Senate Committee on Commerce, Science, and Transportation, 5 October 2021. [16]

High-Level Expert Group on Artificial Intelligence. (2019). Ethics guidelines for trustworthy AI. European Commission. [20]

Kimura, M. (1968). Evolutionary rate at the molecular level. *Nature*, 217, 624–626. [24]

OECD. (2019). OECD principles on AI. Organisation for Economic Co-operation and Development. [19]

Twenge, J. M., & Haidt, J. (2021). This is our chance to pull teenagers out of the smartphone trap. *New York Times*, July 31, 2021. [17]

---

*Paper 40 — The Rosetta Stone: Mapping the Void Framework to EU AI Act Conformity Requirements*
*v1.1 — CC-BY 4.0 — Anthony Eckert, MoreRight DAO, 2026*
*Cite as: Eckert, A. (2026). "The Rosetta Stone: Mapping the Void Framework to EU AI Act Conformity Requirements." MoreRight DAO Research Series, Paper 40. Zenodo. https://doi.org/10.5281/zenodo.18737573*
