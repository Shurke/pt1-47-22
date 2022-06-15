"""Test module for task_5 tests"""

import ddt
from src.homework5 import task_5
import unittest


@ddt.ddt
class TestDefaultList(unittest.TestCase):
    """Test case for DefaultList"""

    def setUp(self) -> None:
        self.defaultList = task_5.DefaultList

    @ddt.data(
        ([1, 2, 5, 7, 8], 'default', 3, 7),
        ([1, 2, 5, 7, 8], 'default', 10, 'default'),
        ([1, 2, 5, 7, 8], 'default', -1, 8)
    )
    @ddt.unpack
    def test_index(self, lst, default_value, index, expected_result):
        """Test index method from class DefaultList."""
        obj = self.defaultList(lst, default_value)
        result = obj[index]
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3], [6, 7], [1, 2, 3, 6, 7]),
        ([1, 2, 3], [-1, 3, 0], [1, 2, 3, -1, 3, 0]),
    )
    @ddt.unpack
    def test_extend(self, lst, item, expected_result):
        """Test extend method from class DefaultList."""
        result = self.defaultList(lst)
        result.extend(item)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3], 4, [1, 2, 3, 4]),
        ([1, 2, 3, 4], 0, [1, 2, 3, 4, 0]),
    )
    @ddt.unpack
    def test_append(self, lst, item, expected_result):
        """Test append method from class DefaultList."""
        result = self.defaultList(lst)
        result.append(item)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3], 1, 100, [1, 100, 2, 3]),
        ([1, 2, 3, 4], -1, 100, [1, 2, 3, 100, 4]),
    )
    @ddt.unpack
    def test_insert(self, lst, index, item, expected_result):
        """Test insert method from class DefaultList."""
        result = self.defaultList(lst)
        result.insert(index, item)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3, 5, 3], 3, [1, 2, 5, 3]),
        ([5, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    )
    @ddt.unpack
    def test_remove(self, lst, item, expected_result):
        """Test remove method from class DefaultList."""
        result = self.defaultList(lst)
        result.remove(item)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3, 4, 5], 2, [1, 2, 4, 5]),
        ([1, 2, 3, 4, 5], 0, [2, 3, 4, 5]),
    )
    @ddt.unpack
    def test_pop(self, lst, index, expected_result):
        """Test pop method from class DefaultList."""
        result = self.defaultList(lst)
        result.pop(index)
        self.assertEqual(result, expected_result)
