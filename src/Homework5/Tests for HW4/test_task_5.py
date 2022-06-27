from ddt import data
from ddt import ddt
from ddt import unpack
from task05 import max_divisor
import unittest


@ddt
class TestSuiteMaxDivisor(unittest.TestCase):
    """MaxDivisor test suite"""

    @data((10, 2), (16, 16), (12, 4))
    @unpack
    def test_max_divisor(self, num, expected_result):
        """max_divisor function test

        :param num:                 input number
        :param expected_result:     max divisor
        """
        self.assertEqual(max_divisor(num), expected_result)
