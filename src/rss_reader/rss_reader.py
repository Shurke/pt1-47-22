def get_args():
    """


    :return: start arguments
    """

    import argparse

    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')

    # positional args
    parser.add_argument('source', type=str, help='RSS URL')

    # optional args
    parser.add_argument('--version', help='Print version info', action='version', version='Version 0.1')
    parser.add_argument('--json', help='Print result as JSON in stdout', action='store_true')
    parser.add_argument('--verbose', help='Outputs verbose status messages', action='store_true')
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter provided')

    args = parser.parse_args()
    try:
        if args.version or args.h:
            print(args)
    except AttributeError:
        return args


def get_news_dict(url: str, limit: int, verbose: bool, is_json: bool):

    import os
    try:
        import requests
    except ImportError:
        if verbose:
            print('Module "requests" not found. It will install automatically.')
        os.system('python -m pip install requests')
        import requests
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    if str(resp) == '<Response [200]>':
        if verbose:
            print(f'Data received from {url}')
        try:
            import xmltodict
        except ImportError:
            if verbose:
                print('Module "xmltodict" not found. It will install automatically.')
            os.system('python -m pip install xmltodict')
            import xmltodict
        resp_dict = xmltodict.parse(resp.text)

        # print(resp_dict)

        general_news_dict = {}
        general_news_dict['Feed'] = resp_dict['rss']['channel']['title']

        recorded_news = 0
        if limit is None:
            limit = 2147483647

        for item in resp_dict['rss']['channel']['item']:  # parse individual news
            if recorded_news < limit:
                news_dict = {}
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


ARGS = get_args()

NEWS_DICT = get_news_dict(ARGS.source, ARGS.limit, ARGS.verbose, ARGS.json)

if ARGS.json:
    import json
    print(json.dumps(NEWS_DICT, indent=4))
    if ARGS.verbose:
        print('JSON sent.')
else:
    print(f'\nFeed: {NEWS_DICT["Feed"]}\n')

    del NEWS_DICT['Feed']

    for pub, pub_info in NEWS_DICT.items():
        for name, content in pub_info.items():
            print(f'{name}: {content}')
        print()
