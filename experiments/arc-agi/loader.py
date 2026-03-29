"""ARC-AGI task loader and visualizer."""
import json
import os
from pathlib import Path
from typing import Optional

DATA_ROOT = Path(__file__).parent / "data" / "ARC-AGI" / "data"
TRAINING = DATA_ROOT / "training"
EVALUATION = DATA_ROOT / "evaluation"

# ARC color palette (matches official web app)
ARC_COLORS = {
    0: "⬛", 1: "🟦", 2: "🟥", 3: "🟩", 4: "🟨",
    5: "⬜", 6: "🟪", 7: "🟧", 8: "🩵", 9: "🟫",
}


class Grid:
    """Immutable 2D grid of integers 0-9."""

    __slots__ = ('data', 'h', 'w')

    def __init__(self, data: list[list[int]]):
        self.data = [list(row) for row in data]
        self.h = len(data)
        self.w = len(data[0]) if data else 0

    def __eq__(self, other):
        return isinstance(other, Grid) and self.data == other.data

    def __repr__(self):
        return f"Grid({self.h}x{self.w})"

    def show(self) -> str:
        """Emoji visualization."""
        return "\n".join("".join(ARC_COLORS.get(c, "?") for c in row) for row in self.data)

    def show_nums(self) -> str:
        """Numeric visualization."""
        return "\n".join(" ".join(str(c) for c in row) for row in self.data)

    def at(self, r: int, c: int) -> int:
        return self.data[r][c]

    def colors(self) -> set[int]:
        """All unique colors in grid."""
        return {c for row in self.data for c in row}

    def nonzero_colors(self) -> set[int]:
        return self.colors() - {0}

    def shape(self) -> tuple[int, int]:
        return (self.h, self.w)

    def to_list(self) -> list[list[int]]:
        return [list(row) for row in self.data]

    def count(self, color: int) -> int:
        return sum(row.count(color) for row in self.data)

    @staticmethod
    def empty(h: int, w: int, fill: int = 0) -> 'Grid':
        return Grid([[fill] * w for _ in range(h)])


class Task:
    """An ARC-AGI task with training pairs and test pair(s)."""

    def __init__(self, task_id: str, raw: dict):
        self.id = task_id
        self.train = [(Grid(p["input"]), Grid(p["output"])) for p in raw["train"]]
        self.test = [(Grid(p["input"]), Grid(p.get("output", [[]]))) for p in raw["test"]]

    @property
    def n_train(self) -> int:
        return len(self.train)

    def show(self):
        """Print full task visualization."""
        print(f"=== Task {self.id} ({self.n_train} train, {len(self.test)} test) ===")
        for i, (inp, out) in enumerate(self.train):
            print(f"\n--- Train {i} ---")
            print(f"Input {inp.shape()}:")
            print(inp.show())
            print(f"Output {out.shape()}:")
            print(out.show())
        for i, (inp, out) in enumerate(self.test):
            print(f"\n--- Test {i} ---")
            print(f"Input {inp.shape()}:")
            print(inp.show())
            if out.h > 0 and out.w > 0:
                print(f"Expected {out.shape()}:")
                print(out.show())


def load_task(task_id: str, split: str = "training") -> Task:
    """Load a single task by ID."""
    folder = TRAINING if split == "training" else EVALUATION
    path = folder / f"{task_id}.json"
    with open(path) as f:
        return Task(task_id, json.load(f))


def load_all(split: str = "training") -> list[Task]:
    """Load all tasks from a split."""
    folder = TRAINING if split == "training" else EVALUATION
    tasks = []
    for path in sorted(folder.glob("*.json")):
        with open(path) as f:
            tasks.append(Task(path.stem, json.load(f)))
    return tasks


def task_ids(split: str = "training") -> list[str]:
    """List all task IDs in a split."""
    folder = TRAINING if split == "training" else EVALUATION
    return sorted(p.stem for p in folder.glob("*.json"))


def stats(split: str = "training") -> dict:
    """Quick dataset statistics."""
    tasks = load_all(split)
    grid_sizes = []
    n_colors = []
    for t in tasks:
        for inp, out in t.train:
            grid_sizes.append(inp.h * inp.w)
            grid_sizes.append(out.h * out.w)
            n_colors.append(len(inp.colors()))
    return {
        "n_tasks": len(tasks),
        "avg_grid_cells": sum(grid_sizes) / len(grid_sizes),
        "max_grid_cells": max(grid_sizes),
        "avg_colors": sum(n_colors) / len(n_colors),
    }
