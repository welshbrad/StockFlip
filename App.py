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
        symbol = self.searchBar.text()

        searchText = QListWidgetItem()
        searchText.setText("Searching...")
        self.searchList.addItem(searchText)

        if symbol in Utils.get_symbols():
            self.searchList.clear()
            wid = ui_company_listing.CompanyListing(self)
            stock = Utils.get_stock(symbol)
            stock = stock.get_quote()
            wid.populate(stock, symbol)
        else:
            self.searchList.clear()
            item = QListWidgetItem()
            item.setText("Symbol " + symbol + " not found.")
            self.searchList.addItem(item)
            return
        wid2 = QListWidgetItem()
        wid2.setSizeHint(QtCore.QSize(100, 100))

        self.searchList.addItem(wid2)
        self.searchList.setItemWidget(wid2, wid)
        self.searchList.update()
    
    def on_add_to_quick_access(self, event):
        assert self.searchList.count() <= 1
        if self.searchList.count() == 0:
            return
        else:
            item = self.searchList.item(0)
            itemWidget = self.searchList.itemWidget(item)
            self.quickAccessList.addItem(item)
            self.quickAccessList.setItemWidget(item, itemWidget)
            self.searchList.clear()
            print(itemWidget.companyLabel)
            self.quickAccessList.repaint()
      
    def loadSearchBar(self):
        self.sendToQuickAccessButton.mousePressEvent = self.on_add_to_quick_access
        self.searchButton.clicked.connect(self.on_search)

    def loadQuickAccessAndCompanySearch(self):
        for symbol in pf.quick_access_companies:
            wid = ui_company_listing.CompanyListing(self)
            stock = Companies.quick_access_data.get_quote()[symbol]
            wid.companyLabel.setText(str(symbol))
            wid.percentChangeLabel.setText(str(stock["changePercent"])+"%")
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
        self.listWidget.repaint()

    def loadPortfolio(self):
        self.loggedInAsUser.setText(pf.username)
        self.currentBalance.setText(str(pf.credits))    
        
        #current workspace - adding a list of portfolio items to the portfolio seciton of the gui using custom widgets in a list view
        #This is the scrollable list of custom tile widgets
        for company, stock in pf.owned_stocks.items():
            wid = ui_portfolioTile.PortfolioTile(self)
            wid.companyLabel.setText(str(company))
            wid.ownedStockLabel.setText("Shares owned: "+ str(stock))
            wid2 = QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(100, 40))
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
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login_UI()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        mainApp = MainApp()
        mainApp.show()
        sys.exit(app.exec_())

