import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from task02 import get_ranges


@ddt
class TestSuiteGetRanges(unittest.TestCase):
    """ test suite for get Ranges function"""
    @data(([0, 1, 2, 3, 4, 7, 8, 10], "0-4,7-8,10"),
          ([4, 7, 10], "4,7,10"),
          ([2, 3, 8, 9], "2-3,8-9"))
    @unpack
    def test_get_ranges(self, nums_range, expected_result):
        """
        :param nums_range:           List of integers
        :param expected_result:      Short list
        """
        self.assertEqual(get_ranges(nums_range), expected_result)
