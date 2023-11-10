import math

import numpy as np


def bounding_box(gc, substrate):
    # Calculate the bounds of the bounding box
    x_min = max(0, int(gc.position[0] - gc.size))
    x_max = min(substrate.cols - 1, int(gc.position[0] + gc.size))
    y_min = max(0, int(gc.position[1] - gc.size))
    y_max = min(substrate.rows - 1, int(gc.position[1] + gc.size))

    return x_min, x_max, y_min, y_max


def calculate_potential(gc, gcs, substrate, step):
    # TODO: make configurable
    # Settings init
    forward_on = True
    reverse_on = True
    ff_inter_on = True
    ft_inter_on = True

    # TODO: take position as a parameter
    ft_ligands, ft_receptors = fiber_target_interaction(gc, substrate)
    ff_ligands, ff_receptors = ff_interaction(gc, gcs)

    if not ff_inter_on: ff_ligands, ff_receptors = 0, 0
    if not ft_inter_on: ft_ligands, ft_receptors = 0, 0

    forward_sig = gc.receptor * (ft_ligands + (step * ff_ligands))
    reverse_sig = gc.ligand * (ft_receptors + (step * ff_receptors))

    if not forward_on: forward_sig = 0
    if not reverse_on: reverse_sig = 0

    # TODO: carry this square to density
    return (abs(math.log(reverse_sig or 1) - math.log(forward_sig or 1))) ** 2


def fiber_target_interaction(gc, substrate):
    borders = bounding_box(gc, substrate)
    edge_length = abs(borders[2] - borders[3])
    center = (borders[2] + borders[3]) / 2, (borders[0] + borders[1]) / 2

    sum_ligands = 0
    sum_receptors = 0

    for i in range(borders[2], borders[3]):
        for j in range(borders[0], borders[1]):
            d = euclidean_distance(center, (i, j))
            if d > edge_length / 2:
                continue
            sum_ligands += substrate.ligands[i, j]
            sum_receptors += substrate.receptors[i, j]

    return sum_ligands, sum_receptors


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def ff_interaction(gc1, gcs):
    sum_ligands = 0
    sum_receptors = 0

    for gc2 in gcs:
        if gc1 == gc2:
            # Eliminate self from the gcs list, otherwise always a match
            continue
        d = euclidean_distance(gc2.position, gc1.position)
        if d <= gc1.size * 2:
            area = intersection_area(gc1.position, gc2.position, gc1.size)
            sum_ligands += area * gc2.ligand
            sum_receptors += area * gc2.receptor

    return sum_ligands, sum_receptors


def intersection_area(gc1_pos, gc2_pos, radius):
    d = euclidean_distance(gc1_pos, gc2_pos)  # Distance between the centers of the circles

    if d == 0:
        return radius * radius * math.pi
    elif d > radius * 2:
        return 0
    else:
        # Partial overlap of two circles
        x = (d ** 2) / (2 * d)
        z = x ** 2
        y = math.sqrt(radius ** 2 - z)
        return radius ** 2 * math.acos(x / radius) - x * y
