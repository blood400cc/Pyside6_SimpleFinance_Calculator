# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BCalculator_CAGR v2EMnQwf.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QPushButton, QTextEdit, )

class Ui_DialogCAGR(object):
    def setupUi(self, DialogCAGR):
        if not DialogCAGR.objectName():
            DialogCAGR.setObjectName(u"DialogCAGR")
        DialogCAGR.resize(401, 132)
        self.CAGRStartyear = QTextEdit(DialogCAGR)
        self.CAGRStartyear.setObjectName(u"CAGRStartyear")
        self.CAGRStartyear.setGeometry(QRect(90, 20, 101, 21))
        self.CAGRStartyear.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CAGRStartyear.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label = QLabel(DialogCAGR)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setToolTipDuration(1)
        self.BtnCAGRok = QPushButton(DialogCAGR)
        self.BtnCAGRok.setObjectName(u"BtnCAGRok")
        self.BtnCAGRok.setGeometry(QRect(146, 100, 75, 24))
        self.BtnCAGRcancel = QPushButton(DialogCAGR)
        self.BtnCAGRcancel.setObjectName(u"BtnCAGRcancel")
        self.BtnCAGRcancel.setGeometry(QRect(226, 100, 75, 24))
        self.BtnCAGRquit = QPushButton(DialogCAGR)
        self.BtnCAGRquit.setObjectName(u"BtnCAGRquit")
        self.BtnCAGRquit.setGeometry(QRect(306, 100, 75, 24))
        self.label_2 = QLabel(DialogCAGR)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 20, 81, 16))
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(1)
        self.CAGREndyear = QTextEdit(DialogCAGR)
        self.CAGREndyear.setObjectName(u"CAGREndyear")
        self.CAGREndyear.setGeometry(QRect(280, 20, 101, 21))
        self.CAGREndyear.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CAGREndyear.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_3 = QLabel(DialogCAGR)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 81, 16))
        self.label_3.setFont(font)
        self.label_3.setToolTipDuration(1)
        self.label_4 = QLabel(DialogCAGR)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 60, 81, 16))
        self.label_4.setFont(font)
        self.label_4.setToolTipDuration(1)
        self.CAGRStartvalue = QTextEdit(DialogCAGR)
        self.CAGRStartvalue.setObjectName(u"CAGRStartvalue")
        self.CAGRStartvalue.setGeometry(QRect(90, 60, 101, 21))
        self.CAGRStartvalue.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CAGRStartvalue.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CAGREndvalue = QTextEdit(DialogCAGR)
        self.CAGREndvalue.setObjectName(u"CAGREndvalue")
        self.CAGREndvalue.setGeometry(QRect(280, 60, 101, 21))
        self.CAGREndvalue.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CAGREndvalue.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.retranslateUi(DialogCAGR)

        QMetaObject.connectSlotsByName(DialogCAGR)
    # setupUi

    def retranslateUi(self, DialogCAGR):
        DialogCAGR.setWindowTitle(QCoreApplication.translate("DialogCAGR", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("DialogCAGR", u"\u56db\u4f4d\u6570\u5e74\u4efd \u59822016", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("DialogCAGR", u"\u8d77\u59cb\u5e74\u4efd\uff1a", None))
        self.BtnCAGRok.setText(QCoreApplication.translate("DialogCAGR", u"\u786e\u8ba4", None))
        self.BtnCAGRcancel.setText(QCoreApplication.translate("DialogCAGR", u"\u6e05\u7a7a", None))
        self.BtnCAGRquit.setText(QCoreApplication.translate("DialogCAGR", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DialogCAGR", u"\u56db\u4f4d\u6570\u5e74\u4efd \u59822016", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DialogCAGR", u"\u7ec8\u6b62\u5e74\u4efd\uff1a", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("DialogCAGR", u"\u56db\u4f4d\u6570\u5e74\u4efd \u59822016", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("DialogCAGR", u"\u8d77\u59cb\u503c\uff1a", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("DialogCAGR", u"\u56db\u4f4d\u6570\u5e74\u4efd \u59822016", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("DialogCAGR", u"\u7ec8\u6b62\u503c\uff1a", None))
    # retranslateUi

