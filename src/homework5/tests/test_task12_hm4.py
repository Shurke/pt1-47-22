"""Test module for task12_hm4 tests."""

import ddt
from src.homework5 import task12_hm4
import unittest


@ddt.ddt
class TestRomanTranslate(unittest.TestCase):
    """Test cases for roman_translate."""

    def setUp(self) -> None:
        self.translate = task12_hm4.roman_translate

    @ddt.data(
        ("XCVI", 96),
        ("LXXXVIII", 88),
        ("CCXLVI", 246),
    )
    @ddt.unpack
    def test_roman_translate(self, number_roman, expected_result):
        """Test roman_translate with next data {0} --> {1}"""
        result = self.translate(number_roman)
        self.assertEqual(result, expected_result)
