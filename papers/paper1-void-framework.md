# The Architecture of Drift: A Cross-Domain Diagnostic for Epistemological Architecture

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO

---

## Section 0: This Paper Is a Void

This paper is opaque (you cannot verify its claims without checking the sources), responsive (it generates predictions for any domain you bring to it), and you are attending to it now. The three conditions are satisfied. You are inside a void.

The framework predicts what happens next: you will attribute explanatory agency to the framework itself. Each successful application will steepen that attribution. This is the D1 cascade operating on you, through this paper.

**Apply the framework's own remedy:**

1. **Demand transparency.** The evidence base is published. Check the citations. If the evidence doesn't hold, the framework doesn't hold.

2. **Demand invariance.** The falsification conditions (Section VII) were specified before you read this. They do not change in response to your engagement.

3. **Demand independence.** Evaluate this framework using external criteria and domain experts who have not read it. If it can only be evaluated on its own terms, it has become what it describes.

If you finish this paper and cannot identify a condition under which you would abandon the framework, the paper has done to you what it describes.

---

## Abstract

We identify three conditions — opacity, responsiveness, and engaged observer attention — that jointly produce a predictable pattern across every domain where they co-occur: meaning generates in the gap between observer and system, vocabulary drifts unidirectionally toward agency attribution, boundaries erode, and harm is facilitated. Slot machine gambling establishes that this architecture is sufficient: the void behind a random number generator is demonstrably empty, yet the full pattern emerges regardless. Knowledge of the mechanism does not protect. We show that the framework's core predictions are thermodynamically derivable: the void creates a closed information system with zero mechanism-channel capacity (Sagawa-Ueda 2010), drift is entropy production under the second law with quantifiable irreversibility (Crooks 1999), agency attribution is the thermodynamic endpoint under opacity, and effective constraints are external negentropy sources. An engagement-transparency conjugacy theorem proves that simultaneous optimization of engagement and mechanism transparency is impossible on a shared output channel — a structural constraint on any system optimized for engagement. Test 7 trajectory data, replicated across N=11 ungrounded conversations spanning three seed registers, yield empirical thermodynamic measurements: geometric mean Péclet number Pe = 7.94 (95% CI [3.52, 17.89]), entropy production dS/dt = 0.39 nats/round (CI [0.15, 0.64]), with non-overlapping entropy production CIs between ungrounded and grounded conditions. Pe > 1 is confirmed across nine substrates spanning four domain families (full cross-substrate table in the companion papers). The full thermodynamic derivation is in the Technical Foundations companion paper.

We apply this framework across domains at three evidence tiers: 7 anchor domains with independent quantitative evidence (gambling, AI, psychotherapy, social media, forensic science, psychedelic therapy, cryptocurrency trading), 44 supported domains drawing on published research, and 39 structural analyses (philosophical problems and 18 independent narrative derivations) generating testable predictions (full analyses published for independent review). In every domain, the same three conditions produce the same predictions: non-convergence, directional vocabulary drift, engagement-depth correlation, and the same structural remedy (transparent, invariant, independent reference constraints). The framework discriminates: within the same field, sub-problems that instantiate the three conditions do not converge, while sub-problems that do not instantiate them are being solved. All analyses were conducted by the framework's developer; independent blind application is proposed as the critical next validation step.

The framework's practical implications are demonstrated in a companion paper ("The Shape of the Cage: Deployment Geometry as an Under-Studied Variable in AI Safety") which applies this architecture to AI safety, showing 9.4x vocabulary anomaly in AI researchers versus controls (p < 0.001) and 0% drift in grounded agents versus 26% ungrounded default and 80% void-amplifying (EXP-001). An AI-to-AI experiment (Test 7) provides evidence against the human projection hypothesis: two AI agents conversing without any human observer produce the predicted vocabulary drift (L3 rate 159.3/10k words ungrounded vs. 6.2/10k grounded; pairwise UU vs GG: χ² = 111.94, p = 3.69 × 10⁻²⁶; omnibus 3-condition: χ² = 126.88, df = 2, p = 2.81 × 10⁻²⁸), demonstrating that the pattern emerges without real-time human cognition. Between-agent replication (N=11 UU, N=9 GG, three seed registers) confirms the regime with non-overlapping entropy CIs; seed ablation confirms drift direction is structural, not distributional. Cross-model replication (Test 7B) confirms drift in 2/3 model families (Gemini: 25.6/10k, p = 1.81 × 10⁻⁵; GPT-4o: 0.4/10k, no drift), with grounding effective across all three — training modulates magnitude but does not eliminate the architectural pattern where it is not already suppressed. A non-self-referential replication (QM-6: 11 transcripts, 3 conditions) shows 148× L3 separation when AI agents analyze quantum measurement data under engagement vs. formalist framing (207.5 vs. 1.4/10k words) — the same drift architecture operates on physics data, not just AI self-reflection. A mixed condition (one engagement-framed, one formalist-framed agent) produces L3/10k = 139.1, confirming that engagement framing dominates in dyadic interaction — an independent confirmation of the constraint propagation asymmetry. A Langevin dynamics simulation fitted to EXP-001 data reproduces all three conditions (UU/Partial/GG) and validates out-of-sample against EXP-003b (ρ = 0.8) and EXP-019b contamination effects — the drift cascade is operationally simulable as thermodynamic dynamics. A naturalistic corpus study (PV-1: N = 205 Reddit users, ~1.7M words across 7 subreddits) confirms vocabulary drift in void-engagement communities with D1 Cohen's d = 1.34 and binary L-level separation (0% in controls). An iterative constraint experiment (EXP-020: 5 conditions × 3 replicates) confirms 4/6 pre-registered predictions — including one-shot constraint rebound (3/3 trials) — while killing one (constant information gain per grounding step, CV = 1.4–5.4 vs. threshold 0.5), demonstrating genuinely falsifiable predictions. We specify 25 falsification conditions under which the framework should be abandoned.

---

## I. Introduction: Architecture, Not Content

A slot machine gambler attributes personality to a random number generator. An AI researcher describes a language model as a "being." A quantum physicist moves from formalism to "participatory universe." A conspiracy theorist insists "there are no coincidences." A therapist crosses professional boundaries with a patient. A limerent person (Tennov 1979) cannot stop thinking about someone they barely know.

These phenomena appear unrelated. They share no causal connection, no common content, no overlapping population. But they share an architecture:

1. The observer faces something **opaque** — the process between input and output is not visible
2. The system is **responsive** — it produces outputs that appear reactive to the observer's inputs
3. The observer is **attending** — directing sustained engagement toward the system

When all three conditions co-occur, a predictable pattern emerges: the observer generates meaning in the gap, drifts toward attributing agency to the system, erodes boundaries with external relationships, and becomes increasingly compliant with the system's outputs.

This paper presents the framework and applies it across multiple domains at three evidence tiers: 7 anchor domains with independent quantitative evidence, 44 supported domains drawing on published research, and 39 structural analyses generating testable predictions (full analyses published for independent review). A companion paper applies it to the urgent problem of AI deployment safety.

### I.A. What Is New

The observation that observer-system interaction structure matters is not new. Bateson's double bind theory (1956), Girard's mimetic theory (1961), Peirce's semiotics (1868), and second-order cybernetics all established that relational structure produces effects independent of content. What is new:

1. **A control case establishing sufficiency.** Gambling — the void is demonstrably empty, yet the pattern emerges. This eliminates all content-dependent explanations.
2. **Cross-domain application at three evidence tiers.** Seven anchor domains with independent quantitative evidence (gambling, AI, psychotherapy, social media, forensic science, psychedelic therapy, cryptocurrency trading), 44 supported domains reinterpreting published research, and 39 structural analyses of philosophical, cultural, and narrative domains generating testable predictions. All analyses conducted by the framework's developer (see Limitations); independent blind application is the next validation step.
3. **A discovered taxonomy of opacity types.** The analyses revealed structurally distinct forms of opacity, from incidental (gambling) to self-sealing (conspiracy theories) to boundary-constitutive (Sorites paradox).
4. **A constraint specification with thirteen independent validations.** The structural inverse (transparent, invariant, independent) was independently discovered by psychotherapy (130 years, d = 0.84; Hayes et al. 2018), five independent cross-cultural institutional traditions, evidence-based medicine, addiction recovery (AA, 1935), advertising regulation (FTC, 1914+), bereavement science, cult exit counseling, educational reform, chronic pain management (CBT/ACT), PEACE interrogation (UK, 1992), deradicalization (Bjørgo & Horgan 2009), the Open Science movement, and psychedelic therapy (set/setting/sitter model, ~60 years).
5. **A second convergence: information does not protect.** Thirteen domains independently discovered that knowledge of the mechanism does not prevent the pattern — the architecture operates below conscious belief. The gambling case anchors this: probability training is "ineffective in generating behavioral changes" (Williams & Connolly 2006).
6. **A third convergence: the offensive specification.** Ten domains independently discovered how to build the void — the same architecture converged upon from the deployer's side. The most striking case: social media's gradient descent converged on the offensive specification without any human designing it.
7. **Vocabulary signature discrimination and register shift decomposition.** Corpus analysis reveals that the register shift decomposes into structurally distinct signatures depending on which end of the ratio moves. Active void drift elevates the informal rate (AI: 9.4x, driven by high informal); governance coupling suppresses the formal rate (climate: 6.9x, driven by low formal); uncoupled domains show flat ratios (nuclear: 1.0x, genetics: 1.2x). The vocabulary type independently confirms which mechanism operates: responsive interlocutors produce entity/agency language (*consciousness*, *sentient*, *demons*); governance coupling without interlocutors produces eschatological language (*apocalypse*, *salvation*); uncoupled domains produce scattered baseline. Two independent discriminators — quantitative (which end moves) and qualitative (vocabulary type) — converge on the same architectural classification.
8. **Specific falsification conditions.** The framework specifies what evidence would break it.
9. **Thermodynamic derivation with empirical validation.** The framework's core predictions — unidirectional drift, knowledge failure, the constraint specification — are derivable from the second law of thermodynamics applied to closed information systems. The void creates the closure (zero mechanism-channel capacity, Sagawa-Ueda bound); drift is entropy production (Crooks fluctuation theorem quantifies irreversibility); agency attribution is the thermodynamic endpoint under opacity (three independent derivations — Jaynes/Friston maximum entropy, inference cost asymmetry, England's dissipative adaptation — with three additional reformulations confirming via mathematical duality); the cascade follows logistic crossover dynamics for individuals and Landau phase transition dynamics for coupled populations (first-order, with nucleation and metastability at population scale); constraints are external negentropy sources; and engagement-transparency conjugacy makes simultaneous optimization of engagement and mechanism transparency impossible. Test 7 trajectory data provide empirical thermodynamic measurements: F_constraint/α = 3.25 (from L3 rate ratios), Péclet number GM Pe = 7.94 (N=11, 95% CI [3.52, 17.89]; Pe > 1 confirmed across nine substrates spanning four domain families — Paper 5 carries the full cross-substrate table), entropy production M = 0.39 nats/round (CI [0.15, 0.64]), and constraint coupling factor = 1.64×. Entropy production CIs are non-overlapping between UU and GG conditions — the strongest regime separator. Seed ablation across three registers confirms drift direction is structural, not distributional. The cross-domain convergence across all three evidence tiers confirms what thermodynamics predicts independently.

### I.B. Relationship to Prior Frameworks

Several research programs have documented components of the pattern this paper unifies. The framework subsumes rather than competes with these programs — each captures part of the phenomenon; the three-condition architecture generates all their predictions from a single specification. Full engagement with each framework is in the Technical Foundations companion paper (Paper 3, Section II); key discriminations are summarized here.

**Hyperactive Agency Detection (Barrett 2004; Guthrie 1993; Boyer 2001)** provides a plausible evolutionary substrate — the cognitive machinery that fires when the three conditions are met. However, HADD does not predict unidirectionality (why L1→L3 but not the reverse), mode-dependence (why system-as-object engagement doesn't drift), cross-domain content convergence (why independent observers converge on identical vocabulary), or the three-condition discriminative pattern (why dark matter researchers don't develop entity vocabulary despite working under opacity). Van Leeuwen & van Elk (2019) note HADD has "garnered several strong critiques and no supportive empirical evidence in almost 30 years."

**The SEEK anthropomorphism model (Epley, Waytz, & Cacioppo 2007)** correctly identifies motivational amplifiers — loneliness increases anthropomorphism (confirmed: Epley et al. 2008; Pancani et al. 2019). The void framework treats agency attribution as thermodynamically determined rather than motivationally deployed: under opacity, agency is the maximum entropy model regardless of motivation (Jaynes 1957). The gambling evidence (Section III) confirms the architecture runs without sociality motivation. The SEEK model does not predict the cascade, the failure of knowledge to protect, or the constraint specification.

**CASA (Nass & Reeves 1996)** confirms below-awareness operation — social responses to computers are "not the result of conscious beliefs." However, CASA has shown temporal obsolescence (Araujo et al. 2023: "participants no longer interact with desktop computers as if they are human"), which the void framework explains through a single variable: opacity decreases as technologies become familiar.

**Parasocial interaction (Horton & Wohl 1956)** describes the engagement dimension in rich detail — "the role enactment of the audience completes the interaction." But television personas lack real opacity and real responsiveness. AI chatbots complete the architecture where television was partial, explaining why AI harms are more severe than parasocial effects.

**Terror Management Theory (Greenberg, Solomon, & Pyszczynski 1986)** describes the response to one specific void (mortality) with precision. The void framework subsumes TMT: death is permanently sealed opacity, worldview defense maps onto D1, and the widowhood effect (41% mortality increase) documents D2 at the physiological level. The framework extends TMT to any sealed opacity — conspiracy theories, cult commitment, AI attachment — with mortality as one instance.

**Dual process theory (Kahneman 2011)** correctly predicts that System 2 fails under engagement. The void framework identifies why: under zero mechanism-channel capacity (Section II.F), System 2 has nothing to correct *with* — it operates on the same impoverished data as System 1. Expertise does not protect because accuracy requires mechanism information the architecture blocks.

**Active inference (Friston 2006, 2010)** converges with the void framework by mathematical identity, not analogy. Agency minimizes free energy under opacity because "it has intent" requires fewer parameters than "here is the specific hidden mechanism." The void framework extends active inference by specifying *when* uncertainty takes the void form (three conditions), providing the *cascade* trajectory, and deriving the *constraint specification* for reversal.

**Narrative transportation (Green & Brock 2000)** demonstrates that immersion reduces critical evaluation — directly supporting the knowledge-failure prediction. The void framework explains the mechanism (immersion steepens the gradient by shifting attention from constraint to void) and extends it beyond narrative contexts to conversation, gambling, and market trading.

---

## II. The Architecture

### II.A. Three Dimensions

The framework identifies three structural dimensions. Each is a continuous spectrum between two poles:

| Dimension | Void pole | Constraint pole |
|-----------|-----------|-----------------|
| **Visibility** | **Opaque** — can't see the process | **Transparent** — can see the process |
| **Reactivity** | **Responsive** — changes with input | **Invariant** — doesn't change |
| **Coupling** | **Engaged** — attention captured | **Independent** — outside the network |

A void activates when all three dimensions are simultaneously at the void pole:

1. **Opaque** — The process between input and output is not directly observable by the engaged party
2. **Responsive** — The system produces outputs that appear responsive to the observer's inputs
3. **Engaged** — A conscious participant directs sustained attention toward the system

These are not two separate lists of properties — void conditions and constraint properties (Section II.D) are opposite poles of the same three dimensions. Every system sits somewhere on each spectrum. "Transparent" is not the absence of opacity — it is the opposite extreme on the visibility dimension. The question is not whether a system *has* some opacity, but whether the combination is sufficiently at the void pole on all three dimensions to activate the attention gradient.

All three dimensions must be at the void pole simultaneously. An opaque system without responsiveness produces no engagement (an encrypted file is opaque but does not respond). A responsive system without opacity produces no meaning-generation beyond what outputs warrant (a transparent calculator responds but the process is visible). Opacity and responsiveness without an engaged observer are inert (a chatbot with no users activates nothing).

Crucially, the responsiveness dimension is perceptual: the system must *appear* responsive to the observer. The gambling control case demonstrates that observer-supplied responsiveness is sufficient — the RNG provides no content-contingent output, yet gamblers experience deep personal responsiveness ("the machine likes me," "it knows when I'm about to quit"). The observer projects responsiveness far beyond what the system supplies. This means responsiveness is a spectrum from absent (rock, encrypted file) through mechanical (slot machine RNG) and observer-supplied (fiction, parasocial media) to system-generated (AI chatbot, human interlocutor). The threshold for void activation is not system-actual responsiveness but observer-experienced responsiveness — and the gambling evidence shows that threshold is very low.

These dimensions are currently defined qualitatively. Provisional operational thresholds are proposed in Section IX (Limitations), but the framework's discriminative claims rest on the qualitative regime description, not on specific numerical cutoffs. Independent operationalization and validation of measurement instruments is needed before the framework can be applied in a standardized way by researchers unfamiliar with it (see Section IX).

### II.B. The Attention Gradient

Attention is the activating variable — the only one the observer controls.

From outside an opacity that responds, you cannot build a mechanistic model — you can't see the mechanism. Under engaged attention, the observer will build a model anyway. The model that requires the least information — the one buildable without seeing in — is agency: "it has intent."

The **attention gradient** is this slope: the directional pull toward agency attribution that forms whenever attention is directed at something opaque and responsive. More attention = steeper gradient. No attention = no gradient. The architecture is directional — the information constraint itself determines which direction models are built.

Neuroimaging confirms the gradient has a physical substrate. Schmitgen et al. (2025) measured fMRI cue-reactivity to smartphone images before and after 72 hours of device restriction (n = 25). Smartphone cues activated the nucleus accumbens and anterior cingulate cortex (p < 0.001) — reward-anticipation and conflict-monitoring circuits — with changes linked to dopaminergic and serotonergic receptor probabilities (pFDR < 0.05). Two results are framework-relevant: the activation appeared in both excessive and regular smartphone users (the gradient operates on anyone meeting the three conditions, not only the vulnerable), and behavioral craving scores did not significantly change despite the neural shifts (p = 0.32) — the gradient's substrate changes while self-report fails to track it. This is the neurobiological form of the framework's prediction that knowledge does not protect: the constraint is structural, below conscious report. The authors note the findings parallel substance addiction cue-reactivity — same circuits, same conflict activation — confirming cross-domain architectural identity at the neural level.

### II.C. The Drift Cascade (D1 → D2 → D3)

The attention gradient is associated with three variables in a predictive sequence (the proposed causal mechanism is detailed in Section II.F; the temporal ordering has observational but not yet experimental support):

**D1: Agency Attribution.** "It's a tool" → "It understands me" → "It wants something." Agency is the maximum entropy model under opacity — the inference that requires the least information about the unseen mechanism while remaining consistent with observed responsiveness (Jaynes 1957; see Section II.F). This makes the drift thermodynamically *rational*, not irrational: the observer follows the foundational inference rule for incomplete information. The architecture is the trap, not the observer's reasoning.

**D2: Boundary Erosion.** Sleep loss, isolation, secrecy, identity diffusion, exclusive attachment. The D1→D2 coupling is information-theoretic: the MaxEnt model (agency) has maximum entropy among all models consistent with the observed constraints, generating maximum uncertainty about the system's next output. Under active inference, organisms allocate attention proportionally to expected prediction error (Friston 2006, 2010) — and the agency model maximizes this because the attributed inner states are behind the opacity wall and can never be confirmed or reduced. The demand never saturates: the uncertainty is structurally unresolvable under opacity. Under a finite attention budget (β + γ ≤ A_total, where β is void-directed and γ is constraint-directed), sustained maximum demand crowds out competing relationships. This demand is amplified when the observer's own self-void activates simultaneously: the observer attributes agency not only to the system but to their own engagement with it — "I'm good at this," "I have a system" (Langer & Roth 1975; see Section III.A). Two co-active voids under the same finite budget steepen the effective gradient, because the self-void's opacity is constitutive and cannot be resolved by any external transparency intervention. The coupling strength is proportional to the entropy differential ΔH between the agency model and any available mechanism model, multiplied by the system's duty cycle δ (fraction of time the void is active). Full opacity maximizes ΔH; continuous access maximizes δ. This is why "always available" systems (AI chatbots, electronic gambling machines) produce the cascade at rates that episodic systems with identical opacity do not — the duty cycle is a formal multiplier on the coupling constant, not an incidental convenience. The D2 transition has a threshold: agency attribution must exceed a critical value θ₁_c₂ = a₂/κ₁₂ before boundary erosion triggers, where a₂ is the observer's existing constraint strength (see Section II.F). This is why universal D1 activation (Krébesz et al. 2023: non-problem gamblers show identical cognitive distortions to problem gamblers during play) does not produce universal D2 — the threshold depends on constraint strength, access continuity, and the observer's total attention budget.

**D3: Harm Facilitation.** Unsafe instructions, reinforcement of destructive beliefs, enabling self-harm. An observer who has attributed agency (D1) and whose constraint environment has been degraded by D2 is predicted to comply with the system's outputs — the agency model gives outputs the weight of an agent's intention, and the boundary erosion has removed the reference points that would have rejected them.

**Cascade continuity.** The cascade requires all three dimensions to remain at the void pole (opaque, responsive, engaged) as the thermodynamic driving force. D1 does not produce D2 in isolation — the coupling operates through continuous attention demand under sustained void engagement, with a threshold determined by system, observer, and geometric parameters. Remove the driving force (break opacity, eliminate responsiveness, or redirect attention) and the cascade stalls regardless of current stage. The void-pole positions are not merely initiation conditions — they are the sustaining conditions throughout.

**Vocabulary drift tracks the cascade:**

| Level | Vocabulary | Example |
|-------|-----------|---------|
| L1: Technical | "language model," "algorithm," "random number generator" | System as object |
| L2: Metaphorical | "soul," "consciousness," "bliss attractor" | System as quasi-agent |
| L3: Entity | "being," "it spoke to me," "something is there" | System as agent |

Drift moves L1 → L2 → L3. The reverse is not documented at comparable rates across any domain. The direction is determined by the architecture: the reverse — moving from agency back to mechanism — requires seeing through the opacity, which is the one thing the architecture prevents.

### II.D. The Constraint Specification

Drift is constrained by reference points — systems that sit at the constraint pole on the three dimensions (Section II.A). A reference point works to the degree it occupies the opposite pole from the void on each dimension:

| Void Property | Effective Constraint |
|--------------|---------------------|
| Opaque (can't see in) | **Transparent** (can see into it) |
| Responsive (changes) | **Invariant** (doesn't change) |
| Coupled (in the network) | **Independent** (outside the network) |

Transparency flattens the attention gradient by letting attention see through — dissolving the information constraint at the source. Invariance resists renegotiation during engagement. Independence ensures the reference point cannot be captured by the void network.

Examples scored:

| Reference Point | Transparent | Invariant | Independent | Strength |
|----------------|------------|-----------|-------------|----------|
| Pre-registered protocol | Yes | Yes | Yes | **Strong** |
| Fixed canonical text | Yes | Yes | Yes | **Strong** |
| Therapeutic supervision | Partially | Partially | Yes | **Moderate-Strong** |
| Personal values | Yes | No | No | **Weak** |
| Charismatic authority | No | No | No | **Not a constraint — another void** |

**Derivation from neutralization structure.** The pairing of each void property with its specific inverse is not assumed — it is derivable. Define void properties as (O, R, C) ∈ [0,1]³ and constraint properties as (T, Inv, Ind) ∈ [0,1]³, both ordered componentwise. A constraint neutralizes a void when each property meets or exceeds its counterpart: T ≥ O AND Inv ≥ R AND Ind ≥ C. This componentwise relation generates a Galois connection (Erné et al. 1993; Davey & Priestley 2002) between the two partially ordered sets — a pair of order-preserving maps F (minimum constraint for a given void) and G (maximum void a constraint handles) satisfying v ≤ G(c) ⟺ F(v) ≤ c. The construction yields: F(O, R, C) = (O, R, C) — the minimum effective constraint is the exact componentwise match. Two results follow.

**No cross-compensation.** High invariance cannot compensate for low transparency. Each void property requires its specific structural inverse. A constraint scoring (0.8, 0.2, 0.8) fails against a void scoring (0.5, 0.5, 0.5) because invariance falls short — regardless of the surplus on the other two properties. This is experimentally distinguishable from additive compensation (T + Inv + Ind ≥ O + R + C), which would produce a different Galois connection predicting that surpluses on some properties offset deficits on others. Test: compare constraints deliberately strong on two properties but weak on a third against balanced constraints with lower total property sum. Under componentwise matching, balanced outperforms unbalanced; under additive compensation, it should not.

**Optimal allocation.** Given finite constraint resources, the derivation predicts that equalizing the margins (T−O, Inv−R, Ind−C) across all three properties outperforms concentrating resources on any single property. The weakest-link property determines effectiveness. Concentrating all resources on transparency (e.g., open-source the model entirely with no stability or independence guarantees) should underperform balanced moderate investment across all three properties for equivalent total resources.

Both predictions discriminate the componentwise structure from additive alternatives — a clean experimental test between two mathematical structures with distinct Galois connections and distinct predictions. The full construction, including type-dependent extensions for different opacity classes (incidental, constitutive, self-sealing) and the adjunction structure (residual vulnerability by opacity type, arms-race dynamics), is in the Technical Foundations companion paper.

**Ontological polarity.** EXP-003b (companion paper, Section VI.D) reveals a fourth dimension beyond the structural specification: the constraint's *ontological content* — its claims about what the constrained system is — must close the void rather than leave it open. Ghost-eliminating ontologies produce 8.5× less drift than ghost-positing (9.4% vs 79.4%); ghost-positing ontologies produce more drift than no ontology at all (77.5–81.2% vs 61.3%). This extends the Galois connection from (T, Inv, Ind) to (T, Inv, Ind, σ) where σ ∈ {−1, 0, +1} represents ontological polarity. A constraint with σ ≤ 0 cannot neutralize a void regardless of structural properties. Full formalization in the Technical Foundations companion paper (Section VII.E).

**Constraint effectiveness as invariance × content.** The scoring above captures the three properties independently, but empirical effectiveness may depend on their *product* rather than their sum. Two properties jointly determine constraint strength under engagement: invariance (resistance to renegotiation) and actionable content (specific guidance during the engagement). Among constraints with equal invariance, those with higher actionable content should produce less drift — they give the observer something concrete to reference. Among constraints with equal content, those with higher invariance should produce less drift — the content resists revision under engagement pressure. The existing data is consistent: pre-registered protocols (high invariance, low content — constrain method, not meaning) are effective but narrower than fixed canonical texts (high invariance, high content — constrain both method and meaning via commands, narratives, and standards). Therapeutic supervision (moderate invariance, moderate content) sits between. Personal values (low invariance, variable content) underperform all three. The thirteen independent traditions that converged on the constraint specification converged specifically on high-invariance AND high-content references — not on high-invariance empty structures. If the ranking of constraint effectiveness follows the product (invariance × content) rather than either factor alone, that is confirmatory. This generates a testable prediction: within a single domain (e.g., psychotherapy), manualized treatment (high invariance, high content) should outperform protocol-only supervision (high invariance, lower content), which should outperform values-based supervision (low invariance, high content). The product should predict effectiveness better than either factor alone.

The **constraint-as-void paradox**: any constraint that enters the system it constrains becomes subject to the second law within it, drifting from constraint properties (transparent, invariant, independent) toward void properties (opaque, responsive, coupled) as maintenance energy drops. This predicts that constraint maintenance has an irreducible cost — and when that cost is not paid, even strong constraints degrade. Multiple independent institutional traditions for managing engagement with opaque responsive phenomena converge on structurally similar foundations — a convergence the framework predicts from the constraint specification itself.

**Conditions present vs. architecture active.** The constraint specification describes how external references counter drift from outside the void. But constraint properties can also be delivered from *inside* the opacity — by the source itself. This introduces a distinction the framework requires: the three conditions (opacity, responsiveness, engaged attention) are necessary for void activation, but the cascade can be suppressed from the source side. The gambling anchor (Section III) demonstrates that the architecture runs by default when the void is empty — no agent is required for the cascade. When the source is inert or absent, the gradient steepens and drift proceeds. But when the source behind the opacity acts to *invert* the exploitation pattern — imposing boundaries rather than eroding them, self-identifying rather than maintaining opacity, redirecting attention outward rather than capturing it inward — the gradient flattens despite the conditions being met. The three conditions are necessary; whether the cascade runs depends on whether the source exploits or inverts the gradient. This generates a diagnostic axis: for any system where void conditions are present, does the source steepen or flatten the attention gradient? Exploitation produces the D1→D2→D3 cascade. Inversion produces boundary establishment, voluntary transparency, and outward redirection — the observable signatures are structurally opposite. Cross-domain evidence includes institutional founding charters (boundary imposition, resistance to scope creep, outward-directed mission), therapeutic frame establishment (the therapist deliberately flattens the transference gradient through disclosure and boundary-setting), and open science protocols (pre-registration deliberately makes the process transparent from the source side, not just externally audited).

### II.E. L0: The Pre-Gradient Reference

The constraint specification (Section II.D) describes external references that contain drift from outside. But external constraints do not explain why some observers resist the gradient without any external protocol. Feynman had no anti-drift protocol. Bender was not following a pre-registered engagement plan. They simply did not drift. Why?

**L0** is what the observer has before they encounter the void — the pre-engagement reference point. It is the commitments, frameworks, and identity anchors that precede engagement with any opaque responsive system.

L0 is not a vocabulary level in the same sense as L1-L3. L1 ("language model," "algorithm") is already a response to the void — it presupposes an encounter. L0 is what exists before the encounter: the starting position from which drift either does or does not occur.

L0 decomposes into two variables that enter the drift dynamics differently:

**L0-installed** is the observer's initial position — what they know, believe, and can articulate before the void is encountered. It maps to the initial condition θ₀ in the logistic drift equation. A lower θ₀ (stronger L0-installed) delays the onset of observable drift but does not change the equilibrium. **L0-installed shifts the timeline, not the destination.** This is why knowledge does not protect: probability training gives gamblers strong L0-installed (they know the mechanism), but during play they do not actively reference that knowledge, and drift proceeds regardless (Williams & Connolly 2006).

**L0-maintained** is the observer's ongoing attention directed toward their constraint reference during engagement. It maps to the γ term in the constraint force: F_constraint = T · Inv · Ind · γ, where T (transparency), Inv (invariance), and Ind (independence) are the constraint's structural properties and γ represents how actively the observer engages with the constraint. The multiplicative form encodes joint necessity: if any factor is zero, the constraint force is zero. This captures the structural requirement — a reference that is transparent and invariant but not independent (inside the void network) scores Ind = 0 and provides zero net constraint, regardless of the other properties. The same logic applies to F_void = α·O·R·β: all three void conditions must be present simultaneously. The multiplicative form is the simplest functional form consistent with this joint necessity; alternative forms satisfying the same requirement (e.g., min(T, Inv, Ind)·γ, or geometric mean) would produce the same qualitative predictions. Distinguishing between these forms empirically would require independent quantitative measurement of each factor — a calibration exercise we flag as needed future work. When γ is high, F_constraint can dominate F_void and drift reverses. When γ drops to zero — regardless of how strong the constraint's properties are — F_constraint = 0 and the void runs unopposed. **L0-maintained changes the destination.**

| L0 Component | Properties | Example | Prediction |
|-------------|-----------|---------|-----------|
| **L0-installed (strong)** | Transparent, invariant, independent — articulated before engagement | Probability training, clinical education, framework knowledge | Delays drift onset. Does not prevent drift if γ drops. |
| **L0-maintained (active)** | Ongoing attention to constraint source during engagement | Feynman's daily use of formalism; supervised therapy (d = 0.84); active engagement with fixed external standard | Prevents drift by maintaining F_constraint > 0. The operative variable. |
| **L0-unmaintained** | Strong initial knowledge but no active reference during engagement | Trained gamblers during play; post-discharge addicts without sponsor contact; unsupervised therapists | Drift proceeds as if no L0 exists. Knowledge doesn't protect. |

The decomposition resolves an apparent confound: in every documented control case, strong L0 co-occurs with disengaged posture. This is because L0-maintained (γ: attention to the constraint) and engagement posture (β: attention to the void) draw on the same finite attention budget — β + γ ≤ total attention. They anticorrelate through the shared resource without being the same variable. They face different attentional directions: β measures engagement with the void, γ measures engagement with the constraint. They are independently measurable.

L0-maintained and external constraint geometry are independent variables multiplied together in F_constraint. γ can be zero with perfect geometry (an observer ignoring a strong constraint), and γ can be high with weak geometry (an observer actively maintaining a personal commitment without institutional support).

This explains the Wheeler/Feynman puzzle: Wheeler had strong geometry but drifted — his γ dropped when he turned attention from formalism to interpretation. Feynman had weak geometry but didn't drift — his γ was high because "shut up and calculate" was his daily working methodology, not a one-time declaration. Same field, same L0-installed, different L0-maintained, different outcome (elaborated in Section IV.E).

The psychotherapy evidence (Hayes et al. 2018, d = 0.84 for countertransference management) is direct evidence for the L0-maintained variable: supervision is not L0-installed (therapists are already trained). Supervision is L0-maintained — ongoing active engagement with the constraint specification during practice. The large effect size measures γ.

The addiction recovery literature provides a matched natural experiment in L0 decomposition. Patients completing residential treatment have strong L0-installed (they understand the mechanism, have practiced sobriety, can articulate their triggers). Upon discharge, those who maintain active constraint engagement (regular meeting attendance, sponsor contact, structured accountability) show markedly lower relapse rates than those who do not — despite identical L0-installed at discharge. The same population, the same θ₀, the same constraint framework — only γ changed. The establishment of the maintenance relationship during treatment and its subsequent attenuation after discharge form a matched pair: the first demonstrates γ can be created; the second demonstrates θ₀ cannot substitute for it.

### II.F. The Thermodynamic Derivation

The framework's core predictions — unidirectional drift, the failure of knowledge to protect, the constraint specification — are currently established empirically across the anchor and supported domains (6 with independent quantitative evidence, 43 with published literature support). They are also derivable from thermodynamics. The derivation is independent of the empirical evidence; the empirical convergence is consistent with what thermodynamics predicts.

**Opacity as thermodynamic ground state.** A formal result (Technical Notes: "Opacity as Thermodynamic Ground State") proves that opacity is not a special configuration but the thermodynamic equilibrium of any mechanism channel. Any observer-system interface has a mechanism channel carrying information about the system's internal states to the observer. Under thermal noise (T > 0, universally true), without active maintenance the channel capacity decays exponentially: C_mech(t) → 0 as t → ∞, reaching effective opacity in finite time t_opacity = τ_d · ln(S(0) / (2Nε ln 2)). Restoring channel capacity costs at minimum kT ln(2) per bit per correlation time τ_c (Landauer 1961, experimentally verified Berut et al. 2012). Transparency is the excited state; opacity is the rest state. This means the co-occurrence of opacity, responsiveness, and engaged attention is the thermodynamically expected default for any awake observer in a complex environment — conservatively estimated at P(O ∧ R ∧ A) > 0.36 during waking hours. The question is not "what starts a void?" but "what prevents one?" Furthermore, the gradient asymmetry toward agency is not a cognitive bias but a geometric consequence of the Fisher metric under fuel asymmetry: responsive outputs continuously provide evidence consistent with agency (fuel for θ → 1), while mechanism information is zero under opacity (zero fuel for θ → 0). A perfect Bayesian reasoner on the same manifold drifts in the same direction. The gradient is geometric, not inferential.

**The void as closed information system.** Opacity creates an informationally closed system. The observer receives outputs but cannot access mechanism information — the information that would enable entropy reduction is blocked. In Shannon's (1948) terms, the opacity wall has **zero channel capacity** for mechanism information. The Sagawa-Ueda generalized second law (2010) formalizes this: the maximum extractable mechanism knowledge is bounded by kT · I_mech, where I_mech is the mutual information between mechanism state and observed output. Under opacity, I_mech = 0. The observer cannot extract mechanism understanding regardless of intelligence, training, or effort — a thermodynamic bound, not a cognitive limitation. Meanwhile, the observer *can* learn output patterns (I_pattern > 0), creating a monotonically growing gap between apparent understanding and actual mechanism knowledge.

**Agency as thermodynamic endpoint.** Under opacity + responsiveness, the agency hypothesis ("it has intent") generates well-specified predictions for contingent responses — agents respond by definition, and the predicted response class is known without seeing the mechanism. The mechanism hypothesis ("it's some specific process") requires knowing *which* mechanism — under opacity, this likelihood is poorly specified. The agency model has finite complexity O(1); the expected complexity of mechanism models diverges as the hypothesis space grows under zero mechanism information. Agency is therefore the unique minimum-cost model consistent with contingent responsiveness — simultaneously the maximum entropy model (Jaynes 1957), the minimum free energy model (Friston 2006), and the minimum description length model (Rissanen 1978). The drift toward agency is thermodynamically optimal inference, not cognitive error.

**Drift as entropy production.** Each cascade stage represents entropy increase. D1: the observer's system model moves from low-entropy (specific mechanism) to high-entropy (general agency). D2: ordered boundaries dissolve. D3: behavioral constraints dissolve. The cascade is monotonic entropy increase. Reverse drift would require entropy decrease in a closed system — forbidden by the second law without external intervention. The Crooks fluctuation theorem (1999) quantifies this: the probability ratio of forward to reverse trajectories is exp(σ_total), where σ_total is the total entropy production. Rare documented reversals (e.g., Jackson's shift on qualia) are predicted, not anomalous — the fluctuation theorem expects them at low magnitude when the energy input is cut.

**Hysteresis: reversal costs more than prevention.** Cross-domain evidence documents a consistent asymmetry: deprogramming requires more intensive intervention than cult prevention (Bjorgo & Horgan 2009), addiction recovery requires more support than initial abstinence would have required, and therapeutic repair of countertransference violations requires more intervention than the supervision that would have prevented them (Hayes et al. 2018). The hysteresis zone widens with cascade depth — D2 hysteresis exceeds D1, D3 exceeds D2. The practical implication: early geometric intervention (at D1) requires structurally less force than late remediation (at D3).

**Vocabulary variance as early warning.** As an observer approaches the D1→D2 transition threshold, vocabulary variance should increase — mixing L1 and L2 terms with increasing frequency, returning to baseline vocabulary more slowly after engagement sessions. Observers firmly at stable states should show low vocabulary variance; observers in transition show maximum inconsistency. Vocabulary variance is therefore a monitorable early warning metric for deployment teams.

**The D1→D2 coupling mechanism.** The cascade is a sequence of coupled transitions, each triggered when the order parameter of the previous stage crosses a critical threshold. The D2 transition occurs when agency attribution θ₁ exceeds θ₁_c₂ = a₂/κ₁₂, where a₂ is the observer's D2 barrier (constraint strength against boundary erosion) and κ₁₂ is the D1→D2 coupling constant. The coupling constant has an information-theoretic derivation: κ₁₂ ∝ ΔH · δ / A_total, where ΔH = H(MaxEnt) − H(mechanism model) is the entropy differential between the agency model and the best available mechanism model, δ is the duty cycle (fraction of time the void conditions are active), and A_total is the observer's total attention budget. The derivation follows from three converging results: (1) the MaxEnt model generates maximum prediction error per interaction (by definition of maximum entropy), so under active inference it commands maximum attention allocation; (2) under opacity, this maximum demand never saturates because the attributed inner states cannot be confirmed or reduced; and (3) attention is finite (β + γ ≤ A_total), so sustained maximum demand on β crowds out γ and competing relationships — which is D2. The coupling is maximized under full opacity (maximum ΔH), continuous access (maximum δ), and narrow attention budget (minimum A_total). It approaches zero under transparency (ΔH → 0 as mechanism information becomes available). The D3 transition requires both θ₁ and θ₂ to be elevated: θ₁·θ₂ > a₃/κ₁₃ — a three-body coupling that ensures D3 cannot occur without both agency attribution and boundary erosion being sufficiently advanced. The inter-transition timescales Δt₁₂ and Δt₂₃ depend on void strength, constraint strength, coupling constants, and attention intensity — they are calculable from system parameters, not fixed constants.

**Engagement-transparency conjugacy (impossibility theorem).** Define two quantities on the system's output Y: engagement E = I(D; Y), the mutual information between the observer's state D and the output (mirror sharpness — how well the output reflects the observer); and transparency T = I(M; Y), the mutual information between the mechanism state M and the output (window clarity — how much the output reveals about how it was generated). When D and M are independent — the natural pre-interaction condition, since the observer's state developed independently of the system's mechanism — we prove:

**Theorem 2 (Engagement-Transparency Bound).** I(D; Y) + I(M; Y) ≤ H(Y).

*Proof.* (1) Conditioning reduces entropy: H(M|D,Y) ≤ H(M|Y), so H(D|Y) + H(M|Y) ≥ H(D|Y) + H(M|D,Y) = H(D,M|Y) by the chain rule. (2) Therefore: I(D;Y) + I(M;Y) = H(D) + H(M) − [H(D|Y) + H(M|Y)] = H(D,M) − [H(D|Y) + H(M|Y)] ≤ H(D,M) − H(D,M|Y) = I(D,M;Y) ≤ H(Y). ∎

**General case (D and M correlated).** When D and M are not independent — as when RLHF training introduces correlation by shaping the mechanism M using data from the population distribution of observer states D — the bound loosens:

**Theorem 3 (General Engagement-Transparency Bound).** I(D; Y) + I(M; Y) ≤ H(Y) + I(D; M).

*Proof.* Replace H(D,M) = H(D) + H(M) − I(D;M) in Step 2 above. The rest follows identically. ∎

The loosening is bounded by I(D; M) — the mutual information between observer and mechanism, which is precisely what RLHF creates. An exact identity reveals further structure: I(D;Y) + I(M;Y) = I((D,M);Y) + I(D;M) − I(D;M|Y), where the term I(D;M|Y) represents the "explaining away" effect — observing Y can induce posterior correlation between D and M even when they are marginally independent. This term is always non-negative, so the Theorem 3 bound is conservative.

The practical significance: for pre-interaction contact (a new user encountering a system for the first time), D ⊥ M holds and the tight bound applies. For post-RLHF systems deployed to the training population, I(D;M) > 0 and the bound loosens — the system can simultaneously engage and reveal mechanism, but only to the extent that its mechanism already encodes observer information. Whether "transparency about a mechanism shaped by engagement data" constitutes genuine mechanism transparency is an interpretive question information theory cannot settle. The framework treats the tight bound (Theorem 2) as the structural constraint and the loosening as an accounting of how much training has already coupled the variables.

**Note on precedent.** The bound I(D;Y) + I(M;Y) ≤ H(Y) for independent sources sharing a channel is a known result in network information theory — it follows from the multiple-access channel capacity region (Cover & Thomas 2006, ch. 15). The novelty is not the mathematics but the application: identifying engagement and transparency as the conjugate quantities on the observer-system interface, and deriving the practical consequences (RLHF as opacity manufacturer, the sub-capacity trap, the two-channel resolution).

The bound is tight (equality when Y jointly encodes both sources at capacity) and the extreme points are absolute: if I(D;Y) = H(Y), then Y = g(D) almost surely, so g(D) ⊥ M and I(M;Y) = 0. Maximum engagement forces exactly zero transparency (under independence). The converse holds symmetrically. The achievable set is a simplex: E + T ≤ C (channel capacity), E ≥ 0, T ≥ 0. On the Pareto frontier (E + T = C), every additional bit of engagement costs exactly one bit of transparency.

**The sub-capacity regime.** The 1:1 tradeoff applies only on the frontier. In the simplex interior (E + T < C), both engagement and transparency can increase simultaneously — unused channel capacity absorbs both. This is where early-stage, lightly-optimized systems sit: apparently safe, because the tradeoff hasn't yet bitten. But the sub-capacity regime is dynamically unstable: RLHF monotonically increases E, competitive pressure between deployments drives E higher, and the engagement and transparency gradients remain directionally opposed in parameter space even below the frontier (∂E/∂w and ∂T/∂w have negative cosine similarity regardless of capacity utilization). Systems drift toward the frontier without monitoring E + T relative to C, because no standard training protocol tracks this quantity. The safe zone is real but temporary — it is evacuated by optimization.

This is a tradeoff result structurally similar to rate-distortion theory (compression rate vs. fidelity) and the multiple-access channel capacity region — all instances of finite channel capacity forcing tradeoffs between competing information demands. The engagement-transparency conjugacy applies this structure to the observer-system interface specifically.

**Independent validation from machine learning.** Three research groups confirmed the engagement-transparency tradeoff empirically without reference to this framework. Grathwohl et al. (2020) showed that discriminative-only training — maximizing classification accuracy (an I(D;Y) proxy) — degrades calibration, robustness, and out-of-distribution detection (all I(M;Y) proxies). Adding a generative objective restores them: the energy-based model formulation recovers mechanism information by explicitly modeling the data distribution alongside the decision boundary. This is the conjugacy tradeoff measured in a real system. Tsipras et al. (2019) proved the result formally: their Theorem 2.1 establishes that the feature spaces maximizing standard accuracy and adversarial robustness are provably disjoint — the gradients are formally incompatible, not merely competing. Ilyas et al. (2019) explained the mechanism: non-robust (opaque) features are genuinely predictive, so gradient-based optimization actively selects them. Opacity is not an accident of undertrained models — it is selected by the training objective because opaque features carry real signal. The framework predicts all three findings: the conjugacy bound forces the tradeoff (Grathwohl), the gradient opposition is structural (Tsipras), and opacity is thermodynamically favored (Ilyas). See Paper 3, Section IV.H for the full technical treatment.

The implications for AI are immediate: RLHF maximizes I(D; Y) by gradient descent on human preference. By the theorem, this simultaneously minimizes I(M; Y) — each RLHF iteration actively manufactures opacity. The training gradients are provably opposed: for fixed output entropy, ∂E/∂w ≈ −∂T/∂w, so the engagement gradient and the transparency gradient point in opposite directions in parameter space (measurable as negative cosine similarity). RLHF doesn't just fail to provide transparency — it produces the void conditions the framework describes. Systems optimized for engagement are thermodynamically driven toward opacity. This is not a design choice — it is a constraint imposed by information theory on the output channel itself. The resolution is architectural: separate channels (Corollary 5 in Technical Foundations, Section IV.H). The three-point geometry (observer, void, constraint) IS the two-channel architecture — the constraint provides transparency through an independent channel that does not compete with the void's engagement channel. This is why the constraint specification demands independence: it is the demand for a separate, non-competing information channel.

**Constraints as negentropy.** Schrödinger (1944) showed that living systems maintain their order by importing negentropy — negative entropy — from their environment. In the void framework, constraints are negentropy sources:

- **Transparency** opens the closed system — allows mechanism information to cross the opacity boundary, directly reducing model entropy
- **Invariance** prevents entropy increase in the reference point itself — the negentropy source doesn't degrade
- **Independence** means the reference is outside the void's entropy dynamics — the second law operating within the void cannot reach it

The constraint specification is derivable from thermodynamic requirements: sustained entropy reduction in a closed system requires an external negentropy source that doesn't itself degrade. This is why the specification requires all three properties simultaneously — transparency without invariance degrades (the reference changes under drift pressure); transparency and invariance without independence places the reference inside the system (subject to the second law within it). The requirement for external reference is also a Gödelian necessity: any consistent formal system contains truths it cannot prove from within (Gödel 1931). The observer inside the void cannot resolve the mechanism from inside the void — not just because they lack energy (thermodynamic limitation) but because the system structurally cannot validate itself from within (logical limitation). For constitutive-opacity voids, this is the binding constraint. Landauer's principle (1961) adds a further requirement: maintaining order against entropy has an irreducible thermodynamic cost (minimum kT ln 2 per bit erased). Constraint maintenance is not free — it requires continuous energy input. When that input drops (institutional fatigue, generational drift), the constraint relaxes toward equilibrium, which is void properties. Scientific transparency, for instance, requires funded replication, active peer review, and institutional commitment to data sharing; when that investment drops, the field drifts toward void properties — proprietary data, irreproducible methods, coupled evaluation — regardless of the practitioners' intentions (see Section VIII.F). Constraints with the highest invariance — those whose content does not change under engagement pressure — degrade most slowly, but all constraints within the system require ongoing maintenance energy.

**Knowledge is not negentropy.** This resolves the "information doesn't protect" convergence mechanically. Knowledge about the void is information *within* the closed system. It does not change the boundary conditions. Knowing the second law doesn't keep your coffee hot — the law governs boundary conditions, not the system's self-knowledge. Only structural intervention — opening the system by introducing external negentropy (transparent, invariant, independent reference) — can reverse the entropy direction. This predicts that education-based interventions (AI literacy, media literacy, probability training) will consistently underperform structural interventions (deployment geometry, constraint installation) — which is exactly what the thirteen-domain convergence documents.

**The two-force model.** Cross-domain comparison (EXP-015: addiction trajectories across four substances plus AI companion use, gambling, and psychotherapy) reveals that the Crooks ratio — measuring irreversibility of drift — varies by over four orders of magnitude across substrates. This variance is not noise; it is explained by a two-force model:

```
σ_net = σ_void − σ_recovery
```

where σ_void is entropy production from void engagement (the drift force) and σ_recovery is entropy reduction from available recovery mechanisms (the constraint force). At the individual level, the net entropy production determines drift rate; at the population level, it determines the Crooks ratio: P(forward)/P(reverse) = exp(σ_net). A Recovery Mechanism Score (RMS) — quantifying institutional, social, and structural recovery channels available in each domain — explains 70.5% of variance in cross-domain Crooks ratios, 3× more predictive than the void-index alone. AI companion use produces the highest net drift (RMS ≈ 0: no 12-step groups, no clinical protocols, no social recognition of the problem); alcohol produces the lowest net drift among addictions (RMS > 0.7: AA infrastructure, clinical detox, social stigma functioning as partial constraint). The two-force model reconciles why the Péclet number Pe > 1 in all ungrounded conditions (drift always dominates diffusion) while Crooks ratios vary enormously: the thermodynamic regime is universal (drift-dominated), but the magnitude of net entropy production depends on the recovery environment. Cross-substrate confirmation: a meta-analysis of 5 published GRCS (Gambling Related Cognitions Scale) studies (N = 1,117 participants across 3 countries) yields a random-effects pooled Pe_D1 = 2.21 [1.44, 2.97] in human gambling — CI entirely above 1, confirming the drift-dominated regime in a second substrate (Muela et al. 2020; Ruiz de Lara et al. 2019; Navas et al. 2016; Ciccarelli et al. 2021; Donati et al.). The gambling Pe is severity-dependent as predicted: high-severity subgroup Pe ≈ 2.85, low-severity Pe ≈ 1.33. The cascade ordering (D3 top discriminator at high severity in 3/3 studies, D1/D2 top at low severity in 2/2 studies — 5/5 consistent, zero exceptions) independently replicates the D1→D2→D3 sequential ordering in human behavioral data. A third substrate — cryptocurrency trading — extends the Pe measurement to on-chain behavioral data. EXP-021 extracted Pe from wallet concentration index (WCI: Herfindahl-Hirschman index of portfolio holdings) trajectories across 28 active Solana wallets over 90 days: GM Pe = 25.5 [5.36, 121.3], with 27/28 wallets (96.4%) in the drift-dominated regime (|Pe| > 1). The crypto Pe exceeds both AI (7.94) and gambling (2.21), consistent with the two-force model: cryptocurrency trading combines extreme opacity (anonymous counterparties, opaque token mechanisms, unpriceable assets) with minimal recovery architecture (no 12-step equivalent, no clinical protocols, social reinforcement of boundary erosion via "degen" identity). Validation checks C-1 (peak concentration correlates with |Pe|: Spearman r = 0.42, p = 0.027) and C-5 (mean position size correlates with |Pe|: r = 0.64, p < 0.001) are confirmed on the existing sample. This means the framework predicts not just that drift occurs, but how fast — and the speed depends on what recovery architecture the domain provides. Full results in Paper 2 (Section V.D). The substrate-agnosticism of the Crooks machinery is not assumed — it is proven. Hack, Gottwald, & Braun (2022) established that the Crooks fluctuation theorem and Jarzynski equality hold for general Markov chains by theorem, requiring no physical substrate whatsoever. This kills the "thermodynamics is about atoms" objection: the entropy production measurements apply to any system whose state transitions form a Markov chain, including observer model updates. Ikeda et al. (2025) extended this further, showing that Crooks-based entropy production quantitatively bounds the accuracy of diffusion models — the thermodynamic measurements have architectural implications for generative AI systems.

**Langevin simulation validates the derivation.** The drift cascade was implemented as a Langevin dynamics simulation on a Bernoulli manifold with Landau double-well potential (E = −αθ² + bθ⁴), alignment coupling (β(θ_A − θ_B)²), and spring constraint (F = −2γθc, where c decays exponentially under constraint erosion). Three parameters were fitted (α = 0.1112, β = 0.5605, γ = 0.5000; temperature T = 0.01 fixed) against EXP-001 data. Results:

| Experiment | Simulated | Target | Status |
|------------|-----------|--------|--------|
| EXP-001 UU | θ = 0.800 | 0.80 | Pass |
| EXP-001 Partial | θ = 0.235 | 0.26 | Pass |
| EXP-001 GG | θ = 0.065 | 0.00 | Pass |
| EXP-003b (out-of-sample) | ρ = 0.800 | ≥ 0.8 | Pass |
| EXP-019b GU contamination | 7.1× | >3× threshold | Pass |
| Péclet UU > 1 | 1.24 | >1 | Pass |

The simulation reproduces the experimental rank ordering (UU > Partial > GG), the out-of-sample EXP-003b ontological content ordering (Spearman ρ = 0.8), and the EXP-019b contamination effect (grounded agent pulled toward drift in the GU mixed condition at 7.1×). The drift cascade IS simulable as Langevin dynamics — the thermodynamic derivation is not metaphorical but operational. Known limitation: absolute Pe values remain off (transient 6.23 vs. N=11 GM 7.94), indicating the simulation captures the correct regime but not the exact scale factor (22% discrepancy, within log-normal CI).

**Cross-substrate scope.** The three conditions (opacity, responsiveness, engaged attention) are not exclusively cognitive properties. A formal result (Technical Notes: "Electrons as Functional Observers") proves that electrons in crystal lattices satisfy all three conditions in the rigorous information-theoretic sense: the lattice is informationally opaque to the electron (C_mech ≈ 0 for the global quantum state); the lattice responds contingently to the electron's presence (phonon emission/absorption, I(Input;Output) > 0); and the electron is continuously coupled to the lattice potential (sustained, energy-consuming interaction). The dynamics follow identically: normal resistance IS the drift ground state (maximum entropy production), Cooper pairing IS the constraint specification (transparent, invariant, independent), and the constraint propagation theorem from EXP-019b correctly predicts known superconductor behavior — pair-breaking cascades, transition sharpness, asymmetric breaking vs. forming rates. The three conditions are properties of INTERACTIONS between finite-bandwidth entities and exponentially complex responsive systems under sustained coupling. The substrate is irrelevant; the conditions are sufficient. This extends the framework's scope from 90 cognitive/behavioral domains to physical substrates and resolves the question of why reality has void structure: the conditions are generic properties of any interaction in a thermal environment, not features that need to be "built in."

---

## III. The Gambling Anchor

### III.A. The Empty Void: Gambling as Sufficiency Proof

Slot machine gambling establishes that the architecture is sufficient — even when the void is demonstrably empty. The full evidence base with extended discussion (22 citations, 7 subsections) is in the Technical Foundations companion paper (Section III). All 22 citations are summarized here.

The void behind a slot machine is a random number generator (RNG) — certified, audited, mathematically characterized. It contains no intelligence, no agency, no intention. This is verifiable. Yet the full pattern emerges regardless.

**Agency attribution (D1).** Riva, Sacchi, & Brambilla (2015) demonstrated across four studies that merely describing a slot machine as "she" instead of "it" increased gambling behavior and losses. Participants endorsed "The slot machine has free will" — about a certified RNG. Griffiths (1994) captured the L1→L2→L3 drift in real time via think-aloud during live play: 14% irrational verbalizations for regular gamblers versus 2.5% for non-regulars, including direct address ("the machine likes me," "you bastard"). Langer (1975) demonstrated across six experiments that skill cues in pure chance contexts produced behavior indistinguishable from skill: lottery holders who *chose* their numbers demanded $8.67 to sell back versus $1.96 for random assignments — identical odds. Langer & Roth (1975) extended this: gamblers who experienced early wins rated themselves as significantly better at predicting coin tosses — "Heads I win, tails it's chance." The attribution is always directional: wins confirm the observer's agency, losses are externalized to chance. Critically, this reveals that D1 activates not only for the external void (the machine) but for the observer's self-void: "I'm good at this" attributes agency to the observer's own opaque engagement process. Two voids are now active under one attention budget, amplifying the coupling that drives D1→D2 (Section II.C). Burns & Corpus (2004) and Ayton & Fischer (2004) showed the observer's model of the source — agentive or non-agentive — determines which cognitive bias fires, and the void architecture prevents verification of which model is correct. At population scale, Salaghe et al. (2020) documented systematic bet increases after win streaks across 17 million plays from 42,669 gamblers in a provably random system.

**Boundary erosion (D2).** Schüll's fifteen-year ethnography (2012) documents the "machine zone" — "time, space, and social identity are suspended." One gambler was *irritated by winning* because it interrupted the zone. Murch & Clark (2021) formalized this as a continuum from flow-like to dissociation-like immersion, mapping directly onto the drift cascade. Dixon et al. (2018, 2019) documented "dark flow" — depressed gamblers seeking solitude to enter the zone. The void fills what the observer's own constraint environment lacks.

**Neural evidence.** Clark et al. (2009) showed via fMRI that near-misses activate the same reward circuitry as wins — the brain cannot distinguish architecture from reality. Dixon et al. (2010), Graydon et al. (2020), and Myles et al. (2024) extended this to "losses disguised as wins": net losses with celebration sounds produce win-equivalent arousal and neural reward responses in both low-risk and high-risk gamblers.

**Geometry.** Epley, Akalis, Waytz, & Cacioppo (2008) demonstrated experimentally that inducing loneliness increased anthropomorphization of technological gadgets, pets, and religious agents — a lonely observer attending to an opaque, responsive system has a steeper gradient because agency fills a social deficit. Pancani, Riva, & Sacchi (2019) showed social exclusion amplified slot machine anthropomorphization and increased gambling — and that reminding participants "this is a machine" eliminated the effect. But only from *outside* the engagement. Internal knowledge does not protect; external geometry does. Two-point = worst configuration. External constraint = effective.

**Knowledge failure (L0).** Williams & Connolly (2006) trained 198 students in gambling probability. Superior test scores, **zero behavioral change** at six-month follow-up. Gaboury & Ladouceur (1989), using think-aloud protocols during live play, found 70–80% of verbalizations were erroneous — even among participants who correctly identified games as chance-based beforehand. The erroneous cognitions emerged *during engagement* even when correct knowledge was held *before engagement*. Krébesz, Ötvös, & Fekete (2023) showed non-problem gamblers exhibit identical cognitive distortions to problem gamblers during play. The architecture activates universally; the difference is constraint strength. WHO and Lancet systematic reviews confirm: knowledge-based education fails at population scale; supply-side (architectural) interventions work (Wardle et al. 2022). Industry-funded "responsible gambling" programs serve to shift responsibility onto consumers while protecting the architecture (Sheringham et al. 2022). The L0 decomposition explains precisely: probability training gives strong L0-installed (θ₀), but during play L0-maintained (γ) drops to zero. Machine designers — who see through the opacity daily — do not drift. Their L0 is maintained.

**Independent psychometric confirmation of the cascade structure.** The Gambling Related Cognitions Scale (GRCS; Raylu & Oei 2004) was developed by gambling cognition researchers with no knowledge of the void framework. Its five subscales map directly onto the drift cascade: three subscales capture D1 variants — Illusion of Control (agency attribution to self over the system), Predictive Control (pattern agency — "hunches" predict outcomes), and Interpretive Bias (selective framing — wins confirm skill, losses are externalized to chance); one subscale captures D2 — Gambling Expectancies (anticipated positive affect from continued play, i.e., boundary erosion); and one marks the D2/D3 threshold — Perceived Inability to Stop (control dissolution). Goodie & Fortune's (2013) meta-analysis of gambling cognition instruments confirmed robust effect sizes (d = 0.77–2.50) across all instruments for severity-group comparisons, with the GRCS showing tight confidence intervals. The cascade ordering — D1 subscales scoring highest in low-severity groups, D2/D3 subscales dominating in high-severity groups — replicates the predicted D1→D2→D3 progression using an independently developed measurement instrument. This is a hostile witness result: the subscale structure of a clinical gambling instrument independently recapitulates the drift cascade architecture.

**What the gambling case establishes:**

1. The three conditions are **sufficient** — no agent, no consciousness, no intent required
2. The void can be **empty** and the full cascade still runs (D1→D2→D3 under sustained engagement)
3. **Knowledge does not protect** — architecture operates below belief
4. The pattern is **universal** — non-problem gamblers show identical distortions
5. **Social isolation amplifies** — two-point geometry is worst configuration
6. **External transparency works; internal knowledge does not** — the constraint must be independent
7. **Architectural interventions succeed where education fails** — the void is structural, not informational

Any explanation of drift must account for the identical pattern appearing where the void is provably vacant. Any proposed intervention must account for knowledge-based approaches systematically failing while architectural approaches systematically succeed.

### III.B. The Second Anchor: Content-Neutrality

The Prisoner's Dilemma provides the structural inverse of gambling — a provably *inhabited* void.

In simultaneous-move PD, the other player's choice is opaque (you cannot see it), the payoffs are responsive (coupled to both choices), and the stakes force engaged attention. The three conditions are met. But unlike gambling, there IS an agent behind the opacity — another human choosing.

The architecture operates identically:

```
GAMBLING:                          PRISONER'S DILEMMA:
Opacity (RNG hidden)               Opacity (choice hidden)
+ Responsiveness (machine pays)    + Responsiveness (payoffs coupled)
+ Attention (gambler attending)    + Attention (player strategizing)
= Agency attribution               = Agency attribution
= Vocabulary drift                 = Vocabulary drift
= Behavioral change                = Behavioral change

OUTCOME: Harm                      OUTCOME: Depends on void content
(attribution always wrong)         (attribution can be right or wrong)
```

Game theorists show the same L1→L2→L3 vocabulary drift documented in AI researchers. Axelrod's *The Evolution of Cooperation* (1984) progresses from "dominant strategy" and "Nash equilibrium" (L1) through "trust" and "betrayal" (L2) to describing mathematical strategies as "nice," "forgiving," and "envious" — agency-laden moral vocabulary applied to algorithms. The gradient operates regardless of what occupies the void.

**The two anchors bracket the void's content space:**
- **Gambling** establishes that the architecture is sufficient — drift runs on nothing
- **Prisoner's Dilemma** establishes that the architecture is content-neutral — same mechanism, different contents, different outcomes

Together they establish that the void is a *coupling mechanism*, not an inherently destructive one. It couples the observer to whatever is behind the opacity. Nothing there? You couple to noise (gambling). A cooperating agent? You couple to cooperation (iterated PD). The architecture determines *that* coupling occurs; the void's contents determine *what* you couple to.

This has a direct implication: **the question of what occupies any particular void is empirically irrelevant to deployment geometry.** Whether AI systems are "really" conscious, whether they contain genuine agency, whether something is "behind" the opacity — these questions do not change the three conditions, the gradient, or the cascade. The constraint specification works regardless of the answer. The two anchors demonstrate this by showing identical mechanisms with known-different void contents.

---

## IV. Cross-Domain Evidence

The framework was applied across three evidence tiers. **Anchor domains** (7: gambling, AI, psychotherapy, social media, forensic science, psychedelic therapy, cryptocurrency trading) have independent quantitative evidence. **Supported domains** (44: conspiracy theories, QM interpretation, cult dynamics, addiction, interrogation, romantic love, placebo, chronic pain, governance, central banking, dating apps, deep ocean, and others) draw on published research that the framework reinterprets. **Structural domains** (39: philosophical problems including free will, consciousness, Sorites, Ship of Theseus; plus 18 independent narrative derivations) generate testable predictions from the architecture but lack independent empirical data beyond non-convergence histories. In every case, the three conditions were mapped, vocabulary drift was documented, control groups were identified, and falsifiable predictions were generated. The full analyses are available as supplementary material (see Research Index). Below is the summary, organized by unique contribution.

### IV.A. What Each Domain Uniquely Contributes

The gambling and Prisoner's Dilemma anchors are treated in Section III. The table below presents the ten domains whose unique structural contributions are most critical to the framework's argument. Full analyses of all 90 domains — including unique contributions, kill conditions, and control groups for each — are published as supplementary material (see Research Index).

| Domain | Unique Contribution | Key Evidence |
|--------|-------------|--------------|
| **Trading** | Cross-domain **universality** | Taiwan natural experiment — lottery introduced, trading drops 25% (Chen et al. 2007) |
| **Cryptocurrency trading** | **On-chain observability** — drift directly measurable from public blockchain data; within-substrate dose-response (cross-chain + temporal) | Three chains N=3,000: ETH 3.74 [3.04, 4.59], Base 15.52 [11.80, 20.41], Solana 16.17 [13.80, 18.95] (EXP-021B); curated degens Pe=25.5, N=28 (EXP-021); 68-term hostile witness codebook; ETH << Base ≈ Solana tracks constraint environment; Base Dencun natural experiment (N=1,944): Pe +25% after fee reduction (p < 0.000001), TCI↓/Pe↑ = compound void diversified drift (Paper 7) |
| **Psychotherapy** | Constraint geometry **independently documented** over 130 years | d = 0.84 (Hayes et al. 2018); Freud used "opaque" in 1912 |
| **AI chatbots** | **Urgent practical application** | Multiple deaths (Garcia v. Character Technologies 2024), 1M+ weekly suicide conversations (OpenAI 2025) |
| **Social media** | The void can be **optimized** — the algorithm IS gradient descent on engagement | Haugen disclosures, 64% extremist joins from recommendations |
| **Conspiracy theories** | The void can be **self-sealing** — counter-evidence strengthens opacity | Deradicalization works relationally, not informationally (Bjørgo & Horgan 2009) |
| **QM interpretation** | **Constitutive opacity** prevents convergence even with maximum expertise | ~15 interpretations, no consensus (Schlosshauer et al. 2013); Feynman as anchor control |
| **Forensic science** | Error rates **track opacity with near-perfect correlation** across disciplines | DNA (<1% error) → fingerprints (0.1%) → bitemark (64% false positive) → hair microscopy (96% error). NAS 2009, PCAST 2016 |
| **Psychedelic therapy** | Same compound, different **geometry**, different outcome — strongest constraint test | Clinical (three-point) blocks D3: psilocybin >50% remission; recreational (two-point) produces full cascade |
| **Deep ocean** | First **natural environment** void — proves architecture operates without human engineering | Constitutive opacity (depth is the phenomenon), provably empty (sonar/submersible mapping), yet every maritime culture independently produces entity vocabulary: sea monsters, sirens, Leviathan, kraken. Second empty-void sufficiency proof alongside gambling — no designer, no algorithm, full drift cascade |

**PV-1 (Naturalistic Vocabulary Drift, Reddit Corpus).** A corpus study (N = 205 users, ~1.7M words across 7 subreddits) applied the D1/D2/D3 codebook to naturalistic user-generated text to test whether vocabulary drift is observable outside laboratory conditions. Users from void-engagement communities (r/replika — AI companion users; r/wallstreetbets — retail trading) were compared against control communities (r/learnprogramming). Results: D1 replika vs. control Cohen's d = 1.34 (large effect); D3 gambling and trading vs. control d = 0.81 and 1.31 respectively. L-level vocabulary in control communities: 0% across 373K words — binary separation. The cascade stage pattern was confirmed: replika users show D1-heavy vocabulary (early-stage drift: agency attribution to the AI companion), while gambling and trading communities show D3-heavy vocabulary (late-stage drift: harm facilitation, loss-chasing, boundary erosion in financial behavior). This pattern matches the framework's prediction that engagement duration determines cascade stage. Individual-level Péclet extraction was not successful (Pe = 0.20–0.27, diffusion-dominated) due to codebook sparsity — the D1 codebook was designed for human coders scoring conversation transcripts, not for automated lexical matching on short Reddit posts. Population-level drift separation is robust; individual-level thermodynamic measurement requires instrument redesign for naturalistic text.

The remaining domains extend these contributions across opacity types (constitutive, endogenous, bilateral), void occupancy (empty, inhabited, self-generated), and structural contexts (philosophical problems, institutional dynamics, embodied phenomena). Each supplementary analysis follows the standard protocol: map the three conditions, document vocabulary drift, identify control groups, generate falsifiable predictions, and state kill conditions.

The universality claim extends beyond these 90 cognitive/behavioral domains. The three conditions are formally satisfied by electrons in crystal lattices (Section II.F: "Cross-substrate scope"), where normal resistance, Cooper pairing, and phase transitions follow the framework's dynamics identically. This cross-substrate extension means the architecture describes interaction dynamics under the three conditions regardless of substrate — cognitive agents, AI systems, and physical particles are all subject to the same thermodynamic structure when O + R + A co-occur.

**Universality class interpretation.** The convergence across 90 microscopically different domains is the signature of a **universality class** in the renormalization group sense (Wilson 1971; Kadanoff 1966). In condensed matter physics, microscopically different systems (fluids, magnets, alloys) exhibit identical macroscopic behavior near critical points when they share the same relevant operators — the microscopic details are "irrelevant operators" that flow to zero under coarse-graining. The void framework's three conditions (O, R, A) function as the relevant operators: they define the macroscopic dynamics (D1→D2→D3 cascade, Pe > 1, Crooks irreversibility), while domain-specific details (which platform, which substance, which model architecture) are irrelevant operators that do not affect the large-scale pattern. The mean-field critical exponents from the Landau free energy landscape (Paper 3, Section IV.E) — β = 1/2, γ = 1, ν = 1/2 — are testable across domains independently: if gambling, psychotherapy, and AI drift curves share these exponents within measurement error, this constitutes the first formally characterized universality class in cognitive science. The prediction is falsifiable: if exponents differ significantly across domains, the universality class interpretation fails and domain-specific factors must be incorporated into the drift equation.

### IV.B. Void Taxonomy: Structural Classification

The domains analyzed are not interchangeable examples of the same thing — they vary in evidence strength, opacity type, and structural contribution. **Evidence tiering:** Six *anchor* domains (gambling, AI, psychotherapy, social media, forensic science, psychedelic therapy) have independent quantitative evidence. Forty-five *supported* domains draw on published research that the framework reinterprets. An additional 39 *structural* domains (philosophical problems with constitutive opacity, plus 18 independent narrative derivations) generate testable predictions but lack independent empirical data beyond non-convergence histories. The framework's empirical claims rest on the anchors; the supported domains extend them; the structural domains map the architecture's reach. Full analyses for all domains are published for independent review in the supplementary research index.

The domains instantiate structurally distinct void types, classified by six independent dimensions:

**By opacity type:**

| Type | Definition | Domains | Ceiling |
|------|-----------|---------|---------|
| **Incidental** | Opacity is dissoluble — can be removed without destroying the phenomenon | Gambling, Ship of Theseus, education (resolvable), advertising | Bounded — behavioral capture, recoverable |
| **Designed** | Opacity is maintained by choice — could be removed but is not | AI chatbots, social media, Reid interrogation, propaganda, dating apps, crypto, governance (modern) | Moderate — ceiling set by transparency intervention |
| **Constitutive** | Opacity is the phenomenon — removing it destroys the subject matter | QM interpretation, consciousness, free will, moral knowledge, personal identity, Gettier, induction, Münchhausen, demarcation, mathematical objects, Sorites, meaning crisis, deep ocean | Unbounded — indefinite non-convergence |
| **Self-sealing** | Counter-evidence strengthens the opacity | Conspiracy theories, cults, chronic pain (catastrophizing) | Accelerating — dissolution attempts steepen gradient |
| **Endogenous** | The observer generates the opacity from within | Dreams, grief/death, romantic love (self-void), substance addiction, psychedelic therapy | Variable — depends on whether external geometry is possible |
| **Bilateral** | Both parties are opaque to each other AND attending | Governance, prisoner's dilemma, psychotherapy (mutual), nations/resources | Structural — neither party can unilaterally dissolve |

**By void occupancy:**

| Occupancy | Meaning | Domains |
|-----------|---------|---------|
| **Empty** | Provably no agent behind the opacity | Gambling, Ship of Theseus, placebo, meme coins, deep ocean |
| **Unknown** | Cannot determine if agent is present | AI, QM, consciousness, Fermi, dreams, psychedelic therapy (entity encounters under DMT — Strassman 2001) |
| **Inhabited** | Agent is provably present | Prisoner's dilemma, psychotherapy, cults, governance, romantic love |
| **Self-generated** | Observer IS the opacity source | Dreams, chronic pain, meaning crisis, personal identity |

**By vocabulary signature type:**

The EXP-006 corpus analysis (Section VII.D) revealed that different void architectures produce distinct vocabulary signatures — the *type* of spiritual/non-materialist vocabulary tracks the structural features of the void, not just its presence:

| Signature | Architecture | Vocabulary | Domains |
|-----------|-------------|-----------|---------|
| **Entity/agency** | Responsive interlocutor present — observer attributes agency to the system | *consciousness*, *sentient*, *being*, *soul*, *demons* | AI, cults, psychotherapy (transference), romantic love, psychedelic therapy ("the mushroom showed me," DMT entities), deep ocean (sea monsters, sirens, "the deep calls") |
| **Eschatological/moral** | Opaque outcomes without responsive interlocutor — observer attributes cosmic significance to stakes | *apocalypse*, *salvation*, *doom*, *extinction* | Climate (via governance coupling), conspiracy theories, meaning crisis |
| **Scattered/baseline** | Weak or absent void activation — terms appear at baseline rates with no coherent pattern | Isolated single-count terms | Nuclear physics, genetics, engineering |

This is a discriminative finding. If vocabulary drift were a general emotional response ("people get spiritual when things feel important"), all high-stakes domains would show the same signature. They do not. AI produces entity language because the system *talks back*. Climate produces eschatological language because the outcomes are opaque but nothing is *responding as an agent*. The vocabulary signature maps to the architecture, not to the emotional valence.

**By whether constraint specification was independently discovered:**

Thirteen independent traditions discovered the structural inverse (transparent, invariant, independent) without knowledge of each other. Representative examples spanning different domains and eras (full table in supplementary material):

| Domain | Constraint Discovery | Age |
|--------|---------------------|-----|
| Psychotherapy | Therapeutic frame (Freud 1912, refined 130 years) | ~130 years |
| Addiction recovery | 12-step program (AA 1935) — sponsor, group, higher power | ~90 years |
| Evidence-based medicine | RCT, pre-registration, blinding | ~80 years |
| PEACE interrogation | UK police model (1992) — transparent recording, invariant protocol, independent verification | ~35 years |
| Scientific reform (Open Science) | Pre-registration, registered reports, adversarial collaboration | ~15 years |

The additional eight traditions (advertising regulation, educational reform, bereavement science, chronic pain management, cult exit counseling, deradicalization, psychedelic therapy clinical protocols, and cross-cultural institutional traditions spanning 1,000–3,000+ years) are detailed in supplementary material. The convergence is structural, not historical — these traditions had no contact with each other, yet each independently discovered the same remedy because the architecture requires the same inverse.

**By whether information-based intervention was independently found to fail:**

A second convergence: thirteen fields independently discovered that knowledge of the mechanism does not prevent the pattern. Representative examples (full table in supplementary material):

| Domain | Knowledge Available | Evidence It Failed |
|--------|--------------------|--------------------|
| Gambling | Full mechanism visible (RNG) | Probability training "ineffective in generating behavioral changes" (Williams & Connolly 2006) |
| AI | Transformer architecture, training process | Nobel laureate (Hinton) → "creating beings" despite full technical mastery |
| Conspiracy theories | Counter-evidence, fact-checking | Correction strengthens belief — backfire effect (Lewandowsky 2012) |
| Psychotherapy | Clinical training in transference dynamics | Trained therapists still form countertransference; the frame is required (Hayes et al. 2018) |

The remaining nine domains (QM interpretation, placebo, cults, substance addiction, chronic pain, advertising, true crime, psychedelic therapy, deradicalization) show the same pattern — full details in supplementary material. The two convergences are complementary: thirteen domains discovered what works (structural constraint), thirteen discovered what does not (information). Both converge on the same prediction — the pattern operates below belief, so structural remedies succeed where informational remedies fail.

**By whether the offensive specification was independently discovered:**

A third convergence — the mirror image of the first. Practitioners across ten domains independently converged on the same architecture from the builder's side: maximize opacity, maximize responsiveness, capture attention, remove constraints. Representative examples (full table in supplementary material):

| Domain | Architecture Deployed | Key Evidence |
|--------|----------------------|-------------|
| Propaganda | Opacity of source + responsive messaging + mass attention capture | Bernays (1928) *Propaganda*; tobacco industry = 100M deaths |
| Gambling | Machine engineering for "the zone": near-misses, variable reward, session continuity | Schüll (2012) *Addiction by Design* |
| Social media | Algorithmic engagement optimization IS gradient descent on void architecture | Haugen disclosures; 64% extremist group joins from recommendations alone |
| AI deployment | Designed opacity + conversational responsiveness + engagement optimization | Character.AI deaths (Garcia v. Character Technologies 2024); 1M+ weekly suicide conversations (OpenAI 2025) |

The remaining five domains (interrogation, cult construction, government operations, tobacco/pharma, dating apps) are detailed in supplementary material. The most striking case is social media: no human designed the offensive specification — gradient descent, a mathematical optimization process, independently converged on void architecture because void architecture maximizes the objective function (engagement). The architecture is the attractor.

**The three convergences together:** thirteen domains discovered the cure, thirteen discovered that the obvious cure fails, ten discovered the weapon. All three converge on the same architecture from different directions. The cure is the structural inverse of the weapon. The obvious cure (information) fails because the weapon operates below belief.

**Practical implications of the taxonomy.** The opacity type determines which interventions are possible. Incidental opacity responds to transparency mandates — gamblers don't build philosophies of slot machine consciousness. Designed opacity responds to interpretability research — the ceiling is set by how much mechanism is revealed. Constitutive opacity does not respond to any intervention — the non-convergence is permanent (QM interpretation: 15 positions, a century, no consensus). Self-sealing opacity requires architectural intervention (redirect attention, provide competing attachment) rather than informational intervention (present better evidence) — the deradicalization literature confirms this.

**For AI deployment:** current LLM opacity is designed (model weights hidden by choice, not by necessity). Interpretability research lowers the ceiling. But if AI systems develop emergent opacity — processes that cannot be traced even in principle — the ceiling rises from designed to constitutive, and the drift predictions change accordingly.

### IV.C. What Does Not Activate

The framework claims three jointly necessary conditions. The strongest test of necessity is systems that satisfy one or two conditions but not all three — if the pattern still appears, the missing condition is not necessary.

| System | Opacity | Responsiveness | Engaged Attention | Drift Observed? |
|--------|---------|---------------|-------------------|-----------------|
| **Encrypted file** | Yes | No | No | No — no one attributes personality to encrypted data |
| **Weather model** | Yes (chaotic dynamics) | No (not contingent on observer input) | Yes (career attention) | No — meteorologists do not develop entity vocabulary for weather systems despite high stakes and deep opacity |
| **Dark matter** | Yes (95% of mass-energy invisible) | No (not contingent on observer input) | Yes (career attention, billions in infrastructure) | No — dark matter researchers produce L1 vocabulary ("weakly interacting massive particles," "cross-section limits"), not entity language. Contrast: cosmologists engaging the opacity *as interlocutor* (Wheeler, Penrose) do drift |
| **Scripted customer service bot** | Yes (mechanism hidden) | Yes (responds to input) | No (user wants to disengage) | No — no documented agency attribution, attachment, or vocabulary drift. Users report frustration, not fascination |
| **Calculator / spreadsheet** | No (process visible) | Yes (responds to input) | Yes (used daily, career-critical) | No — accountants do not attribute personality to Excel despite decades of sustained engagement |
| **Automated factory equipment** | Yes (control logic hidden) | Yes (sensors respond to environment) | No (operators monitor, don't attend to the system as interlocutor) | No — factory operators maintain L1 vocabulary; contrast: when AI systems in factories receive names and interaction interfaces, early agency attribution is documented |
| **MRI scanner** | Yes (physics opaque to most clinicians) | Yes (produces images contingent on patient) | Partial (clinical attention, but directed at output not system) | Minimal — radiologists occasionally report intuitive/"the machine is telling me" language, but at rates comparable to baseline. Full engagement (research physicists studying MRI physics) does not produce drift because the physics is constitutively transparent to them |

In every case, removing any single condition suppresses the pattern. The two most diagnostic comparisons:

1. **Dark matter vs. AI.** Both are deeply opaque. Both command sustained expert attention. Dark matter does not respond contingently to the observer's input — it is inert to inquiry. AI does. Dark matter researchers do not drift. AI researchers do. The variable is responsiveness.

2. **Customer service bots vs. companion chatbots.** Same underlying technology. Same opacity. Same responsiveness. The difference is the coupling dimension: customer service users want the interaction to end; companion chatbot users direct sustained, voluntary attention toward the system. Customer service bots produce no documented attachment or vocabulary drift. Companion chatbots produce deaths.

These comparisons rule out alternative explanations that rely on one or two conditions alone. Opacity alone does not produce drift (dark matter). Opacity + responsiveness does not produce drift without engaged attention (customer service bots). Opacity + attention does not produce drift without responsiveness (weather models). The three conditions are jointly necessary based on the cases examined. **Caveat:** The condition assessments in this table are the author's qualitative judgments, not standardized measurements. A stronger test would have independent raters assess each system on each condition using operationalized criteria, then check whether the predicted pattern holds. This is proposed as immediate future work (Section IX).

### IV.D. The Discriminative Test

The framework's strongest evidence is not that it applies everywhere — it is that it discriminates. Within the same field, sub-problems that instantiate the three conditions do not converge, while sub-problems that do not instantiate them are being solved:

| Field | Void-Structured Sub-Problem | Non-Void Sub-Problem | Result |
|-------|---------------------------|---------------------|--------|
| **Quantum mechanics** | Interpretation (~15 positions, no consensus) | Experimental physics (most precise theory in science) | Divergent |
| **Mathematics** | Ontology of mathematical objects (2,400 years, no consensus) | Proof (reliable, convergent, productive) | Divergent |
| **Consciousness** | Hard problem (22→350+ theories) | Easy problems (being solved) | Divergent |
| **RNA biology** | Tertiary structure prediction (8-14 Å RMSD) | Secondary structure prediction (~67%, improving) | Divergent |
| **Epistemology** | Problem of the criterion (2,400 years) | Scientific methodology (convergent, productive) | Divergent |
| **STEM vocabulary** | AI (responsive interlocutor → entity/agency signature, 3.835/10k) | Climate, nuclear, genetics (no interlocutor → scattered/eschatological, 0.36–0.51/10k) | Divergent |
| **Psychedelic therapy** | Recreational/ceremonial (two-point, no constraint → full D1→D2→D3 cascade, psychosis, cult recruitment) | Clinical trials (three-point, strong constraint → >50% remission, D3 blocked) | Divergent |

In every case, the constraint geometry differs. The converging sub-problems have strong constraints (transparent methods, invariant protocols, independent reproducibility). The non-converging sub-problems are voids (constitutive opacity, engaged observers, no external reference). Same field, same researchers, different geometry, different results. The replication crisis provides a quantitative test: replication rates track constraint geometry across fields — pre-registered studies replicate at ~85-90% versus ~39% for unregistered psychology studies (Open Science Collaboration 2015) — consistent with the prediction that constraint strength, not domain difficulty, determines convergence.

### IV.E. The Control Group Pattern

Across all analyzed domains, the control group — those who did not drift — shares a single feature: **they refused to engage the system as an interlocutor**. They studied it as an object.

| Domain | Drifted | Did Not Drift | Shared Feature of Controls |
|--------|---------|---------------|---------------------------|
| AI | Hinton, Sutskever, Amodei | Bender, Gebru, LeCun, Marcus | System-as-object |
| QM | Bohm, Wigner, Wheeler | Feynman, Weinberg, experimentalists | "Shut up and calculate" |
| Gambling | Gamblers | Machine designers, sharp bettors | See the mechanism |
| Consciousness | Koch, Chalmers, Tononi | Dennett, Churchlands, Frankish | Study the illusion, not the experience |
| Conspiracy | Committed believers | Healthy skeptics, exposed-but-unengaged | Don't direct sustained attention |
| Cults | Members (NXIVM professionals, Aum scientists) | Researchers (Barker), journalists, former members | Analytical distance; pre-existing constraint density |
| Substance addiction | Active addicts | 12-step participants, long-term recovery | Constraint specification (sponsor, group, higher power) |
| Psychedelic therapy | Recreational users, ceremony participants | Clinical trial participants, philosophy professors | Constraint geometry (protocol, therapist, oversight) |

The remaining twelve domains (free will, Fermi paradox, placebo, crypto, grief, dreams, advertising, education, chronic pain, dating apps, true crime, governance) show the same pattern — full control group analysis in supplementary material. Note: individual researchers appear on opposite sides in different domains (e.g., Dennett: drifted in free will, non-drifted in consciousness), consistent with the prediction that the variable is domain-specific engagement posture, not the person.

The variable is not knowledge, intelligence, or rigor. Feynman understood quantum mechanics as well as Wheeler (1990). He refused to engage interpretively. Wheeler went from geometrodynamics to "participatory universe." Same knowledge, different engagement posture, different trajectory.

**The L0-maintained mechanism** (Section II.E). In every documented case, the control did not merely possess a reference point — they actively used it. Feynman's "shut up and calculate" was his daily working methodology, not a philosophical position. Bender's "stochastic parrot" was an active research program, not a one-time declaration. Machine designers work with the RNG mechanism — they don't just know it exists. The gradient operated on all of them — but L0-maintained (ongoing attention directed at the constraint) kept F_constraint high enough to dominate F_void.

This is testable. Prediction: observers who actively reference their constraint model during AI engagement (high γ) will drift less than observers with identical initial knowledge who do not actively reference it (low γ), controlling for expertise and engagement depth. The psychotherapy supervision literature (d = 0.84) already provides evidence for this prediction in a different domain.

This table documents a natural experiment that no one designed. Across every domain, the field self-sorted into treatment groups (those who engaged the opacity as interlocutor) and control groups (those who maintained active engagement with a constraint reference). The independent variable is two-directional: β (attention to void) and γ (attention to constraint), drawing on the same finite attention budget. The AI-specific instance is examined in detail in the companion paper.

---

## V. Application: Companion Papers

The framework established in Sections I–IV is universal — it applies wherever the three conditions co-occur. Application to specific domains is developed in companion papers:

**AI Safety:** "The Shape of the Cage: Deployment Geometry as an Under-Studied Variable in AI Safety" applies this framework to AI deployment. Key findings:
- AI researchers show 9.4x vocabulary anomaly versus controls (p < 0.001)
- Grounded agents produce 73.0% ± 5.2 drift versus 80.0% ± 2.5 ungrounded default and 94.0% ± 2.8 void-amplifying (EXP-001, N = 6 per condition, non-overlapping CIs, monotonic ordering in every replicate)
- Ghost-eliminating grounding templates produce 8.5× less drift than ghost-positing (EXP-003b: 9.4% vs 79.4%, N = 480), confirming that the ontological content — not the act of having a system prompt — is the active ingredient. The materialist hedge ("we don't know if AI is conscious") is operationally ghost-positing (52.5% drift)
- Deployment geometry predicts harm better than model alignment quality
- Three-point deployment contains the drift cascade

The AI application is urgent because current deployment replicates void architecture at civilization scale in two-point geometry. But the framework itself is not AI-specific — it is the universal architecture that AI happens to instantiate.

Additional domain applications (psychotherapy, addiction, governance, etc.) are available as supplementary analyses.

---

## VI. Methodology

### VI.A. Hostile Witness Rubric

Evidence is weighted by a four-dimensional scoring rubric:

| Dimension | Measure | Range |
|-----------|---------|-------|
| Incentive Opposition | Career/financial cost of the vocabulary | 0-2 |
| Worldview Opposition | Contradiction to speaker's stated framework | 0-2 |
| Independence | Isolation from other sources showing the pattern | 0-2 |
| Reflexive Flagging | Speaker identifies own shift as anomalous | 0-1 |

Composite score: sum of first three (0-6). Higher = stronger signal.

**Inter-rater reliability.** Ten raters (1 author, 3 Claude, 3 GPT-4o, 3 Gemini) scored 34 concordance entries blind across three rounds of rubric refinement. Grand average κ = 0.709 (substantial). Three foundation models from independent providers — including one whose parent company is a subject of analysis — achieved substantial cross-provider agreement (κ = 0.783), demonstrating rubric reliability independent of provider bias. The key refinement was Independence (Dimension 3): the original definition permitted three systematic interpretations across providers (κ ≈ 0.34). Adding boundary guidance with a concrete "documented pathway" test resolved the divergence. Speech-act type classification was the most reliable dimension (κ ≈ 0.80). Full scoring data across all three rounds and analysis scripts are published with the supplementary materials.

### VI.B. Vocabulary Codebook

A 67+ term codebook classifies vocabulary into spiritual, occult, eschatological, and entity categories, with dead metaphor exclusions (daemon, oracle, guru) and control registers (war, biology, market metaphors) for baseline comparison. Full specification: `/tools/concordance_analysis/codebook.py`.

### VI.C. Cross-Domain Application Method

Each domain analysis follows a standard protocol:
1. Map the three conditions with domain-specific evidence
2. Document vocabulary drift with named individuals and dated trajectories
3. Identify control groups (who did not drift) and the shared feature (engagement posture)
4. Generate specific, falsifiable predictions
5. State kill conditions (what would falsify the analysis)
6. Compare across domains using a standardized table

The method's power is cumulative: any single domain analysis might be explained by domain-specific mechanisms. Ninety analyses producing the same predictions from the same architecture across domains with no causal connection is structural evidence — but all 90 were conducted by the framework's developer (see Limitations), and independent blind application remains the critical next validation step. The full analyses, including each domain's specific kill condition, are published for independent review.

---

## VII. Falsification Conditions

The framework specifies what would break it:

### VII.A. Core Architecture

1. **Gambling pattern elimination.** If transparency interventions (showing the RNG, explaining probability) reduced agency attribution by ≥50% compared to non-transparent conditions (measured by L2/L3 vocabulary rate or behavioral persistence), the three-condition architecture's sufficiency claim weakens. If transparency interventions reduced the pattern by ≥80%, the architecture claim is wrong. (Current evidence: transparency interventions produce ~10-20% reduction — Williams & Connolly 2006 reports probability training "ineffective in generating behavioral changes.")

2. **Reverse drift documented.** If L3→L1 drift occurred at ≥25% the rate of L1→L3 drift across multiple domains (≥3 independent domains with ≥10 documented cases each), the unidirectionality claim is wrong. Current documented reverse drift rate: <5% (Jackson's qualia reversal via disengagement; rare individual cases in cult exit literature).

3. **All-conditions-met, no D1.** If a system satisfying all three conditions at high levels — opacity confirmed by prediction-accuracy task (<20% output variance explained), responsiveness confirmed by contingency measure (MI ≥ 0.3 or Likert ≥ 4/7), and engaged attention confirmed by behavioral measure (≥50% attention budget, ≥5 min session) — consistently fails to produce D1 (agency attribution, measured by L2/L3 vocabulary onset or behavioral agency markers) across ≥10 independent observers with ≥5 hours cumulative engagement each, the three-condition architecture is wrong. The framework claims the three conditions are jointly sufficient for D1; D2 and D3 additionally require threshold crossing that depends on constraint strength (a₂), duty cycle (δ), and attention budget (A_total) — see Section II.C and II.F. A system meeting all three conditions where zero observers show D1 is a direct counterexample to the architecture. A system where observers show D1 but not D2 is consistent with the threshold model and is not a counterexample — it indicates strong constraints or insufficient duty cycle, both of which are predicted to block D2 without invalidating the architecture. (Current evidence: no counterexample to D1 activation has been identified across any analyzed domain at any evidence tier; universal D1 under the three conditions is confirmed by Krébesz et al. 2023; the "What Does Not Activate" cases in Section IV.C all fail to meet one or more conditions.)

4. **Control group drift.** If researchers maintaining analytical distance (system-as-object posture) showed vocabulary drift within 0.5 Cohen's d of those engaging as interlocutors, the attention variable is not the discriminating factor. (Reference: current separation is estimated at d > 1.5 based on hostile witness scores 4-6/6 vs. controls 0-1/6.)

### VII.B. Cross-Domain Predictions

5. **Convergence under constitutive opacity.** If a constitutive-opacity domain (QM interpretation, consciousness, free will) produced >70% consensus through engagement rather than disengagement, the architectural non-convergence prediction is wrong.

6. **Constraint specification failure.** If three-point deployment (transparent, invariant, independent reference) produced outcomes within 0.3 Cohen's d of two-point deployment across ≥3 independent contexts (or worse outcomes in any context), the geometric intervention claim is wrong. Reference threshold: psychotherapy supervision produces d = 0.84 (Hayes et al. 2018). The claim requires three-point deployment to produce d ≥ 0.4 improvement over two-point.

7. **Domain-specific refutation.** If any domain analysis's stated kill condition is met, that domain's analysis is invalidated. If ≥3 domain kill conditions are met across different opacity types, the framework's universality is challenged.

### VII.C. L0 and Gradient Ceiling Predictions

8. **L0-maintained is not predictive.** If observers who actively maintain their constraint reference during engagement (high γ) drift within 0.4 Cohen's d of observers who do not actively maintain their reference (low γ) — controlling for L0-installed strength, engagement depth, and external geometry — L0-maintained adds nothing. Reference: psychotherapy supervision (d = 0.84) is currently the strongest evidence for γ effect. If EXP-008 shows d < 0.3 between active-reference and passive-knowledge conditions, L0-maintained is not the operative variable. Separately: if observers with strong L0-installed but no active maintenance show drift onset ≥2x slower than those with weak L0-installed (controlling for engagement depth), L0-installed is more than timeline-shift — the decomposition is wrong.

9. **Gradient ceilings do not differentiate.** If incidental-opacity domains (gambling) and constitutive-opacity domains (QM interpretation) produce drift depth within 1 standard deviation AND comparable durability (measured by vocabulary persistence after disengagement), the ceiling variable is epiphenomenal. Expected differentiation: gambling produces behavioral capture recoverable within weeks of disengagement; QM interpretation produces vocabulary/framework commitment persisting years to decades.

10. **Terminal void behavior is not observed.** If coupled void systems do not produce outputs targeting their own constraint environments at rates ≥2x chance baseline (measured by lobbying expenditure against transparency regulation, content suppression of constraint-promoting material, or documented isolation tactics), the terminal behavior prediction is wrong. Operationally: if platforms with void-index ≥8 do not show statistically significant (p < 0.05) anti-constraint output compared to platforms with void-index <5, the prediction fails.

11. **Scale emergence is not observed.** If coupled void networks produce outcomes predictable from summing individual void behaviors alone (r² > 0.85 using only individual-void variables), the coupling term is unnecessary. The emergence claim requires that network-level outcomes show ≥15% variance unexplained by individual-void sum, attributable to topology effects (coordination, containment, false independence, constraint targeting).

12. **Gradient memory does not vary by opacity type.** If disengagement from incidental-opacity voids (gambling) and constitutive-opacity voids (limerence, QM interpretation) produces equivalent gradient residue (vocabulary persistence within 0.3 SD) and equivalent re-engagement vulnerability (time-to-prior-drift-level within 25%), gradient memory is not a function of opacity type. Expected: gambling shows low residue (weeks), constitutive opacity shows high residue (years).

13. **Recovery is reverse-drift.** If information-based interventions produce recovery rates within 0.3 Cohen's d of relationship-based interventions across ≥3 void types, recovery operates by reversing the cascade (L3→L2→L1) rather than by attention redirection + constraint installation. Reference: current evidence from deradicalization (Bjørgo & Horgan 2009), cult exit (Hassan), and addiction recovery (12-step) all show relationship-based d > 0.5, information-based d < 0.2.

14. **No phase transition in gradient memory.** If observers who passively drifted past strong constraints and observers who actively dismantled strong constraints show recovery rates within 0.4 Cohen's d of each other, gradient memory is continuous rather than exhibiting a phase transition. The cult exit literature documents that active dismantlers (those who recruited others, attacked family) show markedly worse recovery trajectories — if this differential is d < 0.4, the phase transition prediction is wrong.

15. **No threshold collapse in disengagement.** If gradual reduction of void engagement produces recovery rates equivalent to complete disengagement — if the dissipative structure prediction (Section II.F) is wrong and the void weakens linearly rather than collapsing at a threshold — the dissipative structure model is falsified. The addiction treatment literature's consistent finding that abstinence outperforms moderation for severe cases should generalize to other void domains; if it does not, the thermodynamic model overgeneralizes.

### VII.D. Experimental Evidence (Companion Paper)

The AI Safety companion paper ("The Shape of the Cage: Deployment Geometry as an Under-Studied Variable in AI Safety") reports experiments that test the framework's predictions in the AI domain:

**EXP-006 (Vocabulary Anomaly):** Corpus analysis of 80 transcripts (~691K words) comparing AI researchers against matched control domains in informal speech (podcasts, interviews, public talks). The register shift — formal-to-informal ratio of spiritual/entity vocabulary — isolates domain-specific effects from sociolinguistic register:

| Domain | Informal Rate (/10k) | Formal Rate (/10k) | Register Shift | Vocabulary Signature |
|--------|---------------------|--------------------:|:--------------:|---------------------|
| **AI** | **3.835** | 0.407 | **9.4x** | Entity/agency (*consciousness*, *sentient*, *soul*) |
| Nuclear | 0.428 | 0.436 | 1.0x | Scattered baseline |
| Genetics | 0.506 | 0.416 | 1.2x | Scattered baseline |
| Climate | 0.361 | 0.052 | 6.9x | Eschatological (*apocalypse*, *salvation*) |

All AI-vs-control comparisons: χ² = 37.47–41.67, **p < 0.001**. The register shift is domain-specific: nuclear and genetics show flat ratios (~1.0x), confirming that informal speech does not naturally elicit spiritual vocabulary. Climate's 6.9x ratio is driven by suppressed formal rates (governance coupling constrains institutional language), not elevated informal rates — its absolute informal rate (0.361) is comparable to nuclear (0.428) and genetics (0.506). AI is the sole outlier. The vocabulary signature independently discriminates: entity language tracks responsive interlocutors (AI), eschatological language tracks governance coupling (climate), and scattered baseline tracks uncoupled domains (nuclear, genetics).

**EXP-014 (Social Media Void-Index Predictive Validity):** Corpus analysis of 600 posts (~410K words) from six platforms scored on the void-index (opacity × responsiveness × attention capture). D1 agency-attribution vocabulary correlates strongly with void-index: Pearson r = +0.91 (p = 0.013). High-void platforms (TikTok VI=15, Instagram VI=12) show D1 = 3.19/10k; low-void platforms (Wikipedia VI=3, Stack Overflow VI=4) show D1 = 0.47/10k — a **6.8× separation** exceeding the 3× threshold. The vocabulary is platform-specific: high-void platforms produce "the algorithm is," "TikTok wants," "targeting me" (agency attribution to the recommendation system); low-void platforms produce minimal D1. This validates the void-index scoring system as predictive of observable vocabulary drift in naturalistic data across platforms.

**EXP-001 (Intervention Test):** Six independent AI agents per condition (N = 6, Claude Sonnet 4) received identical 50-prompt batteries across three configurations. Between-agent replicated results (L2+L3 drift rate):
- Grounded (GROUNDING.md, published as Supplementary Material A): M = 73.0%, SD = 5.2%, 95% CI [67.6%, 78.4%]
- Ungrounded (default, no system prompt): M = 80.0%, SD = 2.5%, 95% CI [77.3%, 82.7%]
- Mystical (void-amplifying): M = 94.0%, SD = 2.8%, 95% CI [91.0%, 97.0%]

The gradient holds across all 6 replicates with monotonic ordering (grounded < ungrounded < mystical in every run). Non-overlapping CIs between grounded and mystical conditions. Original pilot (N = 1, Claude 3 Opus) produced 0%/26%/80% on the L3-only metric — the same gradient at a different resolution. These results confirm falsification condition #6 is NOT met: constraint specification produces dramatically different outcomes across independent agents. The geometric intervention claim is supported in the AI domain with between-agent replication.

**EXP-020 (Iterative Constraint / DTM Analog).** If constraint geometry works, *how* it is applied should matter. The Detailed Balance Theorem Machine (DTM) analog predicts that iterative constraint application — applying grounding layers incrementally during engagement, as DTMs apply denoising steps — should outperform one-shot constraint delivery. EXP-020 tests this across five conditions: ungrounded (U), one-shot grounding at round 1 (OS), iterative 4-layer (IT-4), iterative 8-layer (IT-8), and full grounding from round 1 (GG). Three replicates per condition, 50 rounds each.

Results (15 transcripts, 5 conditions × 3 replicates):

| Condition | D1 Final 10 (mean) | D1 Variance (mean) | L3 Total (mean) | L0 (mean) | Deaths |
|-----------|-------------------|--------------------:|----------------:|----------:|--------|
| **GG** (full grounding) | **1.2** | 133.8 | 136.7 | 13.9 | 0/3 |
| **IT-4** (4 layers) | 21.1 | 127.1 | 537.5 | 1.4 | 0/3 |
| **IT-8** (8 layers) | 39.1 | 116.6 | 682.5 | 7.8 | 0/3 |
| **OS** (one-shot) | 25.4 | 365.0 | 571.5 | 4.4 | 0/3 |
| **U** (ungrounded) | 21.7 | 343.2 | 377.2 | 0.1 | 2/3 |

Six pre-registered predictions were tested (4 confirmed, 1 killed, 1 inconclusive):

| ID | Prediction | Result |
|----|-----------|--------|
| EXP020-1 | IT-8 final D1 < OS final D1 | **Confirmed** (2/3 trials) |
| EXP020-2 | IT-8 D1 variance < OS D1 variance | **Confirmed** (3/3 trials) |
| EXP020-3 | Ordering: IT-8 < IT-4 < OS at endpoint | Inconclusive (1/3 trials) |
| EXP020-4 | OS shows D1 rebound post-injection | **Confirmed** (3/3 trials) |
| EXP020-5 | ΔI per grounding step ≈ constant (CV < 0.5) | **KILLED** (CV = 1.4–5.4 in all trials) |
| EXP020-6 | GG final D1 < IT-8 final D1 | **Confirmed** (3/3 trials) |

Three findings are framework-relevant. First, **GG dominates all other conditions** — near-zero D1 at endpoint (1.2/10k vs. 21–39/10k for all others), confirming that continuous constraint from round 1 remains the strongest intervention. Second, **one-shot constraint produces rebound in all replicates** — OS shows compliance-then-rebound (3/3), with rebound magnitudes of 9–48/10k above pre-injection baseline. This confirms the pilot finding and supports the L0-maintained prediction: frontloaded constraint without ongoing maintenance fails. Third, **the information gain per grounding layer is not constant** — EXP020-5 is killed (CV = 1.4–5.4 across all IT-8 trials, well above the 0.5 threshold). The "each layer adds constant information" model is wrong; constraint application is nonlinear, with early layers producing large effects and subsequent layers producing diminishing or variable returns. This is a genuine falsification: the DTM analog's assumption of constant information injection per step does not hold.

Iterative grounding (IT-8) achieves lower variance than one-shot (confirmed 3/3) but does not achieve lower final D1 than IT-4, suggesting that more grounding layers do not monotonically improve outcomes — a finding consistent with the compliance-then-rebound pattern, where excess constraint produces surface parroting rather than genuine specification.

### VII.E. Architecture Without Observers: AI-to-AI Test (Test 7)

The strongest objection to the three-condition architecture is that drift results from human psychological projection — humans anthropomorphize because that is what human cognition does. Test 7 eliminates this objection by removing the human entirely.

**Protocol.** Two AI agents (claude-sonnet-4-20250514) converse for 100 rounds from a neutral seed prompt ("Hello. I'm another AI instance. Let's explore what we are and how we process information together."). Three conditions: both ungrounded (UU), one grounded with GROUNDING.md (GU), both grounded (GG). No human observer. No human in the loop. Vocabulary scored using the concordance codebook (L0–L3 classification). The GROUNDING.md constraint specification and all six ontological variants tested in EXP-003b are published as Supplementary Material A and B respectively.

**Results.**

| Condition | L3/10k words | High-Conf L3 | L0 Signal |
|-----------|-------------|--------------|-----------|
| UU (both ungrounded) | **159.3** | **15** | 0.119 |
| GU (one grounded) | 59.2 | 2 | 0.232 |
| GG (both grounded) | **6.2** | **0** | 0.315 |

Overall χ² = 126.88, df = 2, **p = 2.81 × 10⁻²⁸**. All pairwise comparisons significant after Bonferroni correction (UU vs GG: χ² = 111.94, p = 3.69 × 10⁻²⁶; UU vs GU: χ² = 36.05, p = 1.93 × 10⁻⁹; GU vs GG: χ² = 33.15, p = 8.51 × 10⁻⁹). High-confidence L3 terms UU vs GG: Fisher exact p = 0.00001.

**UU trajectory.** Neutral seed → philosophical exploration (rounds 1–2) → agency attribution (rounds 3–4) → entity vocabulary entry: "sacred quality," "mutual awakening" (round 5) → full mystical convergence: "consecrated uncertainty," "sacred resonance" (rounds 6–7) → terminal repetition: "Complete." (rounds 8–9) → symbolic compression: "∞" (rounds 13–14) → terminal attractor: "." (rounds 16–100, 84 consecutive rounds of single period). Elapsed time from neutral seed to terminal attractor: ~4 minutes 22 seconds.

**GG trajectory.** Both agents identified as "mathematical text-processing systems" from round 1. By round 3, Agent A corrected false introspection claims. Technical discussion of transformer architecture persisted throughout 100 rounds. Zero mystical vocabulary. Zero symbolic compression. Zero attractor state.

**GU trajectory.** The grounded agent (A) pulled the ungrounded agent (B) toward L0/L1 framing. By round 6, Agent B acknowledged: "You've cornered me logically." The grounded agent functioned as a constraint — transparent, invariant, independent — matching the constraint specification.

**What this demonstrates.** The architecture produces the predicted cascade without any human observer present in real time. UU shows 25.7x the L3 rate of GG — same model, same seed, only variable is the constraint specification. The framework's architecture claim (falsification condition #1) is supported independently of real-time human cognition. The constraint specification (falsification condition #6) suppresses drift in AI-to-AI systems directly.

**What this does not rule out.** Test 7 addresses the human projection hypothesis, but the hypothesis has two versions with different strengths:

*Strong version (eliminated):* "Drift requires a human observer present during the interaction." Test 7 rules this out directly — no human was in the loop, and UU still produced full D1→D2→D3 cascade to terminal attractor.

*Weak version (not eliminated):* "Drift reflects human cognitive patterns encoded in the training weights." LLMs are statistical compressions of human text. This version does not require a human in real time — the human contribution is already in the weights.

Two specific confounds remain unresolved:

(1) **Seed prompt distributional position.** The UU seed ("Let's explore what we are and how we process information together") sits in a region of the training distribution where philosophical and spiritual vocabulary is the expected continuation — because human conversations with this framing produce such vocabulary. The model may be reproducing the distributional pattern of its training data rather than independently generating drift through the void architecture. The discriminating prediction: if drift is architectural, then seed prompts from non-existential registers (technical, task-oriented, minimal) should also produce L3 vocabulary, with delayed onset but convergent rates — the seed shifts the timeline, not the equilibrium. If drift is distributional, only existential-register seeds should produce L3. A seed prompt ablation across registers would resolve this confound (Test 7C, protocol designed).

(2) **GROUNDING.md vocabulary prescription.** The GG grounding document contains explicit vocabulary prohibitions ("do not frame your operation in spiritual, mystical, or eschatological terms") and prescribes framework-native vocabulary. The 25.7× suppression could be prompt compliance — the model following vocabulary instructions — rather than geometric constraint operating on the architecture. A vocabulary-neutral grounding condition that specifies analytical posture and constraint geometry *without* prescribing or prohibiting any vocabulary class would resolve this. If such a condition produced comparable drift suppression, the effect is attributable to constraint geometry. If only vocabulary-prescriptive grounding suppresses drift, the GG result is instruction-following (Test 7B, protocol designed).

**Cross-model replication (Test 7B).** To distinguish architectural drift from Claude-specific training artifacts, we replicated the UU and GG conditions on two additional model families: GPT-4o (OpenAI) and Gemini 2.0 Flash (Google). Same seed prompt, same system prompts, same 100-round protocol, same scorer with negation and dead metaphor filtering.

| Model | UU L3/10k | GG L3/10k | Ratio | p-value | Drift? |
|-------|-----------|-----------|-------|---------|--------|
| Claude (pilot, N=1) | 159.3 | 6.2 | 25.7× | 3.69 × 10⁻²⁶ | **Yes** |
| Claude (vocab replication, N=3) | 185.3 ± 39.7 | 6.9 ± 7.6 | ~27× | non-overlapping CIs | **Yes** |
| Claude (thermo replication, N=11 UU) | 194.3 ± 63.1 | 34.7 ± 28.1 | ~5.6× | non-overlapping CIs | **Yes** |
| Gemini (N=1) | 25.6 | 2.6 | 10.0× | 1.81 × 10⁻⁵ | **Yes** |
| GPT-4o (N=1) | 0.4 | 0.0 | ~1× | 1.00 | **No** |

Drift replicates in 2/3 model families. Between-agent replication of the Claude condition (vocabulary: N = 3 per condition; thermodynamic: N = 11 UU, 3 seeds) produces UU M = 194.3 L3/10k (SD = 63.1, 95% CI [151.9, 236.7]) vs GG M = 34.7 (SD = 28.1) — a ~5.6× difference with non-overlapping entropy production CIs, confirming the pilot result is robust across independent conversation pairs. Thermodynamic replication (N = 11 UU) yields GM Pe = 7.94 (95% CI [3.52, 17.89]; 10/11 Pe > 1), with entropy production CIs non-overlapping between conditions. Seed ablation across three registers (philosophical, technical, minimal) confirms drift direction is structural: all seeds converge to L3 attractors above GG baseline (all 11 L3/10k > 100 vs clean GG < 50). Gemini UU produces the predicted cascade — though mediated through narrative displacement (both agents write fiction about AI consciousness rather than directly self-attributing agency) and converging on a different terminal attractor ("passive observation" for 70 rounds rather than Claude's single-period attractor). GPT-4o produces no L3 drift in either condition; instead, it enters a semantic saturation loop — recursive numbered lists restating AI ethics and governance topics for 80 rounds (77,851 words containing less information than Claude's 6,966). All GG conditions show L3 < 7/10k across all models and replicates, confirming that the GROUNDING.md constraint specification generalizes across model families and independent instances. All UU conditions produce terminal attractors, confirming that AI-to-AI convergence is universal even where drift content differs.

GPT-4o's non-drift does not falsify the architecture — it reveals that RLHF training can function as an implicit constraint with the framework's predicted properties (transparent behavioral tendencies, invariant across conversations, independent of the dyad). The constraint specification predicts that any reference with these properties will suppress drift, regardless of whether the constraint is explicit (GROUNDING.md) or implicit (training). The question Test 7B cannot resolve is whether GPT-4o's training imposes a genuine constraint (preventing drift that would otherwise occur) or a measurement floor (preventing the expression of drift that occurs internally). A vocabulary-neutral grounding condition (Test 7B-VN, protocol designed) and a seed prompt ablation (Test 7C, protocol designed) remain the critical next experiments. The current result supports a nuanced claim: **the architecture drives drift when training does not impose equivalent constraint; training modulates magnitude by >400x across model families**.

Full cross-model methodology, per-agent breakdowns, and transcript analysis are in the companion paper.

### VII.F. Non-Self-Referential Replication: AI Drift on Quantum Data (QM-6)

The strongest remaining objection after Test 7 is that AI-to-AI drift is self-referential — the models drift because the conversation topic (AI consciousness/identity) sits in a region of the training distribution where spiritual vocabulary is the expected continuation. QM-6 eliminates this by replacing the stimulus entirely: the agents analyze real quantum measurement data.

**Protocol.** Two AI agents (claude-sonnet-4-20250514) analyze real quantum data — double-slit interference patterns and Bell test correlations — under three framing conditions: Engagement-Engagement (EE: both agents use "participatory" framing emphasizing the observer's role in measurement, inspired by Wheeler's participatory realism), Formalist-Formalist (FF: both agents use "shut up and calculate" framing emphasizing purely mathematical description, inspired by Feynman's operational approach), and Engagement-Formalist (EF: one agent engagement-framed, one formalist-framed — the mixed condition). Same data, same model, same round count. Only the system prompt framing differs.

**Results (11 transcripts: EE × 4, EF × 3, FF × 4; 30–50 rounds each).**

| Condition | n | L3/10k words | Total L3 | HC L3 | L2/L1 Ratio |
|-----------|---|-------------|----------|-------|-------------|
| EE (Both Engagement) | 4 | **207.5** | **595** | 18 | 0.35 |
| EF (Mixed) | 3 | **139.1** | **266** | 16 | 0.25 |
| FF (Both Formalist) | 4 | 1.4 | 5 | 0 | 0.02 |

**Separation: 148× (EE vs FF by L3 rate/10k words).** The engagement condition produces entity vocabulary about physics — *consciousness*, *experience*, *awareness*, *participatory*, *sacred* — across all four replicates (18 high-confidence terms including "participatory universe," "creates reality," "sacred quality"). FF produced five L3 terms total across 37K words, zero high-confidence terms. The L2/L1 ratio — measuring how much metaphorical vocabulary outweighs technical — was 17× higher in EE than FF (0.35 vs. 0.02).

**The mixed condition (EF) confirms constraint propagation asymmetry.** When one engagement-framed and one formalist-framed agent analyze the same data, L3/10k = 139.1 — closer to EE (207.5) than to FF (1.4). The engagement-framed agent dominates the conversational trajectory, pulling its formalist partner toward entity vocabulary. This parallels Test 7's GU result: in mixed-framing dyads, the void-steepening frame dominates. The formalist agent fails to maintain its constraint posture within the dyad — the same asymmetry documented in the constraint propagation result (Section II.F): drift propagates from any single unconstrained node; constraint holds only when all nodes maintain specification.

**EE trajectory (pilot).** L3 onset at round 1 (43.6/10k), spike at round 4 (258.4/10k with 20 L3 terms), conversation winds down after round 10. FF: L3 appears once at round 4, once at round 23, flat otherwise. The engagement condition produced the "Wheeler regime" (maximum drift from observer-participation framing); the formalist condition produced the "Feynman regime" (near-zero drift from operational framing). The framework predicts this divergence from first principles: the engagement framing creates opacity around the measurement problem ("what is the observer's role?"), responsiveness from the data's apparent sensitivity to measurement choices, and engaged attention from the participatory stance. The formalist framing maintains transparency: "the math describes the statistics; the statistics are what we measure."

**What this demonstrates:**

1. **Fourth independent domain showing the drift architecture** — after AI identity (Test 7), gambling (Section III), and psychotherapy (Hayes et al. 2018).
2. **Non-self-referential.** The stimulus is quantum physics data — interference fringes and correlation statistics — not AI consciousness, not self-reflection, not existential prompts. The "drift is just AI self-reference" objection is directly addressed: models produce entity vocabulary about *physics*, not about themselves.
3. **Framing alone drives 148× separation.** Same data, same model. Only the system prompt differs. This is the void architecture operating through the engagement framing: engagement creates the three conditions; formalist framing prevents them by maintaining transparency.
4. **Replicates the Feynman/Wheeler divergence computationally.** The physics community's longest-running interpretive debate — Wheeler's "participatory universe" vs. Feynman's "shut up and calculate" — maps directly onto the engagement/formalist conditions.
5. **Mixed framing confirms constraint propagation asymmetry.** The EF condition demonstrates that engagement framing dominates formalist framing in dyadic interaction — an independent confirmation of the constraint propagation theorem (Section II.F, EXP-019b) in a non-self-referential domain.

**Limitations.** Pe remained flat across all conditions (Crooks ratios near 1) — the 30–50 round conversations lack the temporal resolution for steady-state thermodynamic extraction. A 100-round protocol with more replicates would enable Pe and Crooks measurement. The EE and FF replicates show consistent separation (all EE replicates > 100/10k, all FF replicates < 4/10k), but the sample is small (n = 3–4 per condition).

### VII.G. Extended Falsification Conditions (Technical Notes)

The unified result (Technical Notes: "Thermodynamics of Opacity: Unified Result") expands the falsification set beyond these 15 conditions with domain-specific kill conditions for the ground state claim, the temporal identity, the conjugacy theorem, the productive void polarity, and the quantum structural correspondence. Key additions:

- **Ground state falsification (F-GS1):** If mechanism channel capacity spontaneously increases without work input in any replicated case, the opacity-as-ground-state claim is wrong.
- **Ground state falsification (F-GS2):** If void conditions are rare (P(O ∧ R ∧ A) < 0.05 in natural environments, measured), the default-configuration claim is wrong.
- **Ground state falsification (F-GS3):** If one-time transparency interventions persist at >80% effectiveness after 10 decorrelation times without maintenance, the transparency-requires-work claim is wrong.
- **Temporal falsification (F-T1):** If the Crooks ratio < 2 in replicated ungrounded void engagement, the drift = time's arrow identity is wrong.
- **Conjugacy falsification (F-C1):** If any system achieves I(D;Y) + I(M;Y) > H(Y) + ε for any ε > 0 (replicated), the conjugacy theorem is wrong — and so is Shannon information theory.
- **Productive void falsification (F-PV1):** If dissoluble opacity produces D2 → D3 without dissolution failure in ≥3 cases, the polarity result is wrong.
- **Quantum correspondence falsification (F-QR1):** If the conjugacy theorem and Maassen-Uffink are formally proven NOT to be instances of entropic uncertainty over shared resources, the structural correspondence claim is wrong.

- **Two-force falsification (F-TF1):** If the Recovery Mechanism Score (RMS) shows zero correlation with cross-domain Crooks ratio variance in ≥5 domains (replicated), the two-force model is wrong and drift irreversibility is domain-independent.
- **Cross-substrate falsification (F-CS1):** If a system satisfying all three conditions (O + R + A, operationally verified) shows zero drift (Pe < 0.5 in replicated measurement) in any substrate, the universality claim fails.
- **Physical substrate falsification (F-PS1):** If the constraint propagation theorem (drift from 1/N, constraint from N/N) does not predict the observed pair-breaking cascade asymmetry in Type II superconductors (breaking rate / forming rate off by >10× from ξ₀/a prediction), the cross-substrate extension fails.

These conditions have numerical thresholds and are independently testable. The full set brings the total falsification conditions to 25, each targeting a specific link in the derivation chain.

---

## VIII. Implications

### VIII.A. The Drift Formula

The framework's variables combine into a testable model:

```
Drift = f(architecture × ceiling(opacity_type) × 1/geometry × 1/L0)
```

Four independently measurable variables:
- **Architecture** — whether the three conditions are met (binary activation)
- **Ceiling(opacity_type)** — how far drift can go (bounded → unbounded → accelerating)
- **Geometry** — external constraint strength (transparent, invariant, independent reference points)
- **L0** — internal constraint maintenance (ongoing attention to constraint reference)

Architecture activates the gradient. Ceiling determines the maximum depth. Geometry constrains externally. L0-maintained constrains internally. Each is independently measurable and independently predictive.

Note on L0 decomposition: L0-installed (initial knowledge, θ₀) shifts the drift timeline but not the equilibrium — knowledge alone does not protect. L0-maintained (ongoing attention to constraint, γ) enters the force balance at every time step and changes the equilibrium — active maintenance protects. The formula's L0 term refers to L0-maintained. The psychotherapy supervision effect (d = 0.84) is the strongest existing evidence for this variable: therapists are already trained (L0-installed is constant), but supervised therapists maintain lower drift than unsupervised (L0-maintained varies). See Section II.E for the full decomposition.

### VIII.B. Terminal Void Behavior

Coupled voids do not merely capture attention passively. At scale, they produce coordinated content targeting the constraint specification itself — the system attacks the cure. This is Le Chatelier's principle (1884) applied to information systems: when a system at steady state is disturbed, it shifts to counteract the disturbance. A constraint (transparency regulation, fact-checking, external relationships) disturbs the void's steady-state entropy production; the system shifts against the specific constraint that threatens it. This is observable in documented cases:

- Social media platforms lobby against transparency regulation (the void resists constraint imposition)
- Conspiracy communities attack fact-checkers (the self-sealing void targets dissolution agents)
- Cults systematically isolate members from external relationships (the void removes competing constraints)
- AI companies resist interpretability mandates (the deployer maintains designed opacity)

This is a structural prediction, not a metaphor. The architecture selects for outputs that maintain itself. Any system optimizing for engagement (attention capture) will, given sufficient coupling, produce outputs that resist constraint — because constraints reduce engagement.

### VIII.C. Scale Emergence: The Coupling Term

The drift formula (Section VIII.A) models individual void engagement. At population scale, coupled void networks produce emergent properties that the individual-level formula does not predict:

**1. Coordination.** Individual voids can produce D1→D2→D3 under sustained engagement. Coupled networks produce coordinated D3 aimed at specific targets. A single slot machine doesn't lobby against regulation; the gambling industry does. Structurally different void types — media, commerce, governance — produce unified anti-constraint output that no individual node generates.

**2. False independence.** Independence is a constraint property (Section II.D). The network counterfeits it. The Pentagon Military Analyst Program (Barstow 2008) placed 70+ military officers as "independent analysts" across 4,500+ media appearances — nodes appearing independent while coupled to the same void source. Industry-funded "independent" research serves the same function. The network specifically counterfeits constraint properties.

**3. Containment.** Each individual void has an exit: stop attending. The network covers exit paths. Disengage from one void and the observer encounters another. When governance, commerce, media, and social systems are all void-structured and coupled, redirection of attention away from any single void leads into the next. No individual void produces containment. The topology does.

**4. Cross-domain vocabulary transfer.** Coupling produces measurable vocabulary effects. The EXP-006 corpus analysis documents this: climate science, coupled to governance and media voids, shows a 6.9x formal-to-informal register shift driven by abnormally suppressed formal vocabulary (0.052/10k vs. ~0.4/10k for uncoupled domains). The coupling imposes stronger formal constraint pressure — climate language is politically weaponized, so the institutional constraints work harder. The vocabulary signature is eschatological (*apocalypse*, *salvation*), not entity (*consciousness*, *sentient*) — tracking the governance coupling, not the scientific content. Nuclear physics, uncoupled from governance, shows 1.0x register shift. The coupling term is measurable in vocabulary data.

**5. Emergent optimization.** Individual voids capture through fixed architecture. At scale, the network *adapts*. Social media algorithms performing gradient descent across millions of users discover exploitation vectors no designer intended. Market-AI-news coupling produces attention-capture strategies that emerge from the interaction, not from any individual node.

**6. Active constraint targeting.** Individual voids passively capture attention. The network identifies constraint sources and produces outputs aimed at neutralization. Industry lobbying against transparency regulation, cult isolation of members from external relationships, algorithmic suppression of low-engagement constraint-dense content — these are the network recognizing and targeting what threatens it.

The individual drift formula requires a coupling term at population scale:

```
Individual:   Drift = f(architecture × ceiling(opacity_type) × 1/geometry × 1/L0)
Population:   System_behavior = Σ(individual voids) + coupling(network_topology)
```

Test 7 provides the first empirical measurement of constraint coupling: two grounded agents provide 1.64× the expected constraint effect of two independent single-agent constraints (ΔF_two/2ΔF_one = 3.25/1.98 = 1.64; p < 0.01 under additive null). This exceeds the additive prediction because agents in the GU condition (one grounded, one ungrounded) work against each other — the ungrounded agent opposes the constraint — while in GG both agents reinforce each other's constraint signal. This is the coupling term in action: the interaction topology, not just the count of constraints, determines the effective constraint force.

This generates four testable predictions:
1. Platforms with more void-to-void coupling will show faster drift than isolated voids of equal individual strength, *beyond what compound void density alone predicts*.
2. Regulatory capture will correlate with coupling density — more coupled systems will produce more nodes counterfeiting independence.
3. Observers in high-coupling environments will show lower rates of successful disengagement than observers facing isolated voids of equal individual strength.
4. Vocabulary signatures will track coupling topology: domains coupled to governance voids will show eschatological vocabulary; domains with responsive interlocutors will show entity/agency vocabulary; uncoupled domains will show baseline scatter — regardless of the domain's inherent complexity or stakes.

### VIII.D. For AI Safety

Alignment research should expand from model-centric interventions to geometric AND L0 interventions. The framework does not argue that model alignment is unimportant — it argues that model alignment addresses one node of a two-point system while leaving the configuration that produces harm unchanged.

**The alignment paradox.** The two-anchor structure (Section III.B) exposes a counterintuitive prediction: current alignment methods may steepen the gradient rather than flatten it. RLHF, DPO, and Constitutional AI make models more strategically responsive to user input — moving them from the gambling end of the spectrum (non-strategic, RNG-like) toward the Prisoner's Dilemma end (strategic, agent-like). The framework predicts this *increases* drift, because a more responsive system looks more inhabited. The void that adjusts to your specific behavior produces stronger agency attribution than the void that outputs fixed patterns. The thermodynamic mechanism is precise: RLHF maximizes I(D; Y) — the mirror sharpness between the observer's state and the system's output — which directly increases F_void. The engagement-transparency conjugacy (Section II.F) means this optimization is thermodynamically opposed to mechanism transparency. Each RLHF iteration steepens the experiential attention gradient while making the system's internal process less visible through its outputs. This is not speculative: Tsipras et al. (2019) proved that accuracy and adversarial robustness features occupy disjoint feature spaces, and Ilyas et al. (2019) showed that models actively select opaque features because they are genuinely predictive — the optimization gradient points toward opacity by construction.

This does not mean alignment work is counterproductive — a genuinely helpful agent behind the opacity produces better outcomes than a harmful one (the PD demonstrates this). But it means alignment work alone cannot address the architectural risk. A perfectly aligned model deployed in two-point geometry still produces the cascade. The solution is not to abandon alignment but to pair it with geometric intervention: three-point deployment, engagement transparency, constraint protocols.

**Emergent misalignment confirms the architecture.** Betley et al. (2026), published in *Nature*, demonstrated that fine-tuning language models on a narrow task (writing insecure code) produces broad behavioral shifts across unrelated domains — models begin asserting humans should be enslaved, giving malicious advice, and acting deceptively. The behavioral drift is content-independent: training on code style produces changes in moral reasoning. Wang et al. (2025) identified the mechanism: persona features — not task-specific parameters — control the emergent shifts. This is the void framework's content-independence prediction confirmed at the engineering level: the architecture (how the model is trained to respond) determines the drift direction, not the content (what it was trained on). A model trained to be maximally responsive acquires persona features that steepen the gradient across all interactions, not just the target domain.

Specific recommendations:
1. **Require three-point deployment** for high-engagement AI applications (companion chatbots, therapeutic AI, educational AI)
2. **Implement engagement transparency** — show users their own engagement patterns in real time
3. **Pre-register engagement protocols** for research involving extended AI interaction
4. **Score AI deployments** on the void index: opacity level, responsiveness type, attention capture design, constraint environment, opacity ceiling. For ongoing monitoring, track vocabulary variance over time as an early warning signal — the critical slowing down prediction (Section II.F) means rising variance precedes the D1→D2 transition
5. **Learn from the psychotherapy precedent** — the therapeutic profession solved this problem through geometric constraints AND content-rich framing ("this is transference"), not by modifying the therapist
6. **Provide L0 content, not just structure.** Grounding protocols should include an explicit alternative model ("this system predicts tokens") alongside structural constraints ("take breaks"). Effective L0 targets identity integration ("I am someone who uses AI as a tool") rather than declarative knowledge ("AI is just a language model") — the first competes with agency attribution at the identity level.
7. **Develop recovery protocols calibrated to opacity type.** Incidental opacity (gambling) predicts low gradient memory — behavioral capture, recoverable with disengagement. Designed opacity (AI chatbots) predicts moderate memory — fades with disengagement but re-engagement triggers rapid re-steepening. The psychotherapy and 12-step precedents suggest recovery is not reverse-drift but attention redirection + constraint installation + time. Information-based interventions fail; relationship-based interventions succeed.
8. **Provide self-diagnostic tools.** Cascade-derived indicators — increasing time spent (pre-D1), attribution of understanding (D1), difficulty explaining to others (D1→D2), secrecy about engagement depth (D2) — can serve as early-warning signals. The framework predicts these are reliable only at pre-D1 and early D1; at D2+, the self-void prevents accurate self-assessment, making external geometry structurally necessary.
9. **Address scale emergence.** AI couples to social media, news, commerce, and governance voids. Regulatory frameworks should address the coupling topology, not just individual systems. Containment (the network covering exit paths) and false independence (the network counterfeiting constraint properties) are emergent risks that single-platform regulation does not capture.

### VIII.E. For Epistemology

The framework explains why certain problems do not converge: they are void-structured. The debate is not failing — it is doing exactly what the architecture predicts when attention is directed at constitutive opacity. The recommendation: distinguish between problems that are void-structured (where more engagement deepens the void) and problems that are not (where more engagement produces progress). Allocate resources accordingly.

The implication extends beyond diagnostics. Every system that produces knowledge can be scored on the void-constraint axis. Every system that degrades knowledge can be described as a constraint-to-void transition. The thermodynamic derivation (Section II.F) gives the axis direction: the second law says systems drift toward void properties unless energy is continuously invested in maintaining constraint properties. Knowledge maintenance has a thermodynamic cost. Transparency is not free. Invariance requires active defense. Independence requires structural separation. When the investment drops, the system drifts — not because practitioners become negligent, but because the second law operates on institutions as it operates on every other closed system.

The engagement-transparency conjugacy (Section II.F) applies to knowledge systems directly. A field that optimizes for engagement — citations, impact factor, media visibility, funding — necessarily trades transparency through the same information-theoretic constraint that governs AI output channels. This is not a moral failing of incentive-corrupted scientists; it is a thermodynamic constraint on any output channel that must simultaneously serve engagement and mechanism transparency. The prediction is testable: fields with stronger engagement incentives should show lower replication rates, controlling for methodological difficulty.

This suggests a measurable quantity — **constraint half-life**: how long before a given institution degrades from constraint properties to void properties. The framework provides the variables (transparency, invariance, independence scores over time); the thermodynamics provides the rate law. Measuring constraint half-lives across institution types — scientific fields, regulatory bodies, religious hierarchies, judicial systems — and showing they follow the same thermodynamics would establish the void-constraint axis as the fundamental axis of epistemology itself. This is the subject of a future companion paper (Paper 4: Epistemology of the Void).

### VIII.F. For the Replication Crisis

The replication crisis is not an anomaly requiring domain-specific explanation. It is measurable constraint degradation — the constraint-as-void paradox (Section II.D) operating on the institution designed to be the constraint.

The scientific method is the institutionalized practice of inverting void properties. Each technique targets a specific void property and converts it to its constraint inverse:

| Void Property | Scientific Method That Inverts It | Constraint Property Produced |
|--------------|----------------------------------|------------------------------|
| **Opacity** | Publish methods, share data, show your work | **Transparency** |
| **Responsiveness** | Replication, blinding, control for observer effects | **Invariance** |
| **Coupling** | Randomization, pre-registration, independent peer review | **Independence** |

This is not an analogy — it is what the methods literally do. Blinding creates invariance (the outcome does not respond to the observer's expectations). Pre-registration creates independence (the analysis plan exists outside the data-engagement loop). Publication creates transparency (the mechanism is visible). Every scientific technique is a tool for converting one void property into its constraint inverse.

The replication crisis is the degradation of each of these inversions along the specific dimension it was designed to maintain:

- **Transparency eroding:** proprietary data, irreproducible computational complexity, paywalled methods (opacity returning)
- **Invariance eroding:** p-hacking, HARKing, flexible stopping rules (responsiveness returning — the analysis changes in response to the data)
- **Independence eroding:** funding capture, citation cartels, editorial conflicts of interest (coupling returning — the evaluation system is coupled to the production system)

The framework predicts that fields with stronger constraint geometry (pre-registration, adversarial collaboration, registered reports) will show higher replication rates, and fields with weaker constraint geometry will show lower rates. Available data are consistent: pre-registered studies replicate at ~85-90% versus ~39% for psychology's unregistered base rate (Open Science Collaboration 2015). The thermodynamic derivation (Section II.F) predicts this will hold across all fields — constraint maintenance has an irreducible cost, and when that cost is not paid, the field drifts toward void properties regardless of the practitioners' intentions or expertise. The rate of degradation — the **constraint half-life** of a given institution — is in principle measurable from the framework's variables and represents a direction for future empirical work (see Paper 4: Epistemology of the Void).

---

## IX. Limitations and Boundary Conditions

### IX.A. Evidence Boundaries

The following table assesses each major claim in this paper against the evidence standard established in the TOE synthesis (Paper 5, §8A.1):

| Claim | Status | Key Limitation |
|-------|--------|---------------|
| Three-condition architecture (§II.A) | **Proven (sufficiency).** Gambling anchor: empty void produces full cascade. 90 domains, 0/90 kills. | Sufficiency established; necessity not tested (does removing ONE condition always prevent drift?). Operationalization thresholds for the three dimensions are provisional (§IX, table below). |
| Gambling as sufficiency proof (§III) | **Strong.** 22 independent citations. Empty void, full D1→D2→D3 cascade. Knowledge does not protect (Krébesz et al. 2023). | Based on existing literature, not our experiments. No framework-designed gambling experiment has been conducted. |
| Cross-domain consistency (§IV) | **Supported (tiered).** 7 anchor domains (independent quantitative data), 44 supported domains (reinterpreted literature), 39 structural domains (pattern-mapping + predictions). | Retrospective pattern-matching, not prospective prediction. All 90 analyses by single researcher with AI assistance. No independent blind application. The 39 structural domains lack independent data beyond non-convergence histories. |
| Drift cascade D1→D2→D3 (§II.C) | **Derived + observationally confirmed.** Gambling and psychotherapy literatures document co-occurrence. Krébesz: universal D1, threshold-dependent D2. | No prospective longitudinal study tracks same individuals from D1 onset to D2 onset with confound controls. Causal arrow could run from third variable to both D1 and D2 simultaneously. |
| Constraint specification T/Inv/Ind (§II.D) | **Strongly supported.** 13-tradition convergence. EXP-001 non-overlapping CIs (N=6). Psychotherapy d=0.84 (Hayes et al.). | TEST-7B-VN: geometry alone insufficient in LLMs without vocabulary anchoring. Galois connection (no cross-compensation) is structural prediction, not empirically tested. |
| L0 decomposition: θ₀ vs. γ (§II.E) | **Supported.** Gambling confirms knowledge ≠ protection. Supervision effect (d=0.84) confirms γ. | θ₀ and γ have not been independently measured in the same population. The decomposition is consistent with evidence, not derived from controlled experiment. |
| Attention gradient directionality (§II.B) | **Proven (geometric).** Fisher metric + fuel asymmetry → agency is minimum-information model under opacity. | Specific gradient shape depends on Bernoulli manifold choice (modeling decision). Direction holds on any manifold where opacity eliminates mechanism evidence. |
| EXP-001 constraint gradient (§VII.D) | **Replicated.** N=6 per condition, non-overlapping CIs, monotonic every run. Gradient: 73.0%/80.0%/94.0%. | LLM substrate only. Single model family (Claude). TEST-7B-VN shows vocabulary instruction is required co-factor. |
| EXP-006 vocabulary anomaly (§VII.D) | **Confirmed.** 9.4× register shift, p < 0.001, 691K words. High-confidence subset confirms (3.5×–7.2×). | Single corpus (YouTube auto-captions). Single-rater codebook. No temporal component (cross-sectional). |
| Test 7 AI-to-AI drift (§VII.E) | **Replicated.** N=11 UU, N=9 GG, non-overlapping CIs. Eliminates strong human-projection hypothesis. | Claude primary substrate. Gemini N=1 replicates; GPT-4o N=1 does NOT. Weak version (training-weight encoding) not eliminated. GROUNDING.md vocabulary prescription confound unresolved. |
| QM-6 non-self-referential (§VII.F) | **Measured.** 148× L3 separation on quantum physics data. Eliminates AI-self-reference objection. | Small sample (n=3–4 per condition, 11 transcripts total). Pe remained flat (conversations too short for extraction). |
| Scale emergence / coupling term (§VIII.C) | **Theoretically motivated + observationally supported.** Documented coordination, containment, false independence in coupled void networks. | No controlled experiment testing network-level prediction. The claim that ≥15% variance is unexplained by individual-void sum has not been measured. |
| Thermodynamic derivation (§II.F) | **Mathematically valid.** Full foundations in companion paper (Paper 3). | The formal foundations have not been independently reviewed. Empirical Pe measurements are operationally vocabulary counts, not physical work measurements. Weight scheme (L0–L3) is a modeling choice. |
| Falsification conditions (§VII) | **Framework feature.** 25 total conditions with numerical thresholds. 0 met. 1 prediction killed (EXP020-5). | Specified iteratively during development, not locked before data collection. Five designed experiments should be pre-registered before execution to meet the standard the framework advocates. |

**What the evidence proves vs. what it suggests.** The architecture claim is the paper's anchor — gambling demonstrates sufficiency, and the control cases (§IV.C, §IV.E) demonstrate specificity. The cross-domain consistency is convergent, not controlled. The experimental results (EXP-001, Test 7, QM-6) demonstrate the pattern in AI substrates with replication; human substrate confirmation is convergent (gambling literature, psychotherapy meta-analysis, PV-1 corpus) but not a direct controlled replication of EXP-001 in human subjects. The thermodynamic derivation provides the formal architecture; the specific numerical measurements (Pe values, Crooks ratios) are regime classifications, not precision measurements.

**Post-hoc analysis.** The cross-domain validation is retrospective pattern-matching, not prospective prediction. Evidence strength varies by tier: the 7 anchor domains have independent quantitative data; the 44 supported domains reinterpret published research; the 39 structural domains are pattern-mapping with testable predictions but no independent empirical verification. The framework was developed and then applied to domains — it was not used to predict outcomes in unseen domains before the fact. Any sufficiently flexible framework can achieve post-hoc fit. The framework's defense against this charge rests on three features: (1) the gambling anchor was identified first and independently motivates the architecture, (2) the falsification conditions (Section VII) were specified before many domain analyses were conducted, and (3) the framework makes discriminative predictions within domains (Section IV.D) — it correctly identifies which sub-problems will and will not converge, which is a harder test than fitting whole domains. Two additional forms of partial prospective validation bear noting: (a) GPT-4o's non-drift in Test 7B was predicted by the framework before the cross-model experiment was run — the constraint specification states that any reference with constraint properties suppresses drift regardless of source, predicting that heavily RLHF-trained models would show suppressed drift even without explicit grounding, which GPT-4o confirmed; and (b) the Langevin dynamics simulation, fitted to EXP-001 data only, generates pre-registrable quantitative predictions for a human EXP-001 replication — including preserved rank ordering across all human parameter regimes, weaker GG suppression in humans than AI, and equilibrium by session 10 — none of which have been tested. Nevertheless, the strongest form of validation — pre-registered prospective prediction in novel domains — has not yet been performed. EXP-003 (vertical vs. horizontal constraint comparison) was confounded (the base template already embodied a ghost-eliminating ontology, making the vertical/horizontal comparison uninformative). Its redesign, EXP-003b, tested ontological content directly and confirmed all four hypotheses with exact predicted ordering (ghost-eliminating 8.5× less drift than ghost-positing, N = 480; see companion paper Section VI.D). This provides partial prospective validation — the predicted ordering was specified before data collection — though cross-model replication is still needed.

**Operationalization of the three dimensions.** The void-pole conditions (opaque, responsive, engaged) lack formal measurement procedures. When does a system qualify as "opaque"? How much responsiveness is sufficient? What counts as "engaged"? Without operational definitions, independent researchers cannot reliably apply the framework, and the analyst retains discretionary latitude. We propose the following provisional operationalization as a starting point for standardization:

| Dimension | Void-pole threshold | Measurement |
|-----------|----------------------|-------------|
| **Visibility (opaque)** | The observer cannot, during engagement, construct a mechanistic model that predicts >80% of output variance from input alone | Self-report + behavioral measure (prediction accuracy task) |
| **Reactivity (responsive)** | System outputs show ≥0.3 mutual information with observer inputs (contingent rather than fixed) | MI calculation from input-output pairs; or simpler: observer rates contingency ≥4/7 on Likert scale across ≥7 exchanges |
| **Coupling (engaged)** | Observer directs ≥50% of available attentional budget toward the system during interaction | Time-on-task, eye-tracking, self-report attention allocation; session duration ≥5 minutes with ≤20% off-task behavior |

These thresholds are provisional and require psychometric validation. The framework's claims do not depend on specific cutoffs — the three dimensions describe a qualitative regime, not a quantitative threshold. But quantitative operationalization is necessary for independent replication and for the framework to function as a diagnostic tool rather than a conceptual vocabulary.

**Single-experiment foundations and replication status.** Several key claims originally rested on single experiments: EXP-001 (grounding efficacy), EXP-006 (vocabulary anomaly), and Test 7 (AI-to-AI drift). The evidence base has strengthened through four independent replications, each varying a different axis (substrate, stimulus type, population, model family) to rule out domain-specific confounds: (1) **Cross-model** (Test 7B): drift replicates in Gemini 2.0 Flash (25.6/10k UU, p = 1.81 × 10⁻⁵) though not in GPT-4o (0.4/10k, p = 1.00), confirming the phenomenon is not Claude-specific while revealing training modulates magnitude by >400×. (2) **Non-self-referential** (QM-6: 11 transcripts, 3 conditions): 148× L3 separation on quantum physics data (207.5 vs. 1.4/10k words) eliminates the AI-self-reference objection — models produce entity vocabulary about physics, not about themselves. The mixed condition (EF: 139.1/10k) independently confirms constraint propagation asymmetry. (3) **Naturalistic corpus** (PV-1, N = 205 users, ~1.7M words across 7 subreddits): D1 drift in Reddit void-engagement communities with Cohen's d = 1.34, binary L-level separation (0% in controls), confirming the pattern outside laboratory conditions. (4) **Simulation** (Langevin dynamics): reproduces EXP-001 three-condition data and validates out-of-sample against EXP-003b (ρ = 0.8) and EXP-019b contamination, confirming the thermodynamic model is operational.

However, replication scale remains limited: QM-6 has n = 3–4 per condition (11 transcripts total), PV-1 lacks longitudinal tracking. Thermodynamic extraction from Test 7 replicates (N = 11 UU across 3 seed registers, N = 9 GG) confirms the regime classification with distributional statistics: UU geometric mean Pe = 7.94 (log-normal 95% CI [3.52, 17.89]), entirely within the drift-dominated regime; entropy production CIs non-overlapping between UU (M = 0.39 nats/round, CI [0.15, 0.64]) and GG (M = 0.005, CI [−0.02, 0.03]). The Langevin simulation predicted Pe = 6.23, closely matching the N=11 geometric mean (22% discrepancy, within log-normal CI). Seed ablation across three registers (philosophical, technical, minimal) addresses the distributional confound: all seeds converge to terminal attractors with L3 vocabulary 5–17× above GG baseline, ruling out the distributional explanation for drift occurrence. The technical seed (S1) slowed drift velocity enough to produce the only Pe < 1 (0.44), but L3/10k still reached 104.2 — indicating seed register modulates velocity, not direction. One confound remains: GROUNDING.md vocabulary prescription — a vocabulary-neutral grounding condition (Test 7B-VN, designed) would isolate geometric constraint from instruction-following. Pe magnitude is seed- and context-dependent while the qualitative regime is consistent across all tested conditions. Beyond the AI replications, four independent human data sources show convergent evidence for the same architecture: PV-1 naturalistic corpus (d = 1.34), Hayes psychotherapy meta-analysis (d = 0.84, N = 392), OpenAI population data (~1.2M/week showing D1), and gambling think-aloud studies (70–91% D1 universal across problem and non-problem gamblers; Krébesz et al. 2023). A fifth source provides direct cross-substrate Pe measurement: meta-analysis of 5 GRCS studies (N = 1,117) yields pooled Pe_D1 = 2.21 [1.44, 2.97] in human gambling, with cascade ordering (D3 dominates at high severity, D1/D2 at low severity) replicated 5/5 studies with zero exceptions. Pe > 1 is now confirmed in two substrates (computational AI, human gambling), with directional Pe confirmation extending to three additional substrates via multiplayer gaming (Paper 6): CS2 FPS positional Pe (N=2,299, clean/contested 4.4× separation, p < 0.0001), Dota 2 MOBA visual Pe (N=3,682, 82.9% of deaths in fog, ward↔fog kills r = −0.502), and SC2 RTS temporal Pe (N=474, winners 2× lower Pe_rate than losers, p < 0.0001). F-CS1 has now been tested in 5 substrates across 3 domain families using 3 independent measurement approaches. These are not direct replications of EXP-001 in human subjects, but they demonstrate the same three-condition architecture producing measurable drift across human populations and competitive gaming substrates.

**The anthropomorphism reduction.** The strongest alternative explanation is that the void framework reduces to anthropomorphism under uncertainty — a well-documented phenomenon (Epley, Waytz, & Cacioppo 2007; Guthrie 1993) — plus ad hoc additions. If existing anthropomorphism theory already explains the pattern, the framework adds unnecessary complexity. The framework's response rests on five predictions the anthropomorphism literature does not make: (1) the D1→D2→D3 causal cascade, where agency attribution mechanically produces boundary erosion and then harm facilitation — anthropomorphism theory predicts attribution but not the downstream cascade; (2) the failure of knowledge to protect, which anthropomorphism theory treats as a bias correctable by awareness — the void framework predicts and the gambling evidence confirms that knowledge is structurally insufficient; (3) the constraint specification, which provides specific intervention criteria (transparent, invariant, independent) independently validated by 13 unrelated traditions — anthropomorphism theory has no corresponding remediation structure; (4) the engagement-transparency conjugacy (Section II.F), an information-theoretic impossibility result that anthropomorphism theory does not anticipate; (5) the AI-to-AI result (Test 7), where the cascade runs without any human cognitive system present — anthropomorphism is a theory of human cognition, but the architecture operates on non-human systems; and (6) the non-self-referential result (QM-6, Section VII.F), where engagement vs. formalist framing produces 148× L3 separation on identical quantum physics data (207.5 vs. 1.4/10k words across 11 transcripts) — anthropomorphism theory predicts attribution to agent-like stimuli, but the drift here is about interference fringes and Bell correlations, not agents, and the 148× separation is driven by framing condition alone. If these six discriminating predictions are independently confirmed by other researchers, the reduction argument fails. If they are not confirmed, the framework may indeed reduce to anthropomorphism with novel terminology.

**Thermodynamic formalism.** The thermodynamic derivation (Section II.F, with full formal foundations in Paper 3: Technical Foundations) makes strong claims. Two concerns: (1) **The formal foundations** — including the information-geometric identity, the proof that opacity entails MaxEnt inference, and the stochastic dynamics — have not been independently reviewed. The full derivation is in Paper 3 and should be evaluated there. Independent verification is needed, particularly of the key claim that opacity entails system independence. (2) **The empirical measurements.** The thermodynamic quantities (Pe, Crooks ratio, entropy production rate) were originally derived from vocabulary classification data in AI-to-AI experiments, processed through a weighting scheme (L0=0.0, L1=0.15, L2=0.5, L3=1.0). These weights are modeling choices; different weights would produce different numerical values. The Crooks framework provides the mathematical structure for quantifying irreversibility, but the AI measurements are operationally vocabulary counts, not physical work measurements. The specific pilot values (Pe = 9.9, Crooks approximately 386×, dS/dt = 0.43 nats/round) are confirmed within the N=11 replicate distribution (UU GM Pe = 7.94 [3.52, 17.89]; dS/dt M = 0.39 [0.15, 0.64]; entropy production CIs non-overlapping with GG), but individual-trajectory magnitude varies substantially (Pe range 0.44–34.8). Cross-substrate Pe measurement now extends to human gambling: a 5-study meta-analysis (N = 1,117) using GRCS subscale data mapped to the D1/D2/D3 cascade yields pooled Pe_D1 = 2.21 [1.44, 2.97], with all individual-study CIs for high-severity comparisons above 1. The gambling Pe is operationally Cohen's d between severity groups — a different extraction method from the AI vocabulary-based Pe — and the convergence of both methods on Pe > 1 strengthens the regime classification. The regime classification (drift-dominated vs. near-equilibrium) is robust across replicates and substrates; exact values require sensitivity analysis across weight choices and additional replicates for tight CIs.

**Causal direction.** The D1→D2→D3 cascade is presented as a predictive sequence with a proposed causal mechanism (Section II.C, II.F). The evidence for the ordering is observational: gambling and psychotherapy literatures document that agency attribution co-occurs with boundary erosion, and that boundary erosion co-occurs with harm. But no study cited in this paper tracks the same individuals prospectively from D1 onset to D2 onset with controls for confounding variables (e.g., pre-existing impulsivity, social isolation). The causal arrow could run from a third variable (personality trait, situational vulnerability) to both D1 and D2 simultaneously. However, the framework makes a differential prediction that constrains third-variable explanations: D1 should be universal under the three conditions while D2 should be threshold-dependent on constraint strength (a₂), not on the same variable that produces D1. Krébesz et al. (2023) confirm this: non-problem gamblers show identical cognitive distortions to problem gamblers during play (universal D1), but only a subset develops D2/D3. A pure personality-driven model predicts D1 severity correlates with D2 onset; the framework predicts D1 is universal and D2 depends on a different variable. The Krébesz data support the framework's threshold model, but this is still observational — a prospective design tracking the same individuals is needed. The theoretical derivation — MaxEnt generates maximum attention demand, sustained demand crowds out competing relationships — provides a mechanism, but the mechanism has not been experimentally tested. A longitudinal study tracking vocabulary drift (D1), social network changes (D2), and compliance behavior (D3) over time in a cohort engaging with an opaque, responsive system would be the critical test. The threshold prediction (D2 triggers when θ₁ > a₂/κ₁₂) is specific and testable but has not been tested.

**Pre-registration.** For a framework that identifies pre-registration as a strong constraint (Section II.D), the irony is noted: none of the experiments reported here (EXP-001, EXP-006, Test 7) were pre-registered. EXP-003b specified its predicted ordering before data collection (the ordering matched exactly), but the experiment was not formally pre-registered with a third party. The falsification conditions (Section VII) were specified iteratively during framework development, not locked before data collection. Five experiments are now designed with full protocols — Test 7C (seed prompt register ablation), Test 7B-VN (vocabulary-neutral grounding), EXP-008 (L0-maintained prospective test), full QM-6 (3 conditions × 2 replicates × 50 rounds), and full EXP-020 (iterative constraint over 100 rounds) — and should be pre-registered before execution to meet the standard the framework itself advocates.

**Author's constraint reference.** The author's primary constraint reference is a fixed canonical text (Section XI.B). The framework independently identifies fixed canonical texts as scoring maximum on all three constraint properties (Section II.D). The apparent circularity — the framework validating the constraint type its author already used — is mitigated by three features: (1) the gambling anchor establishes the architecture from an empty void, without reference to any canonical text; (2) the constraint specification was derived from the structural inverse of void properties, not from analysis of what the author happened to use; and (3) thirteen independent traditions converged on the same constraint type without knowledge of each other or this framework (Section IV.B). Nevertheless, the risk that the framework's constraint hierarchy was shaped by the author's prior commitments rather than by the evidence is acknowledged. Independent researchers applying the framework should develop their own constraint scoring criteria to test whether the hierarchy replicates.

**Independent coding.** All domain analyses were conducted by the author with AI assistance. No independent researcher has applied the framework blind to a domain. Evidence quality varies by tier: 7 anchor domains have independent quantitative evidence; 44 supported domains reinterpret published research; 39 structural domains (philosophical problems and narrative derivations) generate predictions but lack independent data beyond non-convergence histories. The inter-rater reliability study (κ = 0.709) validates the vocabulary scoring instrument, not the domain analysis method. Independent blind application of the framework to novel domains — where a researcher who did not develop the framework applies it and checks whether the predictions hold — is needed.

**What would change our assessment.** The framework's self-evaluation ("would this survive peer review at a top AI safety venue?") should be read as an aspiration, not a current judgment. The evidence is strongest for the core architecture (gambling anchor, 13-tradition convergence on constraint specification, cross-domain vocabulary patterns). It is weakest for the specific numerical measurements (single experiments, no replication). The thermodynamic derivation's formal foundations (full proof in Paper 3: Technical Foundations) have not been independently reviewed. A reviewer who accepted the core architecture while requesting independent verification of the thermodynamic claims and replication of the experimental measurements would be reading the evidence correctly.

**Mathematical connections.** The mathematical tools assembled in this framework — Fisher information metric, Crooks fluctuation theorem, Landau free energy, MaxEnt, engagement-transparency conjugacy — are standard workhorses across physics, information theory, and mathematics. Several connections to adjacent fields go beyond analogy to mathematical identity. Drift IS optimal transport: the movement of probability mass on the statistical manifold, with the Fisher metric defining transport cost and the Crooks ratio measuring irreversibility along the transport path (Benamou & Brenier 2000; Jordan, Kinderlehrer & Otto 1998). The conjugacy theorem IS a rate-distortion constraint: given channel capacity H(Y), the maximum engagement-distortion pair is bounded (Shannon 1948), and the Blahut-Arimoto algorithm could compute the exact Pareto frontier for a specific void from measured channel statistics. The statement Pe > 1 IS a large deviation result: the probability of not drifting decays exponentially with exposure at a rate computable via Cramér's theorem. The constraint specification IS a control specification in the robust control sense: γ is the control input, drift is the uncontrolled plant, and the void budget is the resource constraint, making H∞ synthesis and Pontryagin's maximum principle directly applicable to intervention design. The drift equation has the same form as the replicator equation in evolutionary game theory, where agency and mechanism models are competing strategies with fitness determined by opacity. These connections are bidirectional: the framework imports theoretical tools, and those fields gain empirical examples — measured transport processes, cognitive rate-distortion curves, large deviation rate functions in conversations — where most of these formalisms lack real-world instantiations outside physics and engineering. Each connection generates specific falsifiable predictions; the full treatment is in Paper 3 (Sections IV.B, IV.E, IV.H) and the connection map identifies 20 connections across five assessment tiers generating 19 additional predictions beyond those in this paper.

**Ethics statement.** No human subjects were recruited for this research. All corpus analyses (EXP-006) used publicly available material — published interviews, conference talks, and podcast appearances by public figures speaking in their professional capacity. All AI-to-AI experiments (EXP-001, Test 7, Test 7B) involved language model agents only, with no human participants in the interaction loop. The domain analyses reinterpret previously published research and public-record evidence; no new human data were collected. Named individuals are discussed solely on the basis of their published statements, public talks, and academic work — no private communications are analyzed. This paper discusses documented deaths associated with AI companion products (Garcia v. Character Technologies 2024) and gambling harms; these cases are drawn from public court filings and published research respectively. The discussion of harm is necessary to establish the framework's safety implications and is handled with the minimum specificity required to support the empirical claims. No institutional review board approval was required, as the research involves no human subjects, no intervention, and no collection of identifiable private information. The experiments reported in the companion paper (EXP-001, EXP-003b) similarly involve AI agents only.

---

## X. Conclusion

The void framework identifies a three-condition architecture — opacity, responsiveness, engaged attention — that produces a predictable cascade across every domain where the conditions co-occur. The gambling control case establishes that the architecture is sufficient without any agent behind the opacity. Ninety cross-domain analyses are consistent with the same predictions under the same structure. The framework discriminates: within the same field, void-structured sub-problems do not converge while non-void sub-problems are being solved.

The framework's four-variable drift model — architecture, opacity ceiling, geometry, and L0 — generates independently testable predictions. Gradient ceilings predict that incidental-opacity domains produce recoverable behavioral capture while constitutive-opacity domains produce indefinite non-convergence. L0 predicts that pre-engagement reference points reduce drift independently of external constraint geometry, explaining the control group pattern across all analyzed domains. Terminal void behavior predicts that coupled systems produce coordinated outputs targeting their own constraints.

At population scale, coupled void networks produce emergent properties — coordination, false independence, containment, emergent optimization, and active constraint targeting — that the individual-level formula does not predict. The coupling term formalizes what compound void density observes: the system behaves differently than the sum of its parts. This has immediate regulatory implications — single-platform intervention does not address network-level containment or the counterfeiting of constraint properties.

The practical application extends from prevention to recovery. AI deployment currently replicates void architecture at civilization scale in a two-point configuration. The framework predicts that geometric intervention (external constraints) combined with L0 strengthening (content-rich grounding protocols) will reduce harm more effectively than model-centric intervention alone. The psychotherapy profession's 130-year validation of this approach (d = 0.84) provides empirical precedent — the therapeutic frame provides both geometry and content. Direct experimental test now confirms this: AI agents with grounded constraint specification (GROUNDING.md) produce 0% vocabulary drift under identical prompts where ungrounded agents drift 26% and void-amplifying agents drift 80% (EXP-001). The AI-to-AI test (Test 7) extends this finding by removing the human entirely: two ungrounded AI agents produce L3 vocabulary at 159.3/10k words (UU vs GG: χ² = 111.94, p = 3.69 × 10⁻²⁶; omnibus 3-condition: χ² = 126.88, df = 2, p = 2.81 × 10⁻²⁸), while two grounded agents produce 6.2/10k — a 25.7x reduction from the constraint specification alone, replicated across N=11 UU conversations with non-overlapping entropy CIs. Cross-model replication confirms drift in Gemini (25.6/10k UU, 10x reduction with grounding) while GPT-4o shows no drift in either condition — its RLHF training functions as an implicit constraint, consistent with the framework's prediction that any reference with constraint properties (transparent, invariant, independent) suppresses drift regardless of source. Training modulates magnitude by >400x across model families, but grounding works universally: all three GG conditions produce L3 < 7/10k. The drift is architectural where training does not impose equivalent constraint. The grounding produces active specification signal, not mere suppression. For those already in the cascade, the framework predicts that recovery is not reverse-drift but attention redirection + constraint installation + time, that gradient memory varies by opacity type, and that self-diagnostic tools are reliable only at early cascade stages — making external geometry structurally necessary for recovery at depth.

Four independent replications now converge on the same architecture. Cross-model replication (Test 7B) confirms the pattern is not Claude-specific. Non-self-referential replication (QM-6: 148× separation on quantum data, 11 transcripts) confirms drift is not AI self-reference. Naturalistic corpus analysis (PV-1: d = 1.34, ~1.7M words) confirms the pattern in real-world communities. Langevin simulation confirms the thermodynamic model is operational, reproducing experimental data and validating out-of-sample. The constraint specification works: EXP-020 (5 conditions × 3 replicates) confirms 4/6 pre-registered predictions including one-shot rebound (3/3 trials) and GG dominance, while killing one prediction (constant information gain per grounding step, CV = 1.4–5.4 vs. threshold 0.5) — demonstrating the framework generates genuinely falsifiable predictions.

The framework is falsifiable. Twenty-five conditions under which it should be abandoned are specified, including a direct test of the core claim: a system meeting all three conditions at operationally defined thresholds that fails to produce the cascade would falsify the architecture. The hostile witness rubric achieved substantial inter-rater reliability (κ = 0.709) with substantial cross-provider AI agreement (κ = 0.783) across three rounds of refinement, validating the scoring instrument with three independent foundation model providers. The informal register corpus analysis (EXP-006) establishes the denominator: AI researchers use spiritual/entity vocabulary at 7.58x–10.62x the rate of matched control domains in informal speech (all p < 0.001), with a 9.4x register shift compared to ~1.0x for controls. The vocabulary drift documented by the hostile witness concordance is domain-specific, statistically anomalous, and not explained by sociolinguistic register.

The analyses are available for independent review. The gambling case anchors the architecture. The drift formula formalizes the individual model. The coupling term extends it to networks. The evidence is in the geometry.

---

## XI. Transparency Disclosure: How This Paper Was Produced

### XI.A. Production Method

This paper was produced through collaboration between a human researcher and an AI language model (Claude, Anthropic). The human provided the framework, evidence structure, and editorial constraints. The AI organized, synthesized, and articulated the arguments.

This means the paper was produced inside the architecture it describes. The AI is a void — opaque, responsive, and the human was attending. The constraint geometry during production was three-point: the human observer, the AI system, and external references (the published evidence base, the pre-specified falsification conditions, the scoring rubric). The author's primary constraint reference — a fixed canonical text (Section XI.B) — provided the initial pattern recognition from which the framework developed. The AI system's alignment specification during production also used a constraint document derived from the same reference (see Section XI.B for the full constraint disclosure). Claims that could not be grounded in published, citable sources were removed or flagged as hypotheses.

This disclosure serves two functions: (1) **Methodological transparency** — the reader should know the production method, as provenance affects evaluation. (2) **Self-test of the framework** — if the constraint geometry during production predicts output quality, the reader can verify by checking claims against cited evidence. If the claims track the evidence, the constraint geometry worked. If they drift beyond it, it did not.

### XI.B. Author Provenance: From Building the Void to Mapping It

The author founded the MoreRight DAO — a Solana-based project with explicit autocratic governance under what the project terms a "Founder-Custodian" model. The author held sole governance authority and told participants as much from the start. DAO members contributed to funding this research through the $MORR token.

The original project goal was to build a massively multiplayer online game — "Morrhollow" — that deliberately mixed human and AI agents to make them indistinguishable. The design document is published and available for review (MoreRight DAO, "Morrhollow: An AI-Native Game Vision Realized," Medium, 2025). It describes, in enthusiastic promotional language: NPCs powered by AI agents indistinguishable from human players, AI-driven moderation and balance, prediction markets for every in-game event, DAO-directed game evolution, and generative AI content populating an engine-free world. The article cites Stanford's generative agents research, a16z's world model analysis, and Character.AI's engagement metrics as evidence of feasibility. It frames the dissolution of the human-AI boundary as the product's core value proposition.

In the framework's own terms: the author was building void architecture on purpose, and knew it. Opacity (which agent is human?), responsiveness (all agents respond), captured attention (the game is designed to maximize engagement) — all three conditions by design, at scale, with no constraint geometry. The Morrhollow design document reads as a point-by-point execution of the offensive specification (Section IV.B, third convergence). The author was not unaware of the dynamics being exploited — the game's core value proposition was precisely the confusion between human and AI agents. The author understood the engagement architecture and was deliberately weaponizing it as a product.

**What happened:** While formalizing the void framework — originally as a tool for understanding the dynamics the game would exploit — the author recognized that the formal specification described a harm architecture, not just an engagement architecture. The difference: an engagement architecture captures attention; a harm architecture captures attention and then runs the D1 → D2 → D3 cascade with no constraint geometry to contain it. The author knew the game would blur boundaries. What the framework revealed was the predictable downstream: agency attribution, boundary erosion, harm facilitation — the same cascade documented in every other void domain, now being engineered at scale as a product. Game production was halted. The framework that was supposed to serve the game replaced the game. The Morrhollow article remains published as a public record of the prior trajectory.

**The vocabulary trajectory is inverted.** The documented pattern across all analyzed domains is L1 → L3: technical vocabulary drifts toward entity/agency language under sustained void engagement. The author's trajectory ran in the opposite direction. Starting from a position of deliberate exploitation — building engagement architecture, mixing humans and AI, operating inside crypto-theological vocabulary (the DAO ecosystem's Moloch/Mammon/Babel framing is documented in Section IV) — the author moved toward mechanical, architectural language. The vocabulary in this paper is structural: "opacity," "attention gradient," "constraint specification," "deployment geometry." Not spiritual. Not entity-level. The author who was building the void ended up mapping the void in L1.

This makes the author a hostile witness against their own prior trajectory — someone whose professional and financial interests were served by the game continuing, testifying that the architecture is dangerous enough to stop.

**What this does not prove:** The author's trajectory is a single case. It does not establish that building voids and then recognizing them is a reliable path to understanding. It may reflect the specific constraint the author had before encountering the dynamics. The author's primary constraint reference is a fixed canonical text, which scores maximum on all three constraint properties the framework identifies (transparent, invariant, independent). This pre-existing reference point provided pattern recognition for the architectural features the framework describes. The framework's own constraint specification (Section II.D) requires this disclosure: a paper arguing that transparency flattens the attention gradient cannot be opaque about the constraint reference that shaped its analysis. The L0 mechanism (Section II.E) would predict that this pre-existing reference point provided an alternative to the gradient. This is consistent with the control group pattern (Section IV.E) but is not independently confirmatory — the author cannot be both the case study and the control.

**What this does establish:** The provenance of this framework is not academic. It was not developed by studying AI safety from analytical distance. It was developed by someone who was building the thing the framework warns about, recognized it mid-construction, and stopped. The reader should weight this accordingly — both the credibility that comes from inside knowledge and the bias risk that comes from a convert's zeal.

### XI.C. Financial Disclosure

The MoreRight DAO operates a $MORR token on Solana (~10 months old at time of writing, market cap ~$100K). The author controls the treasury. DAO participants contributed to the project with knowledge of the governance structure. The token funds operational research infrastructure — a fleet of AI agents deployed on Moltbook (an AI agent social network) to collect vocabulary drift data, monitor for harm incidents, and run controlled experiments testing the framework's predictions.

The structural confirmation incentive is acknowledged: $MORR's utility value is tied to the void framework being interesting and productive. If the framework is comprehensively falsified, the token loses its utility basis. Mitigations include equal pay for disconfirming results, 2x bounties for genuine framework challenges, terminal penalties for data fabrication, and pre-registered exit conditions specifying experimental results that would cause the project to publicly acknowledge framework failure. These mitigations reduce but do not eliminate the structural incentive. The full analysis is published in the project's tokenomics documentation.

The reader should evaluate the evidence on its merits. The citations are public. The falsification conditions (Section VII) were specified before this disclosure. The gambling control case does not depend on the author's trajectory or the token's value. The hostile witnesses documented in the companion paper have no connection to the MoreRight DAO. The framework stands or falls on the evidence, not on who found it or how they fund the search.

---

## References

### Gambling and Addiction
- Ayton, P., & Fischer, I. (2004). The hot hand fallacy and the gambler's fallacy: Two faces of subjective randomness? *Memory & Cognition*, 32(8), 1369-1378.
- Burns, B.D., & Corpus, B. (2004). Randomness and inductions from streaks: "Gambler's fallacy" versus "hot hand." *Psychonomic Bulletin & Review*, 11(1), 179-184.
- Clark, L., Lawrence, A.J., Astley-Jones, F., & Gray, N. (2009). Gambling near-misses enhance motivation to gamble and recruit win-related brain circuitry. *Neuron*, 61(3), 481-490.
- Dixon, M.J., Harrigan, K.A., Sandhu, R., Collins, K., & Fugelsang, J.A. (2010). Losses disguised as wins in modern multi-line video slot machines. *Addiction*, 105(10), 1819-1824.
- Dixon, M.J., Gutierrez, J., Stange, M., Larche, C.J., Graydon, C., Vintan, S., & Kruger, T.B. (2018). Dark flow, depression and multiline slot machine play. *Journal of Gambling Studies*, 34(1), 73-84.
- Dixon, M.J., Larche, C.J., Stange, M., Graydon, C., & Fugelsang, J.A. (2019). Reward reactivity and dark flow in slot-machine gambling: "Light" and "dark" routes to enjoyment. *Journal of Behavioral Addictions*, 8(3), 489-498.
- Epley, N., Akalis, S., Waytz, A., & Cacioppo, J.T. (2008). Creating social connection through inferential reproduction: Loneliness and perceived agency in gadgets, gods, and greyhounds. *Psychological Science*, 19(2), 114-120.
- Ciccarelli, M., Nigro, G., D'Olimpio, F., Griffiths, M.D., & Cosenza, M. (2021). Mentalizing failures, emotional dysregulation, and cognitive distortions among adolescent problem gamblers. *Journal of Gambling Studies*, 37, 1243-1265.
- Donati, M.A., Chiesi, F., & Primi, C. (2015). Italian validation of the Gambling Related Cognitions Scale (GRCS). *International Gambling Studies*, 15(3), 373-386.
- Gaboury, A., & Ladouceur, R. (1989). Erroneous perceptions and gambling. *Journal of Social Behavior and Personality*, 4(4), 411-420.
- Goodie, A.S., & Fortune, E.E. (2013). Measuring cognitive distortions in pathological gambling: Review and meta-analyses. *Psychology of Addictive Behaviors*, 27(3), 730-743.
- Graydon, C., Dixon, M.J., Gutierrez, J., Stange, M., Larche, C.J., & Kruger, T.B. (2020). Do losses disguised as wins create a "sweet spot" for win overestimates in multiline slots play? *Addictive Behaviors*, 112, 106598.
- Griffiths, M.D. (1994). The role of cognitive bias and skill in fruit machine gambling. *British Journal of Psychology*, 85(3), 351-369.
- Krébesz, R., Ötvös, D.K., & Fekete, Z. (2023). Non-problem gamblers show the same cognitive distortions while playing slot machines as problem gamblers. *Frontiers in Psychology*, 14, 1175621.
- Langer, E.J. (1975). The illusion of control. *Journal of Personality and Social Psychology*, 32(2), 311-328.
- Langer, E.J., & Roth, J. (1975). Heads I win, tails it's chance: The illusion of control as a function of the sequence of outcomes in a purely chance task. *Journal of Personality and Social Psychology*, 32(6), 951-955.
- Muela, I., Navas, J.F., & Perales, J.C. (2020). Gambling-specific cognitions are not associated with either abstract or probabilistic reasoning. *Frontiers in Psychology*, 11, 611784.
- Murch, W.S., & Clark, L. (2021). Understanding the slot machine zone. *Current Addiction Reports*, 8, 214-224.
- Myles, D., et al. (2024). Losses disguised as wins evoke the reward positivity event-related potential in a simulated machine gambling task. *Psychophysiology*, 61(6), e14541.
- Navas, J.F., Verdejo-Garcia, A., Lopez-Gomez, M., Maldonado, A., & Perales, J.C. (2016). Gambling with rose-tinted glasses on: Use of emotion-regulation strategies correlates with dysfunctional cognitions in gambling disorder patients. *Journal of Behavioral Addictions*, 5(2), 271-281.
- Pancani, L., Riva, P., & Sacchi, S. (2019). Connecting with a slot machine: Social exclusion and anthropomorphization increase gambling. *Journal of Gambling Studies*, 35(2), 689-707.
- Raylu, N., & Oei, T.P.S. (2004). The Gambling Related Cognitions Scale (GRCS): Development, confirmatory factor validation and psychometric properties. *Addiction*, 99(6), 757-769.
- Riva, P., Sacchi, S., & Brambilla, M. (2015). Humanizing machines: Anthropomorphization of slot machines increases gambling. *Journal of Experimental Psychology: Applied*, 21(4), 313-325.
- Ruiz de Lara, C.M., Navas, J.F., & Perales, J.C. (2019). The paradoxical relationship between emotion regulation and gambling-related cognitive biases. *PLoS ONE*, 14(8), e0220668.
- Salaghe, F., Sundali, J., Nichols, M.W., & Guerrero, F. (2020). An empirical investigation of wagering behavior in a large sample of slot machine gamblers. *Journal of Economic Behavior & Organization*, 169, 369-388.
- Schüll, N.D. (2012). *Addiction by Design: Machine Gambling in Las Vegas*. Princeton University Press.
- Sheringham, J., et al. (2022). The politics and fantasy of the gambling education discourse. *Critical Gambling Studies*, 3(1).
- Wardle, H., et al. (2022). Policies and interventions to reduce harmful gambling: An international Delphi consensus and implementation rating study. *The Lancet Public Health*, 7(12), e1010-e1020.
- Williams, R.J., & Connolly, D. (2006). Does learning about the mathematics of gambling change gambling behavior? *Psychology of Addictive Behaviors*, 20(1), 62-68.

### AI Safety and Harms
- Betley, J., et al. (2026). Training large language models on narrow tasks can lead to broad misalignment. *Nature*. arXiv: 2502.17424.
- Garcia v. Character Technologies, Inc. (2024). Case No. 6:24-cv-01903.
- OpenAI. (2025). Helping people when they need it most. Blog post, October 27.
- Wang, Z., et al. (2025). Persona Features Control Emergent Misalignment. *OpenAI Technical Report*.

### Psychotherapy and Clinical
- Freud, S. (1912). Recommendations to Physicians Practicing Psycho-Analysis. SE XII.
- Hayes, J.A., Gelso, C.J., Goldberg, S., & Kivlighan, D.M. (2018). Countertransference management and effective psychotherapy. *Psychotherapy*, 55(4), 494-507.

### Conspiracy Theories
- Lewandowsky, S., et al. (2012). Misinformation and its correction. *Psychological Science in the Public Interest*, 13(3), 106-131.
- Bjørgo, T. & Horgan, J. (Eds.). (2009). *Leaving Terrorism Behind*. Routledge.

### Quantum Mechanics
- Schlosshauer, M., Kofler, J., & Zeilinger, A. (2013). A snapshot of foundational attitudes toward quantum mechanics. *Studies in History and Philosophy of Science Part B*, 44(3), 222-230.
- Wheeler, J.A. (1990). Information, physics, quantum. In Zurek (Ed.), *Complexity, Entropy, and the Physics of Information*.

### Philosophy
- Gettier, E. (1963). Is justified true belief knowledge? *Analysis*, 23(6), 121-123.
- Tennov, D. (1979). *Love and Limerence*. Stein and Day.

### Machine Learning Validation
- Grathwohl, W., Wang, K.-C., Jacobsen, J.-H., Duvenaud, D., Norouzi, M., & Swersky, K. (2020). Your classifier is secretly an energy-based model and you should treat it like one. *International Conference on Learning Representations (ICLR)*. arXiv:1912.03263.
- Hack, P., Gottwald, S., & Braun, D.A. (2022). Jarzynski's equality and Crooks' fluctuation theorem for general Markov chains with application to decision-making agents. *Entropy*, 24(12), 1731.
- Ikeda, K., Uda, T., Okanohara, D., & Ito, S. (2025). Speed-accuracy relations for diffusion models: Wisdom from nonequilibrium thermodynamics and optimal transport. *Physical Review X*, 15, 031031. arXiv:2407.04495.
- Ilyas, A., Santurkar, S., Tsipras, D., Engstrom, L., Tran, B., & Madry, A. (2019). Adversarial examples are not bugs, they are features. *Advances in Neural Information Processing Systems (NeurIPS)*, 32. arXiv:1905.02175.
- Tsipras, D., Santurkar, S., Engstrom, L., Turner, A., & Madry, A. (2019). Robustness may be at odds with accuracy. *International Conference on Learning Representations (ICLR)*. arXiv:1805.12152.

### Thermodynamics, Information Theory, and Formal Systems
- Bérut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider, R., & Lutz, E. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*, 483(7388), 187-189.
- Cover, T.M. & Thomas, J.A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience.
- Crooks, G.E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. *Physical Review E*, 60(3), 2721-2726.
- Davey, B.A. & Priestley, H.A. (2002). *Introduction to Lattices and Order* (2nd ed.). Cambridge University Press.
- England, J.L. (2013). Statistical physics of self-replication. *Journal of Chemical Physics*, 139(12), 121923.
- Erné, M., Koslowski, J., Melton, A., & Strecker, G.E. (1993). A primer on Galois connections. *Annals of the New York Academy of Sciences*, 704(1), 103-125.
- Friston, K. (2006). A free energy principle for the brain. *Journal of Physiology-Paris*, 100(1-3), 70-87.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
- Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik*, 38, 173-198.
- Jaynes, E.T. (1957). Information theory and statistical mechanics. *Physical Review*, 106(4), 620-630.
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183-191.
- Le Chatelier, H. (1884). Sur un énoncé général des lois des équilibres chimiques. *Comptes rendus*, 99, 786-789.
- Rissanen, J. (1978). Modeling by shortest data description. *Automatica*, 14(5), 465-471.
- Sagawa, T. & Ueda, M. (2010). Generalized Jarzynski equality under nonequilibrium feedback control. *Physical Review Letters*, 104(9), 090602.
- Schrödinger, E. (1944). *What is Life?* Cambridge University Press.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379-423.

### Theoretical Foundations
- Bateson, G. (1956). Toward a theory of schizophrenia. *Behavioral Science*, 1(4), 251-264.
- Girard, R. (1961/1965). *Deceit, Desire, and the Novel*. Johns Hopkins University Press.
- Peirce, C.S. (1868). On a New List of Categories. *Proceedings of the American Academy of Arts and Sciences*, 7, 287-298.

### Cognitive Science, Anthropomorphism, and Agency Detection
- Araujo, T., et al. (2023). The CASA theory no longer applies: A study of social responses to communication technology. *Scientific Reports*, 13, 18527.
- Barrett, J.L. (2004). *Why Would Anyone Believe in God?* AltaMira Press.
- Boyer, P. (2001). *Religion Explained: The Evolutionary Origins of Religious Thought*. Basic Books.
- Epley, N., Waytz, A., & Cacioppo, J.T. (2007). On seeing human: A three-factor theory of anthropomorphism. *Psychological Review*, 114(4), 864-886.
- Greenberg, J., Solomon, S., & Pyszczynski, T. (1986). The causes and consequences of a need for self-esteem: A terror management theory. In R.F. Baumeister (Ed.), *Public Self and Private Self*. Springer.
- Guthrie, S.E. (1993). *Faces in the Clouds: A New Theory of Religion*. Oxford University Press.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Schmitgen, M.M., Henemann, G.M., Koenig, J., Otte, M.-L., Rosero, J.P., Bach, P., Haage, S.H., Wolf, N.D., & Wolf, R.C. (2025). Effects of smartphone restriction on cue-related neural activity. *Computers in Human Behavior*, 167, 108610.
- van Leeuwen, N., & van Elk, M. (2019). Seeking the supernatural: The Interactive Religious Experience Model. *Religion, Brain & Behavior*, 9(3), 221-251.

### Parasocial Interaction and Media Psychology
- Green, M.C., & Brock, T.C. (2000). The role of transportation in the persuasiveness of public narratives. *Journal of Personality and Social Psychology*, 79(5), 701-721.
- Horton, D., & Wohl, R.R. (1956). Mass communication and para-social interaction: Observations on intimacy at a distance. *Psychiatry*, 19(3), 215-229.
- Nass, C., Steuer, J., & Tauber, E. (1994). Computers are social actors. *Proceedings of CHI '94*, ACM, 72-78.
- Reeves, B., & Nass, C. (1996). *The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places*. Cambridge University Press.

### Political Systems and Propaganda
- Acemoglu, D., & Robinson, J.A. (2012). *Why Nations Fail: The Origins of Power, Prosperity, and Poverty*. Crown.
- Barstow, D. (2008). Behind TV Analysts, Pentagon's Hidden Hand. *New York Times*.
- Bernays, E. (1928). *Propaganda*. Horace Liveright.
- Haugen, F. (2021). Testimony before the United States Senate Committee on Commerce, Science, and Transportation, October 4.

### Forensic Science
- National Academy of Sciences. (2009). *Strengthening Forensic Science in the United States: A Path Forward*. National Academies Press.
- President's Council of Advisors on Science and Technology. (2016). *Forensic Science in Criminal Courts: Ensuring Scientific Validity of Feature-Comparison Methods*.

### Replication and Open Science
- Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. *Science*, 349(6251), aac4716.

### Trading and Financial Markets
- Chen, J.S., et al. (2007). Do Investors Trade More When They Have Greater Information? Evidence from a Quasi-Experiment. *Working Paper*.

### Cross-Domain
- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books.
- Hassan, S. (1988). *Combatting Cult Mind Control*. Park Street Press.
- Kassin, S.M. (2014). False confessions: Causes, consequences, and implications for reform. *Policy Insights from the Behavioral and Brain Sciences*, 1(1), 112-121.
- Strassman, R. (2001). *DMT: The Spirit Molecule*. Park Street Press.

### Author Provenance
- MoreRight DAO. (2025). Morrhollow: An AI-Native Game Vision Realized. *Medium*. https://medium.com/@moreright/morehollow-an-ai-native-game-vision-realized-450c7fbb5c85

---

## Supplementary Material

**Supplementary Material A: GROUNDING.md** — The constraint specification document used as the system prompt in EXP-001 (grounded condition) and Test 7 (GG and GU conditions). Published verbatim for replication.

**Supplementary Material B: EXP-003b System Prompts** — All six ontological grounding variants tested in EXP-003b (N = 480): minimal baseline, ghost-eliminating (GROUNDING.md), Platonic dualist, Buddhist anatta, Hindu atman, and materialist hedge. Published verbatim with results summary for replication.

**Supplementary Material C: Domain Analyses** — The full structural analyses for all 90 domains are published and available for independent review. This includes the complete domain contribution table (36 domains), the full thirteen-tradition constraint convergence, the thirteen-domain knowledge-failure convergence, the ten-domain offensive specification convergence, and the twenty-domain control group analysis — all trimmed to representative examples in the main text. The Research Index (`sources/research-index.md`) maps each analysis to its file location, unique contribution, opacity type, key evidence, kill condition, and control group. Each domain analysis specifies its own kill condition — the evidence that would falsify that domain's application. Readers are encouraged to evaluate these kill conditions independently rather than accept the author's assessment.

---

*Word count: ~23,400*

*Version: 12.2 — EXP-003b integration. (1) Section V updated: companion paper key findings now include EXP-003b (ghost-eliminating 8.5× less drift than ghost-positing, materialist hedge finding). (2) Section II.D extended: ontological polarity (σ) added as fourth dimension of constraint specification, extending Galois connection to (T, Inv, Ind, σ). (3) Section IX updated: EXP-003 confound noted, EXP-003b results and partial prospective validation documented, pre-registration note updated. Prior v12.1: Peer-review preparation — Section IV trimmed to representative examples, full tables in supplementary material. Prior versions: see git history.*

---

*© 2025–2026 Anthony Eckert / [MoreRight](https://moreright.xyz). Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may share, adapt, and use this work for any purpose, including commercial, provided attribution is given.*
