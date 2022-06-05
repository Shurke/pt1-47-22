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
        ('cup', 6, '6 cup', True),
        ('cup', 6, '0 cup, 3 tablespoons, 3 teaspoons', False),
        ('tablespoons', 50, '3 cup, 2 tablespoon', True),
        ('teaspoons', 159, '3 cup, 5 tablespoons, 0 teaspoons', True)
    )
    @ddt.unpack
    def test_cooking(self, cook_tools, quant, min_actions, expect):
        """Test case for kitchen with cooking tools {0}, quantity {1} and min numb items {2}"""
        result = self.cook(quant, cook_tools) == min_actions
        self.assertEqual(result, expect)
