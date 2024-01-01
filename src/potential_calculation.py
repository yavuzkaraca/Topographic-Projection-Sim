"""
Module providing all methods needed for guidance potential calculation
"""

import math


def calculate_potential(gc, gcs, substrate, step):
    """
    Calculate guidance potential for a growth cone (gc) in a simulation.

    :param gc: Growth Cone object representing the cone for which potential is calculated.
    :param gcs: List of other growth cones (for fiber-fiber interaction).
    :param substrate: Substrate object (for fiber-target interaction).
    :param step: The iteration step of the simulation (used for fiber-fiber interaction).
    :return: The guidance potential as a floating-point number.
    """
    # TODO: make configurable
    # Settings init
    forward_on = True
    reverse_on = True
    ff_inter_on = True
    ft_inter_on = True

    # Calculate the number of receptors and ligands growth cone is exposed to
    ft_ligands, ft_receptors = ft_interaction(gc, substrate)
    ff_ligands, ff_receptors = ff_interaction(gc, gcs)

    if not ff_inter_on: ff_ligands, ff_receptors = 0, 0
    if not ft_inter_on: ft_ligands, ft_receptors = 0, 0

    # TODO: Cis signals

    # Calculate the forward and reverse signals
    forward_sig = gc.receptor * (ft_ligands + gc.ligand + (step * ff_ligands))
    reverse_sig = gc.ligand * (ft_receptors + gc.receptor + (step * ff_receptors))

    if not forward_on: forward_sig = 0
    if not reverse_on: reverse_sig = 0

    return abs(math.log(reverse_sig or 1) - math.log(forward_sig or 1))


def ft_interaction(gc, substrate):
    """
    Calculate fiber-target interaction between a growth cone and a substrate.

    :param gc: Growth Cone object representing the cone for interaction.
    :param substrate: Substrate object where the interaction occurs.
    :return: A tuple containing the sum of ligands and receptors from the substrate area covered
    """

    borders = bounding_box(gc.new_position, gc.size, substrate)

    # Needed to ensure the circular modelling of growth cones
    edge_length = abs(borders[2] - borders[3])
    center = (borders[2] + borders[3]) / 2, (borders[0] + borders[1]) / 2

    sum_ligands = 0
    sum_receptors = 0

    for i in range(borders[2], borders[3]):
        for j in range(borders[0], borders[1]):
            d = euclidean_distance(center, (i, j))
            if d > edge_length / 2:
                # Eliminate cells outside of the circle, as borders define a square matrix
                continue
            sum_ligands += substrate.ligands[i, j]
            sum_receptors += substrate.receptors[i, j]

    return sum_ligands, sum_receptors


def ff_interaction(gc1, gcs):
    """
    Calculate the fiber-fiber interaction between a growth cone (gc1) and a list of other growth cones (gcs).

    :param gc1: The primary Growth Cone object for which interaction is being calculated.
    :param gcs: A list of other Growth Cone objects for potential interactions with gc1.
    :return: A tuple containing the sum of ligands and receptors involved in the ff interaction.
    """
    sum_ligands = 0
    sum_receptors = 0

    for gc2 in gcs:
        if gc1 == gc2:
            # Eliminate self from the gcs list, as self-comparison always matches
            continue
        d = euclidean_distance(gc2.position, gc1.new_position)
        if d < gc1.size * 2:
            area = intersection_area(gc1.new_position, gc2.position, gc1.size)
            sum_ligands += area * gc2.ligand
            sum_receptors += area * gc2.receptor

    return sum_ligands, sum_receptors


def bounding_box(gc_pos, gc_size, substrate):
    """
    Calculate the boundaries of the bounding box for a growth cone (used in fiber-target interaction).

    :param gc_pos: position of Growth Cone.
    :param gc_size: size of Growth Cone.
    :param substrate: Substrate Object defining the area for interaction.
    :return: Tuple representing the boundary values of the square matrix (x_min, x_max, y_min, y_max).
    """
    # Calculate the bounds of the bounding box
    x_min = max(0, gc_pos[0] - gc_size)
    x_max = min(substrate.cols - 1, gc_pos[0] + gc_size)
    y_min = max(0, gc_pos[1] - gc_size)
    y_max = min(substrate.rows - 1, gc_pos[1] + gc_size)

    return x_min, x_max, y_min, y_max


def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in a 2-dimensional space.
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def intersection_area(gc1_pos, gc2_pos, radius):
    """
    Calculate the area of intersection between two circles (circumscribed around growth cones).
    """
    d = euclidean_distance(gc1_pos, gc2_pos)  # Distance between the centers of the circles

    if d == 0:
        # Total overlap
        return radius * radius * math.pi
    elif d > radius * 2:
        # No overlap
        return 0
    else:
        # Partial overlap
        x = (d ** 2) / (2 * d)
        z = x ** 2
        y = math.sqrt(radius ** 2 - z)
        area = radius ** 2 * math.acos(x / radius) - x * y
        # TODO: clean-fix area calculation
        return area * 1.5  # magic number for quick dirty fix
