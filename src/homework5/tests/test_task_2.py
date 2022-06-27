"""Test module for task_2 tests."""

import ddt
from src.homework5 import task_2
import unittest


@ddt.ddt
class TestRealString(unittest.TestCase):
    """Test cases for RealString."""

    @ddt.data(
        ("Яблоко", "Apple", False, True),
        ("Table", "Стол", False, True),
        ("Яблоко", "Огурец", True, False),
        ("Table", "Стол", True, True),
    )
    @ddt.unpack
    def test_more(self, str_1, str_2, is_real_str, expected_result):
        """Test case for gt method with next date {0} > {1}(RealString={2}) --> {3}"""
        str_1 = task_2.RealString(str_1)
        if is_real_str:
            str_2 = task_2.RealString(str_2)
        result = str_1 > str_2
        self.assertEqual(result, expected_result)

    @ddt.data(
        ("Яблоко", "Огурец", False, True),
        ("Яблоко", "Огурец", True, True),
        ("Хлеб", "Bread", False, False),
        ("Хлеб", "Bread", True, False),
    )
    @ddt.unpack
    def test_eq(self, str_1, str_2, is_real_str, expected_result):
        """Test case for eq method with next date {0} = {1}(RealString={2}) --> {3}"""
        str_1 = task_2.RealString(str_1)
        if is_real_str:
            str_2 = task_2.RealString(str_2)
        result = str_1 == str_2
        self.assertEqual(result, expected_result)
