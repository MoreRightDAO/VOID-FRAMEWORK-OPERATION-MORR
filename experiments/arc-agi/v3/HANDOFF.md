# ARC-AGI-3 Byte-Level Solver — Handoff v6

**Date:** 2026-03-29
**Status:** 16 modules, ~15K lines. **LLM-first architecture**: Maestro dispatches LLM as primary solver for keyboard_click games (13/25), physics engines provide structured context. Game Sense module gives LLM visual grid rendering, pattern detection, action diaries, and diff views. Registered API key: `79d0e78f-28b6-450c-83d2-5303dc4c3712`. **Blocked on LLM credits** (OpenAI quota exceeded, no Anthropic key).

---

## What's New (v6 — 2026-03-29)

### Game Sense (`game_sense.py`) — Pro Gamer Eyes for the LLM

**The core insight:** The LLM is the brain. Everything else is infrastructure to make it play better.

**Five capabilities:**
1. **Visual grid renderer** — ASCII maps at 32x32 or 16x16 resolution using mode-pooling (not max-pool, preserves visual appearance). Color-coded character mapping.
2. **Diff renderer** — shows exactly what changed after each action. Changed cells highlighted, bounding box reported.
3. **Action effect tracker** — records what each action does in plain English ("small object moved near (10,10)", "color 3→5 (12 cells)", "TOGGLE pattern"). Maintains full action diary with φ deltas.
4. **Pattern detector** — recognizes 7 common game types from grid structure + action history: MAZE/NAVIGATION, TOGGLE/LIGHTS, MATCH/CLEAR, FLOOD FILL, SOKOBAN/PUSH, SEQUENCE/RHYTHM, PAINTING/DRAWING. Each with confidence score and strategy hint.
5. **Game diary** — persistent memory: discovered rules, winning strategies, failed approaches, key observations. Carries across levels and attempts.

**Wired into:** `llm_hybrid.py` — HybridSolver now builds game_sense context alongside framework context, giving the LLM a complete visual+analytical view of every game state.

### LLM as Primary Solver

**Maestro now dispatches LLM first for keyboard_click games** (13/25 games). Physics solvers are fallbacks.

**Solver order for keyboard_click:** `llm > eckert > instanton > aaa > recursive > packet`

### Enhanced Action Parser

`parse_plan()` now handles mixed keyboard+click plans:
- `PLAN: 1, 1, 3, 6@32,16, 2, 6@40,20, 4` → `[1, 1, 3, (6,32,16), 2, (6,40,20), 4]`
- Also handles: `click(x,y)`, numbered lists, markdown code blocks

### LLM Retry/Resilience

`call_llm()` now retries with exponential backoff (2s, 4s, 8s) on 429/500/502/503 errors.

### API Key

ARC registered key saved to `ops/lab/arc-agi/v3/.env`:
```
ARC_API_KEY=79d0e78f-28b6-450c-83d2-5303dc4c3712
```

**Blocker:** OpenAI account has zero credits. Anthropic key not set. When credits are available:
```bash
export ARC_API_KEY=79d0e78f-28b6-450c-83d2-5303dc4c3712
export OPENAI_API_KEY=<key>
export ARC_BACKEND=openai
export ARC_MODEL=o4-mini
python3 maestro.py --all -v --attempts 2 --budget 500
```

---

## What's New (v5 — 2026-03-29)

### Maestro (`maestro.py`) — The Conductor

**The core problem:** Solvers run independently, each creating fresh state objects (TransitionMemory, CellManifold, KGrammar, etc), throwing everything away between runs. No meta-controller decides WHEN to switch, WHAT to share, or HOW MUCH budget each solver gets. No persistent memory across sessions.

**The solution:** A meta-orchestrator that uses the Eckert manifold as the conducting surface.

**Architecture:**
```
                    ┌──────────────────────────┐
                    │       MAESTRO            │
                    │  SharedState (all solvers)│
                    │  GameLedger (per-game)    │
                    │  CrossGameLedger (global) │
                    └──────┬──────────────┬────┘
            ┌──────────────┤   CONDUCTS   ├──────────────┐
     ┌──────▼──┐    ┌──────▼──┐    ┌──────▼──┐    ┌─────▼───┐
     │ Packet  │    │ Eckert  │    │Instanton│    │  AAA    │
     └─────────┘    └─────────┘    └─────────┘    └─────────┘
```

**Three conducting phases:**
1. **EXPLORE** (barrier × 10 actions): run top 2 solvers maximizing novelty, share knowledge
2. **EXPLOIT** (remaining − reserve): run solver with steepest φ gradient (JKO conducting)
3. **COMPILE** (10% reserve): instanton toward φ-minimum target

**Kill switches:**
- Fantasia saturation > 0.95 → pull solver
- φ stall > 5 steps → increase temperature, switch
- Holonomy novelty < 0.01 → redundant exploration

**New files:**
| File | Lines | Purpose |
|------|-------|---------|
| `maestro.py` | ~420 | The conductor — CLI + Maestro class |
| `shared_state.py` | ~370 | SharedState + GameLedger + CrossGameLedger |
| `eckert_math.py` | ~280 | Clean reusable Eckert math functions |
| `ledger/` | (auto) | Persistent JSON per game + global transfer |

**Solver modifications:** All 5 solvers now accept `shared_state=None` parameter. When provided, they use shared TransitionMemory, CellManifold, KGrammar, MacroLibrary, SpectralNavigator, EckertWinDetector. When None, behavior is identical (zero regression).

**Persistent learning:** GameLedger stores transitions, mechanisms, macros, Fisher maps, φ trajectories, strategy fitness to JSON. CrossGameLedger tracks strategy success per game type and transfers mechanism atoms across games.

**Usage:**
```bash
python3 maestro.py --all -q --compete     # Competition mode
python3 maestro.py --all -q               # Full eval mode
python3 maestro.py cd82 -v                # Single game, verbose
python3 maestro.py --all --attempts 3     # Multi-attempt learning
python3 maestro.py --all --fresh          # Ignore ledger, start fresh
```

### Reusable Math (`eckert_math.py`)

Pure functions, no solver dependencies:
- `pe_from_coordinates(O, R, α, K)` — Pe from manifold coordinates
- `fisher_distance(p, q)` — Čencov-unique distance
- `coordination_barrier(n)` — π/√2 × N exploration cost
- `holonomy_deficit(O_path, R_path, α_path)` — geometric memory (NEW)
- `jko_gradient(φ_trajectory)` — steepness of thermodynamic descent (NEW)
- `pade_extrapolate(trajectory)` — convergence prediction from early data (NEW)
- `pid_decompose(new, shared)` — unique/redundant/synergistic information (NEW)
- `chebyshev_fingerprint(grid)` — game similarity embedding
- `fantasia_saturation(H_Y, I_D_Y, I_M_Y)` — explore/exploit gate

---

## What's New (v4 — 2026-03-29)

### EckertWinDetector (`eckert_win_detector.py`) — Universal Progress Oracle

**The core problem:** Solvers learn game physics perfectly but can't infer win conditions. The Eckert simulator reaches pred_acc=1.0 yet solves 0 levels. ls20 reaches entropy=0.000 yet doesn't win. Goal-guessing (10 hardcoded hypotheses) covers only ~3-4 game types.

**The solution:** A physics-derived progress function φ(state)→[0,1] that measures "how close to winning" from game dynamics alone, no goal guessing needed.

**Thesis:** Win state = where Pe → minimum. At the win state: rules transparent (O→0), outcome invariant (R→0), system independent (α→0). Navigate DOWN the Pe gradient.

**Seven thermodynamic signals:**

| # | Signal | Weight | What it measures |
|---|--------|--------|-----------------|
| 1 | Pe gradient | 0.25 | Distance from Pe minimum on manifold |
| 2 | Free energy | 0.20 | F = E - TS; win state minimizes F |
| 3 | Spectral gap | 0.12 | λ₁ of transition matrix; large = near attractor |
| 4 | Absorption | 0.13 | Low out-degree = terminal state |
| 5 | Crooks gates | 0.10 | Irreversible transitions = milestones |
| 6 | Complexity | 0.12 | zlib ratio descent toward simplicity |
| 7 | Cycle escape | 0.08 | Breaking out of detected cycles |

**Key classes:**
- `EckertWinDetector` — main: observe()/progress()/score_state()/best_action()/is_stuck()
- `TransitionGraph` — sparse Markov chain: spectral gap, absorption, Crooks, cycles
- `PhiScorer` — drop-in replacement for GoalUtilityScorer in aaa_solver
- `phi_fitness()` — fitness function for replicator dynamics in self_learner
- `phi_beam_search()` — beam search scoring by φ instead of entropy
- `pe_minimum_target()` — find compile target for instanton planner

**Wired into all 5 major solvers:**
- `eckert_simulator.py`: detector in EckertSimulator, φ-guided exploit actions, φ stall detection
- `aaa_solver.py`: PhiScorer replaces GoalUtilityScorer when detector has 10+ observations
- `instanton_planner.py`: φ beam search before entropy beam, detector fed from transitions
- `ensemble_solver.py`: final_phi tracked and displayed per solver
- `self_learner.py`: φ imported for strategy fitness

**Observed φ values (first run, 2026-03-29):**
- g50t: φ=0.714 (highest — most progress toward winning)
- cd82: φ=0.599
- tn36: φ=0.610
- su15: φ=0.350 (lowest — stuck early)
- Range: 0.35-0.71 across 25 games

---

## What Exists

### The Stack (12 files in `ops/lab/arc-agi/v3/`)

| File | Lines | What | Novel? |
|------|-------|------|--------|
| `packet_probe.py` | 665 | Phase 0: 30-action game fingerprinting → `GameProfile` | Game type classifier from byte patterns |
| `packet_analyzer.py` | 790 | Deep session analysis: K-Factor, FFT, barrier detection | XOR signature fingerprinting |
| `packet_solver.py` | 655 | 4 dispatched strategies: GreedyNav, ClickScan, Field, DeepScan | Strategy dispatch from profile |
| `recursive_solver.py` | 884 | Fisher + GF(2) vector space + Crooks + K-Grammar | Self-improving loop via Fisher info |
| `spectral_engine.py` | 970 | Full math apparatus: 9 self-improving engines | Chebyshev grammar, replicator dynamics, Kramers potential |
| `instanton_planner.py` | ~1020 | XOR telescope + compile-not-search + **φ beam search** | Compile-not-search + φ guidance |
| `eckert_simulator.py` | ~1850 | Physics-based forward model + **φ-guided action selection** | Eckert manifold, K-Fact rules, Kramers, geodesic planning |
| `eckert_win_detector.py` | ~530 | **NEW** Universal thermodynamic progress oracle | 7 signals, TransitionGraph, PhiScorer |
| `ensemble_solver.py` | ~360 | Profile-based dispatch, 6 solvers, **φ tracking** | φ-based progress monitoring |
| `aaa_solver.py` | ~930 | MCTS + Fisher influence maps + **PhiScorer** | Telescope rollouts, φ value function |
| `llm_hybrid.py` | 520 | Framework-grounded LLM planning (OpenAI/Anthropic) | Byte-level diagnostics as structured LLM context |
| `fisher_pathfinder.py` | 310 | Information-geometric A* pathfinding | Fisher geodesics (§138), K-Factor wall detection |
| `self_learner.py` | ~820 | Multi-attempt self-learning + **φ fitness** | Replicator dynamics, cross-attempt memory |

### Results

| Solver | Game | Type | Levels |
|--------|------|------|--------|
| packet_solver | tn36 | CLICK-ONLY, det, v=5, t=8 | 1/7 |
| instanton_planner | r11l | CLICK-ONLY, det, v=18, t=11 | 1/6 |
| recursive_solver | lp85 | LOCKED, !det, v=21, t=3 | 1/8 |
| **Total** | | | **3/182** |

---

## The Gap & Next Steps (Priority Order)

### 1. TUNE φ WEIGHTS + ADD GAME-TYPE SPECIALIZATION

Current weights are initial estimates. Analysis needed:
- Run all 25 games, collect φ trajectory per game
- Cluster games by φ behavior (fast rise → plateau vs slow climb vs stuck)
- Tune weights per game type (CLICK-ONLY, AGENT-KB, FIELD, LOCKED, MIXED)
- Key hypothesis: games with φ>0.6 but 0 solves are closest to cracking

### 2. CYCLE ESCAPE AS PRIMARY STRATEGY

16/25 games have cycles. Current cycle detection finds them but doesn't exploit them. Strategy:
- For each detected cycle, identify the ESCAPE action (Kramers barrier crossing)
- Compute instanton for cycle escape: compile XOR(in-cycle, out-of-cycle)
- Budget allocation: spend coordination barrier (N×π/√2) on each cycle escape

### 3. COMPLETE TRANSITION TABLE FOR DETERMINISTIC GAMES

14/25 games are deterministic FSMs. With enough exploration the MechanismTable becomes COMPLETE. Then forward sim is exact → MCTS with perfect dynamics (MuZero). The φ detector's free_energy signal would become precise.

### 4. STRONGER COMPILE TARGETS

The instanton planner compiles XOR transformations but targets entropy minimum. Replace with φ minimum target:
- `pe_minimum_target()` finds state with best (low Pe + low entropy + high absorption)
- Compile XOR from current state to φ-minimum state
- This is "compute the move that takes you closest to winning" as linear algebra

### 5. WIN CONDITION ANALYSIS FROM SOLVED GAMES

We solve 3 levels. Analyze WHAT made them win:
- Record the exact winning frame transition
- Fisher map of the winning step: WHERE did the win trigger?
- Generalize: what pattern do winning states share?

---

## Quick Start

```bash
cd ops/lab/arc-agi/v3
export OPENAI_API_KEY=$(grep OPENAI_API_KEY /data/apps/morr/private/secrets/keys.env | cut -d= -f2)

# Competition mode (fastest, 1 solver/game)
python3 ensemble_solver.py --all -q --compete

# Eval mode (2 solvers/game, more thorough)
python3 ensemble_solver.py --all -q --max-solvers 2

# Eckert simulator with φ diagnostics
python3 eckert_simulator.py --all --diag

# Self-learning loop
python3 self_learner.py --all --attempts 3 -q

# Individual solvers
python3 packet_solver.py --all -q
python3 recursive_solver.py --all -q
python3 instanton_planner.py --all -q
python3 aaa_solver.py --all -q
```

---

## Cost

- Zero-LLM solvers (ensemble, MCTS, spectral, eckert): $0
- Self-learner with LLM: ~$0.50-1.00 per 25-game eval (o4-mini, ~6 calls/game)
- Full LLM hybrid: ~$2-5 per 25-game eval
