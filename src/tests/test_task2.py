"""
Unittest for task2.py
"""


import ddt
from src import task2
import unittest


@ddt.ddt
class TestTask2(unittest.TestCase):
    """Test cases for RealString"""

    def setUp(self) -> None:
        self.real_string = task2.RealString

    @ddt.data(
        ('Apple', 'Яблоко', False, True),
        ('Яблоко', 'Apple', True, False)
    )
    @ddt.unpack
    def test_greater_than(self, str_1, str_2, str_2_is_realstring, check):
        """Greater than test: {0} greater than {1}(RealString={2}), expected result: {3}"""
        str_1 = self.real_string(str_1)
        if str_2_is_realstring:
            str_2 = self.real_string(str_2)
        result = str_1 < str_2
        self.assertEqual(result, check)

    @ddt.data(
        ('Apple', 'Яблоко', False, False),
        ('Яблоко', 'Apple', True, True)
    )
    @ddt.unpack
    def test_less_than(self, str_1, str_2, str_2_is_realstring, check):
        """Less than test: {0} less than {1}(RealString={2}), expected result: {3}"""
        str_1 = self.real_string(str_1)
        if str_2_is_realstring:
            str_2 = self.real_string(str_2)
        result = str_1 > str_2
        self.assertEqual(result, check)

    @ddt.data(
        ('Note', 'Cash', False, True),
        ('Яблоко', 'Apple', True, False)
    )
    @ddt.unpack
    def test_equivalent(self, str_1, str_2, str_2_is_realstring, check):
        """Equivalent test: {0} equivalent {1}(RealString={2}), expected result: {3}"""
        str_1 = self.real_string(str_1)
        if str_2_is_realstring:
            str_2 = self.real_string(str_2)
        result = str_1 == str_2
        self.assertEqual(result, check)
