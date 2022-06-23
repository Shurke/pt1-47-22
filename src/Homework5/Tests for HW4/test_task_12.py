import unittest
from ddt import ddt, data, unpack
from task12 import from_roman


@ddt
class FromRomanTestCase(unittest.TestCase):

    @data(('MCMXCV', 1995), ('XCIX', 99))
    @unpack
    def test_max_divisor(self, num, expected_result):
        self.assertEqual(from_roman(num), expected_result)
