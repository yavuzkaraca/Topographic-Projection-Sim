from growth_cone import GrowthCone
from simulation.potential_calculation import euclidean_distance, ft_interaction
from substrate import Substrate

gc_left = GrowthCone((10, 10), 5, 0.01, 0.99)
gc_mid = GrowthCone((10, 10), 5, 0.5, 0.5)
gc_right = GrowthCone((10, 10), 5, 0.01, 0.99)

substrate = Substrate(50, 50, 5, "continuous_gradients", 0)


def test_distance_zero():
    gc_1 = GrowthCone((10, 10), 5, 0, 0)
    gc_2 = GrowthCone((10, 10), 5, 0, 0)

    assert euclidean_distance(gc_1.pos_current, gc_2.pos_current) == 0


def test_intersection_area():
    pass

def test_ft_interaction():
    substrate = Substrate(50, 50, 5, "continuous_gradients", 0, 0)
    substrate.rows
    substrate.cols
    gc_top = GrowthCone((30, 54), 5, 0.5, 0.5)
    gc_mid = GrowthCone((30, 30), 5, 0.5, 0.5)
    gc_bottom = GrowthCone((30, 5), 5, 0.5, 0.5)
    ft_interaction(gc_top, substrate)
    ft_interaction(gc_mid, substrate)
    ft_interaction(gc_bottom, substrate)
