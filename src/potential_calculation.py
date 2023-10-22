import math


def bounding_box(gc, substrate):
    # TODO: make circle
    # Calculate the bounds of the bounding box
    x_min = max(0, int(gc.position[0] - gc.size))
    x_max = min(substrate.cols - 1, int(gc.position[0] + gc.size))
    y_min = max(0, int(gc.position[1] - gc.size))
    y_max = min(substrate.rows - 1, int(gc.position[1] + gc.size))

    return x_min, x_max, y_min, y_max


def calculate_potential_at(gc, gcs, substrate, step):
    ft_ligands, ft_receptors = fiber_target_interaction(gc.pos, gc.size, substrate)
    ff_ligands, ff_receptors = ff_interaction(gc.pos, gc.size, gcs, substrate)

    forward_sig = gc.receptor * (ft_ligands + (step * ff_ligands))
    reverse_sig = gc.ligand * (ft_receptors + (step * ff_receptors))

    return abs(math.log(reverse_sig / forward_sig))


def fiber_target_interaction(gc, substrate):
    borders = bounding_box(gc.size, gc.position, substrate)
    sum_ligands = 0
    sum_receptors = 0
    for i in range(borders[0], borders[1]):
        for j in range(borders[2], borders[3]):
            # TODO: ensure circle box by skipping with a condition here
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

    # TODO: eliminate self from the gcs list, otherwise always a match

    for gc2 in gcs:
        d = euclidean_distance(gc2, gc1.position)
        if d <= gc1.size:
            area = ff_intersection(gc1.size, gc1.position, gc2.position)
            sum_ligands += area * gc2.ligands
            sum_receptors += area * gc2.receptors

    return sum_ligands, sum_receptors


def ff_intersection(gc1_size, gc1_pos, gc2_pos):
    # TODO: fix
    d = euclidean_distance(gc1_pos, gc2_pos)  # Distance between the centers of the circles
    radius = gc1_size
    intersection_area = (radius ** 2 * math.acos(d / (2.0 * radius)) -
                         d / 2.0 * math.sqrt(4 * radius ** 2 - d ** 2))
    return intersection_area


