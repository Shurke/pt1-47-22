"""Test module for task4 (Primes) tests"""
import ddt
from src.homework5 import task4
import unittest


@ddt.ddt
class TestPrimes(unittest.TestCase):
    """Test case for Primes"""

    def setUp(self) -> None:
        self.prime = task4.Primes

    @ddt.data(
        (2, [2, 3], True),
        (5, [2, 3, 5, 7, 11], True),
        (5, [2, 3, 4, 5, 6], False),
        (0, 'Wrong data!', True),
        (-1, 'Wrong data!', True)
    )
    @ddt.unpack
    def test_first(self, numb, prime_lst, expect):
        """Test case for first method with user numb {0} and result {1}"""
        result = prime_lst == self.prime.first(numb)
        self.assertEqual(result, expect)

    @ddt.data(
        (2, 1, [3], True),
        (20, 5, [53, 59, 61, 67, 71], True),
        (20, 5, [54, 55, 56, 57, 58], False),
        (2, 0, 'Wrong data!', True),
        (5, -1, 'Wrong data!', True)
    )
    @ddt.unpack
    def test_last(self, first_numb, last_numb, prime_lst, expect):
        """Test case for last method with user first_numb {0}, last_numb {1} and result {2}"""
        result = prime_lst == self.prime.first(first_numb).last(last_numb)
        self.assertEqual(result, expect)
