
from src.substrate import Substrate  # Import the Substrate class from your substrate module
from src.visualization import visualize_substrate

from src.simulation import Simulation
import src.config as cfg

def run():
    simulation = Simulation(cfg.config)
    simulation.run()



if __name__ == '__main__':
    run()
