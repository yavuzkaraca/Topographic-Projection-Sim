"""
Module providing Growth Cone class for growth cone representation.
"""


class GrowthCone:
    """
    Represents a growth cone in the simulation environment.

    Attributes:
        start_position (tuple): Initial position of the growth cone.
        position (tuple): Center point of the circular modeled growth cone (x, y coordinates).
        new_position (tuple): Potential new position for the growth cone (used for step decision).
        size (int): Radius of the growth cone.
        ligand (float): Ligand value associated with the growth cone.
        receptor (float): Receptor value associated with the growth cone.
        potential (int): Current potential of the growth cone.

    Methods:
        __str__(): Provides a string representation of the growth cone instance.
    """

    def __init__(self, position, size, ligand, receptor):
        """
        Initializes a GrowthCone object with position, size, ligand, and receptor values.

        :param position: Initial position of the growth cone (x, y coordinates).
        :param size: Radius of the circular modeled growth cone.
        :param ligand: Ligand value associated with the growth cone.
        :param receptor: Receptor value associated with the growth cone.
        """
        self.start_position = position
        self.position = position
        self.new_position = position
        self.size = size
        self.ligand = ligand
        self.receptor = receptor
        self.potential = 0

    def __str__(self):
        """
        Provides a string representation of the growth cone's attributes.
        """
        return (f"Receptor: {self.receptor}, Ligand: {self.ligand}, Position: {self.position}, "
                f"Start Position: {self.start_position}, Potential: {self.potential}")
