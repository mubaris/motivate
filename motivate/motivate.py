#!/usr/bin/env python3

import json
import os
import random
import argparse


def getlink(file):
    if os.path.islink(file):
        path = os.path.dirname(os.readlink(file))
    else:
        path = os.path.dirname(file)

    return os.path.dirname(path)


def get_filePath():
    abspath = getlink(__file__)
    file_path = os.path.dirname(os.path.realpath(__file__))
    if os.name == 'nt':
        data_dir = os.path.join(abspath, 'motivate', 'data')
    else:
        data_dir = os.path.join(file_path, 'data')

    try:
        num_of_json = len([f for f in os.listdir(data_dir)
                           if os.path.isfile(os.path.join(data_dir, f))])
        return num_of_json, data_dir
    except FileNotFoundError:
        print("Can't find the data folder. You probably haven't run 'install.sh' yet.")
        exit(1)


def get_file_contents(filename):
    with open(filename) as json_data:
        try:
            quotes = json.load(json_data)
        except ValueError:
            error_msgs(filename)

        ran_no = random.randint(16, len(quotes["data"])) - 1
        if "quote" in quotes["data"][ran_no]:
            quote = quotes["data"][ran_no]["quote"]
            author = quotes["data"][ran_no]["author"]
            if os.name == "nt" or args.nocolor:
                quote = "\"" + quote + "\""
                author = "--" + author
                white_code = ""
            else:
                quote = "\033[1;36m" + "\"" + quote + "\"" + "\033[1;m"
                author = "\033[1;35m" + "--" + author + "\033[1;m"
                white_code = "\x1b[0m"
            output = quote + "\n\t\t" + author
            return output + white_code
        else:
            kwargs = {
                'filename': filename,
                'quotes': quotes["data"][ran_no],
                'ran_no': ran_no
            }
            error_msgs(**kwargs)


def error_msgs(*args, **kwargs):
    if kwargs is None:
        print("---------------Debug info begins:--------------")
        print("Oops, we met a ValueError.")
        print("Please check this file " + args)
        print(
            "1. A Possible reason is that there is a redundant comma behind last group of author/quote in this json file.")
        print("   If so, delete that redundant comma, then it will run smoothly.")
        print("2. Another possible reason is that there is hard line-break or tab in that file.")
        print("   However JSON don't support that. Please use '\\n' or '\\t'.")
        print("For later actions, I help you wrote this filename to JSON_ERROR_LIST.txt.")
        print("I suggest you to test those json file in this website: jsonlint.com")
        f_tmp = open('JSON_ERROR_LIST.txt', "a")
        f_tmp.write(args + "\n")
        f_tmp.close()
        print("---------------Debug info ends:--------------")
        return
    else:
        print("---------------Debug info begins:--------------")
        print("This is a message indicating an error in your json database:")
        print("No key 'quote' is found in the file: " + kwargs.get('filename') + ", item_index = " + str(
            kwargs.get('ran_no')))
        print("Possibly this json file uses capitalized inital letter in its key.")
        print("You might need to change substitute 'Quote' to 'quote', and 'Author' to 'author'.")
        print("Try to print this problematic item:\n" + str(kwargs.get('quotes')))
        print("---------------Debug info ends:--------------")
        cmd_tmp = 'sed -i "s/\"Author\"/\"author\"/g; s/\"Quote\"/\"quote\"/g" ' + kwargs.get('filename')
        print("Try to fix the problem by using command:")
        print(cmd_tmp)
        os.system(cmd_tmp)
        print("Let's check the output:")
        f_tmp = open(kwargs.get('filename'))
        quotes = json.load(f_tmp)
        print(str(quotes["data"][kwargs.get('ran_no')]))
        print("Hopfully this problem has been solved.")


def quote():
    num_of_json, data_dir = get_filePath()  # Get no of json files and directory path
    rand_no = random.randint(1, num_of_json)
    filename = os.path.join(data_dir, str(rand_no).zfill(3) + '.json')
    output = get_file_contents(filename)
    print(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple script to print random motivational quotes.')
    parser.add_argument('--no-colors', dest='nocolor', default=False, action='store_true',
                        help='Argument to disable colored output. Disabled by default.')
    args = parser.parse_args()

    quote()
