# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientSearchDiaglog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClientSearchDialog(object):
    def setupUi(self, ClientSearchDialog):
        ClientSearchDialog.setObjectName("ClientSearchDialog")
        ClientSearchDialog.resize(397, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ClientSearchDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_5 = QtWidgets.QLabel(ClientSearchDialog)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 381, 16))
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(ClientSearchDialog)
        self.widget.setGeometry(QtCore.QRect(101, 40, 211, 161))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.NameLineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.TelLineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.TelLineEdit.setObjectName("TelLineEdit")
        self.IDLineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.IDLineEdit.setObjectName("IDLineEdit")
        self.AddressLineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.AddressLineEdit.setObjectName("AddressLineEdit")
        self.gridLayout.addWidget(self.splitter_2, 0, 1, 4, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.retranslateUi(ClientSearchDialog)
        self.buttonBox.accepted.connect(ClientSearchDialog.accept)
        self.buttonBox.rejected.connect(ClientSearchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ClientSearchDialog)

    def retranslateUi(self, ClientSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        ClientSearchDialog.setWindowTitle(_translate("ClientSearchDialog", "Dialog"))
        self.label_5.setText(_translate("ClientSearchDialog", "仅支持查找包含关键字的记录，不填代表不对该关键字进行限制"))
        self.label.setText(_translate("ClientSearchDialog", "Name:"))
        self.label_3.setText(_translate("ClientSearchDialog", "Tel"))
        self.label_2.setText(_translate("ClientSearchDialog", "ID"))
        self.label_4.setText(_translate("ClientSearchDialog", "Address"))

