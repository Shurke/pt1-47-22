"""Test module for task_1 tests"""

import unittest
from src.homework5 import task_1
import ddt
import collections

collections.Callable = collections.abc.Callable


@ddt.ddt
class TestKgToPounds(unittest.TestCase):
    """Test cases for KgToPounds"""

    def setUp(self) -> None:
        self.kg_to_pounds = task_1.KgToPounds

    def test_KgToPounds_instantiation(self):
        """Test case for class KgToPounds with TypeError"""
        with self.assertRaises(TypeError):
            self.kg_to_pounds('10')

    @ddt.data(
        (10, 22.05),
        (15, 33.075),
        (20, 44.1),
    )
    @ddt.unpack
    def test_to_pounds(self, kg, expected_pounds):
        """Test to_pounds with input data {0} and expected result {1}"""
        result = self.kg_to_pounds(kg).to_pounds()
        self.assertEqual(result, expected_pounds)

    @ddt.data(
        (10, 10),
        (15, 15),
        (20, 20)
    )
    @ddt.unpack
    def test_write_kg(self, kg, expected_kg):
        """Test case for @kg.setter method with input data {0} and expected_kg {1}"""
        result = self.kg_to_pounds(kg).kg
        self.assertEqual(result, expected_kg)
