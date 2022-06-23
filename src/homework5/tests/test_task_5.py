"""Test module for task_5 tests"""

import collections
import ddt
from src.homework5 import task_5
import unittest

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestDefaultList(unittest.TestCase):
    """Test cases for DefaultList"""

    def setUp(self) -> None:
        self.defaultList = task_5.DefaultList

    @ddt.data(
        ([1, 2, 3, 4], 100, 2, 3),
        ([1, 2, 3, 4], 100, 3, 4),
        ([1, 2, 3, 4], 100, 10, 100),
    )
    @ddt.unpack
    def test_index(self, list, default_value, index, expected_result):
        """Test index method from class DefaultList."""
        obj = self.defaultList(list, default_value)
        result = obj[index]
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3, 4], [5, 6], 100, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3, 4], [-10, 0, 10], 100, [1, 2, 3, 4, -10, 0, 10]),
    )
    @ddt.unpack
    def test_extend(self, list_1, list_2, default_value, expected_result):
        """Test extend method from class DefaultList."""
        result = self.defaultList(list_1, default_value)
        result.extend(list_2)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3, 4], 6, 100, [1, 2, 3, 4, 6]),
        ([1, 2, 3, 4], 10, 100, [1, 2, 3, 4, 10]),
    )
    @ddt.unpack
    def test_append(self, list, item, default_value, expected_result):
        """Test append method from class DefaultList."""
        result = self.defaultList(list, default_value)
        result.append(item)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3, 4], 2, 6, 100, [1, 2, 6, 3, 4]),
        ([1, 2, 3, 4], 0, 10, 100, [10, 1, 2, 3, 4]),
    )
    @ddt.unpack
    def test_insert(self, list, index, item, default_value, expected_result):
        """Test insert method from class DefaultList."""
        result = self.defaultList(list, default_value)
        result.insert(index, item)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3, 4], 2, 100, [1, 3, 4]),
        ([1, 2, 3, 4], 3, 100, [1, 2, 4]),
    )
    @ddt.unpack
    def test_remove(self, list, item, default_value, expected_result):
        """Test remove method from class DefaultList."""
        result = self.defaultList(list, default_value)
        result.remove(item)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ([1, 2, 3, 4], 2, 100, [1, 2, 4]),
        ([1, 2, 3, 4], 0, 100, [2, 3, 4]),
    )
    @ddt.unpack
    def test_pop(self, list, index, default_value, expected_result):
        """Test pop method from class DefaultList."""
        result = self.defaultList(list, default_value)
        result.pop(index)
        self.assertEqual(result, expected_result)
