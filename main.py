from build import object_factory
import visualization as vz


def run():
    simulation = object_factory.build_default()
    vz.visualize_growth_cones(simulation.growth_cones).show()
    vz.visualize_substrate(simulation.substrate).show()
    vz.visualize_substrate_separately(simulation.substrate).show()

    result = simulation.run()

    vz.visualize_projection(result, simulation.substrate).show()
    vz.visualize_results_on_substrate(result, simulation.substrate).show()
    vz.visualize_trajectory_on_substrate(result, simulation.substrate, simulation.growth_cones).show()
    vz.visualize_trajectories(simulation.growth_cones).show()
    vz.visualize_adaptation(simulation.growth_cones).show()


if __name__ == '__main__':
    run()



