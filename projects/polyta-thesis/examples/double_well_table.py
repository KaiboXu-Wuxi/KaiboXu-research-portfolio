"""Write an illustrative distance, energy, and force table to stdout."""

import csv
import sys

LEFT_MINIMUM = 2.2  # angstrom
RIGHT_MINIMUM = 2.8  # angstrom
ENERGY_SCALE = 100.0  # kcal mol^-1 angstrom^-4


def energy_and_force(distance):
    """Return the quartic double-well energy and its negative derivative."""
    left = distance - LEFT_MINIMUM
    right = distance - RIGHT_MINIMUM
    energy = ENERGY_SCALE * (left * right) ** 2
    force = -2.0 * ENERGY_SCALE * left * right * (left + right)
    return energy, force


def main():
    writer = csv.writer(sys.stdout)
    writer.writerow(["distance_A", "energy_kcal_per_mol", "force_kcal_per_mol_A"])
    for index in range(141):
        distance = 1.8 + index * 0.01
        energy, force = energy_and_force(distance)
        writer.writerow([f"{distance:.2f}", f"{energy:.8f}", f"{force:.8f}"])


if __name__ == "__main__":
    main()
