"""
Unittest for task5.py
"""


import ddt
from src.old_tasks import task12
from src.old_tasks import task13
from src.old_tasks import task2
from src.old_tasks import task4
from src.old_tasks import task5
from src.old_tasks import task9
import unittest
from unittest.mock import mock_open
from unittest.mock import patch


@ddt.ddt
class TestTask2(unittest.TestCase):
    """Test cases for RealString"""

    def setUp(self) -> None:
        self.task2 = task2.get_string_with_ranges
        self.task4 = task4.nearest_degree
        self.task5 = task5.nearest_divisor
        self.task9 = task9.cooking
        self.task12 = task12.get_arabian
        self.task13_word = task13.word_with_elem
        self.task13_file = task13.get_chem_elements_from_file

    @ddt.data(
        ([0, 1, 2, 3, 4, 7, 8, 10], "0-4,7-8,10"),
        ([4, 7, 10], "4,7,10"),
        ([2, 3, 8, 9], "2-3,8-9")
    )
    @ddt.unpack
    def test_task2(self, row_list, check_value):
        """Test Task2.py with data {0} and expected value {1}"""
        result = self.task2(row_list)
        self.assertEqual(result, check_value)

    @ddt.data(
        (10, '10(8)'),
        (20, '20(16)'),
        (1, '1(1)'),
        (13, '13(16)')
    )
    @ddt.unpack
    def test_task4(self, input_number, check_value):
        """Test Task4.py with data {0} and expected value {1}"""
        result = self.task4(input_number)
        self.assertEqual(result, check_value)

    @ddt.data(
        (10, '10(2)'),
        (16, '16(16)'),
        (12, '12(4)'),
        (96, '96(32)')
    )
    @ddt.unpack
    def test_task5(self, input_number, check_value):
        """Test Task5.py with data {0} and expected value {1}"""
        result = self.task5(input_number)
        self.assertEqual(result, check_value)

    @ddt.data(
        ('cups', 4, 'Necessary 4 cup, 0 tablespoons, 0 teaspoons'),
        ('tablespoons', 54, 'Necessary 3 cup, 6 tablespoons, 0 teaspoons'),
        ('teaspoons', 59, 'Necessary 1 cup, 3 tablespoons, 2 teaspoons')
    )
    @ddt.unpack
    def test_task9(self, name, number, check_value):
        """Test Task9.py with data {0}, {1} and expected value {2}"""
        result = self.task9(number, name)
        self.assertEqual(result, check_value)

    @ddt.data(
        ('LIV', 54),
        ('DLXVII', 567),
        ('MMMCMXCIX', 3999)
    )
    @ddt.unpack
    def test_task12(self, roman_num, check_value):
        """Test Task12.py with data {0} and expected value {1}"""
        result = self.task12(roman_num)
        self.assertEqual(result, check_value)

    def test_task13_file_read(self):
        """Test of reading from Task13.py"""
        with patch("builtins.open", mock_open(read_data="79,Au,Aurum\n")):
            result = self.task13_file()
        check_value = {'Au': 'Aurum'}
        self.assertEqual(result, check_value)

    @ddt.data(
        ('silicon', ['Au', 'Si', 'Li', 'C', 'O', 'N', 'Co'], 'SiLiCoN'),
        ('Cobalt', ['No', 'Wa', 'Y', 'To', 'Wo', 'Rk'], '')
    )
    @ddt.unpack
    def test_task13_word_making_up(self, word, sequence, check_value):
        """Test word making up from Task13.py with data {0}, {1} and expected value {2}"""
        result = self.task13_word(word, sequence)
        self.assertEqual(result, check_value)
