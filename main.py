import object_factory
from src.visualization import visualize_result


def run():
    simulation = object_factory.build_default()
    result = simulation.run()
    visualize_result(result)


if __name__ == '__main__':
    run()
