"""Test module for task_3 tests"""

import ddt
import unittest
import collections
from src.homework5 import task_3

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestSingleton(unittest.TestCase):
    """Test cases for Singleton"""

    @ddt.data(
        ('a', 'b'),
        (1, 2),
    )
    @ddt.unpack
    def test_singleton_new(self, value_1, value_2):
        """Test __new__ in Singleton with input data {0-1}"""
        id_value_1 = task_3.Singleton(value_1)
        id_value_2 = task_3.Singleton(value_2)
        self.assertEqual(id_value_1, id_value_2)

    def test_decorator_singleton(self):
        """Test for decorator singleton"""
        value_1 = RegularTestClass('a')
        value_2 = RegularTestClass('b')
        self.assertEqual(value_1, value_2)


@task_3.singleton
class RegularTestClass:
    """Regular class for wrapper testing"""
    def __init__(self, test):
        self.test = test
