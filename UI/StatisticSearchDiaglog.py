# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatisticSearchDiaglog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatisticSearchDialog(object):
    def setupUi(self, StatisticSearchDialog):
        StatisticSearchDialog.setObjectName("StatisticSearchDialog")
        StatisticSearchDialog.resize(469, 169)
        self.buttonBox = QtWidgets.QDialogButtonBox(StatisticSearchDialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(StatisticSearchDialog)
        self.widget.setGeometry(QtCore.QRect(90, 40, 291, 57))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.businesscomboBox = QtWidgets.QComboBox(self.widget)
        self.businesscomboBox.setObjectName("businesscomboBox")
        self.businesscomboBox.addItem("")
        self.businesscomboBox.addItem("")
        self.gridLayout.addWidget(self.businesscomboBox, 1, 0, 1, 1)
        self.timecomboBox = QtWidgets.QComboBox(self.widget)
        self.timecomboBox.setObjectName("timecomboBox")
        self.timecomboBox.addItem("")
        self.timecomboBox.addItem("")
        self.timecomboBox.addItem("")
        self.gridLayout.addWidget(self.timecomboBox, 1, 1, 1, 1)
        self.numcomboBox = QtWidgets.QComboBox(self.widget)
        self.numcomboBox.setObjectName("numcomboBox")
        self.numcomboBox.addItem("")
        self.numcomboBox.addItem("")
        self.numcomboBox.addItem("")
        self.gridLayout.addWidget(self.numcomboBox, 1, 2, 1, 1)

        self.retranslateUi(StatisticSearchDialog)
        self.buttonBox.rejected.connect(StatisticSearchDialog.reject)
        self.buttonBox.accepted.connect(StatisticSearchDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(StatisticSearchDialog)

    def retranslateUi(self, StatisticSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        StatisticSearchDialog.setWindowTitle(_translate("StatisticSearchDialog", "StatisticSearchDialog"))
        self.label.setText(_translate("StatisticSearchDialog", "??????"))
        self.label_2.setText(_translate("StatisticSearchDialog", "??????"))
        self.label_3.setText(_translate("StatisticSearchDialog", "????????????"))
        self.businesscomboBox.setItemText(0, _translate("StatisticSearchDialog", "??????"))
        self.businesscomboBox.setItemText(1, _translate("StatisticSearchDialog", "??????"))
        self.timecomboBox.setItemText(0, _translate("StatisticSearchDialog", "??????"))
        self.timecomboBox.setItemText(1, _translate("StatisticSearchDialog", "??????"))
        self.timecomboBox.setItemText(2, _translate("StatisticSearchDialog", "??????"))
        self.numcomboBox.setItemText(0, _translate("StatisticSearchDialog", "????????????"))
        self.numcomboBox.setItemText(1, _translate("StatisticSearchDialog", "????????????"))
        self.numcomboBox.setItemText(2, _translate("StatisticSearchDialog", "????????????"))

