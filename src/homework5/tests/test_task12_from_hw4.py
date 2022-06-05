"""Test module for task12_from_hw4 (convert_roman) tests"""
import unittest
import ddt
from src.homework5 import task12_from_hw4


@ddt.ddt
class TestRomanConvert(unittest.TestCase):
    """Test case for method convert_roman"""

    def setUp(self) -> None:
        self.convert = task12_from_hw4.convert_roman

    @ddt.data(
        ('MD', 1500, True),
        ('XCIX', 99, True),
        ('MMCMXCIX', 3000, False)
    )
    @ddt.unpack
    def test_roman_to_decimal(self, roman_numb, dec_numb, expect):
        """Test case for convert_roman with roman {0} and decimal {1} numbers"""
        result = self.convert(roman_numb) == dec_numb
        self.assertEqual(result, expect)
