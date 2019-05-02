import sys
from PyQt5 import QtWidgets

from forms.directory import Directory

class Provider(Directory):
    def __init__(self, parent=None):
        super().__init__("PROVIDER", 'provider', parent=parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Provider()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())