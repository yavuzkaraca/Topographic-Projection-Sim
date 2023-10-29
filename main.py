from src.substrate import Substrate  # Import the Substrate class from your substrate module
from src.visualization import visualize_substrate, visualize_result

from src.simulation import Simulation
import src.config as cfg


def run():
    simulation = Simulation(cfg.config)
    result = simulation.run()
    visualize_result(result)
    # print(result)


if __name__ == '__main__':
    run()
