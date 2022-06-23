from task05 import DefaultList
import unittest


class DefaultListTestCase(unittest.TestCase):

    def test_default_list(self):
        test_list = DefaultList([1, 2, 3, 4, 5])
        self.assertEqual(test_list[7], None)
        test_list.pop(2)
        self.assertEqual(test_list, [1, 2, 4, 5])
        test_list.append(2)
        self.assertEqual(test_list, [1, 2, 4, 5, 2])
        test_list.remove(1)
        self.assertEqual(test_list, [2, 4, 5, 2])
        test_list.insert(2, 99)
        self.assertEqual(test_list, [2, 4, 99, 5, 2])
