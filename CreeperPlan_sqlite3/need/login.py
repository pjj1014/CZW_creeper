# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(800, 500)
        LoginDialog.setMinimumSize(QSize(800, 500))
        LoginDialog.setMaximumSize(QSize(800, 500))
        self.layoutWidget = QWidget(LoginDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(500, 360, 230, 118))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(60, 21))
        self.label.setMaximumSize(QSize(60, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.usernameLineEdit = QLineEdit(self.layoutWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setMinimumSize(QSize(150, 21))
        self.usernameLineEdit.setMaximumSize(QSize(150, 21))

        self.horizontalLayout.addWidget(self.usernameLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(60, 21))
        self.label_2.setMaximumSize(QSize(60, 21))
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.passwordLineEdit = QLineEdit(self.layoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setMinimumSize(QSize(150, 21))
        self.passwordLineEdit.setMaximumSize(QSize(150, 21))
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.passwordLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.loginPushButton = QPushButton(self.layoutWidget)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setMinimumSize(QSize(105, 24))
        self.loginPushButton.setMaximumSize(QSize(105, 24))
        font1 = QFont()
        font1.setPointSize(10)
        self.loginPushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.loginPushButton, 0, Qt.AlignHCenter)

        self.registerPushButton = QPushButton(self.layoutWidget)
        self.registerPushButton.setObjectName(u"registerPushButton")
        self.registerPushButton.setMinimumSize(QSize(105, 24))
        self.registerPushButton.setMaximumSize(QSize(105, 24))
        self.registerPushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.registerPushButton, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_accountsTopUp = QPushButton(self.layoutWidget)
        self.btn_accountsTopUp.setObjectName(u"btn_accountsTopUp")
        self.btn_accountsTopUp.setMinimumSize(QSize(220, 24))
        self.btn_accountsTopUp.setMaximumSize(QSize(220, 24))
        self.btn_accountsTopUp.setFont(font1)

        self.verticalLayout.addWidget(self.btn_accountsTopUp, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label_3 = QLabel(LoginDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 370, 400, 110))
        self.label_3.setMinimumSize(QSize(400, 110))
        self.label_3.setMaximumSize(QSize(400, 110))
        font2 = QFont()
        font2.setPointSize(40)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background: rgb(0, 0, 0);\n"
"border:5px solid rgb(255, 255, 255);\n"
"border-radius:50px;\n"
"color:rgb(255, 255, 255);")
        self.label_4 = QLabel(LoginDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 800, 350))
        self.label_4.setMinimumSize(QSize(800, 350))
        self.label_4.setMaximumSize(QSize(800, 350))
        font3 = QFont()
        font3.setPointSize(40)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"\u722c\u866b\u8ba1\u5212-\u767b\u5f55\u754c\u9762", None))
        self.label.setText(QCoreApplication.translate("LoginDialog", u"<html><head/><body><p align=\"justify\">\u7528\u6237\u540d:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoginDialog", u"<html><head/><body><p align=\"justify\">\u5bc6   \u7801:</p></body></html>", None))
        self.loginPushButton.setText(QCoreApplication.translate("LoginDialog", u"\u767b\u5f55", None))
        self.registerPushButton.setText(QCoreApplication.translate("LoginDialog", u"\u6ce8\u518c", None))
        self.btn_accountsTopUp.setText(QCoreApplication.translate("LoginDialog", u"\u5e10\u53f7\u5145\u503c", None))
        self.label_3.setText(QCoreApplication.translate("LoginDialog", u" CreeperPlan", None))
        self.label_4.setText("")
    # retranslateUi

