import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from task09 import dispenser


@ddt
class TestSuiteDispenser(unittest.TestCase):
    """ Test suite for Dispenser function """

    @data(('teaspoons', 59, '1 cup, 3 tablespoons, 2 teaspoons'))
    @unpack
    def test_dispenser(self, unit_type, quantity, expected_result):
        """

        :param unit_type:        unit type
        :param quantity:         quantity
        :param expected_result:  recalculation
        """
        self.assertEqual(dispenser(unit_type, quantity), expected_result)
