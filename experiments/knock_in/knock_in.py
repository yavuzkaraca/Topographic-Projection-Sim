from build.config import SUBSTRATE_TYPE, CONTINUOUS_GRADIENTS, CONTINUOUS_SIGNAL_START, CONTINUOUS_SIGNAL_END, ROWS, COLS, GC_COUNT, \
    GC_SIZE, STEP_SIZE, \
    STEP_NUM, X_STEP_POSSIBILITY, Y_STEP_POSSIBILITY, SIGMA, FORCE, ADAPTATION_ENABLED, ADAPTATION_MU, \
    ADAPTATION_LAMBDA, ADAPTATION_HISTORY, SIGMOID_STEEPNESS, FORWARD_SIG, REVERSE_SIG, FF_INTER, FT_INTER, SIGMOID_SHIFT
from build import object_factory
import visualization as vz
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
    vz.visualize_projection_disjunctsets(result, simulation.substrate, mutated_gc_indexes)


#  Config
KNOCK_IN_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    CONTINUOUS_SIGNAL_START: 0.01,
    CONTINUOUS_SIGNAL_END: 0.99,
    ROWS: 3,
    COLS: 56,
    GC_COUNT: 50,
    GC_SIZE: 8,
    STEP_SIZE: 1,
    STEP_NUM: 5000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_STEEPNESS: 4,
    SIGMOID_SHIFT: 4,
    SIGMA: 0.12,
    FORCE: False,
    FORWARD_SIG: True,
    REVERSE_SIG: True,
    FF_INTER: True,
    FT_INTER: True,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 40  # 30
}


def run():
    knock_in()


if __name__ == '__main__':
    run()
