# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClientForm(object):
    def setupUi(self, ClientForm):
        ClientForm.setObjectName("ClientForm")
        ClientForm.resize(817, 645)
        self.splitter = QtWidgets.QSplitter(ClientForm)
        self.splitter.setGeometry(QtCore.QRect(70, 580, 401, 32))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.AddBtn = QtWidgets.QPushButton(self.splitter)
        self.AddBtn.setObjectName("AddBtn")
        self.DeleteBtn = QtWidgets.QPushButton(self.splitter)
        self.DeleteBtn.setObjectName("DeleteBtn")
        self.UpdateBtn = QtWidgets.QPushButton(self.splitter)
        self.UpdateBtn.setObjectName("UpdateBtn")
        self.SearchBtn = QtWidgets.QPushButton(self.splitter)
        self.SearchBtn.setObjectName("SearchBtn")
        self.table = QtWidgets.QTableWidget(ClientForm)
        self.table.setGeometry(QtCore.QRect(20, 20, 781, 531))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table.setFont(font)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.messagetextEdit = QtWidgets.QTextEdit(ClientForm)
        self.messagetextEdit.setGeometry(QtCore.QRect(550, 570, 221, 51))
        self.messagetextEdit.setObjectName("messagetextEdit")

        self.retranslateUi(ClientForm)
        QtCore.QMetaObject.connectSlotsByName(ClientForm)

    def retranslateUi(self, ClientForm):
        _translate = QtCore.QCoreApplication.translate
        ClientForm.setWindowTitle(_translate("ClientForm", "ClientForm"))
        self.AddBtn.setText(_translate("ClientForm", "Add"))
        self.DeleteBtn.setText(_translate("ClientForm", "Delete"))
        self.UpdateBtn.setText(_translate("ClientForm", "Update"))
        self.SearchBtn.setText(_translate("ClientForm", "Search"))

