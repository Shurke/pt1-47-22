"""Test module for task13_hm4 tests."""

import ddt
from src.homework5 import task13_hm4
import unittest
from unittest.mock import mock_open
from unittest.mock import patch


@ddt.ddt
class TestReplaceElements(unittest.TestCase):
    """Test cases task13_hm4."""

    def test_read_elements(self):
        """Test of read_elements from task13_hm4"""
        with patch("builtins.open", mock_open(read_data="14,Si,Silicon")):
            result = task13_hm4.read_elements()
        list_elements = ["Si"]
        self.assertEqual(result, list_elements)

    @ddt.data(
        ("Silver", ['B', 'C', 'N', 'O', 'Si', 'Lv', 'Er'], "SiLvEr"),
        ("silicon", ['B', 'C', 'N', 'O', 'Si', 'Li', 'Co', 'N'], "SiLiCoN"),
        ("hydrogen", ['S', 'Si', 'La', 'li', 'C', 'Co', 'O', 'N'], None),
    )
    @ddt.unpack
    def test_replace_elements(self, word, list_elem, expected_result):
        """Test replace_elements with next data {0} --> {1}"""
        result = task13_hm4.replace_elements(word, list_elem)
        self.assertEqual(result, expected_result)

    @ddt.data(
        ("Silver", "SiLvEr",
         "Ваше слово Silver может быть представлено как SiLvEr"),
        ("silicon", "SiLiCoN",
         "Ваше слово silicon может быть представлено как SiLiCoN"),
        ("hydrogen", None,
         "Ваше слово hydrogen невозможно выразить через обозначения химических элементов"),
    )
    @ddt.unpack
    def test_get_output(self, word, ability, expected_result):
        """Test get_output with next data {0}, {1} --> {2}"""
        result = task13_hm4.get_output(word, ability)
        self.assertEqual(result, expected_result)
