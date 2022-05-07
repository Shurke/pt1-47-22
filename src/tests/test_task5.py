"""
Unittest for task5.py
"""


import ddt
from src import task5
import unittest


@ddt.ddt
class TestTask2(unittest.TestCase):
    """Test cases for RealString"""

    def setUp(self) -> None:
        self.task = task5.DefaultList

    @ddt.data(
        ((1, 2, 3), 'def_val', 'append', 4, 6, 'def_val'),
        ((1, 2, 3), 'def_val', 'pop', 2, 1, 2),
        ((1, 2, 3), 'def_val', 'append', 4, 0, 1)
    )
    @ddt.unpack
    def test_class(self, seq, default_value, attr, attr_val, index, check_value):
        """Test class DefaultList"""

        test_object = self.task(seq, default_value)
        getattr(test_object, attr)(attr_val)
        result_val = test_object[index]
        self.assertEqual(result_val, check_value)
