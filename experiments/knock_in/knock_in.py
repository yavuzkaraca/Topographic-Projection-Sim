from matplotlib import pyplot as plt

from build.config import SUBSTRATE_TYPE, CONTINUOUS_GRADIENTS, CUSTOM_FIRST, CUSTOM_SECOND, ROWS, COLS, GC_COUNT, \
    GC_SIZE, STEP_SIZE, \
    STEP_AMOUNT, X_STEP_POSSIBILITY, Y_STEP_POSSIBILITY, SIGMA, FORCE, ADAPTATION_ENABLED, ADAPTATION_MU, \
    ADAPTATION_LAMBDA, ADAPTATION_HISTORY, SIGMOID_GAIN
from build import object_factory
import visualization.visualization as vz
import numpy as np


def knock_in():
    simulation = object_factory.build_simulation(KNOCK_IN_CONFIG)

    gcs = simulation.growth_cones

    vz.visualize_growth_cones(gcs)

    # mutate half of gcs
    mutation_factor = 1.2
    mutated_gc_indexes = np.random.choice(range(0, 49), size=25, replace=False)
    for idx in mutated_gc_indexes:
        gcs[idx].mutate(mutation_factor)

    vz.visualize_growth_cones(gcs)

    result = simulation.run()

    vz.visualize_results_on_substrate(result, simulation.substrate)
    vz.visualize_colored_result(result, simulation.substrate, mutated_gc_indexes)


#  Config
KNOCK_IN_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    CUSTOM_FIRST: 0,
    CUSTOM_SECOND: 0,
    ROWS: 3,  # number of rows = max value along y-axis
    COLS: 56,  # number of cols = max value along x-axis
    GC_COUNT: 50,
    GC_SIZE: 8,
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


def run():
    knock_in()


if __name__ == '__main__':
    run()
