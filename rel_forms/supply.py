
from PyQt5 import QtCore, QtWidgets, QtSql
import sys
from rel_forms.directory import RelDirectory


class Supply(RelDirectory):
    def __init__(self, parent=None):
        super().__init__("SUPPLY", 'supply', parent=parent, hide_column=0)

    def set_relation(self, stm):
        relation = [{'col':1, 'qt_rel': QtSql.QSqlRelation('provider', 'provider_id', 'provider_organization')}]
        for item in relation:
            # 1 параметр столбец куда вешается делегат
            stm.setRelation(item['col'], item['qt_rel'])
            self.tv.setItemDelegateForColumn(item['col'], QtSql.QSqlRelationalDelegate(self.tv))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Supply()

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())