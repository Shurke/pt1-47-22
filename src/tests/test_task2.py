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
        self.task = task2.RealString

    @ddt.data(
        ('Apple', 'Яблоко', False, 'greater than', False),
        ('Apple', 'Яблоко', True, 'less than', True),
        ('NotApple', 'НеЯблоко', False, 'equivalent', True),
    )
    @ddt.unpack
    def test_compare(self, str_1, str_2, str_2_is_realstring, compare, check):
        """Test: {0} {3} {1}(RealString={2}), expected result: {4}"""
        str_1 = self.task(str_1)
        if str_2_is_realstring:
            str_2 = self.task(str_2)
        if compare == 'greater than':
            result = str_1 > str_2
            self.assertEqual(result, check)
        elif compare == 'less than':
            result = str_1 < str_2
            self.assertEqual(result, check)
        else:
            result = str_1 == str_2
            self.assertEqual(result, check)
