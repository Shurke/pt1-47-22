from ddt import data
from ddt import ddt
import unittest
from task03 import Class1
from task03 import Class2


@ddt
class TestSuiteSingleton(unittest.TestCase):
    """Singleton test suite."""

    @data(Class1, Class2)
    def test_singleton(self, test_class):
        """Test singleton class.

        :param test_class:   class for test
        """
        x = test_class()
        y = test_class()
        self.assertIs(x, y)
