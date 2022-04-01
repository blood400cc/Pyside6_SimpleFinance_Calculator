# -*- coding : utf-8-*-
# coding:unicode_escape

#from PySide6.QtGui import *
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
#from PySide6.QtCore import *
import sys
import numpy_financial as npf
from ui_BCalculator_main import Ui_CalcForm
from ui_BCalculator_CAGR import Ui_DialogCAGR
from ui_BCalculator_IRR import Ui_DialogIRR
from ui_BCalculator_NPV import Ui_DialogNPV
from ui_BCalculator_ROE import Ui_DialogROE
from PySide6.QtCore import Signal

class MainWindow(QWidget):
     def __init__(self):
         QWidget.__init__(self)
         self.ui= Ui_CalcForm()
         self.ui.setupUi(self)
         global fLen  # float accuracy contrl
         global dCount  # window clear control
         fLen = 3
         dCount = 1
        # bind button to functions
         self.ui.BtnMultiply.clicked.connect(self.OnClick)
         self.ui.BtnMinus.pressed.connect(self.OnClick)
         self.ui.BtnAdd.pressed.connect(self.OnClick)
         self.ui.BtnDivide.pressed.connect(self.OnClick)
         self.ui.BtnSquare.pressed.connect(self.OnClick)
         self.ui.BtnDot.pressed.connect(self.OnClick)
         self.ui.BtnEqual.pressed.connect(self.OnCompute)
         self.ui.BtnOne.pressed.connect(self.OnClick)
         self.ui.BtnTwo.pressed.connect(self.OnClick)
         self.ui.BtnThree.pressed.connect(self.OnClick)
         self.ui.BtnFour.pressed.connect(self.OnClick)
         self.ui.BtnFive.pressed.connect(self.OnClick)
         self.ui.BtnSix.pressed.connect(self.OnClick)
         self.ui.BtnSeven.pressed.connect(self.OnClick)
         self.ui.BtnEight.pressed.connect(self.OnClick)
         self.ui.BtnNine.pressed.connect(self.OnClick)
         self.ui.BtnZero.pressed.connect(self.OnClick)
         self.ui.BtnCAGR.pressed.connect(self.OnDialogCAGR)
         self.ui.BtnIRR.pressed.connect(self.OnDialogIRR)
         self.ui.BtnROE.pressed.connect(self.OnDialogROE)
         self.ui.BtnLbracket.pressed.connect(self.OnClick)
         self.ui.BtnRbracket.pressed.connect(self.OnClick)
         self.ui.BtnNPV.pressed.connect(self.OnDialogNPV)
         self.ui.BtnCancel.pressed.connect(self.OnCancel)
         self.ui.BtnClear.pressed.connect(self.OnClear)
         self.ui.BtnPlusminus.pressed.connect(self.OnReverse)


# main input module
     def OnClick(self):
         global dCount
         sender = self.sender()
         self.Cleardisplay(sender.text())
         if sender.text() == "x^y":
            self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText() + "**")
         elif sender.text() == "x":
            self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText() + "*")
         else:
            self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText()+sender.text())
         dCount = 1
     def Cleardisplay(self, symbol):
         global dCount
         if dCount == 0:
             if symbol == "+" or symbol == "-" or symbol == "x" or symbol == "/" or symbol == "x^y":
                 dCount = 1
             else:
                 self.ui.textBrowser.setText('')
         else: return()

# main calculate module
     def OnCompute(self):
         if self.ui.textBrowser.toPlainText() != '':
             aTemp = str(float(eval(self.ui.textBrowser.toPlainText())))
             bTemp = self.FloatControl(aTemp)
             self.ui.textBrowser.setText(bTemp)
         global dCount
         dCount = 0

# Assist module
     def OnCancel(self):
         lEn = len(self.ui.textBrowser.toPlainText())
         aInput = self.ui.textBrowser.toPlainText()
         self.ui.textBrowser.setText(str(aInput[0:(lEn - 1)]))
     def OnClear(self):
         self.ui.textBrowser.setText('')
     def OnReverse(self):
         self.ui.textBrowser.setText(str('-('+self.ui.textBrowser.toPlainText()+')'))
     def FloatControl(self, aTemp):
         global fLen
         iCount = 0
         for i in aTemp:
             if i != ".":
                 iCount = iCount + 1
             else:
                 bTemp = aTemp[0:(iCount + (fLen + 1))]
         return bTemp

# Extra function - signal receive from subwindows of extra function
     def getSubwininfo(self, subarg):  # # 主窗口的槽函数, subarg会承载一个从子窗口传回的信号
         self.ui.textBrowser.setText(subarg)
# Extra function - CAGR
     def OnDialogCAGR(self):
         # 注意，这里的dialgoCAGR不能定义成临时变量，必须定义成主窗口类MainWindow的成员变量，如果是临时变量，即前面没有self，那么子窗口只会闪一下，就会消失
         self.dialogCAGR = dialogCAGR()
         self.dialogCAGR.show() #这两句是能够让子窗口显示的关键
         self.dialogCAGR.sub_Signal.connect(self.getSubwininfo) # # 子窗口信号连接主窗口的槽函数
# Extra function - IRR
     def OnDialogIRR(self):
         self.dialogIRR = dialogIRR()
         self.dialogIRR.show() #这两句是能够让子窗口显示的关键
         self.dialogIRR.sub_Signal.connect(self.getSubwininfo) # # 子窗口信号连接主窗口的槽函数
# Extra function - NPV
     def OnDialogNPV(self):
         self.dialogNPV = dialogNPV()
         self.dialogNPV.show()  # 这两句是能够让子窗口显示的关键
         self.dialogNPV.sub_Signal.connect(self.getSubwininfo)  # # 子窗口信号连接主窗口的槽函数
# Extra function - ROE
     def OnDialogROE(self):
         self.dialogROE = dialogROE()
         self.dialogROE.show()  # 这两句是能够让子窗口显示的关键
         self.dialogROE.sub_Signal.connect(self.getSubwininfo)  # # 子窗口信号连接主窗口的槽函数

# for function under construction
     def OnGoing(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Under Construction")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()
# Extra function - CAGR sub-dialog class
class dialogCAGR(QDialog):
    sub_Signal = Signal(str)
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_DialogCAGR()
        self.ui.setupUi(self)
        self.ui.BtnCAGRok.pressed.connect(self.DisplayCAGRanswer)
        self.ui.BtnCAGRcancel.pressed.connect(self.DisplayCAGRclear)
        self.ui.BtnCAGRquit.pressed.connect(self.DisplayCAGRquit)
    def DisplayCAGRanswer(self):
        CGstartyear=eval(self.ui.CAGRStartyear.toPlainText())
        CGendyear=eval(self.ui.CAGREndyear.toPlainText())
        CGstartvalue=eval(self.ui.CAGRStartvalue.toPlainText())
        CGendvalue=eval(self.ui.CAGREndvalue.toPlainText())
        if self.ValidateInput(CGstartyear,CGendyear) == 1:
            CAGRTemp = ((CGendvalue) / CGstartvalue) ** (1 / (CGendyear - CGstartyear)) - 1
            global dCount
            dCount = 0
        # window.ui.textBrowser.setText(CAGRtemp) ## option 2 - 直接调用主窗口类的全局实例window，直接赋值textbrowser的值，一句话完成数值在不同窗口之间的传递
        #bb = "%.2f%%" % (CAGRTemp * 100) ## 这是另外一种百分比转换，可以直接做出精度控制。
        bb = window.FloatControl(str(CAGRTemp * 100)) + '%'
        CAGRAnswer=str(bb) # 传递回的值仍必须是个str 值，此处做成%比值，但有个问题，如果继续在主界面用运算符运算，%分号不能被识别将报错，待解决
        self.sub_Signal.emit(CAGRAnswer) ## option1 - 发射一个信号，由主窗口的信号槽接受，利用了pyside的信号槽机制，但比option2复杂一些，两个窗口类之间需要设置收发机制；出于学习目的保留在这里
    def ValidateInput(self, Startyear, Endyear):
        if len(str(Startyear)) == 4 and len(str(Endyear)) == 4 and Startyear <= Endyear:
            return 1
        else:
            print("please input four digit year number like 1977")
    def DisplayCAGRclear(self):
        self.ui.CAGRStartyear.setText('')
    def DisplayCAGRquit(self):
        self.close()

# Extra function - IRR sub-dialog class
class dialogIRR(QDialog):
    sub_Signal = Signal(str)
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_DialogIRR()
        self.ui.setupUi(self)
        self.ui.BtnIRRok.pressed.connect(self.DisplayIRRanswer)
        self.ui.BtnIRRclear.pressed.connect(self.DisplayIRRclear)
        self.ui.BtnIRRclose.pressed.connect(self.DisplayIRRquit)
    def CalcNpv(self, rate, cashflows):
        total = 0.0
        for i, cashflow in enumerate(cashflows):
            total += cashflow / (1 + rate)**i
            #print(total)
        return total
    def JudIrr(self, cashflow):
        temp=0
        for cash in cashflow:
            temp += cash
        temp1=temp-cashflow[0]
        return temp1
    def DisplayIRRanswer(self,itr=100):
        money_i=-(eval(self.EmpControl(self.ui.IRRyear0invest.toPlainText())))
        if money_i<0:
            money_1 = eval(self.EmpControl(self.ui.IRRyear1r.toPlainText()))
            money_2 = eval(self.EmpControl(self.ui.IRRyear2r.toPlainText()))
            money_3 = eval(self.EmpControl(self.ui.IRRyear3r.toPlainText()))
            money_4 = eval(self.EmpControl(self.ui.IRRyear4r.toPlainText()))
            money_5 = eval(self.EmpControl(self.ui.IRRyear5r.toPlainText()))
            money_6 = eval(self.EmpControl(self.ui.IRRyear6r.toPlainText()))
            money_7 = eval(self.EmpControl(self.ui.IRRyear7r.toPlainText()))
            money_8 = eval(self.EmpControl(self.ui.IRRyear8r.toPlainText()))
            money_9 = eval(self.EmpControl(self.ui.IRRyear9r.toPlainText()))
            money_10 = eval(self.EmpControl(self.ui.IRRyear10r.toPlainText()))
            money_r=[money_i,money_1,money_2,money_3,money_4,money_5,money_6,money_7,money_8,money_9,money_10]
            money_f = eval(self.EmpControl(self.ui.IRRyearfr.toPlainText()))
            print (type(money_f))
            if type(money_f)==type(1):
                money_r.append(money_f)
            else:
                money_r.extend(money_f)
            cashflows=money_r
            if self.JudIrr(cashflows)>0:
                IRRAnswertemp = str(npf.irr(cashflows))
                IRRAnswer = window.FloatControl(IRRAnswertemp)
                self.sub_Signal.emit(IRRAnswer)
            else: print ("negative return on this project")
        else: print ("Please input plus number")
        """
         ---------------------------- here instead using numpy financial's input
         values = np.atleast_1d(values)
         if values.ndim != 1:
             raise ValueError("Cashflows must be a rank-1 array")

         # Strip leading and trailing zeros. Since we only care about
         # positive roots we can neglect roots at zero.
         non_zero = np.nonzero(np.ravel(values))[0]
         values = values[int(non_zero[0]):int(non_zero[-1])+1]

         res = _roots(values[::-1])

         mask = (res.imag == 0) & (res.real > 0)
         if not mask.any():
             return np.nan
         res = res[mask].real
         # NPV(rate) = 0 can have more than one solution so we return
         # only the solution closest to zero.
         rate = 1/res - 1
         rate = rate.item(np.argmin(np.abs(rate)))
         return rate 
         """
    def EmpControl(self, temp):
        if temp != "":
            return temp
        else:
            return "0"
    def DisplayIRRclear(self):
        self.ui.IRRyear0invest.setText('')
        for i in range(1, 7):
            labletemp = f"IRRyear{i}r"  # 此处为了做清空简洁的遍历所有输入框，使用了f“{}”来连接字符串和变量i
            exec(f"self.ui.{labletemp}.setText('')")  # 因为f“”的结果只是个文本字符串，不能直接执行，此处用到了执行命令exec()
    def DisplayIRRquit(self):
        self.close()


# Extra function - NPV sub-dialog class
class dialogNPV(QDialog):
    sub_Signal = Signal(str)

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_DialogNPV()
        self.ui.setupUi(self)
        self.ui.BtnNPVok.pressed.connect(self.DisplayNPVanswer)
        self.ui.BtnNPVclear.pressed.connect(self.DisplayNPVclear)
        self.ui.BtnNPVclose.pressed.connect(self.DisplayNPVquit)

    def CalcNpv(self, rate, cashflows):
        total = 0.0
        for i, cashflow in enumerate(cashflows):
            total += cashflow / (1 + rate) ** i
            # print(total)
        return total

    def DisplayNPVanswer(self):
        money_i = -(eval(self.EmpControl(self.ui.NPVyear0invest.toPlainText())))
        iratetemp = self.EmpControl(self.ui.NPVirate.toPlainText())
        aa = float(iratetemp.strip('%'))   # 去掉s 字符串中的 %
        irate=aa/100 # 变成小数
        if money_i < 0:
            money_1 = eval(self.EmpControl(self.ui.NPVyear1r.toPlainText()))
            money_2 = eval(self.EmpControl(self.ui.NPVyear2r.toPlainText()))
            money_3 = eval(self.EmpControl(self.ui.NPVyear3r.toPlainText()))
            money_4 = eval(self.EmpControl(self.ui.NPVyear4r.toPlainText()))
            money_5 = eval(self.EmpControl(self.ui.NPVyear5r.toPlainText()))
            money_6 = eval(self.EmpControl(self.ui.NPVyear6r.toPlainText()))
            money_r = [money_i, money_1, money_2, money_3, money_4, money_5, money_6]
            money_f = eval(self.EmpControl(self.ui.NPVyearfn.toPlainText()))
            #print(type(money_f))
            if type(money_f) == type(1):
                money_r.append(money_f)
            else:
                money_r.extend(money_f)
            cashflows = money_r
            print (money_r)
        else: print("Please input plus number")
        NPVAnswertemp = str(npf.npv(irate,cashflows))
        NPVAnswer = window.FloatControl(NPVAnswertemp)
        self.sub_Signal.emit(NPVAnswer)

    def EmpControl(self, temp):
        if temp != "":
            return temp
        else:
            return "0"
    def DisplayNPVclear(self):
        self.ui.NPVyear0invest.setText('')
        self.ui.NPVirate.setText('')
        for i in range(1, 7):
            labletemp = f"NPVyear{i}r" #此处为了做清空简洁的遍历所有输入框，使用了f“{}”来连接字符串和变量i
            exec(f"self.ui.{labletemp}.setText('')") #因为f“”的结果只是个文本字符串，不能直接执行，此处用到了执行命令exec()
    def DisplayNPVquit(self):
        self.close()

# Extra function - ROE sub-dialog class
class dialogROE(QDialog):
    sub_Signal = Signal(str)
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_DialogROE()
        self.ui.setupUi(self)
        self.ui.BtnROEok.pressed.connect(self.DisplayROEanswer)
        self.ui.BtnROEclear.pressed.connect(self.DisplayROEclear)
        self.ui.BtnROEclose.pressed.connect(self.DisplayROEquit)

    def CalcROE(self, nMargin, tUrnover,lEver):
        rOE = 0.0
        rOE=nMargin*tUrnover*lEver
        return rOE
    def DisplayROEanswer(self):
        nProfit = eval(self.ui.ROEnetprofit.toPlainText())
        rEvenue = eval(self.ui.ROErevenue.toPlainText())
        aSsets = eval(self.ui.ROEassets.toPlainText())
        eQuity = eval(self.ui.ROEequity.toPlainText())
        if self.ui.ROEmargin.toPlainText() == '':
           nMargin=nProfit/rEvenue
           #print(type(nMargin))
           self.ui.ROEmargin.setText(f'{nMargin}')
        else:
           nMargin=self.ui.ROEmargin.toPlainText()
        if self.ui.ROEturnover.toPlainText() == '':
           tUrnover = rEvenue/aSsets
           #print(type(tUrnover))
           self.ui.ROEturnover.setText(f'{tUrnover}')
        else:
           tUrnover = self.ui.ROEturnover.toPlainText()
        if self.ui.ROElever.toPlainText() == '':
           lEver = aSsets/eQuity
           self.ui.ROElever.setText(f'{lEver}')
           print(type(lEver))
        else:
           lEver = self.ui.ROElever.toPlainText()
        ROEAnswertemp = str(self.CalcROE(nMargin,tUrnover,lEver))
        ROEAnswer = window.FloatControl(ROEAnswertemp)
        self.sub_Signal.emit(ROEAnswer)

    def EmpControl(self, temp):
        if temp != "":
            return temp
        else:
            return "0"
    def DisplayROEclear(self):
        self.ui.ROElever.setText('')
        self.ui.ROEnetprofit.setText('')
        self.ui.ROEturnover.setText('')
        self.ui.ROEequity.setText('')
        self.ui.ROErevenue.setText('')
        self.ui.ROEmargin.setText('')
        self.ui.ROEassets.setText('')
    def DisplayROEquit(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("BCalculator")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())