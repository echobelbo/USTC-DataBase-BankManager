# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientSearch.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClientSearchForm(object):
    def setupUi(self, ClientSearchForm):
        ClientSearchForm.setObjectName("ClientSearchForm")
        ClientSearchForm.resize(490, 240)
        self.NameLineEdit = QtWidgets.QLineEdit(ClientSearchForm)
        self.NameLineEdit.setGeometry(QtCore.QRect(100, 30, 113, 21))
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.label = QtWidgets.QLabel(ClientSearchForm)
        self.label.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.label.setObjectName("label")
        self.IDLineEdit = QtWidgets.QLineEdit(ClientSearchForm)
        self.IDLineEdit.setGeometry(QtCore.QRect(340, 30, 113, 21))
        self.IDLineEdit.setObjectName("IDLineEdit")
        self.label_2 = QtWidgets.QLabel(ClientSearchForm)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ClientSearchForm)
        self.label_3.setGeometry(QtCore.QRect(29, 80, 61, 20))
        self.label_3.setObjectName("label_3")
        self.TelLineEdit = QtWidgets.QLineEdit(ClientSearchForm)
        self.TelLineEdit.setGeometry(QtCore.QRect(100, 80, 113, 21))
        self.TelLineEdit.setObjectName("TelLineEdit")
        self.AddressLineEdit = QtWidgets.QLineEdit(ClientSearchForm)
        self.AddressLineEdit.setGeometry(QtCore.QRect(340, 80, 113, 21))
        self.AddressLineEdit.setObjectName("AddressLineEdit")
        self.label_4 = QtWidgets.QLabel(ClientSearchForm)
        self.label_4.setGeometry(QtCore.QRect(280, 80, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ClientSearchForm)
        self.label_5.setGeometry(QtCore.QRect(70, 130, 381, 16))
        self.label_5.setObjectName("label_5")
        self.SearchBtn = QtWidgets.QPushButton(ClientSearchForm)
        self.SearchBtn.setGeometry(QtCore.QRect(180, 160, 113, 32))
        self.SearchBtn.setObjectName("SearchBtn")

        self.retranslateUi(ClientSearchForm)
        QtCore.QMetaObject.connectSlotsByName(ClientSearchForm)

    def retranslateUi(self, ClientSearchForm):
        _translate = QtCore.QCoreApplication.translate
        ClientSearchForm.setWindowTitle(_translate("ClientSearchForm", "Form"))
        self.label.setText(_translate("ClientSearchForm", "Name:"))
        self.label_2.setText(_translate("ClientSearchForm", "ID"))
        self.label_3.setText(_translate("ClientSearchForm", "Tel"))
        self.label_4.setText(_translate("ClientSearchForm", "Address"))
        self.label_5.setText(_translate("ClientSearchForm", "仅支持查找包含关键字的记录，不填代表不对该关键字进行限制"))
        self.SearchBtn.setText(_translate("ClientSearchForm", "Search"))

