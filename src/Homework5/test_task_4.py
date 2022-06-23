import unittest
from ddt import ddt, data, unpack
from task04 import Primes


@ddt
class PrimesTestCase(unittest.TestCase):

    @data((1, None, [2]),
          (2, None, [2, 3]),
          (5, None, [2, 3, 5, 7, 11]),
          (20, 5, [53, 59, 61, 67, 71]))
    @unpack
    def test_primes(self, first_nums, last_nums, expected_list):
        primes = Primes()
        if not last_nums:
            self.assertEqual(primes.first(first_nums), expected_list)
        if last_nums:
            primes.first(first_nums)
            self.assertEqual(primes.last(last_nums), expected_list)
