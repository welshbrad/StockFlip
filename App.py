#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
import sys
import Login as loginfile
import Companies as companies

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
	
	#companies.display_company_list()
	
	
	loginWindow = UI().initLoginScreen()
	mainWindow = UI().initUI()
	

	
	
	
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()  




