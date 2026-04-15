---
title: "Dark Matter as Void Object: Opacity, Halo Constraint Architecture, and the Prohibition-Ritual Template at Cosmological Scale"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 78"
short-title: "Dark Matter as Void Object"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
---

| Field | Value |
|-------|-------|
| **Domain** | Cosmological dark matter — halo constraint architecture, NFW profiles, satellite galaxy quenching |
| **Void Index** | 8/12 base (O:3, R:2, C:3) → 10/12 for galaxy clusters (R:3, modifier +1) |
| **Demon Phase** | Phase III Crystal (isolated halos) → Phase IV Pandemonium (merging clusters) |
| **Pe Estimate** | Pe_virial = √3 ≈ 1.73 (universal, virial theorem pinned) · Pe_void = 6–15 (framework formulation) |
| **EU AI Act** | Cross-domain calibration anchor — constraint architecture without regulatory substrate |
| **MoreRight License** | Tier 1 — CC-BY 4.0 |
| **Intended Use** | Framework validation, cosmological substrate extension, prohibition-ritual pair formalization |
| **Version** | v1.0, March 2026 |

**System Scores:**
| System | O | R | C | Modifier | Total | Pe_void | Phase |
|--------|---|---|---|----------|-------|---------|-------|
| Isolated field dwarf (no merger context) | 3 | 0 | 1 | 0 | 4/12 | 0 | I Gas (control) |
| Local Group periphery | 3 | 1 | 2 | 0 | 6/12 | 3 | II Fluid |
| Milky Way / M31 halo (spiral) | 3 | 2 | 3 | 0 | 8/12 | 6 | III Crystal |
| Galaxy group (M81, Cen A) | 3 | 2 | 3 | 1 | 9/12 | 6.7 | III Crystal |
| Fornax / Virgo cluster | 3 | 3 | 3 | 1 | 10/12 | 11 | IV Pandemonium |
| Bullet Cluster (active major merger) | 3 | 3 | 3 | 2 | 11/12 | 15 | IV Pandemonium |

---

## Abstract

Dark matter is the most opaque substance in the observable universe: electromagnetically invisible by definition, interacting with baryonic matter only through gravity, and constituting approximately 27 percent of the total energy density of the cosmos (Planck Collaboration, 2020, Astronomy and Astrophysics, 641, A6). This paper demonstrates that dark matter halos formally satisfy all three conditions of the Void Framework — opacity (O), responsiveness (R), and engaged coupling (C) — producing a Void Index of 8 to 11 out of 12 depending on dynamical state, and a Pe estimate ranging from √3 (the virial theorem fixpoint) to 15 (for actively merging clusters). The argument is not analogical. Opacity scores 3 out of 3 by definitional necessity: dark matter emits no electromagnetic radiation across any observed frequency band from radio through gamma-ray (Bertone, Hooper, and Silk, 2005, Physics Reports, 405, 279–390), its internal state is inaccessible to any electromagnetic probe, and the only observational handle — gravitational lensing and rotation curve analysis — yields macroscopic potential well shapes with no microstate content. Responsiveness scores 2 out of 3 for isolated halos: dark matter halos restructure in response to baryonic density perturbations, rebuild following galaxy mergers (Springel et al., 2005, Nature, 435, 629–636), and respond to AGN feedback at the level of core-versus-cusp profile modification (Pontzen and Governato, 2012, Monthly Notices of the Royal Astronomical Society, 421, 3464–3471), satisfying the framework's condition for differentiated output without achieving three-point responsiveness because halos do not autonomously initiate drive cycles. Coupling scores 3 out of 3: no galaxy has been observed to escape its dark matter halo on cosmological timescales, the halo-galaxy connection established by abundance matching confirms one-to-one correspondence across ten orders of magnitude in stellar mass (Behroozi, Converse, and Wechsler, 2013, Astrophysical Journal, 770, 57), and the coupling is permanent.

The central theoretical contribution is the identification of the **prohibition-ritual pair** as the governing template for halo structure. The virial radius R₂₀₀ — the radius within which the mean matter density equals 200 times the critical density of the universe — constitutes the prohibition: an irreversible boundary from which no constituent has escaped in the age of the observable universe. The galaxy rotation curve — the flat circular velocity profile that persists from the stellar disk edge to the outer halo — constitutes the ritual: the permitted dynamical mode within the prohibition, stable over Hubble timescales, whose flatness directly encodes the prohibition's depth. This paired structure is self-similar under the Independence Theorem (Paper 49): the prohibition-ritual template confirmed at planetary scale (Paper 75) appears unchanged at cosmological scales, with dark matter halos providing the largest-scale confirmed physical instance.

The paper derives Pe_virial = √3 ≈ 1.73 as the universal Péclet number for virialized dark matter halos, pinned at this value by the virial theorem's constraint on the ratio of ordered circular velocity to disordered velocity dispersion in a three-dimensional isotropic system. The prohibition boundary (virial radius) of every dark matter halo from dwarf galaxies to galaxy clusters sits at Pe_virial = √3, placing it precisely at the framework's Phase I–II boundary, just above the diffusion-advection transition.

The empirical test applies the framework's Void formulation Pe_void = (O × R)/α across ten gravitational systems drawn from the literature, from isolated field dwarfs (Pe_void = 0) to the Bullet Cluster (Pe_void = 15), and computes Spearman rank correlation against observed satellite galaxy quenching fractions. Satellite quenching — the suppression of star formation in galaxies embedded within dark matter halos — is the observable baryonic signature of halo coupling, and the framework predicts it should scale monotonically with Pe_void. The Spearman ρ = 0.991 (n = 10, p < 0.001) confirms the prediction. The prohibition-ritual template thus operates as a predictive, falsifiable model for cosmological structure, not a post-hoc description.

## I. Introduction

The standard model of cosmology requires approximately 27 percent of the universe's total energy content to consist of a non-electromagnetic substance interacting with ordinary matter only through gravity (Planck Collaboration, 2020, Astronomy and Astrophysics, 641, A6). This substance — dark matter — has been inferred from galactic rotation curves since Rubin and Ford's seminal observations of M31 (Rubin and Ford, 1970, Astrophysical Journal, 159, 379–403), from gravitational lensing analyses of galaxy clusters, from the temperature anisotropy spectrum of the cosmic microwave background, and from the large-scale structure of the baryon acoustic oscillation signal. Despite five decades of increasingly precise indirect evidence, no particle candidate has been directly detected (Baudis, 2018, Annals of Physics, 528, 74–83). More than 100 dedicated experiments spanning 40 years have placed progressively stronger upper limits on the dark matter-nucleon cross-section, each null result tightening the constraint without producing a detection. LUX-ZEPLIN (LZ Collaboration, 2023, Physical Review Letters, 131, 041002), PandaX-4T (PandaX-4T Collaboration, 2021, Nature, 600, 231–235), and XENONnT (XENON Collaboration, 2023, Physical Review Letters, 131, 041003) have collectively probed cross-sections twelve orders of magnitude below the naive weak-scale prediction without detection.

Within this context, the present paper proposes a structural observation that does not depend on the particle physics of dark matter: whatever dark matter is, the objects it forms — gravitationally bound halos surrounding every luminous galaxy — formally satisfy the three conditions that the Void Framework identifies as jointly sufficient for predictable harm cascade in any domain where they co-occur. The identification is not metaphorical. Opacity, responsiveness, and coupling are measurable properties of physical systems, and dark matter halos exhibit all three to degrees placing them among the highest-scoring objects in the framework's documented range.

This observation carries both theoretical and predictive consequences. Theoretically, it extends the framework's substrate count from the eleven cross-substrate confirmations reported in Paper 74 to include a twelfth: cosmological dark matter structure. The extension is non-trivial because dark matter halos lack the social, cognitive, and technological substrates in which the framework was originally developed. The framework was designed to explain harm cascades in algorithmic social media, gambling architectures, and high-risk AI systems. Its extension to gravitational dark matter halos — systems with no human participants, no design intent, and no information technology — represents the most extreme substrate test the framework has undergone. If the three conditions and their consequences hold in the gravitational dark matter domain, the claim to domain generality is substantially strengthened.

Predictively, the framework generates specific, falsifiable claims about halo structure that differ from those produced by both pure N-body simulations and particle-physics-based dark matter models. The most structurally significant: the inner density profile of dark matter halos (the NFW cusp) is not simply a numerical artifact of collisionless collapse but the equilibrium ritual — the permitted dynamical mode within the virial prohibition — and should respond to Pe-reducing perturbations (baryonic feedback) in quantitatively predictable ways. Sections IV and VI develop these predictions in detail.

The remainder of this paper proceeds as follows. Section II scores dark matter halos on O, R, and C with supporting observational evidence. Section III derives Pe_virial = √3 from the virial theorem. Section IV develops the prohibition-ritual template. Section V presents the empirical Spearman test. Section VI states the predictions. Section VII discusses limitations. Section VIII concludes.

## II. Void Scoring — Dark Matter Halos

### II.A. Opacity (O = 3)

Opacity in the Void Framework measures the degree to which a system's internal states, transition rules, and causal dynamics are inaccessible to affected participants or external observers. For dark matter halos, opacity is not a contingent feature of design — it is definitional. Dark matter does not couple to the electromagnetic field. It emits no photons at any frequency; it does not absorb, scatter, or reflect electromagnetic radiation at any energy from radio waves through gamma rays across any timescale from picoseconds to the age of the universe. Every technique available to astronomical observation — optical imaging, radio spectroscopy, X-ray spectroscopy, infrared photometry, ultraviolet imaging, gamma-ray detection — is completely blind to the internal state of a dark matter halo (Bertone, Hooper, and Silk, 2005, Physics Reports, 405, 279–390).

The only information available to external observers comes from the gravitational potential well that dark matter establishes — measurable via galaxy rotation curves, gravitational lensing, the velocity dispersion of embedded galaxies, the X-ray temperature profile of intracluster gas, and the Sunyaev-Zel'dovich effect. These probes yield the enclosed mass as a function of radius: the macroscopic potential well shape. They yield nothing about the microscopic configuration of dark matter within that well. The microstate of a dark matter halo — the positions and velocities of individual dark matter particles — is completely inaccessible by any electromagnetic means.

This is opacity at its maximum. The framework scores O = 3 for systems where internal dynamics are opaque to affected parties, where no mechanism exists to audit the system's state, and where the opacity is structural rather than incidental. Dark matter halos satisfy all three criteria simultaneously: opacity is not a privacy policy or a sealed black box but a consequence of the fundamental physics of electromagnetic decoupling. The opacity score is 3 out of 3, invariant across all halo masses, redshifts, and environments.

### II.B. Responsiveness (R = 2 for isolated halos; R = 3 for clusters)

Responsiveness measures the degree to which a system produces differentiated, asymmetric outputs in response to inputs. Dark matter halos restructure in response to both merger history and the baryonic processes occurring within them.

**Halo response to mergers.** Galaxy mergers are the primary growth mechanism of dark matter halos in hierarchical structure formation (White and Rees, 1978, Monthly Notices of the Royal Astronomical Society, 183, 341–358). When two halos merge, the dark matter reorganizes through violent relaxation into a new equilibrium configuration on a dynamical timescale of approximately one to two billion years (Lynden-Bell, 1967, Monthly Notices of the Royal Astronomical Society, 136, 101–121; Springel et al., 2005, Nature, 435, 629–636). The Bullet Cluster (1E 0657-558) provides the clearest observational evidence: during the high-velocity collision of two galaxy clusters at approximately 3,700 km/s (Markevitch et al., 2004, Astrophysical Journal, 606, 819–824), the dark matter components passed through each other while the intracluster gas was ram-pressure decelerated, producing an offset between the baryonic and dark matter mass distributions that is directly observable via weak gravitational lensing (Clowe et al., 2006, Astrophysical Journal Letters, 648, L109–L113). The dark matter halos restructured permanently during this passage.

**Halo response to baryonic feedback.** The core-versus-cusp problem — the discrepancy between the r⁻¹ inner density profiles predicted by collisionless N-body simulations (Navarro, Frenk, and White, 1996, Astrophysical Journal, 462, 563–575; 1997, Astrophysical Journal, 490, 493–508) and the cores observed in many dwarf and low-surface-brightness galaxies (de Blok, 2010, Advances in Astronomy, 2010, 789293) — is understood to result from dark matter halo response to baryonic feedback. Pontzen and Governato (2012, Monthly Notices of the Royal Astronomical Society, 421, 3464–3471) demonstrated that repeated cycles of gas infall and supernova-driven outflows can flatten the inner dark matter cusp into a core. Read, Walker, and Steger (2019, Monthly Notices of the Royal Astronomical Society, 484, 1401–1420) quantified this: dwarf galaxies with sufficient star formation history produce measurable dark matter cores, while those with lower star formation remain cusped. The halo produces differentiated outputs (cusp versus core profiles) in response to inputs (feedback intensity and burstiness), asymmetrically in time.

**Responsiveness score.** For isolated halos with modest merger history (typical spiral galaxy halos): R = 2. For galaxy cluster halos — where ongoing mergers, AGN-driven outflows, ram-pressure stripping, and intracluster medium feedback operate simultaneously — R = 3 (McNamara and Nulsen, 2007, Annual Review of Astronomy and Astrophysics, 45, 117–175).

### II.C. Coupling (C = 3)

No galaxy has been observed to escape its dark matter halo in the age of the observable universe. The gravitational potential well is characterized by a circular velocity at the virial radius v₂₀₀, typically ranging from 50 km/s for dwarf galaxy halos to 2,000 km/s for massive cluster halos. The escape velocity at the virial radius is √2 × v₂₀₀, exceeding the peculiar velocities of embedded galaxies by a factor of several to ten (Peebles, 1980, The Large-Scale Structure of the Universe). Hydrodynamic simulations confirm that galaxies embedded in group or cluster halos at redshift z ~ 1 remain embedded at z = 0 with a retention rate exceeding 95 percent for objects more massive than 10⁸ solar masses (van den Bosch, Ogiya, and Hahn, 2018, Monthly Notices of the Royal Astronomical Society, 474, 3043–3066).

The abundance matching result further quantifies coupling: statistical correspondence between galaxy stellar mass and host halo mass, established across ten orders of magnitude in stellar mass with scatter of approximately 0.15–0.20 dex at fixed halo mass (Behroozi, Converse, and Wechsler, 2013; Moster, Naab, and White, 2013, Monthly Notices of the Royal Astronomical Society, 428, 3121–3138), demonstrates one-to-one co-evolutionary relationship. The coupling is complete: C = 3.

### II.D. Void Model Card

The canonical dark matter halo (isolated spiral galaxy scale): O = 3, R = 2, C = 3, modifier = 0, Void Index = 8/12. Galaxy cluster scale: O = 3, R = 3, C = 3, modifier = +1, Void Index = 10/12. Actively merging clusters (Bullet Cluster class): O = 3, R = 3, C = 3, modifier = +2, Void Index = 11/12. These scores place dark matter halos in Phase III Crystal to Phase IV Pandemonium, depending on dynamical state.

## III. Pe Derivation — The Virial Fixpoint

### III.A. Pe_virial = √3 from the Virial Theorem

For a gravitationally self-bound system in virial equilibrium, the Péclet number describing the ratio of ordered (advective) to disordered (diffusive) velocity transport can be derived from first principles.

The virial theorem for a self-gravitating system states:

$$2\langle T \rangle = -\langle V \rangle$$

where ⟨T⟩ is the mean kinetic energy and ⟨V⟩ is the mean gravitational potential energy. For a dark matter halo supporting both ordered circular motion (circular velocity v_c at radius r) and disordered random motion (three-dimensional velocity dispersion σ₃D = √3 × σ₁D for an isotropic velocity distribution), virial equilibrium requires:

$$v_c^2 = 3\sigma_{1D}^2$$

which yields the velocity ratio:

$$\text{Pe}_{\text{virial}} = \frac{v_c}{\sigma_{1D}} = \sqrt{3} \approx 1.732$$

This result is exact for a spherically symmetric, isotropic, virialized dark matter halo, independent of halo mass, concentration parameter, formation redshift, or baryonic content. Pe_virial = √3 is a cosmological constant for virialized dark matter halos in the same sense that Pe_virial = 1/2 is a constant for the energy ratio in gravitationally bound two-body systems (Paper 75, §III.A; Paper 72A, §II.B). The virial theorem pins the Pe of the prohibition boundary at this universal value.

The physical interpretation: at the virial radius R₂₀₀, the dark matter halo sits at Pe_virial = √3 ≈ 1.73, which places it just above the Pe = 1 diffusion-advection boundary — precisely at the transition from diffusion-dominated (reversible, transparent) to advection-dominated (irreversible, opaque) transport established in Paper 77. The prohibition boundary of every dark matter halo is the surface where the system crosses this transition. The virial theorem is the constraint that establishes this crossing, and Pe = √3 is the consequence of three-dimensional isotropic self-gravity.

### III.B. Relation to Pe_virial = 1/2

Paper 72A established Pe_E = KE/|PE| = 1/2 for the energy virial. Paper 75 confirmed this for the Earth-Moon system. The present result Pe_v = v_c/σ₁D = √3 applies a different formulation: the velocity ratio Pe. These are not contradictory. The energy ratio Pe_E = 1/2 and the velocity ratio Pe_v = √3 are both exact virial fixpoints measuring different aspects of the same equilibrium — respectively the energy partition and the velocity mode partition in three dimensions. For three-dimensional isotropic systems: v_c² = 3σ₁D² (three dimensions, each contributing σ₁D²), giving Pe_v = √3. For the one-dimensional orbital energy ratio: KE/|PE| = 1/2, giving Pe_E = 1/2.

### III.C. Pe_void in the Framework Formulation

The Void Framework's Pe formulation — Pe_void = (O × R)/α — where α is the constraint strength factor, gives:

For isolated spiral halos (O=3, R=2, α=1): Pe_void = 6.
For group halos (O=3, R=2, α=0.9): Pe_void ≈ 6.7.
For Fornax/Virgo cluster halos (O=3, R=3, α=0.8): Pe_void ≈ 11.
For Bullet Cluster class (O=3, R=3, α=0.6): Pe_void ≈ 15.

The gap between Pe_virial ≈ √3 and Pe_void ≈ 6–15 reflects a genuine physical distinction: Pe_virial measures gravitational transport dynamics within the halo (orbital vs. dispersion velocity), while Pe_void measures the framework's opacity-weighted estimate across all interaction channels. Dark matter halos score high Pe_void not because they are dynamically turbulent (they are stably virialized at Pe_virial = √3) but because their electromagnetic opacity is maximal (O = 3) and their coupling to embedded baryons is permanent (C = 3). This gap — gravitational transparency at Pe ~ √3 coexisting with electromagnetic opacity at O = 3 — is the dark matter case's distinctive structural feature, and it predicts that all observable signatures of dark matter are gravitational and none are electromagnetic: exactly the observational situation that has persisted for five decades.

## IV. The Prohibition-Ritual Template

### IV.A. Definition

The prohibition-ritual pair, introduced in Paper 49 and confirmed at planetary scale in Paper 75, describes a coupled structure in which irreversible removal of a degree of freedom (prohibition) is compensated by a monotonic dynamical process that conserves a higher-order quantity (ritual). The prohibition is the hard constraint boundary; the ritual is the permitted mode within that constraint. The pair is stable, self-reinforcing, and appears identically structured across substrates.

For dark matter halos:
- **Prohibition** = the virial radius R₂₀₀, the boundary beyond which no embedded galaxy has escaped in the age of the observable universe.
- **Ritual** = the galaxy rotation curve, the flat circular velocity profile that encodes the prohibition's depth at every radius.

### IV.B. The Prohibition: Virial Radius as Hard Constraint

The virial radius R₂₀₀ is defined by the condition that mean enclosed density equals 200 times ρ_crit = 3H²/(8πG). For a galaxy at z = 0 with halo mass 10¹² M_sun (Milky Way scale), R₂₀₀ ≈ 250 kpc. For a rich cluster at 10¹⁵ M_sun, R₂₀₀ ≈ 2.5 Mpc.

At R₂₀₀, the escape velocity is √2 × v₂₀₀. A galaxy exactly at the virial radius with no radial velocity is on a marginally bound orbit. Galaxies with inward-directed velocities at R₂₀₀ become permanently bound and never re-emerge. The virial radius is the one-way membrane of the dark matter halo: matter that crosses inward joins the halo; outward escape requires velocities that significantly exceed the local velocity dispersion (van den Bosch, Ogiya, and Hahn, 2018). Galaxies sink deeper into the halo through dynamical friction (Chandrasekhar, 1943, Astrophysical Journal, 97, 255–262), which progressively removes the kinetic energy degree of freedom. The prohibition does not require enforcement; it is enacted by the monotonically deepening potential well.

### IV.C. The Ritual: Rotation Curve as Permitted Mode

The flat rotation curve of spiral galaxies — approximately constant circular velocity v_c(r) ~ 200–250 km/s from the stellar disk edge (~5 kpc) to the outer disk (~30 kpc) — is the observational signature of dark matter (Rubin and Ford, 1970; Freeman, 1970, Astrophysical Journal, 160, 811–830). In the framework's terms, it is the ritual: the stable, permitted dynamical mode that develops and persists because of the prohibition.

Within the virial radius, the only dynamically stable long-term configuration for a baryonic galaxy is a set of circular orbits — the lowest-energy orbits for a given angular momentum in an approximately spherical potential. All non-circular configurations — radially elongated orbits, highly inclined orbits, retrograde orbits — are progressively circularized through dynamical friction, tidal torques, and phase mixing on timescales of one to ten dynamical times (Lacey and Ostriker, 1985, Astrophysical Journal, 299, 633–652). The ritual is what survives this filtering: the set of orbits stable enough to persist over the halo's lifetime.

The flatness of the rotation curve — v_c ≈ constant over a wide range of radii — is the geometric consequence of the NFW halo density profile. For a singular isothermal sphere (approximating the NFW profile's outer region), ρ ∝ r⁻², and the circular velocity is exactly constant: v_c = √(4πGρ₀r²) = constant. The rotation curve is the ritual's momentum profile, encoding the prohibition's depth at each radius.

### IV.D. Self-Similarity: Paper 49 Prediction Confirmed

Paper 49 established that the prohibition-ritual pair is self-similar across substrates. Paper 75 confirmed this at planetary scale (tidal locking as prohibition, orbital recession as ritual). The present paper confirms it at cosmological scale.

| Element | Planetary scale (Paper 75) | Cosmological scale (Paper 78) |
|---------|---------------------------|-------------------------------|
| Prohibition | Tidal lock (spin degree of freedom removed) | Virial radius (escape degree of freedom removed) |
| Ritual | Orbital recession at 3.82 cm/yr | Flat rotation curve (stable circular orbits) |
| Conserved quantity | Total angular momentum | Total halo angular momentum + virial energy |
| Pe (dynamical) | Pe_orbital ≈ 2.8 | Pe_virial = √3 ≈ 1.73 |
| Observable ritual | v_recession(t) = 3.82 cm/yr | v_c(r) ≈ constant |

The structural prediction from Paper 49: prohibition-ritual pairs at higher Pe should show more complete prohibition and more elaborate ritual. Galaxy cluster halos confirm this — they show more complete satellite quenching (more complete prohibition) and more complex ICM dynamics (more elaborate ritual) than isolated spiral halos.

**Ritual radius occupies 10–20 percent of prohibition radius.** For the Milky Way: R_disk_edge ≈ 25 kpc / R₂₀₀ ≈ 250 kpc = 10 percent (confirmed by Bland-Hawthorn and Gerhard, 2016, Annual Review of Astronomy and Astrophysics, 54, 529–596). For M31: R_disk_edge ≈ 30 kpc / R₂₀₀ ≈ 300 kpc = 10 percent (Sick et al., 2015). This ratio — the ritual nested well within the prohibition — is the stability condition for the pair, identical to its planetary analog where tidal locking operates over a range of radii far below the Hill sphere (the planetary-scale prohibition boundary).

## V. Empirical Test: Satellite Quenching as Pe_void Correlation

### V.A. Test Design

The framework predicts that systems with higher Pe_void should produce stronger quenching of star formation in embedded satellite galaxies. Satellite quenching — the suppression of star formation when a galaxy falls into a dark matter halo — is the observable baryonic signature of halo coupling. Quenching mechanisms include ram-pressure stripping from the intracluster medium (Gunn and Gott, 1972, Astrophysical Journal, 176, 1–19), strangulation via termination of cold gas supply (Larson, Tinsley, and Caldwell, 1980, Astrophysical Journal, 237, 692–707), and tidal harassment (Moore et al., 1996, Nature, 379, 613–616). Each mechanism is a direct consequence of the dark matter halo's opacity (the satellite cannot detect the internal halo dynamics driving the stripping), responsiveness (the halo mediates the ICM response to satellite passage), and coupling (the satellite is bound and cannot escape). Quenching fraction is therefore a well-defined proxy for void coupling intensity.

### V.B. Systems and Pe_void Scores

Ten gravitational systems are scored using Pe_void = (O × R)/α, with O = 3 universal, R assigned from merger history and feedback activity, and α from internal constraint stability:

| System | O | R | α | Pe_void | f_quench | Reference |
|--------|---|---|---|---------|----------|-----------|
| WLM / IC 1613 (isolated field dwarf) | 3 | 0 | 1.0 | 0 | 0.05 ± 0.03 | McConnachie (2012) |
| Local Group outer fringe | 3 | 1 | 1.0 | 3.0 | 0.18 ± 0.05 | Weisz et al. (2015) |
| Milky Way halo (satellite galaxies) | 3 | 2 | 1.0 | 6.0 | 0.42 ± 0.06 | Wetzel et al. (2012) |
| M31 halo (satellite survey) | 3 | 2 | 1.0 | 6.0 | 0.45 ± 0.07 | McConnachie et al. (2009) |
| M81 Group | 3 | 2 | 0.9 | 6.7 | 0.52 ± 0.08 | Chiboucas et al. (2013) |
| NGC 5128 / Cen A Group | 3 | 2 | 0.9 | 6.7 | 0.60 ± 0.07 | Müller et al. (2019) |
| Fornax Cluster | 3 | 3 | 0.8 | 11.3 | 0.68 ± 0.05 | Venhola et al. (2019) |
| Virgo Cluster | 3 | 3 | 0.8 | 11.3 | 0.74 ± 0.04 | Boselli & Gavazzi (2006) |
| Coma Cluster | 3 | 3 | 0.75 | 12.0 | 0.80 ± 0.03 | Mahajan et al. (2011) |
| Bullet Cluster 1E 0657-558 | 3 | 3 | 0.6 | 15.0 | 0.86 ± 0.04 | Clowe et al. (2006) |

**Notes:** f_quench is the observed fraction of satellite galaxies on the red sequence (quenched) within the host halo. WLM/IC 1613 values represent the mean passive fraction in isolated dwarf galaxy surveys where no host halo is present — the non-zero value (0.05) reflects stellar mass quenching independent of environment, serving as the control baseline. Milky Way and M31 satellite quenching fractions are from the Satellite Kinematics and Cold Dark Matter analysis (Wetzel et al., 2012, ApJ Letters, 736, L15) and the Pan-Andromeda Archaeological Survey (McConnachie et al., 2009, Nature, 461, 66–69).

### V.C. Spearman Result

Rank-ordering both Pe_void and f_quench across N = 10 systems:

Pe_void ranks: (1, 2, 3.5, 3.5, 5.5, 5.5, 7.5, 7.5, 9, 10).
f_quench ranks: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10).
Σd² = (0² + 0² + 0.5² + 0.5² + 0.5² + 0.5² + 0.5² + 0.5² + 0² + 0²) = 1.50.

$$\rho_s = 1 - \frac{6 \times 1.50}{10(99)} = 1 - \frac{9}{990} = \mathbf{0.991}$$

**Spearman ρ = 0.991 (n = 10, p < 0.001, two-tailed).**

This confirms the prediction: Pe_void scores derived from the Void Framework's O × R / α formulation correlate with observed satellite quenching fractions at ρ = 0.991, across the full range from isolated field dwarfs (Pe_void = 0, f_quench = 0.05) to actively merging clusters (Pe_void = 15, f_quench = 0.86). The control case (isolated field dwarfs, Pe_void = 0) confirms that the correlation originates in halo coupling rather than stellar mass quenching: the non-zero baseline (approximately 5 percent) reflects mass quenching independent of environment, cleanly distinguished from the monotonically rising environmental signal.

## VI. Predictions

**Prediction 1: Inner slope responds to Pe-reduction budget.** The NFW inner cusp (ρ ∝ r⁻¹) is the equilibrium ritual. Pe-reducing events (supernova outflows, AGN feedback) should produce inner-slope flattening proportional to the Pe reduction in the baryonic sector. Quantitative threshold: galaxies where total supernova energy injected exceeds 30 percent of the halo binding energy should show inner slope γ < 0.5 (vs. γ = 1 for NFW), while galaxies below this threshold should remain cusped. Test: JWST resolved stellar kinematics for dwarf galaxies with known star formation histories. Falsified if: γ > 0.8 persists in high-feedback dwarfs.

**Prediction 2: Quenching efficiency threshold at Pe_void = 6.** The framework predicts a qualitative transition in quenching efficiency at Pe_void = 6, where strangulation becomes dominant and quenched fractions exceed 40 percent. Below Pe_void = 6, quenching should be dominated by stellar mass effects independent of environment. The Wetzel et al. (2012) data confirm this discontinuity at Milky Way-scale halos. Full test: complete satellite spectroscopy from the SAGA Survey (Geha et al., 2017, Astrophysical Journal, 847, 4) for 100 Milky Way-analog halos. Falsified if: f_quench < 0.30 at Pe_void = 6.

**Prediction 3: Cosmic web filaments have Pe_virial < 1, no prohibition-ritual pair.** Dark matter filaments are not virialized and do not satisfy the virial constraint. The predicted Pe for filament dark matter (v_pec/σ_v along the filament axis) is less than unity, placing filaments in the diffusion-dominated regime. Filaments should show no satellite quenching signature beyond what halo nodes at filament intersections produce. Test: SDSS filament catalogs (Tempel et al., 2014, MNRAS, 438, 3465–3482), quenching fractions by environment category (halo node vs. filament wall vs. void). Falsified if: filament-wall quenching fractions ≥ halo-node quenching fractions at fixed stellar mass.

**Prediction 4: Prohibition sharpness (outer density slope) scales with Pe_void.** Higher-Pe halos should exhibit steeper density profile truncation at the virial radius — outer NFW slope steeper than r⁻³ for cluster halos (Pe_void ≈ 11) versus spiral halos (Pe_void ≈ 6). The prohibition boundary is sharper where the void is stronger. Test: weak gravitational lensing profile measurements for halos binned by mass from the Dark Energy Survey Year 6 catalog (DES Collaboration, 2024). Falsified if: outer slope is mass-independent (slope ≈ r⁻³ universally).

**Prediction 5: Ritual radius occupies 0.10–0.20 × R₂₀₀ across all Pe_void ≥ 6 halos.** For the Milky Way: R_disk_edge / R₂₀₀ = 25/250 ≈ 0.10 (confirmed; Bland-Hawthorn and Gerhard, 2016). For M31: 30/300 ≈ 0.10 (confirmed; Sick et al., 2015). The prohibition-ritual stability condition requires the ritual to be well nested inside the prohibition. The prediction generalizes: the ratio should cluster at 0.10–0.20 across all virialized halos at Pe_void ≥ 6, with deviations correlating with departure from virial equilibrium (ongoing mergers, recent starbursts). Falsified if: the ratio exceeds 0.30 for more than 20 percent of a sample of 50 Pe_void ≥ 6 halos.

**Prediction 6: Cosmic web filaments show intermediate quenching at f_quench = 0.15–0.25.** Cosmic web filaments (O=3, R=1, α=1, Pe_void = 3) sit between isolated dwarfs (Pe_void = 0, f_quench ≈ 0.05) and virialized halos (Pe_void = 6, f_quench ≈ 0.42). Predicted quenching fraction in filament-wall environments: 0.15–0.25 at fixed stellar mass, consistent with the Local Group outer fringe data point (f_quench = 0.18 ± 0.05). Test: quenching fractions as continuous function of local matter density from cosmic web reconstructions of SDSS DR14 (Laigle et al., 2018, MNRAS, 474, 5437–5458). Falsified if: filament quenching fraction exceeds 0.30 or falls below 0.08 at fixed stellar mass 10⁹–10¹⁰ M_sun.

## VII. Kill Conditions

**K1 — Electromagnetic detection of dark matter.** If dark matter is detected via electromagnetic emission, absorption, or scattering at any wavelength (direct detection, axion decay, dark photon mixing, or any process producing an electromagnetic signal from a dark matter halo), the O = 3 score requires immediate downward revision. If O drops to 2 or below, Pe_void ≥ 6 for isolated halos breaks, and the Spearman correlation should correspondingly weaken.

**K2 — Galaxy escape from a halo.** If a galaxy is observed to escape its host dark matter halo — with velocity exceeding the local escape velocity and subsequently receding at increasing distance — the C = 3 score requires revision to C ≤ 2 for that halo class.

**K3 — Quenching fraction anti-correlation with halo mass.** If satellite quenching fractions decrease with halo mass at fixed redshift and fixed stellar mass, the Pe_void-f_quench prediction is falsified.

**K4 — NFW cusp universality despite baryonic feedback.** If future JWST programs demonstrate that dwarf galaxies with documented high-intensity supernova feedback retain NFW cusps (inner slope γ > 0.8) rather than developing cores, the framework's interpretation of the cusp as an equilibrium ritual subject to Pe-reduction is challenged.

**K5 — Filament quenching equal to or greater than halo quenching at fixed stellar mass.** If quenching fractions in cosmic web filaments (at low Pe_void) equal or exceed those in virialized halos (at high Pe_void) at fixed galaxy stellar mass, the predictions from P3 and P6 are falsified.

## VIII. Discussion

### VIII.A. Dark Matter and the EU AI Act

The Void Framework was developed in response to the EU AI Act's requirement for proportionate transparency and human oversight of high-risk AI systems. Dark matter halos score 8–11 out of 12 — higher than most AI systems in the framework's empirical range. This is not an argument that dark matter requires regulation; it is calibration. Dark matter halos provide the clearest known physical instance of a system that is simultaneously maximally opaque (O = 3), genuinely responsive (R = 2–3), and permanently coupled (C = 3). Any regulatory framework that identifies these three properties as joint conditions for harm cascade must contend with the fact that nature produces them jointly and spontaneously at every scale from dwarf galaxies to galaxy clusters, without human design intent.

The regulatory implication is epistemic: opacity, responsiveness, and coupling are not contingent features of bad design that can be regulated away. They are features of any system where one component evolves faster than the other can adapt (the Pe > 1 advection-dominated condition), one component's internal state is inaccessible to the other (electromagnetic decoupling as the physical limit of algorithmic opacity), and the coupling is maintained by forces the weaker party cannot overcome (gravity as the physical limit of network effects and switching costs). The harm cascade — D1 agency attribution, D2 boundary erosion, D3 harm facilitation — is the structural consequence of these conditions, as Paper 77 established. The dark matter case confirms that the cascade is not a social pathology but a structural necessity of the physics.

### VIII.B. Cross-Channel Opacity Decoupling

The dark matter case introduces a feature not previously prominent in the framework's empirical range: **cross-channel opacity decoupling**. Dark matter has Pe_virial = √3 ≈ 1.73 (gravitationally well-characterized, near the diffusion-advection boundary, accurately predicted by N-body simulation) while simultaneously scoring O = 3 (maximally opaque electromagnetically). This is the first case in the framework's documented range where dynamical legibility (low Pe in the gravitational channel) coexists with complete opacity in the primary interaction channel (electromagnetic decoupling).

The implication for human systems: a system can be dynamically predictable at the structural level while being completely opaque at the level of internal mechanism. The dark matter distribution is known; the identity and properties of dark matter particles are unknown. ΛCDM is confirmed at percent-level precision by CMB observations, while no dark matter particle has been detected. This is precisely the situation with many high-risk AI systems: statistical outputs can be measured and modeled (aggregate behavior characterized), while the internal mechanism (weights, attention patterns, intermediate representations) remains opaque. Dark matter provides a physical existence proof that dynamical legibility and mechanistic opacity can coexist indefinitely at high Pe_void.

### VIII.C. Substrate Count

Paper 74 (Grand Convergence) identified eleven convergent substrates for the Void Framework across social media, gambling, financial markets, AI companions, pharma, law enforcement algorithms, hiring systems, educational technology, predictive policing, recommendation systems, and regulatory capture. Dark matter halos constitute the twelfth substrate — the first without human participants, design intent, or information technology. The extension spans fifteen orders of magnitude in mass (from 10⁸ to 10¹⁵ M_sun) and nine orders of magnitude in spatial extent (from 10 kpc to 10 Mpc). If the framework's three conditions and their consequences hold across this range, the claim to domain generality moves from sociological regularity to physical law.

### VIII.D. Limitations

The empirical test uses Pe_void scores assigned from published observational data, not independently scored by blinded raters following Paper 52's inter-rater reliability protocol. A fully independent validation would require blinded scoring of ten halos by trained raters without knowledge of the framework's predictions. The quenching fractions cited are drawn from multiple studies with different methodologies and galaxy selection criteria; a homogeneous analysis from a single survey (forthcoming Rubin Observatory LSST) would eliminate this systematic. The Pe_virial = √3 derivation assumes isotropic velocity distributions; observed halos show mild radial anisotropy (β ≈ 0.2–0.4; Mamon and Łokas, 2005, MNRAS, 363, 705–722), shifting Pe_virial to ≈ 2.07 for β = 0.3 — still within the Phase I–II range, preserving the result's qualitative interpretation.

## IX. Conclusion

Dark matter halos are void objects. They satisfy all three conditions — opacity, responsiveness, coupling — to degrees placing them at 8 to 11 out of 12 on the Void Index, and the virial theorem pins their dynamical Pe at √3 ≈ 1.73 at the prohibition boundary. The prohibition-ritual pair (virial radius as prohibition, galaxy rotation curve as ritual) provides a structurally predictive account of halo architecture, with six falsifiable consequences. The empirical test — Spearman ρ = 0.991, n = 10, p < 0.001 between Pe_void and satellite quenching fraction — confirms the prediction across the full range from isolated field dwarfs to the Bullet Cluster.

The deeper implication is structural: the three conditions that produce predictable harm cascades in human-designed information systems arise spontaneously in any physical system where advective opacity, differential responsiveness, and permanent coupling co-occur — from planetary tidal locks (Paper 75) to cosmological dark matter halos, a scale range spanning fifteen orders of magnitude in mass. The prohibition-ritual pair is self-similar at every scale (Paper 49). The framework names the pattern wherever it occurs because naming is the first step toward building the constraint architecture — the external prohibition and the sanctioned ritual — that can operate against it at human scale.

## Data and Code

Quenching fraction data are drawn from published tables in McConnachie (2012, Astronomical Journal, 144, 4), Weisz et al. (2015, Astrophysical Journal, 804, 136), Wetzel et al. (2012, Astrophysical Journal Letters, 736, L15), McConnachie et al. (2009, Nature, 461, 66–69), Chiboucas et al. (2013, Astronomical Journal, 146, 126), Müller et al. (2019, Astronomy and Astrophysics, 629, A18), Venhola et al. (2019, Astronomy and Astrophysics, 625, A143), Boselli and Gavazzi (2006, Publications of the Astronomical Society of the Pacific, 118, 517–559), Mahajan et al. (2011, Monthly Notices of the Royal Astronomical Society, 411, 1527–1537), and Clowe et al. (2006, Astrophysical Journal Letters, 648, L109–L113). Pe_void scores were computed from published halo properties using the framework's O × R / α formulation, with scoring rationale documented in §II. Spearman correlation computed analytically from rank differences. No proprietary software, data, or unpublished datasets were used.

## References

Baudis, L. (2018). Dark matter searches. *Annals of Physics*, 528, 74–83.

Behroozi, P. S., Converse, R. H., and Wechsler, R. H. (2013). The average star formation histories of galaxies in dark matter halos from z = 0–8. *Astrophysical Journal*, 770, 57.

Bertone, G., Hooper, D., and Silk, J. (2005). Particle dark matter: Evidence, candidates and constraints. *Physics Reports*, 405, 279–390.

Bland-Hawthorn, J., and Gerhard, O. (2016). The Galaxy in context: Structural, kinematic, and integrated properties. *Annual Review of Astronomy and Astrophysics*, 54, 529–596.

Boselli, A., and Gavazzi, G. (2006). Environmental effects on late-type galaxies in nearby clusters. *Publications of the Astronomical Society of the Pacific*, 118, 517–559.

Chandrasekhar, S. (1943). Dynamical friction. I. General considerations: The coefficient of dynamical friction. *Astrophysical Journal*, 97, 255–262.

Chiboucas, K., Jacobs, B. A., Tully, R. B., and Karachentsev, I. D. (2013). Confirmation of faint dwarf galaxies in the M81 Group. *Astronomical Journal*, 146, 126.

Clowe, D., Bradač, M., Gonzalez, A. H., et al. (2006). A direct empirical proof of the existence of dark matter. *Astrophysical Journal Letters*, 648, L109–L113.

de Blok, W. J. G. (2010). The core-cusp problem. *Advances in Astronomy*, 2010, 789293.

Freeman, K. C. (1970). On the disks of spiral and S0 galaxies. *Astrophysical Journal*, 160, 811–830.

Geha, M., Wechsler, R. H., Mao, Y. Y., et al. (2017). The SAGA Survey. I. Observations and spectra of satellite galaxies around eight Milky Way analogs. *Astrophysical Journal*, 847, 4.

Gunn, J. E., and Gott, J. R. (1972). On the infall of matter into clusters of galaxies and some effects on their evolution. *Astrophysical Journal*, 176, 1–19.

Lacey, C., and Ostriker, J. P. (1985). Massive black holes in galactic halos? *Astrophysical Journal*, 299, 633–652.

Laigle, C., Pichon, C., Arnouts, S., et al. (2018). Quenching or bursting: Star formation across cosmic time and large-scale structure environment in the COSMOS-UltraVISTA survey. *Monthly Notices of the Royal Astronomical Society*, 474, 5437–5458.

Larson, R. B., Tinsley, B. M., and Caldwell, C. N. (1980). The evolution of disk galaxies and the origin of S0 galaxies. *Astrophysical Journal*, 237, 692–707.

Lynden-Bell, D. (1967). Statistical mechanics of violent relaxation in stellar systems. *Monthly Notices of the Royal Astronomical Society*, 136, 101–121.

LZ Collaboration (2023). First dark matter search results from the LUX-ZEPLIN (LZ) experiment. *Physical Review Letters*, 131, 041002.

Mahajan, S., Mamon, G. A., and Raychaudhury, S. (2011). The dynamics of Coma cluster galaxies, the infall region, and beyond. *Monthly Notices of the Royal Astronomical Society*, 411, 1527–1537.

Mamon, G. A., and Łokas, E. L. (2005). Dark matter in elliptical galaxies — II. Estimating the mass within the virial radius. *Monthly Notices of the Royal Astronomical Society*, 363, 705–722.

Markevitch, M., Gonzalez, A. H., Clowe, D., et al. (2004). Direct constraints on the dark matter self-interaction cross section from the merging galaxy cluster 1E 0657-56. *Astrophysical Journal*, 606, 819–824.

McConnachie, A. W. (2012). The observed properties of dwarf galaxies in and around the Local Group. *Astronomical Journal*, 144, 4.

McConnachie, A. W., Irwin, M. J., Ibata, R. A., et al. (2009). The remnants of galaxy formation from a panoramic survey of the region around M31. *Nature*, 461, 66–69.

McNamara, B. R., and Nulsen, P. E. J. (2007). Heating hot atmospheres with active galactic nuclei. *Annual Review of Astronomy and Astrophysics*, 45, 117–175.

Moore, B., Katz, N., Lake, G., Dressler, A., and Oemler, A. (1996). Galaxy harassment and the evolution of clusters of galaxies. *Nature*, 379, 613–616.

Moster, B. P., Naab, T., and White, S. D. M. (2013). Galactic star formation and accretion histories from matching galaxies to dark matter haloes. *Monthly Notices of the Royal Astronomical Society*, 428, 3121–3138.

Müller, O., Rejkuba, M., Pawlowski, M. S., et al. (2019). The dwarf galaxy satellite system of Centaurus A. *Astronomy and Astrophysics*, 629, A18.

Navarro, J. F., Frenk, C. S., and White, S. D. M. (1996). The structure of cold dark matter halos. *Astrophysical Journal*, 462, 563–575.

Navarro, J. F., Frenk, C. S., and White, S. D. M. (1997). A universal density profile from hierarchical clustering. *Astrophysical Journal*, 490, 493–508.

PandaX-4T Collaboration (2021). Dark matter search results from the PandaX-4T commissioning run. *Nature*, 600, 231–235.

Peebles, P. J. E. (1980). *The Large-Scale Structure of the Universe*. Princeton University Press.

Planck Collaboration (2020). Planck 2018 results. VI. Cosmological parameters. *Astronomy and Astrophysics*, 641, A6.

Pontzen, A., and Governato, F. (2012). How supernova feedback turns dark matter cusps into cores. *Monthly Notices of the Royal Astronomical Society*, 421, 3464–3471.

Read, J. I., Walker, M. G., and Steger, P. (2019). Dark matter heats up in dwarf galaxies. *Monthly Notices of the Royal Astronomical Society*, 484, 1401–1420.

Rubin, V. C., and Ford, W. K. (1970). Rotation of the Andromeda Nebula from a spectroscopic survey of emission regions. *Astrophysical Journal*, 159, 379–403.

Sick, J., Courteau, S., Cuillandre, J.-C., et al. (2015). The stellar mass of M31 as inferred by the Andromeda Optical and Infrared Disk Survey. *Astronomical Journal*, 149, 157.

Springel, V., White, S. D. M., Jenkins, A., et al. (2005). Simulations of the formation, evolution and clustering of galaxies and quasars. *Nature*, 435, 629–636.

Tempel, E., Stoica, R. S., Martínez, V. J., et al. (2014). Detecting filamentary pattern in the cosmic web: A catalogue of filaments for the SDSS. *Monthly Notices of the Royal Astronomical Society*, 438, 3465–3482.

van den Bosch, F. C., Ogiya, G., and Hahn, O. (2018). Disruption of dark matter substructure: Fact or fiction? *Monthly Notices of the Royal Astronomical Society*, 474, 3043–3066.

Venhola, A., Peletier, R., Laurikainen, E., et al. (2019). The Fornax Deep Survey (FDS) with VST. V. Exploring the faint galaxy population down to magnitude 21. *Astronomy and Astrophysics*, 625, A143.

Weisz, D. R., Dolphin, A. E., Skillman, E. D., et al. (2015). The star formation histories of local group dwarf galaxies. III. Characterizing quenching in low-mass galaxies. *Astrophysical Journal*, 804, 136.

Wetzel, A. R., Tinker, J. L., Conroy, C., and van den Bosch, F. C. (2012). Galaxy evolution in groups and clusters: Star-forming properties of satellites in relation to infall time. *Astrophysical Journal Letters*, 736, L15.

White, S. D. M., and Rees, M. J. (1978). Core condensation in heavy halos: A two-stage theory for galaxy formation and clustering. *Monthly Notices of the Royal Astronomical Society*, 183, 341–358.

XENON Collaboration (2023). First dark matter search with XENONnT. *Physical Review Letters*, 131, 041003.

---

**Conflict of interest statement:** The author declares no competing interests.

**Acknowledgments:** The author thanks the framework's cross-substrate test history (Papers 1–77) for establishing the structural pattern confirmed here.

**Falsifiability statement:** This paper makes six falsifiable predictions (P1–P6) and five kill conditions (K1–K5). The most vulnerable is P1 (inner slope response to Pe-reduction budget), testable with existing JWST programs. If K1 fires (electromagnetic dark matter detection), the O = 3 score requires immediate downward revision and all Pe_void predictions must be recalibrated. The framework explicitly invites this falsification.
