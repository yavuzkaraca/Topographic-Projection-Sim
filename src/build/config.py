"""
Module providing configuration settings for a retinotectal projection model.
"""

"""
--------------------------------------
        CONFIGURATION KEYS
--------------------------------------
"""

# Simulation Basic Parameters
GC_COUNT = "gc_count"
GC_SIZE = "gc_size"
STEP_SIZE = "step_size"
STEP_AMOUNT = "step_amount"

# Simulation Advanced Parameters
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


# Adaptation
ADAPTATION_ENABLED = "adaptation_enabled"
ADAPTATION_MU = "adaptation_mu"
ADAPTATION_LAMBDA = "adaptation_lambda"
ADAPTATION_HISTORY = "adaptation_history"


# Substrate Types
CONTINUOUS_GRADIENTS = "continuous_gradients"
WEDGES = "wedges"
STRIPE = "stripe"
GAP = "gap"
GAP_INV = "gap_inv"

# Substrate Parameters
SUBSTRATE_TYPE = "substrate_type"
ROWS = "rows"
COLS = "cols"
# -----------   Continuous  -----------
CONTINUOUS_SIGNAL_START = "continuous_signal_start"
CONTINUOUS_SIGNAL_END = "continuous_signal_end"
# -----------   Wedges  -----------
WEDGE_NARROW_EDGE = "wedge_narrow_edge"
WEDGE_WIDE_EDGE = "wedge_wedge"
# -----------   Stripe Assay  -----------
STRIPE_FWD = "stripe_fwd"
STRIPE_REW = "stripe_rew"
STRIPE_CONC = "stripe_conc"
STRIPE_WIDTH = "stripe_width"
# -----------   Gap Assay   -----------
GAP_BEGIN = "gap_begin"
GAP_END = "gap_end"
LIGAND = "ligand"
RECEPTOR = "receptor"
GAP_FIRST_BLOCK = "gap_first_block"
GAP_SECOND_BLOCK = "gap_second_block"

"""
--------------------------------------
        CONFIGURATION MODULES
--------------------------------------
"""

simulation_basic = {
    GC_COUNT: 20,
    GC_SIZE: 3,
    STEP_SIZE: 1,
    STEP_AMOUNT: 8000,
}

simulation_advanced = {
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

adaptation = {
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.01,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 50
}

# Substrates

continuous_substrate = {
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    ROWS: 100,
    COLS: 100,
    CONTINUOUS_SIGNAL_START: 0.01,
    CONTINUOUS_SIGNAL_END: 6.99
}

wedges_substrate = {
    SUBSTRATE_TYPE: WEDGES,
    ROWS: 96,
    COLS: 96,
    WEDGE_NARROW_EDGE: 1,
    WEDGE_WIDE_EDGE: 12
}

stripe_substrate = {
    SUBSTRATE_TYPE: STRIPE,
    ROWS: 150,
    COLS: 150,
    STRIPE_FWD: True,
    STRIPE_REW: True,
    STRIPE_CONC: 1,
    STRIPE_WIDTH: 12
}

gap_substrate = {
    SUBSTRATE_TYPE: GAP,
    ROWS: 96,
    COLS: 96,
    GAP_BEGIN: 0.5,
    GAP_END: 0.1,
    GAP_FIRST_BLOCK: LIGAND,
    GAP_SECOND_BLOCK: RECEPTOR
}

gap_inv_substrate = {
    SUBSTRATE_TYPE: GAP_INV,
    ROWS: 46,
    COLS: 166,
    GAP_BEGIN: 0.4,
    GAP_END: 0.3,
    GAP_FIRST_BLOCK: RECEPTOR,
}

"""
--------------------------------------
        DEFAULT CONFIGURATIONS
--------------------------------------
"""

continuous_config = {
    GC_COUNT: 100,
    GC_SIZE: 3,
    STEP_SIZE: 1,
    STEP_AMOUNT: 8000,
    **simulation_advanced,
    **adaptation,
    **continuous_substrate
}

wedges_config = {
    GC_COUNT: 10,
    GC_SIZE: 10,
    STEP_SIZE: 1,
    STEP_AMOUNT: 8000,
    **simulation_advanced,
    ADAPTATION_ENABLED: False,
    **wedges_substrate
}

stripe_config = {
    GC_COUNT: 10,
    GC_SIZE: 10,
    STEP_SIZE: 1,
    STEP_AMOUNT: 8000,
    **simulation_advanced,
    ADAPTATION_ENABLED: False,
    **stripe_substrate
}

gap_config = {
    GC_COUNT: 5,
    GC_SIZE: 5,
    STEP_SIZE: 2,
    STEP_AMOUNT: 8000,
    **simulation_advanced,
    **adaptation,
    **gap_substrate
}

"""
--------------------------------------
        CUSTOM CONFIGURATION
--------------------------------------
"""

custom_config = {
    GC_COUNT: 15,
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
    FT_INTER: True,
    ADAPTATION_ENABLED: True,
    ADAPTATION_MU: 0.006,
    ADAPTATION_LAMBDA: 0.0045,
    ADAPTATION_HISTORY: 50,
    SUBSTRATE_TYPE: CONTINUOUS_GRADIENTS,
    ROWS: 100,
    COLS: 100,
    CONTINUOUS_SIGNAL_START: 0.01,
    CONTINUOUS_SIGNAL_END: 1
}

"""
--------------------------------------
        CURRENT CONFIGURATION
--------------------------------------
"""

# Current configuration
current_config = custom_config




