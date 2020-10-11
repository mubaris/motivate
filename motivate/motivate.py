#!/usr/bin/env python3

import argparse
import json
import os
import random
from quotes_byAuthor import quotes_byAuthor
from rich.console import Console
from rich.panel import Panel

def getlink(file):
    if os.path.islink(file):
        path = os.path.dirname(os.readlink(file))
    else:
        path = os.path.dirname(file)

    return os.path.dirname(path)


def quote():
    abspath = getlink(__file__)

    if os.name == 'nt':
        data_dir = os.path.join(abspath, 'motivate', 'data')
    else:
        data_dir = os.path.join('/opt', 'motivate', 'data')

    try:
        num_of_json = len([f for f in os.listdir(data_dir)
                           if os.path.isfile(os.path.join(data_dir, f))])
    except FileNotFoundError:
        print("Can't find the data folder. You probably haven't run 'install.sh' yet.")
        exit(1)

    rand_no = random.randint(1, num_of_json)
    filename = os.path.join(data_dir, str(rand_no).zfill(3) + '.json')
    with open(filename) as json_data:
        try:
            quotes = json.load(json_data)
        except ValueError:
            print ("---------------Debug info begins:--------------")
            print("Oops, we met a ValueError.")
            print("Please check this file "+filename)
            print("1. A Possible reason is that there is a redundant comma behind last group of author/quote in this json file.")
            print("   If so, delete that redundant comma, then it will run smoothly.")
            print("2. Another possible reason is that there is hard line-break or tab in that file.")
            print("   However JSON don't support that. Please use '\\n' or '\\t'.")
            print("For later actions, I help you wrote this filename to JSON_ERROR_LIST.txt.")
            print("I suggest you to test those json file in this website: jsonlint.com")
            f_tmp = open('JSON_ERROR_LIST.txt', "a")
            f_tmp.write(filename+"\n")
            f_tmp.close()
            print ("---------------Debug info ends:--------------")
            return

        ran_no = random.randint(1, len(quotes["data"])) - 1
        if "quote" in quotes["data"][ran_no]:
            author = quotes["data"][ran_no]["author"]
            quote = quotes["data"][ran_no]["quote"]
            if os.name == "nt" or args.nocolor:
                quote = "\"" + quote + "\""
                author = "--" + author
            else:
                quote = f"[b]{quote}[/b]"
                author = f'[yellow]--{author}'
                #white_code = "\x1b[0m"
            output = f"{quote}\n{author}"
            console = Console()
            console.print(Panel(output, expand=False ))
        else:
            print ("---------------Debug info begins:--------------")
            print("This is a message indicating an error in your json database:")
            print("No key 'quote' is found in the file: "+filename+", item_index = "+str(ran_no))
            print("Possibly this json file uses capitalized inital letter in its key.")
            print("You might need to change substitute 'Quote' to 'quote', and 'Author' to 'author'.")
            print("Try to print this problematic item:\n"+str(quotes["data"][ran_no]))
            print ("---------------Debug info ends:--------------")
            cmd_tmp = 'sed -i "s/\"Author\"/\"author\"/g; s/\"Quote\"/\"quote\"/g" '+filename
            print("Try to fix the problem by using command:")
            print(cmd_tmp)
            os.system(cmd_tmp)
            print("Let's check the output:")
            f_tmp = open(filename)
            quotes = json.load(f_tmp)
            print(str(quotes["data"][ran_no]))
            print("Hopfully this problem has been solved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple script to print random motivational quotes.')
    parser.add_argument('--no-colors', dest='nocolor', default=False, action='store_true', help='Argument to disable colored output. Disabled by default.')
    parser.add_argument('-a' , '--author' , type=str, help="Random quote by auther" )
    args = parser.parse_args()

    if args.author:
        quotes_byAuthor(args)
    else:
        quote()
