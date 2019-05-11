import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtSql

from db import SALARY
from rel_forms.directory import RelDirectory


class Salary(RelDirectory):
    def __init__(self, parent=None):
        super().__init__("SALARY", 'salary', parent=parent, sa_class=SALARY, hide_column=0)

    @property
    def name(self):
        return 'Зарплата'

    def set_relation(self, stm):
        relation = [{'col': 1, 'qt_rel': QtSql.QSqlRelation('worker_info', 'worker_id', 'worker_last_name')}]
        for item in relation:
            # 1 параметр столбец куда вешается делегат
            stm.setRelation(item['col'], item['qt_rel'])
            self.tv.setItemDelegateForColumn(item['col'], QtSql.QSqlRelationalDelegate(self.tv))

    def set_headers(self, stm):
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Сотрудник')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Зарплата')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Премия')
        stm.setHeaderData(4, QtCore.Qt.Horizontal, 'Аванс')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Salary()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
