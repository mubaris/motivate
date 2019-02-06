import os
import json
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
quotes = []
for filename in os.listdir("./data"):
    filename = os.fsdecode(filename)
    print(filename)
    if filename.endswith(".json"):
        with open("data/" + filename, encoding="utf-8") as file:
            file_data = json.loads(file.read())
            quotes.extend(file_data["data"])
    else:
        continue
file_num = 1
for chunk in chunker(quotes, 20):
    with open("data/%03d.json" % file_num, "w") as file:
        file.write(json.dumps({"data": chunk}, sort_keys=True, indent=4))
    file_num += 1
