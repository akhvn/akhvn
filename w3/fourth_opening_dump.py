import json
with open("1.json", "r") as file:
    data = json.load(file)
    data_initial = data.copy()
    print(json.dumps(data, indent=4, sort_keys=True))
    to_add = {"week": 3}
    t = data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]
    t["week"] = 3
with open("1.json", "w") as file:
    json.dump(data, file, indent=4)
with open("1.json", "r") as file:
    data1 = json.load(file)
    print(json.dumps(data1, indent=4, sort_keys=True))    
