import smtplib
import Login as login
from random import randint
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re
import os
#Stock Flip info
global from_address
from_address='stockflip4020@gmail.com' #stock flip email @ domain @gmail.com
global from_password
from_password='Stockflip@4020'
global from_name
from_name='Stock Flip'

#send code for requesting password reset to the user email
def sendCodeEmail(code, emailE, username):
    to_address = emailE
    to_name = username
    subject = 'Reset Password Request'
    msg = 'Dear ' +to_name + ',\nYou have requested a password request for Stock Flip.\nYour Code is: ' +str(code)

    message = MIMEMultipart()
    message['From'] = from_name
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(msg, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    #log in to the server
    server.login(from_address, from_password)
    text = message.as_string()
    server.sendmail(from_address, emailE, text)

    server.close()

#send notification if there is a change in specific stock
def sendNotification(nameOfStock, emailE, username, state, value):
    to_address = emailE
    to_name = username
    subject = 'Stock Notification'
    msg = 'Dear ' +to_name+',\n This is the email notification about the stock '+nameOfStock+'.\n'
    msg += 'The stock '+nameOfStock+' has been '+state+' to '+str(value)

    message = MIMEMultipart()
    message['From'] = from_name
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(msg, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    #log in to the server
    server.login(from_address, from_password)
    text = message.as_string()
    server.sendmail(from_address, emailE, text)

    server.close()

def sendMessage(username, emailE, subject, message):
    to_address = emailE
    to_name = username
    msg = 'Dear ' +to_name+'\n'+message
    
    message = MIMEMultipart()
    message['From'] = from_name
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(msg, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    #log in to the server
    server.login(from_address, from_password)
    text = message.as_string()
    server.sendmail(from_address, emailE, text)

    server.close()

#sendMessage('vu3','vu3@mail.usf.edu','Test','TestMessage')
