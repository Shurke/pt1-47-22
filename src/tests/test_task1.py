"""
Unittest for task1.py
"""


import ddt
from src import task1
import unittest


@ddt.ddt
class TestTask1(unittest.TestCase):
    """Test cases for KgToPounds"""

    def setUp(self) -> None:
        self.converter = task1.KgToPounds

    @ddt.data(
        (9, 9),
        (6, 6)
    )
    @ddt.unpack
    def test_kg(self, value, expected_value):
        """Test @property for KgToPounds.kg with value {0}"""
        test_object = self.converter(0)
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
        test_object = self.converter(kg)
        result = test_object.to_pounds()
        self.assertEqual(result, pounds)
