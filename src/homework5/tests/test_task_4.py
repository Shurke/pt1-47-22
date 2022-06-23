"""Test module for task_4 tests"""

import ddt
import unittest
import collections
from src.homework5 import task_4

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestPrimes(unittest.TestCase):
    """Test cases for Primes"""

    @ddt.data(
        (2, [2, 3]),
        (5, [2, 3, 5, 7, 11]),
        (8, [2, 3, 5, 7, 11, 13, 17, 19]),
    )
    @ddt.unpack
    def test_first(self, amount, expected_result):
        """Test first with input data {0} and expected result {1}"""
        result = task_4.Primes.first(amount).prime_list
        self.assertEqual(result, expected_result)

    @ddt.data(
        (5, 2, [7, 11]),
        (8, 3, [13, 17, 19]),
        (20, 5, [53, 59, 61, 67, 71]),
    )
    @ddt.unpack
    def test_last(self, amount_first, amount_last, expected_result):
        """Test case for last method with input data {0-1} and expected_result {2}"""
        result = task_4.Primes.first(amount_first).last(amount_last)
        self.assertEqual(result, expected_result)
