# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BCalculator_main v2znMOcF.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_CalcForm(object):
    def setupUi(self, CalcForm):
        if not CalcForm.objectName():
            CalcForm.setObjectName(u"CalcForm")
        CalcForm.resize(360, 300)
        self.textBrowser = QTextBrowser(CalcForm)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 20, 341, 51))
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.BtnCAGR = QPushButton(CalcForm)
        self.BtnCAGR.setObjectName(u"BtnCAGR")
        self.BtnCAGR.setGeometry(QRect(10, 80, 61, 31))
        self.BtnCancel = QPushButton(CalcForm)
        self.BtnCancel.setObjectName(u"BtnCancel")
        self.BtnCancel.setGeometry(QRect(80, 80, 61, 31))
        self.BtnClear = QPushButton(CalcForm)
        self.BtnClear.setObjectName(u"BtnClear")
        self.BtnClear.setGeometry(QRect(150, 80, 61, 31))
        self.BtnSquare = QPushButton(CalcForm)
        self.BtnSquare.setObjectName(u"BtnSquare")
        self.BtnSquare.setGeometry(QRect(220, 80, 61, 31))
        self.BtnPlusminus = QPushButton(CalcForm)
        self.BtnPlusminus.setObjectName(u"BtnPlusminus")
        self.BtnPlusminus.setGeometry(QRect(290, 80, 61, 31))
        self.BtnIRR = QPushButton(CalcForm)
        self.BtnIRR.setObjectName(u"BtnIRR")
        self.BtnIRR.setGeometry(QRect(10, 120, 61, 31))
        self.BtnSeven = QPushButton(CalcForm)
        self.BtnSeven.setObjectName(u"BtnSeven")
        self.BtnSeven.setGeometry(QRect(80, 120, 61, 31))
        self.BtnEight = QPushButton(CalcForm)
        self.BtnEight.setObjectName(u"BtnEight")
        self.BtnEight.setGeometry(QRect(150, 120, 61, 31))
        self.BtnNine = QPushButton(CalcForm)
        self.BtnNine.setObjectName(u"BtnNine")
        self.BtnNine.setGeometry(QRect(220, 120, 61, 31))
        self.BtnDivide = QPushButton(CalcForm)
        self.BtnDivide.setObjectName(u"BtnDivide")
        self.BtnDivide.setGeometry(QRect(290, 120, 61, 31))
        self.BtnROE = QPushButton(CalcForm)
        self.BtnROE.setObjectName(u"BtnROE")
        self.BtnROE.setGeometry(QRect(10, 160, 61, 31))
        self.BtnFour = QPushButton(CalcForm)
        self.BtnFour.setObjectName(u"BtnFour")
        self.BtnFour.setGeometry(QRect(80, 160, 61, 31))
        self.BtnFive = QPushButton(CalcForm)
        self.BtnFive.setObjectName(u"BtnFive")
        self.BtnFive.setGeometry(QRect(150, 160, 61, 31))
        self.BtnSix = QPushButton(CalcForm)
        self.BtnSix.setObjectName(u"BtnSix")
        self.BtnSix.setGeometry(QRect(220, 160, 61, 31))
        self.BtnMultiply = QPushButton(CalcForm)
        self.BtnMultiply.setObjectName(u"BtnMultiply")
        self.BtnMultiply.setGeometry(QRect(290, 160, 61, 31))
        self.BtnOne = QPushButton(CalcForm)
        self.BtnOne.setObjectName(u"BtnOne")
        self.BtnOne.setGeometry(QRect(80, 200, 61, 31))
        self.BtnNPV = QPushButton(CalcForm)
        self.BtnNPV.setObjectName(u"BtnNPV")
        self.BtnNPV.setGeometry(QRect(10, 200, 61, 31))
        self.BtnTwo = QPushButton(CalcForm)
        self.BtnTwo.setObjectName(u"BtnTwo")
        self.BtnTwo.setGeometry(QRect(150, 200, 61, 31))
        self.BtnThree = QPushButton(CalcForm)
        self.BtnThree.setObjectName(u"BtnThree")
        self.BtnThree.setGeometry(QRect(220, 200, 61, 31))
        self.BtnMinus = QPushButton(CalcForm)
        self.BtnMinus.setObjectName(u"BtnMinus")
        self.BtnMinus.setGeometry(QRect(290, 200, 61, 31))
        self.BtnLbracket = QPushButton(CalcForm)
        self.BtnLbracket.setObjectName(u"BtnLbracket")
        self.BtnLbracket.setGeometry(QRect(10, 240, 31, 31))
        self.BtnEqual = QPushButton(CalcForm)
        self.BtnEqual.setObjectName(u"BtnEqual")
        self.BtnEqual.setGeometry(QRect(220, 240, 61, 31))
        self.BtnAdd = QPushButton(CalcForm)
        self.BtnAdd.setObjectName(u"BtnAdd")
        self.BtnAdd.setGeometry(QRect(290, 240, 61, 31))
        self.BtnDot = QPushButton(CalcForm)
        self.BtnDot.setObjectName(u"BtnDot")
        self.BtnDot.setGeometry(QRect(150, 240, 61, 31))
        self.BtnZero = QPushButton(CalcForm)
        self.BtnZero.setObjectName(u"BtnZero")
        self.BtnZero.setGeometry(QRect(80, 240, 61, 31))
        self.BtnRbracket = QPushButton(CalcForm)
        self.BtnRbracket.setObjectName(u"BtnRbracket")
        self.BtnRbracket.setGeometry(QRect(40, 240, 31, 31))

        self.retranslateUi(CalcForm)

        QMetaObject.connectSlotsByName(CalcForm)
    # setupUi

    def retranslateUi(self, CalcForm):
        CalcForm.setWindowTitle(QCoreApplication.translate("CalcForm", u"B-Calculator v2.0", None))
        self.BtnCAGR.setText(QCoreApplication.translate("CalcForm", u"CAGR", None))
        self.BtnCancel.setText(QCoreApplication.translate("CalcForm", u"\u64a4\u9500", None))
        self.BtnClear.setText(QCoreApplication.translate("CalcForm", u"\u6e05\u9664", None))
        self.BtnSquare.setText(QCoreApplication.translate("CalcForm", u"x^y", None))
        self.BtnPlusminus.setText(QCoreApplication.translate("CalcForm", u"+/-", None))
        self.BtnIRR.setText(QCoreApplication.translate("CalcForm", u"IRR", None))
        self.BtnSeven.setText(QCoreApplication.translate("CalcForm", u"7", None))
        self.BtnEight.setText(QCoreApplication.translate("CalcForm", u"8", None))
        self.BtnNine.setText(QCoreApplication.translate("CalcForm", u"9", None))
        self.BtnDivide.setText(QCoreApplication.translate("CalcForm", u"/", None))
        self.BtnROE.setText(QCoreApplication.translate("CalcForm", u"ROE", None))
        self.BtnFour.setText(QCoreApplication.translate("CalcForm", u"4", None))
        self.BtnFive.setText(QCoreApplication.translate("CalcForm", u"5", None))
        self.BtnSix.setText(QCoreApplication.translate("CalcForm", u"6", None))
        self.BtnMultiply.setText(QCoreApplication.translate("CalcForm", u"x", None))
        self.BtnOne.setText(QCoreApplication.translate("CalcForm", u"1", None))
        self.BtnNPV.setText(QCoreApplication.translate("CalcForm", u"NPV", None))
        self.BtnTwo.setText(QCoreApplication.translate("CalcForm", u"2", None))
        self.BtnThree.setText(QCoreApplication.translate("CalcForm", u"3", None))
        self.BtnMinus.setText(QCoreApplication.translate("CalcForm", u"-", None))
        self.BtnLbracket.setText(QCoreApplication.translate("CalcForm", u"(", None))
        self.BtnEqual.setText(QCoreApplication.translate("CalcForm", u"=", None))
        self.BtnAdd.setText(QCoreApplication.translate("CalcForm", u"+", None))
        self.BtnDot.setText(QCoreApplication.translate("CalcForm", u".", None))
        self.BtnZero.setText(QCoreApplication.translate("CalcForm", u"0", None))
        self.BtnRbracket.setText(QCoreApplication.translate("CalcForm", u")", None))
    # retranslateUi

