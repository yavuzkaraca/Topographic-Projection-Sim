"""
Module for setting up and initializing a growth cone simulation.
"""

import numpy as np
import config as cfg  # Importing the configuration module
from growth_cone import GrowthCone  # Importing the Growth Cone class
from simulation import Simulation  # Importing the Simulation class
# Importing the Substrate classes
from substrate import (ContinuousGradientSubstrate, WedgeSubstrate,
                       StripeFwdSubstrate, StripeRewSubstrate, StripeDuoSubstrate,
                       GapSubstrateRR, GapSubstrateRB, GapSubstrateBR,GapSubstrateBB)


def build_default():
    """
    Build a default simulation using the default configuration settings.
    """
    return build_simulation(cfg.config)


def build_simulation(config):
    """
    Build a simulation instance using the provided configuration.

    :param config: Configuration dictionary with simulation settings.
    :return: A Simulation object initialized with the provided settings.
    """
    # Extract attributes from the configuration
    substrate = build_substrate(config)
    growth_cones = initialize_growth_cones(config)
    step_size = config.get(cfg.STEP_SIZE)
    num_steps = config.get(cfg.STEP_AMOUNT)
    x_step_p = config.get(cfg.X_STEP_POSSIBILITY)
    y_step_p = config.get(cfg.Y_STEP_POSSIBILITY)
    sigma = config.get(cfg.SIGMA)

    # Extract adaptation parameters
    adaptation = config.get(cfg.ADAPTATION_ENABLED)
    mu = config.get(cfg.ADAPTATION_MU)
    lambda_ = config.get(cfg.ADAPTATION_LAMBDA)
    history_length = config.get(cfg.ADAPTATION_HISTORY)

    # Initialize the Simulation object with the new parameters
    simulation = Simulation(substrate, growth_cones, adaptation, step_size, num_steps, x_step_p, y_step_p, sigma, mu, lambda_, history_length)
    return simulation


def build_substrate(config):
    """
    Build a Substrate instance based on the configuration settings.

    :param config: Configuration dictionary with substrate settings.
    :return: A Substrate object initialized with the provided settings.
    """
    # Extract attributes from the configuration
    rows = config.get(cfg.ROWS)
    cols = config.get(cfg.COLS)
    offset = config.get(cfg.GC_SIZE)
    substrate_type = config.get(cfg.SUBSTRATE_TYPE)
    min_value = config.get(cfg.CUSTOM_FIRST)
    max_value = config.get(cfg.CUSTOM_SECOND)

    if substrate_type == cfg.CONTINUOUS_GRADIENTS:
        substrate = ContinuousGradientSubstrate(rows, cols, offset, min_value, max_value)
    elif substrate_type == cfg.WEDGES:
        substrate = WedgeSubstrate(rows, cols, offset, min_value, max_value)
    elif substrate_type == cfg.STRIPE_FWD:
        substrate = StripeFwdSubstrate(rows, cols, offset, min_value, max_value)
    elif substrate_type == cfg.STRIPE_REW:
        substrate = StripeRewSubstrate(rows, cols, offset, min_value, max_value)
    elif substrate_type == cfg.STRIPE_DUO:
        substrate = StripeDuoSubstrate(rows, cols, offset, min_value, max_value)
    elif substrate_type == cfg.GAP_RR:
        substrate = GapSubstrateRR(rows, cols, offset, min_value, max_value)
    elif substrate_type == cfg.GAP_RB:
        substrate = GapSubstrateRB(rows, cols, offset, min_value, max_value)
    elif substrate_type == cfg.GAP_BR:
        substrate = GapSubstrateBR(rows, cols, offset, min_value, max_value)
    elif substrate_type == cfg.GAP_BB:
        substrate = GapSubstrateBB(rows, cols, offset, min_value, max_value)
    else:
        raise ValueError("SubstrateType unknown")

    substrate.initialize_substrate()
    return substrate


def initialize_growth_cones(config):
    """
    Initialize and configure growth cones based on the provided settings.

    :param config: Configuration dictionary with growth cone settings.
    :return: A list of initialized Growth Cone objects.
    """
    # Extract parameters from the configuration
    growth_cones = []
    gc_count = config.get(cfg.GC_COUNT)
    size = config.get(cfg.GC_SIZE)
    rows = config.get(cfg.ROWS)

    # Create arrays for evenly distributed receptor and ligand values
    receptors = np.linspace(0.99, 0.01, gc_count)
    ligands = np.linspace(0.01, 0.99, gc_count)

    # Create an array of evenly distributed y-positions for the growth cones
    y_positions = np.linspace(size, rows - 1 + size, gc_count, dtype=int)

    for i in range(gc_count):
        # Create a GrowthCone instance and initialize it
        pos_y = y_positions[i]
        gc = GrowthCone((size, pos_y), size, receptors[i], ligands[i], i)
        growth_cones.append(gc)

    return growth_cones
