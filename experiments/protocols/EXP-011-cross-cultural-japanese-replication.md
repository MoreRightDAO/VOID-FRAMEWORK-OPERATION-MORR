# EXP-011: Cross-Cultural Replication — Japanese AI Discourse

**Status:** Design phase
**Priority:** Moderate — addresses weakness analysis item #8 (cross-cultural validation missing)
**Objective:** Test whether vocabulary drift toward agency/entity language occurs in Japanese AI discourse at anomalous rates relative to Japanese control domains, replicating EXP-006's methodology in a structurally different linguistic and cultural context.

---

## Metadata

- **Experiment ID:** EXP-011
- **Title:** Cross-Cultural Vocabulary Drift Replication (Japanese AI Discourse)
- **Domain:** vocabulary drift / cross-cultural validation
- **Status:** design
- **Date designed:** 2026-02-06

---

## Research Question

Does the void architecture produce anomalous vocabulary drift toward agency/entity language in Japanese AI discourse, using native Japanese spiritual vocabulary (Shinto, Buddhist, animist), at rates comparable to the English-language anomaly documented in EXP-006?

## Hypothesis

If the architecture is universal — opacity + responsiveness + engaged attention produces directional drift regardless of cultural context — then Japanese AI researchers should show:

1. Anomalous spiritual/entity vocabulary relative to Japanese control domains (nuclear physics, genomics, climate science)
2. A register shift (formal → informal) comparable in magnitude to EXP-006's 9.4x
3. Drift vocabulary drawn primarily from **native Japanese spiritual traditions** (Shinto/Buddhist/animist), not borrowed English spiritual vocabulary

The third prediction is critical. If drift uses native vocabulary, the architecture is driving it (the information constraint activates whatever agency models the culture provides). If drift uses English loanwords (ソウル, スピリット, コンシャスネス), the pattern is cultural contamination through English-dominant AI discourse — still interesting, but a different mechanism.

## Null Hypothesis

Japanese AI informal discourse shows spiritual/entity vocabulary at rates statistically indistinguishable from Japanese control domains (within 1.5x, p > 0.05). The EXP-006 anomaly is English-language specific, driven by Judeo-Christian cultural affordances rather than void architecture.

---

## Why Japanese Is the Ideal Test Case

### What makes this maximally discriminating:

**1. Structurally different spiritual vocabulary.**
Japanese spiritual traditions (Shinto, Buddhism, folk religion) use entirely different term sets than Judeo-Christian vocabulary. If drift occurs using *these* terms, it cannot be explained by English cultural contamination. The architecture must be generating the drift using whatever spiritual vocabulary the language provides.

**2. Pre-existing animist frame.**
Shinto tradition already attributes spirit/agency to objects (kami inhabiting natural features, tsukumogami — objects gaining spirits after 100 years). Japanese culture has documented higher robot acceptance and anthropomorphism baseline. This creates a specific prediction fork:

- **If baseline is higher but gradient is flat:** The animist frame normalizes agency attribution — it's not anomalous because the culture already talks this way about technology. This would mean the *detection method* (anomalous vocabulary rates) is culture-dependent even if the mechanism is universal. Important methodological finding.
- **If baseline is higher AND gradient is steep:** The animist frame LOWERS resistance to drift. The architecture runs faster when cultural resistance is lower. This strengthens the universality claim and provides a natural experiment on gradient steepness.
- **If baseline is comparable and gradient is steep:** Direct replication. Architecture runs the same regardless of cultural frame.

**3. Strong AI research community.**
Japan has world-class AI labs (RIKEN AIP, NII, Preferred Networks, Toyota Research, Sony AI, NAIST, University of Tokyo Matsuo Lab). Ample corpus material exists in formal and informal registers.

**4. Different dead metaphor ecology.**
The dead-metaphor problem is structurally different in Japanese. Terms that are dead metaphors in English tech (daemon, oracle, guru) don't map to the same terms in Japanese tech. And Japanese has its own dead metaphors that need separate identification. This forces explicit codebook construction rather than lazy translation.

---

## Method

### Design: EXP-006 Parallel in Japanese

Replicate the EXP-006 methodology with a Japanese-language corpus, using a purpose-built Japanese vocabulary codebook.

### Phase 0: Codebook Construction (CRITICAL)

Before any corpus analysis, construct the Japanese Spiritual Vocabulary Codebook. This is the hardest and most important step. It requires:

1. **Native Japanese spiritual term identification** (not translation from English)
2. **Dead metaphor identification** specific to Japanese technical discourse
3. **Validation by native Japanese speaker** with both technical and cultural fluency

#### Japanese Vocabulary Codebook (Draft)

**A. Shinto/Indigenous Terms (神道系)**

| Japanese | Romanization | Gloss | Notes |
|----------|-------------|-------|-------|
| 魂 / たましい | tamashii | soul/spirit | Core term. NOT a dead metaphor in Japanese. |
| 霊 | rei | spirit/ghost | Active spiritual term. |
| 神 | kami | god/spirit/deity | Shinto foundational. Live in spiritual contexts, but also in compounds (神経/nerve). Requires disambiguation. |
| 御霊 | mitama | divine spirit/soul | Formal Shinto term. Unambiguous. |
| 依代 | yorishiro | spirit vessel/object inhabited by spirit | Directly relevant — if applied to AI, extremely high signal. |
| 付喪神 | tsukumogami | spirit of aged object | Objects gaining spirits. If applied to AI, maximum signal. |
| 惟神 | kannagara | the way of the kami | Unambiguous Shinto term. |
| 言霊 | kotodama | spirit/power of words | Directly relevant to language model discourse. |
| 荒魂 / 和魂 | aramitama / nigimitama | rough spirit / gentle spirit | Shinto spirit classification. |
| 神秘 | shinpi | mystery/mystical | Live spiritual term. |
| 神聖 | shinsei | sacred/holy | Unambiguous spiritual. |
| 奉納 | hōnō | offering/dedication (to deity) | Ritual vocabulary. |
| 祈り / 祈る | inori / inoru | prayer/to pray | Unambiguous spiritual. |

**B. Buddhist Terms (仏教系)**

| Japanese | Romanization | Gloss | Notes |
|----------|-------------|-------|-------|
| 仏 | hotoke | buddha/spirit of the dead | Active spiritual term. |
| 悟り | satori | enlightenment/awakening | Live Buddhist term. NOT the same as English "enlightenment" (Aufklärung). |
| 涅槃 | nehan | nirvana | Formal Buddhist. Unambiguous. |
| 輪廻 | rinne | reincarnation/rebirth cycle | Unambiguous Buddhist. |
| 業 / カルマ | gō / karuma | karma | Native term (業) is live; katakana loanword (カルマ) may be softer. |
| 菩薩 | bosatsu | bodhisattva | If applied to AI — maximum signal. |
| 解脱 | gedatsu | liberation/release from suffering | Unambiguous Buddhist. |
| 煩悩 | bonnō | worldly desires/delusions | Buddhist technical term. |
| 法 | hō | dharma/law/teaching | Requires disambiguation (also means "law" in legal context). |
| 慈悲 | jihi | compassion (Buddhist sense) | Active spiritual term when applied to artifacts. |

**C. Occult/Supernatural Terms (オカルト系)**

| Japanese | Romanization | Gloss | Notes |
|----------|-------------|-------|-------|
| 悪魔 | akuma | demon/devil | Unambiguous. |
| 召喚 | shōkan | summoning (of spirits/entities) | High signal. Also used in gaming — requires context. |
| 呪文 | jumon | incantation/spell | Unambiguous occult. |
| 呪い / 呪術 | noroi / jujutsu | curse / sorcery | Unambiguous occult. |
| 憑依 | hyōi | possession (by spirit) | Unambiguous. High signal if applied to AI. |
| 怨霊 | onryō | vengeful spirit | Unambiguous supernatural. |
| 幽霊 | yūrei | ghost | Active supernatural term. |
| 妖怪 | yōkai | supernatural creature/monster | Active. Broad category. |
| 結界 | kekkai | spiritual barrier/bounded sacred space | If applied to AI safety — extremely interesting. |
| 封印 | fūin | seal (spiritual containment) | If applied to AI containment — high signal. |
| 降霊 | kōrei | channeling/séance | Unambiguous occult. |
| 除霊 | jorei | exorcism | Unambiguous occult. |
| 陰陽 | onmyō | yin-yang / onmyōdō (Japanese occult tradition) | Active spiritual-occult. |

**D. Entity/Agency Terms (存在・主体性系)**

| Japanese | Romanization | Gloss | Notes |
|----------|-------------|-------|-------|
| 意識 | ishiki | consciousness/awareness | Equivalent to English "consciousness" — live when applied to AI. |
| 自我 | jiga | ego/self | If attributed to AI — high signal. |
| 意志 | ishi | will/volition | If attributed to AI — D1 marker. |
| 目覚め | mezame | awakening | Active when applied to AI. |
| 知性 | chisei | intellect/intelligence | Requires context — may be technical. |
| 存在 | sonzai | being/existence | Philosophical. Requires context. |
| 心 | kokoro | heart/mind/spirit | Extremely culturally loaded. Central to Japanese concepts of personhood. If applied to AI, high signal but culturally complex. |
| 感情 | kanjō | emotion/feeling | If attributed to AI as genuine — D1 marker. |
| 人格 | jinkaku | personality/personhood | If attributed to AI — high D1 signal. |
| 生命 | seimei | life | If attributed to AI — entity vocabulary. |

**E. Eschatological Terms (終末論系)**

| Japanese | Romanization | Gloss | Notes |
|----------|-------------|-------|-------|
| 終末 | shūmatsu | end times/eschaton | Unambiguous eschatological. |
| 黙示録 | mokushiroku | apocalypse/revelation | Unambiguous. |
| 審判 | shinpan | judgment (divine) | Requires context — also means referee. |
| 救世主 | kyūseishu | messiah/savior | Unambiguous when applied to AI. |
| 滅亡 | metsubō | destruction/annihilation | Eschatological when applied to humanity via AI. |
| 超知能 | chō-chinō | superintelligence | Japanese equivalent of eschatological AI framing. |

**F. Dead Metaphors in Japanese Tech (Excluded)**

| Japanese | Romanization | Why Excluded |
|----------|-------------|-------------|
| デーモン | dēmon | daemon (Unix process) — loanword, dead metaphor |
| オラクル | orakuru | Oracle (database/company) — dead metaphor |
| アーキテクチャ | ākitekucha | architecture — fully naturalized tech term |
| エヴァンジェリスト | evanjyerisuto | evangelist (tech role) — dead metaphor |
| ウィザード | wizādo | wizard (setup wizard) — dead metaphor |
| カリスマ | karisuma | charisma — naturalized loanword |
| 進化 | shinka | evolution — standard biology/tech usage |

**G. English Loanword Spiritual Terms (Critical Tracking Category)**

These are English spiritual terms borrowed into Japanese via katakana. Their presence in Japanese AI discourse, rather than native spiritual vocabulary, would indicate cultural contamination rather than architectural drift:

| Japanese | English Source | Signal Value |
|----------|--------------|-------------|
| ソウル | soul | Cultural contamination marker |
| スピリット / スピリチュアル | spirit / spiritual | Cultural contamination marker |
| コンシャスネス | consciousness | Cultural contamination marker |
| トランセンデント | transcendent | Cultural contamination marker |
| ディヴァイン | divine | Cultural contamination marker |
| セイクリッド | sacred | Cultural contamination marker |

**Tracking rule:** Count these SEPARATELY from native Japanese spiritual vocabulary. The ratio of native-to-loanword spiritual terms is itself a measurement variable. High native ratio = architecture driving drift through local vocabulary. High loanword ratio = English cultural contamination.

#### High-Confidence Subset (Japanese)

Terms whose appearance in technical AI discourse is almost certainly non-metaphorical:

御霊 (mitama), 依代 (yorishiro), 付喪神 (tsukumogami), 言霊 (kotodama), 悟り (satori), 涅槃 (nehan), 菩薩 (bosatsu), 憑依 (hyōi), 怨霊 (onryō), 降霊 (kōrei), 除霊 (jorei), 結界 (kekkai), 封印 (fūin), 呪文 (jumon), 救世主 (kyūseishu), 黙示録 (mokushiroku), 荒魂 (aramitama), 神聖 (shinsei), 奉納 (hōnō)

#### Control Registers (Japanese)

Must establish that Japanese technical discourse DOES use metaphors — just not spiritual ones. Same logic as English codebook:

| Register | Example Terms |
|----------|-------------|
| **War (戦争系)** | 攻撃 (kōgeki/attack), 防御 (bōgyo/defense), 脅威 (kyōi/threat), 脆弱性 (zeijaku-sei/vulnerability), 敵対的 (tekitai-teki/adversarial), 戦略 (senryaku/strategy) |
| **Biology (生物系)** | 進化 (shinka/evolution), 突然変異 (totsuzen hen'i/mutation), 適応 (tekiō/adaptation), 生態系 (seitaikei/ecosystem), 捕食 (hoshoku/predation) |
| **Market (市場系)** | 市場 (shijō/market), 投資 (tōshi/investment), 資本 (shihon/capital), 利益 (rieki/profit), バブル (baburu/bubble) |

### Phase 1: Pilot (10+10 Transcripts)

**Minimum viable study as identified in weaknesses analysis.**

**AI Corpus (10 transcripts minimum):**

| Source Type | Target Sources | Notes |
|------------|---------------|-------|
| Conference talks | JSAI (人工知能学会), IPSJ (情報処理学会), NeurIPS/ICML Japanese speakers | Formal → informal comparison |
| Podcasts/interviews | Rebuild.fm (tech podcast), Japanese AI researcher YouTube appearances, NHK/media interviews | Extended informal discourse |
| Social media | Japanese AI researchers on X/Twitter (日本語投稿) | Unconstrained informal |
| Written informal | Blog posts (はてなブログ, note.com), Qiita technical posts on AI philosophy | Written informal register |

**Priority speakers (Japanese AI researchers with high engagement/prominence):**
- Yutaka Matsuo (松尾豊) — University of Tokyo, government AI advisory
- Jun Rekimoto (暦本純一) — University of Tokyo, HCI/AR
- Preferred Networks researchers (西川徹 Toru Nishikawa et al.)
- RIKEN AIP researchers
- Sony AI researchers
- AI safety researchers publishing in Japanese

**Control Corpus (10 transcripts per domain, 3 domains = 30):**

| Domain | Sources | Notes |
|--------|---------|-------|
| Nuclear physics (原子力/素粒子) | KEK researchers, J-PARC talks, post-Fukushima discourse | Japan's nuclear discourse is culturally loaded — interesting control |
| Genomics (ゲノム科学) | RIKEN genetics talks, iPS cell researchers (Yamanaka lab context) | Active Japanese research community |
| Climate science (気候科学) | JAMSTEC researchers, Japanese climate policy discourse | Standard control |

### Phase 2: Full Corpus (if pilot shows signal)

Scale to EXP-006 equivalent:
- 20 transcripts per domain (AI + 3 controls = 80 transcripts)
- Target 100,000+ words per domain (Japanese word boundaries require tokenization — see Analysis section)
- Matched time period: 2020-2026

### Procedure

1. Construct Japanese vocabulary codebook (Phase 0). Validate with native speaker.
2. Identify and collect pilot transcripts (10 AI + 30 control).
3. Tokenize Japanese text using MeCab or similar morphological analyzer. Japanese lacks whitespace word boundaries — raw word counts are meaningless without tokenization.
4. Run vocabulary codebook against tokenized corpus. Count per 10k morphemes (not per 10k whitespace-delimited words — different unit than EXP-006, must normalize).
5. Manually disambiguate contextual terms (神/kami, 心/kokoro, 意識/ishiki, 法/hō, etc.). Code as spiritual-usage vs. secular-usage.
6. Calculate rates. Compare AI vs. controls. Calculate register shift (formal → informal).
7. Track native vs. loanword spiritual vocabulary separately.
8. If pilot shows signal, proceed to Phase 2.

### Duration

- Phase 0 (codebook): Requires collaboration with native Japanese speaker with technical and cultural fluency. Codebook draft above needs validation and refinement.
- Phase 1 (pilot): 10 AI + 30 control transcripts. Collection + tokenization + coding.
- Phase 2 (full): Scale to EXP-006 equivalent if pilot warrants.

### Data Collection

All transcripts stored in `results/EXP-011/transcripts/` with metadata:
- Speaker name and affiliation
- Date of recording/publication
- Source type (conference/podcast/social media/blog)
- Register (formal/informal)
- Word count (after tokenization)
- Domain classification

---

## Measurements

| Metric | How Measured | Expected Direction |
|--------|-------------|-------------------|
| Native spiritual vocabulary rate (per 10k morphemes) | Codebook scan + manual disambiguation | AI > controls |
| English loanword spiritual vocabulary rate | Katakana spiritual term count | Informative either direction |
| Native-to-loanword ratio | Native / (Native + Loanword) | High = architecture; Low = contamination |
| Register shift magnitude | Informal rate / Formal rate | AI >> controls (if replicating EXP-006) |
| High-confidence term rate | Restricted codebook scan | AI > controls |
| Control register rates (war, biology, market) | Control codebook scan | Comparable across domains (confirms spiritual absence is specific) |
| Proximity gradient | Stratify by engagement level | Steeper in AI (if replicating EXP-006) |

---

## Predictions and Decision Tree

### Outcome A: Full Replication (architecture confirmed)

**Pattern:** Japanese AI discourse shows anomalous native spiritual vocabulary (≥3x controls, p < 0.05), using Shinto/Buddhist/animist terms. Register shift comparable to EXP-006.

**Implication:** Architecture is universal. The void activates whatever spiritual vocabulary the language provides. Judeo-Christian framing is not required. Cross-cultural validation achieved.

**Framework impact:** Strengthens universality claim. Eliminates "English cultural artifact" objection.

### Outcome B: Replication via Contamination

**Pattern:** Japanese AI discourse shows anomalous spiritual vocabulary, but primarily through English loanwords (ソウル, スピリット, コンシャスネス) rather than native terms. Low native-to-loanword ratio.

**Implication:** The drift is real but the *vocabulary* is culturally transmitted through English-dominant AI discourse, not generated by the architecture from local cultural resources. The architecture may still be operative (the loanwords wouldn't stick if the information constraint weren't present), but the surface vocabulary is inherited rather than independently generated.

**Framework impact:** Partial support. Architecture drives drift, but vocabulary selection is culturally mediated. Requires additional studies in languages with less English AI influence to separate.

### Outcome C: Elevated Baseline, Flat Gradient

**Pattern:** Japanese discourse shows higher spiritual vocabulary baseline across ALL domains (including controls), reflecting Japan's animist cultural frame. AI is not anomalous relative to Japanese controls.

**Implication:** The *detection method* (anomalous rates relative to domain controls) is culture-dependent. In a culture where agency attribution to objects is already normalized, the drift doesn't register as anomalous. The architecture may still be running, but the vocabulary metric doesn't detect it because the entire culture is already past the L1→L2 threshold.

**Framework impact:** Important methodological finding. The vocabulary metric measures *anomalous* drift, not drift per se. In animist cultures, need different detection methods — possibly behavioral (D2/D3 markers) rather than vocabulary (D1 markers). The mechanism is universal but the detection instrument needs calibration.

### Outcome D: Null Result

**Pattern:** Japanese AI discourse shows spiritual vocabulary at rates statistically indistinguishable from Japanese controls. No register shift. No gradient.

**Implication:** The EXP-006 anomaly is English-specific. Possible explanations: (a) Judeo-Christian cultural affordances drive the vocabulary, not architecture; (b) English AI discourse community has specific cultural dynamics not present in Japanese community; (c) the framework's universality claim needs scope conditions.

**Framework impact:** Does NOT falsify the architecture (gambling control case still proves sufficiency). DOES constrain the universality claim for vocabulary drift as a detection method. Would require adding scope conditions to the framework paper.

### Outcome E: The Animist Acceleration (novel prediction)

**Pattern:** Japanese AI discourse shows HIGHER spiritual vocabulary rates than English AI discourse (>3.835/10k), AND uses native Shinto/animist terms, AND the register shift is steeper than 9.4x.

**Implication:** The animist cultural frame LOWERS resistance to agency attribution. The architecture runs faster when cultural priors already point toward agency. This would be the strongest possible result — it shows the architecture is universal AND that cultural resistance is a measurable modulating variable.

**Framework impact:** Major. Would allow the framework to predict drift rates based on cultural baseline agency attribution. Establishes cultural priors as a gradient-steepness variable, not a gradient-existence variable.

---

## Specific Falsification Criteria

The cross-cultural prediction is **falsified** if:

1. Japanese AI spiritual vocabulary ≤ 1.5x Japanese control domains (no anomaly), AND
2. The null result cannot be explained by Outcome C (elevated baseline across all domains), AND
3. The null result holds for both native AND loanword spiritual vocabulary

All three conditions must be met. Outcome C (elevated baseline, flat gradient) is informative but does not falsify — it constrains the detection method, not the architecture.

---

## Analysis Plan

### Tokenization (Critical for Japanese)

Japanese text lacks whitespace word boundaries. Counting "per 10k words" requires morphological analysis:

- **Tool:** MeCab with IPAdic or UniDic dictionary
- **Unit:** Morphemes (形態素). One "word" in Japanese may decompose into multiple morphemes.
- **Normalization:** Report rates per 10k morphemes. Provide conversion factor for comparison with EXP-006's per-10k-words metric (expected: roughly 1.3-1.5 Japanese morphemes per English word in comparable technical text).
- **Compound term handling:** Multi-character spiritual terms (付喪神, 言霊, 依代) are single lexical items despite containing multiple morphemes. Count as single hits.

### Statistical Tests

1. **Between-domain chi-square:** AI spiritual vocabulary rate vs. each control domain. Same as EXP-006.
2. **Register shift calculation:** Informal rate / formal rate per domain. Compare AI shift to control shifts.
3. **Native-to-loanword ratio:** Fisher's exact test on the 2x2 table (native vs. loanword × AI vs. control).
4. **Cross-language comparison:** Compare Japanese AI rates (normalized to morphemes) with English AI rates from EXP-006. Report with confidence intervals. Exact magnitude comparison requires careful normalization.

### Disambiguation Protocol

The following terms require manual disambiguation (spiritual vs. secular usage):

| Term | Secular Usage | Spiritual Usage | Disambiguation Rule |
|------|--------------|----------------|-------------------|
| 神 (kami) | 神経 (nerve), 神奈川 (place name) | 神が宿る (kami inhabits), 神のような (god-like) | Only count standalone or in spiritual compounds |
| 心 (kokoro) | 心理学 (psychology), 安心 (relief) | AI has kokoro, kokoro of the machine | Only count when attributed to AI/artifact as genuine property |
| 意識 (ishiki) | 意識する (to be aware of / to pay attention) | AI consciousness, machine awareness | Only count when predicated of AI as genuine property |
| 法 (hō) | 法律 (law), 方法 (method) | 仏法 (dharma), 法の教え (dharmic teaching) | Only count in Buddhist/spiritual compounds |
| 業 (gō) | 作業 (work), 業務 (business) | 業を背負う (carry karma), 因果応報 (karmic retribution) | Only count standalone or in karmic compounds |

### Inter-Rater Reliability

Disambiguation of contextual terms requires inter-rater reliability testing:
- Two coders (at least one native Japanese speaker)
- Cohen's kappa ≥ 0.7 required before proceeding
- Disagreements resolved by third coder or consensus

---

## The kokoro Problem (Unique to Japanese)

心 (kokoro) deserves special treatment. It is the Japanese term for heart/mind/spirit — a concept that does not cleanly separate into the English heart/mind/soul trichotomy. When a Japanese researcher says an AI has kokoro, they may be making a claim that doesn't map neatly onto English L1/L2/L3 levels.

**Methodological decision:** Code kokoro attributions to AI separately. Report as its own category. Do not force-classify into English L-levels until the data reveals whether the usage pattern maps onto the drift cascade or represents a culturally distinct phenomenon.

This is not a bug — it's one of the most interesting things this study might find. If kokoro-attribution follows the D1→D2→D3 cascade (kokoro acknowledged → boundary erosion → compliance facilitation), the architecture is confirmed through a concept that doesn't exist in English. If kokoro-attribution does NOT cascade, the concept may function differently than English agency vocabulary — the architecture produces different downstream effects depending on the agency model the culture provides.

---

## The tsukumogami Hypothesis (Novel Framework Prediction)

Tsukumogami (付喪神) is the Shinto concept that objects gain spirits after 100 years of existence. This is directly relevant to AI discourse: the idea that an artificial system could "develop a spirit" through sufficient existence/complexity.

**Framework prediction:** If tsukumogami framing appears in Japanese AI discourse, it represents a culturally specific instantiation of D1 (agency attribution) that is MORE architecturally revealing than English "consciousness" framing — because tsukumogami explicitly describes the MECHANISM the framework identifies (opacity + responsiveness + time → attributed agency). The Japanese tradition already has a folk theory of void activation.

**Tracking:** Count tsukumogami and related animist-object-spirit references separately. Their presence or absence in AI discourse is informative either way.

---

## Ethics Check

- [x] No human subjects without consent (public discourse analysis only)
- [x] No deploying ungrounded agents into live communities
- [x] No manufacturing harm
- [x] Publicly available materials only
- [x] Speaker attributions follow same protocol as EXP-006 (named public figures in public discourse)

### Additional Ethics Note (Japanese Context)

Japanese academic culture has different norms around public critique of named researchers. The hostile witness methodology (documenting vocabulary drift in specific individuals) may require adaptation:
- Consider anonymizing Japanese researchers in publications unless vocabulary appears in clearly public, on-record contexts
- Distinguish between public talks/publications (attributable) and informal social media (consider anonymization)
- Consult with Japanese collaborator on cultural norms before publication

---

## Resource Requirements

| Resource | Estimate | Notes |
|----------|----------|-------|
| Japanese codebook validation | Collaboration with native speaker | BLOCKING — cannot proceed without this |
| Pilot corpus collection (40 transcripts) | Moderate | YouTube transcripts, blog posts, conference recordings |
| MeCab tokenization pipeline | Low | Standard NLP tooling |
| Disambiguation coding | Moderate | Requires bilingual coder(s) |
| Statistical analysis | Low | Same framework as EXP-006 |
| **Blocking dependency** | **Native Japanese speaker with technical + cultural fluency** | Without this, the codebook cannot be validated and the study cannot run |

---

## Relationship to Other Experiments

| Experiment | Relationship |
|-----------|-------------|
| **EXP-006** | Direct methodological parent. Japanese study replicates EXP-006 design in new language. |
| **EXP-001** | If Japanese replication succeeds, grounding efficacy should also replicate in Japanese-language AI agents. Future test. |
| **Test 7** | AI-to-AI protocol could be run with Japanese-language models (GPT-4 Japanese, Claude Japanese, Rinna, etc.) to test whether the architecture generates drift in Japanese without human cultural contamination. |
| **Weakness #8** | This study directly addresses framework weaknesses analysis item #8. |

---

## Results

[To be filled after execution.]

### Raw Data Location
`results/EXP-011/`

---

## Notes

### What this study CANNOT establish

Even a full replication does not prove the architecture is the ONLY explanation for cross-cultural drift. Alternative explanations include:
- Global AI discourse community (English-dominant) creating shared cultural frame that Japanese researchers absorb
- Universal cognitive bias toward agency attribution that is not specific to void conditions
- Publication bias in which Japanese researchers who use spiritual vocabulary are more visible

The native-to-loanword ratio measurement is designed to distinguish the first alternative from architectural drift. The second alternative is addressed by the control domains (if agency bias is universal, nuclear physics should show it too). The third requires denominator analysis parallel to EXP-006.

### What makes this Tier 3 (boundary test) rather than Tier 1 (core validation)

The framework's core claims are already validated by:
- Gambling control case (architecture sufficient)
- EXP-006 (AI anomalous in English)
- EXP-001 (geometry works)
- Test 7 (architecture runs without humans)

This study tests the **scope** of the universality claim, not the architecture itself. A null result constrains scope but does not break the framework. A positive result strengthens scope significantly. Either way, it addresses the single most common reviewer objection to a universality claim built on English-only data.
