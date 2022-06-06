"""Test module for task2_from_hw4 (get_ranges) tests"""
import ddt
from src.homework5 import task2_from_hw4
import unittest


@ddt.ddt
class TestGetRange(unittest.TestCase):
    """Test case for get_ranges"""

    def setUp(self) -> None:
        self.ranges = task2_from_hw4.get_ranges

    @ddt.data(
        ([0, 1, 2, 3, 4, 7, 8, 10], '0 - 4,7 - 8,10', True),
        ([4, 7, 10], '4,7,10', True),
        ([2, 3, 8, 9], '2, 3, 8, 9', False)
    )
    @ddt.unpack
    def test_get_ranges(self, inp_str, otp_str, expect):
        """Test case for method get_ranges with input string {0} and output list{1}"""
        result = otp_str == self.ranges(inp_str)
        self.assertEqual(result, expect)
