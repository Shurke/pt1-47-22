import requests
import xmltodict


__rs_version__ = '0.1'


def get_args():
    """


    :return: start arguments
    """

    import argparse

    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')

    # positional args
    parser.add_argument('source', type=str, help='RSS URL')

    # optional args
    parser.add_argument('--version', help='Print version info', action='version',
                        version=f'Version {__rs_version__}')
    parser.add_argument('--json', help='Print result as JSON in stdout', action='store_true')
    parser.add_argument('--verbose', help='Outputs verbose status messages', action='store_true')
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


def main():
    cons_args = get_args()

    news_dict = get_news_dict(cons_args.source, cons_args.limit, cons_args.verbose)

    if cons_args.json:
        import json
        print(json.dumps(news_dict, indent=4))
        if cons_args.verbose:
            print('JSON sent.')
    else:
        print(f'\nFeed: {news_dict["Feed"]}\n')

        del news_dict['Feed']

        for pub, pub_info in news_dict.items():
            for name, content in pub_info.items():
                print(f'{name}: {content}')
            print()


if __name__ == '__main__':
    main()
