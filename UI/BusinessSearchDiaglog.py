# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BusinessSearchDiaglog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BusinessSearchDialog(object):
    def setupUi(self, BusinessSearchDialog):
        BusinessSearchDialog.setObjectName("BusinessSearchDialog")
        BusinessSearchDialog.resize(976, 411)
        self.buttonBox = QtWidgets.QDialogButtonBox(BusinessSearchDialog)
        self.buttonBox.setGeometry(QtCore.QRect(500, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(BusinessSearchDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(660, 80, 221, 253))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 8, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)
        self.repaydatecomboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.repaydatecomboBox.setObjectName("repaydatecomboBox")
        self.repaydatecomboBox.addItem("")
        self.repaydatecomboBox.addItem("")
        self.repaydatecomboBox.addItem("")
        self.repaydatecomboBox.addItem("")
        self.gridLayout_3.addWidget(self.repaydatecomboBox, 7, 2, 1, 2)
        self.repaystatuscomboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.repaystatuscomboBox.setObjectName("repaystatuscomboBox")
        self.repaystatuscomboBox.addItem("")
        self.repaystatuscomboBox.addItem("")
        self.repaystatuscomboBox.addItem("")
        self.repaystatuscomboBox.addItem("")
        self.gridLayout_3.addWidget(self.repaystatuscomboBox, 8, 2, 1, 2)
        self.repayidcomboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.repayidcomboBox.setObjectName("repayidcomboBox")
        self.repayidcomboBox.addItem("")
        self.repayidcomboBox.addItem("")
        self.gridLayout_3.addWidget(self.repayidcomboBox, 0, 2, 1, 1)
        self.repayloanidlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.repayloanidlineEdit.setObjectName("repayloanidlineEdit")
        self.gridLayout_3.addWidget(self.repayloanidlineEdit, 1, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 7, 0, 1, 1)
        self.repayamountcomboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.repayamountcomboBox.setObjectName("repayamountcomboBox")
        self.repayamountcomboBox.addItem("")
        self.repayamountcomboBox.addItem("")
        self.repayamountcomboBox.addItem("")
        self.repayamountcomboBox.addItem("")
        self.gridLayout_3.addWidget(self.repayamountcomboBox, 3, 2, 1, 1)
        self.repayidlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.repayidlineEdit.setObjectName("repayidlineEdit")
        self.gridLayout_3.addWidget(self.repayidlineEdit, 0, 3, 1, 1)
        self.repayloanidcomboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.repayloanidcomboBox.setObjectName("repayloanidcomboBox")
        self.repayloanidcomboBox.addItem("")
        self.repayloanidcomboBox.addItem("")
        self.gridLayout_3.addWidget(self.repayloanidcomboBox, 1, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 3, 0, 1, 1)
        self.repayamountlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.repayamountlineEdit.setObjectName("repayamountlineEdit")
        self.gridLayout_3.addWidget(self.repayamountlineEdit, 3, 3, 1, 1)
        self.repayleftamountcomboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.repayleftamountcomboBox.setObjectName("repayleftamountcomboBox")
        self.repayleftamountcomboBox.addItem("")
        self.repayleftamountcomboBox.addItem("")
        self.repayleftamountcomboBox.addItem("")
        self.repayleftamountcomboBox.addItem("")
        self.gridLayout_3.addWidget(self.repayleftamountcomboBox, 4, 2, 1, 1)
        self.repayleftamountlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.repayleftamountlineEdit.setObjectName("repayleftamountlineEdit")
        self.gridLayout_3.addWidget(self.repayleftamountlineEdit, 4, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 4, 0, 1, 1)
        self.widget = QtWidgets.QWidget(BusinessSearchDialog)
        self.widget.setGeometry(QtCore.QRect(110, 80, 251, 248))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.loanidcomboBox = QtWidgets.QComboBox(self.widget)
        self.loanidcomboBox.setObjectName("loanidcomboBox")
        self.loanidcomboBox.addItem("")
        self.loanidcomboBox.addItem("")
        self.gridLayout.addWidget(self.loanidcomboBox, 0, 1, 1, 1)
        self.loanidlineEdit = QtWidgets.QLineEdit(self.widget)
        self.loanidlineEdit.setObjectName("loanidlineEdit")
        self.gridLayout.addWidget(self.loanidlineEdit, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.clientidcomboBox = QtWidgets.QComboBox(self.widget)
        self.clientidcomboBox.setObjectName("clientidcomboBox")
        self.clientidcomboBox.addItem("")
        self.clientidcomboBox.addItem("")
        self.gridLayout.addWidget(self.clientidcomboBox, 1, 1, 1, 1)
        self.clientidlineEdit = QtWidgets.QLineEdit(self.widget)
        self.clientidlineEdit.setText("")
        self.clientidlineEdit.setObjectName("clientidlineEdit")
        self.gridLayout.addWidget(self.clientidlineEdit, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.accountidcomboBox = QtWidgets.QComboBox(self.widget)
        self.accountidcomboBox.setObjectName("accountidcomboBox")
        self.accountidcomboBox.addItem("")
        self.accountidcomboBox.addItem("")
        self.gridLayout.addWidget(self.accountidcomboBox, 2, 1, 1, 1)
        self.accountidlineEdit = QtWidgets.QLineEdit(self.widget)
        self.accountidlineEdit.setText("")
        self.accountidlineEdit.setObjectName("accountidlineEdit")
        self.gridLayout.addWidget(self.accountidlineEdit, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.loanamountcomboBox = QtWidgets.QComboBox(self.widget)
        self.loanamountcomboBox.setObjectName("loanamountcomboBox")
        self.loanamountcomboBox.addItem("")
        self.loanamountcomboBox.addItem("")
        self.loanamountcomboBox.addItem("")
        self.loanamountcomboBox.addItem("")
        self.gridLayout.addWidget(self.loanamountcomboBox, 3, 1, 1, 1)
        self.loanamountlineEdit = QtWidgets.QLineEdit(self.widget)
        self.loanamountlineEdit.setObjectName("loanamountlineEdit")
        self.gridLayout.addWidget(self.loanamountlineEdit, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.loandatecomboBox = QtWidgets.QComboBox(self.widget)
        self.loandatecomboBox.setObjectName("loandatecomboBox")
        self.loandatecomboBox.addItem("")
        self.loandatecomboBox.addItem("")
        self.loandatecomboBox.addItem("")
        self.loandatecomboBox.addItem("")
        self.gridLayout.addWidget(self.loandatecomboBox, 4, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.loanrepaycomboBox = QtWidgets.QComboBox(self.widget)
        self.loanrepaycomboBox.setObjectName("loanrepaycomboBox")
        self.loanrepaycomboBox.addItem("")
        self.loanrepaycomboBox.addItem("")
        self.loanrepaycomboBox.addItem("")
        self.loanrepaycomboBox.addItem("")
        self.gridLayout.addWidget(self.loanrepaycomboBox, 6, 1, 1, 2)
        self.loangrantstatuscomboBox = QtWidgets.QComboBox(self.widget)
        self.loangrantstatuscomboBox.setObjectName("loangrantstatuscomboBox")
        self.loangrantstatuscomboBox.addItem("")
        self.loangrantstatuscomboBox.addItem("")
        self.loangrantstatuscomboBox.addItem("")
        self.loangrantstatuscomboBox.addItem("")
        self.gridLayout.addWidget(self.loangrantstatuscomboBox, 5, 1, 1, 2)
        self.widget1 = QtWidgets.QWidget(BusinessSearchDialog)
        self.widget1.setGeometry(QtCore.QRect(400, 80, 221, 253))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_14 = QtWidgets.QLabel(self.widget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget1)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 8, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.grantdatecomboBox = QtWidgets.QComboBox(self.widget1)
        self.grantdatecomboBox.setObjectName("grantdatecomboBox")
        self.grantdatecomboBox.addItem("")
        self.grantdatecomboBox.addItem("")
        self.grantdatecomboBox.addItem("")
        self.grantdatecomboBox.addItem("")
        self.gridLayout_2.addWidget(self.grantdatecomboBox, 7, 2, 1, 2)
        self.grantstatuscomboBox = QtWidgets.QComboBox(self.widget1)
        self.grantstatuscomboBox.setObjectName("grantstatuscomboBox")
        self.grantstatuscomboBox.addItem("")
        self.grantstatuscomboBox.addItem("")
        self.grantstatuscomboBox.addItem("")
        self.grantstatuscomboBox.addItem("")
        self.gridLayout_2.addWidget(self.grantstatuscomboBox, 8, 2, 1, 2)
        self.grantidcomboBox = QtWidgets.QComboBox(self.widget1)
        self.grantidcomboBox.setObjectName("grantidcomboBox")
        self.grantidcomboBox.addItem("")
        self.grantidcomboBox.addItem("")
        self.gridLayout_2.addWidget(self.grantidcomboBox, 0, 2, 1, 1)
        self.grantloanidlineEdit = QtWidgets.QLineEdit(self.widget1)
        self.grantloanidlineEdit.setObjectName("grantloanidlineEdit")
        self.gridLayout_2.addWidget(self.grantloanidlineEdit, 1, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget1)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 7, 0, 1, 1)
        self.grantamountcomboBox = QtWidgets.QComboBox(self.widget1)
        self.grantamountcomboBox.setObjectName("grantamountcomboBox")
        self.grantamountcomboBox.addItem("")
        self.grantamountcomboBox.addItem("")
        self.grantamountcomboBox.addItem("")
        self.grantamountcomboBox.addItem("")
        self.gridLayout_2.addWidget(self.grantamountcomboBox, 3, 2, 1, 1)
        self.grantidlineEdit = QtWidgets.QLineEdit(self.widget1)
        self.grantidlineEdit.setObjectName("grantidlineEdit")
        self.gridLayout_2.addWidget(self.grantidlineEdit, 0, 3, 1, 1)
        self.grantloanidcomboBox = QtWidgets.QComboBox(self.widget1)
        self.grantloanidcomboBox.setObjectName("grantloanidcomboBox")
        self.grantloanidcomboBox.addItem("")
        self.grantloanidcomboBox.addItem("")
        self.gridLayout_2.addWidget(self.grantloanidcomboBox, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget1)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)
        self.grantamountlineEdit = QtWidgets.QLineEdit(self.widget1)
        self.grantamountlineEdit.setObjectName("grantamountlineEdit")
        self.gridLayout_2.addWidget(self.grantamountlineEdit, 3, 3, 1, 1)
        self.grantleftamountcomboBox = QtWidgets.QComboBox(self.widget1)
        self.grantleftamountcomboBox.setObjectName("grantleftamountcomboBox")
        self.grantleftamountcomboBox.addItem("")
        self.grantleftamountcomboBox.addItem("")
        self.grantleftamountcomboBox.addItem("")
        self.grantleftamountcomboBox.addItem("")
        self.gridLayout_2.addWidget(self.grantleftamountcomboBox, 4, 2, 1, 1)
        self.grantleftamountlineEdit = QtWidgets.QLineEdit(self.widget1)
        self.grantleftamountlineEdit.setObjectName("grantleftamountlineEdit")
        self.gridLayout_2.addWidget(self.grantleftamountlineEdit, 4, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget1)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 4, 0, 1, 1)
        self.widget2 = QtWidgets.QWidget(BusinessSearchDialog)
        self.widget2.setGeometry(QtCore.QRect(170, 50, 841, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loancheckBox = QtWidgets.QCheckBox(self.widget2)
        self.loancheckBox.setTabletTracking(False)
        self.loancheckBox.setAcceptDrops(False)
        self.loancheckBox.setChecked(True)
        self.loancheckBox.setObjectName("loancheckBox")
        self.horizontalLayout.addWidget(self.loancheckBox)
        self.grantcheckBox = QtWidgets.QCheckBox(self.widget2)
        self.grantcheckBox.setTabletTracking(False)
        self.grantcheckBox.setAcceptDrops(False)
        self.grantcheckBox.setChecked(True)
        self.grantcheckBox.setObjectName("grantcheckBox")
        self.horizontalLayout.addWidget(self.grantcheckBox)
        self.repaycheckBox = QtWidgets.QCheckBox(self.widget2)
        self.repaycheckBox.setTabletTracking(False)
        self.repaycheckBox.setAcceptDrops(False)
        self.repaycheckBox.setChecked(True)
        self.repaycheckBox.setObjectName("repaycheckBox")
        self.horizontalLayout.addWidget(self.repaycheckBox)

        self.retranslateUi(BusinessSearchDialog)
        self.buttonBox.accepted.connect(BusinessSearchDialog.accept)
        self.buttonBox.rejected.connect(BusinessSearchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BusinessSearchDialog)

    def retranslateUi(self, BusinessSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        BusinessSearchDialog.setWindowTitle(_translate("BusinessSearchDialog", "BusinessSearchDialog"))
        self.label_16.setText(_translate("BusinessSearchDialog", "贷款号"))
        self.label_21.setText(_translate("BusinessSearchDialog", "还款情况"))
        self.label_22.setText(_translate("BusinessSearchDialog", "贷款还款号"))
        self.repaydatecomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.repaydatecomboBox.setItemText(1, _translate("BusinessSearchDialog", "一年之内"))
        self.repaydatecomboBox.setItemText(2, _translate("BusinessSearchDialog", "两年之内"))
        self.repaydatecomboBox.setItemText(3, _translate("BusinessSearchDialog", "两年以上"))
        self.repaystatuscomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.repaystatuscomboBox.setItemText(1, _translate("BusinessSearchDialog", "未发放"))
        self.repaystatuscomboBox.setItemText(2, _translate("BusinessSearchDialog", "发放中"))
        self.repaystatuscomboBox.setItemText(3, _translate("BusinessSearchDialog", "已发放"))
        self.repayidcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.repayidcomboBox.setItemText(1, _translate("BusinessSearchDialog", "是"))
        self.label_23.setText(_translate("BusinessSearchDialog", "还款日期"))
        self.repayamountcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.repayamountcomboBox.setItemText(1, _translate("BusinessSearchDialog", "等于"))
        self.repayamountcomboBox.setItemText(2, _translate("BusinessSearchDialog", "大于"))
        self.repayamountcomboBox.setItemText(3, _translate("BusinessSearchDialog", "小于"))
        self.repayloanidcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.repayloanidcomboBox.setItemText(1, _translate("BusinessSearchDialog", "是"))
        self.label_24.setText(_translate("BusinessSearchDialog", "还款金额"))
        self.repayleftamountcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.repayleftamountcomboBox.setItemText(1, _translate("BusinessSearchDialog", "等于"))
        self.repayleftamountcomboBox.setItemText(2, _translate("BusinessSearchDialog", "大于"))
        self.repayleftamountcomboBox.setItemText(3, _translate("BusinessSearchDialog", "小于"))
        self.label_25.setText(_translate("BusinessSearchDialog", "剩余还款金额"))
        self.label_7.setText(_translate("BusinessSearchDialog", "贷款号"))
        self.loanidcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.loanidcomboBox.setItemText(1, _translate("BusinessSearchDialog", "是"))
        self.label_10.setText(_translate("BusinessSearchDialog", "贷款人身份证号"))
        self.clientidcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.clientidcomboBox.setItemText(1, _translate("BusinessSearchDialog", "是"))
        self.label_13.setText(_translate("BusinessSearchDialog", "贷款人账户号"))
        self.accountidcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.accountidcomboBox.setItemText(1, _translate("BusinessSearchDialog", "是"))
        self.label_8.setText(_translate("BusinessSearchDialog", "贷款金额"))
        self.loanamountcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.loanamountcomboBox.setItemText(1, _translate("BusinessSearchDialog", "等于"))
        self.loanamountcomboBox.setItemText(2, _translate("BusinessSearchDialog", "大于"))
        self.loanamountcomboBox.setItemText(3, _translate("BusinessSearchDialog", "小于"))
        self.label_9.setText(_translate("BusinessSearchDialog", "贷款日期"))
        self.loandatecomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.loandatecomboBox.setItemText(1, _translate("BusinessSearchDialog", "一年之内"))
        self.loandatecomboBox.setItemText(2, _translate("BusinessSearchDialog", "两年之内"))
        self.loandatecomboBox.setItemText(3, _translate("BusinessSearchDialog", "两年以上"))
        self.label_11.setText(_translate("BusinessSearchDialog", "发放情况"))
        self.label_12.setText(_translate("BusinessSearchDialog", "偿还情况"))
        self.loanrepaycomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.loanrepaycomboBox.setItemText(1, _translate("BusinessSearchDialog", "未偿还"))
        self.loanrepaycomboBox.setItemText(2, _translate("BusinessSearchDialog", "偿还中"))
        self.loanrepaycomboBox.setItemText(3, _translate("BusinessSearchDialog", "已偿还"))
        self.loangrantstatuscomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.loangrantstatuscomboBox.setItemText(1, _translate("BusinessSearchDialog", "未发放"))
        self.loangrantstatuscomboBox.setItemText(2, _translate("BusinessSearchDialog", "发放中"))
        self.loangrantstatuscomboBox.setItemText(3, _translate("BusinessSearchDialog", "已发放"))
        self.label_14.setText(_translate("BusinessSearchDialog", "贷款号"))
        self.label_19.setText(_translate("BusinessSearchDialog", "发放情况"))
        self.label_15.setText(_translate("BusinessSearchDialog", "贷款发放号"))
        self.grantdatecomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.grantdatecomboBox.setItemText(1, _translate("BusinessSearchDialog", "一年之内"))
        self.grantdatecomboBox.setItemText(2, _translate("BusinessSearchDialog", "两年之内"))
        self.grantdatecomboBox.setItemText(3, _translate("BusinessSearchDialog", "两年以上"))
        self.grantstatuscomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.grantstatuscomboBox.setItemText(1, _translate("BusinessSearchDialog", "未发放"))
        self.grantstatuscomboBox.setItemText(2, _translate("BusinessSearchDialog", "发放中"))
        self.grantstatuscomboBox.setItemText(3, _translate("BusinessSearchDialog", "已发放"))
        self.grantidcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.grantidcomboBox.setItemText(1, _translate("BusinessSearchDialog", "是"))
        self.label_18.setText(_translate("BusinessSearchDialog", "发放日期"))
        self.grantamountcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.grantamountcomboBox.setItemText(1, _translate("BusinessSearchDialog", "等于"))
        self.grantamountcomboBox.setItemText(2, _translate("BusinessSearchDialog", "大于"))
        self.grantamountcomboBox.setItemText(3, _translate("BusinessSearchDialog", "小于"))
        self.grantloanidcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.grantloanidcomboBox.setItemText(1, _translate("BusinessSearchDialog", "是"))
        self.label_17.setText(_translate("BusinessSearchDialog", "发放金额"))
        self.grantleftamountcomboBox.setItemText(0, _translate("BusinessSearchDialog", "不限"))
        self.grantleftamountcomboBox.setItemText(1, _translate("BusinessSearchDialog", "等于"))
        self.grantleftamountcomboBox.setItemText(2, _translate("BusinessSearchDialog", "大于"))
        self.grantleftamountcomboBox.setItemText(3, _translate("BusinessSearchDialog", "小于"))
        self.label_20.setText(_translate("BusinessSearchDialog", "剩余发放金额"))
        self.loancheckBox.setText(_translate("BusinessSearchDialog", "查询贷款情况"))
        self.grantcheckBox.setText(_translate("BusinessSearchDialog", "查询发放记录"))
        self.repaycheckBox.setText(_translate("BusinessSearchDialog", "查询还款记录"))
