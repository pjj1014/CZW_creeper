# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowCreeper.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDateTimeEdit, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 780)
        MainWindow.setMinimumSize(QSize(1020, 780))
        MainWindow.setMaximumSize(QSize(1020, 780))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 360, 482, 24))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(80, 20))
        self.label_10.setMaximumSize(QSize(80, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_10.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(28, 20))
        self.label_11.setMaximumSize(QSize(28, 20))
        self.label_11.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.de_beginDate = QDateEdit(self.layoutWidget)
        self.de_beginDate.setObjectName(u"de_beginDate")
        self.de_beginDate.setMinimumSize(QSize(100, 20))
        self.de_beginDate.setMaximumSize(QSize(100, 20))
        self.de_beginDate.setFont(font)
        self.de_beginDate.setCurrentSection(QDateTimeEdit.YearSection)
        self.de_beginDate.setCalendarPopup(True)
        self.de_beginDate.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_12.addWidget(self.de_beginDate)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(28, 20))
        self.label_12.setMaximumSize(QSize(28, 20))
        self.label_12.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.de_endData = QDateEdit(self.layoutWidget)
        self.de_endData.setObjectName(u"de_endData")
        self.de_endData.setMinimumSize(QSize(100, 20))
        self.de_endData.setMaximumSize(QSize(100, 20))
        self.de_endData.setFont(font)
        self.de_endData.setCalendarPopup(True)

        self.horizontalLayout_13.addWidget(self.de_endData)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)

        self.cb_dateChoose = QCheckBox(self.layoutWidget)
        self.cb_dateChoose.setObjectName(u"cb_dateChoose")
        self.cb_dateChoose.setMinimumSize(QSize(110, 20))
        self.cb_dateChoose.setMaximumSize(QSize(110, 20))
        self.cb_dateChoose.setFont(font)

        self.horizontalLayout_14.addWidget(self.cb_dateChoose)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 180, 481, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(56, 20))
        self.label.setMaximumSize(QSize(56, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.le_userName = QLineEdit(self.layoutWidget_2)
        self.le_userName.setObjectName(u"le_userName")
        self.le_userName.setMinimumSize(QSize(142, 20))
        self.le_userName.setMaximumSize(QSize(142, 20))

        self.horizontalLayout.addWidget(self.le_userName)

        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 20))
        self.label_2.setMaximumSize(QSize(40, 20))
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.le_passWord = QLineEdit(self.layoutWidget_2)
        self.le_passWord.setObjectName(u"le_passWord")
        self.le_passWord.setMinimumSize(QSize(142, 20))
        self.le_passWord.setMaximumSize(QSize(142, 20))
        self.le_passWord.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.le_passWord)

        self.btn_login = QPushButton(self.layoutWidget_2)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(75, 23))
        self.btn_login.setMaximumSize(QSize(75, 23))

        self.horizontalLayout.addWidget(self.btn_login)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(510, 430, 500, 170))
        self.frame.setMinimumSize(QSize(500, 170))
        self.frame.setMaximumSize(QSize(500, 170))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 10, 460, 15))
        self.label_28.setMinimumSize(QSize(460, 15))
        self.label_28.setMaximumSize(QSize(460, 15))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_28.setFont(font2)
        self.label_28.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.label_28.setScaledContents(False)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_28.setWordWrap(False)
        self.label_28.setMargin(0)
        self.layoutWidget_3 = QWidget(self.frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 40, 461, 129))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.btn_chooseDoc = QPushButton(self.layoutWidget_3)
        self.btn_chooseDoc.setObjectName(u"btn_chooseDoc")
        self.btn_chooseDoc.setMinimumSize(QSize(75, 20))
        self.btn_chooseDoc.setMaximumSize(QSize(75, 20))
        self.btn_chooseDoc.setFont(font)

        self.horizontalLayout_30.addWidget(self.btn_chooseDoc)

        self.le_docPath = QLineEdit(self.layoutWidget_3)
        self.le_docPath.setObjectName(u"le_docPath")
        self.le_docPath.setMinimumSize(QSize(240, 20))
        self.le_docPath.setMaximumSize(QSize(240, 20))
        self.le_docPath.setFont(font)

        self.horizontalLayout_30.addWidget(self.le_docPath)

        self.btn_startClean = QPushButton(self.layoutWidget_3)
        self.btn_startClean.setObjectName(u"btn_startClean")
        self.btn_startClean.setMinimumSize(QSize(75, 20))
        self.btn_startClean.setMaximumSize(QSize(75, 20))
        self.btn_startClean.setFont(font)

        self.horizontalLayout_30.addWidget(self.btn_startClean)


        self.verticalLayout_3.addLayout(self.horizontalLayout_30)

        self.pte_clean_gjc = QPlainTextEdit(self.layoutWidget_3)
        self.pte_clean_gjc.setObjectName(u"pte_clean_gjc")
        self.pte_clean_gjc.setMinimumSize(QSize(459, 63))
        self.pte_clean_gjc.setMaximumSize(QSize(459, 63))
        self.pte_clean_gjc.setFont(font)

        self.verticalLayout_3.addWidget(self.pte_clean_gjc)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_27 = QLabel(self.layoutWidget_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(75, 20))
        self.label_27.setMaximumSize(QSize(75, 20))
        self.label_27.setFont(font)
        self.label_27.setLayoutDirection(Qt.LeftToRight)
        self.label_27.setAutoFillBackground(False)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_27)

        self.pb_docClearProgressBar = QProgressBar(self.layoutWidget_3)
        self.pb_docClearProgressBar.setObjectName(u"pb_docClearProgressBar")
        self.pb_docClearProgressBar.setMinimumSize(QSize(240, 20))
        self.pb_docClearProgressBar.setMaximumSize(QSize(240, 20))
        self.pb_docClearProgressBar.setFont(font)
        self.pb_docClearProgressBar.setValue(0)
        self.pb_docClearProgressBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_31.addWidget(self.pb_docClearProgressBar)

        self.btn_openDoc = QPushButton(self.layoutWidget_3)
        self.btn_openDoc.setObjectName(u"btn_openDoc")
        self.btn_openDoc.setMinimumSize(QSize(75, 20))
        self.btn_openDoc.setMaximumSize(QSize(75, 20))
        self.btn_openDoc.setFont(font)

        self.horizontalLayout_31.addWidget(self.btn_openDoc)


        self.verticalLayout_3.addLayout(self.horizontalLayout_31)

        self.layoutWidget_4 = QWidget(self.centralwidget)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 570, 481, 34))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_21 = QLabel(self.layoutWidget_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_21)

        self.cb_qualificationCertificate = QComboBox(self.layoutWidget_4)
        self.cb_qualificationCertificate.setObjectName(u"cb_qualificationCertificate")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_qualificationCertificate.sizePolicy().hasHeightForWidth())
        self.cb_qualificationCertificate.setSizePolicy(sizePolicy)
        self.cb_qualificationCertificate.setMinimumSize(QSize(200, 20))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setUnderline(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.cb_qualificationCertificate.setFont(font3)

        self.horizontalLayout_21.addWidget(self.cb_qualificationCertificate)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_22 = QLabel(self.layoutWidget_4)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setMinimumSize(QSize(0, 30))
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_22)

        self.doubleSpinBox = QDoubleSpinBox(self.layoutWidget_4)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy2)
        self.doubleSpinBox.setMinimumSize(QSize(60, 20))
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.100000000000000)
        self.doubleSpinBox.setValue(0.650000000000000)

        self.horizontalLayout_22.addWidget(self.doubleSpinBox)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_22)

        self.layoutWidget_5 = QWidget(self.centralwidget)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 480, 481, 39))
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_15 = QLabel(self.layoutWidget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_15)

        self.cb_itemAmount = QComboBox(self.layoutWidget_5)
        self.cb_itemAmount.setObjectName(u"cb_itemAmount")
        self.cb_itemAmount.setMinimumSize(QSize(100, 20))
        self.cb_itemAmount.setFont(font)

        self.horizontalLayout_17.addWidget(self.cb_itemAmount)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_16 = QLabel(self.layoutWidget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(100, 20))
        self.label_16.setMaximumSize(QSize(100, 20))
        self.label_16.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_16)

        self.le_minimumAmount = QLineEdit(self.layoutWidget_5)
        self.le_minimumAmount.setObjectName(u"le_minimumAmount")

        self.horizontalLayout_18.addWidget(self.le_minimumAmount)

        self.label_17 = QLabel(self.layoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setUnderline(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.label_17.setFont(font4)

        self.horizontalLayout_18.addWidget(self.label_17)

        self.le_maximunAmount = QLineEdit(self.layoutWidget_5)
        self.le_maximunAmount.setObjectName(u"le_maximunAmount")

        self.horizontalLayout_18.addWidget(self.le_maximunAmount)

        self.cb_customAmount = QCheckBox(self.layoutWidget_5)
        self.cb_customAmount.setObjectName(u"cb_customAmount")

        self.horizontalLayout_18.addWidget(self.cb_customAmount)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)

        self.layoutWidget_6 = QWidget(self.centralwidget)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 100, 484, 61))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_qd = QPushButton(self.layoutWidget_6)
        self.btn_qd.setObjectName(u"btn_qd")
        self.btn_qd.setMinimumSize(QSize(125, 20))
        self.btn_qd.setMaximumSize(QSize(125, 20))
        self.btn_qd.setFont(font)

        self.horizontalLayout_5.addWidget(self.btn_qd)

        self.le_driverPath = QLineEdit(self.layoutWidget_6)
        self.le_driverPath.setObjectName(u"le_driverPath")
        self.le_driverPath.setMinimumSize(QSize(346, 20))
        self.le_driverPath.setMaximumSize(QSize(346, 20))
        self.le_driverPath.setFont(font)
        self.le_driverPath.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.le_driverPath)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radio_edge = QRadioButton(self.layoutWidget_6)
        self.radio_edge.setObjectName(u"radio_edge")
        self.radio_edge.setMinimumSize(QSize(237, 20))
        self.radio_edge.setMaximumSize(QSize(237, 20))
        self.radio_edge.setFont(font)

        self.horizontalLayout_6.addWidget(self.radio_edge)

        self.radio_chrome = QRadioButton(self.layoutWidget_6)
        self.radio_chrome.setObjectName(u"radio_chrome")
        self.radio_chrome.setMinimumSize(QSize(237, 20))
        self.radio_chrome.setMaximumSize(QSize(237, 20))
        self.radio_chrome.setFont(font)
        self.radio_chrome.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radio_chrome)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.layoutWidget_7 = QWidget(self.centralwidget)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 400, 481, 22))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(80, 20))
        self.label_13.setMaximumSize(QSize(80, 20))
        self.label_13.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_13)

        self.rb_fullTextInclludingAttachments = QRadioButton(self.layoutWidget_7)
        self.rb_fullTextInclludingAttachments.setObjectName(u"rb_fullTextInclludingAttachments")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rb_fullTextInclludingAttachments.sizePolicy().hasHeightForWidth())
        self.rb_fullTextInclludingAttachments.setSizePolicy(sizePolicy3)
        self.rb_fullTextInclludingAttachments.setMinimumSize(QSize(140, 20))
        self.rb_fullTextInclludingAttachments.setMaximumSize(QSize(140, 20))
        self.rb_fullTextInclludingAttachments.setFont(font)
        self.rb_fullTextInclludingAttachments.setCheckable(True)
        self.rb_fullTextInclludingAttachments.setChecked(True)

        self.horizontalLayout_15.addWidget(self.rb_fullTextInclludingAttachments)

        self.rb_titleSearch = QRadioButton(self.layoutWidget_7)
        self.rb_titleSearch.setObjectName(u"rb_titleSearch")
        sizePolicy3.setHeightForWidth(self.rb_titleSearch.sizePolicy().hasHeightForWidth())
        self.rb_titleSearch.setSizePolicy(sizePolicy3)
        self.rb_titleSearch.setMinimumSize(QSize(100, 20))
        self.rb_titleSearch.setMaximumSize(QSize(100, 20))
        self.rb_titleSearch.setFont(font)

        self.horizontalLayout_15.addWidget(self.rb_titleSearch)

        self.rb_fullTextNoAttachment = QRadioButton(self.layoutWidget_7)
        self.rb_fullTextNoAttachment.setObjectName(u"rb_fullTextNoAttachment")
        sizePolicy3.setHeightForWidth(self.rb_fullTextNoAttachment.sizePolicy().hasHeightForWidth())
        self.rb_fullTextNoAttachment.setSizePolicy(sizePolicy3)
        self.rb_fullTextNoAttachment.setMinimumSize(QSize(130, 20))
        self.rb_fullTextNoAttachment.setMaximumSize(QSize(130, 20))
        self.rb_fullTextNoAttachment.setFont(font)

        self.horizontalLayout_15.addWidget(self.rb_fullTextNoAttachment)

        self.layoutWidget_8 = QWidget(self.centralwidget)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(10, 220, 481, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_8)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMinimumSize(QSize(110, 20))
        self.label_3.setMaximumSize(QSize(110, 20))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.te_searchBox = QTextEdit(self.layoutWidget_8)
        self.te_searchBox.setObjectName(u"te_searchBox")
        sizePolicy4.setHeightForWidth(self.te_searchBox.sizePolicy().hasHeightForWidth())
        self.te_searchBox.setSizePolicy(sizePolicy4)
        self.te_searchBox.setMinimumSize(QSize(350, 60))
        self.te_searchBox.setMaximumSize(QSize(350, 60))
        self.te_searchBox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.te_searchBox)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(950, 750, 62, 20))
        self.label_25.setMinimumSize(QSize(62, 20))
        self.label_25.setMaximumSize(QSize(62, 20))
        self.layoutWidget_9 = QWidget(self.centralwidget)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(10, 530, 481, 25))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_18)

        self.cb_acquisitionMethods = QComboBox(self.layoutWidget_9)
        self.cb_acquisitionMethods.setObjectName(u"cb_acquisitionMethods")
        sizePolicy3.setHeightForWidth(self.cb_acquisitionMethods.sizePolicy().hasHeightForWidth())
        self.cb_acquisitionMethods.setSizePolicy(sizePolicy3)
        self.cb_acquisitionMethods.setFont(font)

        self.horizontalLayout_20.addWidget(self.cb_acquisitionMethods)

        self.label_19 = QLabel(self.layoutWidget_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_19)

        self.cb_capitalSource = QComboBox(self.layoutWidget_9)
        self.cb_capitalSource.setObjectName(u"cb_capitalSource")
        sizePolicy3.setHeightForWidth(self.cb_capitalSource.sizePolicy().hasHeightForWidth())
        self.cb_capitalSource.setSizePolicy(sizePolicy3)
        self.cb_capitalSource.setFont(font)

        self.horizontalLayout_20.addWidget(self.cb_capitalSource)

        self.label_20 = QLabel(self.layoutWidget_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_20)

        self.cb_bidEvaluationMethod = QComboBox(self.layoutWidget_9)
        self.cb_bidEvaluationMethod.setObjectName(u"cb_bidEvaluationMethod")
        sizePolicy3.setHeightForWidth(self.cb_bidEvaluationMethod.sizePolicy().hasHeightForWidth())
        self.cb_bidEvaluationMethod.setSizePolicy(sizePolicy3)
        self.cb_bidEvaluationMethod.setFont(font)

        self.horizontalLayout_20.addWidget(self.cb_bidEvaluationMethod)

        self.layoutWidget_10 = QWidget(self.centralwidget)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(510, 60, 501, 361))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_24 = QLabel(self.layoutWidget_10)
        self.label_24.setObjectName(u"label_24")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy5)
        self.label_24.setMinimumSize(QSize(78, 72))
        self.label_24.setMaximumSize(QSize(78, 72))
        self.label_24.setFont(font)
        self.label_24.setTextFormat(Qt.AutoText)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_24)

        self.te_hy = QTextEdit(self.layoutWidget_10)
        self.te_hy.setObjectName(u"te_hy")
        sizePolicy4.setHeightForWidth(self.te_hy.sizePolicy().hasHeightForWidth())
        self.te_hy.setSizePolicy(sizePolicy4)
        self.te_hy.setMinimumSize(QSize(393, 65))
        self.te_hy.setMaximumSize(QSize(393, 65))

        self.horizontalLayout_25.addWidget(self.te_hy)


        self.gridLayout_2.addLayout(self.horizontalLayout_25, 1, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rb_cleanGjc = QRadioButton(self.layoutWidget_10)
        self.rb_cleanGjc.setObjectName(u"rb_cleanGjc")
        self.rb_cleanGjc.setMinimumSize(QSize(180, 17))
        self.rb_cleanGjc.setMaximumSize(QSize(180, 17))
        self.rb_cleanGjc.setFont(font)
        self.rb_cleanGjc.setChecked(True)

        self.verticalLayout.addWidget(self.rb_cleanGjc)

        self.rb_saveGjc = QRadioButton(self.layoutWidget_10)
        self.rb_saveGjc.setObjectName(u"rb_saveGjc")
        self.rb_saveGjc.setMinimumSize(QSize(180, 17))
        self.rb_saveGjc.setMaximumSize(QSize(180, 17))
        self.rb_saveGjc.setFont(font)
        self.rb_saveGjc.setChecked(False)

        self.verticalLayout.addWidget(self.rb_saveGjc)


        self.horizontalLayout_26.addLayout(self.verticalLayout)

        self.pte_cleanORsave_gjc = QPlainTextEdit(self.layoutWidget_10)
        self.pte_cleanORsave_gjc.setObjectName(u"pte_cleanORsave_gjc")
        self.pte_cleanORsave_gjc.setMinimumSize(QSize(290, 65))
        self.pte_cleanORsave_gjc.setMaximumSize(QSize(290, 65))

        self.horizontalLayout_26.addWidget(self.pte_cleanORsave_gjc)


        self.gridLayout_2.addLayout(self.horizontalLayout_26, 2, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.btn_choosePosition = QPushButton(self.layoutWidget_10)
        self.btn_choosePosition.setObjectName(u"btn_choosePosition")
        self.btn_choosePosition.setMinimumSize(QSize(86, 23))
        self.btn_choosePosition.setMaximumSize(QSize(86, 23))
        self.btn_choosePosition.setFont(font)
        self.btn_choosePosition.setAutoDefault(False)

        self.horizontalLayout_27.addWidget(self.btn_choosePosition)

        self.le_tablePath = QLineEdit(self.layoutWidget_10)
        self.le_tablePath.setObjectName(u"le_tablePath")
        self.le_tablePath.setMinimumSize(QSize(386, 20))
        self.le_tablePath.setMaximumSize(QSize(386, 20))
        self.le_tablePath.setFont(font)

        self.horizontalLayout_27.addWidget(self.le_tablePath)


        self.gridLayout_2.addLayout(self.horizontalLayout_27, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_homePageSearch = QPushButton(self.layoutWidget_10)
        self.btn_homePageSearch.setObjectName(u"btn_homePageSearch")
        self.btn_homePageSearch.setEnabled(False)
        self.btn_homePageSearch.setMinimumSize(QSize(236, 23))
        self.btn_homePageSearch.setMaximumSize(QSize(236, 23))
        self.btn_homePageSearch.setCheckable(False)
        self.btn_homePageSearch.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_homePageSearch)

        self.btn_searchPageSearch = QPushButton(self.layoutWidget_10)
        self.btn_searchPageSearch.setObjectName(u"btn_searchPageSearch")
        self.btn_searchPageSearch.setMinimumSize(QSize(236, 23))
        self.btn_searchPageSearch.setMaximumSize(QSize(236, 23))

        self.horizontalLayout_3.addWidget(self.btn_searchPageSearch)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.layoutWidget_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(64, 23))
        self.label_5.setMaximumSize(QSize(64, 23))
        self.label_5.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.le_page = QLineEdit(self.layoutWidget_10)
        self.le_page.setObjectName(u"le_page")
        self.le_page.setMinimumSize(QSize(327, 20))
        self.le_page.setMaximumSize(QSize(327, 20))

        self.horizontalLayout_4.addWidget(self.le_page)

        self.btn_captureData = QPushButton(self.layoutWidget_10)
        self.btn_captureData.setObjectName(u"btn_captureData")
        self.btn_captureData.setMinimumSize(QSize(75, 23))
        self.btn_captureData.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_4.addWidget(self.btn_captureData)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_6 = QLabel(self.layoutWidget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(64, 23))
        self.label_6.setMaximumSize(QSize(64, 23))
        self.label_6.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label_6)

        self.pb_progressBar = QProgressBar(self.layoutWidget_10)
        self.pb_progressBar.setObjectName(u"pb_progressBar")
        self.pb_progressBar.setMinimumSize(QSize(327, 20))
        self.pb_progressBar.setMaximumSize(QSize(327, 20))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setUnderline(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.pb_progressBar.setFont(font5)
        self.pb_progressBar.setValue(0)
        self.pb_progressBar.setTextVisible(True)
        self.pb_progressBar.setOrientation(Qt.Horizontal)
        self.pb_progressBar.setInvertedAppearance(False)

        self.horizontalLayout_28.addWidget(self.pb_progressBar)

        self.btn_openExcel = QPushButton(self.layoutWidget_10)
        self.btn_openExcel.setObjectName(u"btn_openExcel")
        self.btn_openExcel.setMinimumSize(QSize(75, 23))
        self.btn_openExcel.setMaximumSize(QSize(75, 23))
        self.btn_openExcel.setFont(font)

        self.horizontalLayout_28.addWidget(self.btn_openExcel)


        self.gridLayout_2.addLayout(self.horizontalLayout_28, 6, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_23 = QLabel(self.layoutWidget_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(78, 72))
        self.label_23.setMaximumSize(QSize(78, 72))
        self.label_23.setFont(font)

        self.horizontalLayout_24.addWidget(self.label_23)

        self.te_gjc = QTextEdit(self.layoutWidget_10)
        self.te_gjc.setObjectName(u"te_gjc")
        self.te_gjc.setMinimumSize(QSize(393, 65))
        self.te_gjc.setMaximumSize(QSize(393, 65))

        self.horizontalLayout_24.addWidget(self.te_gjc)


        self.gridLayout_2.addLayout(self.horizontalLayout_24, 0, 0, 1, 1)

        self.layoutWidget_11 = QWidget(self.centralwidget)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(10, 320, 481, 31))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.layoutWidget_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(52, 20))
        self.label_4.setMaximumSize(QSize(52, 20))
        self.label_4.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_4)

        self.cb_provincial = QComboBox(self.layoutWidget_11)
        self.cb_provincial.setObjectName(u"cb_provincial")
        self.cb_provincial.setEnabled(True)
        self.cb_provincial.setMinimumSize(QSize(100, 20))
        self.cb_provincial.setMaximumSize(QSize(100, 20))
        self.cb_provincial.setFont(font)

        self.horizontalLayout_10.addWidget(self.cb_provincial)

        self.cb_city = QComboBox(self.layoutWidget_11)
        self.cb_city.setObjectName(u"cb_city")
        self.cb_city.setMinimumSize(QSize(120, 20))
        self.cb_city.setMaximumSize(QSize(120, 20))
        self.cb_city.setFont(font)

        self.horizontalLayout_10.addWidget(self.cb_city)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.layoutWidget_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(52, 20))
        self.label_9.setMaximumSize(QSize(52, 20))
        self.label_9.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.cb_informationType = QComboBox(self.layoutWidget_11)
        self.cb_informationType.setObjectName(u"cb_informationType")
        sizePolicy3.setHeightForWidth(self.cb_informationType.sizePolicy().hasHeightForWidth())
        self.cb_informationType.setSizePolicy(sizePolicy3)
        self.cb_informationType.setMinimumSize(QSize(120, 20))
        self.cb_informationType.setMaximumSize(QSize(120, 20))

        self.horizontalLayout_7.addWidget(self.cb_informationType)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)

        self.layoutWidget_12 = QWidget(self.centralwidget)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(10, 60, 481, 31))
        self.horizontalLayout_29 = QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.layoutWidget_12)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(40, 20))
        self.label_8.setMaximumSize(QSize(40, 20))
        self.label_8.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.le_proxy = QLineEdit(self.layoutWidget_12)
        self.le_proxy.setObjectName(u"le_proxy")
        sizePolicy5.setHeightForWidth(self.le_proxy.sizePolicy().hasHeightForWidth())
        self.le_proxy.setSizePolicy(sizePolicy5)
        self.le_proxy.setMinimumSize(QSize(291, 20))
        self.le_proxy.setMaximumSize(QSize(291, 20))
        self.le_proxy.setFont(font)

        self.horizontalLayout_9.addWidget(self.le_proxy)


        self.horizontalLayout_29.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.check_interface = QCheckBox(self.layoutWidget_12)
        self.check_interface.setObjectName(u"check_interface")
        sizePolicy1.setHeightForWidth(self.check_interface.sizePolicy().hasHeightForWidth())
        self.check_interface.setSizePolicy(sizePolicy1)
        self.check_interface.setMinimumSize(QSize(62, 20))
        self.check_interface.setMaximumSize(QSize(62, 20))
        self.check_interface.setFont(font)

        self.horizontalLayout_8.addWidget(self.check_interface)

        self.check_notEvidence = QCheckBox(self.layoutWidget_12)
        self.check_notEvidence.setObjectName(u"check_notEvidence")
        sizePolicy1.setHeightForWidth(self.check_notEvidence.sizePolicy().hasHeightForWidth())
        self.check_notEvidence.setSizePolicy(sizePolicy1)
        self.check_notEvidence.setMinimumSize(QSize(62, 20))
        self.check_notEvidence.setMaximumSize(QSize(62, 20))
        self.check_notEvidence.setFont(font)

        self.horizontalLayout_8.addWidget(self.check_notEvidence)


        self.horizontalLayout_29.addLayout(self.horizontalLayout_8)

        self.layoutWidget_13 = QWidget(self.centralwidget)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(10, 440, 494, 22))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 20))
        self.label_14.setMaximumSize(QSize(80, 20))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_14)

        self.rb_intelligentSearch = QRadioButton(self.layoutWidget_13)
        self.rb_intelligentSearch.setObjectName(u"rb_intelligentSearch")
        sizePolicy3.setHeightForWidth(self.rb_intelligentSearch.sizePolicy().hasHeightForWidth())
        self.rb_intelligentSearch.setSizePolicy(sizePolicy3)
        self.rb_intelligentSearch.setMinimumSize(QSize(200, 20))
        self.rb_intelligentSearch.setMaximumSize(QSize(200, 20))
        self.rb_intelligentSearch.setFont(font)
        self.rb_intelligentSearch.setChecked(True)

        self.horizontalLayout_16.addWidget(self.rb_intelligentSearch)

        self.rb_accurateSearch = QRadioButton(self.layoutWidget_13)
        self.rb_accurateSearch.setObjectName(u"rb_accurateSearch")
        sizePolicy3.setHeightForWidth(self.rb_accurateSearch.sizePolicy().hasHeightForWidth())
        self.rb_accurateSearch.setSizePolicy(sizePolicy3)
        self.rb_accurateSearch.setMinimumSize(QSize(200, 20))
        self.rb_accurateSearch.setMaximumSize(QSize(200, 20))
        self.rb_accurateSearch.setFont(font)

        self.horizontalLayout_16.addWidget(self.rb_accurateSearch)

        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 750, 30, 20))
        self.label_26.setMinimumSize(QSize(30, 20))
        self.label_26.setMaximumSize(QSize(30, 20))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 40, 1020, 20))
        self.label_7.setMinimumSize(QSize(1020, 20))
        self.label_7.setMaximumSize(QSize(1020, 20))
        font6 = QFont()
        font6.setFamilies([u"\u9ed1\u4f53"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"font: 10pt \"\u9ed1\u4f53\";\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0)")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.te_log = QTextBrowser(self.centralwidget)
        self.te_log.setObjectName(u"te_log")
        self.te_log.setGeometry(QRect(10, 610, 1000, 140))
        self.te_log.setMinimumSize(QSize(1000, 140))
        self.te_log.setMaximumSize(QSize(1000, 140))
        font7 = QFont()
        font7.setPointSize(10)
        self.te_log.setFont(font7)
        self.label_userInfo = QLabel(self.centralwidget)
        self.label_userInfo.setObjectName(u"label_userInfo")
        self.label_userInfo.setGeometry(QRect(0, 10, 500, 20))
        self.label_userInfo.setMinimumSize(QSize(500, 20))
        self.label_userInfo.setMaximumSize(QSize(500, 20))
        self.label_userInfo.setFont(font7)
        self.label_userInfo.setStyleSheet(u"background: rgb(194, 255, 250);\n"
"border-radius:10px;\n"
"color:rgb(0, 0, 0);")
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(590, 10, 420, 26))
        self.horizontalLayout_32 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.btn_keep = QPushButton(self.layoutWidget1)
        self.btn_keep.setObjectName(u"btn_keep")
        self.btn_keep.setMinimumSize(QSize(100, 24))
        self.btn_keep.setMaximumSize(QSize(100, 24))
        self.btn_keep.setFont(font7)

        self.horizontalLayout_32.addWidget(self.btn_keep)

        self.btn_changePassword = QPushButton(self.layoutWidget1)
        self.btn_changePassword.setObjectName(u"btn_changePassword")
        self.btn_changePassword.setMinimumSize(QSize(100, 24))
        self.btn_changePassword.setMaximumSize(QSize(100, 24))
        self.btn_changePassword.setFont(font7)

        self.horizontalLayout_32.addWidget(self.btn_changePassword)

        self.btn_switchUser = QPushButton(self.layoutWidget1)
        self.btn_switchUser.setObjectName(u"btn_switchUser")
        self.btn_switchUser.setMinimumSize(QSize(100, 24))
        self.btn_switchUser.setMaximumSize(QSize(100, 24))
        self.btn_switchUser.setSizeIncrement(QSize(0, 0))
        self.btn_switchUser.setFont(font7)

        self.horizontalLayout_32.addWidget(self.btn_switchUser)

        self.btn_quit = QPushButton(self.layoutWidget1)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setMinimumSize(QSize(100, 24))
        self.btn_quit.setMaximumSize(QSize(100, 24))
        self.btn_quit.setFont(font7)

        self.horizontalLayout_32.addWidget(self.btn_quit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_homePageSearch.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u722c\u866b\u8ba1\u5212-\u4e3b\u754c\u9762", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u65f6\u95f4", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.cb_dateChoose.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u9009\u62e9\u65e5\u671f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u7528\u6237\u540d:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u5bc6\u7801:</p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u72ec\u7acb\u8fd0\u884c\u7a0b\u5e8f", None))
        self.btn_chooseDoc.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u6863", None))
        self.le_docPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.btn_startClean.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6e05\u7406", None))
        self.pte_clean_gjc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5982\u5bf9\u6807\u9898\u4e2d\u542b\u6709\u7684\u67d0\u4e9b\u5173\u952e\u8bcd\uff0c\u8fd8\u6709\u53e6\u5916\u4e8c\u6b21\u6e05\u7406\u7684\u9700\u6c42\uff0c\u8bf7\u5728\u6b64\u586b\u5199\uff0c\u591a\u4e2a\u5173\u952e\u8bcd\u53ef\u7528\u82f1\u6587\u9017\u53f7\u201c,\u201d\u9694\u5f00", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u8fdb\u5ea6", None))
        self.btn_openDoc.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u6587\u6863", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u8d28\u8bc1\u4e66", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u76f8\u4f3c\u5ea6\n"
"(\u53bb\u91cd\u590d\u7387)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u91d1\u989d", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u91d1\u989d(\u4e07\u5143)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cb_customAmount.setText("")
        self.btn_qd.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9webdriver\u9a71\u52a8", None))
        self.le_driverPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u5668\u9a71\u52a8\u8def\u5f84", None))
        self.radio_edge.setText(QCoreApplication.translate("MainWindow", u"Microsoft Edge", None))
        self.radio_chrome.setText(QCoreApplication.translate("MainWindow", u"Chrome", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009\u8303\u56f4", None))
        self.rb_fullTextInclludingAttachments.setText(QCoreApplication.translate("MainWindow", u"\u5168\u6587\u641c\u7d22\u542b\u9644\u4ef6", None))
        self.rb_titleSearch.setText(QCoreApplication.translate("MainWindow", u"\u6807\u9898\u641c\u7d22 ", None))
        self.rb_fullTextNoAttachment.setText(QCoreApplication.translate("MainWindow", u"\u5168\u6587\u641c\u7d22\u4e0d\u542b\u9644\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u641c\u7d22\u5173\u952e\u8bcd", None))
        self.te_searchBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u641c\u7d22\u5173\u952e\u8bcd", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"by-\u5f6d\u4fca\u5091", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u65b9\u5f0f", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u91d1\u6765\u6e90", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u6807\u529e\u6cd5", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009\u7684\u884c\u4e1a\n"
"\u5173\u952e\u8bcd", None))
        self.te_hy.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u4ece\u6807\u9898\u4e2d\u7b5b\u9009\u7684\u884c\u4e1a\u5173\u952e\u8bcd\u5f52\u7eb3\uff0c\u591a\u4e2a\u5173\u952e\u8bcd\u53ef\u7528\u82f1\u6587\u9017\u53f7\",\"\u9694\u5f00", None))
        self.rb_cleanGjc.setText(QCoreApplication.translate("MainWindow", u"\u9700\u6e05\u7406\u6807\u9898\u4e2d\u542b\u6709\u7684\u5173\u952e\u8bcd", None))
        self.rb_saveGjc.setText(QCoreApplication.translate("MainWindow", u"\u4ec5\u4fdd\u7559\u6807\u9898\u4e2d\u542b\u6709\u7684\u5173\u952e\u8bcd", None))
        self.pte_cleanORsave_gjc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u9700\u8981\u6e05\u7406\u6807\u9898\u4e2d\u542b\u6709\u67d0\u4e2a\u5173\u952e\u8bcd\u7684/\u4ec5\u4fdd\u7559\u6807\u9898\u4e2d\u542b\u6709\u67d0\u4e2a\u5173\u952e\u8bcd\u7684\uff0c\u591a\u4e2a\u5173\u952e\u8bcd\u53ef\u7528\u82f1\u6587\",\"\u9694\u5f00", None))
        self.btn_choosePosition.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5b58\u50a8\u4f4d\u7f6e", None))
        self.le_tablePath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.btn_homePageSearch.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875\u9762\u641c\u7d22", None))
        self.btn_searchPageSearch.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u9875\u9762\u641c\u7d22", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u722c\u53d6\u9875\u6570", None))
        self.le_page.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u9875\u6570", None))
        self.btn_captureData.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u722c\u53d6", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u8fdb\u5ea6", None))
        self.btn_openExcel.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u6587\u6863", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009\u7684\u5173\u952e\u8bcd", None))
        self.te_gjc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u4ece\u6807\u9898\u4e2d\u7b5b\u9009\u7684\u5173\u952e\u8bcd\u5f52\u7eb3\uff0c\u591a\u4e2a\u5173\u952e\u8bcd\u53ef\u7528\u82f1\u6587\u9017\u53f7\",\"\u9694\u5f00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5730\u533a\u8303\u56f4", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u7c7b\u578b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406IP", None))
        self.check_interface.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u754c\u9762", None))
        self.check_notEvidence.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u7559\u75d5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009\u6a21\u5f0f", None))
        self.rb_intelligentSearch.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u641c\u7d22", None))
        self.rb_accurateSearch.setText(QCoreApplication.translate("MainWindow", u"\u7cbe\u51c6\u641c\u7d22", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"V 0.1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u62db\u7f51\u6293\u53d6\u4fe1\u606f", None))
        self.label_userInfo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_keep.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.btn_changePassword.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5bc6\u7801", None))
        self.btn_switchUser.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u7528\u6237", None))
        self.btn_quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
    # retranslateUi

