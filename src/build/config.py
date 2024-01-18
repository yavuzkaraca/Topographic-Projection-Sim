"""
Module providing configuration settings for a retinotectal projection simulation.
"""

# Substrate Types
CONTINUOUS_GRADIENTS = "continuous_gradients"
WEDGES = "wedges"
STRIPE_FWD = "stripe_fwd"
STRIPE_REW = "stripe_rew"
STRIPE_DUO = "stripe_duo"
GAP_RR = "gap_rr"
GAP_RB = "gap_rb"
GAP_BR = "gap_br"
GAP_BB = "gap_bb"
GAP_INV = "gap_inv"

# Simulation Parameters
SUBSTRATE_TYPE = "substrate_type"

# small edge length ; - ; last column of first part
CUSTOM_FIRST = "custom_first"
# big edge length ; stripe width ; first column of last part
CUSTOM_SECOND = "custom_second"

ROWS = "rows"
COLS = "cols"
GC_COUNT = "gc_count"
GC_SIZE = "gc_size"
STEP_SIZE = "step_size"
STEP_AMOUNT = "step_amount"
X_STEP_POSSIBILITY = "x_step_possibility"
Y_STEP_POSSIBILITY = "y_step_possibility"
SIGMA = "sigma"
TRAJECTORY_FRQ = "trajectory_freq"  # TODO: integrate into object factory

# Adaptation
ADAPTATION_ENABLED = "adaptation_enabled"
ADAPTATION_MU = "adaptation_mu"
ADAPTATION_LAMBDA = "adaptation_lambda"
ADAPTATION_HISTORY = "adaptation_history"


# Default configuration values
CONTINUOUS_CONFIG = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    CUSTOM_FIRST: 0,
    CUSTOM_SECOND: 0,
    ROWS: 100,  # number of rows = max value along y-axis
    COLS: 100,  # number of cols = max value along x-axis
    GC_COUNT: 20,
    GC_SIZE: 5,
    STEP_SIZE: 1,
    STEP_AMOUNT: 16000,
    X_STEP_POSSIBILITY: 0.55,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY_FRQ: 50,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.006,  # 0.006
    ADAPTATION_LAMBDA: 0.0045,  # 0.0045
    ADAPTATION_HISTORY: 50
}

# Default configuration values
STRIPE_ASSAY_CONFIG = {
    SUBSTRATE_TYPE: STRIPE_DUO,
    CUSTOM_FIRST: 1,
    CUSTOM_SECOND: 12,
    ROWS: 150,  # number of rows = max value along y-axis
    COLS: 150,  # number of cols = max value along x-axis
    GC_COUNT: 10,
    GC_SIZE: 10,
    STEP_SIZE: 2,
    STEP_AMOUNT: 5000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY_FRQ: 50,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.006,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 10
}

# Default configuration values
WEDGES_CONFIG = {
    SUBSTRATE_TYPE: WEDGES,
    CUSTOM_FIRST: 1,
    CUSTOM_SECOND: 12,
    ROWS: 96,  # number of rows = max value along y-axis
    COLS: 96,  # number of cols = max value along x-axis
    GC_COUNT: 10,
    GC_SIZE: 10,
    STEP_SIZE: 1,
    STEP_AMOUNT: 20000,
    X_STEP_POSSIBILITY: 0.50,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY_FRQ: 50,
    ADAPTATION_ENABLED: False,
    ADAPTATION_MU: 0.006,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 10
}

# Default configuration values
GAP_ASSAY_CONFIG = {
    SUBSTRATE_TYPE: GAP_BB,
    CUSTOM_FIRST: 0.4,
    CUSTOM_SECOND: 0.2,  # 0.03
    ROWS: 96,  # number of rows = max value along y-axis
    COLS: 96,  # number of cols = max value along x-axis
    GC_COUNT: 5,
    GC_SIZE: 5,
    STEP_SIZE: 2,
    STEP_AMOUNT: 15000,  # 8000
    X_STEP_POSSIBILITY: 0.55,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMA: 0.12,
    TRAJECTORY_FRQ: 50,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,  # 0.006
    ADAPTATION_LAMBDA: 0.002,  # 0.0045
    ADAPTATION_HISTORY: 50  # 10
}


# Current configuration settings
default_config = CONTINUOUS_CONFIG

