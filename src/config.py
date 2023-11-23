"""
Module providing configuration settings for a retinotectal projection simulation.
"""

# Configuration keys
CONTINUOUS_GRADIENTS = "continuous_gradients"
WEDGES = "wedges"
STRIPE_FWD = "stripe_fwd"
STRIPE_REW = "stripe_rew"
STRIPE_DUO = "stripe_duo"

SUBSTRATE_TYPE = "substrate_type"
MIN_VALUE = "min_value"
MAX_VALUE = "max_value"
ROWS = "rows"
COLS = "cols"
OFFSET = "offset"
ADAPTATION = "adaptation_enabled"
GC_COUNT = "gc_count"
GC_SIZE = "gc_size"
STEP_SIZE = "step_size"
STEP_AMOUNT = "step_amount"
X_STEP_POSSIBILITY = "x_step_possibility"
Y_STEP_POSSIBILITY = "y_step_possibility"
SIGMA = "sigma"
TRAJECTORY = "trajectory"

# Default configuration values
DEFAULT_CONFIG = {
    SUBSTRATE_TYPE: WEDGES,
    MIN_VALUE: 1,
    MAX_VALUE: 12,
    ROWS: 100,  # number of rows = max value along y-axis
    COLS: 100,  # number of cols = max value along x-axis
    OFFSET: 10,  # should equal gc_size
    ADAPTATION: False,
    GC_COUNT: 10,
    GC_SIZE: 10,
    STEP_SIZE: 1,
    STEP_AMOUNT: 20000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY: 100
}

# Current configuration settings
config = DEFAULT_CONFIG
