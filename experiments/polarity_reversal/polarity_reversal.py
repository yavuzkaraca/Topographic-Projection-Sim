from build.config import SUBSTRATE_TYPE, CONTINUOUS_GRADIENTS, CUSTOM_FIRST, CUSTOM_SECOND, ROWS, COLS, GC_COUNT, \
    GC_SIZE, STEP_SIZE, \
    STEP_AMOUNT, X_STEP_POSSIBILITY, Y_STEP_POSSIBILITY, SIGMA, FORCE, ADAPTATION_ENABLED, ADAPTATION_MU, \
    ADAPTATION_LAMBDA, ADAPTATION_HISTORY, SIGMOID_STEEPNESS, FORWARD_SIG, REVERSE_SIG, FF_INTER, FT_INTER, SIGMOID_SHIFT
from build import object_factory
import visualization as vz
import numpy as np

#  Config
POLARITY_REV_1_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    CUSTOM_FIRST: 0,
    CUSTOM_SECOND: 0,
    ROWS: 3,  # number of rows = max value along y-axis
    COLS: 12,  # number of cols = max value along x-axis
    GC_COUNT: 100,
    GC_SIZE: 1,
    STEP_SIZE: 1,
    STEP_AMOUNT: 2000,
    X_STEP_POSSIBILITY: 0.55,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_STEEPNESS: 4,
    SIGMOID_SHIFT: 100,
    SIGMA: 0.05,
    FORCE: False,
    FORWARD_SIG: True,
    REVERSE_SIG: True,
    FF_INTER: False,
    FT_INTER: True,
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
    COLS: 12,  # number of cols = max value along x-axis
    GC_COUNT: 100,
    GC_SIZE: 1,
    STEP_SIZE: 1,
    STEP_AMOUNT: 3000,
    X_STEP_POSSIBILITY: 0.55,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_STEEPNESS: 4,
    SIGMOID_SHIFT: 100,
    SIGMA: 0.05,
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


def polarity_reversal_two_halves():
    """
    Polarity reversal experiment with two nasal populations as waves that grow onto substrate in sequential order.
    :return:
    """
    # Fist Phase
    simulation = object_factory.build_simulation(POLARITY_REV_1_CONFIG)
    gc_len = int(len(simulation.growth_cones) / 2)
    gc_first = simulation.growth_cones[0:gc_len]
    vz.visualize_growth_cones(gc_first)

    simulation.growth_cones = gc_first
    result1 = simulation.run()

    vz.visualize_results_on_substrate(result1, simulation.substrate)
    vz.visualize_projection(result1, simulation.substrate, "First Wave of Growth Cones", True)

    # Stabilize gc_first
    for gc in gc_first:
        gc.freeze = True

    # Second Phase
    simulation = object_factory.build_simulation(POLARITY_REV_2_CONFIG)
    gc_second = simulation.growth_cones[0:gc_len]
    gcs = gc_first + gc_second
    vz.visualize_growth_cones(gcs)

    simulation.growth_cones = gcs
    result2 = simulation.run()

    vz.visualize_results_on_substrate(result2, simulation.substrate)
    vz.visualize_projection_disjunctsets(result2, simulation.substrate, np.arange(gc_len - 1 / 2),
                                         "Second Wave", "First Wave")


def run():
    polarity_reversal_two_halves()


if __name__ == '__main__':
    run()
