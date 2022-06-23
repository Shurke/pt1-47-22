"""Test module for task5_hw4 tests"""

import collections
import ddt
from src.homework4 import task5
import unittest

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestFindNear(unittest.TestCase):
    """Test cases for find_near"""

    @ddt.data(
        (10, 2),
        (16, 16),
        (12, 4),
    )
    @ddt.unpack
    def test_find_near(self, numb, expected_nearest_divisor):
        """Test find_near with input data {0} and expected nearest divisor {1}"""
        result = task5.find_near(numb)
        self.assertEqual(result, expected_nearest_divisor)
