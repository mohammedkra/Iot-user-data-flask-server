import json
from check_login.bcrypter import check_password

users_jsonfile = "data_center/users.json"

#THIS METHOD CHECKS USER AUTHEN
def checkusr(jsondata):

    #Retrive the username and password from the sent data
    username = jsondata ['username']
    password = jsondata ['password']

    #Load the file where users are stored
    with open (users_jsonfile) as file:
        loadeddata = json.load(file)
        userlist = loadeddata['users']

        #Search for the user in the file
        for user in userlist:

            #Check if the username exists and that there is a match between passwords
            if (user['username'] == username and check_password(password,user['password'])):
                return True
    return False