"""
Module for setting up all the objects in the model.
"""

import numpy as np

from build import config as cfg
from model.growth_cone import GrowthCone
from model.simulation import Simulation
from model.substrate import (ContinuousGradientSubstrate, WedgeSubstrate,
                             StripeSubstrate, GapSubstrate, GapSubstrateInverted)


def build_default():
    """
    Build a default model.
    """
    return build_simulation(cfg.current_config)


def build_simulation(config):
    """
    Build substrate object and growth cone list to then build the simulation instance.
    """
    # Build other parts
    substrate = build_substrate(config)
    growth_cones = initialize_growth_cones(config)

    # Extract attributes from the configuration
    step_size = config.get(cfg.STEP_SIZE)
    num_steps = config.get(cfg.STEP_AMOUNT)

    x_step_p = config.get(cfg.X_STEP_POSSIBILITY)
    y_step_p = config.get(cfg.Y_STEP_POSSIBILITY)
    sigmoid_steepness = config.get(cfg.SIGMOID_STEEPNESS)
    sigmoid_shift = config.get(cfg.SIGMOID_SHIFT)
    sigma = config.get(cfg.SIGMA)
    force = config.get(cfg.FORCE)
    forward_sig = config.get(cfg.FORWARD_SIG)
    reverse_sig = config.get(cfg.REVERSE_SIG)
    ff_inter = config.get(cfg.FF_INTER)
    ft_inter = config.get(cfg.FT_INTER)

    adaptation = config.get(cfg.ADAPTATION_ENABLED)
    mu = 0
    lambda_ = 0
    history_length = 0

    if adaptation:
        mu = config.get(cfg.ADAPTATION_MU)
        lambda_ = config.get(cfg.ADAPTATION_LAMBDA)
        history_length = config.get(cfg.ADAPTATION_HISTORY)

    # Initialize the Simulation object with the new parameters
    simulation = Simulation(substrate, growth_cones, adaptation, step_size, num_steps, x_step_p, y_step_p,
                            sigmoid_steepness, sigmoid_shift, sigma, force, forward_sig, reverse_sig, ff_inter,
                            ft_inter, mu, lambda_, history_length)
    return simulation


def build_substrate(config):
    """
    Build a Substrate instance.
    """
    # Extract attributes from the configuration
    rows = config.get(cfg.ROWS)
    cols = config.get(cfg.COLS)
    offset = config.get(cfg.GC_SIZE)
    substrate_type = config.get(cfg.SUBSTRATE_TYPE)

    if substrate_type == cfg.CONTINUOUS_GRADIENTS:
        continuous_signal_start = config.get(cfg.CONTINUOUS_SIGNAL_START)
        continuous_signal_end = config.get(cfg.CONTINUOUS_SIGNAL_END)
        substrate = ContinuousGradientSubstrate(rows, cols, offset, signal_start=continuous_signal_start,
                                                signal_end=continuous_signal_end)

    elif substrate_type == cfg.WEDGES:
        wedge_narrow_edge = config.get(cfg.WEDGE_NARROW_EDGE)
        wedge_wide_edge = config.get(cfg.WEDGE_WIDE_EDGE)
        substrate = WedgeSubstrate(rows, cols, offset, narrow_edge=wedge_narrow_edge, wide_edge=wedge_wide_edge)

    elif substrate_type == cfg.STRIPE:
        stripe_fwd = config.get(cfg.STRIPE_FWD)
        stripe_rew = config.get(cfg.STRIPE_REW)
        stripe_conc = config.get(cfg.STRIPE_CONC)
        stripe_width = config.get(cfg.STRIPE_WIDTH)
        substrate = StripeSubstrate(rows, cols, offset, fwd=stripe_fwd, rew=stripe_rew, conc=stripe_conc,
                                    width=stripe_width)

    elif substrate_type == cfg.GAP:
        gap_begin = config.get(cfg.GAP_BEGIN)
        gap_end = config.get(cfg.GAP_END)
        gap_first_block = config.get(cfg.GAP_FIRST_BLOCK)
        gap_second_block = config.get(cfg.GAP_SECOND_BLOCK)
        substrate = GapSubstrate(rows, cols, offset, begin=gap_begin, end=gap_end, first_block=gap_first_block,
                                 second_block=gap_second_block)

    elif substrate_type == cfg.GAP_INV:
        gap_begin = config.get(cfg.GAP_BEGIN)
        gap_end = config.get(cfg.GAP_END)
        gap_first_block = config.get(cfg.GAP_FIRST_BLOCK)
        substrate = GapSubstrateInverted(rows, cols, offset, begin=gap_begin, end=gap_end, first_block=gap_first_block)

    else:
        raise ValueError("SubstrateType unknown")

    substrate.initialize_substrate()
    return substrate


def initialize_growth_cones(config):
    """
    Initialize and configure growth cones.
    """
    # Extract parameters from the configuration
    growth_cones = []
    gc_count = config.get(cfg.GC_COUNT)
    size = config.get(cfg.GC_SIZE)
    rows = config.get(cfg.ROWS)

    # Non-linear gradient for receptors, starting at 0.99 and decreasing to 0.01
    receptor_gradient = np.linspace(0, 1, gc_count) ** 1.4
    receptors = 0.01 + receptor_gradient * 0.99

    # This is the inverse of the receptor gradient
    ligands = 0.01 + receptor_gradient * 0.99
    ligands = ligands[::-1]

    # Create an array of evenly distributed y-positions for the growth cones
    y_positions = np.linspace(size, rows - 1 + size, gc_count, dtype=int)

    for i in range(gc_count):
        # Create a GrowthCone instance and initialize it
        pos_y = y_positions[i]
        gc = GrowthCone((size, pos_y), size, ligands[i], receptors[i], i)
        growth_cones.append(gc)

    return growth_cones
