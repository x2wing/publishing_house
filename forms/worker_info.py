import sys
from PyQt5 import QtWidgets

from forms.directory import Directory

class Worker_info(Directory):
    def __init__(self, parent=None):
        super().__init__("WORKER_INFO", 'worker_info', parent)

    @property
    def name(self):
        return 'Информация о сотруднике'


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Worker_info()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
