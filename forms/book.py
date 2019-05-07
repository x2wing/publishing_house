import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from forms.directory import Directory
from db import BOOK


class Book(Directory):
    def __init__(self, parent=None):
        super().__init__("BOOK", 'book', sa_class=BOOK, parent=parent, )

    @property
    def name(self):
        return 'Книги'

    def set_headers(self, stm):
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название книги')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Автор книги')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Число страниц')
        stm.setHeaderData(4, QtCore.Qt.Horizontal, 'Количество заказаных копий')
        stm.setHeaderData(5, QtCore.Qt.Horizontal, 'Цена книги')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Book()
    window.set_model()
    window.show()
    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
