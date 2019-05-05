import sys

from PyQt5 import QtWidgets

from forms.directory import Directory


class Order_of_books(Directory):
    def __init__(self, parent=None):
        super().__init__("ORDER_OF_BOOKS", 'order_of_books', parent=parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Order_of_books()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
