"""Test module for task2_hw4 tests"""

import ddt
import unittest
import collections
from src.homework4 import task2

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestGetRanges(unittest.TestCase):
    """Test cases for get_ranges"""

    @ddt.data(
        ([0, 1, 2, 3, 4, 7, 8, 10], "0-4,7-8,10"),
        ([4, 7, 10], "4,7,10"),
        ([2, 3, 8, 9], "2-3,8-9"),
    )
    @ddt.unpack
    def test_get_ranges(self, inp_list, expected_result):
        """Test get_ranges with input data {0} and expected result {1}"""
        result = task2.get_ranges(inp_list)
        self.assertEqual(result, expected_result)
