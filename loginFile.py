from tkinter import *
import os
userData = 'UserInfo.txt'

def CheckLogin(idEL, passEL):
    with open(userData) as f:
        data = f.readlines()
        id = data[0].rstrip()
        passW = data[1].rstrip()

    for x in range(0, len(data)-1, 2):
        id = data[x].rstrip()
        passW = data[x+1].rstrip()
        if idEL == id and passEL == passW:
            a = True
            break;
        else:
            a = False
        

    if a == True:
        r = Tk()
        r.title(':D')
        r.geometry('150x50')
        rlbl = Label(r, text = '\nLogged In')
        rlbl.pack()
        r.mainloop()
    else:
        r = Tk()
        r.title(':D')
        r.geometry('150x50')
        rlbl = Label(r, text='\nInvalid Username or Password')
        rlbl.pack()
        r.mainloop()

def SignUp():
    global passE
    global idE
    global roots
    
    roots = Tk()
    roots.title('Signup')
    intruction = Label(roots, text='Please Create a new Account\n')
    intruction.grid(row=0, column=0, sticky=E)

    idL = Label(roots, text='New Username: ')
    passL = Label(roots, text='New Password: ')
    idL.grid(row=1, column=0, sticky=W)
    passL.grid(row=2, column=0, sticky=W)

    idE = Entry(roots)
    passE = Entry(roots, show='*')
    idE.grid(row = 1, column = 1)
    passE.grid(row = 2, column =1)


    signupButton = Button(roots, text='Signup', command = FSSignup)
    signupButton.grid(columnspan = 2, sticky = W)
    roots.mainloop()

def FSSignup():
    with open(userData, 'a') as f:
        f.write(idE.get())
        f.write('\n')
        f.write(passE.get())
        f.write('\n')
        f.close()
    roots.destroy()
