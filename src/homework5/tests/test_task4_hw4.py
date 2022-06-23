"""Test module for task4_hw4 tests"""

import collections
import ddt
from src.homework4 import task4
import unittest

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestFindNear(unittest.TestCase):
    """Test cases for find_near"""

    @ddt.data(
        (10, 3),
        (20, 4),
        (40, 5),
        (70, 6),
    )
    @ddt.unpack
    def test_find_near(self, numb, expected_nearest_degree):
        """Test find_near with input data {0} and expected nearest degree {1}"""
        result = task4.find_near(numb)
        self.assertEqual(result, expected_nearest_degree)
