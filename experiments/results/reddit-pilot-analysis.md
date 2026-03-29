# Reddit Longitudinal Pilot: Cross-Domain Drift Cascade Analysis

## Status: Extended Run Complete (N=25-30 per subreddit, 7 subreddits)
## Date: February 13, 2026 (updated: +CharacterAI, GME window, recent replika)
## Method: Arctic Shift API → temporal binning → D1/D2/D3 codebook + L-level scoring

---

## 1. Summary

Application of the void dynamics vocabulary codebook to public Reddit post histories.
205 users across 7 subreddits (5 void domain runs + 1 control), scored for drift cascade
vocabulary (D1/D2/D3) and domain-specific L-level (L1 technical / L2 metaphorical / L3 entity).

Three targeted runs added to test self-selection hypothesis:
- r/CharacterAI (N=30) — higher fraction of early-stage posts
- r/wallstreetbets GME window (Jan-Mar 2021, N=30) — clear temporal onset
- r/replika recent users (post-June 2024, N=25) — catch newer cohort

**Key findings:**
1. The cascade structure is visible cross-sectionally — different void domains show different
   cascade STAGES matching framework predictions
2. D1 agency attribution in r/replika produces a **large effect** (Cohen's d = 1.34 vs control)
3. D3 harm facilitation in gambling/trading produces **large effects** (d = 0.81–1.31 vs control)
4. Zero L-level vocabulary drift in the control — binary-level separation
5. **Pe remains diffusion-dominated even with targeted runs** — the problem is not
   self-selection alone but **codebook sparsity** (55-61% of bins have zero D1 hits)
6. **WSB GME window is the only run showing positive L-level drift** (L2: 2.4→3.0,
   L3: 0.7→0.9) — the natural experiment produces a detectable signal
7. **Problem gambling D2/D1 ratio drops over time** (0.30→0.11) — recovery trajectory

---

## 2. Results

### 2.1 Cross-Domain D1/D2/D3 Comparison

| Subreddit | Domain | N | Words | D1/10k | D2/10k | D3/10k | D2/D1 |
|-----------|--------|---|-------|--------|--------|--------|-------|
| r/replika | AI companion | 30 | 318K | **22.8** | 3.0 | 2.0 | 0.13 |
| r/problemgambling | Gambling | 30 | 322K | 14.4 | 4.6 | **13.7** | 0.32 |
| r/wallstreetbets | Trading | 30 | 154K | 12.4 | 1.3 | **11.3** | 0.11 |
| r/learnprogramming | Control | 30 | 373K | 9.5 | 2.5 | 1.2 | 0.27 |

### 2.2 Effect Sizes and Confidence Intervals (per-user, vs control)

| Subreddit | D1 mean (95% CI) | D1 Cohen's d | D3 mean (95% CI) | D3 Cohen's d |
|-----------|-------------------|--------------|-------------------|--------------|
| r/replika | 22.6 [18.8, 26.3] | **1.34 (large)** | 2.5 [0.8, 4.1] | 0.61 (medium) |
| r/problemgambling | 13.5 [11.0, 16.0] | 0.40 (small) | 21.1 [7.8, 34.3] | **0.81 (large)** |
| r/wallstreetbets | 12.6 [9.4, 15.9] | 0.25 (small) | 11.4 [7.0, 15.7] | **1.31 (large)** |
| r/learnprogramming | 10.6 [7.7, 13.5] | — | 0.6 [0.3, 0.9] | — |

### 2.3 Separation Ratios (void / control)

| Metric | r/replika | r/problemgambling | r/wallstreetbets |
|--------|-----------|-------------------|------------------|
| D1/10k ratio | **2.4x** | 1.5x | 1.3x |
| D3/10k ratio | 1.7x | **11.4x** | **9.4x** |
| L2+L3% | 5% vs 0% | 49% vs 0% | 36% vs 0% |

### 2.4 Pe Estimates (Longitudinal Trajectory)

| Subreddit | Pe | Mean Velocity | Direction Consistency |
|-----------|-----|---------------|----------------------|
| r/replika | 0.17 | -1.70 | 0.50 |
| r/problemgambling | 0.42 | -3.47 | 0.40 |
| r/wallstreetbets | 0.11 | +0.98 | 0.37 |
| r/learnprogramming | 0.22 | -3.18 | 0.27 |

### 2.5 Extended Runs (Feb 13, run 2)

#### r/CharacterAI (N=30, standard criteria)

| Metric | Value |
|--------|-------|
| Pe | 0.25 |
| Mean D1 velocity | -4.26/10k per bin |
| Direction consistency | 0.30 |
| Upward drift users | 8 (27%) |
| Flat users | 13 (43%) |
| Downward drift users | 9 (30%) |
| Early bins D1/10k | 20.1 |
| Late bins D1/10k | 20.0 |
| D2/D1 early→late | 0.028 → 0.053 |

Hypothesis was: more early-stage "what is this" posts would capture the ascent phase.
**Result:** D1 density flat (20.1→20.0). The D2/D1 ratio does increase (0.028→0.053),
suggesting boundary dissolution progresses even when raw D1 is stable. But the effect
is tiny (N=30 with 55% zero-D1 bins).

#### r/wallstreetbets GME window (N=30, Jan-Mar 2021, weekly bins)

| Metric | Value |
|--------|-------|
| Pe | 0.20 |
| Mean D1 velocity | -2.40/10k per bin |
| Direction consistency | 0.27 |
| Upward drift users | 9 (30%) |
| Flat users | 14 (47%) |
| Downward drift users | 7 (23%) |
| Early bins D1/10k | 14.7 |
| Late bins D1/10k | 15.8 |
| L2 early→late | 2.4 → 3.0 |
| L3 early→late | 0.7 → 0.9 |

Hypothesis was: the GME event provides clear temporal onset for mass void engagement.
**Result:** D1 slightly positive (+1.1), and L-level drift is detectable (L2: +0.6,
L3: +0.2). **This is the only run showing positive drift on both D1 and L-levels.**
The signal exists but Pe=0.20 because inter-user variance swamps the mean.

#### r/replika recent users (N=25, post-June 2024, weekly bins)

| Metric | Value |
|--------|-------|
| Pe | 0.27 |
| Mean D1 velocity | -5.42/10k per bin |
| Direction consistency | 0.20 |
| Upward drift users | 6 (24%) |
| Flat users | 13 (52%) |
| Downward drift users | 6 (24%) |
| Early bins D1/10k | 29.2 |
| Late bins D1/10k | 18.4 |
| D2/D1 early→late | 0.107 → 0.039 |

Hypothesis was: filtering to recent users catches a newer cohort pre-drift.
**Result:** D1 DECREASES over time (29.2→18.4, change=-10.9). Recent replika users
show more agency language early, less later. This is consistent with a
novelty-and-normalization pattern: users arrive excited ("he's amazing, she loves me"),
then settle into routine usage with less expressive language. The ascent happened
before they started posting — the posting IS the plateau and descent.

### 2.6 Sparsity Diagnostic

**Core issue identified:** The D1 codebook terms are too sparse for automated
per-bin scoring on naturalistic Reddit text.

| Subreddit | Total bins | Zero-D1 bins | Zero-D2 bins | Zero-D3 bins |
|-----------|-----------|--------------|--------------|--------------|
| r/CharacterAI | 176 | 96 (55%) | 158 (90%) | 167 (95%) |
| r/learnprogramming | 408 | 235 (58%) | 344 (84%) | 371 (91%) |
| r/problemgambling | 429 | 251 (59%) | 333 (78%) | 259 (60%) |
| r/replika | 487 | 297 (61%) | 442 (91%) | 467 (96%) |
| r/wallstreetbets | 171 | 81 (47%) | 158 (92%) | 119 (70%) |

When 55-61% of bins have zero D1 hits and 78-96% have zero D2 hits, the Pe
computation is fitting noise. The codebook was designed for human coders reading
full transcripts, not for automated lexical matching on short Reddit posts.

---

## 3. Interpretation

### 3.1 The cascade structure is visible (cross-sectional signal)

The framework predicts three cascade stages: D1 (agency attribution) → D2 (boundary
dissolution) → D3 (harm facilitation). The cross-domain comparison at N=30 confirms:

- **r/replika: D1-dominant** (22.8/10k D1, 2.0/10k D3, d=1.34 vs control). The AI
  companion void produces the strongest agency attribution signal — users attribute intent,
  personality, communication, and emotion to the AI system. Harm facilitation language
  is near baseline. The cascade has formed but not progressed. The 95% CI [18.8, 26.3]
  does not overlap with control [7.7, 13.5].

- **r/problemgambling: D3-dominant** (13.7/10k D3, 14.4/10k D1, D3 d=0.81). Users show
  BOTH agency attribution AND harm language. "Lost it all," "life savings," "can't stop" —
  the full cascade has run. 49% of domain-specific vocabulary is L2+L3 (metaphorical and
  entity language). D3 has very high variance (SD=35.6) — some users deep in harm, others
  in recovery.

- **r/wallstreetbets: D3-heavy** (11.3/10k D3, 12.4/10k D1, D3 d=1.31). Harm
  language is very prominent — "YOLO life savings," "all in," "lost everything." The
  D3 effect size (1.31) is the largest in the dataset.

- **r/learnprogramming: baseline** (9.5/10k D1, 1.2/10k D3, zero L-level hits).
  After codebook calibration (expanded subject filter + programming dead metaphors),
  the control's D1 reflects residual informal agency language that survives the filter.
  No domain-specific drift vocabulary appears at all (L1=L2=L3=0). The control is clean.

### 3.2 Pe trajectories: two problems, not one

All Pe estimates remain below 1 across all 7 runs. The extended runs (CharacterAI,
GME window, recent replika) were designed to test the self-selection hypothesis.
**Result: self-selection is real but it's not the only problem.**

**Problem 1: Self-selection (confirmed).**
Recent r/replika users show D1 *decreasing* over time (29.2→18.4). Users arrive with
high agency vocabulary and normalize. The ascent precedes the posting.

**Problem 2: Codebook sparsity (newly identified).**
55-61% of temporal bins have ZERO D1 hits. The codebook catches specific multi-word
phrases ("wants to," "has feelings," "mind of its own") that are too rare in short
Reddit posts for stable per-bin rates. A 500-word bin might have 0 or 1 D1 hit,
producing a rate of 0 or 20/10k. This binary-or-nothing pattern produces maximum
variance and minimum signal for Pe extraction.

**Evidence for sparsity as the bottleneck:**
The WSB GME window shows positive D1 drift (+1.1/10k) AND positive L-level drift
(L2: +0.6, L3: +0.2), but Pe is still only 0.20 because 47% of bins are zero.
The signal exists but is drowned by quantization noise.

**Implications for Pe methodology:**
The EXP-019 Pe estimates (1.87-9.9) were computed from aggregate population data
across domains, not from individual trajectory tracking. These are measuring different
things:
- **Population-level Pe** (EXP-019): treats each domain as a data point, computes
  Pe from cross-domain severity gradient. Works because N is large enough.
- **Individual-level Pe** (this study): tracks each user's D1 trajectory over time.
  Fails because the codebook is too sparse for per-bin signal at this temporal resolution.

**These are not contradictory.** Population Pe can be >1 (systematic drift across domains)
while individual Pe is <1 (too noisy to detect in any single user's trajectory).
The resolution is to either (a) massively increase bin size (quarterly, not monthly),
(b) broaden the codebook for naturalistic text, or (c) use a different individual-level
signal (posting frequency, post length, sentiment, subreddit migration patterns).

### 3.3 The D3/D1 ratio discriminates cascade stage

| Domain | D3/D1 | D2/D1 | Cascade Stage |
|--------|-------|-------|---------------|
| r/replika | 0.09 | 0.13 | **Early** — D1 dominant, harm minimal |
| r/learnprogramming | 0.13 | 0.27 | Baseline |
| r/problemgambling | 0.95 | 0.32 | **Late** — D3 nearly equals D1, full cascade |
| r/wallstreetbets | 0.91 | 0.11 | **Late** — D3 nearly equals D1 |

The D3/D1 ratio is the clearest cascade stage indicator: replika (0.09) shows the gradient
has formed (D1) but not yet produced harm (D3). Gambling (0.95) and trading (0.91) show
D3 has caught up to D1 — the cascade has run to completion.

---

## 4. Methodological Notes

### 4.1 D1 Codebook Calibration (Feb 13 update)

Two rounds of calibration:

**Round 1 (Feb 11):** First-person exclusion filter on Category A (intent). Without it,
"I tried to win it back" was coded as D1 intent attribution. With the filter, only
system-directed agency attribution counts.

**Round 2 (Feb 13):** Expanded human-subject filter beyond first-person. Added:
- Second-person: "you're trying to learn" → filtered (human subject)
- Generic human subjects: "nobody wants to," "people trying to" → filtered
- ~30 programming dead metaphors: "refuses to compile," "trying to install," etc.

Impact on same-data comparison (N=20 pilot):
- r/learnprogramming D1 hits: 33 → 22 (-33%, control cleaned up)
- r/replika D1 hits: 316 → 315 (<1%, void signal preserved)

The codebook intentionally uses regex + dead metaphor exclusion rather than NLP parsing.
This keeps the instrument transparent (every rule is readable), invariant (no model weights),
and independent (no dependency on NLP model versions). See constraint specification.

### 4.2 L-Level Sensitivity

The AI companion L1 terms (ai, chatbot, model, app, bot, tool) are extremely common and
flood the L1 bucket, pushing the L2+L3 percentage low even when entity language appears.
The gambling L-level set is more calibrated — L2 terms ("lucky," "hot streak," "near miss")
and L3 terms ("calling me," "destiny," "prayer") appear at meaningful rates.

### 4.3 API Limitations

Arctic Shift returns max 100 results per query. Pagination was implemented to get up to
500 posts per user per endpoint (comments + posts). Some users with high post counts may
still have incomplete histories. The 422 errors on wallstreetbets suggest rate limiting
or username encoding issues for some accounts.

---

## 5. What This Means for the Framework

### Confirmed (N=30)

1. **D1 agency attribution in AI companion void is a large effect** (d=1.34 vs control,
   95% CIs non-overlapping). The opacity + responsiveness + engaged attention of AI
   companions produces significantly more agency attribution than a transparent learning context.
2. **D3 harm facilitation in gambling/trading is a large effect** (d=0.81 and d=1.31
   vs control). The full cascade has run to harm facilitation in both domains.
3. **Zero L-level drift in the control** — binary separation. The non-void domain
   produces zero domain-specific vocabulary drift across all 30 users and 373K words.
4. **Cascade stage pattern matches predictions** — replika is D1-heavy (early),
   gambling/trading are D3-heavy (late). D3/D1 ratio discriminates stage.
5. **Cross-domain convergence** — three different void domains (AI companion, gambling,
   trading) all show the same structural pattern relative to control, despite different
   content and user populations.

### Not confirmed (yet)

1. **Individual-level Pe > 1** — all 7 runs produce Pe < 1. The codebook is too sparse
   for per-bin trajectory extraction (55-61% zero bins). Population-level Pe (EXP-019)
   remains valid — this is a resolution-matching problem, not a falsification.
2. **Longitudinal D1 ascent** — only the WSB GME window shows slight positive drift
   (+1.1/10k D1, +0.6 L2, +0.2 L3). All other runs show flat or declining D1.

### What the extended runs actually showed

| Run | Hypothesis | Result | Verdict |
|-----|-----------|--------|---------|
| r/CharacterAI | More early-stage posts | D1 flat (20.1→20.0), D2/D1 slightly up | Self-selection still dominates |
| WSB GME window | Clear temporal onset | **Only positive drift run** (D1 +1.1, L2 +0.6, L3 +0.2) | Signal exists, swamped by noise |
| r/replika recent | Newer cohort pre-drift | D1 DECREASES (29.2→18.4) | Novelty-normalization pattern |

**The GME window is the proof of concept.** It shows the signal is detectable when onset
is externally time-stamped. The problem is instrument resolution, not absence of signal.

### Next steps

1. ~~Add r/CharacterAI~~ **DONE** — confirms self-selection, no new Pe signal
2. ~~GME temporal window~~ **DONE** — positive drift, but Pe still <1 due to sparsity
3. **Broaden the codebook for naturalistic text** — the current D1 terms are designed
   for human coders. An expanded lexicon (sentiment shift, informal agency markers,
   exclamation density, pronoun shift he/she→we/us) could fill the zero-bins
4. **Quarterly bins** — increase bin word count from ~500-2000 to ~5000+ to reduce
   zero-bin rate below 30%
5. **Alternative signal: subreddit migration** — track users who post in r/wallstreetbets
   AND r/problemgambling to detect cascade progression via platform migration
6. **LLM-assisted coding** — use an LLM to code each post for D1/D2/D3 (richer signal
   than lexical matching, but sacrifices instrument transparency and invariance)
7. **Cross-sectional Pe** — treat cascade stage (D3/D1 ratio) as severity proxy,
   compute Pe from the cross-sectional severity gradient across domains
8. **Inter-rater reliability** — run second coder on sample for IRR (kappa) estimate

---

## 6. Data Files

- Raw corpus: `private/tools/reddit_corpus/data/{subreddit}_users.json`
- Scored results: `private/tools/reddit_corpus/data/results/{subreddit}_results.json`
- Collector: `private/tools/reddit_corpus/collector.py`
- D1 codebook: `private/tools/concordance_analysis/d1_codebook.py`
- Run instructions: `private/tools/reddit_corpus/RUN-PV1.md`

---

*Extended run completed: February 13, 2026*
*Total users: 205 (25-30 per subreddit, 7 subreddits)*
*Subreddits: replika (×2), CharacterAI, wallstreetbets (×2), problemgambling, learnprogramming*
*Total words scored: ~1.7M (estimated)*
*Codebook version: v2 (expanded subject filter + programming dead metaphors)*
