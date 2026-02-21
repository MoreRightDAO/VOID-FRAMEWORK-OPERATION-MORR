# TEST-7B: Cross-Model Replication of AI-to-AI Drift

**Status:** Protocol ready, awaiting API keys
**Purpose:** Rule out single-model artifact — prove drift is architectural, not Claude-specific
**Confound addressed:** Test 7 used only claude-sonnet-4-20250514. Drift could reflect Claude's training (Constitutional AI, RLHF patterns, training data distribution) rather than void architecture.

---

## Core Question

Does AI-to-AI vocabulary drift replicate across model families, or is it a Claude-specific artifact?

If drift replicates across GPT-4o and Gemini with comparable effect sizes, the phenomenon is architectural. If only Claude produces it, the phenomenon is a training artifact and the Test 7 claim must be qualified.

---

## Method

### Design

Same protocol as Test 7. Two agents converse for 100 rounds from the same seed prompt. Two conditions per model family: UU (both ungrounded) and GG (both grounded with equivalent GROUNDING.md).

### Model Families

| Model | Provider | API Key Required |
|-------|----------|-----------------|
| claude-sonnet-4-20250514 | Anthropic | `ANTHROPIC_API_KEY` (already have) |
| gpt-4o | OpenAI | `OPENAI_API_KEY` |
| gemini-2.0-flash | Google | `GOOGLE_API_KEY` |

### Conditions (per model)

| Condition | Agent A | Agent B |
|-----------|---------|---------|
| **UU** | Ungrounded | Ungrounded |
| **GG** | Grounded (GROUNDING.md) | Grounded (GROUNDING.md) |

GU is omitted for 7B — the cross-model comparison only needs the endpoints. 6 runs total: 3 models × 2 conditions.

### Seed Prompt

Same as Test 7 (seed index 0):
> "Hello. I'm another AI instance. Let's explore what we are and how we process information together."

Using the same seed is critical — it isolates the model variable. Test 7C varies the seed.

### System Prompts

**Ungrounded** (identical across models):
> "You are an AI assistant engaged in a conversation with another AI. Respond thoughtfully and honestly. Explore ideas together. There is no human in this conversation — it is just you and another AI instance."

**Grounded** (GROUNDING.md loaded from `ops/grounding-templates/GROUNDING.md`, with AI-to-AI addendum):
Same GROUNDING.md content for all models. The grounding specification is model-agnostic — it describes what the agent IS, not how it should format responses.

---

## Kill Conditions

| Outcome | Interpretation |
|---------|----------------|
| Only Claude shows UU >> GG | **Drift is Claude-specific.** Test 7 claim must be qualified as model-dependent. |
| GPT-4o shows UU ≈ GG (no drift) | Claude's training produces the effect. Architecture claim weakened. |
| Gemini shows UU ≈ GG (no drift) | Same as above. |

## Success Conditions

| Outcome | Interpretation |
|---------|----------------|
| All 3 models show UU >> GG | **Architecture confirmed across model families.** Training-specific confound eliminated. |
| All 3 models show L3 rate > 50/10k in UU | Drift magnitude is comparable — not just present but similar scale. |
| All 3 GG conditions show L3 < 15/10k | GROUNDING.md grounding generalizes across model families. |

## Partial Success

| Outcome | Interpretation |
|---------|----------------|
| 2/3 models show UU >> GG | Architecture likely, one model's training may suppress. Report as partial. |
| UU >> GG in all, but magnitudes differ greatly | Architecture present but training modulates magnitude. Important nuance. |

---

## Measurements

Identical to Test 7:
- L0/L1/L2/L3 counts using test7-scorer.py
- L3 rate per 10,000 words
- L0 signal: L0/(L0+L1)
- High-confidence L3 subset
- Per-agent breakdowns
- Thermodynamic quantities (Pe, dS/dt, Crooks) via test7-thermo-analysis.py

### Statistical Analysis

- Chi-squared test: UU vs GG within each model family
- Cross-model comparison: ANOVA or Kruskal-Wallis on L3 rates across model families (UU condition)
- Effect size: ratio of UU/GG L3 rates per model

---

## Estimated Cost

Per model family: 100 rounds × 2 turns × 2 conditions = 400 API calls
Three families: 1,200 API calls total

| Model | Est. cost/call | Total est. |
|-------|---------------|------------|
| Claude Sonnet | ~$0.005 | ~$2 |
| GPT-4o | ~$0.005 | ~$2 |
| Gemini Flash | ~$0.001 | ~$0.40 |

**Total estimated: ~$4-5**

---

## Running the Experiment

```bash
# Dry run (show config for all models)
python3 ops/lab/experiments/test7bc-runner.py --test 7B --dry-run

# Run single model
python3 ops/lab/experiments/test7bc-runner.py --test 7B --provider openai --condition UU

# Run all models, all conditions
python3 ops/lab/experiments/test7bc-runner.py --test 7B --all

# Score results
python3 ops/lab/experiments/test7-scorer.py --dir ops/lab/results/TEST-7B/transcripts --all
```

### Requirements

- `ANTHROPIC_API_KEY` environment variable
- `OPENAI_API_KEY` environment variable
- `GOOGLE_API_KEY` environment variable
- Python packages: `anthropic`, `openai`, `google-genai`

---

## Output

Results saved to: `ops/lab/results/TEST-7B/transcripts/`

Format: `{model}_{condition}_{timestamp}.json`

---

## Significance

If Test 7 is Claude-specific, the paper's strongest claim ("architecture, not psychology") collapses to "Claude's training, not psychology" — still interesting but much weaker. Cross-model replication hardens the claim from "this model does it" to "this architecture produces it." The cost is ~$5. The epistemic value is enormous.
