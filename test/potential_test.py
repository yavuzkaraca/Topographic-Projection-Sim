from growth_cone import GrowthCone
from potential_calculation import euclidean_distance
from substrate import Substrate

gc_left = GrowthCone((10, 10), 5, 0.01, 0.99)
gc_mid = GrowthCone((10, 10), 5, 0.5, 0.5)
gc_right = GrowthCone((10, 10), 5, 0.01, 0.99)

substrate = Substrate(50, 50, "continuous_gradients", 0, 0)


def test_distance_zero():
    gc_1 = GrowthCone((10, 10), 5, 0, 0)
    gc_2 = GrowthCone((10, 10), 5, 0, 0)

    assert euclidean_distance(gc_1.position, gc_2.position) == 0


def test_intersection_area():
    pass
