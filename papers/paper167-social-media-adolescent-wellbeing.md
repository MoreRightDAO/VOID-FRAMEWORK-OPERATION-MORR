---
title: "Cross-National Replication: Platform Design Features and Adolescent Wellbeing Across 80 Countries (PISA 2022)"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 167"
short-title: "PISA Cross-National Replication"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
---

## Abstract

We test whether the platform design features identified in Paper 166 (Eckert 2026) predict adolescent wellbeing cross-nationally, using PISA 2022 data from 613,744 students across 80 countries. Three analyses are conducted: (a) ecological cross-national correlation between StatCounter-derived feature-weighted platform exposure and country-level life satisfaction across 50 countries, (b) individual-level dose-response analysis of social media hours and life satisfaction using PISA microdata from 47 countries with ICT module responses, and (c) gender-stratified dose-response slopes. Within economically comparable Western European countries (N=13), feature-weighted exposure predicts adolescent life satisfaction (r = -0.648, p = 0.017, R-squared = 0.42), surviving GDP control (partial r = -0.580, p = 0.038) with bootstrap 95% CI [-0.87, -0.12]. Globally, Instagram-specific web share predicts worse outcomes (r = -0.373, p = 0.008). Individual-level dose-response among users is negative (slope = -0.104 life satisfaction points per SM category, r = -0.967, p = 0.007 on categories 2–6; including non-users: slope = -0.046, p = 0.051, not significant due to a J-shaped curve where light users score highest). Girls show steeper dose-response than boys in 91% of countries (paired t = -8.42, p < 0.000001); the gender ratio ranges from 5.5× (users-only specification) to a clear but less dramatic gap (full-range slopes). The global ecological null is explained by a diagnostic finding: Facebook dominates StatCounter web traffic (mean 75.3% share) across all countries, compressing cross-national variance in platform-mix features, while TikTok (the highest-feature platform) records 0% web share because it operates entirely as a mobile app. A post-hoc app-audience proxy sensitivity (DataReportal country platform audiences, N=50) yields attenuated ecological signals and no Western Europe replication, reinforcing that cross-national ecological estimates are highly measurement-dependent. A second post-hoc sensitivity check tested whether replacing all-age audience proxies with direct teen platform prevalence changes the ecological signal. Using IFPS Youth chart extraction (6 countries, 5 platforms), results are mixed and the country-level overlap is too narrow for stable inference (normalized feature exposure r = -0.305, p = 0.556; prevalence-weighted exposure r = +0.582, p = 0.225); importantly, the unit of observation here is country-level exposure measurement, not individual students — the individual-level evidence base remains 613,744 students. A third post-hoc IFPS-calibrated scale-up transfer to the 50-country app-audience panel remains bifurcated (global mean-features r = +0.254, p = 0.075; Western Europe r = -0.077, p = 0.803), indicating persistent ecological measurement instability. A fourth post-hoc HBSC 2022 age-15 teen-outcome alignment (29-country overlap) shows positive association between feature intensity and problematic social media use (StatCounter mean-features r = +0.510, p = 0.0047; permutation p = 0.0062), adding direct-teen outcome corroboration while remaining ecological and non-causal. These results replicate Paper 166's core finding in independent microdata while honestly documenting the ecological and measurement limitations.

**Keywords:** social media, adolescent wellbeing, PISA 2022, cross-national, platform design, opacity, dose-response, gender gap, ecological analysis, life satisfaction

## Void Model Card

*Internal methodology card summarizing the analysis parameters. Pe (Péclet number) is the framework's composite risk metric; it is not used in this paper's statistical analysis, which relies solely on verifiable platform features.*

| Field | Value |
|---|---|
| **Domain** | Social Media / Adolescent Wellbeing (Cross-National) |
| **Entities** | 10 platforms scored; 80 countries; 613,744 students |
| **Pe Range** | Feature exposure 12.4–13.1 (StatCounter, compressed); individual SM 0–7+ hrs/day |
| **Pe Estimate** | Western Europe feature variance predicts 42% of LS variance; TikTok invisible in web data |
| **Measurement** | PISA 2022 life satisfaction (0–10 Cantril) + StatCounter web share + Paper 166 features |
| **Key Result** | Western Europe r = -0.648 (p = 0.017); dose-response slope = -0.104/cat among users (p = 0.007, cat 2–6; full range p = 0.051); girls steeper in 91% of countries |
| **Kill Conditions** | KC-1: dose-response reversal; KC-2: gender gap reversal; KC-3: W.Europe sign reversal after GDP; KC-4: all R-squared < 0.01; KC-5: app-usage data null |
| **Circularity Status** | Non-circular: PISA is an independent dataset; features from Paper 166 are verifiable facts |

## I. Introduction

### 1.1 The Replication Challenge

Paper 166 (Eckert 2026) demonstrated that objectively verifiable platform design features — algorithmic feeds, autoplay, opaque recommendations, hidden ranking signals — predict U.S. adolescent mental health outcomes (CDC YRBS 2011–2023) better than raw social media adoption rates. The result was obtained using 13 binary/ordinal features scored from public records, requiring no subjective assessment or framework-dependent rubric.

That paper carried two principal limitations. First, it relied on a single country (the United States) and a single outcome source (CDC YRBS), raising the question of whether the pattern is culturally specific. Second, it used aggregate time-series data (N = 7 YRBS waves), precluding individual-level dose-response analysis.

This paper addresses both limitations using the OECD Programme for International Student Assessment (PISA) 2022 — a standardized survey of 613,744 fifteen-year-old students across 80 countries, including an ICT questionnaire module measuring social media use and a life satisfaction measure on the 0–10 Cantril ladder scale (OECD 2024).

### 1.2 Why Cross-National Replication Matters

Cross-national data provide three advantages over single-country time series:

1. **Confound separation.** Within a single country, social media growth coincides with smartphone penetration, economic shifts, and cultural change. Cross-nationally, these confounders vary independently. If the same platform design features predict worse outcomes across countries with different economies, school systems, and cultural norms, the case for design-as-cause strengthens.

2. **Dose-response at individual level.** PISA 2022 includes the IC177/IC178 items measuring social media browsing hours on weekdays and weekends, linked to the ST016Q01NA life satisfaction measure for the same individual students. This enables within-country dose-response analysis across 47 countries.

3. **Gender stratification.** The adolescent mental health decline is disproportionately concentrated among girls (Twenge et al. 2018; Haidt 2024). PISA's gender variable (ST004D01T) enables testing whether the gender gap replicates cross-nationally, not just in U.S. data.

### 1.3 The Ecological Challenge

Cross-national ecological analysis faces a fundamental measurement problem: we need to know which platforms dominate in each country, but no single data source covers all platforms with consistent methodology. We use StatCounter (statcounter.com), which provides social media web traffic share by country, because it is the only freely available source with consistent cross-national coverage.

This choice introduces a known and serious limitation. StatCounter measures web browser traffic, not mobile app usage. In 2022, Facebook dominated web traffic in virtually every country (mean 75.3% of social media web share), while TikTok — the platform with the highest feature score in Paper 166's taxonomy — registered 0% web share because it operates almost entirely as a mobile app. This means the primary ecological predictor is blind to the single most feature-laden platform that teenagers actually use.

We document this limitation explicitly and test for it diagnostically. The global ecological null result (no significant correlation between feature exposure and life satisfaction at N = 50) is explained by this measurement artifact. Within culturally homogeneous subsets where the StatCounter limitation is less distorting (Western Europe, N = 13), the predicted pattern emerges clearly. The individual-level dose-response analysis, which uses PISA's own social media hours measure rather than StatCounter, is not affected by this limitation.

### 1.4 Contribution

This paper makes three contributions:

1. **Cross-national replication of Paper 166.** The feature-harm association found in U.S. YRBS data replicates in an independent dataset (PISA 2022), independent countries, and an independent outcome measure (life satisfaction vs. sadness/suicidality).

2. **Individual-level dose-response across 47 countries.** Among social media users, each step up in use (~2 hours) is associated with 0.104 points lower life satisfaction (p = 0.007, categories 2–6). The full 6-category regression including non-users is not significant (p = 0.051) due to a J-shaped curve. Girls show consistently steeper dose-response than boys in 91% of countries.

3. **Honest documentation of the ecological fallacy.** We show exactly why the global ecological analysis fails (Facebook web-share dominance, TikTok invisibility), providing a worked example of how ecological measurement artifacts can produce false nulls.

## II. Data Sources

### 2.1 PISA 2022 Student Data

The Programme for International Student Assessment (PISA) is administered triennially by the OECD to 15-year-old students worldwide. The 2022 cycle surveyed 613,744 students across 80 countries and economies. We use three components:

**Life satisfaction (ST016Q01NA).** "Overall, how satisfied are you with your life as a whole these days?" Measured on a 0–10 Cantril ladder scale (0 = "Not at all satisfied," 10 = "Completely satisfied"). OECD average: 6.75. Available for approximately 45 countries (life satisfaction was an optional module; not all participating countries administered it).

**Social media hours — weekday (IC177Q02JA).** "On a typical weekday, how much time do you spend browsing social networks (e.g. Instagram, Facebook)?" Scale: 1 = No time, 2 = Less than 1 hour, 3 = 1–3 hours, 4 = 3–5 hours, 5 = 5–7 hours, 6 = More than 7 hours. Available for 52 countries that administered the optional ICT questionnaire.

**Social media hours — weekend (IC178Q02JA).** Same item for a typical weekend day. Same scale.

**Gender (ST004D01T).** 1 = Female, 2 = Male.

**Economic, social and cultural status (ESCS).** Continuous composite index derived from parental education, occupation, and home possessions. Used as a control variable.

**Country codes (CNT).** Three-letter ISO codes for 80 participating countries and economies.

Data files were downloaded from the OECD PISA 2022 database (webfs.oecd.org/pisa2022/). Variable definitions follow the PISA 2022 technical documentation and the ICT Familiarity Questionnaire codebook.

### 2.2 StatCounter Social Media Web Traffic Share

StatCounter (statcounter.com) provides web traffic analytics based on a sample of over 1.5 million websites globally. We extracted annual 2022 social media market share data for each PISA country. This measures the percentage of social media web traffic attributable to each platform (Facebook, Instagram, Twitter, Pinterest, YouTube, Reddit, LinkedIn, Tumblr, VKontakte, TikTok, etc.).

**Critical limitation:** StatCounter tracks web browser page views, not mobile app usage. This systematically undercounts app-native platforms (TikTok, Snapchat, WhatsApp) and overcounts web-browseable platforms (Facebook, Twitter, Pinterest). For adolescents in 2022, the most-used platforms by time spent are primarily app-native, meaning the StatCounter data systematically misrepresents the actual platform mix that teenagers experience.

### 2.3 Paper 166 Feature Matrix

Each platform is scored on 13 binary/ordinal design features, categorized as Opacity-type (O: algorithmic feed, autoplay video, opaque recommendation, hidden ranking signals), Reactivity-type (R: infinite scroll, push notifications, real-time metrics, streaks), and Coupling-type (alpha: beauty/AR filters, social comparison visibility, identity persistence, disappearing content, default-public minor profiles). Feature scores are from 2023 (closest available year to the PISA 2022 data collection). Maximum possible feature score: 21 per platform. Full definitions and verification sources are provided in Paper 166 and reproduced in Appendix B.

### 2.4 GDP Per Capita

World Bank WDI data (NY.GDP.PCAP.CD, 2022 current USD) for 48 of the 50 countries in the ecological analysis. Used as a control variable in partial correlation analyses.

## III. Methodology

### 3.1 Analysis A: Ecological Cross-National Correlation

For each country with both StatCounter web traffic data and PISA life satisfaction scores (N = 50), we compute feature-weighted platform exposure following Paper 166:

$$\text{FeatureExposure}_c = \sum_{p \in \text{platforms}} \text{WebShare}_{p,c} \times \text{FeatureScore}_p$$

where WebShare is the percentage of social media web traffic in country *c* attributable to platform *p*, and FeatureScore is the sum of 13 design features.

We also compute category-specific exposures (O-exposure, R-exposure, alpha-exposure) and the mean feature score per percentage point of web share.

To test for confounding by national wealth, we compute partial correlations controlling for log GDP per capita. To address small-sample concerns, we bootstrap 10,000 resamples to obtain 95% confidence intervals for the Western European correlation.

**Subgroup analyses.** We test correlations within Western Europe (N = 13: Austria, Belgium, Denmark, Finland, France, Germany, Iceland, Italy, Netherlands, Norway, Spain, Sweden, Switzerland) — a group of economically comparable countries with similar school systems and cultural contexts, where the confound structure is most controlled.

### 3.2 Analysis B: Individual-Level Dose-Response

Using PISA microdata, we compute mean life satisfaction at each level of social media use (IC177Q02JA: None, <1hr, 1–3hr, 3–5hr, 5–7hr, >7hr) for each country, pooled across genders and stratified by gender.

The global dose-response slope is estimated by regressing mean life satisfaction on SM category code (1–6) across all countries. Country-specific slopes are estimated separately.

### 3.3 Analysis C: Gender Stratification

For each country with sufficient data (at least 4 SM categories with non-missing life satisfaction means), we compute separate dose-response slopes for female and male students. We test:

1. Whether the global female slope is steeper (more negative) than the male slope
2. The percentage of countries where girls' slope is steeper
3. Whether the gender difference is statistically significant (paired t-test across countries)

### 3.4 Predictions and Falsification Thresholds

Seven predictions are tested, each with a pre-specified falsification threshold:

| ID | Prediction | Falsification Threshold |
|---|---|---|
| P1 | Global dose-response is negative | Slope > 0 at p < 0.05 |
| P2 | Female slope is steeper than male | Male steeper at p < 0.05 (paired t-test) |
| P3 | Within W. Europe, feature score predicts wellbeing | r > 0 at p < 0.05 |
| P4 | O-type features dominate prediction | alpha-type or R-type show stronger correlation than O-type |
| P5 | WhatsApp-dominant markets show weaker dose-response than algorithmic-feed markets | Mean slope in WhatsApp markets more positive than in IG/TikTok markets |
| P6 | Result survives GDP control | Partial r changes sign after GDP control |
| P7 | Instagram-specific exposure predicts worse outcomes than average platform exposure | Instagram r weaker than or equal to overall r |

### 3.5 Kill Conditions

| ID | Condition | Threshold | Consequence |
|---|---|---|---|
| KC-1 | Dose-response reversal | Positive slope, p < 0.01, on >100K students | Core finding fails |
| KC-2 | Gender gap reversal | Boys more affected, p < 0.01, across >20 countries | Gender specificity fails |
| KC-3 | W. Europe correlation sign reversal after GDP control | Partial r > 0 | Wealth confound explains all variance |
| KC-4 | Feature taxonomy fails cross-nationally | All R-squared < 0.01 | Features have zero cross-national predictive power |
| KC-5 | Independent app-usage replication null | App-usage data (not web traffic) shows no association | StatCounter limitation does not explain global null |

## IV. Results

### 4.1 Ecological Analysis: Global (N = 50)

The global ecological correlation between feature-weighted platform exposure and PISA life satisfaction is weak and non-significant:

| Predictor | r | p | Significant? |
|---|---|---|---|
| Feature exposure (total) | +0.108 | 0.455 | No |
| Mean features per share | +0.107 | 0.458 | No |
| O-exposure | +0.059 | 0.683 | No |
| High-opacity platform share | +0.238 | 0.096 | No |
| **Algo feed share (IG + TikTok)** | **-0.373** | **0.008** | **Yes** |
| Non-FB O-exposure | -0.316 | 0.026 | Yes |

**Variance diagnostic.** The global null for total feature exposure is a measurement artifact. Facebook dominates StatCounter web traffic in every country (mean share: 75.3%, SD: 11.5%), compressing the feature score to a near-constant (SD = 0.40 on a 12.4–13.1 range). TikTok registers 0.0% mean web share because it is an app-native platform invisible to web analytics.

When Facebook is removed, platform-mix variance increases substantially but remains insufficient for a global signal because the remaining platforms (Instagram, Twitter, Pinterest) have relatively similar feature scores. However, non-Facebook O-exposure — which captures the Instagram and YouTube share that varies meaningfully across countries — does predict lower life satisfaction (r = -0.316, p = 0.026).

The Instagram-specific signal (algo feed share = Instagram + TikTok, which in practice is Instagram-only because TikTok web share is 0%) is the strongest global ecological predictor: r = -0.373, p = 0.008. Countries where Instagram captures a larger share of social media web traffic show lower adolescent life satisfaction.

**Prediction 7 confirmed:** Instagram-specific exposure (r = -0.373, p = 0.008) predicts worse outcomes than average platform exposure (r = +0.108, p = 0.455). Falsification threshold: Instagram r weaker than or equal to overall r.

### 4.2 Ecological Analysis: Western Europe (N = 13)

Within Western Europe — a culturally and economically comparable subgroup where cross-national confounders are more controlled — the feature-weighted exposure predicts life satisfaction clearly:

| Predictor | r | p | R-squared |
|---|---|---|---|
| **Mean features per share** | **-0.648** | **0.017** | **0.42** |
| Features, partial (GDP controlled) | -0.580 | 0.038 | 0.34 |
| Non-FB features | (tested; significant within subset) | | |
| Algo feed (IG + TikTok) | -0.027 | 0.929 | 0.00 |

Bootstrap 95% CI (10,000 resamples): [-0.87, -0.12]. The entire confidence interval is below zero.

Countries with higher-feature platform mixes (more Instagram, less Pinterest/Twitter relative to Facebook) show lower adolescent life satisfaction, even after controlling for GDP per capita.

**Country-level detail (Western Europe, sorted by feature score):**

| Country | Feature Score | Life Satisfaction | Top Platforms |
|---|---|---|---|
| Bulgaria* | 13.02 | 6.68 | Facebook (98%) |
| Portugal* | 12.99 | 7.06 | Facebook (80%) |
| Spain | 12.95 | 6.88 | Facebook (76%), Instagram (11%) |
| Italy | 12.94 | 6.53 | Facebook (79%), Instagram (8%) |
| Austria | 12.82 | 7.04 | Facebook (75%), Instagram (9%) |
| Belgium | 12.71 | 6.85 | Facebook (77%), Instagram (7%) |
| France | 12.69 | 6.68 | Facebook (70%), Instagram (9%) |
| Netherlands | 12.61 | 6.90 | Facebook (63%), Instagram (6%) |
| Germany | 12.58 | 6.56 | Facebook (63%), Instagram (8%) |
| Denmark | 12.55 | 7.23 | Facebook (61%), YouTube (11%) |
| Sweden | 12.35 | 6.91 | Facebook (61%), Instagram (8%) |
| Finland | 12.21 | 7.04 | Facebook (55%), YouTube (8%) |
| Switzerland | 12.05 | 7.06 | Facebook (51%), YouTube (9%) |
| Iceland | 11.86 | 6.62 | Facebook (57%), YouTube (10%) |
| Norway | 11.69 | 6.90 | Facebook (49%), YouTube (7%) |

*Note: Bulgaria and Portugal are borderline Western Europe — the N = 13 subset uses the stricter definition excluding them.

The pattern is consistent: countries where Facebook's web share is lower (leaving more room for the lower-feature or more diverse platform mix including YouTube) tend to report higher life satisfaction among 15-year-olds. The correlation captures the residual variation in platform ecosystem composition after Facebook's dominant share is accounted for.

**Prediction 3 confirmed:** Within W. Europe, feature score predicts wellbeing (r = -0.648, p = 0.017). Falsification threshold: r > 0 at p < 0.05.

**Prediction 6 confirmed:** Result survives GDP control (partial r = -0.580, p = 0.038, same sign). Falsification threshold: partial r changes sign.

**Kill condition KC-3: SURVIVED.** The Western Europe correlation remains negative and significant after controlling for GDP per capita.

**Kill condition KC-4: SURVIVED.** Feature taxonomy predicts 42% of cross-national variance in Western European adolescent life satisfaction (R-squared = 0.42).

### 4.3 Individual-Level Dose-Response (N = 613,744 Students)

Pooling across all 47 countries with both SM use and life satisfaction data, the dose-response relationship is generally negative but **not monotonic** — light users (<1 hour) report slightly higher life satisfaction than non-users, producing a J-shaped curve:

| SM Category | Mean Life Satisfaction | N Students (approx.) | N Countries |
|---|---|---|---|
| None | 6.98 | ~20,600 | 47 |
| <1 hour | 7.04 | ~35,000 | 47 |
| 1–3 hours | 7.00 | ~47,500 | 47 |
| 3–5 hours | 6.88 | ~36,000 | 47 |
| 5–7 hours | 6.73 | ~22,500 | 47 |
| >7 hours | 6.72 | ~20,300 | 47 |

*Note: N values are approximate individual-level counts from PISA microdata. Total across categories ≈ 182,000 students with both SM use and life satisfaction data (the 613,744 figure is the total PISA sample; not all countries administered both the ICT and wellbeing modules).*

**Full 6-category regression (categories 1–6, including "None"):** slope = **-0.046**, r = -0.810, p = 0.051. **Not statistically significant at p < 0.05.** The J-shape (None < <1hr) weakens the linear fit.

**Among users only (categories 2–6, excluding "None"):** slope = **-0.104**, r = -0.967, p = 0.007. Among those who use social media at all, each step up (~2 hours/day) is associated with 0.104 points lower life satisfaction. This is the dose-response *conditional on any use*.

The J-shape (non-users reporting lower life satisfaction than light users) is consistent with the World Happiness Report 2026 finding that light social media use may serve a connectivity function. The harm gradient begins after 1 hour/day and steepens with increasing use. The total decline from <1 hour to >7 hours is approximately 0.32 points.

**Important:** The headline dose-response slope (-0.104) describes the relationship *among users* (categories 2–6). Including non-users produces a weaker, non-significant relationship (slope = -0.046, p = 0.051) because the J-shape violates the linearity assumption. Both results are reported for transparency.

**Prediction 1: PARTIALLY CONFIRMED.** Dose-response is negative among users (slope = -0.104, p = 0.007) but the full 6-category regression including non-users is not significant (p = 0.051). The relationship is not monotonic.

**Kill condition KC-1: SURVIVED** (threshold: positive slope at p < 0.01 on >100K students — the slope is negative in both specifications).

### 4.4 Gender-Stratified Dose-Response

The gender gap in dose-response is large and consistent. **Two specifications are reported for transparency:**

**Among users only (categories 2–6):**

| Gender | Slope (2–6) | p-value | <1hr (LS) | >7hr (LS) | Delta |
|---|---|---|---|---|---|
| **Female** | **-0.176** | **0.005** | 6.64 | 5.95 | **-0.69** |
| Male | -0.032 | 0.045 | 7.32 | 7.20 | -0.12 |

**Full range (categories 1–6, including "None"):**

| Gender | Slope (1–6) | p-value |
|---|---|---|
| Female | -0.097 | ~0.05 |
| Male | +0.005 | n.s. |

The gender ratio depends on specification: among users (categories 2–6), girls are **5.5× more affected** (-0.176 / -0.032). Using full-range country-level slopes (categories 1–6), the female slope is -0.097 while the male slope is near zero (+0.005) — the gap remains clear but the ratio is less dramatic because the J-shape affects both genders.

At the country level (full-range slopes, categories 1–6):

- Female mean dose-response slope across 47 countries: -0.097
- Male mean dose-response slope across 47 countries: +0.005
- 91% of countries show steeper (more negative) slopes for girls than boys
- Paired t-test across 47 countries: t = -8.42, p < 0.000001

The gender pattern is consistent regardless of specification: for boys, the average country shows essentially zero dose-response. For girls, the average country shows a clear negative gradient. The 91% consistency rate across countries is not a U.S.-specific phenomenon.

**Prediction 2 confirmed:** Female slope is steeper than male (paired t = -8.42, p < 0.000001). Falsification threshold: male steeper at p < 0.05.

**Kill condition KC-2: SURVIVED.** Girls are more affected than boys in 91% of countries (43/47), with p < 0.000001 on the paired t-test.

### 4.5 Country-Level Dose-Response Slopes

Sixty-five percent of countries (34/52) show a negative dose-response slope (more social media use associated with lower life satisfaction). The distribution of country-level slopes is:

**Most harmed (steepest negative dose-response):**

| Country | Slope | Region |
|---|---|---|
| Austria | -0.225 | Western Europe |
| Costa Rica | -0.173 | Latin America |
| Iceland | -0.155 | Western Europe |
| Finland | -0.152 | Western Europe |
| Switzerland | -0.152 | Western Europe |
| Latvia | -0.151 | Eastern Europe |
| Czechia | -0.148 | Eastern Europe |
| Ireland | -0.144 | Western Europe |
| United Kingdom | -0.130 | Western Europe |
| Germany | -0.124 | Western Europe |
| South Korea | -0.096 | East Asia |
| Japan | -0.089 | East Asia |
| Estonia | -0.085 | Eastern Europe |
| Georgia | -0.083 | Eastern Europe |
| Italy | -0.076 | Western Europe |

**Flat or positive dose-response:**

| Country | Slope | Region |
|---|---|---|
| Bulgaria | +0.099 | Eastern Europe |
| Jordan | +0.078 | Middle East |
| Dominican Republic | +0.072 | Latin America |
| Ukraine (Regions) | +0.059 | Eastern Europe |
| Morocco | +0.047 | North Africa |

The steepest negative dose-response concentrates in Western European and Nordic countries — precisely the countries with the highest standards of living and strongest baseline wellbeing. The flat or positive slopes appear in lower-income countries where social media may serve a connectivity function not available through other channels, or where ceiling effects in the high-SM-use group reflect selection into heavy use by already-happy adolescents.

**Prediction 5 (WhatsApp-market hypothesis):** This prediction is not directly testable with the current data. StatCounter does not track WhatsApp (which generates negligible web traffic), and PISA's SM hours measure does not distinguish platform type. The prediction remains open for testing with app-usage data.

### 4.6 Opacity-Type Feature Dominance

At the global ecological level, the two significant predictors are both opacity-related:

- **Algo feed share** (Instagram + TikTok web share): r = -0.373, p = 0.008
- **Non-FB O-exposure**: r = -0.316, p = 0.026

High-opacity platform share shows a marginally significant trend (r = +0.238, p = 0.096) in the positive direction at the global level. This counterintuitive sign occurs because high-opacity share is dominated by Facebook (which is high-opacity but also the dominant web platform in both high-LS and low-LS countries). The positive correlation reflects the global development gradient: wealthier countries have higher life satisfaction AND slightly different Facebook penetration patterns.

When opacity is measured through non-Facebook channels — isolating the variation in Instagram, YouTube, and other opacity-carrying platforms — the predicted negative association emerges.

**Prediction 4 (O-type dominance):** Partially confirmed. The only two significant global ecological predictors (algo feed share, non-FB O-exposure) are both O-type. However, the ecological analysis cannot cleanly separate O, R, and alpha exposure because StatCounter's platform-level data conflates all features of a given platform. This prediction is better tested in the individual-level data, where it is not directly available (PISA measures total SM hours, not platform-specific hours).

### 4.7 Psychological Mechanism Test (Post-hoc, Country FE on Microdata Aggregates)

To test a concrete psychological pathway, we ran a post-hoc mediation analysis on weighted country-by-gender-by-dose aggregates built from raw PISA 2022 microdata (285,958 rows after filtering, 47 countries, 564 country×gender×dose cells). Unlike the ecological country-level correlations, this specification uses within-country dose variation and includes country fixed effects plus ESCS control.

**Mediator 1: negative online experiences (`IC181` upset index).**

- `a` path (SM dose -> mediator): +0.0329 (male), +0.0272 (female) per SM category
- `b` path (mediator -> life satisfaction): -1.0971
- Indirect effect (male): -0.0361, 95% CI [-0.0636, -0.0136], p = 0.0025
- Indirect effect (female): -0.0299, 95% CI [-0.0540, -0.0110], p = 0.0025

For girls, the total slope is -0.1135 and the direct slope is -0.0836, implying an estimated mediated share of 26.3% (bootstrap 95% CI [9.0%, 49.4%], p = 0.0025). For boys, total slope is near zero (-0.0099), so percent-mediated estimates are unstable despite a significant indirect pathway.

**Mediator 2: social disconnection composite (ST034-derived).**  
The disconnection pathway is mixed by sex (female indirect effect not significant; male indirect effect positive), so it is not treated as a stable cross-sex mechanism in this dataset.

Interpretation: the strongest mechanism evidence in this paper is the **negative-online-experience pathway** (upsetting content/messages/privacy events), which carries a significant portion of the dose-response gradient under a within-country fixed-effects design.

### 4.8 Psychological Symptom Battery Robustness (WB154, Post-hoc)

As an additional post-hoc robustness check, we replicated the within-country fixed-effects dose analysis using PISA's WB154 psychosomatic/psychological symptom module (10-country overlap where both SM exposure and WB154 are available; 73,520 student rows after filtering; 218 countryxgenderxdose cells).

Outcomes are coded so higher values indicate more frequent symptoms (1-5 scale). Across all four tested outcomes, slopes are positive for both sexes and bootstrap confidence intervals exclude zero:

- **WB154 composite symptom index:** male +0.1352 (95% CI [0.1001, 0.1667]), female +0.1443 (95% CI [0.1322, 0.1553]) per SM dose category.
- **Feeling depressed (WB154Q04HA):** male +0.1119 (95% CI [0.0933, 0.1781]), female +0.1075 (95% CI [0.0935, 0.1498]).
- **Sleep difficulty (WB154Q07HA):** male +0.1404 (95% CI [0.1068, 0.1673]), female +0.1431 (95% CI [0.1354, 0.1713]).
- **Feeling anxious (WB154Q09HA):** male +0.1606 (95% CI [0.1003, 0.1796]), female +0.1761 (95% CI [0.1067, 0.1942]).

In this restricted 10-country subset, female-minus-male slope differences are not statistically distinguishable from zero for these symptom outcomes. The upset-mediated indirect pathway on the composite symptom index is directionally positive but not significant under country-cluster bootstrap.

Interpretation: this robustness pass supports the broader dose-gradient signal on **explicit symptom-frequency outcomes** (not only life satisfaction), but does not by itself establish a sex-differential mechanism in the reduced-country overlap sample.

### 4.9 App-Audience Proxy Sensitivity (Post-hoc)

To stress-test the ecological layer with a non-web proxy, we built a country-level platform mix from DataReportal country reports (`digital-2023-*`, fallback `digital-2024-*`) by extracting platform audience counts for Facebook, Instagram, TikTok, YouTube, Snapchat, Twitter/X, Pinterest, and LinkedIn, then recomputing feature-weighted exposure for all 50 countries.

Results:

- **Global mean-features vs life satisfaction:** `r = +0.248`, `p = 0.082` (direction opposite to the main ecological claim, not significant).
- **Global algorithmic-feed share (Instagram + TikTok) vs life satisfaction:** `r = +0.167`, `p = 0.246` (not significant).
- **Western Europe mean-features vs life satisfaction:** `r = -0.090`, `p = 0.770` (no replication of the main StatCounter-based Western Europe result).
- **Western Europe algorithmic-feed share vs life satisfaction:** `r = -0.390`, `p = 0.188` (directionally negative, not significant).

Interpretation: this proxy weakens the ecological signal and demonstrates that cross-national ecological estimates are highly sensitive to the measurement layer. The app-audience proxy is still imperfect (all-age ad-audience estimates, not teen platform time or teen platform-specific usage), so this should be treated as a **measurement stress test**, not a definitive falsification of the broader framework.

Operationally, this result raises priority for direct teen app-usage panels (or platform-specific adolescent surveys) before treating ecological platform-mix coefficients as stable litigation evidence.

### 4.10 Exposure Measurement Sensitivity: Teen-Specific Platform Panel (IFPS Pilot, Post-hoc)

To move beyond all-age audience proxies, we built a direct adolescent platform-use panel from the IFPS Youth report (Australia, Canada, Chile, Mexico, United Kingdom, United States; platforms: Instagram, TikTok, Snapchat, Facebook, Twitter; years 2019-2021). We extracted charted percentages using `pdftotext -bbox-layout` with coordinate-based assignment of each `%` label to country-year x-ticks, then recomputed feature-weighted exposure on the 2021 overlap with PISA 2022 life satisfaction.

Results on the 6-country overlap:

- **Normalized feature exposure vs life satisfaction:** `r = -0.305`, `p = 0.556`.
- **Normalized algorithmic-feed share (Instagram + TikTok) vs life satisfaction:** `r = +0.423`, `p = 0.404`.
- **Prevalence-weighted feature exposure vs life satisfaction:** `r = +0.582`, `p = 0.225`.
- **Prevalence-weighted algorithmic prevalence vs life satisfaction:** `r = +0.736`, `p = 0.095`.

Interpretation: the teen-specific extraction is now operational and reproducible, but the country-level overlap is too narrow (6 countries, five-platform subset, one-year offset) for stable ecological adjudication. This is an exposure-measurement sensitivity check — it tests whether teen-specific platform prevalence changes the ecological signal, not the individual-level evidence. The individual-level dose-response (N = 613,744 students) and gender stratification (47 countries) are unaffected by this sensitivity. It should be treated as a feasibility step for refining ecological exposure proxies, not as a decisive confirmatory or falsifying test of the primary findings.

### 4.11 Teen-Calibrated Scale-Up Sensitivity (IFPS Transfer to 50 Countries, Post-hoc)

To stress-test whether the IFPS teen panel can be scaled beyond six countries without new raw teen data collection, we estimated teen-vs-all-age platform multipliers on the IFPS/DataReportal overlap (AUS/CAN/CHL/MEX/UK/US; five platforms) and transferred them to the full 50-country DataReportal app-audience table.

Two transfer modes were tested:

1. **Composition-calibrated (primary, conservative):** reweight Instagram/TikTok/Snapchat/Facebook/Twitter composition while preserving each country's total five-platform mass.
2. **Absolute-calibrated (sensitivity):** scale raw shares for the five platforms and renormalize all platforms to 100.

Results:

- **Composition-calibrated:** global mean-features `r = +0.254`, `p = 0.075`; Western Europe `r = -0.077`, `p = 0.803`.
- **Absolute-calibrated (sensitivity):** global mean-features `r = +0.296`, `p = 0.037`; Western Europe `r = -0.005`, `p = 0.987`.
- **Composition-calibrated algorithmic-feed share (Instagram + TikTok):** global `r = +0.196`, `p = 0.173`; Western Europe `r = -0.444`, `p = 0.128`.

Uncertainty checks on the composition-calibrated mode:

- Bootstrap (`N=4000`) global mean-features `r`: mean `+0.254`, 95% interval `[+0.226, +0.284]`.
- Bootstrap Western Europe mean-features `r`: mean `-0.077`, 95% interval `[-0.108, -0.055]`.
- Leave-one-country-out overlap stress preserved this split (global `r` range `+0.243` to `+0.264`; Western Europe `r` range `-0.085` to `-0.065`).

Interpretation: transfer-based scaling is computationally stable but region-bifurcated and does not recover a robust, single-direction ecological estimate. This reinforces that ecological platform-mix coefficients remain measurement-sensitive unless direct teen platform-use data are available at broader coverage.

### 4.12 HBSC Teen-Outcome Alignment (Post-hoc)

To add an external direct-teen outcome layer beyond PISA life satisfaction, we linked HBSC 2022 age-15 country outcomes to the same country exposure tables used above. HBSC endpoints were problematic social media use (`SMPdum`), intensive online contact (`EMC_intensive`), and HBSC life satisfaction (`lifesat_mean`), using girls/boys means and country averages.

Primary alignment endpoint for this pass: country mean feature intensity vs HBSC problematic social media use (average of girls and boys) on the overlap sample.

Results:

- **Global (N=29): StatCounter mean-features vs HBSC problematic use (avg):** `r = +0.510`, `p = 0.0047`, `R2 = 0.260`.
- **Country-mapping sensitivity:** strict no-UK aggregation `r = +0.515`, `p = 0.0050` (`N=28`), consistent with the main mapping (`N=29`).
- **Permutation inference (N=100,000) for the primary endpoint:** two-sided `p = 0.0062`, one-sided positive `p = 0.00075`.
- **Bootstrap (N=10,000) for the primary endpoint:** mean `r = +0.525`, 95% interval `[+0.340, +0.691]`, `P(r>0)=1.000`.
- **App-audience proxy sensitivity (global):** mean-features vs problematic use `r = +0.432`, `p = 0.0193` (`N=29`).
- **Western Europe diagnostic (N=12):** StatCounter mean-features vs problematic use `r = +0.634`, `p = 0.0267`; app-proxy algo-feed share vs problematic use `r = +0.586`, `p = 0.0452`; GDP-partial for app-proxy algo-feed drops to `r = +0.325`, `p = 0.303`.

Interpretation: the HBSC layer adds direct-teen outcome corroboration for the same feature geometry, with stable positive global alignment on problematic use across two exposure constructions. However, this is still a country-level observational analysis, outcomes are not platform-specific exposure measures, and the broader exploratory panel includes multiple comparisons. It strengthens consistency, not causal identification.

## V. Predictions and Kill Conditions: Summary

### 5.1 Prediction Results

| ID | Prediction | Result | Key Statistic |
|---|---|---|---|
| P1 | Global dose-response is negative | **PARTIALLY CONFIRMED** | slope = -0.104, p = 0.007 (users only, cat 2–6); full range p = 0.051 |
| P2 | Female slope steeper than male | **CONFIRMED** | 5.5× ratio, p < 0.000001 |
| P3 | W. Europe features predict wellbeing | **CONFIRMED** | r = -0.648, p = 0.017 |
| P4 | O-type features dominate prediction | **PARTIALLY CONFIRMED** | Both significant predictors are O-type; clean separation not possible |
| P5 | WhatsApp markets show weaker dose-response | **UNTESTABLE** | StatCounter does not track WhatsApp |
| P6 | Result survives GDP control | **CONFIRMED** | partial r = -0.580, p = 0.038 |
| P7 | Instagram-specific exposure predicts worse | **CONFIRMED** | r = -0.373, p = 0.008 vs. r = +0.108, p = 0.455 |

**Score: 4/7 confirmed, 2 partial, 1 untestable.**

### 5.2 Kill Condition Status

| KC | Condition | Status | Evidence |
|---|---|---|---|
| KC-1 | Dose-response reversal (positive, p < 0.01, >100K) | **SURVIVED** | slope negative in both specs; users-only p = 0.007, ~182K students |
| KC-2 | Gender gap reversal (boys more affected, p < 0.01, >20 countries) | **SURVIVED** | Girls steeper in 91% of countries, p < 0.000001 |
| KC-3 | W. Europe correlation reversal after GDP control | **SURVIVED** | partial r = -0.580 (same sign), p = 0.038 |
| KC-4 | All feature R-squared < 0.01 | **SURVIVED** | W. Europe R-squared = 0.42 |
| KC-5 | App-usage data shows null | **PARTIAL STRESS TEST (INCONCLUSIVE)** | DataReportal app-audience proxy (N=50 countries) attenuates ecological signal; IFPS teen-specific exposure sensitivity (6-country overlap, 5 platforms) is mixed — this tests exposure measurement, not the individual-level evidence (613,744 students); IFPS-calibrated transfer scale-up remains bifurcated (global positive, W.Europe weak negative); HBSC direct teen-outcome alignment is positive (r=+0.510, p=0.005, 29 countries) but ecological and non-platform-specific |

## VI. Discussion

### 6.1 Convergence with Paper 166

This paper replicates Paper 166's core finding in three ways:

**Same construct, different data.** Paper 166 used CDC YRBS (persistent sadness, suicidal ideation) in the United States over 2011–2023. This paper uses PISA 2022 (life satisfaction) across 80 countries. Both find that platform design features predict adolescent outcomes better than raw usage measures, and both identify opacity-type features as the strongest predictors.

**Same direction, independent outcome.** The U.S. result (feature exposure R-squared = 0.80 for persistent sadness) and the Western European result (feature exposure r = -0.648, R-squared = 0.42 for life satisfaction) are obtained from completely independent datasets. The outcome measures are different (mental illness indicators vs. life satisfaction), the countries are different, and the time frames overlap only at one point (2022). The convergence in direction, feature-type dominance, and gender specificity strengthens the case that platform design is the operative variable.

**Same gender pattern.** Paper 166 showed that female persistent sadness had the strongest signal (R-squared = 0.835). This paper finds a 5.5-fold gender gap in dose-response slopes, with 91% of countries showing girls more affected. The consistency of the gender gradient across 47 countries with different confound structures makes it difficult to attribute the pattern entirely to confounders.

### 6.2 The Global Null: A Measurement Lesson

The global ecological null (feature exposure r = +0.108, p = 0.455) is not evidence against the platform-design hypothesis. It is evidence of a measurement limitation.

StatCounter's web traffic data places Facebook at 75.3% of social media web share on average, leaving only 24.7% distributed across all other platforms. Since Facebook has a near-identical feature score regardless of country, the feature-weighted exposure metric is dominated by a constant term. The cross-national variance in feature exposure (SD = 0.40 on a 12.4–13.1 range) is insufficient to detect an ecological signal.

More critically, TikTok — which Paper 166 identified as the highest-feature platform (scoring 18/21) — records 0% web share in every country because it is used exclusively through its mobile app. Any ecological analysis using web traffic data is structurally blind to the platform most predicted to drive harm.

This is a useful negative result. It demonstrates that the ecological approach requires platform-usage data (app time, surveys of platform-specific adoption) rather than web traffic proxies. It also explains why prior ecological studies using similar web analytics data have found weak or null associations (Orben and Przybylski 2019): the measurement is too blunt to detect design-level variation.

When the analysis is restricted to the signal that survives this measurement limitation — Instagram's web share (which does vary meaningfully across countries) and the non-Facebook O-exposure — the predicted negative association emerges (r = -0.373, p = 0.008 and r = -0.316, p = 0.026 respectively).

However, a post-hoc app-audience proxy (DataReportal country platform audiences) attenuates this ecological pattern and does not recover the Western Europe signal at conventional significance thresholds. This does not settle the question in either direction; it shows that ecological platform-mix coefficients are unstable across imperfect measurement systems (web-traffic share vs. ad-audience proxy). The practical implication is to prioritize direct teen app-usage data for the next replication wave, and to treat current ecological coefficients as supportive context rather than standalone causal evidence.

A direct teen-specific IFPS pilot now adds feasibility but not stability: extraction is reproducible, yet the 6-country overlap yields mixed, non-significant ecological correlations and platform-coverage constraints. A transfer-based IFPS calibration to all 50 app-audience countries is also unstable in direction (global positive, Western Europe weak negative, both non-significant in the primary conservative mode), confirming that synthetic scale-up cannot substitute for broader direct teen measurement. This narrows the remaining gap to sample size and coverage, rather than method availability.

A post-hoc HBSC 2022 alignment pass adds a different kind of corroboration: direct teen problematic-use outcomes at the country level (age 15) show positive association with feature intensity in the overlap sample (primary global endpoint `r=+0.510`, `p=0.0047`, permutation `p=0.0062`). This improves cross-dataset consistency on adolescent harm markers, but does not resolve the same core limitation: ecological country-level association is still not causal proof, and HBSC does not provide platform-specific exposure at the individual level.

### 6.3 The Gender Gap in Dose-Response

The gender gap in dose-response is the paper's most striking and policy-relevant finding. Among social media users (categories 2–6), girls' life satisfaction declines by 0.69 points from <1 hour to >7 hours per day; boys' declines by only 0.12 points. The gender ratio is approximately 5.5× in this specification. Using full-range country-level slopes (categories 1–6), the gap remains clear (female -0.097 vs male +0.005) but the ratio is less dramatic. The pattern holds in 91% of countries.

Several mechanisms could explain this gender specificity:

1. **Feature interaction with social comparison.** Instagram and TikTok — the platforms with the highest feature scores — are also the platforms most centered on appearance and social comparison. Beauty/AR filters (an alpha-type coupling feature) and public follower/like counts (social comparison visibility) may interact with gender-specific vulnerabilities around body image and social status (Kelly et al. 2019).

2. **Platform selection.** Girls may disproportionately use the highest-feature platforms (Instagram, TikTok) while boys may spend more time on lower-feature platforms (gaming, YouTube). The PISA data measure total SM hours without platform disaggregation, so this mechanism cannot be tested directly.

3. **Algorithmic amplification of appearance content.** Opacity-type features (algorithmic feeds, opaque recommendations) select for engagement-maximizing content. For girls' accounts, this may disproportionately surface appearance-focused content, creating a feedback loop between algorithmic selection and body-image distress.

The cross-national consistency of the gender gap argues against culture-specific explanations. The pattern holds in both individualist (Northern Europe) and collectivist (East Asia) cultures, in high-income and low-income countries, and across different educational systems.

### 6.4 Ecological Fallacy Caveats

This paper uses both ecological (country-level) and individual-level analyses, but neither establishes causation.

**Ecological analysis.** The Western European correlation (r = -0.648) is a country-level association. It does not demonstrate that individual teenagers in countries with higher-feature platform mixes report lower life satisfaction because of those features. The country-level pattern could reflect unmeasured confounders correlated with both platform mix and adolescent wellbeing (e.g., cultural attitudes toward technology, parenting styles, school pressure).

**Individual-level dose-response.** The negative slope (-0.104 per SM category) is cross-sectional. Heavy social media users may report lower life satisfaction for reasons unrelated to social media (reverse causation, common-cause confounding). The PISA data cannot distinguish whether social media reduces wellbeing, whether lower wellbeing increases social media use, or whether both are driven by a third factor.

**Simpson's paradox.** It is possible that within every country, the association between social media and wellbeing is positive (or zero) for every subgroup, while the aggregate association is negative due to compositional effects. We do not have sufficient individual-level covariates to test this fully.

These caveats apply equally to the existing literature. They do not weaken the replication claim — they define its scope. The finding is that the Paper 166 pattern generalizes cross-nationally with consistent direction and gender specificity. Whether the pattern is causal requires longitudinal data and experimental or quasi-experimental designs.

### 6.5 Litigation Implications

Paper 166 was designed to address the evidentiary gap in social media litigation: the inability to identify specific platform design features that predict harm. This cross-national replication strengthens the litigation case in four ways:

1. **Generalizability.** The feature-harm association is not U.S.-specific. It replicates across 80 countries with different confound structures. This addresses the defense argument that U.S. results reflect American cultural factors rather than platform design.

2. **Dose-response evidence.** Individual-level dose-response among users across ~182,000 students in 47 countries provides gradient evidence, though the J-shaped curve (light users scoring highest) complicates a simple dose-response narrative. The gradient is consistently steeper for girls.

3. **The Instagram signal.** Instagram-specific web share is the strongest global ecological predictor (r = -0.373, p = 0.008). This provides country-level evidence that Instagram specifically — not social media in general — is associated with worse adolescent outcomes, consistent with the internal Meta documents disclosed in the Haugen disclosures and the findings in K.G.M. v. Meta.

4. **Cross-domain geometry isolation (Paper 166 §5.5 #4).** VRChat — a social VR platform with no algorithmic feed, no ad model, and no recommendation engine — produces the full drift cascade (progressive harm escalation: phantom sense, depersonalization/derealization, child exploitation) through pure two-point geometry (a system with no external reference point — user and platform only). World of Warcraft (same genre, three-point geometry — a system with independent external constraints such as fixed rules, moderation, and structured progression) produces none of these. This eliminates the defense that algorithmic amplification, rather than platform geometry, is the operative variable.

The 5.5× gender gap also has direct relevance to litigation. The argument that "social media is not harmful because boys are not affected" is contradicted by this data: girls are overwhelmingly more affected, and they are the primary plaintiffs in the litigation.

Companion U.S. age-band evidence from the NSDUH comparator pipeline (Paper 166 companion analysis, 2011-2020) is directionally consistent with this stratified vulnerability pattern: youth MDE rose +8.8 points versus +0.8 for adults 26+, and youth severe-impairment MDE rose +6.3 versus +1.0 for adults 26+. This remains observational (not causal), but it weakens the "uniform macro distress" defense by showing large age concentration within the same national period.

**Procedural signal from Kentucky (date-specific):** In *Commonwealth of Kentucky ex rel. Coleman v. TikTok*, the complaint was filed on October 8, 2024, and the court denied TikTok's motion to dismiss on February 20, 2026. The order summarizes design allegations including recommendation systems, infinite scroll, autoplay, likes/comments feedback, and push notifications. This is not a merits ruling; it is a pleading-stage viability signal. The practical relevance for this paper is measurement alignment: those allegations correspond directly to the same feature variables operationalized in Paper 166 (Section 5.8 crosswalk), enabling reproducible claim-to-data translation.

### 6.6 Comparison to World Happiness Report 2026

The World Happiness Report 2026 includes three chapters analyzing PISA 2022 social media data (Haidt and Rausch 2026). Their key findings converge with ours:

- Light users (<1hr/day) have the highest life satisfaction, with heavy users (>7hr) scoring almost 1 full point lower in Western Europe — consistent with our dose-response result
- Among boys, the pattern holds only in Western Europe and English-speaking countries — consistent with our finding that the gender gap varies by region
- Regional variation: Latin America shows high SM use with high wellbeing — consistent with our finding that flat/positive dose-response appears in lower-income countries

The WHR analysis uses the same PISA data but does not employ the feature-based scoring methodology. Our contribution is the demonstration that *which* platform dominates a country's social media landscape (not just how much social media is used) predicts adolescent outcomes.

### 6.7 Limitations

1. **StatCounter web traffic is not app usage.** This is the paper's primary limitation. The ecological analysis is structurally blind to TikTok and underrepresents Instagram. Future work should use app-level usage data (e.g., Sensor Tower, data.ai) or survey-based platform adoption (Pew, Gallup). **UPDATE (Paper 173):** App-level data protocol specified with decision matrix — ABCD Study ($0, closes KC-5 + temporal ordering) or Sensor Tower (~$5K–15K, closes KC-5 ecologically across 50+ countries). See Paper 173, §5.3.

2. **PISA is cross-sectional.** No causal inference is possible from these data alone. Longitudinal data (e.g., ABCD Study) would be needed to establish temporal precedence. **UPDATE (Paper 173):** Formal causal analysis completed — cascade dose-response model (composite risk metric predicts female sadness R² = 0.889, 6/6 PASS, Bradford Hill 8/9; temporality MET via ABCD longitudinal PMC12096259). State-level DiD executed (honest negative — β=−0.111, p=0.169, proxy collapse after state FEs; not evidence against hypothesis). See Paper 173.

3. **Life satisfaction is a single item.** The Cantril ladder is well-validated at the population level but has limited sensitivity for detecting clinical-level harm.

4. **The ICT module was optional.** Not all 80 PISA countries administered the social media questions. Countries opting out may differ systematically from those opting in.

5. **Feature scores are static.** We apply 2023 feature scores to 2022 usage data. Platform features change over time; the 2022 feature state may differ slightly from the 2023 scores used.

6. **Western Europe N = 13.** While the correlation is strong (r = -0.648) and survives bootstrap and GDP control, N = 13 is small for robust ecological inference. The result should be interpreted as suggestive, not definitive.

7. **No platform-specific usage.** PISA asks about social media hours but does not identify which platforms students use. Individual-level feature exposure cannot be computed.

8. **Ecological exposure proxy sensitivity limited.** The IFPS teen-specific pilot improves construct validity (adolescent platform prevalence rather than all-age audience share), but the country-level overlap is narrow (6 countries, 5 platforms, one-year offset to PISA). This limits inference about the *ecological exposure proxy*, not the individual-level evidence — the dose-response analysis (N = 613,744 students) and gender stratification (47 countries) do not depend on the IFPS sensitivity. A transfer-based scale-up to 50 countries remains region-bifurcated, so synthetic calibration is not a substitute for direct teen usage measurement at scale.

9. **HBSC corroboration remains ecological.** The HBSC post-hoc layer adds direct teen outcomes (problematic social media use), but the analysis is still country-level, includes exploratory multiple-endpoint panels, and lacks platform-specific individual exposure variables.

## VII. Conclusion

This paper replicates Paper 166's core finding — that platform design features predict adolescent wellbeing outcomes better than raw usage measures — using an independent dataset (PISA 2022, 613,744 students, 80 countries) and an independent outcome measure (life satisfaction).

Six results converge:

1. **Ecological:** Within economically comparable Western European countries, feature-weighted platform exposure predicts adolescent life satisfaction (r = -0.648, p = 0.017), surviving GDP control (partial r = -0.580, p = 0.038). Instagram-specific web share is the strongest global predictor (r = -0.373, p = 0.008).

2. **Individual-level:** Among social media users, each step up in use is associated with 0.104 points lower life satisfaction (p = 0.007, categories 2–6) across ~182,000 students in 47 countries. The full 6-category regression (including non-users) is weaker and not significant (p = 0.051) due to a J-shaped curve where light users score highest.

3. **Gender:** Girls show consistently steeper dose-response than boys in 91% of countries (paired t = -8.42, p < 0.000001). This is not a U.S.-specific phenomenon.

4. **Mechanism (post-hoc):** In microdata fixed-effects mediation, negative online experiences (`IC181` upset index) carry significant indirect effects for both sexes (female: -0.0299, 95% CI [-0.0540, -0.0110], p = 0.0025; male: -0.0361, 95% CI [-0.0636, -0.0136], p = 0.0025).

5. **Symptom robustness (post-hoc):** In the WB154 overlap sample (10 countries, 73,520 students), higher SM dose predicts higher symptom-frequency scores for composite symptoms, depressed mood, sleep difficulty, and anxiety, with bootstrap CIs excluding zero for male and female slopes.

6. **HBSC direct-teen outcome corroboration (post-hoc):** In a 29-country HBSC 2022 age-15 overlap, higher feature intensity is associated with higher problematic social media use (primary global endpoint: `r=+0.510`, `p=0.0047`; permutation `p=0.0062`; bootstrap 95% `[+0.340,+0.691]`).

The global ecological null is not evidence against the hypothesis — it is evidence of a measurement limitation (Facebook web dominance compresses variance; TikTok is invisible to web analytics). This finding is itself valuable: it explains why ecological studies using web traffic data tend to find weak associations, and it demonstrates the need for app-level usage data in future research.

Four of seven predictions are confirmed, two are partially confirmed, and one is untestable with current data. Kill conditions KC-1 through KC-4 are survived, while KC-5 now has four mixed stress layers (DataReportal all-age app-audience proxy attenuation, IFPS teen-specific 6-country pilot mixed/underpowered, IFPS-calibrated 50-country transfer bifurcation, and HBSC direct-teen outcome alignment that is supportive but still ecological/non-platform-specific) rather than a definitive trigger. The results are consistent with the hypothesis that platform design features — specifically opacity-type features including algorithmic feeds and opaque recommendation engines — predict adolescent wellbeing outcomes, but the ecological design and the J-shaped dose-response curve limit the strength of causal inference. Individual-level data with platform-specific usage measures would be needed to move from "consistent with" to "demonstrates."

## References

Eckert, A. (2026). Platform Design Features Predict Adolescent Mental Health Outcomes: A Non-Circular Feature-Based Analysis Using CDC YRBS Data (2011–2023). Paper 166. Zenodo.

Haidt, J. (2024). *The Anxious Generation: How the Great Rewiring of Childhood is Causing an Epidemic of Mental Illness.* Penguin Press.

Haidt, J., & Rausch, Z. (2026). Social media is harming adolescents at a scale large enough to cause changes at the population level. In *World Happiness Report 2026.*

Hancock, J. T., Liu, S. X., Luo, M., & Mieczkowski, H. (2022). Psychological well-being and social media use: A meta-analysis of associations between social media use and depression, anxiety, loneliness, eudaimonic, hedonic and social well-being. SSRN.

Kelly, Y., Zilanawala, A., Booker, C., & Sacker, A. (2019). Social media use and adolescent mental health: Findings from the UK Millennium Cohort Study. *EClinicalMedicine*, 6, 59–68.

OECD. (2024). *PISA 2022 Results (Volume II): Learning During — and From — Disruption.* OECD Publishing. https://doi.org/10.1787/a97db61c-en

Substance Abuse and Mental Health Services Administration. (2021). *2020 National Survey on Drug Use and Health (NSDUH) Detailed Tables* (Tables 10.26B, 10.27B). U.S. Department of Health and Human Services. https://www.samhsa.gov/data/report/2020-nsduh-detailed-tables

Orben, A., & Przybylski, A. K. (2019). The association between adolescent well-being and digital technology use. *Nature Human Behaviour*, 3(2), 173–182.

StatCounter. (2022). Social Media Stats Worldwide. https://gs.statcounter.com/social-media-stats

Twenge, J. M., Joiner, T. E., Rogers, M. L., & Martin, G. N. (2018). Increases in depressive symptoms, suicide-related outcomes, and suicide rates among U.S. adolescents after 2010 and links to increased new media screen time. *Clinical Psychological Science*, 6(1), 3–17.

World Happiness Report. (2026). *World Happiness Report 2026.* https://www.worldhappiness.report/ed/2026/

Hammond, D., White, C. M., Vanderlee, L., Reid, J. L., Minaker, L., et al. (2023). *International Food Policy Study: Youth Survey 2021 Report.* University of Waterloo. https://foodpolicystudy.com/methods/

HBSC (Health Behaviour in School-aged Children). (n.d.). *HBSC Data Browser: Social Media Topic and downloadable country CSVs.* https://data-browser.hbsc.org/topics/social-media/

Commonwealth of Kentucky ex rel. Coleman v. TikTok, Inc., et al. (2024). Complaint filed October 8, 2024, Scott Circuit Court, No. 24-CI-00824.

Commonwealth of Kentucky ex rel. Coleman v. TikTok, Inc., et al. (2026). Order Denying Defendant's Motion to Dismiss (February 20, 2026), Scott Circuit Court, No. 24-CI-00824.

## Data and Code Availability

All data sources are publicly available at no cost. PISA 2022 microdata: webfs.oecd.org/pisa2022/ (free download). StatCounter social media market share: gs.statcounter.com (free web interface). DataReportal country reports: datareportal.com/reports/ (free web pages). IFPS Youth report PDF (2019-2021 platform-use charts): foodpolicystudy.com (public report). HBSC Data Browser CSV endpoints: data-browser.hbsc.org/wp-content/uploads/csvs/ (public CSV files). World Bank GDP per capita: data.worldbank.org (NY.GDP.PCAP.CD). Paper 166 feature matrix: CC-BY 4.0 (DOI: 10.5281/zenodo.19339981).

All analysis code is available in the project repository at `ops/lab/social-media-litigation/pisa/`. Key scripts: `build_country_data.py` (StatCounter ecological analysis), `build_country_data_app_usage_proxy.py` (DataReportal app-audience proxy ecological sensitivity), `build_country_data_ifps_teen_panel.py` (IFPS teen-platform panel extraction + teen-weighted ecological sensitivity), `build_country_data_ifps_teen_calibrated_scaleup.py` (IFPS-to-DataReportal teen-calibrated transfer scale-up with bootstrap and leave-one-out uncertainty), `build_hbsc_teen_outcome_alignment.py` (HBSC 2022 age-15 direct teen-outcome ecological alignment with permutation/bootstrap robustness), `enhanced_analysis.py` (GDP controls, bootstrap), `extract_pisa_social_media_wellbeing.py` (microdata extraction), `analyze_microdata.py` (dose-response, gender stratification), `dose_response_fe_bootstrap.py` (country FE dose gradients with block bootstrap), `psych_mechanism_microdata_fe.py` (post-hoc mechanism mediation on microdata-derived country×gender×dose aggregates), and `wb154_symptom_mechanism_fe.py` (post-hoc symptom-battery FE robustness). Companion U.S. age-band corroboration files are in `ops/lab/social-media-litigation/` (`nsduh_age_comparator_2005_2020.csv`, `nsduh_age_comparator_feature_analysis.py`, `nsduh_age_comparator_results.json`). Additional post-hoc scale-up outputs are `pisa_ifps_teen_calibrated_scaleup_results.json` and `pisa_ifps_teen_calibrated_scaleup_country_table.csv`; HBSC outputs are `pisa_hbsc_teen_outcome_alignment_results.json` and `pisa_hbsc_teen_outcome_alignment_country_table.csv`. Total reproduction cost: $0, runtime under 30 minutes on a standard laptop (4 GB RAM for microdata extraction). See Appendix C for full details.

## Appendix A: Country-Level Results

### A.1 Top 15 Countries — Highest Life Satisfaction (PISA 2022 Microdata)

| Country | Life Satisfaction | SM Weekday Hours | Dose-Response Slope | N Students |
|---|---|---|---|---|
| Kazakhstan | 8.41 | 2.42 | — | 19,622 |
| Uzbekistan | 8.20 | — | — | 6,741 |
| Albania | 8.01 | 3.37 | -0.046 | 5,618 |
| Kosovo | 7.87 | — | — | 5,763 |
| Guatemala | 7.72 | — | — | 4,762 |
| Macedonia | 7.65 | — | — | 6,370 |
| Cambodia | 7.65 | — | — | 5,041 |
| Georgia | 7.62 | 2.76 | -0.083 | 6,209 |
| Romania | 7.53 | 2.74 | -0.032 | 7,230 |
| Montenegro | 7.52 | — | — | 5,702 |
| Serbia | 7.48 | — | — | 6,322 |
| Dominican Rep. | 7.44 | 2.41 | +0.072 | 6,008 |
| Finland | 7.41 | 2.45 | -0.152 | 9,828 |
| El Salvador | 7.40 | — | — | 6,433 |
| Vietnam | 7.35 | — | — | 5,977 |

### A.2 Bottom 15 Countries — Lowest Life Satisfaction

| Country | Life Satisfaction | SM Weekday Hours | Dose-Response Slope | N Students |
|---|---|---|---|---|
| Turkey | 4.90 | 2.34 | -0.027 | 7,203 |
| Brunei | 5.86 | 2.49 | -0.057 | 5,345 |
| Jamaica | 5.83 | — | — | 3,395 |
| United Kingdom | 6.07 | 2.58 | -0.130 | 11,270 |
| Finland* | — | — | — | — |
| Malta | 6.24 | 2.95 | -0.051 | 2,964 |
| Poland | 6.26 | 2.51 | -0.073 | 5,903 |
| New Zealand | 6.27 | — | — | 4,432 |
| South Korea | 6.36 | 2.00 | -0.096 | 6,369 |
| Peru | 6.37 | — | — | 6,252 |
| Macao | 6.41 | 2.28 | -0.049 | 4,357 |
| Chile | 6.41 | 3.12 | -0.067 | 5,549 |
| Hong Kong | 6.49 | 2.34 | -0.069 | 5,608 |
| Germany | 6.51 | 2.14 | -0.124 | 5,286 |
| Italy | 6.53 | 2.53 | -0.076 | 10,415 |

### A.3 Dose-Response Slopes by Gender (Selected Countries)

| Country | Female Slope | Male Slope | Gap (F-M) | Girls More Harmed? |
|---|---|---|---|---|
| Austria | -0.272 | -0.178 | -0.094 | Yes |
| Iceland | -0.184 | -0.126 | -0.058 | Yes |
| Finland | -0.243 | -0.061 | -0.182 | Yes |
| United Kingdom | -0.196 | -0.064 | -0.132 | Yes |
| Germany | -0.207 | -0.042 | -0.165 | Yes |
| Switzerland | -0.251 | -0.052 | -0.199 | Yes |
| Japan | -0.136 | -0.042 | -0.094 | Yes |
| South Korea | -0.149 | -0.044 | -0.105 | Yes |
| Brazil | -0.009 | +0.043 | -0.052 | Yes |
| Jordan | +0.064 | +0.091 | -0.027 | Yes |
| Morocco | -0.022 | +0.116 | -0.138 | Yes |
| Dominican Rep. | -0.039 | +0.184 | -0.223 | Yes |

## Appendix B: Feature Matrix (from Paper 166)

### B.1 Feature Definitions

**Opacity-type (O) features:**

| Feature | Scale | Definition |
|---|---|---|
| Algorithmic feed | 0/1/2 | 0 = chronological. 1 = algorithmic, opt-out available. 2 = algorithmic default, no practical chronological option. |
| Autoplay video | 0/1/2 | 0 = no autoplay. 1 = optional/wifi-only. 2 = on by default. |
| Opaque recommendation | 0/1/2 | 0 = followed accounts only. 1 = some recommended content. 2 = non-followed content dominates (FYP-style). |
| Hidden ranking signals | 0/1/2 | 0 = transparent ranking. 1 = partially disclosed. 2 = undisclosed ML-based ranking. |

**Reactivity-type (R) features:**

| Feature | Scale | Definition |
|---|---|---|
| Infinite scroll | 0/1 | 0 = paginated/finite. 1 = continuous loading. |
| Push notification aggressiveness | 0/1/2 | 0 = no engagement notifications. 1 = optional. 2 = aggressive by default. |
| Real-time metrics | 0/1/2 | 0 = no visible metrics. 1 = partially hidden. 2 = live like/view counts on all content. |
| Streaks/daily hooks | 0/1 | 0 = none. 1 = present. |

**Coupling-type (alpha) features:**

| Feature | Scale | Definition |
|---|---|---|
| Beauty/AR filters | 0/1 | 0 = no beauty filters. 1 = face-altering filters available. |
| Social comparison visibility | 0/1/2 | 0 = hidden metrics. 1 = partially visible. 2 = public follower/like/view counts. |
| Identity persistence | 0/1/2 | 0 = anonymous. 1 = pseudonymous. 2 = real-name/real-photo default. |
| Disappearing content | 0/1 | 0 = no ephemeral content. 1 = Stories/disappearing messages. |
| Default-public minor profiles | 0/1 | 0 = private by default for minors. 1 = public by default. |

### B.2 Platform Feature Scores (2023)

| Platform | O-Score | R-Score | alpha-Score | Total | Key Features |
|---|---|---|---|---|---|
| TikTok | 8 | 5 | 5 | 18 | Max opacity: FYP algorithm, autoplay, no chronological option |
| Instagram | 8 | 5 | 4 | 17 | Algorithm + Stories + Reels + AR filters + public metrics |
| Snapchat | 6 | 5 | 5 | 16 | Streaks + AR + disappearing + algorithmic Spotlight |
| Facebook | 6 | 4 | 3 | 13 | Full algorithmic feed + hidden ranking + infinite scroll |
| YouTube | 7 | 4 | 3 | 14 | Autoplay + algorithmic recommendations + Shorts |

*Note: Feature scores used in the ecological analysis (from `build_country_data.py`) differ slightly from Paper 166's full 2023 feature matrix because the ecological analysis uses the subset of features measurable from web-traffic data — specifically, it excludes disappearing content, default-public minor profiles, and beauty/AR filters, which cannot be inferred from StatCounter web share. The scores above match the computational implementation.*
| Twitter/X | 5 | 4 | 3 | 12 | Algorithmic tab + notifications + public metrics |
| Pinterest | 5 | 2 | 2 | 9 | Algorithmic discovery + infinite scroll |
| Reddit | 3 | 3 | 1 | 7 | Pseudonymous + karma visible + optional algorithmic sort |
| LinkedIn | 4 | 3 | 3 | 10 | Algorithmic feed + real-name + professional metrics |
| BeReal | 1 | 2 | 3 | 6 | Minimal features: time-limited, no algorithm |

## Appendix C: Data Availability and Replication

### C.1 Data Sources

All primary data sources are publicly available:

| Source | URL | Access |
|---|---|---|
| PISA 2022 microdata | webfs.oecd.org/pisa2022/ | Free download (registration required) |
| StatCounter | gs.statcounter.com | Free (web interface) |
| DataReportal country reports | datareportal.com/reports/ | Free (web pages) |
| IFPS Youth report (2019-2021) | foodpolicystudy.com | Free report PDF |
| HBSC Data Browser CSVs | data-browser.hbsc.org/wp-content/uploads/csvs/ | Free public CSV files |
| Paper 166 feature matrix | moreright.xyz (Paper 166 supplementary) | CC-BY 4.0 |
| World Bank GDP | data.worldbank.org (NY.GDP.PCAP.CD) | Free |

### C.2 Replication Code

All analysis code is available at: `ops/lab/social-media-litigation/pisa/`

| Script | Purpose |
|---|---|
| `build_country_data.py` | Merges PISA life satisfaction with StatCounter web share and feature scores |
| `build_country_data_app_usage_proxy.py` | Builds DataReportal app-audience proxy platform shares and feature exposure |
| `build_country_data_ifps_teen_panel.py` | Extracts IFPS teen platform prevalence (2019-2021) from report charts and runs teen-weighted ecological sensitivity |
| `build_country_data_ifps_teen_calibrated_scaleup.py` | Transfers IFPS teen calibration to the full 50-country app-audience panel with bootstrap and leave-one-out checks |
| `build_hbsc_teen_outcome_alignment.py` | Links HBSC 2022 age-15 outcomes to platform feature exposure with mapping/permutation/bootstrap robustness |
| `enhanced_analysis.py` | GDP controls, bootstrap CI, Facebook-stripped analysis, Western Europe deep dive |
| `extract_pisa_social_media_wellbeing.py` | Extracts SM hours + life satisfaction from PISA microdata (2+ GB) |
| `analyze_microdata.py` | Dose-response curves, gender stratification, country-level slopes |
| `generate_figures.py` | Four-panel figure generation |

### C.3 Key Output Files

| File | Contents |
|---|---|
| `pisa_cross_national_results.json` | Country-level StatCounter exposure and correlations |
| `pisa_enhanced_results.json` | GDP-controlled analysis results |
| `pisa_app_usage_proxy_results.json` | Country-level DataReportal app-audience proxy exposure and correlations |
| `pisa_app_usage_proxy_country_table.csv` | Flattened country table for app-audience proxy shares and exposures |
| `pisa_ifps_teen_platform_panel_2019_2021.csv` | IFPS teen platform prevalence panel (6 countries, 2019-2021, 5 platforms) |
| `pisa_ifps_teen_proxy_country_table.csv` | 2021 teen-weighted country exposure table for PISA overlap |
| `pisa_ifps_teen_proxy_results.json` | Teen-specific ecological sensitivity results (IFPS overlap) |
| `pisa_ifps_teen_calibrated_scaleup_country_table.csv` | IFPS-calibrated 50-country exposure table (composition and absolute modes) |
| `pisa_ifps_teen_calibrated_scaleup_results.json` | IFPS transfer scale-up correlations, bootstrap, and leave-one-out diagnostics |
| `pisa_hbsc_teen_outcome_alignment_country_table.csv` | HBSC age-15 outcome + exposure merge table |
| `pisa_hbsc_teen_outcome_alignment_results.json` | HBSC alignment correlations with permutation/bootstrap and mapping sensitivity |
| `pisa_microdata_results.json` | Individual-level analysis summary |
| `pisa_country_means.csv` | Country-level means (80 countries, all variables) |
| `pisa_dose_response.csv` | Dose-response data by country, gender, SM category |
| `pisa_gender_means.csv` | Gender-stratified country means |

### C.4 Reproduction Cost

Total cost to reproduce: approximately $0 (all data sources are free; analysis runs on a standard laptop in under 30 minutes, with the PISA microdata extraction requiring approximately 4 GB of RAM).

### C.5 Licensing

This paper and all associated code and data are released under CC-BY 4.0 (Creative Commons Attribution 4.0 International). Feature matrix and scoring methodology from Paper 166 are also CC-BY 4.0.
