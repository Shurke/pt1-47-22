import unittest
from ddt import ddt, data, unpack
from task02 import get_ranges


@ddt
class GetRangesTestCase(unittest.TestCase):

    @data(([0, 1, 2, 3, 4, 7, 8, 10], "0-4,7-8,10"),
          ([4, 7, 10], "4,7,10"),
          ([2, 3, 8, 9], "2-3,8-9"))
    @unpack
    def test_get_ranges(self, nums_range, expected_result):
        self.assertEqual(get_ranges(nums_range), expected_result)
