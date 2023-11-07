# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changePasswd.ui'
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


class Ui_changePasswd(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(500, 260)
        Form.setMinimumSize(QSize(500, 260))
        Form.setMaximumSize(QSize(500, 260))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(12)
        font.setBold(False)
        Form.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 430, 186))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_change = QPushButton(self.layoutWidget)
        self.btn_change.setObjectName(u"btn_change")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_change.sizePolicy().hasHeightForWidth())
        self.btn_change.setSizePolicy(sizePolicy)
        self.btn_change.setMinimumSize(QSize(207, 30))
        self.btn_change.setMaximumSize(QSize(207, 30))
        self.btn_change.setSizeIncrement(QSize(0, 0))
        self.btn_change.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_change)

        self.btn_return = QPushButton(self.layoutWidget)
        self.btn_return.setObjectName(u"btn_return")
        sizePolicy.setHeightForWidth(self.btn_return.sizePolicy().hasHeightForWidth())
        self.btn_return.setSizePolicy(sizePolicy)
        self.btn_return.setMinimumSize(QSize(207, 30))
        self.btn_return.setMaximumSize(QSize(207, 30))
        self.btn_return.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_return)

        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(65, 30))
        self.label.setMaximumSize(QSize(65, 30))
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.le_originalPasswd = QLineEdit(self.layoutWidget)
        self.le_originalPasswd.setObjectName(u"le_originalPasswd")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_originalPasswd.sizePolicy().hasHeightForWidth())
        self.le_originalPasswd.setSizePolicy(sizePolicy1)
        self.le_originalPasswd.setMinimumSize(QSize(350, 30))
        self.le_originalPasswd.setMaximumSize(QSize(350, 30))
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.le_originalPasswd.setFont(font1)
        self.le_originalPasswd.setMaxLength(18)
        self.le_originalPasswd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.le_originalPasswd)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(65, 30))
        self.label_2.setMaximumSize(QSize(65, 30))
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_changePasswd = QLineEdit(self.layoutWidget)
        self.le_changePasswd.setObjectName(u"le_changePasswd")
        sizePolicy1.setHeightForWidth(self.le_changePasswd.sizePolicy().hasHeightForWidth())
        self.le_changePasswd.setSizePolicy(sizePolicy1)
        self.le_changePasswd.setMinimumSize(QSize(350, 30))
        self.le_changePasswd.setMaximumSize(QSize(350, 30))
        self.le_changePasswd.setFont(font1)
        self.le_changePasswd.setMaxLength(18)
        self.le_changePasswd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.le_changePasswd)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(65, 30))
        self.label_3.setMaximumSize(QSize(65, 30))
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.le_confirmPasswd = QLineEdit(self.layoutWidget)
        self.le_confirmPasswd.setObjectName(u"le_confirmPasswd")
        sizePolicy1.setHeightForWidth(self.le_confirmPasswd.sizePolicy().hasHeightForWidth())
        self.le_confirmPasswd.setSizePolicy(sizePolicy1)
        self.le_confirmPasswd.setMinimumSize(QSize(350, 30))
        self.le_confirmPasswd.setMaximumSize(QSize(350, 30))
        self.le_confirmPasswd.setFont(font1)
        self.le_confirmPasswd.setMaxLength(18)
        self.le_confirmPasswd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.le_confirmPasswd)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4fee\u6539\u5bc6\u7801", None))
        self.btn_change.setText(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
        self.btn_return.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u539f \u5bc6 \u7801", None))
        self.le_originalPasswd.setPlaceholderText(QCoreApplication.translate("Form",
                                                                             u"\u4ee5\u5b57\u6bcd\u5f00\u5934\uff0c\u957f\u5ea6\u57283~18\u4e4b\u95f4\uff0c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57",
                                                                             u"\u4ee5\u5b57\u6bcd\u5f00\u5934\uff0c\u957f\u5ea6\u57283~18\u4e4b\u95f4\uff0c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57"))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6    \u7801", None))
        self.le_changePasswd.setPlaceholderText(QCoreApplication.translate("Form",
                                                                           u"\u4ee5\u5b57\u6bcd\u5f00\u5934\uff0c\u957f\u5ea6\u57283~18\u4e4b\u95f4\uff0c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57",
                                                                           u"\u4ee5\u5b57\u6bcd\u5f00\u5934\uff0c\u957f\u5ea6\u57283~18\u4e4b\u95f4\uff0c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57"))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.le_confirmPasswd.setPlaceholderText(QCoreApplication.translate("Form",
                                                                            u"\u4ee5\u5b57\u6bcd\u5f00\u5934\uff0c\u957f\u5ea6\u57283~18\u4e4b\u95f4\uff0c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57",
                                                                            u"\u4ee5\u5b57\u6bcd\u5f00\u5934\uff0c\u957f\u5ea6\u57283~18\u4e4b\u95f4\uff0c\u53ea\u80fd\u5305\u542b\u5b57\u6bcd\u3001\u6570\u5b57"))
    # retranslateUi
