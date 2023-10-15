CONTINUOUS_GRADIENTS = "continuous_gradients"
WEDGES = "wedges"

# Default configuration values
DEFAULT_CONFIG = {
    "substrate_type": WEDGES,
    "min_value": 2,
    "max_value": 40,
    "adaptation_enabled": False,
    "gc_count": 10,
    "gc_size": 10,
    "step_size": 5,
    "step_amount": 3000,
    "x_step_possibility": 0.33,
    "y_step_possibility": 0.25,
    "sigma": 1.0
}


# Function to read configuration from a file (e.g., JSON, YAML)
def read_config(filename):
    # Implement reading from a file and return a dictionary
    pass


# Function to write configuration to a file
def write_config(filename, config):
    # Implement writing to a file
    pass


# Function to merge user-provided configuration with defaults
def merge_config(user_config):
    config = DEFAULT_CONFIG.copy()
    config.update(user_config)
    return config
