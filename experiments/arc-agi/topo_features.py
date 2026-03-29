"""Topological and percolation features for ARC-AGI grids.

Draws from two math apparatus sections:
- §73  Topological Classification: Euler characteristic, connected components,
       holes, winding-number-like invariants for grid objects
- §156 Percolation Threshold: spanning clusters, occupation density,
       critical connectivity analysis

These features tell the solver WHAT KIND of transform a task requires
before it tries to solve it.
"""
from collections import Counter, deque
from typing import Optional

import numpy as np

from loader import Grid, Task
from dsl import find_objects, extract_object, background_color, grid_to_numpy


# ─── §73: Topological invariants ─────────────────────────────────

def euler_characteristic(g: Grid, bg: int = None) -> int:
    """Compute the Euler characteristic χ = V - E + F for the non-bg region.

    Uses the cell-complex definition on the grid:
      V = vertices (corners of non-bg cells)
      E = edges (shared between adjacent non-bg cells)
      F = faces (non-bg cells themselves)

    χ = #components - #holes  (for 2D planar regions)
    """
    if bg is None:
        bg = background_color(g)

    # Binary mask: 1 = foreground
    m = np.array([[1 if g.data[r][c] != bg else 0
                   for c in range(g.w)] for r in range(g.h)], dtype=np.int32)

    # Count faces (non-bg cells)
    F = int(m.sum())
    if F == 0:
        return 0

    # Count edges (shared boundaries between adjacent non-bg cells)
    # Horizontal edges
    E_h = int((m[:, :-1] & m[:, 1:]).sum()) if g.w > 1 else 0
    # Vertical edges
    E_v = int((m[:-1, :] & m[1:, :]).sum()) if g.h > 1 else 0
    E = E_h + E_v

    # Count vertices (corners shared by non-bg cells)
    # A vertex exists at each 2x2 block corner where at least one cell is non-bg
    # For Euler char, count vertices where adjacent cells share a corner
    V = 0
    if g.h > 1 and g.w > 1:
        for r in range(g.h - 1):
            for c in range(g.w - 1):
                block = m[r, c] + m[r, c+1] + m[r+1, c] + m[r+1, c+1]
                if block >= 2:
                    # Vertex exists if 2+ cells meet at this corner
                    V += 1

    # Standard grid Euler: χ = V - E + F
    return V - E + F


def count_holes(g: Grid, bg: int = None) -> int:
    """Count enclosed holes (background regions fully surrounded by foreground).

    A hole = a connected component of bg cells that doesn't touch the grid border.
    This is the genus of the foreground region.
    """
    if bg is None:
        bg = background_color(g)

    visited = set()
    holes = 0

    for r in range(g.h):
        for c in range(g.w):
            if g.data[r][c] == bg and (r, c) not in visited:
                # BFS to find this bg component
                component = set()
                queue = deque([(r, c)])
                visited.add((r, c))
                touches_border = False

                while queue:
                    cr, cc = queue.popleft()
                    component.add((cr, cc))
                    if cr == 0 or cr == g.h - 1 or cc == 0 or cc == g.w - 1:
                        touches_border = True
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < g.h and 0 <= nc < g.w:
                            if g.data[nr][nc] == bg and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))

                if not touches_border and len(component) > 0:
                    holes += 1

    return holes


def object_topology(g: Grid, obj: set[tuple[int, int]], bg: int = 0) -> dict:
    """Topological features of a single object.

    Returns genus (holes), boundary length, compactness, and convexity.
    """
    if not obj:
        return {"genus": 0, "boundary": 0, "compactness": 0, "convexity": 0, "area": 0}

    area = len(obj)

    # Boundary = perimeter cells (adjacent to bg or grid edge)
    boundary = 0
    for r, c in obj:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= g.h or nc < 0 or nc >= g.w or (nr, nc) not in obj:
                boundary += 1

    # Extract object into its own grid for hole counting
    obj_grid = extract_object(g, obj, bg)
    genus = count_holes(obj_grid, bg)

    # Compactness = 4π·area / perimeter² (1.0 for circle, less for complex shapes)
    compactness = round(4 * 3.14159 * area / (boundary ** 2), 3) if boundary > 0 else 0

    # Convexity = area / convex_hull_area
    rs = [r for r, c in obj]
    cs = [c for r, c in obj]
    bbox_area = (max(rs) - min(rs) + 1) * (max(cs) - min(cs) + 1)
    convexity = round(area / bbox_area, 3) if bbox_area > 0 else 0

    return {
        "genus": genus,
        "boundary": boundary,
        "compactness": compactness,
        "convexity": convexity,
        "area": area,
    }


# ─── §156: Percolation features ──────────────────────────────────

def occupation_density(g: Grid, bg: int = None) -> float:
    """Fraction of non-background cells. Analogous to site occupation probability p."""
    if bg is None:
        bg = background_color(g)
    total = g.h * g.w
    occupied = sum(1 for r in range(g.h) for c in range(g.w) if g.data[r][c] != bg)
    return round(occupied / total, 4) if total > 0 else 0


def spans_grid(g: Grid, color: int = None, bg: int = None, axis: str = "both") -> dict:
    """Check if a color/foreground spans the grid edge-to-edge.

    Spanning = percolation. A cluster spans if it connects opposite borders.
    axis: "h" (left-right), "v" (top-bottom), "both"
    """
    if bg is None:
        bg = background_color(g)

    # Get cells of interest
    if color is not None:
        cells = {(r, c) for r in range(g.h) for c in range(g.w) if g.data[r][c] == color}
    else:
        cells = {(r, c) for r in range(g.h) for c in range(g.w) if g.data[r][c] != bg}

    if not cells:
        return {"spans_h": False, "spans_v": False, "spans_both": False}

    # Find connected components via BFS
    visited = set()
    spans_h = False
    spans_v = False

    for start in cells:
        if start in visited:
            continue
        queue = deque([start])
        visited.add(start)
        component = set()
        while queue:
            cr, cc = queue.popleft()
            component.add((cr, cc))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = cr + dr, cc + dc
                if (nr, nc) in cells and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        # Check spanning
        rows = {r for r, c in component}
        cols = {c for r, c in component}
        if 0 in cols and (g.w - 1) in cols:
            spans_h = True
        if 0 in rows and (g.h - 1) in rows:
            spans_v = True

    return {
        "spans_h": spans_h,
        "spans_v": spans_v,
        "spans_both": spans_h and spans_v,
    }


def largest_cluster_fraction(g: Grid, bg: int = None) -> float:
    """Size of largest connected component / total foreground cells.

    Near 1.0 = one dominant cluster (above percolation).
    Near 0.0 = fragmented (below percolation).
    """
    if bg is None:
        bg = background_color(g)
    objects = find_objects(g, bg)
    if not objects:
        return 0.0
    total_fg = sum(len(o) for o in objects)
    largest = max(len(o) for o in objects)
    return round(largest / total_fg, 4) if total_fg > 0 else 0


def color_adjacency_graph(g: Grid, bg: int = None) -> dict[tuple[int, int], int]:
    """Build adjacency counts between colors.

    Returns dict of (color_a, color_b) -> count of adjacencies.
    This captures the interaction structure between colors.
    """
    if bg is None:
        bg = background_color(g)

    adj = Counter()
    for r in range(g.h):
        for c in range(g.w):
            v = g.data[r][c]
            for dr, dc in [(0, 1), (1, 0)]:  # right and down only (avoid double-counting)
                nr, nc = r + dr, c + dc
                if 0 <= nr < g.h and 0 <= nc < g.w:
                    nv = g.data[nr][nc]
                    if v != nv:  # only different-color adjacencies
                        pair = (min(v, nv), max(v, nv))
                        adj[pair] += 1
    return dict(adj)


def border_colors(g: Grid) -> set[int]:
    """Colors that appear on the grid border."""
    colors = set()
    for c in range(g.w):
        colors.add(g.data[0][c])
        colors.add(g.data[g.h - 1][c])
    for r in range(g.h):
        colors.add(g.data[r][0])
        colors.add(g.data[r][g.w - 1])
    return colors


def interior_colors(g: Grid) -> set[int]:
    """Colors that appear only in the interior (not on border)."""
    border = border_colors(g)
    all_colors = g.colors()
    return all_colors - border


# ─── Combined feature extraction ─────────────────────────────────

def topo_features(g: Grid, bg: int = None) -> dict:
    """Full topological + percolation feature vector for a grid."""
    if bg is None:
        bg = background_color(g)

    objects = find_objects(g, bg)

    # Per-object topology
    obj_topos = []
    for obj in sorted(objects, key=len, reverse=True)[:8]:
        obj_topos.append(object_topology(g, obj, bg))

    total_holes = sum(t["genus"] for t in obj_topos)
    total_boundary = sum(t["boundary"] for t in obj_topos)

    # Percolation
    spanning = spans_grid(g, bg=bg)
    density = occupation_density(g, bg)

    return {
        # §73: Topology
        "n_components": len(objects),
        "n_holes": total_holes,
        "euler_chi": len(objects) - total_holes,  # χ = components - holes
        "total_boundary": total_boundary,
        "mean_compactness": round(np.mean([t["compactness"] for t in obj_topos]), 3) if obj_topos else 0,
        "mean_convexity": round(np.mean([t["convexity"] for t in obj_topos]), 3) if obj_topos else 0,
        "has_holes": total_holes > 0,
        "max_genus": max((t["genus"] for t in obj_topos), default=0),

        # §156: Percolation
        "density": density,
        "spans_h": spanning["spans_h"],
        "spans_v": spanning["spans_v"],
        "spans_both": spanning["spans_both"],
        "largest_cluster_frac": largest_cluster_fraction(g, bg),
        "n_border_colors": len(border_colors(g)),
        "n_interior_colors": len(interior_colors(g)),

        # Color interaction
        "n_color_adjacencies": len(color_adjacency_graph(g, bg)),
    }


def transform_topo_delta(task: Task) -> dict:
    """Topological changes from input→output across training examples.

    This tells you what the transform DOES topologically:
    - Adds holes? (fill_or_mark type)
    - Changes component count? (split/merge)
    - Changes spanning? (connect/disconnect)
    - Changes density? (grow/shrink)
    """
    deltas = []
    for inp, out in task.train:
        bg = background_color(inp)
        inp_f = topo_features(inp, bg)
        out_f = topo_features(out, bg)

        delta = {}
        for key in inp_f:
            iv, ov = inp_f[key], out_f[key]
            if isinstance(iv, (int, float)) and isinstance(ov, (int, float)):
                delta[key] = round(ov - iv, 4)
            elif isinstance(iv, bool):
                delta[key] = (iv, ov)  # transition
        deltas.append(delta)

    # Aggregate: check consistency across examples
    if not deltas:
        return {}

    agg = {}
    for key in deltas[0]:
        vals = [d.get(key) for d in deltas]
        if all(isinstance(v, (int, float)) for v in vals):
            agg[f"{key}_delta"] = vals[0] if len(set(vals)) == 1 else "varies"
            agg[f"{key}_consistent"] = len(set(vals)) == 1
            if all(v == 0 for v in vals):
                agg[f"{key}_preserved"] = True
        elif all(isinstance(v, tuple) for v in vals):
            agg[f"{key}_transition"] = vals[0] if len(set(vals)) == 1 else "varies"

    return agg


def classify_topo(task: Task) -> dict:
    """High-level topological classification of the task.

    Returns tags that can guide solver strategy selection.
    """
    delta = transform_topo_delta(task)
    tags = set()

    # Check what changes
    if delta.get("n_holes_consistent") and delta.get("n_holes_delta", 0) != 0:
        if delta["n_holes_delta"] == "varies":
            tags.add("variable_holes")
        elif delta["n_holes_delta"] > 0:
            tags.add("creates_holes")
        else:
            tags.add("fills_holes")

    if delta.get("n_components_consistent") and delta.get("n_components_delta", 0) != 0:
        d = delta["n_components_delta"]
        if d == "varies":
            tags.add("variable_components")
        elif d > 0:
            tags.add("splits_objects")
        else:
            tags.add("merges_objects")

    if delta.get("density_preserved"):
        tags.add("density_preserved")
    elif delta.get("density_consistent"):
        d = delta.get("density_delta", 0)
        if isinstance(d, (int, float)):
            if d > 0.05:
                tags.add("grows")
            elif d < -0.05:
                tags.add("shrinks")

    # Spanning changes
    for axis in ["spans_h", "spans_v"]:
        trans = delta.get(f"{axis}_transition")
        if trans == (False, True):
            tags.add("connects")
        elif trans == (True, False):
            tags.add("disconnects")

    # Hole-related
    inp_features = [topo_features(inp, background_color(inp)) for inp, _ in task.train]
    if any(f["has_holes"] for f in inp_features):
        tags.add("input_has_holes")

    # Boundary-related
    if delta.get("total_boundary_preserved"):
        tags.add("boundary_preserved")

    # When topology gives no signal, try harder with other analyses
    if not tags:
        # Check symmetry changes
        from dsl import is_symmetric_h, is_symmetric_v, is_symmetric_diag
        sym_changes = []
        for inp, out in task.train:
            inp_sym = (is_symmetric_h(inp), is_symmetric_v(inp), is_symmetric_diag(inp))
            out_sym = (is_symmetric_h(out), is_symmetric_v(out), is_symmetric_diag(out))
            if inp_sym != out_sym:
                sym_changes.append((inp_sym, out_sym))
        if sym_changes:
            # Check if symmetry is being created
            if all(not any(s[0]) and any(s[1]) for s in sym_changes):
                tags.add("creates_symmetry")
            elif all(any(s[0]) and not any(s[1]) for s in sym_changes):
                tags.add("breaks_symmetry")
            else:
                tags.add("modifies_symmetry")

        # Check if it's a positional rearrangement (same colors, different positions)
        for inp, out in task.train:
            if inp.h == out.h and inp.w == out.w:
                inp_counts = Counter(c for row in inp.data for c in row)
                out_counts = Counter(c for row in out.data for c in row)
                if inp_counts == out_counts:
                    tags.add("rearrangement")
                    break

    if not tags:
        tags.add("topo_neutral")

    return {
        "tags": sorted(tags),
        "delta": delta,
    }


# ─── CLI ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    from loader import load_task, task_ids

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python topo_features.py <task_id>     # analyze one task")
        print("  python topo_features.py survey [N]    # survey task types")
        sys.exit(0)

    if sys.argv[1] == "survey":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        ids = task_ids("training")[:limit]
        tag_counts = Counter()

        for tid in ids:
            task = load_task(tid)
            cls = classify_topo(task)
            for tag in cls["tags"]:
                tag_counts[tag] += 1

        print(f"Topological survey of {limit} tasks:")
        print(f"{'Tag':<25} {'Count':>5} {'Pct':>6}")
        print("-" * 40)
        for tag, count in tag_counts.most_common():
            print(f"{tag:<25} {count:>5} {count/limit:>5.1%}")
    else:
        task_id = sys.argv[1]
        task = load_task(task_id)
        task.show()

        print("\n=== Topological Features ===")
        bg = background_color(task.train[0][0])
        for i, (inp, out) in enumerate(task.train):
            print(f"\n--- Example {i} ---")
            inp_f = topo_features(inp, bg)
            out_f = topo_features(out, bg)
            print(f"Input:  {inp_f}")
            print(f"Output: {out_f}")

        print(f"\n=== Transform Topo Delta ===")
        delta = transform_topo_delta(task)
        for k, v in sorted(delta.items()):
            if not str(k).endswith("_preserved") or v:
                print(f"  {k}: {v}")

        print(f"\n=== Classification ===")
        cls = classify_topo(task)
        print(f"Tags: {cls['tags']}")
