"""ARC-AGI-3 Packet Probe — Phase 0 game analysis via byte-level tricks.

Spends 20-30 actions (zero LLM) to build a complete GameProfile:
  - Game type classification
  - Determinism check
  - Action→direction mapping
  - Nibble transition vocabulary (the game's "instruction set")
  - Bit-plane independence (which bits carry which mechanics)
  - XOR template library (reusable action fingerprints)
  - Delta compression signature (rule complexity estimate)
  - Cycle detection via XOR accumulation
  - Clickable region heatmap (for ACTION6 games)
  - Markov order estimate (how much history matters)

The GameProfile feeds directly into solver selection.
"""
import hashlib
import zlib
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage

import arc_agi
from arcengine import GameState


# ─── Bit / byte primitives ───────────────────────────────────────

def pack_4bit(grid: np.ndarray) -> bytes:
    flat = grid.astype(np.uint8).flatten()
    return ((flat[0::2] << 4) | (flat[1::2] & 0x0F)).tobytes()


def frame_hash(grid: np.ndarray) -> str:
    return hashlib.md5(grid.astype(np.uint8).tobytes()).hexdigest()[:12]


def xor_grids(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a.astype(np.uint8) ^ b.astype(np.uint8)


def zlib_ratio(data: bytes) -> float:
    """Compression ratio — lower = more structured."""
    compressed = zlib.compress(data, level=9)
    return len(compressed) / len(data)


def bit_plane(grid: np.ndarray, bit: int) -> np.ndarray:
    """Extract single bit plane (0=LSB, 3=MSB for 4-bit values)."""
    return (grid.astype(np.uint8) >> bit) & 1


def rle_count(data: bytes) -> int:
    """Run-length encoding run count — fewer runs = more spatial structure."""
    if len(data) < 2:
        return len(data)
    runs = 1
    for i in range(1, len(data)):
        if data[i] != data[i-1]:
            runs += 1
    return runs


# ─── XOR template matching ───────────────────────────────────────

def extract_xor_template(xor: np.ndarray) -> Optional[dict]:
    """Extract the bounding box of an XOR pattern as a reusable template."""
    changed = xor > 0
    if not changed.any():
        return None

    rows, cols = np.where(changed)
    r0, r1 = int(rows.min()), int(rows.max()) + 1
    c0, c1 = int(cols.min()), int(cols.max()) + 1
    template = xor[r0:r1, c0:c1].copy()

    return {
        "template": template,
        "origin": (r0, c0),
        "shape": template.shape,
        "hash": hashlib.md5(template.tobytes()).hexdigest()[:8],
        "n_changed": int(changed.sum()),
        "density": int(changed.sum()) / (template.shape[0] * template.shape[1]),
    }


def templates_match(t1: dict, t2: dict, position_invariant: bool = True) -> bool:
    """Check if two XOR templates encode the same transformation."""
    if t1["shape"] != t2["shape"]:
        return False
    if position_invariant:
        return np.array_equal(t1["template"], t2["template"])
    return t1["hash"] == t2["hash"] and t1["origin"] == t2["origin"]


# ─── Game profile ────────────────────────────────────────────────

@dataclass
class GameProfile:
    """Complete Phase 0 analysis of a game — feeds into solver."""
    game_id: str
    available_actions: list[int]
    win_levels: int

    # Classification
    game_type: str          # AGENT-KB, AGENT-HYBRID, CLICK-ONLY, FIELD, MIXED, LOCKED
    is_deterministic: bool  # same state + action = same result
    markov_order: int       # 0 = memoryless, 1 = depends on previous action, etc.

    # Action analysis
    action_directions: dict     # action → (dr, dc) movement vector (for keyboard actions)
    action_noop_rate: dict      # action → fraction of times it does nothing
    action_templates: dict      # action → list of XOR template dicts
    action_compression: dict    # action → mean zlib ratio of XOR

    # Byte-level
    nibble_vocab: dict          # "a→b" → count — the game's color transition alphabet
    bit_plane_entropy: list     # [bit0_ent, bit1_ent, bit2_ent, bit3_ent]
    bit_plane_independence: float  # 0=fully coupled, 1=fully independent

    # Structure
    xor_rle_mean: float         # mean RLE runs in XOR — lower = more spatially structured
    delta_compress_mean: float  # mean zlib ratio — lower = simpler rules
    com_spread: float           # center-of-mass spread — low = agent, high = field
    com_centroid: tuple         # (r, c) where changes concentrate

    # Cycle / predictability
    has_cycles: bool            # XOR accumulation returns to zero
    cycle_length: int           # shortest detected cycle (0 = no cycle found)

    # Click games
    click_heatmap: Optional[np.ndarray]  # 64×64 float, where clicks have effect
    clickable_colors: list      # colors that respond to clicks

    # Templates
    template_library: dict      # hash → template dict — unique transition fingerprints
    n_unique_templates: int

    # Raw for downstream
    probe_frames: list          # raw numpy frames captured during probe
    probe_actions: list         # actions taken during probe

    def solver_hint(self) -> str:
        """One-line hint for the solver."""
        parts = [self.game_type]
        if self.is_deterministic:
            parts.append("DETERMINISTIC")
        if self.has_cycles:
            parts.append(f"CYCLES(len={self.cycle_length})")
        parts.append(f"vocab={len(self.nibble_vocab)}")
        parts.append(f"templates={self.n_unique_templates}")
        parts.append(f"compress={self.delta_compress_mean:.3f}")
        if self.click_heatmap is not None:
            n_hot = int((self.click_heatmap > 0.3).sum())
            parts.append(f"clickable={n_hot}px")
        return " | ".join(parts)

    def best_actions(self) -> list[int]:
        """Actions sorted by effectiveness (lowest noop rate first)."""
        return sorted(self.action_noop_rate.keys(),
                      key=lambda a: self.action_noop_rate.get(a, 1.0))


# ─── Probe engine ────────────────────────────────────────────────

def probe_game(game_id: str, budget: int = 30, verbose: bool = False) -> GameProfile:
    """Run Phase 0 packet probe on a game. Returns GameProfile."""

    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    available = list(obs.available_actions)
    win_levels = obs.win_levels
    has_click = 6 in available
    has_keys = any(a in available for a in [1, 2, 3, 4])
    non_click = [a for a in available if a != 6]

    frames = [np.array(obs.frame[0])]
    actions_taken = []
    state_action_results = {}  # (state_hash, action) → result_hash
    rng = np.random.default_rng(42)

    # ─── Tracking accumulators ───
    action_xors = defaultdict(list)          # action → [xor arrays]
    action_noops = defaultdict(int)
    action_total = defaultdict(int)
    action_templates = defaultdict(list)
    action_compression = defaultdict(list)
    nibble_vocab = Counter()
    coms = []
    all_rle = []
    all_compress = []
    click_hits = np.zeros((64, 64), dtype=np.float32)
    click_total = np.zeros((64, 64), dtype=np.float32)
    clickable_colors = set()
    template_library = {}

    # ─── Phase 1: Systematic action testing (keyboard) ───
    step = 0
    base_hash = frame_hash(frames[0])

    def take_action(action, click_x=None, click_y=None):
        nonlocal obs, step
        prev_grid = np.array(obs.frame[0])
        prev_hash = frame_hash(prev_grid)

        if action == 6 and click_x is not None:
            obs = env.step(6, data={"x": click_x, "y": click_y})
        else:
            obs = env.step(action)

        curr_grid = np.array(obs.frame[0])
        curr_hash = frame_hash(curr_grid)
        frames.append(curr_grid)
        actions_taken.append(action)

        # XOR analysis
        xor = xor_grids(prev_grid, curr_grid)
        is_noop = not xor.any()

        action_total[action] += 1
        if is_noop:
            action_noops[action] += 1
        else:
            action_xors[action].append(xor)

            # Nibble vocabulary
            changed = xor > 0
            old_v = prev_grid[changed]
            new_v = curr_grid[changed]
            for o, n in zip(old_v.tolist(), new_v.tolist()):
                nibble_vocab[f"{o:x}→{n:x}"] += 1

            # Template
            tmpl = extract_xor_template(xor)
            if tmpl:
                action_templates[action].append(tmpl)
                template_library[tmpl["hash"]] = tmpl

            # Compression
            xor_bytes = xor.tobytes()
            cr = zlib_ratio(xor_bytes)
            action_compression[action].append(cr)
            all_compress.append(cr)
            all_rle.append(rle_count(xor_bytes))

            # Center of mass
            rows, cols = np.where(changed)
            coms.append((float(rows.mean()), float(cols.mean())))

        # Determinism tracking
        key = (prev_hash, action)
        if key in state_action_results:
            if state_action_results[key] != curr_hash:
                state_action_results[key] = "__NONDETERMINISTIC__"
        else:
            state_action_results[key] = curr_hash

        step += 1
        return is_noop, xor, curr_grid

    # Test each keyboard action 3× from start
    for a in non_click:
        if step >= budget:
            break
        # Reset to start for clean test
        obs = env.reset()
        frames_reset = [np.array(obs.frame[0])]
        for _ in range(3):
            if step >= budget or obs.state in (GameState.WIN, GameState.GAME_OVER):
                break
            take_action(a)

    # ─── Phase 2: Click probing (for ACTION6 games) ───
    if has_click and step < budget:
        obs = env.reset()
        frames.append(np.array(obs.frame[0]))
        g = np.array(obs.frame[0])
        bg = int(np.bincount(g.flatten()).argmax())

        # Scan: click on each distinct color region
        colors_present = sorted(set(g.flatten().tolist()) - {bg})
        for color in colors_present:
            if step >= budget:
                break
            positions = np.where(g == color)
            if len(positions[0]) == 0:
                continue
            # Click center of this color's mass
            cy = int(positions[0].mean())
            cx = int(positions[1].mean())
            click_total[cy, cx] += 1
            noop, xor, _ = take_action(6, click_x=cx, click_y=cy)
            if not noop:
                click_hits[cy, cx] += 1
                clickable_colors.add(color)
                if verbose:
                    print(f"  Click ({cx},{cy}) color={color}: HIT ({int(xor.sum())} changed)")

        # Random clicks on non-bg pixels for remaining budget
        nonbg = np.where(g != bg)
        while step < budget and len(nonbg[0]) > 0:
            if obs.state in (GameState.WIN, GameState.GAME_OVER):
                break
            idx = rng.integers(len(nonbg[0]))
            cy, cx = int(nonbg[0][idx]), int(nonbg[1][idx])
            click_total[cy, cx] += 1
            noop, xor, _ = take_action(6, click_x=cx, click_y=cy)
            if not noop:
                click_hits[cy, cx] += 1
                clickable_colors.add(int(g[cy, cx]))

    # ─── Phase 3: Mixed exploration for remaining budget ───
    while step < budget:
        if obs.state in (GameState.WIN, GameState.GAME_OVER):
            break
        if non_click:
            a = non_click[step % len(non_click)]
            take_action(a)
        elif has_click:
            g = np.array(obs.frame[0])
            bg = int(np.bincount(g.flatten()).argmax())
            nonbg = np.where(g != bg)
            if len(nonbg[0]) > 0:
                idx = rng.integers(len(nonbg[0]))
                take_action(6, click_x=int(nonbg[1][idx]), click_y=int(nonbg[0][idx]))
            else:
                break
        else:
            break

    # ─── Analyze results ───

    # Determinism
    is_deterministic = "__NONDETERMINISTIC__" not in state_action_results.values()

    # Action directions (for keyboard games)
    action_dirs = {}
    for a in non_click:
        xors = action_xors.get(a, [])
        if len(xors) < 2:
            continue
        # Average displacement of changed cells
        drs, dcs = [], []
        for i in range(1, len(xors)):
            prev_rows, prev_cols = np.where(xors[i-1] > 0)
            curr_rows, curr_cols = np.where(xors[i] > 0)
            if len(prev_rows) > 0 and len(curr_rows) > 0:
                dr = curr_rows.mean() - prev_rows.mean()
                dc = curr_cols.mean() - prev_cols.mean()
                drs.append(dr)
                dcs.append(dc)
        if drs:
            action_dirs[a] = (round(np.mean(drs), 1), round(np.mean(dcs), 1))

    # Noop rates
    noop_rates = {a: action_noops[a] / max(action_total[a], 1) for a in available}

    # Bit plane analysis
    g = frames[0].astype(np.uint8)
    bp_entropy = []
    bp_changes = [np.zeros(4) for _ in range(4)]
    for bit in range(4):
        plane = bit_plane(g, bit)
        p = plane.mean()
        ent = -(p * np.log2(p + 1e-12) + (1-p) * np.log2(1-p + 1e-12)) if 0 < p < 1 else 0
        bp_entropy.append(round(ent, 4))

    # Bit plane independence: check if XOR bits are correlated
    bp_independence = 0.0
    if action_xors:
        all_xor_stack = []
        for xors in action_xors.values():
            all_xor_stack.extend(xors)
        if len(all_xor_stack) >= 3:
            xor_bits = np.stack([
                np.stack([bit_plane(x, b).flatten() for b in range(4)])
                for x in all_xor_stack[:10]
            ])  # shape: (n_samples, 4, 4096)

            # Correlation between bit planes across XOR samples
            flat = xor_bits.reshape(xor_bits.shape[0], 4, -1)
            means = flat.mean(axis=(0, 2))
            if means.sum() > 0:
                # Pairwise correlation of bit plane activation
                corrs = []
                for i in range(4):
                    for j in range(i+1, 4):
                        a_flat = flat[:, i, :].flatten().astype(float)
                        b_flat = flat[:, j, :].flatten().astype(float)
                        if a_flat.std() > 0 and b_flat.std() > 0:
                            corr = abs(np.corrcoef(a_flat, b_flat)[0, 1])
                            corrs.append(corr)
                if corrs:
                    bp_independence = round(1.0 - np.mean(corrs), 4)

    # Compression stats
    compress_mean = np.mean(all_compress) if all_compress else 1.0
    rle_mean = np.mean(all_rle) if all_rle else 4096

    # CoM spread
    if coms:
        com_arr = np.array(coms)
        com_spread = float(np.std(com_arr, axis=0).mean())
        com_centroid = (float(com_arr[:, 0].mean()), float(com_arr[:, 1].mean()))
    else:
        com_spread = 0.0
        com_centroid = (32.0, 32.0)

    # Cycle detection: check if XOR(frame_0, frame_i) ever returns to zero
    has_cycles = False
    cycle_length = 0
    base = frames[0].astype(np.uint8)
    for i in range(1, len(frames)):
        diff = int((base ^ frames[i].astype(np.uint8) > 0).sum())
        if diff == 0 and i > 1:
            has_cycles = True
            cycle_length = i
            break

    # Click heatmap normalization
    click_hm = None
    if has_click and click_total.sum() > 0:
        with np.errstate(divide='ignore', invalid='ignore'):
            click_hm = np.where(click_total > 0, click_hits / click_total, 0.0)

    # Game type classification
    noop_total = sum(action_noops.values()) / max(sum(action_total.values()), 1)
    if noop_total > 0.8:
        game_type = "LOCKED"
    elif com_spread < 5 and not has_click:
        game_type = "AGENT-KB"
    elif com_spread < 5 and has_click and has_keys:
        game_type = "AGENT-HYBRID"
    elif has_click and not has_keys:
        game_type = "CLICK-ONLY"
    elif com_spread > 15:
        game_type = "FIELD"
    else:
        game_type = "MIXED"

    # Markov order estimate: do transitions depend on previous action?
    # If same action from same state always gives same result → order 0
    # If same action from same state gives different results → order ≥ 1
    markov_order = 0 if is_deterministic else 1

    # Action compression means
    act_compress = {a: round(np.mean(v), 4) if v else 1.0
                   for a, v in action_compression.items()}

    profile = GameProfile(
        game_id=game_id,
        available_actions=available,
        win_levels=win_levels,
        game_type=game_type,
        is_deterministic=is_deterministic,
        markov_order=markov_order,
        action_directions=action_dirs,
        action_noop_rate=noop_rates,
        action_templates={a: ts for a, ts in action_templates.items()},
        action_compression=act_compress,
        nibble_vocab=dict(nibble_vocab.most_common()),
        bit_plane_entropy=bp_entropy,
        bit_plane_independence=bp_independence,
        xor_rle_mean=round(rle_mean, 1),
        delta_compress_mean=round(compress_mean, 4),
        com_spread=round(com_spread, 1),
        com_centroid=com_centroid,
        has_cycles=has_cycles,
        cycle_length=cycle_length,
        click_heatmap=click_hm,
        clickable_colors=sorted(clickable_colors),
        template_library=template_library,
        n_unique_templates=len(template_library),
        probe_frames=frames,
        probe_actions=actions_taken,
    )

    if verbose:
        print_profile(profile)

    return profile


# ─── Extrapolation engine ────────────────────────────────────────

def predict_frame(profile: GameProfile, current_frame: np.ndarray, action: int) -> Optional[np.ndarray]:
    """Predict the next frame from current frame + action using template library.

    If the game is deterministic and we've seen this state+action before,
    we can predict the exact result. If not, we use the closest matching
    template to estimate what will change.

    Returns predicted frame or None if unpredictable.
    """
    curr_hash = frame_hash(current_frame)

    # Exact match: did we see this exact state + action during probe?
    for i, (f, a) in enumerate(zip(profile.probe_frames[:-1], profile.probe_actions)):
        if a == action and frame_hash(f) == curr_hash:
            return profile.probe_frames[i + 1].copy()

    # Template-based prediction: apply the most common template for this action
    templates = profile.action_templates.get(action, [])
    if not templates:
        return None

    # Find template with best spatial overlap to current non-bg content
    current_bg = int(np.bincount(current_frame.flatten()).argmax())
    best_tmpl = None
    best_score = -1

    for tmpl in templates:
        r0, c0 = tmpl["origin"]
        th, tw = tmpl["shape"]
        # Check if the template region in current frame has content
        region = current_frame[r0:r0+th, c0:c0+tw]
        if region.shape != (th, tw):
            continue
        non_bg = (region != current_bg).sum()
        if non_bg > best_score:
            best_score = non_bg
            best_tmpl = tmpl

    if best_tmpl is None:
        return None

    # Apply template: XOR the template onto the current frame
    predicted = current_frame.copy().astype(np.uint8)
    r0, c0 = best_tmpl["origin"]
    th, tw = best_tmpl["shape"]
    predicted[r0:r0+th, c0:c0+tw] ^= best_tmpl["template"]
    return predicted


def interpolate_path(profile: GameProfile, start_frame: np.ndarray,
                     target_frame: np.ndarray) -> Optional[list[int]]:
    """Given start and target frames, infer the action sequence to get there.

    Uses the nibble vocabulary to figure out what color transitions are needed,
    then maps those to actions via the template library.
    """
    xor = xor_grids(start_frame, target_frame)
    if not xor.any():
        return []  # already there

    # What nibble transitions are needed?
    changed = xor > 0
    old_v = start_frame[changed]
    new_v = target_frame[changed]
    needed_transitions = Counter()
    for o, n in zip(old_v.tolist(), new_v.tolist()):
        needed_transitions[f"{o:x}→{n:x}"] += 1

    # Which actions produce these transitions?
    action_scores = defaultdict(float)
    for action, templates in profile.action_templates.items():
        for tmpl in templates:
            tmpl_xor = tmpl["template"]
            # Check overlap with needed change region
            r0, c0 = tmpl["origin"]
            th, tw = tmpl["shape"]
            target_region = xor[r0:r0+th, c0:c0+tw]
            if target_region.shape == tmpl_xor.shape:
                overlap = (tmpl_xor > 0) & (target_region > 0)
                action_scores[action] += overlap.sum()

    if not action_scores:
        return None

    # Greedy: pick the action that covers the most needed changes
    best_action = max(action_scores, key=action_scores.get)

    # Estimate how many times we need to repeat
    total_changes = int(changed.sum())
    avg_changes_per_action = np.mean([t["n_changed"] for t in profile.action_templates.get(best_action, [{"n_changed": 1}])])
    n_actions = max(1, int(total_changes / avg_changes_per_action))

    return [best_action] * n_actions


# ─── Pretty print ────────────────────────────────────────────────

def print_profile(p: GameProfile):
    print(f"\n{'='*65}")
    print(f"  GAME PROFILE: {p.game_id}")
    print(f"  {p.solver_hint()}")
    print(f"{'='*65}")
    print(f"  Actions: {p.available_actions}  Win levels: {p.win_levels}")
    print(f"  Deterministic: {p.is_deterministic}  Markov order: {p.markov_order}")

    if p.has_cycles:
        print(f"  CYCLES DETECTED: length={p.cycle_length}")

    print(f"\n  --- Byte-Level ---")
    print(f"  Nibble vocab ({len(p.nibble_vocab)} transitions):")
    for k, v in list(p.nibble_vocab.items())[:10]:
        print(f"    {k}: {v}×")
    print(f"  Bit plane entropy: {p.bit_plane_entropy}")
    print(f"  Bit plane independence: {p.bit_plane_independence:.3f}")
    print(f"  Mean XOR compress ratio: {p.delta_compress_mean:.4f}")
    print(f"  Mean XOR RLE runs: {p.xor_rle_mean:.0f} / 4096")

    print(f"\n  --- Actions ---")
    for a in p.available_actions:
        noop = p.action_noop_rate.get(a, 0)
        n_templates = len(p.action_templates.get(a, []))
        compress = p.action_compression.get(a, 0)
        direction = p.action_directions.get(a, None)
        parts = [f"noop={noop:.0%}", f"templates={n_templates}", f"compress={compress:.4f}"]
        if direction:
            parts.append(f"dir=({direction[0]:.0f},{direction[1]:.0f})")
        print(f"  Action {a}: {', '.join(parts)}")

    print(f"\n  --- Spatial ---")
    print(f"  CoM spread: {p.com_spread:.1f}  centroid: ({p.com_centroid[0]:.0f},{p.com_centroid[1]:.0f})")
    print(f"  Templates: {p.n_unique_templates} unique")

    if p.clickable_colors:
        print(f"\n  --- Click Analysis ---")
        print(f"  Clickable colors: {p.clickable_colors}")
        if p.click_heatmap is not None:
            n_hot = int((p.click_heatmap > 0.3).sum())
            print(f"  Clickable pixels (>30% hit rate): {n_hot}")
    print()


# ─── Main ────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="ARC-AGI-3 Packet Probe")
    parser.add_argument("game_id", nargs="?", default=None,
                       help="Game ID to probe (omit for all)")
    parser.add_argument("-b", "--budget", type=int, default=30)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.all or args.game_id is None:
        arcade = arc_agi.Arcade()
        envs = arcade.get_environments()
        print(f"{'Game':<22s} {'Type':<16s} {'Det':>4s} {'Cyc':>4s} "
              f"{'Vocab':>6s} {'Tmpl':>5s} {'Cmpr':>6s} {'RLE':>5s} "
              f"{'Spread':>7s} {'Hint'}")
        print("-" * 110)
        for e in envs:
            try:
                p = probe_game(e.game_id, budget=args.budget, verbose=False)
                cyc = f"{p.cycle_length}" if p.has_cycles else "-"
                det = "Y" if p.is_deterministic else "N"
                print(f"{p.game_id:<22s} {p.game_type:<16s} {det:>4s} {cyc:>4s} "
                      f"{len(p.nibble_vocab):>6d} {p.n_unique_templates:>5d} "
                      f"{p.delta_compress_mean:>6.4f} {p.xor_rle_mean:>5.0f} "
                      f"{p.com_spread:>7.1f} {p.solver_hint()}")
            except Exception as ex:
                print(f"{e.game_id:<22s} ERROR: {str(ex)[:80]}")
    else:
        p = probe_game(args.game_id, budget=args.budget, verbose=True)
