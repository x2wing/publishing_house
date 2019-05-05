import sys

from PyQt5 import QtWidgets, QtSql

from rel_forms.directory import RelDirectory


class Order_of_books(RelDirectory):
    def __init__(self, parent=None):
        super().__init__("ORDER_OF_BOOKS", 'order_of_books', parent=parent)

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Order_of_books()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
