from src.substrate import Substrate  # Import the Substrate class from your substrate module
from src.visualization import visualize_substrate
import matplotlib.pyplot as plt

def run():

    # Create a Substrate instance with your desired rows and columns
    rows = 140
    cols = 140
    substrate = Substrate(rows, cols)

    # Assign the configuration dictionary to the Substrate


    # Initialize the substrate with wedges
    substrate.initialize_substrate()

    # Print the substrate
    print(substrate)

    visualize_substrate(substrate)



if __name__ == '__main__':
    run()
