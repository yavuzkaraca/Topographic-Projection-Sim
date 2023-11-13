import object_factory
from src.visualization import visualize_result


def run():
    simulation = sim_builder.build_default()
    result = simulation.run()
    visualize_result(result)
    # print(result)


if __name__ == '__main__':
    run()
