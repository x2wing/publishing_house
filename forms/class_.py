import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from db import CLASS
from forms.directory import Directory


class Class(Directory):
    def __init__(self, parent=None):
        super().__init__("CLASS", 'class', sa_class=CLASS, parent=parent)

    @property
    def name(self):
        return 'Класс обслуживания'

    def set_headers(self, stm):
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Класс обслуживания')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Class()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
