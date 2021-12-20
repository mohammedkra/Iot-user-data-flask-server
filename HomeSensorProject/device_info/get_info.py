import json
import os

jsonfile = "data_center/deviceInfo.json"

def checkFile(jsonfile):
    return os.path.exists(jsonfile)

def checkFileIfEmpty(jsonfile):
    return os.path.getsize(jsonfile)

#THIS METHOD RETRIEVES ALL DEVICE INFORMATION
def getInfo():
    #Check if file exists
    if(not checkFile(jsonfile) or checkFileIfEmpty(jsonfile) == 0):
        return False
    
    with open(jsonfile, 'r') as file:
        object = json.load(file)
        json_object = json.dumps(object)
    return json_object
