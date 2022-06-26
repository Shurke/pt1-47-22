import unittest
from ddt import ddt, data, unpack
from task04 import Primes


@ddt
class TestSuitePrimes(unittest.TestCase):
    """Primes test suite."""

    @data((1, [2]),
          (2, [2, 3]),
          (5, [2, 3, 5, 7, 11]))
    @unpack
    def test_primes_first(self, first_nums, expected_list):
        """Test Primes.first() method.

        :param first_nums:      class for test
        :param expected_list:   class for test
        """
        primes = Primes()
        self.assertEqual(primes.first(first_nums), expected_list)

    @data((20, 5, [53, 59, 61, 67, 71]))
    @unpack
    def test_primes_last(self, first_nums, last_nums, expected_list):
        """Test Primes.last() method.

        :param first_nums:      class for test
        :param last_nums:       class for test
        :param expected_list:   class for test
        """
        primes = Primes()
        primes.first(first_nums)
        self.assertEqual(primes.last(last_nums), expected_list)
