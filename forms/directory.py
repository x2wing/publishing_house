import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtSql
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget
from sqlalchemy import Table

from db import BOOK, conf


class ComboBox(QtWidgets.QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        print(parent, repr(parent), type(parent))
        print('ComboBox', parent.get_cols())  # parent.sa_class.columns.keys()
        self.addItems(parent.get_cols())


class Directory(QWidget):
    def __init__(self, window_title, db_table, sa_class, parent=None, sort_column=0, hide_column=0, ):
        super().__init__(parent)
        self.hide_column = hide_column
        self.sa_class = sa_class

        self.setWindowTitle(window_title)
        # нужно сначала создать виджет чтобы подцепилась модель
        self.tv = QtWidgets.QTableView(self)

        self.con = self.connect()
        self.stm = self.create_model(db_table, sort_column)
        self.set_headers(self.stm)
        self.create_ui(hide_column)

    @property
    def name(self):
        return 'Вкладка'

    def set_headers(self, stm):
        pass

    def create_model(self, db_table, sort_column):
        stm = QtSql.QSqlTableModel(self)
        # stm = QtSql.QSqlRelationalTableModel()
        stm.setTable(db_table)
        stm.setSort(sort_column, QtCore.Qt.AscendingOrder)

        stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)

        stm.select()
        return stm

    def del_model(self):
        self.tv.setModel(QStandardItemModel(1, 1))

    def set_model(self):
        self.tv.setModel(self.stm)
        self.tv.hideColumn(self.hide_column)
        self.stm.select()

    def create_ui(self, hide_column):
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()

        self.column = ComboBox(self)
        self.condition = QtWidgets.QComboBox(self)
        self.condition.addItems(['>', '<', '=', ])
        self.value = QtWidgets.QLineEdit(self)

        btnFilter = QtWidgets.QPushButton('Фильтровать', self)
        btnFilter.clicked.connect(self.setFilter)

        # self.tv.setModel(self.stm)
        self.tv.hideColumn(hide_column)
        # self.tv.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        btnAdd = QtWidgets.QPushButton('&Добавить запись')
        btnAdd.clicked.connect(self.addRecord)
        btnDel = QtWidgets.QPushButton('&Удалить запись')
        btnDel.clicked.connect(self.delRecord)

        btnSave = QtWidgets.QPushButton('&Сохранить изменения')
        btnSave.clicked.connect(self.saveRecord)
        btnRemove = QtWidgets.QPushButton('&Удалить изменения')
        btnRemove.clicked.connect(self.setFilter)

        hbox.addWidget(self.column)
        hbox.addWidget(self.condition)
        hbox.addWidget(self.value)
        hbox.addWidget(btnFilter)
        vbox.addLayout(hbox)
        vbox.addWidget(self.tv)
        vbox.addWidget(btnAdd)
        vbox.addWidget(btnDel)
        vbox.addWidget(btnSave)
        vbox.addWidget(btnRemove)

        self.setLayout(vbox)
        self.resize(600, 500)
        # self.show()

    def setFilter(self):
        column = self.column.currentText()
        condition = self.condition.currentText()
        value = self.value.text()
        print(column, condition, value)
        self.stm.setFilter(f"{column}{condition}'{value}'")
        self.stm.select()

    def addRecord(self):
        self.stm.insertRow(self.stm.rowCount())

    def delRecord(self):
        self.stm.removeRow(self.tv.currentIndex().row())
        self.stm.submitAll()
        self.stm.select()

    def saveRecord(self):
        result = self.stm.submitAll()
        print(f'результат сохранения {result}')

    def connect(self):
        con = QtSql.QSqlDatabase.addDatabase(conf.qtdriver)
        print(QtSql.QSqlDatabase.drivers())
        con.setHostName(conf.hostname)
        con.setPort(int(conf.port))
        con.setDatabaseName(conf.database)
        con.setUserName(conf.user)
        con.setPassword(conf.password)
        if con.isOpen():
            con.close()
        if not con.open():
            raise Exception("Error opening database: {0}".format(con.lastError().text()))
        return con

    def get_cols(self):
        if issubclass(self.sa_class.__class__, Table):
            result = self.sa_class.columns.keys()
        else:
            result = self.sa_class.__table__.columns.keys()
        return result


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Directory("abstract_editor", 'book', BOOK)
    window.show()
    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
