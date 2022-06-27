"""Test module for task_3 tests."""

import ddt
from src.homework5 import task_3
import unittest


@ddt.ddt
class TestSingleton(unittest.TestCase):
    """Test cases for Singleton."""

    @ddt.data(
        ('x', 'y'),
        (10, 20)
    )
    @ddt.unpack
    def test_class_singleton(self, value_1, value_2):
        """Test for Singleton class with next date {0} = {1}"""
        id_1 = task_3.Singleton(value_1)
        id_2 = task_3.Singleton(value_2)
        self.assertEqual(id_1, id_2)

    def test_singleton(self):
        """Test for decorator singleton"""
        obj_1 = RegularTestClass('123')
        obj_2 = RegularTestClass('1234')
        self.assertIs(obj_1, obj_2)


@task_3.singleton
class RegularTestClass:
    """Regular class for wrapper testing"""

    def __init__(self, test):
        self.test = test
