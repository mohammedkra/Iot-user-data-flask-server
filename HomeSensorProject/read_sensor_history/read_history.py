import json
import os

state_json_file = "data_center/state.json"

def checkFile(jsonfile):
    return os.path.exists(jsonfile)

def checkFileIfEmpty(jsonfile):
    return os.path.getsize(jsonfile)

#THIS METHOD READS SENSOR STATUS HISTORY
def readStatusHistory():

    #Check if file exists
    if(not checkFile(state_json_file) or checkFileIfEmpty(state_json_file) == 0):
        return False
    
    with open(state_json_file, 'r') as file:
        object = json.load(file)
        json_object = json.dumps(object['states'])
    return json_object
