"""Test module for task4_from_hw4 (two_degree) tests"""
import unittest
import ddt
from src.homework5 import task4_from_hw4


@ddt.ddt
class TestTwoDegree(unittest.TestCase):
    """Test case for two_degree"""

    def setUp(self) -> None:
        self.degree = task4_from_hw4.two_degree

    @ddt.data(
        (10, 'The nearest degree of two to the entered number: 8', True),
        (10, 'The nearest degree of two to the entered number: 10', False),
        (1, 'The nearest degree of two to the entered number: 1', True),
        (13, 'The nearest degree of two to the entered number: 16', True)
    )
    @ddt.unpack
    def test_two_degree(self, inp_numb, deg, expect):
        """Test case for two_degree method with entered numb {0} and nearest degree {1}"""
        result = deg == self.degree(inp_numb)
        self.assertEqual(result, expect)
