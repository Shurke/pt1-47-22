import unittest
from ddt import ddt, data, unpack
from task09 import dispenser


@ddt
class DispenserTestCase(unittest.TestCase):

    @data(('teaspoons', 59, '1 cup, 3 tablespoons, 2 teaspoons'))
    @unpack
    def test_dispenser(self, unit_type, quantity, expected_result):
        self.assertEqual(dispenser(unit_type, quantity), expected_result)
