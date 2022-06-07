# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatisticForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatisticForm(object):
    def setupUi(self, StatisticForm):
        StatisticForm.setObjectName("StatisticForm")
        StatisticForm.resize(817, 588)
        self.messagetextEdit = QtWidgets.QTextEdit(StatisticForm)
        self.messagetextEdit.setGeometry(QtCore.QRect(529, 509, 221, 51))
        self.messagetextEdit.setObjectName("messagetextEdit")
        self.SearchBtn = QtWidgets.QPushButton(StatisticForm)
        self.SearchBtn.setGeometry(QtCore.QRect(350, 520, 84, 32))
        self.SearchBtn.setObjectName("SearchBtn")
        self.table = QtWidgets.QTableWidget(StatisticForm)
        self.table.setGeometry(QtCore.QRect(80, 30, 671, 441))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table.setFont(font)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)

        self.retranslateUi(StatisticForm)
        QtCore.QMetaObject.connectSlotsByName(StatisticForm)

    def retranslateUi(self, StatisticForm):
        _translate = QtCore.QCoreApplication.translate
        StatisticForm.setWindowTitle(_translate("StatisticForm", "StatisticForm"))
        self.SearchBtn.setText(_translate("StatisticForm", "Search"))

