"""Test module for task13_hm4 tests."""

import unittest
from unittest.mock import patch, mock_open

import ddt

from homework5 import task13_hm4


@ddt.ddt
class TestReplaceElements(unittest.TestCase):
    """Test cases task13_hm4."""

    def setUp(self) -> None:
        self.open_file = task13_hm4.read_elements
        self.word = task13_hm4.replace_elements
        self.output = task13_hm4.get_output

    def test_read_elements(self):
        """Test of read_elements from task13_hm4"""
        with patch("builtins.open", mock_open(read_data="14,Si,Silicon")):
            result = self.open_file()
        list_elements = ["Si"]
        self.assertEqual(result, list_elements)

    @ddt.data(
        ("Silver", "SiLvEr"),
        ("silicon", "SiLiCoN"),
        ("hydrogen", None),
    )
    @ddt.unpack
    def test_replace_elements(self, word, expected_result):
        """Test replace_elements with next data {0} --> {1}"""
        result = self.word(word, self.open_file())
        self.assertEqual(result, expected_result)

    @ddt.data(
        ("Silver", "SiLvEr", "Ваше слово Silver может быть представлено как SiLvEr"),
        ("silicon", "SiLiCoN", "Ваше слово silicon может быть представлено как SiLiCoN"),
        ("hydrogen", None, "Ваше слово hydrogen невозможно выразить через обозначения химических элементов"),
    )
    @ddt.unpack
    def test_get_output(self, word, ability, expected_result):
        """Test get_output with next data {0}, {1} --> {2}"""
        result = self.output(word, ability)
        self.assertEqual(result, expected_result)