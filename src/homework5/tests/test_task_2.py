"""Test module for task_2 tests"""

import collections
import ddt
from src.homework5 import task_2
import unittest

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestRealString(unittest.TestCase):
    """Test cases for RealString"""

    @ddt.data(
        ('Яблоко', 'Apple', False),
        ('Дом', 'House', False),
        ('Дом', 'Кот', True)
    )
    @ddt.unpack
    def test_eq(self, str_1, str_2, expected_result):
        """Test __eq__ with input data {0, 1} and expected result {2}"""
        str_1 = task_2.RealString(str_1)
        result = str_1 == str_2
        self.assertEqual(result, expected_result)

    @ddt.data(
        ('Яблоко', 'Apple', False),
        ('Дом', 'House', True),
        ('Дом', 'Кот', False)
    )
    @ddt.unpack
    def test_lt(self, str_1, str_2, expected_result):
        """Test __lt__ with input data {0, 1} and expected result {2}"""
        str_1 = task_2.RealString(str_1)
        result = str_1 < str_2
        self.assertEqual(result, expected_result)
