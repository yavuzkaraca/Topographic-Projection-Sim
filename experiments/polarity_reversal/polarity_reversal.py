from build.config import SUBSTRATE_TYPE, CONTINUOUS_GRADIENTS, CUSTOM_FIRST, CUSTOM_SECOND, ROWS, COLS, GC_COUNT, \
    GC_SIZE, STEP_SIZE, \
    STEP_AMOUNT, X_STEP_POSSIBILITY, Y_STEP_POSSIBILITY, SIGMA, FORCE, ADAPTATION_ENABLED, ADAPTATION_MU, \
    ADAPTATION_LAMBDA, ADAPTATION_HISTORY, SIGMOID_GAIN
from build import object_factory
import visualization.visualization as vz
import numpy as np


def polarity_reversal():
    # Fist Phase
    simulation = object_factory.build_simulation(POLARITY_REV_1_CONFIG)
    gc_first = simulation.growth_cones[0:25]
    vz.visualize_growth_cones(gc_first)

    simulation.growth_cones = gc_first
    result1 = simulation.run()

    vz.visualize_results_on_substrate(result1, simulation.substrate)
    vz.visualize_colored_result(result1, simulation.substrate, [])

    # Stabilize gc_first
    for gc in gc_first:
        gc.potential = 0

    # Second Phase
    simulation = object_factory.build_simulation(POLARITY_REV_2_CONFIG)
    gc_second = simulation.growth_cones[0:25]
    gcs = gc_first + gc_second
    vz.visualize_growth_cones(gcs)

    simulation.growth_cones = gcs
    result2 = simulation.run()

    vz.visualize_results_on_substrate(result2, simulation.substrate)
    vz.visualize_colored_result(result2, simulation.substrate, [])


#  Config
POLARITY_REV_1_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    CUSTOM_FIRST: 0,
    CUSTOM_SECOND: 0,
    ROWS: 3,  # number of rows = max value along y-axis
    COLS: 56,  # number of cols = max value along x-axis
    GC_COUNT: 50,
    GC_SIZE: 5,
    STEP_SIZE: 1,
    STEP_AMOUNT: 10000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_GAIN: 8,
    SIGMA: 0.12,
    FORCE: False,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 40  # 30
}

POLARITY_REV_2_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    CUSTOM_FIRST: 0,
    CUSTOM_SECOND: 0,
    ROWS: 3,  # number of rows = max value along y-axis
    COLS: 56,  # number of cols = max value along x-axis
    GC_COUNT: 50,
    GC_SIZE: 5,
    STEP_SIZE: 1,
    STEP_AMOUNT: 10000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_GAIN: 100,
    SIGMA: 0.12,
    FORCE: False,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 40  # 30
}


def run():
    polarity_reversal()


if __name__ == '__main__':
    run()
