import sys

from PyQt5.QtWidgets import QMainWindow, qApp, QApplication, QFileDialog, \
    QWidget, \
    QAction, QMdiArea, QMdiSubWindow, QTabWidget


from forms import Book, Class, Clients, Provider, Shops, Worker_info
from action import  Exit_act, Book_act, Class_act, Clients_act, Provider_act, Shops_act, Worker_info_act
from action import  Order_of_books_act, Production_act, Salary_act, Supply_act
from trash.custom_widget import Directory
from tabs import Tabs


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # self.mdi = QMdiArea()
        # self.setCentralWidget(self.mdi)
        # self.statusBar()
        self.tabs = Tabs(self)
        self.setCentralWidget(self.tabs)

        # self.tabs.setGeometry(0,0,600,300)

        # d1 = Directory('tst1', 'clients')
        # d2 = Directory('tst1', 'salary')
        # d3 = Directory('tst1', 'class')
        # d4 = Directory('tst1', 'supply')
        # self.add_tab(d1,'tab')
        # self.add_tab(d2,'tab')
        # self.add_tab(d3,'tab')
        # self.add_tab(d4,'tab')

        # book = Book()
        # self.tabs.addTab(book, book.name)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        # fileMenu.addAction(Open_action(self))
        fileMenu.addAction(Exit_act(self))

        directoryMenu = menubar.addMenu('&Справочники')
        directoryMenu.addAction(Book_act(self, self.tabs))
        directoryMenu.addAction(Class_act(self, self.tabs))
        directoryMenu.addAction(Clients_act(self, self.tabs))
        directoryMenu.addAction(Provider_act(self, self.tabs))
        directoryMenu.addAction(Shops_act(self, self.tabs))
        directoryMenu.addAction(Worker_info_act(self, self.tabs))

        relationMenu = menubar.addMenu('&Журналы')
        relationMenu.addAction(Order_of_books_act(self, self.tabs))
        relationMenu.addAction(Production_act(self, self.tabs))
        relationMenu.addAction(Salary_act(self, self.tabs))
        relationMenu.addAction(Supply_act(self, self.tabs))

        reportsMenu = menubar.addMenu('&Отчеты')
        QueryMenu = menubar.addMenu('&Запросы')

        # self.setGeometry(300, 300, 300, 200)
        # self.showFullScreen()

        self.setWindowTitle('База данных книготорговой организация')


        self.showMaximized()
        # self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
