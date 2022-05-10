"""
RSS-reader disk write testing
"""


import ddt
import os
from print_wrapper import print_wrapper
import rss_reader
import unittest
from unittest import mock


@ddt.ddt
class TestRssCustom(unittest.TestCase):
    """Test class (disk_write)"""

# disk write test
    def test_write_news(self):
        """Test write to disk with write_news() from rss_reader.py"""

        raw_dict = {
            'Source': 'http://test_write_news/',
            'line_1': {
                'Title': 'test_write_news',
                'Date': '20222704'
            }
        }
        print_wrapper(rss_reader.write_news)(raw_dict)
        with open('cached news/test_write_news/test_writ... 20222704.txt', 'r',
                  encoding='utf-8') as opened_file:
            checked_str = opened_file.read()
        os.remove('cached news/test_write_news/test_writ... 20222704.txt')
        os.rmdir('cached news/test_write_news')
        with open('test_data/test_write_news.txt', 'r', encoding='utf-8') as opened_file:
            control_str = opened_file.read()
        self.assertEqual(checked_str, control_str)

    def test_convert_to_html(self):
        """Test write to disk with convert_to_html() from rss_reader.py"""
        def html_convert_data(*args, **kwargs):
            return 'test_convert_to_html'
        raw_dict = {
            'Feed': 'html_test',
            'Source': 'http://test_write_news/',
            'line_1': {
                'Title': 'test_write_news',
                'Date': '20222704'
            }
        }
        with mock.patch('datetime.datetime') as mock_method:
            mock_method.return_value = mock.Mock()
            mock.Mock.now = html_convert_data
            rss_reader.convert_to_html(raw_dict)
        with open('conversions/html/test_convert_to.html', 'r',
                  encoding='utf-8') as opened_file:
            check_str = opened_file.read()
        with open('test_data/test_convert_to.html', 'r',
                  encoding='utf-8') as opened_file:
            control_str = opened_file.read()
        os.remove('conversions/html/test_convert_to.html')
        self.assertEqual(check_str, control_str)

    def test_convert_to_pdf(self):
        """Test write to disk with convert_to_pdf() from rss_reader.py"""
        raw_dict = {
            'Feed': 'html_test',
            'Source': 'http://test_write_news/',
            'line_1': {
                'Title': 'test_write_news',
                'Date': '20222704'
            }
        }
        listdir_old = set(os.listdir('conversions/pdf'))
        rss_reader.convert_to_pdf(raw_dict)
        listdir_new = set(os.listdir('conversions/pdf'))
        new_items = listdir_new - listdir_old
        self.assertEqual(len(new_items), 1)
        os.remove(f'conversions/pdf/{new_items.pop()}')
