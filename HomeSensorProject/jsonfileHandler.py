import json
import os
state_json_file = 'state.json'
users_jsonfile = 'users.json'

#THIS METHOD CHECKS IF FIlE EXISTS
def checkFile(jsonfile):
    return os.path.exists(jsonfile)

def checkFileIfEmpty(jsonfile):
    return os.path.getsize(jsonfile)

#THIS METHOD REWRITES JSONFILE
def writeJsonFile(data, jsonfile):
    with open(jsonfile, 'w') as file:
        json.dump(data, file, indent=1)

#THIS METHOD ASSIGN NEW STATEID FOR THE SENSOR OR ALARM
def assigStateId(json_file):
 with open(json_file, 'r') as file:
        object = json.load(file)
        list = object ['states']
        id = int(list[-1]['stateId']) +1
        return id

#THIS METHOD WRITES STATE DATA TO SPECIFIED JSONFILE
def writeStatus(data, jsonfile):

    #Check if file exists
    if(not checkFile(jsonfile) or checkFileIfEmpty(jsonfile) == 0):
        return False
    #Assign a stateId for the sent data
    data['stateId'] = str (assigStateId(jsonfile))

    #Open jsonfile to write the data into
    with open(jsonfile) as file:
        loadeddata = json.load(file)

        #Specify the part where the new data should be written
        key = loadeddata['states']

        #Append the new data
        key.append(data)

        #Rewrite the josnfile
        writeJsonFile(loadeddata, jsonfile)

        #Indicates that the operation succeeded
        return True



#THIS METHOD READS SENSOR STATUS HISTORY
def readStatusHistory():

    #Check if file exists
    if(not checkFile(state_json_file) or checkFileIfEmpty(state_json_file) == 0):
        return False
    
    with open(state_json_file, 'r') as file:
        object = json.load(file)
        json_object = json.dumps(object['states'])
    return json_object
