import argparse
import xmltodict
import requests
import json
import os


__rss_version__ = '0.1'


def get_args():
    """


    :return: start arguments
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
    try:
        if console_args.version or console_args.h:
            print(console_args)
    except AttributeError:
        return console_args


def get_news_dict(url: str, limit: int, verbose: bool):

    resp = requests.get(url)
    resp.encoding = 'utf-8'
    if str(resp) == '<Response [200]>':
        if verbose:
            print(f'Data received from {url}')
        resp_dict = xmltodict.parse(resp.text)

        general_news_dict = dict()
        general_news_dict['Feed'] = resp_dict['rss']['channel']['title']
        general_news_dict['Source'] = url

        recorded_news = 0
        if limit is None:
            limit = 2147483647

        for item in resp_dict['rss']['channel']['item']:  # parse individual news
            if recorded_news < limit:
                news_dict = dict()
                news_dict['Title'] = item["title"]
                news_dict['Link'] = item["link"]
                news_dict['Date'] = item["pubDate"]
                if verbose:
                    print(f'Add title, link and pubDate to publish:\n{news_dict["title"]}')
                try:
                    news_dict['Inline picture'] = item["media:content"]["@url"]
                    if verbose:
                        print('Add image_link to this publish.')
                except KeyError:
                    if verbose:
                        print('This publish has no Inline picture.')

                recorded_news += 1

                general_news_dict[f'pub_{recorded_news}'] = news_dict
                if verbose:
                    print(f'Add pub_{recorded_news} to dict')

        if verbose:
            print('Dictionary formed.')

        return general_news_dict

    else:
        print(f'{url} did not respond to the request. Check url or try later.')
        exit('No response')


def print_json_news(news_dict, is_verb):
    print(json.dumps(news_dict, indent=4))
    if is_verb:
        print('JSON sent!')


def print_news(news_dict, is_verb):
    print(f'\nFeed: {news_dict["Feed"]}\n')

    for pub, pub_info in news_dict.items():
        if pub not in ('Feed', 'Source'):
            for name, content in pub_info.items():
                print(f'{name}: {content}')
            print()

    if is_verb:
        print('All news sent!')


def write_news(news_dict, is_verb):
    if not os.path.exists('cached news'):
        os.mkdir('cached news')
        if is_verb:
            print('Added directory "cached news"')
    source_list = os.listdir('cached news')
    source = news_dict['Source'].split('://')[1].split('/')[0]
    if source not in source_list:
        os.mkdir(f'cached news/{source}')
        if is_verb:
            print(f'Added directory "cached news/{source}"')

    for pub, pub_info in news_dict.items():
        if pub not in ('Feed', 'Source'):
            news_file_name = f'{pub_info["Title"][0:9]}...' \
                             f' {pub_info["Date"].replace(":", "").replace("-", "")}.txt'
            if news_file_name not in os.listdir(f'cached news/{source}'):
                with open(f'cached news/{source}/{news_file_name}', 'w') as opened_file:
                    opened_file.write(json.dumps(pub_info, indent=4))
                if is_verb:
                    print(f'News {news_file_name} successfully recorded!')
            elif is_verb:
                print(f'News {news_file_name} is already recorded!')


def read_news(source: str, date: str, limit: int or bool, is_verb: bool, is_json):
    if limit is None:
        limit = 2147483647
    source_list = []
    if source == 'None':
        for item in os.listdir('cached news'):
            source_list.append(item)
    else:
        source_list.append(source)

    news_dict_from_source = {}

    read_news_count = 0

    for source in source_list:
        if read_news_count < limit:
            news_dict_from_source['Feed'] = f'cached news from {source} on {date}'
            for news_name in os.listdir(f'cached news/{source}'):
                if read_news_count < limit:
                    if news_name[13:21] == date:
                        read_news_count += 1
                        with open(f'cached news/{source}/{news_name}') as opened_file:
                            news_json = json.load(opened_file)
                            news_dict_from_source[f'pub_{read_news_count}'] = news_json

        news_dict_manager(news_dict_from_source, is_json, is_verb)
        if is_verb:
            print(f'Print cached news from {source}')


def news_dict_manager(news_dict: dict, is_json: bool, is_verb: bool):
    if is_json:
        print_json_news(news_dict, is_verb)
    else:
        print_news(news_dict, is_verb)


def main():
    cons_args = get_args()

    if cons_args.date:
        read_news(cons_args.source, cons_args.date, cons_args.limit,
                  cons_args.verbose, cons_args.json)

    else:
        if cons_args.source == 'None':
            print('error: the following arguments are required: source')
        else:
            news_dict = get_news_dict(cons_args.source[0], cons_args.limit, cons_args.verbose)
            write_news(news_dict, cons_args.verbose)
            news_dict_manager(news_dict, cons_args.json, cons_args.verbose)

    exit()


if __name__ == '__main__':
    main()
