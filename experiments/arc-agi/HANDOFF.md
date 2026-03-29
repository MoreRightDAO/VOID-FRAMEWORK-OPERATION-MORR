# ARC-AGI Exploration — Handoff

**Branch:** `main` (merged from `claude/arc-agi-exploration-zoLLY`)
**Date:** 2026-03-26
**Status:** First LLM eval complete — 63.2% on 19 tasks. API credit exhausted mid-run.

---

## What Exists

Four solver layers, bottom-up:

| File | What | Accuracy |
|------|------|----------|
| `solver.py` | Brute-force DSL hypothesis search | 5.0% (20/400) |
| `smart_solver.py` | K-Factor guided DSL (prunes hypothesis space by transform type) | 6.8% (27/400) |
| `llm_solver.py` | Claude API solver with DSL fast-path fallback | TBD |
| `evo_solver.py` | Evolutionary code evolution (Imbue-inspired) — the main event | **63.2%** (12/19 tasks) |

Supporting modules:
- `loader.py` — Grid class, task loading, visualization (emoji grids)
- `dsl.py` — 40+ grid primitives (rotate, tile, crop, flood_fill, objects, etc.)
- `k_factor.py` — K-Factorization decomposition (§136), transform classification, **color mapping analysis** (NEW)
- `topo_features.py` — Topology: Euler characteristic, holes, percolation, spanning, **symmetry/rearrangement detection** (IMPROVED)

Data: `data/ARC-AGI/` — standard ARC-AGI JSON format (400 training, 400 eval). Cloned from `fchollet/ARC-AGI`.

---

## First LLM Eval Results (2026-03-26)

**12/19 tasks solved (63.2%)** — API credits exhausted after 19 tasks.

| Category | Count | Notes |
|----------|-------|-------|
| Solved | 12 | 6 seed, 4 mutate, 1 crossover, 1 DSL |
| Unsolved | 5 | Best fitness: 0.734, 0.474, 0.473, 0.392, 0.351 |
| Wrong on test | 2 | Overfitting — passes training, fails generalization |

**Method breakdown of solves:**
- `seed` (50%): Model gets it on first attempt with 4 LLM calls
- `mutate` (33%): Evolution fixes partially-correct code
- `crossover` (8%): Combining two partial solutions
- `dsl` (8%): Pure DSL (no LLM needed)

**Key finding:** Seeds are very effective. When evolution is needed, it typically solves in 1-2 generations.

### Failure Mode Analysis

All failures share these traits:
1. **`same_size_transform` type** — the hardest category
2. **Large grids** (14×9 to 21×21) — more cells = more failure surface
3. **Conditional color mappings** — model can't determine when color changes vs stays
4. **`topo_neutral` in 43% of failures** — no topological signal to guide reasoning

---

## Changes Made This Session (2026-03-26)

### 1. Color Mapping Analysis (k_factor.py)
`analyze_color_mappings(task)` — detects per-color transforms:
- Direct swaps (color A always → color B, >95% confidence)
- Conditional mappings (color A → B or C depending on context)
- Preserved colors
- Surfaced in seed and mutation prompts as `IMPORTANT COLOR RULE` and `CONDITIONAL`

### 2. Cell-Level Diff in Prompts (evo_solver.py)
- **Seed prompts** now show exact cell changes for same-size grids: `(row,col): old→new`
- **Mutation prompts** show exact wrong cells: `(row,col): got X, expected Y`
- Capped at 20-30 cells to avoid prompt bloat

### 3. Improved Topo Neutral (topo_features.py)
When topology gives zero signal, now checks:
- Symmetry changes: `creates_symmetry`, `breaks_symmetry`, `modifies_symmetry`
- Positional rearrangement: `rearrangement` (same color counts, different positions)
- Result: `topo_neutral` dropped from 42% to 29% of tasks

### 4. Anti-Overfitting Detection (evo_solver.py)
`_looks_hardcoded()` — checks if generated code contains literal output grid data. Penalizes fitness to 0.9 (still high, but won't be declared "solved").

### 5. Analysis Context in Mutation Prompts (evo_solver.py)
Mutation prompts now include K-Factor type and color mapping info, not just the failing code/examples.

### 6. Timeout Increase
`timeout_per_task`: 120s → 300s. The old timeout killed evolution mid-run on tasks that needed it.

### 7. Empty Population Guard (evo_solver.py)
Graceful handling when all seeds fail (API error, etc.) instead of crashing.

---

## Evo Solver Architecture

```
Phase 0: DSL fast-path (catches ~27 easy tasks for free, 0 API calls)
Phase 1: Seed 4 candidates with diverse strategies (objects/rules/symmetry/counting/topology)
Phase 2: Evolution loop (up to 6 gens, 20 LLM calls max)
  - Tournament selection + elite preservation (top 2)
  - Mutation: LLM sees failing examples + current code + cell diff → fix
  - Crossover (30%): LLM combines two complementary candidates
  - Stagnation detection: inject fresh seed after 2 flat gens
Phase 3: Return best candidate
```

Config: `EvoConfig` dataclass — population 8, 6 gens, 2 elite, 4 seeds, 20 call budget, 300s timeout.

---

## LLM Call Setup

### System Prompt: Shape × Scale Decomposition Framework (4,571 chars, ~1,142 tokens)

The master system prompt (`SYSTEM_PROMPT` in `llm_solver.py`) encodes a structured analysis framework derived from the Void Framework's math apparatus:

1. **Shape × Scale Decomposition** (from K-Factorization §136): every transform factors into abstract structure change vs concrete realization change
2. **Mandatory Analysis Steps**: dimensional analysis → color census → topological inventory → symmetry/periodicity → object-level analysis
3. **12 Common Archetypes**: flood fill, gravity, pattern completion, stamping, conditional recoloring, scaling, extraction, overlay, borders, counting→dimensions, relative position rules, Kronecker products
4. **Anti-Patterns**: explicit warnings against hardcoding, fixed-size assumptions, stack-overflow recursion

Per-operation prompts build on this:

| Operation | System Prompt | Temp | Purpose |
|-----------|--------------|------|---------|
| Seeds | Master framework (4,571 chars) | 0.7 | Structured analysis + diverse exploration |
| Mutations | Debugging framework — diff-based diagnosis, 6-step checklist | 0.5 | Precise fixing |
| Crossovers | Synthesis framework — find unified rule, don't if-else | 0.6 | Merge approaches |

Model configurable via `ARC_MODEL` env var (default: `claude-sonnet-4-20250514`).

---

## Grounding Signal Quality (updated)

**K-Factor `classify_transform()`** — decent:
- `fill_or_mark`: 24% — useful
- `same_size_transform`: 34% — too vague (majority of failures fall here)
- `crop_or_extract`: 11% — useful
- `recolor_or_rearrange`: 10% — useful
- Scaling types: 6% — very useful

**Topo `classify_topo()`** — improved (was 42% neutral, now 29%):
- `topo_neutral`: 29% (was 42%)
- `input_has_holes`: 29%
- `density_preserved`: 17%
- `creates_symmetry`: 7% (NEW)
- `merges_objects`: 11%

**Color `analyze_color_mappings()`** — NEW:
- Direct swaps detected with >95% confidence
- Conditional mappings surfaced with per-target percentages
- Both types surfaced in seed + mutation prompts

---

## Recommended Next Steps (priority order)

1. **Top up API credits** and run full 50-task eval to get stable accuracy estimate
2. **A/B test grounding** — run 50 tasks without color/topo hints, compare accuracy
3. **Extended thinking** — try Claude with thinking blocks for harder tasks
4. **Multi-attempt** — run 8 independent attempts per task, take any success (Imbue approach). Parallelize with asyncio.
5. **Smarter `same_size_transform` classification** — this bucket is too large. Sub-classify into filling, pattern completion, rule application, etc.
6. **Better crossover selection** — currently picks the candidate with most complementary examples. Should also consider diverse strategies.

---

## Cost Analysis

From the 19-task run:
- Total LLM calls: ~130 (avg 7.6/task for non-DSL tasks)
- DSL tasks: 0 calls (free)
- Seed-solved tasks: 4 calls
- Evolution-solved tasks: 5-14 calls
- Unsolved tasks: 20 calls (hit budget)
- Estimated cost for 400 tasks at Sonnet pricing: ~$30-50

---

## File Inventory

```
ops/lab/arc-agi/
├── HANDOFF.md          ← this file
├── README.md           ← overview + usage
├── loader.py           ← Grid, Task, load_task(), task_ids(), visualization
├── dsl.py              ← 40+ grid primitives
├── solver.py           ← brute-force DSL (5.0%)
├── smart_solver.py     ← K-Factor guided DSL (6.8%)
├── k_factor.py         ← K-Factorization + color mapping analysis
├── topo_features.py    ← Topology + symmetry/rearrangement detection
├── llm_solver.py       ← Claude API: call_llm, SYSTEM_PROMPT, extract_code
├── evo_solver.py       ← Evolutionary solver: 63.2% on 19 tasks
├── data/
│   └── ARC-AGI/        ← cloned from fchollet/ARC-AGI
│       └── data/
│           ├── training/    ← 400 ARC-AGI training tasks (JSON)
│           └── evaluation/  ← 400 ARC-AGI eval tasks (JSON)
├── results/
│   └── eval-50-v2.log  ← first eval run log
├── notebooks/          ← (empty)
└── solvers/            ← (empty)
```
