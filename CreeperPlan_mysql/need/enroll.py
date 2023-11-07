# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enroll.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(500, 280)
        Form.setMinimumSize(QSize(500, 280))
        Form.setMaximumSize(QSize(500, 280))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(12)
        font.setBold(False)
        Form.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 40, 410, 186))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(50, 30))
        self.label.setMaximumSize(QSize(50, 30))
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.le_user = QLineEdit(self.layoutWidget)
        self.le_user.setObjectName(u"le_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_user.sizePolicy().hasHeightForWidth())
        self.le_user.setSizePolicy(sizePolicy1)
        self.le_user.setMinimumSize(QSize(350, 30))
        self.le_user.setMaximumSize(QSize(350, 30))
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.le_user.setFont(font1)
        self.le_user.setMaxLength(16)
        self.le_user.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.le_user.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.le_user)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 30))
        self.label_2.setMaximumSize(QSize(50, 30))
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_password = QLineEdit(self.layoutWidget)
        self.le_password.setObjectName(u"le_password")
        sizePolicy1.setHeightForWidth(self.le_password.sizePolicy().hasHeightForWidth())
        self.le_password.setSizePolicy(sizePolicy1)
        self.le_password.setMinimumSize(QSize(350, 30))
        self.le_password.setMaximumSize(QSize(350, 30))
        self.le_password.setFont(font1)
        self.le_password.setMaxLength(18)
        self.le_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.le_password)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 30))
        self.label_3.setMaximumSize(QSize(50, 30))
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.le_name = QLineEdit(self.layoutWidget)
        self.le_name.setObjectName(u"le_name")
        sizePolicy1.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy1)
        self.le_name.setMinimumSize(QSize(350, 30))
        self.le_name.setMaximumSize(QSize(350, 30))
        self.le_name.setFont(font1)
        self.le_name.setMaxLength(16)

        self.horizontalLayout_3.addWidget(self.le_name)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 30))
        self.label_4.setMaximumSize(QSize(50, 30))
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.le_phone = QLineEdit(self.layoutWidget)
        self.le_phone.setObjectName(u"le_phone")
        sizePolicy1.setHeightForWidth(self.le_phone.sizePolicy().hasHeightForWidth())
        self.le_phone.setSizePolicy(sizePolicy1)
        self.le_phone.setMinimumSize(QSize(350, 30))
        self.le_phone.setMaximumSize(QSize(350, 30))
        self.le_phone.setFont(font1)
        self.le_phone.setInputMethodHints(Qt.ImhNone)
        self.le_phone.setMaxLength(11)

        self.horizontalLayout_4.addWidget(self.le_phone)

        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_enroll = QPushButton(self.layoutWidget)
        self.btn_enroll.setObjectName(u"btn_enroll")
        sizePolicy.setHeightForWidth(self.btn_enroll.sizePolicy().hasHeightForWidth())
        self.btn_enroll.setSizePolicy(sizePolicy)
        self.btn_enroll.setMinimumSize(QSize(200, 30))
        self.btn_enroll.setMaximumSize(QSize(200, 30))
        self.btn_enroll.setSizeIncrement(QSize(0, 0))
        self.btn_enroll.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_enroll)

        self.btn_return = QPushButton(self.layoutWidget)
        self.btn_return.setObjectName(u"btn_return")
        sizePolicy.setHeightForWidth(self.btn_return.sizePolicy().hasHeightForWidth())
        self.btn_return.setSizePolicy(sizePolicy)
        self.btn_return.setMinimumSize(QSize(200, 30))
        self.btn_return.setMaximumSize(QSize(200, 30))
        self.btn_return.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_return)

        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.le_user.setPlaceholderText(QCoreApplication.translate("Form",
                                                                   u"\u5b57\u6bcd\u5f00\u5934\uff0c\u5141\u8bb83-16\u5b57\u8282\uff0c\u5141\u8bb8\u5b57\u6bcd\u6570\u5b57\u4e0b\u5212\u7ebf",
                                                                   u"\u5b57\u6bcd\u5f00\u5934\uff0c\u5141\u8bb83-16\u5b57\u8282\uff0c\u5141\u8bb8\u5b57\u6bcd\u6570\u5b57\u4e0b\u5212\u7ebf"))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("Form",
                                                                       u"\u4ee5\u5b57\u6bcd\u5f00\u5934\uff0c\u957f\u5ea6\u57283~18\u4e4b\u95f4\uff0c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57",
                                                                       u"\u4ee5\u5b57\u6bcd\u5f00\u5934\uff0c\u957f\u5ea6\u57283~18\u4e4b\u95f4\uff0c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57"))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u540d\u5b57", None))
        self.le_name.setPlaceholderText(QCoreApplication.translate("Form",
                                                                   u"\u8bf7\u8f93\u5165\u540d\u5b57(\u4e2d\u6587\u3001\u82f1\u6587\u3001\u6570\u5b57\u5305\u62ec\u4e0b\u5212\u7ebf)",
                                                                   None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u624b\u673a\u53f7", None))
        self.le_phone.setPlaceholderText(
            QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7", None))
        self.btn_enroll.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.btn_return.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
    # retranslateUi
