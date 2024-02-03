from build.config import SUBSTRATE_TYPE, CONTINUOUS_GRADIENTS, CUSTOM_FIRST, CUSTOM_SECOND, ROWS, COLS, GC_COUNT, \
    GC_SIZE, STEP_SIZE, \
    STEP_AMOUNT, X_STEP_POSSIBILITY, Y_STEP_POSSIBILITY, SIGMA, TRAJECTORY_FRQ, ADAPTATION_ENABLED, ADAPTATION_MU, \
    ADAPTATION_LAMBDA, ADAPTATION_HISTORY
from build import object_factory
import src.visualization as vz
import numpy as np


def knock_in():
    simulation = object_factory.build_simulation(KNOCK_IN_CONFIG)

    # mutate half of gcs
    mutated_gc_indexes = np.random.choice(range(0, 49), size=25, replace=False)
    extra_receptor = 0.5
    for idx in mutated_gc_indexes:
        simulation.growth_cones[idx].receptor_current += extra_receptor

    result = simulation.run()

    vz.visualize_results_on_substrate(result, simulation.substrate)
    vz.visualize_colored_result(result, simulation.substrate, mutated_gc_indexes)


#  Config
KNOCK_IN_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    CUSTOM_FIRST: 0,
    CUSTOM_SECOND: 0,
    ROWS: 3,  # number of rows = max value along y-axis
    COLS: 96,  # number of cols = max value along x-axis
    GC_COUNT: 50,
    GC_SIZE: 5,
    STEP_SIZE: 1,
    STEP_AMOUNT: 15000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY_FRQ: 1,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 40  # 30
}


def run():
    knock_in()


if __name__ == '__main__':
    run()
