"""
Module providing configuration settings for a retinotectal projection model.
"""

# Substrate Types
CONTINUOUS_GRADIENTS = "continuous_gradients"
WEDGES = "wedges"
STRIPE = "stripe"
GAP = "gap"
GAP_INV = "gap_inv"

# Common Substrate Parameters
ROWS = "rows"
COLS = "cols"
# Continuous
CONTINUOUS_SIGNAL_START = "continuous_signal_start"
CONTINUOUS_SIGNAL_END = "continuous_signal_end"
# Wedge
WEDGE_NARROW_EDGE = "wedge_narrow_edge"
WEDGE_WIDE_EDGE = "wedge_wedge"
# Stripe
STRIPE_FWD = "stripe_fwd"
STRIPE_REW = "stripe_rew"
STRIPE_CONC = "stripe_conc"
STRIPE_WIDTH = "stripe_width"
# Gap
GAP_BEGIN = "gap_begin"
GAP_END = "gap_end"
LIGAND = "ligand"
RECEPTOR = "receptor"
GAP_FIRST_BLOCK = "gap_first_block"
GAP_SECOND_BLOCK = "gap_second_block"


# Substrate Configurations
substrate_configs = {
    CONTINUOUS_GRADIENTS: {
        ROWS: 100,
        COLS: 100,
        CONTINUOUS_SIGNAL_START: 0,
        CONTINUOUS_SIGNAL_END: 1
    },
    WEDGES: {
        ROWS: 96,
        COLS: 96,
        WEDGE_NARROW_EDGE: 1,
        WEDGE_WIDE_EDGE: 12
    },
    STRIPE: {
        ROWS: 150,
        COLS: 150,
        STRIPE_FWD: True,
        STRIPE_REW: True,
        STRIPE_CONC: 1,
        STRIPE_WIDTH: 12,
    },
    GAP: {
        ROWS: 96,
        COLS: 96,
        GAP_BEGIN: 0.4,
        GAP_END: 0.2,
        GAP_FIRST_BLOCK: LIGAND,
        GAP_SECOND_BLOCK: RECEPTOR,
    },
    GAP_INV: {
        ROWS: 46,
        COLS: 166,
        GAP_BEGIN: 0.4,
        GAP_END: 0.3,
        GAP_FIRST_BLOCK: LIGAND
    }
}

# Simulation Parameters
GC_COUNT = "gc_count"
GC_SIZE = "gc_size"
STEP_SIZE = "step_size"
STEP_AMOUNT = "step_amount"
X_STEP_POSSIBILITY = "x_step_possibility"
Y_STEP_POSSIBILITY = "y_step_possibility"
SIGMOID_STEEPNESS = "sigmoid_gain"
SIGMOID_SHIFT = "sigmoid_shift"
SIGMA = "sigma"
FORCE = "force"
FORWARD_SIG = "forward_sig"
REVERSE_SIG = "reverse_sig"
FF_INTER = "ff_inter"
FT_INTER = "ft_inter"

simulation_config = {
    GC_COUNT: 100,
    GC_SIZE: 3,
    STEP_SIZE: 1,
    STEP_AMOUNT: 8000,
    X_STEP_POSSIBILITY: 0.55,
    Y_STEP_POSSIBILITY: 0.50,
    SIGMOID_STEEPNESS: 4,
    SIGMOID_SHIFT: 3,
    SIGMA: 0.12,
    FORCE: False,
    FORWARD_SIG: True,
    REVERSE_SIG: True,
    FF_INTER: True,
    FT_INTER: True
}

# Adaptation
ADAPTATION_ENABLED = "adaptation_enabled"
ADAPTATION_MU = "adaptation_mu"
ADAPTATION_LAMBDA = "adaptation_lambda"
ADAPTATION_HISTORY = "adaptation_history"

adaptation_config = {
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.006,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 50
}

"""
--------------------------------------
        DEFAULT CONFIGURATIONS
--------------------------------------
"""

default_configs = {
    CONTINUOUS_GRADIENTS: {**simulation_config, **adaptation_config, **substrate_configs[CONTINUOUS_GRADIENTS]},
    WEDGES: {**simulation_config, **adaptation_config, **substrate_configs[WEDGES]},
    STRIPE: {**simulation_config, **adaptation_config, **substrate_configs[STRIPE]},
    GAP: {**simulation_config, **adaptation_config, **substrate_configs[GAP]}
}

# Current default configuration
default_config = default_configs[CONTINUOUS_GRADIENTS]


