# Additional Dataset Sources for Social Media / Mental Health Research
**Compiled:** 2026-03-30

## Priority Ranking (for feature-based platform scoring correlation)

### Tier 1 — High Value, Accessible

| Dataset | N | Platform-Specific? | Access | Key Value |
|---|---|---|---|---|
| **OECD PISA 2022** | 270K+ (47 countries) | Partial (SM category) | Free download: oecd.org/pisa | Cross-national SM hours → wellbeing. WHR 2026 used it. |
| **Hancock et al. (2022) effect sizes** | 200+ studies | Some platform-specific | Researchbox #683 | Coded effect sizes mappable to our scoring |
| **Pew 2022-2025 annual series** | ~1,300-1,500/year | YES (adoption rates) | Free account: pewinternet.org/datasets | Annual platform adoption + attitudes |

### Tier 2 — High Value, Access Restrictions

| Dataset | N | Platform-Specific? | Access | Key Value |
|---|---|---|---|---|
| **Gallup 2023 Teen Survey** | 1,591 teens + 6,643 parents | YES (7 platforms, hours/day) | Reports only (raw data restricted) | Only survey with platform-specific hours + mental health |
| **ABCD Study (NIH)** | 11,875 | No (total screen time) | NDA application: nda.nih.gov/abcd | Brain imaging + screen time + mental health, longitudinal |
| **UK Millennium Cohort Study** | 10,904 at age 14 | No | UK Data Service (free reg) | Longitudinal, dose-response established |

### Tier 3 — Moderate Value

| Dataset | N | Platform-Specific? | Access | Key Value |
|---|---|---|---|---|
| **Monitoring the Future** | 25K-50K/year | Limited | ICPSR (free) | 50-year series, some screen time since 2014 |
| **Understanding Society (UK)** | 19,734 households | No | UK Data Service | Longitudinal, SM frequency scale |
| **Common Sense Census 2021** | 1,306 | Partial | Reports only | Time-diary methodology |
| **DSA Transparency Database** | All VLOPs | YES (per-platform) | Free Parquet | Content moderation, NOT engagement metrics |
| **KGM trial exhibits** | N/A | YES (IG, YT) | PACER/CourtListener | Design features found negligent by jury |

### Not Useful for Direct Correlation

| Dataset | Why Not |
|---|---|
| **NSDUH** | No social media questions at all |
| **Instagram internal research** | No structured public data (narrative slides only) |
| **Surgeon General advisory** | Synthesis only, no new data |

## Key URLs

- PISA 2022: https://www.oecd.org/en/data/datasets/pisa-2022-database.html
- Hancock et al.: https://researchbox.org/683
- Pew datasets: http://www.pewinternet.org/datasets/
- Gallup reports: https://news.gallup.com/poll/512576/teens-spend-average-hours-social-media-per-day.aspx
- ABCD Study: https://nida.nih.gov/research-topics/adolescent-brain/longitudinal-study-adolescent-brain-cognitive-development-abcd-study
- UK MCS: https://beta.ukdataservice.ac.uk/datacatalogue/series/series?id=2000031
- MTF: https://www.icpsr.umich.edu/web/NAHDAP/series/35
- Orben & Przybylski replication: https://osf.io/e84xu/
- Haidt/Twenge collaborative review: https://docs.google.com/document/d/1w-HOfseF2wF9YIpXwUUtP65-olnkPyWcgF5BiAtBEy0/edit
- DSA Transparency DB: https://transparency.dsa.ec.europa.eu/
- KGM v Meta: https://www.courtlistener.com/docket/69764041/kg-v-meta-platforms-inc/
- WHR 2026 SM chapter: https://www.worldhappiness.report/ed/2026/social-media-is-harming-adolescents-at-a-scale-large-enough-to-cause-changes-at-the-population-level/

## Next Steps

1. **Download PISA 2022 ICT + Wellbeing data** — test whether countries with higher adoption of high-opacity platforms show worse adolescent wellbeing
2. **Pull Hancock et al. effect sizes from Researchbox** — map studies to our platform feature scoring
3. **Request Pew 2022-2024 microdata** — platform-specific adoption by demographics for weighted analysis
4. **Apply for ABCD restricted data** — requires institutional affiliation (may need university partnership)
