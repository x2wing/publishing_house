import sys

from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtCore, QtWidgets, QtSql
from abc import ABC, abstractmethod

from forms.directory import Directory
from db import CLASS, BOOK, CLIENTS, SHOPS, PROVIDER, WORKER_INFO, SALARY, ORDER_OF_BOOKS, SUPPLY, db


class RelDirectory(Directory):

    def __init__(self, window_title, db_table, parent=None, sort_column=0, hide_column=-1,):
        super().__init__(window_title, db_table, parent, sort_column, hide_column)
        # self.fk_column = fk_column


    # def create_ui(self, hide_column):
    #     Directory.create_ui(self, hide_column)
    #     # self.tv.doubleClicked.connect(self.fill_cell)



    def create_model(self, db_table, sort_column):
        # stm = QtSql.QSqlTableModel()
        stm = QtSql.QSqlRelationalTableModel()
        stm.setTable(db_table)
        stm.setSort(sort_column, QtCore.Qt.AscendingOrder)

        stm.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        stm.setJoinMode(QtSql.QSqlRelationalTableModel.InnerJoin)
        self.set_relation(stm)

        stm.select()
        return stm

    # @abstractmethod
    def set_relation(self, stm):
        pass
        # relation = [{'col':1, 'qt_rel': QtSql.QSqlRelation('provider', 'provider_id', 'provider_organization')}]
        # for item in relation:
        #     # 1 параметр столбец куда вешается делегат
        #     stm.setRelation(item['col'], item['qt_rel'])
        #     self.tv.setItemDelegateForColumn(item['col'], QtSql.QSqlRelationalDelegate(self.tv))


    # def fill_cell(self, model_index):
    #     if model_index.column() == self.fk_column:
    #         provider = {item[0]:item[1] for item in db.session.query(PROVIDER.provider_organization, PROVIDER.provider_id)}
    #
    #         print(provider)
    #
    #         provider_organization, ok = QInputDialog.getItem(self, 'Title', 'Выберите элемент', provider,
    #                                                          editable=False)
    #         print('result', provider[provider_organization], 'ok=', ok)
    #         self.stm.setData(model_index, provider[provider_organization])
    #         # stm.select()
    #         print(model_index.column())
    #         # print(mi.data(), 'double click')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RelDirectory("abstract_editor", 'supply')

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
