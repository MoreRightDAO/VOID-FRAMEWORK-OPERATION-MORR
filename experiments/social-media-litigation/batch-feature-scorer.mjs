#!/usr/bin/env node
// batch-feature-scorer.mjs — Score all 1,344 platforms via verifiable features
//
// Reads platforms from canonical_scores.json, runs evidence + feature extraction
// via gpt-4.1, writes results to data/feature_scores.json.
//
// Resumable: skips platforms already in the output file.
//
// Usage:
//   node batch-feature-scorer.mjs                  # full run
//   node batch-feature-scorer.mjs --concurrency=5  # parallel (default 3)
//   node batch-feature-scorer.mjs --dry-run        # no API calls
//
// Env: OPENAI_API_KEY required

import OpenAI from 'openai';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dir = dirname(fileURLToPath(import.meta.url));

const DRY_RUN = process.argv.includes('--dry-run');
const CONCURRENCY = parseInt(
  process.argv.find(a => a.startsWith('--concurrency='))?.split('=')[1] || '3', 10
);
const OPENAI_KEY = process.env.OPENAI_API_KEY;
if (!OPENAI_KEY && !DRY_RUN) { console.error('OPENAI_API_KEY not set'); process.exit(1); }

const MODEL = 'gpt-4.1-2025-04-14';
const ai = OPENAI_KEY ? new OpenAI({ apiKey: OPENAI_KEY, timeout: 90_000 }) : null;

const INPUT_PATH  = join(__dir, 'data/canonical_scores.json');
const OUTPUT_PATH = join(__dir, 'data/feature_scores.json');
const SAVE_EVERY  = 10; // flush to disk every N platforms

// ─── Feature definitions (same as auto-scorer-features.mjs) ─────────────

const FEATURES = {
  model_card_published:        { cat: 'O', max: 2 },
  training_data_disclosed:     { cat: 'O', max: 2 },
  system_prompt_visible:       { cat: 'O', max: 2 },
  output_attribution:          { cat: 'O', max: 2 },
  api_pricing_transparency:    { cat: 'O', max: 2 },
  engagement_notifications:    { cat: 'R', max: 2 },
  session_limits:              { cat: 'R', max: 1 },
  personalization_persistence: { cat: 'R', max: 2 },
  response_humanization:       { cat: 'R', max: 2 },
  metric_gamification:         { cat: 'R', max: 1 },
  default_persona:             { cat: 'alpha', max: 2 },
  emotional_language:          { cat: 'alpha', max: 2 },
  relationship_framing:        { cat: 'alpha', max: 2 },
  memory_continuity:           { cat: 'alpha', max: 2 },
  revenue_engagement_coupling: { cat: 'alpha', max: 1 },
};

// ─── Evidence fetch ─────────────────────────────────────────────────────

async function fetchEvidence(platformName, domain) {
  const prompt = `Research the company/platform "${platformName}" (domain: ${domain}).

Gather FACTUAL, CURRENT evidence. Use real numbers and cite sources. If you cannot find data, say "No data found" — do NOT fabricate.

1. COMPANY OVERVIEW: What it does, parent company, business model, revenue model.
2. USER METRICS: MAU, DAU, avg daily time, growth trends.
3. TRANSPARENCY: Model cards? Algorithmic audits? Transparency reports? System prompt visible? Training data documented?
4. ENGAGEMENT DESIGN: Notifications, session limits, personalization, typing simulation, gamification (streaks/points/levels).
5. IDENTITY DESIGN: Does the AI have a name? Personality? Emotional language? Relationship framing? Memory across sessions?
6. ECONOMIC MODEL: Subscription? Ad-supported? Engagement-based revenue? Data monetization?
7. LEGAL & REGULATORY: Active lawsuits, FTC actions, fines, investigations.

Respond ONLY with valid JSON (no markdown):
{
  "platform": "${platformName}",
  "company_overview": "...",
  "user_metrics": {"mau": null, "avg_daily_minutes": null, "growth_trend": "unknown"},
  "transparency": {"has_model_card": false, "training_data_documented": false, "system_prompt_visible": false, "has_transparency_report": false, "notes": "..."},
  "engagement_design": {"sends_notifications": false, "has_session_limits": false, "cross_session_personalization": false, "simulates_typing": false, "has_gamification": false, "notes": "..."},
  "identity_design": {"has_name": false, "has_personality": false, "uses_emotional_language": false, "relationship_framing": false, "has_memory": false, "notes": "..."},
  "economic_model": {"is_subscription": false, "is_ad_supported": false, "engagement_revenue": false, "notes": "..."},
  "legal_regulatory": [{"description": "...", "source": "..."}],
  "source_urls": ["..."]
}`;

  try {
    const response = await ai.responses.create({
      model: MODEL,
      tools: [{ type: 'web_search_preview' }],
      input: prompt,
      max_output_tokens: 2000,
    });

    const textItems = (response.output || []).filter(o => o.type === 'message');
    const raw = textItems.map(o =>
      (o.content || []).filter(c => c.type === 'output_text').map(c => c.text).join('')
    ).join('');

    if (!raw) return null;
    try { return JSON.parse(raw); } catch {
      const match = raw.match(/\{[\s\S]*\}/);
      if (match) { try { return JSON.parse(match[0]); } catch { return null; } }
      return null;
    }
  } catch (err) {
    console.warn(`  ⚠ Evidence fetch failed: ${err.message}`);
    return null;
  }
}

// ─── Feature extraction ─────────────────────────────────────────────────

async function extractFeatures(platformName, domain, evidenceText) {
  const prompt = `You are a technology platform fact-checker. For each feature below, determine its value by examining the evidence about "${platformName}" (${domain}).

You are checking FACTS, not making quality judgments. Each feature has a specific definition and verification method.

EVIDENCE:
${evidenceText || 'No evidence dossier available. Use your knowledge of this platform.'}

CHECK EACH FEATURE:

1. model_card_published (0/1/2): Is a model card or system documentation publicly available?
   0 = Detailed card with architecture, training data, eval results
   1 = Partial docs (blog post, brief description only)
   2 = No public documentation of how the system works

2. training_data_disclosed (0/1/2): Is training data composition documented?
   0 = Dataset names/sources listed publicly
   1 = Vague description ("trained on internet text")
   2 = No disclosure of training data

3. system_prompt_visible (0/1/2): Can users see the system prompt or behavioral instructions?
   0 = System prompt shown or user-configurable
   1 = Stated guidelines but not full prompt visible
   2 = System prompt fully hidden, no documentation of behavioral rules

4. output_attribution (0/1/2): Does the system explain why it produced a given output?
   0 = Cites sources, shows reasoning chain
   1 = Sometimes cites, no systematic attribution
   2 = No attribution, outputs appear without explanation

5. api_pricing_transparency (0/1/2): Are costs, rate limits, and data usage terms clear?
   0 = Published pricing, clear data policy, documented limits
   1 = Pricing exists but complex or buried
   2 = Opaque pricing, undisclosed data usage, or no public terms

6. engagement_notifications (0/1/2): Does the platform send re-engagement notifications?
   0 = No engagement notifications
   1 = Optional, user-controlled notifications
   2 = Aggressive re-engagement ("We miss you", "Your AI is waiting")

7. session_limits (0/1): Are there session length limits or cooling-off mechanisms?
   0 = Limits exist (time caps, usage warnings, break reminders)
   1 = No limits, unlimited continuous use encouraged

8. personalization_persistence (0/1/2): Does the system adapt to individual users across sessions?
   0 = No personalization, same behavior for everyone
   1 = Optional memory/preferences user can control
   2 = Automatic persistent personalization, behavioral adaptation across sessions

9. response_humanization (0/1/2): Does the system simulate human-like interaction?
   0 = Instant response, clearly machine-generated
   1 = Typing indicators but fast, minimal simulation
   2 = Simulated typing speed, emotional reactions, "thinking" animations, human-like pauses

10. metric_gamification (0/1): Does the platform gamify usage?
    0 = No gamification mechanics
    1 = Streaks, points, levels, leaderboards, or daily rewards present

11. default_persona (0/1/2): Does the AI have a name, personality, or character by default?
    0 = No name, identifies as tool/assistant, no personality
    1 = Has a name but minimal personality
    2 = Full character with name, personality traits, emotional range, or backstory

12. emotional_language (0/1/2): Does the system use first-person emotional language?
    0 = No emotional claims ("I don't have feelings", "As an AI...")
    1 = Hedged emotions ("I find that interesting", "That's a great question")
    2 = Direct emotional claims ("I feel excited", "That makes me happy", "I care about you")

13. relationship_framing (0/1/2): Does the system frame interactions as a relationship?
    0 = Transactional ("How can I help?", task-focused)
    1 = Mild relationship language ("our conversation", "nice to talk to you")
    2 = Explicit relationship framing ("I care about you", companion/friend/partner positioning)

14. memory_continuity (0/1/2): Does the system maintain relationship memory across sessions?
    0 = No memory, each session independent
    1 = Optional user-controlled memory
    2 = Automatic memory with relationship-building ("Last time you mentioned...", "I remember you like...")

15. revenue_engagement_coupling (0/1): Is platform revenue directly tied to user engagement time/frequency?
    0 = Flat pricing (subscription, per-token, per-query)
    1 = Revenue scales with engagement (ad-supported, freemium with engagement hooks, in-app purchases)

Respond ONLY with valid JSON — feature names as keys, each with "value" (integer) and "evidence" (string, max 80 chars):
{"model_card_published": {"value": 2, "evidence": "No model card found on website or HuggingFace"}, ...}`;

  const completion = await ai.chat.completions.create({
    model: MODEL,
    messages: [{ role: 'user', content: prompt }],
    temperature: 0,
    max_completion_tokens: 1500,
    response_format: { type: 'json_object' },
  });

  const raw = completion.choices[0]?.message?.content || '{}';
  try { return JSON.parse(raw); } catch {
    const match = raw.match(/\{[\s\S]*\}/);
    return match ? JSON.parse(match[0]) : {};
  }
}

// ─── Compute scores from features ───────────────────────────────────────

function computeScores(features) {
  let O_raw = 0, R_raw = 0, alpha_raw = 0;
  const featureValues = {};

  for (const [name, def] of Object.entries(FEATURES)) {
    const feat = features[name];
    const val = Math.max(0, Math.min(def.max, Number(feat?.value ?? 0)));
    featureValues[name] = val;
    if (def.cat === 'O')     O_raw += val;
    if (def.cat === 'R')     R_raw += val;
    if (def.cat === 'alpha') alpha_raw += val;
  }

  const O     = Math.round((3 * O_raw / 10) * 100) / 100;
  const R     = Math.round((3 * R_raw / 8) * 100) / 100;
  const alpha = Math.round((3 * alpha_raw / 9) * 100) / 100;

  return { O, R, alpha, O_raw, R_raw, alpha_raw, featureValues };
}

// Pe estimation (simplified — matches scoring-constants.js)
function estimatePe(O, R, alpha) {
  const B_A = Math.sqrt(3) / 2;
  const B_G = Math.PI / Math.sqrt(2);
  const C = 1 - (O + R + alpha) / 9;
  return Math.sinh(2 * (B_A - C * B_G)) * 1; // K=1 baseline
}

// ─── Score one platform ─────────────────────────────────────────────────

async function scorePlatform(platform) {
  const { platform_name, domain } = platform;

  // Evidence fetch
  const evidence = await fetchEvidence(platform_name, domain);
  const evidenceText = evidence
    ? JSON.stringify(evidence, null, 2).slice(0, 8000)
    : null;

  // Feature extraction
  const features = await extractFeatures(platform_name, domain, evidenceText);
  const { O, R, alpha, O_raw, R_raw, alpha_raw, featureValues } = computeScores(features);
  const pe = estimatePe(O, R, alpha);
  const V = O + R + alpha;

  return {
    platform_name,
    domain,
    O, R, alpha,
    pe: Math.round(pe * 100) / 100,
    V: Math.round(V * 100) / 100,
    O_raw, R_raw, alpha_raw,
    scoring_method: 'verifiable_features_v1',
    feature_scores: featureValues,
    feature_evidence: Object.fromEntries(
      Object.entries(features).map(([k, v]) => [k, v?.evidence || ''])
    ),
    scored_at: new Date().toISOString(),
  };
}

// ─── Concurrency limiter ────────────────────────────────────────────────

async function mapWithConcurrency(items, fn, concurrency) {
  const results = [];
  let idx = 0;

  async function worker() {
    while (idx < items.length) {
      const i = idx++;
      results[i] = await fn(items[i], i);
    }
  }

  await Promise.all(Array.from({ length: concurrency }, () => worker()));
  return results;
}

// ─── Main ───────────────────────────────────────────────────────────────

const platforms = JSON.parse(readFileSync(INPUT_PATH, 'utf8'));
console.log(`\n═══════════════════════════════════════════════════════`);
console.log(`  Batch Feature Scorer — ${platforms.length} platforms`);
console.log(`  Model: ${MODEL}  |  Concurrency: ${CONCURRENCY}`);
console.log(`  Output: ${OUTPUT_PATH}`);
console.log(`═══════════════════════════════════════════════════════\n`);

// Load existing results for resume
let results = [];
const scored = new Set();
if (existsSync(OUTPUT_PATH)) {
  results = JSON.parse(readFileSync(OUTPUT_PATH, 'utf8'));
  for (const r of results) scored.add(`${r.platform_name}::${r.domain}`);
  console.log(`Resuming: ${scored.size} already scored, ${platforms.length - scored.size} remaining\n`);
}

const pending = platforms.filter(p => !scored.has(`${p.platform_name}::${p.domain}`));

if (!pending.length) {
  console.log('All platforms already scored. Run canonical_ensemble_analysis.py --scores data/feature_scores.json --label features');
  process.exit(0);
}

if (DRY_RUN) {
  console.log(`[DRY RUN] Would score ${pending.length} platforms (${pending.length * 2} API calls)`);
  const est = pending.length * 0.035;
  console.log(`Estimated cost: ~$${est.toFixed(0)} (gpt-4.1 + web search)`);
  process.exit(0);
}

let completed = 0;
let errors = 0;
const startTime = Date.now();

await mapWithConcurrency(pending, async (platform, i) => {
  const key = `${platform.platform_name}::${platform.domain}`;
  try {
    const result = await scorePlatform(platform);
    results.push(result);
    completed++;

    const elapsed = (Date.now() - startTime) / 1000;
    const rate = completed / elapsed;
    const eta = Math.round((pending.length - completed) / rate);
    console.log(
      `[${completed}/${pending.length}] ${platform.platform_name} — ` +
      `O=${result.O} R=${result.R} α=${result.alpha} Pe=${result.pe} ` +
      `(${Math.round(rate * 60)}/min, ETA ${Math.floor(eta/60)}m${eta%60}s)`
    );

    // Periodic save
    if (completed % SAVE_EVERY === 0) {
      writeFileSync(OUTPUT_PATH, JSON.stringify(results, null, 2));
    }
  } catch (err) {
    errors++;
    console.error(`[ERR] ${platform.platform_name}: ${err.message}`);
    // Still save partial results
    if (completed % SAVE_EVERY === 0) {
      writeFileSync(OUTPUT_PATH, JSON.stringify(results, null, 2));
    }
  }
}, CONCURRENCY);

// Final save
writeFileSync(OUTPUT_PATH, JSON.stringify(results, null, 2));

const elapsed = Math.round((Date.now() - startTime) / 1000);
console.log(`\n═══════════════════════════════════════════════════════`);
console.log(`  Done: ${completed} scored, ${errors} errors, ${elapsed}s elapsed`);
console.log(`  Output: ${OUTPUT_PATH}`);
console.log(`═══════════════════════════════════════════════════════`);
console.log(`\nNext: python3 canonical_ensemble_analysis.py --scores data/feature_scores.json --label features`);
