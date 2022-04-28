"""
RSS-reader main testing
"""


import ddt
from print_wrapper import print_wrapper
import rss_reader
import unittest
from unittest import mock


@ddt.ddt
class TestRssCustom(unittest.TestCase):
    """Test class (main)"""

    @ddt.data(
        ({'key': 'value'}, False, ['some source'], False, False, False, False, False),
        ({'key': 'value'}, 20220428, 'None', False, False, False, False, True),
        ({'key': 'value'}, False, 'None', False, True, False, True, False),
        ({'key': 'value'}, False, ['some source'], True, True, True, True, True),
        ({'key': 'value'}, False, ['some source'], False, True, False, True, True),
        ({'key': 'value'}, False, ['some source'], True, False, False, False, False),
        ({'key': 'value'}, 20220428, ['some source'], False, True, True, True, False),
        ({'key': 'value'}, 20220428, ['some source'], True, False, False, False, False),
    )
    @ddt.unpack
    def test_main(self, raw_dict, date, source, limit, verb, json, pdf, html):
        """Full-synthetic. Data: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}"""

        rss_reader.read_news = mock.Mock(return_value=raw_dict)
        rss_reader.news_dict_manager = mock.Mock()
        rss_reader.get_news_dict = mock.Mock(return_value=raw_dict)
        rss_reader.write_news = mock.Mock()

        with mock.patch('rss_reader.get_args') as mock_method:
            mock_method.source = source
            mock_method.date = date
            mock_method.limit = limit
            mock_method.verbose = verb
            mock_method.json = json
            mock_method.to_pdf = pdf
            mock_method.to_html = html

            rss_reader.get_args = mock.Mock(return_value=mock_method)
            cons_txt_and_func_result = print_wrapper(rss_reader.main)()

            if date:
                rss_reader.read_news.assert_called_with(source, date, limit, verb)
                rss_reader.news_dict_manager.assert_called_with(raw_dict, json, verb, html, pdf)

            else:
                if source == 'None':
                    check_str = cons_txt_and_func_result[0]
                    control_str = '\033[95merror: the following arguments are required:' \
                                  ' \033[31msource\033[0m\n'
                    self.assertEqual(check_str, control_str)
                else:
                    rss_reader.get_news_dict.assert_called_with(source[0], limit, verb)
                    rss_reader.write_news.assert_called_with(raw_dict, verb)
                    rss_reader.news_dict_manager.assert_called_with(raw_dict, json, verb, html, pdf)
