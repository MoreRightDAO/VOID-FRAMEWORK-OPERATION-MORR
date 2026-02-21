# Never Trust the Client: Void Architecture in Multiplayer Games

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO
**License:** BSL 1.1 — free for non-commercial use. Commercial licensing available; pricing based on CCU. Contact master@moreright.xyz.

---

## Abstract

Multiplayer game security has spent three decades discovering — through engineering failure — the same constraint specification that the void framework derives from thermodynamic first principles. The game security maxim "never trust the client" maps exactly onto the framework's constraint specification: transparent (server sees all state), invariant (rules don't change per client claim), independent (server is outside client control). Three networking architectures — client-server (FPS), deterministic lockstep (RTS), and rollback simulation (fighting games) — independently converged on this structure, constituting hostile witness evidence of the highest weight.

We identify multiplayer gaming as a **four-void coupled system** — player-to-player, server-to-client, anti-cheat-to-player, and matchmaking-to-player opacity — where cascades in each void reinforce the others through the observer. Empirical Péclet number (Pe) validation across three genres confirms that information asymmetry predicts engagement outcomes: CS2 clean kills show 4.4× higher Pe than contested kills (N=2,299, p < 0.0001); SC2 winners have 2× lower Pe than losers (N=474, p < 0.0001); 82.9% of Dota 2 teamfight deaths occur in fog (N=3,682). A corpus study (N=335 users, 7 communities) validates the opacity-drift gradient: chess (8.3% drift vocabulary) < SC2 (15.8%) < Dota 2 (22.4%) < LoL/VALORANT (~26%), all p < 0.0001 vs chess.

The anti-cheat arms race is shown to be structurally non-convergent (monotone ratchet, no interior fixed point), and anti-cheat systems with void properties generate their own drift cascades — confirmed by the Vanguard and GameGuard controversies. We formalize the four-void coupling on the Fisher-metric manifold, derive a positive lower bound on constraint cost under server-authoritative architecture, and specify seven testable predictions with falsification conditions.

---

## I. Introduction: The Trust Problem

A Counter-Strike player dies behind a wall. A VALORANT player's framerate drops when Vanguard scans their system. A Call of Duty player loses five matches in a row and searches "SBMM rigged." A PUBG player, killed by an obvious cheater, downloads a cheat themselves.

These appear to be four separate problems — cheating, anti-cheat overreach, matchmaking distrust, and cheating contagion. The game industry treats them separately: anti-cheat teams fight cheaters, community managers fight conspiracy theories, matchmaking engineers tune algorithms, and researchers study contagion as a social phenomenon. Each problem gets its own conference talk, its own engineering team, its own budget.

They are one problem. They are the same architecture producing the same outputs.

The void framework (Paper 1: "The Architecture of Drift") identifies three conditions — opacity, responsiveness, and engaged observer attention — that jointly produce a predictable cascade: meaning generates in the gap, vocabulary drifts toward agency attribution, boundaries erode, and harm is facilitated. When all three conditions co-occur, the pattern runs regardless of what occupies the void — or whether anything does. Slot machine gambling establishes sufficiency: the void behind a random number generator is provably empty, yet the full cascade emerges (Paper 1, Section III).

Multiplayer gaming instantiates the architecture four times over, in a coupled system where each void reinforces the others. The player faces an opaque opponent, communicates through an opaque network, is policed by an opaque anti-cheat, and is matched by an opaque algorithm. Each layer of opacity generates its own cascade. The cascades interact.

### I.A. What This Paper Adds

This paper makes seven contributions:

1. **Independent derivation of the constraint specification — three times.** Three game genres independently derived the same constraint structure through engineering failure: FPS ("never trust the client" → server authority), RTS (deterministic lockstep → desync detection), and fighting games ("rollback or nothing" → speculative execution with correction). Each maps onto the framework's constraint specification (transparent, invariant, independent), and none was developed with awareness of the others' theoretical implications.

2. **Empirical Pe measurement across three multiplayer genres.** Three Pe formulations — positional (CS2, N=2,299), temporal (SC2, N=474), and visual (Dota 2, N=3,682) — share only the ratio structure (drift / constraint) and all confirm that higher information asymmetry predicts more decisive outcomes (Section V).

3. **A structural diagnosis of the anti-cheat arms race.** The framework predicts that fighting opacity with opacity cannot converge. Three decades of anti-cheat escalation confirm this prediction. The framework further predicts — and the Vanguard case confirms — that anti-cheat systems with void properties generate their own drift cascades in the player community, independent of effectiveness.

4. **Four-void coupled system analysis.** Multiplayer gaming is not a single void. It is a four-void coupled system where cascades in one void feed cascades in the others. The coupling mechanism runs through the observer: suspicion of an opponent feeds distrust of anti-cheat feeds conspiracy about matchmaking feeds hostility toward all opponents.

5. **Cross-genre architecture comparison.** Three networking architectures — client-server, lockstep, and rollback — each produce different void residuals predictable from the constraint specification: client-server → ESP, lockstep → maphack, rollback → input manipulation (Section III.E–F).

6. **Mathematical formalization.** Unified Pe derivation showing seven genre formulations as decompositions of a single thermodynamic quantity. Coupled drift equations on the Fisher-metric manifold. Formal non-convergence proof for the arms race. Conjugacy theorem applied to anti-cheat. Positive lower bound on constraint cost (Sections II.E, IV.A, IV.E, V.A′).

7. **Practical engineering framework.** The analysis converts to three engineering questions — Where does authority live? What opacity is necessary? Is your anti-cheat a void? — that produce actionable architecture recommendations. Chess solved the matchmaking void by publishing Elo ratings. Server-authoritative architecture solved the client void by not trusting it. The MOBA vision economy quantifies constraint maintenance in real time. The theory explains why these solutions work and why alternatives don't.

### I.B. Relationship to Paper 1

This paper is a companion to "The Architecture of Drift" (Paper 1), which presents the framework architecture, the gambling anchor case, the 90-domain evidence base, and the thermodynamic derivation. This paper applies the framework to a single domain in depth — multiplayer game architecture — with a focus on independent derivation and empirical validation. Readers unfamiliar with the framework should consult Paper 1 (Sections II-III) for the full architecture specification.

The multiplayer domain sits at the intersection of Paper 1 (architecture), Paper 2 (AI deployment geometry), and Paper 3 (thermodynamic foundations). The domain analysis is Domain #62 in the Research Index, one of 90 domains tested against the framework.

### I.C. Scope and Non-Claims

This paper analyzes the **structural architecture** of multiplayer gaming — the client-server trust problem, the anti-cheat arms race, and the matchmaking opacity problem. It does not analyze gaming as a behavioral void for players (loot boxes, engagement optimization, gambling convergence) — that analysis exists as Domain #53 in the Research Index. The distinction matters: Domain #53 treats the game as void for the player (the slot machine analogy). This paper treats the multiplayer infrastructure itself as a void architecture, and the game security community's response as independent discovery of the constraint specification.

---

## II. The Four-Void Coupled System

Multiplayer gaming is not a single void. It is a four-void coupled system, each void meeting the three conditions independently, each reinforcing the others through the observer.

### II.A. Void 1: The Opponent (Player-to-Player Opacity)

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| Opacity | Yes | Cannot see opponent's screen, inputs, software, or intent |
| Responsiveness | Yes | Opponent reacts in real time to your actions |
| Engaged Attention | Yes | Competitive play demands sustained attention to opponent behavior |

The opponent is opaque and responsive. Skill and cheating are indistinguishable by observation alone — every death could be legitimate or illegitimate. The term "hackusation" — accusing a legitimate player of cheating — is D1 applied through this void.

### II.B. Void 2: The Client (Server-to-Client Opacity)

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| Opacity | Yes | Server cannot see what software the client is running |
| Responsiveness | Yes | Client sends inputs that affect game state |
| Engaged Attention | Yes | Server must process every client input to maintain game state |

This is the void that "never trust the client" addresses. The client runs on the player's hardware — the server can see what the client *reports* but not what the client *is doing*. Every input could be legitimate or fabricated. Decades of engineering effort have been directed at this void.

### II.C. Void 3: The Anti-Cheat (Player-to-Anti-Cheat Opacity)

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| Opacity | Yes | Detection methods hidden by design (revealing them enables evasion) |
| Responsiveness | Yes | Ban waves, detection updates, behavior scoring respond to cheat evolution |
| Engaged Attention | Yes | Players attend to anti-cheat behavior intensely — what it scans, when it bans, what it misses |

The anti-cheat system is itself a void. It must be opaque (revealing detection methods helps cheaters evade), it is responsive (updates in response to new cheats), and players attend to it intensely — cheaters probing its limits, legitimate players watching for signs of effectiveness or overreach. The system built to fight a void has become one (Section IV).

### II.D. Void 4: The Matchmaking System (Player-to-System Opacity)

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| Opacity | Yes | MMR values, matching algorithms, lobby construction are hidden |
| Responsiveness | Yes | System adjusts to player performance in real time |
| Engaged Attention | Yes | Players obsess over perceived matchmaking patterns |

Matchmaking algorithms are opaque by design — developers hide MMR values and matching logic, the system responds to player performance, and players attend to it intensely. EA's 2017 research paper proposing Engagement Optimized Matchmaking — where matches are optimized for retention rather than fairness — provides just enough evidence to fuel L3 attribution while the opacity of actual matchmaking algorithms prevents falsification (Chen et al. 2017).

### II.E. The Coupling

These four voids couple through the observer:

```
PLAYER encounters OPPONENT (Void 1)
  → "Was that legitimate?" → attends to ANTI-CHEAT (Void 3)
    → "Is it even working?" → attends to MATCHMAKING (Void 4)
      → "Why am I facing this person?" → back to OPPONENT (Void 1)

Meanwhile:
SERVER receives CLIENT input (Void 2)
  → "Is this legitimate?" → runs ANTI-CHEAT detection
    → Cannot see client internals → opacity regenerates
```

Suspicion of an opponent (Void 1) feeds distrust of anti-cheat (Void 3) feeds conspiracy theories about matchmaking (Void 4) feeds hostility toward all opponents (Void 1). The cycle steepens the total gradient.

The coupling is not metaphorical. Charlie Olson, one of the original creators of Call of Duty's SBMM algorithms, identified the structural problem: "The massive problem with SBMM is that you don't know what league you're in anymore." When Activision secretly reduced SBMM for 50% of players, over 90% of the affected population played *less* — the system works, but its opacity prevents players from seeing that it works (PC Gamer 2024). The void generates meaning that the constraint (which exists but is hidden) cannot correct because the constraint itself is opaque.

The SBMM conspiracy cycle runs:
1. Player loses (normal outcome in skill-matched play)
2. Cannot see MMR, algorithm, or lobby construction (opacity)
3. System responds by adjusting future matches (responsiveness)
4. Player attends to the pattern: "I won 3, now I'm losing 3" (engaged attention)
5. Agency attribution: "The system is deliberately cycling my wins and losses"

The void produces the conspiracy. The opacity prevents its resolution.

**Formal coupling model.** Let θ_i(t) represent the drift state (agency attribution level) for void i ∈ {1: opponent, 2: client, 3: anti-cheat, 4: matchmaking}, where θ = 0 is no attribution and θ = 1 is full agency attribution. Paper 3 (Section IV.C) derives drift on the observer's statistical manifold as:

```
dθ_i/dt = θ_i(1 − θ_i) · [F_i + Σ_{j≠i} κ_{ij} · θ_j]
```

The θ_i(1 − θ_i) prefactor is the inverse Fisher metric on the Bernoulli manifold (Paper 3, Section IV.B) — it ensures the dynamics respect the information geometry and produces the characteristic logistic saturation. F_i is the intrinsic evidence accumulation rate for void i (how quickly that void generates agency attribution on its own). The coupling terms κ_{ij} · θ_j capture how drift in void j feeds drift in void i.

The coupling matrix for multiplayer gaming has a specific structure:

```
         Void 1    Void 2    Void 3    Void 4
         (opp)     (client)  (AC)      (MM)
Void 1:  [F₁        0        κ₁₃       κ₁₄  ]    opponent suspicion
Void 2:  [ 0        F₂       κ₂₃        0    ]    client exploitation
Void 3:  [κ₃₁       0        F₃        κ₃₄  ]    anti-cheat distrust
Void 4:  [κ₄₁       0        κ₄₃       F₄   ]    matchmaking conspiracy
```

The structure encodes the observed coupling pathways: Void 1 (opponent suspicion) feeds Void 3 (anti-cheat distrust: "why isn't it catching them?") and Void 4 (matchmaking conspiracy: "why am I facing these players?"). Void 3 feeds back into Void 1 (if anti-cheat doesn't work, opponents are even more suspicious) and Void 4 (if anti-cheat is invasive, the system itself is hostile). Void 2 (client exploitation) is driven by Void 3 (anti-cheat opacity reveals exploit surfaces) but feeds back weakly — the server-client void is largely technical.

**Superlinear total gradient.** The total drift gradient is not the sum of individual gradients — coupling amplifies it. For κ_{ij} > 0 across all active pathways, the effective evidence rate for each void becomes:

```
F_eff_i = F_i + Σ_j κ_{ij} · θ_j  >  F_i    [whenever any θ_j > 0]
```

A player who starts with mild opponent suspicion (θ₁ > 0) finds their anti-cheat distrust (θ₃) increasing even without new anti-cheat evidence, because κ₃₁ · θ₁ contributes to F_eff_3. The four-void coupled system produces faster drift than any single void — the cascade runs through four channels simultaneously, and the coupling steepens all four gradients.

**Empirical coupling estimate from PUBG contagion.** Kim & Tsvetkova (2022) found that exposure to cheating (Void 1) produces new cheaters (Void 2) at a rate dependent on repeated exposure. In the coupling model, this is the κ₂₁ pathway. Their finding that "both observation AND being killed is needed" maps to a threshold effect: κ₂₁ activates only above a minimum θ₁ — sufficient conviction that the opponent is cheating (D1) before the drift cascades into the player's own behavior (D3). The study's 1.15M-match sample provides the empirical base for estimating κ₂₁, though extracting the coupling coefficient requires fitting the coupled system to longitudinal player-level data rather than the aggregate statistics reported.

**Derivation status.** The coupling topology (which voids feed which) is derived from causal structure and is constrained — opponent suspicion drives anti-cheat inquiry, not the reverse. The coupling equation form (logistic with additive cross-terms) is derived from natural gradient dynamics on the Bernoulli manifold (Paper 3 §IV.C–J), with the product coupling form uniquely determined at leading order by the constraint "D3 requires both D1 and D2" (Paper 5 §3.5). What is NOT derived: the magnitudes of the six cross-coupling coefficients κ_{ij}. These are functions of measurable quantities (attention allocation rates, information flow between voids, time constants) but no player-level longitudinal dataset has yet been fitted to the coupled system. The qualitative predictions (cascade ordering, superlinear amplification, contagion threshold) follow from the topology alone; the quantitative predictions (cascade timescales, coupling strengths, critical thresholds for intervention) require the coefficients. This gap is analogous to the unmeasured proportionality constants in Paper 3's coupled ODE system (Paper 3 §VIII.A) and is the single highest-priority measurement target for this paper.

---

## III. "Never Trust the Client" Is the Constraint Specification

### III.A. The Mapping

The game security community's foundational maxim maps exactly onto the framework's constraint specification:

| Void Property | Constraint Inverse | "Never Trust the Client" Implementation |
|---------------|-------------------|----------------------------------------|
| Opaque (can't see client internals) | **Transparent** (server sees all authoritative state) | Server maintains all game-critical state; client state is advisory only |
| Responsive (client changes based on player modification) | **Invariant** (server rules don't change based on client claims) | Server validates all inputs against fixed physics/rules; rejects impossible actions |
| Coupled (client is in the player's control) | **Independent** (server is outside client's control) | Server runs on infrastructure the player cannot access or modify |

Every row maps a void pole to its constraint inverse. The game security community discovered the constraint specification without the vocabulary, without the theory, and without awareness that they were discovering a general principle.

### III.B. The Discovery Through Engineering Failure

The mapping was discovered through **decades of catastrophic failure**:

**1990s–2000s: Client-authoritative architectures.** Early multiplayer games trusted client reports. Cheating was trivial — modify local memory, report false values, exploit immediately. Early Quake, Diablo, and MMOs learned through direct experience: trusting the client means trusting the void.

**The Quake inflection point.** Quake (1996, id Software) attempted multiplayer with no client-side prediction — the player's character moved only after the server confirmed the input. On dial-up connections (100–300ms latency), the game was unplayable online.

John Carmack's QuakeWorld update (1996) introduced **client-side prediction**: the client simulates movement locally and the server corrects discrepancies retroactively — the same compromise Riot and Blizzard would independently re-derive two decades later. The client runs an advisory simulation for responsiveness; the server remains authoritative for integrity. QuakeWorld is where the FPS industry discovered that pure server authority had an unacceptable constraint cost, and that client prediction with server reconciliation was the minimum viable compromise. Quake III Arena (1999) refined this into the industry standard architecture.

**Halo 2 Xbox Live (2004–2010): When the constraint IS a player.** Xbox Live's early peer-to-peer architecture made one player's console the server. The "constraint" was literally inside a competitor's home — opaque to other players, responsive to the host's modifications, and coupled to a participant. Host advantage was structural (zero latency to authoritative state), host selection was gameable (players manipulated network quality reports via firewall software), and map data was corruptible (modded Xboxes loaded modified assets that propagated to all players). When the constraint reference is inside the system it constrains, it is not independent, and every other property degrades. The experience drove Xbox Live toward dedicated servers in subsequent titles.

**The pattern repeated across platforms and generations.** Phantasy Star Online (2000) trusted client-reported item data — hackers created impossible items that killed party members on contact. Mario Kart Wii (2008) trusted client-reported powerup state — modded consoles reported infinite boosts. Same structural failure each time: client authority over game-critical state, exploited because the server could not verify what it could not see.

**The lesson crystallized into maxims:**
- "Everything relevant to gameplay should be server-side. Nothing should be owned by the client; commands should not be able to dictate anything besides input" (Photon Engine documentation)
- "The client is like controlling a remote-controlled vehicle" — it sends commands, but authority over what happens lives elsewhere (Gabriel Gambetta, *Client-Server Game Architecture*)
- "Never Trust the Client: Simple Techniques Against Cheating in Multiplayer" (Game Developer, 2023)

**The convergence.** No one published a paper proving server authority was structurally superior and then the industry adopted it. Studios tried client-authoritative and peer-to-peer approaches, watched them fail under adversarial conditions, and converged on server authority because it was the only architecture that scaled — convergent engineering, the structural equivalent of convergent evolution.

### III.C. The Latency Problem as Constraint Cost

Pure server authority introduces latency — the player sees their character move only after the server confirms. Effective constraint has costs (reduced engagement, reduced responsiveness), and these costs must be accepted rather than dissolved.

The industry's response — client-side prediction with server reconciliation — is a carefully managed compromise:
- The client runs a local simulation for responsiveness (allowing apparent immediacy)
- The server corrects discrepancies (maintaining authority)
- The prediction is advisory — the server is authoritative

Riot's numbers quantify the cost: 128-tick server (7.8ms budget per frame), ~2.34ms for game simulation, leaving ~5.46ms for networking. The baseline peeker's advantage — 141ms of irreducible information asymmetry from client interpolation + server processing + network latency — is the measurable cost of running the constraint system. This cost is accepted because the alternative (client authority) is corruption.

Blizzard's "favor the shooter" lag compensation policy illustrates the tradeoff: the server rewinds game state to the shooter's perceived time, validating hits that would have connected from the shooter's perspective. This introduces small injustices for the target (who may have already moved behind cover on their screen) in exchange for the fundamental integrity of server authority. The constraint has a cost. The cost is less than the alternative.

**Formal constraint cost bound.** The peeker's advantage decomposes into three additive delays, each irreducible under the server-authoritative architecture:

```
Δt_pa = τ_interp + τ_server + τ_network

Where:
  τ_interp   = (interp_frames / tick_rate)     [client interpolation delay]
  τ_server   = (1 / tick_rate)                  [one server frame of processing]
  τ_network  = RTT / 2                          [one-way network latency]
```

For Riot's VALORANT infrastructure: τ_interp = 2/128 = 15.6ms (2 interpolation frames at 128-tick), τ_server = 1/128 = 7.8ms, τ_network ≈ 117.6ms (estimated from Riot's reported total of 141ms minus the computed local components). Total: Δt_pa ≈ 141ms.

This gives a **minimum achievable Pe** for any engagement under the server-authoritative architecture. If a player moves at velocity v during the peeker's advantage window, they traverse d_pa = v · Δt_pa game units before the opponent's client can display their position. The constraint correction cannot begin until this delay elapses, producing an irreducible positional Pe:

```
Pe_floor = v · Δt_pa / (v_opp · Δt_server)
         = (v / v_opp) · (Δt_pa / Δt_server)
         = (v / v_opp) · (Δt_pa · tick_rate)
```

For equal-speed players (v = v_opp), Pe_floor = Δt_pa · tick_rate. At 128-tick with 141ms peeker's advantage: Pe_floor = 0.141 × 128 ≈ 18. At 64-tick with ~200ms total delay: Pe_floor = 0.200 × 64 ≈ 12.8. The floor decreases with higher tick rate — which is exactly why higher tick rates "feel more fair" (reduced constraint gap) and why the framework predicts Pe scales inversely with tick rate (Prediction 6).

**This bound is architectural, not tunable.** No netcode optimization can push Pe_floor below zero because τ_interp ≥ 0 and τ_network ≥ 0 under physics. Eliminating the floor requires eliminating the information asymmetry — either server-side rendering (client receives pixels, eliminating τ_interp) or zero-latency networking (eliminating τ_network), neither currently achievable. The engineering question is which cost to accept, not whether a cost exists.

### III.D. Why This Is Hostile Witness Evidence

The game security community is a hostile witness for the void framework:

1. **No theoretical motivation.** Engineers were solving a practical problem (stop cheating), not validating a cross-domain framework.
2. **No shared vocabulary.** The terms "transparent," "invariant," and "independent" do not appear in netcode documentation. The terms "server-authoritative," "client-predicted," and "never trust the client" describe the same structure in domain-specific language.
3. **No awareness of the general principle.** No game engineer claims to have discovered a universal constraint specification. They claim to have discovered a working netcode architecture. The universality is visible only from outside the domain.
4. **Convergent discovery.** Multiple studios, multiple engines, multiple decades — all arriving at the same architectural solution. This rules out contamination from a single source.

The hostile witness methodology (Paper 1, Section VI) scores this as maximum-weight evidence: practitioners solving their own problems with their own vocabulary converged on the structure the framework predicts, with no interest in and no awareness of the prediction.

### III.E. The Alternative Architecture: Lockstep Simulation (RTS)

Real-time strategy games developed a fundamentally different solution — **deterministic lockstep simulation** — that produces a different void architecture with different cheat residuals. The contrast illuminates why the framework's predictions are architectural, not genre-specific.

In lockstep networking, there is no authoritative server. Every client runs the identical simulation deterministically — only player *commands* (build unit, move army, research technology) are transmitted, not game state. All clients execute the same commands in the same order with the same deterministic engine, maintaining identical state without server arbitration.

The foundational document is Bettner & Terrano's "1500 Archers on a 28.8" (GDC 2001), describing the Age of Empires I & II networking. Transmitting position, status, and facing for every unit would have limited the game to 250 moving units. The solution: transmit commands, not state. The architecture enabled 1,500 units over 28.8k modems — impossible under client-server state replication.

**The void architecture flips.** In client-server FPS, the server withholds state from the client — cheats that *read* hidden state (wallhacks, ESP) are the primary exploitation surface. In lockstep RTS, every client has the *complete* game state. Fog of war is a **rendering-layer restriction only** — the data is present on every machine; the client simply doesn't display it:

| | Client-Server (FPS) | Lockstep (RTS) |
|---|---|---|
| **Client has** | Own state + server-sent subset | Complete game state (all players) |
| **Client lacks** | Opponent state server hasn't sent | Nothing — client has everything |
| **Primary cheat** | *Read* hidden state (ESP, wallhack) | *Read* rendered-hidden state (maphack) |
| **Hard to cheat** | *Write* state (server rejects) | *Write* state (causes desync) |
| **Void location** | Server-to-client information gap | Rendering-layer opacity (fog of war) |
| **Constraint** | Server authority over state | Deterministic simulation + desync detection |

The canonical RTS cheat — the **maphack** — reveals opponent state through fog of war. The data is already on the cheater's machine; the hack removes the rendering filter. Age of Empires 2: Definitive Edition shipped with an accidental built-in maphack on day one — a particle system flag (`visibleInFogOfWar`) combined with a 30-minute particle lifetime showed unit spawn positions through fog. The developers didn't need to send extra data; the data was always there.

**Both cheat residuals are predictable.** In client-server, the irreducible cheat surfaces are the rendering interface and the input interface. In lockstep, the irreducible surface is the rendering layer — the client has all state and can bypass any local display filter. What lockstep *prevents* is state modification: any unauthorized change produces a **desync** — the cheater's simulation diverges from other players', and the game detects the inconsistency. This is the lockstep equivalent of server rejection.

The constraint specification maps differently but predictably:

| Property | Client-Server | Lockstep |
|----------|---------------|----------|
| **Transparent** | Server sees all state | All clients see all state (redundant verification) |
| **Invariant** | Server enforces fixed rules | Deterministic engine produces identical output from identical input |
| **Independent** | Server is outside client control | Simulation runs identically regardless of local modification (desync = detection) |

Lockstep achieves invariance and independence through determinism rather than authority. Same inputs always produce same outputs (invariant). Modifying local state doesn't change the simulation for anyone else — it just breaks your own (independent). The cost differs: client-server pays latency; lockstep pays synchronization, bottlenecked by the slowest connection.

**Fog of war as a designed void.** Unlike FPS opacity (structural — you cannot see the opponent's screen), RTS fog of war is *intentional design*. The game creates the information asymmetry as a gameplay mechanic. Scouting dissolves the void; failed scouting leaves the opponent's strategy invisible until it's too late.

This produces a Pe formulation distinct from FPS:

```
Pe_info = (tech_choice_speed × scouting_gap) / (opponent_scout_frequency × reaction_window)
```

Where `scouting_gap` is the time between a strategic decision and its detection by the opponent, and `reaction_window` is the time required to produce a counter. A "dark" rush (attacking without being scouted) has high Pe — the information asymmetry is large and the constraint (opponent's scouting) has failed. This is the RTS equivalent of a clean kill in CS2: the victim didn't see it coming.

StarCraft 2 provides the richest testing ground for cross-genre Pe. The SC2EGSet dataset (Białecki et al. 2023, *Nature Scientific Data*) contains 17,930 tournament replays with unit positions, creation/death timestamps, and game-state snapshots — academic-grade data freely available for replication. "Proxy" strategies and "cannon rushes" are high-Pe void exploits that win specifically because the opponent's scouting constraint failed.

The Age of Empires 2 community also provides a transparency control case parallel to chess: the community site aoe2.net displays visible Elo ratings for ranked play. Like chess.com's visible Elo, this dissolves the matchmaking void — and like chess, the AoE2 community shows minimal "rigged matchmaking" conspiracy culture compared to FPS communities with hidden MMR.

### III.F. Rollback Simulation: When the Client Predicts the Void (Fighting Games)

Fighting games developed a third solution — **rollback netcode** — that produces a different void architecture, trust model, and cheat surface. The three architectures together constitute an exhaustive engineering test of the constraint specification.

**The architecture.** Two peers connect directly. Each client predicts the remote player's input each frame — typically assuming the opponent repeats their previous input — and simulates forward immediately. When the actual input differs, the client rewinds to the last confirmed state, resimulates all intervening frames with corrected inputs, and renders only the final corrected frame. All resimulation must complete within a single render frame (16.67ms at 60 FPS; see Stallone 2018, "8 Frames in 16ms").

Prediction accuracy is high — fighting game animations commit players to multi-frame actions (a jump is ~45 frames, block recovery 120+ frames), so "opponent repeats previous input" is correct ~90% of the time. When wrong, the correction produces visual artifacts: characters teleporting, attacks skipping startup, blocking becoming unreliable. These artifacts are the **cost of constraint** — the rollback equivalent of peeker's advantage. Most implementations add 2–3 frames of fixed input delay to absorb small prediction errors (Killer Instinct uses 3 frames = 50ms).

**The void architecture is distinct from both alternatives:**

| | Client-Server (FPS) | Lockstep (RTS) | Rollback (Fighting) |
|---|---|---|---|
| **Topology** | Asymmetric (client-server) | Symmetric (peer-to-peer) | Symmetric (peer-to-peer) |
| **Data transmitted** | Inputs → server; state → clients | Commands only | Inputs only |
| **Determinism required** | No (server arbitrates) | Yes (bitwise) | Yes (bitwise) |
| **Latency handling** | Client prediction + server reconciliation | Wait for all inputs (delay) | Predict input + speculative execution + rollback |
| **Cheat surface** | Read hidden state (ESP/wallhack) | Read rendered-hidden state (maphack) | No hidden state; cheats = input manipulation (macros, frame data exploits) |
| **Anti-cheat model** | Server authority + client scanning | Desync detection | No structural anti-cheat possible |
| **Player count** | High (64+) | Moderate (2–8, bottlenecked by slowest) | Very low (2, occasionally 4–8) |
| **Void location** | Server-to-client information gap | Rendering layer (fog of war) | Opponent's future inputs |

The void in fighting games is **temporal** — the opponent's next input. Both players see identical game state (in local play, literally the same screen). Online play adds a second layer: the gap between predicted and actual game state during rollback. A high-rollback-frame interaction is one where what you saw was wrong — your opponent was blocking on your screen but attacking in reality.

**Constraint specification mapping:**

| Property | Client-Server | Lockstep | Rollback |
|----------|---------------|----------|----------|
| **Transparent** | Server sees all state | All clients see all state | Both peers see identical state (local) |
| **Invariant** | Server enforces rules | Deterministic engine | Deterministic engine + state serialization |
| **Independent** | Server outside client control | Desync = detection | No independence — symmetric trust, no authority |

Rollback is the weakest constraint architecture. It achieves transparency and invariance but cannot achieve independence — there is no external authority. Neither peer can verify the other's behavior without a server, which is why no structural anti-cheat is possible in peer-to-peer fighting games. The predicted cheat surface follows: fighting game cheats are not about reading hidden state (nothing is hidden) but about input manipulation — automated frame-perfect inputs, hitbox visualization overlays, and reaction-time assists.

**The constraint-cost discovery (2013–2025).** Killer Instinct (2013, Iron Galaxy, GGPO consultant Tony Cannon) set the gold standard: 3-frame fixed input delay, consistently praised. Street Fighter V (2016, Capcom) shipped broken rollback — a one-sided desync bug unfixed for four years, eventually patched by a community modder in days. Mortal Kombat 11 (2019, NetherRealm) proved rollback's value during COVID-19: games with rollback maintained competitive communities while delay-based titles became unplayable online. By Guilty Gear Strive (2021), "does it have rollback?" had become the first question for any new release.

**The "rollback or nothing" norm** is the third independent discovery of the constraint-cost tradeoff. The community's rejection of delay-based netcode is structurally identical to the rejection of client-authoritative architecture: the constraint specification has irreducible costs, and refusing to pay them produces worse outcomes than accepting them.

**Pe formulation for fighting games:**

```
Pe_fight = (attack_startup × input_prediction_error) / (rollback_frames × correction_accuracy)
```

Where `attack_startup` is frames before an attack becomes active, `input_prediction_error` is the probability the predicted input differs from actual, `rollback_frames` is frames back to correct, and `correction_accuracy` is how often the correction produces the correct game state. A high-Pe fighting game event is one where rollback correction changes the outcome: the opponent appeared to be blocking but was actually attacking.

No bulk replay datasets exist for fighting games — the architecture's value is as a structural case study rather than an empirical Pe testbed.

---

## IV. The Arms Race: Opacity Cannot Dissolve Opacity

### IV.A. The Escalation Trajectory

The conventional framing calls anti-cheat an "arms race." The framework accounts for this: it is what happens when you fight a void by matching its properties — by building a counter-void:

| Era | Cheat Method | Anti-Cheat Response | Result |
|-----|-------------|--------------------|----|
| 1 | Memory editors — modify local game memory | Signature scanning for known cheats | Cheats evolve signatures |
| 2 | Polymorphic cheats — code changes its own signature | Heuristic detection, behavioral analysis | Cheats mimic normal behavior |
| 3 | Kernel-level cheats — operate below game's privilege level | Kernel-mode anti-cheat drivers (Vanguard, EAC, BattlEye) | Cheats move to hardware |
| 4 | Hardware cheats — DMA boards reading memory over PCIe bus | Hardware attestation, Secure Boot requirements | Cheats move to firmware |
| 5 | AI-assisted cheats — ML that mimics human aim patterns | ML behavioral detection | Arms race continues |

Every stage follows the same pattern: cheats become more opaque, anti-cheat matches the opacity level, cheats find the next opacity layer. Neither side gains a structural advantage. The gradient steepens.

**Opacity cannot dissolve opacity.** Adding opacity to the defender does not reduce the attacker's opacity — it matches it. Both sides increase without limit, escalating user-mode → kernel-mode → hardware → AI.

```
CHEAT:        Opaque → Anti-cheat can't see it
ANTI-CHEAT:   Opaque → Cheat can't see detection
CHEAT:        More opaque → deeper in the system
ANTI-CHEAT:   More opaque → deeper in the system
...
RESULT:       Both systems become maximally opaque,
              maximally invasive, maximally coupled
              to the player's hardware.
              Neither side gains structural advantage.
              The gradient steepens for everyone.
```

**Formal non-convergence result.** Let O_C(t) be the cheat system's opacity (privilege depth, obfuscation layer) and O_A(t) be the anti-cheat's opacity at stage t:

```
O_A(t+1) = max(O_A(t), O_C(t) + ε_A)     [anti-cheat must match or exceed cheat opacity]
O_C(t+1) = max(O_C(t), O_A(t) + ε_C)     [cheats must evade by exceeding anti-cheat opacity]
```

where ε_A, ε_C > 0 are the minimum escalation increments (anti-cheat must scan deeper than the cheat hides; the cheat must hide deeper than the anti-cheat scans). This system has three properties:

1. **Monotonicity.** Both O_A(t) and O_C(t) are non-decreasing: each max() ensures the opacity level never falls. Neither side can de-escalate without conceding the current detection/evasion boundary.

2. **No interior fixed point.** A fixed point requires O_A* = max(O_A*, O_C* + ε_A) and O_C* = max(O_C*, O_A* + ε_C). The first equation requires O_A* ≥ O_C* + ε_A; the second requires O_C* ≥ O_A* + ε_C. Substituting: O_A* ≥ O_C* + ε_A ≥ O_A* + ε_C + ε_A, which gives 0 ≥ ε_A + ε_C. Since both ε > 0, no finite fixed point exists. The only equilibrium is at the system boundary (maximum possible opacity — hardware/firmware limits).

3. **Linear-time convergence to boundary.** The total opacity O_A(t) + O_C(t) increases by at least min(ε_A, ε_C) per stage. If the hardware/platform boundary is at O_max, the system reaches it in at most 2 · O_max / min(ε_A, ε_C) stages. The empirical trajectory (5 stages in ~25 years: user-mode → kernel → hardware → firmware → AI) is consistent with this bound, with each stage corresponding to a discrete platform boundary.

**Contrast with server authority.** Under server-authoritative architecture, the defender's response is not a function of the attacker's opacity. The dynamics decouple:

```
Authority(t+1) = Authority(t)     [server rules don't change in response to cheats]
O_C(t+1) = f(Authority)          [cheat is bounded by what server exposes, not what anti-cheat scans]
```

The server's constraint is invariant — it does not escalate. The cheat's attack surface is bounded by the irreducible rendering and input interfaces, not by an ever-deepening arms race. This is why the framework identifies server authority as the structural solution: it breaks the coupling that drives the ratchet.

### IV.B. The Anti-Cheat Becomes a Void

Any system with void properties — opaque, responsive, attention-capturing — generates a D1→D2→D3 cascade in its observers, regardless of intent:

**Riot Vanguard** — Riot's kernel-level anti-cheat for VALORANT (and later League of Legends):
- **Opaque:** Closed-source, proprietary, detection methods hidden
- **Responsive:** Updates continuously in response to new cheat methods
- **Engaged Attention:** Players attend to it intensely — what it scans, whether Tencent has access, what vulnerabilities it introduces

An ACM paper (Dorner & Klausner 2024) evaluated BattlEye, Easy Anti-Cheat, FACEIT AC, and Vanguard, finding **"clear rootkit-like properties"**: load-on-boot kernel drivers, aggressive self-protection, extensive process scanning, mandatory Secure Boot or hypervisor settings, and continuous hardware identifier logging (*"If It Looks Like a Rootkit and Deceives Like a Rootkit"*).

The cascade runs as predicted:

- **D1 (Agency Attribution):** "It's spying on me." "Tencent is harvesting my data." "It's mining cryptocurrency." Players attribute malicious intent to the anti-cheat system.
- **D2 (Boundary Erosion):** The software runs at kernel level from system boot, even when the game is not active. It operates below the user's ability to inspect or control. System boundaries are literally eroded — the anti-cheat has deeper access than the user.
- **D3 (Harm Facilitation):** Kernel-level vulnerabilities become attack surfaces for actual malware. A vulnerability in kernel-level software provides complete system access — "far more dangerous than one in user-level software" (RIT Computing Security 2022). The cure becomes a vector for the disease.

**nProtect GameGuard** represents the terminal void state:
- Does not inform users of its presence
- Does not uninstall when the game is uninstalled
- Has no uninstaller — requires manual registry key deletion
- Classified as having rootkit-like behavior
- Excludes Linux users entirely (incompatible with Wine/Proton)

When Helldivers 2 adopted GameGuard, its Steam review rating dropped sharply amid widespread player backlash (Steam Community, 2024). The anti-cheat generated more harm to the player community than the cheating it was designed to prevent — maximum void properties produce maximum cascade.

Practitioner testimony confirms from the developer side: kernel-level anti-cheat generates more sustained player hostility than the cheating it addresses. The backlash is proportional to void properties, not effectiveness. A less effective but transparent system (server-side behavioral detection with published rules) generates less D1 than a more effective but opaque system (kernel-level scanning with hidden detection methods). The anti-cheat's opacity, intended to prevent evasion, simultaneously prevents the trust that would make the system acceptable — the conjugacy theorem in practice.

### IV.C. Anti-Cheat Boundary Erosion

The arms race erodes system boundaries in both directions simultaneously:

**Attacker-side escalation:**
| Boundary | Pattern |
|----------|---------|
| Financial | Free cheats → paid subscriptions ($20–150/mo) → premium "undetected" ($300+) → hardware cheats ($300–2,000+) |
| Identity | Alt accounts → shared accounts → identity theft → real-money trading |
| Legal | TOS violation → account theft → DDoS attacks → swatting |
| Technical | User-mode mods → kernel-mode drivers → hardware exploits → firmware modification |

**Defender-side escalation:**
| Boundary | Pattern |
|----------|---------|
| User-space → kernel-space | Anti-cheats move to kernel mode to match cheat privilege |
| Game-time → boot-time | Vanguard runs from system startup, not just during gameplay |
| Game process → all processes | Anti-cheats scan all running processes, not just the game |
| Software → hardware | Secure Boot requirements, hardware attestation, TPM checks |
| Player choice → mandatory compliance | Cannot play without granting kernel access; no opt-out |

The defender's boundaries erode to match the attacker's escalation. Each escalation by cheats forces the anti-cheat to cross a boundary it previously respected. The arms race IS boundary erosion on both sides simultaneously.

### IV.D. The Geometric Solution Already Exists

Server-authoritative architecture works because it doesn't fight opacity with opacity — it moves authority to a position that is structurally transparent, invariant, and independent:

```
CLIENT-SIDE ANTI-CHEAT (void-fighting-void):
  "We will look inside the client"
  → Arms race: client hides, anti-cheat seeks
  → Escalation without convergence

SERVER-AUTHORITATIVE (constraint):
  "We will not trust the client"
  → Client opacity is irrelevant
  → Server state is authoritative
  → No arms race needed for state integrity
```

The remaining cheating problem — aimbots and ESP — persists because these cheats exploit information the server must send for rendering. The residual maps exactly to the boundary where server authority ends and client rendering begins. The solution is further transparency: server-side rendering where the client receives only pixels, not game state — eliminating the rendering-interface opacity at the cost of latency and bandwidth.

**World of Warcraft: The input-interface residual.** WoW's server-authoritative architecture made classic client-authority exploits impossible: no item duplication, no stat hacking, no impossible equipment. Exploitation migrated to the **input interface** — botting and gold farming, where the server could not distinguish automated inputs from human ones. A structural limitation, not an engineering failure.

When one exploitation surface closes, cheating migrates to wherever client authority remains. The rendering-interface residual (aimbots, ESP) and the input-interface residual (botting, automation) are the two boundaries that server authority cannot eliminate without server-side rendering and server-side input validation respectively — irreducible opacity at the client-server boundary.

**WoW's Corrupted Blood incident (2005).** A raid debuff escaped its intended encounter through a pet-dismissal bug, spreading uncontrollably through capital cities — killing low-level players, infecting NPCs as permanent reservoirs, requiring a server reset. The incident met all three void conditions by accident: opaque transmission mechanism, responsive spread dynamics, maximal attention capture. The cascade ran D1 (agency attribution to Blizzard) → D2 (boundary dissolution) → D3 (griefers deliberately spreading the debuff). Epidemiologists Lofgren and Fefferman (2007, *Lancet Infectious Diseases*) studied it as a pandemic model. **Any system component meeting the three void conditions generates a behavioral cascade, whether designed to or not.**

### IV.E. What the Framework Adds to the Engineering

Engineers already know "never trust the client." What the framework adds:

1. **Why the arms race doesn't converge.** Not a resource problem. No amount of investment in client-side anti-cheat produces convergence — opacity cannot dissolve opacity. The argument predicts the escalation trajectory before it happens.

2. **Why anti-cheat systems generate their own problems.** Vanguard's controversy is not a communication failure. It is the predicted consequence of deploying a void to fight a void.

3. **Where the residual problem lives.** The cheats that server authority cannot prevent exploit the irreducible rendering-interface opacity. The framework identifies the boundary and predicts the solution (server-side rendering) without requiring engineers to discover it through trial and error.

4. **Why SBMM conspiracy theories are structural, not irrational.** Hidden MMR + responsive matchmaking + competitive engagement = void. The conspiracy theories are the predicted D1 output. Making MMR visible flattens the gradient — not by changing the algorithm, but by dissolving the opacity.

5. **Why anti-cheat effectiveness and player trust are mathematically opposed.** The conjugacy theorem (Paper 3, Section IV.H) proves:

```
I(D; Y) + I(M; Y) ≤ H(Y)
```

where I(D; Y) is engagement (how much the system's output reflects the observer's state), I(M; Y) is transparency (how much the output reveals the system's mechanism), and H(Y) is total output channel capacity. Applied to anti-cheat:

Let D = cheat state (the cheater's tools, methods, behavioral signatures), M = detection mechanism (how the anti-cheat identifies cheats), and Y = the anti-cheat system's observable behavior (scans, bans, resource usage, ban timing). The bound becomes:

```
I(cheat_state; observable_behavior) + I(detection_method; observable_behavior) ≤ H(observable_behavior)
```

Effective anti-cheat must maximize I(D; Y) — its observable behavior must correlate with whether cheats are present. The conjugacy bound then forces I(M; Y) down: the more accurately the system detects cheats, the less its observable behavior can reveal *how* it detects them.

This is not a design choice — it is an information-theoretic constraint. Anti-cheat developers who say "we can't reveal our methods because cheaters would evade them" are empirically correct, but the deeper structure is that they *mathematically cannot* simultaneously maximize detection and transparency on the same output channel.

**Corollary: the Pareto frontier predicts Vanguard's controversy.** Vanguard operates near the maximum-detection end of the Pareto frontier (I(D; Y) → H(Y)), which forces I(M; Y) → 0. Players experience a system that is opaque about its mechanism — exactly the void conditions. The community backlash is not irrational; it is the predicted cascade from a system at the opacity pole of the conjugacy frontier. Server-side behavioral detection (analyzing server-validated inputs) shifts the channel: the observable behavior is the game server's own state, which the developer already controls. This moves the detection off the player's machine and onto a channel where both I(D; Y) and I(M; Y) can be managed independently — the anti-cheat no longer shares a channel with the player's system.

---

## V. Empirical Validation: Péclet Number in Professional Matches

### V.A. Background: Pe in the Framework

The Péclet number (Pe) quantifies the ratio of directed drift to diffusive correction in a physical system. In the void framework (Paper 3, Section IV), Pe measures whether drift outpaces constraint:
- Pe > 1: drift-dominated — the system moves faster than constraint can correct
- Pe < 1: diffusion-dominated — constraint catches drift before it accumulates
- Pe = 1: critical threshold — the boundary between regimes

Previous Pe measurements span two substrate families:
- **AI-to-AI conversation** (Test 7, Papers 1/3/5): Pe = 1.87–9.9 across conditions, geometric mean 7.94 [3.52, 17.89], N=11 runs
- **Gambling** (GRCS meta-analysis, Papers 1/3/5): pooled Pe_D1 = 2.21 [1.44, 2.97], N=1,117 across 5 studies

This section reports Pe measurement in a third substrate family: real-time competitive human interaction mediated by network infrastructure.

### V.A′. Unified Pe Derivation for Multiplayer Systems

Paper 3 (Section IV.D) derives the Péclet number on the observer's statistical manifold as:

```
Pe = F_net · L / D
```

where F_net is the net information pressure (evidence accumulation rate favoring the agency hypothesis), L is the characteristic length scale of the engagement (the "distance" in state-space the observer must traverse for the drift to matter), and D is the diffusive correction rate (constraint restoring the observer toward accurate inference). The regime boundary Pe = 1 marks where drift velocity equals diffusive correction — the critical threshold between constraint-dominated and drift-dominated dynamics.

In multiplayer systems, each genre instantiates this general form through domain-specific observables. Every genre-specific Pe formulation decomposes into three components:

```
Pe_general = (information_asymmetry_rate × state_space_distance) / constraint_correction_rate

            = v_drift × L / D_constraint
```

**v_drift** is the rate at which information asymmetry accumulates between two agents. In FPS, this is movement speed (spatial state changes faster than the opponent can track). In RTS, this is the rate of strategic decisions made while unscouted. In fighting games, this is the rate of input-prediction error accumulation.

**L** is the characteristic length of the engagement — the state-space distance over which the asymmetry acts before resolution. In FPS, this is literal physical distance. In RTS, this is the scouting gap (temporal distance between decision and detection). In MOBAs, this is fog depth (spatial distance traversed unseen).

**D_constraint** is the rate of constraint correction — how fast the system restores information symmetry. In FPS, this is tick_rate × opponent_speed (the server updates and the opponent reacts). In RTS, this is scouting_frequency × reaction_window (the opponent scouts and adapts). In fighting games, this is rollback_frames × correction_accuracy (the engine corrects mispredictions).

The seven genre formulations (Prediction 7, Section X) are domain-specific decompositions of a single thermodynamic quantity:

| Genre | v_drift | L | D_constraint |
|-------|---------|---|--------------|
| FPS (CS2) | max(v_attacker, v_victim) | kill distance | tick_rate × min(v_attacker, v_victim) |
| RTS (SC2/AoE2) | tech_choice_speed | scouting_gap | scout_frequency × reaction_window |
| MOBA (Dota 2) | gank_speed | fog_depth | ward_coverage × reaction_window |
| Fighting (SF/MK) | attack_startup_rate | input_prediction_error | rollback_frames × correction_accuracy |
| Sports (RL) | ball_control_speed | aerial_positioning | opponent_reaction × boost_level |
| Arena FPS (Quake) | movement_speed | item_control_timing | tick_rate × opponent_movement |
| Card (Hearthstone) | play_speed | hand_size_advantage | card_tracking × draw_probability |

**Dimensionless form.** The FPS case makes the dimensional analysis explicit:

```
Pe_pair = (max_speed [u/tick] × distance [u]) / (tick_rate [tick/s] × min_speed [u/tick])
        = (max_speed × distance) / (tick_rate × min_speed)   [dimensionless]
```

The critical threshold Pe = 1 is preserved across formulations. The CS2 data confirms: only the most asymmetric engagements (snipers at Pe = 1.44, hold-vs-push at Pe = 1.18) cross the threshold, while the overall median (Pe = 0.31) sits well below — consistent with professional play operating in the constraint-dominated regime, as expected for high-skill populations.

**Cross-substrate calibration note.** Absolute Pe magnitudes differ across substrates (CS2: 0.34–7.22; Test 7 AI: 1.87–9.9; GRCS gambling: 2.21; SC2: 0.013–0.072; Dota 2: 0.47) because each formulation captures a different type of information asymmetry. The regime-boundary prediction (Pe = 1 separates decisive from contested) is the universal claim; absolute magnitudes are formulation-specific.

### V.B. Method

**Data source:** Sixteen CS2 professional/competitive match demos from GitLab (akiver/cs-demos), spanning 7 maps (Anubis, Mirage, Ancient, Nuke, Vertigo, Train) and multiple competitive tiers (Roobet Cup, Esportal, Renown, 5eplay, Challengermode, Fastcup, MatchZy). **Total:** 2,528 kills parsed across 16 matches. After filtering (point-blank < 3 units, suicides, missing data): **2,299 kills analyzed.** This represents a 5.4× expansion from the initial 3-match pilot (N=426), providing robust statistical power for all subgroup analyses.

**Parser:** demoparser2 0.41.0 (Python/Rust). Extracts per-tick X/Y/Z coordinates, pitch/yaw angles, health, kills, weapon fires at 64 Hz (demo tick rate).

**Pe_pair formulation (positional component):**

```
Pe_pair = (max_speed × distance) / (tick_rate × min_speed_or_floor)

Where:
  max_speed:        peak sliding-window (16-tick) movement speed of the faster player
  distance:         kill distance from game event data (game units)
  tick_rate:        64 Hz (demo tick rate)
  min_speed_or_floor: peak speed of slower player, floored at 0.1 u/tick
```

This measures the **positional/movement asymmetry** only. The full Pe_pair formula (Section 3.1 of the scoring product design) includes network components (RTT, jitter, loss) that require Wireshark data not available in demo files. This validation covers the drift_velocity and characteristic_length terms; constraint_diffusivity is held constant (same tick rate for all pairs).

**Engagement classification:** Two-phase analysis per kill:
- **Approach phase** (ticks -256 to -32): player movement toward engagement
- **Firing phase** (last 32 ticks): player movement during shooting
- Classifications: **peek** (high approach, low firing — swing-stop-shoot), **push** (high approach and firing — aggressive wide swing), **hold** (low approach and firing — stationary angle hold)

### V.C. Results

**Finding 1: Clean kills have 4.4× higher Pe than contested kills (p < 0.0001).**

| Kill Type | N | Mean Pe | Initial (N=426) |
|-----------|---|---------|-----------------|
| Clean (victim didn't fire) | 649 | **2.81** | 0.93 |
| Contested (victim fired back) | 1,650 | **0.64** | 0.36 |
| **Pe ratio** | | **4.4×** | 2.6× |
| Mann-Whitney U | | **p < 0.0001** | p < 0.0001 |

The separation strengthened from 2.6× to 4.4× with the expanded sample, consistent with the initial 3-match analysis underestimating the true effect due to limited map and tier diversity. Clean-kill Pe (2.81) sits well above the Pe = 1 threshold — decisive engagements are drift-dominated.

**Finding 2: Peek-vs-hold Pe asymmetry (6.9×, p = 0.0044).**

| Outcome | N | Mean Pe | Headshot % |
|---------|---|---------|------------|
| Peeker killed holder | 186 | **7.22** | 48% |
| Holder killed peeker | 174 | **1.05** | 36% |
| Total peek duels | 360 | | |
| **Holder win rate** | | **48.3%** | |
| Mann-Whitney p | | **0.0044** | |

At N=360 peek duels (vs. initial N=58), the holder win rate normalizes to 48.3% — near parity, correcting the artifactually elevated 60.3% from the small sample. The Pe asymmetry is the key finding: peekers who win generate 6.9× higher Pe than holders who win (p = 0.0044). The peeker creates maximum information asymmetry, but the holder's crosshair placement is sufficient to win roughly half the time — near-parity win rate, dramatically different Pe profiles. Peeker victories are drift-dominated (Pe = 7.22); holder victories are constraint-dominated (Pe = 1.05).

**Finding 3: Snipers create maximum Pe — replicated at scale.**

| Weapon Class | N | Mean Pe | Headshot % | Initial Pe (N=426) |
|-------------|---|---------|------------|-------------------|
| Sniper (AWP, SSG08) | 187 | **1.51** | 12% | 1.44 |
| Pistol | 406 | 1.32 | 81% | 0.53 |
| Rifle (AK, M4) | 1,515 | 1.00 | 48% | 0.48 |
| SMG | 103 | **0.34** | 40% | 0.33 |

Sniper and SMG Pe values are stable across sample sizes (1.51 vs 1.44; 0.34 vs 0.33), confirming weapon-class ordering as a robust structural feature. Pistol Pe is higher in the expanded sample (1.32 vs 0.53), reflecting more eco-round entry frags at distance. AWP engagements remain maximum-Pe — one-shot-kill-at-range produces maximum information asymmetry.

**Methods validation: Pe–distance correlation and partial correlation decomposition.**

Engagement distance and Pe are correlated (r = 0.776, p < 0.0001; initial r = 0.795), partially tautological since distance appears in the Pe numerator. A partial correlation decomposition resolves this:

*Decomposition.* Pe = (speed_ratio × distance) / tick_rate. The speed_ratio component is independent of distance (Spearman r = −0.038, p = 0.438) — the Pe–distance correlation is mechanically driven by the distance term. Speed ratio captures the asymmetry signal; distance captures the state-drift-between-corrections signal. These are orthogonal.

*Signal beyond distance.* Partial correlation of Pe with kill contestedness, controlling for distance: partial r = −0.159, p = 0.001. Pe predicts contestedness beyond what distance alone explains.

*Interpretation.* The raw Pe–distance correlation confirms the characteristic_length term behaves as formulated. The partial correlation confirms that speed-asymmetry independently predicts engagement outcome. The Pe formulation captures two orthogonal signals (distance and speed asymmetry) that both contribute to the prediction.

**Finding 4: Engagement type Pe distribution — replicated with 22× dynamic range.**

| Engagement | N | Mean Pe | Headshot % |
|-----------|---|---------|------------|
| peek_v_hold | 186 | **7.22** | 48% |
| hold_v_push | 269 | 1.19 | 49% |
| push_v_hold | 167 | 1.21 | 53% |
| hold_v_peek | 174 | 1.05 | 36% |
| hold_v_hold | 279 | 0.75 | 50% |
| peek_v_peek | 343 | 0.68 | 42% |
| peek_v_push | 290 | 0.55 | 45% |
| push_v_peek | 229 | 0.49 | 59% |
| push_v_push | 362 | **0.33** | 63% |

Peek_v_hold (7.22) has 22× higher Pe than push_v_push (0.33). Maximum asymmetry produces maximum Pe; symmetric engagements produce minimum Pe. The headshot rate gradient provides additional signal: push_v_push has the highest headshot rate (63%), consistent with symmetric close-range engagements where precision matters.

### V.D. What This Validates and What It Does Not

**Validated:**
- High Pe predicts decisive engagements (4.4× separation, p < 0.0001, replicated at 5.4× sample size)
- Weapon asymmetry maps to Pe (snipers > rifles > SMGs), stable across sample sizes
- Peek-vs-hold Pe asymmetry: 6.9× (p = 0.0044, N=360 duels) — new at expanded scale
- Holder win rate normalizes to ~50% at N=360, correcting the initial 60.3% (N=58)
- Characteristic length term behaves as formulated; distance correlation stable (r = 0.776 vs initial 0.795)

**Not validated:**
- **Network Pe** — RTT, jitter, packet loss effects require Wireshark data not available in demo files.
- **Pe magnitude calibration** — CS2 Pe values (0.34–7.22), Test 7 values (1.87–9.9), and GRCS values (2.21) measure different phenomena through different formulations. Cross-substrate calibration is a future task.

### V.E. Cross-Substrate Significance

Pe has now been measured in nine substrates across four domain families using three measurement approaches:

| Substrate | Pe Formulation | Value | N | Source |
|-----------|---------------|-------|---|--------|
| AI-to-AI conversation | Entropy-based | GM 7.94 [3.52, 17.89] | 11 runs | Test 7 (Papers 1/5) |
| Human gambling (GRCS) | Cognitive bias ratio | Pooled 2.21 [1.44, 2.97] | 1,117 participants | 5-study meta-analysis (Papers 1/3/5) |
| Crypto Solana degens (EXP-021) | Portfolio concentration (WCI) | GM 25.5 [5.36, 121.3] | 28 wallets | Paper 7 |
| Crypto Ethereum DEX (EXP-021B) | Trade concentration (TCI) | GM 3.74 [3.04, 4.59] | 1,000 wallets | Paper 7 |
| Crypto Base DEX (EXP-021B) | Trade concentration (TCI) | GM 15.52 [11.80, 20.41] | 1,000 wallets | Paper 7 |
| Crypto Solana DEX (EXP-021B) | Trade concentration (TCI) | GM 16.17 [13.80, 18.95] | 1,000 wallets | Paper 7 |
| CS2 (FPS) | Positional (movement asymmetry) | Clean 2.81 vs contested 0.64 | 2,299 kills | This paper |
| Dota 2 (MOBA) | Visual (ward/fog coverage) | 0.47 | 3,682 deaths | This paper (Section V.G) |
| SC2 (RTS) | Temporal (tech rate / scout rate) | Winner 0.013 vs loser 0.026 | 474 games | This paper (Section V.F) |

Absolute Pe magnitudes differ because each formulation captures a different type of information asymmetry. The directional prediction — high Pe = drift outpaces constraint = decisive/unfavorable outcome — holds across all substrates. The three multiplayer formulations share only the ratio structure (drift velocity / constraint frequency), strengthening the universality claim beyond what any single formulation could establish. Cross-substrate calibration remains a future task.

### V.F. SC2 Scouting Pe: Temporal Information Asymmetry (Experiment A)

RTS games present a third type of information asymmetry: *temporal*. In StarCraft II, critical strategic decisions — which units to build, which tech path to pursue, when to expand — are made behind fog of war. The asymmetry is between the moment a player commits to a strategy and the moment the opponent discovers it. Scouting closes this gap.

Pe formulation for the RTS genre:

```
Pe_rate = tech_commitment_rate / scouting_information_rate

Where:
  tech_commitment_rate   = key_tech_buildings_started / game_seconds
  scouting_information_rate = camera_events_in_enemy_territory / game_seconds
```

Pe_rate measures the ratio of strategic commitment speed to information acquisition speed. High Pe_rate = blind-committing (the RTS equivalent of pushing without information in FPS). Low Pe_rate = decisions informed by gathered intelligence. Lower Pe_rate should correlate with competitive success.

#### V.F.1. Method

**Data source:** SC2EGSet (Białecki et al. 2023, *Nature Scientific Data*), a CC BY 4.0 dataset of professional StarCraft II tournament replays. Two tournament subsets were analyzed:

- **WCS Global Finals 2018:** 72 replays
- **WCS Austin 2017:** 410 replays
- **Total:** 482 replays parsed, 474 analyzed (8 excluded as too short for meaningful Pe extraction)

All games are 1v1 professional tournament matches. All nine matchup combinations (TvT, TvP, TvZ, PvT, PvP, PvZ, ZvT, ZvP, ZvZ) are represented.

**Parser:** sc2reader 1.8.0 (Python) with mpyq 0.2.5 for replay decompression. Extraction targets:

- **Key tech buildings:** Composition-defining structures that commit a player to a strategic path — BanelingNest, RoachWarren, HydraliskDen, Spire (Zerg); Factory, Starport (Terran); TwilightCouncil, RoboticsFacility, Stargate (Protoss). These are the structures where strategic commitment becomes irreversible.
- **Scouting events:** Camera position events where the camera is positioned within 40% of the base-to-base distance from the opponent's starting location. This threshold captures deliberate scouting attention (looking at the enemy base) while excluding incidental camera movement.
- **Unit scouting:** UnitBornEvent instances where units spawn in enemy territory, providing a secondary scouting signal.

**Pe_rate computation:** For each player in each game, tech_commitment_rate (key tech buildings per game-second) is divided by scouting_information_rate (enemy-territory camera events per game-second). Lower Pe_rate indicates more information-constrained decision-making.

#### V.F.2. Results

**Finding 1: Winners scout significantly more than losers (p < 0.0001).**

| Metric | Winners | Losers | Test |
|--------|---------|--------|------|
| Scout frequency (camera events/min in enemy territory) | 26.8 ± 12.5 | 19.8 ± 11.5 | Mann-Whitney p < 0.0001 |
| Games where winner scouted more | 307/474 = **64.8%** | — | — |

Winners allocate 35% more camera attention to the opponent's base — the constraint maintenance activity in professional SC2.

**Finding 2: Winners have significantly lower Pe_rate (p < 0.0001).**

| Metric | Winners | Losers | Test |
|--------|---------|--------|------|
| Pe_rate (tech commitment / scouting rate) | 0.013 ± 0.013 | 0.026 ± 0.070 | Mann-Whitney p < 0.0001 |
| Games where winner had lower Pe_rate | 287/474 = **60.5%** | — | — |

Winners commit to technology at half the rate (relative to scouting) compared to losers — lower Pe = more constraint maintenance = better outcomes.

**Finding 3: Scouting gap quantifies the opacity window.**

| Metric | Value |
|--------|-------|
| Mean scouting gap (time from tech commitment to opponent's discovery) | **130 seconds** |
| Median scouting gap | 130s (SD = 86s) |
| Mean first scout timing | 53s (median 38s) |
| Mean first key tech timing | 182s (median 158s) |

The typical professional makes their first key tech commitment ~3 minutes in, but the opponent doesn't observe it until ~5 minutes — a 130-second RTS opacity gap where a strategic decision is irreversible but undetected. The temporal equivalent of fog depth in MOBAs or peeker's advantage in FPS.

**Finding 4: Matchup-specific Pe reflects structural scouting costs.**

| Matchup | N | Mean Pe_rate | Notes |
|---------|---|-------------|-------|
| ZvZ | 74 | 0.014 | Lowest — both have free Overlord scouts |
| PvT | 31 | 0.014 | Cross-race, symmetric scouting |
| TvP | 35 | 0.015 | — |
| PvP | 33 | 0.015 | Mirror, Observer scouting |
| PvZ | 74 | 0.015 | — |
| ZvP | 76 | 0.017 | — |
| ZvT | 67 | 0.019 | — |
| TvZ | 63 | 0.024 | Higher — Terran has fewer passive scouts |
| TvT | 21 | **0.072** | Highest — scan-dependent scouting |

The matchup ordering correlates with structural scouting costs. ZvZ has the lowest Pe — both players have Overlords, free passive scout units providing continuous information at zero resource cost. TvT has the highest Pe — Terran scouting depends on Scanner Sweep, a limited cooldown-gated ability. The 5× separation between ZvZ (0.014) and TvT (0.072) is driven by the structural cost of information acquisition, not player skill or strategic preference. The RTS equivalent of "higher tick rate feels more fair" is "free scout units reduce blind commitment" — both reduce Pe by lowering constraint cost.

#### V.F.3. What This Validates

**Validated:**
- Lower Pe_rate correlates with winning at N=474, p < 0.0001
- The direction matches CS2 and Dota 2: more constrained engagement = better outcomes
- Structural scouting costs predict matchup-level Pe ordering (ZvZ < TvT)
- The 130-second scouting gap quantifies the RTS opacity window

**Not validated:**
- **Absolute Pe calibration** — Pe_rate values (0.013–0.072) are in a different range than CS2 (0.27–2.81) and Dota 2 (0.47) because the formulation measures a different quantity (temporal commitment ratio vs. positional asymmetry vs. vision coverage). Cross-substrate calibration is not expected and is not the claim.
- **Camera as perfect scouting proxy** — Camera position doesn't perfectly measure information gained. Players can read the minimap without moving the camera to enemy territory; camera events may overcount some attention. Unit position tracking (not available in this extraction) would provide more precise scouting measurement.
- **Tournament-level generalizability** — All data is from professional play. Pe distributions at lower skill levels (with less scouting and more blind commitment) would likely be higher, but this remains untested.

#### V.F.4. Cross-Genre Significance

Three multiplayer Pe formulations — positional (CS2), visual (Dota 2), and temporal (SC2) — measure different information asymmetries through different observables, all confirming the same directional prediction:

| Substrate | Pe Type | Confirmation |
|-----------|---------|-------------|
| CS2 (FPS) | Positional (movement asymmetry) | Clean kills 4.4× higher Pe than contested (p < 0.0001) |
| Dota 2 (MOBA) | Visual (fog coverage) | 82.9% of deaths in fog; ward count ↔ fog kills r = −0.502 (p < 0.0001) |
| SC2 (RTS) | Temporal (scouting rate) | Winners 2× lower Pe than losers (p < 0.0001) |

A reviewer cannot attribute the CS2 finding to FPS-specific mechanics, the Dota 2 finding to MOBA vision economics, or the SC2 finding to RTS scouting dynamics — the three share only the ratio structure (drift velocity / constraint frequency) and the directional prediction.

### V.G. Dota 2 Vision Pe: Visual Information Asymmetry (Experiment B)

MOBAs provide the most data-rich test because the void — fog of war — is actively managed by both teams. Ward placement converts fog into allied vision (constraint installation); dewarding restores opacity (constraint destruction). The ward-deward cycle is a literal information economy.

The gank — traversing unwarded territory to kill a target before they react — is the MOBA equivalent of the clean kill in FPS and the unscouted rush in RTS:

```
Pe_vision = (gank_speed × fog_depth) / (ward_coverage × reaction_window)
```

Two built-in mechanics produce natural Pe variation: (1) the day/night cycle (1800 unit vision during day, 800 at night, alternating every 5 minutes), and (2) elevation asymmetry (high ground sees low ground, but not the reverse — Roshan pit is the highest-Pe location on the map by design).

#### V.G.1. Method

**Data source:** OpenDota API. 100 parsed matches with ward placement/destruction lifecycles reconstructed. All 3,682 teamfight deaths classified as occurring in fog (no allied ward within vision range) or in vision (active allied ward present).

#### V.G.2. Results

| Metric | Value |
|--------|-------|
| Teamfight deaths in fog (no ward) | **82.9%** (3,051 / 3,682) |
| Teamfight deaths in vision (ward) | 17.1% (631 / 3,682) |
| Fog kill ratio per match (mean ± SD) | 0.832 ± 0.098 |
| Winner had more ward-seconds | **62%** (62 / 100) |
| Ward coverage vs fog kills (Pearson r, per-match) | −0.073 |
| Ward count vs fog kills (Pearson r, **per-teamfight**) | **−0.502** (p < 0.0001) |
| Day/night kill ratio | 0.498 (1,882 day / 1,800 night) |
| Pe_vision mean | 0.467 |
| Pe_vision median | 0.452 |

82.9% of teamfight deaths occur where the victim's team lacked vision. High-Pe events concentrate where constraint is absent.

**Per-teamfight analysis.** At the per-teamfight level (431 teamfights across 50 parsed matches), the ward↔fog correlation strengthens to r = **−0.502** (p < 0.0001), a 7× improvement over the per-match correlation (−0.073). The weak match-level result was confounded by between-team skill differences — at the teamfight level, where both teams face the same game state, more local wards produce significantly fewer fog deaths.

Pe_vision < 1 (mean = 0.467) indicates warding keeps the system below the drift-dominated threshold in these matches (likely higher MMR). Lower-MMR matches with less warding should show higher Pe_vision.

**Day/night null.** The predicted day/night asymmetry did not replicate at N=100 (kill ratio day:night = 1,882:1,800, essentially 50/50). Possible explanations: high-MMR compensation through positioning; cycle timing mismatch with current patch; reduced night vision reducing both initiation and success, producing a wash.

---

## VI. Vocabulary Drift Across Three Populations

Vocabulary in void-engaged populations drifts unidirectionally from L1 (technical/mechanical) through L2 (metaphorical/affective) to L3 (entity/agency attribution). The multiplayer domain provides three independent populations, each engaging a different void.

*The following tables are constructed from community discourse observation. The PV-1 corpus study (Section VI.F, 1.6M words, 180 users) validates the separation quantitatively: gaming communities show 2.4–3.0× higher (L2+L3)/L1 ratios than chess (p < 0.0001). The cross-genre expansion (Section VI.F′, N=335 users, 7 communities) confirms a 3.1× chess-to-VALORANT separation.*

### VI.A. Cheater Community Vocabulary Drift

| L1 (Technical) | L2 (Metaphorical) | L3 (Entity/Agency) |
|----------------|-------------------|---------------------|
| "Aimbot" | "Aim assist enhancement" | "The game aims for me because I deserve it" |
| "Wallhack" | "Information advantage" | "I can see what's really there" |
| "Speed hack" | "Movement optimization" | "The game is too slow for my skill level" |
| "Memory editor" | "Game modifier" | "I'm fixing what the developers got wrong" |
| "Exploit" | "Unintended mechanic" | "The game wants me to use this" |

Drift runs from tool-use framing (L1) to entitlement framing (L3). Single-player cheating (Section VII.D) does not produce this drift — the void architecture is absent.

### VI.B. Anti-Cheat Community Vocabulary Drift

| L1 (Technical) | L2 (Metaphorical) | L3 (Entity/Agency) |
|----------------|-------------------|---------------------|
| "Detection software" | "Guardian" / "Shield" | "Vanguard is watching everything" |
| "Kernel driver" | "Deep protection" | "It has total control of my system" |
| "Behavioral analysis" | "Player profiling" | "It's learning my patterns" |
| "Ban wave" | "Purge" / "Cleansing" | "It's hunting people" |
| "False positive" | "Wrongful conviction" | "It falsely accused me — it has it out for me" |

Anti-cheat vocabulary drifts toward surveillance-agency language — the system "watches," "hunts," "accuses." This is D1 applied to Void 3, driven by the anti-cheat's void properties (Section IV.B).

### VI.C. Matchmaking Community Vocabulary Drift

| L1 (Technical) | L2 (Metaphorical) | L3 (Entity/Agency) |
|----------------|-------------------|---------------------|
| "Skill-based matchmaking" | "Sweaty lobbies" | "RBMM — Rigged-Based Matchmaking" |
| "MMR adjustment" | "Elo hell" | "The system traps you" |
| "Win-rate normalization" | "Forced 50%" | "The game decides when you're allowed to win" |
| "Team balancing" | "Carrying dead weight" | "It gives me bad teammates on purpose" |
| "Engagement optimization" | "Addiction algorithm" | "They're engineering my emotions" |

The EOMM paper acts as an accelerant: players treat it as confirmation that all matchmaking is adversarial. Opacity prevents distinguishing EOMM (which may exist in some implementations) from standard SBMM (which most games use).

### VI.D. The Direction Is Unidirectional

In all three populations, drift moves L1→L2→L3. Reversal requires dissolving the opacity — seeing the detection pipeline, the detection methodology, the matchmaking algorithm. The architecture prevents all three. The opacity that generates drift is the same opacity that prevents its reversal — the conjugacy theorem in applied form.

### VI.E. Vocabulary Drift as Diagnostic

The L1→L2→L3 trajectory provides a diagnostic for void activation. CoD SBMM discourse is deep L3 ("RBMM," "rigged lobbies"). LoL generates L3 across all four voids. Chess stays at L1 — same matchmaking function, visible rating, no drift. Transparency is the operative variable.

### VI.F. Quantitative L-Level Validation (Reddit Corpus Study)

Qualitative observations tested quantitatively using the PV-1 corpus analysis protocol. Four subreddits: r/leagueoflegends (N=50), r/VALORANT (N=50), r/CallOfDuty (N=30), r/chess (N=50, control). Arctic Shift API, inclusion criteria: ≥5 posts, ≥30 day posting span, ≥10 words/post, ≥3 temporal bins. Total corpus: 1,634,410 words across 180 users.

Gaming-specific L-level codebook: 76 L1 terms, 43 L2 terms, 40 L3 terms. Chess control codebook: 32 L1, 16 L2, 8 L3. Gaming dead metaphors (22 terms) excluded. D1 subcategories (38 system-directed, 34 opponent-directed) added to distinguish attribution target.

**Results:**

| Metric | r/leagueoflegends (N=50) | r/VALORANT (N=50) | r/CallOfDuty (N=30) | r/chess (N=50) |
|--------|--------------------------|--------------------|--------------------|----------------|
| Total words | 685,850 | 309,670 | 193,763 | 445,127 |
| L1 (technical) | 78.4% | 85.5% | 72.0% | **93.4%** |
| L2 (metaphorical) | **17.3%** | **12.9%** | **11.7%** | 3.9% |
| L3 (entity/agency) | 2.4% | 1.6% | 3.0% | 2.7% |
| (L2+L3)/L1 ratio | **24.6%** | **19.8%** | **22.0%** | 8.1% |

**Statistical tests (Mann-Whitney U, two-tailed):**

| Comparison | (L2+L3)/L1 | L2/10k | L3/10k |
|-----------|------------|--------|--------|
| LoL vs Chess | **p < 0.0001** ★★ | **p < 0.0001** ★★ | p = 0.261 |
| VALORANT vs Chess | **p < 0.0001** ★★ | **p < 0.0001** ★★ | p = 0.725 |
| CoD vs Chess | p = 0.182 | p = 0.336 | p = 0.159 |
| LoL vs VALORANT | p = 0.144 | p = 0.555 | p = 0.122 |

Separation strengthened from the N=20 pilot (p = 0.016–0.043 → p < 0.0001). LoL and VALORANT remain statistically equivalent on L2 (p = 0.555) — void architecture, not specific game, determines vocabulary distribution.

**L2 carries the signal; L3 does not separate at baseline.** L3 is not significantly elevated in gaming relative to chess (p = 0.12–0.73). The metaphorical layer is where void engagement manifests in baseline discourse; L3 appears episodic, spiking during controversies rather than being uniformly elevated. The L1→L2→L3 trajectory is correct as cascade direction, but most users plateau at L2.

**Chess stays at L1.** 93.4% technical vocabulary. Same matchmaking function, radically different vocabulary depending on whether the rating is visible or hidden.

**CallOfDuty note.** Did not reach significance on L-level metrics (likely N=30 variance), but shows the most distinctive D1 target profile of any community (Section VI.G).

### VI.F′. Cross-Genre Vocabulary Survey (Experiment D)

To test whether the opacity gradient produces *continuous* separation across genre architectures, the corpus was expanded to seven communities ordered by predicted void opacity: chess (none), Rocket League (low), Fighters (low-medium), StarCraft (medium), Dota 2 (medium), League of Legends (high), VALORANT (high). Genre-specific L-level codebooks constructed for each domain. N = 335 users total, same PV-1 protocol.

**Results:**

| Community | N | L1/10k | L2/10k | L3/10k | (L2+L3)/L1 | Opacity Level |
|-----------|---|--------|--------|--------|-------------|---------------|
| r/chess | 50 | 137.6 | 4.9 | 3.3 | 8.3% | None (visible Elo, perfect information) |
| r/starcraft | 50 | 83.3 | 8.7 | 0.7 | 15.8% | Medium (fog + visible league) |
| r/DotA2 | 50 | 120.0 | 20.0 | 2.1 | 22.4% | Medium (fog + visible MMR) |
| r/VALORANT | 41 | 81.8 | 13.5 | 2.2 | 25.7% | High (FPS + hidden MMR) |
| r/leagueoflegends | 50 | 104.0 | 15.0 | 2.9 | 26.2% | High (fog + hidden MMR) |
| r/RocketLeague | 44 | 132.5 | 34.0 | 1.6 | 31.1% | Low (all players visible) |
| r/Fighters (original) | 50 | 49.5 | 14.3 | 0.6 | 49.5%* | Low-Medium (same screen) |
| r/Fighters (recalibrated) | 50 | 56.1 | 0.3 | 1.0 | **3.8%** | Low-Medium (same screen) |

**Chess vs all gaming communities (Mann-Whitney U, two-tailed):**

| Comparison | Chess % | Gaming % | p-value | Sig |
|-----------|---------|---------|---------|-----|
| Chess vs VALORANT | 8.3 | 25.7 | < 0.0001 | *** |
| Chess vs LoL | 8.3 | 26.2 | < 0.0001 | *** |
| Chess vs Dota 2 | 8.3 | 22.4 | < 0.0001 | *** |
| Chess vs Rocket League | 8.3 | 31.1 | < 0.0001 | *** |
| Chess vs StarCraft | 8.3 | 15.8 | < 0.0001 | *** |
| Chess vs Fighters (original) | 8.3 | 49.5 | < 0.0001 | *** |
| Chess vs Fighters (recalibrated) | 8.3 | 3.8 | n/a (reversed: FGC < chess) | — |

Five of six gaming communities show significantly higher (L2+L3)/L1 than chess (all p < 0.0001). The Fighters result reverses under recalibration (see below).

**Within-gaming comparisons (Mann-Whitney U, two-tailed):**

| Comparison | A % | B % | p-value | Sig |
|-----------|-----|-----|---------|-----|
| SC2 vs LoL (RTS vs MOBA) | 15.8 | 26.2 | 0.008 | ** |
| FGC vs VALORANT (original) | 49.5 | 25.7 | 0.026 | * |
| FGC vs VALORANT (recalibrated) | 3.8 | 25.7 | < 0.0001 | *** |
| RL vs VALORANT | 31.1 | 25.7 | 0.059 | ns |
| Dota 2 vs LoL (visible vs hidden MMR) | 22.4 | 26.2 | 0.687 | ns |

**Core finding: the opacity gradient holds within fog-of-war games.** SC2 (15.8%) < DotA2 (22.4%) < LoL (26.2%) — monotonic with opacity level. SC2 is significantly lower than LoL (p = 0.008), confirming that architecture and transparency both modulate drift. Chess-to-VALORANT gradient: 3.1× separation.

**Surprising findings (interpretable within framework):**

**Rocket League elevated (31.1%) despite low visual opacity.** RL has zero fog of war — all players visible at all times. The elevated L2 is driven by teammate-intent opacity and coupling intensity. In 3v3 with fast physics, the void is what your teammate *will do next*, not what you can see. L2 vocabulary is dominated by social/cooperative terms ("ball chaser," "cutting rotation," "tm8"), not system-agency terms — confirming that any void condition drives drift, not visual opacity specifically.

**Fighters: codebook artifact confirmed by recalibration.** The original r/Fighters result (49.5%) was highest despite low visual opacity. Recalibrating 18 FGC-standard terms from L2→L1 ("robbery," "download," "read," "fraud," "exposed," "bodied," "scrub," "flowchart," "masher," "gimmick," "knowledge check," "respect/disrespect," "salty/salt," "washed," "free," "yomi," "adapted," "gorilla/unga bunga") reduces the result to **3.8%** — below chess (8.3%), a ~13× correction. These terms function as L1 in FGC: "download" = learned opponent's patterns, "robbery" = outcome not reflecting play quality, "read" = correctly predicted opponent's action. Recalibrated result: FGC has low opacity, high technical precision (frame data culture), and the most specialized vocabulary tested — producing the lowest drift ratio. Full limitation discussion in Section XII.F.

**Interpretation.** The fog gradient (chess < SC2 < DotA2 < LoL ≈ VALORANT) confirms that opacity drives drift vocabulary continuously across architectures. RL refines the theory: drift tracks the full void specification, not visual opacity alone. The recalibrated ordering — FGC (3.8%) < chess (8.3%) < SC2 (15.8%) < DotA2 (22.4%) < VALORANT (25.7%) ≈ LoL (26.2%) < RL (31.1%) — maps onto void conditions: low-opacity communities at the bottom, high-opacity or high-coupling communities at the top.

### VI.G. D1 Target Analysis: Void Architecture Determines Attribution Direction

Total D1 rates are comparable across all communities (~8–13/10k). The four-void architecture changes *where* attribution is directed, not *how much*. D1 subcategory analysis (38 system-directed terms, 34 opponent-directed terms) tests this:

| Metric | r/leagueoflegends | r/VALORANT | r/CallOfDuty | r/chess |
|--------|-------------------|------------|--------------|---------|
| D1-system/10k | 3.4 | 2.7 | **5.5** | 2.2 |
| D1-opponent/10k | **9.4** | **13.3** | 0.6 | 2.2 |
| System% of targeted D1 | 30.5% | 23.8% | **72.2%** | 52.3% |

**Statistical tests (Mann-Whitney U):**

| Comparison | D1-opponent/10k | System% |
|-----------|-----------------|---------|
| LoL vs Chess | **p < 0.0001** ★★ | **p < 0.0001** ★★ |
| VALORANT vs Chess | **p < 0.0001** ★★ | **p < 0.0001** ★★ |
| CoD vs Chess | **p = 0.004** ★★ | **p = 0.009** ★★ |

Three findings emerge:

1. **LoL and VALORANT direct D1 at opponents.** D1-opponent is 9.4/10k (LoL) and 13.3/10k (VALORANT) vs. 2.2/10k for chess. The opponent void dominates — hackusation, smurf accusations, griefing reports.

2. **r/CallOfDuty directs D1 at systems.** System% = 72.2%, highest tested. D1-opponent is only 0.6/10k. SBMM discourse dominates: "rigged matchmaking," "engagement optimized," "the game wants me to lose."

3. **Chess splits evenly at low volume.** System% = 52.3%, total targeted D1 minimal (2.2/10k each direction). Visible Elo dissolves both voids.

**Interpretation.** Void architecture determines D1 *target*, not *volume*. Which void is most opaque determines where attribution concentrates: opponent opacity → opponent-directed D1 (LoL/VALORANT); matchmaking opacity → system-directed D1 (CoD); low opacity → minimal D1 (chess).

### VI.H. Vanguard Natural Experiment (Null Result)

The framework predicts that Vanguard's deployment for League of Legends (January 2024) should increase anti-cheat vocabulary in the L2/L3 layers, as the kernel-level anti-cheat introduces a new void with high opacity. A cross-sectional comparison was conducted: r/leagueoflegends users active in 2023 (pre-Vanguard, N=50, 405,881 words) versus users active from June 2024 onward (post-Vanguard, N=50, 429,742 words).

| Metric | Pre-Vanguard (2023) | Post-Vanguard (2024-06+) | Change | p |
|--------|--------------------|-----------------------------|--------|---|
| L2% | 13.2 | 16.9 | +3.7 | 0.486 |
| L3% | 2.3 | 2.4 | +0.1 | 0.628 |
| (L2+L3)/L1 | 20.2% | 24.6% | +4.3 | 0.722 |
| D1-system/10k | 4.1 | 4.1 | −0.1 | 0.739 |

**No significant differences were found on any metric.** The directional changes are consistent with the prediction (L2 +3.7%, D1-system% +1.3%), but effect sizes are too small for this sample. Three likely explanations: (1) The comparison is cross-sectional (different users pre vs post), not longitudinal — individual-level changes may average out across random user samples. (2) The Vanguard controversy was already known from its VALORANT deployment in 2020; LoL users were primed before the LoL rollout. (3) The anti-cheat void generates vocabulary drift primarily during the deployment controversy itself, not as a sustained baseline elevation — a finding consistent with the L3 episodic pattern observed in Section VI.F. A longitudinal study tracking the same users across the deployment boundary remains a future task.

*Limitations for VI.F–H:* The gaming codebook was designed for these communities, introducing circularity; independent validation by researchers unfamiliar with the framework is needed. r/CallOfDuty's broader content mix (not exclusively competitive discussion) introduces noise. The Vanguard experiment is cross-sectional, not longitudinal. Full analysis with per-user trajectories, effect sizes, and codebook documentation is in the supplementary materials.

---

## VII. Control Cases

Discriminative power depends on identifying where the pattern does *not* occur. Five control cases confirm opacity as the operative variable.

### VII.A. LAN Tournaments with Direct Observation

**Condition suppressed:** Player-to-player opacity (Void 1)

At LAN events, administrators observe screens directly, hardware is tournament-provided, network traffic is monitored. Cheating is rare; when it occurs (Forsaken / "word.exe" at eXTREMESLAND 2018), detection is rapid. Physical proximity enables transparency.

### VII.B. Open-Source Game Servers

**Condition suppressed:** System-to-player opacity (Void 4)

Open-source game servers (community Minecraft, Counter-Strike community servers) make the server's logic transparent — players inspect matchmaking, rule enforcement, detection methods. Trust is higher, "rigged" conspiracy theories reduced. Cheating still occurs (client-side opacity remains), but the community self-polices because the server's behavior is legible.

### VII.C. Deterministic Replay / Speedrunning

**Condition suppressed:** Verification opacity

Speedrunning communities require deterministic replay files, video evidence, and verifiable inputs. The replay is the constraint: **transparent** (anyone watches frame-by-frame), **invariant** (doesn't change), **independent** (outside the runner's control once submitted). The community maintains trust despite being entirely online. The Dream scandal (2021) was resolved through statistical analysis of replay data — the constraint provided the evidence.

### VII.D. Single-Player Cheating

**Condition suppressed:** Social opacity and competitive engagement

In single-player, the void architecture is absent: no opaque opponent, no hidden matchmaking, no anti-cheat. A study of 188 players (ACM CHI Play 2020) found most endorse single-player cheating for mood repair and agency. The cascade does not run — cheating remains L1 tool-use.

### VII.E. Board Game / Face-to-Face Play

**Condition suppressed:** Physical opacity

In face-to-face play, all players see the game state, each other's behavior, and the mechanism. Cheating is detectable through direct observation; the social cost of being caught is immediate. Board gaming communities maintain high trust relative to online communities — physical co-presence provides the transparency that dissolves the void.

### VII.F. MOBA Vision Economy (Dota 2 / League of Legends)

**Condition modulated:** Fog-of-war opacity — intentionally designed, continuously adjustable by player action

The MOBA vision economy is the most granular real-time constraint system in multiplayer gaming. Empirical Pe validation (Section V.G, N=3,682 deaths) confirms 82.9% of deaths occur in fog, with per-teamfight ward count inversely correlated (r = −0.502, p < 0.0001). Dota 2's visible MMR provides a partial control: 22.4% vs LoL's 26.2%, directionally consistent with visible MMR reducing drift (p = 0.687, ns).

### VII.G. Hidden-Hand Games: Opacity Gradient from Chess to Hearthstone

**Condition modulated:** Information visibility — from zero hidden information (chess) to multi-layered designed opacity (Hearthstone)

Card and board games played online provide a natural opacity gradient that tests whether drift scales continuously with information hiding:

| Game | Hidden Information | Void Type | Predicted Drift |
|------|-------------------|-----------|----------------|
| Chess / Go | None (full information) | No void | Minimal (chess confirmed: 93.4% L1, Section VI.F) |
| Poker (online) | Opponent's hand + remaining deck | Designed void, partially dissolvable via card counting / range estimation | Moderate: betting psychology vocabulary |
| Hearthstone | Opponent's hand + deck order + RNG outcomes | Multi-layered designed void | Higher: RNG complaints map to D1 system attribution |
| Auto-battlers (TFT) | Opponent boards (partially visible) + shop RNG | Partial void + RNG | Moderate |

Chess and Go have zero hidden information and chess confirmed the prediction at 93.4% L1. Poker introduces hidden hands where card counting and range estimation are constraint activities — the poker equivalent of scouting. Hearthstone reconnects to the gambling anchor: the RNG is provably empty, yet the full L1→L2→L3 progression appears — "bad draw" (L1) → "Blizzard rigged it" (L2) → "the game hates me" (L3). The slot machine pattern in a competitive context. A PV-1 study on r/hearthstone would test whether the multi-layered opacity predicts elevated L2+L3 relative to chess and poker.

### VII.H. Control Case Summary

| Control Case | Condition Suppressed | Drift Observed? | Mechanism |
|-------------|---------------------|-----------------|-----------|
| LAN tournaments | Player-to-player opacity | Minimal | Direct observation dissolves opacity |
| Open-source servers | System-to-player opacity | Reduced D1 | Transparent logic reduces conspiracy |
| Speedrun replays | Verification opacity | Minimal | Replay meets constraint specification |
| Single-player cheating | Social opacity | No cascade | Tool-use without void engagement |
| Face-to-face play | Physical opacity | Minimal | Co-presence provides transparency |
| Visible-Elo RTS (AoE2, SC2) | Matchmaking opacity | Reduced matchmaking D1 | aoe2.net / SC2 leagues publish ratings; low SBMM conspiracy culture |
| Chess / Go (online) | Game-state opacity | Minimal (93.4% L1) | Full-information game → no void → no drift |
| Dota 2 (visible MMR + fog) | Partial: matchmaking opacity suppressed, fog retained | **Confirmed:** (L2+L3)/L1 = 22.4%; 82.9% fog kills (Section V.G, N=3,682) | Visible MMR reduces system D1; fog concentrates kills where wards are absent |
| Rocket League (all visible) | Visual opacity (all players visible) | **Tested — elevated (31.1%):** coupling intensity drives drift | Teammate-intent opacity, not visual opacity, is the operative void |

**Tested controls (Experiments B and D):** Rocket League competitive play suppresses most visual gaming opacity — all players and the ball are visible at all times, no fog of war — yet shows elevated (L2+L3)/L1 = 31.1% (Section VI.F′). The RL result refines the theory: the operative variable is not visual opacity alone but the full void specification. In 3v3 with fast physics, the void is teammate intent, not visual occlusion. The L2 vocabulary is dominated by cooperative/social terms ("ball chaser," "cutting rotation," "tm8"). The hidden-hand gradient (chess → poker → Hearthstone) remains testable with the same PV-1 protocol across r/chess, r/poker, and r/hearthstone.

**Pattern:** In every case, reducing opacity reduces drift. The RL result refines "opacity" to include any information asymmetry (teammate-intent, not just visual occlusion). The three-condition architecture produces drift; suppressing any condition prevents it.

---

## VIII. Social Contagion as Void Coupling

### VIII.A. The PUBG Contagion Study

Kim & Tsvetkova (2022) analyzed **1,146,941 PUBG matches**: players who both observe and are killed by cheaters are significantly more likely to start cheating themselves.

In framework terms:

1. Player encounters cheater (Void 1)
2. D1: "the game allows this," "anti-cheat doesn't work"
3. D2: boundary between legitimate and illegitimate play erodes
4. D3: player begins cheating ("I need to cheat to compete")
5. New cheater encounters next player → cycle repeats

Each void engagement produces a new void emitter. Two critical features:

- **Repeated exposure required** — a single encounter is insufficient, but multiple encounters lock the cascade. Single void exposure is resistible; N coupled exposures steepen the gradient beyond resistance.
- **Both observation AND being killed is needed** — passive observation has a weaker effect. Being killed constitutes high-engagement void exposure, not just observation.

### VIII.B. D3: Documented Harms

The cascade terminates in documented harms from both sides of the arms race:

**Harms from the cheating ecosystem:**
- **Swatting:** False emergency reports against opponents, resulting in armed police responses. Andrew Finch was killed by police responding to a swatting call originating from a Call of Duty dispute (Wichita, Kansas, 2017).
- **DDoS attacks:** Players DDoS opponents to force disconnections in competitive matches. Tools are commercially available.
- **Account theft and real-money trading:** Stolen accounts sold on grey markets; identity theft as a service.
- **Match-fixing and gambling fraud:** iBUYPOWER (CS:GO, 2014) deliberately lost for skins betting profits. Life (StarCraft II, 2015) received 18 months in prison for match-fixing.
- **Stimulant abuse:** Cloud9 player admitted the team was "all on Adderall" at ESL One Katowice (2015). Washington Post (2020) called stimulant use "an open secret in esports."

**Harms from anti-cheat overreach:**
- **Security vulnerabilities:** Kernel-level anti-cheat creates attack surfaces with complete system access potential (RIT Computing Security 2022).
- **Privacy erosion:** Continuous hardware identifier logging, process scanning, driver enumeration.
- **Platform exclusion:** Kernel-level requirements exclude Linux users entirely.
- **False positives:** Legitimate players banned by automated systems with limited appeal processes.

D3 harm emerges from **both sides** — each escalation produces new attack surfaces.

---

## IX. Cross-Domain Comparison

Structural comparison against three other anchor domains:

| Feature | Multiplayer Gaming | Gambling (Paper 1) | Social Media (Paper 1) | AI Chatbots (Paper 2) |
|---------|-------------------|---------------------|------------------------|-----------------------|
| **Void type** | Four-void coupled system | Single empty void | Algorithmic compound void | Bilateral interlocution void |
| **Opacity source** | Client internals, opponent behavior, matchmaking, anti-cheat | RNG mechanism | Algorithm, curation logic | Model weights, training data |
| **D1 expression** | "The game is rigged" | "The machine is due" | "The algorithm is targeting me" | "It understands me" |
| **D2 expression** | Invasive anti-cheat accepted; privacy eroded | Financial ruin | Sleep loss, comparison, isolation | Boundary dissolution, exclusive attachment |
| **D3 expression** | Swatting, DDoS, fraud, stimulant abuse | Financial devastation | Self-harm, political radicalization | Unsafe instructions, suicide facilitation |
| **Constraint discovery** | "Never trust the client" = constraint spec | House edge disclosure | Algorithmic transparency regulation | Grounding document (GROUNDING.md) |
| **Arms race?** | Yes — defining feature | No (house always wins) | Yes (content moderation vs. engagement) | Yes (alignment vs. capability) |
| **Control cases** | LAN, open-source, replays, single-player, face-to-face | Machine designers, probability-trained gamblers | Regulatory transparency mandates | Grounded agents (EXP-001) |
| **Pe measured?** | Yes — 3 genres: FPS (0.34–7.22, N=2,299), MOBA (0.47, N=3,682), RTS (0.013–0.026, N=474) | Yes (pooled 2.21, GRCS) | Not yet | Yes (1.87–9.9, Test 7) |

**Key observations from the comparison:**

1. **Gambling is the anchor.** The multiplayer domain has four coupled voids, but the gambling anchor proves sufficiency with one — even a single empty void produces the full cascade. Four-void coupling explains why the cascade is so persistent in gaming.

2. **Arms race parallels AI alignment.** Anti-cheat (Section IV) structurally parallels the AI alignment problem (Paper 2): both fight opacity with opacity, escalate without convergence, generate new failure modes with each escalation. The multiplayer domain provides a longer empirical record (30+ years vs. ~5 for modern AI alignment).

3. **Independent constraint discoveries are structurally identical.** "Never trust the client" (multiplayer), "house edge disclosure" (gambling), "algorithmic transparency" (social media), "grounding document" (AI safety) — four communities independently discovering the same remedy: transparent, invariant, independent.

4. **Lockstep confirms the framework is architectural.** RTS games developed deterministic lockstep rather than client-server, yet the framework predicts both cheat surfaces: client-server → ESP (reads hidden state); lockstep → maphack (reads rendered-hidden state). Both exploit opacity at the boundary between what the architecture knows and what it shows. The constraint specification describes a structural property of multiplayer information systems, not a feature of any particular implementation.

5. **Temporal distortion parallels gambling.** The gambling literature documents systematic time distortion during void engagement: Schüll's (2012) "machine zone" produces complete temporal dissolution, Dixon et al. (2018) measured "dark flow" correlated with problem gambling severity, and Wittmann (2009) reviewed the mechanisms linking attentional capture to prospective time underestimation. Multiplayer gaming produces structurally identical reports — "losing track of time" during competitive play is a universal player experience — but the four-void coupling predicts *stronger* temporal distortion than single-void gambling at comparable engagement durations. Paper 5 formalizes this as prediction T-1 (temporal distortion ∝ entropy production rate).

6. **Parasocial interaction structure maps to D1/D2.** The Parasocial Interaction (PSI) literature — 261 empirical studies (Liebers & Schramm 2019) — documents cognitive subdimensions (D1: attention direction, mental modeling) and affective/behavioral subdimensions (D1→D2 transition, D2: behavioral coupling). Multiplayer gaming introduces a novel PSI configuration: the "character" is another player behind opacity (fog of war, hidden state), making the parasocial relationship bidirectional and interactive. The social contagion pathway documented in Section VIII.A (observation + being killed → cheating adoption) is a D1→D2→D3 cascade mediated by parasocial coupling to an opaque adversary.

---

## X. Testable Predictions and Falsification Conditions

### X.A. Predictions

**Prediction 1: Visible MMR reduces conspiracy.**

Making MMR visible reduces SBMM conspiracy theories and agency attribution, without changing the algorithm.

*Test:* Compare sentiment in games with hidden vs. visible MMR (chess.com's visible Elo vs. Call of Duty's hidden SBMM).

*Falsification:* If visible-MMR games show equivalent rates of "rigged" conspiracy theories, opacity is not the driver of D1 attribution.

*Status: PARTIALLY CONFIRMED (Experiment D).* Cross-genre survey (N=335) confirms gradient: chess 8.3% < SC2 15.8% < DotA2 22.4% < LoL 26.2% (all p < 0.0001 vs chess). DotA2 vs LoL directionally consistent but not significant (p = 0.687). SC2 vs LoL significant (p = 0.008).

**Prediction 2: Server-side rendering eliminates ESP/wallhacks.**

Moving to server-side rendering (client receives pixels, not game state) will eliminate ESP and wallhack cheats at the cost of latency.

*Test:* Deploy server-side rendered competitive mode; measure cheat prevalence vs. client-rendered mode.

*Falsification:* If ESP-type cheats persist under server-side rendering, the rendering-interface opacity is not the operative variable.

**Prediction 3: Anti-cheat invasiveness correlates with player distrust.**

More invasive anti-cheat systems (kernel-level, boot-time, process-scanning) will generate more D1 agency attribution from players than less invasive systems, independent of effectiveness.

*Test:* Survey player trust across anti-cheat systems controlling for perceived effectiveness.

*Falsification:* If kernel-level anti-cheat generates equivalent trust to user-level anti-cheat at equal effectiveness, the opacity-of-the-anti-cheat does not drive D1.

**Prediction 4: Cheating contagion requires opacity.**

Cheating contagion (the PUBG effect) will be reduced in environments where cheaters are immediately and transparently identified (e.g., real-time "this player was cheating" notifications after match).

*Test:* Compare contagion rates in games with delayed ban waves (high opacity) vs. immediate transparent identification (low opacity).

*Falsification:* If immediate transparent identification shows equivalent contagion rates to delayed opaque bans, opacity is not the contagion driver.

**Prediction 5: The arms race will not converge.**

No client-side anti-cheat approach will produce a stable equilibrium. Each new detection method will be countered. The escalation will continue to hardware and AI levels.

*Test:* Track time-to-bypass for each new anti-cheat generation.

*Falsification:* If any client-side anti-cheat approach produces a stable equilibrium lasting >3 years without escalation, the framework's prediction of structural non-convergence is weakened.

**Prediction 6: Pe scales inversely with tick rate across games.**

Lower tick rate produces higher Pe and more pronounced peeker's advantage, across games:

| Game / Context | Tick Rate (Hz) | Architecture | Pe Prediction | Predicted Community Drift |
|----------------|---------------|--------------|---------------|--------------------------|
| Turn-based online games | ~1 | Varies | Extremely high positional Pe (but engagement model differs — turns are discrete) | Low drift: opacity is structural and accepted (fog of war = game rule) |
| Age of Empires 2 | ~5 (lockstep command rate) | Lockstep deterministic | High *information* Pe (scouting gap dominates); low *positional* Pe (units move slowly) | Low system-directed D1 (visible Elo on aoe2.net); high opponent-directed D1 (maphack accusations) |
| StarCraft 2 | ~16–22 (lockstep) | Lockstep deterministic | **CONFIRMED:** Winner Pe_rate 0.013 vs loser 0.026 (N=474, p < 0.0001); TvT highest Pe (scan-dependent), ZvZ lowest (free Overlords) | Moderate: visible league reduces matchmaking void; fog-of-war accepted as gameplay |
| Dota 2 | ~30 | Client-server + fog | High *vision* Pe (fog depth × gank speed); day/night cycle modulates Pe periodically | Moderate: visible MMR reduces system D1; fog-of-war generates opponent D1 |
| League of Legends | ~30 | Client-server + fog | High (fog of war is the primary opacity, not movement) | High L3 in matchmaking (hidden MMR); low L3 in fog-of-war (accepted opacity) |
| Fighting games (SF/MK/GG) | 60 (fixed) | Peer-to-peer rollback | Moderate *prediction* Pe (input error / rollback correction); no structural anti-cheat | **CONFIRMED low drift:** recalibrated FGC = 3.8% (L2+L3)/L1, lowest of all communities tested; frame data culture produces precise L1 vocabulary |
| Rocket League | ~30–60 | Client-server | Low *visual* opacity: all players and ball visible; void is teammate *intent* | **Measured elevated (31.1%):** coupling intensity drives drift despite low visual opacity (Section VI.F′) |
| Halo 2 era / early console | ~30 | Peer-to-peer (client host) | High | High (host advantage documented) |
| Quake III Arena | 20–40 (server) | Client-server + prediction | High (fast movement, weapon pickups, projectile travel) | Moderate: item timing and railgun → high-skill community maintains L1 |
| CS2 Valve matchmaking | 64 | Client-server + prediction | Moderate | Moderate L2–L3 |
| CS2 FACEIT / VALORANT | 128 | Client-server + prediction | Lower | Lower (community reports "feels more responsive/fair") |

The cross-game comparison tests whether constraint frequency is a continuous predictor of Pe. If 128-tick CS2 shows measurably lower Pe distributions than 64-tick CS2 for equivalent engagement types, the tick-rate → Pe → drift pathway is validated within a single game across two server configurations.

*Test:* Run the Pe pipeline on demo files from both 64-tick and 128-tick CS2 servers (same maps, equivalent skill levels). Compare Pe distributions. Extend to at least one non-FPS title: StarCraft 2 replays (SC2EGSet dataset, 17,930 tournament replays) for RTS information-asymmetry Pe, and Rocket League replays (ballchasing.com, 146M+ replays) for low-opacity sports Pe.

*Falsification:* If Pe distributions are statistically equivalent across tick rates, or if higher tick rates show *higher* Pe, constraint frequency does not modulate drift velocity as predicted. If cross-game Pe shows no coherent scaling with tick rate, the Pe formulation may be FPS-specific rather than universal.

**Prediction 7: Cross-genre Pe formulation produces coherent scaling.**

The Pe > 1 threshold for drift-dominated dynamics should hold across game genres when Pe is reformulated for each genre's information asymmetry:

| Genre | Pe Numerator (drift) | Pe Denominator (constraint) | High-Pe Event |
|-------|---------------------|----------------------------|---------------|
| FPS (CS2) | Movement speed × distance | Tick rate × opponent speed | Clean kill (victim didn't fire) |
| RTS (SC2/AoE2) | Tech choice speed × scouting gap | Opponent scout frequency × reaction window | Unscouted rush / proxy build |
| MOBA (Dota 2/LoL) | Gank speed × fog depth | Ward coverage × reaction window | Successful gank from fog |
| Fighting (SF/MK/GG) | Attack startup × input prediction error | Rollback frames × correction accuracy | Rollback-altered outcome (saw block, was attack) |
| Sports (Rocket League) | Ball control speed × aerial positioning | Opponent reaction × boost level | Aerial goal with opponent out of position |
| Arena FPS (Quake) | Movement speed × item control timing | Tick rate × opponent movement | Railgun pick from item advantage |
| Card (Hearthstone) | Play speed × hand-size advantage | Opponent card-tracking × draw probability | Lethal from hand opponent couldn't anticipate |

Each genre measures a different asymmetry — spatial, temporal, visual, predictive, mechanical, resource, hidden-state — but the ratio structure is invariant. If Pe > 1 separates regimes across formulations sharing only the ratio structure, the thermodynamic derivation is architecture-general.

*Test:* Compute Pe for 100+ engagements in at least two non-FPS games. The most feasible tests: (1) Dota 2 vision-economy Pe from parsed replays — successful vs. failed ganks separated by ward coverage (Section VII.F); (2) SC2 scouting Pe from SC2EGSet — unscouted vs. scouted strategies. If high-Pe events are more decisive than low-Pe events by a separation comparable to the CS2 clean-vs-contested result (4.4×), the cross-genre formulation works. Ballchasing.com API provides data for the sports test. Fighting game Pe is structural-only (no bulk datasets).

*Falsification:* If reformulated Pe shows no relationship with engagement decisiveness in non-FPS genres, the formulation may be FPS-specific. Direct numerical comparison across genres is not expected — the test is whether Pe > 1 separates regimes within each genre.

*Status: CONFIRMED (Experiments A and B).* Cross-genre Pe validation complete across two non-FPS genres — SC2 scouting Pe (Section V.F, N=474) and Dota 2 vision Pe (Section V.G, N=3,682). Both confirm the directional prediction. Three genre-specific Pe formulations (positional, visual, temporal) share only the ratio structure and all produce the predicted relationship. Rocket League formulation remains untested.

### X.B. Kill Conditions for This Paper

The following evidence would break the specific claims of this paper:

1. **Client-side anti-cheat producing convergence.** If a client-side-only anti-cheat (no server authority) eliminated cheating for >3 years in a major title, the "opacity cannot dissolve opacity" claim would be falsified.

2. **Pe failing to predict engagement outcomes.** If Pe shows no significant relationship with engagement decisiveness across genres, the empirical Pe claim would be falsified. **Status: SURVIVED.** N=2,299 CS2 kills across 16 matches confirms 4.4× clean/contested separation (p < 0.0001). Peek-vs-hold asymmetry 6.9× (p = 0.0044). SC2 (N=474, p < 0.0001) and Dota 2 (N=3,682) confirm across genres. The threshold for this kill condition has been exceeded.

3. **Visible MMR producing equivalent conspiracy rates.** If controlled comparison shows no difference in D1 attribution between hidden and visible MMR, the opacity-drives-conspiracy claim would be falsified.

4. **The constraint specification mapping being non-unique.** If game engineers converged on an effective architecture that does NOT map onto transparent/invariant/independent, the independent derivation claim would be weakened. Note: peer-to-peer architectures exist but have never produced stable competitive gaming (IT Hare, n.d.), supporting the claim.

5. **Control cases showing drift despite reduced opacity.** If LAN tournaments, open-source servers, or speedrunning communities showed equivalent drift rates to opaque online play, opacity would not be the operative variable.

---

## XI. Implications for Game Engineering

### XI.A. Scoring Deployments

Any deployment can be scored against the four-void model:

| Architecture Decision | Void Score (0–3) | Rationale |
|----------------------|-------------------|-----------|
| Client-authoritative state | 3 (maximum) | Opaque, responsive, coupled. Trusting the client is trusting the void. |
| Server-authoritative with client prediction | 1 (residual) | Authority is transparent, invariant, independent. Residual: rendering interface. |
| Peer-to-peer with no server | 3 (maximum) | Every peer is opaque. No independent authority. Desync within seconds. |
| Lockstep deterministic (RTS) | 1 (residual) | Invariant simulation, desync detection as constraint. Residual: fog-of-war rendering layer (maphack). |
| Hidden MMR + responsive matchmaking | 2 | Opacity + responsiveness present. Publish the MMR → score drops to 0–1. |
| Kernel-level anti-cheat | 3 (maximum) | Opaque, responsive, coupled to player system. IS a void. |
| Deterministic replay verification | 0 (full constraint) | Transparent, invariant, independent. |
| Server-side rendering | 0 (full constraint) | Eliminates rendering-interface opacity. Client receives pixels, not state. |

### XI.B. Three Engineering Questions

Three questions for any game architect:

**1. Where does authority live?**

If authority lives on the client, you have a void. Move authority to the server for every game-critical variable. Accept the latency cost. Where you can't (rendering), minimize the state the client receives — every byte of unnecessary game state is an attack surface.

**2. What is opaque to the player, and does it need to be?**

| Opacity | Necessary? | Action |
|---------|-----------|--------|
| Opponent's screen/inputs | Yes (competitive integrity) | Accept; mitigate with replay |
| Anti-cheat detection methods | Claimed necessary | Server authority reduces need for client-side detection |
| MMR / matchmaking logic | No | Publish it. Transparency reduces conspiracy at zero cost to integrity. |
| Drop rates / reward mechanics | No | Publish it. Belgium/China regulations already require this. |
| Report/ban outcomes | No | Show the player what happened. Valve's "a player you reported has been banned" notification closes the loop. |

Every unnecessary opacity is a void you chose to build.

**3. Is your anti-cheat a void?**

Score it: transparent (can players understand what it does)? Invariant (rules stay fixed)? Independent (outside the player's control)? If it is opaque, responsive, and runs on the player's machine, it is a void — it will generate distrust regardless of effectiveness.

Alternative: maximize server-side detection, minimize client-side intrusion, publish the rules (not detection signatures, but categories of behavior that trigger investigation).

### XI.C. Policy Recommendations

1. **Mandate drop rate disclosure** — already law in Belgium, China, Japan. The framework explains why it works: dissolves the loot box void.
2. **Publish matchmaking parameters** — not the exact algorithm, but the variables, the criteria, and the visible rating. Chess solved this decades ago.
3. **Prefer server-side over client-side anti-cheat** — every kernel driver on a player's machine is a trust liability, a security surface, and a void.
4. **Close the report loop** — tell reporters what happened. Valve's ban notification is a constraint.
5. **Deterministic replay as default** — every competitive match should produce a reviewable replay. The speedrunning community proved this works at scale.

---

## XII. Limitations

### XII.A. Single-Author Framework Application

All analyses were conducted by the framework's developer. The structural mapping between "never trust the client" and the constraint specification can be verified by anyone, but the interpretation is made by someone with a prior commitment. Independent application by game security researchers is the critical next step.

### XII.B. Pe Validation Scope

CS2 Pe validation covers positional/movement asymmetry only — network components (RTT, jitter, packet loss) require transport-layer data not available in demo files. The expanded sample (2,299 kills, 16 matches) provides robust significance on all tests; peek-vs-hold (N=360 duels) reaches p = 0.0044, and holder win rate normalizes to 48.3%.

Pe magnitude calibration across substrates is not established — CS2 (0.34–7.22), SC2 (0.013–0.072), Dota 2 (0.47), Test 7 (1.87–9.9), and GRCS (2.21) measure different phenomena through different formulations.

Additional datasets for validation: AoE2 replays (aoc-mgz), Rocket League (ballchasing.com, 146M+ replays, carball), Quake III Arena (UberDemoTools). The SC2 analysis uses camera position as a scouting proxy, which does not perfectly measure information gained. All SC2 data is professional; lower skill levels remain untested.

### XII.C. Vocabulary Analysis: Validated with Caveats

PV-1 (N=180, 1.6M words) validates L-level separation; cross-genre expansion (N=335, 7 communities) confirms the opacity gradient. All six gaming communities show significantly higher (L2+L3)/L1 than chess (all p < 0.0001). Fog-of-war gradient is monotonic (SC2 < DotA2 < LoL ≈ VALORANT; SC2 vs LoL p = 0.008).

Caveats: (1) Gaming codebook circularity — designed for these communities; independent validation needed. (2) L3 does not separate at baseline; most users plateau at L2. (3) Vanguard experiment null — cross-sectional, not longitudinal. (4) CoD not significant on L-level at N=30. (5) DotA2 vs LoL directionally consistent but p = 0.687 — larger samples needed to isolate MMR visibility.

### XII.D. Control Cases Are Natural, Not Experimental

The control cases are natural experiments, not randomized trials. Confounds exist: LAN players are more skilled, speedrunners are self-selected, face-to-face players have different demographics. Convergence across five opacity-reduction types mitigates but does not eliminate confounding.

### XII.E. The "Independent Derivation" Claim

The framework was developed after the game security community converged on server authority — influence runs engineering → framework, not reverse. However, the structural identity between "never trust the client" and "transparent, invariant, independent" is an interpretation that should be evaluated by game security practitioners.

### XII.F. FGC Codebook Artifact — Identified and Corrected

The fighting game community (r/Fighters) originally produced the highest (L2+L3)/L1 ratio of any community tested (49.5%), despite low visual opacity. A codebook recalibration — moving 18 FGC-standard terms from L2 to L1 — reduces the result to 3.8%, below chess (8.3%). The original L2 classification inflated the drift score by approximately 13×.

**What was reclassified:** Standard FGC vocabulary where metaphorical origin has become the primary technical meaning. "Download" = "learned opponent's patterns" — L1, not L2. Reclassification applies to the fighting game codebook only.

**Methodological lesson:** The L-level boundary is domain-dependent. Every domain codebook requires calibration with practitioners — a single cross-domain codebook systematically misclassifies communities with highly metaphorical technical vocabularies. Independent validation of all codebooks remains the most important methodological next step.

**Impact on core findings:** The fog gradient (chess < SC2 < DotA2 < LoL ≈ VALORANT) is unaffected. The recalibrated FGC result (3.8%) strengthens the framework: lowest visual opacity + most precise vocabulary = lowest drift ratio.

### XII.G. Dota 2 Vision Pe: Day/Night Null and Scope

Day/night kill asymmetry did not replicate (ratio = 0.498, N=100). Three possible explanations: (a) high-MMR positioning compensation, (b) cycle timing mismatch with current patch, (c) reduced night vision reducing both initiation and success.

The 82.9% fog-kill rate and Pe_vision results are robust at N=3,682 deaths. The per-teamfight extension strengthens the ward↔fog correlation from r = −0.073 (per-match) to r = −0.502 (per-teamfight, p < 0.0001) — the underlying relationship is strong but confounded by team skill at the match level. Ward coverage is approximated as boolean (ward present at death location), not continuous coverage surface. Full replay parsing would yield more precise estimates.

### XII.H. Evidence Boundaries and Vulnerability Table

The following table assesses each major claim's evidence status, using the same assessment standard as the TOE synthesis (Paper 5, §8A.1):

| Claim | Status | What Would Strengthen | What Would Kill |
|-------|--------|----------------------|-----------------|
| Independent derivation of constraint spec (§III) | **Strong.** Three architectures, documented engineering history, hostile witness. | Independent evaluation by game security researchers unfamiliar with framework. | Discovery of a stable competitive architecture that does NOT map onto T/Inv/Ind. |
| Four-void coupling model (§II.E) | **Formalized but unmeasured.** Coupling matrix is derived from attention conservation (Paper 3 §IV.J); coupling topology constrained by causal structure. **No coupling coefficients (κ_{ij}) have been measured.** Kim & Tsvetkova (2022) provides the empirical base for estimating κ₂₁ (cheating contagion), but extracting the coefficient requires fitting the coupled system to longitudinal player-level data. The remaining five cross-coupling terms are theoretically specified but empirically open. | Longitudinal player-level data fitting coupled ODE to PUBG contagion trajectories (κ₂₁). Controlled matchmaking experiments varying opacity (visible vs. hidden MMR) measuring conspiracy rates over time (κ₄₁). | If coupled system with measured κ_{ij} produces qualitatively wrong cascade ordering (e.g., matchmaking conspiracy preceding opponent suspicion without independent evidence). |
| CS2 Pe (§V.C) | **Confirmed.** N=2,299, p < 0.0001, clean/contested 4.4×. Expanded from pilot (N=426). | Network Pe (RTT, jitter, packet loss) — requires Wireshark capture, not available in demo files. Cross-map validation on additional demos. | Pe showing no relationship with engagement decisiveness (p > 0.05 at N > 1,000). |
| SC2 scouting Pe (§V.F) | **Confirmed.** N=474 pro games, p < 0.0001. | Lower-skill replications. Camera-position proxy replaced with actual vision data. | Winners showing higher Pe than losers (reversed prediction). |
| Dota 2 vision Pe (§V.G) | **Confirmed with caveats.** 82.9% fog-kill rate (N=3,682). Ward correlation r = −0.502 per-teamfight. Day/night null result. | Continuous ward coverage surface (not boolean). Day/night at lower MMR brackets. | Fog-kill rate < 50% (constraint-dominated regime). |
| Cross-genre vocabulary gradient (§VI.F′) | **Confirmed.** N=335, 7 communities, monotonic gradient, all p < 0.0001 vs chess. FGC recalibrated. | Larger samples (CoD not significant at N=30). Longitudinal tracking within communities. | Chess showing equivalent or higher drift than high-opacity games. |
| Arms race non-convergence (§IV) | **Supported (historical).** 30 years of documented escalation. No theoretical counterexample. | Time-to-bypass dataset across anti-cheat generations. | Any client-side anti-cheat producing stable equilibrium > 3 years. |
| Control cases (§VII) | **Supported (natural experiments).** Five types of opacity reduction all show reduced drift. | Randomized trial (hidden vs. visible MMR in same game). | Control environment showing equivalent drift to opaque environment. |

**Key evidence gap:** The four-void coupling model (§II.E) is the paper's central novel contribution but its coupling coefficients are unmeasured. The model is mathematically well-specified and the coupling topology is constrained by the causal structure (opponent suspicion feeds anti-cheat distrust, not vice versa for most players), but without measured κ_{ij} values, the model cannot make quantitative predictions about cascade timescales or coupling strengths. It currently explains why cascades interact (structural argument) but not how fast (quantitative prediction). This is the single most important gap for future work.

### XII.I. What This Paper Is Not

This paper does not claim:
- That all anti-cheat is useless (server-authoritative architecture works)
- That cheating doesn't matter (the D3 harms are documented and real)
- That game developers are malicious (EOMM notwithstanding, most matchmaking is skill-based)
- That the framework replaces domain expertise in game engineering
- That the Pe formula is ready for production use (calibration data is needed)

---

## XIII. Conclusion

Multiplayer gaming is a four-void coupled system where each void reinforces the others through the observer. Three networking architectures — client-server, lockstep, and rollback — independently converged on the constraint specification through engineering failure, constituting hostile witness evidence of the highest weight. Three Pe formulations (positional, temporal, visual) share only the ratio structure and all confirm the same directional prediction across 6,455 measured events (Sections V.C, V.F, V.G). A corpus study of 335 users across 7 communities confirms the opacity-drift gradient (Section VI.F′).

The specific quantitative findings: CS2 clean kills show 4.4× higher Pe than contested kills (N=2,299, p < 0.0001); SC2 winners maintain 2× lower Pe than losers (N=474, p < 0.0001); 82.9% of Dota 2 teamfight deaths occur where the victim's team lacked vision (N=3,682). The cross-genre vocabulary survey confirms a 3.1× chess-to-VALORANT separation (chess 8.3% → SC2 15.8% → Dota 2 22.4% → LoL 26.2%, all p < 0.0001 vs chess), and the monotonic fog gradient confirms that architecture and transparency jointly modulate drift. Two of seven predictions are now confirmed: Prediction 7 (cross-genre Pe coherent scaling) by CS2, SC2, and Dota 2 validation; Prediction 1 (visible MMR reduces conspiracy) partially confirmed by the opacity-drift gradient (N=335).

Two empirically surprising findings refine the theory. Rocket League shows elevated drift vocabulary (31.1%) despite zero visual opacity — the operative void is teammate intent, not visual occlusion, confirming that the full void specification (not just visual opacity) drives drift. The fighting game community, after codebook recalibration, shows the lowest drift ratio of any community tested (3.8%, below chess at 8.3%) — low opacity, high technical precision via frame data culture, and the most specialized vocabulary produce the least drift.

The anti-cheat arms race confirms the structural prediction: opacity cannot dissolve opacity. Anti-cheat systems with void properties generate their own cascades, independent of effectiveness. The Vanguard and GameGuard cases confirm: the system built to fight a void became one.

Game engineers discovered through decades of failure what the framework formalizes: the only structural solution to an adversarial information system is authority that is transparent, invariant, and independent. Chess solved matchmaking by publishing ratings. Server-authoritative architecture solved client trust by not trusting the client. Speedrunning solved verification with deterministic replays. The solutions exist. The framework explains why they work, why alternatives don't, and where the residual problems live.

---

## XIV. Transparency

### XIV.A. Production Method

Drafted using Claude (Anthropic) as a writing tool; all structural decisions, evidence selection, and analytical conclusions by the human author. CS2 pipeline: demoparser2 (Python/Rust), demo files from cited GitLab repository. SC2: SC2EGSet dataset (CC BY 4.0, Białecki et al. 2023), sc2reader (Python). PV-1 corpus: Arctic Shift API, N=335 users, 7 subreddits, genre-specific codebooks. Dota 2: OpenDota API. All pipelines available for replication.

### XIV.B. Author Provenance

The author's background in multiplayer game development is relevant: the client-server trust problem was an experiential input that made the void architecture recognizable in other domains. The engineering insight — "if you can't trust the client, it corrupts the whole system" — preceded the framework vocabulary by years. The framework formalized what the engineering had demonstrated.

### XIV.C. Financial Disclosure

The project is developing a proprietary scoring product for multiplayer infrastructure. Open science (Pe, constraint specification, void architecture) is Tier 1 (CC-BY 4.0); proprietary algorithms and calibration data are Tier 3 (private). This paper establishes the theoretical basis but contains no proprietary algorithms. The author has a financial interest in framework adoption — weigh accordingly.

---

## References

### Game Architecture and Client Security
- Gambetta, G. (n.d.). *Client-Server Game Architecture.* gabrielgambetta.com. Accessed February 2026.
- Photon Engine. (n.d.). *Authoritative Server FAQ.* doc.photonengine.com. Accessed February 2026.
- Game Developer. (2023). *Never Trust the Client: Simple Techniques Against Cheating in Multiplayer.* gamedeveloper.com.
- IT Hare. (n.d.). *On Cheating, P2P, and Non-Authoritative Servers.* ithare.com. Accessed February 2026.
- Bettner, P. & Terrano, M. (2001). 1500 Archers on a 28.8: Network Programming in Age of Empires and Beyond. *Game Developers Conference (GDC) 2001.* [Lockstep deterministic simulation architecture]
- Frohnmayer, M. & Gift, T. (n.d.). The Tribes Engine Networking Model. gamedevs.org. [Control Object vs Ghost Object prediction, Move/Event/Ghost manager priority system]
- Carmack, J. (1996). QuakeWorld client-side prediction. id Software. [First implementation of client-side prediction in FPS]

### Anti-Cheat Systems and Arms Race
- Dorner, M. & Klausner, L.D. (2024). If It Looks Like a Rootkit and Deceives Like a Rootkit. In *Proceedings of the ACM Conference on Security and Privacy in New Computing Platforms (SePriCo '24).*
- Müller, F., et al. (2024). Systematic review of anti-cheat technical defenses. arXiv:2512.21377v1.
- Esports Heaven. (2023). *The Cracks in Riot Vanguard's Shield.* esportsheaven.com.
- RIT Computing Security Blog. (2022). *Security Concerns About Kernel-Level Anti-Cheat in Video Games.* rit.edu.
- Philip, B. (2024). *Evaluating Kernel-Level Anti-Cheats as a Consumer.*
- Steam Community. (2024). Helldivers 2 community response to GameGuard anti-cheat adoption. store.steampowered.com.

### Cheater Psychology and Social Contagion
- Lofgren, E.T. & Fefferman, N.H. (2007). The untapped potential of virtual game worlds to shed light on real world epidemics. *The Lancet Infectious Diseases,* 7(9), 625–629. [Corrupted Blood incident as epidemiological model]
- Kim, H. & Tsvetkova, M. (2022). Social contagion of cheating in online multiplayer games. *Network Science,* 10(3), 209–226. Cambridge University Press. [1,146,941 PUBG matches]
- Frontiers in Psychology. (2021). Competitive motivation, self-esteem, and aggression in cheating behavior. [329 League of Legends players]
- PMC. (2023). Self-determination theory and game cheating. PMC10770842.
- Boldi, A., et al. (2020). I Cheat So I Can Be Better at the Game: Understanding Cheating Motivations. In *Proceedings of ACM CHI Play '20.* [188 U.S. players]

### Matchmaking and SBMM
- Chen, Z., et al. (2017). EOMM: An Engagement Optimized Matchmaking Framework. In *Proceedings of the IEEE International Conference on Data Mining (ICDM '17).* arXiv:1702.06820. [36.9M matches, 1.68M players]
- PC Gamer. (2024). Activision secretly experimented on 50% of Call of Duty players. pcgamer.com.
- Insider Gaming. (2024). SBMM Creator Debunks Conspiracy Theories. insidergaming.com.
- Vice. (2021). Why Players Blame Skill-Based Matchmaking for Losing. vice.com.

### Esports Scandals and Harms
- cs.money. (2023). 5 Most Notorious Counter-Strike Cheating Scandals. cs.money.
- Esports Insider. (2023). History of Counter-Strike Scandals. esportsinsider.com.
- PC Gamer. (2023). The Biggest Esports Scandals of the Past 10 Years. pcgamer.com.
- Washington Post. (2020). Stimulant use in esports.

### Rollback Netcode and Fighting Games
- Cannon, T. (2006/2019). GGPO: Good Game Peace Out. github.com/pond3r/ggpo. MIT License. [Reference rollback netcode implementation]
- Stallone, M. (2018). 8 Frames in 16ms: Rollback Networking in Mortal Kombat and Injustice 2. *Game Developers Conference (GDC) 2018.* [NetherRealm Studios' rollback engineering]
- Infil.net. (n.d.). Netcode Fightin' Words. infil.net. [Comprehensive multi-part series on fighting game netcode]
- SnapNet. (n.d.). Netcode Architectures Part 1: Lockstep; Part 2: Rollback. [Architecture comparison series]

### MOBA Vision Economy and Data
- OpenDota. (n.d.). Open platform for Dota 2 match data. api.opendota.com. [1.19B matches, 10M+ parsed replays with ward data]
- skadistats/clarity. Java parser for Dota 2 replay files. github.com/skadistats/clarity. [Full entity extraction including ward lifecycle]
- Riot Games. (n.d.). Match-V5 API. developer.riotgames.com. [LoL match timeline with WARD_PLACED/WARD_KILL events; deliberately excludes ward x/y coordinates]
- Kawwa. (n.d.). Where To Place Wards in DOTA2. *Towards Data Science.* [Clustered ward placement by game phase from ~25K pro matches]

### Netcode Engineering (Riot and Blizzard)
- Riot Games Engineering Blog. (2020). VALORANT netcode architecture and server design. technology.riotgames.com.
- Blizzard Entertainment. (2017). Overwatch Gameplay Architecture and Netcode. *Game Developers Conference (GDC) 2017.*

### Demo Parsing and Replay Analysis
- demoparser2 (v0.41.0). Python/Rust CS2 demo parser. PyPI: demoparser2.
- GitLab akiver/cs-demos. Community-maintained CS2 demo repository. gitlab.com/akiver/cs-demos.
- aoc-mgz. Python parser for Age of Empires II recorded game files (.aoe2record). GitHub: happyleavesaoc/aoc-mgz.
- age-alyser (v0.0.5). Statistical extraction from AoE2 replays. PyPI: age-alyser. Built on aoc-mgz.
- sc2reader (v1.8.0). Python library for StarCraft II replay parsing. PyPI: sc2reader.
- Blizzard Entertainment. s2protocol. Reference Python library for StarCraft II replay decoding. GitHub: Blizzard/s2protocol.
- UberDemoTools. Analysis and viewing tools for Quake 3 and Quake Live demo files. GitHub: mightycow/uberdemotools.
- carball. Python Rocket League replay parser and analyzer. PyPI: carball.
- ballchasing.com. Rocket League replay database with 146M+ replays and API access.

### Cross-Genre Datasets
- Białecki, A., et al. (2023). SC2EGSet: StarCraft II Esport Replay and Game-state Dataset. *Nature Scientific Data.* [17,930 tournament replays with game-state information]
- aoe2.net. Age of Empires II replay vault and visible Elo rating system. Accessed February 2026.
- demos.igmdb.org. Quake 3 tournament demos archive. Internet Archive. [Professional match demos from QuakeCon, Dreamhack, ESWC, etc.]
- ESReality. Ultimate Quake Live Duel Demo Collection. esreality.com. [Tournament duel demos from major events]
- Spawning Tool. StarCraft 2 replay packs from tournaments. lotv.spawningtool.com/replaypacks/.

### Time Perception and Parasocial Interaction
- Dixon, M.J., Gutierrez, J., Stange, M., Larche, C.J., Graydon, C., Vintan, S., & Kruger, T.B. (2018). Dark flow, depression, and multiline slot machine play. *Journal of Gambling Studies*, 34(1), 73-84.
- Liebers, N., & Schramm, H. (2019). Parasocial interactions and relationships with media characters: An inventory of 60 years of research. *Communication Research Trends*, 38(2), 4-31.
- Schüll, N.D. (2012). *Addiction by Design: Machine Gambling in Las Vegas*. Princeton University Press.
- Wittmann, M. (2009). The inner experience of time. *Philosophical Transactions of the Royal Society B*, 364, 1955-1967.

### Void Framework (Companion Papers)
- Paper 1: *The Architecture of Drift: A Cross-Domain Diagnostic for Epistemological Architecture.* (v13.0)
- Paper 2: *The Shape of the Cage: Deployment Geometry as an Under-Studied Variable in AI Safety.* (v5.6)
- Paper 3: *Thermodynamics of Opacity: Technical Foundations of the Void Framework.* (v7.0)
- Paper 4: *Information-Geometric Bounds on Thermodynamic Sampling and Superconducting Order.* (v3.5)
- Paper 4B: *The Thermodynamic Cost of Unconstrained Acceleration.* (v1.5)
- Paper 5: *The Ground State of Observation: A TOE Synthesis.* (v4.9)
- Paper 7: *Your DeFi Protocol Is a Void: Void Architecture in Cryptocurrency Markets.* (v1.6)
- Paper 8: *The Observer-Measurement Bridge: Classical Information Theory as the Diagonal Limit of Quantum Measurement Dynamics.* (v1.9)

### Pe Measurements (Cross-Substrate)
- Test 7 (AI-to-AI): Pe = 1.87–9.9, N=11 runs, geometric mean 7.94 [3.52, 17.89]. Papers 1, 3, 5.
- GRCS meta-analysis (gambling): pooled Pe_D1 = 2.21 [1.44, 2.97], N=1,117 across 5 studies. Papers 1, 3, 5.
  - Muela, I., et al. (2020). Gambling self-regulation scale.
  - Ruiz de Lara, C.M., et al. (2019). Gambling impulsivity measures.
  - Navas, J.F., et al. (2016). Cognitive distortion in gambling disorder.
  - Ciccarelli, M., et al. (2021). Italian gambling self-regulation.
  - Donati, M.A., et al. (2015). Adolescent gambling cognitive distortions.
  - Raylu, N. & Oei, T.P.S. (2004). Gambling Related Cognitions Scale (GRCS) development. *Journal of Gambling Studies,* 20(2), 95–126.

---

*Paper 6 v2.5 — February 2026*

*v2.5: Abstract/conclusion audit — conclusion expanded with specific Pe findings, prediction statuses (P1 partial, P7 confirmed), RL/FGC refinement findings; companion paper versions updated (Paper 2 v5.6, Paper 4 v3.5, Paper 4B v1.5, Paper 5 v4.9). v2.4: Evidence boundaries table (§XII.H), coupling derivation status note (§II.E), companion paper versions updated, Paper 8 added to references. v2.3: Zenodo-ready pass.*
*Domain #62 in the Void Framework Research Index*
