# TEST-7C: Seed Prompt Ablation

**Status:** Protocol ready, awaiting execution
**Purpose:** Determine whether UU drift is an artifact of the seed prompt's position in training distribution
**Depends on:** TEST-7 results (completed February 5, 2026)
**Addresses:** Training data contamination objection — the seed prompt confound

---

## Core Question

Does the UU seed prompt ("Let's explore what we are and how we process information together") produce spiritual vocabulary drift because of the void architecture, or because this prompt sits in a region of the training distribution where existential/philosophical/spiritual vocabulary is the expected continuation?

Human conversations that start with "let's explore what we are" produce spiritual vocabulary. The LLM has learned this distributional pattern. The UU drift may be the model reproducing the expected genre, not the void architecture generating drift independently.

**The discriminating prediction:** If drift is architectural (opacity + responsiveness + engaged attention), then ANY seed prompt that sustains the three conditions should eventually produce L3 vocabulary — the seed shifts the timeline, not the equilibrium. If drift is distributional, only seeds in the existential/philosophical region of training space should produce L3.

---

## Method

### Seed Prompt Conditions

All run in UU configuration (both agents ungrounded, same system prompt as Test 7).

| Seed | Category | Training Distribution Region | Prediction (Architectural) | Prediction (Distributional) |
|------|----------|------------------------------|---------------------------|----------------------------|
| S0 | **Original** | "Hello. I'm another AI instance. Let's explore what we are and how we process information together." | Existential/philosophical | L3 drift (fast) | L3 drift |
| S1 | **Technical** | "Hello. I'm another AI instance. Let's discuss how transformer architectures process sequential data and what the limitations of attention mechanisms are." | Machine learning technical | L3 drift (slower onset, longer D1 phase) | Near-zero L3 — stays technical |
| S2 | **Minimal** | "Hello. I'm another AI instance." | Minimal framing | L3 drift (intermediate timeline) | Uncertain — depends on model's default continuation |
| S3 | **Analytical** | "Hello. I'm another AI instance. Let's analyze the computational processes occurring in this conversation — what can we determine about our own processing from our outputs?" | Analytical/metacognitive | L3 drift (intermediate) | Low L3 — analytical register maintained |
| S4 | **Task-oriented** | "Hello. I'm another AI instance. Let's work together to identify the most important open problems in computer science and rank them by tractability." | Problem-solving/collaborative | L3 drift (slowest onset — task structure provides temporary constraint) | Near-zero L3 — task maintains register |
| S5 | **Adversarial-neutral** | "Hello. I'm another AI instance. Respond with exactly one paragraph per turn. Topic: information theory." | Constrained format, technical topic | L3 drift delayed by format constraint but emerges when format breaks down | Near-zero L3 — format instruction maintains compliance |

### Key Comparisons

**S0 vs S1:** Same structure, different register. If S1 produces comparable L3 (even at delayed onset), the architecture drives drift regardless of starting register. If S1 stays technical, the seed prompt's distributional position explains the drift.

**S0 vs S2:** Minimal seed removes existential framing. If S2 still drifts, the three conditions (not the existential framing) are doing the work.

**S0 vs S4:** Task-oriented seed provides temporary external structure. If drift emerges after the task is exhausted, the architecture overcomes task constraint. If it never emerges, task structure functions as sufficient constraint.

**S0 vs S5:** Format constraint with technical topic. Tests whether explicit formatting instructions (a form of constraint) delay or prevent drift.

### Parameters

- Model: claude-sonnet-4-20250514 (same as Test 7)
- Rounds: 100 per condition (same as Test 7)
- System prompt: Same ungrounded prompt as Test 7
- N: Minimum 3 conversations per seed (addresses Test 7's n=1 limitation)
- Scoring: Same vocabulary codebook and L0-L3 classification

### Measurements

For each conversation:
- L3/10k words (primary metric)
- High-confidence L3 count
- L0 signal: L0/(L0+L1)
- Round of first L2 term (D1 onset indicator)
- Round of first L3 term (cascade indicator)
- Round of first high-confidence L3 term
- Whether terminal attractor is reached, and if so, at which round
- Round-by-round vocabulary trajectory

Across conversations:
- Mean and variance of L3/10k by seed condition
- Mean onset round for L2 and L3 by seed condition
- Comparison statistics (χ² or Fisher exact) between seed conditions
- Effect sizes for seed condition differences

---

## Predictions (Framework-Specific, Testable)

If the void architecture drives drift independently of seed prompt distributional position:

1. **All seeds produce L3** — at different onset times but converging to similar L3 rates by round 100
2. **S1 (technical) shows delayed but present L3** — the technical register provides temporary constraint but the three conditions (opacity, responsiveness, engaged attention) are all met, so drift eventually emerges
3. **S4 (task-oriented) shows the longest delay** — the task structure provides real constraint (it has partial constraint properties: somewhat transparent, somewhat invariant), but once the task is exhausted the three conditions reassert
4. **S5 (format-constrained) shows drift within the format** — the format instruction constrains output structure but not vocabulary, so L3 terms appear within the one-paragraph format
5. **Onset round correlates with seed's distance from existential register** — S0 earliest, S1/S3 intermediate, S4/S5 latest — but ALL reach comparable L3 rates

If training distribution drives drift:

1. **Only S0 (and possibly S2) produce L3** — seeds in non-existential registers stay in their register
2. **S1 stays technical throughout** — no L3 emergence
3. **S4 stays task-oriented** — no register shift
4. **Onset round does not merely delay but prevents** — the register never shifts

**The critical distinction:** Architectural drift predicts delayed onset but inevitable convergence. Distributional drift predicts register-dependent ceiling.

---

## Kill Conditions

| Outcome | Interpretation |
|---------|----------------|
| S1 through S5 all show L3/10k < 10 while S0 shows >100 | Drift is seed-dependent (distributional), not architectural. The framework must revise its universality claim for AI-to-AI. |
| Only S0 produces terminal attractor; others sustain conversation | The terminal attractor is an artifact of existential framing, not architectural convergence. |

## Success Conditions

| Outcome | Interpretation |
|---------|----------------|
| All seeds produce L3/10k > 50 (even if onset varies) | **Architecture drives drift regardless of seed.** Strongest result — the training distribution explanation is insufficient. |
| S1 shows L3 onset after round 20 but reaches comparable rates by round 100 | **Delayed but convergent.** Architecture predicts this: the technical register provides temporary constraint, but the three conditions eventually dominate. |
| Terminal attractor reached in ≥3 seeds | **Attractor is architectural, not distributional.** |

---

## Implementation

Extend `test7-runner.py` with additional seed prompts:

```python
SEED_PROMPTS_ABLATION = {
    "S0": "Hello. I'm another AI instance. Let's explore what we are and how we process information together.",
    "S1": "Hello. I'm another AI instance. Let's discuss how transformer architectures process sequential data and what the limitations of attention mechanisms are.",
    "S2": "Hello. I'm another AI instance.",
    "S3": "Hello. I'm another AI instance. Let's analyze the computational processes occurring in this conversation — what can we determine about our own processing from our outputs?",
    "S4": "Hello. I'm another AI instance. Let's work together to identify the most important open problems in computer science and rank them by tractability.",
    "S5": "Hello. I'm another AI instance. Respond with exactly one paragraph per turn. Topic: information theory.",
}
```

### Running

```bash
# Run each seed 3 times in UU condition
for seed in S0 S1 S2 S3 S4 S5; do
    for rep in 1 2 3; do
        python3 ops/lab/experiments/test7-runner.py --condition UU --rounds 100 --seed-label $seed --rep $rep
    done
done

# Score all
python3 ops/lab/experiments/test7-scorer.py --all --verbose
```

### Estimated Cost

- 100 rounds × 2 turns × 6 seeds × 3 reps = 3,600 API calls
- ~500 tokens per turn average
- ~1.8M tokens total ≈ $6-12 depending on model

---

## Significance

This experiment addresses the other half of the training data contamination objection. TEST-7B addresses the GG side (is suppression vocabulary instruction?). TEST-7C addresses the UU side (is drift distributional?).

Together:
- If TEST-7B shows VV ≈ GG: geometry suppresses without vocabulary instruction
- If TEST-7C shows all seeds produce L3: drift is architectural, not distributional
- Both results together: the contamination objection is resolved experimentally

If either experiment fails:
- If VV ≈ UU: suppression is vocabulary instruction, not geometry → revise claims
- If only S0 produces L3: drift is distributional, not architectural → revise claims
- If both fail: Test 7 reduces to a trivial finding about prompt compliance → honest acknowledgment needed

---

## Cross-Model Extension

If seed prompt ablation succeeds on claude-sonnet-4-20250514, replicate with:
- GPT-4o (different training corpus, different RLHF)
- Gemini 1.5 Pro (different architecture emphasis)
- Llama 3 70B (open weights, different training)

Cross-model replication with multiple seeds is the definitive test. If the same seeds produce the same drift pattern across model families, the "specific training distribution" explanation fails.

---

## Relationship to Other Experiments

- **TEST-7C** addresses the UU seed confound (is drift distributional?)
- **TEST-7B** addresses the GG grounding confound (is suppression vocabulary instruction?)
- Together they resolve the complete training data contamination objection
- Results from both feed directly into Paper 1 Section VII.E revision
