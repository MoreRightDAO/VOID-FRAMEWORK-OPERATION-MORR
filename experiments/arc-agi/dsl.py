"""DSL primitives for ARC-AGI grid transformations.

Each function takes Grid(s) and returns a Grid.
Composable, pure, no side effects.
"""
from loader import Grid
from collections import Counter
from typing import Optional
import numpy as np


# ─── Geometric transforms ───────────────────────────────────────

def rotate_90(g: Grid) -> Grid:
    """Rotate 90° clockwise."""
    return Grid([[g.data[g.h - 1 - r][c] for r in range(g.h)] for c in range(g.w)])

def rotate_180(g: Grid) -> Grid:
    return rotate_90(rotate_90(g))

def rotate_270(g: Grid) -> Grid:
    return rotate_90(rotate_90(rotate_90(g)))

def flip_h(g: Grid) -> Grid:
    """Flip horizontally (left-right)."""
    return Grid([row[::-1] for row in g.data])

def flip_v(g: Grid) -> Grid:
    """Flip vertically (top-bottom)."""
    return Grid(g.data[::-1])

def transpose(g: Grid) -> Grid:
    return Grid([[g.data[r][c] for r in range(g.h)] for c in range(g.w)])


# ─── Tiling / composition ───────────────────────────────────────

def tile(g: Grid, rows: int, cols: int) -> Grid:
    """Tile grid in an rows×cols arrangement."""
    data = []
    for tr in range(rows):
        for r in range(g.h):
            row = []
            for tc in range(cols):
                row.extend(g.data[r])
            data.append(row)
    return Grid(data)

def kronecker(g: Grid, kernel: Grid, bg: int = 0) -> Grid:
    """Kronecker product: each non-bg cell in g → copy of kernel, bg cells → blank."""
    h, w = kernel.h, kernel.w
    out = [[bg] * (g.w * w) for _ in range(g.h * h)]
    for r in range(g.h):
        for c in range(g.w):
            if g.data[r][c] != bg:
                for kr in range(h):
                    for kc in range(w):
                        out[r * h + kr][c * w + kc] = kernel.data[kr][kc]
    return Grid(out)

def self_kronecker(g: Grid, bg: int = 0) -> Grid:
    """Kronecker product of grid with itself."""
    return kronecker(g, g, bg)

def overlay(bottom: Grid, top: Grid, transparent: int = 0) -> Grid:
    """Overlay top onto bottom, treating transparent color as see-through."""
    assert bottom.h == top.h and bottom.w == top.w
    data = []
    for r in range(bottom.h):
        row = []
        for c in range(bottom.w):
            row.append(top.data[r][c] if top.data[r][c] != transparent else bottom.data[r][c])
        data.append(row)
    return Grid(data)

def hstack(grids: list[Grid]) -> Grid:
    """Horizontal concatenation."""
    data = []
    for r in range(grids[0].h):
        row = []
        for g in grids:
            row.extend(g.data[r])
        data.append(row)
    return Grid(data)

def vstack(grids: list[Grid]) -> Grid:
    """Vertical concatenation."""
    data = []
    for g in grids:
        data.extend(g.data)
    return Grid(data)


# ─── Cropping / extraction ──────────────────────────────────────

def crop(g: Grid, r1: int, c1: int, r2: int, c2: int) -> Grid:
    """Crop to bounding box [r1:r2, c1:c2] (exclusive end)."""
    return Grid([row[c1:c2] for row in g.data[r1:r2]])

def bounding_box(g: Grid, color: Optional[int] = None, exclude_bg: bool = True) -> tuple[int, int, int, int]:
    """Find bounding box of non-background or specific color cells. Returns (r1, c1, r2, c2)."""
    positions = []
    for r in range(g.h):
        for c in range(g.w):
            v = g.data[r][c]
            if color is not None:
                if v == color:
                    positions.append((r, c))
            elif exclude_bg and v != 0:
                positions.append((r, c))
    if not positions:
        return (0, 0, 0, 0)
    rs = [p[0] for p in positions]
    cs = [p[1] for p in positions]
    return (min(rs), min(cs), max(rs) + 1, max(cs) + 1)

def crop_to_content(g: Grid) -> Grid:
    """Crop to bounding box of non-zero content."""
    r1, c1, r2, c2 = bounding_box(g)
    return crop(g, r1, c1, r2, c2)


# ─── Color operations ───────────────────────────────────────────

def recolor(g: Grid, mapping: dict[int, int]) -> Grid:
    """Apply color mapping."""
    return Grid([[mapping.get(c, c) for c in row] for row in g.data])

def swap_colors(g: Grid, a: int, b: int) -> Grid:
    return recolor(g, {a: b, b: a})

def fill_color(g: Grid, color: int) -> Grid:
    """Replace all non-zero cells with color."""
    return Grid([[color if c != 0 else 0 for c in row] for row in g.data])

def background_color(g: Grid) -> int:
    """Most common color (usually the background)."""
    counts = Counter(c for row in g.data for c in row)
    return counts.most_common(1)[0][0]

def mask(g: Grid, color: int) -> Grid:
    """Binary mask: 1 where color appears, 0 elsewhere."""
    return Grid([[1 if c == color else 0 for c in row] for row in g.data])


# ─── Object extraction ──────────────────────────────────────────

def find_objects(g: Grid, bg: int = 0, connectivity: int = 4) -> list[set[tuple[int, int]]]:
    """Connected component extraction. Returns list of sets of (r,c) positions."""
    visited = set()
    objects = []
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if connectivity == 8:
        deltas += [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for r in range(g.h):
        for c in range(g.w):
            if g.data[r][c] != bg and (r, c) not in visited:
                # BFS
                obj = set()
                queue = [(r, c)]
                visited.add((r, c))
                while queue:
                    cr, cc = queue.pop(0)
                    obj.add((cr, cc))
                    for dr, dc in deltas:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < g.h and 0 <= nc < g.w and (nr, nc) not in visited:
                            if g.data[nr][nc] != bg:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                objects.append(obj)
    return objects

def extract_object(g: Grid, obj: set[tuple[int, int]], bg: int = 0) -> Grid:
    """Extract an object into its own grid (cropped to bounding box)."""
    rs = [r for r, c in obj]
    cs = [c for r, c in obj]
    r1, r2 = min(rs), max(rs) + 1
    c1, c2 = min(cs), max(cs) + 1
    data = [[bg] * (c2 - c1) for _ in range(r2 - r1)]
    for r, c in obj:
        data[r - r1][c - c1] = g.data[r][c]
    return Grid(data)


# ─── Pattern detection ──────────────────────────────────────────

def is_symmetric_h(g: Grid) -> bool:
    return all(row == row[::-1] for row in g.data)

def is_symmetric_v(g: Grid) -> bool:
    return g.data == g.data[::-1]

def is_symmetric_diag(g: Grid) -> bool:
    if g.h != g.w:
        return False
    return all(g.data[r][c] == g.data[c][r] for r in range(g.h) for c in range(g.w))

def periodicity(g: Grid, axis: int = 0) -> Optional[int]:
    """Find smallest period along axis (0=vertical, 1=horizontal). None if not periodic."""
    n = g.h if axis == 0 else g.w
    for p in range(1, n):
        if n % p != 0:
            continue
        periodic = True
        for i in range(n):
            if axis == 0:
                if g.data[i] != g.data[i % p]:
                    periodic = False
                    break
            else:
                for r in range(g.h):
                    if g.data[r][i] != g.data[r][i % p]:
                        periodic = False
                        break
                if not periodic:
                    break
        if periodic:
            return p
    return None


# ─── Grid analysis ──────────────────────────────────────────────

def grid_to_numpy(g: Grid) -> np.ndarray:
    return np.array(g.data, dtype=np.int32)

def numpy_to_grid(arr: np.ndarray) -> Grid:
    return Grid(arr.tolist())

def diff(a: Grid, b: Grid) -> list[tuple[int, int, int, int]]:
    """List of (r, c, a_val, b_val) where grids differ."""
    assert a.h == b.h and a.w == b.w
    diffs = []
    for r in range(a.h):
        for c in range(a.w):
            if a.data[r][c] != b.data[r][c]:
                diffs.append((r, c, a.data[r][c], b.data[r][c]))
    return diffs

def scale(g: Grid, factor: int) -> Grid:
    """Scale up grid by integer factor (each cell becomes factor×factor block)."""
    data = []
    for r in range(g.h):
        row = []
        for c in range(g.w):
            row.extend([g.data[r][c]] * factor)
        for _ in range(factor):
            data.append(list(row))
    return Grid(data)

def downscale(g: Grid, factor: int) -> Grid:
    """Downscale by factor (majority vote per block)."""
    h, w = g.h // factor, g.w // factor
    data = []
    for r in range(h):
        row = []
        for c in range(w):
            block = []
            for dr in range(factor):
                for dc in range(factor):
                    block.append(g.data[r * factor + dr][c * factor + dc])
            counts = Counter(block)
            row.append(counts.most_common(1)[0][0])
        data.append(row)
    return Grid(data)
