import os
import re
from PyQt5.QtWidgets import QMessageBox
from Login import Authenticator, hash_pass
from EmailJob import sendCodeEmail
from Utils import overrides

class resetPass():
    def __init__(self, username, password, email):
        self.username = str(username)
        self.password = str(password)  
        self.hashedPass = hash_pass(self.password)
        self.email = str(email)
        self.return_string = 'Invalid Password'

    def checkCredentials(self):
        if self.isValidPassword():
                #if statement: connect to database to check for matched email and password:
                checkCode()
                return True,''
            #else: return False, "Invalid username and email address"
        else:
            return False, self.return_string
    
    def isValidPassword(self):
        if len(self.password) < 8 or len(self.password) > 64:
            self.return_string = 'Invalid Password'
            return False
        return True

    def perform_check_code(self):
        codeE = self.ui.codeLineEdit.text()
        if (code == codeE):
            self.changePassword()
        else:
            print("Invalid Code")
            return False
        
    def checkCode(self):
        global code
        code = randint(10000,99999)
        sendCodeEmail(code, self.email, self.username)
        self.ui = uic.loadUI('UI/check_code.ui')
        self.ui.setModal(True)
        self.ui.CheckCodeButton.clicked.connect(self.perform_check_code)
        self.ui.show()
        self.ui.exec_

    def changePassword(self):
        #connect to DB and change the password of current user
        return True
