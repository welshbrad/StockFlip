/********************************************************************************
** Form generated from reading UI file 'main.ui'
**
** Created by: Qt User Interface Compiler version 5.9.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAIN_ADMIN_H
#define MAIN_ADMIN_H

#include <QtCore/QVariant>
#include <QtWebEngineWidgets/QWebEngineView>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
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
#include <QtWidgets/QSpacerItem>
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
    QAction *actionMessage_User;
    QWidget *centralwidget;
    QGridLayout *gridLayout_2;
    QSpacerItem *horizontalSpacer;
    QFrame *frame_2;
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout_5;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_9;
    QLabel *lastUpdatedLabel;
    QPushButton *refreshButton;
    QFrame *line_3;
    QGridLayout *gridLayout;
    QLabel *label_3;
    QLabel *currentBalance;
    QLabel *stockBalanceLabel_2;
    QLabel *loggedInAsUser;
    QLabel *totalValueLabel;
    QLabel *totalValue;
    QListWidget *listWidget;
    QLabel *label_6;
    QFrame *line_2;
    QVBoxLayout *verticalLayout_4;
    QLabel *companyLabel;
    QLabel *companyFullNameLabel;
    QLabel *priceLabel;
    QLabel *numSharesOwnedLabel;
    QFrame *line_4;
    QFrame *trade_frame;
    QHBoxLayout *horizontalLayout_6;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout_3;
    QLabel *label_4;
    QLabel *label_7;
    QLabel *label_8;
    QVBoxLayout *verticalLayout_6;
    QComboBox *tradeCombo;
    QLineEdit *numToTrade;
    QLabel *totalPriceLabel;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *confirmButton;
    QLabel *tradeErrorLabel;
    QFrame *frame;
    QVBoxLayout *verticalLayout;
    QVBoxLayout *verticalLayout_8;
    QGridLayout *gridLayout_9;
    QLineEdit *searchBar;
    QPushButton *searchButton;
    QListWidget *searchList;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QLabel *label_5;
    QPushButton *sendToQuickAccessButton;
    QPushButton *removeFromQuickAccessButton;
    QListWidget *quickAccessList;
    QFrame *company_info_panel;
    QVBoxLayout *verticalLayout_7;
    QVBoxLayout *verticalLayout_9;
    QLabel *company_info_symbol_label;
    QLabel *company_info_name_label;
    QGridLayout *gridLayout_3;
    QLabel *label_21;
    QLabel *label_22;
    QLabel *label_16;
    QLabel *label_20;
    QLabel *label_12;
    QLabel *label_11;
    QLabel *label_23;
    QLabel *label_10;
    QLabel *label_17;
    QLabel *label_18;
    QLabel *label_19;
    QLabel *label_15;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_2;
    QLabel *label_24;
    QLabel *label_25;
    QLabel *label_26;
    QLabel *label_27;
    QLabel *label_28;
    QWebEngineView *webEngineView;
    QSpacerItem *verticalSpacer;
    QStatusBar *statusbar;
    QMenuBar *menuBar;
    QMenu *menuMenu;
    QMenu *menuAdmin_Menu;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1193, 754);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
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
        actionMessage_User = new QAction(MainWindow);
        actionMessage_User->setObjectName(QStringLiteral("actionMessage_User"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(centralwidget->sizePolicy().hasHeightForWidth());
        centralwidget->setSizePolicy(sizePolicy1);
        centralwidget->setMaximumSize(QSize(16777215, 16777215));
        gridLayout_2 = new QGridLayout(centralwidget);
        gridLayout_2->setSpacing(5);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout_2->setContentsMargins(10, 10, 10, 10);
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 0, 4, 1, 1);

        frame_2 = new QFrame(centralwidget);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        sizePolicy.setHeightForWidth(frame_2->sizePolicy().hasHeightForWidth());
        frame_2->setSizePolicy(sizePolicy);
        frame_2->setMinimumSize(QSize(350, 0));
        frame_2->setMaximumSize(QSize(350, 16777215));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(frame_2);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setSpacing(5);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        verticalLayout_5->setContentsMargins(3, 3, 3, 3);
        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        label_9 = new QLabel(frame_2);
        label_9->setObjectName(QStringLiteral("label_9"));
        QFont font;
        font.setPointSize(16);
        font.setBold(false);
        font.setWeight(50);
        label_9->setFont(font);

        horizontalLayout_5->addWidget(label_9);

        lastUpdatedLabel = new QLabel(frame_2);
        lastUpdatedLabel->setObjectName(QStringLiteral("lastUpdatedLabel"));
        lastUpdatedLabel->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout_5->addWidget(lastUpdatedLabel);

        refreshButton = new QPushButton(frame_2);
        refreshButton->setObjectName(QStringLiteral("refreshButton"));
        refreshButton->setMaximumSize(QSize(25, 25));
        QIcon icon;
        icon.addFile(QStringLiteral("../res/refresh.png"), QSize(), QIcon::Normal, QIcon::Off);
        refreshButton->setIcon(icon);

        horizontalLayout_5->addWidget(refreshButton);


        verticalLayout_5->addLayout(horizontalLayout_5);

        line_3 = new QFrame(frame_2);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);

        verticalLayout_5->addWidget(line_3);

        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setHorizontalSpacing(0);
        gridLayout->setVerticalSpacing(6);
        gridLayout->setContentsMargins(0, 0, 0, 0);
        label_3 = new QLabel(frame_2);
        label_3->setObjectName(QStringLiteral("label_3"));
        QFont font1;
        font1.setPointSize(12);
        label_3->setFont(font1);

        gridLayout->addWidget(label_3, 1, 0, 1, 1);

        currentBalance = new QLabel(frame_2);
        currentBalance->setObjectName(QStringLiteral("currentBalance"));
        currentBalance->setFont(font1);

        gridLayout->addWidget(currentBalance, 5, 1, 1, 1);

        stockBalanceLabel_2 = new QLabel(frame_2);
        stockBalanceLabel_2->setObjectName(QStringLiteral("stockBalanceLabel_2"));
        stockBalanceLabel_2->setFont(font1);

        gridLayout->addWidget(stockBalanceLabel_2, 5, 0, 1, 1);

        loggedInAsUser = new QLabel(frame_2);
        loggedInAsUser->setObjectName(QStringLiteral("loggedInAsUser"));
        loggedInAsUser->setFont(font1);

        gridLayout->addWidget(loggedInAsUser, 1, 1, 1, 1);

        totalValueLabel = new QLabel(frame_2);
        totalValueLabel->setObjectName(QStringLiteral("totalValueLabel"));
        totalValueLabel->setFont(font1);

        gridLayout->addWidget(totalValueLabel, 2, 0, 1, 1);

        totalValue = new QLabel(frame_2);
        totalValue->setObjectName(QStringLiteral("totalValue"));
        totalValue->setFont(font1);

        gridLayout->addWidget(totalValue, 2, 1, 1, 1);


        verticalLayout_5->addLayout(gridLayout);

        listWidget = new QListWidget(frame_2);
        listWidget->setObjectName(QStringLiteral("listWidget"));
        sizePolicy.setHeightForWidth(listWidget->sizePolicy().hasHeightForWidth());
        listWidget->setSizePolicy(sizePolicy);
        listWidget->setMinimumSize(QSize(0, 100));
        listWidget->setMaximumSize(QSize(16777215, 16777215));
        QPalette palette1;
        QBrush brush1(QColor(247, 247, 247, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette1.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette1.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        QBrush brush2(QColor(240, 240, 240, 255));
        brush2.setStyle(Qt::SolidPattern);
        palette1.setBrush(QPalette::Disabled, QPalette::Base, brush2);
        listWidget->setPalette(palette1);
        listWidget->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
        listWidget->setAlternatingRowColors(true);
        listWidget->setVerticalScrollMode(QAbstractItemView::ScrollPerPixel);
        listWidget->setResizeMode(QListView::Adjust);

        verticalLayout_5->addWidget(listWidget);

        label_6 = new QLabel(frame_2);
        label_6->setObjectName(QStringLiteral("label_6"));
        QFont font2;
        font2.setPointSize(16);
        font2.setItalic(false);
        font2.setUnderline(false);
        font2.setKerning(true);
        label_6->setFont(font2);

        verticalLayout_5->addWidget(label_6);

        line_2 = new QFrame(frame_2);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        verticalLayout_5->addWidget(line_2);

        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setSpacing(3);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(0, 3, 0, 3);
        companyLabel = new QLabel(frame_2);
        companyLabel->setObjectName(QStringLiteral("companyLabel"));
        QFont font3;
        font3.setPointSize(14);
        font3.setBold(true);
        font3.setWeight(75);
        companyLabel->setFont(font3);

        verticalLayout_4->addWidget(companyLabel);

        companyFullNameLabel = new QLabel(frame_2);
        companyFullNameLabel->setObjectName(QStringLiteral("companyFullNameLabel"));
        companyFullNameLabel->setFont(font1);

        verticalLayout_4->addWidget(companyFullNameLabel);

        priceLabel = new QLabel(frame_2);
        priceLabel->setObjectName(QStringLiteral("priceLabel"));
        priceLabel->setFont(font1);

        verticalLayout_4->addWidget(priceLabel);

        numSharesOwnedLabel = new QLabel(frame_2);
        numSharesOwnedLabel->setObjectName(QStringLiteral("numSharesOwnedLabel"));
        numSharesOwnedLabel->setFont(font1);

        verticalLayout_4->addWidget(numSharesOwnedLabel);

        line_4 = new QFrame(frame_2);
        line_4->setObjectName(QStringLiteral("line_4"));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);

        verticalLayout_4->addWidget(line_4);

        trade_frame = new QFrame(frame_2);
        trade_frame->setObjectName(QStringLiteral("trade_frame"));
        trade_frame->setMinimumSize(QSize(0, 100));
        trade_frame->setFrameShape(QFrame::StyledPanel);
        trade_frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_6 = new QHBoxLayout(trade_frame);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        label_4 = new QLabel(trade_frame);
        label_4->setObjectName(QStringLiteral("label_4"));
        QFont font4;
        font4.setPointSize(14);
        label_4->setFont(font4);
        label_4->setLayoutDirection(Qt::RightToLeft);

        verticalLayout_3->addWidget(label_4);

        label_7 = new QLabel(trade_frame);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setFont(font4);
        label_7->setLayoutDirection(Qt::RightToLeft);

        verticalLayout_3->addWidget(label_7);

        label_8 = new QLabel(trade_frame);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setFont(font4);
        label_8->setLayoutDirection(Qt::RightToLeft);

        verticalLayout_3->addWidget(label_8);


        horizontalLayout->addLayout(verticalLayout_3);

        verticalLayout_6 = new QVBoxLayout();
        verticalLayout_6->setObjectName(QStringLiteral("verticalLayout_6"));
        tradeCombo = new QComboBox(trade_frame);
        tradeCombo->setObjectName(QStringLiteral("tradeCombo"));
        QSizePolicy sizePolicy2(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(tradeCombo->sizePolicy().hasHeightForWidth());
        tradeCombo->setSizePolicy(sizePolicy2);
        tradeCombo->setMinimumSize(QSize(0, 30));
        tradeCombo->setMaximumSize(QSize(100, 30));
        tradeCombo->setFont(font4);
        tradeCombo->setLayoutDirection(Qt::LeftToRight);

        verticalLayout_6->addWidget(tradeCombo);

        numToTrade = new QLineEdit(trade_frame);
        numToTrade->setObjectName(QStringLiteral("numToTrade"));
        numToTrade->setMaximumSize(QSize(100, 16777215));
        numToTrade->setFont(font4);
        numToTrade->setInputMethodHints(Qt::ImhDigitsOnly);

        verticalLayout_6->addWidget(numToTrade);

        totalPriceLabel = new QLabel(trade_frame);
        totalPriceLabel->setObjectName(QStringLiteral("totalPriceLabel"));
        totalPriceLabel->setFont(font4);

        verticalLayout_6->addWidget(totalPriceLabel);


        horizontalLayout->addLayout(verticalLayout_6);


        horizontalLayout_6->addLayout(horizontalLayout);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_2);

        confirmButton = new QPushButton(trade_frame);
        confirmButton->setObjectName(QStringLiteral("confirmButton"));
        QSizePolicy sizePolicy3(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(confirmButton->sizePolicy().hasHeightForWidth());
        confirmButton->setSizePolicy(sizePolicy3);
        confirmButton->setMinimumSize(QSize(50, 50));
        confirmButton->setMaximumSize(QSize(50, 50));
        confirmButton->setLayoutDirection(Qt::RightToLeft);

        horizontalLayout_6->addWidget(confirmButton);


        verticalLayout_4->addWidget(trade_frame);

        tradeErrorLabel = new QLabel(frame_2);
        tradeErrorLabel->setObjectName(QStringLiteral("tradeErrorLabel"));
        QPalette palette2;
        QBrush brush3(QColor(175, 19, 19, 255));
        brush3.setStyle(Qt::SolidPattern);
        palette2.setBrush(QPalette::Active, QPalette::WindowText, brush3);
        QBrush brush4(QColor(158, 11, 11, 255));
        brush4.setStyle(Qt::SolidPattern);
        palette2.setBrush(QPalette::Active, QPalette::Text, brush4);
        palette2.setBrush(QPalette::Inactive, QPalette::WindowText, brush3);
        palette2.setBrush(QPalette::Inactive, QPalette::Text, brush4);
        QBrush brush5(QColor(120, 120, 120, 255));
        brush5.setStyle(Qt::SolidPattern);
        palette2.setBrush(QPalette::Disabled, QPalette::WindowText, brush5);
        palette2.setBrush(QPalette::Disabled, QPalette::Text, brush5);
        tradeErrorLabel->setPalette(palette2);
        QFont font5;
        font5.setPointSize(10);
        tradeErrorLabel->setFont(font5);

        verticalLayout_4->addWidget(tradeErrorLabel);


        verticalLayout_5->addLayout(verticalLayout_4);


        verticalLayout_2->addLayout(verticalLayout_5);


        gridLayout_2->addWidget(frame_2, 0, 0, 2, 1);

        frame = new QFrame(centralwidget);
        frame->setObjectName(QStringLiteral("frame"));
        sizePolicy.setHeightForWidth(frame->sizePolicy().hasHeightForWidth());
        frame->setSizePolicy(sizePolicy);
        frame->setMinimumSize(QSize(450, 0));
        frame->setMaximumSize(QSize(50, 16777215));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(frame);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout_8 = new QVBoxLayout();
        verticalLayout_8->setSpacing(5);
        verticalLayout_8->setObjectName(QStringLiteral("verticalLayout_8"));
        verticalLayout_8->setSizeConstraint(QLayout::SetDefaultConstraint);
        verticalLayout_8->setContentsMargins(3, 3, 3, 3);
        gridLayout_9 = new QGridLayout();
        gridLayout_9->setSpacing(5);
        gridLayout_9->setObjectName(QStringLiteral("gridLayout_9"));
        gridLayout_9->setContentsMargins(0, 5, 0, 5);
        searchBar = new QLineEdit(frame);
        searchBar->setObjectName(QStringLiteral("searchBar"));
        searchBar->setMaximumSize(QSize(16777215, 16777215));
        searchBar->setFont(font4);

        gridLayout_9->addWidget(searchBar, 0, 0, 1, 1);

        searchButton = new QPushButton(frame);
        searchButton->setObjectName(QStringLiteral("searchButton"));
        searchButton->setMaximumSize(QSize(16777215, 16777215));

        gridLayout_9->addWidget(searchButton, 0, 1, 1, 1);


        verticalLayout_8->addLayout(gridLayout_9);

        searchList = new QListWidget(frame);
        searchList->setObjectName(QStringLiteral("searchList"));
        QSizePolicy sizePolicy4(QSizePolicy::Preferred, QSizePolicy::Maximum);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(searchList->sizePolicy().hasHeightForWidth());
        searchList->setSizePolicy(sizePolicy4);
        searchList->setMinimumSize(QSize(0, 85));
        searchList->setMaximumSize(QSize(16777215, 85));
        QPalette palette3;
        palette3.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette3.setBrush(QPalette::Disabled, QPalette::Base, brush2);
        searchList->setPalette(palette3);

        verticalLayout_8->addWidget(searchList);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(5);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(5, 5, 5, 5);
        label = new QLabel(frame);
        label->setObjectName(QStringLiteral("label"));
        label->setFont(font4);

        horizontalLayout_2->addWidget(label);

        label_5 = new QLabel(frame);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout_2->addWidget(label_5);

        sendToQuickAccessButton = new QPushButton(frame);
        sendToQuickAccessButton->setObjectName(QStringLiteral("sendToQuickAccessButton"));
        sendToQuickAccessButton->setMaximumSize(QSize(25, 25));
        QIcon icon1;
        icon1.addFile(QStringLiteral("../res/arrow.png"), QSize(), QIcon::Normal, QIcon::Off);
        sendToQuickAccessButton->setIcon(icon1);

        horizontalLayout_2->addWidget(sendToQuickAccessButton);

        removeFromQuickAccessButton = new QPushButton(frame);
        removeFromQuickAccessButton->setObjectName(QStringLiteral("removeFromQuickAccessButton"));
        removeFromQuickAccessButton->setMaximumSize(QSize(25, 25));
        QIcon icon2;
        icon2.addFile(QStringLiteral("../res/x.png"), QSize(), QIcon::Normal, QIcon::Off);
        removeFromQuickAccessButton->setIcon(icon2);

        horizontalLayout_2->addWidget(removeFromQuickAccessButton);


        verticalLayout_8->addLayout(horizontalLayout_2);

        quickAccessList = new QListWidget(frame);
        quickAccessList->setObjectName(QStringLiteral("quickAccessList"));
        sizePolicy.setHeightForWidth(quickAccessList->sizePolicy().hasHeightForWidth());
        quickAccessList->setSizePolicy(sizePolicy);
        quickAccessList->setMinimumSize(QSize(0, 400));
        quickAccessList->setMaximumSize(QSize(16777215, 16777215));
        QPalette palette4;
        palette4.setBrush(QPalette::Active, QPalette::Base, brush1);
        palette4.setBrush(QPalette::Inactive, QPalette::Base, brush1);
        palette4.setBrush(QPalette::Disabled, QPalette::Base, brush2);
        quickAccessList->setPalette(palette4);
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


        verticalLayout->addLayout(verticalLayout_8);


        gridLayout_2->addWidget(frame, 0, 2, 2, 1);

        company_info_panel = new QFrame(centralwidget);
        company_info_panel->setObjectName(QStringLiteral("company_info_panel"));
        sizePolicy.setHeightForWidth(company_info_panel->sizePolicy().hasHeightForWidth());
        company_info_panel->setSizePolicy(sizePolicy);
        company_info_panel->setMinimumSize(QSize(300, 300));
        company_info_panel->setFrameShape(QFrame::StyledPanel);
        company_info_panel->setFrameShadow(QFrame::Raised);
        verticalLayout_7 = new QVBoxLayout(company_info_panel);
        verticalLayout_7->setObjectName(QStringLiteral("verticalLayout_7"));
        verticalLayout_9 = new QVBoxLayout();
        verticalLayout_9->setObjectName(QStringLiteral("verticalLayout_9"));
        verticalLayout_9->setContentsMargins(3, 3, 3, 3);
        company_info_symbol_label = new QLabel(company_info_panel);
        company_info_symbol_label->setObjectName(QStringLiteral("company_info_symbol_label"));
        company_info_symbol_label->setMaximumSize(QSize(16777215, 30));
        company_info_symbol_label->setFont(font);

        verticalLayout_9->addWidget(company_info_symbol_label);

        company_info_name_label = new QLabel(company_info_panel);
        company_info_name_label->setObjectName(QStringLiteral("company_info_name_label"));
        company_info_name_label->setMinimumSize(QSize(0, 30));
        company_info_name_label->setMaximumSize(QSize(16777215, 30));

        verticalLayout_9->addWidget(company_info_name_label);


        verticalLayout_7->addLayout(verticalLayout_9);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        gridLayout_3->setContentsMargins(3, 3, 3, 3);
        label_21 = new QLabel(company_info_panel);
        label_21->setObjectName(QStringLiteral("label_21"));

        gridLayout_3->addWidget(label_21, 2, 1, 1, 1);

        label_22 = new QLabel(company_info_panel);
        label_22->setObjectName(QStringLiteral("label_22"));

        gridLayout_3->addWidget(label_22, 3, 1, 1, 1);

        label_16 = new QLabel(company_info_panel);
        label_16->setObjectName(QStringLiteral("label_16"));

        gridLayout_3->addWidget(label_16, 2, 2, 1, 1);

        label_20 = new QLabel(company_info_panel);
        label_20->setObjectName(QStringLiteral("label_20"));

        gridLayout_3->addWidget(label_20, 1, 1, 1, 1);

        label_12 = new QLabel(company_info_panel);
        label_12->setObjectName(QStringLiteral("label_12"));

        gridLayout_3->addWidget(label_12, 1, 0, 1, 1);

        label_11 = new QLabel(company_info_panel);
        label_11->setObjectName(QStringLiteral("label_11"));

        gridLayout_3->addWidget(label_11, 3, 0, 1, 1);

        label_23 = new QLabel(company_info_panel);
        label_23->setObjectName(QStringLiteral("label_23"));

        gridLayout_3->addWidget(label_23, 4, 1, 1, 1);

        label_10 = new QLabel(company_info_panel);
        label_10->setObjectName(QStringLiteral("label_10"));

        gridLayout_3->addWidget(label_10, 4, 0, 1, 1);

        label_17 = new QLabel(company_info_panel);
        label_17->setObjectName(QStringLiteral("label_17"));

        gridLayout_3->addWidget(label_17, 3, 2, 1, 1);

        label_18 = new QLabel(company_info_panel);
        label_18->setObjectName(QStringLiteral("label_18"));

        gridLayout_3->addWidget(label_18, 4, 2, 1, 1);

        label_19 = new QLabel(company_info_panel);
        label_19->setObjectName(QStringLiteral("label_19"));

        gridLayout_3->addWidget(label_19, 0, 1, 1, 1);

        label_15 = new QLabel(company_info_panel);
        label_15->setObjectName(QStringLiteral("label_15"));

        gridLayout_3->addWidget(label_15, 1, 2, 1, 1);

        label_13 = new QLabel(company_info_panel);
        label_13->setObjectName(QStringLiteral("label_13"));

        gridLayout_3->addWidget(label_13, 2, 0, 1, 1);

        label_14 = new QLabel(company_info_panel);
        label_14->setObjectName(QStringLiteral("label_14"));

        gridLayout_3->addWidget(label_14, 0, 2, 1, 1);

        label_2 = new QLabel(company_info_panel);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout_3->addWidget(label_2, 0, 0, 1, 1);

        label_24 = new QLabel(company_info_panel);
        label_24->setObjectName(QStringLiteral("label_24"));

        gridLayout_3->addWidget(label_24, 0, 3, 1, 1);

        label_25 = new QLabel(company_info_panel);
        label_25->setObjectName(QStringLiteral("label_25"));

        gridLayout_3->addWidget(label_25, 1, 3, 1, 1);

        label_26 = new QLabel(company_info_panel);
        label_26->setObjectName(QStringLiteral("label_26"));

        gridLayout_3->addWidget(label_26, 2, 3, 1, 1);

        label_27 = new QLabel(company_info_panel);
        label_27->setObjectName(QStringLiteral("label_27"));

        gridLayout_3->addWidget(label_27, 3, 3, 1, 1);

        label_28 = new QLabel(company_info_panel);
        label_28->setObjectName(QStringLiteral("label_28"));

        gridLayout_3->addWidget(label_28, 4, 3, 1, 1);


        verticalLayout_7->addLayout(gridLayout_3);

        webEngineView = new QWebEngineView(company_info_panel);
        webEngineView->setObjectName(QStringLiteral("webEngineView"));
        webEngineView->setMinimumSize(QSize(300, 300));
        webEngineView->setUrl(QUrl(QStringLiteral("file:///C:/Users/bwelsh/Documents/GitHub/StockFlip/graphed.html")));

        verticalLayout_7->addWidget(webEngineView);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_7->addItem(verticalSpacer);


        gridLayout_2->addWidget(company_info_panel, 0, 3, 2, 1);

        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1193, 21));
        menuMenu = new QMenu(menuBar);
        menuMenu->setObjectName(QStringLiteral("menuMenu"));
        menuAdmin_Menu = new QMenu(menuBar);
        menuAdmin_Menu->setObjectName(QStringLiteral("menuAdmin_Menu"));
        MainWindow->setMenuBar(menuBar);
        QWidget::setTabOrder(searchBar, searchButton);
        QWidget::setTabOrder(searchButton, searchList);
        QWidget::setTabOrder(searchList, sendToQuickAccessButton);
        QWidget::setTabOrder(sendToQuickAccessButton, removeFromQuickAccessButton);
        QWidget::setTabOrder(removeFromQuickAccessButton, quickAccessList);
        QWidget::setTabOrder(quickAccessList, listWidget);
        QWidget::setTabOrder(listWidget, refreshButton);

        menuBar->addAction(menuMenu->menuAction());
        menuBar->addAction(menuAdmin_Menu->menuAction());
        menuMenu->addAction(actionAdjust_Credits);
        menuMenu->addAction(actionChange_Password);
        menuMenu->addAction(actionReset_Account);
        menuMenu->addAction(actionExit);
        menuAdmin_Menu->addAction(actionDelete_User);
        menuAdmin_Menu->addAction(actionMessage_User);

        retranslateUi(MainWindow);
        QObject::connect(searchBar, SIGNAL(returnPressed()), searchButton, SLOT(click()));
        QObject::connect(searchButton, SIGNAL(clicked()), searchList, SLOT(reset()));
        QObject::connect(quickAccessList, SIGNAL(itemPressed(QListWidgetItem*)), listWidget, SLOT(clearSelection()));
        QObject::connect(listWidget, SIGNAL(itemPressed(QListWidgetItem*)), quickAccessList, SLOT(clearSelection()));
        QObject::connect(actionExit, SIGNAL(triggered()), MainWindow, SLOT(close()));
        QObject::connect(numToTrade, SIGNAL(returnPressed()), confirmButton, SLOT(click()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        actionAdjust_Credits->setText(QApplication::translate("MainWindow", "Adjust Credits", Q_NULLPTR));
        actionChange_Password->setText(QApplication::translate("MainWindow", "Change Password", Q_NULLPTR));
        actionExit->setText(QApplication::translate("MainWindow", "Exit", Q_NULLPTR));
        actionReset_Account->setText(QApplication::translate("MainWindow", "Reset Account", Q_NULLPTR));
        actionDelete_User->setText(QApplication::translate("MainWindow", "Delete_User", Q_NULLPTR));
        actionMessage_User->setText(QApplication::translate("MainWindow", "Message_User_By_Email", Q_NULLPTR));
        label_9->setText(QApplication::translate("MainWindow", "Portfolio", Q_NULLPTR));
        lastUpdatedLabel->setText(QString());
        refreshButton->setText(QString());
        label_3->setText(QApplication::translate("MainWindow", "Logged in as:", Q_NULLPTR));
        currentBalance->setText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        stockBalanceLabel_2->setText(QApplication::translate("MainWindow", "StockFlip Credits:", Q_NULLPTR));
        loggedInAsUser->setText(QApplication::translate("MainWindow", "-", Q_NULLPTR));
        totalValueLabel->setText(QApplication::translate("MainWindow", "Total Value:", Q_NULLPTR));
        totalValue->setText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        label_6->setText(QApplication::translate("MainWindow", "Trade", Q_NULLPTR));
        companyLabel->setText(QApplication::translate("MainWindow", "No Company Selected", Q_NULLPTR));
        companyFullNameLabel->setText(QString());
        priceLabel->setText(QString());
        numSharesOwnedLabel->setText(QString());
        label_4->setText(QApplication::translate("MainWindow", "Action       ", Q_NULLPTR));
        label_7->setText(QApplication::translate("MainWindow", "Shares", Q_NULLPTR));
        label_8->setText(QApplication::translate("MainWindow", "Total Price", Q_NULLPTR));
        tradeCombo->clear();
        tradeCombo->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "Buy", Q_NULLPTR)
         << QApplication::translate("MainWindow", "Sell", Q_NULLPTR)
        );
        totalPriceLabel->setText(QApplication::translate("MainWindow", "-", Q_NULLPTR));
        confirmButton->setText(QApplication::translate("MainWindow", "Confirm", Q_NULLPTR));
        tradeErrorLabel->setText(QString());
        searchBar->setPlaceholderText(QApplication::translate("MainWindow", "Search Symbols", Q_NULLPTR));
        searchButton->setText(QApplication::translate("MainWindow", "Search", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "Quick Access", Q_NULLPTR));
        label_5->setText(QApplication::translate("MainWindow", "Add/Remove Quick Access", Q_NULLPTR));
        sendToQuickAccessButton->setText(QString());
        removeFromQuickAccessButton->setText(QString());
        company_info_symbol_label->setText(QApplication::translate("MainWindow", "Symbol", Q_NULLPTR));
        company_info_name_label->setText(QApplication::translate("MainWindow", "Name", Q_NULLPTR));
        label_21->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_22->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_16->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_20->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_12->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_11->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_23->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_10->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_17->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_18->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_19->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_15->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_13->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_14->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_2->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_24->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_25->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_26->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_27->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        label_28->setText(QApplication::translate("MainWindow", "TextLabel", Q_NULLPTR));
        menuMenu->setTitle(QApplication::translate("MainWindow", "Menu", Q_NULLPTR));
        menuAdmin_Menu->setTitle(QApplication::translate("MainWindow", "Admin Menu", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAIN_ADMIN_H
