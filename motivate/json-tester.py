import os
import json

os.chdir("data")
json_files = os.listdir()

all_json_good = True
for json_file in json_files:
    if os.path.isdir(json_file):
        continue

    try:
        with open(json_file) as json_data:
            quotes = json.load(json_data)

            for index, quote in enumerate(quotes["data"], 1):
                q = quote["quote"]
                a = quote["author"]
    except Exception as e:
        print("Error: ", json_file)
        print(str(e))
        all_json_good = False

if all_json_good:
    print("All JSON files good!")
