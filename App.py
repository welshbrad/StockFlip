#!/usr/bin/python3
# -*- coding: utf-8 -*-

version = "1.86"
title = "StockFlip - version " + version

import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from random import randint
from Login import Authenticator, AccountCreator, PasswordChange, ResetPassword
import database1 as db
import EmailJob as ej
import Portfolio as pf
import ui_portfolioTile
import ui_company_listing
import Utils
import Companies
import UpdaterThread
from datetime import datetime
from PyQt5 import QtWebEngineWidgets

import Grapher
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
        authenticate = Authenticator(username.lower(), password)
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
        else:
            QMessageBox.about(self, "Success", message + "       ")
        
    def create_account(self):
        self.ui = uic.loadUi('UI/create_account.ui')
        self.ui.setModal(True)
        self.ui.CreateAccountButton.clicked.connect(self.perform_create_account)
        self.ui.show()
        self.ui.exec_() #== QtWidgets.QDialog.Accepted:

    def perform_reset_password(self):
        code = randint(10000, 99999)
        resetpassword = ResetPassword(self.ui.usernameLineEdit.text(), self.ui.passwordLineEdit.text(), \
                                      self.ui.confirmPasswordLineEdit.text(), self.ui.emailLineEdit.text(), code)
        valid, message = resetpassword.checkCredentials()
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
        self.company_selected = False

        #timer.timeout.connect(self.refresh_ui_data)
        #timer.start(UpdaterThread.time_delta * 1000)
        uic.loadUi('UI/main.ui', baseinstance=self)
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
        self.confirmButton.clicked.connect(self.on_confirm_trade)

        self.actionAdjust_Credits.triggered.connect(self.adjust_credit)
        self.actionChange_Password.triggered.connect(self.change_password)
        self.actionReset_Account.triggered.connect(self.confirm_reset_account)
        checkRole = db.check_role(pf.username)
        if checkRole =="admin":
            self.actionDelete_User.triggered.connect(self.delete_user)
            self.actionMessage_User.triggered.connect(self.send_message)
        else:
            self.actionDelete_User.triggered.connect(self.not_admin)
            self.actionMessage_User.triggered.connect(self.not_admin)

        #connect the owned_stocks and quick access list widget selected item to update the currently selected company in order to update the chart and trade sections
        self.listWidget.itemPressed.connect(lambda: self.on_select_tile(self.listWidget))
        self.quickAccessList.itemPressed.connect(lambda: self.on_select_tile(self.quickAccessList))
        self.searchList.itemPressed.connect(lambda: self.on_select_tile(self.searchList))

        self.numToTrade.textChanged.connect(lambda: self.on_update_trade_text(self.numToTrade.text()))
        self.trade_frame.hide()
        self.company_info_panel.hide()

    """
    Quick utility for formatting QLabel strings for money
    """
    def format_dollars(self, value):
        return "$" + str("{:,}".format(value))

    """
    Populates the graph and detailed compoany information section of the main app
    """
    def update_company_info_panel(self):
        if not self.company_selected:
            return
        self.company_info_symbol_label.setText(str(self.active_widget.companyLabel.text()))
        self.company_info_name_label.setText(str(Companies.get_stock(self.company_selected)["companyName"]))

        stats = Utils.get_key_stats(self.company_selected)
        
        self.markCapLabel.setText(self.format_dollars(stats["marketcap"]))
        self.weekHighLabel.setText(self.format_dollars(stats["week52high"]))
        self.weekLowLabel.setText(self.format_dollars(stats["week52low"]))
        self.ytdChangePercentLabel.setText(str(round(stats["ytdChangePercent"],2))+"%")
        self.divRateLabel.setText(self.format_dollars(stats["dividendRate"]))
        self.divYieldLabel.setText(str(round(stats["dividendYield"], 2))+"%")
        self.revLabel.setText(self.format_dollars(stats["revenue"]))
        self.profitLabel.setText(self.format_dollars(stats["grossProfit"]))
        self.news.setText("Test")

        stock = Companies.get_stock(self.company_selected)
        self.prc.setText(self.format_dollars(Companies.get_latest_price(self.company_selected)))
        self.lo.setText(self.format_dollars(stock["low"]))
        self.hi.setText(self.format_dollars(stock["high"]))
        self.vol.setText(self.format_dollars(stock["latestVolume"]))
        self.opn.setText(self.format_dollars(stock["open"]))
        self.cls.setText(self.format_dollars(stock["close"]))
        self.company_info_panel.show()
        self.webEngineView.setHtml(Grapher.make_html(self.company_selected))
        #self.webEngineView.update()
        #self.webEngineView.show()
        
    """
    This will update the trade section text when typing in an amount into the Shares field
    """
    def on_update_trade_text(self, text):
        if self.company_selected is None:
            return False
        try:
            number = int(text)
        except Exception:
            self.totalPriceLabel.setText("-")
            return False
        else:
            total_price = Companies.get_stock(self.company_selected)["latestPrice"] * int(text)
            self.totalPriceLabel.setText("$" + str("{:,}".format(total_price)))

    """
    When a user clicks on any company tile in the Quick access, search, or owned stocks lists, it will set an active_company widget and then populate the trade screen
    and market info panel
    """
    def on_select_tile(self, listWidget):
        self.trade_frame.hide()
        self.active_list_widget = listWidget
        item = listWidget.currentItem()
        if item is not None:
            self.active_widget = listWidget.itemWidget(item)
            symbol = self.active_widget.companyLabel.text()
            self.company_selected = symbol
            self.update_company_info_panel()
            #print(self.company_selected)
            self.companyLabel.setText(self.company_selected)
            #turn get_company_name(symbol) into Util function
            self.companyFullNameLabel.setText(Companies.get_stock(self.company_selected)["companyName"])
            self.priceLabel.setText("Share Price: $" + str("{:,}".format(Companies.get_stock(self.company_selected)["latestPrice"])))
            self.numSharesOwnedLabel.setText("Shares Owned: " + str(pf.get_num_owned(self.company_selected)))
            self.trade_frame.show()


    """
    This is what is run when the user hits the refresh button
    """
    def refresh_ui_data(self):
        self.listWidget.clear()
        self.loadPortfolio()
        self.quickAccessList.clear()
        self.loadQuickAccessAndCompanySearch()
        self.update_company_info_panel()

        #set our "last updated" label to our new delta
        self.lastUpdatedLabel.setText("Last updated: " + datetime.now().strftime('%I:%M %p '))

    """
    Clear the trade section when no company selected
    """
    def trade_update(self):
        self.listWidget.clear()
        self.loadPortfolio()
        self.company_selected = None
        self.trade_frame.hide()
        self.tradeErrorLabel.clear()

        self.companyLabel.setText("No Company Selected")
        self.companyFullNameLabel.clear()
        self.priceLabel.clear()
        self.numSharesOwnedLabel.clear()

    """
    Accepts a string, searches for a company and populates a new listWidgetItem if search is a success
    """
    def on_search(self):
        self.searchList.clear()
        text = self.searchBar.text()
        symbol = Utils.symbol_from_name(text)

        if text.upper() in Companies.get_available_symbols():
            self.searchList.clear()
            self.searchedWid = ui_company_listing.CompanyListing(self)
            stock = Companies.get_stock(text)
            self.searchedWid.populate(stock, text.upper())
            self.searchedSymbol = text
        elif symbol is not None:            
            self.searchList.clear()
            self.searchedWid = ui_company_listing.CompanyListing(self)
            stock = Companies.get_stock(symbol)
            self.searchedWid.populate(stock, symbol)
            self.searchedSymbol = text
        else:
            self.searchList.clear()
            item = QListWidgetItem()
            item.setText("Company " + text + " not found.")
            self.searchList.addItem(item)
            self.searchedSymbol = None
            return
        self.searchedItem = QListWidgetItem()
        self.searchedItem.setSizeHint(QtCore.QSize(100, 100))

        self.searchList.addItem(self.searchedItem)
        self.searchList.setItemWidget(self.searchedItem, self.searchedWid)
        self.searchList.update()
    
    """
    Select a tile and remove from quick access list widget. Triggered by the X button on the screen
    """
    def on_remove_quick_access(self, event):
        item = self.quickAccessList.currentItem()
        if item is not None:
            symbol = self.quickAccessList.itemWidget(item).companyLabel.text()
            print(symbol)
            pf.quick_access_companies.remove(symbol)
            db.remove_user_quick_access(pf.username, symbol)
            self.quickAccessList.takeItem(self.quickAccessList.row(item))

    """
    Takes the searched-for widget and adds it to the Quick Access widget list. Triggered by the arrow button on the screen.
    """
    def on_add_to_quick_access(self, event):
        if self.searchList.count() != 1:
            return
        symbol = self.searchedSymbol
        if not isinstance(symbol, str):
            return
        if symbol in pf.quick_access_companies:
            QMessageBox.about(self, "Error", "This symbol is already in your Quick Access list.")
            return
        if pf.add_to_quick_access(symbol, to_beginning=True):
            db.insert_user_quick_access(pf.username, symbol)
            self.loadQuickAccessAndCompanySearch()
            
    """
    Triggered by the trade button, sends field data to the portfolio trade functions for checking and processing
    """
    def on_confirm_trade(self):
        if self.company_selected is not None:
            buy_or_sell = str(self.tradeCombo.currentText())
            try:
                quantity = int(self.numToTrade.text())
            except:
                self.tradeErrorLabel.setText("Shares field must contain an integer.")
                return False

            if buy_or_sell == "Buy":
                status, error = pf.buy(self.companyLabel.text(), self.numToTrade.text())
                if status:
                    QMessageBox.about(self, "Success", "Trade was successful!")
                    self.trade_update()
                else:
                    self.tradeErrorLabel.setText(error)
                    return False
            if buy_or_sell == "Sell":
                status, error = pf.sell(self.companyLabel.text(), self.numToTrade.text())
                if status:
                    QMessageBox.about(self, "Success", "Trade was successful!")
                    self.trade_update()
                else:
                    self.tradeErrorLabel.setText(error)
                    return False
            return True
    
    """

    This section is for loading widgets and sections of the UI

    """


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
        pf.total_value = pf.calculate_total_value()
        db.update_total_value(pf.username, pf.total_value)
        
    def loadPortfolio(self):
        self.loggedInAsUser.setText(pf.username)
        self.currentBalance.setText("$" + str("{:,}".format(round(pf.num_credits, 2))))
        db.update_credit(pf.username, pf.num_credits)
        self.loadTotalValue()

        for symbol, num_stock in pf.owned_stocks.items():
            stock = Companies.get_stock(symbol)
            wid = ui_portfolioTile.PortfolioTile(self)
            wid.populate(stock, num_stock)
            wid2 = QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(300, 75))
            self.listWidget.addItem(wid2)
            self.listWidget.setItemWidget(wid2, wid)
            stocklist = db.find_stock_of_user(pf.username)
            check = False
            for i in stocklist:
                if symbol == i[1]:
                    check = True
                    db.update_stock(pf.username, symbol, num_stock)
            if check == False:
                db.insert_stock(pf.username, symbol, num_stock)
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
        db.update_credit(pf.username, pf.num_credits)
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
        newPassword = self.ui.newPasswordEdit.text()
        confirmnewPassword = self.ui.confirmNewPasswordEdit.text()
        changePassword = PasswordChange(pf.username, newPassword, \
                                confirmnewPassword)
        valid, message = changePassword.isValidPassword()
        if not valid:
            QMessageBox.about(self, "Error", message + "       ")
        else:
            db.update_password(pf.username, newPassword)
            QMessageBox.about(self, "Success", message + "       ")

    def confirm_reset_account(self):
        self.ui = uic.loadUi('UI/confirm_reset_account.ui')
        self.ui.setModal(True)
        self.ui.AcceptButton.clicked.connect(self.perform_reset_account)
        #update_credit()
        self.ui.show()
        self.ui.exec_()

    def perform_reset_account(self):
        db.rm_reset_user(pf.username)
        db.insert_UP(pf.username)
        pf.reset()
        self.refresh_ui_data()

    def not_admin(self):
        self.ui = uic.loadUi('UI/not_admin_warning.ui')
        self.ui.setModal(True)
        self.ui.show()
        self.ui.exec_()

    def delete_user(self):
        self.ui = uic.loadUi('UI/delete_user_panel.ui')
        self.ui.setModal(True)
        self.ui.AcceptDeleteButton.clicked.connect(self.perform_delete_user)
        self.ui.show()
        self.ui.exec_()

    def perform_delete_user(self):
        username_email = str(self.ui.username_emailEdit.text())
        checkuser = db.check_user(username_email)
        checkemail = db.check_email(username_email)
        for i in checkemail:
            print("")
        if checkuser:
            db.delete_user(username_email)
        elif checkemail:
                db.delete_user(i[0])
        else:
            message = "Invalid Username or Email Address"
            QMessageBox.about(self, "Error", message + "       ")
            

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
        mainApp = MainApp()
        mainApp.setWindowIcon(QtGui.QIcon('res/icon.png'))
        mainApp.show()
        
        #try:
        Companies.update_company_information()
        #except:
        #QMessageBox.about(mainApp, "No Connection", "You must be connected to the Internet in order to get accurate data.")
        
        #This will continuously pull from the API and push all the data into the cache
        updater = UpdaterThread.UpdaterThread(1, "updater")
        updater.daemon = True
        updater.start()

        ret = app.exec_()
        sys.exit(ret)
