"""Test module for task1 (KgToPounds) tests"""
import ddt
from src.homework5 import task1
import unittest


@ddt.ddt
class TestKgToPounds(unittest.TestCase):
    """TestCase for KgToPounds"""

    def setUp(self) -> None:
        self.kg_to_pounds = task1.KgToPounds

    @ddt.data(
        (10, 22.05),
        (100, 220.5),
        (1000, 2205),
        ('1', 'Wrong data')
    )
    @ddt.unpack
    def test_to_pounds(self, kg, expected_res):
        """Test case for to_pounds method with kg={0} and result={1}"""
        result_to_pounds = self.kg_to_pounds(kg).to_pounds()
        self.assertEqual(result_to_pounds, expected_res)

    @ddt.data(
        (76, 76),
        (4, 4)
    )
    @ddt.unpack
    def test_write_kg(self, value, expected_kg):
        """Test case for kg method with kg={0} and expected_kg {1}"""
        result_kg = self.kg_to_pounds(value).kg
        self.assertEqual(result_kg, expected_kg)
