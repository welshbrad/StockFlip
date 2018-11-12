import sys
import hashlib
import re
import os
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from Utils import overrides
from PyQt5.QtWidgets import QMessageBox
from random import randint
import EmailJob as ej
import Portfolio as pf
import database1 as db

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
        self.username = str(username)
        self.password = str(password)  
        self.hashedPass = hash_pass(self.password)
        self.return_string = ''

    '''
    Uses username and raw password combo from the UI form and checks with the MySQL server to make sure user entered correct credentials
    Returns True iff hashed password and username matches database combination
    '''
    def checkCredentials(self):
        if self.isValidUsername() and self.isValidPassword():
            check = db.check_user_password(self.username, self.password)
            if check:
                self.createSession()
                return True, ''
            else:
                self.return_string ="Invalid Username or Password"
                return False, self.return_string
        else:
            print("Invalid credentials")  #Remove this once the above part is implemented
            return False, self.return_string

    def isValidUsername(self):
        if len(self.username) < 3 or len(self.username) > 16:
            self.return_string = "Invalid Username"
            return False
        return True

    def isValidPassword(self):
        if len(self.password) < 8 or len(self.password) > 64:
            self.return_string = "Invalid Password"
            return False
        return True

    def createSession(self):
        credit = db.find_credits(self.username)
        total_value = db.find_total_value(self.username)
        pf.username = self.username
        pf.num_credits = credit
        pf.total_value = total_value
        stock = db.find_stock_of_user(pf.username)
        for i in stock:
            pf.set_stock(i[1], i[2])
        quick_access = db.find_user_quick_access(pf.username)
        for i in quick_access:
            pf.add_to_quick_access(i[1])
        

'''
This will take data from the create_account UI form, which already contains login credentials for future user
'''
class AccountCreator(Authenticator):
    def __init__(self, username, password, re_password, email):
        super().__init__(username, password)
        self.re_password = str(re_password)
        self.email = str(email)
     
    
    @overrides(Authenticator)
    def checkCredentials(self):
        if self.isValidUsername() and self.isValidPassword() and self.isValidEmail():
            checkUser = db.check_user(self.username)
            checkEmail = db.check_email(self.email)
            if checkUser:
                self.return_string ="Username is already existed!"
                return False, self.return_string
            if checkEmail:
                self.return_string ="Email is already used!"
                return False, self.return_string
            else:
                db.insert_user(self.username, self.password, self.email, "member")
                db.insert_UP(self.username)
                #add some quick access stock to new user
                db.insert_user_quick_access(self.username, "AAPL")
                db.insert_user_quick_access(self.username, "GOOGL")
                db.insert_user_quick_access(self.username, "COST")
                db.insert_user_quick_access(self.username, "EBAY")
                db.insert_user_quick_access(self.username, "FOX")
                return True, 'Valid'
        return False, self.return_string

    @overrides(Authenticator)
    def isValidPassword(self):
        if super().isValidPassword():
            if (self.password == self.re_password):
                return True
            else:
                self.return_string = "Passwords don't match"
                return False
        return False

    def isValidEmail(self):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', self.email):
            self.return_string = "Invalid Email"
            return False
        return True

class PasswordChange(Authenticator):
    def __init__(self, username, password, re_password):
        super().__init__(username, password)
        self.re_password = str(re_password)

    def isValidPassword(self):
        if super().isValidPassword():
            if (self.password == self.re_password):
                return True, " "
            else:
                return False, "Passwords don't match"
        return False, "Invalid Password"

class ResetPassword(Authenticator):
    def __init__(self, username, password, re_password, email):
        super().__init__(username, password)
        self.re_password = str(re_password)
        self.email = str(email)
        
    def checkCredentials(self):
        if self.isValidUsername() and self.isValidPassword() and self.isValidEmail():
            checkUserEmail = db.check_user_email(self.username, self.email)
            if checkUserEmail:
                    self.checkCode()
                    return True, " "
            else:
                return False, "Invalid Username or Email Address"
        return False, self.return_string

    @overrides(Authenticator)
    def isValidPassword(self):
        if super().isValidPassword():
            if (self.password == self.re_password):
                return True
            else:
                self.return_string = "Passwords don't match"
                return False
        return False

    def isValidEmail(self):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', self.email):
            self.return_string = "Invalid Email"
            return False, self.return_string
        return True, " "

    def perform_check_code(self):
        codeE = self.ui.codeLineEdit.text()
        print(code+"ok")
        print(code +" "+ codeE)
        print("OK5")
        if (self.code == codeE):
            #self.changePassword()
            return True, " "
        else:
            print("Invalid Code")
            return False, "Invalid Code"
        
    def checkCode(self):
        global code
        code = randint(10000,99999)
        ej.sendCodeEmail(code, self.email, self.username)
        self.ui = uic.loadUi('UI/check_code.ui')
        self.ui.setModal(True)
        self.ui.CheckCodeButton.clicked.connect(self.perform_check_code)
        self.ui.show()
        self.ui.exec_()
        
#hi = ResetPassword("vunguyen1", "123qweqwe", \
#                   "123qweqwee", "vu3@mail.usf.edu")
#valid, message = hi.checkCredentials()
