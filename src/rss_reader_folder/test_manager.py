"""
RSS-reader manager testing
"""


import ddt
import rss_reader
import unittest
from unittest import mock


@ddt.ddt
class TestRssCustom(unittest.TestCase):
    """Test class (manager)"""

    @ddt.data(
        ({'key': 'value'}, True, True, True),
        ({'key': 'value'}, False, True, True),
        ({'key': 'value'}, False, False, True),
        ({'key': 'value'}, False, False, False),
        ({'key': 'value'}, True, False, False),
        ({'key': 'value'}, True, True, False)
    )
    @ddt.unpack
    def test_news_dict_manager(self, raw_dict, json, html, pdf):
        """Full-synthetic test aimed at verifying the manager call. Data: {0}, {1}, {2}, {3}, {4}"""

        rss_reader.print_json_news = mock.Mock()
        rss_reader.convert_to_html = mock.Mock()
        rss_reader.convert_to_pdf = mock.Mock()
        rss_reader.write_news = mock.Mock()
        rss_reader.print_news = mock.Mock()

        rss_reader.news_dict_manager(raw_dict, json, html, pdf)

        if json:
            rss_reader.print_json_news.assert_called_with(raw_dict)
        if html:
            rss_reader.convert_to_html.assert_called_with(raw_dict)
        if pdf:
            rss_reader.convert_to_pdf.assert_called_with(raw_dict)
        if not pdf and not html and not json:
            rss_reader.print_news.assert_called_with(raw_dict)
