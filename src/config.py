CONTINUOUS_GRADIENTS = "continuous_gradients"
WEDGES = "wedges"

SUBSTRATE_TYPE = "substrate_type"
MIN_VALUE = "min_value"
MAX_VALUE = "max_value"
ROWS = "row"
COLS = "cols"
ADAPTATION = "adaptation_enabled"
GC_COUNT = "gc_count"
GC_SIZE = "gc_size"
STEP_SIZE = "step_size"
STEP_AMOUNT = "step_amount"
X_STEP_POSSIBILITY = "x_step_possibility"
Y_STEP_POSSIBILITY = "y_step_possibility"
SIGMA = "sigma"

# Default configuration values
DEFAULT_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    MIN_VALUE: 2,
    MAX_VALUE: 40,
    ROWS: 50,
    COLS: 100,
    ADAPTATION: False,
    GC_COUNT: 10,
    GC_SIZE: 10,
    STEP_SIZE: 2,
    STEP_AMOUNT: 30000,
    X_STEP_POSSIBILITY: 0.45,
    Y_STEP_POSSIBILITY: 0.25,
    SIGMA: 1.0
}

# Current configuration settings
config = DEFAULT_CONFIG

