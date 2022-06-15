"""Test module for task5_hw4 tests."""

import unittest
import ddt
from homework5 import task5_hm4


@ddt.ddt
class TestGetMaxDivisor(unittest.TestCase):
    """Test cases for get_max_divisor."""

    def setUp(self) -> None:
        self.divide = task5_hm4.get_max_divisor

    @ddt.data(
        (10, "10(2)"),
        (16, "16(16)"),
        (12, "12(4)"),
        (0, "The entered number is less than or equal to 0"),
        (-3, "The entered number is less than or equal to 0"),
    )
    @ddt.unpack
    def test_get_max_divisor(self, input_number, expected_result):
        """Test get_max_divisor with next data {0} --> {1}"""
        result = self.divide(input_number)
        self.assertEqual(result, expected_result)
