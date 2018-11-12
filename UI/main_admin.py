/********************************************************************************
** Form generated from reading UI file 'main_admin.ui'
**
** Created by: Qt User Interface Compiler version 5.9.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAIN_ADMIN_H
#define MAIN_ADMIN_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionAdjust_Credits;
    QAction *actionChange_Password;
    QAction *actionExit;
    QAction *actionReset_Account;
    QAction *actionDelete_User;
    QAction *actionDelete_User_by_Email;
    QAction *actionSend_Message_to_UserEmail;
    QWidget *centralwidget;
    QGridLayout *gridLayout_2;
    QFrame *frame;
    QWidget *verticalLayoutWidget_4;
    QVBoxLayout *verticalLayout_8;
    QGridLayout *gridLayout_9;
    QLineEdit *searchBar;
    QPushButton *searchButton;
    QListWidget *searchList;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QLabel *label_5;
    QLabel *sendToQuickAccessButton;
    QListWidget *quickAccessList;
    QFrame *frame_2;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout_5;
    QGridLayout *gridLayout;
    QLabel *loggedInAsUser;
    QLabel *label_3;
    QLabel *currentBalance;
    QLabel *stockBalanceLabel_2;
    QLabel *totalValueLabel;
    QLabel *totalValue;
    QLabel *label_2;
    QPushButton *refreshButton;
    QListWidget *listWidget;
    QWidget *companyInfoWidget;
    QPushButton *pushButton;
    QStatusBar *statusbar;
    QMenuBar *menuBar;
    QMenu *menuMenu;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1251, 839);
        QPalette palette;
        QBrush brush(QColor(255, 255, 255, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::AlternateBase, brush);
        palette.setBrush(QPalette::Inactive, QPalette::AlternateBase, brush);
        palette.setBrush(QPalette::Disabled, QPalette::AlternateBase, brush);
        MainWindow->setPalette(palette);
        actionAdjust_Credits = new QAction(MainWindow);
        actionAdjust_Credits->setObjectName(QStringLiteral("actionAdjust_Credits"));
        actionChange_Password = new QAction(MainWindow);
        actionChange_Password->setObjectName(QStringLiteral("actionChange_Password"));
        actionExit = new QAction(MainWindow);
        actionExit->setObjectName(QStringLiteral("actionExit"));
        actionReset_Account = new QAction(MainWindow);
        actionReset_Account->setObjectName(QStringLiteral("actionReset_Account"));
        actionDelete_User = new QAction(MainWindow);
        actionDelete_User->setObjectName(QStringLiteral("actionDelete_User"));
        actionDelete_User_by_Email = new QAction(MainWindow);
        actionDelete_User_by_Email->setObjectName(QStringLiteral("actionDelete_User_by_Email"));
        actionSend_Message_to_UserEmail = new QAction(MainWindow);
        actionSend_Message_to_UserEmail->setObjectName(QStringLiteral("actionSend_Message_to_UserEmail"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(100);
        sizePolicy.setHeightForWidth(centralwidget->sizePolicy().hasHeightForWidth());
        centralwidget->setSizePolicy(sizePolicy);
        gridLayout_2 = new QGridLayout(centralwidget);
        gridLayout_2->setSpacing(5);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout_2->setContentsMargins(10, 10, 10, 10);
        frame = new QFrame(centralwidget);
        frame->setObjectName(QStringLiteral("frame"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(frame->sizePolicy().hasHeightForWidth());
        frame->setSizePolicy(sizePolicy1);
        frame->setMinimumSize(QSize(410, 600));
        frame->setMaximumSize(QSize(410, 800));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayoutWidget_4 = new QWidget(frame);
        verticalLayoutWidget_4->setObjectName(QStringLiteral("verticalLayoutWidget_4"));
        verticalLayoutWidget_4->setGeometry(QRect(0, 0, 410, 801));
        verticalLayout_8 = new QVBoxLayout(verticalLayoutWidget_4);
        verticalLayout_8->setSpacing(5);
        verticalLayout_8->setObjectName(QStringLiteral("verticalLayout_8"));
        verticalLayout_8->setContentsMargins(5, 5, 5, 5);
        gridLayout_9 = new QGridLayout();
        gridLayout_9->setSpacing(5);
        gridLayout_9->setObjectName(QStringLiteral("gridLayout_9"));
        gridLayout_9->setContentsMargins(0, 5, 0, 5);
        searchBar = new QLineEdit(verticalLayoutWidget_4);
        searchBar->setObjectName(QStringLiteral("searchBar"));
        searchBar->setMaximumSize(QSize(16777215, 16777215));
        QFont font;
        font.setPointSize(14);
        searchBar->setFont(font);

        gridLayout_9->addWidget(searchBar, 0, 0, 1, 1);

        searchButton = new QPushButton(verticalLayoutWidget_4);
        searchButton->setObjectName(QStringLiteral("searchButton"));
        searchButton->setMaximumSize(QSize(16777215, 16777215));

        gridLayout_9->addWidget(searchButton, 0, 1, 1, 1);


        verticalLayout_8->addLayout(gridLayout_9);

        searchList = new QListWidget(verticalLayoutWidget_4);
        searchList->setObjectName(QStringLiteral("searchList"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Maximum);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(searchList->sizePolicy().hasHeightForWidth());
        searchList->setSizePolicy(sizePolicy2);
        searchList->setMinimumSize(QSize(0, 85));
        searchList->setMaximumSize(QSize(16777215, 85));
        QPalette palette1;
        QBrush brush1(QColor(247, 247, 247, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette1.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        QBrush brush2(QColor(240, 240, 240, 255));
        brush2.setStyle(Qt::SolidPattern);
        palette1.setBrush(QPalette::Disabled, QPalette::Base, brush2);
        searchList->setPalette(palette1);

        verticalLayout_8->addWidget(searchList);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(5);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(5, 5, 5, 5);
        label = new QLabel(verticalLayoutWidget_4);
        label->setObjectName(QStringLiteral("label"));
        label->setFont(font);

        horizontalLayout_2->addWidget(label);

        label_5 = new QLabel(verticalLayoutWidget_4);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout_2->addWidget(label_5);

        sendToQuickAccessButton = new QLabel(verticalLayoutWidget_4);
        sendToQuickAccessButton->setObjectName(QStringLiteral("sendToQuickAccessButton"));
        sendToQuickAccessButton->setMaximumSize(QSize(20, 16777215));
        QFont font1;
        font1.setFamily(QStringLiteral("Calibri"));
        font1.setPointSize(16);
        font1.setBold(true);
        font1.setWeight(75);
        sendToQuickAccessButton->setFont(font1);
        sendToQuickAccessButton->setStyleSheet(QStringLiteral("background-color: rgb(221, 214, 210);"));
        sendToQuickAccessButton->setAlignment(Qt::AlignCenter);

        horizontalLayout_2->addWidget(sendToQuickAccessButton);


        verticalLayout_8->addLayout(horizontalLayout_2);

        quickAccessList = new QListWidget(verticalLayoutWidget_4);
        quickAccessList->setObjectName(QStringLiteral("quickAccessList"));
        QSizePolicy sizePolicy3(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(quickAccessList->sizePolicy().hasHeightForWidth());
        quickAccessList->setSizePolicy(sizePolicy3);
        quickAccessList->setMinimumSize(QSize(0, 0));
        QPalette palette2;
        palette2.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette2.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette2.setBrush(QPalette::Disabled, QPalette::Base, brush2);
        quickAccessList->setPalette(palette2);
        quickAccessList->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
        quickAccessList->setAutoScroll(true);
        quickAccessList->setEditTriggers(QAbstractItemView::DoubleClicked|QAbstractItemView::EditKeyPressed);
        quickAccessList->setProperty("showDropIndicator", QVariant(true));
        quickAccessList->setDragEnabled(false);
        quickAccessList->setDragDropOverwriteMode(false);
        quickAccessList->setDragDropMode(QAbstractItemView::NoDragDrop);
        quickAccessList->setDefaultDropAction(Qt::CopyAction);
        quickAccessList->setAlternatingRowColors(true);
        quickAccessList->setVerticalScrollMode(QAbstractItemView::ScrollPerPixel);
        quickAccessList->setMovement(QListView::Static);
        quickAccessList->setResizeMode(QListView::Adjust);

        verticalLayout_8->addWidget(quickAccessList);


        gridLayout_2->addWidget(frame, 0, 2, 2, 1);

        frame_2 = new QFrame(centralwidget);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        sizePolicy1.setHeightForWidth(frame_2->sizePolicy().hasHeightForWidth());
        frame_2->setSizePolicy(sizePolicy1);
        frame_2->setMinimumSize(QSize(310, 600));
        frame_2->setMaximumSize(QSize(310, 800));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        verticalLayoutWidget = new QWidget(frame_2);
        verticalLayoutWidget->setObjectName(QStringLiteral("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(0, 0, 311, 801));
        verticalLayout_5 = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout_5->setSpacing(5);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        verticalLayout_5->setContentsMargins(5, 5, 5, 5);
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(10, 10, 10, 10);
        loggedInAsUser = new QLabel(verticalLayoutWidget);
        loggedInAsUser->setObjectName(QStringLiteral("loggedInAsUser"));
        QFont font2;
        font2.setPointSize(12);
        loggedInAsUser->setFont(font2);

        gridLayout->addWidget(loggedInAsUser, 1, 1, 1, 1);

        label_3 = new QLabel(verticalLayoutWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setFont(font2);

        gridLayout->addWidget(label_3, 1, 0, 1, 1);

        currentBalance = new QLabel(verticalLayoutWidget);
        currentBalance->setObjectName(QStringLiteral("currentBalance"));
        currentBalance->setFont(font2);

        gridLayout->addWidget(currentBalance, 5, 1, 1, 1);

        stockBalanceLabel_2 = new QLabel(verticalLayoutWidget);
        stockBalanceLabel_2->setObjectName(QStringLiteral("stockBalanceLabel_2"));
        stockBalanceLabel_2->setFont(font2);

        gridLayout->addWidget(stockBalanceLabel_2, 5, 0, 1, 1);

        totalValueLabel = new QLabel(verticalLayoutWidget);
        totalValueLabel->setObjectName(QStringLiteral("totalValueLabel"));
        totalValueLabel->setFont(font2);

        gridLayout->addWidget(totalValueLabel, 2, 0, 1, 1);

        totalValue = new QLabel(verticalLayoutWidget);
        totalValue->setObjectName(QStringLiteral("totalValue"));
        totalValue->setFont(font2);

        gridLayout->addWidget(totalValue, 2, 1, 1, 1);

        label_2 = new QLabel(verticalLayoutWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        QFont font3;
        font3.setPointSize(14);
        font3.setBold(true);
        font3.setWeight(75);
        label_2->setFont(font3);

        gridLayout->addWidget(label_2, 0, 0, 1, 1);

        refreshButton = new QPushButton(verticalLayoutWidget);
        refreshButton->setObjectName(QStringLiteral("refreshButton"));

        gridLayout->addWidget(refreshButton, 6, 1, 1, 1);


        verticalLayout_5->addLayout(gridLayout);

        listWidget = new QListWidget(verticalLayoutWidget);
        listWidget->setObjectName(QStringLiteral("listWidget"));
        QSizePolicy sizePolicy4(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(100);
        sizePolicy4.setHeightForWidth(listWidget->sizePolicy().hasHeightForWidth());
        listWidget->setSizePolicy(sizePolicy4);
        listWidget->setMinimumSize(QSize(0, 0));
        listWidget->setMaximumSize(QSize(16777215, 16777215));
        QPalette palette3;
        palette3.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::Base, brush2);
        listWidget->setPalette(palette3);
        listWidget->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
        listWidget->setAlternatingRowColors(true);
        listWidget->setVerticalScrollMode(QAbstractItemView::ScrollPerPixel);
        listWidget->setResizeMode(QListView::Adjust);

        verticalLayout_5->addWidget(listWidget);


        gridLayout_2->addWidget(frame_2, 0, 1, 2, 1);

        companyInfoWidget = new QWidget(centralwidget);
        companyInfoWidget->setObjectName(QStringLiteral("companyInfoWidget"));
        sizePolicy3.setHeightForWidth(companyInfoWidget->sizePolicy().hasHeightForWidth());
        companyInfoWidget->setSizePolicy(sizePolicy3);
        companyInfoWidget->setMinimumSize(QSize(400, 400));
        companyInfoWidget->setMaximumSize(QSize(800, 600));

        gridLayout_2->addWidget(companyInfoWidget, 0, 4, 1, 1);

        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));

        gridLayout_2->addWidget(pushButton, 1, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1251, 21));
        menuMenu = new QMenu(menuBar);
        menuMenu->setObjectName(QStringLiteral("menuMenu"));
        MainWindow->setMenuBar(menuBar);

        menuBar->addAction(menuMenu->menuAction());
        menuMenu->addAction(actionAdjust_Credits);
        menuMenu->addAction(actionChange_Password);
        menuMenu->addAction(actionReset_Account);
        menuMenu->addSeparator();
        menuMenu->addAction(actionDelete_User);
        menuMenu->addAction(actionSend_Message_to_UserEmail);
        menuMenu->addAction(actionExit);

        retranslateUi(MainWindow);
        QObject::connect(searchBar, SIGNAL(returnPressed()), searchButton, SLOT(click()));
        QObject::connect(searchButton, SIGNAL(clicked()), searchList, SLOT(reset()));
        QObject::connect(listWidget, SIGNAL(itemClicked(QListWidgetItem*)), listWidget, SLOT(doItemsLayout()));
        QObject::connect(actionExit, SIGNAL(triggered()), MainWindow, SLOT(close()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        actionAdjust_Credits->setText(QApplication::translate("MainWindow", "Adjust Credits", Q_NULLPTR));
        actionChange_Password->setText(QApplication::translate("MainWindow", "Change Password", Q_NULLPTR));
        actionExit->setText(QApplication::translate("MainWindow", "Exit", Q_NULLPTR));
        actionReset_Account->setText(QApplication::translate("MainWindow", "Reset Account", Q_NULLPTR));
        actionDelete_User->setText(QApplication::translate("MainWindow", "Delete User", Q_NULLPTR));
        actionDelete_User_by_Email->setText(QApplication::translate("MainWindow", "Delete User by Email", Q_NULLPTR));
        actionSend_Message_to_UserEmail->setText(QApplication::translate("MainWindow", "Send Message to User Email", Q_NULLPTR));
        searchBar->setPlaceholderText(QApplication::translate("MainWindow", "Search Symbols", Q_NULLPTR));
        searchButton->setText(QApplication::translate("MainWindow", "Search", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "Quick Access", Q_NULLPTR));
        label_5->setText(QApplication::translate("MainWindow", "Add to Quick Access", Q_NULLPTR));
        sendToQuickAccessButton->setText(QApplication::translate("MainWindow", "<p> &darr; </p>", Q_NULLPTR));
        loggedInAsUser->setText(QApplication::translate("MainWindow", "-", Q_NULLPTR));
        label_3->setText(QApplication::translate("MainWindow", "Logged in as:", Q_NULLPTR));
        currentBalance->setText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        stockBalanceLabel_2->setText(QApplication::translate("MainWindow", "StockFlip Credits:", Q_NULLPTR));
        totalValueLabel->setText(QApplication::translate("MainWindow", "Total Value:", Q_NULLPTR));
        totalValue->setText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        label_2->setText(QApplication::translate("MainWindow", "Portfolio", Q_NULLPTR));
        refreshButton->setText(QApplication::translate("MainWindow", "Refresh", Q_NULLPTR));
        pushButton->setText(QApplication::translate("MainWindow", "PushButton", Q_NULLPTR));
        menuMenu->setTitle(QApplication::translate("MainWindow", "Menu", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAIN_ADMIN_H
