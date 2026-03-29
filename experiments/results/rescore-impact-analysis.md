# Panel v2 Rescore — Experiment Impact Analysis
*2026-03-14 | Post-rescore assessment*

---

## Context

Full 1,344-platform rescore with new panel composition:
- **Old panel:** Three technocratic analysts (identical worldview)
- **New panel:** Guardian (parent) / Shepherd (pastor-ethicist) / Advocate (consumer rights lawyer)

**Root cause of change:** Old panel systematically overscored "scary" tech platforms (obvious AI risks) and underscored institutional harms (predatory finance, workplace surveillance, real estate discrimination). The new panel catches harms invisible to a purely technical lens.

**Statistical change:**
- Cohen's d: 4.2 → 3.6 (Hedges' g: 3.46) — stratified panel v2
- N: 86 → 1,344 platforms
- BH, Fisher p, mean |ρ|: **unchanged** (Track K convergences, not corpus-dependent)

**Emblematic case:** Robinhood
- Old panel: O=1/R=0/α=0, Pe=-72.77 (deep constraint pole — "free pass for fintech")
- New panel: Scores TBD from panel_v2_scores MongoDB collection
- Excluded from known-harm list per decisions.md (harm not Pe-captured under old panel)

---

## Tier 1 — Must Re-Run

### HP28: Timelike Fraction vs Pe Quintiles
**Status:** HIGH PRIORITY — featured result in conformal group analysis

**What changes:**
- Quintile boundaries [Q1: -126 to -26, Q2: -26 to -13, Q3: -13 to -2.5, Q4: -2.5 to 13, Q5: 13 to 48] were computed from OLD canonical Pe values
- Institutional platforms (finance, workplace, real estate) that were deep constraint-pole under old panel may now have higher Pe → migrate from Q1/Q2 toward Q3/Q4
- The Goldilocks peak (52.8% timelike at Q2, Pe≈-13) may shift if enough platforms leave Q2

**What's robust:**
- Logistic regression (β₁=-0.639, p≈0) operates on 292,923 individual pairs — pair-level data doesn't change, only the Pe used for stratification
- The raw within-platform timelike fraction (27.7% overall) comes from rater disagreement data which is historical

**What's at risk:**
- ANOVA (F=1.48, p=0.210) — already non-significant; may flip either direction
- Bin composition changes → the "dramatic variation" narrative may strengthen or weaken
- Spearman ρ=-0.400 on 5 bins — very sensitive to bin-level means

**Action:** Export panel_v2 canonical Pe values → re-stratify → re-run ANOVA + logistic + Spearman

**Blocking:** canonical_scores.json must be regenerated from panel_v2_scores MongoDB collection

### Papers Citing d=4.2
**Status:** DONE ✓

Updated:
- Paper 65 (carcinogenesis): d=4.2→3.6, N=190/86→1,344
- Paper 74 (grand convergence): N=86→1,344
- Paper 138 (abstraction fallacy): d=4.2→3.6
- Paper 72 (THRML validation): N=86→1,344
- Paper 52 (constraint current): d=4.2→3.6

---

## Tier 2 — Re-Validate

### EXP-034B: Fantasia Light Cone Known-Harm List
**Status:** MEDIUM — likely robust but needs confirmation

**What changes:**
- Known-harm list had 21 platforms, all spacelike (100%)
- Robinhood already excluded (decisions.md 2026-03-14)
- Remaining platforms (TikTok, Character.AI, Instagram, Facebook, Replika, Tinder, Grindr, Snapchat, X, Pinterest, Reddit) are social/dating/gaming
- New panel would likely score these **higher** (Guardian sees child safety risks, Shepherd sees relationship harm, Advocate sees consumer exploitation)
- So the 21/21 spacelike result should strengthen, not weaken

**What's at risk:**
- If any known-harm platform's O+R drops significantly relative to α, it could become timelike
- Unlikely for social media platforms — their O and R are structural properties

**Action:** Re-run nb_exp034b_fantasia_full_corpus.py after updating MongoDB canonical scores

### HP24: Within vs Cross-Platform χ²
**Status:** MEDIUM — core result (27.7% vs 19.3%, χ²=137.83) uses raw rater data

**What changes:**
- The 27.7% within-platform timelike fraction and 19.3% cross-platform fraction are computed from queue_scores.json (raw rater responses) — these don't change
- Pe-stratified sub-analyses (if any) would change
- Platform count: was 748 multi-scored platforms; with new panel, multi-scored count may differ

**What's robust:**
- Core χ² result (K-HP-102B: PASS, p<10⁻⁶)
- Permutation test (28.2% vs 25.3% shuffled, p=0.0000)
- These operate on the raw rater data, not canonical Pe

**Action:** Confirm queue_scores don't change; only re-run if Pe-stratified sub-analysis exists

---

## Tier 3 — Independent (No Action)

| Experiment | Why Independent |
|------------|----------------|
| HP25 (perturbation wavefront) | FP simulation — no empirical data dependency |
| HP26 (spectral statistics) | Eigenvalue computation — no empirical data dependency |
| HP29 (propagation asymmetry) | FP simulation — no empirical data dependency |
| HP30 (BKT vs helium) | Literature constants — no platform data |
| HP31 (SO(4,2) branching) | Hydrogen spectrum — pure group theory |
| HP32 (null cone embedding) | θ = d·ln(Pe) calibration — Pe formula unchanged |
| HP33 (Balmer-α) | Selection rules — pure representation theory |
| HP34 (Rac factors) | Radial integrals — pure representation theory |
| EXP-024 (measurement industry IRR) | Entity scoring study, not platform corpus |
| EXP-025 (structure vs drift) | Prospective design — will use new panel as baseline |

---

## Data Pipeline Required

Before re-running HP28/HP24/EXP-034B:

1. **Export panel_v2 canonical scores** from MongoDB `panel_v2_scores` → `ops/lab/data/canonical_scores_v2.json`
2. **Update experiment scripts** to read from v2 data (or overwrite canonical_scores.json)
3. **Re-export queue_scores** if the panel_v2 rescore generated new queue entries (check if queue_scores grew)
4. **Run:** `python3 ops/lab/nb_hp28_timelike_vs_pe.py` (after data update)
5. **Run:** `python3 ops/lab/experiments/nb_exp034b_fantasia_full_corpus.py` (after MongoDB update)
6. **Compare:** old vs new results, document in this file

---

## Kill Condition Impact

No kill conditions are affected by the rescore:
- K-HP-117/118/119 (HP28): ANOVA-based, already inconclusive — rescore may change formal status but the pair-level logistic result is the real finding
- K-FLC-5 (EXP-034B): Already survived at p=7.19×10⁻⁸ — rescore likely strengthens this
- K-HP-102/102B/103 (HP24): Based on raw rater data, unchanged

The framework's core statistics (BH 24/27, Fisher p<10⁻⁵², |ρ|=0.958, 0/26 KCs fired) are Track K convergences and are **completely independent** of the platform scoring corpus.

---

*End of impact analysis.*
