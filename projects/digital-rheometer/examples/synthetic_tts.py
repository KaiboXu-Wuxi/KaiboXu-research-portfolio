"""Plot time–temperature superposition for synthetic relaxation curves."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

REFERENCE_TEMPERATURE = 333.15  # kelvin
ACTIVATION_ENERGY = 50_000.0  # joules per mole
GAS_CONSTANT = 8.314462618  # joules per mole kelvin


def shift_factor(temperature):
    inverse_temperature_difference = 1.0 / temperature - 1.0 / REFERENCE_TEMPERATURE
    return np.exp(ACTIVATION_ENERGY / GAS_CONSTANT * inverse_temperature_difference)


def relaxation_modulus(reduced_time):
    return np.exp(-((reduced_time / 20.0) ** 0.65))


def main(output_path):
    time = np.geomspace(0.1, 1000.0, 180)
    figure, (raw, shifted) = plt.subplots(
        1, 2, figsize=(9.2, 3.9), sharey=True, layout="constrained"
    )
    figure.suptitle("Time–temperature superposition with synthetic data", fontsize=13)

    for celsius, color, linestyle in zip(
        (40, 60, 80), ("#1966a0", "#a94727", "#177451"), ("-", "--", ":")
    ):
        reduced_time = time / shift_factor(celsius + 273.15)
        modulus = relaxation_modulus(reduced_time)
        style = dict(color=color, linestyle=linestyle, linewidth=2)
        raw.semilogx(time, modulus, label=f"{celsius} °C", **style)
        shifted.semilogx(reduced_time, modulus, **style)

    raw.set(title="Before shifting", xlabel="Time (s)", ylabel="Normalized modulus")
    shifted.set(title="After shifting", xlabel="Reduced time, t/aT (s)")
    raw.legend(frameon=False)
    for axis in (raw, shifted):
        axis.set(xlim=(0.1, 1000), ylim=(-0.02, 1.03))
        axis.grid(alpha=0.22)
    figure.savefig(output_path)
    plt.close(figure)


if __name__ == "__main__":
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("synthetic-master-curve.svg")
    main(output)
