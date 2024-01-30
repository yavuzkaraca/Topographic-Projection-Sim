from experiments.adap_investigation.four_plots_comparison import (adaptation_comparison_lambda, adaptation_comparison_mu,
                                                                  adaptation_comparison_history)

from build import object_factory
import src.visualization as vz
import build.config as cfg


def run():
    simulation = object_factory.build_default()
    vz.visualize_substrate(simulation.substrate)

    result = simulation.run()

    # dirty fix
    trajectory_freq = cfg.default_config.get(cfg.TRAJECTORY_FRQ)  # TODO: Visualization Object

    vz.visualize_result(result, simulation.substrate)
    vz.visualize_results_on_substrate(result, simulation.substrate)
    vz.visualize_trajectory_on_substrate(result, simulation.substrate, simulation.growth_cones, trajectory_freq)

    # vz.visualize_substrate_separately(simulation.substrate)
    # vz.visualize_trajectories(simulation.growth_cones)


if __name__ == '__main__':
    run()
