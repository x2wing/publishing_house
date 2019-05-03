import sys
from abc import abstractmethod

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog,\
 QTreeWidgetItem, QTreeView, QAbstractItemView, \
    QTableWidgetItem, QAction, QMdiArea, QMdiSubWindow, QTextEdit, QMainWindow, QTabWidget, QPushButton

from forms.book import Book

class C_Action(QAction):
    def __init__(self, mdi:QMdiArea=None, name: str='Default', parent=None, ):
        super(C_Action, self).__init__(name, parent)
        self.mdi = mdi

    def set_params(self, shortcut: str, tittle=None, obj=None):
        self.title = tittle
        self.obj = obj
        self.setShortcut(shortcut)
        self.triggered.connect(self.act)


    def act(self):
        print(dir(self))
        sub = QMdiSubWindow()
        sub.setWidget(self.obj())
        sub.setWindowTitle(self.title)
        self.mdi.addSubWindow(sub)
        sub.show()
        print(dir(self))

class Book_action(C_Action):
    def __init__(self, mdi, parent):
        super().__init__(mdi, '&Book', parent)
        self.set_params(shortcut='Ctrl+B', tittle='Book', obj=Book)









class Open_action(C_Action):
    def __init__(self, parent):
        super(Open_action, self).__init__( name='&Open', parent=parent)
        self.set_params(shortcut='Ctrl+O')

    def act(self):
        import os
        description = 'Загрузить hdf5'  # заголовок окна диалога
        default_path = os.path.dirname(os.path.abspath(__file__))  # дефолтный путь диалогового окна
        filter = "Таблицы hdf5  (*.hdf5)"  # фильтр расширения
        # получаем путь к файлу
        path, _ = QFileDialog.getOpenFileName(None, description, default_path, filter)

class Exit_action(C_Action):
    def __init__(self, parent):
        super(Exit_action, self).__init__(name='&Exit', parent=parent)
        self.set_params(shortcut='Ctrl+Q')

    def act(self):
        qApp.quit()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(Open_action(self))
        fileMenu.addAction(Exit_action(self))

        directoryMenu = menubar.addMenu('&Directory')
        # directoryMenu.addAction(Book_action(self.mdi, self))

        reportsMenu = menubar.addMenu('&Reports')
        QueryMenu = menubar.addMenu('&Query')


        tab = QTabWidget(self)
        tab.setTabShape(QTabWidget.Rounded)
        tab.setTabsClosable(True)
        tab.addTab(QPushButton('Test'), 'Test')
        tab.addTab(QPushButton('Test'), 'Test1')
        tab.addTab(QPushButton('Test'), 'Test2')
        tab.addTab(QPushButton('Test'), 'Test3')
        # self.setGeometry(300, 300, 300, 200)
        self.showFullScreen()
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())