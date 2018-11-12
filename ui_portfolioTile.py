from PyQt5 import QtCore, QtGui, QtWidgets

class PortfolioTile(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(PortfolioTile, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(310, 40)
        self.setMinimumSize(QtCore.QSize(300, 40))
        self.setMaximumSize(QtCore.QSize(310, 75))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.companyLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.companyLabel.setFont(font)
        self.companyLabel.setObjectName("CompanyLabel")
        self.horizontalLayout.addWidget(self.companyLabel)
        self.priceLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.horizontalLayout.addWidget(self.priceLabel)
        self.percentChangeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.percentChangeLabel.setObjectName("percentChangeLabel")
        self.horizontalLayout.addWidget(self.percentChangeLabel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 310, 40))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ownedStockLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ownedStockLabel.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.ownedStockLabel)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
   

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
      

    def populate(self, stock, num_owned):
        self.priceLabel.setText(str(stock["latestPrice"]))
        self.companyLabel.setText(str(stock["symbol"]))
        self.ownedStockLabel.setText("Shares owned: "+ str(num_owned))
        change_perc = stock["changePercent"]*100
        if change_perc < 0:
            color = "red"
        else:
            color = "green"
        change_perc = str(round(change_perc, 2))
        self.percentChangeLabel.setText("<font color="+color+">"+change_perc+"%</font>")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.companyLabel.setText(_translate("Form", "AAPL"))
        self.priceLabel.setText(_translate("Form", "$205.00"))
        self.percentChangeLabel.setText(_translate("Form", "+2.05%"))
        self.ownedStockLabel.setText(_translate("Form", "Shares Owned: 1500"))

