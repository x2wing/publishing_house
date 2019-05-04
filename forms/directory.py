import sys

from PyQt5 import QtWidgets, QtSql
from PyQt5.QtWidgets import QWidget
from PyQt5 import  QtCore

class Directory(QWidget):
    def __init__(self, window_title, db_table, hide_column=0, parent=None):
        super().__init__(parent)
        self.setWindowTitle(window_title)
        con = self.connect()
        self.stm = self.create_model(db_table)
        self.create_ui(hide_column)


    def create_model(self, db_table):
        stm = QtSql.QSqlTableModel(parent=self)
        stm.setTable(db_table)
        stm.setSort(1, QtCore.Qt.AscendingOrder)

        stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        stm.select()
        return stm

    def create_ui(self, hide_column):
        vbox = QtWidgets.QVBoxLayout()
        self.tv = QtWidgets.QTableView()
        self.tv.setModel(self.stm)
        self.tv.hideColumn(hide_column)

        btnAdd = QtWidgets.QPushButton('&Добавить запись')
        btnAdd.clicked.connect(self.addRecord)
        btnDel = QtWidgets.QPushButton('&Удалить запись')
        btnDel.clicked.connect(self.setFilter)

        btnSave = QtWidgets.QPushButton('&Сохранить изменения')
        btnSave.clicked.connect(self.saveRecord)
        btnRemove = QtWidgets.QPushButton('&Удалить изменения')
        btnRemove.clicked.connect(self.removeRecords)

        vbox.addWidget(self.tv)
        vbox.addWidget(btnAdd)
        vbox.addWidget(btnDel)
        vbox.addWidget(btnSave)
        vbox.addWidget(btnRemove)

        self.setLayout(vbox)
        self.resize(600, 500)
        self.show()

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

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
