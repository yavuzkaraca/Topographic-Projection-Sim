from build import object_factory
import src.visualization as vz
import build.config as cfg


def adaptation_comparison():
    gc = []

    simulation = object_factory.build_simulation(cfg.GAP_INVERTED_CONFIG)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(cfg.GAP_INVERTED_CONFIG_HIGH_LAMBDA)
    simulation.run()
    gc.extend(simulation.growth_cones)

    simulation = object_factory.build_simulation(cfg.GAP_INVERTED_CONFIG_HIGH_MU)
    simulation.run()
    gc.extend(simulation.growth_cones)

    gc[0].id = "Standard"
    gc[1].id = "High Lambda"
    gc[2].id = "High Mu"

    vz.visualize_adaptation(gc)


def run():
    simulation = object_factory.build_default()
    vz.visualize_substrate(simulation.substrate)

    result = simulation.run()

    # dirty fix
    trajectory_freq = cfg.default_config.get(cfg.TRAJECTORY_FRQ)

    vz.visualize_result(result, simulation.substrate)
    vz.visualize_results_on_substrate(result, simulation.substrate)
    vz.visualize_trajectory_on_substrate(result, simulation.substrate, simulation.growth_cones, trajectory_freq)

    # vz.visualize_substrate_separately(simulation.substrate)
    # vz.visualize_trajectories(simulation.growth_cones)


if __name__ == '__main__':
    run()
    adaptation_comparison()
