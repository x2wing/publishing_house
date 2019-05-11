import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtSql

from rel_forms.directory import RelDirectory
from db import ORDER_OF_BOOKS

class Order_of_books(RelDirectory):
    def __init__(self, parent=None):
        super().__init__("ORDER_OF_BOOKS", 'order_of_books', sa_class=ORDER_OF_BOOKS, parent=parent, hide_column=0)

    @property
    def name(self):
        return 'Заказы'

    def set_relation(self, stm):
        relation = [{'col': 2, 'qt_rel': QtSql.QSqlRelation('provider', 'provider_id', 'provider_organization')},
                    {'col': 3, 'qt_rel': QtSql.QSqlRelation('shops', 'shop_id', 'shop_name')},
                    {'col': 4, 'qt_rel': QtSql.QSqlRelation('clients', 'client_id', 'client_last_name')},
                    {'col': 8, 'qt_rel': QtSql.QSqlRelation('worker_info', 'worker_id', 'worker_last_name')},
                    {'col': 10, 'qt_rel': QtSql.QSqlRelation('class', 'class_id', 'class_name')}]
        for item in relation:
            # 1 параметр столбец куда вешается делегат
            stm.setRelation(item['col'], item['qt_rel'])
            self.tv.setItemDelegateForColumn(item['col'], QtSql.QSqlRelationalDelegate(self.tv))

    def set_headers(self, stm):
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название заказа')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Поставщик')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Магазин')
        stm.setHeaderData(4, QtCore.Qt.Horizontal, 'Клиент')
        stm.setHeaderData(5, QtCore.Qt.Horizontal, 'Дата заказа')
        stm.setHeaderData(6, QtCore.Qt.Horizontal, 'Сумма предоплаты')
        stm.setHeaderData(7, QtCore.Qt.Horizontal, 'Дата завершения заказа')
        stm.setHeaderData(8, QtCore.Qt.Horizontal, 'Сотрудник, создавший заказ')
        stm.setHeaderData(9, QtCore.Qt.Horizontal, 'Активный')
        stm.setHeaderData(10, QtCore.Qt.Horizontal, 'Класс обслуживаия')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Order_of_books()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
