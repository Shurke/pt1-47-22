import unittest
from ddt import ddt, data, unpack
from task05 import max_divisor


@ddt
class MaxDivisorTestCase(unittest.TestCase):

    @data((10, 2), (16, 16), (12, 4))
    @unpack
    def test_max_divisor(self, num, expected_result):
        self.assertEqual(max_divisor(num), expected_result)
