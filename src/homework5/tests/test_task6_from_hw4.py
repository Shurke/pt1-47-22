"""Test module for task9_from_hw4 (kitchen) tests"""
import unittest
import ddt
from src.homework5 import task9_from_hw4


@ddt.ddt
class TestKitchen(unittest.TestCase):
    """Test case for kitchen"""

    def setUp(self) -> None:
        self.cook = task9_from_hw4.kitchen

    @ddt.data(

    )
    @ddt.unpack
    def test_cooking(self):
        """Test case for kitchen """
