#!/usr/bin/env python3

import json
import os
import platform
import random


def getlink(file):
    if os.name == 'nt':
        if os.path.islink(file):
            path = os.path.dirname(os.readlink(file))
        else:
            path = os.path.dirname(file)
    else:
        if os.path.islink(file):
            path = os.path.dirname(os.readlink(file))
        else:
            path = os.path.dirname(file)
    return os.path.dirname(path)


def quote():
    abspath = getlink(__file__)
    if abspath == '/usr/local':
        data_dir = os.path.join(abspath, 'share', 'motivate', 'data')
    else:
        data_dir = os.path.join(abspath, 'motivate', 'data')
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
            quote = quotes["data"][ran_no]["quote"]
            author = quotes["data"][ran_no]["author"]
            if platform.system() == "Windows":
                quote = "\"" + quote + "\""
                author = "--" + author
                white_code = ""
            else:
                quote = "\033[1;36m" + "\"" + quote + "\"" + "\033[1;m"
                author = "\033[1;35m" + "--" + author + "\033[1;m"
                white_code = "\x1b[0m"
            output = quote + "\n\t\t" + author
            print(output + white_code)
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
    quote()
