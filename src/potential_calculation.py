import math


def bounding_box(gc, substrate):
    # TODO: make circle
    # Calculate the bounds of the bounding box
    x_min = max(0, int(gc.position[0] - gc.size))
    x_max = min(substrate.cols - 1, int(gc.position[0] + gc.size))
    y_min = max(0, int(gc.position[1] - gc.size))
    y_max = min(substrate.rows - 1, int(gc.position[1] + gc.size))

    return x_min, x_max, y_min, y_max


def calculate_potential(gc, gcs, substrate, step):
    # TODO: take position as a parameter
    ft_ligands, ft_receptors = fiber_target_interaction(gc, substrate)
    ff_ligands, ff_receptors = ff_interaction(gc, gcs)

    forward_sig = gc.receptor * (ft_ligands + (step * ff_ligands))
    reverse_sig = gc.ligand * (ft_receptors + (step * ff_receptors))

    # print(f"forward_sig: {forward_sig}, reverse_sig: {reverse_sig}")
    # print(f"ft_ligands: {ft_ligands}, ft_receptors: {ft_receptors}, ff_ligands: {ff_ligands}, ff_receptors: {ff_receptors}")

    return abs(math.log(reverse_sig or 1) - math.log(forward_sig or 1))


def fiber_target_interaction(gc, substrate):
    borders = bounding_box(gc, substrate)
    sum_ligands = 0
    sum_receptors = 0

    # print(f"border: {borders[0]},{borders[1]}, {borders[2]}, {borders[3]}")
    for i in range(borders[2], borders[3]):
        for j in range(borders[0], borders[1]):
            # TODO: ensure circle box by skipping with a condition here
            sum_ligands += substrate.ligands[i, j]
            sum_receptors += substrate.receptors[i, j]

    # print(f"sum_ligands: {sum_ligands}, sum_receptors: {sum_receptors}")
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
            # TODO: eliminate self from the gcs list, otherwise always a match
            continue
        d = euclidean_distance(gc2.position, gc1.position)
        if d <= gc1.size:
            area = intersection_area(gc1.position, gc2.position, gc1.size)
            sum_ligands += area * gc2.ligand
            sum_receptors += area * gc2.receptor

    return sum_ligands, sum_receptors


def intersection_area(gc1_pos, gc2_pos, radius):
    d = euclidean_distance(gc1_pos, gc2_pos)  # Distance between the centers of the circles

    if d == 0:
        return radius * radius * math.pi
    elif d > radius:
        return 0
    else:
        # Partial overlap of two circles
        x = (d ** 2) / (2 * d)
        z = x ** 2
        y = math.sqrt(radius ** 2 - z)
        return radius ** 2 * math.acos(x / radius) - x * y
