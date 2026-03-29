"""ARC-AGI-3 Packet Analyzer — treat game frames as raw byte streams.

Each 64×64 frame = 2048 packed bytes (4-bit per cell).
A gameplay session = time series of packets.
Transitions (XOR) = the signal.

Apply the math apparatus:
  - Shannon entropy → information content per frame/transition
  - 2D FFT → spatial frequency structure (periodicity, symmetry)
  - K-Factorization → shape vs scale decomposition of transitions
  - Transition signatures → fingerprint action effects (repeatable = rule)
  - Attractor detection → states the game pulls toward (= goals)
  - Barrier estimation → transition cost / reversibility
"""
import hashlib
import json
import os
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage, signal
from scipy.spatial.distance import cdist

import arc_agi
from arcengine import GameAction, GameState


# ─── Packet primitives ───────────────────────────────────────────

def pack_4bit(grid: np.ndarray) -> bytes:
    """Pack 64×64 grid (values 0-15) into 2048 bytes."""
    flat = grid.astype(np.uint8).flatten()
    packed = (flat[0::2] << 4) | (flat[1::2] & 0x0F)
    return packed.tobytes()


def unpack_4bit(data: bytes, shape=(64, 64)) -> np.ndarray:
    """Unpack 2048 bytes back to 64×64 grid."""
    arr = np.frombuffer(data, dtype=np.uint8)
    high = (arr >> 4) & 0x0F
    low = arr & 0x0F
    return np.stack([high, low], axis=-1).flatten()[:shape[0]*shape[1]].reshape(shape)


def frame_hash(grid: np.ndarray) -> str:
    """Fast 12-char hash of a frame."""
    return hashlib.md5(grid.astype(np.uint8).tobytes()).hexdigest()[:12]


# ─── Information measures ────────────────────────────────────────

def shannon_entropy(grid: np.ndarray) -> float:
    """Shannon entropy in bits per cell."""
    vals, counts = np.unique(grid, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs + 1e-12))


def joint_entropy(grid_a: np.ndarray, grid_b: np.ndarray) -> float:
    """Joint entropy H(A,B) of two frames."""
    pairs = grid_a.flatten().astype(np.int32) * 16 + grid_b.flatten().astype(np.int32)
    vals, counts = np.unique(pairs, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs + 1e-12))


def mutual_information(grid_a: np.ndarray, grid_b: np.ndarray) -> float:
    """I(A;B) = H(A) + H(B) - H(A,B). High = frames share structure."""
    return shannon_entropy(grid_a) + shannon_entropy(grid_b) - joint_entropy(grid_a, grid_b)


def transfer_entropy(frames: list[np.ndarray], lag: int = 1) -> float:
    """Approximate transfer entropy — does the past predict the future?

    High TE = transitions are predictable (rule-based).
    Low TE = transitions are noisy or random.
    """
    if len(frames) < lag + 2:
        return 0.0

    # Use color histograms as state summaries
    states = []
    for f in frames:
        vals, counts = np.unique(f, return_counts=True)
        hist = np.zeros(16)
        hist[vals] = counts
        states.append(hist / hist.sum())

    # TE ≈ H(future|past) - H(future|past,past-lag)
    # Approximate with histogram KL divergence
    conditional_ents = []
    for i in range(lag + 1, len(states)):
        # Transition from i-1 to i
        diff = np.abs(states[i] - states[i-1]).sum()
        # Transition conditioned on i-1-lag
        diff_cond = np.abs(states[i] - states[i-1]).sum() - np.abs(states[i-1] - states[i-1-lag]).sum() * 0.5
        conditional_ents.append(max(0, diff - abs(diff_cond)))

    return np.mean(conditional_ents) if conditional_ents else 0.0


# ─── Spatial frequency analysis ──────────────────────────────────

def fft_spectrum(grid: np.ndarray) -> dict:
    """2D FFT → radial power spectrum + dominant frequencies."""
    fft = np.fft.fft2(grid.astype(np.float64))
    power = np.abs(np.fft.fftshift(fft)) ** 2

    cy, cx = grid.shape[0] // 2, grid.shape[1] // 2
    Y, X = np.mgrid[:64, :64]
    R = np.sqrt((X - cx)**2 + (Y - cy)**2).astype(int)
    max_r = min(cx, cy)

    radial = np.zeros(max_r)
    for r in range(max_r):
        mask = R == r
        if mask.any():
            radial[r] = power[mask].mean()

    # Normalize (skip DC)
    radial_norm = radial.copy()
    if radial[0] > 0:
        radial_norm = radial / radial[0]

    # Find peaks (skip DC at r=0)
    peaks = []
    for r in range(2, max_r - 1):
        if radial[r] > radial[r-1] and radial[r] > radial[r+1]:
            peaks.append((r, float(radial_norm[r])))
    peaks.sort(key=lambda p: p[1], reverse=True)

    return {
        "radial": radial,
        "radial_norm": radial_norm,
        "dc_power": float(radial[0]),
        "total_power": float(power.sum()),
        "peaks": peaks[:5],
        "dominant_freq": peaks[0][0] if peaks else 0,
        "spectral_centroid": float(np.average(np.arange(max_r), weights=radial + 1e-12)),
    }


def transition_spectrum(grid_a: np.ndarray, grid_b: np.ndarray) -> dict:
    """FFT of the XOR transition — what spatial frequencies changed?"""
    xor = (grid_a.astype(np.uint8) ^ grid_b.astype(np.uint8)).astype(np.float64)
    if xor.sum() == 0:
        return {"changed": False}
    return {**fft_spectrum(xor), "changed": True, "n_changed": int((xor > 0).sum())}


# ─── Transition packet ───────────────────────────────────────────

@dataclass
class TransitionPacket:
    """A single frame→frame transition as a data packet."""
    seq: int                    # sequence number
    action: int                 # action taken
    frame_before_hash: str
    frame_after_hash: str

    # Byte-level
    xor_bytes: bytes            # packed XOR (2048 bytes)
    xor_signature: str          # MD5 of XOR (fingerprint)
    n_changed: int              # cells that changed

    # Information
    entropy_before: float
    entropy_after: float
    entropy_delta: float        # positive = more complex
    mutual_info: float          # shared structure

    # Spatial
    bbox: tuple                 # (r_min, c_min, r_max, c_max)
    center_of_mass: tuple       # (r, c) of changes
    change_density: float       # n_changed / bbox_area

    # Spectral
    dominant_freq: int
    spectral_centroid: float

    # State
    is_noop: bool               # nothing changed
    is_reversible: bool         # same signature as a known reverse
    game_state: str
    levels_completed: int

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items() if k != 'xor_bytes'}
        d['xor_hex_head'] = self.xor_bytes[:32].hex()
        return d


# ─── Session recorder ────────────────────────────────────────────

class PacketSession:
    """Records and analyzes a full game session as a packet stream."""

    def __init__(self, game_id: str):
        self.game_id = game_id
        self.frames: list[np.ndarray] = []
        self.packets: list[TransitionPacket] = []
        self.action_signatures: dict[int, list[str]] = defaultdict(list)  # action → list of sigs
        self.state_graph: dict[str, dict[int, str]] = defaultdict(dict)   # hash → {action → hash}
        self.visit_counts: Counter = Counter()
        self.attractors: list[str] = []  # frequently revisited states
        self.barriers: list[int] = []    # transitions with high entropy delta

    def record_frame(self, grid: np.ndarray, action: Optional[int], obs):
        """Record a frame and compute transition packet if applicable."""
        grid = grid.copy()
        h = frame_hash(grid)
        self.visit_counts[h] += 1
        self.frames.append(grid)

        if action is None or len(self.frames) < 2:
            return None

        prev = self.frames[-2]
        curr = self.frames[-1]
        prev_h = frame_hash(prev)
        curr_h = h

        # XOR
        xor = prev.astype(np.uint8) ^ curr.astype(np.uint8)
        xor_packed = pack_4bit(xor)
        xor_sig = hashlib.md5(xor_packed).hexdigest()[:8]
        n_changed = int((xor > 0).sum())

        # Spatial
        is_noop = n_changed == 0
        bbox = (0, 0, 0, 0)
        com = (0.0, 0.0)
        density = 0.0
        if not is_noop:
            rows, cols = np.where(xor > 0)
            r_min, r_max = int(rows.min()), int(rows.max())
            c_min, c_max = int(cols.min()), int(cols.max())
            bbox = (r_min, c_min, r_max, c_max)
            bbox_area = (r_max - r_min + 1) * (c_max - c_min + 1)
            density = n_changed / bbox_area
            com = (float(rows.mean()), float(cols.mean()))

        # Information
        ent_before = shannon_entropy(prev)
        ent_after = shannon_entropy(curr)
        mi = mutual_information(prev, curr)

        # Spectral (on XOR)
        if not is_noop:
            spec = fft_spectrum(xor.astype(np.float64))
            dom_freq = spec["dominant_freq"]
            spec_centroid = spec["spectral_centroid"]
        else:
            dom_freq = 0
            spec_centroid = 0.0

        # Reversibility check
        reverse_map = {1: 2, 2: 1, 3: 4, 4: 3}
        is_reversible = False
        if action in reverse_map:
            rev = reverse_map[action]
            if xor_sig in self.action_signatures.get(rev, []):
                is_reversible = True

        # State graph
        self.state_graph[prev_h][action] = curr_h
        self.action_signatures[action].append(xor_sig)

        pkt = TransitionPacket(
            seq=len(self.packets),
            action=action,
            frame_before_hash=prev_h,
            frame_after_hash=curr_h,
            xor_bytes=xor_packed,
            xor_signature=xor_sig,
            n_changed=n_changed,
            entropy_before=ent_before,
            entropy_after=ent_after,
            entropy_delta=ent_after - ent_before,
            mutual_info=mi,
            bbox=bbox,
            center_of_mass=com,
            change_density=density,
            dominant_freq=dom_freq,
            spectral_centroid=spec_centroid,
            is_noop=is_noop,
            is_reversible=is_reversible,
            game_state=str(obs.state),
            levels_completed=obs.levels_completed,
        )
        self.packets.append(pkt)

        # Barrier detection: large entropy increase = crossing a barrier
        if abs(pkt.entropy_delta) > 0.05:
            self.barriers.append(pkt.seq)

        return pkt

    def analyze(self) -> dict:
        """Full session analysis."""
        if not self.packets:
            return {"error": "no packets recorded"}

        # Action fingerprints: do same actions produce same signatures?
        action_consistency = {}
        for action, sigs in self.action_signatures.items():
            unique = len(set(sigs))
            total = len(sigs)
            action_consistency[action] = {
                "unique_signatures": unique,
                "total_uses": total,
                "consistency": 1 - (unique - 1) / max(total - 1, 1),
                "signatures": list(Counter(sigs).most_common(5)),
            }

        # Attractors: states visited more than once
        attractors = [(h, c) for h, c in self.visit_counts.most_common(10) if c > 1]

        # State graph stats
        n_states = len(self.state_graph)
        n_edges = sum(len(v) for v in self.state_graph.values())

        # Transition entropy time series
        ent_deltas = [p.entropy_delta for p in self.packets]
        n_changed_series = [p.n_changed for p in self.packets]

        # Spectral fingerprint: do different actions have different frequency signatures?
        action_spectra = defaultdict(list)
        for p in self.packets:
            if not p.is_noop:
                action_spectra[p.action].append(p.dominant_freq)

        action_freq_profile = {}
        for action, freqs in action_spectra.items():
            action_freq_profile[action] = {
                "mean_freq": float(np.mean(freqs)),
                "std_freq": float(np.std(freqs)),
                "mode_freq": int(Counter(freqs).most_common(1)[0][0]) if freqs else 0,
            }

        # Reversibility ratio
        n_reversible = sum(1 for p in self.packets if p.is_reversible)

        # Noop ratio — how often does an action do nothing?
        n_noop = sum(1 for p in self.packets if p.is_noop)
        noop_by_action = defaultdict(int)
        total_by_action = defaultdict(int)
        for p in self.packets:
            total_by_action[p.action] += 1
            if p.is_noop:
                noop_by_action[p.action] += 1

        # Center of mass trajectory — where is the "action"?
        com_trajectory = [(p.center_of_mass[0], p.center_of_mass[1])
                         for p in self.packets if not p.is_noop]

        # Does CoM cluster (agent-based) or scatter (field-based)?
        if len(com_trajectory) > 2:
            coms = np.array(com_trajectory)
            com_spread = float(np.std(coms, axis=0).mean())
            com_centroid = (float(coms[:, 0].mean()), float(coms[:, 1].mean()))
        else:
            com_spread = 0.0
            com_centroid = (32.0, 32.0)

        return {
            "game_id": self.game_id,
            "total_frames": len(self.frames),
            "total_packets": len(self.packets),
            "state_graph": {
                "n_states": n_states,
                "n_edges": n_edges,
                "branching_factor": n_edges / max(n_states, 1),
            },
            "action_consistency": action_consistency,
            "action_freq_profile": action_freq_profile,
            "attractors": attractors,
            "barriers": self.barriers,
            "reversibility_ratio": n_reversible / max(len(self.packets), 1),
            "noop_ratio": n_noop / max(len(self.packets), 1),
            "noop_by_action": {a: noop_by_action[a] / max(total_by_action[a], 1)
                              for a in total_by_action},
            "entropy_series": ent_deltas,
            "change_size_series": n_changed_series,
            "com_spread": com_spread,
            "com_centroid": com_centroid,
            "game_type_estimate": self._estimate_game_type(com_spread, n_noop, action_consistency),
        }

    def _estimate_game_type(self, com_spread, n_noop, action_consistency) -> str:
        """Estimate if this is agent-based, logic-based, or orchestration."""
        # Low CoM spread + high action consistency = agent moving around
        # High CoM spread + low consistency = field/logic manipulation
        # Many noops = constrained interaction

        avg_consistency = np.mean([v["consistency"] for v in action_consistency.values()])

        if com_spread < 5.0 and avg_consistency > 0.3:
            return "AGENT (localized movement, consistent actions)"
        elif com_spread > 15.0:
            return "FIELD (distributed changes, likely logic/pattern)"
        elif n_noop / max(len(self.packets), 1) > 0.3:
            return "CONSTRAINED (many blocked actions, puzzle-like)"
        else:
            return "MIXED (orchestration or multi-object)"


# ─── K-Factorization for transitions ─────────────────────────────

def k_factor_transition(grid_a: np.ndarray, grid_b: np.ndarray) -> dict:
    """Apply K-Factorization (§136) to a frame transition.

    Q = Q_shape(O,R,α) · Q_scale(K)

    Shape: what structural pattern changed (objects, topology, symmetry)
    Scale: how much changed (magnitude, extent, intensity)

    Separating these tells us whether two transitions are the "same rule
    applied at different scales" vs "different rules".
    """
    xor = (grid_a.astype(np.uint8) ^ grid_b.astype(np.uint8))

    if xor.sum() == 0:
        return {"shape": "identity", "scale": 0, "k_class": "noop"}

    # === SHAPE COMPONENT ===

    # 1. Topology of changed region
    binary = (xor > 0).astype(np.int32)
    labeled, n_components = ndimage.label(binary)

    # 2. Component analysis
    components = []
    for i in range(1, n_components + 1):
        mask = labeled == i
        rows, cols = np.where(mask)
        size = int(mask.sum())
        bbox_h = rows.max() - rows.min() + 1
        bbox_w = cols.max() - cols.min() + 1
        compactness = size / (bbox_h * bbox_w) if bbox_h * bbox_w > 0 else 0
        components.append({
            "size": size,
            "bbox": (int(rows.min()), int(cols.min()), int(rows.max()), int(cols.max())),
            "compactness": round(compactness, 3),
            "aspect": round(bbox_w / max(bbox_h, 1), 2),
        })
    components.sort(key=lambda c: c["size"], reverse=True)

    # 3. Symmetry of changed region
    sym_h = np.allclose(binary, binary[::-1, :])
    sym_v = np.allclose(binary, binary[:, ::-1])
    sym_d = np.allclose(binary, binary.T) if binary.shape[0] == binary.shape[1] else False

    # 4. Color transition pattern
    changed_mask = xor > 0
    old_vals = grid_a[changed_mask]
    new_vals = grid_b[changed_mask]
    color_transitions = Counter(zip(old_vals.tolist(), new_vals.tolist()))

    # Is it a pure swap? (A→B and B→A in equal amounts)
    is_swap = False
    for (a, b), count in color_transitions.items():
        if (b, a) in color_transitions and color_transitions[(b, a)] == count:
            is_swap = True
            break

    # Shape classification
    if n_components == 1 and components[0]["compactness"] > 0.7:
        shape_class = "compact_single"  # one tight cluster moved
    elif n_components == 2 and is_swap:
        shape_class = "swap"  # two regions swapped
    elif n_components == 1 and components[0]["compactness"] < 0.3:
        shape_class = "diffuse_single"  # scattered change
    elif n_components >= 3:
        shape_class = "multi_component"  # many things changed
    else:
        shape_class = f"components_{n_components}"

    # === SCALE COMPONENT ===

    total_cells = grid_a.size
    n_changed = int(changed_mask.sum())
    scale_ratio = n_changed / total_cells

    # Intensity: how much did values change?
    intensity = float(np.abs(grid_b.astype(float) - grid_a.astype(float))[changed_mask].mean())

    return {
        "shape": shape_class,
        "scale": round(scale_ratio, 6),
        "intensity": round(intensity, 2),
        "n_components": n_components,
        "components": components[:5],
        "symmetry": {"horizontal": sym_h, "vertical": sym_v, "diagonal": sym_d},
        "color_transitions": {f"{a}→{b}": c for (a, b), c in color_transitions.most_common(10)},
        "is_swap": is_swap,
        "k_class": f"{shape_class}@{scale_ratio:.4f}",
    }


# ─── Barrier detection (§136D2) ──────────────────────────────────

def estimate_barrier(session: PacketSession) -> dict:
    """Estimate game barriers from the packet stream.

    Barrier = d × π/√2 in the framework.
    Here d = effective dimensionality of the transition space.

    A barrier appears as:
    - Entropy spike in the transition series
    - Change in action effectiveness (consistency drops)
    - State graph branching point
    - Level transition
    """
    if len(session.packets) < 3:
        return {"barriers": []}

    # 1. Entropy derivative (second-order = acceleration)
    ent = [p.entropy_delta for p in session.packets]
    ent_accel = np.diff(ent, n=2) if len(ent) > 2 else np.array([])

    # 2. Change magnitude spikes
    changes = np.array([p.n_changed for p in session.packets], dtype=float)
    if len(changes) > 1:
        change_z = (changes - changes.mean()) / (changes.std() + 1e-12)
    else:
        change_z = np.zeros_like(changes)

    # 3. Detect barrier crossings
    barriers = []
    for i in range(1, len(session.packets) - 1):
        score = 0.0
        reasons = []

        # Entropy spike
        if i < len(ent_accel) and abs(ent_accel[i-1]) > 0.02:
            score += abs(ent_accel[i-1])
            reasons.append(f"entropy_accel={ent_accel[i-1]:.4f}")

        # Change magnitude spike
        if abs(change_z[i]) > 1.5:
            score += abs(change_z[i]) * 0.1
            reasons.append(f"change_z={change_z[i]:.2f}")

        # Noop→effect or effect→noop transition
        if session.packets[i].is_noop != session.packets[i-1].is_noop:
            score += 0.3
            reasons.append("noop_transition")

        # New state never seen before with high change count
        if session.visit_counts[session.packets[i].frame_after_hash] == 1 and changes[i] > changes.mean():
            score += 0.2
            reasons.append("new_state")

        if score > 0.3:
            barriers.append({
                "seq": i,
                "action": session.packets[i].action,
                "score": round(score, 3),
                "reasons": reasons,
            })

    barriers.sort(key=lambda b: b["score"], reverse=True)

    # Effective dimensionality from unique transition signatures
    unique_sigs = len(set(p.xor_signature for p in session.packets if not p.is_noop))
    d_eff = max(1, unique_sigs)
    theoretical_barrier = d_eff * np.pi / np.sqrt(2)

    return {
        "barriers": barriers[:10],
        "d_eff": d_eff,
        "theoretical_barrier": round(theoretical_barrier, 3),
        "unique_transitions": unique_sigs,
    }


# ─── Run a capture session ───────────────────────────────────────

def capture_game(game_id: str, n_actions: int = 50, strategy: str = "explore") -> PacketSession:
    """Play a game and capture the packet stream."""
    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    session = PacketSession(game_id)
    grid = np.array(obs.frame[0])
    session.record_frame(grid, None, obs)

    available = list(obs.available_actions)
    print(f"[{game_id}] Available actions: {available}")
    print(f"[{game_id}] Win levels: {obs.win_levels}")

    has_click = 6 in available
    has_keys = any(a in available for a in [1, 2, 3, 4])

    if strategy == "explore":
        # Systematic: try each action multiple times, then mix
        action_seq = []
        non_click = [a for a in available if a != 6]
        # Phase 1: test each non-click action individually
        for a in non_click:
            action_seq.extend([a, a, a])
        # Phase 2: pairs and triples
        for a in non_click:
            for b in non_click:
                if a != b:
                    action_seq.extend([a, b])
        # Phase 3: fill remaining budget with cycling
        while len(action_seq) < n_actions:
            action_seq.extend(non_click if non_click else [6])
        action_seq = action_seq[:n_actions]
    elif strategy == "random":
        rng = np.random.default_rng(42)
        non_click = [a for a in available if a != 6]
        action_seq = rng.choice(non_click if non_click else [6], size=n_actions).tolist()
    else:
        action_seq = [int(x) for x in strategy.split(",")]

    rng = np.random.default_rng(42)

    for i, action in enumerate(action_seq):
        if obs.state in (GameState.WIN, GameState.GAME_OVER):
            print(f"[{game_id}] Game ended at step {i}: {obs.state}")
            break

        if action == 6:
            # Click: target non-background pixels
            g = np.array(obs.frame[0])
            bg = int(np.bincount(g.flatten()).argmax())
            nonbg = np.where(g != bg)
            if len(nonbg[0]) > 0:
                idx = rng.integers(len(nonbg[0]))
                obs = env.step(6, data={"x": int(nonbg[1][idx]), "y": int(nonbg[0][idx])})
            else:
                obs = env.step(6, data={"x": 32, "y": 32})
        else:
            obs = env.step(action)
        grid = np.array(obs.frame[0])
        pkt = session.record_frame(grid, action, obs)

        if pkt and obs.levels_completed > 0 and i > 0:
            prev_level = session.packets[-2].levels_completed if len(session.packets) > 1 else 0
            if obs.levels_completed > prev_level:
                print(f"[{game_id}] LEVEL UP at step {i}! ({prev_level} → {obs.levels_completed})")

    return session


# ─── Pretty print ────────────────────────────────────────────────

def print_analysis(analysis: dict):
    """Pretty-print a session analysis."""
    print(f"\n{'='*60}")
    print(f"  PACKET ANALYSIS: {analysis['game_id']}")
    print(f"{'='*60}")
    print(f"  Frames: {analysis['total_frames']}  Packets: {analysis['total_packets']}")
    print(f"  Game type: {analysis['game_type_estimate']}")
    print(f"  State graph: {analysis['state_graph']['n_states']} states, "
          f"{analysis['state_graph']['n_edges']} edges, "
          f"branching={analysis['state_graph']['branching_factor']:.2f}")
    print(f"  Reversibility: {analysis['reversibility_ratio']:.1%}")
    print(f"  Noop ratio: {analysis['noop_ratio']:.1%}")
    print(f"  CoM spread: {analysis['com_spread']:.1f} (centroid: {analysis['com_centroid'][0]:.0f},{analysis['com_centroid'][1]:.0f})")

    print(f"\n  --- Action Consistency ---")
    for action, info in sorted(analysis['action_consistency'].items()):
        print(f"  Action {action}: {info['unique_signatures']}/{info['total_uses']} unique sigs "
              f"(consistency={info['consistency']:.2f})  "
              f"top: {info['signatures'][:3]}")

    if analysis['action_freq_profile']:
        print(f"\n  --- Action Frequency Profiles ---")
        for action, info in sorted(analysis['action_freq_profile'].items()):
            print(f"  Action {action}: mean_freq={info['mean_freq']:.1f} "
                  f"std={info['std_freq']:.1f} mode={info['mode_freq']}")

    if analysis['attractors']:
        print(f"\n  --- Attractors (revisited states) ---")
        for h, count in analysis['attractors'][:5]:
            print(f"  State {h}: visited {count}×")

    if analysis['noop_by_action']:
        print(f"\n  --- Noop Rate by Action ---")
        for action, rate in sorted(analysis['noop_by_action'].items()):
            print(f"  Action {action}: {rate:.1%} noop")

    print()


def print_barriers(barrier_info: dict):
    """Print barrier analysis."""
    print(f"  --- Barrier Analysis ---")
    print(f"  d_eff = {barrier_info['d_eff']} unique transition types")
    print(f"  Theoretical barrier = d×π/√2 = {barrier_info['theoretical_barrier']}")

    if barrier_info['barriers']:
        print(f"  Detected {len(barrier_info['barriers'])} barrier crossings:")
        for b in barrier_info['barriers'][:5]:
            print(f"    seq={b['seq']} action={b['action']} "
                  f"score={b['score']} [{', '.join(b['reasons'])}]")
    print()


def print_k_factors(session: PacketSession, n: int = 10):
    """Print K-Factorization analysis of transitions."""
    print(f"  --- K-Factorization (first {n} transitions) ---")
    for pkt in session.packets[:n]:
        if pkt.is_noop:
            print(f"  [{pkt.seq}] action={pkt.action} → NOOP")
            continue

        kf = k_factor_transition(
            session.frames[pkt.seq],
            session.frames[pkt.seq + 1]
        )
        print(f"  [{pkt.seq}] action={pkt.action} → "
              f"shape={kf['shape']} scale={kf['scale']:.4f} "
              f"intensity={kf['intensity']} "
              f"components={kf['n_components']} "
              f"swap={kf['is_swap']} "
              f"colors={list(kf['color_transitions'].keys())[:3]}")
    print()


# ─── Main ────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ARC-AGI-3 Packet Analyzer")
    parser.add_argument("game_id", nargs="?", default="tr87-cd924810",
                       help="Game ID to analyze")
    parser.add_argument("-n", "--actions", type=int, default=60,
                       help="Number of actions to take")
    parser.add_argument("-s", "--strategy", default="explore",
                       help="Strategy: explore, random, or comma-separated actions")
    parser.add_argument("--all", action="store_true",
                       help="Run on all 25 environments")
    parser.add_argument("--save", type=str, default=None,
                       help="Save analysis to JSON file")
    args = parser.parse_args()

    if args.all:
        arcade = arc_agi.Arcade()
        envs = arcade.get_environments()
        results = {}
        for env_info in envs:
            gid = env_info.game_id
            try:
                session = capture_game(gid, n_actions=args.actions)
                analysis = session.analyze()
                barrier_info = estimate_barrier(session)
                analysis["barriers_detail"] = barrier_info
                print_analysis(analysis)
                print_barriers(barrier_info)
                results[gid] = analysis
            except Exception as e:
                print(f"[{gid}] ERROR: {e}")
                results[gid] = {"error": str(e)}

        if args.save:
            # Clean for JSON serialization
            for gid, r in results.items():
                if "entropy_series" in r:
                    r["entropy_series"] = [round(x, 6) for x in r["entropy_series"]]
                    r["change_size_series"] = [int(x) for x in r["change_size_series"]]
            with open(args.save, "w") as f:
                json.dump(results, f, indent=2, default=str)
            print(f"Saved to {args.save}")
    else:
        session = capture_game(args.game_id, n_actions=args.actions, strategy=args.strategy)
        analysis = session.analyze()
        barrier_info = estimate_barrier(session)

        print_analysis(analysis)
        print_barriers(barrier_info)
        print_k_factors(session)

        if args.save:
            analysis["barriers_detail"] = barrier_info
            analysis["entropy_series"] = [round(x, 6) for x in analysis["entropy_series"]]
            analysis["change_size_series"] = [int(x) for x in analysis["change_size_series"]]
            with open(args.save, "w") as f:
                json.dump(analysis, f, indent=2, default=str)
            print(f"Saved to {args.save}")
