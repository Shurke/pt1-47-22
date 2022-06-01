"""Test module for task5 (DefaultList) tests"""
import unittest
import ddt
import task5


@ddt.ddt
class TestDefaultList(unittest.TestCase):
    """Test case for DefaultList"""

    def setUp(self) -> None:
        self.def_lst = task5.DefaultList

    @ddt.data(

    )
    @ddt.unpack
    def test_index(self, user_lst, ):
