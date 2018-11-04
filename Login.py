import hashlib
import re
import os
from Utils import overrides
userData = 'UserInfo.txt'

'''
Utility function to hash a password. Used by Authenticator and AccountCreator
'''
def hash_pass(password):
    encodedPass = str(password).encode('utf-8')
    hashedPass = hashlib.md5(encodedPass).hexdigest()
    return hashedPass
        
'''
Authenticator: Holds credentials and provides functions to check validity of the credentials
'''
class Authenticator():
    def __init__(self, username, password):
        self.username = username
        self.password = password  
        self.hashedPass = hash_pass(self.password)

    '''
    Uses username and raw password combo from the UI form and checks with the MySQL server to make sure user entered correct credentials
    Returns True iff hashed password and username matches database combination
    '''
    def checkCredentials(self):
        if self.isValidUsername() and self.isValidPassword():
            # Connect to the MySQL server and check username + password combo
            # If authenticated, return true and set session token
            print("Valid credentials") #Remove this once the above part is implemented
            return True
        print("Invalid credentials")  #Remove this once the above part is implemented
        return False

    def isValidUsername(self):
        if len(self.username) < 4 or len(self.username) > 16:
            return False
        return True

    def isValidPassword(self):
        if len(self.password) < 8 or len(self.password) > 32:
            return False
        return True
        

'''
This will take data from the create_account UI form, which already contains login credentials for future user
'''
class AccountCreator(Authenticator):
    def __init__(self, username, password, re_password, email):
        super().__init__(username, password)
        self.re_password = re_password
        self.email = email
    
    @overrides(Authenticator)
    def checkCredentials(self):
        if self.isValidUsername() and self.isValidPassword() and self.isValidEmail():
            #Connect to DB, create new user, setup table
            print("Valid signup credentials") #Remove this once the above part is implemented

    @overrides(Authenticator)
    def isValidPassword(self):
        

    def isValidEmail(self):
        if not re.match('\S+@\S+.\S+', self.email) or len(self.email) > 64:
            return False
        return True
