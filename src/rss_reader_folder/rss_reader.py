"""
Welcome to a simple console rss-reader. Use the -h flag to start using the application. You can also
package the application using the console's "python setup.py sdist bdist_wheel" and then install it
in your virtual environment with "python setup.py install" - after that you can use the "rss_reader"
entry point anywhere :)
"""


import argparse
from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from colorama import Fore
from colorama import init
import datetime
from decimal import Decimal
import json
import logging
import os
from pathlib import Path
import requests
import xmltodict


__rss_version__ = '0.1'
init(autoreset=True)
logger = logging.getLogger('Verbose_logger')


def get_args() -> argparse.Namespace:
    """That functions parse args from command line.

    Also checks for use of the --version or --help flag.

    :return: console_args - Namespace with args, or print them in console and exit().
    """
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')

    # positional args
    parser.add_argument('source', type=str, help='RSS URL', default='None', nargs='*')

    # optional args
    parser.add_argument('--version', help='Print version info', action='version',
                        version=f'Version {__rss_version__}')
    parser.add_argument('--json', help='Print result as JSON in stdout', action='store_true')
    parser.add_argument('--verbose', help='Outputs verbose status messages', action='store_true')
    parser.add_argument('--to-html', help='Convert news to .html', action='store_true')
    parser.add_argument('--to-pdf', help='Convert news to .pdf', action='store_true')
    parser.add_argument('--date', help='Find cached news on this date', action='store',
                        default=None)
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter provided')

    console_args = parser.parse_args()

    return console_args


def get_news_dict(url: str, limit: int) -> dict:
    """Pars RSS-feed from 'url' with 'limit' of results.

    :param url: RSS-feed source url
    :param limit: limit of news
    :return: dict with news
    """

    resp = requests.get(url)
    resp.encoding = 'utf-8'
    general_news_dict = {}
    if resp.status_code == 200:
        logger.debug('Data received from %s' % url)
        resp_dict = xmltodict.parse(resp.text)

        general_news_dict['Feed'] = resp_dict['rss']['channel']['title']
        general_news_dict['Source'] = url

        recorded_news = 0
        if limit is None:
            limit = 2147483647

        for item in resp_dict['rss']['channel']['item']:  # parse individual news
            if recorded_news < limit:
                news_dict = {}
                news_dict['Title'] = str(item["title"]).encode().decode()
                text_data = item.get("text", None)
                if text_data is not None:
                    news_dict['Text'] = text_data
                    logger.debug('Add text to this publish.')
                else:
                    logger.debug('This publish has no text.')
                news_dict['Link'] = item["link"]
                news_dict['Date'] = item["pubDate"]
                logger.debug('Add title, link and pubDate to publish:\n%s' % news_dict["Title"])
                inline_picture_data = item.get("media:content", None)
                if inline_picture_data is not None:
                    news_dict['Inline picture'] = item["media:content"]["@url"]
                    logger.debug('Add image_link to this publish.')
                else:
                    logger.debug('This publish has no Inline picture.')

                recorded_news += 1

                general_news_dict[f'pub_{recorded_news}'] = news_dict
                logger.debug('Add pub_%s to dict' % recorded_news)

        logger.debug('Dictionary formed.')
    else:
        print(f'{url} did not respond to the request. Check url or try later.')
    return general_news_dict


def print_json_news(news_dict: dict):
    """Print json-object from news_dict"""
    print(json.dumps(news_dict, indent=4))
    logger.debug('JSON sent!')


def print_news(news_dict: dict):
    """Print news from news_dict"""
    print(f'\n{Fore.GREEN}Feed: {Fore.YELLOW + news_dict["Feed"]}\n')

    for pub, pub_info in news_dict.items():
        if pub not in ('Feed', 'Source'):
            for name, content in pub_info.items():
                print(f'{Fore.GREEN + name}: {Fore.BLUE + content}')
            print()

    logger.debug('All news sent!')


def write_news(news_dict: dict):
    """Passive function that caches news after it has been parsed.

    :param news_dict: use get_news_dict to get a news_dict
    """
    check_and_make_dir('cached news')
    source = news_dict['Source'].split('://')[1].split('/')[0]
    check_and_make_dir(f'cached news/{source}')

    for pub, pub_info in news_dict.items():
        if pub not in ('Feed', 'Source'):
            news_file_name = f'{pub_info["Title"][0:9].replace(":", "")}...' \
                             f' {pub_info["Date"].replace(":", "").replace("-", "")}.txt'
            if news_file_name not in os.listdir(f'cached news/{source}'):
                file_name_to_open = f'cached news/{source}/{news_file_name}'
                with open(file_name_to_open, 'w', encoding='utf-8', errors='ignore') as opened_file:
                    opened_file.write(json.dumps(pub_info, indent=4))
                logger.debug('News %s successfully recorded!' % news_file_name)
            logger.debug('News %s is already recorded!' % news_file_name)


def read_news_from_cache(source: list or str, date: str, limit: int or bool) -> dict:
    """That function emulates the work of the get_news_dict function, getting data from the cache.

    :param source: if 'None' - use all sources in cached data
    :param date: in format YYYYMMDD
    :param limit: if you don't need ALL news from this date
    :return: dict with news
    """
    if limit is None:
        limit = 2147483647
    source_list = []
    if source == 'None':
        for item in os.listdir('cached news'):
            source_list.append(item)
    else:
        input_source = source[0].split('://')[1].split('/')[0]
        if input_source in os.listdir('cached news'):
            source_list.append(input_source)

    cached_news_dict = {}
    read_news_count = 0
    cached_news_dict['Feed'] = f'cached news for {date}'

    for loc_source in source_list:
        if read_news_count < limit:

            for news_name in os.listdir(f'cached news/{loc_source}'):
                if read_news_count < limit:
                    if news_name[13:21] == date:
                        read_news_count += 1
                        file_name_to_open = f'cached news/{loc_source}/{news_name}'
                        with open(file_name_to_open, 'r', encoding='utf-8') as opened_file:
                            news_json = json.load(opened_file)
                            cached_news_dict[f'pub_{read_news_count}'] = news_json

    logger.debug('Printed cached news for %s' % date)

    return cached_news_dict


def convert_to_html(news_dict: dict):
    """Converts and writes news html-file"""
    # This function is not recommended for reading by persons with an unstable psyche.
    string_to_write = '<!DOCTYPE html>\n' \
                      '<html lang="en">\n' \
                      '<head>\n' \
                      '  <meta charset="UTF-8">\n' \
                      '  <meta http-equiv="X-UA-Compatible" content="IE=edge">\n' \
                      '  <meta name="viewport" content="width=device-width,' \
                      ' initial-scale=1.0">\n' \
                      '  <title>HTML-conversion</title>\n' \
                      '</head>\n' \
                      '\n' \
                      '<body>\n'
    list_to_write = [string_to_write]
    list_to_write.append(f'Feed: {news_dict["Feed"]}<br><br>')
    for pub, pub_info in news_dict.items():
        if pub not in ('Feed', 'Source'):
            for title, content in pub_info.items():
                list_to_write.append(f'{title}: {content}<br>')
            list_to_write.append('<br>')

    list_to_write.append('</body>\n\n</html>')

    check_and_make_dir('conversions')
    check_and_make_dir('conversions/html')

    row_html_file_name = str(datetime.datetime.now()).replace("-", "")
    html_file_name = row_html_file_name.replace(" ", "T").replace(":", "")[0:15]
    file_name_to_open = f'conversions/html/{html_file_name}.html'
    with open(file_name_to_open, 'w', encoding='utf-8') as opened_file:
        opened_file.write(''.join(list_to_write))

    logger.debug('HTML-file was successfully written')


def convert_to_pdf(news_dict: dict):
    """Converts and writes news pdf-file"""
    # This function is not recommended for reading by persons with an unstable psyche.
    heading_color = HexColor("0b3954")
    text_color = HexColor("070071")
    doc = Document()
    page = Page()
    doc.append_page(page)

    layout = SingleColumnLayout(page)
    font_path: Path = Path(__file__).parent / "timesnewromanpsmt.ttf"
    custom_font = TrueTypeFont.true_type_font_from_file(font_path)
    layout.add(Paragraph(f"Feed {news_dict['Feed']}", font=custom_font, font_color=heading_color,
                         font_size=Decimal(24)))

    for pub, pub_info in news_dict.items():
        if pub not in ('Feed', 'Source'):
            layout_write_list = []
            for title, content in pub_info.items():
                layout_write_list.append(f'{title}: {content}\n\n')
            layout.add(
                Paragraph(f'{"".join(layout_write_list)}', font=custom_font, font_color=text_color))

    check_and_make_dir('conversions')
    check_and_make_dir('conversions/pdf')

    row_pdf_file_name = str(datetime.datetime.now()).replace("-", "")
    pdf_file_name = row_pdf_file_name.replace(" ", "T").replace(":", "")[0:15]
    file_name_to_open = f'conversions/pdf/{pdf_file_name}.pdf'
    with open(file_name_to_open, 'wb') as opened_file:
        PDF.dumps(opened_file, doc)

    logger.debug('PDF-file was successfully written')


def check_and_make_dir(dir_name):
    """Checks for the existence of the specified directory and, if necessary, creates it."""
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        logger.debug('Added directory "%s"' % dir_name)


def news_dict_manager(news_dict: dict, is_json: bool, is_html: bool, is_pdf: bool):
    """Simple what_to_do manager.

    :param news_dict: use get_news_dict() to get news_dict
    :param is_json: post here True if you want to claim json-object
    :param is_html: post here True if you want to convert into html-file
    :param is_pdf: post here True if you want to convert into html-file
    :return:
    """
    if is_json:
        print_json_news(news_dict)
    if is_html:
        convert_to_html(news_dict)
    if is_pdf:
        convert_to_pdf(news_dict)
    if not is_pdf and not is_html and not is_json:
        write_news(news_dict)
        print_news(news_dict)


def main():
    """main function. Run it if you want to get started."""
    cons_args = get_args()

    if cons_args.verbose:
        logging.basicConfig(level='DEBUG')
        logger.setLevel(logging.DEBUG)

    if cons_args.date:
        news_dict = read_news_from_cache(cons_args.source, cons_args.date, cons_args.limit, )
        news_dict_manager(news_dict, cons_args.json, cons_args.to_html, cons_args.to_pdf)

    else:
        if cons_args.source == 'None':
            print('\033[95merror: the following arguments are required: \033[31msource\033[0m')
        else:
            news_dict = get_news_dict(cons_args.source[0], cons_args.limit)
            write_news(news_dict)
            news_dict_manager(news_dict, cons_args.json, cons_args.to_html, cons_args.to_pdf)


if __name__ == '__main__':
    main()
