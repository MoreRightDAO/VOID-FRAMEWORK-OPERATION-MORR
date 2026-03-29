"""Evolutionary ARC-AGI solver — Darwinian code evolution.

Inspired by Imbue's approach (95.1% ARC-AGI-2):
1. Seed population with diverse candidate transforms (LLM-generated)
2. Score each candidate against training pairs (partial credit)
3. Select top candidates
4. Mutate via LLM (ask it to fix/improve failing code)
5. Crossover: combine ideas from multiple candidates
6. Repeat until a candidate passes all training pairs

Key insight: partial scoring lets evolution make incremental progress.
A transform that gets 2/3 examples right is close — one mutation away.
"""
import json
import hashlib
import os
import sys
import time
import random
import traceback
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Optional, Callable

import numpy as np

from loader import Task, Grid, load_task, load_all, task_ids
from dsl import *
from solver import verify_on_train, apply_to_test
from k_factor import classify_transform, shape_signature, scale_params, analyze_color_mappings
from topo_features import classify_topo, topo_features
from llm_solver import call_llm, extract_code, compile_transform, grid_to_text, API_KEY, BACKEND, MODEL


# ─── Configuration ───────────────────────────────────────────────

@dataclass
class EvoConfig:
    """Evolution hyperparameters."""
    population_size: int = 8        # candidates per generation
    max_generations: int = 6        # evolution rounds
    elite_count: int = 2            # top candidates preserved unchanged
    mutation_temp: float = 0.8      # LLM temperature for mutations
    crossover_rate: float = 0.3     # probability of crossover vs mutation
    seed_count: int = 4             # initial LLM-seeded candidates
    timeout_per_task: float = 300.0 # seconds per task
    max_llm_calls: int = 20        # budget per task


# ─── Candidate representation ───────────────────────────────────

@dataclass
class Candidate:
    """A candidate transform program."""
    code: str                       # Python source code
    fitness: float = 0.0            # 0.0 to 1.0 (fraction of training pairs correct)
    example_scores: list = field(default_factory=list)  # per-example scores
    generation: int = 0
    parent_id: str = ""
    method: str = "seed"            # seed, mutate, crossover, dsl

    @property
    def id(self) -> str:
        return hashlib.md5(self.code.encode()).hexdigest()[:8]

    def compile(self) -> Optional[Callable]:
        """Compile code into a callable. Returns None on failure."""
        try:
            raw_fn = compile_transform(self.code)
            def transform(g: Grid) -> Grid:
                result = raw_fn(g.to_list())
                return Grid(result)
            return transform
        except Exception:
            return None


# ─── Fitness evaluation ──────────────────────────────────────────

def _looks_hardcoded(code: str, task: Task) -> bool:
    """Check if code likely hardcodes training outputs rather than learning the rule.

    Red flags: contains literal output grid data, or if-elif chains matching inputs.
    """
    # Check if any training output grid appears literally in the code
    for _, out in task.train:
        row_str = str(out.data)
        if row_str in code:
            return True
        # Also check for individual rows being hardcoded (common overfitting pattern)
        hardcoded_rows = sum(1 for row in out.data if str(row) in code)
        if hardcoded_rows >= max(2, out.h // 2):
            return True
    return False


def score_candidate(candidate: Candidate, task: Task) -> float:
    """Score a candidate against training pairs.

    Returns fraction correct (0.0 to 1.0).
    Partial credit: each correct example contributes 1/n_train.
    Cell-level partial credit for almost-right answers.
    """
    transform = candidate.compile()
    if transform is None:
        candidate.fitness = 0.0
        candidate.example_scores = [0.0] * len(task.train)
        return 0.0

    scores = []
    for inp, expected in task.train:
        try:
            result = transform(inp)
            if result == expected:
                scores.append(1.0)
            elif result.h == expected.h and result.w == expected.w:
                # Partial credit: fraction of cells correct
                total = expected.h * expected.w
                correct = sum(
                    1 for r in range(expected.h) for c in range(expected.w)
                    if result.data[r][c] == expected.data[r][c]
                )
                scores.append(0.5 * correct / total)  # max 0.5 for partial
            else:
                # Wrong dimensions — tiny credit if close
                size_ratio = min(result.h * result.w, expected.h * expected.w) / \
                             max(result.h * result.w, expected.h * expected.w, 1)
                scores.append(0.1 * size_ratio)
        except Exception:
            scores.append(0.0)

    candidate.fitness = sum(scores) / len(scores) if scores else 0.0
    candidate.example_scores = scores

    # Penalize likely hardcoded solutions
    if candidate.fitness >= 1.0 and _looks_hardcoded(candidate.code, task):
        candidate.fitness = 0.9  # still high but won't be declared "solved"

    return candidate.fitness


# ─── Seed generation ─────────────────────────────────────────────

def build_seed_prompt(task: Task) -> str:
    """Build prompt for initial seed generation."""
    parts = []
    parts.append("You are solving an ARC-AGI puzzle. Each puzzle has input→output grid pairs.")
    parts.append("Grids use digits 0-9 as colors (0 is usually background/black).")
    parts.append("")

    for i, (inp, out) in enumerate(task.train):
        parts.append(f"=== Example {i+1} ===")
        parts.append(f"Input ({inp.h}×{inp.w}):")
        parts.append(grid_to_text(inp))
        parts.append(f"Output ({out.h}×{out.w}):")
        parts.append(grid_to_text(out))

        # Compact cell-diff for same-size grids
        if inp.h == out.h and inp.w == out.w:
            changes = []
            for r in range(inp.h):
                for c in range(inp.w):
                    if inp.data[r][c] != out.data[r][c]:
                        changes.append((r, c, inp.data[r][c], out.data[r][c]))
            if changes and len(changes) <= 20:
                parts.append(f"Changes ({len(changes)} cells):")
                for r, c, old, new in changes:
                    parts.append(f"  ({r},{c}): {old}→{new}")
            elif changes:
                parts.append(f"Changes: {len(changes)} of {inp.h*inp.w} cells differ")
        parts.append("")

    # Add K-Factor classification hint
    cls = classify_transform(task)
    parts.append(f"Analysis: transform type = {cls['type']}, size ratio = {cls['size_ratio']}")
    parts.append(f"  same_size={cls['always_same_size']}, preserves_objects={cls['preserves_objects']}")
    parts.append(f"  preserves_colors={cls['preserves_colors']}")

    # Add color mapping analysis
    color_info = analyze_color_mappings(task)
    if color_info["description"]:
        parts.append(f"  color_analysis: {color_info['description']}")
    if color_info.get("has_direct_swap"):
        maps = color_info["mappings"]
        swap_detail = [f"{ic}→{m['dominant_target']}" for ic, m in maps.items()
                      if not m["preserved"] and m["confidence"] > 0.95]
        if swap_detail:
            parts.append(f"  IMPORTANT COLOR RULE: {', '.join(swap_detail)}")
    if color_info.get("has_conditional"):
        maps = color_info["mappings"]
        for ic, m in maps.items():
            if m["confidence"] <= 0.95 and not m["preserved"]:
                targets = [f"color {oc} ({pct:.0%})" for oc, pct in m["all_targets"].items() if pct > 0.05]
                parts.append(f"  CONDITIONAL: color {ic} maps to {' or '.join(targets)} depending on context")

    # Add topological hints (§73 + §156)
    topo = classify_topo(task)
    tags = topo["tags"]
    parts.append(f"  topo_tags={tags}")
    if "input_has_holes" in tags:
        parts.append("  NOTE: Input grids contain enclosed holes (background regions surrounded by foreground)")
    if "fills_holes" in tags:
        parts.append("  NOTE: Transform FILLS holes — enclosed regions get a new color")
    if "merges_objects" in tags:
        parts.append("  NOTE: Transform merges/connects separate objects")
    if "splits_objects" in tags:
        parts.append("  NOTE: Transform splits objects into parts")
    if "grows" in tags:
        parts.append("  NOTE: Transform increases density (adds cells)")
    if "density_preserved" in tags:
        parts.append("  NOTE: Density is preserved — same number of non-bg cells in/out")
    if "creates_symmetry" in tags:
        parts.append("  NOTE: Transform CREATES symmetry — output is more symmetric than input")
    if "rearrangement" in tags:
        parts.append("  NOTE: Transform REARRANGES cells — same color counts, different positions (gravity/sorting/sliding)")
    parts.append("")

    parts.append("Write a Python function `transform(grid: list[list[int]]) -> list[list[int]]`")
    parts.append("that implements the transformation rule. `numpy` is available as `np`.")
    parts.append("Return ONLY the function in ```python``` markers.")

    return "\n".join(parts)


def build_diverse_seed_prompt(task: Task, strategy: str) -> str:
    """Build prompt with a specific reasoning strategy."""
    base = build_seed_prompt(task)

    strategies = {
        "objects": "\n\nApproach: Think about this in terms of OBJECTS. "
                   "What are the distinct objects in each grid? How do they move, change, or interact?",
        "rules": "\n\nApproach: Think about this as a SET OF RULES. "
                 "What simple if-then rules could map each input cell to the output?",
        "symmetry": "\n\nApproach: Think about SYMMETRY and PATTERNS. "
                    "What symmetries exist? What repeating patterns? Is there tiling, mirroring, or rotation?",
        "counting": "\n\nApproach: Think about COUNTING and ARITHMETIC. "
                    "Count colors, objects, rows, columns. Is there a numeric relationship?",
        "topology": "\n\nApproach: Think about TOPOLOGY and CONNECTIVITY. "
                    "What are the connected components? Are there enclosed holes? "
                    "Does the transform fill regions, connect components, or change boundaries? "
                    "Think about flood fill, border detection, and enclosed areas.",
    }

    return base + strategies.get(strategy, "")


def generate_seeds(task: Task, n: int, verbose: bool = False) -> list[Candidate]:
    """Generate initial population via diverse LLM prompts."""
    candidates = []
    strategies = ["objects", "rules", "symmetry", "counting", "topology"]

    for i in range(n):
        strategy = strategies[i % len(strategies)]
        prompt = build_diverse_seed_prompt(task, strategy)

        try:
            if verbose:
                print(f"  Seeding ({strategy})...")
            response = call_llm(prompt, temperature=0.7)  # uses SYSTEM_PROMPT from llm_solver
            code = extract_code(response)
            c = Candidate(code=code, generation=0, method=f"seed:{strategy}")
            candidates.append(c)
        except Exception as e:
            if verbose:
                print(f"  Seed failed: {e}")

    return candidates


# ─── Mutation ────────────────────────────────────────────────────

def build_mutation_prompt(task: Task, parent: Candidate, all_candidates: list[Candidate]) -> str:
    """Build prompt to mutate a candidate based on its failures."""
    parts = []
    parts.append("The current function gets some examples right but not all. Fix it.")
    parts.append("")

    # Show task
    for i, (inp, out) in enumerate(task.train):
        status = "✓" if parent.example_scores[i] >= 1.0 else "✗"
        parts.append(f"=== Example {i+1} [{status}] ===")
        parts.append(f"Input ({inp.h}×{inp.w}):")
        parts.append(grid_to_text(inp))
        parts.append(f"Output ({out.h}×{out.w}):")
        parts.append(grid_to_text(out))

        # Show what the current code produces for failing examples
        if parent.example_scores[i] < 1.0:
            transform = parent.compile()
            if transform:
                try:
                    result = transform(inp)
                    parts.append(f"Current output ({result.h}×{result.w}):")
                    parts.append(grid_to_text(result))

                    # Cell-level diff for same-size grids
                    if result.h == out.h and result.w == out.w:
                        wrong_cells = []
                        for r in range(out.h):
                            for c in range(out.w):
                                if result.data[r][c] != out.data[r][c]:
                                    wrong_cells.append((r, c, result.data[r][c], out.data[r][c]))
                        if wrong_cells and len(wrong_cells) <= 30:
                            parts.append(f"DIFF ({len(wrong_cells)} wrong cells):")
                            for r, c, got, expected_val in wrong_cells:
                                parts.append(f"  ({r},{c}): got {got}, expected {expected_val}")
                        elif wrong_cells:
                            parts.append(f"DIFF: {len(wrong_cells)} cells wrong out of {out.h*out.w}")
                    elif result.h != out.h or result.w != out.w:
                        parts.append(f"SIZE MISMATCH: got {result.h}×{result.w}, expected {out.h}×{out.w}")
                except Exception as e:
                    parts.append(f"Current output: ERROR - {e}")
        parts.append("")

    # Include analysis context
    cls = classify_transform(task)
    parts.append(f"Analysis: type={cls['type']}, same_size={cls['always_same_size']}")
    color_info = analyze_color_mappings(task)
    if color_info["description"]:
        parts.append(f"Color info: {color_info['description']}")
    parts.append("")

    parts.append(f"Current code (fitness={parent.fitness:.2f}, correct={sum(1 for s in parent.example_scores if s >= 1.0)}/{len(parent.example_scores)}):")
    parts.append(f"```python\n{parent.code}\n```")
    parts.append("")

    # Show what other candidates got right (cross-pollination)
    other_insights = []
    for c in all_candidates:
        if c.id != parent.id and c.fitness > 0:
            correct_examples = [i for i, s in enumerate(c.example_scores) if s >= 1.0]
            if correct_examples:
                other_insights.append(f"  Another approach (fitness={c.fitness:.2f}) gets examples {correct_examples} right")
    if other_insights:
        parts.append("Other candidates in the population:")
        parts.extend(other_insights[:3])
        parts.append("")

    parts.append("Fix the function to handle ALL examples correctly.")
    parts.append("Return ONLY the improved function in ```python``` markers.")

    return "\n".join(parts)


def mutate(task: Task, parent: Candidate, population: list[Candidate],
           verbose: bool = False) -> Optional[Candidate]:
    """Mutate a candidate using LLM-guided improvement."""
    prompt = build_mutation_prompt(task, parent, population)

    # Mutation system prompt: structured debugging using the framework
    mutation_system = """You are debugging a partially-correct ARC-AGI grid transform function.

## Debugging Framework

1. **Identify the failure pattern**: Look at the DIFF. Are wrong cells clustered (spatial bug) or scattered (logic bug)?
2. **Check dimensional analysis**: Is the output the right size? If not, fix sizing logic first.
3. **Check color mapping**: For each wrong cell, what color did you produce vs expected? Is there a systematic color error?
4. **Check boundary conditions**: Errors often cluster at grid edges, object boundaries, or region transitions.
5. **Check object handling**: Are you finding all objects? Using the right connectivity (4 vs 8)?
6. **Check the rule generality**: Does your code work for the passing examples by accident (hardcoded values) or by genuine rule?

Common bugs: off-by-one in slicing, wrong flood fill direction, missing diagonal neighbors, incorrect color mapping, not handling objects of different sizes, assuming fixed grid dimensions.

Return ONLY the corrected function in ```python``` markers. Do NOT hardcode training outputs."""

    try:
        response = call_llm(prompt, system=mutation_system, temperature=0.5)
        code = extract_code(response)

        # Don't accept identical code
        if code.strip() == parent.code.strip():
            return None

        child = Candidate(
            code=code,
            generation=parent.generation + 1,
            parent_id=parent.id,
            method="mutate",
        )
        return child
    except Exception as e:
        if verbose:
            print(f"  Mutation failed: {e}")
        return None


# ─── Crossover ───────────────────────────────────────────────────

def build_crossover_prompt(task: Task, parent_a: Candidate, parent_b: Candidate) -> str:
    """Build prompt to combine two candidate approaches."""
    parts = []
    parts.append("Neither approach below works perfectly alone, but each gets different examples right.")
    parts.append("Combine them into one function that handles ALL examples.")
    parts.append("")

    for i, (inp, out) in enumerate(task.train):
        a_ok = "✓" if parent_a.example_scores[i] >= 1.0 else "✗"
        b_ok = "✓" if parent_b.example_scores[i] >= 1.0 else "✗"
        parts.append(f"=== Example {i+1} [A:{a_ok} B:{b_ok}] ===")
        parts.append(f"Input ({inp.h}×{inp.w}):")
        parts.append(grid_to_text(inp))
        parts.append(f"Output ({out.h}×{out.w}):")
        parts.append(grid_to_text(out))
        parts.append("")

    parts.append(f"Approach A (fitness={parent_a.fitness:.2f}):")
    parts.append(f"```python\n{parent_a.code}\n```")
    parts.append("")
    parts.append(f"Approach B (fitness={parent_b.fitness:.2f}):")
    parts.append(f"```python\n{parent_b.code}\n```")
    parts.append("")
    parts.append("Write a NEW function that combines the best ideas from both approaches")
    parts.append("to handle ALL examples correctly. Return ONLY the function in ```python``` markers.")

    return "\n".join(parts)


def crossover(task: Task, parent_a: Candidate, parent_b: Candidate,
              verbose: bool = False) -> Optional[Candidate]:
    """Crossover two candidates using LLM-guided combination."""
    prompt = build_crossover_prompt(task, parent_a, parent_b)

    # Crossover system prompt: synthesis using framework analysis
    crossover_system = """You are combining two partially-correct ARC-AGI transform functions.

## Synthesis Strategy

1. **Identify what each approach gets RIGHT**: Which examples pass? What rule does each capture?
2. **Find the common structure**: Often both approaches share 80% of the logic. The difference is in edge handling, color mapping, or boundary conditions.
3. **Check if they're complementary**: Approach A handles objects, B handles background? A does horizontal, B does vertical? Combine the conditions.
4. **Don't just if-else between them**: Merging two hardcoded branches creates brittle code. Find the UNIFIED rule that explains all examples.
5. **Prefer the simpler approach** when both handle an example correctly — simpler generalizes better.

Return ONLY the combined function in ```python``` markers. Do NOT hardcode training outputs."""

    try:
        response = call_llm(prompt, system=crossover_system, temperature=0.6)
        code = extract_code(response)

        child = Candidate(
            code=code,
            generation=max(parent_a.generation, parent_b.generation) + 1,
            parent_id=f"{parent_a.id}×{parent_b.id}",
            method="crossover",
        )
        return child
    except Exception as e:
        if verbose:
            print(f"  Crossover failed: {e}")
        return None


# ─── Main evolution loop ─────────────────────────────────────────

def evolve_task(task: Task, config: EvoConfig = None, verbose: bool = False) -> tuple[bool, list[Grid], str, dict]:
    """Run evolutionary search on a single task.

    Returns: (success, predictions, best_code, stats)
    """
    if config is None:
        config = EvoConfig()

    stats = {
        "generations": 0,
        "llm_calls": 0,
        "best_fitness_history": [],
        "total_candidates": 0,
        "method": "none",
    }

    t0 = time.time()
    llm_calls = 0

    # ── Phase 0: Quick DSL check ──
    from smart_solver import smart_solve
    dsl_result = smart_solve(task, verbose=False)
    if dsl_result is not None:
        name, predictions = dsl_result
        if verbose:
            print(f"  DSL solved: {name}")
        stats["method"] = f"dsl:{name}"
        return (True, predictions, f"# DSL: {name}", stats)

    if not API_KEY:
        if verbose:
            print("  No API key — DSL-only mode")
        return (False, [], "", stats)

    # ── Phase 1: Seed population ──
    if verbose:
        print(f"  Generating {config.seed_count} seeds...")

    population = generate_seeds(task, config.seed_count, verbose=verbose)
    llm_calls += config.seed_count

    # Score initial population
    for c in population:
        score_candidate(c, task)
        if verbose:
            print(f"    {c.id} fitness={c.fitness:.3f} [{c.method}] "
                  f"scores={[f'{s:.2f}' for s in c.example_scores]}")
        if c.fitness >= 1.0:
            predictions = apply_to_test(task, c.compile())
            stats.update(generations=0, llm_calls=llm_calls, method="seed",
                        total_candidates=len(population))
            return (True, predictions, c.code, stats)

    if not population:
        if verbose:
            print("  No seeds generated (API error?)")
        return (False, [], "", stats)

    stats["best_fitness_history"].append(max((c.fitness for c in population), default=0))

    # ── Phase 2: Evolution loop ──
    for gen in range(config.max_generations):
        if time.time() - t0 > config.timeout_per_task:
            if verbose:
                print(f"  Timeout at gen {gen}")
            break

        if llm_calls >= config.max_llm_calls:
            if verbose:
                print(f"  LLM budget exhausted at gen {gen}")
            break

        if not population:
            break

        if verbose:
            best = max(population, key=lambda c: c.fitness)
            print(f"  Gen {gen+1}: best={best.fitness:.3f} pop={len(population)}")

        # Sort by fitness
        population.sort(key=lambda c: c.fitness, reverse=True)

        # Elite preservation
        new_pop = population[:config.elite_count]

        # Generate children
        while len(new_pop) < config.population_size and llm_calls < config.max_llm_calls:
            if time.time() - t0 > config.timeout_per_task:
                break

            # Select parents (tournament selection — pick best of 2 random)
            if len(population) >= 2:
                a, b = random.sample(population[:max(4, len(population))], 2)
                parent = a if a.fitness >= b.fitness else b
            else:
                parent = population[0]

            # Crossover or mutation
            child = None
            if random.random() < config.crossover_rate and len(population) >= 2:
                # Crossover: pick two parents with complementary strengths
                other_candidates = [c for c in population if c.id != parent.id and c.fitness > 0]
                if other_candidates:
                    other = max(other_candidates, key=lambda c: sum(
                        1 for i, s in enumerate(c.example_scores)
                        if s >= 1.0 and parent.example_scores[i] < 1.0
                    ))
                    child = crossover(task, parent, other, verbose=verbose)
                    llm_calls += 1
                    if verbose and child:
                        print(f"    Crossover: {parent.id}×{other.id}")

            if child is None:
                child = mutate(task, parent, population, verbose=verbose)
                llm_calls += 1
                if verbose and child:
                    print(f"    Mutate: {parent.id} → {child.id}")

            if child is not None:
                score_candidate(child, task)
                new_pop.append(child)

                if verbose:
                    print(f"    {child.id} fitness={child.fitness:.3f} [{child.method}] "
                          f"scores={[f'{s:.2f}' for s in child.example_scores]}")

                # Early exit if we found a perfect solution
                if child.fitness >= 1.0:
                    predictions = apply_to_test(task, child.compile())
                    stats.update(
                        generations=gen + 1,
                        llm_calls=llm_calls,
                        method=child.method,
                        total_candidates=stats.get("total_candidates", 0) + len(new_pop),
                    )
                    if verbose:
                        print(f"  SOLVED at gen {gen+1} via {child.method}!")
                    return (True, predictions, child.code, stats)

        population = new_pop
        stats["total_candidates"] += len(new_pop)
        best_fitness = max((c.fitness for c in population), default=0)
        stats["best_fitness_history"].append(best_fitness)

        # Stagnation detection: if no improvement for 2 gens, inject fresh seeds
        if len(stats["best_fitness_history"]) >= 3:
            recent = stats["best_fitness_history"][-3:]
            if max(recent) - min(recent) < 0.01:
                if verbose:
                    print(f"  Stagnation detected — injecting fresh seed")
                fresh = generate_seeds(task, 1, verbose=False)
                llm_calls += 1
                for c in fresh:
                    score_candidate(c, task)
                    population.append(c)

    # ── Phase 3: Return best candidate (even if imperfect) ──
    stats.update(generations=config.max_generations, llm_calls=llm_calls)

    if population:
        best = max(population, key=lambda c: c.fitness)
        if best.fitness >= 1.0:
            predictions = apply_to_test(task, best.compile())
            stats["method"] = best.method
            return (True, predictions, best.code, stats)

    return (False, [], "", stats)


# ─── Shotgun solver (mass seeding) ────────────────────────────────

def shotgun_task(task: Task, n_attempts: int = 32, verbose: bool = False) -> tuple[bool, list, str, dict]:
    """Mass-seed a task with n_attempts independent LLM calls.

    The Greenblatt insight: more attempts > smarter attempts.
    Each attempt is independent — diverse strategies, high temperature.
    Holdout validation: if task has 3+ training examples, hold one out
    to catch overfitting before declaring success.

    Returns: (success, predictions, best_code, stats)
    """
    stats = {
        "generations": 0,
        "llm_calls": 0,
        "best_fitness_history": [],
        "total_candidates": 0,
        "method": "none",
    }

    # ── Phase 0: Quick DSL check ──
    from smart_solver import smart_solve
    dsl_result = smart_solve(task, verbose=False)
    if dsl_result is not None:
        name, predictions = dsl_result
        if verbose:
            print(f"  DSL solved: {name}")
        stats["method"] = f"dsl:{name}"
        return (True, predictions, f"# DSL: {name}", stats)

    if not API_KEY:
        return (False, [], "", stats)

    # ── Holdout setup ──
    # If 3+ training examples, hold one out as pseudo-test to catch overfitting
    use_holdout = len(task.train) >= 3
    if use_holdout:
        holdout_idx = len(task.train) - 1  # hold out last example
        holdout_inp, holdout_out = task.train[holdout_idx]
        # Create a reduced task for verification
        import copy
        train_task = copy.deepcopy(task)
        train_task.train = task.train[:holdout_idx]
    else:
        train_task = task
        holdout_inp = holdout_out = None

    # ── Phase 1: Mass seeding ──
    strategies = ["objects", "rules", "symmetry", "counting", "topology"]
    winners = []
    best_fitness = 0.0

    if verbose:
        print(f"  Shotgun: {n_attempts} attempts (holdout={'yes' if use_holdout else 'no'})")

    for i in range(n_attempts):
        strategy = strategies[i % len(strategies)]
        # Vary temperature for diversity
        temp = 0.6 + (i % 5) * 0.1  # 0.6, 0.7, 0.8, 0.9, 1.0

        prompt = build_diverse_seed_prompt(train_task, strategy)
        try:
            response = call_llm(prompt, temperature=temp)
            code = extract_code(response)
            c = Candidate(code=code, generation=0, method=f"seed:{strategy}")
            stats["llm_calls"] += 1
            stats["total_candidates"] += 1

            # Score against training (or reduced training if holdout)
            score_candidate(c, train_task)

            if c.fitness > best_fitness:
                best_fitness = c.fitness
                if verbose:
                    print(f"    [{i+1}/{n_attempts}] {c.id} fitness={c.fitness:.3f} ({strategy}) ★")

            if c.fitness >= 1.0:
                # Passes training — now check holdout
                transform = c.compile()
                if transform is None:
                    continue

                if use_holdout:
                    try:
                        holdout_result = transform(holdout_inp)
                        if holdout_result != holdout_out:
                            if verbose:
                                print(f"    [{i+1}/{n_attempts}] {c.id} OVERFIT — passes training, fails holdout")
                            continue  # overfit, try next
                    except Exception:
                        continue

                # Also verify against FULL training set (including holdout)
                full_pass = True
                for inp, expected in task.train:
                    try:
                        if transform(inp) != expected:
                            full_pass = False
                            break
                    except Exception:
                        full_pass = False
                        break

                if full_pass:
                    predictions = apply_to_test(task, transform)
                    stats["method"] = f"shotgun:{strategy}"
                    if verbose:
                        print(f"    [{i+1}/{n_attempts}] {c.id} SOLVED ✓ ({strategy})")
                    return (True, predictions, c.code, stats)

        except Exception as e:
            if verbose and "credit balance" in str(e).lower():
                print(f"    API credits exhausted at attempt {i+1}")
                break
            # Other errors — just skip this attempt

    stats["best_fitness_history"] = [best_fitness]
    return (False, [], "", stats)


def evaluate_shotgun(split: str = "training", limit: int = None,
                     n_attempts: int = 32, verbose: bool = False) -> dict:
    """Evaluate shotgun solver on tasks."""
    ids = task_ids(split)
    if limit:
        ids = ids[:limit]

    solved = 0
    dsl_solved = 0
    shotgun_solved = 0
    results = []
    total_llm_calls = 0
    t0 = time.time()

    for i, tid in enumerate(ids):
        task = load_task(tid, split)
        if verbose:
            print(f"\n[{i+1}/{len(ids)}] Task {tid}")

        success, predictions, code, stats = shotgun_task(task, n_attempts=n_attempts, verbose=verbose)
        total_llm_calls += stats.get("llm_calls", 0)

        if success:
            correct = all(
                pred == expected
                for pred, (_, expected) in zip(predictions, task.test)
                if expected.h > 0
            )
            if correct:
                solved += 1
                if stats["method"].startswith("dsl:"):
                    dsl_solved += 1
                else:
                    shotgun_solved += 1
                if verbose:
                    print(f"  ✓ CORRECT [{stats['method']}] (calls={stats['llm_calls']})")
            else:
                if verbose:
                    print(f"  ✗ Wrong on test [{stats['method']}]")
            results.append((tid, correct, stats["method"], stats))
        else:
            results.append((tid, False, "unsolved", stats))
            if verbose:
                best = stats['best_fitness_history'][-1] if stats['best_fitness_history'] else 0
                print(f"  ✗ Unsolved (best_fitness={best:.3f}, calls={stats['llm_calls']})")

    elapsed = time.time() - t0
    return {
        "total": len(ids),
        "solved": solved,
        "dsl_solved": dsl_solved,
        "shotgun_solved": shotgun_solved,
        "accuracy": solved / len(ids) if ids else 0,
        "time_s": elapsed,
        "total_llm_calls": total_llm_calls,
        "avg_calls_per_task": total_llm_calls / len(ids) if ids else 0,
        "results": results,
    }


# ─── Pe-adaptive solver ───────────────────────────────────────────

def estimate_barrier(task: Task) -> str:
    """Estimate task barrier (difficulty) using framework-inspired analysis.

    Returns: "low", "medium", "high"

    Low barrier: DSL-solvable transforms (geometric, simple recolor, crop)
    Medium barrier: single-concept transforms (fill, stamp, gravity)
    High barrier: multi-concept transforms (conditional + spatial + relational)
    """
    cls = classify_transform(task)
    topo = classify_topo(task)
    color_info = analyze_color_mappings(task)
    tags = topo["tags"]

    # Count independent concepts (analogous to barrier dimension d)
    concepts = 0

    # Dimensional concept
    if not cls["always_same_size"]:
        concepts += 1

    # Color concept
    if color_info.get("has_conditional"):
        concepts += 2  # conditional coloring is hard
    elif color_info.get("has_direct_swap"):
        concepts += 1

    # Topological concept
    if "fills_holes" in tags or "merges_objects" in tags or "splits_objects" in tags:
        concepts += 1

    # Symmetry concept
    if "creates_symmetry" in tags or "modifies_symmetry" in tags:
        concepts += 1

    # Grid size as complexity proxy
    avg_cells = sum(inp.h * inp.w for inp, _ in task.train) / len(task.train)
    if avg_cells > 200:
        concepts += 1  # large grids are harder

    # Few training examples = less constraint info
    if len(task.train) <= 2:
        concepts += 1

    if concepts <= 1:
        return "low"
    elif concepts <= 2:
        return "medium"
    else:
        return "high"


def adaptive_task(task: Task, verbose: bool = False) -> tuple[bool, list, str, dict]:
    """Pe-adaptive solver. Estimates task barrier, then allocates resources accordingly.

    Low barrier (Pe~0):   DSL only, 0 LLM calls
    Medium barrier (Pe~3): 8 shotgun attempts, constraint prompt
    High barrier (Pe~8):   32 attempts + evolution fallback on near-misses
    """
    stats = {
        "generations": 0,
        "llm_calls": 0,
        "best_fitness_history": [],
        "total_candidates": 0,
        "method": "none",
    }

    # Phase 0: DSL (Pe=0, invariant, transparent, independent)
    from smart_solver import smart_solve
    dsl_result = smart_solve(task, verbose=False)
    if dsl_result is not None:
        name, predictions = dsl_result
        if verbose:
            print(f"  DSL solved: {name}")
        stats["method"] = f"dsl:{name}"
        return (True, predictions, f"# DSL: {name}", stats)

    if not API_KEY:
        return (False, [], "", stats)

    barrier = estimate_barrier(task)
    if verbose:
        print(f"  Barrier: {barrier}")

    # Phase 1: Shotgun at appropriate intensity
    if barrier == "low":
        n_attempts = 4
    elif barrier == "medium":
        n_attempts = 8
    else:
        n_attempts = 24

    success, predictions, code, shot_stats = shotgun_task(
        task, n_attempts=n_attempts, verbose=verbose
    )
    stats["llm_calls"] += shot_stats.get("llm_calls", 0)
    stats["total_candidates"] += shot_stats.get("total_candidates", 0)

    if success:
        stats["method"] = shot_stats["method"]
        return (True, predictions, code, stats)

    # Phase 2: For high-barrier tasks with near-misses, try evolution
    best = shot_stats["best_fitness_history"][-1] if shot_stats["best_fitness_history"] else 0
    if barrier == "high" and best >= 0.5:
        if verbose:
            print(f"  Near-miss ({best:.3f}) — trying evolution")
        config = EvoConfig(seed_count=2, max_generations=4, max_llm_calls=12)
        evo_success, evo_preds, evo_code, evo_stats = evolve_task(task, config, verbose=verbose)
        stats["llm_calls"] += evo_stats.get("llm_calls", 0)
        if evo_success:
            stats["method"] = evo_stats["method"]
            return (True, evo_preds, evo_code, stats)

    stats["best_fitness_history"] = shot_stats.get("best_fitness_history", [])
    return (False, [], "", stats)


def evaluate_adaptive(split: str = "training", limit: int = None,
                      verbose: bool = False) -> dict:
    """Evaluate Pe-adaptive solver."""
    ids = task_ids(split)
    if limit:
        ids = ids[:limit]

    solved = 0
    dsl_solved = 0
    llm_solved = 0
    results = []
    total_llm_calls = 0
    barrier_stats = {"low": [0, 0], "medium": [0, 0], "high": [0, 0]}
    t0 = time.time()

    for i, tid in enumerate(ids):
        task = load_task(tid, split)
        if verbose:
            print(f"\n[{i+1}/{len(ids)}] Task {tid}")

        barrier = estimate_barrier(task)
        barrier_stats[barrier][1] += 1

        success, predictions, code, stats = adaptive_task(task, verbose=verbose)
        total_llm_calls += stats.get("llm_calls", 0)

        if success:
            correct = all(
                pred == expected
                for pred, (_, expected) in zip(predictions, task.test)
                if expected.h > 0
            )
            if correct:
                solved += 1
                barrier_stats[barrier][0] += 1
                if stats["method"].startswith("dsl:"):
                    dsl_solved += 1
                else:
                    llm_solved += 1
                if verbose:
                    print(f"  ✓ CORRECT [{stats['method']}] (calls={stats['llm_calls']})")
            else:
                if verbose:
                    print(f"  ✗ Wrong on test [{stats['method']}]")
            results.append((tid, correct, stats["method"], stats))
        else:
            results.append((tid, False, "unsolved", stats))
            if verbose:
                best = stats['best_fitness_history'][-1] if stats.get('best_fitness_history') else 0
                print(f"  ✗ Unsolved (best={best:.3f}, calls={stats['llm_calls']})")

    elapsed = time.time() - t0
    return {
        "total": len(ids),
        "solved": solved,
        "dsl_solved": dsl_solved,
        "llm_solved": llm_solved,
        "accuracy": solved / len(ids) if ids else 0,
        "time_s": elapsed,
        "total_llm_calls": total_llm_calls,
        "avg_calls_per_task": total_llm_calls / len(ids) if ids else 0,
        "barrier_stats": {k: f"{v[0]}/{v[1]}" for k, v in barrier_stats.items()},
        "results": results,
    }


# ─── Batch evaluation ────────────────────────────────────────────

def evaluate_evo(split: str = "training", limit: int = None,
                 config: EvoConfig = None, verbose: bool = False) -> dict:
    """Evaluate evolutionary solver on tasks."""
    if config is None:
        config = EvoConfig()

    ids = task_ids(split)
    if limit:
        ids = ids[:limit]

    solved = 0
    dsl_solved = 0
    evo_solved = 0
    results = []
    total_llm_calls = 0
    t0 = time.time()

    for i, tid in enumerate(ids):
        task = load_task(tid, split)
        if verbose:
            print(f"\n[{i+1}/{len(ids)}] Task {tid}")

        success, predictions, code, stats = evolve_task(task, config, verbose=verbose)
        total_llm_calls += stats.get("llm_calls", 0)

        if success:
            correct = all(
                pred == expected
                for pred, (_, expected) in zip(predictions, task.test)
                if expected.h > 0
            )
            if correct:
                solved += 1
                if stats["method"].startswith("dsl:"):
                    dsl_solved += 1
                else:
                    evo_solved += 1
                if verbose:
                    print(f"  ✓ CORRECT [{stats['method']}] (gen={stats['generations']}, calls={stats['llm_calls']})")
            else:
                if verbose:
                    print(f"  ✗ Wrong on test [{stats['method']}]")
            results.append((tid, correct, stats["method"], stats))
        else:
            results.append((tid, False, "unsolved", stats))
            if verbose:
                print(f"  ✗ Unsolved (best_fitness={stats['best_fitness_history'][-1] if stats['best_fitness_history'] else 0:.3f})")

    elapsed = time.time() - t0
    return {
        "total": len(ids),
        "solved": solved,
        "dsl_solved": dsl_solved,
        "evo_solved": evo_solved,
        "accuracy": solved / len(ids) if ids else 0,
        "time_s": elapsed,
        "total_llm_calls": total_llm_calls,
        "avg_calls_per_task": total_llm_calls / len(ids) if ids else 0,
        "results": results,
    }


# ─── CLI ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("-")]

    if not args:
        print("Evolutionary ARC-AGI Solver")
        print("=" * 40)
        print()
        print("Usage:")
        print("  python evo_solver.py <task_id> [-v]          # solve one task")
        print("  python evo_solver.py eval [N] [-v]           # evaluate N tasks (evo mode)")
        print("  python evo_solver.py shotgun [N] [A] [-v]    # N tasks, A attempts each (default 32)")
        print("  python evo_solver.py adaptive [N] [-v]       # Pe-adaptive: auto-tunes per task")
        print("  python evo_solver.py eval [-v]               # evaluate all")
        print()
        print(f"Backend: {BACKEND} | Model: {MODEL} | Key: {'set' if API_KEY else 'NOT SET'}")
        print(f"  Set OPENAI_API_KEY or ANTHROPIC_API_KEY. Override model with ARC_MODEL.")
        print()

        # Quick DSL baseline
        from solver import evaluate
        stats = evaluate("training")
        print(f"DSL baseline: {stats['solved']}/{stats['total']} ({stats['accuracy']:.1%})")
        sys.exit(0)

    if args[0] == "adaptive":
        limit = int(args[1]) if len(args) > 1 else None

        if not API_KEY:
            print("No API key. Set OPENAI_API_KEY or ANTHROPIC_API_KEY.")
            sys.exit(1)

        print(f"Pe-adaptive solver: {'all' if not limit else limit} tasks")
        print(f"Backend: {BACKEND} | Model: {MODEL}")
        print(f"Low barrier → 4 attempts | Medium → 8 | High → 24 + evo fallback")
        print()

        stats = evaluate_adaptive("training", limit=limit, verbose=verbose)

        print(f"\n{'='*60}")
        print(f"Results:")
        print(f"  Total solved: {stats['solved']}/{stats['total']} ({stats['accuracy']:.1%})")
        print(f"  DSL solved:   {stats['dsl_solved']}")
        print(f"  LLM solved:   {stats['llm_solved']}")
        print(f"  Time:         {stats['time_s']:.1f}s")
        print(f"  LLM calls:    {stats['total_llm_calls']} ({stats['avg_calls_per_task']:.1f}/task)")
        print(f"  By barrier:   {stats['barrier_stats']}")

    elif args[0] == "shotgun":
        limit = int(args[1]) if len(args) > 1 else None
        n_attempts = int(args[2]) if len(args) > 2 else 32

        if not API_KEY:
            print("No API key. Set OPENAI_API_KEY or ANTHROPIC_API_KEY.")
            sys.exit(1)

        print(f"Shotgun solver: {'all' if not limit else limit} tasks × {n_attempts} attempts")
        print(f"Backend: {BACKEND} | Model: {MODEL}")
        print(f"Holdout validation: enabled for tasks with 3+ training examples")
        print()

        stats = evaluate_shotgun("training", limit=limit, n_attempts=n_attempts, verbose=verbose)

        print(f"\n{'='*60}")
        print(f"Results:")
        print(f"  Total solved: {stats['solved']}/{stats['total']} ({stats['accuracy']:.1%})")
        print(f"  DSL solved:   {stats['dsl_solved']}")
        print(f"  Shotgun solved: {stats['shotgun_solved']}")
        print(f"  Time:         {stats['time_s']:.1f}s")
        print(f"  LLM calls:    {stats['total_llm_calls']} ({stats['avg_calls_per_task']:.1f}/task)")

    elif args[0] == "eval":
        limit = int(args[1]) if len(args) > 1 else None
        config = EvoConfig()

        if not API_KEY:
            print("No API key set — running DSL-only mode")
            print("  Set OPENAI_API_KEY or ANTHROPIC_API_KEY")
            from smart_solver import evaluate_smart
            stats = evaluate_smart("training", verbose=verbose)
            print(f"Smart DSL: {stats['solved']}/{stats['total']} ({stats['accuracy']:.1%})")
            sys.exit(0)

        print(f"Running evolutionary solver on {'all' if not limit else limit} tasks...")
        print(f"Backend: {BACKEND} | Model: {MODEL}")
        print(f"Config: pop={config.population_size}, gens={config.max_generations}, "
              f"seeds={config.seed_count}, budget={config.max_llm_calls} calls/task")
        print()

        stats = evaluate_evo("training", limit=limit, config=config, verbose=verbose)

        print(f"\n{'='*60}")
        print(f"Results:")
        print(f"  Total solved: {stats['solved']}/{stats['total']} ({stats['accuracy']:.1%})")
        print(f"  DSL solved:   {stats['dsl_solved']}")
        print(f"  Evo solved:   {stats['evo_solved']}")
        print(f"  Time:         {stats['time_s']:.1f}s")
        print(f"  LLM calls:    {stats['total_llm_calls']} ({stats['avg_calls_per_task']:.1f}/task)")

    else:
        task_id = args[0]
        task = load_task(task_id)
        task.show()
        print()

        config = EvoConfig()
        success, predictions, code, stats = evolve_task(task, config, verbose=True)

        if success:
            print(f"\nSOLVED [{stats['method']}] in {stats['generations']} generations, "
                  f"{stats['llm_calls']} LLM calls")
            print(f"\nCode:\n{code}")
            for i, p in enumerate(predictions):
                print(f"\nPrediction {i}:")
                print(p.show())
        else:
            print(f"\nUNSOLVED after {stats['generations']} generations, "
                  f"{stats['llm_calls']} LLM calls")
            if stats["best_fitness_history"]:
                print(f"Best fitness trajectory: {[f'{f:.3f}' for f in stats['best_fitness_history']]}")
