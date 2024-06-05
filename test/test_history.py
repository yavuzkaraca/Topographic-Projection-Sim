import unittest
from model.growth_cone import History


class TestHistory(unittest.TestCase):
    def setUp(self):
        self.history = History(0, 0, 0, 0, 0, 0, 0)

    def test_update_potential(self):
        self.history.update_potential(1)
        self.assertEqual(self.history.potential[-1], 1)

    def test_update_adap_co(self):
        self.history.update_adap_co(1)
        self.assertEqual(self.history.adap_co[-1], 1)

    def test_update_position(self):
        self.history.update_position(1)
        self.assertEqual(self.history.position[-1], 1)

    def test_update_ligand(self):
        self.history.update_ligand(1)
        self.assertEqual(self.history.ligand[-1], 1)

    def test_update_receptor(self):
        self.history.update_receptor(1)
        self.assertEqual(self.history.receptor[-1], 1)

    def test_update_reset_force_receptor(self):
        self.history.update_reset_force_receptor(1)
        self.assertEqual(self.history.reset_force_receptor[-1], 1)

    def test_update_reset_force_ligand(self):
        self.history.update_reset_force_ligand(1)
        self.assertEqual(self.history.reset_force_ligand[-1], 1)
