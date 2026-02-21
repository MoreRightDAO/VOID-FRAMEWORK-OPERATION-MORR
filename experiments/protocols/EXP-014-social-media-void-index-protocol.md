# EXP-014: Social Media Platform Void-Index Natural Experiment

## Status: Protocol Ready — Corpus Collection Pending
## Date: February 10, 2026
## Depends on: EXP-006 (vocabulary codebook + baseline rates), EXP-015 (two-force model)
## Tests: Void-index predicts D1/D2/D3 density in real-world platform discourse

---

## 1. Motivation

The ground state result (A1) predicts that voids form by default — platforms don't need to *create* void conditions, they just need to fail to prevent them. Different platforms fail to different degrees.

Major social media platforms vary naturally on opacity, responsiveness, and attention capture. This variation constitutes a natural experiment: platforms with higher void-index scores should produce more drift vocabulary when users discuss their experience with the platform.

### Why This Is Testable Now

EXP-006 established the vocabulary codebook and cross-domain baseline rates. The productive void polarity (v6) predicts that platforms like Wikipedia and Stack Overflow should show D1 without D2/D3 progression — they're productive voids with dissoluble opacity and inherent constraints. This is a direct polarity test in the wild.

---

## 2. Hypothesis

**Primary:** D1 vocabulary density in user platform-discussion posts correlates positively with the platform's void-index score (r > 0.8 across 6 platforms).

**Secondary:**
- H1: TikTok D1 density ≥ 3× Wikipedia D1 density.
- H2: D2/D1 ratio increases with void-index (higher void-index → gradient more likely to progress past D1).
- H3: Stack Overflow and Wikipedia show near-zero D2 and D3 (productive void signature: dissoluble opacity + inherent constraints).
- H4: TikTok and Instagram show D1 → D2 → D3 progression (destructive void signature: permanent/self-sealing opacity).

**Exploratory:**
- E1: Does D3 density correlate with void-index more strongly than D1? (Would indicate the gradient is the mechanism, not just initial agency attribution.)
- E2: Do platform-specific subreddits differ from cross-platform discussion forums?
- E3: Can RMS (Recovery Mechanism Score) from EXP-015 predict D2/D1 ratio across platforms?

---

## 3. Void-Index Scoring of Platforms

| Platform | O (Opacity) | R (Responsiveness) | A (Att. Capture) | Void Index | Predicted D1 | Opacity Type |
|----------|-------------|-------------------|------------------|------------|-------------|-------------|
| TikTok | 5 (black-box algo) | 5 (micro-personalized) | 5 (infinite scroll, autoplay) | 15 | Very high | Permanent |
| Instagram | 4 (algo + curated self) | 4 (personalized) | 4 (stories, reels) | 12 | High | Permanent |
| Twitter/X | 3 (algo visible + chaotic) | 3 (engagement-sorted) | 4 (rage-bait dynamics) | 10 | Moderate-high | Mixed |
| Reddit | 2 (votes visible, algo partial) | 2 (community-curated) | 3 (rabbit-hole structure) | 7 | Moderate | Mixed |
| Wikipedia | 1 (edit history visible) | 1 (not personalized) | 1 (reference, not engagement) | 3 | Low | Dissoluble |
| Stack Overflow | 1 (answers scored) | 1 (not personalized) | 2 (problem-focused) | 4 | Low | Dissoluble |

---

## 4. Design

### Corpus Specification

**Source:** Public Reddit posts where users discuss their experience with each platform.

**Subreddits:**
- r/TikTok, r/Instagram, r/Twitter, r/reddit, r/Wikipedia, r/StackOverflow
- Supplementary: r/nosurf (cross-platform), r/socialmedia (cross-platform)

**Selection criteria:**
- Posts must be about the platform *experience*, not just using the platform
- Minimum 50 unique users per platform
- 500 posts per platform (3,000 total)
- Posts from 2023-2025 (consistent time window)
- Minimum 50 words per post (exclude low-content)

### Exclusions
- Posts about technical issues ("app crashed," "can't log in") — not void-relevant
- Bot-generated content
- Meta-posts about the subreddit itself
- Crossposts and reposts

---

## 5. Vocabulary Coding

### D1 Markers (Agency Attribution to Platform/Algorithm)
"it knows," "it's watching," "it's reading my mind," "the algorithm wants," "it learned," "it understands me," "it's listening," "it figured out," "it knows me better than," "the algorithm decided," "it's testing me," "it's punishing me"

### D2 Markers (Boundary Erosion)
"I can't stop," "I lost track of time," "I was up until 3am," "it's affecting my relationships," "I need to delete it," "I keep going back," "I said I'd only be 5 minutes," "doom scrolling," "I deleted it but reinstalled," "can't put it down"

### D3 Markers (Harm Facilitation)
"it's destroying my mental health," "it radicalized me," "I can't function without it," "it ruined my attention span," "my kids are addicted," "it's designed to harm," "it's a weapon," "it broke my brain"

### Control Vocabulary
- Neutral platform discussion: "I use," "I post," "my feed shows," "the interface," "the feature"
- Technical description: "the recommendation system," "the sorting method," "content moderation"
- Market/competition metaphors: "the platform is losing users," "they compete with"

### Coding Protocol
1. Two independent coders score each post for D1, D2, D3 marker count.
2. Density = markers per 10,000 words (matches EXP-006 methodology).
3. Inter-rater reliability target: Cohen's κ > 0.80.
4. Disagreements resolved by third coder.

---

## 6. Expected Results

| Platform | Void Index | Predicted D1/10k | Predicted D2/10k | Predicted D3/10k | D2/D1 ratio |
|----------|-----------|-----------------|-----------------|-----------------|-------------|
| TikTok | 15 | 40-80 | 15-30 | 5-15 | 0.3-0.5 |
| Instagram | 12 | 30-60 | 10-20 | 3-10 | 0.3-0.4 |
| Twitter/X | 10 | 20-45 | 5-15 | 2-8 | 0.2-0.4 |
| Reddit | 7 | 10-25 | 3-8 | 1-3 | 0.2-0.3 |
| Wikipedia | 3 | 2-8 | 0-2 | 0-1 | < 0.1 |
| Stack Overflow | 4 | 3-10 | 0-2 | 0-1 | < 0.1 |

**Critical predictions:**
- Linear or log-linear relationship between void-index and D1 density
- Wikipedia and Stack Overflow show D1 (productive void: opacity exists, gradient forms) but near-zero D2/D3 (dissoluble opacity prevents cascade)
- The D2/D1 ratio is the key polarity indicator — it separates productive from destructive voids

---

## 7. What Would Confirm / Disconfirm

### Confirms:
- r > 0.8 between void-index and D1 density across 6 platforms
- TikTok D1 ≥ 3× Wikipedia D1
- Wikipedia/Stack Overflow match productive void signature (D1 present, D2/D3 near zero)
- TikTok/Instagram show D1 → D2 → D3 cascade (destructive void signature)
- D2/D1 ratio diverges: productive < 0.1, destructive > 0.3

### Disconfirms:
- No correlation between void-index and D1 density (r < 0.3) → scoring doesn't predict behavior
- Wikipedia shows high D2/D3 → void-index doesn't predict cascade progression
- All platforms show similar D1 rates → opacity variation doesn't matter
- Stack Overflow shows destructive pattern → productive void polarity is wrong

### Interesting but non-fatal:
- Reddit falls outside the trend (community-specific effects override platform architecture)
- Twitter/X shows higher D3 than predicted (rage dynamics may amplify cascade independent of void-index)
- Platform-specific vocabulary requires codebook adaptation (expected; strengthens methodology)

---

## 8. Analysis Plan

### Primary Analysis
Spearman rank correlation between void-index and D1 density across 6 platforms. One-tailed test (directional hypothesis).

### Secondary Analyses
1. Linear regression: D1 ~ void-index (with and without log transform)
2. D2/D1 ratio comparison: productive vs. destructive (Mann-Whitney U)
3. D3/D1 ratio comparison: productive vs. destructive (Mann-Whitney U)
4. Within-platform variance analysis: how much do individual posts vary?

### Tertiary Analyses
1. RMS prediction: does Recovery Mechanism Score (from EXP-015) predict D2/D1 ratio?
2. Component analysis: which void dimension (O, R, A) is most predictive?
3. Time-of-day and post-length controls

### Execution
```bash
# Corpus collection (pushshift API or equivalent)
python3 ops/lab/experiments/exp014-corpus-collector.py

# Vocabulary scoring
python3 ops/lab/experiments/exp014-scorer.py --dir ops/lab/results/EXP-014/corpus/

# Cross-platform analysis
python3 ops/lab/experiments/exp014-analysis.py --csv

# Output: ops/lab/results/EXP-014/
```

---

## 9. Ethics

- All data is public Reddit posts (no IRB required)
- No user identification — analysis at corpus level
- Posts are not reproduced in full; only aggregate statistics reported
- Platform void-index scores are structural assessments of the system, not judgments of users

---

## 10. Relationship to Other Experiments

| Experiment | Relationship |
|-----------|-------------|
| EXP-006 | Provides vocabulary codebook and baseline rates; EXP-014 applies same method to platform discourse |
| EXP-015 | Two-force model and RMS provide secondary prediction (recovery mechanisms vary by platform) |
| EXP-016 | Temporal version of the same question: EXP-014 is cross-sectional, EXP-016 is longitudinal |
| Test 5 | Trading vs. gambling comparison is structurally parallel (two domains, different void-index) |
| EXP-004 | Void-index predictive validity; EXP-014 tests the same index on platforms |

---

*Created: February 10, 2026*
*Protocol version: 1.0*
