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

unique_quotes = []
seen_quotes = set()
for x in quotes:
    if(x['quote'] not in seen_quotes):
        unique_quotes += [x]
        seen_quotes.add(x['quote'])		
with open('data_unique/unique_quotes.json', 'w') as outfile:
    outfile.write(u'{ \"data\": [')
    for i, _ in enumerate(unique_quotes):
        if(i != 0):
            outfile.write(u',')

        json.dump(unique_quotes[i], outfile, ensure_ascii=False, indent=4)
    outfile.write(u']}')
