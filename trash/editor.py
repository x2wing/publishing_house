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


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Qsqltablemodel")
print(QtSql.QSqlDatabase.drivers())

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


stm = QtSql.QSqlTableModel(parent=window)
stm.setTable('supply')
stm.setSort(1,QtCore.Qt.AscendingOrder)

stm.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
stm.select()

vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)

btnAdd = QtWidgets.QPushButton('&Добавить запись')
btnAdd.clicked.connect(addRecord)
btnDel = QtWidgets.QPushButton('&Удалить запись')
btnDel.clicked.connect(setFilter)

vbox.addWidget(tv)
vbox.addWidget(btnAdd)
vbox.addWidget(btnDel)

window.setLayout(vbox)
window.resize(300,250)
window.show()
sys.exit(app.exec())




# query = QtSql.QSqlQuery()
# query.exec_(request)