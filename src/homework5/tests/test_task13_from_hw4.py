"""Test module for task13_from_hw4 (chemistry word) tests"""
import unittest
from unittest.mock import mock_open
from unittest.mock import patch
import ddt
from src.homework5 import task13_from_hw4


@ddt.ddt
class TestChemistry(unittest.TestCase):
    """Test case for task13(chemistry word)"""

    def setUp(self) -> None:
        self.output = task13_from_hw4.chemistry_output
        self.word = task13_from_hw4.chemistry_word
        self.opn = task13_from_hw4.mendeleev_list

    def test_file_read(self):
        """Test case of file reading"""
        with patch("builtins.open", mock_open(read_data="30,Zn,Zinc")):
            result = self.opn()
        expect = ['zn']
        self.assertEqual(result, expect)

    @ddt.data(
        ('silicon', 'silicon', True),
        ('silicon', None, False),
        ('CupRum', None, True)
    )
    @ddt.unpack
    def test_chemistry_word(self, word, res_value, expect):
        """Test case of chemistry_word method with word for convert {0} and result value {1}"""
        result = self.word(word, self.opn()) == res_value
        self.assertEqual(result, expect)

    @ddt.data(
        ('silicon', 'The word silicon can be represented with chemical elements as silicon',
         'silicon', True),
        ('silicon', 'The word silicon cannot be converted with chemical elements', 'silicon', False),
        ('CupRum', 'The word CupRum cannot be converted with chemical elements', None, True)
    )
    @ddt.unpack
    def test_chemistry_output(self, user_word, ability, lst_chem, expect):
        """Test case of chemistry_output method with user_word {0} and ability {1}"""
        result = self.output(user_word, lst_chem) == ability
        self.assertEqual(result, expect)
