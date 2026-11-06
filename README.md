# Kaibo Xu | Materials Research Portfolio

I am a master's student in Materials Science and Engineering at Northwestern University. I use molecular simulation and data-driven models to study how molecular structure and dynamics influence mechanical behavior. My current research focuses on dynamic polymer networks.

## Project pages

- [Poly(TA) thesis](projects/polyta-thesis/README.md) · coarse-grained model validation and a tabulated-force example
- [Digital Rheometer](projects/digital-rheometer/README.md) · stress relaxation, time–temperature superposition, and a synthetic example
- [OSU CFRP capstone](projects/osu-cfrp-capstone/README.md) · lap shear results from the public poster

## 1. Modeling Dynamic Poly(TA) Networks

*Master's thesis in progress · Northwestern University · Shull Group*

**Research question.** How does reversible disulfide exchange affect the structure and relaxation of poly(thioctic acid), and how might iron(III) coordination change that behavior?

**My contribution.** I built a seven-bead coarse-grained representation of thioctic acid from atomistic trajectories and fitted bonded potentials for use in LAMMPS. I compared coarse-grained bond, angle, and torsion distributions with the mapped atomistic references. Where a coordinate sampled multiple conformations, I used a tabulated potential to retain the corresponding minima.

**Modeling decision.** For a side-chain distance with two preferred states, I used a tabulated double-well potential. Directly differentiating the sampled energy profile introduced artificial force spikes. I smoothed the energy before calculating forces, then checked that the coarse-grained trajectory sampled both distance states. Agreement was stronger for bond lengths than for some angle populations.

**Current direction.** I am extending the model to ring-opened chains and developing an MD–kinetic Monte Carlo workflow for topology changes. The effects of iron(III) coordination on network stability and relaxation are research questions for that extension.

## 2. Digital Rheometer for Dynamic Polymer Networks

*MSE 459 team project · Northwestern University · 2026*

**Team.** Mulin Zou, Kaibo Xu, and Ruizhi Jia.

**Research question.** Can a machine-learning surrogate predict stress-relaxation curves across temperatures and crosslinker molecular weights?

**My contribution.** I worked on feature design, result analysis, and application of the trained model. Our team compared random forests, gradient-boosted trees, and a multilayer perceptron using leave-one-group-out validation. Tree-based predictions showed step changes in time, while the perceptron provided smooth curves for time–temperature superposition.

**Model application.** I analyzed the horizontal and vertical shift factors used to build master curves and examined how apparent activation energy and half-relaxation time varied with crosslinker molecular weight. The surrogate suggested a nonmonotonic activation-energy trend. The apparent minimum motivates a follow-up question about whether the trend persists with additional measurements and whether the model could support inverse design.

## 3. Surface Treatment and Failure of Bonded CFRP Joints

*Senior design team project · The Ohio State University · 2024*

**Team.** Lana Al-Tamim, Kaibo Xu, and Harsh Gaur. Advised by Peter Anderson and sponsored by Honda Aircraft Company.

**Research question.** How do atmospheric-pressure plasma and laser surface treatments affect the lap shear strength of bonded carbon fiber-reinforced polymer joints compared with standard surface preparation methods?

**My contribution.** I helped prepare bonded specimens, perform single-lap shear tests, and examine fracture surfaces using optical microscopy.

**Results.** Among the conditions tested, plasma treatment at a nozzle distance of 6 mm and a traverse speed of 150 mm/s produced the highest lap shear strength. Optical microscopy showed different failure modes in the representative specimens, including light fiber tear after plasma treatment and fiber tear after sanding.

**Public poster.** *Atmospheric Plasma and Laser Treatment to Maximize Polymer Composite Bond Strength*, The Ohio State University.
