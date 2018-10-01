# Utilitary to parse a txt file to the json format to make contributions easier
# The file must be in the following format
#			"quote1",Author
#	    "quote2",Other Author
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
			divided_string = line.strip("\n").split('\",')
			quote = divided_string[0].strip('\"')
			author = divided_string[1][1:] if divided_string[1][0] == ' ' else divided_string[1]
			quotes.append({
				"author":  author,
				"quote": quote
			})

	final_dictionary = {"data":quotes}

	with open('quotes.json', 'w') as j:
		json.dump(final_dictionary, j)

	print("Sucess! Result file: quotes.json")
