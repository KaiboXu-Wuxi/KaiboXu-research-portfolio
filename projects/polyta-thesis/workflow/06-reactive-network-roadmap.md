[← Poly(TA) project](../README.md)

# 6. Reactive-network comparison

The thesis slides document the force field, fixed-topology linear-chain bulk, contact statistics, and small-strain baseline. The next comparison tests how an evolving covalent topology changes those observables.

| Step | Work to carry forward |
| --- | --- |
| Define a neat poly(TA) reactive system | Specify reactive sulfur sites and allowed ring opening, ring closure, and inter-chain disulfide exchange. Track rings, chain sizes, and connectivity as reactions change the topology. |
| Couple molecular dynamics and kinetic Monte Carlo | Use MD to sample conformations and KMC to select eligible reaction events. Establish how event eligibility, rates, and the MD interval affect reaction counts and connectivity. |
| Compare fixed and reactive topologies | Use the linear-chain bulk and the signed-strain protocol as baselines. Measure contact persistence and stress relaxation under comparable conditions. |
| Extend to Fe(III) coordination | Add a coordinated comparison system to test how carboxylate associations affect structure and relaxation alongside reversible disulfide chemistry. |

Other force-field checks include the sensitivity to the attractive tail, a larger timestep and speed benchmark, and comparison of the WCA- and LJ-based models over a wider range of conditions.
