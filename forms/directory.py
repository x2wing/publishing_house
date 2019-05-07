import sys

from PyQt5 import QtWidgets, QtSql
from PyQt5.QtWidgets import QWidget, QSizePolicy
from PyQt5 import  QtCore
from PyQt5.QtGui import  QStandardItemModel
from db import BOOK

class ComboBox(QtWidgets.QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        print('ComboBox',BOOK.__table__.columns.keys())

class Directory(QWidget):
    def __init__(self, window_title, db_table, parent=None, sort_column=0, hide_column=0,  ):
        super().__init__(parent)
        self.hide_column = hide_column
        self.setWindowTitle(window_title)
        # нужно сначала создать виджет чтобы подцепилась модель
        self.tv = QtWidgets.QTableView(self)

        self.con = self.connect()
        self.stm = self.create_model(db_table, sort_column)
        self.create_ui(hide_column)

    @property
    def name(self):
        return 'Вкладка'


    def create_model(self, db_table, sort_column):
        stm = QtSql.QSqlTableModel(self)
        # stm = QtSql.QSqlRelationalTableModel()
        stm.setTable(db_table)
        stm.setSort(sort_column, QtCore.Qt.AscendingOrder)

        stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        stm.select()
        return stm

    def del_model(self):
        self.tv.setModel(QStandardItemModel(1,1))

    def set_model(self):
        self.tv.setModel(self.stm)
        self.stm.select()

    def create_ui(self, hide_column):
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()

        column= ComboBox(self)
        condition= QtWidgets.QComboBox(self)
        value = QtWidgets.QLineEdit(self)


        # self.tv.setModel(self.stm)
        self.tv.hideColumn(hide_column)
        # self.tv.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        btnAdd = QtWidgets.QPushButton('&Добавить запись')
        btnAdd.clicked.connect(self.addRecord)
        btnDel = QtWidgets.QPushButton('&Удалить запись')
        btnDel.clicked.connect(self.setFilter)

        btnSave = QtWidgets.QPushButton('&Сохранить изменения')
        btnSave.clicked.connect(self.saveRecord)
        btnRemove = QtWidgets.QPushButton('&Удалить изменения')
        btnRemove.clicked.connect(self.removeRecords)

        hbox.addWidget(column)
        hbox.addWidget(condition)
        hbox.addWidget(value)
        vbox.addLayout(hbox)
        vbox.addWidget(self.tv)
        vbox.addWidget(btnAdd)
        vbox.addWidget(btnDel)
        vbox.addWidget(btnSave)
        vbox.addWidget(btnRemove)

        self.setLayout(vbox)
        self.resize(600, 500)
        # self.show()

    def setFilter(self, column, condition, value):
        self.stm.setFilter('worker_id=1')
        self.stm.select()

    def addRecord(self):
        self.stm.insertRow(self.stm.rowCount())

    def delRecord(self):
        self.stm.removeRow(self.tv.currentIndex().row())
        self.stm.select()

    def setFilter(self):
        self.stm.setFilter('worker_id=1')
        self.stm.select()

    def saveRecord(self):
        result = self.stm.submitAll()
        print(f'результат сохранения {result}')

    def removeRecords(self):
        self.stm.select()

    def connect(self):
        con = QtSql.QSqlDatabase.addDatabase("QPSQL")
        print(QtSql.QSqlDatabase.drivers())
        con.setHostName('localhost')
        con.setPort(5432)
        con.setDatabaseName('publishing_company')
        con.setUserName('postgres')
        con.setPassword('1')
        if con.isOpen():
            con.close()
        if not con.open():
            raise Exception("Error opening database: {0}".format(con.lastError().text()))
        return con




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Directory("abstract_editor", 'book')
    window.show()
    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
