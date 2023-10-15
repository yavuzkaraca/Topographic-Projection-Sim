from substrate import Substrate  # Import the Substrate class from your substrate module

def run():


    # Example configuration for initializing wedges
    config_dict = {
        "substrate_type": "wedges",
        "min_edge_length": 3,  # Adjust the edge lengths as needed
        "max_edge_length": 6,
    }

    # Create a Substrate instance with your desired rows and columns
    rows = 6
    cols = 30
    substrate = Substrate(rows, cols, config_dict)

    # Assign the configuration dictionary to the Substrate


    # Initialize the substrate with wedges
    substrate.initialize_substrate()

    # Print the substrate
    print(substrate)


if __name__ == '__main__':
    run()
