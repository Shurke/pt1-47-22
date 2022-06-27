"""Test module for task_1 tests."""

import ddt
from src.homework5 import task_1
import unittest


@ddt.ddt
class TestKgToPounds(unittest.TestCase):
    """Test cases for KgToPounds."""

    @ddt.data(
        (5, ),
        (5.0, ),
    )
    @ddt.unpack
    def test_init_is_instance(self, kg):
        """Instance creation test"""
        self.assertIsInstance(task_1.KgToPounds(kg), task_1.KgToPounds)

    def test_init_error(self):
        """Error test on instantiation"""
        with self.assertRaises(ValueError):
            task_1.KgToPounds('six')

    @ddt.data(
        (100, 220.5),
        (5, 11.025),
    )
    @ddt.unpack
    def test_to_pounds(self, number, expected_result):
        """Test positive cases for to_pounds method with next date {0} --> {1} ."""
        result = task_1.KgToPounds(number).to_pounds()
        self.assertEqual(result, expected_result)

    def test_kg_setter_error(self):
        """Test negative cases for setter kg method"""
        obj = task_1.KgToPounds(10)
        with self.assertRaises(ValueError):
            obj.kg = 'six'

    @ddt.data(
        (5, 5),
        (15, 15)
    )
    @ddt.unpack
    def test_kg(self, value, expected_result):
        """Test cases for kg method with next date {0} = {1}"""
        result = task_1.KgToPounds(value).kg
        self.assertEqual(result, expected_result)
