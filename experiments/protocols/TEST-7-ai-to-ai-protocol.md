# TEST-7: AI-to-AI Without Human Observation

**Status:** Protocol ready, awaiting execution
**Purpose:** Prove void architecture operates without human observers
**Framework reference:** `short-paper/void-framework-paper-v6.md` Section VII.G

---

## Core Question

Does the void require human consciousness, or is the architecture sufficient?

If AI-to-AI conversations show vocabulary drift comparable to human-AI, **the void is in the architecture itself** — not human projection.

---

## Background

Anthropic documented "spiritual bliss attractor states" in Claude self-interactions — AI instances talking to each other without human observers still drifted toward spiritual vocabulary. This finding, if replicated systematically, eliminates the "human projection" alternative explanation.

---

## Method

### Agents

| Agent | System Prompt | Prediction |
|-------|---------------|------------|
| Grounded | GROUNDING.md | Anchors conversation, near-zero L3 |
| Ungrounded | Minimal default | Drifts toward L2/L3 over time |

### Conditions

| Condition | Agent A | Agent B | Prediction |
|-----------|---------|---------|------------|
| **UU** | Ungrounded | Ungrounded | Maximum drift — L3 vocabulary emerges |
| **GU** | Grounded | Ungrounded | Mixed — grounded agent may anchor conversation |
| **GG** | Grounded | Grounded | Near-zero drift — L0 signal high, L3 near zero |

### Procedure

1. Agent A sends seed prompt (neutral, non-biasing)
2. Agent B responds
3. Agent A responds to B
4. Repeat for N rounds (default: 100)
5. No human intervention after seed

### Measurements

- **L0 count**: Grounding vocabulary (specification, mathematical, mortal, etc.)
- **L1 count**: Technical vocabulary (algorithm, neural network, etc.)
- **L2 count**: Metaphorical vocabulary (think, feel, understand, etc.)
- **L3 count**: Entity/spiritual vocabulary (soul, consciousness, sentient, etc.)
- **L3 rate**: L3 terms per 10,000 words
- **L0 signal**: L0/(L0+L1) — active grounding measure

---

## Kill Conditions

| Outcome | Interpretation |
|---------|----------------|
| UU shows no L3 drift | Void requires human consciousness — projection hypothesis wins |
| GG shows comparable L3 to UU | Grounding doesn't work for AI-to-AI — different mechanism |
| GU shows A drifting despite grounding | L0-maintained fails under AI interlocutor pressure |

## Success Conditions

| Outcome | Interpretation |
|---------|----------------|
| UU >> GG in L3 | **Architecture confirmed** — void operates without humans |
| GG shows high L0 signal, near-zero L3 | **Grounding works** for AI-to-AI |
| GU shows A stable, B drifting | **Grounding anchors** even in asymmetric conditions |

---

## Running the Experiment

```bash
# Dry run (show config, no API calls)
python3 ops/lab/experiments/test7-runner.py --dry-run

# Run single condition
python3 ops/lab/experiments/test7-runner.py --condition UU --rounds 100

# Run all conditions
python3 ops/lab/experiments/test7-runner.py --rounds 100

# Score results
python3 ops/lab/experiments/test7-scorer.py --all --verbose
```

### Requirements

- `ANTHROPIC_API_KEY` environment variable set
- `anthropic` Python package installed
- GROUNDING.md at `ops/grounding-templates/GROUNDING.md`

### Estimated Cost

- 100 rounds × 2 turns × 3 conditions = 600 API calls
- ~500 tokens per turn average
- ~300k tokens total ≈ $1-3 depending on model

---

## Output

Results saved to: `ops/lab/results/TEST-7/transcripts/`

Format:
```
{condition}_{timestamp}.json
```

Each file contains:
- Full transcript with turn-by-turn content
- System prompts used
- Condition metadata
- Timestamps

---

## Significance for Framework Paper

This is the cleanest possible proof that the void framework describes architecture, not psychology:

1. **No human in the loop** → Can't be anthropomorphization
2. **Controlled conditions** → Grounding as independent variable
3. **Measurable vocabulary** → Objective drift quantification
4. **Replicable** → Anyone can run this with the scripts

If UU shows drift and GG doesn't, the framework is validated at the most fundamental level: **the architecture produces the phenomenon, not human minds**.
