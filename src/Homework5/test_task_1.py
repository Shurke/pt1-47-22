from ddt import data
from ddt import ddt
from ddt import unpack
from task01 import KgToPounds
import unittest


@ddt
class TestSuiteKgToPounds(unittest.TestCase):
    """Roman kg conversion test suite."""

    @data((1, 2.205), (5, 11.025))
    @unpack
    def test_kg_to_pounds(self, new_kg, expected_result):
        """Test conversion Kg to pounds.

        :param new_kg:            value to conversion
        :param expected_result:   expected num
        """
        default_val = 0
        kg_to_pounds = KgToPounds(default_val)
        self.assertEqual(kg_to_pounds.kg, default_val)
        kg_to_pounds.kg = new_kg
        self.assertEqual(kg_to_pounds.kg, new_kg)
        self.assertEqual(kg_to_pounds.to_pounds(), expected_result)

    @data(('1'), ({}), ([]))
    def test_handling_invalid_values(self, invalid_val):
        """Test handling invalid values in the KgToPounds.

        :param invalid_val:   value for check
        """
        with self.assertRaises(ValueError):
            kg_to_pounds = KgToPounds(invalid_val)

        valid_val = 1
        kg_to_pounds = KgToPounds(valid_val)
        with self.assertRaises(ValueError):
            kg_to_pounds.kg = invalid_val
