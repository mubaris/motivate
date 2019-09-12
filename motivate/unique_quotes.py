#!/usr/bin/env python3

import json
import os
import string
import unicodedata
import sys

scriptpath = os.path.dirname(__file__)
data_dir = os.path.join(scriptpath, 'data')
quote_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
quotes = []
for f in quote_files:
    with open(f, 'r') as quote_file:
        quotes += json.load(quote_file)['data']

unique_quotes = []
seen_quotes = set()
remove_punct_map = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))
for x in quotes: 
    q = x['quote'].lower() 
    quote = q.translate(remove_punct_map) #avoid repeats from different syntax, punctuation, cases
    if quote not in seen_quotes:
        unique_quotes.append(x)
        seen_quotes.add(quote)	

with open('data_unique/unique_quotes.json', 'w') as unique_quotes_file:
    json.dump({'data': list(unique_quotes)}, unique_quotes_file, indent=4, ensure_ascii=False)
    unique_quotes_file.write('\n')