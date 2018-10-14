from tkinter import *
import hashlib
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
                return x; #if there is existed ID
        return -1; #if there is no-existed ID
   
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
    passE1 = Entry(roots)
    passE2 = Entry(roots)
    emailE = Entry(roots)
    idE.grid(row = 1, column = 1)
    passE1.grid(row = 2, column = 1)
    passE2.grid(row = 3, column = 1)
    emailE.grid(row = 4, column = 1)


    signupButton = Button(roots, text='Signup', command = FSSignup)
    signupButton.grid(columnspan = 2, sticky = W)
    roots.mainloop()

def FSSignup():
    #check Username open(userData) as f
    check = CheckUsername(idE.get())
    if check != -1:
        roots = Tk()
        roots.title('Error')
        error = Label(roots, text='Username already existed')
        error.grid(row=0, column=0, sticky=E)
    else:
        if (passE1.get() != passE2.get()):
            roots = Tk()
            roots.title('Error')
            error = Label(roots, text='Password does not match')
            error.grid(row=0, column=0, sticky=E)
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
