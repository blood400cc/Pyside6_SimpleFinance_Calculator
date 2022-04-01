# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BCalculator_NPV v2HkMkkP.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QLabel, QPushButton,
    QSizePolicy, QTextEdit)

class Ui_DialogNPV(object):
    def setupUi(self, DialogNPV):
        if not DialogNPV.objectName():
            DialogNPV.setObjectName(u"DialogNPV")
        DialogNPV.resize(399, 233)
        self.label = QLabel(DialogNPV)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 91, 16))
        self.NPVyear0invest = QTextEdit(DialogNPV)
        self.NPVyear0invest.setObjectName(u"NPVyear0invest")
        self.NPVyear0invest.setGeometry(QRect(110, 20, 71, 21))
        self.NPVyear0invest.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyear0invest.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyear1r = QTextEdit(DialogNPV)
        self.NPVyear1r.setObjectName(u"NPVyear1r")
        self.NPVyear1r.setGeometry(QRect(90, 60, 91, 21))
        self.NPVyear1r.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyear1r.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_2 = QLabel(DialogNPV)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 62, 81, 16))
        self.label_3 = QLabel(DialogNPV)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 91, 81, 16))
        self.NPVyear3r = QTextEdit(DialogNPV)
        self.NPVyear3r.setObjectName(u"NPVyear3r")
        self.NPVyear3r.setGeometry(QRect(90, 90, 91, 21))
        self.NPVyear3r.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyear3r.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_4 = QLabel(DialogNPV)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 122, 81, 16))
        self.NPVyear5r = QTextEdit(DialogNPV)
        self.NPVyear5r.setObjectName(u"NPVyear5r")
        self.NPVyear5r.setGeometry(QRect(90, 120, 91, 21))
        self.NPVyear5r.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyear5r.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_6 = QLabel(DialogNPV)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 62, 81, 16))
        self.NPVyear2r = QTextEdit(DialogNPV)
        self.NPVyear2r.setObjectName(u"NPVyear2r")
        self.NPVyear2r.setGeometry(QRect(290, 60, 91, 21))
        self.NPVyear2r.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyear2r.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_7 = QLabel(DialogNPV)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 91, 81, 16))
        self.NPVyear4r = QTextEdit(DialogNPV)
        self.NPVyear4r.setObjectName(u"NPVyear4r")
        self.NPVyear4r.setGeometry(QRect(290, 90, 91, 21))
        self.NPVyear4r.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyear4r.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_8 = QLabel(DialogNPV)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 122, 81, 16))
        self.NPVyear6r = QTextEdit(DialogNPV)
        self.NPVyear6r.setObjectName(u"NPVyear6r")
        self.NPVyear6r.setGeometry(QRect(290, 120, 91, 21))
        self.NPVyear6r.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyear6r.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyearfn = QTextEdit(DialogNPV)
        self.NPVyearfn.setObjectName(u"NPVyearfn")
        self.NPVyearfn.setGeometry(QRect(190, 160, 191, 21))
        self.NPVyearfn.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVyearfn.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.label_12 = QLabel(DialogNPV)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 160, 161, 16))
        self.BtnNPVok = QPushButton(DialogNPV)
        self.BtnNPVok.setObjectName(u"BtnNPVok")
        self.BtnNPVok.setGeometry(QRect(150, 200, 75, 24))
        self.BtnNPVclear = QPushButton(DialogNPV)
        self.BtnNPVclear.setObjectName(u"BtnNPVclear")
        self.BtnNPVclear.setGeometry(QRect(230, 200, 75, 24))
        self.BtnNPVclose = QPushButton(DialogNPV)
        self.BtnNPVclose.setObjectName(u"BtnNPVclose")
        self.BtnNPVclose.setGeometry(QRect(310, 200, 75, 24))
        self.label_13 = QLabel(DialogNPV)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 20, 91, 16))
        self.NPVirate = QTextEdit(DialogNPV)
        self.NPVirate.setObjectName(u"NPVirate")
        self.NPVirate.setGeometry(QRect(300, 20, 81, 21))
        self.NPVirate.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NPVirate.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.retranslateUi(DialogNPV)

        QMetaObject.connectSlotsByName(DialogNPV)
    # setupUi

    def retranslateUi(self, DialogNPV):
        DialogNPV.setWindowTitle(QCoreApplication.translate("DialogNPV", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogNPV", u"\u521d\u59cb\u6295\u8d44(\u6b63\u6570)\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("DialogNPV", u"\u7b2c\u4e00\u671f\u6536\u76ca\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("DialogNPV", u"\u7b2c\u4e09\u671f\u6536\u76ca\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("DialogNPV", u"\u7b2c\u4e94\u671f\u6536\u76ca\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("DialogNPV", u"\u7b2c\u4e8c\u671f\u6536\u76ca\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("DialogNPV", u"\u7b2c\u56db\u671f\u6536\u76ca\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("DialogNPV", u"\u7b2c\u516d\u671f\u6536\u76ca\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("DialogNPV", u"\u540e\u7eed\u6536\u76ca\uff08\u4ee5\u82f1\u6587\u9017\u53f7\u5206\u9694\uff09\uff1a", None))
        self.BtnNPVok.setText(QCoreApplication.translate("DialogNPV", u"\u786e\u8ba4", None))
        self.BtnNPVclear.setText(QCoreApplication.translate("DialogNPV", u"\u6e05\u7a7a", None))
        self.BtnNPVclose.setText(QCoreApplication.translate("DialogNPV", u"\u9000\u51fa", None))
        self.label_13.setText(QCoreApplication.translate("DialogNPV", u"\u8d44\u91d1\u6210\u672c(%)\uff1a", None))
    # retranslateUi

