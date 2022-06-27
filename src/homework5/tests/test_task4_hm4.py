"""Test module for task4_hw4 tests."""

import ddt
from src.homework5 import task4_hm4
import unittest


@ddt.ddt
class TestGetDegreeTwo(unittest.TestCase):
    """Test cases for get_degree_two."""

    @ddt.data(
        (10, "10(8)"),
        (20, "20(16)"),
        (1, "1(1)"),
        (13, "13(16)"),
        (0, "The entered number is less than or equal to 0"),
        (-3, "The entered number is less than or equal to 0"),
    )
    @ddt.unpack
    def test_get_degree_two(self, input_number, expected_result):
        """Test get_degree_two with next data {0} --> {1}"""
        result = task4_hm4.get_degree_two(input_number)
        self.assertEqual(result, expected_result)
