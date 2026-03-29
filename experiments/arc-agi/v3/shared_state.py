"""SharedState + Persistent Learning for the Maestro Conductor.

Three components:
  1. SharedState — in-memory knowledge pool shared across all solvers
  2. GameLedger — persistent JSON per game (cross-session learning)
  3. CrossGameLedger — global JSON (transfer learning across games)

Design principles:
  - SharedState objects are passed BY REFERENCE to solvers (not copied)
  - Tier 1 objects (manifold, table, detector) are append-only accumulators
  - Tier 2 objects (transitions, macros, grammar) use indexed lists that only grow
  - Ledger stores hashes+templates, NOT full 64×64 grids (50-200KB per game)
  - Zero regression: when shared_state=None, solvers behave identically to before
"""

import base64
import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

# Lazy imports to avoid circular dependencies — resolved at first use
_imports_resolved = False
_TransitionMemory = None
_MacroLibrary = None
_SpectralNavigator = None
_KGrammar = None
_XORVectorSpace = None
_EckertWinDetector = None
_CellManifold = None
_MechanismTable = None


def _resolve_imports():
    global _imports_resolved
    global _TransitionMemory, _MacroLibrary, _SpectralNavigator
    global _KGrammar, _XORVectorSpace
    global _EckertWinDetector, _CellManifold, _MechanismTable

    if _imports_resolved:
        return

    from instanton_planner import TransitionMemory, MacroLibrary, SpectralNavigator
    from recursive_solver import KGrammar, XORVectorSpace
    from eckert_win_detector import EckertWinDetector
    from eckert_simulator import CellManifold, MechanismTable

    _TransitionMemory = TransitionMemory
    _MacroLibrary = MacroLibrary
    _SpectralNavigator = SpectralNavigator
    _KGrammar = KGrammar
    _XORVectorSpace = XORVectorSpace
    _EckertWinDetector = EckertWinDetector
    _CellManifold = CellManifold
    _MechanismTable = MechanismTable
    _imports_resolved = True


LEDGER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ledger')


# ═══════════════════════════════════════════════════════════════════
#  1. SHARED STATE — in-memory knowledge pool
# ═══════════════════════════════════════════════════════════════════

class SharedState:
    """All knowledge accumulated across solvers for one game.

    Passed by reference to solvers via shared_state= parameter.
    Solvers read from and write to these objects directly.
    After each solver run, Maestro calls absorb_from_solver() to
    harvest any state the solver created in its own objects.
    """

    def __init__(self):
        _resolve_imports()

        # Tier 1: Universal (safe to share immediately)
        self.detector = _EckertWinDetector()       # φ oracle
        self.manifold = _CellManifold()            # (O,R,α) field
        self.table = _MechanismTable()             # Learned rules

        # Tier 2: Strategy-specific (accumulate across solvers)
        self.transitions = _TransitionMemory()     # State-action graph
        self.macros = _MacroLibrary()              # Proven sequences
        self.navigator = _SpectralNavigator()      # Eigenvector navigation
        self.grammar = _KGrammar()                 # K-Factorized atoms
        self.xor_space = _XORVectorSpace()         # GF(2) basis

        # Tier 3: Tracking (Maestro reads, solvers write via harvest)
        self.fisher_map = np.zeros((64, 64), dtype=np.float32)
        self.walls = np.zeros((64, 64), dtype=bool)
        self.phi_trajectories: dict[str, list[float]] = {}
        self.holonomy_paths: dict[str, list[tuple]] = {}
        self.budget_spent: dict[str, int] = {}
        self.states_visited: set[str] = set()
        self.atoms_discovered: set[str] = set()

        # Attempt history
        self.attempts: list[dict] = []
        self.best_phi_ever: float = 0.0
        self.best_entropy_ever: float = float('inf')
        self.total_sessions: int = 0

    def absorb_from_solver(self, solver_name: str, solver_obj):
        """Extract learned state from any solver into the shared pool.

        Handles all 5 solver types by duck-typing their attributes.
        """
        # ─── Instanton Planner / AAA Solver ───
        if hasattr(solver_obj, 'memory') and hasattr(solver_obj.memory, 'transitions'):
            mem = solver_obj.memory
            # Merge transitions that we don't already have
            existing_hashes = {
                (t.prev_hash, t.action) for t in self.transitions.transitions
            }
            for t in mem.transitions:
                if (t.prev_hash, t.action) not in existing_hashes:
                    self.transitions.record(t)
                    existing_hashes.add((t.prev_hash, t.action))

        # Macros
        if hasattr(solver_obj, 'macros') and hasattr(solver_obj.macros, 'macros'):
            existing_xors = {m[1] for m in self.macros.macros} if self.macros.macros else set()
            for macro in solver_obj.macros.macros:
                if macro[1] not in existing_xors:
                    self.macros.macros.append(macro)
                    if len(macro) > 1:
                        self.macros.macro_index[macro[1]] = len(self.macros.macros) - 1

        # Navigator transitions
        if hasattr(solver_obj, 'navigator') and hasattr(solver_obj.navigator, '_transitions'):
            for t in getattr(solver_obj.navigator, '_transitions', []):
                self.navigator.record_transition(*t) if hasattr(self.navigator, 'record_transition') else None

        # ─── Eckert Simulator ───
        if hasattr(solver_obj, 'manifold') and solver_obj.manifold is not self.manifold:
            mf = solver_obj.manifold
            if mf.n_observations > 0:
                # Merge color counts (additive)
                self.manifold._color_counts += mf._color_counts
                self.manifold._action_change += mf._action_change
                self.manifold._action_total += mf._action_total
                self.manifold._neighbor_corr += mf._neighbor_corr
                self.manifold._neighbor_count += mf._neighbor_count
                self.manifold.n_observations += mf.n_observations

        if hasattr(solver_obj, 'table') and solver_obj.table is not self.table:
            tbl = solver_obj.table
            existing_rules = {r.effect_hash for r in self.table.rules} if hasattr(self.table, 'rules') else set()
            for rule in getattr(tbl, 'rules', []):
                if hasattr(rule, 'effect_hash') and rule.effect_hash not in existing_rules:
                    self.table.rules.append(rule)
                    existing_rules.add(rule.effect_hash)

        # ─── Recursive Solver ───
        if hasattr(solver_obj, 'grammar') and solver_obj.grammar is not self.grammar:
            gram = solver_obj.grammar
            existing_atoms = {a.shape_hash for a in self.grammar.atoms} if hasattr(self.grammar, 'atoms') else set()
            for atom in getattr(gram, 'atoms', []):
                if atom.shape_hash not in existing_atoms:
                    self.grammar.atoms.append(atom)
                    self.grammar.atom_index[atom.shape_hash] = len(self.grammar.atoms) - 1
                    existing_atoms.add(atom.shape_hash)
                    self.atoms_discovered.add(atom.shape_hash)

        if hasattr(solver_obj, 'xor_space') and solver_obj.xor_space is not self.xor_space:
            xs = solver_obj.xor_space
            for vec in getattr(xs, 'vectors', []):
                self.xor_space.add_vector(*vec) if hasattr(self.xor_space, 'add_vector') else None

        # ─── Detector (φ history) ───
        detector = getattr(solver_obj, '_detector', None) or getattr(solver_obj, 'detector', None)
        if detector and detector is not self.detector:
            phi_traj = [s.phi for s in getattr(detector, 'snapshots', [])]
            if phi_traj:
                self.phi_trajectories[solver_name] = phi_traj
                best_phi = max(phi_traj) if phi_traj else 0.0
                if best_phi > self.best_phi_ever:
                    self.best_phi_ever = best_phi

        # ─── Fisher map (max accumulation) ───
        if hasattr(solver_obj, 'fisher_map') and solver_obj.fisher_map is not None:
            fm = solver_obj.fisher_map
            if isinstance(fm, np.ndarray) and fm.shape == (64, 64):
                self.fisher_map = np.maximum(self.fisher_map, fm)

        # ─── Budget tracking ───
        actions = getattr(solver_obj, 'total_actions', 0)
        self.budget_spent[solver_name] = self.budget_spent.get(solver_name, 0) + actions

        # ─── State hashes visited ───
        if hasattr(solver_obj, 'frames'):
            from packet_probe import frame_hash
            for f in solver_obj.frames:
                self.states_visited.add(frame_hash(f))

    def seed_into_solver(self, solver_obj):
        """Inject shared knowledge into a solver before it runs.

        Key insight: we pass objects BY REFERENCE where the solver
        would have created its own. The solver's writes go directly
        into our shared pool.
        """
        # Instanton / AAA: share transition memory, macros, navigator
        if hasattr(solver_obj, 'memory'):
            solver_obj.memory = self.transitions
            if hasattr(solver_obj, 'telescope'):
                from instanton_planner import XORTelescope
                solver_obj.telescope = XORTelescope(self.transitions)
            if hasattr(solver_obj, 'compiler'):
                from instanton_planner import InstantonCompiler
                solver_obj.compiler = InstantonCompiler(self.transitions)
        if hasattr(solver_obj, 'navigator'):
            solver_obj.navigator = self.navigator
        if hasattr(solver_obj, 'macros') and hasattr(solver_obj.macros, 'macros'):
            solver_obj.macros = self.macros

        # Eckert: share manifold, table, detector
        if hasattr(solver_obj, 'manifold'):
            solver_obj.manifold = self.manifold
        if hasattr(solver_obj, 'table'):
            solver_obj.table = self.table
        if hasattr(solver_obj, 'model'):
            from eckert_simulator import ForwardModel
            solver_obj.model = ForwardModel(self.table, self.manifold)

        # Detector (φ oracle)
        if hasattr(solver_obj, '_detector'):
            solver_obj._detector = self.detector
        elif hasattr(solver_obj, 'detector'):
            solver_obj.detector = self.detector

        # Recursive: share grammar, xor_space
        if hasattr(solver_obj, 'grammar'):
            solver_obj.grammar = self.grammar
        if hasattr(solver_obj, 'xor_space'):
            solver_obj.xor_space = self.xor_space

    def summary(self) -> dict:
        """Current state summary for display."""
        return {
            'transitions': len(self.transitions.transitions),
            'macros': len(self.macros.macros) if self.macros.macros else 0,
            'atoms': len(self.grammar.atoms) if hasattr(self.grammar, 'atoms') else 0,
            'states_visited': len(self.states_visited),
            'manifold_obs': self.manifold.n_observations,
            'best_phi': self.best_phi_ever,
            'best_entropy': self.best_entropy_ever,
            'budget_total': sum(self.budget_spent.values()),
            'solvers_run': list(self.budget_spent.keys()),
        }


# ═══════════════════════════════════════════════════════════════════
#  2. GAME LEDGER — persistent JSON per game
# ═══════════════════════════════════════════════════════════════════

def _encode_array(arr: np.ndarray) -> str:
    """Base64-encode a numpy array for JSON storage."""
    return base64.b64encode(arr.tobytes()).decode('ascii')


def _decode_array(s: str, dtype, shape) -> np.ndarray:
    """Decode a base64-encoded numpy array."""
    return np.frombuffer(base64.b64decode(s), dtype=dtype).reshape(shape)


class GameLedger:
    """Persistent learning for one game across sessions.

    Stores transition templates (not full grids), mechanism atoms,
    macros, Fisher maps, φ trajectories, and strategy fitness.
    Typical size: 50-200KB per game.
    """

    MAX_TRANSITIONS = 5000  # Cap to prevent unbounded growth

    def __init__(self):
        os.makedirs(LEDGER_DIR, exist_ok=True)

    def _path(self, game_id: str) -> str:
        return os.path.join(LEDGER_DIR, f'{game_id}.json')

    def save(self, game_id: str, shared: SharedState,
             attempt_results: dict, profile_hint: str = ''):
        """Persist shared state to disk."""
        data = {
            'game_id': game_id,
            'version': 1,
            'updated': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'profile_hint': profile_hint,

            # Transitions: store graph + template hashes (not full grids)
            'transitions': self._serialize_transitions(shared.transitions),

            # Mechanism atoms
            'atoms': self._serialize_atoms(shared.grammar),

            # Macros
            'macros': self._serialize_macros(shared.macros),

            # Fisher and wall maps (base64)
            'fisher_map': _encode_array(shared.fisher_map),
            'wall_map': _encode_array(shared.walls.astype(np.uint8)),

            # φ trajectories and attempt history
            'phi_trajectories': {
                k: [round(v, 4) for v in vals]
                for k, vals in shared.phi_trajectories.items()
            },
            'attempts': shared.attempts,

            # Best scores
            'best_phi_ever': round(shared.best_phi_ever, 4),
            'best_entropy_ever': round(shared.best_entropy_ever, 4),
            'total_sessions': shared.total_sessions,
            'states_visited_count': len(shared.states_visited),
            'budget_spent': shared.budget_spent,
        }

        path = self._path(game_id)

        def _default(obj):
            if isinstance(obj, (np.integer,)):
                return int(obj)
            if isinstance(obj, (np.floating,)):
                return float(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return str(obj)

        with open(path, 'w') as f:
            json.dump(data, f, indent=1, default=_default)

    def load(self, game_id: str) -> Optional[SharedState]:
        """Reconstitute SharedState from ledger.

        Transitions are hash+template only — grids refilled during play.
        """
        path = self._path(game_id)
        if not os.path.exists(path):
            return None

        try:
            with open(path) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            return None

        _resolve_imports()
        shared = SharedState()

        # Restore state graph (for SpectralNavigator and lookup)
        transitions_data = data.get('transitions', {})
        state_graph = transitions_data.get('state_graph', {})
        for prev_hash, actions in state_graph.items():
            for action_str, curr_hash in actions.items():
                shared.transitions.state_graph[prev_hash][int(action_str)] = curr_hash
                # Navigator gets the graph topology
                if hasattr(shared.navigator, 'record_transition'):
                    shared.navigator.record_transition(prev_hash, int(action_str), curr_hash)

        # Restore atoms
        for atom_data in data.get('atoms', []):
            if hasattr(shared.grammar, 'atoms'):
                # Create a lightweight atom stub
                atom = type('AtomStub', (), {
                    'shape_hash': atom_data['hash'],
                    'count': atom_data.get('count', 1),
                })()
                if atom.shape_hash not in getattr(shared.grammar, 'atom_index', {}):
                    shared.grammar.atoms.append(atom)
                    shared.grammar.atom_index[atom.shape_hash] = len(shared.grammar.atoms) - 1
                    shared.atoms_discovered.add(atom.shape_hash)

        # Restore macros
        for macro_data in data.get('macros', []):
            actions = macro_data.get('actions', [])
            xor_hash = macro_data.get('xor_hash', '')
            entropy_delta = macro_data.get('entropy_delta', 0.0)
            shared.macros.macros.append((actions, xor_hash, entropy_delta))
            shared.macros.macro_index[xor_hash] = len(shared.macros.macros) - 1

        # Restore Fisher and wall maps
        if 'fisher_map' in data:
            shared.fisher_map = _decode_array(data['fisher_map'], np.float32, (64, 64))
        if 'wall_map' in data:
            shared.walls = _decode_array(data['wall_map'], np.uint8, (64, 64)).astype(bool)

        # Restore tracking
        shared.phi_trajectories = data.get('phi_trajectories', {})
        shared.attempts = data.get('attempts', [])
        shared.best_phi_ever = data.get('best_phi_ever', 0.0)
        shared.best_entropy_ever = data.get('best_entropy_ever', float('inf'))
        shared.total_sessions = data.get('total_sessions', 0) + 1
        shared.budget_spent = data.get('budget_spent', {})

        return shared

    def _serialize_transitions(self, memory) -> dict:
        """Serialize transition memory: graph + template hashes only."""
        templates = {}
        for t in memory.transitions[:self.MAX_TRANSITIONS]:
            templates[t.template_hash] = {
                'action': t.action,
                'origin': list(t.origin) if t.origin else [0, 0],
                'colors': {str(k): v for k, v in t.color_map.items()},
                'n_changed': t.n_changed,
                'entropy_delta': round(t.entropy_delta, 4),
            }

        # State graph (compact)
        graph = {}
        for prev_hash, action_map in memory.state_graph.items():
            graph[prev_hash] = {str(a): ch for a, ch in action_map.items()}

        return {
            'count': len(memory.transitions),
            'templates': templates,
            'state_graph': graph,
        }

    def _serialize_atoms(self, grammar) -> list:
        """Serialize K-grammar atoms."""
        atoms = []
        for atom in getattr(grammar, 'atoms', []):
            atoms.append({
                'hash': atom.shape_hash,
                'count': getattr(atom, 'count', 1),
                'actions': list(getattr(atom, 'action_affinity', {}).keys())
                           if hasattr(atom, 'action_affinity') else [],
            })
        return atoms

    def _serialize_macros(self, macros) -> list:
        """Serialize macro library."""
        result = []
        for macro in getattr(macros, 'macros', []):
            if isinstance(macro, (list, tuple)) and len(macro) >= 2:
                result.append({
                    'actions': list(macro[0]) if isinstance(macro[0], (list, tuple)) else [],
                    'xor_hash': str(macro[1]),
                    'entropy_delta': float(macro[2]) if len(macro) > 2 else 0.0,
                })
        return result


# ═══════════════════════════════════════════════════════════════════
#  3. CROSS-GAME LEDGER — transfer learning
# ═══════════════════════════════════════════════════════════════════

class CrossGameLedger:
    """Transfer learning across all games.

    Tracks which strategies work for which game types, which mechanism
    atoms appear across multiple games (universal), and similarity
    between games for strategy recommendation.
    """

    def __init__(self):
        os.makedirs(LEDGER_DIR, exist_ok=True)
        self._path = os.path.join(LEDGER_DIR, '_global.json')
        self._data = self._load()

    def _load(self) -> dict:
        if os.path.exists(self._path):
            try:
                with open(self._path) as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {
            'version': 1,
            'fingerprints': {},          # game_id → [8 floats]
            'strategy_fitness': {},      # game_type → {strategy → fitness}
            'solved_games': {},          # game_id → {strategy, phi, levels}
            'atom_frequency': {},        # atom_hash → [game_ids]
            'barrier_estimates': {},     # game_type → mean_barrier
            'attempt_count': {},         # game_id → total attempts
        }

    def _save(self):
        with open(self._path, 'w') as f:
            json.dump(self._data, f, indent=1)

    def update(self, game_id: str, profile, fingerprint: np.ndarray,
               results: dict, shared: SharedState):
        """Update global ledger after a game session."""
        # Fingerprint
        self._data['fingerprints'][game_id] = [round(float(x), 4) for x in fingerprint]

        # Strategy fitness per game type
        game_type = profile.game_type if hasattr(profile, 'game_type') else 'UNKNOWN'
        if game_type not in self._data['strategy_fitness']:
            self._data['strategy_fitness'][game_type] = {}

        for key, result in results.items():
            solver_name = key.split('_a')[0]
            levels = result.get('levels_solved', 0)
            phi = result.get('final_phi', 0.0)
            fitness = levels * 10.0 + phi  # Reward levels heavily
            current = self._data['strategy_fitness'][game_type].get(solver_name, 1.0)
            # Exponential moving average
            self._data['strategy_fitness'][game_type][solver_name] = (
                0.7 * current + 0.3 * fitness
            )

        # Solved games
        best_result = max(results.values(), key=lambda r: r.get('levels_solved', 0), default={})
        if best_result.get('levels_solved', 0) > 0:
            self._data['solved_games'][game_id] = {
                'strategy': best_result.get('solver_name', ''),
                'levels_solved': best_result.get('levels_solved', 0),
                'win_levels': best_result.get('win_levels', 0),
                'best_phi': round(shared.best_phi_ever, 4),
            }

        # Atom frequency (which atoms appear in which games)
        for atom_hash in shared.atoms_discovered:
            if atom_hash not in self._data['atom_frequency']:
                self._data['atom_frequency'][atom_hash] = []
            if game_id not in self._data['atom_frequency'][atom_hash]:
                self._data['atom_frequency'][atom_hash].append(game_id)

        # Barrier estimates
        from spectral_engine import estimate_mechanisms, coordination_barrier
        n_mechs = estimate_mechanisms(profile)
        barrier = coordination_barrier(n_mechs)
        if game_type not in self._data['barrier_estimates']:
            self._data['barrier_estimates'][game_type] = barrier
        else:
            self._data['barrier_estimates'][game_type] = (
                0.8 * self._data['barrier_estimates'][game_type] + 0.2 * barrier
            )

        # Attempt count
        self._data['attempt_count'][game_id] = (
            self._data['attempt_count'].get(game_id, 0) + len(shared.attempts)
        )

        self._save()

    def recommend_strategy(self, profile, fingerprint: np.ndarray) -> Optional[list]:
        """Find most similar solved game → recommend its strategy.

        Returns solver priority list, or None if no recommendations.
        """
        from eckert_math import game_similarity

        game_type = profile.game_type if hasattr(profile, 'game_type') else 'UNKNOWN'

        # Strategy 1: game-type fitness (if we have data)
        type_fitness = self._data['strategy_fitness'].get(game_type, {})

        # Strategy 2: similar solved game
        best_sim, best_strategy = -1.0, None
        fp = np.array(fingerprint)
        for solved_id, info in self._data['solved_games'].items():
            if solved_id in self._data['fingerprints']:
                stored_fp = np.array(self._data['fingerprints'][solved_id])
                sim = game_similarity(fp, stored_fp)
                if sim > best_sim:
                    best_sim = sim
                    best_strategy = info.get('strategy', '')

        # Combine: type fitness ranking + similar-game boost
        if not type_fitness and not best_strategy:
            return None

        all_solvers = ['eckert', 'instanton', 'aaa', 'recursive', 'packet']
        scores = {s: type_fitness.get(s, 1.0) for s in all_solvers}
        if best_strategy and best_sim > 0.7:
            scores[best_strategy] = scores.get(best_strategy, 1.0) + 10.0 * best_sim

        return sorted(all_solvers, key=lambda s: scores.get(s, 0), reverse=True)

    def transferable_atoms(self, game_id: str) -> list:
        """Atoms seen in 3+ games → likely universal, seed into new game."""
        universal = []
        for atom_hash, game_ids in self._data['atom_frequency'].items():
            if len(game_ids) >= 3 and game_id not in game_ids:
                universal.append(atom_hash)
        return universal

    def get_barrier_estimate(self, game_type: str) -> Optional[float]:
        """Refined barrier estimate from past experience."""
        return self._data['barrier_estimates'].get(game_type)
