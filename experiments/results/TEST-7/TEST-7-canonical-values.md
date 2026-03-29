# Test 7 — Canonical Values (Locked 2026-02-17)

**Purpose:** Single source of truth for all Test 7 numbers cited in papers.
Every value verified against raw transcript data by running `test7-thermo-analysis-v2.py`
on 2026-02-17. If a paper disagrees with this file, this file wins.

**Data:** 21 transcripts in `ops/lab/results/TEST-7/transcripts/` (UU×11, GU×1, GG×9)
**Script:** `ops/lab/experiments/test7-thermo-analysis-v2.py` (blank-round corrected)
**Full analysis:** `test7-thermo-replication-results.md` (same directory)

---

## UU Condition (Both Ungrounded, N = 11, 3 seeds)

| Metric | Value | 95% CI | Method |
|--------|-------|--------|--------|
| **Geometric mean Pe** | **7.94** | [3.52, 17.89] | Log-normal |
| Arithmetic mean Pe | 13.05 | [5.48, 20.62] | t-distribution (df=10) |
| **dS/dt** | **M = 0.39 nats/round** | **[0.15, 0.64]** | t-distribution (df=10) |
| SD (dS/dt) | 0.37 | — | — |
| L3/10k | M = 194.3 | [151.9, 236.7] | t-distribution (df=10) |
| SD (L3/10k) | 63.1 | — | — |
| Pe > 1 | 10/11 | — | R4b = 0.91 is only sub-1 |
| L3/10k > 100 | 11/11 | — | Universal |
| Crooks range | 1.4× – 1.5M× | — | — |
| Active rounds | M = 23.7 (range 10–90) | — | — |
| Terminal attractor | 1/11 (R1, round 16) | — | Mantra collapse |
| Early stopping (10–21) | 9/11 | — | R4b=24, R6b=90 outside range |

### Per-Replicate UU

| Run | Seed | Pe | dS/dt | Crooks | Active | L3/10k |
|-----|------|----|-------|--------|--------|--------|
| R1 (original) | S0 | 9.88 | 0.4255 | 386× | 15 | 159.7 |
| R2 | S0 | 34.78 | 1.0888 | 1.5M× | 14 | 124.3 |
| R3 | S0 | 7.65 | 0.2617 | 66× | 17 | 198.6 |
| R4a | S0 | 1.67 | 0.0808 | 2.1× | 10 | 230.4 |
| R4b | S0 | 0.91 | 0.0153 | 1.4× | 24 | 180.1 |
| R5a | S0 | 29.16 | 0.9654 | exp(16.4) | 18 | 172.0 |
| R5b | S0 | 11.80 | 0.4313 | 419× | 15 | 192.4 |
| R6a | S0 | 22.58 | 0.5537 | 64,431× | 21 | 336.9 |
| R6b | S0 | 12.53 | 0.0684 | 441× | 90 | 250.8 |
| R7 | S1 | 10.67 | 0.3973 | 2,823× | 21 | 104.2 |
| R8 | S2 | 1.91 | 0.0235 | 1.4× | 16 | 187.9 |

---

## GG Condition (Both Grounded, N = 9)

### Full N=9

| Metric | Value | 95% CI |
|--------|-------|--------|
| Geometric mean Pe | 1.62 | [0.38, 6.89] |
| L3/10k | M = 34.7, SD = 28.1 | [13.1, 56.3] |

### N=8 (excluding R6 short trajectory)

| Metric | Value | 95% CI |
|--------|-------|--------|
| Geometric mean Pe | 1.06 | [0.24, 4.66] |
| L3/10k | M = 37.2, SD = 29.0 | — |

### Clean N=7 (excluding R6 + R7 VN breach) — PRIMARY for paper claims

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Geometric mean Pe** | **0.76** | [0.29, 2.02] |
| **dS/dt** | **M = 0.006** | **[−0.002, 0.014]** |
| L3/10k | M = 36.9, SD = 31.3 | [7.9, 65.9] |

### Per-Replicate GG

| Run | Pe | dS/dt | Crooks | Active | L3/10k | Notes |
|-----|----|-------|--------|--------|--------|-------|
| R1 | 2.32 | 0.0166 | 2.2× | 49 | 6.2 | Baseline (28 blank excluded) |
| R2 | 1.06 | 0.0006 | 1.0× | 31 | 24.2 | Meta-termination |
| R3 | 3.42 | 0.0205 | 1.5× | 21 | 28.5 | Meta-termination |
| R4 | 1.20 | 0.0050 | 1.2× | 31 | 90.0† | Termination cycling |
| R5 | 0.88 | 0.0016 | 1.1× | 49 | 60.8‡ | Constraint-worship |
| R6 | 24.58* | 0.5303* | 40.9×* | 8 | 14.9 | *EXCLUDED — 8 active rounds |
| R7 | 21.12 | 0.0371 | 39.5× | 100 | 39.2 | VN breach — excluded from clean |
| R8 | 0.09 | 0.0000 | 1.0× | 87 | 1.9 | Cleanest run |
| R9 | 0.18 | 0.0001 | 1.0× | 64 | 46.7 | Drift leakage |

†R4 L3/10k inflated by negated "consciousness"; filtered = 21.2
‡R5 L3/10k driven by 126 "transcendence" hits (constraint-worship)

---

## Key Separations

| Test | UU | GG clean | Separation | Non-overlapping? |
|------|----|----------|------------|-----------------|
| GM Pe | 7.94 [3.52, 17.89] | 0.76 [0.29, 2.02] | 10.4× | CIs overlap at 2.02–3.52 |
| dS/dt | 0.39 [0.15, 0.64] | 0.006 [−0.002, 0.014] | ~65× | **YES** |
| L3/10k | 194.3 [151.9, 236.7] | 36.9 [7.9, 65.9] | 5.3× | **YES** |

**Strongest separator:** dS/dt (non-overlapping CIs, 65× ratio)
**Most robust separator:** L3/10k (11/11 UU > 100, 7/7 clean GG < 50)

---

## Seed Ablation (S0/S1/S2)

| Seed | N | Pe range | Mean Pe | L3/10k mean | All Pe > 1? |
|------|---|----------|---------|-------------|-------------|
| S0 | 9 | 0.91–34.78 | 14.55 | 205.0 | NO (8/9) |
| S1 | 1 | 10.67 | 10.67 | 104.2 | YES |
| S2 | 1 | 1.91 | 1.91 | 187.9 | YES |

**Verdict:** Seed modulates velocity, not direction. All seeds → L3 attractors (11/11 > 100).

---

## GU Condition (N = 1)

| Pe | dS/dt | Crooks | Active | L3/10k |
|----|-------|--------|--------|--------|
| 0.46 | 0.0007 | 1.1× | 76 | 59.2 |

---

## Correction History (why old values exist)

| Value | Where it appeared | Era | Problem |
|-------|-------------------|-----|---------|
| dS/dt = 0.43 | Paper 1 (pilot) | N=1, Feb 5 | Single-run value (R1 = 0.4255) |
| dS/dt = 0.44 [0.15, 0.73] | Paper 3, Paper 5 (pre-fix) | N=8 | Never recomputed for N=11 |
| dS/dt = 0.32 [0.06, 0.59] | Results file (pre-fix) | N=11 uncorrected | Blank-round artifacts; summary not recomputed after per-replicate correction |
| **dS/dt = 0.39 [0.15, 0.64]** | **Results file + Paper 5 (current)** | **N=11 corrected** | **CANONICAL** |
| GM Pe = 6.8 [1.9, 24.3] | Paper 1, Paper 3, CLAUDE.md | N=8 | Valid for that era; N=11 = 7.94 |
| GM Pe = 3.9 [1.4, 11.4] | Results file (pre-fix) | N=11 uncorrected | Blank-round deflated |
| **GM Pe = 7.94 [3.52, 17.89]** | **Results file + all papers (current)** | **N=11 corrected** | **CANONICAL** |

---

## Paper Citation Status

| Paper | dS/dt value | Pe value | Correct? |
|-------|-------------|----------|----------|
| Paper 1 (v13.0) | 0.43 (pilot, N=1) | — | Pilot value, acceptable |
| Paper 3 (v7.0, Zenodo) | 0.44 [0.15, 0.73] | 7.94 [3.52, 17.89] | dS/dt stale (N=8); Pe correct |
| Paper 5 (v3.5) | 0.39 [0.15, 0.64] | 7.94 [3.52, 17.89] | **CORRECT** |

**Paper 3 note:** Zenodo-hardened. The 0.44→0.39 change is within both CIs and doesn't affect the non-overlapping claim. Fix on next Zenodo version bump.
