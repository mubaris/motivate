#!/usr/bin/env python3

import json
import os

scriptpath = os.path.dirname(__file__)
data_dir = os.path.join(scriptpath, 'data')
quote_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
quotes = []
for f in quote_files:
    with open(f, 'r') as quote_file:
        quotes += json.load(quote_file)['data']

unique_quotes = []
seen_quotes = set()
for x in quotes:
    if x['quote'] not in seen_quotes:
        unique_quotes.append(x)
        seen_quotes.add(x['quote'])		

with open('data_unique/unique_quotes.json', 'w') as unique_quotes_file:
    json.dump({'data': list(unique_quotes)}, unique_quotes_file, indent=4, ensure_ascii=False)
    unique_quotes_file.write('\n')
