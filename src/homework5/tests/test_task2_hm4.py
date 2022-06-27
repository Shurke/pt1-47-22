"""Test module for task2_hw4 tests."""

import ddt
from src.homework5 import task2_hw4
import unittest


@ddt.ddt
class TestGetRange(unittest.TestCase):
    """Test cases for get_ranges."""

    @ddt.data(
        ([0, 1, 2, 3, 4, 7, 8, 10], "0-4,7-8,10"),
        ([4, 7, 10], "4,7,10"),
        ([2, 3, 8, 9], "2-3,8-9"),
    )
    @ddt.unpack
    def test_get_ranges(self, input_list, expected_result):
        """Test get_ranges with next data {0} --> {1}"""
        result = task2_hw4.get_ranges(input_list)
        self.assertEqual(result, expected_result)
