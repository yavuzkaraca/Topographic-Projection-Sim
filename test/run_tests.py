import unittest

# Import your test modules
from test.test_growth_cones import TestGrowthCone
from test.test_history import TestHistory
from test.test_substrate import TestBaseSubstrate

if __name__ == '__main__':
    # Create a test suite combining all test cases
    suite = unittest.TestSuite()

    # Load tests from each test module
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestGrowthCone))
    suite.addTests(loader.loadTestsFromTestCase(TestHistory))
    suite.addTests(loader.loadTestsFromTestCase(TestBaseSubstrate))

    # Create a test runner that will run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)