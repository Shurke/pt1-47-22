import unittest
from ddt import ddt, data, unpack
from task01 import KgToPounds


@ddt
class KgToPoundsTestCase(unittest.TestCase):

    @data((1, 2.205), (5, 11.025))
    @unpack
    def test_kg_to_pounds(self, kg, expected_result):
        kg_to_pounds = KgToPounds(kg)
        self.assertEqual(kg_to_pounds.kg, kg)
        self.assertEqual(kg_to_pounds.to_pounds(), expected_result)
