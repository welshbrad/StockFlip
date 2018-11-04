import hashlib
import re
import os
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
            print("Valid credentials")
            return True
        print("Invalid credentials")
        return False

    def isValidUsername(self):
        if len(self.username) < 4 or len(self.username) > 16:
            return False
        return True

    def isValidPassword(self):
        if len(self.password) < 8 or len(self.password) > 32:
            return False
        return True
        
class AccountCreator(Authenticator):
    def __init__(self, username, password, re_password, email):
        super().__init__(username, password)
        self.re_password = re_password
        self.email = email
    
        print(self.hashedPass)

    def checkCredentials(self):
        pass




    # def isValidEmail(self):
    #     if not re.match('\S+@\S+.\S+', self.email) or len(self.email) > 64:
    #         return False
    #     return True




'''

def CheckLogin(idEL, passEL):
    with open(userData) as f:
        data = f.readlines()

    checkID = CheckUsername(idEL)
    if checkID == -1: #no exisited ID -> invalue id
        r = Tk()
        r.title(':D')
        r.geometry('150x50')
        rlbl = Label(r, text='\nInvalid Username or Password')
        rlbl.pack()
        r.mainloop()
        return False
    else:
        passW = data[checkID+1].rstrip()
        pass2check = hashing(passEL)
        if  pass2check == passW:
            r = Tk()
            r.title(':D')
            r.geometry('150x50')
            rlbl = Label(r, text = '\nLogged In')
            rlbl.pack()
            r.mainloop()
            return True
        else:
            r = Tk()
            r.title(':D')
            r.geometry('150x50')
            rlbl = Label(r, text='\nInvalid Username or Password')
            rlbl.pack()
            r.mainloop()
            return False

def CheckUsername(idE):
    with open(userData) as f:
        data = f.readlines()
        for x in range(1, len(data)-1, 4): #read from second line of the txt file and 4 line is a set of user
            id = data[x].rstrip()
            if idE == id:
                return x #if there is existed ID
        return -1 #if there is no-existed ID



def SignUp():
    global passE1
    global passE2
    global emailE
    global idE
    global roots
    
    roots = Tk()
    roots.title('Signup')
    intruction = Label(roots, text='Please Create a new Account\n')
    intruction.grid(row=0, column=0, sticky=E)

    idL = Label(roots, text='New Username: ')
    passL1 = Label(roots, text='New Password: ')
    passL2 = Label(roots, text='Re-enter password: ')
    emailL = Label (roots, text='Enter email: ')
    idL.grid(row=1, column=0, sticky=W)
    passL1.grid(row=2, column=0, sticky=W)
    passL2.grid(row=3, column=0, sticky=W)
    emailL.grid(row=4,column=0, sticky=W)

    idE = Entry(roots)
    passE1 = Entry(roots, show='*')
    passE2 = Entry(roots, show='*')
    emailE = Entry(roots)
    idE.grid(row = 1, column = 1)
    passE1.grid(row = 2, column = 1)
    passE2.grid(row = 3, column = 1)
    emailE.grid(row = 4, column = 1)


    signupButton = Button(roots, text='Signup', command = FSSignup)
    signupButton.grid(columnspan = 2, sticky = W)
    passE1.delete(0, END)
    passE2.delete(0, END)
    roots.mainloop()


def FSSignup():
    #check Email
    checkEmail = isValidEmail(emailE.get())
    if checkEmail == False:
        roots = Tk()
        roots.title('Email Error')
        error = Label(roots, text='Invalid Email Format (abc@abc.abc)')
        error.grid(row=0, column=0, sticky=E)
        return
    #check Username
    isValidUsernameFormat = isValidUsername(idE.get())
    if isValidUsernameFormat == False:
        roots = Tk()
        roots.title('Username Error')
        error = Label(roots, text='Invalid Username Format:')
        ins1 = Label (roots, text='Username must contain at least 4 character')
        error.grid(row=0, column=0, sticky=E)
        ins1.grid(row=0, column=0, sticky=E)
        return
    checkUser = CheckUsername(idE.get())
    if checkUser != -1:
        roots = Tk()
        roots.title('Username Error')
        error = Label(roots, text='Username already existed')
        error.grid(row=0, column=0, sticky=E)
    else:
        #check Password match
        if (passE1.get() != passE2.get()):
            roots = Tk()
            roots.title('Error')
            error = Label(roots, text='Password does not match')
            error.grid(row=0, column=0, sticky=W)
        else:
            #check valid password
            checkPass = isValidPassword(passE1.get())
            if checkPass == False:
                roots = Tk()
                roots.title('Password does not match')
                
                instruction = Label(roots, text='Password must contains:')
                instruction.grid(row=0, column=0, sticky=W)
                ins1 = Label(roots, text='_At least 1 lowercase character')
                ins2 = Label(roots, text='_At least 1 uppercase character')
                ins3 = Label(roots, text='_Length from 4 to 32 character')
                
                ins1.grid(row=1, column=0, sticky=W)
                ins2.grid(row=2, column=0, sticky=W)
                ins3.grid(row=3, column=0, sticky=W)
                
            else:
                with open(userData, 'a') as f:
                    f.write(idE.get())
                    f.write('\n')
                    pass2write = hashing(passE1.get())
                    f.write(pass2write)
                    f.write('\n')
                    f.write(emailE.get())
                    f.write('\n')
                    f.write('\n') #extra line between two users' data
                    f.close()
                    roots = Tk()
                    roots.title('Success')
                    success = Label(roots, text='Account is created sucessfully')
                    
                success.grid(row=0,column=0,sticky=E)

'''