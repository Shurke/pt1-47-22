"""Test module for task9_hm4 tests."""

import unittest
import ddt
from src.homework5 import task9_hm4


@ddt.ddt
class TestUnitConversion(unittest.TestCase):
    """Test cases for unit_conversion."""

    def setUp(self) -> None:
        self.unit = task9_hm4.unit_conversion

    @ddt.data(
        (59, "tablespoons", "3 cups, 11 tablespoons"),
        (59, "teaspoons", "1 cups, 3 tablespoons, 2 teaspoons"),
        (-59, "teaspoons", "The amount entered must be greater than zero"),
        (8, "poons", "The entered type is invalid"),
    )
    @ddt.unpack
    def test_unit_conversion(self, number, input_str, expected_result):
        """Test unit_conversion with next data {0}, {1} --> {2}"""
        result = self.unit(number, input_str)
        self.assertEqual(result, expected_result)
