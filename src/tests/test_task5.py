"""
Unittest for task5.py
"""


import ddt
from src import task5
import unittest


@ddt.ddt
class TestTask2(unittest.TestCase):
    """Test cases for DefaultList"""

    def setUp(self) -> None:
        self.default_list = task5.DefaultList

    @ddt.data(
        ((1, 2, 3), 'def_val', 'pop', 2, 1, 2),
        ((1, 2, 3), 'def_val', 'append', 4, 0, 1),
        ((1, 2, 3), 'def_val', 'extend', [4, 5], 3, 4),
        ((1, 2, 3), 'def_val', 'remove', 2, 1, 3)
    )
    @ddt.unpack
    def test_methods_without_insert(self, seq, default_value, attr, attr_val, index, check_value):
        """Test methods without insert from class DefaultList ()"""

        test_object = self.default_list(seq, default_value)
        getattr(test_object, attr)(attr_val)
        result_val = test_object[index]
        self.assertEqual(result_val, check_value)

    @ddt.data(
        ((1, 2, 3), 'def_val', 2, 1, 1, 2),
        ((1, 2, 3), 'def_val', 4, 2, 0, 1),
    )
    @ddt.unpack
    def test_method_insert(self, seq, default_value, attr_val, attr_ind, index, check_value):
        """Test method insert from class DefaultList"""

        test_object = self.default_list(seq, default_value)
        test_object.insert(attr_ind, attr_val)
        result_val = test_object[index]
        self.assertEqual(result_val, check_value)

    @ddt.data(
        ((1, 2, 3), 'def_val', 6, 'def_val'),
        ((4, 5, 6), 'def_val', 0, 4)
    )
    @ddt.unpack
    def test_default_value(self, seq, default_value, index, check_value):
        """Test default value of instance from class DefaultList"""

        test_object = self.default_list(seq, default_value)
        result_val = test_object[index]
        self.assertEqual(result_val, check_value)
