import json
with open("i.json", "r") as file:
    data = json.load(file)
data ["products"].append ("цукор")

with open ("i.json", "w") as file:
    json.dump(data,file, ensure_ascii=False)
print(data)