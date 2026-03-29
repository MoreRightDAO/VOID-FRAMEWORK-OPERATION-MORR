"""ARC-AGI solver framework.

Strategy: hypothesis generation → verification against training pairs → application to test.
Each solver is a function: (task) → Optional[list[Grid]] (one output per test input).
"""
from loader import Task, Grid, load_task, load_all
from dsl import *
from typing import Optional, Callable
import time

SolverFn = Callable[[Task], Optional[list[Grid]]]


class SolverResult:
    """Result from running a solver on a task."""
    def __init__(self, task_id: str, solver_name: str, predictions: Optional[list[Grid]],
                 correct: Optional[bool], time_s: float):
        self.task_id = task_id
        self.solver = solver_name
        self.predictions = predictions
        self.correct = correct
        self.time_s = time_s


def verify_on_train(task: Task, transform: Callable[[Grid], Grid]) -> bool:
    """Check if a transform correctly maps all training inputs to outputs."""
    for inp, expected in task.train:
        try:
            result = transform(inp)
            if result != expected:
                return False
        except Exception:
            return False
    return True


def apply_to_test(task: Task, transform: Callable[[Grid], Grid]) -> list[Grid]:
    """Apply verified transform to all test inputs."""
    return [transform(inp) for inp, _ in task.test]


# ─── Hypothesis generators ──────────────────────────────────────
# Each returns a list of candidate transforms

def identity_hypotheses() -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Basic geometric transforms."""
    return [
        ("identity", lambda g: g),
        ("rotate_90", rotate_90),
        ("rotate_180", rotate_180),
        ("rotate_270", rotate_270),
        ("flip_h", flip_h),
        ("flip_v", flip_v),
        ("transpose", transpose),
    ]


def tiling_hypotheses(task: Task) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Tiling and repetition."""
    hyps = []
    # Check output/input size ratios
    for inp, out in task.train[:1]:
        if out.h > 0 and inp.h > 0 and out.w > 0 and inp.w > 0:
            rh = out.h / inp.h
            rw = out.w / inp.w
            if rh == int(rh) and rw == int(rw):
                rh, rw = int(rh), int(rw)
                hyps.append((f"tile_{rh}x{rw}", lambda g, r=rh, c=rw: tile(g, r, c)))
                hyps.append((f"scale_{rh}", lambda g, f=rh: scale(g, f)))

    # Self-kronecker
    hyps.append(("self_kronecker", lambda g: self_kronecker(g, 0)))

    return hyps


def color_mapping_hypotheses(task: Task) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Simple color swaps/remaps."""
    hyps = []
    # Try all pairwise swaps
    all_colors = set()
    for inp, out in task.train:
        all_colors |= inp.colors() | out.colors()

    for a in all_colors:
        for b in all_colors:
            if a < b:
                hyps.append((f"swap_{a}_{b}", lambda g, x=a, y=b: swap_colors(g, x, y)))

    return hyps


def crop_hypotheses(task: Task) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Cropping to content."""
    hyps = [
        ("crop_to_content", crop_to_content),
    ]
    # Crop to specific color bounding box
    for inp, out in task.train[:1]:
        for color in inp.nonzero_colors():
            hyps.append((f"crop_to_{color}", lambda g, c=color: crop(g, *bounding_box(g, c))))
    return hyps


def composition_hypotheses(task: Task = None) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Compositions of basic transforms."""
    hyps = []

    # Flip + rotate combos
    for name1, fn1 in identity_hypotheses():
        for name2, fn2 in identity_hypotheses():
            if name1 != "identity" and name2 != "identity":
                hyps.append((f"{name1}+{name2}", lambda g, f1=fn1, f2=fn2: f2(f1(g))))

    # Overlay with rotations
    for name, fn in identity_hypotheses()[1:]:  # skip identity
        hyps.append((f"overlay_self+{name}",
                      lambda g, f=fn: overlay(g, f(g), 0)))

    return hyps


def size_change_hypotheses(task: Task) -> list[tuple[str, Callable[[Grid], Grid]]]:
    """Hypotheses involving output size different from input."""
    hyps = []
    for inp, out in task.train[:1]:
        # Fixed output size (fill with most common input color)
        oh, ow = out.shape()
        hyps.append((f"resize_to_{oh}x{ow}",
                      lambda g, h=oh, w=ow: Grid.empty(h, w, background_color(g))))

        # Object-based: extract largest object
        def extract_largest(g):
            objs = find_objects(g)
            if not objs:
                return g
            largest = max(objs, key=len)
            return extract_object(g, largest)
        hyps.append(("extract_largest_object", extract_largest))

        # Extract each object, try each
        def extract_nth(g, n=0):
            objs = find_objects(g)
            if n < len(objs):
                return extract_object(g, objs[n])
            return g
        for i in range(5):
            hyps.append((f"extract_object_{i}", lambda g, n=i: extract_nth(g, n)))

    return hyps


# ─── Master solver ──────────────────────────────────────────────

ALL_HYPOTHESIS_GENERATORS = [
    identity_hypotheses,
    tiling_hypotheses,
    color_mapping_hypotheses,
    crop_hypotheses,
    composition_hypotheses,
    size_change_hypotheses,
]


def solve_task(task: Task, verbose: bool = False) -> Optional[tuple[str, list[Grid]]]:
    """Try all hypotheses on a task. Returns (hypothesis_name, predictions) or None."""
    for gen in ALL_HYPOTHESIS_GENERATORS:
        if gen == identity_hypotheses:
            hypotheses = gen()
        else:
            hypotheses = gen(task)

        for name, transform in hypotheses:
            if verify_on_train(task, transform):
                if verbose:
                    print(f"  ✓ {name}")
                try:
                    predictions = apply_to_test(task, transform)
                    return (name, predictions)
                except Exception as e:
                    if verbose:
                        print(f"    (failed on test: {e})")
    return None


def evaluate(split: str = "training", verbose: bool = False) -> dict:
    """Run solver on all tasks in a split. Returns accuracy stats."""
    tasks = load_all(split)
    solved = 0
    failed = 0
    results = []
    t0 = time.time()

    for task in tasks:
        result = solve_task(task, verbose=verbose)
        if result is not None:
            name, predictions = result
            # Check correctness against test outputs (if available)
            correct = all(
                pred == expected
                for pred, (_, expected) in zip(predictions, task.test)
                if expected.h > 0
            )
            if correct:
                solved += 1
                results.append((task.id, name, True))
                if verbose:
                    print(f"✓ {task.id}: {name}")
            else:
                failed += 1
                results.append((task.id, name, False))
                if verbose:
                    print(f"✗ {task.id}: {name} (wrong on test)")
        else:
            failed += 1
            results.append((task.id, None, False))

    elapsed = time.time() - t0
    return {
        "split": split,
        "total": len(tasks),
        "solved": solved,
        "accuracy": solved / len(tasks) if tasks else 0,
        "time_s": elapsed,
        "results": results,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "eval":
        print("Running full evaluation on training set...")
        stats = evaluate("training", verbose="--verbose" in sys.argv)
        print(f"\n{'='*50}")
        print(f"Solved: {stats['solved']}/{stats['total']} ({stats['accuracy']:.1%})")
        print(f"Time: {stats['time_s']:.1f}s")
    elif len(sys.argv) > 1:
        task_id = sys.argv[1]
        task = load_task(task_id)
        task.show()
        print()
        result = solve_task(task, verbose=True)
        if result:
            name, preds = result
            print(f"\nSolved with: {name}")
            for i, p in enumerate(preds):
                print(f"\nPrediction {i}:")
                print(p.show())
        else:
            print("\nNo solution found with current hypotheses.")
    else:
        print("Usage:")
        print("  python solver.py <task_id>     # solve one task")
        print("  python solver.py eval           # evaluate all")
        print("  python solver.py eval --verbose # verbose evaluation")
