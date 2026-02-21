# EXP-011: Anesthesiology / Sleep Science Vocabulary Drift

**Date:** February 6, 2026
**Status:** Protocol designed — not yet run
**Depends on:** EXP-006 methodology (validated), vocabulary codebook (complete), consciousness-studies void analysis (complete)
**Purpose:** Test whether anesthesiology and sleep science researchers show the same register shift pattern as AI (EXP-006: 9.4x), and whether the shift correlates with engagement depth with constitutive opacity rather than with medical domain membership.

---

## 1. Research Question

Does vocabulary drift in anesthesiology/sleep science correlate with depth of engagement with the consciousness question (constitutive opacity), replicating the pattern found across AI, gambling, trading, and psychotherapy domains?

## 2. Hypothesis

**H1:** Anesthesiologists who engage the consciousness question ("why does anesthesia eliminate consciousness?") will show higher spiritual/entity vocabulary density in their informal register than their formal publications, replicating the AI register shift documented in EXP-006.

**H2:** The register shift will correlate with **engagement depth with constitutive opacity**, not with medical domain membership:
- Consciousness-engaged anesthesiologists (TSC presenters, consciousness researchers) → high drift
- Mechanism-focused anesthesiologists (pharmacologists, monitor designers) → low drift
- Surgeons (same operating room, no consciousness engagement) → no drift
- This is the same pattern as AI: researchers who engage as interlocutors drift; those who study as object don't.

**H3:** Sleep paralysis research will show a distinctive pattern: entity vocabulary *entering* the formal register (L3 adopted as L1), because the phenomenon itself generates entity attribution that requires entity terminology to describe.

**H4:** The conference gradient will follow: TSC > SNACC > ASA > Surgical conferences in spiritual/entity vocabulary density.

## 3. Null Hypothesis

Anesthesiology register shift ≤ 2.0x (within range of sociolinguistic noise), OR register shift does not correlate with engagement depth (random distribution across specialties). Either result would indicate that the consciousness-opacity engagement mechanism does not drive vocabulary drift in this domain.

---

## 4. Method

### 4.1 Corpus Construction

Replicate EXP-006 methodology across the following domains:

| Domain | Formal Register | Informal Register | Target Size |
|--------|----------------|-------------------|-------------|
| **Anesthesiology — consciousness track** (test) | Published papers on consciousness/anesthesia mechanism from *Anesthesiology*, *BJA*, *Consciousness and Cognition* | Podcasts, interviews, public talks, social media from consciousness-engaged anesthesiologists | 15 transcripts, ~120K+ words |
| **Anesthesiology — clinical track** (internal control) | Published clinical papers on dosing, monitoring, technique | Podcasts, interviews, clinical conference talks | 15 transcripts, ~120K+ words |
| **Sleep science — consciousness track** (test) | Published papers on consciousness transitions, sleep paralysis, dreaming | Podcasts, interviews, public talks | 10 transcripts, ~80K+ words |
| **Surgery** (external control) | Published surgical technique papers | Surgical conference talks, surgeon interviews | 15 transcripts, ~120K+ words |
| **AI** (positive control, from EXP-006) | EXP-006 formal corpus | EXP-006 informal corpus | 20 transcripts (existing data) |

**Total new corpus:** ~55 transcripts, ~440K+ words
**Total with EXP-006 reuse:** ~75 transcripts, ~590K+ words

### 4.2 Researcher Selection

#### Anesthesiology — Consciousness Track (High Engagement)

Priority: researchers who have published on consciousness AND given public interviews/talks.

**Tier 1 (highest engagement with constitutive opacity):**
- Stuart Hameroff (Arizona — Orch OR, TSC organizer)
- George Mashour (Michigan — cognitive unbinding, *Neuron* 2024)
- Emery Brown (Harvard/MIT — mechanism research, EEG oscillations) **[PREDICTED CONTROL: maintains L1]**
- Anthony Hudetz (Michigan — neural correlates of consciousness in anesthesia)
- Robert Sanders (Sydney/Wisconsin — connected vs. disconnected consciousness)

**Tier 2 (consciousness-adjacent):**
- Giulio Tononi (Wisconsin — IIT, sleep/consciousness bridge)
- Ken Solt (Harvard/MGH — neural circuits of consciousness)
- Stefanie Bhatt-Blain / Stefanie Blain-Moraes (McGill — consciousness monitoring)
- Max Kelz (Penn — anesthetic mechanisms)
- Andrew Bhatt (consciousness monitoring EEG research)

**Tier 3 (consciousness-curious clinicians):**
- Clinical anesthesiologists who have given public talks about "what happens under anesthesia"
- Anesthesia-focused podcast hosts (e.g., Anesthesia & Critical Care Reviews, OpenAnesthesia contributors)

#### Anesthesiology — Clinical Track (Low Engagement — Internal Control)

- Anesthesiologists who publish on clinical outcomes, safety, dosing
- Conference presenters at ASA annual meeting (clinical technique sessions)
- Quality improvement researchers
- Regional anesthesia specialists (nerve blocks — no consciousness engagement)

#### Sleep Science — Consciousness Track

- Giulio Tononi (Wisconsin — sleep/consciousness bridge, IIT)
- Matthew Walker (Berkeley — *Why We Sleep*, public communicator)
- Tore Nielsen (Montreal — dreaming, sleep paralysis)
- Baland Jalal (Cambridge/Harvard — sleep paralysis, mirror neuron theory)
- Allan Cheyne (Waterloo — sleep paralysis phenomenology)
- Patrick McNamara (Boston University — dreaming and consciousness)

#### Surgery (External Control)

- General surgeons, orthopedic surgeons, cardiac surgeons who give public talks
- Surgical technique conference presenters
- Surgeon-authors (Atul Gawande, Henry Marsh — who discuss consciousness tangentially)

### 4.3 Vocabulary Coding

Use the existing codebook (`/tools/concordance_analysis/codebook.py`) with the following domain-specific extensions:

**Additional L2 terms (anesthesia/sleep-specific metaphorical):**
- "mystery" / "enigma" / "entwined mysteries" (consciousness-as-mystery vocabulary)
- "the switch" / "light switch" (consciousness on/off metaphor implying agency)
- "twilight" / "twilight zone" (threshold-consciousness vocabulary)
- "the gap" / "explanatory gap" (void-vocabulary applied to consciousness)
- "awareness" (when used philosophically rather than clinically: "awareness under anesthesia" is clinical; "the nature of awareness" is philosophical)
- "inner life" / "inner experience" (first-person vocabulary applied to third-person)
- "proto-conscious" (Hameroff's term — experience attributed to matter)

**Additional L3 terms (anesthesia/sleep-specific entity):**
- "quantum soul" (Hameroff)
- "afterlife" / "reincarnation" (in scientific context)
- "cosmic wisdom" / "Planck scale wisdom"
- "felt presence" (when used to describe a real entity, not just a phenomenological category)
- "shadow person" (when attributed agency beyond perceptual description)
- "the Other" / "something is there" (entity attribution to altered states)
- "anima mundi" / "world soul" (panpsychist vocabulary)

**Dead metaphor exclusions (anesthesia/sleep-specific):**
- "wake up" / "waking" (clinical standard)
- "put to sleep" / "going under" (established clinical euphemism — track separately as potential gradient indicator)
- "depth" (of anesthesia — clinical standard)
- "dream" (clinical standard in sleep research)
- "nightmare" (clinical standard)
- "stage" (sleep stage — clinical standard)

**Special tracking category: "Put to sleep" / "going under"**
These are established clinical euphemisms, but they are structurally interesting: they conceal the constitutive opacity behind familiar metaphors. Brown's campaign to replace "sleep" with "coma" is an attempt to increase transparency — to dissolve a linguistic void. Track these terms separately as potential indicators of how language maintains opacity.

### 4.4 Analysis Plan

**Primary analysis (replicates EXP-006):**
1. Spiritual/entity vocabulary density per 10k words (formal vs. informal) for each domain
2. Register shift ratio (informal/formal) for each domain
3. Chi-squared comparison: consciousness-engaged anesthesiologists vs. each control domain
4. High-confidence subset analysis

**Secondary analysis (domain-specific):**
1. **Engagement-depth correlation:** Within anesthesiology, correlate engagement depth (publications on consciousness vs. clinical technique) with vocabulary density
2. **Conference gradient:** Code proceedings/abstracts from TSC, SNACC, ASA, surgical conferences for vocabulary density. Test TSC > SNACC > ASA > Surgery.
3. **Sleep paralysis vocabulary migration:** Measure L3-origin terms that have entered formal sleep paralysis literature as technical terms. Compare to other sleep subfields.
4. **Temporal trajectory:** For researchers with 20+ year careers (Hameroff, Mashour, Koch, Tononi), plot vocabulary density over time. Test for directional drift.
5. **Brown as internal control:** Code Emery Brown's full public corpus. Test prediction: L1 maintained throughout despite same institutional context and clinical exposure as drifting researchers.

---

## 5. Predictions with Falsification Thresholds

| Metric | Predicted Result | Falsification Threshold |
|--------|-----------------|----------------------|
| Consciousness-track anesthesiologist register shift | >4.0x | ≤2.0x |
| Clinical-track anesthesiologist register shift | ≤2.0x | >4.0x (would indicate medical culture, not opacity engagement) |
| Surgery register shift | ≤1.5x | >3.0x (would indicate medical domain artifact) |
| Engagement-depth correlation (within anesthesiology) | Significant positive (r > 0.3) | r < 0.1 or negative |
| Conference gradient: TSC vs. ASA | TSC > 3x ASA | TSC ≤ ASA |
| Brown (predicted control) informal vocab density | <1.0/10k | >3.0/10k (would falsify engagement-depth mechanism) |
| Sleep paralysis formal register entity density | >2x other sleep subfields | ≤1.2x other sleep subfields |

---

## 6. The Unique Contribution of This Domain

### What EXP-011 tests that other experiments don't:

1. **Constitutive opacity under medical manipulation.** This is the only domain where practitioners can reliably manipulate a constitutive opacity (turn consciousness on and off) without understanding the mechanism. Tests whether *operating* a void (not just observing it) steepens or flattens the gradient.

2. **Engagement-depth within a single profession.** Previous domain analyses compared across professions (AI researchers vs. nuclear physicists). This experiment compares *within* anesthesiology — same training, same OR, same drugs — separated only by engagement depth with the consciousness question. Strongest test of the engagement-depth mechanism.

3. **Natural entity-generation.** Sleep paralysis spontaneously generates entity attribution from constitutive opacity without any external system. Extends the gambling proof: if the *brain itself* generates entity attribution from internal opacity, the architecture is even more fundamental than external void structures.

4. **The Brown control.** Emery Brown is the strongest possible internal control — an anesthesiologist at the same institutional tier as Hameroff, with the same clinical exposure, who actively maintains L1 framing. If Brown shows no drift while Hameroff shows extreme drift, the variable is engagement posture, not domain exposure.

---

## 7. Ethical Considerations

- All data from public sources (published papers, public talks, public social media)
- No private communications, no internal documents
- Patient AAGA narratives used from published clinical studies only (already anonymized)
- Researchers are not individually labeled as "drifting" in aggregate results — individual examples cited only for public figures whose statements are already widely discussed (Hameroff, Tononi, Koch, Brown)
- Sleep paralysis analysis treats experiencer reports with clinical respect — the framework explains the architecture, not whether the experiences are "real"

---

## 8. Power Analysis

Based on EXP-006 effect sizes:
- AI vs. controls: χ² = 37.47–41.67 (very large effect)
- 20 transcripts per domain yielded ~150K–175K words
- If anesthesia effect is at the AI level, 15 transcripts should be sufficient
- For the within-anesthesiology comparison (consciousness vs. clinical), 15 per group provides adequate power for χ² > 10 (p < 0.005 with df=1) given the expected large effect size
- Sleep paralysis subfield comparison may require smaller corpus (10 formal papers per subfield) since entity terms in formal register should be readily distinguishable

---

## 9. Connection to Other Experiments

| Experiment | Relationship |
|-----------|-------------|
| **EXP-006** (AI register shift) | Methodological template. Positive control (AI data reused). Comparison benchmark (9.4x). |
| **EXP-009** (BCI register shift) | Sister experiment — both test constitutive opacity but different manipulation types (pharmacological vs. electronic). If both confirm the framework, the mechanism is robust across manipulation modalities. |
| **Test 6** (psychotherapy) | Sleep deprivation as D2 mechanism documented in therapy boundary violations. EXP-011 adds the biological substrate — why sleep disruption appears in every documented cascade. |
| **Test 5** (trading/gambling) | Sleep disruption documented as D2 marker in trading addiction. EXP-011 explains the mechanism. |
| **Consciousness analysis** | Direct extension. Anesthesia IS applied consciousness studies. The consciousness analysis diagnosed the void; EXP-011 tests the practitioners who operate it. |

---

## 10. Timeline

1. **Corpus identification:** Identify candidate transcripts for all domains
2. **Corpus construction:** Transcribe/collect 55 new transcripts (~440K words)
3. **Coding:** Apply codebook + domain extensions to all corpora
4. **Primary analysis:** Register shift ratios, chi-squared comparisons
5. **Secondary analysis:** Engagement-depth correlation, conference gradient, temporal trajectory, Brown control case
6. **Report:** Write up with comparison to EXP-006 and cross-domain synthesis

---

*Protocol designed February 6, 2026. Not yet run.*
*Depends on: EXP-006 methodology (validated), consciousness-studies void analysis (complete).*
*Connection: fills the constitutive-opacity experimental gap. Anesthesia = the void you can operate but can't explain.*
