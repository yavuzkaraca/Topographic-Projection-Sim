from build import object_factory
import visualization as vz


def run():
    simulation = object_factory.build_default()
    vz.visualize_growth_cones(simulation.growth_cones)
    vz.visualize_substrate(simulation.substrate)
    vz.visualize_substrate_separately(simulation.substrate)

    result = simulation.run()

    vz.visualize_result(result,simulation.substrate)
    vz.visualize_results_on_substrate(result, simulation.substrate)
    vz.visualize_trajectory_on_substrate(result, simulation.substrate, simulation.growth_cones)
    vz.visualize_trajectories(simulation.growth_cones)


if __name__ == '__main__':
    run()



