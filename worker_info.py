import sys
from PyQt5 import QtWidgets

from directory import Directory

class Worker_info(Directory):
    def __init__(self):
        super().__init__("WORKER_INFO", 'worker_info')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Worker_info()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
