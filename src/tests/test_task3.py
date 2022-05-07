"""
Unittest for task3.py
"""


import ddt
from src import task3
import unittest


@ddt.ddt
class TestTask2(unittest.TestCase):
    """Test cases for RealString"""

    def setUp(self) -> None:
        self.task = task3.SingletonClass

    def test_class(self):
        """Test class SingletonClass"""

        object_1 = self.task('MyName')
        object_2 = self.task('NotMyName')
        self.assertEqual(object_1, object_2)

    def test_wrapper(self):
        """Test class-wrapper singleton_wrapper"""

        @task3.singleton_wrapper
        class CustomTestClass:

            def __init__(self, name):
                self.name = name

            @staticmethod
            def some_business_method():
                """Method docstring(pylint)"""
                return 'You are very cool!'

            @staticmethod
            def some_other_business_method():
                """Method docstring(pylint)"""
                return 'You are very cool!'

        object_1 = CustomTestClass('MyName')
        object_2 = CustomTestClass('NotMyName')
        self.assertEqual(object_1, object_2)
