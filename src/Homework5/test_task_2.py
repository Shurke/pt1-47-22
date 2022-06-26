import unittest
from ddt import ddt, data, unpack
from task02 import RealString


@ddt
class TestSuiteRealString(unittest.TestCase):
    """RealString test suite."""

    @data(('Яблоко', 'Apple', '>'),
          ('Я', 'I', '=='),
          ('You', 'Вы', '>'))
    @unpack
    def test_real_string(self, first_str, second_str, condition):
        """Test real string working.

        :param first_str:         first str
        :param second_str:        second str"""
        condition_mapping = {'>': self.assertGreater,
                             '==': self.assertEqual}
        real_string = RealString(first_str)
        condition_mapping[condition](real_string, second_str)
