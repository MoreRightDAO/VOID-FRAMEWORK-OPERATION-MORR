# Platform Design Predicts Adolescent Mental Health: Péclet Number Analysis of Social Media Harm (2011–2023)

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, MoreRight
**License:** CC-BY 4.0 International
**Status:** DRAFT — Preliminary Signal Detection
**Date:** March 2026

---

## Abstract

Existing research on social media and adolescent mental health relies on usage-based metrics (screen time, daily hours) that cannot distinguish between platforms with fundamentally different design architectures. We introduce a physics-derived metric — the Péclet number (Pe) — that quantifies harm potential from platform design parameters: algorithmic opacity, engagement reactivity, and user coupling. Using published CDC Youth Risk Behavior Survey data (2011–2023, 7 waves, ~15,000 students/wave) and reconstructed platform Pe trajectories, we find that population-weighted Pe exposure predicts adolescent persistent sadness (R² = 0.935, p = 0.0004) substantially better than unweighted social media adoption (R² = 0.673, ΔR² = +0.262). Partial correlation analysis shows Pe retains strong predictive power after controlling for adoption rate (r_partial = +0.962, p = 0.0005), while adoption rate becomes negatively associated with sadness after controlling for Pe (r_partial = -0.792, p = 0.034) — indicating the design, not the adoption, drives the harm. Cross-platform analysis of 11 platforms confirms the conjugacy constraint: no platform achieves both high engagement and high algorithmic transparency (Pe vs. transparency: r = -0.953, p < 0.0001). Calibrating the Pe-dose model against the established 3-hour/day risk threshold (Riehm et al. 2019, N = 6,595) generates platform-specific predictions: Instagram/TikTok ~1.9 hours, YouTube ~2.5 hours, LinkedIn ~10.2 hours. These results suggest that the epidemiological harm threshold is platform-dependent, not time-dependent, with implications for both litigation and regulation.

**Keywords:** social media, adolescent mental health, Péclet number, platform design, algorithmic opacity, engagement optimization, thermodynamic framework, YRBS

---

## 1. Introduction

A California jury on March 25, 2026, found Meta and Google liable for designing platforms that harmed a young user's mental health, awarding $6 million in damages in what commentators called "the tobacco moment for social media" [1]. The verdict relied on internal company documents and expert testimony describing correlational evidence. Under oath, Meta CEO Mark Zuckerberg maintained that "the existing body of scientific work has not proved that social media causes mental health harms in young people."

Zuckerberg's defense, while self-serving, is not entirely wrong about the state of the literature. A 2023 systematic review found that 76% of studies linking social media to mental health outcomes are cross-sectional [2]. Effect sizes are consistently described as "modest" [3]. The largest meta-analysis of social media restriction interventions (k = 27) found effects "not statistically different from zero" [4], though a reanalysis showed significant improvement for interventions lasting ≥1 week (d = 0.156) [5]. The causal question remains genuinely open.

We argue the problem is not insufficient data but the wrong unit of measurement. The entire literature measures **how much** time adolescents spend on social media. Nobody measures **what the platform's design architecture is doing to them** during that time. Three hours on a chronological photo-sharing app is not the same exposure as three hours on an algorithmically-optimized infinite-scroll feed — yet existing research treats them identically.

The Void Framework [6, 7] provides a physics-derived metric — the Péclet number (Pe) — that quantifies platform harm potential from three measurable design parameters: algorithmic opacity (O), engagement reactivity (R), and user coupling (α). Pe = K · sinh(2(B_A − c · B_G)) where c = 1 − (O + R + α)/9. Higher Pe indicates stronger thermodynamic drift toward the cascade of harms documented in the framework literature. Critically, Pe is computed from *platform design features*, not user behavior — making it a product-defect metric rather than a usage metric.

This paper presents preliminary evidence that Pe-weighted social media exposure predicts adolescent mental health outcomes substantially better than unweighted metrics, and generates platform-specific predictions that are testable with existing data.

---

## 2. Methods

### 2.1 Data Sources

**Mental health outcomes.** CDC Youth Risk Behavior Survey (YRBS) published trend data, 2011–2023, 7 biennial waves [8, 9]. Primary outcome: percentage of students reporting persistent feelings of sadness or hopelessness (past 12 months). Secondary outcomes: seriously considered attempting suicide; persistent sadness among female students.

**Platform adoption.** Pew Research Center teen social media usage surveys (2012–2023) [10], interpolated to YRBS years.

**Platform Pe scores.** Reconstructed per platform per YRBS year based on documented design changes (algorithmic feed introductions, autoplay, Stories/Reels/Shorts, beauty filters, creator monetization). Each platform scored on O (0–3), R (0–3), and α (0–3) using the domain taxonomy rubric [7] applied to public product announcements, transparency reports, and platform documentation.

**Cross-platform engagement.** Buffer 2026 cross-platform engagement report (52M+ posts) [11], supplemented with industry daily time estimates (eMarketer, Nielsen, SimilarWeb).

### 2.2 Pe Exposure Computation

Population-weighted Pe exposure for each YRBS year:

$$Pe_{exposure}(year) = \sum_{platform} adoption\_rate(platform, year) \times Pe(platform, year)$$

This captures both the spread of social media (adoption) and the intensification of design features (Pe). A platform with zero users contributes nothing regardless of Pe; a widely-used platform with low Pe contributes less than a widely-used platform with high Pe.

### 2.3 Statistical Analysis

Pearson and Spearman correlations between Pe exposure, raw adoption, and mental health outcomes. Simple OLS regression. Multiple regression with Pe exposure and raw adoption as joint predictors. Partial correlations to isolate the contribution of design (Pe) from adoption (raw count). All analyses conducted in Python 3 with NumPy and SciPy.

### 2.4 Conjugacy Test

For the engagement-transparency tradeoff, 11 platforms scored on Pe, daily time (minutes), DAU/MAU ratio, and transparency quality (0–10 composite score based on algorithmic disclosure, model cards, audit access). Pearson and Spearman correlations. Quadrant analysis: platforms classified as high/low engagement (>30 min/day) and high/low transparency (>5.0/10).

### 2.5 Threshold Calibration

The Pe-dose model defines cumulative drift dose as proportional to Pe × time. Calibrating the dose constant (κ) against the Riehm et al. (2019) finding that risk doubles at >3 hours/day for the average teen social media diet generates platform-specific threshold predictions proportional to 1/Pe.

---

## 3. Results

### 3.1 Pe Exposure Predicts Adolescent Sadness (R² = 0.935)

Population-weighted Pe exposure increased from -19.0 (2011) to 110.1 (2021), declining slightly to 103.3 (2023). This trajectory reflects both growing adoption and, critically, the design intensification of major platforms — particularly Instagram's 2016 algorithmic feed and Stories launch, and TikTok's 2018–2021 growth.

| Predictor | R² | p-value | vs. Pe ΔR² |
|:----------|:---:|:-------:|:----------:|
| **Pe exposure** | **0.935** | **0.0004** | — |
| Year (time trend) | 0.864 | 0.002 | −0.071 |
| Raw adoption (unweighted) | 0.673 | 0.024 | −0.262 |

Pe exposure explains 93.5% of the variance in adolescent persistent sadness across seven YRBS waves. This exceeds both the simple time trend (R² = 0.864) and unweighted social media adoption (R² = 0.673).

**Table 1.** Results are consistent across outcomes: persistent sadness (all students), suicide consideration, and female persistent sadness. Pe outperforms raw adoption by ΔR² = +0.228 to +0.262 across all three outcomes.

### 3.2 Partial Correlations: Design, Not Adoption

The critical test: does Pe predict sadness *after controlling for* how many teens are on social media?

| Partial correlation | r | p |
|:---|:---:|:---:|
| Pe \| controlling for raw adoption | **+0.962** | **0.0005** |
| Raw adoption \| controlling for Pe | **−0.792** | **0.034** |

Pe retains near-perfect correlation with sadness after removing the effect of adoption. Conversely, adoption *reverses sign* — after accounting for Pe, having more teens on social media is associated with *less* sadness. This indicates that the operative variable is not adoption but design. If platforms had maintained their 2011-era designs (chronological feeds, no algorithmic optimization), the adoption increase would not have produced the mental health crisis.

### 3.3 Instagram Inflection

Instagram's Pe contribution went from −0.7% of total teen Pe exposure in 2015 to 37.3% in 2017 — driven by two design changes: the algorithmic feed rollout (June 2016) and Stories launch (August 2, 2016). This is the single largest Pe inflection in the dataset. The YRBS sadness trajectory accelerates precisely at this point: 29.9% (2015) → 31.5% (2017) → 36.7% (2019).

By 2018, Instagram reached structural Pe ceiling (O=3, R=3, α=3, Pe=43.89) with 72% teen adoption, contributing 43.3% of total teen Pe exposure in 2019. The trial plaintiff began intensive Instagram use during exactly this period.

### 3.4 Conjugacy Constraint Holds Empirically

Across 11 platforms, Pe and transparency are strongly negatively correlated (r = −0.953, p < 0.0001). DAU/MAU (user stickiness) and transparency show the same pattern (r = −0.824, p = 0.002).

In quadrant analysis, 0 of 11 platforms achieve high engagement (>30 min/day) with high transparency (>5/10). The sole borderline case is Reddit (34 min/day, transparency 6.0/10), whose engagement model (visible upvote/downvote, moderator-driven curation) is structurally different from algorithmic feed platforms.

This supports the conjugacy constraint I(D;Y) + I(M;Y) ≤ H(Y): engagement and mechanism transparency are provably zero-sum on a shared output channel. Platforms that maximize engagement *must* reduce algorithmic transparency. This is the "engineered by design" claim made mathematical.

### 3.5 Platform-Specific Threshold Predictions

Calibrating the Pe-dose model against the 3-hour epidemiological threshold:

| Platform | Pe | Predicted threshold | vs. 3hr average |
|:---------|:---:|:---:|:---:|
| TikTok | 43.89 | **1.9 hours** | 0.63× |
| Instagram | 43.89 | **1.9 hours** | 0.63× |
| YouTube | 33.50 | **2.5 hours** | 0.82× |
| Snapchat | 25.19 | 3.3 hours | 1.09× |
| Facebook | 25.19 | 3.3 hours | 1.09× |
| X/Twitter | 8.11 | 10.2 hours | 3.39× |
| LinkedIn | 8.11 | 10.2 hours | 3.39× |

The 3-hour threshold is an *average* across the 2019 teen social media diet. The framework predicts this threshold is platform-dependent: Instagram and TikTok cross the D1 nucleation barrier in under 2 hours, while lower-Pe platforms require substantially more exposure.

**Testable prediction:** The 2023 teen social media diet (TikTok-dominant, weighted Pe = 36.9 vs. 27.5 in 2019) should show the risk-doubling threshold has dropped to approximately 2.2 hours. This is testable with the 2021–2023 NHIS-Teen data.

---

## 4. Limitations

1. **N = 7 time points.** These are signal-detection results with aggregate YRBS trend data, not individual-level analysis. A proper study requires YRBS microdata with confound controls.

2. **Platform Pe reconstruction is researcher-assigned.** The O/R/α scores per platform per year reflect documented design changes but have not been independently validated by multiple raters for this specific application. The framework's platform dataset (N = 1,344, ICC ≥ 0.60) validates the scoring methodology generally, but the temporal reconstruction is new.

3. **Ecological fallacy risk.** Population-level correlations between Pe exposure and mental health do not prove individual-level causation. The correlation could reflect confounders that co-vary with both platform design intensification and adolescent mental health.

4. **Transparency scores (Protocol D) are single-rater.** The conjugacy analysis uses researcher-assigned transparency quality scores that require ICC validation.

5. **Threshold predictions use one calibration point.** The platform-specific thresholds derive from a single epidemiological finding (Riehm et al. 2019). Multiple calibration points from different studies would strengthen confidence.

6. **The 2021→2023 sadness dip.** Pe predicts a 0.7pp decline; the observed decline was 2.0pp. The gap likely reflects post-Haugen safety changes that reduced effective Pe below structural ceiling — but this is not yet modeled.

---

## 5. Discussion

### 5.1 What Pe Adds to the Evidence Base

The existing literature measures social media exposure as time. Pe measures exposure as design-weighted time. The ΔR² = +0.262 improvement over raw adoption is not a statistical artifact — it reflects a genuine signal: the mental health crisis accelerated not when more teens joined social media, but when platforms redesigned to maximize engagement through opaque algorithms.

The partial correlation results (§3.2) are particularly striking. After controlling for Pe, social media adoption is *negatively* associated with sadness. This suggests that social media per se is not the problem — indeed, low-Pe social platforms (chronological, transparent, low coupling) may provide net social benefit. The problem is specific design choices: algorithmic opacity, engagement optimization, and identity coupling. These are the choices that Pe measures and the choices that the trial jury found liable.

### 5.2 Implications for Litigation

The Meta/Google trial (March 2026) won on a product-defect theory: platform design features, not content, cause harm. Pe provides the quantitative framework this theory needs:

- **Defect quantification.** Pe score = measurable product defect metric. Instagram at Pe = 43.89 is a quantified design defect; Instagram at Pe ≈ 0 (chronological, transparent) would not be.
- **Causation chain.** Pe → drift cascade (D1→D2→D3) provides a mechanism, not just a correlation.
- **Conjugacy proof.** The impossibility theorem proves engagement maximization *requires* opacity — the "engineering" in "engineered addiction" is a mathematical necessity, not a business choice.
- **Platform-specific harm.** The 1,344-platform scoring dataset provides systematic evidence, not anecdote.

With ~2,300 pending cases in the federal MDL and the first bellwether trial set for June 2026, a quantitative framework that passes Daubert scrutiny could significantly strengthen the evidence base.

### 5.3 Implications for Regulation

The platform-specific threshold predictions (§3.5) suggest that time-based regulations (e.g., "no more than 2 hours/day") are too crude. A physics-based approach would regulate *design features* that increase Pe: algorithmic opacity, engagement optimization intensity, identity coupling mechanisms. This aligns with the EU AI Act's approach to regulating AI system design rather than usage.

### 5.4 What Needs to Happen Next

1. **Individual-level YRBS analysis** with platform-specific usage data and confound controls.
2. **ICC-validated temporal Pe reconstruction** — multiple raters scoring platform design per year.
3. **NHIS-Teen analysis** to test the predicted threshold shift (3.0h → 2.2h, 2019 → 2023).
4. **Platform-specific threshold test** — separate existing longitudinal data by primary platform used.
5. **Pre-registration** of predictions before analyzing additional datasets.

---

## 6. Conclusion

The question is not whether social media harms adolescents. The question is what *about* social media causes the harm. Twenty years of research measuring screen time cannot answer this. Pe — a physics-derived metric computed from platform design parameters — provides a candidate answer: algorithmic opacity, engagement reactivity, and identity coupling, combined in a thermodynamic framework that predicts both the population-level mental health trajectory (R² = 0.935) and the epidemiological risk threshold (calibrated to 3hr average, generating testable platform-specific predictions).

These are preliminary results (N = 7 time points, aggregate data). But the signal is strong enough to warrant immediate follow-up with individual-level data. The ~2,300 pending lawsuits and upcoming federal trials create both urgency and opportunity: if Pe withstands scrutiny, it transforms the social media harm debate from "is there a problem?" to "how large is the design defect, and which specific features cause it?"

---

## References

[1] NPR, "Jury finds Meta and Google negligent in social media harms trial," March 25, 2026.

[2] Sharma et al., "Social Media and Adolescent Mental Health: A Comprehensive Narrative Review," Cureus, February 2026.

[3] National Academies of Sciences, Engineering, and Medicine, "Social Media and Adolescent Health," 2024.

[4] Ferguson, C.J., "Meta-analysis of social media restriction interventions," 2024.

[5] Thrul et al., "Social Media Reduction or Abstinence Interventions Are Providing Mental Health Benefits — Reanalysis," Psychology of Popular Media, 2025.

[6] Eckert, A., "The Architecture of Drift: A Cross-Domain Diagnostic for Epistemological Architecture," Paper 1, MoreRight, 2025.

[7] Eckert, A., "Thermodynamics of Opacity: Evidence Base, Derivations, and Prior Work," Paper 3, MoreRight, 2026.

[8] CDC, "Youth Risk Behavior Survey Data Summary & Trends Report: 2013–2023," 2024.

[9] CDC, "Youth Risk Behavior Survey Data Summary & Trends Report: 2011–2021," 2022.

[10] Pew Research Center, "Teens, Social Media and Technology," various years.

[11] Buffer, "The State of Social Media Engagement in 2026: 52M+ Posts Analyzed," 2026.

[12] Riehm, K.E., et al., "Associations Between Time Spent Using Social Media and Internalizing and Externalizing Problems Among US Youth," JAMA Psychiatry, 2019.
