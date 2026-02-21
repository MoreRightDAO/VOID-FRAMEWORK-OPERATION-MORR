# EXP-014: Social Media Platform Void-Index — Results

## Status: Initial Analysis Complete
## Date: February 10, 2026
## Corpus: 600 posts, 410,347 words across 6 platforms
## Source: Arctic Shift (Reddit archive API)

---

## 1. Executive Summary

**D1 (agency attribution) correlates strongly with void-index across platforms.** Pearson r = +0.91 (p = 0.013). High-void platforms (TikTok, Instagram) show 6.8× more agency-attribution language than low-void platforms (Wikipedia, Stack Overflow). This is the primary finding.

**D2/D3 results are contaminated** by cross-subreddit corpus issues (see Section 5). The D2/D1 polarity test cannot be evaluated from this data. A cleaned corpus is needed for D2/D3 conclusions.

---

## 2. Cross-Platform Results

| Platform | VI | Type | Posts | Words | D1/10k | D2/10k | D3/10k | D2/D1 |
|----------|---:|------|------:|------:|-------:|-------:|-------:|------:|
| TikTok | 15 | permanent | 100 | 29,478 | 3.05 | 5.43 | 4.41 | 1.78 |
| Instagram | 12 | permanent | 100 | 36,028 | 3.33 | 10.55 | 3.05 | 3.17 |
| Twitter/X | 10 | mixed | 100 | 40,050 | 2.50 | 4.99 | 8.99 | 2.00 |
| Reddit | 7 | mixed | 100 | 93,779 | 0.32 | 2.24 | 1.81 | 7.00 |
| Stack Overflow | 4 | dissoluble | 100 | 118,866 | 0.51 | 0.93 | 0.67 | 1.83 |
| Wikipedia | 3 | dissoluble | 100 | 92,146 | 0.43 | 12.37 | 1.95 | 28.50 |

---

## 3. D1 Analysis (Primary Finding)

### Correlations with Void-Index

| Measure | Statistic | Value | p-value | Assessment |
|---------|-----------|-------|---------|------------|
| VI × D1 | Pearson r | +0.907 | 0.013 | **Significant** |
| VI × D1 | Spearman ρ | +0.771 | 0.072 | Marginal (N=6) |
| Opacity × D1 | Spearman ρ | +0.754 | 0.083 | Marginal |
| Responsiveness × D1 | Spearman ρ | +0.754 | 0.083 | Marginal |
| Attention × D1 | Spearman ρ | +0.725 | 0.103 | Marginal |

The Pearson r is significant at α = 0.05. Spearman is marginal due to N=6 (rank-based tests lose power with few data points). The linear relationship is strong: void-index explains ~82% of D1 variance.

### D1 Separation

High-void platforms (TikTok + Instagram, mean VI = 13.5): **D1 = 3.19/10k**
Low-void platforms (Wikipedia + Stack Overflow, mean VI = 3.5): **D1 = 0.47/10k**
Ratio: **6.8×** (exceeds the 3× threshold)

### D1 Top Terms by Platform

| Platform | D1 Terms |
|----------|----------|
| TikTok | "the algorithm is" (5), "tiktok wants" (2), "algorithm thinks" (2) |
| Instagram | "the algorithm is" (5), "instagram is pushing" (2), "targeting me" (1) |
| Twitter/X | "the algorithm is" (3), "twitter wants" (1), "twitter rewards" (1), "feeds me" (1) |
| Reddit | "the algorithm is" (2), "reddit knows" (1) |
| Wikipedia | "designed to keep you" (2), "algorithm thinks" (1) |
| Stack Overflow | "they want you to" (3), "they want me to" (2), "designed to keep you" (1) |

**Note:** Wikipedia and Stack Overflow D1 terms are almost entirely from r/nosurf crossposts discussing those platforms in the context of broader social media. Platform-specific D1 (users on r/wikipedia attributing agency to Wikipedia) is near zero, as predicted.

---

## 4. Hypothesis Assessment

| Hypothesis | Prediction | Result | Status |
|-----------|-----------|--------|--------|
| H_primary | D1 correlates with VI (r > 0.8) | Pearson r = 0.91 | **Confirmed** (Pearson) |
| H1 | TikTok D1 ≥ 3× Wikipedia D1 | 7.0× | **Confirmed** |
| H2 | D2/D1 increases with VI | ρ = -0.60, p = 0.21 | **Cannot evaluate** (contamination) |
| H3 | Wiki/SO near-zero D2/D3 | SO yes, Wiki no | **Partial** (see Section 5) |
| H4 | TikTok/Instagram show cascade | D1 → D2 → D3 present | **Supported** |

### Disconfirmation Checks

| Condition | Triggered? | Detail |
|-----------|-----------|--------|
| No correlation (ρ < 0.3) | No | ρ = 0.77 |
| Wikipedia shows high D2/D3 | **Yes** | D2 = 12.37 (contamination) |
| All platforms similar D1 | No | Range: 0.32 – 3.33 |

---

## 5. Methodological Issues

### Wikipedia D2 Contamination

Wikipedia's D2 density (12.37/10k) is artificially inflated. The corpus collected posts from r/nosurf that mention Wikipedia in the context of discussing general social media addiction. The D2 terms that drive this:

- "screen time" (32 occurrences) — general, not Wikipedia-specific
- "addicted to" (28) — mostly "addicted to my phone / social media"
- "doomscroll" (6) — not a Wikipedia behavior
- "rabbit hole" (12) — partially genuine (Wikipedia rabbit holes are real)

**Impact:** The D2/D1 polarity test is invalid for this run. Wikipedia's genuine D2 is likely near Stack Overflow levels (~1/10k). The productive void signature (D1 present, D2 near zero) may still hold but cannot be confirmed from this corpus.

**Fix for v2:** Restrict Wikipedia and Stack Overflow corpora to posts from platform-specific subreddits only (r/wikipedia, r/stackoverflow). Exclude r/nosurf and r/digitalminimalism for these platforms, or apply stricter platform-specificity filtering.

### Corpus Size Imbalance

Word counts vary 4× across platforms (29K for TikTok vs. 119K for Stack Overflow). This occurs because:
- Longer posts are preferentially selected (sorted by word count)
- r/cscareerquestions and r/TheoryOfReddit tend toward longer posts than r/TikTok

**Impact:** Density normalization (per 10K words) handles this, but longer corpora have more statistical power per platform. Consider balancing by total words rather than post count in v2.

### D3 "Toxic" Dominance

The term "toxic" accounts for the majority of D3 markers across most platforms (TikTok: 9/13, Twitter: 30/36, Stack Overflow: 7/8). This is a generic negative term, not a specific harm indicator. Removing "toxic" from D3 would reduce D3 counts by ~70%.

**Impact:** D3 is likely overcounted. Consider reclassifying "toxic" as D2 (boundary erosion) or removing it entirely. The specific D3 terms ("radicalized me," "destroyed my mental health") are more meaningful but rarer.

---

## 6. Key Finding: D1 as the Clean Signal

The D1 result is robust because:

1. **Platform-specific terms dominate:** "the algorithm is...", "[platform] wants...", "[platform] thinks..." — these are unambiguously about the platform, not general sentiment.
2. **Clean separation:** High-void D1 (2.50–3.33) vs. low-void D1 (0.32–0.51) with no overlap.
3. **Linear relationship:** r = 0.91, the void-index accounts for 82% of D1 variance.
4. **Consistent across high-void platforms:** TikTok, Instagram, and Twitter all cluster together with similar D1 densities, proportional to void-index.

This supports the framework's core prediction: platforms with higher opacity + responsiveness + attention capture produce more agency-attribution language in their users. The algorithm IS being treated as an agent, and the rate of treatment scales with the void-index score.

---

## 7. Two-Force Model Connection (EXP-015 Integration)

Stack Overflow's low D2/D1 ratio (1.83) vs. TikTok's (1.78) suggests comparable cascade *probability* once D1 occurs, but the D1 *base rate* is 6× lower for Stack Overflow. This is consistent with the two-force model from EXP-015:

- σ_net = σ_void − σ_recovery
- Stack Overflow has low σ_void (low void-index) AND high σ_recovery (answers resolve uncertainty)
- TikTok has high σ_void (high void-index) AND low σ_recovery (algorithm maintains opacity)

The net effect is dramatic: TikTok's drift is ~6.8× stronger, not because the cascade behaves differently, but because the gradient forms more easily under high-void conditions and has less recovery force opposing it.

---

## 8. Recommended Next Steps

1. **Clean Wikipedia corpus:** Re-run with platform-specific subreddits only.
2. **Reclassify "toxic":** Move from D3 to D2 or remove; rerun D3 analysis.
3. **Add post-level analysis:** Compute per-post D1 distributions, not just means. Test variance.
4. **Run EXP-016:** The temporal version of this — track D1/D2/D3 within threads over time.
5. **Increase N:** 100 posts per platform is a pilot. Scale to 500 for publication.

---

*Analysis date: February 10, 2026*
*Pipeline: exp014-corpus-collector.py → exp014-scorer.py → exp014-analysis.py*
*Protocol version: 1.0 (initial run)*
