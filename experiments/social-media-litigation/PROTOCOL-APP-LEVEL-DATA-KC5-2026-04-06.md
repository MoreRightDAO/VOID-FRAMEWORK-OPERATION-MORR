# Protocol: App-Level Usage Data Acquisition (KC-5 Closure)

**Date:** 2026-04-06
**Status:** READY — awaiting data procurement decision
**Paper:** 173, §5.3 (Protocol C)
**Priority:** HIGH — closes the last open kill condition from Papers 166/167

---

## The Problem

Paper 167's ecological analysis uses StatCounter web traffic shares to proxy platform usage across 80 countries. This has a known measurement artifact:
- **TikTok: 0% web traffic share** (app-native platform, teens don't use TikTok in browsers)
- **Facebook: ~75% web traffic share** (overrepresented because older users browse Facebook on desktop)
- **Instagram/Snapchat: underrepresented** (primarily app-based teen usage)

KC-5 asks: would the ecological pattern hold with actual app-level teen usage data?

## Data Sources (Ranked)

### Option 1: Sensor Tower Academic License

**Cost:** ~$5K–15K/year
**Data:** App downloads, daily/monthly active users, usage time — by country, age demographic, device
**Coverage:** All major platforms (Instagram, TikTok, Snapchat, YouTube, Facebook, Discord, BeReal, WhatsApp)
**Countries:** 50+ (matching PISA coverage)
**Apply:** https://sensortower.com/contact (request academic pricing)

**Why it's the gold standard:** Direct measurement of teen app engagement, not web traffic proxy. Can compute feature exposure using actual teen-weighted app usage.

### Option 2: data.ai (formerly App Annie)

**Cost:** Similar to Sensor Tower
**Data:** App usage intelligence, similar metrics
**Apply:** https://www.data.ai/en/

### Option 3: ABCD Study (Free)

**Cost:** $0 (NIH-funded, requires institutional NDA)
**Data:** Platform-specific screen time at individual level, longitudinal (age 9–14+)
**N:** ~12,000 US adolescents
**Apply:** https://nda.nih.gov/abcd
**Limitation:** US only; individual-level (not ecological), so analysis design differs from Paper 167

### Option 4: Gallup World Poll

**Cost:** Academic partnership required
**Data:** Platform-specific usage questions in some 2024+ waves
**Coverage:** 140+ countries
**Limitation:** Not all waves include social media questions; availability uncertain

## Analysis Plan (Sensor Tower / data.ai)

### Step 1: Compute App-Level Feature Exposure by Country

```python
# For each country c and platform p:
app_exposure_c = sum(
    feature_score[p] * teen_app_usage_share[p][c]
    for p in platforms
)
```

Replace StatCounter web traffic share with Sensor Tower teen app usage share.

### Step 2: Replicate Paper 167 Analysis A

Correlate app-level feature exposure with PISA 2022 life satisfaction across:
- All 50 countries (N = 50)
- Western Europe subset (N = 13)
- With and without GDP control

### Step 3: Compare Web vs App Exposure

| Metric | StatCounter (web) | Sensor Tower (app) |
|--------|-------------------|-------------------|
| Global r | Paper 167 result | New result |
| W. Europe r | −0.648 | New result |
| TikTok contribution | 0% | Actual |
| Facebook contribution | ~75% | Actual |

### Step 4: KC-5 Verdict

- If app-level r ≥ web-level r: **KC-5 KILLED permanently** — measurement artifact was attenuating signal
- If app-level r is significant but weaker: **KC-5 SURVIVED** — pattern holds but weaker
- If app-level r is null (p > 0.10): **KC-5 FIRED** — ecological pattern was measurement artifact

## Analysis Plan (ABCD Study)

Different design — individual-level, not ecological:

### Step 1: Classify Platforms by Feature Score

Using Paper 166 feature matrix, assign each platform a feature score. High-feature platforms (Instagram, TikTok, Snapchat) vs low-feature platforms (iMessage, email, educational apps).

### Step 2: Test Dose-Response

```python
# For each participant:
high_feature_time = time_on_instagram + time_on_tiktok + time_on_snapchat
low_feature_time = time_on_messaging + time_on_educational

# Model:
CBCL_internalizing ~ high_feature_time + low_feature_time + covariates
```

If β(high_feature) > β(low_feature): feature architecture matters at individual level, confirming the ecological pattern with individual data.

### Step 3: Longitudinal (Protocol B overlap)

Test temporal ordering: high_feature_time at T → CBCL at T+1, controlling for CBCL at T.

## Decision Matrix

| Budget | Recommended Path | Closes |
|--------|-----------------|--------|
| $0 | ABCD Study only | KC-5 (US, individual-level) + temporal ordering |
| $5K–15K | Sensor Tower + ABCD | KC-5 (ecological, 50+ countries) + temporal ordering |
| Partnership | Gallup + ABCD | KC-5 (140 countries) + temporal ordering |

**Minimum viable:** ABCD alone closes both KC-5 and the temporal ordering gap. Cost: $0, time: 2–4 weeks.

## Output Files

- `app_level_kc5_results.json`
- `app_level_kc5_analysis.py`
- `abcd_feature_doseresponse.py` (if ABCD path)
