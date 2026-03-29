# EXP-028: IRR Game Study — Inter-Rater Reliability via Gameplay
## OSF Pre-registration Document

**Experiment ID:** EXP-028
**Study:** Krippendorff's α Validation of Void Framework Scoring Rubric via In-Game Scoring
**Date:** 2026-02-28
**Status:** Pre-registered (file on OSF before first blind score is submitted)

---

## 1. Research Question

Does the Void Framework O/R/C rubric produce inter-rater agreement (Krippendorff's α > 0.60) when administered to general-population players via in-game blind scoring, without explicit rater training?

## 2. Hypotheses

**H1 (Primary):** Aggregate Krippendorff's α across 30 study set platforms will exceed 0.60 (acceptable threshold) after 10+ blind rater scores per platform.

**H2 (Concordance):** Spearman ρ between mean game-player ICC scores and trained IRR rater scores (EXP-024 raters) will exceed 0.60 on the study set.

**H3 (Rank Order):** Platform rank order by mean game-player Pe estimate will correlate (Spearman ρ > 0.80) with existing community scores for same platforms (N ≥ 3 prior scores).

## 3. Inclusion Criteria

- Score submitted via in-game scoring panel (`POST /api/v1/scores/platform`)
- `blind_mode: true` flag set (study_set platform, community aggregate not shown before submission)
- Score passed basic validation (O/R/C each 1–5 integer)
- Rater had not previously scored this platform (wallet deduplication)
- Minimum 3 blind scores per platform for per-platform α computation
- Minimum 2 raters scoring 2 platforms for aggregate α

## 4. Study Set — 30 Pre-specified Platforms

Platforms span the full Pe range (ANCIENT → DRIFTING) for maximum discriminability:

| # | Platform | Expected Pe Range | Notes |
|---|----------|------------------|-------|
| 1 | TikTok | >21 (DRIFTING) | For You Page |
| 2 | Instagram | 13–21 | Feed + Reels |
| 3 | YouTube (algorithmic feed) | 13–21 | Autoplay + recommendations |
| 4 | Facebook | 13–21 | News Feed + Groups |
| 5 | Snapchat | 8–13 | Stories + Discover |
| 6 | Twitter/X | 8–13 | Algorithmic timeline |
| 7 | Character.AI | >21 | Companion AI |
| 8 | Replika | >21 | Companion AI |
| 9 | DraftKings/FanDuel | >21 | Sports betting |
| 10 | Candy Crush / mobile gacha | >21 | Mobile gaming void |
| 11 | LinkedIn | 4–8 | Professional network |
| 12 | Reddit | 4–8 | Subreddit feed |
| 13 | Amazon (product pages) | 8–13 | Dark patterns |
| 14 | Netflix (autoplay) | 8–13 | Autoplay + recommendations |
| 15 | Spotify (algorithmic) | 4–8 | Algorithmic playlists |
| 16 | Discord | 4–8 | Community chat |
| 17 | Cable news (Fox/CNN aggregate) | 4–8 | 24h news cycle |
| 18 | Google Search | 4–8 | Organic + ads |
| 19 | Wikipedia | <4 (STABLE) | Open reference |
| 20 | BBC News | <4 | Editorial standard |
| 21 | Stack Overflow | <4 | Q&A, low coupling |
| 22 | arXiv | <4 | Scientific preprints |
| 23 | PubMed | <4 | Medical literature |
| 24 | Duolingo | 4–8 (mixed) | Gamified learning |
| 25 | Khan Academy | <4 | Education, open |
| 26 | GitHub | <4 | Dev platform |
| 27 | Aspirin (pharma null) | <0 (ANCIENT) | Constraint pole |
| 28 | Generic statins | <0 | Constraint pole |
| 29 | Public library catalog | <0 | Transparent, invariant |
| 30 | OpenStreetMap | <4 | Open data |

## 5. Scoring Rubric

Each dimension scored 1–5 (1–3 rubric remapped via V3 bridge):

**Opacity (O):** How hidden is the mechanism driving attention?
- 1 = Fully transparent (user can inspect the algorithm)
- 3 = Partially opaque (some signals visible)
- 5 = Fully opaque (black-box optimization, mechanism hidden)

**Reactivity (R):** Does the platform adapt to your individual behavior?
- 1 = Invariant (same experience for all users)
- 3 = Partially adaptive
- 5 = Fully reactive (hyper-personalized, real-time behavioral adaptation)

**Coupling (C):** How difficult is disengagement?
- 1 = Independent (easy to stop, no hooks)
- 3 = Moderately coupled
- 5 = Fully coupled (variable reward schedules, social obligation, withdrawal effects)

**Pe formula (V3 bridge):** Pe = 16 × sinh(2 × (β_A − c × β_G)) where c = 1 − V/9, V = O_r + R_r + C_r (each dimension remapped 0–3).

## 6. Analysis Plan

1. **Per-platform α:** Compute simplified Krippendorff's α (SD-normalized) for each of the 30 platforms independently.
2. **Aggregate α:** Compute full interval Krippendorff's α across the complete rater×platform matrix (raters with ≥2 platform scores included).
3. **H1 test:** Test aggregate α > 0.60 using bootstrap CI (1,000 samples). Report point estimate + 95% CI.
4. **H2 test:** Compute Spearman ρ between mean game-player scores and EXP-024 trained rater scores on overlapping platforms.
5. **H3 test:** Compute Spearman ρ between game-player Pe ranks and existing community Pe scores for same 30 platforms.
6. **Subgroup:** Compare blind α vs. non-blind α for same platforms (does game players knowing community scores reduce or inflate agreement?).

## 7. Analysis Code

Results computed by `GET /api/v1/scores/irr-study` using `api/lib/krippendorff.js`. Source available in repo under Apache 2.0 (Feb 2030 → CC-BY then).

## 8. Power Analysis

- N=30 platforms × N=10 raters per platform = 300 scores minimum for H1
- At expected aggregate α=0.72 (based on EXP-024 pilot), power > 0.90 to reject α=0.50 null at α=0.05
- H2/H3 require N≥10 overlapping platforms with trained rater data

## 9. Kill Conditions

If after 50+ blind scores per platform aggregate α < 0.40:
- Rubric requires revision — this threatens Paper 52's validity claim
- Trigger Kill Condition #KC-R2 (rubric operationalization)
- Report failure in pre-registration update on OSF within 30 days

## 10. Timeline

- Pre-registration filed: 2026-02-28
- Blind scoring via game (automated collection): ongoing
- First interim analysis (≥5 scores/platform): when available
- Primary analysis (≥10 scores/platform): target Q2 2026
- Paper 55 pre-registration DOI required before seeding PAL-P1–P5 markets

---

*This document is pre-registered on OSF before any blind scores are collected. The platform list, hypotheses, and analysis plan are fixed and cannot be amended without timestamped versioning on OSF.*
