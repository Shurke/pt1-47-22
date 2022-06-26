"""
Unittest for task4.py
"""


import ddt
from src import task4
import unittest


@ddt.ddt
class TestTask2(unittest.TestCase):
    """Test cases for Primes"""

    @ddt.data(
        (1, [2]),
        (2, [2, 3]),
        (5, [2, 3, 5, 7, 11]),
        (0, []),
        (-1, [])
    )
    @ddt.unpack
    def test_method_first(self, right_limit, check_list):
        """Test method first() from class Primes"""

        result_list = task4.Primes.first(right_limit)
        self.assertEqual(result_list, check_list)

    @ddt.data(
        (20, 5, [53, 59, 61, 67, 71]),
        (20, 0, []),
        (20, -1, [])
    )
    @ddt.unpack
    def test_method_last(self, right_limit, left_limit, check_list):
        """Test method last() from class Primes"""

        result_list = task4.Primes.first(right_limit).last(left_limit)
        self.assertEqual(result_list, check_list)
