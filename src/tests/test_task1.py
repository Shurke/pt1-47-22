"""
Unittest for task1.py
"""


import ddt
from src import task1
import unittest


@ddt.ddt
class TestTask1(unittest.TestCase):
    """Test cases for KgToPounds"""

    def test_instance(self):
        """Tests for correct instantiation"""
        instance = task1.KgToPounds(5)
        self.assertIsInstance(instance, task1.KgToPounds)

    @ddt.data(
        (9, 9),
        (6, 6)
    )
    @ddt.unpack
    def test_kg(self, value, expected_value):
        """Test @property for KgToPounds.kg with value {0}"""
        test_object = task1.KgToPounds(0)
        test_object.kg = value
        self.assertEqual(test_object.kg, expected_value)

    @ddt.data(
        (5, 11.025),
        (7, 15.435),
        (0, 0.0)
    )
    @ddt.unpack
    def test_to_pounds_positive(self, kg, pounds):
        """Test positive cases for to_pounds method with input kg={0} and output pounds={1}"""
        test_object = task1.KgToPounds(kg)
        result = test_object.to_pounds()
        self.assertEqual(result, pounds)

    def test_wrong_kg_init(self):
        """Test negative case: create instance with string"""
        with self.assertRaises(ValueError) as context:
            task1.KgToPounds('5')
        self.assertIsInstance(context.exception, ValueError)

    def test_wrong_kg_set(self):
        """Test negative case: set kg with string"""
        test_instance = task1.KgToPounds(5)
        with self.assertRaises(ValueError) as context:
            test_instance.kg = '2'
        self.assertIsInstance(context.exception, ValueError)
