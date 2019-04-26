import sys
from PyQt5 import QtWidgets

from directory import Directory

class Book(Directory):
    def __init__(self):
        super().__init__("BOOK", 'book')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Directory("abstract_editor", 'book')

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
