#!/usr/bin/python3
# -*- coding: utf-8 -*-

version = "2.46"
title = "StockFlip - version " + version

import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
from PyQt5.QtWidgets import *
from Login import Authenticator, AccountCreator
from ResetPassword import resetPass
import Portfolio as pf
import ui_portfolioTile
import ui_company_listing
import Utils
import Companies
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
        uic.loadUi('UI/main.ui', baseinstance=self)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(title)
        self.show()
        self.showMaximized()
        self.loadPortfolio()
        
        #Load up all the data and cache it for quick access companies
        Companies.quick_access_data = Companies.init_quick_access_companies(pf.quick_access_companies)
        
        self.loadQuickAccessAndCompanySearch()
        self.loadMarketInfo()

        self.loadSearchBar()

    def loadMarketInfo(self):
        pass

    def on_search(self):
        self.searchList.clear()
        symbol = self.searchBar.text().upper()

        searchText = QListWidgetItem()
        searchText.setText("Searching...")
        self.searchList.addItem(searchText)

        if symbol in Utils.get_symbols():
            self.searchList.clear()
            self.searchedWid = ui_company_listing.CompanyListing(self)
            stock = Utils.get_stock(symbol)
            stock = stock.get_quote()
            self.searchedWid.populate(stock, symbol)
        else:
            self.searchList.clear()
            item = QListWidgetItem()
            item.setText("Symbol " + symbol + " not found.")
            self.searchList.addItem(item)
            return
        self.searchedItem = QListWidgetItem()
        self.searchedItem.setSizeHint(QtCore.QSize(100, 100))

        self.searchList.addItem(self.searchedItem)
        self.searchList.setItemWidget(self.searchedItem, self.searchedWid)
        self.searchList.update()
    
    def on_add_to_quick_access(self, event):
        assert self.searchList.count() <= 1
        if self.searchList.count() == 0:
            return
        else:
            #itemWidget = self.searchList.itemWidget(item)
            self.quickAccessList.addItem(self.searchedItem)
            self.quickAccessList.setItemWidget(self.searchedItem, self.searchedWid)
           # print(itemWidget.companyLabel)
            self.quickAccessList.update()
            self.searchList.clear()
      
    def loadSearchBar(self):
        self.sendToQuickAccessButton.mousePressEvent = self.on_add_to_quick_access
        self.searchButton.clicked.connect(self.on_search)

    def loadQuickAccessAndCompanySearch(self):
        for symbol in pf.quick_access_companies:
            wid = ui_company_listing.CompanyListing(self)
            stock = Companies.quick_access_data.get_quote()[symbol]
            wid.companyLabel.setText(str(symbol))
            wid.percentChangeLabel.setText(str(round(stock["changePercent"], 3))+"%")
            wid.priceLabel.setText("$" + str(stock["latestPrice"]))
            wid.openLabel.setText("$" + str(stock["open"]))
            wid.highLabel.setText("$" + str(stock["high"]))
            wid.lowLabel.setText("$" + str(stock["low"]))
            wid.closeLabel.setText("$" + str(stock["close"]))
            wid.volumeLabel.setText(str(stock["latestVolume"]))

            wid2 = QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(100, 100))
            self.quickAccessList.addItem(wid2)
            self.quickAccessList.setItemWidget(wid2, wid)

    def updatePortfolio(self, event):
        sender = self.sender()
        sender.resize(300,75)
        self.listWidget.update()
        self.listWidget.repaint()

    def loadPortfolio(self):
        self.loggedInAsUser.setText(pf.username)
        self.currentBalance.setText(str(pf.credits))    

        for symbol, num_stock in pf.owned_stocks.items():
            # wid2 = QListWidgetItem()
            # wid2.setSizeHint(QtCore.QSize(100, 100))
            #stock = Companies.quick_access_data.get_quote()[symbol]
            wid = ui_portfolioTile.PortfolioTile(self)
            wid.companyLabel.setText(str(symbol))
            #wid.priceLabel.setText("$" + str(stock["latestPrice"]))
            #wid.percentChangeLabel.setText(str(round(stock["changePercent"],2))+"%")
            wid.ownedStockLabel.setText("Shares owned: "+ str(num_stock))
            wid2 = QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(300, 75))
            self.listWidget.addItem(wid2)
            self.listWidget.setItemWidget(wid2, wid)

        self.listWidget.currentItemChanged.connect(self.updatePortfolio) 

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
        pf.credits = credit
        print(credit)
        #not done yet need to connect to DB to change the credit of user

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
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login_UI()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        mainApp = MainApp()
        mainApp.show()
        sys.exit(app.exec_())

