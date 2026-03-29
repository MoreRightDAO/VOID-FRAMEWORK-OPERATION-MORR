"""K-Factorization-guided smart solver for ARC-AGI.

Uses transform classification to prune the hypothesis space,
then searches more deeply within the relevant category.
"""
import time
import sys
from loader import Task, Grid, load_task, load_all, task_ids
from dsl import *
from solver import verify_on_train, apply_to_test
from k_factor import classify_transform, task_complexity
from typing import Optional, Callable


def same_size_hypotheses(task: Task) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Hypotheses for tasks where input and output have the same size."""
    hyps = []

    # Geometric
    hyps.extend([
        ("identity", lambda g: g),
        ("rotate_90", rotate_90),
        ("rotate_180", rotate_180),
        ("rotate_270", rotate_270),
        ("flip_h", flip_h),
        ("flip_v", flip_v),
        ("transpose", transpose),
    ])

    # Compositions
    for n1, f1 in [("rot90", rotate_90), ("rot180", rotate_180), ("flip_h", flip_h), ("flip_v", flip_v)]:
        for n2, f2 in [("rot90", rotate_90), ("rot180", rotate_180), ("flip_h", flip_h), ("flip_v", flip_v)]:
            hyps.append((f"{n1}+{n2}", lambda g, a=f1, b=f2: b(a(g))))

    # Overlay with transforms
    for name, fn in [("rot90", rotate_90), ("rot180", rotate_180), ("rot270", rotate_270),
                     ("flip_h", flip_h), ("flip_v", flip_v)]:
        hyps.append((f"overlay+{name}", lambda g, f=fn: overlay(g, f(g), 0)))

    # Color operations
    all_colors = set()
    for inp, out in task.train:
        all_colors |= inp.colors() | out.colors()

    for a in all_colors:
        for b in all_colors:
            if a < b:
                hyps.append((f"swap_{a}_{b}", lambda g, x=a, y=b: swap_colors(g, x, y)))

    # Fill operations: find what color maps to what
    for inp, out in task.train[:1]:
        for target_color in out.nonzero_colors():
            if target_color not in inp.nonzero_colors():
                # New color introduced — try filling based on object properties
                def fill_objects_with(g, tc=target_color):
                    bg = background_color(g)
                    objs = find_objects(g, bg)
                    result = Grid([list(row) for row in g.data])
                    for obj in objs:
                        for r, c in obj:
                            result.data[r][c] = tc
                    return result
                hyps.append((f"fill_all_objects_{target_color}", fill_objects_with))

    # Gravity operations (move colored cells down/right/etc)
    def gravity_down(g):
        arr = grid_to_numpy(g)
        bg = background_color(g)
        result = arr.copy()
        for c in range(g.w):
            col = [arr[r][c] for r in range(g.h) if arr[r][c] != bg]
            result[:, c] = bg
            for i, v in enumerate(col):
                result[g.h - len(col) + i, c] = v
        return numpy_to_grid(result)

    def gravity_up(g):
        arr = grid_to_numpy(g)
        bg = background_color(g)
        result = arr.copy()
        for c in range(g.w):
            col = [arr[r][c] for r in range(g.h) if arr[r][c] != bg]
            result[:, c] = bg
            for i, v in enumerate(col):
                result[i, c] = v
        return numpy_to_grid(result)

    def gravity_right(g):
        arr = grid_to_numpy(g)
        bg = background_color(g)
        result = arr.copy()
        for r in range(g.h):
            row = [arr[r][c] for c in range(g.w) if arr[r][c] != bg]
            result[r, :] = bg
            for i, v in enumerate(row):
                result[r, g.w - len(row) + i] = v
        return numpy_to_grid(result)

    def gravity_left(g):
        arr = grid_to_numpy(g)
        bg = background_color(g)
        result = arr.copy()
        for r in range(g.h):
            row = [arr[r][c] for c in range(g.w) if arr[r][c] != bg]
            result[r, :] = bg
            for i, v in enumerate(row):
                result[r, i] = v
        return numpy_to_grid(result)

    hyps.extend([
        ("gravity_down", gravity_down),
        ("gravity_up", gravity_up),
        ("gravity_right", gravity_right),
        ("gravity_left", gravity_left),
    ])

    return hyps


def scale_hypotheses(task: Task, ratio: tuple) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Hypotheses for tasks with consistent size scaling."""
    hyps = []
    rh, rw = int(ratio[0]), int(ratio[1])

    # Simple tiling
    hyps.append((f"tile_{rh}x{rw}", lambda g, r=rh, c=rw: tile(g, r, c)))

    # Pixel scaling
    if rh == rw:
        hyps.append((f"scale_{rh}", lambda g, f=rh: scale(g, f)))

    # Self-kronecker
    hyps.append(("self_kronecker", lambda g: self_kronecker(g, 0)))

    # Kronecker with different bg
    for bg in range(10):
        hyps.append((f"self_kronecker_bg{bg}", lambda g, b=bg: self_kronecker(g, b)))

    # Tile then transform
    for name, fn in [("flip_h", flip_h), ("flip_v", flip_v), ("rot90", rotate_90)]:
        hyps.append((f"tile_{rh}x{rw}+{name}",
                      lambda g, r=rh, c=rw, f=fn: f(tile(g, r, c))))

    # Mirror tiling (tile but alternate flips)
    def mirror_tile_h(g, rows=rh, cols=rw):
        data = []
        for tr in range(rows):
            for r in range(g.h):
                row = []
                for tc in range(cols):
                    if tc % 2 == 0:
                        row.extend(g.data[r])
                    else:
                        row.extend(g.data[r][::-1])
                data.append(row)
        return Grid(data)

    def mirror_tile_v(g, rows=rh, cols=rw):
        data = []
        for tr in range(rows):
            for r in range(g.h):
                actual_r = r if tr % 2 == 0 else (g.h - 1 - r)
                row = []
                for tc in range(cols):
                    row.extend(g.data[actual_r])
                data.append(row)
        return Grid(data)

    hyps.extend([
        ("mirror_tile_h", mirror_tile_h),
        ("mirror_tile_v", mirror_tile_v),
    ])

    return hyps


def crop_hypotheses(task: Task) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Hypotheses for tasks that crop/extract from input."""
    hyps = []

    hyps.append(("crop_to_content", crop_to_content))

    # Extract each object
    def make_extract_fn(n):
        def fn(g):
            bg = background_color(g)
            objs = find_objects(g, bg)
            objs.sort(key=len, reverse=True)
            if n < len(objs):
                return extract_object(g, objs[n], bg)
            return g
        return fn

    for i in range(10):
        hyps.append((f"extract_obj_{i}", make_extract_fn(i)))

    # Extract smallest/largest
    def extract_smallest(g):
        bg = background_color(g)
        objs = find_objects(g, bg)
        if objs:
            smallest = min(objs, key=len)
            return extract_object(g, smallest, bg)
        return g

    hyps.append(("extract_smallest", extract_smallest))

    # Crop to specific color
    for inp, out in task.train[:1]:
        for color in inp.nonzero_colors():
            def crop_color(g, c=color):
                bb = bounding_box(g, c)
                if bb[2] > bb[0]:
                    return crop(g, *bb)
                return g
            hyps.append((f"crop_color_{color}", crop_color))

    # Downscale
    for factor in [2, 3, 4, 5]:
        for inp, out in task.train[:1]:
            if inp.h % factor == 0 and inp.w % factor == 0:
                hyps.append((f"downscale_{factor}", lambda g, f=factor: downscale(g, f)))

    return hyps


def variable_size_hypotheses(task: Task) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Catch-all for variable-size transformations."""
    hyps = []

    # All crop hypotheses
    hyps.extend(crop_hypotheses(task))

    # All same-size hypotheses that might work on different sizes
    hyps.extend([
        ("identity", lambda g: g),
        ("rotate_90", rotate_90),
        ("flip_h", flip_h),
        ("flip_v", flip_v),
        ("crop_to_content", crop_to_content),
    ])

    # Transpose (changes dimensions)
    hyps.append(("transpose", transpose))

    return hyps


def smart_solve(task: Task, verbose: bool = False) -> Optional[tuple[str, list[Grid]]]:
    """K-Factorization-guided solver."""
    classification = classify_transform(task)
    task_type = classification["type"]

    if verbose:
        print(f"  K-Factor type: {task_type}")
        print(f"  Size ratio: {classification['size_ratio']}")

    # Select hypothesis generators based on classification
    if classification["always_same_size"]:
        hyps = same_size_hypotheses(task)
    elif task_type.startswith("uniform_scale_") or task_type.startswith("scale_"):
        hyps = scale_hypotheses(task, classification["size_ratio"])
        hyps.extend(same_size_hypotheses(task))  # fallback
    elif task_type == "crop_or_extract":
        hyps = crop_hypotheses(task)
    else:
        hyps = variable_size_hypotheses(task)
        hyps.extend(scale_hypotheses(task, classification["size_ratio"]))
        hyps.extend(same_size_hypotheses(task))

    # Try all hypotheses
    for name, transform in hyps:
        if verify_on_train(task, transform):
            try:
                predictions = apply_to_test(task, transform)
                if verbose:
                    print(f"  ✓ {name}")
                return (name, predictions)
            except Exception:
                pass

    return None


def evaluate_smart(split: str = "training", verbose: bool = False) -> dict:
    """Run smart solver on all tasks."""
    tasks = load_all(split)
    solved = 0
    results = []
    type_stats = {}
    t0 = time.time()

    for task in tasks:
        classification = classify_transform(task)
        task_type = classification["type"]

        if task_type not in type_stats:
            type_stats[task_type] = {"total": 0, "solved": 0}
        type_stats[task_type]["total"] += 1

        result = smart_solve(task, verbose=verbose)
        if result is not None:
            name, predictions = result
            correct = all(
                pred == expected
                for pred, (_, expected) in zip(predictions, task.test)
                if expected.h > 0
            )
            if correct:
                solved += 1
                type_stats[task_type]["solved"] += 1
                results.append((task.id, name, True))
                if verbose:
                    print(f"✓ {task.id}: {name} [{task_type}]")
            else:
                results.append((task.id, name, False))
                if verbose:
                    print(f"✗ {task.id}: {name} (wrong on test) [{task_type}]")
        else:
            results.append((task.id, None, False))

    elapsed = time.time() - t0

    return {
        "total": len(tasks),
        "solved": solved,
        "accuracy": solved / len(tasks) if tasks else 0,
        "time_s": elapsed,
        "type_stats": type_stats,
        "results": results,
    }


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "eval":
        verbose = "--verbose" in sys.argv or "-v" in sys.argv
        print("Running K-Factor-guided evaluation...")
        stats = evaluate_smart("training", verbose=verbose)
        print(f"\n{'='*60}")
        print(f"Solved: {stats['solved']}/{stats['total']} ({stats['accuracy']:.1%})")
        print(f"Time: {stats['time_s']:.1f}s")
        print(f"\nBy transform type:")
        for t, s in sorted(stats['type_stats'].items(), key=lambda x: x[1]['total'], reverse=True):
            pct = s['solved'] / s['total'] * 100 if s['total'] else 0
            print(f"  {t:30s}: {s['solved']:3d}/{s['total']:3d} ({pct:5.1f}%)")
    elif len(sys.argv) > 1:
        task = load_task(sys.argv[1])
        task.show()
        print()
        result = smart_solve(task, verbose=True)
        if result:
            name, preds = result
            print(f"\nSolved: {name}")
            for p in preds:
                print(p.show())
        else:
            print("\nUnsolved.")
    else:
        print("Usage: python smart_solver.py <task_id> | eval [--verbose]")
