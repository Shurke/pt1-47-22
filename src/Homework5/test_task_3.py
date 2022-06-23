import unittest
from ddt import ddt, data
from task03 import Class1, Class2


@ddt
class SingletonTestCase(unittest.TestCase):

    @data(Class1, Class2)
    def test_singleton(self, test_class):
        x = test_class()
        y = test_class()
        x.val = 72
        self.assertIs(x, y)
        self.assertEqual(y.val, 72)
        y.val = 1
        self.assertEqual(x.val, 1)
