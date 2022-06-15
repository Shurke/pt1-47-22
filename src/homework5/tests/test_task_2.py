"""Test module for task_2 tests."""


import unittest
import ddt
from src.homework5 import task_2


@ddt.ddt
class TestRealString(unittest.TestCase):
    """Test cases for RealString."""

    def setUp(self) -> None:
        self.string = task_2.RealString

    @ddt.data(
        ("Яблоко", "Apple", False, True),
        ("Table", "Стол", False, True),
        ("Яблоко", "Огурец", True, False),
        ("Table", "Стол", True, True),
    )
    @ddt.unpack
    def test_more(self, str_1, str_2, str_2_is_exemplar, expected_result):
        """Test case for gt method with next date {0} > {1}(RealString={2}) --> {3}"""
        str_1 = self.string(str_1)
        if str_2_is_exemplar:
            str_2 = self.string(str_2)
        result = str_1 > str_2
        self.assertEqual(result, expected_result)

    @ddt.data(
        ("Яблоко", "Огурец", False, True),
        ("Яблоко", "Огурец", True, True),
        ("Хлеб", "Bread", False, False),
        ("Хлеб", "Bread", True, False),
    )
    @ddt.unpack
    def test_eq(self, str_1, str_2, str_2_is_exemplar, expected_result):
        """Test case for eq method with next date {0} = {1}(RealString={2}) --> {3}"""
        str_1 = self.string(str_1)
        if str_2_is_exemplar:
            str_2 = self.string(str_2)
        result = str_1 == str_2
        self.assertEqual(result, expected_result)
