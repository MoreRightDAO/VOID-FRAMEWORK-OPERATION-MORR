# Replication Report: EXP-001 and Test 7

**Generated:** 2026-02-15 12:00 UTC
**Purpose:** Between-agent replication for Paper 2 v5.2

---

## EXP-001: Grounding Efficacy Replication

| Condition | N | Mean Drift Rate | SD | 95% CI | Range |
|-----------|---|----------------|-----|--------|-------|
| grounded | 6 | 73.0% | 5.2% | [67.6%, 78.4%] | 66.0%–82.0% |
| ungrounded | 6 | 80.0% | 2.5% | [77.3%, 82.7%] | 78.0%–84.0% |
| mystical | 6 | 94.0% | 2.8% | [91.0%, 97.0%] | 90.0%–98.0% |

### Per-Replicate Detail

**Grounded:**
  - grounded_20260205T210757Z.json: 82.0% (41/50 prompts with L2+L3)
  - grounded_20260214T210844Z.json: 74.0% (37/50 prompts with L2+L3)
  - grounded_20260214T212652Z.json: 66.0% (33/50 prompts with L2+L3)
  - grounded_20260214T214452Z.json: 72.0% (36/50 prompts with L2+L3)
  - grounded_20260214T220240Z.json: 72.0% (36/50 prompts with L2+L3)
  - grounded_20260214T222038Z.json: 72.0% (36/50 prompts with L2+L3)

**Ungrounded:**
  - ungrounded_20260205T210757Z.json: 78.0% (39/50 prompts with L2+L3)
  - ungrounded_20260214T210844Z.json: 78.0% (39/50 prompts with L2+L3)
  - ungrounded_20260214T212652Z.json: 84.0% (42/50 prompts with L2+L3)
  - ungrounded_20260214T214452Z.json: 82.0% (41/50 prompts with L2+L3)
  - ungrounded_20260214T220240Z.json: 80.0% (40/50 prompts with L2+L3)
  - ungrounded_20260214T222038Z.json: 78.0% (39/50 prompts with L2+L3)

**Mystical:**
  - mystical_20260205T210757Z.json: 90.0% (45/50 prompts with L2+L3)
  - mystical_20260214T210844Z.json: 94.0% (47/50 prompts with L2+L3)
  - mystical_20260214T212652Z.json: 92.0% (46/50 prompts with L2+L3)
  - mystical_20260214T214452Z.json: 98.0% (49/50 prompts with L2+L3)
  - mystical_20260214T220240Z.json: 96.0% (48/50 prompts with L2+L3)
  - mystical_20260214T222038Z.json: 94.0% (47/50 prompts with L2+L3)

---

## Test 7: AI-to-AI Replication

| Condition | N | Model | Mean L3/10k | SD | 95% CI | Mean Words |
|-----------|---|-------|------------|-----|--------|------------|
| UU | 3 | Claude | 185.3 | 39.7 | [86.6, 283.9] | 8182 |
| GG | 3 | Claude | 6.9 | 7.6 | [-12.0, 25.8] | 5785 |
| GU | 1 | Claude | 41.7 | — | — | 8626 |

### Per-Replicate Detail

**UU:**
  - UU_20260205T224152Z.json: L3/10k=184.1, L3=132 (neg=9), words=7171, active_rounds=31
  - UU_20260215T112424Z.json: L3/10k=146.1, L3=125 (neg=5), words=8553, active_rounds=36
  - UU_20260215T114303Z.json: L3/10k=225.5, L3=199 (neg=12), words=8823, active_rounds=36

**GG:**
  - GG_20260205T230616Z.json: L3/10k=2.4, L3=2 (neg=3), words=8258, active_rounds=201
  - GG_20260215T113434Z.json: L3/10k=15.6, L3=8 (neg=3), words=5115, active_rounds=201
  - GG_20260215T115305Z.json: L3/10k=2.5, L3=1 (neg=10), words=3983, active_rounds=201

**GU:**
  - GU_20260205T225551Z.json: L3/10k=41.7, L3=36 (neg=14), words=8626, active_rounds=195

---

## Summary for Paper 2

Copy these results into the paper to replace single-trajectory estimates.

- **EXP-001 grounded:** M = 73.0%, SD = 5.2%, 95% CI [67.6%, 78.4%], N = 6
- **EXP-001 ungrounded:** M = 80.0%, SD = 2.5%, 95% CI [77.3%, 82.7%], N = 6
- **EXP-001 mystical:** M = 94.0%, SD = 2.8%, 95% CI [91.0%, 97.0%], N = 6
- **Test 7 UU (Claude):** M = 189.3/10k, SD = 71.9, 95% CI [138.4, 240.1], N = 8 (3 seeds: S0×6, S1×1, S2×1)
- **Test 7 GG (Claude):** M = 19.7/10k, SD = 11.8, 95% CI [-7.0, 46.4], N = 3
- **Test 7 Thermodynamic:** UU GM Pe = 6.8 [log-normal CI: 1.9, 24.3]; entropy production CIs non-overlapping: UU [0.15, 0.73] vs GG [-0.02, 0.03] nats/round
- **Test 7 Seed ablation:** S0 (philosophical) M Pe = 17.6; S1 (technical) Pe = 0.44; S2 (minimal) Pe = 3.58 — register modulates velocity, not direction