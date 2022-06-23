import unittest
from ddt import ddt, data, unpack
from task02 import RealString


@ddt
class RealStringTestCase(unittest.TestCase):

    @data(('Яблоко', 'Apple'),
          ('Я', 'I'),
          ('You', 'Вы'))
    @unpack
    def test_real_string(self, first_str, second_str):
        real_string = RealString(first_str)
        if len(first_str) > len(second_str):
            assert real_string > second_str
        elif len(first_str) == len(second_str):
            self.assertEqual(real_string, second_str)
