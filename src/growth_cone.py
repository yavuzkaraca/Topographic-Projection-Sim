class GrowthCone:
    def __init__(self, position, config_dict):
        self.position = position  # Center point of the circular modeled GC, as x,y
        self.size = 10  # Radius of the circle
        self.ligand = 0
        self.receptor = 0
        self.potential = 0
