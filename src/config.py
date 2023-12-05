"""
Module providing configuration settings for a retinotectal projection simulation.
"""

# Substrate Types
CONTINUOUS_GRADIENTS = "continuous_gradients"
WEDGES = "wedges"
STRIPE_FWD = "stripe_fwd"
STRIPE_REW = "stripe_rew"
STRIPE_DUO = "stripe_duo"
GAP = "gap"

# Simulation Parameters
SUBSTRATE_TYPE = "substrate_type"
MIN_VALUE = "min_value"
MAX_VALUE = "max_value"
ROWS = "rows"
COLS = "cols"
OFFSET = "offset"
GC_COUNT = "gc_count"
GC_SIZE = "gc_size"
STEP_SIZE = "step_size"
STEP_AMOUNT = "step_amount"
X_STEP_POSSIBILITY = "x_step_possibility"
Y_STEP_POSSIBILITY = "y_step_possibility"
SIGMA = "sigma"
TRAJECTORY = "trajectory"

# Adaptation
ADAPTATION_ENABLED = "adaptation_enabled"
ADAPTATION_MU = "adaptation_mu"
ADAPTATION_LAMBDA = "adaptation_lambda"
ADAPTATION_HISTORY = "adaptation_history"

# Stipe Assay configuration values
STRIPE_ASSAY_CONFIG = {
    SUBSTRATE_TYPE: STRIPE_DUO,
    MIN_VALUE: 1,
    MAX_VALUE: 12,
    ROWS: 150,  # number of rows = max value along y-axis
    COLS: 150,  # number of cols = max value along x-axis
    OFFSET: 5,  # should equal gc_size
    GC_COUNT: 10,
    GC_SIZE: 10,
    STEP_SIZE: 2,
    STEP_AMOUNT: 5000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY: 100,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.006,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 10
}

# Default configuration values
WEDGES_CONFIG = {
    SUBSTRATE_TYPE: WEDGES,
    MIN_VALUE: 1,
    MAX_VALUE: 12,
    ROWS: 96,  # number of rows = max value along y-axis
    COLS: 96,  # number of cols = max value along x-axis
    OFFSET: 10,  # should equal gc_size
    GC_COUNT: 10,
    GC_SIZE: 10,
    STEP_SIZE: 1,
    STEP_AMOUNT: 20000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY: 100,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.006,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 10
}

GAP_ASSAY_CONFIG = {
    SUBSTRATE_TYPE: GAP,
    MIN_VALUE: 3,
    MAX_VALUE: 2,
    ROWS: 96,  # number of rows = max value along y-axis
    COLS: 96,  # number of cols = max value along x-axis
    OFFSET: 5,  # should equal gc_size
    GC_COUNT: 5,
    GC_SIZE: 10,
    STEP_SIZE: 2,
    STEP_AMOUNT: 20000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY: 100,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.006,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 10
}


# Default configuration values
DEFAULT_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    MIN_VALUE: 0,
    MAX_VALUE: 0,
    ROWS: 100,  # number of rows = max value along y-axis
    COLS: 100,  # number of cols = max value along x-axis
    OFFSET: 10,  # should equal gc_size
    GC_COUNT: 5,
    GC_SIZE: 10,
    STEP_SIZE: 1,
    STEP_AMOUNT: 20000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY: 100,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.006,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 10
}

# Current configuration settings
config = GAP_ASSAY_CONFIG
