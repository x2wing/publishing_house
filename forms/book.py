import sys
from PyQt5 import QtWidgets

from forms.directory import Directory

class Book(Directory):
    def __init__(self, parent=None):
        super().__init__("BOOK", 'book', parent=parent)

    @property
    def name(self):
        return 'Книги'


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Book()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
