from build.config import SUBSTRATE_TYPE, GAP_INV, CUSTOM_FIRST, CUSTOM_SECOND, ROWS, COLS, GC_COUNT, GC_SIZE, STEP_SIZE, \
    STEP_AMOUNT, X_STEP_POSSIBILITY, Y_STEP_POSSIBILITY, SIGMA, FORCE, ADAPTATION_ENABLED, ADAPTATION_MU, \
    ADAPTATION_LAMBDA, ADAPTATION_HISTORY, SIGMOID_GAIN, FORWARD_SIG, REVERSE_SIG, FF_INTER, FT_INTER
from build import object_factory
import visualization.visualization as vz


def adaptation_comparison():
    gc = []

    simulation = object_factory.build_simulation(GAP_INVERTED_CONFIG)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_CONFIG_HIGH_LAMBDA)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_CONFIG_HIGH_MU)
    simulation.run()
    gc.extend(simulation.growth_cones)

    gc[0].id = "Standard"
    gc[1].id = "High Lambda"
    gc[2].id = "High Mu"

    vz.visualize_adaptation(gc)


# Different Experiments

"""
Parameter investigation
"""
GAP_INVERTED_CONFIG = {
    SUBSTRATE_TYPE: GAP_INV,
    CUSTOM_FIRST: 0.35,
    CUSTOM_SECOND: 0.3,  # 0.3
    ROWS: 96,  # number of rows = max value along y-axis
    COLS: 96,  # number of cols = max value along x-axis
    GC_COUNT: 1,
    GC_SIZE: 5,
    STEP_SIZE: 1,
    STEP_AMOUNT: 140,  # 100
    X_STEP_POSSIBILITY: 1,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_GAIN: 8,
    SIGMA: 1,
    FORCE: True,
    FORWARD_SIG: True,
    REVERSE_SIG: True,
    FF_INTER: True,
    FT_INTER: True,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 20  # 30
}

GAP_INVERTED_CONFIG_HIGH_LAMBDA = {
    SUBSTRATE_TYPE: GAP_INV,
    CUSTOM_FIRST: 0.35,
    CUSTOM_SECOND: 0.3,  # 0.3
    ROWS: 96,  # number of rows = max value along y-axis
    COLS: 96,  # number of cols = max value along x-axis
    GC_COUNT: 1,
    GC_SIZE: 5,
    STEP_SIZE: 1,
    STEP_AMOUNT: 140,  # 100
    X_STEP_POSSIBILITY: 1,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_GAIN: 8,
    SIGMA: 1,
    FORCE: True,
    FORWARD_SIG: True,
    REVERSE_SIG: True,
    FF_INTER: True,
    FT_INTER: True,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.06,  # 0.06
    ADAPTATION_HISTORY: 20  # 30
}

GAP_INVERTED_CONFIG_HIGH_MU = {
    SUBSTRATE_TYPE: GAP_INV,
    CUSTOM_FIRST: 0.35,
    CUSTOM_SECOND: 0.3,  # 0.3
    ROWS: 96,  # number of rows = max value along y-axis
    COLS: 96,  # number of cols = max value along x-axis
    GC_COUNT: 1,
    GC_SIZE: 5,
    STEP_SIZE: 1,
    STEP_AMOUNT: 140,  # 100
    X_STEP_POSSIBILITY: 1,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_GAIN: 8,
    SIGMA: 1,
    FORCE: True,
    FORWARD_SIG: True,
    REVERSE_SIG: True,
    FF_INTER: True,
    FT_INTER: True,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.015,  # 0.015
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 20  # 30
}
