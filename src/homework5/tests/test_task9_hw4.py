"""Test module for task9_hw4 tests"""

import unittest
from src.homework4 import task9
import ddt
import collections

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestConverse(unittest.TestCase):
    """Test cases for converse"""

    @ddt.data(
        ({'cup': 1, 'tablespoon': 1, 'teaspoon': 50}, {'cup': 4, 'tablespoon': 1, 'teaspoon': 2}),
        ({'cup': 1, 'tablespoon': 20, 'teaspoon': 10}, {'cup': 5, 'tablespoon': 2, 'teaspoon': 0}),
        ({'cup': 2, 'tablespoon': 10, 'teaspoon': 50}, {'cup': 6, 'tablespoon': 5, 'teaspoon': 1}),
    )
    @ddt.unpack
    def test_converse(self, component, expected_component):
        """Test converse with input data {0} and expected nearest divisor {1}"""
        result = task9.converse(component)
        self.assertEqual(result, expected_component)
