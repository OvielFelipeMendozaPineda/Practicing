import os
import json

def fromJson(filename):
    inputFolder = f"J:/Visual Studio Code/Python/notasUniversidad/notsUniversidad/Json/{filename}"
    jsonPath = os.path.join(inputFolder, f"{filename}.json" )
    with open(jsonPath, "r") as file:
        filename = json.load(file)
    return filename
def toJSON(data, filename):
    outputFolder = f"J:/Visual Studio Code/Python/notasUniversidad/notsUniversidad/Json/{filename}"
    dictName = filename
    if not os.path.exists(outputFolder):
        os.mkdir(outputFolder)
    jsonPath = os.path.join(outputFolder, f"{dictName}.json" )
    with open(jsonPath, "w+") as file:
        json.dump(data, file, indent=4)