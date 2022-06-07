# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BusinessForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BusinessForm(object):
    def setupUi(self, BusinessForm):
        BusinessForm.setObjectName("BusinessForm")
        BusinessForm.resize(906, 645)
        self.splitter = QtWidgets.QSplitter(BusinessForm)
        self.splitter.setGeometry(QtCore.QRect(170, 580, 401, 32))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.AddBtn = QtWidgets.QPushButton(self.splitter)
        self.AddBtn.setObjectName("AddBtn")
        self.DeleteBtn = QtWidgets.QPushButton(self.splitter)
        self.DeleteBtn.setObjectName("DeleteBtn")
        self.SearchBtn = QtWidgets.QPushButton(self.splitter)
        self.SearchBtn.setObjectName("SearchBtn")
        self.messagetextEdit = QtWidgets.QTextEdit(BusinessForm)
        self.messagetextEdit.setGeometry(QtCore.QRect(620, 560, 221, 51))
        self.messagetextEdit.setObjectName("messagetextEdit")
        self.widget = QtWidgets.QWidget(BusinessForm)
        self.widget.setGeometry(QtCore.QRect(530, 20, 321, 521))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.granttable = QtWidgets.QTableWidget(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.granttable.setFont(font)
        self.granttable.setObjectName("granttable")
        self.granttable.setColumnCount(0)
        self.granttable.setRowCount(0)
        self.verticalLayout.addWidget(self.granttable)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.repaytable = QtWidgets.QTableWidget(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.repaytable.setFont(font)
        self.repaytable.setObjectName("repaytable")
        self.repaytable.setColumnCount(0)
        self.repaytable.setRowCount(0)
        self.verticalLayout.addWidget(self.repaytable)
        self.widget1 = QtWidgets.QWidget(BusinessForm)
        self.widget1.setGeometry(QtCore.QRect(50, 20, 461, 521))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.loantable = QtWidgets.QTableWidget(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.loantable.setFont(font)
        self.loantable.setObjectName("loantable")
        self.loantable.setColumnCount(0)
        self.loantable.setRowCount(0)
        self.verticalLayout_2.addWidget(self.loantable)

        self.retranslateUi(BusinessForm)
        QtCore.QMetaObject.connectSlotsByName(BusinessForm)

    def retranslateUi(self, BusinessForm):
        _translate = QtCore.QCoreApplication.translate
        BusinessForm.setWindowTitle(_translate("BusinessForm", "BusinessForm"))
        self.AddBtn.setText(_translate("BusinessForm", "Add"))
        self.DeleteBtn.setText(_translate("BusinessForm", "Delete"))
        self.SearchBtn.setText(_translate("BusinessForm", "Search"))
        self.label_5.setText(_translate("BusinessForm", "                                    贷款发放情况"))
        self.label_4.setText(_translate("BusinessForm", "                                   贷款还款情况"))
        self.label_3.setText(_translate("BusinessForm", "                                                         贷款情况"))

