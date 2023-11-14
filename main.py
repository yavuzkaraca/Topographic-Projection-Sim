import object_factory
import src.visualization as vz


def run():
    simulation = object_factory.build_default()
    vz.visualize_substrate_separately(simulation.substrate)
    vz.visualize_substrate(simulation.substrate)

    result = simulation.run()
    vz.visualize_result(result)
    vz.visualize_results_on_substrate(result, simulation.substrate)


if __name__ == '__main__':
    run()
