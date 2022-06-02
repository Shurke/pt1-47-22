"""Test module for task3 (Singleton) tests"""
import unittest
import ddt
from src.homework5 import task3


@ddt.ddt
class TestSingleton(unittest.TestCase):
    """Test case for Singleton"""

    def setUp(self) -> None:
        self.singleton = task3.Singleton

    @ddt.data(
        ((1, 2, 3), (4, 5, 6)),
        ('Hello', 'World')
    )
    @ddt.unpack
    def test_class_singleton(self, inst_1, inst_2):
        """Test for Singleton class with different elem {0} and {1}"""
        id_first = self.singleton(inst_1)
        id_second = self.singleton(inst_2)
        self.assertEqual(id_first, id_second)

    @ddt.data(
        ((1, 2, 3), (4, 5, 6)),
        ('Hello', 'World')
    )
    @ddt.unpack
    def test_wrapper_singleton(self, inst_1, inst_2):
        """Test for Singleton class"""
        id_first = ClassTestWrap(inst_1)
        id_second = ClassTestWrap(inst_2)
        self.assertEqual(id_first, id_second)


@task3.singleton
class ClassTestWrap:
    def __init__(self, smth_test):
        self.smth_test = smth_test

    def multiply(self):
        return self.smth_test * 2
