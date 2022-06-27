from ddt import data
from ddt import ddt
from ddt import unpack
import unittest
from task04 import get_nearest_power_of_two


@ddt
class TestSuiteGetNearestPowerOfTwo(unittest.TestCase):
    """Test suite for GetNearestPowerOfTwo function"""

    @data((10, 8), (20, 16), (1, 1), (13, 16))
    @unpack
    def test_get_nearest_power_of_two(self, num, expected_result):
        """

        :param num:               Input number
        :param expected_result:   Nearest power of Two
        """
        self.assertEqual(get_nearest_power_of_two(num), expected_result)
