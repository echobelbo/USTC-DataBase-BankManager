from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets

from UI.AccountAddDialog import Ui_AccountAddDialog
from UI.AccountDeleteDialog import Ui_AccountDeleteDialog
from UI.AccountForm import Ui_AccountForm
from UI.AccountSearchDiaglog import Ui_AccountSearchDialog
from UI.AccountUpdateDialog import Ui_AccountUpdateDialog
from UI.BusinessAddDialog import Ui_BusinessAddDialog
from UI.BusinessDeleteDialog import Ui_BusinessDeleteDialog
from UI.BusinessForm import Ui_BusinessForm
from UI.BusinessSearchDiaglog import Ui_BusinessSearchDialog
from UI.ClientDeleteDialog import Ui_ClientDeleteDialog
from UI.StatisticForm import Ui_StatisticForm
from UI.StatisticSearchDiaglog import Ui_StatisticSearchDialog
from UI.table import Ui_TablePage
from UI.ClientForm import Ui_ClientForm
from UI.ClientSearchDiaglog import Ui_ClientSearchDialog
from UI.ClientAddDialog import Ui_ClientAddDialog
from UI.ClientUpdateDialog import Ui_ClientUpdateDialog
from login import LoginDialog
from db import *

debug = True


def transferContent(content):
    if content is None:
        return None
    else:
        string = ""
        for c in content:
            if c == '"':
                string += '\\\"'
            elif c == "'":
                string += "\\\'"
            elif c == "\\":
                string += "\\\\"
            else:
                string += c
        return string


class MainWindow(QMainWindow):
    " The Entrance of the Main window"

    def __init__(self):
        super().__init__()
        # 主窗口需要有一个UI界面，我们使用TablePage作为主窗口显示的UI界面
        self.ui = Ui_TablePage()
        self.ui.setupUi(self)

        # 初始化配置
        self.initLayout()
        self.initBinding()

        self.show()

        if debug:
            self.db = db_login("root", "010503", "127.0.0.1", "lab3")
            self.dbname = "lab3"
            self.ui.ClearBtn.setEnabled(True)
            self.ui.SearchBtn.setEnabled(True)
            self.ui.ClientBtn.setEnabled(True)
            self.ui.AccountBtn.setEnabled(True)
            self.ui.BusinessBtn.setEnabled(True)
            self.ui.StatisticsBtn.setEnabled(True)
        else:
            self.db = None
            self.dbname = ''

    def initLayout(self):
        # 设置主窗口UI界面的初始布局
        self.ui.ClearBtn.setEnabled(False)
        self.ui.SearchBtn.setEnabled(False)
        self.ui.ClientBtn.setEnabled(False)
        self.ui.AccountBtn.setEnabled(False)
        self.ui.BusinessBtn.setEnabled(False)
        self.ui.StatisticsBtn.setEnabled(False)
        self.ui.title.setText("All Tables for Database - ")
        self.ui.table.setColumnCount(2)  # 不设置不显示这些列
        self.ui.table.setHorizontalHeaderLabels(['Table Name', 'Row Count'])
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    def initBinding(self):
        # 将主界面按钮点击动作绑定到函数
        self.ui.ClearBtn.clicked.connect(self.clearTable)
        self.ui.SearchBtn.clicked.connect(self.renderTable)
        self.ui.ClientBtn.clicked.connect(self.show_client)
        self.ui.AccountBtn.clicked.connect(self.show_account)
        self.ui.BusinessBtn.clicked.connect(self.show_business)
        self.ui.StatisticsBtn.clicked.connect(self.show_statistic)
        # 将菜单点击动作绑定到函数
        self.ui.actionLogin.triggered.connect(self.Login)

        self.ui.actionLogout.triggered.connect(self.LogOut)

    # all the function to bind with
    def clearTable(self):
        self.ui.table.setRowCount(0)

    def renderTable(self):
        self.ui.table.setRowCount(0)

        tabs = db_showtable(self.db)

        currentRowCount = self.ui.table.rowCount()
        for tab in tabs:
            self.ui.table.insertRow(currentRowCount)

            item0 = QTableWidgetItem(str(tab[0]))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            item1 = QTableWidgetItem(str(tab[1]))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)

            self.ui.table.setItem(currentRowCount, 0, item0)  # 列1
            self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
            currentRowCount += 1
            self.ui.table.setRowCount(currentRowCount)

    def show_client(self):
        self.ClientWindow = ClientForm()
        self.ClientWindow.show()

    def show_account(self):
        self.AccountWindow = AccountForm()
        self.AccountWindow.show()

    def show_business(self):
        self.BusinessWindow = BusinessForm()
        self.BusinessWindow.show()

    def show_statistic(self):
        self.StatisticWindow = StatisticForm()
        self.StatisticWindow.show()

    def Login(self):
        dialog = LoginDialog(self)
        dialog.exec_()

        if self.db != None:
            print(self.db)
            self.ui.ClearBtn.setEnabled(True)
            self.ui.SearchBtn.setEnabled(True)
            self.ui.ClientBtn.setEnabled(True)
            self.ui.AccountBtn.setEnabled(True)
            self.ui.BusinessBtn.setEnabled(True)
            self.ui.StatisticsBtn.setEnabled(True)
            self.ui.title.setText("All Tables for Database - " + self.dbname)
            self.renderTable()

    def LogOut(self):
        db_close(self.db)
        self.db = None
        self.dbname = ''
        self.ui.ClearBtn.setEnabled(False)
        self.ui.SearchBtn.setEnabled(False)
        self.ui.ClientBtn.setEnabled(False)
        self.ui.AccountBtn.setEnabled(False)
        self.ui.BusinessBtn.setEnabled(False)
        self.ui.StatisticsBtn.setEnabled(False)
        self.clearTable()


class ClientForm(QWidget):
    def __init__(self):
        super().__init__()
        self.db = db_login("root", "010503", "127.0.0.1", "lab3")
        self.ui = Ui_ClientForm()
        self.ui.setupUi(self)
        self.ui.table.setColumnCount(8)  # 不设置不显示这些列
        self.ui.table.setHorizontalHeaderLabels(['ID', 'name', 'tel', 'address', 'cname', 'ctel', 'cemail', 'relation'])
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
        self.show()

        self.ui.SearchBtn.clicked.connect(self.ClientSearch)
        self.ui.AddBtn.clicked.connect(self.ClientAdd)
        self.ui.DeleteBtn.clicked.connect(self.ClientDelete)
        self.ui.UpdateBtn.clicked.connect(self.ClientUpdate)

    def ClientSearch(self):
        self.ClientSearchChild = Ui_ClientSearchDialog()
        self.ClientSearchDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.ClientSearchChild.setupUi(self.ClientSearchDialog)
        self.ClientSearchChild.buttonBox.accepted.connect(self.GetClientSearch)
        self.ClientSearchChild.buttonBox.rejected.connect(self.ClientSearchClose)
        self.ClientSearchDialog.exec_()

    def GetClientSearch(self):
        self.searchdict = {'name': self.ClientSearchChild.NameLineEdit.text(),
                           'id': self.ClientSearchChild.IDLineEdit.text(),
                           'tel': self.ClientSearchChild.TelLineEdit.text(),
                           'address': self.ClientSearchChild.AddressLineEdit.text()}
        labels = []
        for label in ['name', 'id', 'tel', 'address']:
            if self.searchdict[label] != '':
                labels.append(label)
        length = len(labels)
        string = ''
        if length != 0:
            string = ' where'
            for label in labels:
                string += ' ' + label + ' like \'%' +  transferContent(str(self.searchdict[label])) + '%\''
                length -= 1
                if length > 0:
                    string += ' and'
        print(string)
        tabs = db_search(self.db, 'client', string)

        rowNum = len(tabs)  # 获取查询到的行数
        columnNum = len(tabs[0]) if rowNum > 0 else 0  # 获取查询到的列数

        self.ui.table.setRowCount(0)
        currentRowCount = self.ui.table.rowCount()
        for tab in tabs:
            self.ui.table.insertRow(currentRowCount)
            item = {}
            for i in range(columnNum):
                item[i] = QTableWidgetItem(str(tab[i]))
                item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.table.setItem(currentRowCount, i, item[i])  # 列i+1
            # self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
            currentRowCount += 1
            self.ui.table.setRowCount(currentRowCount)

        self.ClientSearchDialog.close()

    def ClientSearchClose(self):
        self.ClientSearchDialog.close()

    def ClientAdd(self):
        print(self.db)
        self.ClientAddChild = Ui_ClientAddDialog()
        self.ClientAddDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.ClientAddChild.setupUi(self.ClientAddDialog)
        self.ClientAddChild.buttonBox.accepted.connect(self.GetClientAdd)
        self.ClientAddChild.buttonBox.rejected.connect(self.ClientAddClose)
        self.ClientAddDialog.exec_()

    def GetClientAdd(self):
        self.adddict = {'name': self.ClientAddChild.namelineEdit.text(), 'id': self.ClientAddChild.idlineEdit.text(),
                        'tel': self.ClientAddChild.tellineEdit.text(),
                        'address': self.ClientAddChild.addresslineEdit.text(),
                        'cname': self.ClientAddChild.cnamelineEdit.text(),
                        'cemail': self.ClientAddChild.cemaillineEdit.text(),
                        'ctel': self.ClientAddChild.ctellineEdit.text(),
                        'relation': self.ClientAddChild.relationlineEdit.text()}
        try:
            if self.adddict['id'] == '':
                self.ClientAddFailDialog("id不能为空")
                self.ClientAddDialog.close()
                return 0
            for index in self.adddict:
                self.adddict[index] = transferContent(self.adddict[index])
            sql = "insert into client values('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                self.adddict['id'], self.adddict['name'], self.adddict['tel'], self.adddict['address'],
                self.adddict['cname'],
                self.adddict['ctel'], self.adddict['cemail'], self.adddict['relation'])
            print(sql)
            print(self.db)
            cursor = self.db.cursor()
            cursor.execute(sql)
            cursor.close()
            print('success')
            self.db.commit()
            self.ClientAddSuccessDialog()
        except Exception as err:
            print(str(type(err))[8:-2])
            print('fail!!!!')
            self.db.rollback()
            self.ClientAddFailDialog(str(type(err))[8:-2])
            return 0

        self.ClientAddDialog.close()

    def ClientAddClose(self):
        self.ClientAddDialog.close()

    def ClientAddSuccessDialog(self):
        self.ui.messagetextEdit.setText("插入记录成功")

    def ClientAddFailDialog(self, message):
        self.ui.messagetextEdit.setText("插入记录失败，错误类型为%s" % message)

    def ClientDelete(self):
        self.ClientDeleteChild = Ui_ClientDeleteDialog()
        self.ClientDeleteDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.ClientDeleteChild.setupUi(self.ClientDeleteDialog)
        self.ClientDeleteChild.buttonBox.accepted.connect(self.GetClientDelete)
        self.ClientDeleteChild.buttonBox.rejected.connect(self.ClientDeleteClose)
        self.ClientDeleteDialog.exec_()

    def GetClientDelete(self):
        self.deletedict = {'name': self.ClientDeleteChild.namelineEdit.text(),
                           'id': self.ClientDeleteChild.idlineEdit.text(),
                           'tel': self.ClientDeleteChild.tellineEdit.text(),
                           'address': self.ClientDeleteChild.addresslineEdit.text(),
                           'cname': self.ClientDeleteChild.cnamelineEdit.text()}
        self.DeleteCheck1 = self.ClientDeleteChild.checkBox1.isChecked()
        self.DeleteCheck2 = self.ClientDeleteChild.checkBox2.isChecked()
        self.deletecomboBoxdict = {'name': True if self.ClientDeleteChild.namecomboBox.currentText() == '是' else False,
                                   'id': True if self.ClientDeleteChild.idcomboBox.currentText() == '是' else False,
                                   'tel': True if self.ClientDeleteChild.telcomboBox.currentText() == '是' else False,
                                   'address': True if self.ClientDeleteChild.addresscomboBox.currentText() == '是' else False,
                                   'cname': True if self.ClientDeleteChild.cnamecomboBox.currentText() == '是' else False}

        try:
            current_index = []
            current_delete = []
            if self.DeleteCheck1:
                for index in self.deletedict:
                    if self.deletedict[index] != '':
                        current_index.append(index)
                string = ''
                for index in current_index:
                    current_sql = index + " = '%s'" % transferContent(self.deletedict[index]) if self.deletecomboBoxdict[
                        index] else index + " like '%" + transferContent(self.deletedict[index]) + "%'"
                    if index == current_index[0]:
                        string = "where " + current_sql
                    else:
                        string += " and " + current_sql

                tabs = db_search(self.db, 'client', string)
                for tab in tabs:
                    current_delete.append(tab[0])
            if self.DeleteCheck2:
                columns = ['id', 'tel', 'address', 'cname', 'ctel', 'cemail', 'relation']
                string = "where name=''"
                for index in columns:
                    string += " or %s=''" % index

                tabs = db_search(self.db, 'client', string)
                for tab in tabs:
                    current_delete.append(tab[0])

            current_delete = list(set(current_delete))
            flag = True
            for tmp_id in current_delete:
                cursor = self.db.cursor()
                sql = "select id from client where id='%s' and id not in (select client.id from client, CLS where" \
                      " client.id=CLS.client_id) and id not in (select client.id from client, CAB where" \
                      " client.id=CAB.client_id)" % transferContent(tmp_id)
                if cursor.execute(sql) == 1:
                    sql = "delete from client where id='%s'" % transferContent(tmp_id)
                    print(sql)
                    cursor.execute(sql)
                    cursor.close()
                    print('success')
                    self.db.commit()
                else:
                    flag = False
            if flag:
                self.ClientDeleteSuccessDialog()
            else:
                self.ClientDeleteFailDialog('部分客户不可被删除')
        except Exception as err:
            print(str(type(err))[8:-2])
            print('fail')
            self.db.rollback()
            self.ClientDeleteFailDialog(str(type(err))[8:-2])
            return 0

        self.ClientDeleteDialog.close()

    def ClientDeleteClose(self):
        self.ClientDeleteDialog.close()

    def ClientDeleteSuccessDialog(self):
        self.ui.messagetextEdit.setText("删除记录成功")

    def ClientDeleteFailDialog(self, message):
        self.ui.messagetextEdit.setText("删除记录失败，错误类型为%s" % message)

    def ClientUpdate(self):
        self.ClientUpdateChild = Ui_ClientUpdateDialog()
        self.ClientUpdateDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.ClientUpdateChild.setupUi(self.ClientUpdateDialog)
        self.ClientUpdateChild.buttonBox.accepted.connect(self.GetClientUpdate)
        self.ClientUpdateChild.buttonBox.rejected.connect(self.ClientUpdateClose)
        self.ClientUpdateDialog.exec_()

    def GetClientUpdate(self):
        self.olddict = {}
        self.olddict['name'] =  transferContent(self.ClientUpdateChild.namelineEdit.text())
        self.olddict['id'] =  transferContent(self.ClientUpdateChild.idlineEdit.text())
        self.olddict['tel'] = transferContent(self.ClientUpdateChild.tellineEdit.text())
        self.olddict['address'] = transferContent(self.ClientUpdateChild.addresslineEdit.text())
        self.olddict['cname'] = transferContent(self.ClientUpdateChild.cnamelineEdit.text())
        self.olddict['ctel'] = transferContent(self.ClientUpdateChild.ctellineEdit.text())
        self.olddict['cemail'] = transferContent(self.ClientUpdateChild.cemaillineEdit.text())
        self.olddict['relation'] = transferContent(self.ClientUpdateChild.relationlineEdit.text())

        self.combodict = {}  # 1 是 2 含有 3 为空
        self.combodict[
            'name'] = 1 if self.ClientUpdateChild.namecomboBox.currentText() == '是' else 2 if self.ClientUpdateChild.namecomboBox.currentText() == '含有' else 3
        self.combodict[
            'id'] = 1 if self.ClientUpdateChild.idcomboBox.currentText() == '是' else 2 if self.ClientUpdateChild.idcomboBox.currentText() == '含有' else 3
        self.combodict[
            'tel'] = 1 if self.ClientUpdateChild.telcomboBox.currentText() == '是' else 2 if self.ClientUpdateChild.telcomboBox.currentText() == '含有' else 3
        self.combodict[
            'address'] = 1 if self.ClientUpdateChild.addresscomboBox.currentText() == '是' else 2 if self.ClientUpdateChild.addresscomboBox.currentText() == '含有' else 3
        self.combodict[
            'cname'] = 1 if self.ClientUpdateChild.cnamecomboBox.currentText() == '是' else 2 if self.ClientUpdateChild.cnamecomboBox.currentText() == '含有' else 3
        self.combodict[
            'ctel'] = 1 if self.ClientUpdateChild.ctelcomboBox.currentText() == '是' else 2 if self.ClientUpdateChild.ctelcomboBox.currentText() == '含有' else 3
        self.combodict[
            'cemail'] = 1 if self.ClientUpdateChild.cemailcomboBox.currentText() == '是' else 2 if self.ClientUpdateChild.cemailcomboBox.currentText() == '含有' else 3
        self.combodict[
            'relation'] = 1 if self.ClientUpdateChild.relationcomboBox.currentText() == '是' else 2 if self.ClientUpdateChild.relationcomboBox.currentText() == '含有' else 3

        self.newdict = {}
        self.newdict['name'] = transferContent(self.ClientUpdateChild.namelineEdit_2.text())
        self.newdict['id'] = transferContent(self.ClientUpdateChild.idlineEdit_2.text())
        self.newdict['tel'] = transferContent(self.ClientUpdateChild.tellineEdit_2.text())
        self.newdict['address'] = transferContent(self.ClientUpdateChild.addresslineEdit_2.text())
        self.newdict['cname'] = transferContent(self.ClientUpdateChild.cnamelineEdit_2.text())
        self.newdict['ctel'] = transferContent(self.ClientUpdateChild.ctellineEdit_2.text())
        self.newdict['cemail'] = transferContent(self.ClientUpdateChild.cemaillineEdit_2.text())
        self.newdict['relation'] = transferContent(self.ClientUpdateChild.relationlineEdit_2.text())

        self.checkdict = {}
        self.checkdict['name'] = self.ClientUpdateChild.namecheckBox.isChecked()
        self.checkdict['id'] = self.ClientUpdateChild.idcheckBox.isChecked()
        self.checkdict['tel'] = self.ClientUpdateChild.telcheckBox.isChecked()
        self.checkdict['address'] = self.ClientUpdateChild.addresscheckBox.isChecked()
        self.checkdict['cname'] = self.ClientUpdateChild.cnamecheckBox.isChecked()
        self.checkdict['ctel'] = self.ClientUpdateChild.ctelcheckBox.isChecked()
        self.checkdict['cemail'] = self.ClientUpdateChild.cemailcheckBox.isChecked()
        self.checkdict['relation'] = self.ClientUpdateChild.relationcheckBox.isChecked()

        try:
            search_condition = ""
            for col in ['name', 'id', 'tel', 'address', 'cname', 'ctel', 'cemail', 'relation']:
                if self.combodict[col] == 3 or self.olddict[col] != "":
                    if search_condition == "":
                        search_condition += " where"
                    else:
                        search_condition += " and"
                    if self.combodict[col] == 3:
                        search_condition += " %s=''" % col
                    elif self.combodict[col] == 2:
                        search_condition += " " + col + " like " + "\'%" + self.olddict[col] + "%\'"
                    else:
                        search_condition += " %s='" % col + self.olddict[col] + "'"
            # print(search_condition)
            tabs = db_search(self.db, 'client', search_condition)
            # print(tabs)
            current_update = []
            for tab in tabs:
                current_update.append(tab[0])

            set_condition = ""
            for col in ['name', 'id', 'tel', 'address', 'cname', 'ctel', 'cemail', 'relation']:
                if self.checkdict[col]:
                    if set_condition == "":
                        set_condition += " set"
                    else:
                        set_condition += ","
                    set_condition += " " + col + "='" + self.newdict[col] + "'"
            if set_condition == "" or len(current_update) == 0 or (len(current_update) > 1 and self.checkdict['id']):
                if set_condition == "":
                    self.ClientUpdateFailDialog("未设置更新条件")
                elif len(current_update) == 0:
                    self.ClientUpdateFailDialog("没有找到符合查找条件的记录")
                else:
                    self.ClientUpdateFailDialog("不允许将ID批量更改同一个值")
            else:
                for tmp_id in current_update:
                    sql = "update client" + set_condition + " where id='%s'" % tmp_id
                    print(sql)
                    cursor = self.db.cursor()
                    cursor.execute(sql)
                    cursor.close()
                    print('success')
                    self.db.commit()
            self.ClientUpdateSuccessDialog()
        except Exception as err:
            print(str(type(err))[8:-2])
            print('fail')
            self.db.rollback()
            self.ClientUpdateFailDialog(str(type(err))[8:-2])
            return 0

        self.ClientUpdateDialog.close()

    def ClientUpdateClose(self):
        self.ClientUpdateDialog.close()

    def ClientUpdateSuccessDialog(self):
        self.ui.messagetextEdit.setText("更新记录成功")

    def ClientUpdateFailDialog(self, message):
        self.ui.messagetextEdit.setText("更新记录失败，错误类型为%s" % message)


class AccountForm(QWidget):
    def __init__(self):
        super().__init__()
        self.db = db_login("root", "010503", "127.0.0.1", "lab3")
        self.ui = Ui_AccountForm()
        self.ui.setupUi(self)
        self.ui.checkingtable.setColumnCount(5)  # 不设置不显示这些列
        self.ui.checkingtable.setHorizontalHeaderLabels(['账户号', '余额', '开户日期', '最近访问日期', '透支额'])
        self.ui.checkingtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
        self.ui.checkingtable.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

        self.ui.savingtable.setColumnCount(6)  # 不设置不显示这些列
        self.ui.savingtable.setHorizontalHeaderLabels(['账户号', '余额', '开户日期', '最近访问日期', '利率', '货币类型'])
        self.ui.savingtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
        self.ui.savingtable.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

        self.ui.othertable.setColumnCount(4)  # 不设置不显示这些列
        self.ui.othertable.setHorizontalHeaderLabels(['账户号', '身份证号', '姓名', '开户地点'])
        self.ui.othertable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽self.show()
        self.ui.othertable.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

        self.ui.othertable_2.setColumnCount(4)  # 不设置不显示这些列
        self.ui.othertable_2.setHorizontalHeaderLabels(['账户号', '身份证号', '姓名', '开户地点'])
        self.ui.othertable_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽self.show()
        self.ui.othertable_2.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

        self.ui.SearchBtn.clicked.connect(self.AccountSearch)
        self.ui.AddBtn.clicked.connect(self.AccountAdd)
        self.ui.DeleteBtn.clicked.connect(self.AccountDelete)
        self.ui.UpdateBtn.clicked.connect(self.AccountUpdate)

    def AccountSearch(self):
        self.AccountSearchChild = Ui_AccountSearchDialog()
        self.AccountSearchDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.AccountSearchChild.setupUi(self.AccountSearchDialog)
        self.AccountSearchChild.buttonBox.accepted.connect(self.GetAccountSearch)
        self.AccountSearchChild.buttonBox.rejected.connect(self.AccountSearchClose)
        self.AccountSearchDialog.exec_()

    def GetAccountSearch(self):
        searchdict = {'checkid': self.AccountSearchChild.checkidlineEdit.text(),
                      'checkbalance': self.AccountSearchChild.checkbalancelineEdit.text(),
                      'checkoverdraft': self.AccountSearchChild.checkoverdraftlineEdit.text(),
                      'saveid': self.AccountSearchChild.saveidlineEdit.text(),
                      'savebalance': self.AccountSearchChild.savebalancelineEdit.text(),
                      'saverate': self.AccountSearchChild.saveratelineEdit.text()}
        searchcomboBox = {'checkid': self.AccountSearchChild.checkidcomboBox.currentIndex(),
                          'checkbalance': self.AccountSearchChild.checkbalancecomboBox.currentIndex(),
                          'checkopeningdate': self.AccountSearchChild.checkopeningdatecomboBox.currentIndex(),
                          'checkrecentreach': self.AccountSearchChild.checkrecentreachcomboBox.currentIndex(),
                          'checkoverdraft': self.AccountSearchChild.checkoverdraftcomboBox.currentIndex(),
                          'saveid': self.AccountSearchChild.saveidcomboBox.currentIndex(),
                          'savebalance': self.AccountSearchChild.savebalancecomboBox.currentIndex(),
                          'saveopeningdate': self.AccountSearchChild.saveopeningdatecomboBox.currentIndex(),
                          'saverecentreach': self.AccountSearchChild.saverecentreachcomboBox.currentIndex(),
                          'saverate': self.AccountSearchChild.saveratecomboBox.currentIndex(),
                          'savecurrency': self.AccountSearchChild.savecurrencycomboBox.currentIndex()}
        checkBox = {'check': self.AccountSearchChild.checkcheckBox.isChecked(),
                    'save': self.AccountSearchChild.savecheckBox.isChecked(),
                    'CAB1': self.AccountSearchChild.CABcheckBox.isChecked(),
                    'CAB2': self.AccountSearchChild.CABcheckBox_2.isChecked()}
        CAB1content = self.AccountSearchChild.CABlineEdit.text()
        CAB2content = self.AccountSearchChild.CABlineEdit_2.text()

        condition1 = ""
        for label in ['checkid', 'checkbalance', 'checkopeningdate', 'checkrecentreach', 'checkoverdraft']:
            if searchcomboBox[label] != 0:
                condition1 += " and"
                if label == "checkid":
                    tmp_con = ' account.id'
                    tmp_con += "='" + searchdict[label] + "'" if searchcomboBox[label] == 1 else " like '%" + \
                                                                                                 searchdict[
                                                                                                     label] + "%'"
                    condition1 += tmp_con
                elif label == "checkbalance":
                    tmp_con = ' account.balance'
                    tmp_con += '=' if searchcomboBox[label] == 1 else '>' if searchcomboBox[label] == 2 else '<'
                    tmp_con += searchdict[label]
                    condition1 += tmp_con
                elif label == "checkopeningdate":
                    tmp_con = ' to_days(curdate())-to_days(account.opening_date)'
                    tmp_con += '<365' if searchcomboBox[label] == 1 else '<731' if searchcomboBox[
                                                                                       label] == 2 else '>730'
                    condition1 += tmp_con
                elif label == "checkrecentreach":
                    tmp_con = ' to_days(curdate())-to_days(account.recent_reach)'
                    tmp_con += '<31' if searchcomboBox[label] == 1 else '<181' if searchcomboBox[
                                                                                      label] == 2 else '<366' if \
                        searchcomboBox[label] == 3 else '>365'
                    condition1 += tmp_con
                else:
                    tmp_con = ' checking_account.overdraft'
                    tmp_con += '=' if searchcomboBox[label] == 1 else '>' if searchcomboBox[label] == 2 else '<'
                    tmp_con += searchdict[label]
                    condition1 += tmp_con
        sql = "select account.id, account.balance, account.opening_date, account.recent_reach, checking_account.overdraft" \
              " from account, checking_account where checking_account.account_id=account.id"

        sql += condition1
        print(sql)
        cursor = self.db.cursor()
        cursor.execute(sql)
        tabs1 = cursor.fetchall()

        rowNum1 = len(tabs1)  # 获取查询到的行数
        columnNum1 = len(tabs1[0]) if rowNum1 > 0 else 0  # 获取查询到的列数

        condition2 = ""
        for label in ['saveid', 'savebalance', 'saveopeningdate', 'saverecentreach', 'saverate', 'savecurrency']:
            if searchcomboBox[label] != 0:
                condition2 += " and"
                if label == "saveid":
                    tmp_con = ' account.id'
                    tmp_con += "='" + searchdict[label] + "'" if searchcomboBox[label] == 1 else " like '%" + \
                                                                                                 searchdict[
                                                                                                     label] + "%'"
                    condition2 += tmp_con
                elif label == "savebalance":
                    tmp_con = ' account.balance'
                    tmp_con += '=' if searchcomboBox[label] == 1 else '>' if searchcomboBox[label] == 2 else '<'
                    tmp_con += searchdict[label]
                    condition2 += tmp_con
                elif label == "saveopeningdate":
                    tmp_con = ' to_days(curdate())-to_days(account.opening_date)'
                    tmp_con += '<365' if searchcomboBox[label] == 1 else '<731' if searchcomboBox[
                                                                                       label] == 2 else '>730'
                    condition2 += tmp_con
                elif label == "saverecentreach":
                    tmp_con = ' to_days(curdate())-to_days(account.recent_reach)'
                    tmp_con += '<31' if searchcomboBox[label] == 1 else '<181' if searchcomboBox[
                                                                                      label] == 2 else '<366' if \
                        searchcomboBox[label] == 3 else '>365'
                    condition2 += tmp_con
                elif label == "saverate":
                    tmp_con = ' saving_account.rate'
                    tmp_con += '=' if searchcomboBox[label] == 1 else '>' if searchcomboBox[label] == 2 else '<'
                    tmp_con += searchdict[label]
                    condition2 += tmp_con
                else:
                    tmp_con = "saving_account.currency_type='RMB'" if searchcomboBox[
                                                                          label] == 1 else "saving_account.currency_type='dollar'" if \
                        searchcomboBox[
                            label] == 2 else "saving_account.currency_type<>'RMB' and saving_account.currency_type<>'dollar'"
                    condition2 += tmp_con
        sql = "select account.id, account.balance, account.opening_date, account.recent_reach, saving_account.rate, saving_account.currency_type from account, saving_account where saving_account.account_id=account.id"

        sql += condition2
        print(sql)
        cursor = self.db.cursor()
        cursor.execute(sql)
        tabs2 = cursor.fetchall()

        rowNum2 = len(tabs2)  # 获取查询到的行数
        columnNum2 = len(tabs2[0]) if rowNum2 > 0 else 0  # 获取查询到的列数

        try:
            if checkBox['check']:
                # print(len(tabs1), "\n\n\n\n")
                self.ui.checkingtable.setRowCount(0)
                currentRowCount = self.ui.checkingtable.rowCount()
                for tab in tabs1:
                    self.ui.checkingtable.insertRow(currentRowCount)
                    item = {}
                    for i in range(columnNum1):
                        item[i] = QTableWidgetItem(str(tab[i]))
                        item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ui.checkingtable.setItem(currentRowCount, i, item[i])  # 列i+1
                    # self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
                    currentRowCount += 1
                    self.ui.checkingtable.setRowCount(currentRowCount)
            if checkBox['save']:
                self.ui.savingtable.setRowCount(0)
                currentRowCount = self.ui.savingtable.rowCount()
                for tab in tabs2:
                    self.ui.savingtable.insertRow(currentRowCount)
                    item = {}
                    for i in range(columnNum2):
                        item[i] = QTableWidgetItem(str(tab[i]))
                        item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ui.savingtable.setItem(currentRowCount, i, item[i])  # 列i+1
                    # self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
                    currentRowCount += 1
                    self.ui.savingtable.setRowCount(currentRowCount)
            if checkBox['CAB1']:
                sql = "select account.id, client.id,client.name, branch.name from account, client, branch, CAB where account.id=CAB.account_ID and client.id=CAB.client_id and CAB.branch_name=branch.name and account.id='" + CAB1content + "'"
                print(sql)
                cursor = self.db.cursor()
                cursor.execute(sql)
                tabs3 = cursor.fetchall()
                rowNum3 = len(tabs3)  # 获取查询到的行数
                columnNum3 = len(tabs3[0]) if rowNum3 > 0 else 0  # 获取查询到的列数
                self.ui.othertable.setRowCount(0)
                currentRowCount = self.ui.othertable.rowCount()
                for tab in tabs3:
                    self.ui.othertable.insertRow(currentRowCount)
                    item = {}
                    for i in range(columnNum3):
                        item[i] = QTableWidgetItem(str(tab[i]))
                        item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ui.othertable.setItem(currentRowCount, i, item[i])  # 列i+1
                    # self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
                    currentRowCount += 1
                    self.ui.othertable.setRowCount(currentRowCount)
            if checkBox['CAB2']:
                sql = "select account.id, client.id,client.name, branch.name from account, client, branch, CAB where account.id=CAB.account_ID and client.id=CAB.client_id and CAB.branch_name=branch.name and client.id='" + CAB2content + "'"
                print(sql)
                cursor = self.db.cursor()
                cursor.execute(sql)
                tabs4 = cursor.fetchall()
                rowNum4 = len(tabs4)  # 获取查询到的行数
                columnNum4 = len(tabs4[0]) if rowNum4 > 0 else 0  # 获取查询到的列数
                self.ui.othertable_2.setRowCount(0)
                currentRowCount = self.ui.othertable_2.rowCount()
                for tab in tabs4:
                    self.ui.othertable_2.insertRow(currentRowCount)
                    item = {}
                    for i in range(columnNum4):
                        item[i] = QTableWidgetItem(str(tab[i]))
                        item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ui.othertable_2.setItem(currentRowCount, i, item[i])  # 列i+1
                    # self.ui.table.setItem(currentRowCount, 1, item1)  # 列2
                    currentRowCount += 1
                    self.ui.othertable_2.setRowCount(currentRowCount)
            self.AccountSearchSuccessDialog()

        except Exception as err:
            print(str(type(err))[8:-2])
            print('fail')
            self.db.rollback()
            self.AccountSearchFailDialog(str(type(err))[8:-2])
        finally:
            self.AccountSearchDialog.close()

    def AccountSearchSuccessDialog(self):
        self.ui.messagetextEdit.setText("查询记录成功")

    def AccountSearchFailDialog(self, message):
        self.ui.messagetextEdit.setText("查询记录失败，错误类型为%s" % message)

    def AccountSearchClose(self):
        self.AccountSearchDialog.close()

    def AccountAdd(self):
        self.AccountAddChild = Ui_AccountAddDialog()
        self.AccountAddDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.AccountAddChild.setupUi(self.AccountAddDialog)
        self.AccountAddChild.buttonBox.accepted.connect(self.GetAccountAdd)
        self.AccountAddChild.buttonBox.rejected.connect(self.AccountAddClose)
        self.AccountAddDialog.exec_()

    def GetAccountAdd(self):
        self.adddict = {'account': self.AccountAddChild.accountlineEdit.text(),
                        'client': self.AccountAddChild.clientlineEdit.text(),
                        'type': "checking" if self.AccountAddChild.comboBox.currentIndex() == 1 else "saving",
                        'branch': self.AccountAddChild.branchlineEdit.text(),
                        'rate': self.AccountAddChild.ratelineEdit.text(),
                        'currency': self.AccountAddChild.typelineEdit.text(),
                        'overdraft': self.AccountAddChild.overdraftlineEdit.text()}
        if self.adddict['account'] == '' or self.adddict['client'] == '' or self.adddict['branch'] == '' or (
                self.adddict['type'] == 'checking' and self.adddict['overdraft'] == '') or (
                self.adddict['type'] == 'saving' and (
                self.adddict['rate'] == '' or self.adddict['currency'] == '') or self.adddict['type'] not in [
                    'checking', 'saving']):
            self.AccountAddFailDialog('信息输入不全')
        else:
            sql = "select count(*) from client where id='" + self.adddict['client'] + "'"
            cursor = self.db.cursor()
            cursor.execute(sql)
            number1 = cursor.fetchone()[0]
            sql = "select count(*) from branch where name='" + self.adddict['branch'] + "'"
            cursor.execute(sql)
            number2 = cursor.fetchone()[0]
            if number1 + number2 < 2:
                self.AccountAddFailDialog("客户或网点不在数据库中")
            else:
                sql = "select count(*) from account where id='" + self.adddict['account'] + "'"
                cursor.execute(sql)
                number3 = cursor.fetchone()[0]
                if number3 == 0:
                    sql = "insert into account values ('" + self.adddict['account'] + "', '" + self.adddict[
                        'type'] + "', 0, curdate(), curdate())"
                    try:
                        print(sql)
                        cursor.execute(sql)
                        print('success')
                        # self.db.commit()
                        if self.adddict['type'] == "checking":
                            sql = "insert into checking_account values(" + self.adddict["overdraft"] + ", '" + \
                                  self.adddict[
                                      "account"] + "')"
                        else:
                            sql = "insert into saving_account values(" + self.adddict["rate"] + ", '" + self.adddict[
                                "currency"] + "', '" + self.adddict["account"] + "')"
                        print(sql)
                        cursor.execute(sql)
                        print("success")
                        # self.db.commit()
                        sql = "insert into CAB values ('" + self.adddict['client'] + "', '" + self.adddict[
                        'account'] + "', '" + self.adddict['type'] + "', '" + self.adddict['branch'] + "')"
                        try:
                            print(sql)
                            cursor.execute(sql)
                            print("success")
                            self.db.commit()
                            self.AccountAddSuccessDialog()
                        except Exception as err:
                            print(str(type(err))[8:-2])
                            print('fail')
                            self.db.rollback()
                            self.AccountAddFailDialog(str(type(err))[8:-2])
                            return 0
                    except Exception as err:
                        print(str(type(err))[8:-2])
                        print('fail')
                        self.db.rollback()
                        self.AccountAddFailDialog(str(type(err))[8:-2])
                        return 0


        self.AccountAddDialog.close()

    def AccountAddClose(self):
        self.AccountAddDialog.close()

    def AccountAddSuccessDialog(self):
        self.ui.messagetextEdit.setText("插入记录成功")

    def AccountAddFailDialog(self, message):
        self.ui.messagetextEdit.setText("插入记录失败，错误类型为%s" % message)

    def AccountDelete(self):
        self.AccountDeleteChild = Ui_AccountDeleteDialog()
        self.AccountDeleteDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.AccountDeleteChild.setupUi(self.AccountDeleteDialog)
        self.AccountDeleteChild.buttonBox.accepted.connect(self.GetAccountDelete)
        self.AccountDeleteChild.buttonBox.rejected.connect(self.AccountDeleteClose)
        self.AccountDeleteDialog.exec_()

    def GetAccountDelete(self):
        self.deletedict = {'account': self.AccountDeleteChild.accountlineEdit.text(),
                           'client': self.AccountDeleteChild.clientlineEdit.text(),
                           'check': self.AccountDeleteChild.checkBox.isChecked()}
        cursor = self.db.cursor()
        if not self.deletedict['check']:
            try:
                sql = "delete from account where id='%s'" % self.deletedict['account']
                print(sql)
                if cursor.execute(sql) > 0:
                    print('success')
                    self.AccountDeleteSuccessDialog()
                    self.db.commit()
                else:
                    self.AccountDeleteFailDialog("未找到符合条件的记录")
            except Exception as err:
                print(str(type(err))[8:-2])
                print('fail')
                self.db.rollback()
                self.AccountDeleteFailDialog(str(type(err))[8:-2])
        else:
            try:
                sql = "delete from CAB where account_id='%s' and client_id='%s'" % (
                    self.deletedict['account'], self.deletedict['client'])
                print(sql)
                if cursor.execute(sql) > 0:
                    print('success')
                    self.AccountDeleteSuccessDialog()
                    self.db.commit()
                else:
                    self.AccountDeleteFailDialog("未找到符合条件的记录")
            except Exception as err:
                print(str(type(err))[8:-2])
                print('fail')
                self.db.rollback()
                self.AccountDeleteFailDialog(str(type(err))[8:-2])
        self.AccountDeleteDialog.close()

    def AccountDeleteClose(self):
        self.AccountDeleteDialog.close()

    def AccountDeleteSuccessDialog(self):
        self.ui.messagetextEdit.setText("删除记录成功")

    def AccountDeleteFailDialog(self, message):
        self.ui.messagetextEdit.setText("删除记录失败，错误类型为%s" % message)

    def AccountUpdate(self):
        self.db = db_login("root", "010503", "127.0.0.1", "lab3")
        self.AccountUpdateChild = Ui_AccountUpdateDialog()
        self.AccountUpdateDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.AccountUpdateChild.setupUi(self.AccountUpdateDialog)
        self.AccountUpdateChild.buttonBox.accepted.connect(self.GetAccountUpdate)
        self.AccountUpdateChild.buttonBox.rejected.connect(self.AccountUpdateClose)
        self.AccountUpdateDialog.exec_()

    def GetAccountUpdate(self):
        self.olddict = {'account': self.AccountUpdateChild.accountlineEdit.text(),
                        'type': 'saving' if self.AccountUpdateChild.comboBox.currentIndex() == 0 else 'checking',
                        'currency': self.AccountUpdateChild.currencylineEdit.text(),
                        'rate': self.AccountUpdateChild.ratelineEdit.text(),
                        'overdraft': self.AccountUpdateChild.overdraftlineEdit.text()}

        self.checkdict = {'type': self.AccountUpdateChild.typecheckBox.isChecked(),
                          'rate': self.AccountUpdateChild.ratecheckBox.isChecked(),
                          'currency': self.AccountUpdateChild.currencycheckBox.isChecked(),
                          'overdraft': self.AccountUpdateChild.overdraftcheckBox.isChecked()}

        try:
            cursor = self.db.cursor()
            sql = "select type from account where id='%s'" % self.olddict['account']
            print(sql)
            cursor.execute(sql)
            now_type = cursor.fetchone()[0]
            print(now_type)
            if self.checkdict['type']:
                if self.olddict['type'] == 'saving' and now_type == 'saving':
                    if self.checkdict['rate'] and self.checkdict['currency']:
                        sql = "update saving_account set rate=" + self.olddict[
                            'rate'] + ", currency='%s' where account_id='%s'" % (self.olddict['currency'], self.olddict[
                            'account'])
                    elif self.checkdict['rate']:
                        sql = "update saving_account set rate=" + self.olddict[
                            'rate'] + " where account_id='%s'" % self.olddict['account']
                    elif self.checkdict['currency']:
                        sql = "update saving_account set currency_type='%s' where account_id='%s'" % (
                            self.olddict['currency'], self.olddict['account'])
                    else:
                        sql = ""
                    if sql != "":
                        print(sql)
                        cursor.execute(sql)
                elif self.olddict['type'] == 'checking' and now_type == 'checking':
                    if self.checkdict['overdraft']:
                        sql = "update checking_account set overdraft=" + self.olddict[
                            'overdraft'] + " where account_id='%s'" % self.olddict['account']
                        print(sql)
                        cursor.execute(sql)
                elif self.olddict['type'] == 'checking':
                    sql = "delete from saving_account where account_id='%s'" % self.olddict['account']
                    print(sql)
                    cursor.execute(sql)
                    sql = "insert into checking_account values(%s, '%s')" % (self.olddict['overdraft'], self.olddict[
                        'account'])
                    print(sql)
                    cursor.execute(sql)
                    sql = "update account set type='checking' where id='%s'" % self.olddict['account']
                    print(sql)
                    cursor.execute(sql)
                    self.db.commit()
                else:
                    sql = "delete from checking_account where account_id='%s'" % self.olddict['account']
                    print(sql)
                    cursor.execute(sql)
                    sql = "insert into saving_account values(%s, '%s', '%s')" % (self.olddict['rate'], self.olddict[
                        'currency'], self.olddict['account'])
                    print(sql)
                    cursor.execute(sql)
                    sql = "update account set type='saving' where id='%s'" % self.olddict['account']
                    print(sql)
                    cursor.execute(sql)
                    self.db.commit()
            else:
                if now_type == 'checking' and self.checkdict['overdraft']:
                    sql = "update checking_account set overdraft=%s where account_id='%s'" % (
                        self.olddict['overdraft'], self.olddict['account'])
                    print(sql)
                    cursor.execute(sql)
                if now_type == 'saving' and self.checkdict['rate']:
                    sql = "update saving_account set rate=%s where account_id='%s'" % (
                        self.olddict['rate'], self.olddict['account'])
                    print(sql)
                    cursor.execute(sql)
                if now_type == 'saving' and self.checkdict['currency']:
                    sql = "update saving_account set currency_type='%s' where account_id='%s'" % (
                        self.olddict['currency'], self.olddict['account'])
                    print(sql)
                    cursor.execute(sql)
            self.db.commit()
            self.AccountUpdateSuccessDialog()

        except Exception as err:
            print(str(type(err))[8:-2])
            print('fail')
            self.db.rollback()
            self.AccountUpdateFailDialog(str(type(err))[8:-2])

        self.AccountUpdateDialog.close()

    def AccountUpdateClose(self):
        self.AccountUpdateDialog.close()

    def AccountUpdateSuccessDialog(self):
        self.ui.messagetextEdit.setText("更新记录成功")

    def AccountUpdateFailDialog(self, message):
        self.ui.messagetextEdit.setText("更新记录失败，错误类型为%s" % message)


class BusinessForm(QWidget):
    def __init__(self):
        super().__init__()
        self.db = db_login("root", "010503", "127.0.0.1", "lab3")
        self.ui = Ui_BusinessForm()
        self.ui.setupUi(self)
        self.ui.loantable.setColumnCount(7)  # 不设置不显示这些列
        self.ui.loantable.setHorizontalHeaderLabels(['贷款号', '申请时间', '贷款总额', '发放情况', '还款情况', '贷款人', '贷款账户'])
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

        self.ui.SearchBtn.clicked.connect(self.BusinessSearch)
        self.ui.AddBtn.clicked.connect(self.BusinessAdd)
        self.ui.DeleteBtn.clicked.connect(self.BusinessDelete)

    def BusinessSearch(self):
        self.BusinessSearchChild = Ui_BusinessSearchDialog()
        self.BusinessSearchDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.BusinessSearchChild.setupUi(self.BusinessSearchDialog)
        self.BusinessSearchChild.buttonBox.accepted.connect(self.GetBusinessSearch)
        self.BusinessSearchChild.buttonBox.rejected.connect(self.BusinessSearchClose)
        self.BusinessSearchDialog.exec_()

    def GetBusinessSearch(self):
        loancomboBoxdict = {'loanid': self.BusinessSearchChild.loanidcomboBox.currentIndex(),
                            'clientid': self.BusinessSearchChild.clientidcomboBox.currentIndex(),
                            'accountid': self.BusinessSearchChild.accountidcomboBox.currentIndex(),
                            'loanamount': self.BusinessSearchChild.loanamountcomboBox.currentIndex(),
                            'loangrantstatus': self.BusinessSearchChild.loangrantstatuscomboBox.currentIndex(),
                            'loanrepaystatus': self.BusinessSearchChild.loanrepaycomboBox.currentIndex()}

        loantextdict = {'loanid': self.BusinessSearchChild.loanidlineEdit.text(),
                        'clientid': self.BusinessSearchChild.clientidlineEdit.text(),
                        'accountid': self.BusinessSearchChild.accountidlineEdit.text(),
                        'loanamount': self.BusinessSearchChild.loanamountlineEdit.text()}

        grantcomboBoxdict = {'grantid': self.BusinessSearchChild.grantidcomboBox.currentIndex(),
                             'grantloanid': self.BusinessSearchChild.grantloanidcomboBox.currentIndex(),
                             'grantamount': self.BusinessSearchChild.grantamountcomboBox.currentIndex(),
                             'grantleftamount': self.BusinessSearchChild.grantleftamountcomboBox.currentIndex(),
                             'grantdate': self.BusinessSearchChild.grantdatecomboBox.currentIndex(),
                             'grantstatus': self.BusinessSearchChild.grantstatuscomboBox.currentIndex()}

        granttextdict = {'grantid': self.BusinessSearchChild.grantidlineEdit.text(),
                         'grantloanid': self.BusinessSearchChild.grantloanidlineEdit.text(),
                         'grantamount': self.BusinessSearchChild.grantamountlineEdit.text(),
                         'grantleftamount': self.BusinessSearchChild.grantleftamountlineEdit.text()}

        repaycomboBoxdict = {'repayid': self.BusinessSearchChild.repayidcomboBox.currentIndex(),
                             'repayloanid': self.BusinessSearchChild.repayloanidcomboBox.currentIndex(),
                             'repayamount': self.BusinessSearchChild.repayamountcomboBox.currentIndex(),
                             'repayleftamount': self.BusinessSearchChild.repayleftamountcomboBox.currentIndex(),
                             'repaydate': self.BusinessSearchChild.repaydatecomboBox.currentIndex(),
                             'repaystatus': self.BusinessSearchChild.repaystatuscomboBox.currentIndex()}

        repaytextdict = {'repayid': self.BusinessSearchChild.repayidlineEdit.text(),
                         'repayloanid': self.BusinessSearchChild.repayloanidlineEdit.text(),
                         'repayamount': self.BusinessSearchChild.repayamountlineEdit.text(),
                         'repayleftamount': self.BusinessSearchChild.repayleftamountlineEdit.text()}

        checkBox = {'loan': self.BusinessSearchChild.loancheckBox.isChecked(),
                    'grant': self.BusinessSearchChild.grantcheckBox.isChecked(),
                    'repay': self.BusinessSearchChild.repaycheckBox.isChecked()}

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
            self.BusinessSearchSuccessDialog()

        except Exception as err:
            print(str(type(err))[8:-2])
            print('fail')
            self.db.rollback()
            self.BusinessSearchFailDialog(str(type(err))[8:-2])
        finally:
            self.BusinessSearchDialog.close()

    def BusinessSearchSuccessDialog(self):
        self.ui.messagetextEdit.setText("查询记录成功")

    def BusinessSearchFailDialog(self, message):
        self.ui.messagetextEdit.setText("查询记录失败，错误类型为%s" % message)

    def BusinessSearchClose(self):
        self.BusinessSearchDialog.close()

    def BusinessAdd(self):
        self.BusinessAddChild = Ui_BusinessAddDialog()
        self.BusinessAddDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.BusinessAddChild.setupUi(self.BusinessAddDialog)
        self.BusinessAddChild.buttonBox.accepted.connect(self.GetBusinessAdd)
        self.BusinessAddChild.buttonBox.rejected.connect(self.BusinessAddClose)
        self.BusinessAddDialog.exec_()

    def GetBusinessAdd(self):
        self.adddict = {'loanid': self.BusinessAddChild.loanidlineEdit.text(),
                        'loanaccount': self.BusinessAddChild.loanaccountlineEdit.text(),
                        'loanclient': self.BusinessAddChild.loanclientlineEdit.text(),
                        'loantotal': self.BusinessAddChild.loantotalidlineEdit.text(),
                        'grantid': self.BusinessAddChild.grantidlineEdit.text(),
                        'grantloanid': self.BusinessAddChild.grantloanidlineEdit.text(),
                        'grantamount': self.BusinessAddChild.grantamountlineEdit.text(),
                        'repayid': self.BusinessAddChild.repayidlineEdit.text(),
                        'repayloanid': self.BusinessAddChild.repayloanidlineEdit.text(),
                        'repayamount': self.BusinessAddChild.repayamountlineEdit.text()}

        self.addcomboBox = {'grant': self.BusinessAddChild.grantcomboBox.currentIndex(),
                            'repay': self.BusinessAddChild.repaycomboBox.currentIndex()}

        self.addcheckBox = {'loan': self.BusinessAddChild.loancheckBox.isChecked(),
                            'grant': self.BusinessAddChild.grantcheckBox.isChecked(),
                            'repay': self.BusinessAddChild.repaycheckBox.isChecked()}

        if self.addcheckBox['loan']:
            sql = "select * from CAB where client_id in ('%s') and account_id in ('%s')" % (
                self.adddict['loanclient'], self.adddict['loanaccount'])
            cursor = self.db.cursor()
            print(sql)
            if cursor.execute(sql) == 0:
                self.BusinessAddFailDialog("贷款人和贷款账户不对应")
                return 0
            sql1 = "insert into loan values('%s', curdate(), %s, '未发放', '未偿还')" % (
                self.adddict['loanid'], self.adddict['loantotal'])
            sql2 = "insert into CLS values('%s', '%s', '%s')" % (
                self.adddict['loanclient'], self.adddict['loanaccount'], self.adddict['loanid'])
            try:
                print(sql1)
                cursor = self.db.cursor()
                cursor.execute(sql1)
                print(sql2)
                cursor.execute(sql2)
                self.db.commit()
                self.BusinessAddSuccessDialog()
            except Exception as err:
                print(str(type(err))[8:-2])
                print('fail')
                self.db.rollback()
                self.BusinessAddFailDialog(str(type(err))[8:-2])
                return 0
        if self.addcheckBox['grant']:
            sql1 = "select * from grant_loan where loan_lid='%s'" % self.adddict['grantloanid']
            cursor = self.db.cursor()
            flag = True if cursor.execute(sql1) != 0 else False
            if flag:
                sql = "select left_amount from grant_loan where loan_lid='%s' order by left_amount asc" % self.adddict[
                    'grantloanid']
                print(sql)
                cursor = self.db.cursor()
                cursor.execute(sql)
                now_left = cursor.fetchone()[0]
            else:
                sql = "select total from loan where lid='%s'" % self.adddict['grantloanid']
                cursor.execute(sql)
                now_left = cursor.fetchone()[0]
            if now_left == 0:
                self.BusinessAddFailDialog("该贷款已发放完毕")
            elif now_left < float(self.adddict['grantamount']):
                self.BusinessAddFailDialog("超过未发放金额")
            else:
                try:
                    sql = "insert into grant_loan values('%s', curdate(), %s, %s, '%s')" % (
                        self.adddict['grantid'], self.adddict['grantamount'],
                        str(now_left - float(self.adddict['grantamount'])), self.adddict['grantloanid'])
                    print(sql)
                    cursor.execute(sql)
                    if now_left - float(self.adddict['grantamount']) == 0:
                        sql = "update loan set grant_status='已发放' where lid='%s'" % self.adddict['grantloanid']
                    else:
                        sql = "update loan set grant_status='发放中' where lid='%s'" % self.adddict['grantloanid']
                    print(sql)
                    cursor.execute(sql)
                    self.db.commit()
                    if self.addcomboBox['grant'] == 1:
                        sql = "select account_id from CLS where loan_lid='%s'" % self.adddict['grantloanid']
                        print(sql)
                        cursor.execute(sql)
                        tmp_account_id = cursor.fetchone()[0]
                        sql = "update account set balance=balance+%s where id='%s'" % (
                            self.adddict['grantamount'], tmp_account_id)
                        print(sql)
                        cursor.execute(sql)
                        self.db.commit()
                except Exception as err:
                    print(str(type(err))[8:-2])
                    print('fail')
                    self.db.rollback()
                    self.BusinessAddFailDialog(str(type(err))[8:-2])
                    return 0
        if self.addcheckBox['repay']:
            sql1 = "select * from repay_loan where loan_lid='%s'" % self.adddict['repayloanid']
            cursor = self.db.cursor()
            flag = True if cursor.execute(sql1) != 0 else False
            if flag:
                sql = "select left_amount from repay_loan where loan_lid='%s' order by left_amount asc" % self.adddict[
                    'repayloanid']
                print(sql)
                cursor = self.db.cursor()
                cursor.execute(sql)
                now_left = cursor.fetchone()[0]
            else:
                sql = "select total from loan where lid='%s'" % self.adddict['repayloanid']
                cursor.execute(sql)
                now_left = cursor.fetchone()[0]
            if now_left == 0:
                self.BusinessAddFailDialog("该贷款已经还款完毕")
            elif now_left < float(self.adddict['repayamount']):
                self.BusinessAddFailDialog("超过剩余欠款金额")
            else:
                try:
                    sql = "insert into repay_loan values('%s', curdate(), %s, %s, '%s')" % (
                        self.adddict['repayid'], str(float(self.adddict['repayamount'])),
                        str(now_left - float(self.adddict['repayamount'])), self.adddict['repayloanid'])
                    print(sql)
                    cursor.execute(sql)
                    if now_left - float(self.adddict['repayamount']) == 0:
                        sql = "update loan set repay_status='已偿还' where lid='%s'" % self.adddict['repayloanid']
                    else:
                        sql = "update loan set repay_status='偿还中' where lid='%s'" % self.adddict['repayloanid']
                    print(sql)
                    cursor.execute(sql)
                    print('here')
                    if self.addcomboBox['repay'] == 1:
                        sql = "select account_id from CLS where loan_lid='%s'" % self.adddict['repayloanid']
                        print(sql)
                        cursor.execute(sql)
                        tmp_account_id = cursor.fetchone()[0]
                        sql = "update account set balance=balance-%s where id='%s'" % (
                            self.adddict['repayamount'], tmp_account_id)
                        print(sql)
                        cursor.execute(sql)
                    self.db.commit()
                    self.BusinessAddSuccessDialog()
                except Exception as err:
                    print(str(type(err))[8:-2])
                    print('fail')
                    self.db.rollback()
                    self.BusinessAddFailDialog(str(type(err))[8:-2])

        self.BusinessAddDialog.close()

    def BusinessAddClose(self):
        self.BusinessAddDialog.close()

    def BusinessAddSuccessDialog(self):
        self.ui.messagetextEdit.setText("插入记录成功")

    def BusinessAddFailDialog(self, message):
        self.ui.messagetextEdit.setText("插入记录失败，错误类型为%s" % message)

    def BusinessDelete(self):
        self.BusinessDeleteChild = Ui_BusinessDeleteDialog()
        self.BusinessDeleteDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.BusinessDeleteChild.setupUi(self.BusinessDeleteDialog)
        self.BusinessDeleteChild.buttonBox.accepted.connect(self.GetBusinessDelete)
        self.BusinessDeleteChild.buttonBox.rejected.connect(self.BusinessDeleteClose)
        self.BusinessDeleteDialog.exec_()

    def GetBusinessDelete(self):
        self.idtext = self.BusinessDeleteChild.idlineEdit.text()
        sql = "select grant_status from loan where lid='%s'" % self.idtext
        cursor = self.db.cursor()
        print(sql)
        cursor.execute(sql)
        tmp_status = cursor.fetchone()
        tmp_status = tmp_status[0] if tmp_status is not None else None
        if tmp_status == None:
            self.BusinessDeleteFailDialog("未查询到相关记录")
        elif tmp_status == "发放中":
            self.BusinessDeleteFailDialog("不允许删除发放中的贷款")
        else:
            sql = "delete from loan where lid='%s'" % self.idtext
            try:
                print(sql)
                cursor.execute(sql)
                print('success')
                self.db.commit()
                self.BusinessDeleteSuccessDialog()
            except Exception as err:
                print(str(type(err))[8:-2])
                print('fail')
                self.db.rollback()
                self.BusinessDeleteFailDialog(str(type(err))[8:-2])
                return 0

        self.BusinessDeleteDialog.close()

    def BusinessDeleteClose(self):
        self.BusinessDeleteDialog.close()

    def BusinessDeleteSuccessDialog(self):
        self.ui.messagetextEdit.setText("删除记录成功")

    def BusinessDeleteFailDialog(self, message):
        self.ui.messagetextEdit.setText("删除记录失败，错误类型为%s" % message)


class StatisticForm(QWidget):
    def __init__(self):
        super().__init__()
        self.db = db_login("root", "010503", "127.0.0.1", "lab3")
        self.ui = Ui_StatisticForm()
        self.ui.setupUi(self)

        self.ui.SearchBtn.clicked.connect(self.StatisticSearch)

    def StatisticSearch(self):
        self.StatisticSearchChild = Ui_StatisticSearchDialog()
        self.StatisticSearchDialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏
        self.StatisticSearchChild.setupUi(self.StatisticSearchDialog)
        self.StatisticSearchChild.buttonBox.accepted.connect(self.GetStatisticSearch)
        self.StatisticSearchChild.buttonBox.rejected.connect(self.StatisticSearchClose)
        self.StatisticSearchDialog.exec_()

    def GetStatisticSearch(self):
        self.type = self.StatisticSearchChild.businesscomboBox.currentIndex()
        self.time = self.StatisticSearchChild.timecomboBox.currentIndex()
        self.num = self.StatisticSearchChild.numcomboBox.currentIndex()
        if self.type == 0:
            self.GetSaving()
        else:
            self.GetLoan()
        self.StatisticSearchSuccessDialog()

    def GetSaving(self):
        self.StatisticSetSaving()
        cursor = self.db.cursor()
        sql = "select name from branch"
        print(sql)
        cursor.execute(sql)
        ans = cursor.fetchall()
        branch_names = []
        for sub_ans in ans:
            branch_names.append(sub_ans[0])
        self.ui.table.setRowCount(0)
        currentRowCount = self.ui.table.rowCount()
        rowNum = len(branch_names)  # 获取查询到的行数
        columnNum = 5  # 获取查询到的列数
        for branch_name in branch_names:
            sql = "select sum(bal), sum(multi), DATE_FORMAT(curdate(), '%Y-%m-%d'), DATE_FORMAT(curdate()," \
                  " '%Y-%m-%d') from (select distinct(account.ID), account.balance as bal," \
                  " account.balance*saving_account.rate as multi from account, saving_account," \
                  " CAB where account.id=saving_account.account_id and CAB.account_ID=account.ID" \
                  " and CAB.branch_name='" + branch_name + "') as A"
            print(sql)
            cursor.execute(sql)
            ans = cursor.fetchone()
            tmp_ans = [branch_name] + list(ans)
            for i in range(1, 3):
                tmp_ans[i] = tmp_ans[i] if tmp_ans[i] is not None else 0
            ans = tuple(tmp_ans)
            self.ui.table.insertRow(currentRowCount)
            for i in range(columnNum):
                tmp_item = QTableWidgetItem(str(ans[i]))
                tmp_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.table.setItem(currentRowCount, i, tmp_item)  # 列i+1
            currentRowCount += 1
        self.ui.table.setRowCount(currentRowCount)
        self.StatisticSearchSuccessDialog()

    def GetLoan(self):
        self.StatisticSetLoan()
        cursor = self.db.cursor()
        sql = "select name from branch"
        print(sql)
        cursor.execute(sql)
        ans = cursor.fetchall()
        branch_names = []
        for sub_ans in ans:
            branch_names.append(sub_ans[0])
        self.ui.table.setRowCount(0)
        currentRowCount = self.ui.table.rowCount()
        columnNum = 6  # 获取查询到的列数

        for branch_name in branch_names:
            for i in range(1, self.num + 3):
                lag = i if self.time == 0 else i * 3 if self.time == 1 else i * 12
                plag = i - 1 if self.time == 0 else i * 3 - 3 if self.time == 1 else i * 12 - 12
                sql = "select sum(total) from loan where lid in (select loan.lid from CAB,CLS,loan where" \
                      " CAB.client_ID=CLS.client_ID and CAB.account_id=CLS.account_id and" \
                      " CLS.loan_LID=loan.lid and CAB.branch_name='%s' and datediff(loan.date," \
                      " DATE_SUB(CURDATE(),INTERVAL %s Month))<=0 and datediff(loan.date," \
                      " DATE_SUB(CURDATE(),INTERVAL %s Month))>=0)" % (branch_name, str(plag), str(lag))
                print(sql)
                cursor.execute(sql)
                loan_ans = cursor.fetchone()[0]
                loan_ans = loan_ans if loan_ans is not None else 0

                sql = "select sum(grant_amount) from grant_loan where id in (select grant_loan.id from CAB,CLS,grant_loan where" \
                      " CAB.client_ID=CLS.client_ID and CAB.account_id=CLS.account_id and" \
                      " CLS.loan_LID=grant_loan.loan_lid and CAB.branch_name='%s' and datediff(grant_loan.grant_date," \
                      " DATE_SUB(CURDATE(),INTERVAL %s Month))<=0 and datediff(grant_loan.grant_date," \
                      " DATE_SUB(CURDATE(),INTERVAL %s Month))>=0)" % (branch_name, str(plag), str(lag))
                print(sql)
                cursor.execute(sql)
                grant_ans = cursor.fetchone()[0]
                grant_ans = grant_ans if grant_ans is not None else 0

                sql = "select sum(repay_amount) from repay_loan where id in (select repay_loan.id from CAB,CLS,repay_loan where" \
                      " CAB.client_ID=CLS.client_ID and CAB.account_id=CLS.account_id and" \
                      " CLS.loan_LID=repay_loan.loan_lid and CAB.branch_name='%s' and datediff(repay_loan.repay_date," \
                      " DATE_SUB(CURDATE(),INTERVAL %s Month))<=0 and datediff(repay_loan.repay_date," \
                      " DATE_SUB(CURDATE(),INTERVAL %s Month))>=0)" % (branch_name, str(plag), str(lag))
                print(sql)
                cursor.execute(sql)
                repay_ans = cursor.fetchone()[0]
                repay_ans = repay_ans if repay_ans is not None else 0

                sql = "select DATE_FORMAT(DATE_SUB(CURDATE(),INTERVAL %s Month)" % str(lag) + ", '%Y-%m-%d')"
                print(sql)
                cursor.execute(sql)
                begin_date = cursor.fetchone()[0]

                sql = "select DATE_FORMAT(DATE_SUB(CURDATE(),INTERVAL %s Month)" % str(plag) + ", '%Y-%m-%d')"
                print(sql)
                cursor.execute(sql)
                end_date = cursor.fetchone()[0]

                ans = (branch_name, str(loan_ans), str(grant_ans), str(repay_ans), begin_date, end_date)

                self.ui.table.insertRow(currentRowCount)

                for j in range(columnNum):
                    tmp_item = QTableWidgetItem(str(ans[j]))
                    tmp_item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.table.setItem(currentRowCount, j, tmp_item)  # 列i+1
                currentRowCount += 1

        self.ui.table.setRowCount(currentRowCount)
        self.StatisticSearchSuccessDialog()

    def StatisticSearchSuccessDialog(self):
        self.ui.messagetextEdit.setText("统计成功")

    def StatisticSearchFailDialog(self, message):
        self.ui.messagetextEdit.setText("统计失败，错误类型为%s" % message)

    def StatisticSearchClose(self):
        self.StatisticSearchDialog.close()

    def StatisticSetSaving(self):
        self.ui.table.setColumnCount(5)  # 不设置不显示这些列
        self.ui.table.setHorizontalHeaderLabels(['支行名称', '储蓄总额', '总利息', '统计日期起点', '统计日期终点'])
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    def StatisticSetLoan(self):
        self.ui.table.setColumnCount(6)  # 不设置不显示这些列
        self.ui.table.setHorizontalHeaderLabels(['支行名称', '贷款总额', '发放总额', '偿还总额', '统计日期起点', '统计日期终点'])
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec_())
