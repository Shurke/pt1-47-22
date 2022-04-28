"""
RSS-reader output testing
"""


import ddt
from print_wrapper import print_wrapper
import rss_reader
import unittest


@ddt.ddt
class TestRssCustom(unittest.TestCase):
    """Test class (output)"""

# output test
    @ddt.data(
        ('message', ),
        ('404', )
    )
    @ddt.unpack
    def test_print_verb(self, message):
        """Test output with print_verb() from rss_reader.py, message: {0}"""
        console_text = print_wrapper(rss_reader.print_verb)(message)[0]
        self.assertEqual(console_text, f'\x1b[31m{message}\n')

    @ddt.data(
        ({'line_1': 'data_1', 'line_2': {'line_2_1': 'data_2_1', 'line_2_2': 'data_2_2'}}, False),
        ({'line_1': 'data_1', 'line_2': {'line_2_1': 'data_2_1', 'line_2_2': 'data_2_2'}}, True)
    )
    @ddt.unpack
    def test_print_json_news(self, inp_dict, verb):
        """Test output with print_json_news() from rss_reader.py, dict: {0}, verb: {1}"""
        console_text = print_wrapper(rss_reader.print_json_news)(inp_dict, verb)[0]
        console_line_list = console_text.split('\n')
        self.assertEqual(console_line_list[0], '{')
        self.assertEqual(console_line_list[2], '    "line_2": {')
        if verb:
            self.assertEqual(console_line_list[-2], '\x1b[31mJSON sent!')

    @ddt.data(
        (True, ),
        (False, )
    )
    @ddt.unpack
    def test_print_news(self, verb):
        """Test output with print_news() from rss_reader.py"""
        input_dict = {
            'Feed': 'feed',
            'line_1': {
                'name_1': 'text_1',
                'name_2': 'text_2'
            }
        }
        console_text = print_wrapper(rss_reader.print_news)(input_dict, verb)[0]
        if verb:
            file_name = 'test_data/test_print_news_verb.txt'
        else:
            file_name = 'test_data/test_print_news.txt'
        with open(file_name, 'r', encoding='utf-8') as opened_file:
            control_str = opened_file.read()
        self.assertEqual(console_text, control_str)
