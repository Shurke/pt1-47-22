import unittest
from ddt import ddt, data, unpack
from task05 import DefaultList


@ddt
class TestSuiteDefaultList(unittest.TestCase):
    """DefaultList test suite."""

    @data(([1, 2, 3, 4, 5], None))
    @unpack
    def test_default_list_index_error(self, test_list, expected_val):
        """Test DefaultList index err.

        :param test_list:      list of test
        :param expected_val:   expected value
        """
        test_list = DefaultList(test_list)
        out_of_range_idx = len(test_list) + 1
        self.assertEqual(test_list[out_of_range_idx], expected_val)

    @data(([1, 2, 3, 4, 5], [1, 2, 3, 4]))
    @unpack
    def test_default_list_pop(self, test_list, expected_list):
        """Test DefaultList pop functionality.

        :param test_list:      list of test
        :param expected_list:  expected list
        """
        test_list = DefaultList(test_list)
        test_list.pop()
        self.assertEqual(test_list, expected_list)

    @data(([1, 2], [1, 2, 3], 3))
    @unpack
    def test_default_list_append(self, test_list, expected_list, append_val):
        """Test DefaultList append functionality.

        :param test_list:      list of test
        :param expected_list:  expected list
        :param append_val:     val for append
        """
        test_list = DefaultList(test_list)
        test_list.append(append_val)
        self.assertEqual(test_list, expected_list)

    @data(([1, 2, 3], [2, 3], 1))
    @unpack
    def test_default_list_remove(self, test_list, expected_list, remove_val):
        """Test DefaultList remove functionality.

        :param test_list:      list of test
        :param expected_list:  expected list
        :param remove_val:     val for append
        """
        test_list = DefaultList(test_list)
        test_list.remove(remove_val)
        self.assertEqual(test_list, expected_list)

    @data(([1, 2, 3], [1, 2, 99, 3], 2, 99))
    @unpack
    def test_default_list_insert(self, test_list, expected_list, insert_idx, insert_val):
        """Test DefaultList insert functionality.

        :param test_list:      list of test
        :param expected_list:  expected list
        :param insert_idx:     index for insert
        :param insert_val:     val for insert
        """
        test_list = DefaultList(test_list)
        test_list.insert(insert_idx, insert_val)
        self.assertEqual(test_list, expected_list)
