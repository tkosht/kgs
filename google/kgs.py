import sys
import json
import urllib
import urllib.parse
import urllib.request
import argparse
from jq import jq


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", default=False,
                        help="if you specified, execute as debug mode. default: 'False'")
    parser.add_argument("--trace", action="store_true", default=False,
                        help="if you specified, execute as trace mode. default: 'False'")
    parser.add_argument("keywords", type=str, nargs="*", default=["Taylor", "Swift"],
                        help="you can specify the list of keywords")
    parser.add_argument("-l", "--limit", type=int, default=10,
                        help="you can specify the limit number of results")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()


    pattern='.itemListElement[].result|{"name": .name, "id": .["@id"], "type": .["@type"]}'

    api_key = open('.api_key').read()
    query = "+".join(args.keywords)
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
            'query': query,
            'limit': args.limit,
            'indent': False,
            'key': api_key,
            }
    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())
    res = jq(pattern).transform(response, text_output=True)
    print(res)
