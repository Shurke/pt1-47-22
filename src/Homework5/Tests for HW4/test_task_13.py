import unittest
from ddt import ddt, data, unpack
from task13 import matching_with_elements


@ddt
class MatchingWithElementsTestCase(unittest.TestCase):

    @data(('silicon', ' SiLiCON'), ('Silver', 'SiLvEr'))
    @unpack
    def test_max_divisor(self, name, expected_result):
        self.assertEqual(matching_with_elements(name), expected_result)
