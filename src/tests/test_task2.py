"""
Unittest for task2.py
"""


import ddt
from src import task2
import unittest


@ddt.ddt
class TestTask2(unittest.TestCase):
    """Test cases for RealString"""

    @ddt.data(
        ('Apple', 'Яблоко', False, True),
        ('Яблоко', 'Apple', True, False)
    )
    @ddt.unpack
    def test_greater_than(self, str_1, str_2, str_2_is_realstring, check):
        """Greater than test: {0} greater than {1}(RealString={2}), expected result: {3}"""
        str_1 = task2.RealString(str_1)
        if str_2_is_realstring:
            str_2 = task2.RealString(str_2)
        result = str_1 < str_2
        self.assertEqual(result, check)

    @ddt.data(
        ('Apple', 'Яблоко', False, False),
        ('Яблоко', 'Apple', True, True)
    )
    @ddt.unpack
    def test_less_than(self, str_1, str_2, str_2_is_realstring, check):
        """Less than test: {0} less than {1}(RealString={2}), expected result: {3}"""
        str_1 = task2.RealString(str_1)
        if str_2_is_realstring:
            str_2 = task2.RealString(str_2)
        result = str_1 > str_2
        self.assertEqual(result, check)

    @ddt.data(
        ('Note', 'Cash', False, True),
        ('Яблоко', 'Apple', True, False)
    )
    @ddt.unpack
    def test_equivalent(self, str_1, str_2, str_2_is_realstring, check):
        """Equivalent test: {0} equivalent {1}(RealString={2}), expected result: {3}"""
        str_1 = task2.RealString(str_1)
        if str_2_is_realstring:
            str_2 = task2.RealString(str_2)
        result = str_1 == str_2
        self.assertEqual(result, check)

    @ddt.data(
        ('greater', ),
        ('less', ),
        ('equivalent', )
    )
    @ddt.unpack
    def test_negative_cases(self, action):
        """Test '{0}' for TypeError"""
        with self.assertRaises(TypeError) as context:
            test_instance = task2.RealString('Some string')
            if action == 'greater':
                if test_instance > 0:
                    pass
            elif action == 'less':
                if test_instance < 0:
                    pass
            elif action == 'equivalent':
                if test_instance == 0:
                    pass
            else:
                raise ValueError('incorrect action')
        self.assertIsInstance(context.exception, TypeError)
