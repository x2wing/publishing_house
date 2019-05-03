import sys

from PyQt5 import QtCore, QtWidgets, QtSql
from forms.directory import Directory



class RelDirectory(Directory):
    def create_ui(self, hide_column):
        Directory.create_ui(self, hide_column)
        self.tv.doubleClicked.connect(self.fill_cell)

    def fill_cell(self, mi):
        
        self.stm.setData(mi, '1')
        # stm.select()
        print(mi.column())
        print(mi.data(), 'double click')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RelDirectory("abstract_editor", 'supply', hide_column=-1)

    # print(QtSql.QSqlDatabase.drivers())
    sys.exit(app.exec())
