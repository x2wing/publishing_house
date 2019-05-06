from PyQt5 import QtCore, QtWidgets, QtSql
import sys
from rel_forms.directory import RelDirectory

class Production(RelDirectory):
    def __init__(self, parent=None):
        super().__init__("PRODUCTION", 'production', parent=parent)

    @property
    def name(self):
        return 'Книги в заказе'

    def set_relation(self, stm):
        relation = [{'col':0, 'qt_rel': QtSql.QSqlRelation('book', 'book_identifier', 'name_of_book')},
                    {'col':1, 'qt_rel': QtSql.QSqlRelation('order_of_books', 'order_id', 'order_name')}]
        for item in relation:
            # 1 параметр столбец куда вешается делегат
            stm.setRelation(item['col'], item['qt_rel'])
            self.tv.setItemDelegateForColumn(item['col'], QtSql.QSqlRelationalDelegate(self.tv))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Production()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())