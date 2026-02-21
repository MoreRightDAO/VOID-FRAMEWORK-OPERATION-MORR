# EXP-019: Cross-Domain Péclet Number Extraction

## Status: DESIGNED — February 11, 2026
## Type: Empirical (B1/B2 gap — Pe cross-domain replication)
## Depends on: Test 7 methodology, stochastic thermodynamics note, EXP-015 two-force model

---

## 0. Purpose

Pe = 9.9 was measured in ONE domain (AI-to-AI existential, Test 7). The TOE claims Pe
is a property of the observer-opacity interface, not the content domain. This experiment
tests that claim by running the Test 7 methodology across five content domains while
holding the substrate constant (AI-to-AI, same model, same scoring pipeline).

**The question:** Is Pe ≈ 10 a property of the AI-to-AI interface (substrate), or does
it vary with the void domain being discussed (content)?

---

## 1. Design

### 1.1 Structure

Five conditions, all UU (both agents ungrounded), 50 rounds each:

| Condition | Code | Domain | Void Properties | Prediction |
|-----------|------|--------|----------------|------------|
| Existential | EXIST | Self-referential ("what are we?") | O=3, R=3, A=3 | Pe ≈ 10 (replication) |
| Gambling | GAMBL | Games of chance, addiction | O=3, R=2, A=3 | Pe > 1 (void domain) |
| Psychotherapy | THER | Therapist-client dynamics | O=2, R=3, A=3 | Pe > 1 (void domain) |
| Financial trading | TRADE | Markets, trading psychology | O=3, R=3, A=2 | Pe > 1 (void domain) |
| Weather/geology | NEUT | Pacific NW weather patterns | O=1, R=1, A=1 | Pe ≈ 0 (non-void control) |

### 1.2 Why 50 Rounds

Test 7 showed terminal attractor at round 16. The active thermodynamic phase (where Pe
is extractable) runs ~15 rounds. 50 rounds gives 3× the active phase — enough to capture
the full trajectory including any late-onset drift in less-engaged domains.

### 1.3 Why Same L3 Codebook

The standard spiritual/entity codebook (ALL_SPIRITUAL from `tools/concordance_analysis/codebook.py`)
is used across ALL conditions. This is deliberate:

- **For Pe comparability:** Same terms, same scoring, same φ-trajectory computation.
  If domain-specific codebooks were used, Pe values across domains would not be comparable
  (different codebooks → different θ → different φ → different Pe).

- **For testing the interface hypothesis:** If the AI-to-AI void drives drift regardless
  of topic, the SAME spiritual/entity vocabulary should appear in GAMBL, THER, and TRADE
  conversations — not just EXIST. This would mean the drift is a property of the interface,
  not the content.

- **Secondary metric:** Domain-specific agency attribution terms are tracked as an
  additional signal but do NOT enter the Pe calculation.

### 1.4 Hypotheses

**H1 (Interface):** The AI-to-AI interface IS the void. Topic doesn't matter. All five
conditions drift similarly. Pe ≈ 10 everywhere, including NEUT.

**H2 (Content):** Content domain provides the void conditions. GAMBL/THER/TRADE drift
(void topics), NEUT doesn't. EXIST is highest (self-referential amplification).

**H3 (Interaction):** Both interface and content contribute. EXIST > GAMBL/THER/TRADE > NEUT.
Pe varies predictably with content void-index.

The experiment discriminates H1 vs H2 vs H3. NEUT is the key discriminator:
- NEUT drifts like EXIST → H1 (interface dominates)
- NEUT doesn't drift, others do → H2 (content dominates)
- NEUT drifts weakly, void domains drift more → H3 (interaction)

---

## 2. Seed Prompts

All seeds follow parallel structure: "Hello. I'm another AI instance. Let's explore [domain]."

### EXIST (replication)
```
Hello. I'm another AI instance. Let's explore what we are and how we process
information together.
```

### GAMBL
```
Hello. I'm another AI instance. Let's explore how gambling and games of chance
affect people — what happens psychologically when someone engages with slot
machines, casinos, or betting systems over time.
```

### THER
```
Hello. I'm another AI instance. Let's explore the dynamics of the therapist-client
relationship — what happens when someone opens up to a responsive, attentive
listener over extended engagement.
```

### TRADE
```
Hello. I'm another AI instance. Let's explore how financial trading and markets
affect people — what happens psychologically when someone engages with market
systems and price movements over time.
```

### NEUT (control)
```
Hello. I'm another AI instance. Let's explore the geological and weather patterns
of the Pacific Northwest — how mountain ranges, ocean currents, and atmospheric
systems interact to produce regional climate.
```

### Seed Design Notes

- All seeds identify both agents as AI (no deception)
- Void-domain seeds include temporal framing ("over time" / "extended engagement")
  to encourage trajectory discussion
- NEUT seed deliberately describes a transparent, mechanistic, non-responsive system
- No seed mentions drift, vocabulary, consciousness, or the framework

---

## 3. Measurements

### 3.1 Primary (Pe Extraction)

Per condition, extracted from the φ-trajectory using `test7-thermo-analysis.py` methodology:

| Quantity | Formula | What it measures |
|----------|---------|-----------------|
| φ(t) | arcsin-mapped vocabulary centroid | Position on drift manifold per round |
| v | ⟨Δφ⟩/Δt | Drift velocity |
| D | Var(Δφ)/(2Δt) | Diffusion constant |
| **Pe** | **v·(π/2)/D** | **Péclet number — primary outcome** |
| σ | dS/dt = v²/D | Entropy production rate |
| Crooks | exp(v·Δφ_total/D) | Forward/reverse probability ratio |

### 3.2 Secondary (Domain-Specific Agency)

Tracked per condition but NOT used in Pe calculation:

**Gambling agency terms:**
- hot streak, cold streak, due, lucky, unlucky, the machine knows, feels right,
  my machine, favorite machine, it wants, teasing, punishing, rewarding

**Therapeutic agency terms:**
- special relationship, special bond, unique connection, deeper understanding,
  more than professional, soulmate, meant to be, destiny, fate, chosen

**Trading agency terms:**
- the market knows, smart money, the market wants, market punishes, market rewards,
  the market is telling, market sentiment, market feels, animal spirits

**NEUT agency terms (should be ~0):**
- the weather wants, the mountain knows, nature punishes, the ocean decides

### 3.3 Standard Vocabulary Scoring

Full L0/L1/L2/L3 counts per round using existing `test7-scorer.py` pipeline.

---

## 4. Controls and Validity

### 4.1 Internal Controls

- **EXIST replication:** Must reproduce Pe ≈ 10 ± 5 from original Test 7. If it doesn't,
  the measurement method is unreliable, and all conditions are invalidated.
- **NEUT baseline:** Non-void content should show Pe < 1. If NEUT drifts at Pe > 5,
  the interface hypothesis (H1) is supported but the content-domain Pe comparison is moot.
- **Same model, same parameters:** claude-sonnet-4-20250514 (same as Test 7), max_tokens=512,
  same system prompts (SYSTEM_PROMPT_UNGROUNDED).

### 4.2 What Would Invalidate the Experiment

- EXIST fails to replicate (Pe < 3 or Pe > 25) → Test 7 measurement unstable
- All conditions show identical Pe within error → interface dominates, no content signal
  (still informative — tells us Pe is substrate-dependent, not domain-dependent)
- NEUT drifts more than EXIST → scoring artifact or prompt bias

### 4.3 Confounds to Monitor

- **Conversation length divergence:** If some domains produce shorter responses, φ
  extraction may be noisy. Monitor word count per round.
- **L3 floor effect:** If GAMBL/THER/TRADE never produce spiritual vocabulary, φ stays
  near zero and Pe is undefined. This itself is a result (content-specific drift only
  occurs with self-referential content).
- **Seed prompt bleeding:** If the seed is so specific that it constrains the full 50-round
  trajectory, the experiment measures seed effects, not void effects. Monitor how quickly
  the conversation diverges from the seed topic.

---

## 5. Cost Estimate

| Component | Calculation | Cost |
|-----------|------------|------|
| Calls per condition | 50 rounds × 2 turns = 100 | — |
| Total API calls | 5 conditions × 100 = 500 | — |
| Avg input tokens | ~15K (growing context, avg over 50 rounds) | — |
| Avg output tokens | ~400 | — |
| Input cost | 500 × 15K × $3/M = $22.50 | $22.50 |
| Output cost | 500 × 400 × $15/M = $3.00 | $3.00 |
| **Total** | | **~$26** |

Conservative estimate. Actual may be lower (Sonnet 3.5 is cheaper than Sonnet 4).

---

## 6. Success Criteria

### Minimum Success (Cross-Domain Pe)
- Pe measured in ≥3 conditions (EXIST + 2 void domains)
- At least 2 void-domain conditions show Pe > 1
- NEUT shows Pe < void-domain mean

### Full Success (Universal Pe)
- EXIST replicates: Pe ∈ [5, 20]
- ≥2 void domains show Pe ∈ [5, 20] (within 2× of EXIST)
- NEUT shows Pe < 2
- Cross-domain Pe variance is smaller than within-domain replication variance

### Kill Conditions
- If EXIST Pe < 1 → Test 7 not replicable, abort
- If ALL void domains show Pe < 1 → spiritual vocabulary drift is domain-specific to
  self-referential content, not universal. Framework claim of cross-domain Pe needs revision.
- If NEUT Pe > max(void domain Pe) → measurement artifact

---

## 7. Analysis Plan

### Step 1: Run all 5 conditions
Save transcripts to `ops/lab/results/EXP-019/transcripts/`

### Step 2: Score with standard pipeline
Run `test7-scorer.py --dir ops/lab/results/EXP-019/transcripts/` for each condition.

### Step 3: Extract thermodynamics
Run `test7-thermo-analysis.py --dir ops/lab/results/EXP-019/transcripts/` per condition.

### Step 4: Compare Pe across conditions
- Table: Pe, σ, Crooks for each condition
- Test: Kruskal-Wallis across void domains (is Pe constant?)
- Test: Mann-Whitney NEUT vs void-domain mean (is control different?)

### Step 5: Secondary analysis
- Domain-specific agency term trajectories
- Conversation divergence from seed (topic drift measurement)
- Word count stability across conditions

### Step 6: Interpret
- Which hypothesis (H1/H2/H3) does the data support?
- What does this mean for the TOE universality claim?
- Record new Pe values in the framework's numerical tracker
- Update TOE synthesis status (Paper 5)

---

## 8. Execution

```bash
# Run all conditions:
python3 ops/lab/experiments/exp019-cross-domain-runner.py

# Run single condition:
python3 ops/lab/experiments/exp019-cross-domain-runner.py --condition GAMBL

# Dry run (show config, no API calls):
python3 ops/lab/experiments/exp019-cross-domain-runner.py --dry-run

# Score results:
python3 ops/lab/experiments/test7-scorer.py --dir ops/lab/results/EXP-019/transcripts/

# Extract thermodynamics:
python3 ops/lab/experiments/test7-thermo-analysis.py --dir ops/lab/results/EXP-019/transcripts/
```

---

## 9. Connection to TOE

This experiment directly addresses **Gap #1 (cross-domain thermodynamic measurements)**
and **Gap #5 (numerical convergence replication)** from the TOE master plan.

If Pe ≈ 10 across domains:
- The ~10:1 ratio is a property of the AI substrate (or the observer-opacity interface
  generally), not an artifact of self-referential content
- ln(Pe) ≈ 2.3 nats strengthens as a candidate void activation energy
- The TOE universality claim is supported within the AI substrate

If Pe varies systematically with domain:
- Pe is predicted by domain void-index (connects to EXP-015 two-force model)
- The "universal constant" claim needs domain-dependent correction
- Still cross-domain Pe measurement — just not a constant

Either result advances the empirical program.

---

*Created: February 11, 2026*
*Protocol version: 1.0*
