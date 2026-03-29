# ARC-AGI Exploration

Void Framework approach to the Abstraction and Reasoning Corpus.

## Architecture

```
loader.py        # Task loading, Grid class, visualization
dsl.py           # 40+ grid primitives (rotate, tile, crop, objects, etc.)
solver.py        # Brute-force hypothesis search (5.0% baseline)
k_factor.py      # K-Factorization grid decomposition & transform classification (§136)
topo_features.py # Topological + percolation features (§73, §156)
smart_solver.py  # K-Factor-guided solver (6.8% — 27/400)
llm_solver.py    # Claude API-powered solver with DSL fallback
evo_solver.py    # Evolutionary code evolution (Darwinian approach)
```

## Results

| Solver | Accuracy | Time | Notes |
|--------|----------|------|-------|
| DSL brute-force | 5.0% (20/400) | 1.5s | Pure hypothesis enumeration |
| K-Factor guided | 6.8% (27/400) | 1.8s | Classification-directed search |
| LLM hybrid | TBD | ~API | DSL first, Claude fallback |
| Evolutionary | TBD | ~API | Population-based code evolution (Imbue-inspired) |

## Key Insight

K-Factorization (§136) separates **shape** from **scale**. Applied to ARC:
- Tasks that change grid size are scale operations → small hypothesis space
- Tasks that preserve size are shape operations → need deeper reasoning
- The `classify_transform()` function acts as a barrier detector

## Usage

```bash
# Solve one task
python smart_solver.py 007bbfb7

# Evaluate all 400 training tasks
python smart_solver.py eval --verbose

# K-Factor analysis of a task
python k_factor.py 007bbfb7

# LLM solver (needs ANTHROPIC_API_KEY)
ANTHROPIC_API_KEY=sk-... python llm_solver.py 10

# Evolutionary solver — the meta
ANTHROPIC_API_KEY=sk-... python evo_solver.py 00d62c1b -v   # single task
ANTHROPIC_API_KEY=sk-... python evo_solver.py eval 50 -v    # batch eval
```

## Evolutionary Solver Design

Inspired by Imbue's Darwinian Evolver (95.1% ARC-AGI-2):

1. **DSL fast path** — catch easy tasks for free (6.8%, 0 API calls)
2. **Seed** — 4 diverse LLM-generated candidates (objects/rules/symmetry/counting strategies)
3. **Score** — partial credit fitness (cell-level accuracy, not binary)
4. **Select** — tournament selection + elite preservation
5. **Mutate** — LLM sees failing examples + current code → generates fix
6. **Crossover** — LLM combines two complementary candidates
7. **Repeat** — up to 6 generations, 20 LLM calls max per task

K-Factor (§136) + topological (§73, §156) classification feeds into seed prompts as structural hints.

## Math Apparatus Applied

| Section | Feature | What it gives ARC |
|---------|---------|-------------------|
| §136 K-Factorization | `classify_transform()` | Shape/scale separation, transform type |
| §73 Topology | `euler_characteristic()`, `count_holes()`, `object_topology()` | Components, holes, genus, compactness |
| §156 Percolation | `spans_grid()`, `occupation_density()`, `largest_cluster_frac()` | Connectivity, spanning clusters, density |

Survey of 400 training tasks:
- 47% topologically neutral (no topo change)
- 25% have holes in input (fill candidates)
- 20% preserve density exactly
- 12% preserve boundary length
- 8% merge objects, 4% split objects

---

## ARC-AGI-3 (Interactive Games)

Released 2026-03-24. **135 interactive mini-games**, 64×64 grids, 16 colors, 7 actions. No rules given — discover by playing. Scored by RHAE (quadratic penalty on excess actions vs human baseline).

Full handoff: **`v3/HANDOFF.md`**

### Architecture

```
v3/
├── packet_probe.py         # Phase 0: 30-action GameProfile fingerprint
├── packet_analyzer.py      # K-Factor, FFT, entropy, XOR signatures
├── packet_solver.py        # 4-strategy dispatcher (1/182 levels)
├── recursive_solver.py     # Fisher/GF(2)/Crooks self-improving loop (1/182)
├── spectral_engine.py      # 9 math-apparatus engines (diagnostic)
├── instanton_planner.py    # Novel compile-not-search planner (1/176)
├── void_agent.py           # LLM-guided SCRY/BIND/CAST
└── void_math_agent.py      # Zero-LLM greedy agent
```

### Key Result

Byte-level analysis (zero LLM) classifies all 25 public games, discovers their rules (nibble vocab, XOR templates, GF(2) rank), and detects determinism + cycles. Three different solvers crack three different games. **Next step: ensemble + LLM hybrid.**
