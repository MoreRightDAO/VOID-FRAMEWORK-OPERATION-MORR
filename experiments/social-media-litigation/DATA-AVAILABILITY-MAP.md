# Social Media Litigation Data Availability Map

Date: 2026-04-01
Scope: U.S. adolescent mental-health trend evidence for Papers 166/167 and hostile-review support.

## What We Have (Directly in Repo)

| Dataset | Coverage | Unit | Key variables we use | Status |
|---|---|---|---|---|
| CDC YRBS trend tables | 2011-2023 (biennial) | U.S. national trend | persistent sadness, suicidality outcomes, sex splits | In repo (`yrbs-trend-data.csv`) |
| SAMHSA NSDUH adolescent MDE | 2004-2024 (annual; methodology break noted 2020/2021) | U.S. national trend | past-year MDE, MDE with severe impairment | In repo (`nsduh_adolescent_mde_2004_2024.csv`) |
| PISA 2022 | 2022 (single wave) | student/country cross-section | wellbeing and related indicators used in paper | In repo (`pisa/` artifacts) |
| Platform feature timeline | 2011-2023 (+ 2024 carry-forward assumption) | platform-year | algorithmic/engagement feature intensity + adoption weighting | In repo (`feature-matrix.json`) |

## What We Do NOT Have (Core Gap)

| Missing data object | Why it matters |
|---|---|
| Public U.S. individual-level panel that joins **platform-level feature exposure** to **clinical mental-health outcomes** over time | Needed for stronger causal identification and reduced ecological fallacy risk |
| Public nationwide dataset with user-level exposure to specific recommender/engagement design changes (autoplay/recommendation intensity) | Needed for direct treatment assignment instead of aggregate proxying |
| Consistent annual U.S. teen sadness/suicidality series with platform-usage linkage from pre-2011 onward | Needed to extend pre-trend diagnostics with directly linked exposure |

## What This Means Right Now

1. We **do** have strong trend data and timing-alignment data.
2. We **do not** have a public joined panel that can by itself deliver clean causal proof.
3. Current evidence is strongest as: structural timing + replication + hostile-witness internal admissions, with explicit non-causal limits.

## Immediate Next Acquisition Targets

1. State-level panels that can be linked to staggered feature/adoption ramp intensity.
2. Restricted-access microdata products with adolescent mental-health outcomes and digital-use measures in the same respondents.
3. Any regulator or litigation discovery datasets with internal experiment logs tied to engagement and youth harm markers.
