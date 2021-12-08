import bcrypt

salt_file = "data_center/salt.txt"
#THIS METHOD RETRIEVES THE BCRYPT SALT
def get_salt():
    with open(salt_file,"r") as file:
        salt = file.read()
    return salt

#THIS METHOD IS USED FOR BCRYPTING PASSWORDS
def hashPassWord(password):
    return bcrypt.hashpw(password, get_salt())

#THIS METHOD IS USED TO CHECK A MATCH BETWEEN 2 PASSWORDS
def check_password(inputPassword, existingPassword):
    return bcrypt.checkpw(inputPassword, existingPassword)
