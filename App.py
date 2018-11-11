#!/usr/bin/python3
# -*- coding: utf-8 -*-

version = "1.76"
title = "StockFlip - version " + version

import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from Login import Authenticator, AccountCreator
from ResetPassword import resetPass
import EmailJob as ej
import Portfolio as pf
import ui_portfolioTile
import ui_company_listing
import Utils
import Companies
import UpdaterThread


'''
Loads and displays the UI for the account login. Valid credentials need to be passed into this UI in order to display the main window
'''
class Login_UI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('UI/login_dialog.ui', baseinstance=self)
        self.ui.LoginButton.clicked.connect(self.perform_login)
        self.ui.CreateAccButton.clicked.connect(self.create_account)
        self.ui.ResetPassButton.clicked.connect(self.reset_password)

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

    def perform_reset_password(self):
        passreset = resetPass(self.ui.usernameLineEdit.text(), self.ui.passwordLineEdit.text(), \
                                 self.ui.confirmPasswordLineEdit.text(), self.ui.emailLineEdit.text())
        valid, message = passreset.checkCredentials()
        if not valid:
            QMessageBox.about(self, "Error", message + "       ")

    def reset_password(self):
        self.ui = uic.loadUi('UI/reset_password.ui')
        self.ui.setModal(True)
        self.ui.ResetPasswordButton.clicked.connect(self.perform_reset_password)
        self.ui.show()
        self.ui.exec_()


'''
This is where the main application window is created and displayed. 
'''
class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        timer = QTimer(self)
        #timer.timeout.connect(self.refresh_ui_data)
        #timer.start(UpdaterThread.time_delta * 1000)

        if 1 == 1: #if enter as member
            uic.loadUi('UI/main.ui', baseinstance=self)
            self.actionAdjust_Credits.triggered.connect(self.adjust_credit)
            self.actionChange_Password.triggered.connect(self.change_password)
            self.actionReset_Account.triggered.connect(self.confirm_reset_account)
            self.initUI()
        else: #else if enter as admin
            uic.loadUi('UI/main_admin.ui', baseinstance=self)
            self.actionAdjust_Credits.triggered.connect(self.adjust_credit)
            self.actionChange_Password.triggered.connect(self.change_password)
            self.actionReset_Account.triggered.connect(self.confirm_reset_account)
            self.actionDelete_User.triggered.connect(self.delete_user)
            self.actionSend_Message_to_UserEmail.triggered.connect(self.send_message)
            self.initUI()
 
    def initUI(self):
        self.setWindowTitle(title)
        self.show()
        self.showMaximized()
        self.loadPortfolio()
        self.loadQuickAccessAndCompanySearch()
        self.loadSearchBar()
        self.refreshButton.clicked.connect(self.refresh_ui_data)
        self.removeFromQuickAccessButton.clicked.connect(self.on_remove_quick_access)

    #TODO -  make faster and prefer to refresh rather than just reloading with new information 
    def refresh_ui_data(self):
        self.listWidget.clear()
        self.loadPortfolio()
        self.quickAccessList.clear()
        self.loadQuickAccessAndCompanySearch()
        print(Companies.charts["AAPL"])

    def on_search(self):
        self.searchList.clear()
        symbol = self.searchBar.text().upper()

        searchText = QListWidgetItem()
        searchText.setText("Searching...")
        self.searchList.addItem(searchText)
        if symbol in Companies.get_available_symbols():
            self.searchList.clear()
            self.searchedWid = ui_company_listing.CompanyListing(self)
            stock = Companies.get_stock(symbol)
            self.searchedWid.populate(stock, symbol)
            self.searchedSymbol = symbol
        else:
            self.searchList.clear()
            item = QListWidgetItem()
            item.setText("Symbol " + symbol + " not found.")
            self.searchList.addItem(item)
            self.searchedSymbol = None
            return
        self.searchedItem = QListWidgetItem()
        self.searchedItem.setSizeHint(QtCore.QSize(100, 100))

        self.searchList.addItem(self.searchedItem)
        self.searchList.setItemWidget(self.searchedItem, self.searchedWid)
        self.searchList.update()
    
    def on_remove_quick_access(self, event):
        item = self.quickAccessList.currentItem()
        if item is not None:
            symbol = self.quickAccessList.itemWidget(item).companyLabel.text()
            print(symbol)
            pf.quick_access_companies.remove(symbol)
            self.quickAccessList.takeItem(self.quickAccessList.row(item))

    def on_add_to_quick_access(self, event):
        if self.searchList.count() != 1:
            return
        symbol = self.searchedSymbol
        if not isinstance(symbol, str):
            return
        if pf.add_to_quick_access(symbol, to_beginning=True):  
            self.loadQuickAccessAndCompanySearch()
      
    def loadSearchBar(self):
        self.sendToQuickAccessButton.mousePressEvent = self.on_add_to_quick_access
        self.searchButton.clicked.connect(self.on_search)

    def loadQuickAccessAndCompanySearch(self):
        self.quickAccessList.clear()
        for symbol in pf.quick_access_companies:
            wid = ui_company_listing.CompanyListing(self)
            stock = Companies.get_stock(symbol)
            if stock is not None:
                wid.populate(stock, symbol)
            wid2 = QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(100, 100))
            self.quickAccessList.addItem(wid2)
            self.quickAccessList.setItemWidget(wid2, wid)

    def loadTotalValue(self):
        self.totalValue.setText("$" + str("{:,}".format(pf.calculate_total_value())))

    def loadPortfolio(self):
        self.loggedInAsUser.setText(pf.username)
        self.currentBalance.setText(str(pf.num_credits))
        self.loadTotalValue()

        for symbol, num_stock in pf.owned_stocks.items():
            stock = Companies.get_stock(symbol)
            wid = ui_portfolioTile.PortfolioTile(self)
            wid.populate(stock, num_stock)
            wid2 = QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(300, 75))
            self.listWidget.addItem(wid2)
            self.listWidget.setItemWidget(wid2, wid)

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

    def adjust_credit(self):
        self.ui = uic.loadUi('UI/adjust_credits.ui')
        self.ui.setModal(True)
        self.ui.AcceptCreditButton.clicked.connect(self.perform_adjust_credit)
        self.ui.show()
        self.ui.exec_()

    def perform_adjust_credit(self):
        credit = int(self.ui.amountCreditEdit.text())
        pf.num_credits = credit
        self.currentBalance.setText(str(pf.num_credits))
        self.loadTotalValue()
        self.currentBalance.update()
       
    def change_password(self):
        self.ui = uic.loadUi('UI/change_password.ui')
        self.ui.setModal(True)
        self.ui.currentUsername.setText(pf.username)
        self.ui.changePasswordButton.clicked.connect(self.perform_change_password)
        self.ui.show()
        self.ui.exec_()

    def perform_change_password(self):
        email = self.ui.emailEdit.text()
        newPassword = self.ui.newPasswordEdit.text()
        confirmnewPassword = self.ui.confirmNewPasswordEdit.text()
        passreset = resetPass(pf.username, newPassword, \
                                 confirmPasswordEdit, email)
        valid, message = passreset.checkCredentials()
        if not valid:
            QMessageBox.about(self, "Error", message + "       ")

    def confirm_reset_account(self):
        self.ui = uic.loadUi('UI/confirm_reset_account.ui')
        self.ui.setModal(True)
        self.ui.AcceptButton.clicked.connect(self.perform_reset_account)
        #update_credit()
        self.ui.show()
        self.ui.exec_()

    def perform_reset_account(self):
        pf.reset()
        self.listWidget.clear()
        self.quickAccessWidget.clear()
        self.loadPortfolio()
        self.loadQuickAccessAndCompanySearch()

    def delete_user(self):
        self.ui = uic.loadUi('UI/delete_user_panel.ui')
        self.ui.setModal(True)
        self.ui.AcceptDeleteButton.clicked.connect(self.perform_delete_user)
        self.ui.show()
        self.ui.exec_()

    def perform_delete_user(self):
        username_email = self.ui.username_emailEdit.text()
        #print("Username "+str(username)+" is deleted!")
        #connect to database to delete relevant username info or email Info

    def send_message(self):
        self.ui = uic.loadUi('UI/send_message.ui')
        self.ui.setModal(True)
        self.ui.SendButton.clicked.connect(self.perform_send_message)
        self.ui.show()
        self.ui.exec_()

    def perform_send_message(self):
        user = self.ui.userEdit.text()
        email = self.ui.emailEdit.text()
        subject = self.ui.subjectEdit.text()
        message = self.ui.messageEdit.text()
        print(user+'\n'+email+'\n'+subject+'\n'+message)
        ej.sendMessage(user, email, subject, message)        
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login_UI()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        Companies.update_company_information()

        #This will continuously pull from the API and push all the data into the cache
        updater = UpdaterThread.UpdaterThread(1, "updater")
        updater.daemon = True
        updater.start()

        mainApp = MainApp()
        mainApp.show()
        
        ret = app.exec_()
        sys.exit(ret)
