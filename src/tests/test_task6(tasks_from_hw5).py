"""
Unittest for task6.py (testing tasks from hw_5)
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
class TestOldTaskTask2(unittest.TestCase):
    """Test cases for old_task/task2.py"""

    @ddt.data(
        ([0, 1, 2, 3, 4, 7, 8, 10], "0-4,7-8,10"),
        ([4, 7, 10], "4,7,10"),
        ([2, 3, 8, 9], "2-3,8-9")
    )
    @ddt.unpack
    def test_task2(self, row_list, check_value):
        """Task2.py: Tests the conversions sequences {0} to ranges {1}"""
        result = task2.get_string_with_ranges(row_list)
        self.assertEqual(result, check_value)


@ddt.ddt
class TestOldTaskTask4(unittest.TestCase):
    """Test cases for old_task/task4.py"""

    @ddt.data(
        (10, '10(8)'),
        (20, '20(16)'),
        (1, '1(1)'),
        (13, '13(16)')
    )
    @ddt.unpack
    def test_task4(self, input_number, check_value):
        """Task4.py: Tests returning the nearest power of two (like {1}) to a number {0}"""
        result = task4.nearest_degree(input_number)
        self.assertEqual(result, check_value)


@ddt.ddt
class TestOldTaskTask5(unittest.TestCase):
    """Test cases for old_task/task5.py"""

    @ddt.data(
        (10, '10(2)'),
        (16, '16(16)'),
        (12, '12(4)'),
        (96, '96(32)')
    )
    @ddt.unpack
    def test_task5(self, input_number, check_value):
        """Task5.py: Test return of the largest divisor (like{1} for {0}) that is a degree of two"""
        result = task5.nearest_divisor(input_number)
        self.assertEqual(result, check_value)


@ddt.ddt
class TestOldTaskTask9(unittest.TestCase):
    """Test cases for old_task/task9.py"""

    @ddt.data(
        ('cups', 4, 'Necessary 4 cup, 0 tablespoons, 0 teaspoons'),
        ('tablespoons', 54, 'Necessary 3 cup, 6 tablespoons, 0 teaspoons'),
        ('teaspoons', 59, 'Necessary 1 cup, 3 tablespoons, 2 teaspoons')
    )
    @ddt.unpack
    def test_task9(self, name, number, check_value):
        """Task9.py: Tests the conversion in cooking: {1} {0} -> {2}"""
        result = task9.cooking(number, name)
        self.assertEqual(result, check_value)


@ddt.ddt
class TestOldTaskTask12(unittest.TestCase):
    """Test cases for old_task/task12.py"""

    @ddt.data(
        ('LIV', 54),
        ('DLXVII', 567),
        ('MMMCMXCIX', 3999)
    )
    @ddt.unpack
    def test_task12(self, roman_num, check_value):
        """Task12.py: Tests the conversions of Roman number {0} to Arabic {1}"""
        result = task12.get_arabian(roman_num)
        self.assertEqual(result, check_value)


@ddt.ddt
class TestOldTaskTask13(unittest.TestCase):
    """Test cases for old_task/task13.py"""

    def test_task13_file_read(self):
        """Test of file reading from Task13.py"""
        with patch("builtins.open", mock_open(read_data="79,Au,Aurum\n")):
            result = task13.get_chem_elements_from_file()
        check_value = {'Au': 'Aurum'}
        self.assertEqual(result, check_value)

    @ddt.data(
        ('silicon', ['Au', 'Si', 'Li', 'C', 'O', 'N', 'Co'], 'SiLiCoN'),
        ('Cobalt', ['No', 'Wa', 'Y', 'To', 'Wo', 'Rk'], '')
    )
    @ddt.unpack
    def test_task13_word_making_up(self, word, sequence, check_value):
        """Test word making up from Task13.py with data {0}, {1} and expected value {2}"""
        result = task13.word_with_elem(word, sequence)
        self.assertEqual(result, check_value)
