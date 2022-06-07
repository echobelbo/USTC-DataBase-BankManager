def __init__(self):
    super().__init__()
    self.db = db_login("root", "7988814aa", "127.0.0.1", "lab3")
    self.ui = Ui_StatisticForm()
    self.ui.setupUi(self)
    self.ui.loantable.setColumnCount(6)  # 不设置不显示这些列
    self.ui.loantable.setHorizontalHeaderLabels(['贷款号', '贷款总额', '发放情况', '还款情况', '贷款人', '贷款账户'])
    self.ui.loantable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
    self.ui.loantable.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    self.ui.granttable.setColumnCount(5)  # 不设置不显示这些列
    self.ui.granttable.setHorizontalHeaderLabels(['贷款发放号', '发放日期', '本次发放金额', '剩余发放金额', '贷款号'])
    self.ui.granttable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
    self.ui.granttable.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    self.ui.repaytable.setColumnCount(5)  # 不设置不显示这些列
    self.ui.repaytable.setHorizontalHeaderLabels(['贷款还款号', '还款日期', '本次还款金额', '剩余还款金额', "贷款号"])
    self.ui.repaytable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽self.show()
    self.ui.repaytable.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    self.ui.SearchBtn.clicked.connect(self.StatisticSearch)
    self.ui.AddBtn.clicked.connect(self.StatisticAdd)
    self.ui.DeleteBtn.clicked.connect(self.StatisticDelete)


def StatisticSearch(self):
    self.StatisticSearchChild = Ui_StatisticSearchDialog()
    self.StatisticSearchDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
    self.StatisticSearchChild.setupUi(self.StatisticSearchDialog)
    self.StatisticSearchChild.buttonBox.accepted.connect(self.GetStatisticSearch)
    self.StatisticSearchChild.buttonBox.rejected.connect(self.StatisticSearchClose)
    self.StatisticSearchDialog.exec_()


def GetStatisticSearch(self):
    loancomboBoxdict = {'loanid': self.StatisticSearchChild.loanidcomboBox.currentIndex(),
                        'clientid': self.StatisticSearchChild.clientidcomboBox.currentIndex(),
                        'accountid': self.StatisticSearchChild.accountidcomboBox.currentIndex(),
                        'loanamount': self.StatisticSearchChild.loanamountcomboBox.currentIndex(),
                        'loangrantstatus': self.StatisticSearchChild.loangrantstatuscomboBox.currentIndex(),
                        'loanrepaystatus': self.StatisticSearchChild.loanrepaycomboBox.currentIndex()}

    loantextdict = {'loanid': self.StatisticSearchChild.loanidlineEdit.text(),
                    'clientid': self.StatisticSearchChild.clientidlineEdit.text(),
                    'accountid': self.StatisticSearchChild.accountidlineEdit.text(),
                    'loanamount': self.StatisticSearchChild.loanamountlineEdit.text()}

    grantcomboBoxdict = {'grantid': self.StatisticSearchChild.grantidcomboBox.currentIndex(),
                         'grantloanid': self.StatisticSearchChild.grantloanidcomboBox.currentIndex(),
                         'grantamount': self.StatisticSearchChild.grantamountcomboBox.currentIndex(),
                         'grantleftamount': self.StatisticSearchChild.grantleftamountcomboBox.currentIndex(),
                         'grantdate': self.StatisticSearchChild.grantdatecomboBox.currentIndex(),
                         'grantstatus': self.StatisticSearchChild.grantstatuscomboBox.currentIndex()}

    granttextdict = {'grantid': self.StatisticSearchChild.grantidlineEdit.text(),
                     'grantloanid': self.StatisticSearchChild.grantloanidlineEdit.text(),
                     'grantamount': self.StatisticSearchChild.grantamountlineEdit.text(),
                     'grantleftamount': self.StatisticSearchChild.grantleftamountlineEdit.text()}

    repaycomboBoxdict = {'repayid': self.StatisticSearchChild.repayidcomboBox.currentIndex(),
                         'repayloanid': self.StatisticSearchChild.repayloanidcomboBox.currentIndex(),
                         'repayamount': self.StatisticSearchChild.repayamountcomboBox.currentIndex(),
                         'repayleftamount': self.StatisticSearchChild.repayleftamountcomboBox.currentIndex(),
                         'repaydate': self.StatisticSearchChild.repaydatecomboBox.currentIndex(),
                         'repaystatus': self.StatisticSearchChild.repaystatuscomboBox.currentIndex()}

    repaytextdict = {'repayid': self.StatisticSearchChild.repayidlineEdit.text(),
                     'repayloanid': self.StatisticSearchChild.repayloanidlineEdit.text(),
                     'repayamount': self.StatisticSearchChild.repayamountlineEdit.text(),
                     'repayleftamount': self.StatisticSearchChild.repayleftamountlineEdit.text()}

    checkBox = {'loan': self.StatisticSearchChild.loancheckBox.isChecked(),
                'grant': self.StatisticSearchChild.grantcheckBox.isChecked(),
                'repay': self.StatisticSearchChild.repaycheckBox.isChecked()}

    condition1 = ""
    for label in loancomboBoxdict:
        if loancomboBoxdict[label] != 0:
            condition1 += " and"
            if label == "loanid":
                condition1 += " loan.lid='%s'" % loantextdict['loanid']
            elif label == "clientid":
                condition1 += " CLS.client_id='%s'" % loantextdict['clientid']
            elif label == "accountid":
                condition1 += " CLS.account_id='%s'" % loantextdict['accountid']
            elif label == "loanamount":
                tmp_con = ' loan.total'
                tmp_con += '=' if loancomboBoxdict[label] == 1 else '>' if loancomboBoxdict[label] == 2 else '<'
                tmp_con += loantextdict[label]
                condition1 += tmp_con
            elif label == "loangrantstatus":
                tmp_con = " loan.grant_status='"
                tmp_con += "未发放'" if loancomboBoxdict[label] == 1 else "发放中'" if loancomboBoxdict[
                                                                                     label] == 2 else "已发放'"
                condition1 += tmp_con
            else:
                tmp_con = " loan.repay_status='"
                tmp_con += "未偿还'" if loancomboBoxdict[label] == 1 else "偿还中'" if loancomboBoxdict[
                                                                                     label] == 2 else "已偿还'"
                condition1 += tmp_con

    sql = "select loan.*, CLS.client_id, CLS.account_id from CLS,loan where CLS.loan_lid = loan.lid"

    sql += condition1
    print(sql)
    cursor = self.db.cursor()
    cursor.execute(sql)
    tabs1 = cursor.fetchall()

    rowNum1 = len(tabs1)  # 获取查询到的行数
    columnNum1 = len(tabs1[0]) if rowNum1 > 0 else 0  # 获取查询到的列数

    condition2 = ""
    for label in grantcomboBoxdict:
        if grantcomboBoxdict[label] != 0:
            if condition2 != "":
                condition2 += " and"
            else:
                condition2 += " where"
            if label == "grantid":
                condition2 += " id='%s'" % granttextdict['grantid']
            elif label == "grantloanid":
                condition2 += " loan_lid='%s'" % granttextdict['grantloanid']
            elif label == "grantamount":
                tmp_con = ' grant_amount'
                tmp_con += '=' if grantcomboBoxdict[label] == 1 else '>' if grantcomboBoxdict[label] == 2 else '<'
                tmp_con += granttextdict[label]
                condition2 += tmp_con
            elif label == "grantleftamount":
                tmp_con = ' left_amount'
                tmp_con += '=' if grantcomboBoxdict[label] == 1 else '>' if grantcomboBoxdict[label] == 2 else '<'
                tmp_con += granttextdict[label]
                condition2 += tmp_con
            elif label == "grantstatus":
                tmp_con = " grant_status='"
                tmp_con += "未发放'" if grantcomboBoxdict[label] == 1 else "发放中'" if grantcomboBoxdict[
                                                                                      label] == 2 else "已发放'"
                condition2 += tmp_con
            else:
                tmp_con = ' to_days(curdate())-to_days(grant_date)'
                tmp_con += '<365' if grantcomboBoxdict[label] == 1 else '<731' if grantcomboBoxdict[
                                                                                      label] == 2 else '>730'
                condition2 += tmp_con

    sql = "select * from grant_loan"

    sql += condition2
    print(sql)
    cursor = self.db.cursor()
    cursor.execute(sql)
    tabs2 = cursor.fetchall()

    rowNum2 = len(tabs2)  # 获取查询到的行数
    columnNum2 = len(tabs2[0]) if rowNum2 > 0 else 0  # 获取查询到的列数

    condition3 = ""
    for label in repaycomboBoxdict:
        if repaycomboBoxdict[label] != 0:
            if condition3 != "":
                condition3 += " and"
            else:
                condition3 += " where"
            if label == "repayid":
                condition3 += " id='%s'" % repaytextdict['repayid']
            elif label == "repayloanid":
                condition3 += " loan_lid='%s'" % repaytextdict['repayloanid']
            elif label == "repayamount":
                tmp_con = ' repay_amount'
                tmp_con += '=' if repaycomboBoxdict[label] == 1 else '>' if repaycomboBoxdict[label] == 2 else '<'
                tmp_con += repaytextdict[label]
                condition3 += tmp_con
            elif label == "repayleftamount":
                tmp_con = ' left_amount'
                tmp_con += '=' if repaycomboBoxdict[label] == 1 else '>' if repaycomboBoxdict[label] == 2 else '<'
                tmp_con += repaytextdict[label]
                condition3 += tmp_con
            elif label == "repaystatus":
                tmp_con = " repay_status='"
                tmp_con += "未偿还'" if repaycomboBoxdict[label] == 1 else "偿还中'" if repaycomboBoxdict[
                                                                                      label] == 2 else "已偿还'"
                condition3 += tmp_con
            else:
                tmp_con = ' to_days(curdate())-to_days(repay_date)'
                tmp_con += '<365' if repaycomboBoxdict[label] == 1 else '<731' if repaycomboBoxdict[
                                                                                      label] == 2 else '>730'
                condition3 += tmp_con

    sql = "select * from repay_loan"

    sql += condition3
    print(sql)
    cursor = self.db.cursor()
    cursor.execute(sql)
    tabs3 = cursor.fetchall()

    rowNum3 = len(tabs3)  # 获取查询到的行数
    columnNum3 = len(tabs3[0]) if rowNum3 > 0 else 0  # 获取查询到的列数

    try:
        if checkBox['loan']:
            self.ui.loantable.setRowCount(0)
            currentRowCount = self.ui.loantable.rowCount()
            for tab in tabs1:
                self.ui.loantable.insertRow(currentRowCount)
                item = {}
                for i in range(columnNum1):
                    item[i] = QTableWidgetItem(str(tab[i]))
                    item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.loantable.setItem(currentRowCount, i, item[i])  # 列i+1
                # self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
                currentRowCount += 1
                self.ui.loantable.setRowCount(currentRowCount)
        if checkBox['grant']:
            self.ui.granttable.setRowCount(0)
            currentRowCount = self.ui.granttable.rowCount()
            for tab in tabs2:
                self.ui.granttable.insertRow(currentRowCount)
                item = {}
                for i in range(columnNum2):
                    item[i] = QTableWidgetItem(str(tab[i]))
                    item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.granttable.setItem(currentRowCount, i, item[i])  # 列i+1
                # self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
                currentRowCount += 1
                self.ui.granttable.setRowCount(currentRowCount)
        if checkBox['repay']:
            self.ui.repaytable.setRowCount(0)
            currentRowCount = self.ui.repaytable.rowCount()
            for tab in tabs3:
                self.ui.repaytable.insertRow(currentRowCount)
                item = {}
                for i in range(columnNum3):
                    item[i] = QTableWidgetItem(str(tab[i]))
                    item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.repaytable.setItem(currentRowCount, i, item[i])  # 列i+1
                # self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
                currentRowCount += 1
                self.ui.repaytable.setRowCount(currentRowCount)
        self.db.commit()
        self.StatisticSearchSuccessDialog()

    except Exception as err:
        print(str(type(err))[8:-2])
        print('fail')
        self.db.rollback()
        self.StatisticSearchFailDialog(str(type(err))[8:-2])
    finally:
        self.StatisticSearchDialog.close()


def StatisticSearchSuccessDialog(self):
    self.ui.messagetextEdit.setText("查询记录成功")


def StatisticSearchFailDialog(self, message):
    self.ui.messagetextEdit.setText("查询记录失败，错误类型为%s" % message)


def StatisticSearchClose(self):
    self.StatisticSearchDialog.close()
