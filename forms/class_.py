import sys
from PyQt5 import QtWidgets

from forms.directory import Directory

class Class(Directory):
    def __init__(self, parent=None):
        super().__init__("CLASS", 'class', parent=parent)

    @property
    def name(self):
        return 'Класс обслуживания'


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Class()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())