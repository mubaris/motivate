import json
import os
import random
from rich.console import Console
from rich.panel import Panel

scriptpath = os.path.dirname(__file__)
data_dir = os.path.join(scriptpath, 'data_unique')
filename = os.path.join(data_dir, 'unique_quotes.json')
newFile = os.path.join(data_dir, 'quotes_byAuthor.json')

"""
Function for generating quotes_byAuthor file 
which combines quotes from same authors in single list
"""
def create_byAuther_file():
    unique_author = set()
    quotes_byAuthor = {}

    with open(file=filename ) as json_data:
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

        for quote in quotes["data"]:
            unique_author.add(quote["author"])
        
        for author in unique_author:
            quote_list = []
            for quote in quotes["data"]:
                if author == quote["author"]:
                    quote_list.append(quote["quote"])

            quotes_byAuthor[author] = {"quotes" : quote_list}
                
        with open(newFile, 'w') as quotes_byAuthor_file:
            json.dump({'data': dict(quotes_byAuthor)}, quotes_byAuthor_file, indent=4, ensure_ascii=False)
            quotes_byAuthor_file.write('\n')

def quotes_byAuthor(args):
    if(os.path.exists(newFile) == False):
        create_byAuther_file()
    try:
        with open(file=newFile ) as json_data:
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
            author = args.author
            ran_no = random.randint(1, len(quotes["data"][author]["quotes"])) - 1
            if "quotes" in quotes["data"][author]:
                quote = quotes["data"][author]["quotes"][ran_no]
                if os.name == "nt" or args.nocolor:
                    quote = "\"" + quote + "\""
                    author = "--" + author
                else:
                    quote = f"[b]{quote}[/b]"
                    author = f'[yellow]--{author}'
                    #white_code = "\x1b[0m"
                output = f"{quote}\n{author}"
                console = Console()
                console.print(Panel(output, expand=False))

    except FileNotFoundError:
        print("Can't find the quotes_byAuthor.json file")
        exit(1)
