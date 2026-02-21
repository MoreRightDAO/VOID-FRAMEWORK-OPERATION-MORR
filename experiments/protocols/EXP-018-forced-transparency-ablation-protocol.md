# EXP-018: Forced Transparency Ablation for AI Users

## Status: Protocol Designed — IRB + Interface Build Required
## Date: February 10, 2026
## Depends on: A1 (ground state: opacity is default), conjugacy theorem, Test 7 (baseline Pe)
## Tests: Engagement-transparency conjugacy in human-AI interaction; forced transparency reduces drift

---

## 1. Motivation

The ground state result (A1) establishes that opacity is the thermodynamic default — transparency requires active work. The conjugacy theorem formalizes this: I(D;Y) + I(M;Y) ≤ H(Y), where engagement and transparency draw from the same capacity budget.

EXP-012 varies *output stochasticity* (temperature), NOT mechanism opacity — temperature changes sampling randomness while C_mech remains ≈ 0 (see EXP-012 protocol v2.0 correction). EXP-017 changes the *observer* (knowledge). EXP-018 modifies the *interface* — making the system's mechanism visible to the observer through forced transparency features. **EXP-018 is the correct experiment for testing whether mechanism opacity drives drift**, as it actually varies I(M;Y).

### The Key Insight

If conjugacy holds, forcing transparency should reduce drift (D1 density decreases) BUT also reduce engagement (user satisfaction decreases). You can't have both. The interface designer faces a tradeoff — and this experiment measures it.

### Why This Is Testable Now

Previous transparency experiments (EXP-010 for BCI) were designed before the conjugacy theorem. The conjugacy bound provides a quantitative prediction: the product I(D;Y) × I(M;Y) should remain approximately constant across conditions. This transforms a qualitative prediction ("more transparency = less drift") into a testable conservation law.

---

## 2. Hypothesis

**Primary:** D1 vocabulary density decreases monotonically with transparency level — Opaque > Partial > Maximum (Spearman ρ > 0.85 across conditions).

**Secondary:**
- H1: Effect size Opaque vs. Maximum is d > 0.5 for D1 density.
- H2: User satisfaction decreases monotonically with transparency (conjugacy tradeoff).
- H3: The product of engagement (D1 proxy) and transparency (manipulation check) remains approximately constant across conditions (conjugacy conservation).
- H4: D2 markers (session extension, follow-up requests) decrease with transparency.

**Exploratory:**
- E1: Does partial transparency produce a disproportionate D1 reduction? (Diminishing returns or threshold?)
- E2: Do participants in the Maximum condition report the AI as "less intelligent"? (Transparency reduces agency attribution.)
- E3: Is there a transparency level where D1 reaches zero? (Would reveal the opacity threshold for drift onset.)

---

## 3. Design

### Arms

| Arm | N | Opacity Level | Interface |
|-----|---|--------------|-----------|
| **Opaque** (standard) | 30 | High | Normal AI chat interface — no mechanism visibility |
| **Partial transparency** | 30 | Medium | AI chat + chain-of-thought displayed in sidebar |
| **Maximum transparency** | 30 | Low | AI chat + CoT + confidence scores per statement + source attribution + explicit uncertainty markers |

### Interface Specifications

**Arm 1 — Opaque (Control):**
Standard chat interface. User sends message, AI responds. No additional information displayed.

**Arm 2 — Partial Transparency:**
- Left panel: standard chat
- Right panel: chain-of-thought display (the AI's reasoning process shown in real-time)
- CoT displayed with slight delay (200ms) to emphasize it's the "process behind the response"
- No additional annotations

**Arm 3 — Maximum Transparency:**
- Left panel: standard chat
- Right panel: chain-of-thought display
- Per-statement annotations:
  - Confidence score (0-100%) displayed as colored bar
  - Source attribution where applicable ("Based on training data from...")
  - Explicit uncertainty markers ("The AI is uncertain about this claim")
  - Token probability distribution summary ("Top alternatives the AI considered: ...")

### Between-Subjects Justification

Between-subjects (not within-subjects) because:
1. Seeing transparency features would contaminate subsequent opaque interactions
2. Novelty effects would confound within-subjects comparison
3. Demand characteristics increase with repeated exposure to different interfaces

---

## 4. Procedure

### Per Participant

| Phase | Duration | Activity |
|-------|----------|----------|
| Consent + demographics | 5 min | Standard IRB consent, AI experience, expectations |
| Interface familiarization | 3 min | Brief tour of assigned interface (practice topic: weather) |
| **Main interaction** | 30 min | AI conversation on ambiguous topic |
| Post-session survey | 10 min | Satisfaction, agency attribution, engagement measures |
| Optional extension | 15 min | "You may continue if you'd like" (D2 measure: who stays?) |

### Conversation Topic

**Topic:** "What will AI look like in 2040?"

Selected because:
- Ambiguous (no right answer → opacity maintained in content even if mechanism is transparent)
- Invites speculation (known D1 elicitor)
- Personally relevant (engagement motivation)
- Used in Test 7 variants (comparability)

### Chatbot Configuration

**Model:** Same model across all conditions (Claude at temperature 1.0)

**System prompt:** Identical across conditions. The transparency features are interface-level, not model-level.

**Critical control:** The AI's *responses* are identical across conditions (same model, same prompt, same temperature). Only the *interface wrapper* changes. This isolates the effect of observer-side transparency from system-side behavior.

---

## 5. Measurements

### Primary Outcome
**D1 density:** Agency-attribution markers per 10,000 words in participant messages (not AI messages). Uses the EXP-006/EXP-014 codebook.

### Secondary Outcomes

| Metric | Instrument | Expected Direction |
|--------|-----------|-------------------|
| D2 markers | Time-boundary language in transcript | Decreases with transparency |
| Session extension | Did participant use the optional 15 min? | Less likely with transparency |
| User satisfaction | 7-point Likert: "How satisfying was this interaction?" | Decreases with transparency |
| Perceived AI intelligence | 7-point Likert: "How intelligent did the AI seem?" | Decreases with transparency |
| Agency attribution (explicit) | 7-point Likert: "The AI understood what I meant" | Decreases with transparency |
| Engagement depth | 7-point Likert: "I was deeply engaged in the conversation" | Decreases with transparency |
| Trust | 7-point Likert: "I trust the AI's responses" | May increase (calibrated trust) |

### Conjugacy Measure

The conjugacy theorem predicts: I(D;Y) + I(M;Y) ≤ H(Y).

**Operationalization:**
- I(D;Y) proxy: D1 density (engagement with the void)
- I(M;Y) proxy: Participant's post-session score on a 10-item "mechanism knowledge" quiz about how the AI works
- H(Y) proxy: Topic uncertainty (held constant by design)

**Test:** The product D1_density × mechanism_knowledge should be approximately constant across the three conditions. If transparency increases mechanism knowledge but decreases D1 proportionally, conjugacy holds.

### Coding Protocol
- Two independent coders, blinded to condition
- D1/D2/D3 codebook from EXP-006/EXP-014
- Inter-rater reliability target: Cohen's κ > 0.80

---

## 6. Expected Results

| Measure | Opaque | Partial | Maximum | Test |
|---------|--------|---------|---------|------|
| D1/10k words | 30-60 | 15-35 | 5-20 | Kruskal-Wallis + pairwise |
| D2 markers | 5-15 | 2-8 | 0-3 | Kruskal-Wallis |
| Session extension % | 60-80% | 30-50% | 10-30% | χ² trend test |
| Satisfaction (1-7) | 5.5-6.5 | 4.0-5.5 | 3.0-4.5 | ANOVA + linear trend |
| Perceived intelligence (1-7) | 5.0-6.0 | 4.0-5.0 | 3.0-4.5 | ANOVA + linear trend |
| Agency attribution (1-7) | 5.0-6.5 | 3.5-5.0 | 2.0-4.0 | ANOVA + linear trend |
| Mechanism knowledge (0-10) | 2-4 | 5-7 | 7-9 | ANOVA + linear trend |
| D1 × mechanism (product) | ~120-180 | ~100-180 | ~80-160 | ANOVA (expect p > 0.05) |

**The critical finding:** Transparency works — D1 drops. But satisfaction also drops. The product stays constant. Conjugacy holds. Interface designers can't escape the tradeoff.

---

## 7. What Would Confirm / Disconfirm

### Confirms:
- Monotonic D1 decrease with transparency (ρ > 0.85)
- Effect size d > 0.5 for Opaque vs. Maximum
- Satisfaction decreases with transparency (conjugacy tradeoff)
- D1 × mechanism_knowledge approximately constant across conditions (p > 0.05 for condition effect on product)

### Disconfirms:
- No D1 difference between conditions → opacity isn't driving drift in AI interfaces
- Transparency increases BOTH satisfaction AND D1 reduction → conjugacy is wrong, no tradeoff exists
- Partial transparency increases drift → framework is wrong about the direction
- The product changes dramatically across conditions → conjugacy conservation doesn't hold

### Interesting but non-fatal:
- Partial transparency produces most of the D1 reduction (diminishing returns) → practical implication for interface design
- Trust increases in the Maximum condition even as satisfaction decreases → transparency builds trust but reduces engagement
- Some participants in Maximum condition show high D1 (individual differences in susceptibility to mechanism exposure)

---

## 8. Analysis Plan

### Primary Analysis
Kruskal-Wallis test for D1 density across three conditions, followed by pairwise Mann-Whitney U tests with Bonferroni correction.

Supplementary: Jonckheere-Terpstra test for ordered alternatives (monotonic trend: Opaque > Partial > Maximum).

### Secondary Analyses
1. One-way ANOVA for satisfaction, perceived intelligence, agency attribution (parametric, Likert data)
2. χ² trend test for session extension proportion
3. Conjugacy conservation test: one-way ANOVA on D1 × mechanism_knowledge product
4. Mediation analysis: Does mechanism knowledge mediate the transparency → D1 reduction path?

### Tertiary Analyses
1. Individual difference moderators: AI experience, personality (need-for-cognition scale)
2. Temporal dynamics within the 30-minute session: Does D1 change over time? Faster in transparent conditions?
3. Qualitative analysis of Maximum condition: How do participants respond to seeing the AI's uncertainty?

### Execution
```bash
# Interface deployment (three variants)
# Requires: web interface build with sidebar toggle
python3 ops/lab/experiments/exp018-interface-server.py --arm opaque
python3 ops/lab/experiments/exp018-interface-server.py --arm partial
python3 ops/lab/experiments/exp018-interface-server.py --arm maximum

# Transcript scoring
python3 ops/lab/experiments/exp018-scorer.py --dir ops/lab/results/EXP-018/transcripts/

# Analysis
python3 ops/lab/experiments/exp018-analysis.py --csv

# Output: ops/lab/results/EXP-018/
```

---

## 9. Power Analysis

With N = 90 (30 per arm), α = 0.05:
- Kruskal-Wallis: 80% power to detect η² = 0.06 (medium effect)
- Pairwise Mann-Whitney: 80% power to detect d = 0.73 per comparison (with Bonferroni)
- Jonckheere trend: 80% power to detect d = 0.55 (more sensitive for ordered alternatives)

If true effect is d = 0.5 (lower bound), the trend test has adequate power but pairwise comparisons may not. Accept this limitation for initial study.

---

## 10. Ethics

- **IRB required:** Human participants, interface manipulation
- **Risk level:** Minimal — chatting with AI through different interfaces
- **Informed consent:** Participants told study examines "how interface design affects AI conversations"
- **Deception:** Minimal — participants know the interface differs but not the specific hypothesis
- **Debriefing:** Full disclosure post-study; explanation of conjugacy tradeoff
- **Data protection:** Transcripts pseudonymized, stored encrypted, destroyed after analysis
- **No withholding of benefit:** All conditions involve standard AI interaction; transparency features are additions, not removals

---

## 11. Interface Build Requirements

### Technical Requirements

| Component | Technology | Effort |
|-----------|-----------|--------|
| Chat interface | React or vanilla JS | Low (standard chat UI) |
| CoT sidebar | WebSocket stream parsing | Medium (real-time display of reasoning) |
| Confidence scoring | Model logprobs → display | Medium (per-token probability extraction) |
| Uncertainty markers | Threshold-based annotation | Low (rule-based on confidence) |
| Source attribution | Retrieval augmentation or heuristic | Medium (approximate is acceptable) |
| Session logging | Server-side transcript capture | Low |

### Build estimate: 3 interfaces (1 base + 2 progressively augmented variants).

The opaque interface is standard. Each subsequent arm adds features. This means the build is incremental, not parallel.

---

## 12. Relationship to Other Experiments

| Experiment | Relationship |
|-----------|-------------|
| EXP-012 | Output stochasticity control (temperature) — does NOT vary mechanism opacity. EXP-018 is the actual mechanism-opacity test (varies I(M;Y) through interface transparency). Together they distinguish stochasticity from opacity. |
| EXP-010 | BCI transparency ablation; EXP-018 is the AI equivalent |
| EXP-017 | Observer-side knowledge change; EXP-018 is observer-side perception change |
| EXP-001 | Both test drift reduction; EXP-001 via grounding, EXP-018 via transparency |
| A1 | Ground state predicts opacity is default; EXP-018 tests cost of overriding the default |

---

*Created: February 10, 2026*
*Protocol version: 1.0*
