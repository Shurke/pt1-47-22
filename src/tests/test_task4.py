"""
Unittest for task4.py
"""


import ddt
from src import task4
import unittest


@ddt.ddt
class TestTask2(unittest.TestCase):
    """Test cases for RealString"""

    def setUp(self) -> None:
        self.task = task4.Primes

    @ddt.data(
        (1, None, [2]),
        (2, None, [2, 3]),
        (5, None, [2, 3, 5, 7, 11]),
        (20, 5, [53, 59, 61, 67, 71])
    )
    @ddt.unpack
    def test_class(self, right_limit, left_limit, check_list):
        """Test class Primes"""

        if left_limit:
            result_list = self.task.first(right_limit).last(left_limit)
        else:
            result_list = self.task.first(right_limit)

        self.assertEqual(result_list, check_list)
