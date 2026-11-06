[← Portfolio home](../../README.md)

# Modeling Dynamic Poly(TA) Networks

*Master’s thesis in progress · Northwestern University · Shull Group*

I am developing a coarse-grained model of poly(thioctic acid), or poly(TA), to study how reversible disulfide reactions affect polymer structure and mechanical relaxation. The project builds from atomistic conformations to linear-chain bulk simulations. The next comparison is between fixed and reactive disulfide topologies, followed by a study of how Fe(III) coordination changes network behavior.

## Research workflow

| Stage | Modeling decision and validation | Status |
| --- | --- | --- |
| [1. Closed-ring monomer](workflow/01-closed-ring-monomer.md) | Split a coarse side-chain bead into two. Fit bonded potentials and compare finite-temperature atomistic and coarse-grained distributions. | Validated at 300 K |
| [2. Open repeat unit and oligomer junction](workflow/02-open-repeat-and-junction.md) | Fit the repeat unit using the center of an atomistic trimer. Obtain a separately reweighted equilibrium reference for the internal disulfide junction of a tetramer. Test transfer across three chain lengths. | Bonded working model established |
| [3. Bulk nonbonded force field](workflow/03-nonbonded-force-field.md) | Fit mapped atomistic radial distribution functions (RDFs) with iterative Boltzmann inversion (IBI). Compare WCA- and LJ-based models under pressure control. | Working set selected for linear-chain simulations |
| [4. Linear chains and bulk relaxation](workflow/04-linear-chains-and-bulk.md) | Build 16-repeat-unit chains and independently pack three bulk replicas. Compare density convergence with slower chain conformational relaxation. | Three bulk replicas characterized |
| [5. Transient contacts and mechanical baseline](workflow/05-contacts-and-mechanical-baseline.md) | Compare C1 contact persistence at the site and chain levels. Measure the small-strain stress response with signed-strain and zero-strain controls. | Fixed-topology baseline established |
| [6. Reactive-network comparison](workflow/06-reactive-network-roadmap.md) | Define allowed topology changes and their kinetics, then compare neat and Fe(III)-coordinated systems. | Next in the workflow |

## Where the model stands

The working model combines the bonded oligomer parameters with WCA + IBI03 and a weak attractive tail. In the nonbonded calibration system at 300 K and 1 atm, its mean density was **1.208 g/cm³**, compared with **1.201 g/cm³** for the atomistic reference. The larger linear-chain system reached approximately **1.251 g/cm³**. Its chain conformations relaxed more slowly than the density.

In the linear-chain bulk, chain pairs stayed associated longer than individual C1 sites. After a small step strain, the measured residual stress at 80–100 ps could not be resolved from zero. Together, these observations establish a baseline for testing what changes when disulfide connectivity can evolve.

The project pages contain selected figures from my thesis slides. The [Python example](examples/double_well_table.py) illustrates how to export an energy–force table using example parameters.
