import sys

from PyQt5 import QtCore, QtWidgets, QtSql


def addRecord():
    stm.insertRow(stm.rowCount())


def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select()


def setFilter():
    stm.setFilter('worker_id=1')
    stm.select()

def dt_change():
    stm.submit()
    stm.submitAll()
    print('data changed')

def saveRecord():
    result = stm.submitAll()
    print(f'результат сохранения {result}')

def foo(mi):
    stm.setData(mi,'1')
    # stm.select()
    print(mi.column())
    print(mi.data(), 'double click')

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Qsqltablemodel")
# print(QtSql.QSqlDatabase.drivers())

con = QtSql.QSqlDatabase.addDatabase("QPSQL")
con.setHostName('localhost')
con.setPort(5432)
con.setDatabaseName('publishing_company')
con.setUserName('postgres')
con.setPassword('1')
if con.isOpen():
    con.close()
if not con.open():
    raise Exception("Error opening database: {0}".format(con.lastError().text()))

stm = QtSql.QSqlRelationalTableModel(parent=window)
stm.setJoinMode(QtSql.QSqlRelationalTableModel.InnerJoin)
stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
stm.setTable('supply')
stm.setSort(1, QtCore.Qt.AscendingOrder)
stm.dataChanged.connect(dt_change)


# stm.setRelation(0, QtSql.QSqlRelation('provider', 'provider_id', 'provider_organization'))

stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
stm.select()

vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.doubleClicked.connect(foo)
tv.setModel(stm)
# tv.setItemDelegateForColumn(0, QtSql.QSqlRelationalDelegate(tv))

btnAdd = QtWidgets.QPushButton('&Добавить запись')
btnAdd.clicked.connect(addRecord)
btnDel = QtWidgets.QPushButton('&Удалить запись')
btnDel.clicked.connect(setFilter)
btnSave = QtWidgets.QPushButton('&Сохранить запись')
btnSave.clicked.connect(saveRecord)

vbox.addWidget(tv)
vbox.addWidget(btnAdd)
vbox.addWidget(btnDel)
vbox.addWidget(btnSave)

window.setLayout(vbox)
window.resize(300, 250)
window.show()
sys.exit(app.exec())

# query = QtSql.QSqlQuery()
# query.exec_(request)
