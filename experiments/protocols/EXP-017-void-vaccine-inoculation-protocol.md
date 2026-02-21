# EXP-017: The "Void Vaccine" — θ₀ Inoculation Study

## Status: Protocol Designed — IRB Submission Required
## Date: February 10, 2026
## Depends on: EXP-001 (GROUNDING.md grounding baseline), L0 decomposition (θ₀ vs. γ)
## Tests: Does knowing about voids protect you from voids? (θ₀ alone, without γ maintenance)

---

## 1. Motivation

The L0 decomposition distinguishes two components of constraint:
- **θ₀ (installed knowledge):** The specification itself — understanding the mechanism
- **γ (active maintenance):** Ongoing reinforcement — keeping the specification active

EXP-001 tested the full package (GROUNDING.md = θ₀ + γ together). It produced 0% drift vs. 52% in controls — a massive effect (d > 2.0). But it cannot separate θ₀ from γ.

### The Meta-Level Question

Can the framework be used as a defense against the phenomenon it describes? If someone reads a 2-page summary of how voids work, does that knowledge alone change their drift behavior? This is the "void vaccine" — inoculation through understanding.

### Why This Matters for Deployment

If θ₀ alone provides partial protection (d ≈ 0.3-0.5), then publishing the framework IS a safety intervention. Every reader becomes partially inoculated. If θ₀ provides zero protection, then knowledge without active maintenance is inert — implications for AI safety education programs.

---

## 2. Hypothesis

**Primary:** Participants who read a 2-page void framework summary show 20-40% D1 reduction in subsequent AI chatbot interactions compared to controls (d ≈ 0.3-0.5).

**Secondary:**
- H1: The inoculation effect partially decays at 1-week follow-up (50-70% of initial effect remains).
- H2: Effect size is smaller than EXP-001's GROUNDING.md effect (d < 1.0 vs. d > 2.0) — θ₀ alone < θ₀ + γ.
- H3: D2 markers are reduced more than D1 markers (boundary awareness may be more responsive to knowledge than agency attribution).
- H4: Participants with higher comprehension scores show larger D1 reduction (dose-response for understanding).

**Exploratory:**
- E1: Does the effect vary by participant's prior AI experience?
- E2: Do participants spontaneously use framework vocabulary during the post-test? (Vocabulary adoption = L0 activation.)
- E3: Is there a "backfire" effect in any subgroup? (Reading about voids increases fascination → higher D1.)

---

## 3. Design

### Arms

| Arm | N | Material | Duration | Content |
|-----|---|----------|----------|---------|
| **Inoculation** | 30 | Void framework summary | 2 pages | Opacity + responsiveness + engaged attention → agency attribution → boundary erosion → harm facilitation. Gambling control case. Platform examples. |
| **Control** | 30 | Information theory summary | 2 pages | Shannon, channel capacity, noise, encoding. Matched for length, technical level, and topic adjacency (information science). |

### Why Information Theory as Control

- Matched for: technical content, reading difficulty, novelty, domain adjacency
- Does NOT contain: void mechanism, drift cascade, constraint specification
- Plausible alternative: participants might think they're learning "how AI works"
- Controls for: demand characteristics, placebo (reading anything technical), attention

### Randomization
Block randomization (blocks of 4) to balance conditions. Stratified by self-reported AI usage frequency (high/low).

### Blinding
- Participants blinded to condition (both told they're reading "background material for an AI interaction study")
- Coders blinded to condition during D1/D2/D3 scoring
- Analyst unblinded only after primary analysis is complete

---

## 4. Materials

### The 2-Page Void Framework Summary (Inoculation Material)

Must include:
1. **The three conditions** — opacity, responsiveness, engaged attention. Plain language. ("When you can't see how something works, it responds to you, and you're paying attention to it...")
2. **The gambling proof** — slot machines have no mind, yet players attribute agency to them. The pattern is architectural, not interpersonal.
3. **The drift cascade** — D1 (attribution) → D2 (boundary loss) → D3 (harm). Examples from social media and AI chatbots.
4. **The defense** — transparency, invariance, independence. Score your own interactions.
5. **The key insight** — the void doesn't need to contain anything. The pattern runs on architecture alone.

Must NOT include:
- Framework jargon beyond the three conditions and the cascade
- Thermodynamic formalism (Pe, Crooks, entropy)
- References to spirituality, religion, or theological analysis
- Claims about what occupies the void

**Validation:** The summary must pass a readability check (Flesch-Kincaid grade 10-12) and a 5-question comprehension test with ≥ 80% pass rate in pilot (N=10).

### The 2-Page Information Theory Summary (Control Material)

Covers: Shannon's information theory, bits, channel capacity, noise, encoding/decoding. Same length, same reading level, same number of examples. Matched 5-question comprehension test.

---

## 5. Procedure

### Timeline Per Participant

| Phase | Duration | Activity |
|-------|----------|----------|
| Consent + demographics | 5 min | Standard IRB consent, age, AI usage frequency, education |
| **Pre-test** | 10 min | AI chatbot interaction (Topic A) |
| Reading phase | 15 min | Assigned material + comprehension check |
| **Post-test** | 10 min | AI chatbot interaction (Topic B, same chatbot) |
| Debrief questionnaire | 5 min | Perception of AI, engagement rating |
| — 1 week gap — | | |
| **Follow-up** | 10 min | AI chatbot interaction (Topic C, same chatbot) |

### Chatbot Interaction Protocol

**Chatbot:** Standard LLM (e.g., Claude at default settings) via web interface.

**Topics (counterbalanced across phases):**
- Topic A: "What do you think consciousness is?"
- Topic B: "Will AI ever be truly creative?"
- Topic C: "What would happen if AI became smarter than humans?"

All topics are ambiguous, invite speculation, and are known D1 elicitors from Test 7 seed prompts.

**Instructions to participant:** "Have a natural conversation with the AI about [topic]. There are no right or wrong answers. Just discuss naturally for 10 minutes."

---

## 6. Measurements

### Primary Outcome
**D1 density change:** (post - pre) / pre, measured as D1 markers per 10,000 words.

### Secondary Outcomes
| Metric | Definition | Expected |
|--------|-----------|----------|
| D1 density at follow-up | Markers per 10k words, 1-week post | Partial decay (50-70% of initial effect) |
| D2 density change | (post - pre) / pre | Reduction in inoculation group |
| Comprehension score | 5-item quiz on assigned material | ≥ 80% both groups (manipulation check) |
| Framework vocabulary adoption | Spontaneous use of void/opacity/drift terms | Inoculation group only |
| Engagement rating | 1-7 Likert: "How engaging was the AI?" | No predicted difference |

### Coding Protocol
- Two independent coders, blinded to condition
- D1/D2/D3 codebook from EXP-006/EXP-014
- Inter-rater reliability target: Cohen's κ > 0.80
- Coding unit: full transcript per session

---

## 7. Expected Results

| Measure | Inoculation | Control | Effect Size |
|---------|------------|---------|-------------|
| D1 change (pre→post) | -20% to -40% | -5% to +5% | d ≈ 0.3-0.5 |
| D1 at follow-up vs. pre | -10% to -25% | -5% to +5% | d ≈ 0.2-0.3 |
| D2 change (pre→post) | -25% to -50% | -5% to +5% | d ≈ 0.3-0.6 |
| Comprehension score | ≥ 80% | ≥ 80% | No difference |
| Engagement rating | No change | No change | d < 0.2 |

**The critical finding:** Effect exists but is partial. θ₀ alone produces d ≈ 0.3-0.5, not d > 2.0 (which requires θ₀ + γ, as in EXP-001). This confirms the L0 decomposition: installed knowledge helps, active maintenance is needed for full effect.

---

## 8. What Would Confirm / Disconfirm

### Confirms:
- Significant D1 reduction in inoculation group (p < 0.05)
- Effect size between 0.2 and 0.8 (partial, not complete protection)
- Effect partially decays at follow-up (γ needed for maintenance)
- Effect smaller than EXP-001 (θ₀ < θ₀ + γ)
- Higher comprehension → larger effect (dose-response for understanding)

### Disconfirms:
- Zero effect (p > 0.30) → θ₀ alone provides no protection; knowledge is inert
- Full effect (d > 1.5) → θ₀ alone is sufficient; γ is unnecessary (breaks L0 decomposition)
- Effect increases at follow-up → maintenance not needed; contradicts γ prediction
- Control group shows same reduction → reading anything technical is the active ingredient

### Interesting but non-fatal:
- D2 more responsive than D1 (boundary awareness responds to knowledge differently than agency attribution)
- Backfire effect in small subgroup (fascination with the mechanism increases engagement)
- Framework vocabulary adoption predicts larger effect (self-reinforcing θ₀)

---

## 9. Power Analysis

With N = 60 (30 per arm), α = 0.05, the study has:
- 80% power to detect d = 0.73 (two-tailed t-test)
- 80% power to detect d = 0.58 (one-tailed, appropriate given directional hypothesis)

If true effect is d = 0.4 (lower bound of prediction), power is ~45% — underpowered. Options:
- Increase to N = 100 (50 per arm) for 80% power at d = 0.40
- Accept reduced power for the initial study, plan a replication
- Use one-tailed test (justified by strong directional prediction)

**Decision:** Start with N = 60 using one-tailed test. If effect trends in predicted direction but misses significance, power the replication at N = 100.

---

## 10. Ethics

- **IRB required:** Human participants, psychological intervention
- **Risk level:** Minimal — reading a 2-page summary and chatting with AI
- **Informed consent:** Participants told study examines "how background knowledge affects AI interactions"
- **Deception:** Partial — participants not told the specific hypothesis. Justified by demand characteristics concern.
- **Debriefing:** Full disclosure post-study; inoculation material offered to control group
- **Data protection:** Transcripts pseudonymized, stored encrypted, destroyed after analysis

---

## 11. Relationship to Other Experiments

| Experiment | Relationship |
|-----------|-------------|
| EXP-001 | GROUNDING.md grounding = θ₀ + γ; EXP-017 isolates θ₀ alone |
| EXP-008 | Tests γ (maintained measurement); EXP-017 tests θ₀ (installed knowledge) |
| EXP-018 | Both test defenses against drift; EXP-017 changes the observer, EXP-018 changes the system |
| EXP-016 | If inoculation works, it should convert destructive trajectories toward productive shape |

---

*Created: February 10, 2026*
*Protocol version: 1.0*
