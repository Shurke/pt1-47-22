"""
RSS-reader return testing
"""


import argparse
import datetime
import ddt
from print_wrapper import print_wrapper
import rss_reader
import unittest
from unittest import mock


@ddt.ddt
class TestRss(unittest.TestCase):
    """Test class (return)"""

    maxDiff = None

# "return" test
    def test_get_args(self):
        """Test return from get_args() from rss_reader.py"""

        result = rss_reader.get_args()
        self.assertIsInstance(result, argparse.Namespace)

    def test_get_news_dict(self):
        """Test get_news_dict() from rss_reader.py"""
        with open('test_data/test_get_news_dict_with_mock.txt', 'r',
                  encoding='iso-8859-1') as opened_file:
            mock_data = opened_file.read()
        with mock.patch('requests.get') as mock_method:
            mock_method.return_value = mock.Mock()
            mock.Mock.text = mock_data
            mock.Mock.status_code = 200
            cons_txt_and_raw_dict = print_wrapper(rss_reader.get_news_dict)('https://news.yahoo.'
                                                                            'com/rss/', 5)
            raw_dict = cons_txt_and_raw_dict[1]  # [0] - console output, [1] - func result
            with open('test_data/test_get_news_dict.txt', 'r',
                      encoding='iso-8859-1') as opened_file:
                control_str = opened_file.read()
            self.assertEqual(f'{raw_dict}', control_str)

    @ddt.data(
        (['http://news.yahoo.com/rss'], False),
        (['http://news.yahoo.com/rss'], 5)
    )
    @ddt.unpack
    def test_read_news(self, source, limit):
        """Test return from read_news_from_cache() from rss_reader.py, source: {0}, limit: {1}"""
        date = str(datetime.datetime.now().date()).replace("-", "")
        raw_dict = print_wrapper(rss_reader.read_news_from_cache)(source, date, limit)[1]
        self.assertEqual(raw_dict['Feed'], f'cached news for {date}')
        if limit:
            with self.assertRaises(KeyError):
                self.assertFalse(raw_dict[f'pub_{limit + 1}'])
