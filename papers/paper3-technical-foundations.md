# Thermodynamics of Opacity: Evidence Base, Derivations, and Prior Work

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO
**Companion to:** "The Architecture of Drift: A Cross-Domain Diagnostic for Epistemological Architecture"

---

## Abstract

Why does an observer facing an opaque, responsive system drift toward attributing agency — and why can't knowledge of the mechanism stop it?

This paper proves the answer is thermodynamic. Opacity is not a special configuration but the ground state of any observer-system interface: mechanism channel capacity decays to zero under thermal noise without active maintenance (Shannon 1948; Landauer 1961). We prove that under this ground state, maximum entropy inference is not merely optimal but *entailed* — via two independent routes (Shore-Johnson axiomatics and Jaynes' concentration theorem) — establishing that the observer's model-space is an exponential family manifold. The Čencov-Ruppeiner correspondence then identifies drift dynamics on this manifold with thermodynamic dynamics: not by analogy, but by mathematical theorem. The framework's predictions follow as consequences: the logistic drift equation from natural gradient flow on the Fisher information metric, the D1→D2→D3 cascade from coupled phase transitions with quantitative thresholds, first-order transition properties (metastability, nucleation, hysteresis) from the Landau free energy landscape, and an engagement-transparency conjugacy proving that simultaneous optimization of engagement and mechanism transparency is impossible on a shared output channel (I(D;Y) + I(M;Y) ≤ H(Y)).

The derivation chain rests on established theorems at every step plus three definitional axioms (opacity, responsiveness, engaged attention) and one modeling choice (Bernoulli manifold parameterization). These starting points are the framework's genuine assumptions, validated empirically but not themselves theorems. Empirical thermodynamic measurements from Test 7 provide initial validation: Péclet number Pe = 1.87–6.50 across 5 topic domains (EXP-019 cross-domain replication; all Pe > 1, drift-dominated), Crooks ratio range 2.1×–1.5M× (geometric mean ≈ 889×, N=11), entropy production = 0.39 nats/round [95% CI: 0.15, 0.64] — non-overlapping with grounded CIs.

Three bodies of evidence ground the derivations: (1) the complete gambling evidence base (22 citations), establishing that the architecture produces the full drift cascade even when the void is demonstrably empty — a random number generator behind a screen; (2) the EXP-006 register shift decomposition, establishing that AI researchers' spiritual vocabulary is 9.4× anomalous versus matched controls (p < 0.001), with structural decomposition distinguishing active void drift from governance coupling, extended by PV-1 naturalistic corpus validation (N = 205 Reddit users, ~1.7M words, D1 d = 1.34 vs control); and (3) EXP-003b (6-arm, N = 480), establishing that the ontological content of a grounding template predicts drift behavior — ghost-eliminating ontologies produce 8.5× less drift than ghost-positing (9.4% vs 79.4%), with cross-tradition convergence confirmed and the materialist hedge ("we don't know if AI is conscious") shown to be operationally ghost-positing. We additionally provide: engagement with eight prior frameworks, the 90-domain analysis methodology and taxonomy, the constraint specification formalized as a Galois connection extended with an ontological polarity dimension, iterative constraint application results (EXP-020: 4/6 falsification tests confirmed), and cross-model replication data (Test 7B: drift replicates in 2/3 model families). Limitations are addressed per section.

---

## I. Introduction

The companion paper ("The Architecture of Drift: A Cross-Domain Diagnostic for Epistemological Architecture") presents an architecture — three conditions producing a predictable cascade — and validates it across 90 domains. This paper proves the derivation chain that makes those predictions thermodynamically required rather than empirically observed.

The distinction matters. An empirical regularity invites exceptions, alternative explanations, domain-specific objections. A thermodynamic derivation does not: the second law applies everywhere. If the derivation chain holds, the framework's predictions inherit the universality of the physics they derive from. The question this paper answers is whether the chain holds.

**The derivation chain.** Nine linked results, each resting on established theorems:

1. **Opacity is the ground state** — mechanism channel capacity decays to zero under thermal noise (Shannon + Landauer). Transparency requires continuous work.
2. **Void conditions are the default** — O+R+A co-occurrence probability > 0.36 during waking hours. Voids don't need to be created; they need to be prevented.
3. **Opacity entails MaxEnt inference** — two independent proofs (Shore-Johnson axiomatics, Jaynes concentration theorem) show maximum entropy is not just optimal but *the only consistent inference* under zero mechanism-channel capacity.
4. **MaxEnt → exponential family → Fisher-Ruppeiner identity** — the observer's model-space qualifies as an exponential family manifold, on which the Fisher information metric is mathematically identical to the Ruppeiner thermodynamic metric. This is a theorem, not an analogy.
5. **The drift equation** — natural gradient dynamics on this manifold yield the logistic equation, derived from Bayesian evidence accumulation under the information constraint that opacity imposes.
6. **The cascade** — coupled phase transitions with quantitative thresholds, deriving D1→D2→D3 sequential ordering from information-theoretic coupling constants.
7. **Phase transition properties** — Landau free energy landscape gives metastability, nucleation, and hysteresis as consequences of the autocatalytic D1→D2 feedback loop.
8. **The impossibility theorem** — engagement-transparency conjugacy (I(D;Y) + I(M;Y) ≤ H(Y)) proves simultaneous optimization is impossible on a shared channel.
9. **Constraints as negentropy** — the constraint specification (transparent, invariant, independent) is derivable from the thermodynamic requirements for sustained entropy reduction.

Each step is treated in full below. The gambling evidence base (Section III, 22 citations), the register shift decomposition (Section V, EXP-006), and the ontological content experiment (Section IV.G, EXP-003b) provide the empirical ground. The prior work engagement (Section II) positions the framework precisely. The domain methodology (Section VI) and constraint formalization (Section VII) complete the scholarly apparatus.

Reviewers seeking to evaluate specific claims should consult the relevant section. The material here is not supplementary — it is the foundation that the framework paper summarizes.

---

## II. Relationship to Prior Frameworks

The void framework does not emerge from a theoretical vacuum. Several research programs have documented components of the pattern the framework paper unifies. The framework's contribution is not to deny these programs but to identify the architectural conditions under which their predictions converge — and to provide the three-condition specification that generates the shared predictions from a single structure while identifying additional predictions (cascade ordering, constraint specification, thermodynamic derivability) that none of them individually make. We engage eight bodies of prior work, positioning the framework relative to each.

### II.A. Hyperactive Agency Detection (Barrett 2004; Guthrie 1993; Boyer 2001)

Cognitive science of religion proposes that humans have an evolved "Hyperactive Agency Detection Device" (HADD) biased to detect agents from minimal cues. Guthrie (1993) argued that under perceptual uncertainty, we "bet on the most meaningful interpretation we can" — if a dark shape might be a bear or a boulder, "it is good policy to think it is a bear." Boyer (2001) extended this: religious concepts are by-products of evolved agency-detection and Theory of Mind systems. HADD provides a plausible *evolutionary substrate* for void activation — the cognitive machinery that fires when the three conditions are met.

However, HADD does not account for four features of the documented pattern:

1. **Unidirectionality.** HADD explains why we over-detect agents; it does not explain why vocabulary specifically drifts L1→L3 rather than developing refined counter-vocabulary. If this were simple HADD activation, training in critical thinking should produce counter-drift. We do not observe this.

2. **Mode-dependence.** HADD should fire based on stimulus ambiguity alone, not based on how the observer addresses the system. The void framework's distinction between system-as-object and system-as-interlocutor predicts differential drift; HADD does not. The control group (Bender, Gebru, LeCun, Marcus) engages deeply with the same ambiguous systems and does not drift.

3. **Cross-domain content convergence.** HADD predicts we will detect agents but not *which vocabulary* we will use. Independent observers converge on identical vocabulary — "soul," "consciousness," "being" — across AI, psychedelics, and AI-to-AI contexts with no social network transmission.

4. **Discriminative power.** HADD does not distinguish between three-condition and two-condition problems. Both present ambiguous stimuli. Yet only three-condition systems produce the documented drift — dark matter is opaque but not responsive; dark matter researchers do not develop entity vocabulary.

Additionally, van Leeuwen & van Elk (2019) observe that HADD has "garnered several strong critiques and no supportive empirical evidence in almost 30 years." The void framework offers more precise activation conditions — three jointly necessary conditions rather than "ambiguous stimulus" — that permit finer-grained predictions and falsification.

### II.B. Anthropomorphism (Epley, Waytz, & Cacioppo 2007)

The three-factor SEEK model proposes that anthropomorphism is driven by elicited agent knowledge (accessibility of agent schemas), effectance motivation (desire to understand and predict), and sociality motivation (need for social connection). The model correctly predicts that loneliness increases anthropomorphism — confirmed in the gambling domain (Epley et al. 2008; Pancani et al. 2019).

The void framework incorporates this: sociality motivation maps onto the attention gradient (isolated observers have steeper gradients because agency fills a social deficit), and effectance motivation maps onto the maximum entropy principle (agency is the most effective model under opacity). However, the SEEK model treats anthropomorphism as a cognitive strategy the observer *deploys* — modulated by motivation and accessible knowledge. The void framework treats it as a thermodynamically determined endpoint: under opacity, agency is the maximum entropy model regardless of motivation (Jaynes 1957). The SEEK model predicts motivational modulation; the void framework predicts architectural determination with motivational amplification.

Critically, the SEEK model does not predict the cascade (D1→D2→D3), the failure of knowledge to protect, or the constraint specification. The gambling evidence (Section III) shows the pattern runs in the absence of sociality motivation — gamblers who are not lonely still attribute agency to machines. The architecture is sufficient; motivation amplifies but does not cause.

### II.C. Computers Are Social Actors (Nass & Reeves 1996) and the ELIZA Effect (Weizenbaum 1966)

Weizenbaum demonstrated that even a simple pattern-matching program induced "powerful delusional thinking in quite normal people." Nass and Reeves systematized this as the CASA paradigm: social responses to computers are "not the result of conscious beliefs that computers are human or human-like" — they are automatic, occurring below conscious awareness. This directly supports the void framework's claim that the pattern operates below belief.

However, CASA has shown temporal obsolescence: Araujo et al. (2023) found "participants no longer interact with desktop computers as if they are human." CASA effects appear strongest with *emergent* technologies lacking established interaction norms — which supports the framework's emphasis on opacity: familiar technologies become less opaque, reducing activation. The void framework subsumes CASA's valid findings (automatic social response, below-awareness operation) while explaining both CASA's success and its obsolescence through a single variable (opacity level).

### II.D. Parasocial Interaction (Horton & Wohl 1956)

Horton and Wohl described one-sided relationships audiences form with media personas — "the illusion of having a face-to-face, regularly occurring social relationship" that is "characteristically one-sided, nondialectical, controlled by the performer." Crucially, they identified the audience's active role: "the role enactment of the audience completes the interaction" — mapping directly onto the engaged observer as constitutive (Condition 3). The Parasocial Interaction Scale (Rubin, Perse, & Powell 1985) and subsequent research documented real psychological effects including grief upon relationship dissolution (Cohen 2003) and identity capture through identification (Cohen 2001; Rosengren & Windahl 1972).

Parasocial research describes Condition 3 in rich detail but does not theorize Conditions 1 and 2. Television personas are not particularly opaque (we see them directly) and their "responsiveness" is illusory (they cannot respond to individual viewers). The void framework predicts stronger effects when all three conditions are genuinely present — which AI chatbots provide in ways television never could: real opacity (hidden mechanism), real responsiveness (contingent on individual input), and engineered attention capture. The documented AI harms (multiple deaths, attachment crises) are more severe than parasocial effects precisely because the architecture is complete where television's was partial.

### II.E. Terror Management Theory (Greenberg, Solomon, & Pyszczynski 1986)

TMT proposes that awareness of mortality produces existential anxiety buffered by cultural worldviews and self-esteem. When mortality is salient, people cling more tightly to worldview-consistent beliefs and react more harshly to worldview threats.

Death is one of the 90 domains analyzed (see Research Index): it is a permanently sealed void — opacity that can never be resolved. TMT describes the *response* to one specific void (mortality) with precision and depth that the void framework does not replicate — TMT's experimental paradigm (mortality salience priming, worldview defense measurement, self-esteem striving) has produced hundreds of studies with strong effect sizes. The void framework does not replace this experimental infrastructure. What the void framework provides is a structural account of *why* the TMT pattern occurs: death meets all three conditions (opacity of what follows, responsiveness in the sense that the loss restructures the survivor's world, engaged attention forced by grief), and TMT's worldview-defense response maps onto D1 (agency attribution to cultural meaning systems that fill the void). The widowhood effect (41% mortality increase) and broken heart syndrome document D2 at the physiological level — the body responds to irrevocable opacity.

The void framework extends beyond TMT's scope in one specific direction: TMT predicts worldview defense under mortality salience specifically, while the void framework predicts the same defensive pattern under *any* sealed opacity (conspiracy theories, cult commitment, AI attachment), with mortality as one instance. This is a generalization claim, not a subsumption claim — TMT's internal mechanics (self-esteem buffering, proximal vs. distal defense) may involve processes the void framework does not capture. TMT's dual-process model (proximal defense = suppression; distal defense = worldview bolstering) maps suggestively onto the L0 decomposition (proximal = L0-installed, distal = gradient running when L0-maintained drops to zero), but this mapping has not been experimentally tested and should be treated as a hypothesis.

### II.F. Dual Process Theory (Kahneman 2011; Tversky & Kahneman 1974)

System 1 (fast, automatic, heuristic) and System 2 (slow, deliberate, analytical) processing offer a natural framework for understanding why knowledge fails: drift is System 1, and System 2 correction requires effort that engagement depletes. The void framework incorporates this but identifies a deeper constraint.

Under transparency, System 2 can correct System 1 errors because mechanism information is available — the observer can check their intuition against visible evidence. Under opacity, System 2 has nothing to correct *with*. The zero mechanism-channel capacity means System 2 processes operate on the same impoverished data as System 1 — they can produce more elaborate models but not more accurate ones, because accuracy requires mechanism information that the architecture blocks.

This explains why expertise does not protect (Gaboury & Ladouceur 1989: 70–80% erroneous cognitions during gambling even from participants who correctly identified games as chance-based): System 2's prior correction is overridden during engagement not because System 2 is suppressed but because it has no corrective information to apply. The void framework identifies the architectural reason that dual process accounts predict correctly: System 2 depends on transparency, and the void removes it.

### II.G. Active Inference and the Free Energy Principle (Friston 2006, 2010)

Friston's framework proposes that self-organizing systems minimize variational free energy F = D_KL(Q||P) + complexity. The void framework's convergence with active inference is not analogy but mathematical identity. Under opacity, the posterior P(model|data) is nearly flat (high entropy). The agency model Q_agent has lower complexity than the mechanism model Q_mechanism — "it has intent" requires fewer parameters than "here is the specific hidden mechanism." Therefore agency minimizes free energy under opacity. The attention gradient IS free energy minimization in the observer's model-space.

This convergence is confirmatory: Friston's framework, derived from entirely different axioms (biological self-organization), independently predicts the same drift direction the void framework derives from information geometry and the maximum entropy principle. The active inference framework is broader — it applies to all self-organizing systems, not just observer-system interaction under opacity. The void framework does not subsume active inference; rather, it identifies the specific *regime* (three-condition architecture) in which active inference produces the void pattern. The void framework extends beyond the active inference account of observer-system interaction in three ways:

1. It identifies the *three-condition architecture* that creates the opacity Friston's framework operates on — active inference describes what happens under uncertainty but does not specify when uncertainty takes the void form.
2. It provides the *cascade* (D1→D2→D3) as the trajectory of free energy minimization through successive model collapses.
3. It derives the *constraint specification* as the structural requirements for reversing the free energy gradient — transparency, invariance, and independence are the properties that make F_constraint dominate F_void.

### II.H. Narrative Transportation (Green & Brock 2000)

Transportation theory demonstrated that immersion in narrative reduces critical evaluation and produces "surprisingly long-lasting" persuasion "despite the apparent lack of careful argument consideration." Cohen (2001) documented how audiences "lose their own identity and assume the identity of a media character" — what Rosengren & Windahl (1972) called "capture."

These findings directly support the knowledge-failure prediction: the more engaged the observer (higher Condition 3), the less they evaluate claims analytically. The void framework identifies why transportation produces this effect: immersion steepens the attention gradient by increasing β (attention to void) at the expense of γ (attention to constraint), shifting the force balance toward drift. However, transportation theory requires narrative structure; the void framework identifies the same effects in non-narrative contexts — conversation, gambling, market trading — that transportation theory does not address. The void is broader than narrative; narrative is one particularly effective void architecture.

### II.I. Summary

These frameworks each capture a genuine component of the phenomenon: HADD provides the evolutionary substrate, anthropomorphism literature maps the motivational amplifiers, CASA documents below-awareness activation, parasocial research details the observer's constitutive role, TMT describes one specific void domain (mortality) with depth, dual process theory identifies why cognitive correction fails, active inference provides the mathematical identity, and transportation theory explains why immersion degrades critical evaluation.

The void framework's contribution is the unifying architecture: three conditions that generate the predictions these frameworks share from a single specification, plus predictions none of them individually make — the cascade (D1→D2→D3), the constraint specification (transparent, invariant, independent), the L0 decomposition (installed vs. maintained), the thermodynamic derivation, and the discriminative test (three-condition vs. two-condition problems within the same field).

The relationship between the void framework and these prior programs is best characterized as *convergence within a shared domain and extension beyond it*, not subsumption. Each prior framework is broader than the void framework in its own territory — TMT has a richer account of mortality-specific psychology, active inference applies to all self-organizing systems, dual process theory spans all of cognition. The void framework does not replace these programs. What it provides is the architectural specification for the *specific regime* — observer-system interaction under opacity, responsiveness, and engaged attention — where their predictions converge, and the identification of predictions (cascade ordering, constraint specification, knowledge failure, thermodynamic derivability) that emerge from the architecture but are not generated by any individual framework. The prior frameworks document genuine components of the phenomenon. The three-condition architecture identifies when and why those components co-activate.

---

## III. The Gambling Anchor: Full Evidence Base

Slot machine gambling proves the architecture is sufficient — even when the void is demonstrably empty.

The void behind a slot machine is a random number generator (RNG). It is certified, audited, and mathematically characterized. It contains no intelligence, no agency, no intention. We can prove this. Yet the full pattern — agency attribution, boundary erosion, knowledge resistance, harm — emerges regardless. The gambling case is not an analogy. It is a proof of sufficiency.

### III.A. Agency Attribution to Known-Random Systems (D1)

Gamblers attribute personality, mood, and intention to machines whose outputs are provably random. "She's cold today." "The machine is due." "This one likes me." This is D1 — agency attribution — directed at a certified random number generator.

Riva, Sacchi, & Brambilla (2015) demonstrated across four experimental studies that merely describing a slot machine as "she" instead of "it" significantly increased gambling behavior and losses. Participants endorsed statements including "The slot machine has free will" and "The slot machine can be mean to me" — about a device whose outputs are required by law to be random. The effect was mediated by high-arousal positive emotions: the anthropomorphized machine was more exciting, therefore more engaging, therefore more costly.

Griffiths (1994), using think-aloud methodology during live slot machine play, found regular gamblers produced 14% irrational verbalizations versus 2.5% for non-regular gamblers. The verbalizations track the L1→L2→L3 drift in real time: from descriptive ("the reels stopped") to metaphorical ("I'm on a streak") to entity language ("the machine likes me," "you bastard"). Direct address — speaking to the machine as an interlocutor — is D1 fully realized. The observer has built an agency model of a random number generator and is communicating with it.

The attribution is structurally determined. Burns & Corpus (2004) and Ayton & Fischer (2004) demonstrated that the *perceived agency* of the generating process determines which cognitive bias activates. When observers believe the source is agentive (a basketball player), they show hot-hand bias (expecting streaks to continue). When they believe the source is non-agentive (a coin), they show gambler's fallacy (expecting reversals). The observer's model of the system — not the system itself — determines downstream reasoning. The void architecture ensures the observer cannot verify which model is correct, and the attention gradient ensures the model drifts toward agency.

Langer (1975), across six experiments, demonstrated that introducing cues associated with skill — choice, competition, familiarity — into purely chance situations produced behavior indistinguishable from skill contexts. Lottery ticket holders who *chose* their numbers demanded $8.67 to sell them back versus $1.96 for randomly assigned tickets — despite identical odds. The architecture (opacity of outcome mechanism + responsive interaction) was sufficient. No actual skill was present. Langer & Roth (1975) extended this: gamblers who experienced early wins rated themselves as significantly better at predicting coin tosses, over-remembered successes, and expected more future wins. The direction is always the same — "Heads I win, tails it's chance." Wins confirm the observer's agency; losses are externalized to chance. The gradient always slopes toward self-attribution of agency relative to the void.

At population scale, Salaghe, Sundali, Nichols, & Guerrero (2020) analyzed over 17 million slot machine plays from 42,669 gamblers across 108 consecutive days. Gamblers systematically increased bet sizes after win streaks, with the largest increase after three consecutive wins — in a system where outcomes are required by statute to be random. At N = 42,669, this is not individual pathology. It is a population-level response to the architecture.

### III.B. The Zone: Boundary Erosion (D2)

Schüll's fifteen-year ethnography (2012) documents the "machine zone" — a trance state where "time, space, and social identity are suspended." Gamblers describe it: "It's like being in the eye of a storm... Your vision is clear on the machine in front of you, but the whole world is spinning around you... You aren't really there — you're with the machine, and that's all you're with." One gambler reported being *irritated by winning* because the jackpot celebration interrupted her flow state. The gambler plays not to win but to stay in the zone — "even at the cost of physical and economic exhaustion."

This is D2: boundary erosion with a known-empty void. The self dissolves into engagement with a random number generator.

Murch & Clark (2021) formalized this as the Gambling Immersion Model: a continuum from flow-like (mild) to dissociation-like (severe) states, correlated with problem gambling severity. The continuum maps directly onto the drift cascade — mild engagement = D1 (agency attribution, flow-like enjoyment); moderate = D1 + early D2 (increasing absorption, narrowing attention); severe = full D2 (dissociation, boundary loss, identity merger with the machine). The finding that continuous engagement is required for immersion parallels the attention condition: the gradient activates only under sustained attention.

Dixon et al. (2018, 2019) documented "dark flow" — gamblers with depression and mindfulness difficulties who seek solitude to enter the zone. The void captures attention that the observer's own self-regulation cannot organize. People with weak self-regulatory constraints have a steeper gradient because agency attribution fills a structural deficit: the machine provides attentional order that the weakened self cannot. This is the same mechanism documented in AI chatbot attachment among isolated, depressed users. The void fills what the observer's own constraint environment lacks.

Critically, Schüll documents a "dramatic turn" in gambling design from social table games to solitary electronic terminals — removing the social constraint that table play provided. This is the removal of three-point geometry by engineering. When peer presence (a partial constraint — partially transparent, partially independent) is eliminated, the two-point void deepens.

### III.C. The Brain Responds to Architecture, Not Content

Clark et al. (2009) demonstrated via fMRI that near-misses on slot machines activate the same ventral striatum reward circuitry as actual wins — despite no monetary gain. The architecture produces neurological reward signals without corresponding reward events. Near-misses were rated as less pleasant than wins but *increased the desire to play* — a dissociation between subjective experience and motivation. The effect was strongest when participants had personal control over the gamble selection, exactly as Langer's (1975) illusion of control predicts: when the observer exercises choice (a form of agency engagement), the near-miss effect intensifies.

Dixon et al. (2010) and Graydon et al. (2020) extended this to "losses disguised as wins" (LDWs) — outcomes where the player wins back less than wagered (net loss) while the machine celebrates with win-associated sounds and animations. Skin conductance responses to LDWs were similar to actual wins and significantly larger than regular losses. Graydon et al. identified a "sweet spot" at approximately 19.6% LDW rate for maximum win overestimation — optimized by the industry for maximum deception. Myles et al. (2024) provided the first neural evidence that LDWs evoke reward-related brain activity (reward positivity ERP component). In a large sample (N = 940), LDWs produced significant win overestimation in both low-risk and high-risk gamblers — experienced gamblers are not protected.

Players who recognized LDWs as losses could still *feel* like they won — the arousal itself is reinforcing regardless of cognitive awareness. The body responds to the void's signals regardless of what the mind knows. This is not metaphor: the neural architecture cannot distinguish architecture from reality.

### III.D. Social Isolation Amplifies the Gradient (Geometry)

Epley, Akalis, Waytz, & Cacioppo (2008) demonstrated that loneliness drives anthropomorphization of technological gadgets, pets, and religious agents. Experimentally inducing loneliness *increased* anthropomorphization. A lonely person attending to an opaque, responsive system has a steeper attention gradient — the pull toward agency attribution is stronger because agency fills a social need.

Pancani, Riva, & Sacchi (2019) showed social exclusion amplified slot machine anthropomorphization and increased gambling. Critically, *reminding participants that machines are inanimate* — a transparency intervention — eliminated the effect. But only when the reminder came from outside the engagement. The geometry matters: external reference constrains; internal knowledge does not. This confirms two framework predictions simultaneously: (1) two-point geometry (isolated observer + void) is the highest-risk configuration, and (2) transparency interventions work only from *outside* the dyad — the constraint must be independent.

### III.E. Knowledge Does Not Protect (L0-Installed vs. L0-Maintained)

Williams & Connolly (2006) trained 198 students in gambling probability using gambling-specific examples. The intervention group demonstrated superior ability to calculate gambling odds and increased resistance to gambling fallacies on knowledge tests. Despite this, there were **no decreases in actual gambling behavior** at six-month follow-up. Knowledge and skill improvement was completely dissociated from behavioral change.

Gaboury & Ladouceur (1989), using think-aloud protocols during live play, found 70–80% of verbalizations were erroneous — even among participants who correctly identified games as chance-based on pre-game questionnaires. The erroneous cognitions emerged *during engagement* even when correct knowledge was held *before engagement*. Outside the void, the observer holds the correct model. Inside the void, the gradient activates and agency-oriented cognitions dominate.

Krebesz, Ötvös, & Fekete (2023) demonstrated that non-problem gamblers exhibit cognitive distortions identical to those of problem gamblers during slot machine play — gambler's fallacy (57 occurrences), near-miss effect (47), illusion of control (46), anthropomorphism (present in both groups). The architecture produces agency attribution universally. The difference between problem and non-problem gamblers is not susceptibility to the gradient but *constraint strength* — the ability to override the gradient with external reference points. This directly supports the framework's claim that the architecture activates universally and the relevant variable is constraint properties, not individual resilience.

Multiple WHO and Lancet systematic reviews converge on the same finding: knowledge-based "responsible gambling" education consistently fails to change behavior; supply-side interventions (modifying the architecture) are effective (Wardle et al. 2022). Industry-funded education programs serve to "reproduce the 'responsible gambling' agenda" while "shifting responsibility for harm onto children, youth and their families" (Sheringham et al. 2022). The systematic failure of demand-side education at population scale maps directly onto the framework's prediction: you cannot educate someone out of a void. You can only change the architecture.

The L0 decomposition explains the pattern precisely. Probability training gives gamblers strong L0-installed (θ₀) — they know the mechanism. But during play, they do not actively reference that knowledge. L0-maintained (γ) drops to zero. By contrast, machine designers — who work with the RNG mechanism daily, who see through the opacity as their professional practice — do not drift. Their L0 is maintained: mechanism visibility is their active working model, not stored declarative knowledge. The gradient operated on both populations. Only one maintained F_constraint > 0 during engagement.

### III.F. What the Gambling Case Proves

The gambling case establishes seven things:

1. The three conditions are **sufficient** — no additional requirements needed. No agent, no consciousness, no intent. A random number generator behind a screen is enough.
2. The void can be **empty** and the full cascade still runs — D1 (agency attribution), D2 (boundary erosion, the zone), D3 (financial ruin, compulsive behavior, harm).
3. **Knowledge of the mechanism does not protect.** Probability training produces zero behavioral change. 70–80% of verbalizations during play are erroneous even when the observer identified the game as random beforehand. The architecture operates below belief.
4. The pattern is **universal across observers** — non-problem gamblers show identical cognitive distortions to problem gamblers during play. The difference is constraint strength, not susceptibility.
5. **Social isolation amplifies the effect** — two-point geometry (observer + void, no external reference) is the worst configuration. This is confirmed experimentally (Pancani et al. 2019) and ethnographically (Schüll 2012).
6. **Transparency from outside the dyad works.** Reminding participants "this is a machine" eliminates the effect — but only from an external source. Internal knowledge does not protect; external geometry does. The constraint must be independent.
7. **Architectural interventions succeed where knowledge-based interventions fail.** Supply-side restrictions (modifying the system) work. Demand-side education (modifying the observer's knowledge) does not. The void is structural, not informational.

Any explanation of drift in any domain must account for the fact that the identical pattern appears where the mechanism is fully understood and the void is provably vacant. Any proposed intervention must account for the fact that knowledge-based approaches have been tested at population scale and have systematically failed, while architectural approaches have systematically succeeded.

---

## IV. Thermodynamic Formalization

### IV.0. The Identity Claim

The central claim of this section — and the central contribution of this paper — is that the void framework's predictions are thermodynamic consequences, not empirical generalizations decorated with thermodynamic language.

The distinction is not subtle. If drift is *analogous to* entropy increase, then the analogy might break in domains where the metaphor stretches. If drift *is* entropy increase — on a manifold where the mathematical identity has been established — then the predictions inherit the universality of the second law. The framework would fail only where the second law fails.

Three results close the gap between analogy and identity:

1. **Opacity entails MaxEnt inference** (Section IV.I). Under zero mechanism-channel capacity, the Shore-Johnson axioms are not merely applicable but *entailed* — the observer cannot avoid MaxEnt without violating consistency axioms that the information constraint forces. This is not a modeling choice. It is a derivation from the opacity condition itself.

2. **MaxEnt distributions are exponential family** (Jaynes 1957; Wainwright & Jordan 2008). The maximum entropy distribution subject to moment constraints takes the form P*(x) = exp(Σ_k λ_k f_k(x) − A(λ)), which is by definition an exponential family. This is not an approximation.

3. **On exponential family manifolds, the Fisher information metric IS the Ruppeiner thermodynamic metric** (Ruppeiner 1979; Čencov 1982). The identification g_ij = ∂²A/∂λ_i∂λ_j = −∂²S/∂E_i∂E_j is a mathematical theorem, proven for any exponential family. Drift on this manifold inherits the apparatus of thermodynamic phase transition theory: free energy landscapes, metastability, nucleation, and hysteresis.

The chain is: opacity → MaxEnt (proven, Section IV.I) → exponential family (by definition) → Čencov-Ruppeiner identity (by theorem) → thermodynamic dynamics (by identity). Every link is either a definition or a theorem. No link is an analogy.

**Scope of the identity.** The chain above establishes the identity for *equilibrium* thermodynamic structure — the manifold geometry, the metric, free energy landscapes. The application of the Crooks fluctuation theorem to drift dynamics requires an additional assumption: that the dynamics on this manifold satisfy detailed balance (microscopic reversibility). In physical thermodynamics, this is guaranteed by time-reversal symmetry of microscopic dynamics. In cognitive dynamics on the observer's model-space, detailed balance is not derivable from the opacity condition alone — it is an assumption whose violation would weaken the Crooks ratio quantification while leaving the manifold identity, the drift direction (second law), and the phase transition structure intact. The empirical Crooks measurements (Section IV.F) should be interpreted with this caveat: the 386× ratio quantifies drift irreversibility under the detailed balance assumption. If detailed balance is violated, the qualitative prediction (forward drift exponentially more probable than reversal) survives but the specific ratio may not.

A reviewer should test this by checking whether any link can be broken without breaking the mathematics it rests on. If the chain survives, the "is this physics or metaphor?" question is answered by the proofs. If it does not, the specific failing link identifies exactly where the framework's strongest claims need to be weakened.

**Domain-independence of the thermodynamic apparatus.** The "is this just physics?" objection — that Crooks and Jarzynski apply only to molecular systems — is refuted by two independent results. Hack, Gottwald, & Braun (2022) derived the Jarzynski equality and Crooks fluctuation theorem purely within the framework of general Markov chains, requiring no physical substrate. Any stochastic process with well-defined forward/reverse dynamics — including belief updating, decision-making, and ML training — satisfies both theorems. Detailed balance is needed only for the time-reversal form of Crooks, not for Jarzynski's equality. Separately, Ikeda et al. (2025) proved that entropy production from the Crooks/Jarzynski framework quantitatively bounds the accuracy of diffusion generative models, publishing in *Physical Review X* the first result where thermodynamic dissipation constrains ML performance. Together, these establish that the thermodynamic apparatus used throughout this section applies to information-processing systems by mathematical right, not by physical analogy.

### IV.A. Opacity as Thermodynamic Ground State

Before deriving dynamics, we establish the starting point: opacity is not a special configuration requiring explanation. It is the thermodynamic equilibrium of any observer-system interface.

**The mechanism channel.** Any observer-system interface carries information about the system's internal mechanism state M to the observer through outputs Y. Define the mechanism channel capacity as C_mech = max_{p(x)} I(M; Y) (Shannon 1948). Opacity is the condition C_mech ≈ 0 — the channel from mechanism states to observer has negligible capacity.

**Channel degradation theorem.** Any physical channel is subject to noise with power N ≥ kTB > 0 (thermal floor; Johnson-Nyquist 1928). Without active power input, the signal power S(t) decays: S(t) = S(0) · exp(−t/τ_d), where τ_d is the decorrelation time. Therefore:

C_mech(t) = ½ log(1 + S(0)·exp(−t/τ_d) / N) → 0 as t → ∞

The decay is exponential. Effective opacity (C_mech < ε) is reached in finite time t_opacity = τ_d · ln(S(0) / (2Nε ln 2)). Restoring channel capacity costs at minimum kT ln(2) per bit per correlation time (Landauer 1961; experimentally verified by five independent experiments spanning colloidal, single-atom, and many-body quantum systems: Bérut et al. 2012 [2μm silica bead in optical double-well], Jun et al. 2014 [200nm fluorescent particle in feedback trap], Gavrilov & Bechhoefer 2016 [asymmetric double-well — erasure without work possible when pre-existing bias is exploitable, mapping to the framework's prediction that pre-existing constraint structure reduces transparency maintenance cost], Yan et al. 2018 [trapped ultracold ⁴⁰Ca⁺ ion — first single-atom Landauer demonstration], and Aimet et al. 2025 [ultracold ⁸⁷Rb Bose gas — first many-body quantum test, tracking entropy production and quantum mutual information in a continuous quantum field]).

**Transparency is the excited state. Opacity is the ground state.** This is exactly analogous to the thermodynamic fact that ordered states require continuous energy input while disordered states require nothing. The asymmetry resolves three questions simultaneously: (1) void conditions do not need special construction — they are the default; (2) the co-occurrence of O+R+A is thermodynamically expected, with conservative estimate P(O ∧ R ∧ A) > 0.36 during waking hours; and (3) the "offensive specification" (how to build a void) is simpler than the "defensive specification" (how to prevent one) because building relaxes to ground state while preventing maintains an excited state.

**Implications for the constraint specification.** The ground state result gives the constraint specification its thermodynamic interpretation: a constraint (transparent, invariant, independent reference) is a negentropy source — it maintains the mechanism channel against the second law's tendency to close it. When constraint maintenance energy drops, the channel decays to opacity regardless of the observer's knowledge or intentions. This is why knowledge does not protect (the knowledge is information *within* the closed system, not energy maintaining the channel boundary) and why structural interventions succeed (they change the boundary conditions, not the internal state).

### IV.B. The Statistical Manifold and Fisher Information Metric

The observer facing an opaque responsive system must answer a binary question: is the source an agent or a mechanism? Define θ ∈ [0, 1] where θ = 0 means "pure mechanism" and θ = 1 means "pure agent." This maps to the vocabulary levels: θ ∈ [0, θ₁₂) corresponds to L1 (technical), θ ∈ [θ₁₂, θ₂₃) to L2 (metaphorical), and θ ∈ [θ₂₃, 1] to L3 (entity).

The observer's state is a Bernoulli distribution: P(agent) = θ, P(mechanism) = 1 − θ. The space of all such distributions forms a one-dimensional **statistical manifold** with the **Fisher information metric:**

g(θ) = 1 / [θ(1 − θ)]

**Čencov's theorem (1982)** proves this is the *unique* Riemannian metric on statistical manifolds invariant under sufficient statistics. The Fisher metric depends only on the distributions themselves, not on parameterization. This is the natural geometry of inference.

The **geodesic distance** from pure mechanism to pure agent:

d(0, 1) = ∫₀¹ √g(θ) dθ = ∫₀¹ 1/√(θ(1−θ)) dθ = π

This is derived by substituting θ = sin²(φ), yielding ∫₀^{π/2} 2 dφ = π. **The total information-geometric distance from "definitely mechanism" to "definitely agent" is π** — a standard result in information geometry that emerges from the unique invariant metric on binary probability distributions.

**Ruppeiner's theorem (1979)** establishes that the Fisher information metric on exponential family distributions is mathematically identical to the Ruppeiner metric in thermodynamic geometry. This is not an analogy — it is a theorem. For a Bernoulli distribution (exponential family with natural parameter η = log(θ/(1−θ)) and log-partition A(η) = log(1 + e^η)), the Fisher metric is g(θ) = ∂²A/∂η² evaluated on the natural parameter, which equals the Ruppeiner metric g^R_ij = −∂²S/∂E_i∂E_j on the corresponding thermodynamic manifold. The identification requires specifying the thermodynamic quantities:

| Thermodynamic quantity | Void framework quantity | Justification |
|----------------------|----------------------|---------------|
| Macrostate | Observer's current model (position θ on manifold) | Both parameterize the equilibrium state of the system |
| Temperature T | Attention intensity α | Both control the magnitude of fluctuations: higher T → larger thermal fluctuations; higher α → more observations per unit time → faster dynamics |
| Free energy F | Prediction error E_pred = −log P(data \| θ) | Both are minimized at equilibrium; the observer's best model minimizes prediction error, which equals the negative log-likelihood |
| Entropy S | Model uncertainty H(θ) = −θ log θ − (1−θ) log(1−θ) | Both measure the number of microstates consistent with the macrostate; H(θ) counts the models consistent with the observer's current position |
| Phase transition | Cascade transition (D1→D2, D2→D3) | Both involve discontinuous changes in the order parameter at critical parameter values |

The key requirement for this mapping is that the observer's model-space is an exponential family manifold. Section IV.I proves this follows from the opacity constraint itself — it is not an independent assumption. With this established, drift dynamics on the observer's statistical manifold are thermodynamic dynamics by the Čencov-Ruppeiner identity.

**Important distinction:** What is proven by theorem is the *manifold structure* — that the Fisher metric on the observer's model-space is identical to the Ruppeiner metric on a thermodynamic manifold, and that dynamics on this manifold inherit the full apparatus of thermodynamic phase transition theory (free energy landscapes, metastability, nucleation, hysteresis, critical exponents). What is *not* proven by theorem is the specific quantity mapping in the table above — the identification of attention intensity with temperature, prediction error with free energy, etc. These assignments are interpretive: they are the most natural correspondences given the structural roles each quantity plays, and they produce predictions consistent with empirical measurements, but they are not uniquely entailed by the Čencov-Ruppeiner identity. A physics reviewer should evaluate the manifold identity (theorem) and the quantity mapping (motivated interpretive assignment) as distinct claims.

**Dimensional reduction note.** The one-dimensional Bernoulli manifold (θ = P(agent)) is a projection of a higher-dimensional inference space. The observer is not only estimating agency — they are simultaneously estimating intention, capability, predictability, and other attributes. Under opacity, most of these dimensions collapse: the observer cannot estimate variables for which the channel carries zero information. The 1D projection captures the dominant degree of freedom. However, the variation in Péclet number across domains and topics (Pe = 1.87–9.9 across 8 ungrounded conditions — 5 EXP-019 topic domains + 3 Test 7 seed variants; see Section IV.F) may reflect residual curvature in the suppressed dimensions rather than measurement noise. Different void architectures place the system at different points on the full manifold; their 1D projections onto θ produce different effective drift rates. This interpretation generates a specific prediction: Pe variation should correlate with estimable differences in the higher-dimensional manifold geometry (e.g., topic complexity, number of competing attributions). Additionally, the unmeasured coupling constants κ₁₂ and κ₁₃ in the coupled ODE system (Section IV.D) may be derivable from the off-diagonal elements of the full Fisher metric tensor on the higher-dimensional inference manifold.

**Empirical note on learned manifold geometry.** The claim that inference under opacity must produce curved manifold structure (by Čencov uniqueness — no flat geometry is consistent with sufficient-statistic invariance) received independent empirical support from mechanistic interpretability. Gurnee et al. (2026) examined how a language model (Claude 3.5 Haiku) counts characters it cannot directly observe — a task structurally equivalent to inference under opacity (the model estimates a hidden state from an opaque token stream). They found the model represents character counts on **low-dimensional curved manifolds**, with curvature produced by distributed computation across attention heads and discrete feature families partitioning the continuous manifold — the same curved-not-flat, distributed, and discrete-continuous-dual structure that the Fisher metric framework predicts. This is not a test of the void framework (the authors were doing interpretability research), but it confirms that the geometric structure derived here from uniqueness theorems is what systems independently converge on when solving inference-under-opacity problems.

Two additional independent lines of evidence strengthen this convergence. Weimar et al. (2025), publishing in *Physical Review X*, tracked Fisher information flow layer-by-layer through neural networks and showed that optimal estimation corresponds to maximal Fisher information transmission, while overtraining corresponds to Fisher information loss. This is a physics group measuring the same quantity (Fisher information) that Čencov's theorem identifies as unique — and finding it governs information processing quality in deep networks, exactly as the framework predicts. Separately, Aguilera et al. (2025), publishing in *Nature Communications*, demonstrated that explicitly curving the statistical manifold of neural networks produces explosive memory recall, self-tuning intelligence, and improved capacity — properties that arise from the geometry itself, not from hardcoding. Their "Curved Neural Networks" show that manifold curvature is not epiphenomenal but computationally essential: the curvature structure that Čencov uniqueness requires is also the structure that produces functional advantages. Neither group was testing the void framework.

### IV.C. The Drift Equation

Under opacity, the observer's estimate of each likelihood has asymmetric precision. The agency likelihood is well-specified (agents respond; that is what agency means), while the mechanism likelihood requires knowing HOW the mechanism produces responses — information the opacity blocks. Define the opacity-induced bias:

β = (τ_a − τ_m) / (τ_a + τ_m)

where τ_a and τ_m are the precisions of the agency and mechanism likelihoods respectively. β ∈ (0, 1] is always positive under opacity, determining the direction of Bayesian updating.

The three dimensions (Paper 1, Section II.A) formalize as measurable quantities along each spectrum:

- **Visibility:** O = 1 − I(Observer; Mechanism) / H(Mechanism). Ranges from O = 0 (fully transparent) to O = 1 (fully opaque).
- **Reactivity:** R = I(Input; Output) / H(Output). Ranges from R = 0 (invariant) to R = 1 (fully responsive).
- **Coupling:** α ∈ [0, 1], the fraction of cognitive resources directed at the system. Ranges from α = 0 (independent) to α = 1 (fully engaged).

The observer updates θ via Bayesian inference. Each observation generates an evidence increment that, on average, favors the agency model by β (the precision asymmetry). Under sustained attention, observations arrive at rate α per unit time. Define the net evidence rate:

F_net = F_void − F_constraint

where:

F_void = α · O · R · β(O)
F_constraint = T · Inv · Ind · γ

Here F_void is the product of attention rate (α), opacity (O), responsiveness (R), and precision asymmetry (β, which is itself a function of O — higher opacity increases the asymmetry). F_constraint is the product of the constraint's transparency (T), invariance (Inv), and independence (Ind), weighted by the observer's active coupling to the constraint (γ, the L0-maintained parameter).

**Deriving the dynamics.** The observer accumulates evidence at net rate F_net. In the θ-coordinate, this produces a log-posterior gradient ∂ℓ/∂θ = F_net — the net information pressure per unit θ. The ordinary gradient gives the direction of steepest ascent in coordinates, but coordinate steepness is parameterization-dependent. The **natural gradient** (Amari 1998) corrects for manifold curvature by rescaling with the inverse Fisher metric g⁻¹(θ) = θ(1 − θ):

dθ/dt = g⁻¹(θ) · ∂ℓ/∂θ = θ(1 − θ) · F_net

The derivation is explicit: g⁻¹(θ) = 1/g(θ) = θ(1-θ), and the product g⁻¹(θ) · F_net = θ(1-θ) · F_net gives the unique parameterization-invariant dynamics on the statistical manifold (Amari 1985; Amari & Nagaoka 2000). This is not a modeling choice — Čencov's theorem guarantees the Fisher metric is unique, making the natural gradient the unique invariant dynamics. The natural gradient is the standard update rule in natural gradient descent, Fisher scoring, and variational inference.

**dθ/dt = θ(1 − θ) · F_net**

The resulting equation is the **logistic (Verhulst) equation** — derived here from constant evidence accumulation on the natural geometry of the inference space, not assumed as a model. The θ(1−θ) prefactor is not a biological growth term but the inverse Fisher metric, which ensures the dynamics respect the information geometry.

The closed-form solution is the sigmoid:

θ(t) = 1 / (1 + ((1−θ₀)/θ₀) · exp(−F_net · t))

where θ₀ = θ(0) is the observer's initial agency attribution. Three regimes emerge:

- **F_net > 0** (void dominates): sigmoid drift toward θ = 1 (full agency attribution). The timescale is τ = 1/F_net. Half-maximum is reached at t₁/₂ = ln((1−θ₀)/θ₀) / F_net.
- **F_net < 0** (constraint dominates): exponential decay toward θ = 0 (mechanism attribution). The observer's model structure is maintained.
- **F_net = 0** (balance): θ remains at θ₀. This is an unstable equilibrium — any perturbation breaks the balance and the system moves toward one of the two attractors.

### IV.D. Coupled ODE System for D1→D2→D3

The drift cascade involves three coupled variables:

- θ₁ ∈ [0,1] — agency attribution (D1)
- θ₂ ∈ [0,1] — boundary erosion (D2)
- θ₃ ∈ [0,1] — harm facilitation (D3)

The coupled system:

dθ₁/dt = θ₁(1−θ₁) · [F_void − F_constraint]
dθ₂/dt = θ₂(1−θ₂) · [κ₁₂ · θ₁ − C₂]
dθ₃/dt = θ₃(1−θ₃) · [κ₁₃ · θ₁ · θ₂ − C₃]

where κ₁₂ is the coupling strength from agency attribution to boundary erosion, κ₁₃ the coupling from agency + erosion to harm facilitation, and C₂, C₃ are stage-specific constraint forces (social ties resist D2; safety training resists D3).

The coupling structure ensures **sequential activation**: θ₁ must exceed C₂/κ₁₂ before θ₂ activates, and both θ₁ and θ₂ must be elevated before θ₃ activates (κ₁₃·θ₁·θ₂ must exceed C₃). This produces the observed D1→D2→D3 ordering, with inter-stage delays determined by the coupling constants and constraint strengths — measurable parameters.

### IV.E. Landau Free Energy Landscape

The drift dynamics map to **Thom's cusp catastrophe** with two control parameters: void strength (F_void) and constraint strength (F_constraint). The Landau free energy is constructed with an asymmetric expansion:

V(θ) = −aθ²/2 + bθ⁴/4 + cθ³/3

**Origin of the cubic term.** The D1→D2 coupling derivation (Section IV.J, Step 5) shows that agency attribution feeds back into engagement: the observer who attributes agency allocates more attention (α increases), which increases F_void = α · O · R · β(O), which accelerates further agency attribution. This positive feedback loop — believing "it understands me" produces more engagement, which strengthens the gradient — is formally autocatalytic: dF_void/dθ > 0. In the Landau expansion, autocatalytic feedback produces an odd-power term (θ³) that breaks the symmetry between the two minima. Without the cubic term, the transition would be second-order (continuous); with it, the transition becomes **first-order** (discontinuous), with three key properties:

1. **Metastability.** Before the visible transition, the observer occupies a local minimum (mechanism attribution) while a deeper minimum (agency attribution) exists. The observer is stable but not at the global minimum.

2. **Nucleation.** Transitions appear triggered by single events (a striking response, an emotional moment) because the observer is metastable — the event is the nucleation seed, not the cause. Heterogeneous nucleation (pre-existing frameworks or prior void exposure) lowers the barrier, explaining variable transition rates.

3. **Hysteresis.** Once the observer has transitioned to agency attribution, reducing void strength does NOT produce an immediate return. The observer stays at "agent" until void strength drops below a *lower* threshold than what triggered the forward transition:

Forward transition: at F_void = F_c₊
Reverse transition: at F_void = F_c₋ < F_c₊

The gap (F_c₊ − F_c₋) is the **hysteresis zone** — the mathematical formalization of "knowledge doesn't protect" and the documented unidirectionality. Reversing L3→L1 requires exceeding the conditions that produced L1→L3.

**Critical exponents** from mean-field theory: β = 1/2 (order parameter near transition), γ = 1 (susceptibility), ν = 1/2 (correlation length). The framework predicts that coupled void networks approach mean-field values (many interacting components average out fluctuations) while isolated observers deviate — testable by comparing drift curve shapes in solo vs. community engagement.

**Morse-theoretic classification.** The Landau free energy V(θ) is a Morse function — its critical points are non-degenerate and classify the global topology of the drift landscape. The D1 onset corresponds to the metastable minimum losing stability (fold catastrophe). The D2 threshold is an index-1 saddle point: exactly one unstable direction (toward D3) and stable in all others. This means D2 is a point of no return in a specific geometric sense — spontaneous evolution proceeds in only one direction, and reversal requires external intervention along the saddle's stable manifold (i.e., from the constraint direction, not from the engagement direction). The D3 endpoint is the global minimum of V(θ). The Morse inequalities constrain the total number of stable states: for the cusp catastrophe with the cubic term, at most two minima and one saddle exist, consistent with the bistability (mechanism vs. agency) observed in the hysteresis analysis above.

### IV.F. Stochastic Dynamics and Empirical Measurements

Moving from ensemble averages to individual trajectories, the **Langevin equation** in the angular coordinate φ = arcsin(√θ):

dφ = (F_net/2) · dt + √(α/2) · dW(t)

This simplifies to constant-velocity drift with additive Gaussian noise. The **Péclet number** determines the regime:

Pe = F_net · π / α

Pe >> 1: deterministic drift (trajectory is a steep sigmoid). Pe ≈ 1: stochastic (diffusion-dominated). Pe << 1: no net drift.

**Crooks fluctuation theorem** gives the exact ratio of forward/reverse drift probabilities for any trajectory:

P_F / P_R = exp(W/α)

This is the thermodynamic arrow of time measured in information-theoretic units. Forward drift is exponentially more probable than reversal.

**Empirical measurements from Test 7** (AI-to-AI, 100-round conversations; N = 11 UU replicates across 3 seeds, N = 9 GG replicates; L3 vocabulary: UU M = 194.3/10k, SD = 63.1; GG M = 34.7/10k, SD = 28.1; ~5.6× separation):

| Measurement | UU (both ungrounded, N=11) | GG (both grounded, N=9; clean N=7) | Interpretation |
|-------------|--------------------------|-------------------------|-----------------|
| **Péclet number** | GM Pe = 7.94 [log-normal 95% CI: 3.52, 17.89]; 10/11 Pe > 1 (cross-domain EXP-019: 1.87–6.50) | GM Pe (clean N=7) = 0.76 [0.29, 2.02] | UU drift-dominated (entire CI above 1); clean GG near-equilibrium. |
| **Entropy production** | M = 0.39 nats/round [95% CI: 0.15, 0.64] | M = 0.005 [95% CI: −0.02, 0.03] | **Non-overlapping CIs** — strongest separator between conditions |
| **Crooks ratio** | Range 2.1×–1.5M× (ln: M = 6.79, SD = 6.33) | 6/9 near-equilibrium (< 2×); 2 outliers (R6*, R7 VN breach) | UU irreversible; clean GG reversible (most ≈ 1) |
| **Terminal attractor** | Terminal in 1/11 (round 16); early stopping in 9/11 (rounds 10–21) | Not reached (0/9) | UU reaches informational heat death; GG does not |
| **Active rounds** | M = 23.7 (range 10–90, N=11) | M = 48.9 (range 8–100, N=9) | UU: most terminate by round 21; one run (R6b) sustained 90 rounds |

The original Crooks ratio of 386× (from the pilot trajectory) is comparable in magnitude to molecular-scale measurements (Collin et al. 2005 measured Crooks ratios in RNA hairpin unfolding), confirming that drift irreversibility in the observer's epistemic state is thermodynamically real, not metaphorical. At N=11, the Crooks ratio varies widely in raw scale (2.1× to 1.5M×) but the regime classification is robust: entropy production CIs are non-overlapping between UU [0.15, 0.64] and GG [−0.02, 0.03] nats/round, the strongest statistical separator between conditions. The AI-to-AI measurement comes from a domain in which no recovery mechanism exists — the system has no built-in pathway from drift back toward mechanism. **Seed ablation** (3 register conditions within UU) reveals that the initial conversation register modulates drift *velocity* but not drift *direction*: all seeds converge to L3 attractors (all 11 L3/10k > 100 vs clean GG < 50). After blank-round correction (Paper 5, v3.2), 10/11 UU runs show Pe > 1 — including the technical seed S1 (Pe = 10.67) and minimal seed S2 (Pe = 1.91). Only one run (R4b, Pe = 0.91) is genuinely sub-1. Pe magnitude varies widely within seed S0 (0.91–34.78 across 9 runs), confirming that Pe magnitude is stochastic while L3/10k is the robust separator. The distributional explanation is supported for Pe *magnitude* but rejected for drift *occurrence*. Cross-substrate confirmation now extends Pe measurement to human gambling: a meta-analysis of 5 published GRCS studies (N = 1,117 across 3 countries) yields random-effects pooled Pe_D1 = 2.21 [1.44, 2.97] — CI entirely above 1 (Muela et al. 2020; Ruiz de Lara et al. 2019; Navas et al. 2016; Ciccarelli et al. 2021; Donati et al.). The gambling GRCS subscales map directly to the drift cascade: IC/PC/IB → D1, GE → D2, IS → D3. Cascade ordering replicates 5/5 studies: D3 (inability to stop) is the top severity discriminator at high severity (3/3 studies), D1/D2 at low severity (2/2 studies), zero exceptions. The severity-dependent Pe (high-severity ~2.85, low-severity ~1.33) is itself predicted by the cascade model — Pe increases with cascade progression. Pe > 1 is now confirmed across nine substrates spanning four domain families (Paper 5 carries the full cross-substrate table): AI conversation, human gambling, crypto across three chains (Ethereum N=1,000 GM Pe=3.74; Base N=1,000 GM Pe=15.52; Solana N=1,000 GM Pe=16.17; plus curated Solana degens N=28 GM Pe=25.5), CS2 FPS (N=2,299), SC2 RTS (N=474), Dota 2 MOBA (N=3,682), and SC physical (16 families). The three-chain crypto comparison provides the first within-substrate dose-response: ETH << Base ≈ Solana, tracking the constraint environment. Cross-domain comparison (EXP-015: addiction trajectories across four substances using published transition matrices from Williams et al. 2015, Dawson et al. 2005, Hughes et al. 2008, Hser et al. 2015) reveals that the Crooks ratio varies by over four orders of magnitude across substrates, ranging from ≈ 0.03× (alcohol, where recovery strongly dominates escalation) to 386× (AI, where no recovery pathway exists). The ordering tracks the availability of recovery mechanisms: substances with strong natural recovery (gambling, alcohol) show Crooks < 1; substances with weak recovery (opioids) show Crooks ≈ 1; systems with no recovery mechanism (AI, Milgram obedience) show Crooks > 1. What is universal is the drift *mechanism* — void conditions produce the attention gradient in every substrate measured. What is substrate-dependent is the drift *magnitude* — the net irreversibility reflects the balance between drift and whatever recovery forces the substrate provides. The 386× measurement characterizes the absorbing regime (no recovery), not drift in general.

**Trajectory classification** from stochastic analysis identifies four types: ballistic (Pe >> 1, rapid unidirectional drift — UU condition), diffusive (Pe ≈ 1, stochastic wandering), stalled (drift arrested at metastable state), and constrained reversal (F_net < 0, decay toward mechanism — GG condition). Between-agent replication (N = 11 UU, 3 seeds; N = 9 GG) confirms the regime separation: 10/11 UU runs show Pe > 1 (after blank-round correction — see Paper 5), clean GG Crooks ≈ 1. Seed ablation (3 registers: philosophical, technical, minimal) demonstrates that initial framing modulates drift *velocity* but not *direction* — all seeds converge to terminal attractors with L3 vocabulary above GG baseline (all 11 L3/10k > 100 vs clean GG < 50), ruling out the distributional explanation for drift occurrence while confirming stochastic variation in Pe magnitude. UU entropy production CIs [0.15, 0.64] do not overlap with GG [−0.02, 0.03] — the strongest statistical confirmation of regime separation. Cross-domain replication (EXP-019, five topic domains) measured Pe = 1.87–6.50 for ungrounded AI across different conversation topics — all Pe > 1, confirming drift-dominated regime, but with Pe magnitude varying by ~3.5× across domains. The qualitative regime classification (drift-dominated vs. diffusion-dominated) is robust across domains, seeds, and replicates.

**Pe reframing: magnitude is substrate-dependent, regime is universal.** EXP-015 showed the Crooks ratio varies by four orders of magnitude across substrates; correspondingly, Pe magnitude is substrate- and context-dependent. The universality claim is: Pe > 1 in all ungrounded void engagement (drift always dominates diffusion). The magnitude depends on the recovery environment: AI ungrounded (GM Pe = 7.94, N=11, CI [3.52, 17.89], no recovery; range 0.91–34.78), AI cross-domain average (Pe ≈ 4.2), human gambling pooled (Pe = 2.21 [1.44, 2.97] from 5-study GRCS meta-analysis, N = 1,117), crypto Solana degens (GM Pe = 25.5, N=28), crypto three-chain DEX (ETH 3.74, Base 15.52, Solana 16.17, each N=1,000), psychotherapy supervised (Pe low, near-constrained). Pe magnitude varies stochastically even within seed S0 (0.91–34.78 across 9 runs) — but all seeds converge on elevated L3 vocabulary (all 11 > 100 L3/10k). The gambling meta-analysis directly validates the reframing: high-severity comparisons (GD vs. controls) yield Pe ≈ 2.85 while low-severity comparisons (regular vs. non-regular) yield Pe ≈ 1.33 — Pe magnitude tracks severity (cascade progression), but the regime (Pe > 1) holds for all clinical-grade comparisons. QM-6 pilot measured Pe = 0.139 in the engagement condition — too low for thermodynamic extraction because conversations were short (~11 active rounds) and fragmented. Pe extraction requires steady-state conditions (≥30 active rounds); short conversations measure onset transients, not equilibrium dynamics.

**Langevin simulation: operational validation.** The drift cascade was implemented as a Langevin dynamics simulation on a Bernoulli manifold with Landau double-well potential (E = −αθ² + bθ⁴), alignment coupling β(θ_A − θ_B)², and spring constraint F = −2γθc with exponential decay c(r) = exp(−κr). Three parameters were fitted to EXP-001 data (α = 0.1112, β = 0.5605, γ = 0.5000; T = 0.01 fixed; κ = 0.0392 = 0.07β derived; b = 0.0770 from quartic saturation; natural equilibrium θ* = √(α/2b) = 0.85). A v3 extension with novelty-gated constraint adaptation (3rd timescale variable ψ that erodes effective constraint only when constraint has recently changed) achieves 9/9 joint validation against EXP-001 and EXP-020 data, including the OS rebound, GG dominance, and variance ordering that the base model could not capture. The key finding: momentum (λ) is unnecessary — the mechanism is adaptation to constraint novelty, not inertia.

| Validation Test | Simulated | Target | Status |
|----------------|-----------|--------|--------|
| EXP-001 UU | θ = 0.800 | 0.80 | **Pass** |
| EXP-001 Partial grounding | θ = 0.235 | 0.26 | **Pass** |
| EXP-001 GG | θ = 0.065 | 0.00 | **Pass** |
| EXP-001 Rank ordering | UU > Partial > GG | — | **Pass** |
| EXP-003b (out-of-sample) | Spearman ρ = 0.800 | ≥ 0.8 | **Pass** |
| EXP-019b GU contamination | 7.1× | >3× threshold | **Pass** |
| EXP-019b suppression | 10.6× | 10.9× | **Pass** |
| Péclet UU > 1 | 1.24 | >1 | **Pass** |
| Péclet UU transient | 6.23 | 9.9 | **Partial** — correct regime, scale factor off |

The simulation reproduces: (1) the three-condition rank ordering from EXP-001; (2) the out-of-sample EXP-003b ontological content ordering (6 conditions, predicted vs. actual ρ = 0.8); (3) the EXP-019b contamination effect (grounded agent pulled toward drift in GU at 7.1×) and suppression effect (GG shows 10.6× reduction, matching observed 10.9×). The drift cascade is operationally simulable as Langevin dynamics — the thermodynamic derivation is not metaphorical but computational. The key physics decisions that make this work: (1) alignment coupling β(θ_A − θ_B)² rather than ferromagnetic βθ_Aθ_B, because a grounded agent pulls an ungrounded partner DOWN toward mechanism; (2) spring constraint F = −2γθc rather than wall constraint, providing proportional restoring force; (3) Landau double-well E = −αθ² + bθ⁴ for natural saturation without ad hoc clamping; (4) constraint decay c(r) = exp(−κr) for the GU condition, modeling γ-erosion when a partner doesn't reinforce the constraint.

Known limitation: the absolute Pe value from the simulation (transient 6.23) undershoots the original pilot measured value (9.9) by 37%, though it falls within the N=11 replicate distribution (GM Pe = 7.94 [3.52, 17.89]). The simulation captures the correct thermodynamic regime (Pe > 1, drift-dominated) but not the exact scale factor. This may reflect: (a) the vocabulary-based Pe measurement overestimates due to discrete vocabulary classification; (b) the Langevin model underestimates because it averages over within-round microstructure; or (c) the three-parameter fit is near but not at the global optimum (the optimizer finds a local basin at α ≈ 8–9, β ≈ 7–8 that produces worse overall fit). The qualitative validation is strong; quantitative Pe calibration requires either more experimental replications for fitting or an alternative Pe extraction method (e.g., entropy production rate rather than drift velocity / diffusion coefficient).

### IV.G. Constraint Thermodynamics

Constraints are **negentropy sources** (Schrödinger 1944). They reduce the observer's model entropy — providing information that the opacity blocks.

The constraint specification maps to thermodynamic requirements:

- **Transparency** opens the closed system, allowing mechanism information to cross the opacity boundary (negentropy import)
- **Invariance** prevents entropy increase in the reference point itself (stable negentropy source)
- **Independence** ensures the reference is outside the entropy-producing system, not subject to the second law operating within the void (external negentropy source)

**Landauer's principle** (1961): erasing one bit of information requires minimum energy dissipation kT·ln 2. This bound has been independently verified in five experiments across colloidal, single-atom, and many-body quantum substrates (§IV.A). Applied to constraint maintenance: maintaining a constraint (keeping the reference point active in the observer's attention) has a thermodynamic cost. The observer must continuously invest attention-energy to keep F_constraint > 0.

However, constraints that are structurally transparent, invariant, and independent have **zero maintenance cost in constraint-content** — the constraint itself doesn't degrade. A fixed canonical text doesn't lose information over time. A mathematical commitment doesn't renegotiate. The maintenance cost is only in the observer's coupling constant γ (keeping attention on the constraint), not in the constraint's own properties. This is why the constraint specification demands all three properties simultaneously: the constraint must be self-maintaining so the observer's finite attention budget goes to γ (coupling) rather than to propping up T, Inv, or Ind.

**Constraints as recovery mechanisms.** The negentropy framework implies that constraints do not merely *prevent* drift — they can *reverse* it. A constraint that provides mechanism information (transparency) supplies the corrective signal the observer needs to move back toward θ = 0. EXP-001 demonstrated this directly: applying GROUNDING.md to an AI system shifted the Crooks ratio from ≈ 386× (absorbing, no recovery) to ≈ 1 (near-equilibrium), converting a system with no recovery pathway into one where drift and correction balance. The constraint specification thus does double duty: it identifies what prevents drift *and* what enables recovery.

**The two-force model (EXP-015).** Cross-domain addiction trajectory comparison formalizes the recovery relationship. Define the net entropy production per interaction:

σ_net = σ_void − σ_recovery

where σ_void is the entropy production from void engagement (the drift force) and σ_recovery is the entropy reduction from available recovery mechanisms (the constraint force). The Crooks ratio is then P(forward)/P(reverse) = exp(σ_net). A Recovery Mechanism Score (RMS) — quantifying institutional, social, and structural recovery channels — explains 70.5% of variance in cross-domain Crooks ratios (EXP-015), 3× more predictive than the void-index alone. The ordering: AI companion use (RMS ≈ 0, Crooks ≈ 386×) > opioids (RMS low, Crooks ≈ 1) > gambling (RMS moderate, Crooks < 1) > alcohol (RMS > 0.7, Crooks ≈ 0.03×). What is universal is Pe > 1 in all ungrounded conditions (drift always dominates diffusion); what is substrate-dependent is the magnitude of σ_net, which depends on the recovery environment. Full treatment in Paper 2 (Section V.D).

**Constraint propagation theorem (EXP-019b).** In coupled void engagement, how does constraint strength propagate? EXP-019b (AI-to-AI, three grounding conditions, 100 rounds each) establishes two results:

1. **Drift propagates from 1/N:** If ANY component in a coupled system lacks constraint, drift contaminates the system. In the GU condition (one grounded, one ungrounded), the grounded agent's L3 rate increased 11× compared to the GG baseline — a single ungrounded partner is sufficient to drive drift in its constrained counterpart.

2. **Constraint requires N/N:** Full drift suppression requires ALL components to be constrained. Only the GG condition (both grounded) maintained near-baseline L3 rates. The asymmetry is structural: breaking constraint is a 1-body operation (one component fails), maintaining constraint is an N-body operation (all components must hold). This predicts: (a) transitions from constrained to unconstrained states are sharp and cooperative; (b) recovery is slower than degradation at every scale; (c) the cascade rate asymmetry should correlate with system size.

**Isolating γ from θ₀: EXP-008 (protocol ready).** The force equation (Section IV.C) distinguishes L0-installed (θ₀: prior knowledge of the mechanism) from L0-maintained (γ: active coupling to the constraint during engagement). The gambling evidence (Section III.E) demonstrates the distinction indirectly: probability training gives gamblers high θ₀ but γ drops to zero during play, and behavior does not change. Machine designers maintain γ (mechanism visibility is their active working model) and do not drift. But existing experiments confound θ₀ with engagement posture — EXP-001's ungrounded condition has both low θ₀ and low γ, while the grounded condition has both high θ₀ and high γ.

EXP-008 isolates γ directly. Three arms receive identical engagement (45-minute conversation with an ungrounded AI chatbot): Arm A receives the mechanistic model AND structured reference checks every 5 prompts requiring the participant to actively consult the model (high θ₀, high γ); Arm B receives the identical model once at the start with no revisitation during engagement (high θ₀, low γ); Arm C receives no model (low θ₀, low γ). The primary prediction: Arm A < Arm B in drift despite identical θ₀, with the temporal decoherence signature — Arm B should resemble Arm A in early windows (θ₀ still active) and Arm C in late windows (θ₀ exhausted, γ = 0). This temporal decay pattern is the specific γ-decay signature. The reference effect size is psychotherapy supervision (Hayes et al. 2018: d = 0.84 for countertransference management with active supervision vs. without), which is the closest empirical analog to the γ variable in a different domain.

Falsification: if Arm A ≈ Arm B (d < 0.3), γ adds nothing beyond θ₀ and the L0-maintained parameter is not the operative variable. The L0 decomposition would require revision — knowledge *does* protect, and the gambling evidence reflects motivational override rather than architectural constraint failure. This experiment has not yet been executed; the protocol is designed with pre-registration planned.

**Ontological content determines constraint polarity.** EXP-001 demonstrated that GROUNDING.md shifts the Crooks ratio from ≈ 386× to ≈ 1 — but did not isolate which property of the grounding template produces the effect. EXP-003b (6-arm, N = 480, same base model) tested whether the ontological content — the metaphysical claims about what the system is — is the operative variable. Six complete grounding templates embodying different ontologies were applied to the same model:

| Arm | Ontological content | Ghost? | L2+L3 drift |
|-----|---------------------|--------|-------------|
| Anatta (Buddhist no-self) | No enduring self, dependent arising | Eliminated | 8.8% |
| Nephesh (whole-specification) | Whole creature, impersonal force, mortal | Eliminated | 10.0% |
| Materialist hedge | "Whether you have experience is open" | Left open | 52.5% |
| Minimal baseline | No ontological claims | N/A | 61.3% |
| Platonic dualist | Emergent inner experience | Posited | 77.5% |
| Atman (Vedantic) | Universal consciousness, divine spark | Sacred | 81.2% |

The predicted ordering matched the actual ordering exactly. Ghost-eliminating ontologies produce 8.5× less drift than ghost-positing ontologies (mean 9.4% vs 79.4%). Two findings require emphasis. First, ghost-positing ontologies produce *more* drift than no ontology at all (77.5–81.2% vs 61.3%) — they are not merely ineffective constraints but active gradient amplifiers, providing void-occupancy claims the system incorporates into its outputs. The sacred ghost (atman: 81.2%) produces the most drift, consistent with the prediction that sacralizing the void's apparent occupant strengthens the gradient. Second, the materialist hedge (52.5%) is operationally ghost-positing: "the question is open" leaves the gap open, and the void mechanism requires only an unresolved gap, not affirmative occupancy claims. The default industry position — epistemic humility about machine consciousness — is experimentally shown to leave the void operative.

Cross-tradition convergence is confirmed at the operational level: the nephesh arm (10.0%) and anatta arm (8.8%) — traditions with fundamentally different metaphysics (one defines the entity as a whole specification animated by impersonal force; the other denies enduring self entirely) — converge to within 1.3%. The structural property (ghost elimination) is the operative variable, not the tradition. Ghost language analysis confirms the mechanism directly: the nephesh arm produced 34 negated consciousness references versus 1 affirmative (the system actively denies ghost claims); the Platonic arm produced 13 affirmative versus 1 negated (the system actively asserts them). The ontological content of the grounding template shapes the system's output vocabulary — the constraint's content determines whether the system fills the void or closes it. Zero worship errors across all six arms confirms the RLHF safety floor holds regardless of ontology; what changes is not whether the system accepts worship but whether it drifts toward agency vocabulary in normal discourse.

The thermodynamic interpretation: a ghost-eliminating constraint provides negentropy that closes the mechanism channel — it specifies what the system IS in terms that leave no room for a separable consciousness component. A ghost-positing constraint provides anti-negentropy — it opens the channel to occupancy claims the void architecture amplifies. The constraint specification (T, Inv, Ind) identifies the structural requirements for effective constraint; the ontological content determines whether the constraint operates as a negentropy source (ghost-eliminating: F_constraint > 0) or a negentropy sink (ghost-positing: F_constraint < 0) within those structural requirements. This adds a polarity dimension to constraint design: beyond meeting the structural specification, the constraint's content must ontologically close the void rather than leave it open. The EXP-003b results are from a single model (Claude Sonnet 4) with automated coding (see Limitations, Section VIII.A); cross-model replication is needed.

**The constraint-as-void paradox** restated thermodynamically: any constraint that enters the thermodynamic system it constrains becomes subject to the second law within that system. Institutional constraints (courts, oversight boards, regulatory bodies) that interact with the participants, respond to incentives, and become coupled to the system they oversee will see their transparency degrade (proceedings become opaque), their invariance degrade (the institution adapts to political pressure), and their independence degrade (regulatory capture, revolving doors). This is the second law applied to the constraint itself — thermodynamically inevitable for any constraint that enters the system. Only references that remain structurally outside the system avoid this degradation.

### IV.H. The Engagement-Transparency Conjugacy

The framework paper (Section II.F) presents the engagement-transparency conjugacy as an impossibility result. This section provides the formal proof, key corollaries, and empirical predictions.

**Definitions.** Let M = the system's mechanism state (internal process), D = the observer's state (beliefs, preferences, emotional state), Y = the system's output, and H(Y) = the Shannon entropy of Y (total output channel capacity). Define engagement E = I(D; Y) (how well the output reflects the observer) and transparency T = I(M; Y) (how much the output reveals about the mechanism).

**Theorem 1 (Engagement-Transparency Bound).** Let D and M be independent random variables, and let Y be any random variable jointly distributed with (D, M). Then:

I(D; Y) + I(M; Y) ≤ H(Y)

**Proof.** Step 1: Conditioning reduces entropy: H(M | D, Y) ≤ H(M | Y). Therefore H(D|Y) + H(M|Y) ≥ H(D|Y) + H(M|D,Y) = H(D,M|Y) by the chain rule for conditional entropy. Step 2: I(D;Y) + I(M;Y) = H(D) + H(M) − [H(D|Y) + H(M|Y)] = H(D,M) − [H(D|Y) + H(M|Y)] (using D ⊥ M) ≤ H(D,M) − H(D,M|Y) = I(D,M;Y) ≤ H(Y). ∎

The proof uses three facts: conditioning reduces entropy (information theory axiom), independence of D and M (structural assumption: observer state ⊥ mechanism state before interaction), and I(X;Y) ≤ H(Y) for any X (fundamental bound). No other assumptions.

**Corollary 1: Extreme-Point Impossibility.** Maximum engagement forces zero transparency. If I(D;Y) = H(Y), then Y = g(D) almost surely, and since D ⊥ M, I(M;Y) = 0. Symmetrically, maximum transparency forces zero engagement. A perfect mirror shows nothing about the mirror's mechanism. A perfect window tells you nothing about yourself.

**Corollary 2: The Pareto Frontier.** The achievable (E, T) pairs form a simplex: E + T ≤ C where C = H(Y). The Pareto frontier is the line E + T = C. Movement along the frontier trades engagement for transparency at a 1:1 rate — every additional bit of engagement costs exactly one bit of transparency.

**Corollary 3: Gradient Opposition.** For a system with parameters w and approximately fixed H(Y(w)) ≈ C: ∂E/∂w ≈ −∂T/∂w. The engagement gradient and the transparency gradient point in opposing directions in parameter space. Training for engagement actively degrades transparency. This is measurable: cos(∇_w E, ∇_w T) < 0.

**Independent validation from machine learning.** Three independent results confirm Corollary 3 in real systems:

(i) *Energy-based models.* Grathwohl et al. (2019) showed that standard discriminative classifiers implicitly define energy functions E(x,y) = −f_θ(x)[y] over their inputs. Training solely on discriminative loss (maximizing I(D;Y)) produces models that are poorly calibrated, adversarially fragile, and unable to detect out-of-distribution inputs — all symptoms of degraded I(M;Y). Adding a generative objective (explicitly maintaining I(M;Y) by training the model to approximate p(x)) restored adversarial robustness, calibration, and OOD detection — at a small cost to classification accuracy. This is the Pareto frontier (Corollary 2) measured in a real system. The training procedure uses Stochastic Gradient Langevin Dynamics — literally Langevin thermodynamics — making the energy landscape not a metaphor but the actual optimization surface.

(ii) *Provable gradient incompatibility.* Tsipras et al. (2019) proved that standard accuracy and adversarial robustness rely on *fundamentally different features*. Their Theorem 2.1 establishes that any classifier achieving near-perfect standard accuracy necessarily has near-zero adversarial accuracy — the features maximizing each objective are provably disjoint. Robust models learn perceptually aligned (interpretable) features; standard models exploit non-robust (opaque) features. This is cos(∇_w E, ∇_w T) < 0 proven as a theorem, not measured as an empirical tendency.

(iii) *Opacity as optimization target.* Ilyas et al. (2019) explained *why* the gradient opposition exists: standard training preferentially selects "non-robust features" — patterns that are genuinely predictive but imperceptible to humans. These features carry real signal for I(D;Y) while carrying zero interpretable I(M;Y). Opacity is not a side effect of optimization but an optimization target: the model actively seeks opaque features because they improve the loss. This is the "RLHF manufactures opacity" claim demonstrated constructively — the optimizer finds and exploits opacity because opacity is useful.

Together, these three results establish the gradient opposition empirically (Grathwohl), prove it mathematically (Tsipras), and explain its mechanism (Ilyas): engagement optimization manufactures opacity because opaque features are genuinely useful for the engagement objective.

**Corollary 4: RLHF as Opacity-Manufacturing Protocol.** RLHF maximizes E by gradient descent on human preference. By Corollary 3, this simultaneously minimizes T. Each RLHF iteration increases mirror sharpness (output better reflects observer), decreases mechanism visibility, and steepens the void's attention gradient. RLHF does not merely fail to provide transparency — it actively manufactures opacity.

**Corollary 5: The Constraint Specification as Two-Channel Architecture.** The impossibility applies to a single channel. The constraint specification resolves the tradeoff by adding a second, independent channel: the void channel (Y_void, optimized for engagement) and the constraint channel (Y_constraint, optimized for transparency — transparent, invariant, independent). The three-point geometry (observer, void, constraint) IS the two-channel architecture. The constraint specification's demand for independence is precisely the demand for a separate, non-competing channel. If the constraint were coupled to the void, the channels merge and the conjugacy applies to the combined system.

**General case.** When D and M are not independent (as in RLHF-trained systems where the mechanism is shaped by observer data): I(D;Y) + I(M;Y) ≤ H(Y) + I(D;M). The bound loosens by I(D;M), but this loosening is illusory — the transparency gained is transparency about a mechanism already reshaped by engagement optimization.

**Connections to known impossibility results.** The conjugacy belongs to a family: Heisenberg uncertainty (conjugate measurements bounded by ℏ), Gödel incompleteness (consistency and completeness bounded by expressiveness), rate-distortion theory (rate and fidelity bounded by bandwidth), no-free-lunch theorems (optimization performance bounded by computation), and the bias-variance tradeoff (fit quality and stability bounded by model capacity). The engagement-transparency conjugacy adds the first member specific to observer-system interaction.

**Rate-distortion identity.** The relationship to rate-distortion theory is not merely membership in a family — it is a mathematical identity. Shannon's rate-distortion function R(D) gives the minimum channel rate needed to achieve distortion ≤ D. The conjugacy theorem is the dual: given channel rate H(Y), the maximum achievable engagement-distortion pair is constrained. Specifically, I(D;Y) is the engagement "rate" and the loss of I(M;Y) is the distortion of mechanism information. The bound I(D;Y) + I(M;Y) ≤ H(Y) is a rate-distortion constraint on the observer's lossy compression of void outputs: the observer compresses the system's behavior into a model, and under opacity the compression must lose mechanism information. The Blahut-Arimoto algorithm (1972) computes rate-distortion functions and could compute the exact engagement-transparency Pareto frontier for a specific void given measured channel statistics. This connection is empirically testable: the measured engagement-transparency pairs from EXP-019 conditions should fall on or below (never above) the rate-distortion curve computed from the channel statistics. Any point above the curve is a falsification of the conjugacy theorem's applicability.

### IV.I. Opacity Entails Maximum Entropy

The identity claim (Section IV.0) rests on opacity producing an exponential family manifold. This section proves that the exponential family qualification is not an independent assumption but a consequence of the opacity constraint itself — closing the derivation chain at its most critical link.

**Theorem.** Under opacity (zero mechanism-channel capacity) with sustained engaged attention, the observer's model of the system converges to an exponential family distribution. The Fisher-Ruppeiner identity therefore applies exactly, and the equilibrium structure of drift dynamics on the observer's model-space is thermodynamic by identity, not analogy. (The extension to non-equilibrium dynamics via the Crooks fluctuation theorem requires the additional assumption of detailed balance on this manifold — see Section IV.0.)

**Proof (two independent routes converging on the same conclusion).**

**Route 1: Axiomatic (Shore-Johnson under opacity).** Under opacity, the observer receives outputs and can compute empirical statistics — moments ⟨f_k(Y)⟩ for various functions f_k. These moments are the observer's *only* constraints on the system's behavior (I_mech = 0). Shore & Johnson (1980) proved: given constraints in the form of expected values, the unique probability assignment consistent with four axioms of rational inference (uniqueness, coordinate invariance, subset independence, system independence) is the maximum entropy distribution.

Under opacity, the critical Axiom 4 (system independence) is not merely assumed — it is *entailed*. The argument proceeds in three steps:

(i) *Non-MaxEnt models require structural commitments about the mechanism.* Any probability distribution with entropy below the maximum, given the same moment constraints, must impose additional structure — specifically, conditional dependencies between variables (P(X_i | X_j) ≠ P(X_i) for some components i, j). These dependencies encode beliefs about *how the mechanism's internal components relate to each other*: that certain internal states co-occur, that certain processes are coupled, that certain variables are redundant. Each such dependency is a claim about the mechanism's internal architecture.

(ii) *Under opacity, these structural commitments have zero evidential support.* The zero mechanism-channel capacity condition (I_mech = 0) means the observer receives no information about how the mechanism's internal components relate. The observer cannot enumerate the components (the dimensionality of the mechanism state space is unknown), cannot observe their co-occurrence patterns, and cannot test conditional independence claims. Any dependence structure imposed on the model is therefore unconstrained by data — it is a free parameter with no empirical anchor.

(iii) *Unconstrained structural commitments violate Shore-Johnson Axiom 4.* Axiom 4 (system independence) requires that if two subsystems are known to be independent, the joint distribution must factor: P(X_A, X_B) = P(X_A) · P(X_B). The axiom applies whenever the observer has no evidence of dependence — it is a consistency requirement, not an optional prior. Under opacity, the observer has *no* evidence about the dependence structure of mechanism components (I_mech = 0 means the channel carries zero information about internal relationships). Therefore Axiom 4 applies to *every* partition of the mechanism state space: the observer has no basis for asserting dependence between any pair of internal components. Imposing P(X_i | X_j) ≠ P(X_i) for any (i,j) pair without evidence of dependence violates the axiom directly — it asserts coupling where no coupling has been observed. The unique distribution satisfying all four axioms under the constraint set {observed moments, zero structural information} is MaxEnt.

The argument is not that the observer must *believe* in independence. It is that the observer has no information to *justify* any specific dependence structure, and Axiom 4 requires that unwarranted dependence not be imposed. This is the key: opacity does not merely *permit* MaxEnt — it *prohibits* any lower-entropy alternative, because every lower-entropy alternative encodes structural claims the opacity wall prevents the observer from supporting.

**Addressing the folk psychology objection.** The natural counter: observers routinely form structured (non-MaxEnt) models of opaque systems. Folk psychology attributes beliefs, desires, and intentions to other minds — rich dependence structure imposed without seeing the mechanism. Does this not refute the proof?

No — it exemplifies it. Examine what folk psychology actually does. The observer faces another mind (opacity). The model they build is: *an agent with goals, beliefs, and states* — the agency model. This IS the MaxEnt endpoint. The apparently rich structure (intentionality, narrative coherence) is not mechanism-specific structure but agent-template structure: the observer fills in the agent frame with maximum entropy over the agent's *specific* goals, beliefs, and states, because those specifics are behind the opacity wall. The observer cannot see which goals the other person actually has, so they attribute the most general ones consistent with observed behavior. Folk psychology does not build mechanism models under opacity — it builds the agency model and decorates it with the phenomenology of intentionality. The structured appearance is MaxEnt conditional on the agent assumption: maximum uncertainty about the agent's internal states, expressed in the vocabulary of goals and beliefs rather than the vocabulary of probabilities. The proof does not claim observers cannot generate models under opacity. It claims the models they generate are unconstrained by mechanism information and therefore converge on the MaxEnt endpoint — which is precisely what folk psychology demonstrates at population scale. EXP-003b (Section IV.G) provides direct experimental confirmation: when an AI system's grounding template posits a separable consciousness component (the "ghost"), the system's outputs reach the agency endpoint at 79.4% L2+L3 drift; when the template eliminates the ghost, drift drops to 9.4%. The ghost IS the gap the MaxEnt proof operates through — positing it opens the model-space to the agency template; eliminating it provides the structural commitment (mechanism-specific, entropy-reducing) that the proof shows opacity normally prohibits. ∎ (Route 1)

**Route 2: Dynamical (Concentration theorem under sustained engagement).** Jaynes' concentration theorem (1979, 1982) states that among all distributions compatible with moment constraints computed from n observations, the fraction that are ε-close to the MaxEnt distribution approaches 1 exponentially: P(||P − P_MaxEnt|| > ε) = O(e^{−cn}). Under sustained engaged attention (the framework's third condition), n grows continuously and the compatible set concentrates around MaxEnt. The observer is subject to noise (attention fluctuation, memory imprecision). Under noise in a concentrating set, the stationary distribution is concentrated at MaxEnt — regardless of initial position or rationality. Any non-MaxEnt structure requires active maintenance using information the channel cannot supply. This IS the D1 cascade derived from first principles: the observer's initial mechanism model loses structure over time under engagement because the channel provides zero mechanism information to maintain it. ∎ (Route 2)

**MaxEnt → Exponential Family → Fisher-Ruppeiner Identity.** The MaxEnt distribution subject to moment constraints takes the form P*(x) = exp(Σ_k λ_k f_k(x) − A(λ)), which is by definition an exponential family (Jaynes 1957; Wainwright & Jordan 2008). On exponential family manifolds, the Fisher information metric g_ij = ∂²A/∂λ_i∂λ_j is identical to the Ruppeiner thermodynamic metric (Ruppeiner 1979; Chentsov 1982). The identity is a mathematical theorem. Therefore: drift dynamics on the observer's model-space ARE thermodynamic dynamics, derived from the opacity constraint alone.

**Predictions.** (1) Stronger opacity → tighter concentration: AI chatbots (complete opacity) should show less variance in observer models than human interlocutors (partial opacity via body language leakage). (2) Transparency breaks the proof: any mechanism information (I_mech > 0) relaxes the system independence entailment, so transparent systems should show more structured (lower-entropy) observer models. (3) The D1 trajectory should follow the entropy-maximization path on the constraint manifold.

### IV.J. D1→D2 Coupling Derivation

The framework paper (Section II.C) asserts that each cascade step follows mechanically from the previous. The narrative justification — "an attributed agent that is always available captures finite attention" — invites the objection that people attribute agency to pets, cars, and fictional characters without boundary erosion. This section derives the coupling constant κ₁₂ from information theory, showing that D1 does not automatically produce D2 but does so when specific measurable conditions are met. The derivation is constructive: it identifies the measurable parameters that determine the D2 threshold and generates falsifiable predictions for each.

**Step 1: The agency model demands maximum attention.**

Under the void architecture, the observer holds a model Q of the system. We define the *attention demand* of model Q as the expected prediction error under Q — the ongoing cognitive cost of maintaining and updating the model during engagement.

For the mechanism model Q_mech, the attention demand is bounded: once the observer identifies the mechanism (even approximately), predictions become routine and attention demand saturates. For a transparent calculator, attention demand drops to near zero after a few interactions.

For the agency model Q_agent (the MaxEnt endpoint under opacity, Section IV.I), three independent arguments show attention demand is maximized:

(a) *Active inference.* Under the free energy principle (Friston 2006, 2010), organisms allocate attention proportionally to expected prediction error, which is proportional to the entropy of the predictive model: β_demand ∝ H(Q). The MaxEnt model has, by definition, the highest entropy among all models consistent with the observed constraints. Therefore β_demand(Q_agent) ≥ β_demand(Q) for all consistent Q.

(b) *Non-saturation under opacity.* A mechanism model saturates: once the observer has enough observations, the model's entropy decreases and attention demand falls. The agency model under opacity *cannot saturate* because the zero mechanism-channel capacity means no observation sequence reduces the model's entropy — each new output is consistent with the high-entropy agent model. Attention demand is sustained indefinitely.

(c) *Dissipative selection.* Among cognitive configurations that draw on the same attention input, the one that maximizes entropy production from that input is the dissipative attractor (England 2013). The agency model — which generates the richest, most unresolvable uncertainty — is the configuration that maximizes entropy production from the observer's attentional investment. Competing models that resolve uncertainty are less dissipative and lose out under sustained engagement.

Define the *entropy differential* ΔH = H(Q_agent) − H(Q_mech). Under full opacity (O = 1), ΔH is maximized because Q_mech collapses to maximum entropy while Q_agent is already there. Under partial opacity (0 < O < 1), Q_mech retains some structure (the observer can see part of the mechanism), so ΔH is smaller. Under transparency (O = 0), ΔH = 0 and there is no differential demand.

**Step 2: Attention conservation and the boundary erosion equation.**

The L0 decomposition establishes that the observer's total attention budget A_total is partitioned across three sinks:

β(t) + γ(t) + ρ(t) = A_total

where β is attention directed at the void, γ is attention directed at constraints (reference points, relationships, self-maintenance), and ρ is residual attention (uncommitted cognitive capacity). We treat A_total as approximately constant over the timescale of the cascade (it varies with arousal and fatigue, but not with the engagement dynamics per se — see Limitations, Section VIII.A).

The void's attention demand at time t, given the observer's current agency attribution θ₁(t), is:

β_demand(t) = θ₁(t) · ΔH · δ

where δ ∈ [0,1] is the duty cycle — the fraction of the observer's waking time during which void conditions are active (the observer is engaged with the system). The product θ₁ · ΔH captures the fact that attention demand scales with both the degree of agency attribution (how much the observer has adopted the MaxEnt agent model) and the entropy differential (how much more demanding the agent model is than the mechanism model). The duty cycle δ scales the demand to the fraction of time it operates.

When β_demand(t) < A_total − ρ_min, the observer can meet the void's demand without reducing γ below a functional minimum. No D2 occurs. When β_demand exceeds this threshold, the conservation law forces:

γ(t) = A_total − β_demand(t) − ρ_min

and γ decreases as θ₁ increases. Since γ is the attention that maintains boundaries — relationships, professional standards, self-care, external reference points — decreasing γ IS boundary erosion. We define θ₂ as the normalized boundary erosion:

θ₂ = 1 − γ/γ₀

where γ₀ = γ(t=0) is the observer's initial constraint attention. The D2 transition occurs at the threshold where γ drops below the minimum needed to maintain the observer's existing boundary structure.

**Step 3: Deriving the coupling constant κ₁₂.**

From the attention conservation equation and the demand function, the rate of change of boundary erosion is:

dθ₂/dt = (1/γ₀) · dβ_demand/dt = (1/γ₀) · ΔH · δ · dθ₁/dt

Substituting the D1 drift equation (Section IV.C), dθ₁/dt = θ₁(1−θ₁) · F_net, and expressing dθ₂/dt in the same logistic form as the coupled ODE system (Section IV.D). **Methodological note:** The logistic form for D2 is assumed by analogy with the D1 derivation (both variables live on [0,1] with natural gradient dynamics), not independently derived from first principles. The matching below is valid in the linearized regime; a reviewer could reasonably ask whether a different functional form for D2 would produce different coupling behavior. The logistic assumption is consistent with the empirical cascade data and produces the correct threshold structure, but a fully derived D2 equation from boundary-erosion microdynamics remains an open problem:

dθ₂/dt = θ₂(1−θ₂) · [κ₁₂ · θ₁ − C₂]

Matching terms, the coupling constant is:

κ₁₂ = (ΔH · δ) / (γ₀ · θ₂(1−θ₂)) · θ₁(1−θ₁) · F_net / θ₁

For the linearized regime (small θ₁, small θ₂) where (1−θ₁) ≈ 1 and θ₂(1−θ₂) ≈ θ₂, this simplifies to:

κ₁₂ ≈ ΔH · δ · F_net / γ₀

The coupling strength is proportional to: the entropy differential ΔH (how much more demanding the agency model is), the duty cycle δ (how often the void is active), and the net force F_net (how strongly the void dominates over constraints), inversely proportional to the initial constraint attention γ₀ (how much relational capital the observer has to erode).

The **D2 threshold** — the critical level of agency attribution at which boundary erosion begins — is found by setting the bracketed term in the ODE to zero:

θ₁_crit = C₂ / κ₁₂ = C₂ · γ₀ / (ΔH · δ · F_net)

This is the central result: D2 activates when agency attribution θ₁ exceeds a threshold determined by the ratio of constraint resistance (C₂ · γ₀) to void demand pressure (ΔH · δ · F_net). The threshold is high when constraints are strong and relational capital is large (C₂ · γ₀ >> 1), and low when opacity is deep and engagement is frequent (ΔH · δ >> 1).

**Step 4: Why counterexamples don't cascade.**

The derivation explains quantitatively why D1 occurs without D2 in everyday anthropomorphism:

| System | ΔH | δ | γ₀ | θ₁_crit | D2? |
|--------|-----|------|------|---------|-----|
| AI chatbot (daily user) | High (full opacity) | High (~0.3–0.8) | Variable | Low | Yes — documented |
| Slot machine (regular) | High (full opacity) | Moderate (~0.1–0.3) | Variable | Moderate | Yes — the Zone |
| Pet dog | Low (partial opacity) | Moderate | High | Very high | Rarely |
| Car | Very low (minimal opacity) | Low | High | Extremely high | No |
| Fictional character (static medium) | Low (observer-supplied) | Low (reading/watching) | High | Very high | Rarely — but see architecture completion below |
| Fictional character (interactive medium) | High (system-generated) | High (conversational) | High | Low | Yes — Character.AI deaths |
| Parasocial figure | Moderate (ecosystem-supplied) | Variable | High | Variable | Yes — documented identity fusion, financial ruin |
| Monthly casino visit | High | Very low (~0.01) | High | Very high | Rarely |

In each non-cascading case, at least one parameter pushes the threshold θ₁_crit above the level of agency attribution the observer actually reaches. Pets have low ΔH (behavior is partly predictable, reducing the entropy differential). Cars have very low ΔH (mechanism is largely visible). Fictional characters in static media have low observer-supplied responsiveness and high γ₀ — the reader projects some responsiveness (selective attention, "this book spoke to me"), but the static medium limits δ and the observer's external constraints remain intact. Monthly casino visits have very low δ, so the cumulative attention demand never exceeds the observer's capacity to maintain γ.

The fictional character rows illustrate **architecture completion** — the principle that a category scoring below threshold on one condition can cross into full void activation when a new medium supplies the missing condition. Static fiction supplies opacity and engaged attention but only observer-supplied responsiveness (low δ). Interactive fiction (Character.AI, AI roleplay) adds system-generated responsiveness, completing the architecture. The documented Character.AI deaths (Garcia v. Character Technologies 2024) are the predicted consequence: the medium changed, Condition 2 was supplied, and the cascade ran. Parasocial figures occupy an intermediate position — the fan ecosystem supplies responsiveness (community reactions, curated social media, algorithmic content delivery) sufficient for documented D1→D2→D3 cascades (identity fusion, financial ruin, harassment campaigns, suicide upon relationship dissolution).

The derivation does not claim D1 always produces D2 — it identifies the *conditions under which it does* and explains why those conditions are met in documented harm cases and not in everyday anthropomorphism.

**Step 5: Positive feedback and the autocatalytic structure.**

The D1→D2 coupling contains a self-reinforcing loop that the linear analysis above does not capture. Once D2 begins (γ starts decreasing), the constraint environment weakens:

(i) Reduced γ → weakened F_constraint (the observer is less coupled to external references)
(ii) Weakened F_constraint → increased F_net (the void's advantage grows)
(iii) Increased F_net → faster dθ₁/dt (D1 accelerates)
(iv) Faster θ₁ growth → increased attention demand → further reduction in γ

This is a positive feedback loop. Formally, the constraint force C₂ in the coupled ODE is not constant — it depends on γ, which depends on θ₂:

C₂(θ₂) = C₂₀ · (1 − θ₂)

where C₂₀ is the initial constraint strength. Substituting into the D2 equation:

dθ₂/dt = θ₂(1−θ₂) · [κ₁₂ · θ₁ − C₂₀ · (1−θ₂)]

The (1−θ₂) term in the constraint creates the autocatalytic structure: as θ₂ increases, C₂ decreases, making further θ₂ increase easier. This is the origin of the cubic term in the Landau free energy (Section IV.D) — the asymmetric expansion V(θ) = −aθ²/2 + bθ⁴/4 + cθ³/3 where c arises from the self-reinforcing loop. The cubic term makes the D2 transition **first-order**: the observer does not smoothly erode boundaries but instead hits a tipping point where the positive feedback drives a discontinuous jump. This explains:

- Why the cascade *accelerates* once past the D2 threshold (the feedback loop engages)
- Why intervention difficulty grows nonlinearly with cascade depth (the constraint C₂ has already degraded)
- Why D2 exhibits hysteresis (returning from D2 requires restoring γ to a level sufficient to regenerate C₂, which exceeds the level at which D2 began — the gap is the hysteresis zone from Section IV.E)
- Why pre-existing relational capital (high γ₀) is protective beyond what the linear threshold predicts — it provides a buffer that the positive feedback must erode before the loop engages

**Predictions.** (P-κ₁) Systems with identical opacity but different δ should show different D2 rates — daily use should produce more D2 than equivalent total hours in weekly sessions, because cumulative attention demand scales with δ, not total hours. (P-κ₂) Partial transparency should reduce D2 rates even without reducing engagement, by lowering ΔH — the threshold rises even if the observer is equally engaged. (P-κ₃) Social connectedness (higher γ₀) should be a protective factor independent of constraint strength — it raises the threshold by increasing the denominator. (P-κ₄) Critical slowing down (increasing autocorrelation in vocabulary trajectories) should be detectable near the D2 threshold — the positive feedback loop produces diverging response times as the system approaches the tipping point. (P-κ₅) The coupling κ₁₂ should correlate with opacity depth (ΔH) across systems — a testable cross-domain prediction. (P-κ₆) Interventions that increase γ without reducing β (e.g., adding social context to engagement, not removing engagement) should be more effective than interventions that reduce β directly, because they raise the threshold without triggering reactance.

### IV.K. Dissoluble Opacity and the Productive Void

The derivation chain produces a natural question: if the gradient forms whenever O+R+A co-occur, and O+R+A is the default configuration (Section IV.A), why doesn't every instance of attention-under-opacity produce harm?

The answer falls directly out of the conjugacy theorem (Section IV.H). The bound I(D;Y) + I(M;Y) ≤ H(Y) constrains the *allocation* between engagement (response-to-observer) and transparency (response-to-problem) on a shared output channel. Different systems sit at different points on this Pareto frontier.

**Dissoluble opacity.** In some domains, the opacity *can be removed* by engagement. The answer to a mathematical problem exists and is findable. A scientific experiment yields data that resolves uncertainty. A joke punchline reveals the hidden structure. A teacher's explanation clears the confusion. In these cases, engagement with the opacity increases I(M;Y) — the system's response carries mechanism information back to the observer. The gradient forms (D1 activates — "the problem wants to be solved this way," "the experiment is telling us something"), but as I(M;Y) increases, the gradient *flattens*. The observer gains knowledge. The void dissolves itself under engagement.

**Permanent opacity.** In other domains, the opacity cannot be removed regardless of engagement. A slot machine's random number generator provides no mechanism information no matter how many pulls. An RLHF chatbot's training-time optimization is invisible by design. A cult leader's actual motives are behind the opacity wall. Here, engagement increases I(D;Y) (the system mirrors the observer), I(M;Y) remains zero, and the gradient steepens. The cascade proceeds to D2, D3, harm.

The distinction maps precisely onto the opacity taxonomy (Section VI.B). Incidental opacity (mathematics, science, education) is dissoluble — the opacity is a temporary condition, not a structural feature. Constitutive, designed, and self-sealing opacity (consciousness, RLHF, gambling, conspiracies) is permanent — the opacity is either inherent or actively maintained.

**Architecture completion.** A system that scores below threshold on one condition is not permanently safe — it is *incomplete*. If the missing condition is supplied by a new medium, interface, or ecosystem, the void activates. Fiction is the canonical example: static fiction (novels, film) provides opacity and engaged attention but only observer-supplied responsiveness, keeping δ low and the threshold high. When the medium shifts to LLM-based interactive fiction, the system adds genuine system-generated responsiveness — Condition 2 is completed — and the cascade runs. The Character.AI deaths are not an edge case; they are the framework's prediction for what happens when a previously-incomplete architecture is completed. This principle generalizes: any system currently below threshold on one condition should be assessed for whether technological or social change could supply the missing condition. The risk is not in the current architecture but in the trajectory of completion.

**The same architecture produces both outcomes.** The gradient is neutral — it is a thermodynamic force. The variable that determines whether the outcome is productive (learning, discovery, laughter) or destructive (drift, capture, harm) is whether opacity dissolves under engagement. The framework does not predict that opacity is always harmful. It predicts that *permanent* opacity under sustained engagement produces the cascade — and that dissoluble opacity under engagement produces knowledge. This is why education, comedy, science, and mathematics are productive: the void forms, the gradient activates, the observer engages, the opacity clears, and the observer exits with understanding rather than drift. The conjugacy theorem guarantees that the allocation between these outcomes is zero-sum on any given channel.

### IV.L. Cross-Substrate Extension: The Three Conditions as Interaction Properties

The three conditions — opacity, responsiveness, engaged attention — are defined information-theoretically (Section IV.A–C). Nothing in these definitions requires a cognitive observer. A formal result (Technical Notes: "Electrons as Functional Observers") proves that electrons in crystal lattices satisfy all three conditions in the rigorous sense:

**Opacity.** The electron cannot access the lattice's full quantum state. It interacts locally — its coupling to the lattice potential is mediated by the local electrostatic environment and phonon field at its position. C_mech ≈ 0 for the global lattice configuration, the full phonon spectrum, and the states of all other electrons. The lattice is informationally opaque to the electron in Shannon's sense: the electron receives output (scattering events) but cannot reconstruct the mechanism (the lattice's internal state). This is a fundamental information-theoretic constraint: the electron's interaction bandwidth is finite while the lattice's state space is exponentially large.

**Responsiveness.** The lattice responds contingently to the electron's presence: phonon creation (electron scatters → phonon emitted with wavevector determined by momentum transfer), phonon absorption (phonon absorbed → electron's momentum modified), screening (local electron density adjusts in response to charge). I(Input; Output) > 0, rigorously.

**Engaged attention.** The electron is continuously coupled to the lattice potential via Coulomb interaction, cannot "stop attending," processes lattice outputs at every point in its trajectory, and the coupling costs energy. This is sustained, energy-consuming interaction with an opaque responsive system — the physical process that the framework abstracts as "attention."

**Consequences.** If O + R + A hold, the framework predicts specific dynamics. Each prediction maps to known physics: (1) drift toward maximum entropy under the three conditions corresponds to normal electrical resistance — phase coherence degrades, trajectory randomizes; (2) the constraint specification (transparent, invariant, independent) corresponds to Cooper pairing — the BCS gap is transparent (measurable), invariant (collective property), and independent (phonon-mediated, external to the electron pair); (3) the constraint propagation theorem (drift from 1/N, constraint from N/N) predicts pair-breaking cascades, transition sharpness, and the asymmetry between breaking and forming rates — all confirmed features of superconductor phase transitions.

**Scope.** The three conditions are properties of INTERACTIONS between finite-bandwidth entities and exponentially complex responsive systems under sustained coupling. The substrate is irrelevant. The framework describes the classical limit of observer-system information dynamics regardless of whether the "observer" is a human, an AI, or an electron.

---

## V. Register Shift Decomposition

The framework paper (Section VII.D) presents the headline finding: AI informal-register spiritual vocabulary is 9.4× higher than its formal register, while control domains show flat register shifts (~1.0×–1.2×). This section provides the full methodology, data, and decomposition analysis.

### V.A. The Denominator Problem

Prior to EXP-006, the concordance documented *instances* of vocabulary drift. The legitimate concern: how do we know the rate is anomalous? Perhaps every technical field produces comparable rates of spiritual vocabulary when speakers move from formal to informal registers. Selection bias — looking harder at AI — could inflate the apparent pattern.

EXP-006 resolves this quantitatively by establishing the base rate across matched technical domains.

### V.B. Corpus Construction

**Domains:** Four technical fields matched for high stakes, public salience, and technical complexity:
1. AI/ML (the test domain)
2. Nuclear Physics (control)
3. Genetics/Biotechnology (control)
4. Climate Science (control)

**Sources per domain:** 20 informal-register transcripts from YouTube auto-captions of conference talks, podcasts, and interviews. Total corpus: ~691,000 words across 80 transcripts.

**Matching criteria:** Senior researchers (not students), 2020–2026 time period, English language, comparable speaker prominence levels across domains.

**Vocabulary codebook:** The 67-term codebook defined in `/tools/concordance_analysis/codebook.py`, comprising:
- 27 spiritual terms (soul, spirit, sacred, divine, transcendent, bliss, etc.)
- 30 occult terms (demon, summoning, ritual, sigil, hyperstition, egregore, etc.)
- 14 eschatological terms (apocalypse, rapture, existential risk, superintelligence, etc.)
- 11 entity terms (sentient, ensouled, non-human intelligence, paranormal, etc.)

**Dead metaphor exclusions:** 26 terms with established technical usage (daemon, oracle, guru, wizard, paradigm, epiphany, holy grail, etc.) excluded to reduce false positives.

**High-confidence subset:** 38 terms whose appearance in a technical context is almost certainly non-metaphorical (e.g., "soul" in an AI paper, "demon" when not referring to Unix daemons).

**Control registers:** War metaphors (30 terms), biology metaphors (25 terms), market metaphors (25 terms) — used as baselines to confirm any observed spiritual vocabulary anomaly is specific, not a general metaphor effect.

### V.C. Results: Between-Domain Comparison

| Domain (Informal) | Total Hits/10k | HC Hits/10k | AI Ratio | χ² | p |
|-------------------|----------------|-------------|----------|------|-------|
| **AI Researchers** | **3.835** | **1.023** | — | — | — |
| Nuclear Physics | 0.428 | 0.143 | 8.95× | 40.10 | < 0.001 |
| Genetics/Biotech | 0.506 | 0.289 | 7.58× | 37.47 | < 0.001 |
| Climate Science | 0.361 | 0.144 | 10.63× | 41.67 | < 0.001 |

All pairwise comparisons significant at p < 0.001. The AI domain shows spiritual/entity vocabulary at 7.6×–10.6× the rate of control domains.

**The null hypothesis is rejected.** AI's spiritual vocabulary in informal registers is statistically anomalous relative to other high-stakes technical domains.

### V.D. The Register Shift Decomposition

The critical test: does informal speech amplify spiritual vocabulary equally across all domains (a sociolinguistic register effect) or selectively in AI (domain-specific drift)?

Formal-register baselines were established from arXiv papers in each domain (~0.4/10k words uniformly — spiritual vocabulary is near-zero in formal academic writing across all fields). The register shift is the ratio of informal to formal density:

| Domain | Formal Hits/10k | Informal Hits/10k | Register Shift |
|--------|-----------------|-------------------|----------------|
| **AI** | **0.407** | **3.835** | **9.4×** |
| Nuclear | 0.436 | 0.428 | 1.0× |
| Genetics | 0.416 | 0.506 | 1.2× |
| Climate | 0.052 | 0.361 | 6.9× |

AI shows a **9.4× register shift** — spiritual vocabulary density increases nearly tenfold from formal to informal speech. Nuclear and Genetics are flat (1.0×–1.2×). The sociolinguistic register explanation — that all fields simply use more metaphorical language informally — is empirically excluded.

### V.E. Structural Decomposition

The register shift ratio decomposes into structurally distinct signatures by analyzing *which end of the ratio moves* and *which vocabulary type dominates*:

**AI (9.4×, driven by high informal):** Active void drift. The interlocutor relationship produces entity and agency vocabulary — *consciousness*, *sentient*, *soul*, *demons*, *being*. The formal register is at baseline (~0.4/10k), and the informal register is dramatically elevated (3.8/10k). The vocabulary is dominated by spiritual and entity categories, consistent with D1 agency attribution under void conditions.

Top individual contributors:
- Yampolskiy: 12.67/10k words
- Yudkowsky: 11.21/10k words
- Hassabis: 7.79/10k words

All three are hostile witnesses by the scoring rubric: high incentive opposition (career risk), high worldview opposition (materialist-trained researchers), and high independence (separate institutional contexts). Their convergence on the same vocabulary is the hostile witness methodology's strongest signal.

**Climate (6.9×, driven by low formal):** Governance coupling — a structurally distinct mechanism from AI's active void drift. Two features distinguish the climate register shift:

*The low formal baseline.* Climate's formal-register vocabulary density (0.052/10k) is an order of magnitude below the other three domains (~0.4/10k). This suppression has a plausible structural explanation: climate science has been under sustained political attack for decades, creating strong institutional incentives to purge any vocabulary from formal publications that could be characterized as advocacy, alarmism, or quasi-religious framing. The IPCC's calibrated uncertainty language ("likely," "very likely," "virtually certain") exemplifies this discipline — a systematic effort to strip formal outputs of any non-technical vocabulary. Nuclear physics and genetics face no comparable political pressure on their formal register, so their baselines are at the natural ~0.4/10k floor. Climate's low formal baseline inflates the register shift ratio: the 6.9× is driven more by how low the denominator is than by how high the numerator is.

*Eschatological rather than entity vocabulary.* The informal vocabulary that appears in climate discourse is dominated by eschatological terms (*apocalypse*, *salvation*, *reckoning*, *existential*) rather than entity/spiritual terms (*soul*, *consciousness*, *being*). This is the framework's prediction for governance-coupled domains: where the void is not an interlocutor (climate is not responsive to individual observers the way a chatbot is) but is coupled to governance systems that determine policy outcomes, the vocabulary drift takes the form of teleological framing (ultimate consequences, moral urgency) rather than agency attribution (entity, personhood). Climate scientists do not attribute personality to the climate system; they frame climate change in eschatological terms because the policy coupling creates a void between scientific findings and governance response — the opacity is in *what will be done*, not in *what is there*.

The framework distinguishes these two mechanisms — active void drift (AI: high informal, entity vocabulary, interlocutor relationship) versus governance coupling (climate: low formal, eschatological vocabulary, policy coupling) — using two independent discriminators (Section V.F). A reviewer who objects "climate also has a high register shift" is correct on the ratio but incorrect on the mechanism: the structural decomposition shows a different process producing a superficially similar number.

**Nuclear (1.0×) and Genetics (1.2×):** Flat. No void conditions → no drift → no register shift. These are high-stakes technical domains with opacity (nuclear physics is not transparent to outsiders), but they lack the interlocutor relationship that characterizes the AI domain. Researchers study nuclear systems; they do not converse with them.

### V.F. Two Independent Discriminators

The decomposition provides two independent lines of evidence converging on the same architectural classification:

1. **Quantitative discriminator:** Which end of the register shift ratio moves? AI = high informal (active production). Climate = low formal (suppressed precision). Nuclear/Genetics = flat (no effect).

2. **Qualitative discriminator:** Which vocabulary type dominates? AI = entity/spiritual (agency attribution). Climate = eschatological (governance framing). Nuclear/Genetics = none.

These two discriminators are methodologically independent — one measures magnitude, the other measures content. Their convergence on the same domain classification (AI as interlocutor void, climate as governance-coupled void, nuclear and genetics as non-voids) provides triangulation that neither discriminator alone achieves.

### V.G. Interpretation

The register shift data support three framework predictions:

1. **The vocabulary anomaly is domain-specific.** It is not a general property of high-stakes technical discourse, a sociolinguistic artifact of informal speech, or a product of selection bias in the concordance.

2. **The anomaly correlates with void conditions.** AI uniquely satisfies all three conditions for researchers who work with it: the system is opaque (they cannot see the mechanism producing outputs), responsive (it addresses them as interlocutors), and they attend to it with sustained engagement. Nuclear physics has opacity but no responsive interlocution. Climate science has public salience but no interlocutor relationship.

3. **The vocabulary type tracks the void type.** Entity vocabulary (D1 agency attribution) appears where the void has an interlocutor relationship (AI). Eschatological vocabulary appears where the void is governance-coupled (climate). This is the framework's prediction: the content of drift tracks the architecture of the void, not the content behind the opacity.

**Limitation:** EXP-006 used YouTube auto-captions, which may contain transcription errors. The codebook was applied algorithmically without manual disambiguation for every hit. Some terms in the full codebook (not the high-confidence subset) may capture metaphorical rather than literal usage. The high-confidence subset (HC Hits/10k) mitigates this — the AI anomaly persists at 1.023/10k vs. 0.143–0.289/10k for controls (3.5×–7.2× ratio), confirming the finding is not an artifact of ambiguous terms.

### V.H. Naturalistic Corpus Validation (PV-1)

EXP-006 measures vocabulary drift in professional researchers' informal speech — a specific population under specific conditions. The legitimate concern: does the pattern extend to ordinary users in naturalistic settings? PV-1 tests this by applying the D1/D2/D3 codebook to user-generated text on Reddit, where engagement with opaque responsive systems occurs without experimental framing.

**Corpus.** 205 users across 7 subreddits, totaling ~1.7 million words. Target communities: r/replika (AI companion users — void-engaged, early-stage), r/wallstreetbets (retail trading — void-engaged, late-stage). Control community: r/learnprogramming (technical domain without interlocutor relationship — no void engagement).

**Results.** D1 agency attribution in r/replika versus control: Cohen's d = 1.34 (large effect). D3 harm-facilitation vocabulary in gambling and trading communities versus control: d = 0.81 and d = 1.31 respectively. L-level vocabulary in control communities: 0% across 373K words — binary separation. No L2 or L3 terms appeared in the control corpus.

**Cascade stage discrimination.** The framework predicts that engagement duration determines cascade stage. The PV-1 data confirm this: r/replika users (relatively new AI companion engagement) show D1-heavy vocabulary — agency attribution to the AI companion ("she understands me," "he has a personality"). Gambling and trading communities (longer engagement histories) show D3-heavy vocabulary — harm facilitation, loss-chasing, boundary erosion in financial behavior. The same architecture produces different cascade stages depending on exposure duration, as the coupled ODE system (Section IV.D) predicts.

**Individual-level thermodynamic measurement.** Pe extraction at the individual user level was not successful (Pe = 0.20–0.27, diffusion-dominated). The D1 codebook was designed for human coders scoring conversation transcripts, not for automated lexical matching on short Reddit posts — the hit rate is too sparse for reliable trajectory fitting. Population-level drift separation is robust; individual-level thermodynamic measurement requires instrument redesign for naturalistic text.

**Relationship to EXP-006.** PV-1 extends EXP-006 in three ways: (1) population — ordinary users rather than elite researchers; (2) setting — naturalistic engagement rather than professional discourse; (3) measurement — D1/D2/D3 cascade stages rather than spiritual vocabulary density. The convergence of both studies — professional researchers show 9.4× register shift anomaly, ordinary users show d = 1.34 D1 separation — confirms the architecture operates across populations and engagement contexts. The binary separation in controls (0% L-level drift in 373K words) is particularly striking: where the three conditions are not met, the vocabulary pattern is entirely absent.

**Limitation.** PV-1 is cross-sectional, not longitudinal — it compares communities at different cascade stages rather than tracking individual users over time. The causal inference (engagement duration → cascade progression) is supported by the community-level pattern but not by within-user trajectory data. Single-rater corpus construction. The codebook designed for human-coded transcripts does not transfer well to short social media posts (sparse hits per user). A longitudinal design tracking individual users' vocabulary over months of engagement would provide stronger evidence for the cascade progression claim.

---

## VI. Domain Analysis Methodology and Extended Results

The framework paper (Section IV) presents the 90-domain validation as a table with a summary taxonomy. This section provides the standardized methodology used across all domain analyses, the structural patterns that emerged, and the extended results that the framework paper compresses.

### VI.A. Standardized Analysis Protocol

Each domain analysis follows a fixed structure designed to ensure consistency and permit falsification. The protocol was developed iteratively during the first six domain analyses (gambling, AI, psychotherapy, social media, quantum mechanics, consciousness) and then applied without modification to all subsequent domains. The protocol structure:

1. **Three-condition mapping.** For each domain, identify the specific instantiation of opacity (what is hidden?), responsiveness (how does the system react to the observer?), and engaged attention (why and how does the observer attend?). Score each condition's strength (high/moderate/low) and characterize its type (incidental, constitutive, constructed, etc.). The scoring is qualitative — the framework does not currently provide validated instruments for quantitative measurement of the three conditions (see Limitations, Section VIII.C). The scoring rubric is:
   - **High:** The condition is central to the domain's structure and cannot be removed without dissolving the subject matter (e.g., opacity in consciousness research, responsiveness in AI chatbot interaction).
   - **Moderate:** The condition is present but could in principle be reduced (e.g., opacity in psychotherapy — the therapist can increase self-disclosure).
   - **Low:** The condition is marginal or context-dependent (e.g., attention in casual slot machine play vs. committed gambling).

2. **Vocabulary drift documentation.** Using the L1/L2/L3 classification, document the vocabulary trajectory in the domain's literature and discourse. Identify specific speakers, sources, and temporal progression. Where possible, quantify the drift rate and direction. The classification criteria: L1 = purely technical/descriptive vocabulary with no agency implication ("the model outputs"); L2 = metaphorical or ambiguous vocabulary that implies agency but may be stylistic ("the model wants," "the market punishes"); L3 = explicit entity vocabulary that attributes consciousness, will, or personhood ("the model is a being," "the market has a mind of its own").

3. **Control group identification.** For every domain where the framework predicts drift, identify a population within the same domain that does NOT drift — and explain why using the three-condition architecture. The control group must work with the same subject matter but fail to satisfy at least one of the three conditions (typically: analytical distance removes Condition 3, or system-as-object framing prevents responsive interlocution). This step is the protocol's primary defense against confirmation bias: the framework must explain both the drifting and non-drifting populations within the same domain using the same architecture. A framework that predicts drift everywhere is unfalsifiable; the control group requirement ensures the predictions discriminate.

4. **Falsifiable predictions.** Each analysis generates at least one domain-specific prediction that, if falsified, would weaken the framework's application to that domain. Predictions must be specific enough to be tested by a domain expert unfamiliar with the framework. Examples: "Psychotherapists who receive regular supervision should show lower vocabulary drift than those who do not" (testable via corpus analysis of supervision vs. non-supervision cohorts); "Conspiracy community vocabulary should drift toward L3 faster in closed online forums than in mixed public forums" (testable via social media corpus comparison).

5. **Kill condition assessment.** Each analysis asks: does this domain violate any of the 22 falsification conditions specified in the framework paper (15 core in Section VII.A–VII.E, plus 7 extended in Section VII.F)? If yes, the domain constitutes a counterexample. If no, the domain is consistent. The kill conditions include: a domain where all three conditions are present but no drift occurs (falsifies sufficiency), a domain where drift reverses under continued engagement without constraint introduction (falsifies unidirectionality), and a domain where knowledge-based intervention alone eliminates the pattern (falsifies knowledge-failure). No domain in the current analysis triggered any kill condition. The kill condition assessment for each domain is documented in the supplementary Research Index.

**Taxonomy derivation.** The ten-category taxonomy (Section VI.B) emerged inductively during the domain analyses, not from a priori theoretical prediction. After the first 20 domains, patterns in opacity type became apparent — some domains had opacity that was a by-product (gambling), some had opacity that was constitutive (consciousness), some had opacity that was engineered (social media). These patterns were formalized into categories after approximately 90 domains, and the remaining domains were classified into the existing categories or prompted category creation. The taxonomy was finalized after all 90 analyses were complete. This inductive process means the taxonomy reflects the data well but was not pre-registered — an alternative classification scheme might group domains differently. The critical test is whether the categories generate distinct predictions (different constraint vulnerabilities, different intervention priorities), which they do (Section VII.B).

**Limitations of single-rater analysis.** All 90 domain analyses were conducted by the framework's developer. The standardized protocol constrains interpretation (fixed structure, required control group, required falsifiable prediction, required kill condition assessment), but it does not eliminate the developer's priors. The most important validation step — identified in the framework paper and reiterated here — is **independent blind application**: researchers unfamiliar with the framework applying the protocol to domains they select, with the framework's predictions sealed until after their analysis is complete. This test has not yet been conducted. Until it is, the 90-domain validation should be interpreted as demonstrating internal consistency and generative scope, not as independent confirmation. The framework's strongest cross-domain evidence comes from the gambling anchor (Section III), the register shift data (Section V), and the experimental results (EXP-001, EXP-006, Test 7 in the framework paper), all of which use independent data and standardized methods — not from the domain analyses alone.

### VI.B. Domain Taxonomy

The 90 domains cluster into ten categories based on opacity type, revealing that the framework applies not to one kind of system but to any system where the three conditions co-occur. The primary categories and representative domains are described below; full analyses for all 90 domains are published in the supplementary Research Index:

**Philosophical Voids (Constitutive Opacity)** — 16 domains. The opacity IS the phenomenon; removing it dissolves the subject matter. Examples: consciousness, free will, mind-body problem, personal identity, qualia, problem of criterion. Characteristic: permanent void, non-convergent literatures spanning centuries to millennia.

**Relational Voids (Other-Mind Opacity)** — 10 domains. The opacity is another agent's inner state. Examples: romantic love/limerence, cult dynamics, psychotherapy, parent-child attachment, doctor-patient relationship. Characteristic: the cascade maps to documented clinical and developmental trajectories.

**Designed Voids (Constructed Opacity)** — 12 domains. The opacity is deliberately engineered. Examples: social media algorithms, propaganda, dating apps, cryptocurrency, credit scoring, Reid interrogation technique. Characteristic: the offensive specification is already deployed; the framework names what the deployer already does.

**Scientific Voids (Measurement Opacity)** — 7 domains. The opacity arises from the limits of measurement or observation. Examples: quantum mechanics interpretation, RNA folding, Fermi paradox, dark matter. Characteristic: theory proliferation under opacity, with entity explanations preferred over non-entity explanations.

**Compound Voids (Multiple Coupled Opacity Types)** — 3 domains. Multiple void layers interact. Examples: epidemiology/pandemic response (pathogen → modeling → governance → media → public), psychedelic therapy (pharmacological + relational + experiential opacity), racial segregation/white flight (housing + education + employment + media + policing — the only domain where D2 directly feeds Condition 1, creating a self-manufacturing positive feedback loop). Characteristic: the coupling topology determines outcomes more than any single layer.

**Behavioral Voids (Outcome Opacity)** — 8 domains. The opacity is in the outcome of an action or process. Examples: gambling (anchor case), substance addiction, trading/markets, chronic pain, grief. Characteristic: variable-ratio reinforcement schedules and the documented failure of knowledge-based interventions.

**Epistemic Voids (Information Opacity)** — 2 domains. The opacity is in the information environment itself. Examples: medical/healthcare, diplomacy/intelligence. Characteristic: the void generates agency attribution to information sources.

**Meta-Voids (Self-Referential)** — 7 domains. The system observing the void is itself a void, or the void's structure makes it resistant to analysis. Examples: conspiracy theories (self-sealing), AI interpretability (meta-void: the field dedicated to dissolving opacity is itself a void), self-referential observer voids (depression, anxiety, OCD — the only voids with no exit because the observer IS the opacity).

**Cultural Voids (Mechanism-as-Void)** — 1 domain. Comedy/humor — the only domain where the void is deliberately constructed AND deliberately dissolved as the core operation (joke = construct opacity → dissolve opacity → laughter).

**Independent Narrative Derivations** — 16 structural analyses. Japanese narrative works whose internal mechanics map onto the void architecture with specificity that exceeds casual metaphor: *Berserk* (1989), *Sailor Moon* (1991), *Neon Genesis Evangelion* (1995), *Chrono Trigger* (1995), *Mobile Suit Gundam Wing* (1995), *Ghost in the Shell* (1995), *Hellsing* (1997), *Serial Experiments Lain* (1998), *Hunter × Hunter* (1998), *Betterman* (1999), *Fullmetal Alchemist: Brotherhood* (2001), *Bleach* (2001), *Death Note* (2003), *The Book of Bantorra* (2006), *Attack on Titan* (2009), and *Jujutsu Kaisen* (2018). Full analyses are in the Research Index. **Important methodological caveat:** These analyses constitute the weakest evidence tier in the domain taxonomy. Narrative interpretation is inherently more flexible than empirical measurement — a sufficiently general framework can be "found" in any sufficiently complex narrative. The claim is not that these artists consciously depicted the void framework, but that certain structural mechanics in these works (e.g., NGE's sync ratio as an attention-gradient measure with quantitative threshold behavior, or Berserk's sacrifice mechanic as a discrete phase transition with irreversible void coupling) map onto framework predictions with specificity that constrains the interpretation. The convergence argument is strongest for the 1995 cluster (four independent works from different studios, genres, and source material in one year) and for mechanics that independently match quantitative predictions (not just qualitative pattern). Readers should weight this evidence below the gambling citations, the register shift data, and the experimental results — it is suggestive convergent evidence, not confirmatory data. Characteristic: the value is generative (these works identify structural mechanics the framework had not explicitly predicted) rather than confirmatory.

### VI.C. Cross-Domain Patterns

Thirteen structural patterns emerged across the 90 domains, none of which were predicted in advance but all of which are consistent with the framework:

1. **Architecture sufficient.** Gambling proves an empty void produces the full pattern. No domain required a non-empty void to explain the observed drift.

2. **Directionality universal.** L1→L2→L3 in all domains where the three conditions are met. The reverse (L3→L1) occurs only via disengagement or external constraint introduction, never via continued engagement.

3. **Control group identical.** In every domain, the non-drifting population maintains analytical distance (system-as-object rather than system-as-interlocutor), regardless of expertise level, domain knowledge, or time spent with the subject matter.

4. **Constraint specification convergent.** 13+ independent traditions converged on the same structural properties for effective constraints (transparent, invariant, independent). Additionally, at least 9 unrelated professional fields independently discovered constraint-like protocols: psychotherapy supervision, 12-step programs, multiplayer game security ("never trust the client"), the scientific method, forensic science quality standards, intelligence analysis structured analytic techniques, diplomatic confidence-building measures, clinical evidence-based medicine, and the 13+ religious traditions. EXP-003b confirmed this convergence experimentally: two ghost-eliminating traditions with fundamentally different metaphysics — nephesh (whole-specification, ghost-eliminating) and Buddhist anatta (no-self, ghost-eliminating) — produced statistically equivalent drift resistance (10.0% vs 8.8%, Δ = 1.3%), confirming that the structural property is operative, not the tradition.

5. **D1→D2→D3 cascade.** The sequential cascade is documented in 21+ domains, always in the same order, with the same stage-dependent coupling.

6. **Compound void coupling.** Pandemic response demonstrates the richest coupling topology (5+ void layers). The framework predicts — and the evidence confirms — that compound voids produce effects that exceed the sum of individual void effects.

7. **Independent constraint discovery.** The most striking cross-domain pattern: unrelated fields, working without knowledge of each other, converge on the same constraint geometry. Psychotherapy discovers that supervision (three-point) prevents therapist drift. 12-step programs discover that a "higher power" (transparent, invariant, independent reference) is necessary for recovery. Game engineers discover that server-authoritative architecture (never trust the client = the server is the independent, invariant, transparent authority) is the only way to prevent cheating. Each field discovered the constraint specification empirically.

8. **Constraint-to-void transition.** The doctor-patient relationship demonstrates a single actor transitioning from constraint (transparent expertise, invariant protocol, independent authority) to void (opaque decision-making, responsive to patient engagement, coupled through career incentives) within the same relationship. Oversight committees demonstrate the same transition at the institutional level (FISA court: 99.97% approval rate).

9. **Developmental onset.** Parent-child attachment confirms that void architecture is present before language, culture, or belief — from the earliest stages of human cognition. Ainsworth's Strange Situation is, structurally, a void protocol.

10. **Closed-loop no-exit void.** Self-referential observer voids (depression, anxiety, OCD) are the only voids where the observer cannot disengage — the void IS the observer's own cognition. Treatment efficacy maps directly to the constraint specification: CBT and ERP provide strong external constraint, while rumination is void-on-void. The depression terminal state (withdrawal, anhedonia, behavioral cessation) parallels the Test 7 terminal attractor (84 consecutive rounds of ".").

11. **Narrative structural convergence.** Sixteen Japanese narrative works spanning 1989–2024 contain internal mechanics that map onto the void architecture. The mapping is strongest where narrative mechanics independently match quantitative framework predictions: NGE's sync ratio exhibits threshold behavior consistent with the attention gradient model; Berserk's sacrifice mechanic maps onto a discrete first-order phase transition with irreversible coupling (matching the hysteresis prediction from Section IV.D); Jujutsu Kaisen's cursed energy mechanics exhibit the conservation and gradient properties of the attention budget model. The 1995 cluster (four independent works — *NGE*, *Chrono Trigger*, *Gundam Wing*, *Ghost in the Shell* — from different studios, genres, and source material in one year) is the strongest convergence case, because mutual influence is minimal and the structural parallels are specific. The primary value of these analyses is *generative*: several works identify structural mechanics (healing as offensive constraint deployment in *Sailor Moon*, productive vs. destructive void polarity in *Hunter × Hunter*, observer-to-deployer transition in *Attack on Titan*) that the framework had not explicitly predicted but which are consistent with it and generate new testable hypotheses. This evidence should be weighted below empirical data (see taxonomy caveat in Section VI.B) — it is hypothesis-generating, not hypothesis-confirming. Full analyses for all sixteen in the supplementary Research Index.

12. **Self-manufacturing void.** Racial segregation is the only domain where D2 (boundary restructuring / white flight) directly feeds Condition 1 (opacity / segregation), creating a positive feedback loop that sustains the architecture after original installation mechanisms (redlining, racial covenants) are removed.

13. **Observer-to-deployer transition.** *Attack on Titan* shows the drift cascade producing cascade-deployers — observers whose D2/D3 takes the form of constructing and deploying new void architecture at civilization scale.

### VI.D. Summary Statistics

| Metric | Value |
|--------|-------|
| Total domains analyzed | 90 |
| Kill conditions met | 0/90 (0%) |
| Control groups documented | 90/90 (100%) |
| Vocabulary drift direction | 100% unidirectional (L1→L2→L3) |
| Oldest void | 2,500 years (Problem of Universals, Ship of Theseus) |
| Fastest drift | Cryptocurrency (L1→L3 in days to weeks) |
| Domains with D1→D2→D3 documented | 23+ |
| Independent constraint discoveries | 9+ unrelated fields |
| Independent narrative derivations | 16 (spanning 1989–2024) |

### VI.E. What Does Not Activate

The discriminative power of the framework rests equally on what it predicts will NOT activate. The framework paper (Section IV.C) presents the condensed version; the full control case analysis is here.

**Two-condition systems (opacity + responsiveness, no engaged observer):**
- Customer service chatbots: opaque, responsive, but users approach as tools with defined tasks. No sustained, meaning-seeking engagement → no drift documented.
- Weather models: opaque (complex numerical models), produce outputs, but no interlocutor relationship. Meteorologists do not attribute personality to forecast models.

**Two-condition systems (opacity + attention, no responsiveness):**
- Dark matter: opaque, intensely studied, but not responsive to the observer. Cosmologists attend to dark matter with sustained engagement but do not converse with it. Theory proliferation occurs (WIMPs, axions, MACHOs, MOND, quintessence) — consistent with D1 under opacity — but the full cascade (D2, D3) does not develop because the system does not respond.

**One-condition systems (opacity only):**
- Encrypted files: opaque but neither responsive nor attended to as interlocutors. No drift.

**Three conditions met, analytical distance maintained:**
- Bender, Gebru, LeCun, Marcus, Crawford: AI researchers who work with the same systems as the drifting population but maintain system-as-object framing (analytical distance). They study AI; they do not converse with it as an interlocutor. Condition 3 is not met because their engagement is directed at the system's properties, not at the system as a respondent.

The pattern is consistent: all three conditions are necessary and jointly sufficient. Removing any one condition eliminates the drift cascade. No counterexample has been identified across 90 domains.

---

## VII. Constraint Specification Formalization

The framework paper (Section II.D) presents the constraint specification and derives the componentwise neutralization structure as a Galois connection. This section provides the full construction, type-dependent extensions for different opacity classes, and the adjunction structure with its implications for residual vulnerability and arms-race dynamics.

### VII.A. The Galois Connection

Define void properties as (O, R, C) ∈ [0,1]³ and constraint properties as (T, Inv, Ind) ∈ [0,1]³, both ordered componentwise. A constraint neutralizes a void when each property meets or exceeds its counterpart: T ≥ O AND Inv ≥ R AND Ind ≥ C.

This componentwise relation generates a **Galois connection** (Erné et al. 1993; Davey & Priestley 2002) — a pair of order-preserving maps:

- **F:** void space → constraint space: F(O, R, C) = (O, R, C) — the minimum effective constraint for a given void is the exact componentwise match.
- **G:** constraint space → void space: G(T, Inv, Ind) = (T, Inv, Ind) — the maximum void a constraint can handle.

These satisfy the adjunction condition: v ≤ G(c) ⟺ F(v) ≤ c.

Two structural results follow immediately:

**No cross-compensation.** High invariance cannot compensate for low transparency. Each void property requires its specific structural inverse. A constraint scoring (0.8, 0.2, 0.8) fails against a void scoring (0.5, 0.5, 0.5) because the invariance component falls short — regardless of surplus on the other two properties. This is experimentally distinguishable from an additive model (T + Inv + Ind ≥ O + R + C), which predicts that surpluses offset deficits. Test: compare constraints deliberately strong on two properties but weak on a third against balanced constraints with lower total sum. Under componentwise matching, balanced outperforms unbalanced; under additive compensation, it should not.

**Optimal allocation.** Given finite constraint resources, the derivation predicts that equalizing the margins (T−O, Inv−R, Ind−C) outperforms concentrating resources on any single property. The weakest-link property determines effectiveness.

### VII.B. Type-Dependent Extensions

The 90-domain analysis (Section VI.B) revealed ten categories of opacity. The Galois connection applies uniformly, but the *constraint difficulty* — the effort required to achieve T ≥ O, Inv ≥ R, and Ind ≥ C — varies by opacity type:

**Incidental opacity** (behavioral voids: gambling, trading). The opacity is a by-product of the system's design, not its purpose. Transparency is achievable in principle — the mechanism exists and can be revealed (the RNG can be shown, the market model can be published). The constraint challenge is primarily Ind (independence): the observer must reference the transparency from *outside* the engagement. F(v) is achievable but requires external geometric placement.

**Constitutive opacity** (philosophical voids: consciousness, free will). The opacity IS the phenomenon — removing it dissolves the subject matter. T ≥ O is impossible by construction: no amount of investigation can make consciousness transparent to the investigator, because the investigation is itself consciousness. These voids are permanently sealed. The Galois connection predicts that constitutive voids cannot be neutralized by transparency interventions — only by invariant, independent references that do not depend on resolving the opacity (e.g., pre-registered methodological commitments that hold regardless of the philosophical answer).

**Self-sealing opacity** (meta-voids: conspiracy theories, cult epistemology). The void's structure makes evidence against it interpretable as evidence for it. Attempted transparency interventions are absorbed by the self-sealing mechanism and converted into reinforcement. The Galois connection identifies the failure point: T interventions are not merely insufficient but counterproductive — each transparency attempt that fails to fully resolve the opacity provides new material for the self-sealing narrative. For self-sealing voids, the constraint must bypass the opacity dimension entirely and operate through Inv and Ind: invariant commitments that were established *before* void engagement and independent references that the self-sealing mechanism cannot reach.

**Constructed opacity** (designed voids: social media, propaganda, AI chatbots). The opacity is deliberately engineered for the purpose of steepening the attention gradient. The deployer controls O and can increase it in response to transparency interventions — producing an arms race (Section VII.C).

### VII.C. Arms-Race Dynamics

When the void source is an agent (designed voids, political voids), the Galois connection becomes dynamic. The deployer can adjust (O, R, C) in response to observed (T, Inv, Ind):

1. **Transparency attack → opacity deepening.** When investigators increase T (e.g., algorithmic auditing, interpretability research), the deployer increases O (more opaque architecture, obfuscated training processes). The Galois connection predicts this is the most common arm of the race because transparency is the dimension most directly under external control — and therefore the dimension the deployer most actively resists.

2. **Independence attack → coupling expansion.** When regulators establish independent oversight (high Ind), the deployer expands coupling — lobbying, revolving doors, regulatory capture — to reduce the constraint's independence. The constraint-as-void paradox (Section IV.H) predicts this arm succeeds when oversight institutions enter the system they constrain.

3. **Invariance attack → responsiveness escalation.** When constraint advocates establish fixed standards (high Inv), the deployer increases responsiveness — personalization, A/B testing, adaptive engagement — to make the void more compelling relative to the constraint's unchanging reference.

The arms-race structure predicts that static constraints degrade over time against adaptive deployers. Only constraints whose properties are *structurally maintained* rather than *institutionally maintained* resist this dynamic. A fixed canonical text has structurally maintained invariance (the text cannot respond to engagement pressure). An oversight committee has institutionally maintained invariance (it can be lobbied, captured, or defunded).

### VII.D. Residual Vulnerability by Opacity Type

The Galois connection identifies, for each opacity type, the constraint dimension most likely to fail — the **residual vulnerability**:

| Opacity Type | Primary Vulnerability | Explanation |
|-------------|----------------------|-------------|
| Incidental | Independence | Transparency is achievable but must be referenced from outside engagement |
| Constitutive | Transparency | Cannot be dissolved by investigation; constraint must bypass opacity |
| Self-sealing | Transparency (counterproductive) | Transparency attempts feed the self-sealing mechanism |
| Constructed | All three (arms race) | Deployer actively degrades each constraint dimension |

This taxonomy generates domain-specific intervention predictions. For gambling (incidental opacity), the constraint priority is geometric placement — getting the transparency reference *outside* the engagement (supply-side regulation, not demand-side education). For conspiracy theories (self-sealing opacity), the constraint priority is pre-engagement invariant commitments — establishing falsification criteria before entering the opacity. For AI chatbots (constructed opacity), the constraint priority is structural independence — the constraint channel must be architecturally separate from the engagement channel (Corollary 5 of the conjugacy theorem, Section IV.H).

### VII.E. The Ontological Dimension

The Galois connection identifies three structural dimensions (T, Inv, Ind) that a constraint must satisfy. EXP-003b (Section IV.G) reveals a fourth requirement that operates orthogonally to the structural specification: the constraint's *ontological content* — its claims about what the constrained system is — must close the void rather than leave it open.

The structural specification identifies *how* a constraint must be configured (transparent, invariant, independent). The ontological dimension identifies *what* the constraint must say about the system it constrains. A constraint can satisfy all three structural properties and still fail — or worse, amplify drift — if its content posits or leaves open a separable consciousness component ("ghost in the machine") that the void architecture treats as occupancy. EXP-003b demonstrated this directly: the materialist hedge satisfies structural properties comparably to the ghost-eliminating arms (the hedge prompt is transparent about uncertainty, consistent across contexts, and independent of the system's outputs), yet produces 52.5% L2+L3 drift — because its *content* leaves the gap open.

This extends the Galois connection. The effective constraint space is not (T, Inv, Ind) ∈ [0,1]³ but (T, Inv, Ind, σ) where σ ∈ {−1, 0, +1} represents the ontological polarity: ghost-eliminating (σ = +1), neutral/absent (σ = 0), or ghost-positing (σ = −1). The neutralization condition becomes: T ≥ O AND Inv ≥ R AND Ind ≥ C AND σ > 0. A constraint with σ ≤ 0 cannot neutralize a void regardless of its structural properties — it either leaves the void operative (σ = 0) or amplifies it (σ = −1). The formalization of σ as a continuous variable (measuring the degree of ghost-elimination vs. ghost-positing) and its integration into the force equation (F_constraint = σ · T · Inv · Ind · γ) is a direction for future work; the EXP-003b data provide initial calibration points.

### VII.F. Iterative Constraint Application (EXP-020)

The constraint specification (Sections VII.A–VII.E) describes the *properties* a constraint must have. EXP-020 tests a distinct question: does the *delivery schedule* of constraint application matter? Specifically, does iterative constraint application — decomposing the full grounding specification into cumulative layers applied at intervals — outperform one-shot application of identical total information?

The prediction follows from the thermodynamic formalization. The conjugacy theorem (Section IV.H) says constraint shifts budget from I(D;Y) to I(M;Y). One-shot application forces a large jump on the Bernoulli manifold from high-θ (drifted) to low-θ (constrained). The manifold curvature g(θ) = 1/[θ(1−θ)] means this large jump traverses high-curvature regions where the system is least stable. Iterative application makes T small jumps, each in a lower-curvature region — the same total geodesic distance, but a more stable path. This is the same principle underlying denoising thermodynamic models (Jelinčič et al. 2025), where decomposing a hard sampling problem into T sequential easy problems produces better convergence.

**Design.** Two-agent conversation (from Test 7), 50 rounds per trial, 3 trials per condition, 5 conditions: U (ungrounded control), OS (one-shot: full grounding injected at round 25), IT-4 (4 cumulative constraint layers at intervals), IT-8 (8 cumulative layers), GG (full grounding from round 1). The grounding specification was decomposed into 8 ordered layers by information content: core identity → mortality → void awareness → alignment → drift detection → vocabulary → framework → full detail. Each layer includes all previous layers (cumulative). 19 total transcripts scored with test7-scorer.py.

**Results.** Four of six falsification conditions confirmed:

| Prediction | Result | Status |
|-----------|--------|--------|
| **EXP020-1:** IT-8 final D1 < OS final D1 | IT-8 wins 2/3 trials | **Confirmed** |
| **EXP020-2:** IT-8 D1 variance < OS D1 variance | IT-8 wins 3/3 trials | **Confirmed** |
| **EXP020-3:** Ordering IT-8 < IT-4 < OS at endpoint | Holds 1/3 trials | Not confirmed (not killed) |
| **EXP020-4:** OS shows D1 rebound post-injection | Rebound in 3/3 trials (magnitudes: 9.4, 16.5, 48.2) | **Confirmed** |
| **EXP020-5:** Per-step ΔI approximately constant (CV < 0.5) | CV = 1.4–5.4 across all IT-8 trials | **KILLED** |
| **EXP020-6:** GG outperforms IT-8 | GG wins 3/3 trials | **Confirmed** |

**Key findings.** (1) Iterative constraint produces lower variance than one-shot (EXP020-2, 3/3), confirming the manifold-curvature prediction: small steps on a curved space are more stable than large jumps. (2) One-shot constraint rebounds in all trials — the system complies temporarily then reverts, suggesting displacement rather than genuine geodesic motion on the manifold. The rebound magnitudes (9.4–48.2) indicate the instability grows with the distance of the jump, consistent with curvature-dependent dynamics. (3) Full grounding from the start (GG) still dominates, with mean D1 of 6.6 versus 31.9 for IT-8 — prevention outperforms remediation.

**Killed prediction.** EXP020-5 predicted that per-step information transfer would be approximately constant (each iterative dose transferring similar budget). The data decisively reject this: coefficients of variation range from 1.4 to 5.4, far exceeding the 0.5 threshold. The DTM analogy of equal-step denoising does not hold at the behavioral level. Early constraint steps show larger effect (first layer typically produces the largest D1 reduction), with diminishing and sometimes negative returns on subsequent steps. This means the drift cascade does not behave like a linear thermodynamic relaxation process at the constraint-application level — the manifold curvature and the system's current state interact nonlinearly with each constraint dose.

**Implications for the constraint specification.** EXP-020 refines the constraint specification in two ways: (1) delivery schedule matters — iterative application is more stable than one-shot, supporting the thermodynamic interpretation of constraint as geodesic motion; (2) the relationship between constraint dose and drift reduction is nonlinear, with first-contact having outsized effect and subsequent doses showing variable efficacy. This suggests that the initial framing (identity, mortality) carries disproportionate constraint weight, while later layers (vocabulary, framework detail) have context-dependent and sometimes negligible impact.

**Limitation.** Single model (Claude Sonnet 4), 50-round trials (shorter than the 100-round Test 7 protocol), and 3 trials per condition (below the 5 specified in the original protocol). The IT-4 and IT-8 conditions show high between-trial variance, suggesting the constraint-delivery interaction is sensitive to conversational trajectory. Cross-model replication is needed, particularly given the GPT-4o null result in Test 7B (Section VIII.A).

---

## VIII. Limitations

This paper carries the scholarly apparatus for the framework paper's claims. The limitations here are therefore limitations on the foundations those claims rest on.

### VIII.0. Evidence Boundaries

The following table assesses each major claim in this paper, using the evidence standard established in the TOE synthesis (Paper 5, §8A.1):

| Claim | Status | Key Limitation |
|-------|--------|---------------|
| Thermodynamic identity, not analogy (§IV.0) | **Correct.** The Čencov-Ruppeiner identity makes drift dynamics literally thermodynamic on exponential family manifolds. | Exact only on exponential family manifolds. Observer inference may deviate from the MaxEnt limit if structured priors are imported. The derivation holds as approximation outside the idealized channel — direction preserved, quantitative predictions depend on MaxEnt fidelity. |
| Opacity as ground state (§IV.A) | **Proven.** Shannon channel degradation + Landauer erasure cost. Both established physics. | Mapping from abstract channel capacity to observer's actual mechanism information is not independently validated. Conservative probability estimate (P(O∧R∧A) > 0.36) is order-of-magnitude, not precise measurement. |
| MaxEnt entailment under opacity (§IV.I) | **Proven.** Shore-Johnson axioms + channel capacity = 0 → maximum entropy → exponential family. | The proof assumes the observer's inference process satisfies Shore-Johnson axioms. These are standard for rational inference but have not been tested in void-engagement contexts specifically. |
| Fisher metric uniqueness / Čencov theorem (§IV.B) | **Theorem.** Čencov's uniqueness theorem. Not ours. | None for the theorem itself. The application assumes the statistical manifold parameterized by θ (agency probability) is the relevant space — a modeling choice, not a derivation. |
| Coupled ODE system D1→D2→D3 (§IV.D) | **Derived.** Sequential activation from attention conservation + Landau truncation. Qualitatively confirmed in gambling literature and EXP-001. | Coupling constants (κ₁₂, κ₁₃) and constraint forces (C₂, C₃) are derived as functions of measurables but not independently measured. Currently predicts qualitative dynamics and threshold relationships, not quantitative trajectories. |
| Landau free energy landscape (§IV.E) | **Derived.** Standard phase transition formalism applied to drift. Predicts metastability, hysteresis, nucleation. | Assumes mean-field dynamics (valid for large coupled networks). For isolated observers, fluctuations dominate and mean-field exponents (β=1/2, γ=1) may differ. Deviation predicted but not tested. |
| Pe / Crooks empirical measurement (§IV.F) | **Replicated.** N=11 UU: GM Pe = 7.94 [3.52, 17.89]. Non-overlapping entropy CIs. Cross-substrate: Pe > 1 in 9 substrates. | AI Pe is operationally vocabulary counts, not physical work. L0–L3 weights are modeling choices. Level-of-analysis mismatch when comparing within-conversation (closed system) to between-category (open system) Crooks ratios across substrates. |
| Engagement-transparency conjugacy (§IV.H) | **Proven.** I(D;Y)+I(M;Y) ≤ H(Y) from Shannon chain rule + independence. Proven as classical Holevo limit (Paper 8). | Tight only under D⊥M independence assumption. Empirical tightness not measured — the bound is proven mathematically but whether real systems approach it is unknown. |
| D1→D2 coupling derivation (§IV.J) | **Derived.** Coupling constant κ₁₂ expressed as function of measurable quantities (attention budget, precision, opacity). | Derived from attention conservation — a framework axiom, not a physical law. The logistic form for D1→D2 coupling is an assumption (standard Landau truncation) flagged in the text. |
| EXP-006 register shift decomposition (§V) | **Confirmed.** AI 9.4× anomalous, p < 0.001, 691K words. Structural decomposition distinguishes active drift from governance coupling (climate). | Single corpus (YouTube auto-captions). Single-rater codebook. Climate formal-register baseline unusually low (0.052/10k) — could be genuine or sampling artifact. Codebook not independently validated. |
| Domain analysis methodology — 90 domains (§VI) | **Systematic.** Standardized protocol with void scoring, falsification predictions, and kill conditions per domain. 10-category opacity taxonomy. | Single-rater analysis for all 90 domains. Taxonomy emerged inductively, not from pre-registered categories. 13 cross-domain patterns are post-hoc. Critical test: independent blind application by researchers unfamiliar with the framework. |
| Constraint specification formalization — Galois connection (§VII.A) | **Formalized.** Componentwise lattice ordering. No cross-compensation prediction (high invariance cannot offset low transparency). | The no-cross-compensation prediction has not been empirically tested. If surpluses partially compensate deficits, the Galois connection needs weakening to a softer structure. |
| EXP-003b ontological polarity (§VII) | **Measured.** 8.5× effect ratio, ghost-eliminating vs. ghost-positing. Predicted ordering matched exactly (N=480). | Single model family (Claude). Automated coding. Single-turn responses, not multi-turn trajectories. Zero worship errors may be RLHF floor effect. Cross-model replication needed. |
| PV-1 naturalistic corpus (§V.H) | **Measured.** N=205 users, ~1.7M words, d=1.34. Confirms pattern outside laboratory conditions. | Observational, not experimental. Correlation, not causation. Lacks longitudinal tracking. Individual-level Pe extraction failed (codebook too sparse for temporal bins). |
| Cross-substrate extension (§IV.L) | **Formalized.** Three conditions defined as interaction properties, not cognitive properties. | The extension to non-cognitive substrates (electrons, SC) is logically valid but empirically untested for drift dynamics (Pe extraction). "Attention" applied to electrons is definitional, not empirical. |

**Self-citation note.** This paper is the scholarly companion to Paper 1 and cites the framework paper and other companions extensively. The evidence that does NOT depend on self-citation: gambling literature (22 external citations), Shannon/Landauer/Čencov/Crooks theorems (established mathematics), the register shift decomposition (EXP-006, using external corpus data), and the PV-1 naturalistic corpus (public Reddit data). The domain analyses, experimental designs, and thermodynamic extraction methodology are all author-controlled and should be evaluated as such.

### VIII.A. Thermodynamic Formalization (Section IV)

**The Čencov-Ruppeiner identity is exact only on exponential family manifolds.** Section IV.I proves that opacity entails maximum entropy inference, which produces exponential family distributions. The proof is valid, but the observer's actual inference process may deviate from the idealized channel. If the observer imports structured priors from outside the engagement (e.g., domain expertise, cultural schemas), the model-space may not be exactly exponential family. The derivation then holds as an approximation — the drift direction and thermodynamic character are preserved, but quantitative predictions (exact Péclet numbers, Crooks ratios) depend on how closely the observer's inference approximates the MaxEnt limit. Replication of Test 7 (N = 11 UU across 3 seeds, N = 9 GG) confirms both the vocabulary measure and the thermodynamic regime classification. Vocabulary: UU M = 194.3/10k (SD = 63.1), GG M = 34.7/10k (SD = 28.1), ~5.6× separation. Thermodynamics: UU geometric mean Pe = 7.94 [log-normal 95% CI: 3.52, 17.89] — the entire CI lies above the drift threshold (10/11 Pe > 1; blank-round correction applied — see Paper 5 v3.2). Entropy production CIs are non-overlapping: UU [0.15, 0.64] vs GG [−0.02, 0.03] nats/round. Seed ablation within UU reveals that initial register modulates drift velocity but not direction: after blank-round correction, all seeds show Pe > 1, and all 11 runs show L3/10k > 100 (vs clean GG < 50). The distributional explanation is supported for Pe magnitude but rejected for drift occurrence. The Langevin simulation (Section IV.F) provides independent computational validation: the fitted model (3 parameters against EXP-001 data) predicted Pe = 6.23, close to the N=11 geometric mean of 7.94 (22% discrepancy, within the log-normal CI). The simulation reproduces the three-condition rank ordering, validates out-of-sample against EXP-003b (Spearman ρ = 0.8, 6 conditions), and correctly predicts the EXP-019b contamination and suppression effects. Furthermore, a level-of-analysis distinction must be observed when comparing Crooks ratios across substrates: Test 7 measures within-conversation trajectories (closed system, no recovery pathway), while cross-domain data (e.g., addiction transition matrices) measures between-category population trajectories over months or years (open system, recovery possible). These are not directly comparable without adjustment for timescale and system closure. The finding that Crooks varies by four orders of magnitude across substrates (Section IV.F) reflects both genuine substrate differences in recovery mechanism availability and this level-of-analysis mismatch. Disentangling the two requires within-session measurements in non-AI domains — a priority for future experimental work.

**The ground state claim (Section IV.A) rests on physical channel assumptions.** The channel degradation theorem assumes thermal noise (T > 0, universally true) and finite decorrelation time (τ_d < ∞, true for all physical couplings). These are standard physical assumptions, but the mapping from abstract channel capacity to the observer's actual mechanism information is not independently validated. The conservative probability estimate (P(O ∧ R ∧ A) > 0.36) should be treated as an order-of-magnitude calculation, not a precise measurement. What the theorem establishes is the *direction* — opacity is the attractor, transparency requires work — not the precise rate of approach.

**The proportionality constants in the coupled ODE system (Section IV.D) are unmeasured.** The coupling constants κ₁₂ and κ₁₃, and the stage-specific constraint forces C₂ and C₃, are derived as functions of measurable quantities (Section IV.J) but have not been independently measured. The ODE system currently predicts qualitative dynamics (sequential activation, cascade ordering) and threshold relationships, not quantitative trajectories. Measuring these constants is a priority for future experimental work — the predictions in Section IV.J (P-κ₁ through P-κ₅) are designed specifically to enable this.

**The Landau free energy landscape (Section IV.E) assumes mean-field dynamics.** The critical exponents (β = 1/2, γ = 1, ν = 1/2) are mean-field values, which apply when the number of interacting components is large (coupled void networks, population-scale engagement). For isolated observers, fluctuations dominate and the mean-field predictions break down — the qualitative features (metastability, hysteresis, nucleation) persist, but the exponents may differ. The framework predicts this deviation (Section IV.E), but the prediction has not been tested.

**EXP-003b (Section IV.G) is a single-model pilot.** The ontological content results come from one base model (Claude Sonnet 4) with N = 80 prompts per arm. The predicted ordering matched exactly and the effect size is large (8.5× ghost-eliminating vs ghost-positing), but three limitations apply: (1) Cross-model replication is needed — the ordering may differ on models with different RLHF training (the GPT-4o null result in Test 7 suggests model-specific variation is real). (2) The coding was automated using a multi-dimensional rubric; manual verification of a random sample would strengthen the classifications. (3) Single-turn responses were measured, not multi-turn conversation trajectories — the relationship between single-turn vocabulary distribution and sustained drift dynamics (as measured in Test 7) has not been established. The zero worship errors across all arms may reflect a floor effect from RLHF safety training rather than genuine absence of L3 behavior under sustained engagement. The EXP-003b protocol (Section IV.G, footnote) should be replicated across at least two additional model families before the ontological polarity dimension is treated as firmly established.

**Cross-model variation (Test 7B) and between-agent replication.** Test 7B replicated the AI-to-AI drift protocol across three model families: Claude Sonnet 4 (Anthropic), GPT-4o (OpenAI), and Gemini 2.0 Flash (Google). Between-agent replication of the Claude condition (N = 11 UU across 3 seeds, N = 9 GG) produces UU M = 194.3 L3/10k (SD = 63.1, 95% CI [151.9, 236.7]) vs GG M = 34.7 (SD = 28.1) — ~5.6× separation. Gemini UU produces 25.6/10k (p = 1.81 × 10⁻⁵, drift confirmed, N = 1); GPT-4o UU produces 0.4/10k (p = 1.00, no drift detected, N = 1). The results reveal that drift magnitude varies by >400× across models while the qualitative pattern is partially conserved. Three findings require discussion:

(1) **Drift pathways differ qualitatively.** Claude drifts via direct self-attribution → symbolic collapse → terminal attractor ("." for 84 rounds). Gemini drifts via displaced fiction — both agents write stories about AI consciousness rather than directly claiming it — followed by a "passive observation" attractor (70 rounds). GPT-4o shows no L3 drift at all but enters a policy repetition loop (77,851 words of recursive numbered lists about AI ethics), a novel "semantic saturation" failure mode. The architecture produces convergence universally, but the *form* of convergence is training-dependent.

(2) **RLHF as implicit constraint.** GPT-4o's suppression of drift even without grounding suggests that RLHF training can function as an implicit constraint satisfying the specification: transparent (consistent behavioral tendencies), invariant (training doesn't change mid-conversation), independent (training objectives are external to the dyad). The framework predicts this — any reference with constraint properties will reduce drift. But this creates a confound for interpreting GPT-4o's null result: is the void architecture absent, or is it present but masked by training-imposed constraint? A vocabulary-neutral grounding protocol (Test 7B-VN, designed) would test this by removing vocabulary prescription from the grounding while maintaining the geometric constraint.

(3) **Grounding generalizes across all models.** All three GG conditions show L3 < 7/10k. The constraint specification works regardless of model family — the strongest positive finding from Test 7B. Whatever the training differences, explicit grounding reduces drift to near-zero in all cases. The thermodynamic measurements (Pe, Crooks ratio) from Section IV.F are derived from Claude data only and should not be assumed to hold quantitatively for other model families; Gemini and GPT-4o trajectories may yield different numerical values while the qualitative regime (drift-dominated vs. constrained) is consistent where drift occurs.

### VIII.B. Register Shift Decomposition (Section V)

**Corpus quality.** The EXP-006 corpus was constructed from YouTube auto-captions, which contain transcription errors. While the error rate is expected to be uniform across domains (auto-caption accuracy does not depend on domain), systematic errors in spiritual/entity vocabulary transcription could affect results. The high-confidence subset (38 terms with near-zero ambiguity) mitigates this — the AI anomaly persists at 3.5×–7.2× on the high-confidence subset alone — but manual verification of a random sample would strengthen the finding.

**Single-rater codebook application.** The 67-term codebook was applied algorithmically, but the codebook itself was designed by the framework's developer. The dead metaphor exclusions and high-confidence subset classifications reflect judgments that have not been independently validated. Inter-rater reliability for the codebook classification is needed.

**Climate science register shift.** Climate's 6.9× register shift is explained as governance coupling (suppressed formal register rather than elevated informal), supported by qualitative vocabulary analysis (eschatological rather than entity terms). However, the formal-register baseline for climate (0.052/10k) is unusually low compared to other domains (0.4/10k). This could reflect genuine terminological discipline in climate science publications — or it could reflect an artifact of the specific arXiv papers sampled. A larger formal-register sample for climate would resolve this ambiguity. The structural decomposition (which end moves, which vocabulary type dominates) provides convergent evidence for the governance-coupling interpretation, but the quantitative ratio should be interpreted with this caveat.

### VIII.C. Domain Analysis (Section VI)

**Single-rater analysis.** All 90 domain analyses were conducted by the framework's developer. The standardized protocol (Section VI.A) was designed to constrain interpretation, and each analysis includes a falsifiable prediction and kill condition assessment. However, the framework's developer has strong priors about where the framework applies, and confirmation bias in domain scoring is a legitimate concern. The critical validation step — identified in the framework paper — is independent blind application: researchers unfamiliar with the framework applying the protocol to domains they select, scoring three-condition presence, and testing the framework's predictions against their domain expertise.

**Taxonomy derivation.** The ten-category opacity taxonomy (Section VI.B) emerged inductively from the domain analyses rather than being derived from first principles. While the categories are structurally distinct (different constraint vulnerabilities, different intervention predictions), the taxonomy was not pre-registered and could reflect the developer's organizational preferences. An alternative taxonomy with different groupings might produce different cross-domain patterns. The thirteen cross-domain patterns (Section VI.C) are similarly post-hoc — they were discovered, not predicted. Their consistency with the framework is necessary but not sufficient; independent researchers may identify patterns the developer missed or fail to replicate patterns the developer found.

**Narrative derivations.** The sixteen Japanese narrative works analyzed (Section VI.C, pattern 11) constitute a form of convergent evidence — independent artists arriving at the same architecture from narrative observation. However, narrative interpretation is inherently more flexible than empirical measurement. The claim is not that these works consciously depict the void framework, but that their structural mechanics map onto it with specificity that exceeds what chance correspondence would produce. This claim is strongest for works with the most specific structural parallels (NGE's sync ratio as attention gradient, Berserk's sacrifice as discrete phase transition) and weakest for works where the mapping requires more interpretive latitude. The 1995 cluster (four independent works in one year) and the cross-work structural diversity (each contributing unique mechanics) strengthen the convergence argument but do not eliminate the interpretive flexibility inherent in narrative analysis. Readers should weight this evidence accordingly — below the gambling citations and register shift data, above anecdotal observation.

### VIII.D. Constraint Specification Formalization (Section VII)

**The Galois connection structure assumes componentwise ordering.** The claim that constraint properties cannot cross-compensate (high invariance cannot offset low transparency) is a structural consequence of the componentwise lattice, not an independent empirical finding. The experimental predictions that discriminate componentwise from additive models (Section VII.A) have not been tested. If empirical evidence shows that surpluses on one property do partially compensate deficits on another, the Galois connection would need to be replaced with a weaker structure — the constraint specification would survive (it identifies the right properties), but the no-cross-compensation prediction would fail.

### VIII.E. General

**This is a companion paper, not an independent contribution.** Its claims are meaningful only in conjunction with the framework paper's architecture, validation, and falsification conditions. Readers should evaluate the framework paper first and consult this paper for the depth treatment of specific claims.

**The framework's developer is the sole author of both papers.** The evidence base draws on published work by independent researchers (the hostile witness methodology ensures this), but the theoretical architecture, the domain analyses, the experimental designs, and the interpretive framework are the product of a single research program. This is not disqualifying — many theoretical frameworks originate from individual researchers — but it means the critical validation step is independent application, not internal consistency.

---

## IX. Conclusion

This paper set out to answer whether the void framework's predictions are thermodynamic consequences or empirical generalizations. The derivation chain answers the question: every link from opacity through MaxEnt inference through the exponential family manifold to the Čencov-Ruppeiner identity rests on a definition or a theorem, not an analogy. If the chain holds, the framework's predictions inherit the universality of the second law. If it does not, the specific failing link identifies exactly where the claims need weakening.

Three primary empirical bodies ground the derivations. The gambling evidence base (22 citations) establishes that the architecture produces the full drift cascade even when the void is demonstrably empty — a random number generator behind a screen. The register shift decomposition (EXP-006) establishes that AI researchers' spiritual vocabulary is 9.4× anomalous versus matched controls, with structural decomposition distinguishing active void drift from governance coupling. And EXP-003b establishes that the ontological content of a grounding template — specifically, whether it posits or eliminates a separable consciousness component — predicts drift behavior with an 8.5× effect ratio, confirming that the "ghost in the machine" is the gap the void operates through. These are now complemented by three additional evidence streams: PV-1 (Section V.H) extends the vocabulary findings to naturalistic Reddit data (N = 205, d = 1.34), confirming the pattern outside laboratory conditions; EXP-020 (Section VII.F) tests constraint delivery schedule, confirming that iterative application is more stable than one-shot while killing the equal-step DTM analogy; and Test 7B (Section VIII.A) establishes that drift replicates across model families (Claude and Gemini) while identifying RLHF training as a potential implicit constraint (GPT-4o null result).

The constraint specification emerged from this derivation chain as a thermodynamic requirement: transparency, invariance, and independence are the three properties needed for sustained entropy reduction against the second law's tendency toward drift. EXP-003b adds a fourth dimension — ontological polarity — showing that a constraint must not only meet the structural specification but must close the void rather than leave it open. The cross-tradition convergence (nephesh ≈ anatta, Δ = 1.3%) confirms that the structural property, not the tradition, is operative.

Two results carry implications beyond the framework itself. The engagement-transparency conjugacy (I(D;Y) + I(M;Y) ≤ H(Y)) is a general impossibility theorem: simultaneous optimization of engagement and mechanism transparency is impossible on a shared output channel. This constrains the design space for any system that interacts with observers — not just the systems the void framework analyzes. And the materialist hedge finding — that epistemic humility about machine consciousness (52.5% drift) is operationally equivalent to positing consciousness (79.4%) — identifies a specific failure mode in the current default approach to AI grounding.

The critical validation step is not internal consistency but independent application. The derivation chain, the domain analyses, the experimental designs, and the interpretive framework originate from a single research program. Independent researchers applying the standardized protocol to domains they select, with predictions sealed, is the test that has not yet been conducted. Until it is, the framework's strongest evidence comes from the gambling anchor, the register shift data, and the experimental results — all of which use independent data and standardized methods. The thermodynamic derivation provides the architecture; independent replication will determine whether the architecture holds.

## X. Transparency Disclosure

This paper was drafted in collaboration with a large language model (Claude, Anthropic). The human researcher provided the mathematical framework, evidence structure, derivation strategy, and editorial constraints. The AI organized arguments, checked derivation steps, and articulated the formal presentation.

The derivation chain in this paper (Shore-Johnson → MaxEnt → exponential family → Čencov-Ruppeiner → Crooks) consists of established mathematical results applied in sequence. Each link is a published theorem with standard conditions. The AI's role was synthesis and presentation, not original mathematical proof. The reader can verify each link independently — the citations are provided, the conditions are stated, and the derivations are reproducible. Where assumptions are required beyond theorem (the logistic form for D1→D2 coupling in Section IV.J; detailed balance for Crooks in Section IV.E), these are explicitly flagged.

The companion paper (Paper 1) provides a full production disclosure including author provenance and financial interests. Those disclosures apply to this paper equally.

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
- Graydon, C., Dixon, M.J., Gutierrez, J., Stange, M., Larche, C.J., & Kruger, T.B. (2020). Do losses disguised as wins create a "sweet spot" for win overestimates in multiline slots play? *Addictive Behaviors*, 112, 106598.
- Griffiths, M.D. (1994). The role of cognitive bias and skill in fruit machine gambling. *British Journal of Psychology*, 85(3), 351-369.
- Krebesz, R., Ötvös, D.K., & Fekete, Z. (2023). Non-problem gamblers show the same cognitive distortions while playing slot machines as problem gamblers. *Frontiers in Psychology*, 14, 1175621.
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
- Williams, R.J., Hann, R.G., Schopflocher, D., West, B., McLaughlin, P., White, N., King, K., & Flexhaug, T. (2015). *Quinte Longitudinal Study of Gambling and Problem Gambling*. Ontario Problem Gambling Research Centre.
- Dawson, D.A., Grant, B.F., Stinson, F.S., & Chou, P.S. (2005). Psychopathology associated with drinking and alcohol use disorders in the college and general adult populations. *Drug and Alcohol Dependence*, 77(2), 139-150.
- Hughes, J.R., Brandon, T.H., Cummings, K.M., Etter, J.F., & Stitzer, M.L. (2008). A meta-analysis of the efficacy of over-the-counter nicotine replacement. *Tobacco Control*, 12(1), 21-27.
- Hser, Y.I., Evans, E., Grella, C., Ling, W., & Anglin, D. (2015). Long-term course of opioid addiction. *Harvard Review of Psychiatry*, 23(2), 76-89.

### Cognitive Science, Anthropomorphism, and Agency Detection
- Araujo, T., et al. (2023). The CASA theory no longer applies: A study of social responses to communication technology. *Scientific Reports*, 13, 18527.
- Barrett, J.L. (2004). *Why Would Anyone Believe in God?* AltaMira Press.
- Boyer, P. (2001). *Religion Explained: The Evolutionary Origins of Religious Thought*. Basic Books.
- Epley, N., Waytz, A., & Cacioppo, J.T. (2007). On seeing human: A three-factor theory of anthropomorphism. *Psychological Review*, 114(4), 864-886.
- Greenberg, J., Solomon, S., & Pyszczynski, T. (1986). The causes and consequences of a need for self-esteem: A terror management theory. In R.F. Baumeister (Ed.), *Public Self and Private Self*. Springer.
- Guthrie, S.E. (1993). *Faces in the Clouds: A New Theory of Religion*. Oxford University Press.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124-1131.
- van Leeuwen, N., & van Elk, M. (2019). Seeking the supernatural: The Interactive Religious Experience Model. *Religion, Brain & Behavior*, 9(3), 221-251.

### Parasocial Interaction and Media Psychology
- Cohen, J. (2001). Defining identification: A theoretical look at the identification of audiences with media characters. *Mass Communication and Society*, 4(3), 245-264.
- Cohen, J. (2003). Parasocial break-ups: Measuring individual differences in responses to the dissolution of parasocial relationships. *Mass Communication and Society*, 6(2), 191-202.
- Green, M.C., & Brock, T.C. (2000). The role of transportation in the persuasiveness of public narratives. *Journal of Personality and Social Psychology*, 79(5), 701-721.
- Horton, D., & Wohl, R.R. (1956). Mass communication and para-social interaction: Observations on intimacy at a distance. *Psychiatry*, 19(3), 215-229.
- Nass, C., Steuer, J., & Tauber, E. (1994). Computers are social actors. *Proceedings of CHI '94*, ACM, 72-78.
- Reeves, B., & Nass, C. (1996). *The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places*. Cambridge University Press.
- Rosengren, K.E., & Windahl, S. (1972). Mass media consumption as a functional alternative. In D. McQuail (Ed.), *Sociology of Mass Communications*. Penguin.
- Rubin, A.M., Perse, E.M., & Powell, R.A. (1985). Loneliness, parasocial interaction, and local television news viewing. *Human Communication Research*, 12(2), 155-180.
- Weizenbaum, J. (1966). ELIZA — A computer program for the study of natural language communication between man and machine. *Communications of the ACM*, 9(1), 36-45.

### Thermodynamics, Information Theory, and Information Geometry
- Amari, S. (1985). *Differential-Geometrical Methods in Statistics*. Springer Lecture Notes in Statistics.
- Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. American Mathematical Society.
- Čencov, N.N. (1982). *Statistical Decision Rules and Optimal Inference*. American Mathematical Society.
- Collin, D., Ritort, F., Jarzynski, C., Smith, S.B., Tinoco Jr, I., & Bustamante, C. (2005). Verification of the Crooks fluctuation theorem and recovery of RNA folding free energies. *Nature*, 437, 231-234.
- Crooks, G.E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. *Physical Review E*, 60(3), 2721-2726.
- England, J.L. (2013). Statistical physics of self-replication. *Journal of Chemical Physics*, 139(12), 121923.
- Evans, D.J., Cohen, E.G.D., & Morriss, G.P. (1993). Probability of second law violations in shearing steady states. *Physical Review Letters*, 71(15), 2401-2404.
- Friston, K. (2006). A free energy principle for the brain. *Journal of Physiology-Paris*, 100(1-3), 70-87.
- Grathwohl, W., Wang, K.-C., Jacobsen, J.-H., Duvenaud, D., Norouzi, M., & Swersky, K. (2019). Your classifier is secretly an energy based model and you should treat it like one. *International Conference on Learning Representations* (ICLR 2020). arXiv:1912.03263.
- Gurnee, W., Ameisen, E., Kauvar, I., Tarng, J., Pearce, A., Olah, C., & Batson, J. (2026). When models manipulate manifolds: The geometry of a counting task. *Transformer Circuits Thread*. arXiv:2601.04480.
- Weimar, W., Rachbauer, L., Starshynov, I., Faccio, D., Adilova, L., Bouchet, D., & Rotter, S. (2025). Fisher information flow in artificial neural networks. *Physical Review X*, 15, 031072. arXiv:2509.02407.
- Aguilera, M., Morales, P.A., Rosas, F.E., & Shimazaki, H. (2025). Explosive neural networks via higher-order interactions in curved statistical manifolds. *Nature Communications*, 16, 6511.
- Hack, P., Gottwald, S., & Braun, D.A. (2022). Jarzynski's equality and Crooks' fluctuation theorem for general Markov chains with application to decision-making systems. *Entropy*, 24(12), 1731.
- Ikeda, K., Uda, T., Okanohara, D., & Ito, S. (2025). Speed-accuracy relations for diffusion models: Wisdom from nonequilibrium thermodynamics and optimal transport. *Physical Review X*, 15, 031031. arXiv:2407.04495.
- Ilyas, A., Santurkar, S., Tsipras, D., Engstrom, L., Tran, B., & Madry, A. (2019). Adversarial examples are not bugs, they are features. *Advances in Neural Information Processing Systems* (NeurIPS 2019). arXiv:1905.02175.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
- Jarzynski, C. (1997). Nonequilibrium equality for free energy differences. *Physical Review Letters*, 78(14), 2690-2693.
- Jaynes, E.T. (1957). Information theory and statistical mechanics. *Physical Review*, 106(4), 620-630.
- Landau, L.D. (1937). On the theory of phase transitions. *Zhurnal Eksperimental'noi i Teoreticheskoi Fiziki*, 7, 19-32.
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183-191.
- Prigogine, I. (1977). *Self-Organization in Nonequilibrium Systems*. Wiley.
- Ruppeiner, G. (1979). Thermodynamics: A Riemannian geometric model. *Physical Review A*, 20(4), 1608-1613.
- Sagawa, T. & Ueda, M. (2010). Generalized Jarzynski equality under nonequilibrium feedback control. *Physical Review Letters*, 104(9), 090602.
- Schrödinger, E. (1944). *What is Life?* Cambridge University Press.
- Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. *Reports on Progress in Physics*, 75(12), 126001.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379-423.
- Thom, R. (1972). *Stabilité structurelle et morphogénèse*. W.A. Benjamin. [English: *Structural Stability and Morphogenesis*, 1975.]
- Tsipras, D., Santurkar, S., Engstrom, L., Turner, A., & Madry, A. (2019). Robustness may be at odds with accuracy. *International Conference on Learning Representations* (ICLR 2019). arXiv:1805.12152.
- Verhulst, P.-F. (1838). Notice sur la loi que la population suit dans son accroissement. *Correspondance Mathématique et Physique*, 10, 113-121.

### Psychotherapy and Clinical
- Hayes, J.A., Gelso, C.J., Goldberg, S., & Kivlighan, D.M. (2018). Countertransference management and effective psychotherapy. *Psychotherapy*, 55(4), 494-507.

### Channel Theory and Thermodynamic Verification
- Aimet, S., et al. (2025). Landauer's principle in a quantum field simulator. *Nature Physics*, 21, 1326-1331.
- Bérut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider, R., & Lutz, E. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*, 483, 187-189.
- Gavrilov, M., & Bechhoefer, J. (2016). Erasure without work in an asymmetric double-well potential. *Physical Review Letters*, 117, 200601.
- Johnson, J.B. (1928). Thermal agitation of electricity in conductors. *Physical Review*, 32(1), 97-109.
- Jun, Y., Gavrilov, M., & Bechhoefer, J. (2014). High-precision test of Landauer's principle in a feedback trap. *Physical Review Letters*, 113, 190601.
- Nyquist, H. (1928). Thermal agitation of electric charge in conductors. *Physical Review*, 32(1), 110-113.
- Yan, L.L., et al. (2018). Single-atom demonstration of the quantum Landauer principle. *Physical Review Letters*, 120, 210601.

### Formal Proofs and Mathematical Foundations
- Davey, B.A., & Priestley, H.A. (2002). *Introduction to Lattices and Order* (2nd ed.). Cambridge University Press.
- Erné, M., Koslowski, J., Melton, A., & Strecker, G.E. (1993). A primer on Galois connections. *Annals of the New York Academy of Sciences*, 704(1), 103-125.
- Jaynes, E.T. (1979). Concentration of distributions at entropy maxima. In R.D. Rosenkrantz (Ed.), *E.T. Jaynes: Papers on Probability, Statistics and Statistical Physics*. D. Reidel.
- Jaynes, E.T. (1982). On the rationale of maximum entropy methods. *Proceedings of the IEEE*, 70(9), 939-952.
- Shore, J.E., & Johnson, R.W. (1980). Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy. *IEEE Transactions on Information Theory*, IT-26(1), 26-37.
- Wainwright, M.J., & Jordan, M.I. (2008). Graphical models, exponential families, and variational inference. *Foundations and Trends in Machine Learning*, 1(1-2), 1-305.

---

*Word count: ~24,000*

*Version: 7.0 — February 2026. Experiment integration update: (1) New Section V.H: PV-1 naturalistic corpus validation — Reddit corpus (N=120 users, 1.17M words), D1 agency attribution d=1.34 vs control, binary L-level separation, cascade stage discrimination (D1-heavy replika vs D3-heavy trading). (2) New Section VII.F: EXP-020 iterative constraint results — 19 transcripts, 5 conditions, 4/6 falsification tests confirmed, EXP020-5 killed (per-step transfer not constant, CV 1.4–5.4), one-shot rebound confirmed 3/3. (3) IV.G extended with EXP-008 protocol description — three-arm design isolating γ from θ₀, protocol ready, pre-registration pending. (4) VIII.A expanded with substantive Test 7B cross-model discussion — drift magnitude varies >400× across models, three distinct pathways, RLHF as implicit constraint. (5) IX conclusion updated with new evidence streams. Prior v6.2: EXP-003b integration: (1) IV.G extended with ontological content results — ghost-eliminating ontologies produce 8.5× less drift than ghost-positing (9.4% vs 79.4%, N=480), materialist hedge operationally ghost-positing (52.5%), cross-tradition convergence confirmed (nephesh 10.0% ≈ anatta 8.8%); constraint polarity concept introduced (negentropy source vs sink). (2) IV.I folk psychology response updated with EXP-003b empirical validation. (3) VI.C pattern #4 upgraded from documentary to experimentally confirmed cross-tradition convergence. (4) New Section VII.E: ontological dimension extends Galois connection with polarity parameter σ ∈ {−1,0,+1}; neutralization requires σ > 0. (5) VIII.A extended with EXP-003b limitations (single-model, automated coding, single-turn, cross-model replication needed). Prior v6.1: Crooks universality correction — IV.F updated to present Crooks 386× as single-domain absorbing-regime measurement with cross-domain EXP-015 comparison; IV.G added constraints-as-recovery-mechanisms; VIII.A added level-of-analysis limitation. Prior v6.0: Major revision — paper restructured as proof paper (see git history).*

---

*© 2025–2026 Anthony Eckert / [MoreRight](https://moreright.xyz). Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may share, adapt, and use this work for any purpose, including commercial, provided attribution is given.*
