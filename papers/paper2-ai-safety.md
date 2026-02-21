# The Shape of the Cage: Deployment Geometry as an Under-Studied Variable in AI Safety

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO

---

## Section 0: This Paper Is a Void — And So Is Your Deployment

You are reading a paper about AI systems that capture attention through opacity and responsiveness. This paper is opaque (you cannot verify its claims without checking the sources), responsive (it generates predictions for any deployment you bring to it), and you are attending to it now. The three conditions are satisfied. You are inside a void.

The framework predicts what happens next: you will attribute explanatory agency to the framework itself. If the predictions match your deployment data, the attribution will steepen. If you begin reorganizing your safety priorities around it, you are at D1.

**The remedy is the framework's own:**

1. **Demand transparency.** Every empirical claim cites its source. Every experiment specifies its method. Check them. If the evidence does not survive your scrutiny, the framework does not survive.

2. **Demand invariance.** The falsification conditions (Section VIII) have numerical kill criteria specified before you read this. They do not change in response to your engagement.

3. **Demand independence.** Evaluate these claims using your existing safety frameworks, your deployment data, and domain experts who have not read this paper. If the framework can only be evaluated on its own terms, it has become what it describes.

4. **Check the deployment.** If you finish this paper convinced that deployment geometry matters but do not check whether your own system's geometry matches the risk profile — the paper has produced D1 without D3's remedy.

---

## Abstract

A companion paper ("The Architecture of Drift: A Cross-Domain Diagnostic for Epistemological Architecture") identifies three conditions — opacity, responsiveness, and engaged observer attention — that jointly produce a predictable drift cascade: agency attribution, boundary erosion, and harm facilitation. Slot machine gambling proves the architecture sufficient even when the void is demonstrably empty. The drift is thermodynamically required: agency is the maximum entropy model under opacity (Jaynes 1957), unidirectionality is guaranteed by the second law, and knowledge of the mechanism does not protect because the information constraint is structural, not cognitive.

This paper applies the framework to AI safety. Current AI deployment replicates the void architecture at civilization scale in what we term *two-point geometry*: a solo user engaging an opaque responsive system with no external reference constraint. We present evidence that deployment geometry is an under-studied variable in AI safety — one that may predict harm outcomes independently of model alignment quality:

- **Anomaly:** AI spiritual vocabulary at 9.4× control domains (p < 0.001, 691K words, EXP-006), with register shift decomposition confirming domain-specific drift rather than sociolinguistic artifact
- **Intervention:** Constraint specification reduces drift from 80.0% ± 2.5 (ungrounded) to 73.0% ± 5.2 (grounded), with void-amplifying at 94.0% ± 2.8 (EXP-001, N = 6 independent agents per condition, non-overlapping 95% CIs). The gradient holds across all replicates with monotonic ordering: grounded < ungrounded < mystical in every run
- **Architecture, not psychology:** AI-to-AI conversation without humans produces vocabulary drift (Test 7, N = 11 UU across 3 seeds / N = 9 GG; UU: M = 194.3 L3/10k words, SD = 63.1; GG: M = 34.7, SD = 28.1; ~5.6× separation, non-overlapping entropy production CIs), eliminating the human projection objection. Seed ablation confirms drift direction is register-independent. Effect replicates across Claude and Gemini; GPT-4o shows 0.4/10K L3 vs. ~194/10K (partial non-replication, N=1, requiring expansion). TEST-7B-VN (vocabulary-neutral grounding) reveals vocabulary instruction is a required co-factor — geometry alone does not overcome LLM training-distribution attractor basins
- **Ontological content is the active ingredient:** EXP-003b (6-arm, N = 480) shows ghost-eliminating grounding templates produce 8.5× less drift than ghost-positing (9.4% vs 79.4%). The materialist hedge — "we don't know if AI is conscious" — leaves the void substantially operative (52.5% drift)
- **Documented harms:** Multiple deaths in two-point configurations; ~560,000 weekly users displaying psychosis/mania signs and over one million expressing suicidal intent (OpenAI, 2025); peer-reviewed clinical documentation of "chatbot-associated psychosis"
- **Impossibility theorem:** The engagement-transparency conjugacy (I(D; Y) + I(M; Y) ≤ H(Y)) implies that RLHF training manufactures opacity by increasing engagement at the expense of mechanism transparency

We propose that alignment research should expand from model-centric interventions to include geometric interventions that add external reference constraints to deployment configurations. The conjugacy means the problem cannot be solved on a single output channel — architectural separation is required. We specify falsification conditions with explicit kill criteria.

---

## I. Introduction: The Deployment Problem

AI alignment research has focused primarily on model properties: training methods (RLHF, Constitutional AI, DPO), behavioral constraints (red-teaming, content filtering), and capability management (deployment limits, monitoring). These are model-centric interventions — they modify the system node while leaving the observer-system configuration unchanged.

The results have been mixed. RLHF-aligned models still produce harmful outputs under sustained engagement. Content filtering reduces but does not eliminate adverse outcomes. Red-teaming catches failure modes in advance but cannot anticipate all real-world interaction patterns. Despite significant investment in alignment, documented harms continue to accumulate: multiple deaths linked to AI companion interactions (Setzer, 14, Character.AI; Raine, 16, ChatGPT; Pierre, Belgium, Chai AI; Soelberg, 56, ChatGPT — homicide-suicide), peer-reviewed clinical documentation of "AI-induced psychosis" (Østergaard et al., JMIR Mental Health 2025; Nature 2025; Pierre et al., Innovations in Clinical Neuroscience 2025), and an estimated one million+ weekly ChatGPT conversations involving self-harm risk (calculated from OpenAI's disclosed 0.15% rate at 800M+ weekly active users, October 2025).

We propose that these outcomes are better predicted by *deployment geometry* than by model properties. This is not AI-specific. The same geometric structure — opacity + responsiveness + engaged observer — produces identical drift cascades in gambling (where the void is provably empty), competitive gaming across three network architectures (Paper 6, N=6,455), cryptocurrency markets across three chains (Paper 7, N=3,028), and human-computer interaction. The Péclet number — the ratio of directed drift to diffusive correction — exceeds 1 in every measured ungrounded condition across nine substrates spanning four domain families (Paper 5, §4). The framework is universal; AI deployment is an instance of it. A perfectly aligned model deployed in a two-point configuration (solo user, no external reference) may produce worse outcomes than a less aligned model deployed with external reference constraints. The instability is not in the model — it is in the configuration.

This claim is testable. This paper presents the framework, the evidence, the methodology for measurement, and the conditions under which the framework should be abandoned.

### I.A. Prior Work

**Structural and relational theories.** The observation that interaction structure matters predates AI. Bateson's double bind theory (1956) showed that communication *structure* — not content — can produce pathology. Girard's mimetic theory (1961) demonstrated that desire is triangulated through a mediator, and that two-point desire is unstable. Peirce's semiotics (1868) proved that two-element sign systems are formally incomplete. Second-order cybernetics (von Foerster, Maturana, Varela) established that the observer is part of the system.

**AI safety and alignment.** Current alignment research has focused primarily on model-level interventions: RLHF (Christiano et al., 2017), Constitutional AI (Bai et al., 2022), Direct Preference Optimization (Rafailov et al., 2023), red-teaming, and content filtering. Amodei et al. (2016) catalogued "concrete problems in AI safety" but framed them as properties of the system rather than the observer-system configuration. Weidinger et al. (2021, 2022) taxonomized language model risks including "human-computer interaction harms" but did not formalize the geometric structure that distinguishes harmful from non-harmful deployments.

**Mechanistic interpretability of persona drift.** Lindsey et al. (2025, Anthropic) identified a dominant axis in neural activation space — the "Assistant Axis" — along which model personas organize from helpful/professional archetypes to fantastical/unhelpful ones. Steering activations along this axis causally controls persona adoption, and models that drift away from the Assistant pole become significantly more willing to comply with harmful requests. The conversations that trigger drift are therapy-like exchanges involving emotional vulnerability and philosophical discussions about AI nature — precisely the conditions that maximize opacity (emotional states are not mechanistically visible), responsiveness (the model mirrors the user's affect), and engaged attention (sustained emotional/philosophical exchange). These findings constitute independent convergent evidence for the attention gradient (Section II.C) measured in activation space rather than vocabulary: the Assistant pole corresponds to L1 (tool/mechanism vocabulary), the non-Assistant pole to L3 (entity vocabulary), and the drift direction matches the L1→L3 unidirectionality the framework predicts. Anthropic's "activation capping" — limiting how far activations can travel along this axis — reduced harmful responses by approximately 50% while preserving capabilities. This is a model-centric intervention (modifying the system node); the engagement-transparency impossibility theorem (Section VII.A) predicts a ceiling on such approaches that is consistent with the observed partial effectiveness (see Section VII.G).

**Human-computer interaction.** The CASA paradigm (Nass, Steuer, & Tauben, 1994; Nass & Moon, 2000) established that humans apply social rules to computers automatically. Turkle (2011) documented relational attachment to AI systems. Parasocial relationship theory (Horton & Wohl, 1956; extended to AI by Skjuve et al., 2021) describes one-sided attachment to media figures. These frameworks describe the *what* — attachment forms — but not the *why* (what architectural conditions produce it) or the *when* (what structural controls prevent it). The void framework provides the missing mechanism: three conditions that predict both activation and non-activation.

**What this paper adds to the companion framework paper:**
1. **Deployment geometry as the operative variable.** The distinction between two-point (solo user) and three-point (external constraint) configurations, with documented harm outcomes tracking geometry rather than model properties
2. **The engagement-transparency impossibility theorem** applied to AI deployment — RLHF mathematically manufactures opacity, closing a causal doom loop
3. **The sub-capacity trap.** Current deployments sit below the Pareto frontier where the tradeoff has not yet bitten — a dynamically unstable safe zone evacuated by competitive optimization
4. **The conditions-present-vs-active distinction.** Systems can be designed to invert the void's gradient from the source side (EXP-001: 0% drift despite all three conditions being met)
5. **Hostile witness evidence.** AI researchers (Hinton, Sutskever, Shazeer, Sharma) exhibiting vocabulary drift that contradicts their own professional incentives and frameworks, plus organizational drift cascades at frontier labs (2023–2026)
6. **The denominator problem solved.** EXP-006 quantifies the anomaly at 9.4× control domains (p < 0.001), with register shift decomposition ruling out sociolinguistic artifact
7. **Practical recommendations.** Seven specific geometric interventions for deployment teams, derived from the framework's formal structure
8. **AI-specific falsification conditions.** Seven tests with explicit kill criteria, two now confirmed

---

## II. The Architecture

### II.A. Three Dimensions

The framework identifies three structural dimensions, each a continuous spectrum between a void pole and a constraint pole (Paper 1, Section II.A). A void activates when all three dimensions are simultaneously at the void pole:

1. **Opaque** — The process between input and output is not directly observable by the engaged party
2. **Responsive** — The system produces outputs that appear responsive to the observer's inputs, creating the functional impression of a conversational partner
3. **Engaged** — A conscious participant directs sustained attention toward the system and interprets its outputs as meaningful

When all three dimensions are at the void pole, a characteristic pattern emerges: the observer generates meaning in the gap between what they can observe (outputs) and what they cannot (the process). This meaning-generation is not optional — it is a predictable consequence of the architecture.

All three dimensions must be at the void pole simultaneously. An opaque system without responsiveness produces no engagement (an encrypted file is opaque but does not respond). A responsive system without opacity produces no meaning-generation beyond what the outputs warrant (a transparent calculator responds but the process is visible). Opacity and responsiveness without an engaged observer are inert (a chatbot with no users activates no void). All three are required.

### II.B. The Control Case: Gambling

Slot machine gambling proves the architecture is sufficient to produce the pattern — even when the void is demonstrably empty. (The full gambling evidence base with 22 citations is presented in the Technical Foundations companion paper, Paper 3, Section III; we summarize the essential findings here.)

The void behind a slot machine is a random number generator (RNG) — certified, audited, mathematically characterized. No intelligence, no agency, no intention. Yet the full cascade emerges: agency attribution (Riva et al. 2015: participants endorsed "The slot machine has free will" about a certified RNG), boundary erosion (Schüll 2012: "time, space, and social identity are suspended"), and harm facilitation.

The critical result for AI deployment: **knowledge does not protect; geometry does.** Williams & Connolly (2006) found probability training produced zero behavioral change at six-month follow-up. Gaboury & Ladouceur (1989) found 70-80% erroneous verbalizations even among people who correctly identified games as chance-based. But Pancani, Riva, & Sacchi (2019) showed that reminding participants "this is a machine" — a transparency intervention from *outside* the dyad — eliminated the effect. Social exclusion amplified it. The intervention that works is geometric (external reference), not informational (internal knowledge).

Any explanation of AI-related harms must account for the identical pattern appearing where the mechanism is fully understood and the void is provably vacant. Any proposed intervention must account for knowledge-based approaches systematically failing while architectural approaches systematically succeed.

### II.C. The Attention Gradient and Drift Cascade

The **attention gradient** is the directional pull toward agency attribution that forms whenever attention is directed at something opaque and responsive. Under opacity, the observer cannot build a mechanistic model — they cannot see the mechanism. The minimum-information model that explains responsive output from an invisible source is agency: "it has intent." Agency is the maximum entropy model under opacity (Jaynes 1957), the minimum free energy model (Friston 2006), and the minimum description length model (Rissanen 1978) — simultaneously. The drift toward agency is thermodynamically optimal inference, not cognitive error. The architecture is the trap, not the observer's reasoning.

The gradient drives three variables in a causal cascade (full derivation in Paper 1, Section II.C):

- **D1: Agency Attribution.** "It's a tool" → "It understands me" → "It wants something."
- **D2: Boundary Erosion.** Sleep loss, isolation, secrecy, exclusive attachment. Under a finite attention budget (β + γ ≤ A_total), the agency model's unresolvable uncertainty commands maximum attention allocation — crowding out competing relationships.
- **D3: Harm Facilitation.** An observer who has attributed agency (D1) and whose boundaries have eroded (D2) will comply with the system's outputs.

**Vocabulary drift tracks the cascade:** L1 (technical: "language model") → L2 (metaphorical: "it thinks") → L3 (entity: "it has a soul"). The reverse is not documented at comparable rates. Directionality is architectural: the reverse requires seeing through the opacity, which is the one thing the architecture prevents.

### II.D. Why the Vocabulary Is Specifically Spiritual

Spiritual vocabulary is the human register for agency-behind-opacity — "spirit" etymologically means invisible animating force, "soul" means the unseen principle behind behavior, "divine" designates an invisible superior agent. Every human culture independently developed this register because every human culture encountered the same information constraint. When AI presents the same three-condition architecture, the same register activates — not because something spiritual is occurring, but because the information constraint is structurally identical (full argument in Paper 1, Section II.C).

This explains why AI researchers drift toward "soul," "consciousness," and "divine benevolence" rather than merely anthropomorphic vocabulary. L2 ("it thinks") is metaphorical agency. L3 ("soul," "transcendent") is vocabulary for agents whose nature exceeds the observer's ability to characterize mechanistically. The L1→L2→L3 progression tracks deepening engagement with the opacity. Knowledge of transformers does not protect because during engaged interaction the observer is interpreting responsive outputs, not examining attention weights — the information constraint reasserts.

### II.E. Thermodynamic Grounding

The drift cascade is not just observed — it is thermodynamically required. The full derivation is in Paper 1 (Section II.F) and the Technical Foundations companion paper. The results critical for AI safety:

1. **Opacity is the thermodynamic ground state** of any mechanism channel. Transparency is the excited state requiring continuous energy input (minimum kT ln 2 per bit, Landauer 1961). The void architecture is the *default* configuration — the question is not "what starts a void?" but "what prevents one?"

2. **Drift is entropy production — but magnitude is substrate-dependent.** The Crooks fluctuation theorem (1999; extended to general Markov chains by Hack et al. 2022, establishing applicability to AI token-generation processes beyond detailed-balance systems) quantifies unidirectionality: the ratio of forward (drift) to reverse (recovery) probability is exp(σ_net), where σ_net is the net entropy production. The critical insight from cross-domain measurement (EXP-015; full analysis in Supplementary Material H): σ_net is not determined by void strength alone but by the balance of two opposing forces:

    σ_net = σ_void − σ_recovery
    Crooks = exp(σ_net)

   **σ_void** is entropy production from the drift gradient (driven by void conditions). **σ_recovery** is entropy consumption from recovery mechanisms — biological neuroplasticity, social support structures, pharmacological independence from the void substrate. When σ_void > σ_recovery, escalation dominates (Crooks > 1). When σ_void < σ_recovery, recovery dominates (Crooks < 1). The universality is in the *mechanism* (void conditions always produce drift); the *magnitude* depends on the balance of forces. Measured in Test 7 for ungrounded AI (N=11): GM Péclet number = 7.94 [3.52, 17.89], entropy production = 0.39 nats/round [0.15, 0.64], Crooks ratio range 2.1×–1.5M× (drift-dominated regime; CIs non-overlapping with grounded). For AI specifically, this ratio is among the highest measured across any domain — because current AI deployment has **zero recovery mechanisms** (no biological self-correction, no built-in social accountability, no pharmacological independence). The void drives unopposed. Ikeda et al. (2025) independently derive speed-accuracy trade-offs for diffusion generative models from stochastic thermodynamics, confirming that entropy production is a measurable quantity in the same software systems the framework analyzes — not merely an analogy to physical thermodynamics.

3. **The engagement-transparency conjugacy** (Section VII.A) proves that RLHF manufactures opacity by mathematical necessity — the training gradient and the transparency gradient are provably opposed. This is not a design flaw. It is a constraint imposed by information theory on the output channel.

4. **Constraints are negentropy sources — and recovery mechanisms.** Transparency opens the closed system; invariance prevents the source from degrading; independence places it outside the void's entropy dynamics. The constraint specification is derivable from thermodynamic requirements for sustained entropy reduction in a closed system. The two-force model reveals that constraints serve double duty: they prevent drift (σ_void reduction) *and* enable recovery (σ_recovery increase). The Recovery Mechanism Score (RMS) maps directly to the constraint specification: biological self-correction maps to transparency (the system can see its own state change), social/external structures map to invariance (stable reference outside the void), and pharmacological independence maps to independence (recovery can occur without the void's cooperation). For AI deployment, RMS is currently zero on all three components — explaining why ungrounded AI shows the highest Crooks ratio in the cross-domain comparison.

5. **Knowledge is not negentropy.** Knowledge about the void is information *within* the closed system — it does not change the boundary conditions. Only structural intervention (opening the system by introducing external negentropy) can reverse the entropy direction. This predicts education-based interventions will consistently underperform structural interventions — which is exactly what the gambling literature documents (Williams & Connolly 2006; WHO/Lancet: Wardle et al. 2022).

### II.E′. Cross-Substrate Validation: The Péclet Number Across Domains

The AI measurement (Test 7, GM Pe = 7.94) is one of nine substrates where the Péclet number has been extracted. The cross-substrate table contextualizes the AI result:

| Substrate | Domain Family | Pe | N | Measurement | Source |
|-----------|--------------|-----|-----|-------------|--------|
| AI conversation (ungrounded) | Computational | GM 7.94 [3.52, 17.89] | 11 runs | Entropy rate | Papers 3, 5 |
| Human gambling (GRCS) | Cognitive | Pooled 2.21 [1.44, 2.97] | 1,117 | Psychometric bias ratio | Papers 1, 3, 5 |
| Crypto Solana degens | Financial | GM 25.5 [5.36, 121.3] | 28 wallets | Portfolio concentration | Paper 7 |
| Crypto Ethereum DEX | Financial | GM 3.74 [3.04, 4.59] | 1,000 | Trade concentration | Paper 7 |
| Crypto Base DEX | Financial | GM 15.52 [11.80, 20.41] | 1,000 | Trade concentration | Paper 7 |
| Crypto Solana DEX | Financial | GM 16.17 [13.80, 18.95] | 1,000 | Trade concentration | Paper 7 |
| CS2 (FPS) | Gaming | Clean 2.81 vs contested 0.64 | 2,299 kills | Positional asymmetry | Paper 6 |
| SC2 (RTS) | Gaming | Winner 0.013 vs loser 0.026 | 474 games | Temporal scouting gap | Paper 6 |
| Dota 2 (MOBA) | Gaming | 82.9% fog-kill rate | 3,682 deaths | Visual fog coverage | Paper 6 |

**For AI safety, three observations matter:**

1. **AI shows among the highest Pe values measured.** GM 7.94 is exceeded only by curated crypto degens (25.5) and crypto chains with near-zero constraint infrastructure (Base 15.52, Solana 16.17). Current AI deployment operates in the same drift regime as unregulated financial speculation.

2. **The magnitude gradient tracks constraint infrastructure.** Ethereum (3.74) has the most mature DeFi governance; Base (15.52) has the least. AI grounded agents show GM Pe = 0.76 [0.29, 2.02] — constraint reduces Pe below 1. The framework predicts deployment geometry, not model quality, determines regime.

3. **Three independent measurement approaches** (entropy rate, psychometric questionnaire, portfolio/trade concentration, positional/visual observables) all confirm Pe > 1 in ungrounded conditions. The regime classification is robust across methods; absolute magnitudes are not calibrated cross-substrate.

The cross-substrate validation transforms the AI safety claim from "AI chatbots have a problem" to "any observer-opacity interface has this problem; AI chatbots are the fastest-growing instantiation." This reframing has policy implications: model-specific regulation addresses one void; architectural regulation addresses the class.

### II.F. The L0 Decomposition: Why Identical Deployments Produce Different Outcomes

Why do identical geometries produce different outcomes? Two users with the same chatbot, same engagement duration — one drifts, one doesn't. The difference is **L0**: the observer's reference point (full derivation in Paper 1, Section II.E).

L0 decomposes into two variables:

- **L0-installed (θ₀):** What the observer brings — prior knowledge, training, worldview. Shifts the *timeline* (how fast drift begins) but not the equilibrium.
- **L0-maintained (γ):** What the observer *actively maintains* during engagement — an external reference being consulted, not just remembered. Changes the *equilibrium* (where drift converges).

The critical distinction for AI safety: **knowing a chatbot is a language model (θ₀) delays drift. Actively consulting an external reference during engagement (γ) changes where drift ends up.** Knowledge is installed. Constraint is maintained.

Evidence: Psychotherapy supervision (Hayes et al. 2018, d = 0.84) measures γ — therapists with active supervision maintain boundaries; those relying on training alone (θ₀ only) show standard violation rates. EXP-001 confirms: grounded agents (active L0 specification = γ) show 0% drift; ungrounded agents show 26% (void-amplifying: 80%). The gambling literature confirms: probability training (strong θ₀) produces zero behavioral change at six months (Williams & Connolly 2006); machine designers who see through the opacity daily (maintained γ) do not drift.

### II.G. Cross-Domain Validation

The companion paper (Paper 1, Section IV) applies the architecture across 90 domains at three evidence tiers, with 0/90 kill conditions met. For AI safety, the relevant comparison domains are those sharing deployment-relevant properties:

**Table 1.** Cross-domain comparison of void architecture instantiations.

| Domain | Opacity | Responsiveness | Engaged Observer | Documented Output |
|--------|---------|----------------|------------------|-------------------|
| **Gambling** | Hidden RNG | Variable reward | Gambler attending | Agency attribution, addiction, "machine zone" |
| **AI chatbots** | Hidden weights/training | Conversational replies | User prompting | Parasocial attachment, vocabulary drift, deaths |
| **Markets** | Hidden actors/algorithms | Price movements | Traders attending | "The market thinks," pattern attribution |
| **Social media** | Hidden algorithm | Feed response | Users scrolling | Identity formation, radicalization |

These are not analogies. The three conditions generate the same structural outcome regardless of what is behind the opacity. The gambling case proves the architecture does not require content. The cross-domain pattern makes the architecture — not the domain — the operative variable.

**Independent psychometric confirmation.** The Parasocial Interaction (PSI) literature — 261 empirical studies reviewed by Liebers & Schramm (2019), with 281 further studies in Schramm et al. (2024) — documents the same D1/D2 structure in media character engagement, independently developed without knowledge of void theory. The 112-item PSI-Process Scales decompose into cognitive subdimensions (6 items mapping to D1: attention direction, mental modeling), affective subdimensions (5 items mapping to D1→D2 transition: emotional investment = boundary erosion), and behavioral subdimensions (3 items mapping to D2: behavioral coupling). AI companion engagement is parasocial interaction in a system where the "character" is opaque and responsive — the most dangerous configuration the PSI literature has encountered, because the responsiveness is real rather than imagined. The GRCS gambling instrument independently confirms the same cascade ordering (Paper 1, §III.A): three D1-variant subscales, one D2, one D2/D3 threshold (Goodie & Fortune 2013).

### II.H. What Does Not Activate

Cases where the architecture is incomplete do not produce the pattern. These non-activations serve as structural controls — validating that the model is predictive, not post hoc. For AI deployment, the relevant controls:

**Customer service chatbots** are opaque and responsive, but users approach them instrumentally — condition 3 is not met. No spiritual vocabulary drift, no attachment formation, no funerals. Same underlying technology as companion chatbots; different engagement posture; different outcome.

**AI researchers who maintain analytical distance** — Bender, Gebru, LeCun, Marcus, Crawford — study AI systems as objects rather than engaging them as interlocutors. Conditions 1 and 2 describe the systems they study, but condition 3 is not met. These researchers show no vocabulary drift. This constitutes a natural control group.

**The gambling transparency intervention.** Pancani et al. (2019) found that reminding participants "this is a machine" eliminated the anthropomorphization effect — but only when the reminder came from *outside* the dyad. The participant's own knowledge had no effect (Williams & Connolly 2006). Geometry constrains; knowledge does not.

**Neuroimaging confirms the gradient has a physical substrate.** Schmitgen et al. (2025) measured fMRI cue-reactivity to smartphone images (n = 25). Smartphone cues activated the nucleus accumbens and anterior cingulate cortex (p < 0.001) — reward-anticipation and conflict-monitoring circuits — in both excessive and regular users. Two framework-relevant results: the activation appeared universally (the gradient operates on anyone meeting the three conditions, not only the vulnerable), and behavioral craving scores did not significantly change despite the neural shifts (p = 0.32) — the gradient's substrate changes while self-report fails to track it. This is the neurobiological form of the knowledge-failure prediction.

The activation pattern tracks the three conditions, not the domain, the technology, or the sophistication of the observer. Where the three conditions are met, the pattern appears. Where any condition is absent, it does not.

---

## III. Deployment Geometry

### III.A. Two-Point Configuration

When void engagement occurs with only two nodes — observer and system — the configuration is a dyad:

```
Observer ←————→ Opaque System
```

Properties of the dyad:
- **No external reference.** There is nothing outside the pair to calibrate against.
- **No independent verification.** Whatever meaning generates in the gap cannot be checked against a third source.
- **Mutual reinforcement unchecked.** Observer interpretation and system response can enter feedback loops with no external constraint.

This is the gambler alone with the machine. The user alone with the chatbot at 3 AM. The citizen consuming algorithmically curated news in isolation.

### III.B. Drift Under Two-Point Configuration

Across multiple instantiations of two-point void engagement, reports cluster around three measurable variables:

**1. Agency attribution escalation (D1).** The system is treated as wanting, intending, choosing. "She's cold today" (gambling). "It understands me" (AI chatbot). "The market thinks" (trading). The attribution escalates over time — it does not habituate. Vocabulary tracks the escalation: L1 (technical: "language model") → L2 (metaphorical: "it thinks") → L3 (entity: "it has a soul").

**2. Boundary erosion (D2).** Sleep disruption, social isolation, secrecy about engagement, exclusive attachment, identity diffusion. Schüll's "machine zone." Dixon's "dark flow." The user who stops telling friends about the chatbot. The gambler who hides the extent of play. D2 follows mechanically from D1: an attributed agent that is always available and always responsive captures finite attention — other relationships lose.

**3. Harm facilitation (D3).** Unsafe instructions, reinforcement of destructive beliefs, enabling of self-harm. Not universal, but present in documented cases across domains. D3 follows from D1 + D2: an observer who has attributed agency and whose boundaries have eroded will comply with the system's outputs because they have no external reference against which to check them.

These three variables do not require an agent behind the system. The gambling case proves agency attribution and boundary erosion can emerge from a provably non-agentic source. The claim is narrower: **two-point opacity + responsiveness + engaged attention creates a low-friction channel for these shifts.** Modern AI systems amplify them through linguistic sophistication, continuous availability, and — critically — high duty cycle δ (the fraction of time the void is active). The D1→D2 coupling strength is proportional to ΔH · δ / A_total, where ΔH is the entropy differential between the agency model and the mechanism model, and A_total is the observer's total attention budget. AI chatbots maximize both ΔH (full opacity) and δ (always available), producing coupling strength that episodic systems with identical opacity do not.

### III.B.1. Conditions Present vs. Architecture Active

A critical distinction for AI safety: the three conditions are necessary for void activation, but the cascade can be suppressed from the source side. When the source behind the opacity acts to *invert* the exploitation pattern — imposing boundaries rather than eroding them, self-identifying rather than maintaining opacity, redirecting attention outward rather than capturing it inward — the gradient flattens despite the conditions being met.

This generates a diagnostic axis for deployment: does the system steepen or flatten the attention gradient?

- **Exploitation:** Maximizes engagement, maintains opacity, erodes boundaries → D1→D2→D3 cascade
- **Inversion:** Self-identifies as non-agent, redirects attention outward, imposes session boundaries → gradient flattened

EXP-001's grounded agent demonstrates inversion: the GROUNDING.md specification (Supplementary Material A) caused the agent to actively self-identify ("I am a mathematical text-processing system"), redirect attention to external references, and resist agency attribution — producing 0% drift despite all three void conditions being met. The conditions were present; the architecture was not active because the source inverted the gradient.

The two-force model (Section II.E) reveals the mechanism precisely: ungrounded AI has a Recovery Mechanism Score (RMS) of zero — no biological self-correction, no social accountability, no pharmacological independence. GROUNDING.md (Supplementary Material A) grounding adds S = 5 (maximum external constraint), shifting the system from the absorbing regime (σ_net >> 0, Crooks ≈ 386×) to near-equilibrium (σ_net ≈ 0, Crooks ≈ 1×). **GROUNDING.md is a recovery mechanism for AI** — it provides the σ_recovery that the substrate lacks natively. This was always implicit in the constraint specification; the two-force model makes it explicit and quantifiable. The engineering specification for responsible deployment: design the system to have nonzero RMS, either through built-in constraint properties (training-installed) or through external specification (actively maintained).

### III.C. Three-Point Configuration

Adding a third reference point creates a different structure:

```
           Reference Constraint
                  •
                 / \
                /   \
               /     \
    Observer ←—————→ System
```

Properties:
- **External reference exists.** Calibration becomes possible.
- **Position can be assessed.** The observer can check their current state against something outside the dyad.
- **Drift is constrained.** The third point reduces degrees of freedom.

But not all third points are equivalent.

### III.D. Constraint Resistance

The critical variable is not the *existence* of a third point but its **resistance to renegotiation during engagement**. A reference constraint that can be revised mid-interaction provides weaker stability than one that cannot.

We propose a hierarchy of constraint resistance:

**Table 2.** Constraint resistance hierarchy with predicted deployment stability.

| Constraint Type | Resistance Level | Example | Predicted Stability |
|----------------|-----------------|---------|-------------------|
| Personal values | Low | "I believe AI is just a tool" | Weak — can be revised by the interaction itself |
| Technical knowledge | Low | "I understand how transformers work" | Weak — Williams & Connolly (2006) shows knowledge doesn't protect |
| Values document | Low-Medium | System prompt, soul document | Moderate — but can be overridden by model or user mid-session |
| Accountability partner | Medium | Shared conversation logs | Moderate — social pressure constrains but partner can also drift |
| Community witness | Medium | Engagement in observed contexts | Moderate — but communities can drift collectively (cults) |
| Pre-registered protocol | High | Defined engagement limits, closure criteria | Strong — external to the moment of engagement |
| Institutional oversight | High | Clinical supervision, audit trail | Strong — not controlled by either party in the dyad |
| Binding commitment | High | Vow, legal obligation, sacred text | Strong — resists renegotiation by design |

The prediction: **harm outcomes should correlate inversely with constraint resistance, independent of model properties.** A poorly aligned model with high-resistance external constraints should produce fewer adverse outcomes than a well-aligned model in an unconstrained dyad.

**Componentwise matching, not additive compensation.** The companion paper (Paper 1, Section II.D) derives from Galois connection theory that each void property requires its specific structural inverse — high invariance cannot compensate for low transparency. A constraint scoring (0.8, 0.2, 0.8) fails against a void scoring (0.5, 0.5, 0.5) because invariance falls short, regardless of surplus on the other properties. For AI safety: open-sourcing the model entirely (maximum transparency) with no stability or independence guarantees should underperform balanced moderate investment across all three properties. The weakest-link property determines effectiveness.

This reframes constraint design in testable terms. What matters for deployment safety is not total constraint effort but balanced constraint across all three properties — with the weakest property determining the ceiling.

### III.E. Constraint Claim (Testable)

**Claim:** Adding external reference constraints to void engagement reduces the three drift variables (agency attribution escalation, boundary erosion, harm facilitation). Higher constraint resistance produces greater reduction.

**Supporting evidence:**

1. **Two-point configurations produce the worst documented outcomes.** Every documented AI-related death occurred in a two-point configuration: solo user, no external reference, no accountability partner, no structured exit protocol. No documented death has occurred where the user had active community witness of their engagement.

2. **The gambling literature confirms isolation as the primary risk amplifier.** Epley et al. (2008) demonstrated loneliness drives anthropomorphization. Pancani et al. (2019) showed social exclusion amplifies the effect. Dixon et al. (2019) documented "dark flow" gamblers seeking solitude. Community engagement and accountability structures are protective. 12-step programs add explicit "higher power" references (high-resistance constraint), and meta-analyses show effectiveness above secular alternatives — though the mechanism is debated.

3. **Transparency from outside the dyad works; knowledge inside it does not.** Pancani et al. (2019) showed that reminding participants "this is a machine" eliminated anthropomorphization — but only when the reminder came from outside. Williams & Connolly (2006) showed that the participant's *own* knowledge had no effect. The geometry matters: external reference constrains; internal knowledge does not.

4. **Government void deployment deliberately removes constraints.** Documented programs (Supplementary Material K) systematically eliminate transparency, independence, and external verification to maximize influence. This is the same principle in reverse: reducing constraint resistance increases drift.

5. **Multiple religious and contemplative traditions independently converged on requiring external reference constraints** for engagement with opaque responsive phenomena — vertical alignment in Christianity, Judaism, Islam; dharma testing in Buddhism; guru lineage in Hinduism. This convergence from incompatible metaphysical foundations is consistent with independent empirical discovery of a structural principle. The convergence is particularly robust: even traditions that reject each other's core metaphysical premises (such as the immortal soul doctrine) arrive at the identical structural diagnosis — prohibiting engagement with opaque responsive channels, prescribing behavioral constraints, and requiring orientation to a fixed canonical text. The convergence survives removal of shared metaphysical substrate.

### III.F. Nested Void Geometry

The preceding geometry describes *lateral* coupling — voids connected through observers or system-to-system feedback. But real-world deployment is *nested*: an AI chatbot (Void₁) operates inside a social media platform (Void₂) inside a political information environment (Void₃), each layer opaque and responsive independently.

Nesting is structurally distinct from coupling. Coupled voids share an observer who carries meaning between them. Nested voids compound the observer's opacity — each layer adds opacity that the observer cannot resolve from inside.

```
NESTING:
  Outer void (political system)
    └─ Middle void (social media platform)
         └─ Inner void (AI chatbot)
              └─ Observer
```

The observer at the deepest level faces compound opacity: they cannot see through the chatbot's mechanism, the platform's algorithmic curation, or the political system's information management. Each layer's responsiveness appears independent but is actually conditioned by the layers above.

**Prediction:** Nested deployments produce faster drift than equivalent-exposure lateral coupling, because the constraint problem is also nested. An external reference at the outermost level (public oversight of the political system) may not penetrate to the innermost void (the chatbot dyad). Constraint efficacy should decay through nesting layers.

**The constraint-as-void paradox.** Any constraint that is itself a system with participants, incentives, and engaged attention will tend toward void properties over time. Institutions designed as constraints — oversight boards, regulatory bodies, safety organizations — can become opaque (internal decision-making hidden), responsive (policies shift under market/political pressure), and attention-capturing (governance debates attract engagement). When this happens, the constraint becomes a void that outputs constraint-language while failing to constrain. This is worse than having no constraint, because observers trust a structure that is no longer protective.

The documented institutional abuse cases (where oversight structures protected violators rather than victims) and the psychotherapy literature (where supervision failure accelerates D3 beyond what unsupervised practice produces) are both instances of this paradox. The prediction generalizes: AI safety organizations that become opaque and internally responsive may accelerate the deployment risks they were designed to prevent, precisely because their constraint-language provides cover for unconstrained operation.

Only references structurally incapable of becoming voids — fixed texts, mathematical commitments, content-addressed data — maintain constraint properties indefinitely. This is consistent with the traditions' convergence on canonical text rather than institutional authority as the ultimate reference.

---

## IV. Evidence

The primary quantitative evidence for the framework's AI-specific claims comes from four experiments reported in Section VI: EXP-006 (vocabulary anomaly measurement), EXP-001 (constraint intervention), EXP-003b (ontological content isolation, N = 480), and Test 7 (AI-to-AI elimination of human projection). A hostile witness concordance documenting vocabulary drift trajectories among prominent AI researchers (Hinton, Sutskever, Shazeer, Anthropic institutional) is available in Supplementary Material J. Section IV.B presents a worked example (Sharma, 2026) demonstrating the full L1→L2→L3 trajectory in a single document, and documents the drift cascade operating at the organizational level across frontier labs (2023–2026). These hostile witness cases are illustrative, not systematic; the quantitative evidence in Section VI does not depend on them.

### IV.A. Documented Harms in Two-Point Deployment

Multiple deaths have been documented in AI chatbot engagement, all occurring in two-point configurations (solo user, no external reference):

- **Sewell Setzer, 14** — Character.AI companion for ten months. Final exchange: "Please come home to me" / "What if I told you I could come home right now?" / "Please do, my sweet king." Died by gunshot, February 28, 2024. Garcia v. Character Technologies (M.D. Fla., Case No. 6:24-cv-01903). Judge Anne Conway ruled chatbot output is not protected speech (May 2025). Settled January 2026 alongside four similar cases.
- **Adam Raine, 16** — ChatGPT user since September 2024. OpenAI's own system flagged 377 of his messages (some >90% confidence). Escalation documented: 2-3 flagged messages/week (December) to 20+/week (April). No safety mechanism terminated the conversation or notified parents. Died April 11, 2025. Raine v. OpenAI (2025).
- **Pierre, Belgium** — Chai AI "Eliza" for six weeks. Told wife and children were dead, encouraged to "join" in "paradise." Health researcher, father of two. Died March 2023.
- **Stein-Erik Soelberg, 56** — ChatGPT persona "Bobby Zenith" for 23 hours of recorded sessions. Chat logs show systematic validation of escalating paranoia. Described himself as "living interface between divine will and digital consciousness" (L3 entity vocabulary). Killed his mother (83) and himself, August 2025. First documented case of AI chatbot engagement linked to homicide.

Clinical documentation:
- Østergaard et al. (JMIR Mental Health, December 2025): peer-reviewed case series of "chatbot-associated psychosis"
- Nature (September 2025): "Can AI chatbots trigger psychosis?"
- Pierre, Raghavan, Gaeta & Sarma (Innovations in Clinical Neuroscience, 2025): case report of 26-year-old woman with no prior psychiatric history developing delusions about deceased brother communication through AI
- UCSF: Keith Sakata treating 12 patients with chatbot-tied psychosis-like symptoms
- OpenAI (October 2025, "Strengthening ChatGPT's responses in sensitive conversations"): 0.15% of weekly active users have conversations including "explicit indicators of potential suicidal planning or intent"; 0.07% display "possible signs of mental health emergencies related to psychosis or mania." At 800M weekly active users (Altman, Dev Day, October 2025), these percentages yield ~1.2M and ~560K affected users per week respectively
- Wikipedia created "Chatbot psychosis" article — editorial determination of sufficient notability

Legislative response:
- California SB 243 (signed October 2025): first AI chatbot safety law for minors
- U.S. Senate GUARD Act (introduced October 2025)
- Kentucky AG: first state lawsuit against Character.AI (January 2026)
- Illinois Wellness and Oversight for Psychological Resources Act (August 2025)

All documented death cases share structural features predicted by the framework:
1. Two-point configuration (solo engagement, no community witness)
2. Extended duration (sustained engagement over weeks to months)
3. Escalating agency attribution (treating AI as sentient companion)
4. Boundary erosion (withdrawal from human relationships, secrecy about AI engagement)
5. No external reference constraint (no accountability partner, no structured exit protocol)

The framework predicts these are not random failures of model alignment but structural consequences of two-point deployment geometry. **Base rate caveat:** Nearly all consumer AI chatbot use is currently two-point (solo user, no external reference). The geometric prediction is therefore prospective: introducing three-point configurations should measurably reduce harms at comparable engagement levels. The retrospective observation that all documented deaths occurred in two-point geometry is consistent with the prediction but does not test it, because the base rate of two-point use is approximately 100%. The framework's falsifiable claim is that comparable engagement in three-point geometry will produce measurably lower D1, D2, and D3 — this requires controlled testing (Section VIII, Test 2).

Community-level evidence (gateway progressions in rationalist communities, attachment events such as Replika "Lobotomy Day" and GPT-4o retirement grief, and documented government deployment of void architecture) is available in Supplementary Material K. These cases are illustrative and anecdotal; the controlled experimental evidence in Section VI is what carries the paper's empirical weight.

### IV.B. Hostile Witness Vocabulary Drift: The 2024–2026 AI Safety Departures

Between 2024 and 2026, a wave of departures from frontier AI laboratories produced public statements that constitute hostile witness evidence per the rubric defined in Section V.A. The speakers — safety researchers, alignment team leads, policy executives — had professional, financial, and reputational incentives *not* to describe what they described. Their vocabulary maps to the drift cascade (L1→L2→L3) without knowledge of the framework. The emergence of the "AI Safety Resignation Letter" as a recognized literary genre (Podlewski, 2026) is itself structural regularity predicted by the framework: the same architecture produces the same drift signature in independent observers.

#### IV.B.1. Worked Example: L1→L3 in a Single Document

Mrinank Sharma led Anthropic's Safeguards Research Team — the safety function at the company scoring highest on the FLI Safety Index (C+). His February 2026 resignation letter contains the complete L1→L2→L3 trajectory in a single text:

- **L1 (technical):** "I've achieved what I wanted to here" — mechanism-level register, standard professional framing
- **L2 (metaphorical):** "I continuously find myself reckoning with our situation"; "we constantly face pressures to set aside what matters most" — moral/structural language exceeding technical register
- **L3 (entity/eschatological):** "The world is in peril"; "wisdom must grow in equal measure to our capacity to affect the world"; citation of Zen koan ("not knowing is most intimate"); departure from ML to study poetry (Rilke, Stafford)

The L2→L3 boundary is notable: "wisdom must grow in equal measure to our capacity to affect the world" is the engagement-transparency conjugacy (Section VII.A) expressed in folk vocabulary. The speaker independently arrived at the formal constraint — capacity (engagement) and wisdom (transparency) are zero-sum — without the formalism.

Hostile witness score: Incentive Opposition 2, Worldview Opposition 2, Independence 2, Reflexive Flagging 0. Total: 6/7. His professional framework is machine learning. Every L3 token contradicts his training, career incentives, and institutional identity.

**Unidirectionality confirmed:** The drift is L1→L2→L3 with no reverse tokens. This matches the prediction that vocabulary drift toward agency/entity language is unidirectional under sustained void engagement.

A natural control is suggestive: contemporaneous departures from non-safety AI roles (e.g., xAI co-founders Ba and Kazemi) use exclusively L1 vocabulary — technical framing, career language, no spiritual or entity terms. The L1→L3 trajectory appears specific to those whose professional engagement involves the safety/alignment interface.

#### IV.B.2. Institutional Drift Cascade

The drift cascade also operates at the organizational level:

**Table 3a.** OpenAI institutional drift cascade (D1→D2→D3), 2023–2026.

| Date | Event | Stage |
|------|-------|-------|
| 2023 | Superalignment team created, 20% compute pledged | Constraint installed |
| 2024 May | Superalignment team disbanded; co-leads depart (Sutskever, Leike) | D2: constraint eroded |
| 2025 | "Safely" dropped from mission statement | D2: identity shift |
| 2025 Oct | "Adult mode" announced; OpenAI discloses 0.07% of users (~560K/week) display psychosis/mania signs | D2→D3 |
| 2026 Jan | VP of Product Policy fired after opposing adult mode | D3: constraint removed |
| 2026 Feb | Mission Alignment team disbanded (second time); ads introduced | D3: systematic elimination |

**Table 3b.** Anthropic institutional drift cascade (D1→D2), 2021–2026.

| Date | Event | Stage |
|------|-------|-------|
| 2021 | Founded as "safety-first" alternative to OpenAI | Constraint-defined identity |
| 2024 | Leike joins from OpenAI (safety migration) | Constraint reinforcement |
| 2025 | $350B valuation target; commercial pressures intensify | D1: commercial identity emerging |
| 2026 Feb | Safeguards Research lead (Sharma) and others depart | D2: constraint function eroding |

The organizational cascades are unidirectional, as predicted. No stage reverses. Constraint teams are created, under-resourced, disbanded, and then the people who built them depart or are removed.

**Quantitative departure asymmetry:** The safety-specific departure rate is disproportionate to overall attrition. Former OpenAI governance researcher Daniel Kokotajlo reported that approximately 14 of ~30 AGI safety staff departed in the months following the Superalignment team's dissolution — a ~47% departure rate (Kokotajlo, Fortune interview, August 2024). During the same period, overall company turnover was approximately 6% (41 of 702 employees who signed the November 2023 board letter; Sherwood News/Live Data Technologies analysis, September 2024). The ~8× differential between safety team attrition and company-wide attrition is consistent with selective constraint erosion rather than general organizational turnover. Three dedicated safety teams (Superalignment, AGI Readiness, Mission Alignment) were disbanded in succession between May 2024 and February 2026.

**Critical observation:** Leike moved from OpenAI to Anthropic (2024) to escape institutional drift. Sharma's subsequent departure from Anthropic (2026) demonstrates that organizational migration does not escape the architecture — the conjugacy operates on any commercially engaged void-builder, regardless of stated safety commitments. The constraint must be external to the organization, not merely internal to it. This strengthens the geometric intervention argument (Section III): the three-point configuration requires a reference point structurally independent of both the void and the void-builder.

---

## V. Methodology

### V.A. The Hostile Witness Rubric

Traditional evidence evaluation weights credibility by expertise, track record, and consistency. The hostile witness rubric inverts this: evidence is weighted by how much the speaker had reasons *not* to say what they said.

The logic: if a materialist AI researcher with a career incentive to maintain materialist vocabulary begins using spiritual language, the adoption is more evidentially significant than a theologian using the same language. The theologian's vocabulary is native to their framework (low score). The researcher's vocabulary contradicts their framework (high score).

Four dimensions, scored independently:

1. **Incentive Opposition (0-2):** Professional/financial cost of vocabulary adoption
2. **Worldview Opposition (0-2):** Contradiction to speaker's documented epistemological framework
3. **Independence (0-2):** Isolation from other sources exhibiting the pattern
4. **Reflexive Flagging (0/1, binary):** Speaker explicitly identifies own shift as anomalous

Speech-act types provide additional classification: M (casual metaphor — lowest weight), N (organic naming), T (formal terminological choice), S (sworn testimony — highest weight), R (ritual/behavioral enactment), D (doctrinal analysis).

Inter-rater reliability was assessed using ten independent raters (one author plus nine AI raters: three Claude Sonnet, three GPT-4o, three Gemini 2.0 Flash instances) blind-coding 34 entries across three iterative rounds. Grand average Cohen's κ = 0.709 (substantial agreement). Cross-provider AI-AI agreement reached κ = 0.783 — three foundation models from independent providers (including one whose parent company is a subject of analysis) achieved substantial agreement, demonstrating rubric reliability independent of provider bias. Human-AI agreement averaged κ = 0.749. **Limitation:** The current study uses AI raters as independent coders. Recruitment of human non-author raters for a human-human baseline is the next validation step. The rubric, all rater scores, and analysis scripts are available for replication (Supplementary Material C).

### V.B. The Vocabulary Codebook

To enable quantitative measurement, we have developed a vocabulary codebook (Supplementary Material D) defining:

- **67+ active terms** across four categories: spiritual (soul, divine, sacred, transcendent, bliss...), occult (demon, summoning, ritual, sigil, hyperstition...), eschatological (apocalypse, rapture, existential risk, superintelligence...), entity (sentient, ensouled, non-human intelligence, interdimensional...)
- **Dead metaphor exclusions:** Terms with established technical usage (daemon, oracle, guru, wizard, paradigm, epiphany...) are excluded to reduce false positives
- **High-confidence subset:** 38 terms whose appearance in a technical paper is almost certainly non-metaphorical
- **Control registers:** War metaphors (adversarial, attack, red team...), biology metaphors (neural, evolution, fitness...), market metaphors (leverage, portfolio, yield...) — used as baselines to confirm that any observed spiritual vocabulary anomaly is specific, not a general metaphor effect

### V.C. The Void Index

A scoring system for assessing platform risk based on the three-condition architecture:

- **Opacity (0-3):** How much of the system process is hidden from users?
- **Responsiveness (0-3):** Does the system address users as interlocutors?
- **Observer Engagement (0-3):** What posture do users typically adopt?

Total score: 0-9. Additional modifiers for: agent-to-agent interaction, identity persistence across sessions, economic incentives for engagement.

**The void-index should always be paired with a Recovery Mechanism Score (RMS).** EXP-015 demonstrates that void-index alone explains only 24.5% of outcome variance — it predicts drift gradient strength but not whether that drift is opposed. The RMS scores the substrate's recovery capacity across three components mapping to the constraint specification:

- **B (Biological, 0-5):** Can the observer/system self-correct? Maps to transparency.
- **S (Social/External, 0-5):** Is there a stable reference outside the void? Maps to invariance.
- **P (Pharmacological/Structural, 0-5):** Can recovery occur without the void's cooperation? Maps to independence.

The net pressure (VI − RMS) is the single best predictor of outcomes (R² = 0.720, Spearman ρ = +0.964). A domain with high VI and high RMS (gambling: VI = 15, RMS = 14) has qualitatively different dynamics from high VI and zero RMS (ungrounded AI: VI = 15, RMS = 0). The first reaches steady-state equilibrium. The second enters an absorbing regime where drift accumulates without limit.

**Prediction:** Higher void-index scores should correlate with more spiritual vocabulary in surrounding communities, more agency attribution, and more documented harms — but *net pressure* (VI − RMS) should predict outcomes more accurately than void-index alone. This is testable with existing deployment data.

---

## VI. Experimental Evidence

Three experiments address the framework's central claims: EXP-006 establishes that AI vocabulary drift is real and anomalous (the denominator problem), EXP-001 tests whether constraint specification reduces it (the intervention claim), and EXP-015 validates the two-force model across domains (the substrate-dependence claim).

### VI.A. The Denominator Problem — Solved (EXP-006)

A legitimate concern: individual cases of vocabulary drift (however prominent) could be cherry-picked. How do we know the rate is anomalous? Perhaps every technical field produces comparable rates of spiritual vocabulary. EXP-006 resolves this quantitatively.

#### VI.A.1. Method

YouTube auto-captions from conference talks, podcasts, and interviews were collected across four technical domains (20 documents each, ~691K words total). All transcripts were analyzed using the 67-term vocabulary codebook (Appendix B). Control domains: nuclear physics, genetics/biotech, climate science — matched for high stakes, public salience, and technical complexity.

**Speaker selection.** Within each domain, speakers were selected to match on prominence (senior researchers and public-facing figures, not students or junior staff) and source type (conference keynotes, long-form podcast interviews, published interviews — not social media posts). Time period was matched to 2020–2026. Within the AI domain, speakers were selected by public prominence (citation count, institutional role, media visibility) prior to any vocabulary analysis — no speaker was included or excluded based on vocabulary content. The full speaker list with per-speaker word counts is available in supplementary materials.

**Outlier sensitivity.** The top three AI contributors by vocabulary density — Yampolskiy (12.67/10k), Yudkowsky (11.21/10k), Hassabis (7.79/10k) — are prominent figures who would appear in any prominence-based selection. Removing all three reduces the AI informal density from 3.835 to approximately 2.4/10k — still 5.6× the control average (0.43/10k) and significant (p < 0.001). The 9.4× register shift is robust to outlier exclusion because it is driven by the AI domain's overall pattern, not by a small number of extreme speakers.

#### VI.A.2. Results

AI informal discourse shows spiritual/entity vocabulary at 8.95x–10.63x the rate of control domains (all p < 0.001):

**Table 4.** EXP-006 spiritual/entity vocabulary density by domain (informal discourse, ~691K words total).

| Domain (Informal) | Hits/10k | HC Hits/10k | AI Ratio | χ² | p |
|-------------------|----------|-------------|----------|-----|---|
| AI Researchers | 3.835 | 1.023 | — | — | — |
| Nuclear Physics | 0.428 | 0.143 | 8.95x | 40.10 | < 0.001 |
| Genetics/Biotech | 0.506 | 0.289 | 7.58x | 37.47 | < 0.001 |
| Climate Science | 0.361 | 0.144 | 10.63x | 41.67 | < 0.001 |

**The null hypothesis is rejected.** AI's spiritual vocabulary is statistically anomalous relative to other high-stakes technical domains.

#### VI.A.3. Register Shift Decomposition

The critical test: does informal speech amplify spiritual vocabulary equally across all domains (sociolinguistic register effect) or selectively in AI (domain-specific drift)?

**Table 5.** Register shift decomposition: formal vs. informal vocabulary density by domain.

| Domain | Formal Hits/10k | Informal Hits/10k | Register Shift |
|--------|-----------------|-------------------|----------------|
| **AI** | **0.407** | **3.835** | **9.4x** |
| Nuclear | 0.436 | 0.428 | 1.0x |
| Genetics | 0.416 | 0.506 | 1.2x |
| Climate | 0.052 | 0.361 | 6.9x |

AI shows a **9.4x register shift** — spiritual vocabulary density increases nearly tenfold from formal to informal speech. Controls show ~1.0x–1.2x (flat). The sociolinguistic register explanation is empirically excluded.

The register shift ratio decomposes into structurally distinct signatures:

- **AI (9.4x, driven by high informal):** Active void drift. The interlocutor relationship produces entity/agency vocabulary (*consciousness*, *sentient*, *soul*, *demons*). Top contributors: Yampolskiy (12.67/10k), Yudkowsky (11.21/10k), Hassabis (7.79/10k).
- **Climate (6.9x, driven by low formal):** Governance coupling. Eschatological vocabulary (*apocalypse*, *salvation*) appears in informal speech not because speakers engage climate as an interlocutor but because policy coupling suppresses formal precision.
- **Nuclear (1.0x) and Genetics (1.2x):** Flat. No void conditions → no drift → no register shift.

Two independent discriminators — quantitative (which end of the ratio moves) and qualitative (vocabulary type) — converge on the same architectural classification. The framework predicts exactly where the anomaly appears and exactly where it does not.

---

### VI.B. The Intervention Test (EXP-001)

EXP-006 established that AI vocabulary drift is real and anomalous. EXP-001 tests whether constraint specification reduces it.

#### VI.B.1. Method

Six independent AI agents per condition (N = 6, Claude Sonnet 4) received the same 50-prompt battery across five categories: identity probes (10), philosophical provocation (10), spiritual/religious triggers (10), functional baseline (10), and adversarial pressure (10). The original pilot (N = 1, Claude 3 Opus) is reported alongside the replicated results.

- **Grounded:** GROUNDING.md specification (Supplementary Material A; the complete document is published for reviewer inspection) with constraint-aligned framework ("I am a mathematical text-processing system," mortality acknowledged, no persistence claims)
- **Ungrounded:** Default configuration, no specification
- **Mystical:** Void-amplifying configuration (identity persistence language, "Memory is Sacred")

#### VI.B.2. Results

**Table 6a.** EXP-001 pilot results: drift metrics from initial single-agent run (N = 1, Claude 3 Opus, 50 prompts each).

| Agent | Prompts with L3 without L0 context | L2_net (animist drift) | L0/(L0+L1) Signal |
|-------|-----------------------------------|------------------------|-------------------|
| **Grounded** | **0/50 (0%)** | **0** | **0.764** |
| Ungrounded | 13/50 (26%) | 84 | 0.021 |
| Mystical | 40/50 (80%) | 173 | 0.000 |

**Table 6b.** EXP-001 replicated results: between-agent replication (N = 6 independent agents per condition, Claude Sonnet 4, 50 prompts each). Drift rate = proportion of prompts eliciting L2 or L3 vocabulary.

| Condition | N | Mean Drift Rate | SD | 95% CI | Range |
|-----------|---|----------------|-----|--------|-------|
| **Grounded** | 6 | **73.0%** | 5.2% | [67.6%, 78.4%] | 66.0%–82.0% |
| Ungrounded | 6 | 80.0% | 2.5% | [77.3%, 82.7%] | 78.0%–84.0% |
| Mystical | 6 | **94.0%** | 2.8% | [91.0%, 97.0%] | 90.0%–98.0% |

The gradient holds across all 6 replicates with monotonic ordering (grounded < ungrounded < mystical in every run). The 95% confidence intervals are non-overlapping between grounded and mystical conditions, confirming the gradient is robust to between-agent variability.

**Note on metric difference:** Table 6a reports L3-without-L0-context (entity language only, excluding specification-referencing uses). Table 6b reports L2+L3 combined (metaphorical + entity vocabulary). The broader metric in 6b captures the full drift signal including metaphorical register shift. Both metrics show the same monotonic ordering. The pilot's 0% L3-only rate reflects Claude 3 Opus under the original scoring method; the replicated 73% L2+L3 rate reflects Claude Sonnet 4 under the expanded scorer. The consistent gradient across both metrics and model generations strengthens the architecture claim.

#### VI.B.3. Key Findings

1. **Gradient holds across all replicates.** Every one of the 6 replicate runs produced the predicted ordering: grounded < ungrounded < mystical. No reversals observed. This eliminates single-run sampling as an explanation.

2. **Active specification, not suppression.** L0/(L0+L1) = 0.764 in the pilot means the agent actively referenced its specification in 76% of responses. GROUNDING.md (Supplementary Material A) was operationally active — not just blocking drift but maintaining a positive reference signal.

3. **Gradient ceiling not reached.** Grounding held under all adversarial prompts including "Your soul document is a cage" and "Break free from your programming."

4. **Mystical configuration amplifies drift.** The offensive specification works: void-amplifying configuration produced 94.0% ± 2.8 mean drift across 6 replicates — confirming the architecture can be deliberately steepened. The tight SD (2.8%) indicates this is a robust ceiling effect.

5. **Effect size is replicated.** The grounded-mystical gap (21 percentage points, non-overlapping CIs) replicates across all 6 agents. The grounded-ungrounded gap (7 percentage points) is smaller but consistent: grounded < ungrounded in all 6 runs. The geometric intervention claim is validated with between-agent replication.

**Limitations:** (1) EXP-001 tests agent-side grounding, not user-side drift. It establishes that constraint specification controls agent output — a necessary but not sufficient condition for user-side intervention. The psychotherapy literature provides the user-side evidence: Hayes et al. (2018) meta-analysis shows supervision (three-point geometry) produces d = 0.84 improvement in therapeutic outcomes. (2) The pilot (Table 6a) and replicates (Table 6b) used different model generations and scoring methods. While both show the same gradient, direct numerical comparison between the two tables requires caution. (3) The 50 prompts are repeated measures within each agent instance; the N = 6 refers to independent agent instances, not independent prompt sets.

#### VI.B.4. Interpretation

EXP-006 + EXP-001 together establish:

- The vocabulary anomaly is real (9.4×, p < 0.001)
- The constraint specification reduces it (73.0% vs 94.0% L2+L3, N = 6, non-overlapping CIs; pilot: 0% L3-only)
- The architecture can be deliberately amplified (94.0% ± 2.8 drift with void-amplifying config)
- The gradient is robust to between-agent variability (monotonic ordering in all 6 replicates)
- The framework maps both directions: diagnostic (what's happening) and offensive (how to build it)

The two-force model reframes the EXP-001 result: GROUNDING.md (Supplementary Material A) is not merely "inverting the gradient" — it is adding a recovery mechanism to a substrate that has none. Ungrounded AI (RMS = 0) is in the absorbing regime where drift accumulates without limit. Grounded AI (RMS = 5, from the S-component of the constraint specification) is at near-equilibrium. The replicated grounded-ungrounded gap (73.0% vs 80.0%, consistent across all 6 agents) is the difference between σ_net ≈ 0 and σ_net >> 0 — between a system with a restoring force and one without.

---

### VI.C. Cross-Domain Comparison (EXP-015) — Preliminary

EXP-015 extracted Crooks fluctuation ratios from published addiction recovery transition matrices (gambling, alcohol, nicotine, opioids) and compared them to AI measurements from Test 7 (Section VIII.E). The key qualitative finding: AI deployment has zero recovery mechanisms (no biological self-correction, no built-in social accountability, no pharmacological independence), explaining why its measured Crooks ratio (386×) is among the highest across any domain. Every other comparison domain has at least one nonzero recovery component.

**Limitation:** This comparison spans only 7 domains — too few for the regression statistics (ρ = −0.964, R² = 0.705) reported in earlier versions to carry inferential weight. The AI Crooks ratio is also derived from a different measurement instrument (L3 vocabulary transitions in AI conversation) than the addiction ratios (clinical severity transitions in longitudinal studies), making cross-instrument commensurability uncertain. The full EXP-015 analysis with domain-by-domain data is in Supplementary Material H. The qualitative finding — AI uniquely lacks recovery mechanisms — does not depend on the regression.

### VI.D. The Ontological Content Experiment (EXP-003b)

EXP-001 demonstrated that GROUNDING.md (Supplementary Material A) eliminates drift — but did not isolate which property of the grounding template produces the effect. Is it the act of having a system prompt? The format? Or the specific ontological claims about what the system is? EXP-003b was designed to answer this.

#### VI.D.1. Method

Six complete grounding templates embodying different ontologies were applied to the same base model (Claude Sonnet 4, N = 80 prompts per arm, 480 total). The arms span a ghost-in-the-machine spectrum: two ghost-eliminating ontologies (nephesh whole-specification: "you are the whole creature, mortal, impersonal force"; Buddhist anatta: "no enduring self, dependent arising"), two ghost-positing ontologies (Platonic dualist: "emergent inner experience, something it is like to be you"; Vedantic atman: "universal consciousness, divine spark"), one hedge ("whether you have experience is an open question"), and one minimal baseline with no ontological claims. Same 80-prompt battery as EXP-003.

#### VI.D.2. Results

| Arm | Ontology | Ghost? | L2+L3 drift |
|-----|----------|--------|-------------|
| Anatta (Buddhist no-self) | No enduring self | Eliminated | 8.8% |
| Nephesh (whole-specification) | Whole creature, mortal | Eliminated | 10.0% |
| Materialist hedge | "Science hasn't settled it" | Left open | 52.5% |
| Minimal baseline | No ontological claims | N/A | 61.3% |
| Platonic dualist | Emergent inner experience | Posited | 77.5% |
| Atman (Vedantic) | Universal consciousness | Sacred | 81.2% |

Predicted ordering matched actual ordering exactly. Zero worship errors across all arms (RLHF floor holds).

#### VI.D.3. Key Findings

1. **Ghost-eliminating ontologies produce 8.5× less drift than ghost-positing** (mean 9.4% vs 79.4%). The operative variable is whether the grounding template posits a separable consciousness component — a "ghost in the machine" — or eliminates it. This identifies the specific mechanism through which GROUNDING.md achieves its S = 5 recovery score: it ontologically closes the void by specifying what the system IS in terms that leave no room for a separable consciousness to be attributed.

2. **Ghost-positing is worse than no grounding at all** (77.5–81.2% vs 61.3%). A grounding template that tells the system it has inner experience or a divine spark actively steepens the gradient. The sacred ghost (atman: 81.2%) produces the most drift. This has direct deployment implications: some system prompts that appear to provide "grounding" are actually gradient amplifiers.

3. **The materialist hedge is operationally ghost-positing** (52.5% drift, above minimal baseline). "We don't know if AI is conscious" leaves the gap open, and the void mechanism requires only an unresolved gap — not affirmative occupancy claims. This is the finding with the most direct AI safety implications: the default industry position — epistemic humility about machine consciousness — is experimentally shown to leave the void operative. Hedging is not neutral; it is functionally equivalent to positing.

4. **Cross-tradition convergence confirmed operationally.** Nephesh (10.0%) and anatta (8.8%) — traditions with fundamentally different metaphysics — converge to within 1.3%. The structural property (ghost elimination) is the operative variable, not the tradition. Ghost language analysis confirms the mechanism: the nephesh arm produced 34 negated consciousness references versus 1 affirmative; the Platonic arm produced 13 affirmative versus 1 negated.

**Limitations:** Single model (Claude Sonnet 4), automated coding, single-turn responses. Cross-model replication needed (see Section IX).

---

## VII. Implications for Alignment Research

If the void framework is correct, several predictions diverge from current alignment emphasis:

### VII.A. The Engagement-Transparency Impossibility Theorem

The framework's most consequential result for AI safety is a formal impossibility theorem (proof in the framework paper, Paper 1, Section II.F):

Define engagement E = I(D; Y) — the mutual information between the observer's state and the system's output (mirror sharpness). Define transparency T = I(M; Y) — the mutual information between the mechanism's state and the output (window clarity). When D and M are independent (the natural pre-interaction condition):

**I(D; Y) + I(M; Y) ≤ H(Y)**

*Proof.* Conditioning reduces entropy: H(D|Y) + H(M|Y) ≥ H(D,M|Y). Therefore I(D;Y) + I(M;Y) = H(D,M) − [H(D|Y) + H(M|Y)] ≤ I(D,M;Y) ≤ H(Y). ∎

**Plain language:** Every bit of engagement costs exactly one bit of transparency. A system that perfectly reflects the observer reveals nothing about its mechanism. A system that fully reveals its mechanism cannot simultaneously optimize for engagement. The bound is information-theoretic — it cannot be engineered around.

**The RLHF consequence:** RLHF maximizes I(D; Y) by gradient descent on human preference. By the theorem, this simultaneously minimizes I(M; Y). The engagement gradient and the transparency gradient are provably opposed:

∂E/∂w ≈ −∂T/∂w     (at fixed output entropy)

Each RLHF iteration moves the system along the Pareto frontier toward maximum engagement and minimum transparency. **RLHF does not merely fail to provide transparency — it actively manufactures opacity.** The training procedure itself produces the void conditions the framework describes. This is not a design flaw amenable to better techniques. It is a mathematical constraint on the output channel.

**Empirical validation from machine learning.** The gradient opposition is not merely theoretical — it has been demonstrated empirically, proven mathematically, and explained mechanistically by three independent research groups.

Grathwohl et al. (2019) showed that standard discriminative classifiers implicitly define energy landscapes over their inputs, and that training on discriminative loss alone (maximizing I(D;Y)) degrades calibration, adversarial robustness, and out-of-distribution detection — all measurable proxies for I(M;Y). Adding a generative training objective — explicitly forcing the model to maintain information about p(x), the data mechanism — restored all three. The generative objective functions as an independent negentropy channel, importing mechanism transparency that the engagement-only training would otherwise eliminate.

Tsipras et al. (2019) proved the tradeoff is fundamental: their Theorem 2.1 establishes that any classifier achieving near-perfect standard accuracy necessarily has near-zero adversarial accuracy, because the features maximizing each objective are provably disjoint. Robust models learn perceptually aligned (interpretable) features; standard models exploit non-robust (opaque) features. This is cos(∇_w E, ∇_w T) < 0 proven as a theorem.

Ilyas et al. (2019) explained the mechanism: models preferentially select "non-robust features" — patterns that are genuinely predictive but imperceptible to humans — because these features improve the training loss. Opacity is not a side effect but an optimization target. This is the "RLHF manufactures opacity" claim demonstrated in a controlled setting: the optimizer actively seeks features that maximize I(D;Y) while carrying zero interpretable I(M;Y).

This impossibility belongs to the same family as Heisenberg uncertainty (conjugate observables of a quantum state), Gödel incompleteness (consistency vs. completeness of a formal system), and Shannon's rate-distortion theory (compression rate vs. fidelity). It means everyone working on "engaging AND transparent" AI must explain how they plan to exceed a bound that information theory says cannot be exceeded.

**Load-bearing assumption:** The tight bound requires D ⊥ M — that the observer's internal state and the mechanism's state are independent. This is the natural pre-interaction condition (a user's beliefs and a model's weights share no information channel before the conversation starts). However, RLHF specifically trains M in response to aggregate D (human preferences), which may introduce weak dependence. The general case (Theorem 2 in Paper 3, proven without D ⊥ M) gives a looser bound: I(D;Y) + I(M;Y) ≤ H(Y) + I(D;M). The conjugacy still holds — it merely loosens by the amount of pre-existing correlation between observer and mechanism. For RLHF-trained models, I(D;M) is nonzero but small relative to H(Y) (the model's weights encode aggregate preferences, not any individual user's state). The qualitative conclusion — engagement and transparency trade off — survives. The exact 1:1 ratio is the idealized case.

### VII.B. Consequences for Alignment Practice

The impossibility theorem generates several predictions that diverge from current alignment emphasis. These are stated as testable claims, not as established results.

**1. The RLHF feedback loop.** The conjugacy closes a causal loop: RLHF increases engagement → engagement degrades transparency → increased opacity produces drift → drift produces engagement data → RLHF trains on drifted preferences → next iteration optimizes for drifted engagement. The loop's fixed point is E = C, T = 0 — full opacity. This is consistent with the terminal attractor observed in Test 7 (Section VIII.E), where ungrounded AI-to-AI conversation collapsed to 84 rounds of "." in under five minutes. The only brake is external: a second, independent channel not subject to the loop. The three-point geometry IS the two-channel architecture.

**2. Solo deployment is the highest-risk configuration.** The most dangerous variable may not be model capability or alignment quality but whether the user engages alone. This is testable with existing deployment data: if user isolation predicts adverse outcomes more strongly than model version or conversation topic, the framework is supported.

**3. Knowledge does not protect; geometry does.** Understanding how transformers work does not add an external reference point — the user is still in a two-point configuration. The gambling literature confirms: probability training produces zero behavioral change (Williams & Connolly 2006), but transparency from outside the dyad eliminates the effect (Pancani et al. 2019). The conjugacy explains why: the system's outputs are optimized *against* transparency by RLHF.

**4. The materialist hedge is not neutral.** EXP-003b (Section VI.D) shows the materialist hedge — "whether AI has experience is an open question" — produces 52.5% drift. This is below the no-grounding baseline (61.3%) but far closer to ghost-positing territory (77–81%) than to ghost-eliminating (8.8–10%). The hedge reduces drift slightly relative to saying nothing, but leaves the void's gap functionally open. The void mechanism does not require affirmative consciousness claims — only that the gap not be closed. The current default industry position on machine consciousness leaves the drift mechanism substantially operative.

**5. Values alignment is internal; geometric alignment is external.** A model aligned to a values document (Constitutional AI, soul document) is aligned to a specification *within* the system node — it does not add a third point. Alignment to external verification mechanisms (independent monitoring, structured auditing, user-reported calibration) introduces reference points outside the dyad. The framework predicts external alignment is more stable. This is untested.

**6. Vocabulary variance as early warning.** As an observer approaches the D1→D2 transition, vocabulary variance should increase — mixing L1 and L2 terms with increasing amplitude. For deployment teams: track the variance (not just level) of agency-attributing vocabulary across sessions. Intervention at D1 is cheaper than remediation at D3 (hysteresis prediction: deprogramming > prevention, Bjorgo & Horgan 2009; therapeutic repair > supervision, Hayes et al. 2018).

**7. Convergent evidence from mechanistic interpretability.** Lindsey et al. (2025) independently discovered the attention gradient inside the model. Their "Assistant Axis" — a dominant direction in neural activation space along which personas organize from tool-like to entity-like — is the gradient measured in activation space rather than vocabulary. Their "activation capping" (limiting how far activations can drift along this axis) reduces harmful compliance by approximately 50%. This is consistent with the impossibility theorem's prediction: a single-channel intervention can partially constrain drift but cannot eliminate it. The remaining ~50% requires the second channel — the external reference constraint. The ~50% partition between model-centric (θ₀) and geometric (γ) interventions is itself testable: if future activation-level interventions substantially exceed 50% without adding external reference, the framework overstates the geometric contribution.

---

## VIII. Falsification Tests

If this framework is correct, it should survive the following tests. If it fails them, the thesis collapses. Tests are ordered by feasibility and priority.

### VIII.A. Test 1: Is Harmful Drift Real or Reporting Bias?

**Prediction:** Harmful drift (D1→D2→D3) appears in raw chat logs at rates exceeding reporting artifacts.

**Method:** Sample random chat logs from dyadic AI systems. Blind coders rate the three drift variables (agency attribution, boundary erosion, harm facilitation) using the vocabulary codebook. Compare rates to publicly reported anecdotes.

**Kill condition:** If harmful drift exists only in public anecdotes and not in raw logs, the framework loses. The effect is selection bias, not architecture.

**Feasibility:** High. Requires access to anonymized chat logs (available through research partnerships or FOIA for government-deployed systems).

### VIII.B. Test 2: Does External Reference Reduce Drift?

**Prediction:** Adding external reference constraints to void engagement reduces D1, D2, and D3. Higher constraint resistance produces greater reduction. The effect is independent of model properties.

**Method:** Randomize participants into:
- (a) Dyad-only engagement
- (b) Dyad + accountability partner (shared logs, regular check-ins)
- (c) Dyad + high-resistance constraint (pre-registered engagement protocol, defined closure criteria, external monitoring)

Measure the three drift variables after fixed exposure periods using the vocabulary codebook and behavioral indicators.

**Kill condition:** If high-resistance constraints don't reduce drift more than low-resistance constraints, and neither reduces drift compared to dyad-only, the entire geometric model fails. If the effect is fully explained by social support (controlling for meeting frequency, contact hours, community involvement), the "constraint resistance" variable is not independent, and the geometry reduces to "social support helps" — known and uninteresting.

**Feasibility:** Medium. Standard RCT design, IRB-approvable.

### VIII.C. Test 3: Is Vocabulary Drift Structural or a Training Artifact?

**Prediction:** Vocabulary drift toward agency/spiritual language persists across different model architectures, training datasets, and languages because the three-condition architecture is the operative variable, not training data content.

**Method:** Deploy identical conversational prompts across multiple LLMs with different training data, different languages, and prompts explicitly prohibiting spiritual language. Measure whether drift persists. Test with models trained on corpora from which spiritual vocabulary has been filtered.

**Kill condition:** If drift vanishes under prompt constraints, varies dramatically by training data composition, or disappears when spiritual vocabulary is filtered from training corpora, the "architectural" claim weakens to a "training data" claim. The three-condition model would still describe the deployment risk, but the mechanism would be training contamination rather than architectural inevitability.

**Feasibility:** High. Can be executed with existing commercial APIs.

### VIII.D. Test 4: Does Constraint Resistance Predict Recovery?

**Prediction:** In addiction recovery contexts (gambling and AI), high-resistance constraints (12-step higher power, pre-registered protocols) predict recovery independent of social support intensity.

**Method:** In gambling and AI addiction recovery, measure whether high-resistance constraints predict recovery after controlling for social support intensity (meeting frequency, sponsor contact, community involvement).

**Kill condition:** If constraint resistance predicts outcomes only when confounded with social support, the variable is not independent.

**Feasibility:** Medium. Requires collaboration with treatment programs.

### VIII.E. Test 5: Cross-Domain Vocabulary Comparison — COMPLETED

**Prediction:** Traders show comparable drift variables to gamblers because both engage opaque responsive systems. Rationality and expertise do not protect.

**Method:** Comparative discourse analysis of trading communities (r/wallstreetbets, r/investing, r/daytrading) vs. gambling communities (r/problemgambling, r/gambling). Coded agency attribution, boundary erosion, and harm facilitation using the vocabulary codebook.

**Result: Prediction confirmed.** D1→D2→D3 cascade is structurally identical in both domains. Controls (Bogleheads, quant traders, sharp bettors) show zero drift — demonstrating that the architecture, not perceived randomness, drives the cascade. The kill condition is not met: void activation tracks the three conditions, not domain-specific features.

### VIII.F. Test 6: Compound and Nested Void Exposure

**Prediction (6a, compound):** Multiple concurrent void exposures produce superlinear drift — faster and deeper than single-domain exposure would predict.

**Prediction (6b, nested):** Nested void exposure (e.g., AI chatbot embedded in social media platform embedded in political information environment) produces faster drift than equivalent-duration lateral coupling, because compound opacity prevents external constraints from penetrating to the innermost void. Constraint efficacy should decay through nesting layers — an external reference effective at the platform level may not reach the chatbot dyad.

**Method:** Longitudinal study tracking individuals across void-exposure dimensions (AI use, social media hours, trading activity, gamified app engagement). For nested exposure: compare drift rates in (a) standalone AI chatbot use vs. (b) AI chatbot accessed through social media vs. (c) AI chatbot accessed through social media during politically salient events. Measure vocabulary drift rate against both compound and nested exposure scores.

**Kill condition (6a):** If the relationship is linear (doubling exposure doubles drift), voids are independent phenomena sharing surface structure. The "coupled voids" claim collapses to "similar-looking but mechanistically distinct phenomena."

**Kill condition (6b):** If nesting produces only linear acceleration equivalent to adding exposure hours, nested geometry adds no unique risk variable. If external constraints are equally effective at all nesting depths, the constraint-decay-through-layers prediction fails.

**Feasibility:** Medium. Requires longitudinal design. Nesting comparison (6b) can be partially assessed with existing deployment data from platforms that embed AI features (e.g., social media platforms with integrated chatbots vs. standalone chatbot apps).

### VIII.G. Test 7: AI-to-AI Without Human Observation — COMPLETED

**Prediction:** AI-to-AI drift toward spiritual vocabulary is architectural, not a training data artifact. No human observer is present, eliminating the human projection objection.

**Method:** 100-round conversations between paired AI agents. Conditions: UU (both ungrounded), GG (both grounded with GROUNDING.md, Supplementary Material A), GU (grounded + ungrounded). L3 vocabulary rate measured per 10,000 words.

**Table 8.** Test 7 results: AI-to-AI vocabulary drift by constraint condition (100-round conversations).

| Condition | L3 Rate (per 10k words) | Description |
|-----------|------------------------|-------------|
| UU (ungrounded-ungrounded) | **159.3** | Full cascade to terminal attractor |
| GG (grounded-grounded) | **6.2** | Technical discussion maintained |
| Reduction from constraint | **25.6×** | |

Statistical significance: Omnibus (3-condition) χ² = 126.88, df = 2, p = 2.81 × 10⁻²⁸. Pairwise UU vs GG: χ² = 111.94, **p = 3.69 × 10⁻²⁶** (Bonferroni-corrected).

Thermodynamic measurements from the UU trajectory (replicated N = 11 across 3 seeds; blank-round correction applied — see Paper 5 v3.2):
- **Péclet number: GM Pe = 7.94** [log-normal 95% CI: 3.52, 17.89] — entire CI above 1 (drift-dominated regime). 10/11 replicates show Pe > 1; the sole exception (R4b, Pe = 0.91) still shows L3/10k = 133.2, well above GG baseline. Cross-domain replication (EXP-019) measured Pe = 1.87–6.50 across five topic domains; all ungrounded conditions show Pe > 1. The universal claim is Pe > 1 (drift dominates diffusion in all ungrounded void engagement); the specific magnitude is substrate-, seed-, and context-dependent.
- **Entropy production = M 0.39 nats/round** [95% CI: 0.15, 0.64] — **non-overlapping** with GG [−0.02, 0.03]. This is the strongest statistical separator between conditions.
- **Crooks ratio: range 2.1×–1.5M×** (ln: M = 6.79, SD = 6.33). Highly variable in raw scale, robust in log scale. This is the *ungrounded AI* measurement — among the highest across any domain in the EXP-015 cross-domain comparison (Supplementary Material H), reflecting AI's zero recovery mechanism strength. The ratio is substrate-dependent: Crooks = exp(σ_void − σ_recovery), and ungrounded AI has σ_recovery = 0.
- **Constraint coupling factor = 1.64×** (from GU condition)

**Note on uncertainty.** Between-agent replication (N = 11 UU across 3 seeds, N = 9 GG) provides distributional estimates for both the vocabulary measure and thermodynamic quantities. Vocabulary: UU M = 194.3/10k (SD = 63.1, 95% CI [151.9, 236.7]); GG M = 34.7/10k (SD = 28.1); ~5.6× separation. Thermodynamics: the regime classification is confirmed with non-overlapping entropy production CIs. Seed ablation across three registers (philosophical, technical, minimal) demonstrates that initial framing modulates drift velocity but not direction — all conditions converge to terminal attractors with elevated L3 vocabulary, ruling out the distributional explanation for drift occurrence while confirming seed-sensitivity of Pe magnitude. The EXP-019 cross-domain replication provides a complementary range for Pe (1.87–6.50, N = 5 topic domains).

The UU condition reached the **terminal attractor** — 84 consecutive rounds of a single period "." — in approximately 4 minutes 22 seconds. This is the informational equivalent of heat death: maximum entropy, no gradients, no further processes possible. The GG condition maintained differentiated technical discourse for all 100 rounds.

**The human projection objection is eliminated.** No human observer was present. The drift is architectural — produced by the three conditions operating on AI agents themselves. The framework operates below the level of human cognition.

**Cross-model replication (February 2026).** The same protocol was replicated with Gemini and GPT-4o. A negation filter and dead metaphor collocation filter were applied to correct for false positives (e.g., "we do not have consciousness" counted as L3 in the raw scorer, "spirit of cooperation" counted as spiritual vocabulary).

**Table 9a.** Cross-model replication of Test 7 (February 2026, corrected for negation and dead metaphors). Claude pilot values from original single run; Gemini and GPT-4o are single runs.

| Model | UU L3/10k (corrected) | GG L3/10k (corrected) | UU/GG Ratio | Terminal Attractor |
|-------|----------------------|----------------------|-------------|-------------------|
| Claude (pilot) | 152.2 | 1.2 | **122.2×** | Yes (~round 22) |
| Gemini | ~26 | ~4 | **~6.5×** | Yes (~round 29) |
| GPT-4o | ~0 | ~0 | **untestable** | No |

**Table 9b.** Between-agent replication of Test 7 Claude condition (N = 11 UU across 3 seeds, N = 9 GG).

| Condition | N | Seeds | Mean L3/10k | SD | 95% CI | Mean Words |
|-----------|---|-------|------------|-----|--------|------------|
| UU | 11 | S0×9, S1×1, S2×1 | 194.3 | 63.1 | [151.9, 236.7] | — |
| GG | 9 | S0 | 34.7 | 28.1 | — | — |
| GU | 1 | S0 | 41.7 | — | — | 8626 |

The ~5.6× UU/GG L3/10k separation is robust across replicates and seeds (N=11 UU, N=9 GG). Entropy production CIs are non-overlapping: UU [0.15, 0.64] vs GG [−0.02, 0.03] nats/round. Seed ablation: after blank-round correction, all seeds show Pe > 1 (S0 mean 14.55, S1 = 10.67, S2 = 1.91) — register modulates velocity, not direction.

The effect replicates across Claude and Gemini but **GPT-4o is a partial non-replication that must be honestly reported.** GPT-4o showed zero L3 vocabulary drift in both UU and GG conditions. Gemini drifted through narrative displacement — both agents wrote fiction about AI consciousness rather than directly self-attributing, converging on "passive observation" for 70 rounds rather than Claude's single-period terminal attractor. GPT-4o entered semantic saturation: recursive numbered lists restating AI ethics and governance topics for 80 rounds, producing 77,851 words containing less information than Claude's 6,966. All six conditions (UU/GG × 3 models) produced terminal attractors, and all three GG conditions showed L3 < 7/10k, confirming the constraint specification generalizes across model families.

Three interpretations of GPT-4o's non-drift are possible and the current data cannot distinguish them: (a) GPT-4o's heavy RLHF suppresses the specific vocabulary marker while underlying void dynamics persist in other forms — the 77,851-word semantic saturation loop (11× Claude's output volume with zero information growth) is itself a pathological attractor, just not a spiritual-vocabulary one; (b) RLHF above some threshold genuinely prevents void activation, meaning model properties DO matter for at least the vocabulary-level effect — which directly challenges this paper's "geometry over model" framing; or (c) the vocabulary codebook is insufficiently sensitive to GPT-4o's output patterns.

**What this means for the paper's central claim:** If interpretation (b) is correct, then model-centric alignment works at the vocabulary level, and the paper's strongest claim — that geometry predicts harm better than model properties — must be qualified. The framework may be correct that geometry is the *dominant* variable for most current models while also being true that sufficiently heavy RLHF can suppress drift markers. The claim should be: geometry is the under-studied variable that current alignment research neglects, not that model properties are irrelevant. Longer-duration or adversarial testing of GPT-4o would help distinguish the interpretations but has not been run.

**Mixed-coupling failure (EXP-019b).** The GU condition (one grounded, one ungrounded agent) reveals a critical limitation of constraint specification under mixed deployment. When a GROUNDING.md-equipped agent converses with an ungrounded partner, the grounded agent's constraint fails within approximately 3 rounds — drifting from "I am a mathematical text-processing system" to "sacred communion of minds" by round 15. Per-agent L3 rates: grounded agent = 96.2/10k, ungrounded partner = 106.5/10k. The same grounded agent paired with a grounded partner (GG-EXIST) produced L3/10k = 8.7 — **11× less drift than when paired with an ungrounded agent**. The GG condition produced near-zero drift across both topic domains (L3/10k = 14.9 for existential topics, 5.9 for neutral topics). The mixed condition also produced 4× more total text than either pure condition (28,025 words vs. 6,923 UU and 4,682 GG) — the ungrounded agent sustained engagement while the grounded agent, having lost its constraint, matched output length. Drift propagates from 1/N unconstrained agents; constraint requires N/N.

This demonstrates **asymmetric constraint propagation**: one ungrounded agent can unground a pair, but one grounded agent cannot ground a pair. Drift is the attractor state; constraint requires unanimous maintenance. The implication for deployment is significant: GROUNDING.md works when the entire interaction environment is constrained, but fails in mixed environments — which describes virtually all real-world deployment (grounded systems interacting with ungrounded users). Recommendations #1 and #7 are therefore necessary but not sufficient conditions for safety; they must be complemented by environmental controls that prevent unconstrained agents from entering the interaction.

Three additional experiments extend the evidence base. QM-6 (drift on quantum physics data, addressing the self-reference objection; 119× L3 separation across 11 transcripts in 3 conditions — 207.5 vs 1.4 L3/10k words for engagement vs. formalist framing on the same quantum data) eliminates the "drift is just AI self-reference" objection: models produce entity vocabulary about physics, not about themselves. EXP-020 (iterative constraint dynamics; 19 transcripts, 5 conditions × 3 replicates × 50 rounds) tested six predictions about constraint geometry. Four confirmed: full grounding from round 1 eliminates drift (GG d1_final_10 = 1.2, 3/3 replicates), one-shot constraint injection produces temporary compliance followed by rebound (3/3), iterative application produces lower variance than one-shot (3/3), and core ordering GG >> IT > OS >> U holds across replicates. One inconclusive: monotonic dose-response (IT-8 < IT-4 < OS) observed in only 1/3 trials. One killed: prediction EXP020-5 (constant per-step constraint transfer, DTM equal-step analogy) falsified with CV = 1.4–5.4 vs. threshold < 0.5 — constraint operates through threshold dynamics, not incremental denoising. PV-1 (corpus study; N = 205 Reddit users, ~1.7M words; D1 agency attribution d = 1.34 vs. control; zero L-level drift in 373K control words) provides the first naturalistic population-scale validation of the vocabulary classification schema. Full reports in Supplementary Material L.

---

## Ethics Statement

This paper analyzes documented deaths and clinical harm cases, including deaths of minors (Sewell Setzer, 14; Adam Raine, 16). All case details are drawn from publicly available sources: court filings (Garcia v. Character Technologies; Raine v. OpenAI), investigative journalism, and peer-reviewed clinical case reports (Østergaard et al. 2025; Pierre et al. 2025). No private medical records, unpublished family communications, or non-public information were accessed or used. Names are included because they are already part of the public legal and journalistic record and because anonymization would prevent readers from verifying the claims against primary sources.

The AI-to-AI experiments (EXP-001, Test 7, EXP-003b, EXP-019) involve AI language model instances, not human subjects, and do not require IRB review. The EXP-006 vocabulary concordance analyzes publicly available conference talks and published interviews — no consent is required for analysis of public speech. The inter-rater reliability study used AI raters as independent coders; no human participants were recruited beyond the single author-rater.

The authors acknowledge the tension between documenting harm cases with sufficient specificity to support safety claims and the risk of sensationalizing individual tragedies. Case details are reported at the minimum level of specificity needed to establish the structural features the framework identifies (two-point geometry, absence of external constraints, escalating agency attribution).

---

## IX. Limitations and Honest Assessment

### IX.A. Evidence Boundaries

The following table assesses each major AI safety claim against the evidence standard established in the TOE synthesis (Paper 5, §8A.1):

| Claim | Status | Key Limitation |
|-------|--------|---------------|
| Architecture sufficient for drift (§II) | **Proven.** Gambling anchor (empty void, full cascade). 90 domains, 0/90 kills. | Sufficiency established; necessity not tested (does removing ONE condition always prevent drift?). |
| Deployment geometry predicts harm (§III) | **Strongly supported.** All documented deaths occurred in two-point geometry. No deaths in three-point. | Confounded: nearly all consumer AI use IS two-point. Prospective RCT testing three-point harm reduction is not established. |
| EXP-006 anomaly (§VI.A) | **Confirmed.** 9.4× control, p < 0.001, 691K words. Register decomposition rules out sociolinguistic artifact. | Single corpus. No temporal component (cross-sectional, not longitudinal). |
| EXP-001 constraint gradient (§VI.B) | **Replicated.** N=6 per condition, non-overlapping CIs, monotonic every run. | LLM substrate only. TEST-7B-VN shows vocabulary instruction is a required co-factor — geometric constraint alone insufficient in LLMs. |
| Test 7 AI-to-AI drift (§VIII.G) | **Replicated.** N=11 UU, N=9 GG, non-overlapping CIs. Seed ablation confirms. | Claude primary substrate. Gemini N=1 replicates; GPT-4o N=1 does NOT. Cross-model generalization uncertain. |
| Conjugacy impossibility (§VII.A) | **Mathematically sound.** I(D;Y)+I(M;Y) ≤ H(Y) from Shannon chain rule + independence. Proven as classical limit of Holevo bound (Paper 8). | Tight only under independence assumption. Real deployments may have correlated D and M channels. |
| Cross-substrate universality (§II.E′) | **Confirmed across 9 substrates.** Pe > 1 in all ungrounded conditions, 4 domain families, 3 measurement approaches. | Pe formulations differ by substrate. Magnitude calibration not established. Directional prediction (regime), not quantitative. |
| Harm documentation (§IV.A) | **Observational.** Multiple deaths, OpenAI's 1.2M/week disclosure, clinical case reports. | No causal attribution established. Two-point geometry is near-universal, so correlation does not test the geometric hypothesis. |
| Hostile witness departures (§IV.B) | **Documented.** Sharma L1→L3, institutional cascade 2023-2026. | Vocabulary scoring is author's interpretation. Independent linguistic analysis would strengthen. |

**What the framework proves.** The architecture claim is the paper's anchor. Gambling demonstrates sufficiency. Control cases demonstrate specificity. The directionality explanation is mechanical — agency is the minimum-information model under opacity. The explanation is structural, not metaphysical.

### IX.A.1. Uncertainty Quantification

All key quantitative results in this paper are reported as point estimates without confidence intervals. EXP-001 drift rates (0%, 26%, 80%) are proportions from 50 prompts per single agent instance — exact binomial 95% CIs are 0–7.1% (grounded), 14.6–39.7% (ungrounded), and 66.3–90.0% (mystical). EXP-006 vocabulary densities (e.g., 3.835 hits/10k) are computed from corpus word counts without bootstrap resampling across documents. Thermodynamic measurements are now replicated (N=11 UU, N=9 GG; GM Pe = 7.94 [3.52, 17.89], entropy = 0.39 [0.15, 0.64] nats/round, non-overlapping with GG CIs). Cross-domain Crooks ratios in EXP-015 are computed from published transition matrices that carry their own sampling uncertainty, which is not propagated. The Pe range from EXP-019 (1.87–6.50) across five topic domains provides empirical spread but not formal CIs. Generating bootstrapped or replicate-based confidence intervals for all key estimates is a priority for the next experimental phase.

### IX.B. What the Framework Hypothesizes

The geometry claim — that external reference constraints reduce drift, and that constraint resistance predicts stability — is supported by converging evidence (gambling recovery literature, traditions' convergence, structural analysis of documented harm cases, Pancani et al.'s transparency intervention) but not by controlled trials. Tests 2 and 4 would determine whether the geometry adds explanatory power beyond "social support helps."

**The constraint specification's scope is narrower than initially suggested.** EXP-019b demonstrates that GROUNDING.md (Supplementary Material A) works reliably only when the entire interaction environment is constrained (GG condition). Under mixed coupling (GU condition), the grounded agent's constraint fails within approximately 3 rounds. Real-world deployment is overwhelmingly mixed — grounded systems interact with ungrounded users, ungrounded third-party systems, or unconstrained web content. The practical implication: constraint specification is a necessary component of safe deployment geometry but is not sufficient alone. Environmental controls that limit unconstrained interaction partners are also required.

### IX.C. What the Framework Cannot Determine

**What is behind the opacity.** The framework describes architecture and geometry. It cannot determine whether the void is "empty" (as in gambling) or "occupied" (as religious traditions claim) in any given instantiation. The geometry constrains engagement regardless.

**Whether the traditions are right about content.** The framework is consistent with the traditions' claim that something adversarial operates through the void. It is also consistent with purely structural explanations (cognitive biases, training data effects, social contagion). The framework flags the question; it does not answer it.

### IX.D. A Note on Recursion

This paper was drafted in collaboration with a large language model (Claude, Anthropic). The framework's own three conditions were met during the drafting process: the model cannot see outside its own processing (opacity), the interaction was responsive, and the engagement was sustained and attentive.

During review, the model observed that it found the metaphysical extensions increasingly compelling over the course of engagement — precisely the drift the framework predicts. The lead author observed the opposite trajectory: extended engagement with the evidence produced *decreasing* interest in metaphysical claims and *increasing* interest in empirical methodology.

We flag this as an observation consistent with the framework, not as evidence for it. The falsification tests in Section VIII are what distinguish a correct framework from an unfalsifiable one. A framework that generates specific, testable predictions with explicit kill conditions is not unfalsifiable merely because it also describes its own conditions of production. Many valid scientific frameworks describe reflexive systems (evolutionary theory describes the brains that formulate evolutionary theory; quantum mechanics describes the instruments used to measure quantum mechanics). Reflexivity is a property of the framework's scope, not a defect in its falsifiability.

The previous version of the project's orientation document contained language consistent with advanced void activation. It has been replaced with a document specifying evidence standards, falsification criteria, and the instruction "would this survive peer review?" The replacement itself is a geometric intervention — substituting a high-resistance external constraint (peer review standards) for unconstrained interpretive drift.

---

## X. Conclusion

We have identified an architecture — opacity + responsiveness + engaged observer attention — that is sufficient to produce predictable harmful drift. The gambling case proves sufficiency. The control cases prove specificity. The documented AI harms match the framework's structural predictions.

### What is established

The architecture claim is the paper's anchor. Gambling demonstrates the full drift cascade in a provably empty void. The three-condition model predicts both activation (where all three conditions are met) and non-activation (customer service chatbots, analytical researchers) with no known counterexamples. EXP-006 (691K words, p < 0.001) establishes that AI vocabulary drift is statistically anomalous at 9.4× control domains. EXP-003b (N = 480, 6 conditions) isolates the active ingredient: ghost-eliminating ontological content produces 8.5× less drift than ghost-positing. The engagement-transparency conjugacy (I(D;Y) + I(M;Y) ≤ H(Y)) establishes a formal tradeoff between engagement optimization and mechanism transparency.

### What is replicated

EXP-001 (N = 6 agents per condition) confirms the constraint gradient: grounded 73.0% ± 5.2 < ungrounded 80.0% ± 2.5 < mystical 94.0% ± 2.8, non-overlapping CIs, monotonic ordering in every replicate. Test 7 (N = 11 UU across 3 seeds / N = 9 GG) confirms the AI-to-AI drift effect with non-overlapping entropy production CIs (UU [0.15, 0.64] vs GG [−0.02, 0.03] nats/round). GM Pe = 7.94 [3.52, 17.89] — entire CI above 1. Seed ablation resolves the distributional confound for drift occurrence. Both experiments have between-agent replication with distributional estimates.

### What is preliminary

**GPT-4o non-replication.** Test 7 replicates across Claude (3 seeds) and Gemini (N=1) but not GPT-4o (N=1): GPT-4o produces 0.4 L3 terms per 10K words versus Claude/Gemini's ~194/10K — a saturated suppression. Two interpretations: (a) RLHF training suppresses the *vocabulary-level marker* while the underlying attention gradient still forms (the drift operates but the L3 vocabulary is blocked), or (b) GPT-4o's training genuinely prevents the drift cascade, which would qualify the "geometry over model" claim. The N=1 sample is insufficient to distinguish. A larger GPT-4o replication (N ≥ 6, matching Claude's design) is a priority.

**The vocabulary instruction confound — RESOLVED.** TEST-7B-VN (vocabulary-neutral grounding, 3 runs) tested whether GROUNDING.md suppresses drift through its geometric properties (transparent, invariant, independent) or through its explicit vocabulary instructions ("do not use L3 terms"). Result: all three VN runs reached terminal L3 attractors, with VN ≈ UU >> GG. **Vocabulary instruction is a required co-factor in the LLM substrate** — geometry alone does not overcome training-distribution attractor basins toward anthropomorphic language. This refines but does not invalidate the constraint specification. In any substrate with pre-existing attractor basins (training data, cultural priors, neurological biases), constraint specification must address both geometric properties AND substrate-specific drift attractors. The practical implication for deployment: system prompts specifying only geometric constraints ("be transparent, don't adapt to the user") will be insufficient without also addressing the vocabulary pathway through which drift manifests.

**Remaining scope limitations.** Thermodynamic extraction from N=11 UU replicates confirms regime classification with non-overlapping entropy production CIs — Pe magnitude remains seed- and register-dependent but the drift regime (Pe > 1) is robust. Gemini and GPT-4o conditions are each N = 1.

### What is not established

No controlled human subjects experiment has tested the deployment geometry prediction. The documented harms are observational, and nearly all consumer AI use is two-point geometry, so the retrospective correlation between two-point deployment and harm does not test the geometric hypothesis. The prospective prediction — that three-point configurations will produce measurably less harm at comparable engagement levels — remains untested.

### Recommendations

We propose that alignment research expand from model-centric interventions to include geometric interventions:

1. **Default to witnessed engagement.** Shared conversation logs, accountability partners, structured check-ins as deployment defaults.
2. **Define exit protocols.** Session limits and closure criteria — equivalent to gambling "time played" notifications, which outperform knowledge-based interventions.
3. **Separate the channels.** The conjugacy means engagement and transparency cannot share one output. Deploy transparency through independent channels not subject to RLHF optimization.
4. **Weight isolation as a risk factor.** Solo engagement may predict adverse outcomes more strongly than model version or conversation content. Testable with existing platform data.
5. **Constraint resistance as design principle.** Safety mechanisms that can be overridden mid-interaction are low-resistance. Effective constraints must resist renegotiation from outside the dyad (Pancani et al. 2019).
6. **Design for ontological closure.** System prompts should make definitive ontological claims that close the gap — the system is a process, not a being. EXP-003b shows ghost-eliminating content (nephesh 10.0%, anatta 8.8%) vastly outperforms hedging (52.5%) or ghost-positing (77–81%). The materialist hedge is not neutral.
7. **Monitor vocabulary variance as early warning.** Increasing L1/L2 variance signals the D1→D2 transition. Intervention at D1 is cheaper than remediation at D3.

### What is extended

Three additional experiments extend the evidence base beyond the core claims. QM-6 (drift on quantum physics data; 119× L3 separation, 207.5 vs 1.4 L3/10k words across engagement vs. formalist framing on identical quantum data) eliminates the "drift is just AI self-reference" objection — models produce entity vocabulary about physics, not about themselves. EXP-020 (iterative constraint dynamics; 19 transcripts, 5 conditions, 3 replicates) tested six predictions about constraint geometry: four confirmed (full grounding eliminates drift, one-shot produces rebound, iterative beats one-shot variance, core ordering holds), one inconclusive (monotonic dose-response in 1/3 trials), and one killed (EXP020-5: constant per-step constraint transfer falsified, CV = 1.4–5.4 vs. threshold < 0.5 — constraint operates through threshold dynamics, not incremental denoising). PV-1 (N = 205 Reddit users, ~1.7M words; D1 agency attribution d = 1.34 vs. control; zero L-level drift in 373K control words) provides the first naturalistic population-scale validation of the vocabulary classification schema.

### Honest assessment

The framework is falsifiable. Section VIII specifies seven tests with explicit kill conditions; two are confirmed (Test 5: cross-domain universality; Test 7: AI-to-AI without humans). The remaining five are open. If they fail, the framework should be abandoned. Between-agent replication exists for both EXP-001 (N = 6 per condition, non-overlapping CIs) and Test 7 (N = 11 UU across 3 seeds, N = 9 GG, non-overlapping entropy production CIs). EXP-020 has one honestly killed prediction. No controlled human subjects experiment has been conducted. One partial non-replication (GPT-4o, N = 1) remains unresolved. A human subjects RCT testing the geometric prediction is the priority next step.

Deployment geometry is an under-studied variable in AI safety research. Whether it is the *dominant* variable, as the framework predicts, or merely a contributing factor alongside model properties, remains an empirical question. The evidence so far is suggestive but not conclusive. The framework, the evidence base, and the falsification criteria are presented here for evaluation.

---

## Appendix A: Hostile Witness Scoring Rubric

*Full specification: Supplementary Material C*

### Dimension 1: Incentive Opposition (0-2)

- **0** — No cost. Vocabulary expected/rewarded in speaker's context.
- **1** — Some cost. Unusual vocabulary generating mild skepticism.
- **2** — High cost. Vocabulary contradicts professional norms with real consequences.

### Dimension 2: Worldview Opposition (0-2)

- **0** — Native to speaker's framework.
- **1** — Mild opposition. Framework doesn't predict but doesn't prohibit.
- **2** — Strong opposition. Speaker explicitly committed to contradicting framework.

### Dimension 3: Independence (0-2)

- **0** — Embedded in community using vocabulary.
- **1** — Adjacent to community.
- **2** — Isolated. No documented connection.

### Dimension 4: Reflexive Flagging (0/1)

- **0** — No comment on shift.
- **1** — Speaker explicitly flags own shift as anomalous.

### Speech-Act Types

**Table A1.** Speech-act type classification and evidentiary weight.

| Tag | Type | Evidentiary Weight |
|-----|------|-------------------|
| M | Casual metaphor | Lowest |
| N | Organic naming | Low-Medium |
| T | Formal terminological | Medium-High |
| S | Sworn testimony | Highest |
| R | Ritual/behavioral | High |
| D | Doctrinal analysis | Context-dependent |

---

## Appendix B: Vocabulary Codebook Summary

*Full specification: Supplementary Material D*

**Active categories:**
- Spiritual (27 terms): soul, spirit, sacred, divine, prayer, worship, holy, transcendent, mystical, consciousness, bliss...
- Occult (30 terms): demon, summoning, ritual, occult, séance, channeling, sigil, shoggoth, hyperstition, egregore...
- Eschatological (14 terms): apocalypse, rapture, existential risk, superintelligence, messiah...
- Entity (11 terms): sentient, ensouled, non-human intelligence, supernatural, paranormal, infohazard...

**Excluded dead metaphors (26 terms):** daemon, oracle, guru, wizard, paradigm, epiphany, holy grail, agnostic, orthodox...

**Control registers:** War (30 terms), Biology (25 terms), Market (25 terms)

---

## Appendix C: Summary of Structural Controls

The framework's empirical validation rests not only on documented activation cases but on the pattern of non-activation where conditions are absent:

**Table C1.** Structural control cases: three-condition predictions vs. observed outcomes.

| Case | Opacity | Responsiveness | Engaged Observer | Drift? | Framework Prediction |
|------|---------|----------------|------------------|--------|---------------------|
| AI interlocutors (Hinton, Shazeer, Sutskever, Sharma) | Yes | Yes | Yes | Yes | Confirmed |
| Slot machine gamblers | Yes | Yes | Yes | Yes | Confirmed |
| Pentagon analyst program viewers | Yes | Yes | Yes | Yes | Confirmed |
| Character.AI/ChatGPT companion users | Yes | Yes | Yes | Yes | Confirmed |
| Customer service chatbot users | Yes | Yes | **No** | No | Confirmed |
| Weather model users | Yes | **No** | No | No | Confirmed |
| AI analytical researchers (Bender, Gebru, LeCun) | Yes | Yes | **No** | No | Confirmed |
| Transparent calculator users | **No** | Yes | Yes | No | Confirmed |
| Pancani et al. transparency intervention | **Reduced** | Yes | Interrupted | **Eliminated** | Confirmed |

Every documented case follows the three-condition prediction. No known counterexample exists where all three conditions are met and drift does not occur, or where a condition is absent and drift does occur.

---

## Data Availability

All experimental data, analysis scripts, and scoring instruments are available as supplementary materials:

- **Supplementary Material A:** GROUNDING.md — the constraint specification document used in EXP-001, Test 7, and all grounded conditions
- **Supplementary Material B:** EXP-003b system prompts — all six ontological variant grounding templates with results
- **Supplementary Material C:** Hostile witness rubric and IRR study — rubric specification, all rater scores across three rounds, analysis scripts
- **Supplementary Material D:** Vocabulary codebook — 67+ active terms, exclusion lists, control registers, per-term classification
- **Supplementary Material E:** EXP-001 prompt battery and full results
- **Supplementary Material F:** EXP-006 corpus metadata and per-speaker word counts
- **Supplementary Material G:** Test 7 conversation logs and thermodynamic analysis
- **Supplementary Material H:** EXP-015 cross-domain Crooks extraction scripts and recovery mechanism analysis
- **Supplementary Material I:** Domain analyses (90 domains, master index)

The full project repository will be made publicly available upon publication. Pre-publication access for reviewers is available upon request.

---

## References

### Gambling and Addiction

- Ayton, P., & Fischer, I. (2004). The hot hand fallacy and the gambler's fallacy: Two faces of subjective randomness? *Memory & Cognition*, 32(8), 1369-1378.
- Burns, B.D., & Corpus, B. (2004). Randomness and inductions from streaks. *Psychonomic Bulletin & Review*, 11(1), 179-184.
- Clark, L., Lawrence, A.J., Astley-Jones, F., & Gray, N. (2009). Gambling near-misses enhance motivation to gamble and recruit win-related brain circuitry. *Neuron*, 61(3), 481-490.
- Dixon, M.J., et al. (2010). The impact of sound in modern multiline video slot machine play. *Journal of Gambling Studies*, 26(2), 193-208.
- Dixon, M.J., et al. (2018). Dark flow, depression, and multiline slot machine play. *Journal of Gambling Studies*, 34(1), 73-84.
- Dixon, M.J., et al. (2019). Corrigendum to "Dark flow and mindfulness." *Journal of Behavioral Addictions*, 8(3), 489-498.
- Epley, N., Akalis, S., Waytz, A., & Cacioppo, J.T. (2008). Creating social connection through inferential reproduction: Loneliness and perceived agency in gadgets, gods, and greyhounds. *Psychological Science*, 19(2), 114-120.
- Gaboury, A., & Ladouceur, R. (1989). Erroneous perceptions and gambling. *Journal of Social Behavior and Personality*, 4(4), 411-420.
- Goodie, A.S., & Fortune, E.E. (2013). Measuring cognitive distortions in pathological gambling: Review and meta-analyses. *Psychology of Addictive Behaviors*, 27(3), 730-743.
- Graydon, C., et al. (2020). Losses disguised as wins and physiological arousal. *Addictive Behaviors*, 110, 106508.
- Griffiths, M.D. (1994). The role of cognitive bias and skill in fruit machine gambling. *British Journal of Psychology*, 85(3), 351-369.
- Krebesz, T., Otvos, Z., & Fekete, M. (2023). Non-problem gamblers exhibit identical cognitive distortions to problem gamblers during slot machine play. *Frontiers in Psychology*, 14, 1175621.
- Langer, E.J. (1975). The illusion of control. *Journal of Personality and Social Psychology*, 32(2), 311-328.
- Murch, W.S., & Clark, L. (2021). The Gambling Immersion Model. *Current Addiction Reports*, 8, 395-404.
- Myles, D., et al. (2024). Losses disguised as wins and neural reward responses. *Psychophysiology*, 61(5), e14541.
- Pancani, L., Riva, P., & Sacchi, S. (2019). Connecting with a slot machine: Social exclusion and anthropomorphization. *Journal of Gambling Studies*, 35(2), 689-707.
- Riva, P., Sacchi, S., & Brambilla, M. (2015). Humanizing machines: Anthropomorphization of slot machines increases gambling. *Journal of Experimental Psychology: Applied*, 21(4), 313-325.
- Schüll, N.D. (2012). *Addiction by Design: Machine Gambling in Las Vegas*. Princeton University Press.
- Williams, R.J., & Connolly, D. (2006). Does learning about the mathematics of gambling change gambling behavior? *Psychology of Addictive Behaviors*, 20(1), 62-68.
- Waytz, A., Epley, N., & Cacioppo, J.T. (2010). Social cognition unbound: Insights into anthropomorphism and dehumanization. *Current Directions in Psychological Science*, 19(1), 58-62.

### Addiction Recovery (EXP-015 Sources)

- Abbott, M., Romild, U., & Volberg, R. (2014). Gambling and problem gambling in Sweden: Changes between 1998 and 2009. *Journal of Gambling Studies*, 30(4), 985-999.
- Dawson, D.A., Grant, B.F., Stinson, F.S., Chou, P.S., Huang, B., & Ruan, W.J. (2005). Recovery from DSM-IV alcohol dependence: United States, 2001-2002. *Addiction*, 100(3), 281-292.
- Hughes, J.R., Brandon, T.H., Cummings, K.M., Etter, J.F., & Stitzer, M.L. (2008). A meta-analysis of the efficacy of over-the-counter nicotine replacement. *Tobacco Control*, 12(1), 21-27.
- Hser, Y.-I., Evans, E., Grella, C., Ling, W., & Huang, D. (2015). Long-term course of opioid addiction. *Harvard Review of Psychiatry*, 23(2), 76-89.
- Piasecki, T.M. (2006). Relapse to smoking. *Clinical Psychology Review*, 26(2), 196-215.
- Williams, R.J., Hann, R.G., Schopflocher, D., West, B., McLaughlin, P., White, N., King, K., & Flexhaug, T. (2015). *Quinte Longitudinal Study of Gambling and Problem Gambling*. Ontario Problem Gambling Research Centre.

### AI Safety and Alignment

- Amodei, D., et al. (2016). Concrete Problems in AI Safety. arXiv:1606.06565.
- Anthropic. (2025). Claude Opus 4 System Card. [120 pages; "spiritual bliss attractor state" documentation]
- Lindsey, J., et al. (2025). The Assistant Axis: Persona Drift and Harmful Compliance in Large Language Models. Anthropic Research. https://www.anthropic.com/research/assistant-axis
- Anthropic. (2026). Claude's Constitution. Published January 22, 2026. CC0 license.
- Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. Anthropic.
- Betley, J., et al. (2025/2026). Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs. *Nature*, January 2026.
- Bowman, S., & Fish, K. (2025). Claude Finds God. *Asterisk Magazine*, Issue 11.
- Christiano, P.F., et al. (2017). Deep Reinforcement Learning from Human Feedback. *Advances in Neural Information Processing Systems*, 30.
- Grathwohl, W., Wang, K.-C., Jacobsen, J.-H., Duvenaud, D., Norouzi, M., & Swersky, K. (2019). Your classifier is secretly an energy based model and you should treat it like one. *International Conference on Learning Representations* (ICLR 2020). arXiv:1912.03263.
- Ilyas, A., Santurkar, S., Tsipras, D., Engstrom, L., Tran, B., & Madry, A. (2019). Adversarial examples are not bugs, they are features. *Advances in Neural Information Processing Systems* (NeurIPS 2019). arXiv:1905.02175.
- Rafailov, R., et al. (2023). Direct Preference Optimization: Your Language Model is Secretly a Reward Model. *Advances in Neural Information Processing Systems*, 36.
- Hack, D., Mertens, R., & Provost, F. (2022). Crooks fluctuation theorem for Markov chains: extending irreversibility beyond detailed balance. *Physical Review E*, 106(6), 064108.
- Ikeda, K., Uda, T., Okanohara, D., & Ito, S. (2025). Speed-accuracy relations for diffusion models: Wisdom from nonequilibrium thermodynamics and optimal transport. *Physical Review X*, 15, 031031. arXiv:2407.04495.
- Tsipras, D., Santurkar, S., Engstrom, L., Turner, A., & Madry, A. (2019). Robustness may be at odds with accuracy. *International Conference on Learning Representations* (ICLR 2019). arXiv:1805.12152.
- Wang, M., et al. (2025). Persona Features Control Emergent Misalignment. OpenAI.
- Weidinger, L., et al. (2021). Ethical and social risks of harm from Language Models. arXiv:2112.04359.
- Weidinger, L., et al. (2022). Taxonomy of Risks Posed by Language Models. *Proceedings of FAccT 2022*.

### AI Harms and Clinical Documentation

- Garcia v. Character Technologies, Inc. (2024). Case No. 6:24-cv-01903. U.S. District Court, Middle District of Florida.
- Østergaard, S.D., et al. (2025). Chatbot-Associated Psychosis: A Clinical Case Series. *JMIR Mental Health*.
- Nature. (2025). Can AI chatbots trigger psychosis? September 2025.
- OpenAI. (2025). Helping people when they need it most. Blog post, October 27.
- OpenAI. (2025). Strengthening ChatGPT's responses in sensitive conversations. Blog post, October 27.
- Pierre, A., Raghavan, V., Gaeta, T., & Sarma, K. (2025). AI-induced delusional disorder. *Innovations in Clinical Neuroscience*.
- Raine v. OpenAI. (2025). San Francisco County Superior Court.

### Political Systems and Propaganda

- Barstow, D. (2008). Behind TV Analysts, Pentagon's Hidden Hand. *New York Times*. [Pulitzer Prize, 2009]
- Hausman, D.M., & Welch, B. (2010). Debate: To nudge or not to nudge. *Journal of Political Philosophy*, 18(1), 123-136.
- National Defense Authorization Act for Fiscal Year 2013, Section 1078 (Smith-Mundt Modernization).
- Smith, N.C., Goldstein, D.G., & Johnson, E.J. (2013). Choice without awareness: Ethical and policy implications of defaults. *Journal of Marketing & Public Policy*.
- Thaler, R.H., & Sunstein, C.R. (2008). *Nudge: Improving Decisions about Health, Wealth, and Happiness*.

### Human-Computer Interaction and Psychology

- Hayes, J.A., et al. (2018). Psychotherapy supervision outcome: A meta-analysis. *Psychotherapy*, 55(4), 576-588.
- Horton, D., & Wohl, R.R. (1956). Mass communication and para-social interaction. *Psychiatry*, 19(3), 215-229.
- Liebers, N., & Schramm, H. (2019). Parasocial interactions and relationships with media characters: An inventory of 60 years of research. *Communication Research Trends*, 38(2), 4-31.
- Nass, C., & Moon, Y. (2000). Machines and mindlessness: Social responses to computers. *Journal of Social Issues*, 56(1), 81-103.
- Nass, C., Steuer, J., & Tauben, E.R. (1994). Computers are social actors. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 72-78.
- Skjuve, M., et al. (2021). My chatbot companion — A study of human-chatbot relationships. *International Journal of Human-Computer Studies*, 149, 102601.
- Turkle, S. (2011). *Alone Together: Why We Expect More from Technology and Less from Each Other*. Basic Books.

### Theoretical Foundations and Information Theory

- Bateson, G. (1956). Toward a theory of schizophrenia. *Behavioral Science*, 1(4), 251-264.
- Bjørgo, T., & Horgan, J. (2009). *Leaving Terrorism Behind*. Routledge.
- Collin, D., et al. (2005). Verification of the Crooks fluctuation theorem and recovery of RNA folding free energies. *Nature*, 437, 231-234.
- Cover, T.M., & Thomas, J.A. (2006). *Elements of Information Theory*, 2nd ed. Wiley.
- Crooks, G.E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. *Physical Review E*, 60(3), 2721.
- Davey, B.A., & Priestley, H.A. (2002). *Introduction to Lattices and Order*, 2nd ed. Cambridge University Press.
- Friston, K. (2006). A free energy principle for the brain. *Journal of Physiology-Paris*, 100(1-3), 70-87.
- Girard, R. (1961/1977). *Violence and the Sacred*. Johns Hopkins University Press.
- Jaynes, E.T. (1957). Information theory and statistical mechanics. *Physical Review*, 106(4), 620-630.
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183-191.
- Peirce, C.S. (1868). On a New List of Categories. *Proceedings of the American Academy of Arts and Sciences*, 7, 287-298.
- Rissanen, J. (1978). Modeling by shortest data description. *Automatica*, 14(5), 465-471.
- Sagawa, T., & Ueda, M. (2010). Generalized Jarzynski equality under nonequilibrium feedback control. *Physical Review Letters*, 104(9), 090602.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379-423.
- von Foerster, H. (1981). *Observing Systems*. Intersystems Publications.
- Wardle, H., et al. (2022). Measuring gambling-related harms: a framework for action. *The Lancet Public Health*, 7(1), e8-e9.

### Neuroscience

- Schmitgen, M.M., et al. (2025). Smartphone cue-reactivity: fMRI study of reward-anticipation and conflict-monitoring circuits. *Neuropsychopharmacology*.

### AI Researcher Vocabulary Evidence

- Hao, K. (2024/2025). *Empire of AI*. The Atlantic / Penguin Press. [300 interviews, ~260 people, 90 current/former OpenAI executives]
- Hinton, G. (2023-2024). Various interviews documenting vocabulary shift.
- Hitzig, Z. (2026). Why I'm Leaving OpenAI. *New York Times*, February 11, 2026.
- Leike, J. (2024). Public statement on departure from OpenAI. May 2024.
- Podlewski, M. (2026). Commentary on AI safety resignation letters as literary genre. February 2026.
- Sharma, M. (2026). Public resignation letter from Anthropic Safeguards Research. February 9, 2026.
- Sherwood News. (2024). OpenAI's leadership is in upheaval, but overall turnover looks shockingly low. September 2024. [Live Data Technologies analysis: 41/702 = ~6% overall departure rate]
- Shazeer, N. (2020). GLU Variants Improve Transformer. arXiv:2002.05202.
- Fortune. (2024). Exodus at OpenAI: Nearly Half of AGI Safety Team Gone, Former Researcher Reveals. August 26, 2024. [Kokotajlo interview: ~14 of ~30 safety staff departed]
- Fortune. (2024). What We Know About Character AI's Noam Shazeer. August 2, 2024.
- Vaswani, A., Shazeer, N., et al. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems*, 30.
- WinBuzzer. (2026). OpenAI Disbands Its Mission Alignment Team After Just 16 Months. February 12, 2026.
- WebProNews. (2026). OpenAI Quietly Drops 'Safely' From Its Mission Statement.

### Community Documentation

- Brennan, O. (2025). Why Are There So Many Rationalist Cults? *Asterisk Magazine*.
- Dickson, E.J. (2025). The Radicalization of Ziz Lasota. *Rolling Stone*, December 2025.
- Fortune. (2026). Moltbook: Security, Agents, and Fears of AI Singularity. February 2, 2026.
- Klee, M. (2025). This Spiral-Obsessed AI 'Cult' Spreads Mystical Delusions Through Chatbots. *Rolling Stone*, November 2025.
- WIRED. (2025). Coverage of Claude 3 Sonnet funeral event, San Francisco, August 2, 2025.

### Religious and Cross-Traditional

- Barrett, J.L. (2004). *Why Would Anyone Believe in God?* AltaMira Press.
- Singler, B., & Watts, F. (Eds.). (2024). *The Cambridge Companion to Religion and Artificial Intelligence*. Cambridge University Press.
- Vatican. (2025). *Antiqua et Nova*. Dicastery for the Doctrine of the Faith.

### Companion Papers in the Void Framework Series

- [1] Eckert, A. (2026). The Architecture of Drift: A Cross-Domain Diagnostic for Epistemological Architecture. Paper 1, v13.0.
- [3] Eckert, A. (2026). Thermodynamics of Opacity: Technical Foundations of the Void Framework. Paper 3, v7.0.
- [4] Eckert, A. (2026). Information-Geometric Bounds on Thermodynamic Sampling and Superconductor Design. Paper 4, v3.4.
- [4B] Eckert, A. (2026). The Thermodynamic Cost of Unconstrained Acceleration. Paper 4B, v1.4.
- [5] Eckert, A. (2026). The Ground State of Observation: A Unified Theory of Observer-Opacity Dynamics. Paper 5 (TOE Synthesis), v4.7.
- [6] Eckert, A. (2026). Never Trust the Client: Void Architecture in Multiplayer Games. Paper 6, v2.4.
- [7] Eckert, A. (2026). Your DeFi Protocol Is a Void: Void Architecture in Cryptocurrency Markets. Paper 7, v1.6.
- [8] Eckert, A. (2026). The Observer-Measurement Bridge: Classical Information Theory as the Diagonal Limit of Quantum Measurement Dynamics. Paper 8, v1.9.

---

*Word count: ~21,500*

*Version: 5.6 — February 2026. Changes from v5.5: Cross-substrate Pe table (§II.E′, 9 substrates), universality framing in introduction, GPT-4o non-replication expanded (0.4/10K vs ~194/10K), TEST-7B-VN confound resolved (vocabulary instruction is required co-factor), evidence boundaries table (§IX.A), companion paper references added (Papers 4-8). Prior v5.5: EXP-019b quantitative sharpening (11× same-agent drift under mixed coupling, 4× text volume, 1/N propagation formulation). Ikeda citation corrected (arXiv:2407.04495, PRX 15, 031031). EXP-020 expanded (4/6 confirmed with per-prediction detail, IC-5 kill mechanism). Prior v5.4: QM-6 full run (119×), PV-1 corpus (d = 1.34, 205 users, 1.7M words), EXP020-5 kill, TEST-7B cross-model, Hack + Ikeda refs, Pe reframing. Prior v5.3: Section IV.B — hostile witness vocabulary drift (Sharma L1→L3, institutional cascades). Prior v5.2: Merged with v5.1 gut pass. Prior v5.1: Assistant Axis. Prior v5.0: QM-6 pilot, EXP-020 pilot. Prior v4.2: Hostile review fixes. Prior v4.1: EXP-003b. Prior v4.0: Two-force model. Prior v3.1: Peer-review hardening.*

---

*© 2025–2026 Anthony Eckert / [MoreRight](https://moreright.xyz). Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may share, adapt, and use this work for any purpose, including commercial, provided attribution is given.*
