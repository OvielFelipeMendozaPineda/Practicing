import os
import json

def fromJson(filename):
    inputFolder = f"{os.path.dirname(os.path.abspath(__file__))}/Json/{filename}"
    if not os.path.exists(inputFolder):
        os.makedirs(inputFolder)
    jsonPath = os.path.join(inputFolder, f"{filename}.json" )
    if not os.path.exists(jsonPath):
        with open(jsonPath, "w+") as newfile:
            json.dump({}, newfile)
    with open(jsonPath, "r") as file:
        filename = json.load(file)
    return filename
def toJSON(data, filename):
    outputFolder = f"{os.path.dirname(os.path.abspath(__file__))}/Json/{filename}"
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    jsonPath = os.path.join(outputFolder, f"{filename}.json" )
    with open(jsonPath, "w+", encoding="utf-8") as file:
        json.dump(data, file, indent=4)