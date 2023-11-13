import object_factory
import src.visualization as vz


def run():
    simulation = object_factory.build_default()
    result = simulation.run()
    vz.visualize_result(result)
    vz.visualize_substrate_and_positions(simulation.substrate, result)


if __name__ == '__main__':
    run()
