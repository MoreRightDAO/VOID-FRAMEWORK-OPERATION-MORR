"""K-Factorization-inspired grid decomposition for ARC-AGI.

The insight from §136: Q = Q_shape(O,R,α) · Q_scale(K).
Shape and scale separate. Applied to ARC grids:
- Shape = the abstract pattern (topology, symmetry, relational structure)
- Scale = the concrete realization (size, colors, repetition count)

This gives us a novel decomposition strategy: factor each grid into
its shape signature and scale parameters, then match transformations
at the shape level.
"""
import numpy as np
from loader import Grid, Task
from dsl import (
    find_objects, extract_object, bounding_box, crop,
    is_symmetric_h, is_symmetric_v, is_symmetric_diag,
    periodicity, background_color, grid_to_numpy
)
from collections import Counter
from typing import Optional


# ─── Shape signature ─────────────────────────────────────────────

def shape_signature(g: Grid) -> dict:
    """Extract K-independent shape features from a grid.

    These features are invariant to scale (grid size) and color assignment.
    They capture the abstract relational structure.
    """
    bg = background_color(g)
    objects = find_objects(g, bg)

    sig = {
        # Topology
        "n_objects": len(objects),
        "n_colors": len(g.nonzero_colors()),
        "aspect_ratio": round(g.h / g.w, 3) if g.w > 0 else 0,

        # Symmetry group
        "sym_h": is_symmetric_h(g),
        "sym_v": is_symmetric_v(g),
        "sym_diag": is_symmetric_diag(g),

        # Periodicity
        "period_v": periodicity(g, 0),
        "period_h": periodicity(g, 1),

        # Object statistics (scale-invariant)
        "obj_sizes": sorted([len(o) for o in objects], reverse=True),
        "obj_count_by_size": dict(Counter(len(o) for o in objects)),

        # Fill ratio (scale-invariant)
        "fill_ratio": round(sum(1 for row in g.data for c in row if c != bg) / (g.h * g.w), 3),

        # Color distribution (normalized)
        "color_ratios": _color_ratios(g, bg),
    }

    # Object shape signatures (topology of each object)
    if objects:
        obj_sigs = []
        for obj in sorted(objects, key=len, reverse=True)[:5]:  # top 5 objects
            obj_grid = extract_object(g, obj, bg)
            obj_sigs.append({
                "rel_size": round(len(obj) / (g.h * g.w), 3),
                "aspect": round(obj_grid.h / obj_grid.w, 3) if obj_grid.w > 0 else 0,
                "density": round(len(obj) / (obj_grid.h * obj_grid.w), 3),
            })
        sig["object_shapes"] = obj_sigs

    return sig


def _color_ratios(g: Grid, bg: int) -> dict[int, float]:
    """Normalized color distribution (excluding background)."""
    counts = Counter(c for row in g.data for c in row if c != bg)
    total = sum(counts.values())
    if total == 0:
        return {}
    return {k: round(v / total, 3) for k, v in sorted(counts.items())}


# ─── Scale parameters ───────────────────────────────────────────

def scale_params(g: Grid) -> dict:
    """Extract K-dependent scale features."""
    return {
        "h": g.h,
        "w": g.w,
        "total_cells": g.h * g.w,
        "bg_color": background_color(g),
        "colors": sorted(g.colors()),
    }


# ─── K-Factor decomposition ─────────────────────────────────────

def k_decompose(g: Grid) -> tuple[dict, dict]:
    """Full K-Factorization: returns (shape_sig, scale_params)."""
    return (shape_signature(g), scale_params(g))


# ─── Color mapping analysis ──────────────────────────────────────

def analyze_color_mappings(task: Task) -> dict:
    """Detect per-color transforms across training examples.

    For same-size grids, builds a cell-by-cell mapping of which input
    colors become which output colors. Detects:
    - Direct color swaps (color A always → color B)
    - Conditional mappings (color A → B near edges, A → C in interior)
    - Colors that are preserved vs changed
    - New colors introduced (what generates them)
    """
    if not task.train:
        return {"mappings": {}, "consistent": False, "description": ""}

    # Per-example color transition counts
    all_transitions = Counter()  # (in_color, out_color) -> count
    per_example = []

    for inp, out in task.train:
        if inp.h != out.h or inp.w != out.w:
            # Can't do cell-level mapping for different-size grids
            # Fall back to aggregate color counts
            return _analyze_color_counts(task)

        transitions = Counter()
        for r in range(inp.h):
            for c in range(inp.w):
                transitions[(inp.data[r][c], out.data[r][c])] += 1
                all_transitions[(inp.data[r][c], out.data[r][c])] += 1
        per_example.append(transitions)

    # Build per-input-color mapping
    in_colors = sorted({ic for ic, _ in all_transitions})
    mappings = {}
    for ic in in_colors:
        targets = {oc: all_transitions[(ic, oc)] for _, oc in all_transitions if _ == ic}
        total = sum(targets.values())
        if not total:
            continue
        dominant = max(targets, key=targets.get)
        dominant_pct = targets[dominant] / total
        mappings[ic] = {
            "dominant_target": dominant,
            "confidence": round(dominant_pct, 3),
            "all_targets": {oc: round(cnt / total, 3) for oc, cnt in sorted(targets.items())},
            "preserved": dominant == ic,
        }

    # Check consistency across examples
    consistent = True
    for ex_trans in per_example:
        for ic in in_colors:
            targets = {oc: ex_trans.get((ic, oc), 0) for _, oc in ex_trans if _ == ic}
            if targets:
                ex_dominant = max(targets, key=targets.get)
                if ic in mappings and ex_dominant != mappings[ic]["dominant_target"]:
                    consistent = False

    # Build human-readable description
    desc_parts = []
    preserved = []
    swapped = []
    conditional = []

    for ic, info in sorted(mappings.items()):
        if info["preserved"] and info["confidence"] > 0.99:
            preserved.append(str(ic))
        elif info["confidence"] > 0.95:
            swapped.append(f"{ic}→{info['dominant_target']}")
        elif info["confidence"] > 0.5:
            targets_str = ", ".join(f"{oc}({pct:.0%})" for oc, pct in info["all_targets"].items() if pct > 0.05)
            conditional.append(f"{ic}→[{targets_str}]")

    if preserved:
        desc_parts.append(f"Colors {','.join(preserved)} preserved")
    if swapped:
        desc_parts.append(f"Mappings: {'; '.join(swapped)}")
    if conditional:
        desc_parts.append(f"Conditional: {'; '.join(conditional)}")

    return {
        "mappings": mappings,
        "consistent": consistent,
        "description": ". ".join(desc_parts) if desc_parts else "no clear color mapping",
        "has_direct_swap": any(not m["preserved"] and m["confidence"] > 0.95 for m in mappings.values()),
        "has_conditional": any(m["confidence"] <= 0.95 and not m["preserved"] for m in mappings.values()),
    }


def _analyze_color_counts(task: Task) -> dict:
    """Fallback color analysis for different-size grids."""
    in_colors_all = Counter()
    out_colors_all = Counter()
    for inp, out in task.train:
        for row in inp.data:
            in_colors_all.update(row)
        for row in out.data:
            out_colors_all.update(row)

    new_colors = set(out_colors_all) - set(in_colors_all)
    lost_colors = set(in_colors_all) - set(out_colors_all)

    desc_parts = []
    if new_colors:
        desc_parts.append(f"New colors in output: {sorted(new_colors)}")
    if lost_colors:
        desc_parts.append(f"Colors removed: {sorted(lost_colors)}")

    return {
        "mappings": {},
        "consistent": True,
        "description": ". ".join(desc_parts) if desc_parts else "different grid sizes",
        "has_direct_swap": False,
        "has_conditional": False,
    }


# ─── Transform classification ───────────────────────────────────

def classify_transform(task: Task) -> dict:
    """Analyze what kind of transformation a task requires by comparing
    shape signatures of inputs vs outputs.

    This is the key insight: if the transformation preserves shape but
    changes scale, it's a K-scale operation. If it changes shape but
    preserves scale, it's a shape operation. Most ARC tasks are one or the other.
    """
    analyses = []

    for inp, out in task.train:
        inp_shape, inp_scale = k_decompose(inp)
        out_shape, out_scale = k_decompose(out)

        analysis = {
            # Scale changes
            "size_change": (out_scale["h"] / inp_scale["h"] if inp_scale["h"] else 0,
                           out_scale["w"] / inp_scale["w"] if inp_scale["w"] else 0),
            "same_size": inp_scale["h"] == out_scale["h"] and inp_scale["w"] == out_scale["w"],

            # Shape preservation
            "same_n_objects": inp_shape["n_objects"] == out_shape["n_objects"],
            "same_n_colors": inp_shape["n_colors"] == out_shape["n_colors"],
            "same_symmetry": (inp_shape["sym_h"] == out_shape["sym_h"] and
                             inp_shape["sym_v"] == out_shape["sym_v"]),
            "same_fill_ratio": abs(inp_shape["fill_ratio"] - out_shape["fill_ratio"]) < 0.01,

            # New colors introduced?
            "new_colors": set(out_scale["colors"]) - set(inp_scale["colors"]),
            "lost_colors": set(inp_scale["colors"]) - set(out_scale["colors"]),

            # Object count delta
            "object_delta": out_shape["n_objects"] - inp_shape["n_objects"],
        }
        analyses.append(analysis)

    # Aggregate across training examples
    return {
        "n_examples": len(analyses),
        "consistent_size_change": len(set(a["size_change"] for a in analyses)) == 1,
        "size_ratio": analyses[0]["size_change"] if analyses else (1, 1),
        "always_same_size": all(a["same_size"] for a in analyses),
        "preserves_objects": all(a["same_n_objects"] for a in analyses),
        "preserves_colors": all(a["same_n_colors"] for a in analyses),
        "preserves_symmetry": all(a["same_symmetry"] for a in analyses),

        # Classification
        "type": _classify_type(analyses),
    }


def _classify_type(analyses: list[dict]) -> str:
    """Classify the transform type based on analyses."""
    if all(a["same_size"] for a in analyses):
        if all(a["same_n_objects"] and a["same_n_colors"] for a in analyses):
            return "recolor_or_rearrange"  # same grid structure, different colors/positions
        elif all(len(a["new_colors"]) > 0 for a in analyses):
            return "fill_or_mark"  # adds new colors (e.g., filling regions)
        else:
            return "same_size_transform"
    else:
        ratios = set(a["size_change"] for a in analyses)
        if len(ratios) == 1:
            r = list(ratios)[0]
            if r[0] == r[1] and r[0] == int(r[0]):
                return f"uniform_scale_{int(r[0])}x"
            elif r[0] == int(r[0]) and r[1] == int(r[1]):
                return f"scale_{int(r[0])}x{int(r[1])}"
            else:
                return "variable_scale"
        else:
            if all(a["size_change"][0] < 1 and a["size_change"][1] < 1 for a in analyses):
                return "crop_or_extract"
            return "variable_size"


# ─── Barrier analysis ───────────────────────────────────────────

def task_complexity(task: Task) -> dict:
    """Estimate task complexity using framework-inspired metrics.

    The 'barrier' to solving a task is analogous to §136D2:
    higher barriers require more abstract reasoning.
    """
    classification = classify_transform(task)

    # Count unique transformations needed
    inp_sigs = [shape_signature(inp) for inp, _ in task.train]
    out_sigs = [shape_signature(out) for _, out in task.train]

    # Complexity dimensions
    n_concepts = 0
    if not classification["always_same_size"]:
        n_concepts += 1  # size change
    if not classification["preserves_colors"]:
        n_concepts += 1  # color change
    if not classification["preserves_objects"]:
        n_concepts += 1  # object structure change
    if not classification["preserves_symmetry"]:
        n_concepts += 1  # symmetry change

    # Average grid size (proxy for state space)
    avg_cells = np.mean([inp.h * inp.w for inp, _ in task.train])

    return {
        "classification": classification,
        "n_concepts": n_concepts,
        "avg_grid_cells": avg_cells,
        "estimated_difficulty": n_concepts * np.log(avg_cells + 1),  # barrier ∝ concepts × log(state_space)
    }


if __name__ == "__main__":
    import sys
    from loader import load_task

    if len(sys.argv) < 2:
        print("Usage: python k_factor.py <task_id>")
        sys.exit(1)

    task = load_task(sys.argv[1])
    task.show()

    print("\n=== K-Factorization Analysis ===")
    for i, (inp, out) in enumerate(task.train):
        print(f"\n--- Example {i} ---")
        inp_shape, inp_scale = k_decompose(inp)
        out_shape, out_scale = k_decompose(out)
        print(f"Input shape:  {inp_shape}")
        print(f"Input scale:  {inp_scale}")
        print(f"Output shape: {out_shape}")
        print(f"Output scale: {out_scale}")

    print(f"\n=== Transform Classification ===")
    cls = classify_transform(task)
    print(f"Type: {cls['type']}")
    for k, v in cls.items():
        if k != 'type':
            print(f"  {k}: {v}")

    print(f"\n=== Complexity ===")
    comp = task_complexity(task)
    print(f"Concepts: {comp['n_concepts']}")
    print(f"Difficulty: {comp['estimated_difficulty']:.2f}")
