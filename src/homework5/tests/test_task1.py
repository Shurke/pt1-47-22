"""Test module for task1 (KgToPounds) tests"""
import ddt
from src.homework5 import task1
import unittest


@ddt.ddt
class TestKgToPounds(unittest.TestCase):
    """TestCase for KgToPounds"""

    def setUp(self) -> None:
        self.kg_to_pounds = task1.KgToPounds

    def test_KgToPounds_error(self):
        """Test case for class KgToPounds with raises error"""
        with self.assertRaises(TypeError):
            self.kg_to_pounds('5')

    @ddt.data(
        (10, 22.05),
        (100, 220.5),
        (1000, 2205)
    )
    @ddt.unpack
    def test_to_pounds(self, kg, expected_res):
        """Test case for to_pounds method with kg={0} and result={1}"""
        result_to_pounds = self.kg_to_pounds(kg).to_pounds()
        self.assertEqual(result_to_pounds, expected_res)

    @ddt.data(
        (76, 76, True),
        (4, 4, True),
        (5, 6, False)
    )
    @ddt.unpack
    def test_write_kg(self, value, expected_kg, exp_res):
        """Test case for @kg.setter method with kg={0} and expected_kg {1}"""
        result = expected_kg == self.kg_to_pounds(value).kg
        self.assertEqual(result, exp_res)
