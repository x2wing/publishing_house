import sys
from PyQt5 import QtWidgets

from forms.directory import Directory

class Clients(Directory):
    def __init__(self, parent=None):
        super().__init__("CLIENTS", 'clients', parent=parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Clients()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())