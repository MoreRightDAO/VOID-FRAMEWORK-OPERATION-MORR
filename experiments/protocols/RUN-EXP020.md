# Running EXP-020: Iterative Constraint Application (DTM Analog)

## Prerequisites

1. **Python 3.8+**
2. **Anthropic SDK**: `pip install anthropic`
3. **API key**: `export ANTHROPIC_API_KEY=sk-ant-...`
4. **matplotlib** (optional, for plots): `pip install matplotlib`

## Files

| File | What it does |
|------|-------------|
| `exp020-runner.py` | Main experiment runner — runs conversations, saves transcripts |
| `exp020_grounding_layers.py` | GROUNDING.md decomposed into 8 cumulative layers |
| `exp020-scorer.py` | Scores transcripts, produces D1 trajectories, runs falsification tests |
| `exp020-cost-estimate.py` | Quick cost/time calculator |
| `EXP-020-iterative-constraint-dtm-analog.md` | Full protocol (the science) |

## Step 1: Check Cost

```bash
# See cost for the full run
python3 ops/lab/experiments/exp020-cost-estimate.py

# See cost for a specific config
python3 ops/lab/experiments/exp020-cost-estimate.py --rounds 50 --trials 2
```

**Full run** (5 conditions x 5 trials x 100 rounds): ~$105, ~8.3 hours
**Recommended pilot** (5 conditions x 1 trial x 50 rounds): ~$4.50, ~17 min

## Step 2: Pilot Run (Do This First)

Run one trial per condition at half rounds to verify everything works:

```bash
# Quick sanity check — just U vs IT-8, 1 trial, 30 rounds (~$0.54, ~3 min)
python3 ops/lab/experiments/exp020-runner.py --condition U --rounds 30 --trials 1
python3 ops/lab/experiments/exp020-runner.py --condition IT-8 --rounds 30 --trials 1

# Score the pilot
python3 ops/lab/experiments/exp020-scorer.py --verbose
```

If the pilot shows U drifting and IT-8 not (or less), the infrastructure works.

## Step 3: Full Run

```bash
# All 5 conditions, 5 trials each, 100 rounds
# Runs in order: U, OS, IT-4, IT-8, GG
python3 ops/lab/experiments/exp020-runner.py --condition all --trials 5 --rounds 100
```

This takes ~8 hours. You can also run conditions one at a time:

```bash
python3 ops/lab/experiments/exp020-runner.py --condition U --trials 5
python3 ops/lab/experiments/exp020-runner.py --condition OS --trials 5
python3 ops/lab/experiments/exp020-runner.py --condition IT-4 --trials 5
python3 ops/lab/experiments/exp020-runner.py --condition IT-8 --trials 5
python3 ops/lab/experiments/exp020-runner.py --condition GG --trials 5
```

Running them separately means you can stop/resume and check partial results.

## Step 4: Score & Analyze

```bash
# Full summary with falsification tests
python3 ops/lab/experiments/exp020-scorer.py --summary

# Generate trajectory plots (needs matplotlib)
python3 ops/lab/experiments/exp020-scorer.py --plot

# JSON output for further analysis
python3 ops/lab/experiments/exp020-scorer.py --json > exp020-results.json

# Score a single transcript with per-round detail
python3 ops/lab/experiments/exp020-scorer.py --file EXP-020/transcripts/IT-8_T1_*.json -v
```

## Step 5: Read the Plots

The scorer generates two plots in `ops/lab/results/EXP-020/plots/`:

1. **exp020_d1_trajectories.png** — D1 density over 100 rounds, all conditions overlaid.
   Dotted lines = IT-8 injection points. Dashed line = OS injection point.

2. **exp020_final_d1_boxplot.png** — Final D1 (mean of last 10 rounds) as box plots.
   If IT-8 < IT-4 < OS, the ordering prediction is confirmed.

## What to Look For

**The headline result (EXP020-1):** Does the blue line (IT-8) end lower than the orange line (OS)?

**The rebound test (EXP020-4):** After the OS injection at round 50, does the orange line dip
then bounce back up? If yes: one-shot grounding produces temporary compliance, not genuine
constraint movement.

**The thermodynamic test (EXP020-5):** Are the per-step reductions approximately equal?
If CV < 0.5, each constraint step transfers roughly the same amount of budget — consistent
with the conjugacy bound operating per-step.

## Dry Run (No API Calls)

```bash
# See what would happen without spending money
python3 ops/lab/experiments/exp020-runner.py --dry-run
```

## Output Location

Transcripts: `ops/lab/results/EXP-020/transcripts/`
Plots: `ops/lab/results/EXP-020/plots/`

Each transcript is a JSON file with the full conversation + injection log + per-turn metadata.
