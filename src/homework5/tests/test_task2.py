"""Test module for task2 (RealString) tests"""
import unittest
import ddt
from src.homework5 import task2


@ddt.ddt
class TestRealString(unittest.TestCase):
    """Test case for RealString"""

    def setUp(self) -> None:
        self.real_str = task2.RealString

    @ddt.data(
        ('meat', 'мясо', True),
        ('car', 'машина', False)
    )
    @ddt.unpack
    def test_str_eq(self, str_1, str_2, expect):
        """Test case for compare equal strings {0} and {1}"""
        str_to_compare = self.real_str(str_1).__eq__(str_2)
        self.assertEqual(str_to_compare, expect)

    @ddt.data(
        ('ball', 'мяч', False),
        ('car', 'машина', True),
        ('food', 'meal', False)
    )
    @ddt.unpack
    def test_str_less(self, str_1, str_2, expect):
        """Test case for compare (less) strings {0} and {1}"""
        str_to_compare_1 = self.real_str(str_1)
        str_to_compare_2 = self.real_str(str_2)
        result = str_to_compare_1 < str_to_compare_2
        self.assertEqual(result, expect)

    @ddt.data(
        ('ball', 'мяч', True),
        ('car', 'машина', False),
        ('food', 'meal', False)
    )
    @ddt.unpack
    def test_str_more(self, str_1, str_2, expect):
        """Test case for compare (more) strings {0} and {1}"""
        str_to_compare_1 = self.real_str(str_1)
        str_to_compare_2 = self.real_str(str_2)
        result = str_to_compare_1 > str_to_compare_2
        self.assertEqual(result, expect)
