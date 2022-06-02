"""Test module for task5_from_hw4 (maximum_divisor) tests"""
import unittest
import ddt
from src.homework5 import task5_from_hw4


@ddt.ddt
class TestMaxDivisor(unittest.TestCase):
    """Test case for two_degree"""

    def setUp(self) -> None:
        self.divide = task5_from_hw4.maximum_divisor

    @ddt.data(
        (10, 'Max divisor: 2', True),
        (10, 'Max divisor: 5', False),
        (16, 'Max divisor: 16', True),
        (12, 'Max divisor: 4', True)
    )
    @ddt.unpack
    def test_max_divisor(self, inp_numb, div, expect):
        """Test case for maximum_divisor method with entered numb {0} and maximal divisor {1}"""
        result = div == self.divide(inp_numb)
        self.assertEqual(result, expect)
