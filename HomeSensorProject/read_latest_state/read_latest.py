import json
import os

#THIS METHOD CHECKS IF FIlE EXISTS
def checkFile(jsonfile):
    return os.path.exists(jsonfile)

def checkFileIfEmpty(jsonfile):
    return os.path.getsize(jsonfile)

#THIS METHOD LOADS CURRENT STATE FROM SPECIFIED FILE
def readLatestState(jsonfilename):
    jsonfile = "data_center/"+jsonfilename

    #Check if file exists or empty
    if(not checkFile(jsonfile) or checkFileIfEmpty(jsonfile) == 0):
        return False
    
    with open(jsonfile, 'r') as file:
        object = json.load(file)
        list = object ['states']
    return json.dumps(list[-1])