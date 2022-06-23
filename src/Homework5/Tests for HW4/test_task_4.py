import unittest
from ddt import ddt, data, unpack
from task04 import get_nearest_power_of_two


@ddt
class GetNearestPowerOfTwoTestCase(unittest.TestCase):

    @data((10, 8), (20, 16), (1, 1), (13, 16))
    @unpack
    def test_get_nearest_power_of_two(self, num, expected_result):
        self.assertEqual(get_nearest_power_of_two(num), expected_result)
