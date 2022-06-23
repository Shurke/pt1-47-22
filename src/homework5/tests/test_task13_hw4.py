"""Test module for task13_hw4 tests"""

import unittest
from src.homework4 import task13
import ddt
import collections

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestCheckWord(unittest.TestCase):
    """Test cases for check_word"""

    @ddt.data(
        ('Silver', 'SiLvEr'),
        ('Silicon', 'SiLiCoN'),
    )
    @ddt.unpack
    def test_check_word(self, word, expected_word):
        """Test check_word with input data {0} and expected word {1}"""
        elements = task13.read_file('../../homework4/elements.txt')
        result = task13.check_word(word, elements)
        self.assertEqual(result, expected_word)
