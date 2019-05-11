import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from db import PROVIDER
from forms.directory import Directory


class Provider(Directory):
    def __init__(self, parent=None):
        super().__init__("PROVIDER", 'provider', sa_class=PROVIDER, parent=parent)

    @property
    def name(self):
        return 'Поставщики'

    def set_headers(self, stm):
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название организации')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Адрес')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Номер телефона')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Provider()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
