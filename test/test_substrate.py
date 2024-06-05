import unittest
import numpy as np
from model.substrate.substrate import BaseSubstrate  # Adjust imports as needed


class TestBaseSubstrate(unittest.TestCase):
    def setUp(self):
        self.rows = 10
        self.cols = 10
        self.offset = 2
        self.min_value = 0.0
        self.max_value = 1.0
        self.substrate = BaseSubstrate(self.rows, self.cols, self.offset, self.min_value, self.max_value)

    def test_initialization(self):
        self.assertEqual(self.substrate.rows, self.rows + self.offset * 2)
        self.assertEqual(self.substrate.cols, self.cols + self.offset * 2)
        # Continue for other attributes...

    def test_ligand_receptor_states(self):
        expected_ligands = np.zeros((self.rows + self.offset * 2, self.cols + self.offset * 2))
        expected_receptors = np.zeros_like(expected_ligands)
        np.testing.assert_array_equal(self.substrate.ligands, expected_ligands)
        np.testing.assert_array_equal(self.substrate.receptors, expected_receptors)

    # Continue with other tests for methods like `set_col_ligand_only`, `initialize_substrate`, etc.
