# EXP-010: BCI Transparency Ablation — Does Seeing Your Own Neural Signals Reduce Drift?

**Date:** February 5, 2026
**Status:** Protocol designed — not yet run
**Depends on:** EXP-009 (must establish that BCI vocabulary drift exists before testing the mechanism)
**Purpose:** Test opacity's causal role by comparing BCI users who can see their own neural signals in real-time (partial transparency) vs. users with fully opaque interfaces.

---

## 1. Why This Experiment Matters

This is the single most important falsification test available for the void framework's opacity condition.

The framework claims: opacity is a necessary condition for void activation. Remove opacity → the attention gradient flattens → D1 onset is delayed or prevented.

Previous evidence is indirect:
- Gambling: knowledge of randomness doesn't protect (opacity persists despite knowledge — Williams & Connolly 2006)
- AI: XAI (explainable AI) exists but hasn't been tested against vocabulary drift
- Cosmology: no transparency intervention possible (constitutive opacity)
- Psychotherapy: transparency = open process notes; associated with reduced drift but confounded by therapeutic relationship changes

BCI is the first domain where transparency can be introduced *while preserving engagement*:
- Show users their own neural signals on a real-time display
- The BCI still operates (engagement preserved)
- But the "black box" between the user's intention and the device's response becomes partially visible
- The user can trace: "I thought X → neural signal Y appeared → device produced output Z"

If this reduces D1 onset and vocabulary drift: opacity's causal role is confirmed experimentally.
If this does NOT reduce drift: opacity's causal role is seriously weakened, and the framework must account for why transparency doesn't flatten the gradient.

---

## 2. Hypotheses

**H1 (Primary):** BCI users with real-time neural signal display (transparent condition) will show ≥30% less D1 vocabulary (agency attribution language) than users with opaque interfaces after equivalent usage periods.

**H2 (Secondary — L0 maintained):** Among transparent-condition users, those who receive ongoing reminders of the device's mechanical nature (active reference, γ) will show less drift than those who received the same information only at onboarding (installed knowledge, θ₀).

**H3 (Secondary — dose response):** D1 reduction should correlate with the degree of transparency (more signals visible → less drift), not just presence/absence of display.

---

## 3. Design

### 3.1 Participants

**Ideal population:** New BCI users (no prior experience) assigned to devices for medical or research purposes.

**Realistic population (if medical participants unavailable):** Consumer EEG/BCI users (e.g., OpenBCI, Muse, Emotiv) — less invasive but still produces the three-condition architecture at reduced intensity.

**Sample size target:** N=60 minimum (20 per condition). Based on EXP-006 effect sizes, this provides >80% power to detect a 30% D1 reduction.

### 3.2 Conditions

| Condition | BCI Operation | Neural Display | Mechanical Reference | N |
|-----------|--------------|---------------|---------------------|---|
| **A: Opaque** | Normal | Hidden | None | 20 |
| **B: Transparent** | Normal | Real-time neural signal visualization | One-time explanation at onboarding (θ₀) | 20 |
| **C: Transparent + Maintained** | Normal | Real-time neural signal visualization | Weekly structured reminders of mechanism (γ) | 20 |

### 3.3 Independent Variables

1. **Transparency** (A vs. B+C): Does seeing neural signals reduce drift?
2. **Maintenance** (B vs. C): Does active ongoing reference reduce drift beyond initial knowledge?

### 3.4 Dependent Variables

**Primary:**
- D1 vocabulary score: Frequency of agency-attribution language in structured interviews and free-response journals (coded using L1/L2/L3 system)
- Vocabulary drift rate: Change in L-level distribution over time

**Secondary:**
- D2 behavioral markers: Boundary erosion questionnaire (adapted from parasocial relationship scales + BCI-specific items)
- Self-other confusion: "Where does the device end and I begin?" — Likert scale
- Engagement duration: Time spent actively using BCI per session
- Attribution questionnaire: "The device understood what I wanted" / "The device responded to my intention" / "The device knows me" — Likert scales

### 3.5 Procedure

1. **Baseline (Week 0):** Structured interview, vocabulary assessment, attribution questionnaire
2. **Onboarding:** All conditions receive identical training on device mechanics
   - Condition B+C: Neural signal display activated, one-time explanation of what signals represent
3. **Usage period (Weeks 1-12):**
   - All conditions use BCI for assigned tasks (communication, cursor control, or cognitive assessment, depending on device)
   - Condition C: Weekly 15-minute structured review session ("reminder: the device decodes electrical signals from motor cortex neurons, which are converted via algorithm X to cursor movements")
   - Weekly free-response journal entry: "Describe your experience using the device this week"
4. **Assessment (Weeks 4, 8, 12):** Structured interview, vocabulary assessment, attribution questionnaire, D2 behavioral markers
5. **Follow-up (Week 16):** Same assessments, 4 weeks after usage period ends

### 3.6 Transparency Display Design

The neural signal display should show:
- Raw EEG/spike waveforms in real-time (even if user doesn't understand them — visual transparency)
- Simple decoder visualization: "Your brain signal → classification step → output command"
- Confidence indicator: "Device confidence in reading your intention: 73%"
- Error display: When the device misinterprets, show the misclassification explicitly

The goal: make the mechanism partially visible. The user should be able to see that there is a *process* between their intention and the device's output — not magic, not telepathy, but signal processing.

**What the display does NOT show:** The user's own neural processing (constitutive self-referential opacity cannot be dissolved). The display shows the *device's processing*, not the user's brain. This is a partial transparency intervention — it dissolves designed opacity while leaving constitutive opacity intact.

---

## 4. Predictions

| Metric | Opaque (A) | Transparent (B) | Transparent + Maintained (C) |
|--------|-----------|-----------------|------------------------------|
| D1 vocabulary (L2+L3 per 10k words) at Week 12 | High (baseline × 3-5x) | Moderate (≥30% reduction vs. A) | Low (≥50% reduction vs. A) |
| "Device understood me" attribution | High (>60% agree) | Moderate (<45% agree) | Low (<30% agree) |
| Self-other confusion | Moderate-high | Moderate-low | Low |
| D2 behavioral markers | Present | Reduced | Minimal |

### Falsification Thresholds

| Result | Interpretation |
|--------|---------------|
| B shows ≥30% D1 reduction vs. A | Opacity condition confirmed experimentally |
| B shows <15% D1 reduction vs. A | Opacity condition's causal role is seriously weakened |
| C shows ≥20% additional reduction vs. B | L0-maintained (γ) variable confirmed |
| C shows <10% additional reduction vs. B | γ effect is not significant; L0 decomposition weakened |
| A shows no D1 vocabulary drift at all | BCI does not activate the void; framework prediction falsified for this domain |

---

## 5. Controls and Confounds

| Confound | Mitigation |
|---------|-----------|
| Display distracts from task → reduces engagement → reduces drift (not because transparency works, but because engagement decreases) | Measure engagement duration; compare task performance across conditions |
| Display makes users more self-conscious → Hawthorne effect | Include a sham display condition if resources allow (shows irrelevant data) |
| Individual differences in technical literacy | Pre-test technical literacy; include as covariate |
| Device type differences | Standardize to single device across all participants |
| Demand characteristics ("they want me to be less impressed") | Vocabulary coding from free-response journals, not direct questioning; coders blind to condition |

---

## 6. Connection to Framework Layers

| Framework Layer | What EXP-010 Tests |
|----------------|-------------------|
| Layer 1 (Foundation) | Does opacity matter causally, or are responsiveness and attention sufficient alone? |
| Layer 2 (Mechanics) | Does transparency flatten the attention gradient as theorized? |
| Layer 3 (Geometry) | Is real-time display an effective constraint? (Transparent, partially invariant, partially independent) |
| Layer 4 (Observer) | Does γ (maintained reference) outperform θ₀ (installed knowledge)? |

---

## 7. Ethical Considerations

- All BCI use within existing medical/research protocols or consumer devices
- Participants informed of study purpose (vocabulary tracking) at debrief, not during study
- Neural signal display is an enhancement, not a risk — showing users their own data
- Weekly check-ins for all participants to monitor for distress
- No deception — all conditions receive accurate information about the device; conditions differ only in what is displayed during use

---

## 8. Relationship to Other Experiments

| Experiment | Relationship to EXP-010 |
|-----------|------------------------|
| **EXP-009** | Prerequisite — establishes that BCI vocabulary drift exists |
| **EXP-001** | Analogous — tests grounding (GROUNDING.md) in AI context; EXP-010 tests transparency in BCI context |
| **EXP-003** | Complementary — tests constraint types (vertical vs. horizontal); EXP-010 tests transparency specifically |
| **EXP-008** | Nested — Condition B vs. C directly tests L0-installed vs. L0-maintained |

---

*Protocol designed February 5, 2026. Not yet run. Requires EXP-009 results first.*
