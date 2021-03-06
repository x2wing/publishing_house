import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtSql

from db import PRODUCTION
from rel_forms.directory import RelDirectory


class Production(RelDirectory):
    def __init__(self, parent=None):
        super().__init__("PRODUCTION", 'production', sa_class=PRODUCTION, parent=parent)

    @property
    def name(self):
        return 'Книги в заказе'

    def set_relation(self, stm):
        relation = [{'col': 0, 'qt_rel': QtSql.QSqlRelation('book', 'book_identifier', 'name_of_book')},
                    {'col': 1, 'qt_rel': QtSql.QSqlRelation('order_of_books', 'order_id', 'order_name')}]
        for item in relation:
            # 1 параметр столбец куда вешается делегат
            stm.setRelation(item['col'], item['qt_rel'])
            self.tv.setItemDelegateForColumn(item['col'], QtSql.QSqlRelationalDelegate(self.tv))

    def set_headers(self, stm):
        stm.setHeaderData(0, QtCore.Qt.Horizontal, 'Книга')
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Заказ')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Production()
    window.show()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
