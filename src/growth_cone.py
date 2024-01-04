"""
Module providing Growth Cone class for growth cone representation.
"""
import math


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

    def __init__(self, position, size, ligand, receptor, id):
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
        self.trajectory = []
        self.size = size
        self.start_ligand = ligand
        self.start_receptor = receptor
        self.ligand = ligand
        self.receptor = receptor
        self.potential = 0
        self.adap_coeff = 1  # Adaptation coefficient starts at 1
        self.reset_force_receptor = 0  # Resetting forces start at 0
        self.reset_force_ligand = 0
        self.history = []  # History of guidance potential values
        self.id = id

    def __str__(self):
        """
        Provides a string representation of the growth cone's attributes.
        """
        return (f"Receptor: {self.receptor}, Ligand: {self.ligand}, Position: {self.position}, "
                f"Start Position: {self.start_position}, Potential: {self.potential},"
                f"ID: {self.id}, Adaptation Coefficient: {self.adap_coeff}, "
                f"Reset Forces: {self.reset_force_ligand}, {self.reset_force_receptor}")

    def take_step(self, new_potential):
        self.history.append(new_potential)
        self.potential = new_potential
        self.position = self.new_position

    def update_trajectory(self):
        self.trajectory.append(self.new_position)

    def calculate_adaptation(self, mu, lambda_, h):
        """
        Calculate the adaptation coefficient and the resetting force based on the history.

        :param mu: Adjusting parameter for the adaptation coefficient.
        :param lambda_: Adjusting parameter for the resetting force.
        :param h: The number of historical steps to consider for adaptation.
        """
        # Ensure we have enough history to calculate adaptation
        if len(self.history) >= h:
            recent_history = self.history[-h:]  # Get the last h elements from the history

            # Calculate the adaptation coefficient using the formula from the paper
            adap_coeff_temp = 1 + math.log(
                1 + mu * sum(k * abs(potential_diff) for k, potential_diff in enumerate(recent_history, 1)) / sum(
                    range(1, h + 1)))

            self.adap_coeff = float("{:.6f}".format(adap_coeff_temp))

            # Calculate the resetting force
            self.reset_force_receptor = lambda_ * (self.start_receptor - self.receptor)
            self.reset_force_ligand = lambda_ * (self.start_ligand - self.ligand)

    def apply_adaptation(self):
        """
        Apply the adaptation coefficient and resetting force to the ligand and receptor values.
        """
        ligand_temp = self.ligand * self.adap_coeff
        receptor_temp = self.receptor * self.adap_coeff
        ligand_temp = max(0, ligand_temp + self.reset_force_ligand)
        receptor_temp = max(0, receptor_temp + self.reset_force_receptor)

        self.ligand = float("{:.6f}".format(ligand_temp))
        self.receptor = float("{:.6f}".format(receptor_temp))


