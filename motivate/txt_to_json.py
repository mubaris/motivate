# Utilitary to parse a txt file to the json format to make contributions easier
# The file must be in the following format
# 	"quote1",Author
# 	"quote2",Other Author
# Quote and author name should be comma separated
# Author names should not have comma character in them
# To run: python quotes_to_json.py
# if the quotes file is not named quotes.txt them run: python quotes_to_json.py --file="File name"

import json
import argparse
import os
import sys

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--file", help="Name of the quotes file", default="quotes.txt")
	args = parser.parse_args()

	file_name = args.file

	if not os.path.exists(file_name):
		sys.exit("Error: The specified file doesn't exists.")

	quotes = []
	with open(file_name, 'r') as f:
		for line in f:

			line_split = line.strip().rsplit(',', 1)
			assert len(line_split) == 2, f'line is not valid : {line} '

			quotes.append({
				"author":  line_split[1].strip(),
				"quote": line_split[0].strip('"')
			})

	final_dictionary = {"data":quotes}

	with open('quotes.json', 'w') as j:
		json.dump(final_dictionary, j)

	print("Sucess! Result file: quotes.json")
