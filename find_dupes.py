#!/usr/bin/env python3

import json
import os

scriptpath = os.path.dirname(__file__)
data_dir = os.path.join(scriptpath, 'data')
all_json = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
quotes = []
for f in all_json:
    filename = os.path.join(data_dir, f)
    with open(filename) as json_data:
        quotes += json.load(json_data)['data']

uniq_authors = {quote['author'] for quote in quotes}
uniq_quotes = {quote['quote'] for quote in quotes}

print('Unique quotes: {}, authors: {}'.format(len(uniq_quotes), len(uniq_authors)))

seen = set()
dupes = sorted([x for x in quotes if x['quote'] in seen or seen.add(x['quote'])], key=lambda x: x['quote'])

print(*dupes, sep='\n')
