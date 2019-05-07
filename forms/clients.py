import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from forms.directory import Directory


class Clients(Directory):
    def __init__(self, parent=None):
        super().__init__("CLIENTS", 'clients', parent=parent)

    @property
    def name(self):
        return 'Клиенты'

    def set_headers(self, stm):
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Имя')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Фамилия')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Отчество')
        stm.setHeaderData(4, QtCore.Qt.Horizontal, 'Номер телефона')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Clients()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
