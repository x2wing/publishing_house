import sys
from PyQt5 import QtWidgets

from forms.directory import Directory

class Shops(Directory):
    def __init__(self, parent=None):
        super().__init__("SHOPS", 'shops', parent=parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Shops()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())