#!/usr/bin/env python3

from json import load, dump
from os import listdir
from os.path import dirname, join, isfile


def build_file_list(data_dir):
    return [file for file in listdir(data_dir) if isfile(join(data_dir, file))]

def iterate_add_quotes(data_dir, file_list):
    all_quotes = []
    for single_file in file_list:
        all_quotes += get_quotes(join(data_dir, single_file))
    return unique_authors(all_quotes), unique_quotes(all_quotes), all_quotes  
    
def get_quotes(single_file_path):
    with open(single_file_path, encoding='utf8') as json_data:
        return load(json_data)['data']
    
def unique_authors(quote_list):
    return {quote['author'] for quote in quote_list}
    
def unique_quotes(quote_list):
    return {quote['quote'] for quote in quote_list}
    
def print_uniques(authors, quotes):
    print('Unique quotes: {}, authors: {}'.format(len(quotes), len(authors)))
   
def find_duplicates(all_quotes):
    seen = set()
    return sorted([x for x in all_quotes if x['quote'] in seen or seen.add(x['quote'])], key=lambda x: x['quote'])
    
    
# for each single quote dictionary in the list
# list comprehension to make a list of the tuple of items preserving the pairing while
# use set to remove duplicates
# take these tuples, re-recreate a dictionary
# then build the top level "data": [{'quote': 'author'},....] dictionary
def get_unique_pairs(all_quotes):
    return {"data":[dict(tuple) for tuple in set([tuple(dict_items.items()) for dict_items in all_quotes])]}
 
    
def output_json(processed_quotes):
    with open('data_unique/unique_quotes.json', 'w') as out_file:
        dump(processed_quotes, out_file, indent=4)
   
   
def main(data_directory):
    all_files = build_file_list(data_directory)    
    unique_authors, unique_quotes, all_quotes = iterate_add_quotes(data_directory, all_files)
    
    filtered_quotes = get_unique_pairs(all_quotes)
    print_uniques(unique_authors, unique_quotes)
    
    output_json(filtered_quotes)
   

if __name__ == '__main__':
    scriptpath = dirname(__file__)
    data_dir = join(scriptpath, 'data')
    
    main(data_dir)