import json

def getOptions():
    with open("options.json", "r") as f:
        return json.load(f)
    
def setOptions(options):
    with open("options.json", "w") as f:
        json.dump(options, f, indent=4)