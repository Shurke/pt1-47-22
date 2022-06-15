"""Test module for task_1 tests."""


import unittest
import ddt
from homework5 import task_1


@ddt.ddt
class TestKgToPounds(unittest.TestCase):
    """Test cases for KgToPounds."""

    def setUp(self) -> None:
        self.transducer = task_1.KgToPounds

    @ddt.data(
        (100, 220.5),
        (5, 11.025),
        ("six", "Wrong value")
    )
    @ddt.unpack
    def test_to_pounds(self, number, expected_result):
        """Test cases for to_pounds method with next date {0} --> {1} ."""
        result = self.transducer(number).to_pounds()
        self.assertEqual(result, expected_result)

    @ddt.data(
        (5, 5),
        (15, 15)
    )
    @ddt.unpack
    def test_kg(self, value, expected_result):
        """Test cases for kg method with next date {0} = {1}"""
        result = self.transducer(value).kg
        self.assertEqual(result, expected_result)
