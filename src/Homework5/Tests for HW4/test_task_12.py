import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from task12 import from_roman


@ddt
class TestSuiteFromRoman(unittest.TestCase):
    """Roman numeral conversion test suite."""

    @data(('MCMXCV', 1995), ('XCIX', 99))
    @unpack
    def test_from_roman(self, num, expected_result):
        """Roman numeral conversion test.

        :param num:               roman num
        :param expected_result:   expected num
        """
        self.assertEqual(from_roman(num), expected_result)
