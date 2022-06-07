# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BusinessDeleteDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BusinessDeleteDialog(object):
    def setupUi(self, BusinessDeleteDialog):
        BusinessDeleteDialog.setObjectName("BusinessDeleteDialog")
        BusinessDeleteDialog.resize(606, 274)
        self.buttonBox = QtWidgets.QDialogButtonBox(BusinessDeleteDialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(BusinessDeleteDialog)
        self.textBrowser.setGeometry(QtCore.QRect(406, 50, 141, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(BusinessDeleteDialog)
        self.label_6.setGeometry(QtCore.QRect(450, 30, 41, 16))
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(BusinessDeleteDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 110, 232, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.idlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.idlineEdit.setObjectName("idlineEdit")
        self.horizontalLayout.addWidget(self.idlineEdit)

        self.retranslateUi(BusinessDeleteDialog)
        self.buttonBox.accepted.connect(BusinessDeleteDialog.accept)
        self.buttonBox.rejected.connect(BusinessDeleteDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BusinessDeleteDialog)

    def retranslateUi(self, BusinessDeleteDialog):
        _translate = QtCore.QCoreApplication.translate
        BusinessDeleteDialog.setWindowTitle(_translate("BusinessDeleteDialog", "BusinesDeleteDialog"))
        self.textBrowser.setHtml(_translate("BusinessDeleteDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">处于发放中状态的贷款记录不允许删除，删除贷款时会同时删除发放记录和还款记录</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("BusinessDeleteDialog", "提示框"))
        self.label.setText(_translate("BusinessDeleteDialog", "贷款号"))

