import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from forms.directory import Directory


class Worker_info(Directory):
    def __init__(self, parent=None):
        super().__init__("WORKER_INFO", 'worker_info', parent)

    @property
    def name(self):
        return 'Информация о сотруднике'

    def set_headers(self, stm):
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Фамилия')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Имя')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Отчество')
        stm.setHeaderData(4, QtCore.Qt.Horizontal, 'Серия паспорта')
        stm.setHeaderData(5, QtCore.Qt.Horizontal, 'Номер паспорта')
        stm.setHeaderData(6, QtCore.Qt.Horizontal, 'Должность')
        stm.setHeaderData(7, QtCore.Qt.Horizontal, 'Прописка')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Worker_info()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
