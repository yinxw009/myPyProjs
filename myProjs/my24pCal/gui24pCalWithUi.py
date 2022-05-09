#!/usr/bin/python3
# -*- coding： utf-8 -*-
import sys
import itertools
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

import gui24pCal


#返回4个数计算24的方法，无方法时返回"No Method"
def cal_24(numbers):
    rslt = []
    ops = ['+','-','*','/']
    ops_lst = [[i,j,k] for i in ops for j in ops for k in ops]

    for lst in itertools.permutations(numbers):
        lst = list(map(lambda x:str(x), lst))
        for op in ops_lst:
            expr0 = lst[0]+op[0]+lst[1]+op[1]+lst[2]+op[2]+lst[3]
            expr1 = '('+lst[0]+op[0]+lst[1]+')'+op[1]+lst[2]+op[2]+lst[3]
            expr2 = lst[0]+op[0]+'('+lst[1]+op[1]+lst[2]+')'+op[2]+lst[3]
            expr3 = lst[0]+op[0]+lst[1]+op[1]+'('+lst[2]+op[2]+lst[3]+')'
            expr4 = '('+lst[0]+op[0]+lst[1]+')'+op[1]+'('+lst[2]+op[2]+lst[3]+')'
            expr5 = '('+lst[0]+op[0]+lst[1]+op[1]+lst[2]+')'+op[2]+lst[3]
            expr6 = lst[0]+op[0]+'('+lst[1]+op[1]+lst[2]+op[2]+lst[3]+')'

            for expr in [expr0, expr1, expr2, expr3, expr4,expr5,expr6]:
                try:
                    if(abs(eval(expr)-24) < 0.001):
                        rslt.append(expr+'='+'24')
                except:                                                                 #作除法时，跳过分母为0时的情形
                    pass
    if rslt != None:
        return rslt
    else:
        return 'No method!'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


#所有情况的计算24点的办法，并输出到文本文件
def main():
    inLst = list(eval(input("Please input numbers:")))
    print("[%s,%s,%s,%s]: %s\n"%(inLst[0],inLst[1],inLst[2],inLst[3],cal_24(inLst)))

main()
input('Press <Enter>')