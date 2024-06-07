from build import object_factory, config
import visualization as vz
from build.config import ADAPTATION_ENABLED, ADAPTATION_MU, ADAPTATION_LAMBDA, ADAPTATION_HISTORY

simulation_config = {
    config.GC_COUNT: 1,
    config.GC_SIZE: 5,
    config.STEP_SIZE: 1,
    config.STEP_AMOUNT: 250,
    config.X_STEP_POSSIBILITY: 1,
    config.Y_STEP_POSSIBILITY: 0.50,
    config.SIGMOID_STEEPNESS: 4,
    config.SIGMOID_SHIFT: 3,
    config.SIGMA: 1,
    config.FORCE: True,
    config.FORWARD_SIG: True,
    config.REVERSE_SIG: True,
    config.FF_INTER: True,
    config.FT_INTER: True,
}

substrate_config = config.gap_inv_substrate


def adaptation_comparison_lambda():
    gc = []

    simulation = object_factory.build_simulation(GAP_INVERTED_LAMBDA_1)

    vz.visualize_substrate(simulation.substrate)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_LAMBDA_2)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_LAMBDA_3)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_LAMBDA_4)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_LAMBDA_5)
    simulation.run()
    gc.extend(simulation.growth_cones)

    gc[0].id = "Very Low Lambda"
    gc[1].id = "Low Lambda"
    gc[2].id = "Control"
    gc[3].id = "High Lambda"
    gc[4].id = "Very High Lambda"

    vz.visualize_adaptation(gc)


GAP_INVERTED_LAMBDA_1 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0002,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}

GAP_INVERTED_LAMBDA_2 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.001,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}

GAP_INVERTED_LAMBDA_3 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.005,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}

GAP_INVERTED_LAMBDA_4 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.025,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}

GAP_INVERTED_LAMBDA_5 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.125,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}


def adaptation_comparison_mu():
    gc = []

    simulation = object_factory.build_simulation(GAP_INVERTED_MU_1)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_MU_2)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_MU_3)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_MU_4)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_MU_5)
    simulation.run()
    gc.extend(simulation.growth_cones)

    gc[0].id = "Very Low Mu"
    gc[1].id = "Low Mu"
    gc[2].id = "Control"
    gc[3].id = "High Mu"
    gc[4].id = "Very High Mu"

    vz.visualize_adaptation(gc)


GAP_INVERTED_MU_1 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.002,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}

GAP_INVERTED_MU_2 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.005,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}

GAP_INVERTED_MU_3 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}

GAP_INVERTED_MU_4 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.02,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}

GAP_INVERTED_MU_5 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.05,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 30  # 30
}


def adaptation_comparison_history():
    gc = []

    simulation = object_factory.build_simulation(GAP_INVERTED_HISTORY_1)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_HISTORY_2)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_HISTORY_3)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_HISTORY_4)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(GAP_INVERTED_HISTORY_5)
    simulation.run()
    gc.extend(simulation.growth_cones)

    gc[0].id = "Very Short History"
    gc[1].id = "Short History"
    gc[2].id = "Control"
    gc[3].id = "Long History"
    gc[4].id = "Very Long History"

    vz.visualize_adaptation(gc)


GAP_INVERTED_HISTORY_1 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 1  # 30
}

GAP_INVERTED_HISTORY_2 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 10  # 30
}

GAP_INVERTED_HISTORY_3 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 20  # 30
}

GAP_INVERTED_HISTORY_4 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 40  # 30
}

GAP_INVERTED_HISTORY_5 = {
    **simulation_config,
    **substrate_config,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.01
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 60  # 30
}


def run():
    adaptation_comparison_lambda()
    adaptation_comparison_mu()
    adaptation_comparison_history()


if __name__ == '__main__':
    run()

