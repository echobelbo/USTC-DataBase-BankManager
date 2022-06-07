# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountDeleteDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccountDeleteDialog(object):
    def setupUi(self, AccountDeleteDialog):
        AccountDeleteDialog.setObjectName("AccountDeleteDialog")
        AccountDeleteDialog.resize(606, 330)
        self.buttonBox = QtWidgets.QDialogButtonBox(AccountDeleteDialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 280, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(AccountDeleteDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 140, 232, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.clientlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.clientlineEdit.setObjectName("clientlineEdit")
        self.horizontalLayout_2.addWidget(self.clientlineEdit)
        self.textBrowser = QtWidgets.QTextBrowser(AccountDeleteDialog)
        self.textBrowser.setGeometry(QtCore.QRect(406, 90, 181, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(AccountDeleteDialog)
        self.label_6.setGeometry(QtCore.QRect(470, 70, 41, 16))
        self.label_6.setObjectName("label_6")
        self.layoutWidget1 = QtWidgets.QWidget(AccountDeleteDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 110, 232, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.accountlineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.accountlineEdit.setObjectName("accountlineEdit")
        self.horizontalLayout.addWidget(self.accountlineEdit)

        self.retranslateUi(AccountDeleteDialog)
        self.buttonBox.accepted.connect(AccountDeleteDialog.accept)
        self.buttonBox.rejected.connect(AccountDeleteDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AccountDeleteDialog)

    def retranslateUi(self, AccountDeleteDialog):
        _translate = QtCore.QCoreApplication.translate
        AccountDeleteDialog.setWindowTitle(_translate("AccountDeleteDialog", "AccountDeleteDialog"))
        self.checkBox.setText(_translate("AccountDeleteDialog", "身份证号"))
        self.textBrowser.setHtml(_translate("AccountDeleteDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">删除必须输入完整的账户号。若勾选身份证号，则需输入完整的身份证号，表示删除账户与该客户连接关系，否则表示删除整个账户。</p></body></html>"))
        self.label_6.setText(_translate("AccountDeleteDialog", "提示框"))
        self.label.setText(_translate("AccountDeleteDialog", "账户号"))

