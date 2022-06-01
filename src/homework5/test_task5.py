"""Test module for task5 (DefaultList) tests"""
import unittest
import ddt
import task5


@ddt.ddt
class TestDefaultList(unittest.TestCase):
    """Test case for DefaultList"""

    def setUp(self) -> None:
        self.def_lst = task5.DefaultList

    @ddt.data(
        ([1, 2, 3], 'wrong data', 2, 3),
        ([(1, 2, 3), 25], 'wrong data', 2, 'wrong data'),
        (['Hello'], 'wrong data', 1, 'wrong data')
    )
    @ddt.unpack
    def test_index(self, user_lst, def_value, item_lst, expect):
        """Test case for getitem method with list {0}, error {1} and index {2}"""
        lst_check = self.def_lst(user_lst, def_value)
        result = lst_check[item_lst]
        self.assertEqual(result, expect)

    @ddt.data(
        ([1, 2, 3, 4], 'wrong data', 'extend', [26, 31], 5, 31),
        ([1, 2, 3], 'wrong data', 'append', 4, 3, 4),
        ([1, 2, 3, 4], 'wrong data', 'remove', 4, 2, 3)
    )
    @ddt.unpack
    def test_default_methods(self, test_lst, def_value, name_method, method_value, index, exp_val):
        """Test case for Python's list method with list {0}, name method {2}"""
        lst_check = self.def_lst(test_lst, def_value)
        getattr(lst_check, name_method)(method_value)
        result_def = lst_check[index]
        self.assertEqual(result_def, exp_val)
