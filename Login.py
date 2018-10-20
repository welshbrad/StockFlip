from tkinter import *
import hashlib
import re
import os
userData = 'UserInfo.txt'

def hashing(pass2hash):
    encodedPass = pass2hash.encode('utf-8')
    hashedPass = hashlib.md5(encodedPass).hexdigest()
    return hashedPass

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
        return False;
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

def isValidUsername (idE):
    if (len(idE) < 4):
        return False
    else:
        return True;
def isValidPassword(passE):
    while True:
        if (len(passE)<8 or len(passE)>32):
            return False
        elif not re.search("[a-z]", passE):
            return False
        elif not re.search("[A-Z]", passE):
            return False
        elif not re.search("[0-9]", passE):
            return False
        elif re.search("\s", passE):
            return False
        else:
            return True
        
    
def isValidEmail(emailE):
    if re.match('\S+@\S+.\S+', emailE):
        return True
    else:
        return False

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
