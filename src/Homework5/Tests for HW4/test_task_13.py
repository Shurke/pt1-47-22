from ddt import data
from ddt import ddt
from ddt import unpack
from task13 import matching_with_elements
import unittest


@ddt
class TestSuiteMatchingWithElements(unittest.TestCase):
    """Test for MatchingWithElements function"""

    @data(('silicon', ' SiLiCON'), ('Silver', 'SiLvEr'))
    @unpack
    def test_max_divisor(self, name, expected_result):
        """test_max_divisor function test

        :param name:             input word
        :param expected_result:  output word
        """
        self.assertEqual(matching_with_elements(name), expected_result)
