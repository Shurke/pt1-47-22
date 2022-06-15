"""Test module for task_4 tests."""

import ddt
from src.homework5 import task_4
import unittest


@ddt.ddt
class TestPrimes(unittest.TestCase):
    """Test cases for Primes"""

    def setUp(self) -> None:
        self.primes = task_4.Primes

    @ddt.data(
        (1, [2]),
        (2, [2, 3]),
        (5, [2, 3, 5, 7, 11]),
    )
    @ddt.unpack
    def test_first(self, number_first, expected_result):
        """Test first method with quantity:{0} --> {1}"""
        result = self.primes.first(number_first)
        self.assertEqual(result, expected_result)

    @ddt.data(
        (20, 5, [53, 59, 61, 67, 71])
    )
    @ddt.unpack
    def test_last(self, number_first, number_last, expected_result):
        """Test last method with number_first {0}, number_last {1} --> {2}"""
        result = self.primes.first(number_first).last(number_last)
        self.assertEqual(result, expected_result)
