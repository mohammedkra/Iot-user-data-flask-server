import re

#CHECK VALIDITY OF KEYS
def check_key(request):

    #Retrieve all the keys from the sent data
    keys = request.keys()

    #Only 2 keys are allowed in the request
    if len(keys) > 2:
        return False
    
    #Retrieve each of the 2 sent keys
    username_key = list(keys) [0]
    password_key = list(keys) [1]

    #Keys should only be username and password
    if username_key != "username":
        return False
    
    if password_key != "password":
        return False

    return True

#CHECK VALIDITY OF VALUE
def check_value(request):

    #Retrieve all the values from the sent data
    values = request.values()

    #Retrieve each of the 2 sent values (Assuming that checkkey has succeeded)
    username_value = list(values) [0]
    password_value = list(values) [1]

    #Values should only include numbers and letters
    pattern_to_match = "^[A-Za-z0-9]*$"
    if not bool(re.match(pattern_to_match,username_value)):
        return False
    if not bool(re.match(pattern_to_match,password_value)):
        return False
    return True