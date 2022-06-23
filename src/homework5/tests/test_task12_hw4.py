"""Test module for task12_hw4 tests"""

import collections
import ddt
from src.homework4 import task12
import unittest

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestNumberConverter(unittest.TestCase):
    """Test cases for number_converter"""

    @ddt.data(
        ('XCIX', 99),
        ('IX', 9),
        ('XIV', 14),
    )
    @ddt.unpack
    def test_number_converter(self, roman_numb, expected_numb):
        """Test number_converter with input data {0} and expected number {1}"""
        result = task12.number_converter(roman_numb)
        self.assertEqual(result, expected_numb)
