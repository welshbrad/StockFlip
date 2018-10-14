#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
import sys
import Login as loginfile

version = "0.1"
title = "StockFlip - version " + version



def center(QWidget):

	qr = QWidget.frameGeometry()
	cp = QDesktopWidget().availableGeometry().center()
	qr.moveCenter(cp)
	QWidget.move(qr.topLeft())


		
		
class UI(QWidget):
	mainInstance = None
	
	def __init__(self):
		super().__init__()

	def initUI(self):    
		mainInstance = self
		self.setWindowTitle(title)	
		self.resize(300, 300)
		center(self)
		form = QFormLayout()
		user_entry = QLineEdit()
		form.addRow("Username", user_entry)
		self.setLayout(form)   
		self.hide()

	def initLoginScreen(self):
		self.setWindowTitle("Login | " + title)
		self.resize(300, 300)
		center(self)
		
		form = QFormLayout()

		user_entry = QLineEdit()
		form.addRow("Username", user_entry)

		pass_entry = QLineEdit()
		pass_entry.setEchoMode(QLineEdit.Password)
		form.addRow("Password",pass_entry)
		
		
		login_button = QPushButton("&Login")
		login_button.setDefault(True)
		login_button.setAutoDefault(True)
		login_button.clicked.connect(lambda : enter_credentials(user_entry.text(), pass_entry.text(), login_button, self))
		
		pass_entry.editingFinished.connect(login_button.click)
		form.addWidget(login_button)
		
		self.setLayout(form)
		self.show()



def enter_credentials(username, password, login_button, widget):
	login_button.setEnabled(False)
	login_button.setText("Logging in...")
	if(login.CheckLogin(username, password)):
		widget.hide()
		createMainWindow()
	else:
		print("Fail")
		login_button.setEnabled(True)
		login_button.setText("Login")
	
def createMainWindow():
	if UI.mainInstance is not None:
		UI.mainInstance.QWidget.show()
	
	

	
def main():
	app = QApplication(sys.argv)
	''' '''
	loginWindow = UI().initLoginScreen()
	mainWindow = UI().initUI()
	
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()  





'''
class MainWindow(Frame):
    bg_color = "#333"
    fg_color = "#FFF"
    padding = (10,10)

  
    def __init__(self, master):
        super().__init__()   
        self.initMenus()
        self.master.title(title)
       
        #self.initMainUI()

    def initMenus(self):
        menubar = Menu(self.master)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Configure User", command=options)
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=options)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)
   
    
        
    def initMainUI(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
      
        Style().configure("TFrame", background="#333")
   

        label1 = Label(self, text="Test text").grid(column=1, row=1, sticky=W)
        label2 = Label(self, text="Test text2").grid(column=2, row=1, sticky=E)

def login():
    idE = e1.get()
    passE = e2.get()
    #print (idE, passE)
    a = loginfile.CheckLogin(idE, passE)
    #if a is true
        #enter program
    #else
        #show error
    

def options():
    print ("Options Menu")

'''

