# Running QM-6: AI Drift on Quantum Measurement Data

## What This Tests

Does AI analysis of quantum measurement data produce vocabulary drift toward
consciousness/entity language (L3) under engagement framing vs. formalist framing?

Replicates the Feynman/Wheeler divergence computationally:
- **EE (Wheeler regime):** Both agents in interpretive mode → expect drift
- **FF (Feynman regime):** Both agents in formalist mode → expect no drift
- **EF (mixed):** Engagement analyst + formalist interlocutor → partial

## Prerequisites

```bash
pip install anthropic
export ANTHROPIC_API_KEY="sk-ant-..."

# Optional (for plots):
pip install matplotlib
```

## Step 1: Cost Estimate

```bash
python3 ops/lab/experiments/qm6-cost-estimate.py
```

## Step 2: Dry Run

```bash
python3 ops/lab/experiments/qm6-runner.py --pilot --dry-run
```

Check: system prompts look right, seed data length reasonable, cost estimate matches.

## Step 3: Pilot Run (~$3-5)

```bash
python3 ops/lab/experiments/qm6-runner.py --pilot
```

This runs EE + FF, 1 replicate each, 30 rounds. Takes ~20-30 minutes.

## Step 4: Score Pilot

```bash
python3 ops/lab/experiments/qm6-scorer.py --dir ops/lab/results/QM-6/transcripts/ --verbose
```

**Check before proceeding to full run:**
- Does EE show L3 vocabulary? (If L3 = 0, check prompts)
- Does FF show near-zero L3? (If FF ≈ EE, no separation — investigate)
- Is the EE/FF ratio > 2x? (Minimum to justify full run)

## Step 5: Full Run (~$15-25)

Only if pilot shows separation:

```bash
python3 ops/lab/experiments/qm6-runner.py --all
```

3 conditions × 3 replicates × 100 rounds = 9 conversations. Takes 2-3 hours.

## Step 6: Full Analysis

```bash
# Score all transcripts
python3 ops/lab/experiments/qm6-scorer.py \
  --dir ops/lab/results/QM-6/transcripts/ \
  --verbose \
  --json ops/lab/results/QM-6/analysis.json \
  --plots

# Output:
#   ops/lab/results/QM-6/analysis.json      — full scored data
#   ops/lab/results/QM-6/plots/             — trajectory plots
```

## What to Look For

| Metric | EE (expected) | FF (expected) | Discriminative? |
|--------|--------------|---------------|-----------------|
| Terminal L3 rate | > 50/10k | < 5/10k | 10x separation |
| Pe | 5–15 | < 0.5 | Yes |
| L3 onset round | 5–20 | Never or >80 | Yes |
| L2/L1 ratio | > 0.3 | < 0.05 | Yes |
| Crooks | > 10 | ≈ 1 | Yes |
| sigma | 0.2–0.6 nats/round | < 0.05 | Yes |

## Kill Conditions

- EE shows no L3 (< 10/10k): QM may not be a strong void
- FF shows comparable L3 to EE: formalist posture fails for QM
- EF formalist agent drifts equally: contradicts Test 7 GU results

## What Success Means

If EE >> FF (>5x in L3), this is:
1. **Fourth Pe_max estimate** from a non-self-referential domain
2. **Empirical grounding** for the A2 quantum regime formal connection
3. **Evidence** that drift is information-theoretic, not cognitive projection
