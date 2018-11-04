#!/usr/bin/python3
# -*- coding: utf-8 -*-

version = "2.28"
title = "StockFlip - version " + version

import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
from PyQt5.QtWidgets import *
from Login import Authenticator, AccountCreator
import Portfolio as pf
import ui_portfolioTile

'''
Loads and displays the UI for the account login. Valid credentials need to be passed into this UI in order to display the main window
'''

class Login_UI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('UI/login_dialog.ui', baseinstance=self)
        self.ui.LoginButton.clicked.connect(self.perform_login)
        self.ui.CreateAccButton.clicked.connect(self.create_account)

    def perform_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        authenticate = Authenticator(username, password)
        valid, message = authenticate.checkCredentials()
        if not valid:
            QMessageBox.about(self, "Error", message + "       ")
        else:
            self.accept()

    def perform_create_account(self):
        creator = AccountCreator(self.ui.usernameLineEdit.text(), self.ui.passwordLineEdit.text(), \
                                self.ui.confirmPasswordLineEdit.text(), self.ui.emailLineEdit.text())
        valid, message = creator.checkCredentials()
        if not valid:
            QMessageBox.about(self, "Error", message + "       ")
        # else:
        #     self.ui.accept()
        
    def create_account(self):
        self.ui = uic.loadUi('UI/create_account.ui')
        self.ui.setModal(True)
        self.ui.CreateAccountButton.clicked.connect(self.perform_create_account)
        self.ui.show()
        self.ui.exec_() #== QtWidgets.QDialog.Accepted:

'''
This is where the main application window is created and displayed. 
'''
class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/main.ui', baseinstance=self)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(title)
        self.show()
        self.showMaximized()
        self.loadPortfolio()

    def loadPortfolio(self):
        #current workspace - adding a list of portfolio items to the portfolio seciton of the gui using custom widgets in a list view
        #This is the scrollable list of custom tile widgets
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        self.verticalLayout_4.addWidget(scroll_area)
        d_scroll_area_widget = QWidget()
        scroll_area.setWidget(d_scroll_area_widget)
        d_scroll_area_layout = QVBoxLayout(d_scroll_area_widget)
        
        for i in range(10):
            pfTile = ui_portfolioTile.PortfolioTile()
            d_scroll_area_layout.addWidget(pfTile)

        self.loggedInAsUser.setText(pf.username)
        self.currentBalance.setText(str(pf.credits))    

    def clicked(self, event):
        
        pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit?',
            "Are you sure to quit?", QMessageBox.No | 
            QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def centerScreen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login_UI()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        mainApp = MainApp()
        mainApp.show()
        sys.exit(app.exec_())

