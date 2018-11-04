import smtplib
import Login as login
import EmailJob as emailfunc
from random import randint
from tkinter import *
import re
import os
userData = 'UserInfo.txt'
#check if the email address existed
def checkEmail():
   global emailPos
   emailPos = -1
   with open(userData) as f:
      data = f.readlines()
      for x in range(3, len(data)-1, 5): #read from second line of the txt file and 4 line is a set of user
         email = data[x].rstrip()
         if (email == emailE.get()):
            emailPos = x
         f.close()

      if (emailPos == -1):
         roots = Tk()
         roots.title('Error')
         instruction = Label (roots, text='Invalid Email Address')
         instruction.grid(row=0, column=0, sticky=E)
         roots.mainloop()
      else:
         checkPassword(emailPos)
#check for valid password
def checkPassword(emailPos):
   if (passE1.get() != passE2.get()):
      roots = Tk()
      roots.title('Error')
      error = Label(roots, text='Password does not match')
      error.grid(row=0, column=0, sticky=W)
   else:
      #check valid password
      checkPass = login.isValidPassword(passE1.get())
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
         roots.mainloop()
      else:
         checkCode(emailPos)
         
#send code to user Email and pop-up a code checking window
def checkCode(emailPos):
   global code
   global codeE
   code = randint(10000, 99999)
   with open (userData, 'r') as f:
      data = f.readlines()
      f.close()

   userName = data[emailPos-2].rstrip()
   emailfunc.sendCodeEmail(code, emailE.get(), userName)
   print(code)
   roots = Tk()
   roots.title('Checking Code')
   instruction = Label(roots, text='Please check your email for code')
   instruction.grid(row=0, column=0, columnspan=2, sticky=W)

   codeL = Label(roots, text='Code:')
   codeL.grid(row=1, column=0, sticky=W)
   codeE = Entry(roots)
   codeE.grid(row=1, column=1, sticky=W)
   signupButton = Button(roots, text='Submit', command = confirmedValidCode)
   signupButton.grid(columnspan = 2, sticky = W)
   roots.mainloop()

#check for valid code
def confirmedValidCode():
   codeEntry = int(codeE.get())
   if (codeEntry == code):
      changePassword()
      roots = Tk()
      roots.title('Success')
      instruction = Label (roots, text='Your password has been reseted')
      instruction.grid(row=0, column=0, sticky=E)
      roots.mainloop()
   else:
      roots = Tk()
      roots.title('Error')
      instruction = Label (roots, text='Invalid Code')
      instruction.grid(row=0, column=0, sticky=E)
      roots.mainloop()

#change password if code is valid
def changePassword():
   with open (userData, 'r') as f:
      data = f.readlines()
      f.close()

   with open(userData, 'w') as f:
      for x in range (0, len(data)):
         if (x+1 == emailPos):
            pass2write = login.hashing(passE1.get())
            f.write(pass2write)
            f.write('\n')
         else:
            f.write(data[x])
      f.close()

#reset password interface
def resetPassword():
    global passE1
    global passE2
    global emailE
#    global instruction
#    global roots
    roots = Tk()
    roots.title('Reset Password')
    instruction = Label (roots, text='Please Fill in the space')
    instruction.grid(row=0, column=0, sticky=E)

    emailL = Label (roots, text='Your email address: ')
    passL1 = Label(roots, text='New Password: ')
    passL2 = Label(roots, text='Re-enter new password: ')
    emailL.grid(row=1,column=0, sticky=W)
    passL1.grid(row=2, column=0, sticky=W)
    passL2.grid(row=3, column=0, sticky=W)
    
    emailE = Entry(roots)
    passE1 = Entry(roots, show='*')
    passE2 = Entry(roots, show='*')
    emailE.grid(row = 1, column = 1)
    passE1.grid(row = 2, column = 1)
    passE2.grid(row = 3, column = 1)


    submitButton = Button(roots, text='Submit', command = checkEmail)
    submitButton.grid(columnspan = 2, sticky = W)
    roots.mainloop()
    
