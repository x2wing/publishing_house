import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from action import Exit_act, Book_act, Class_act, Clients_act, Provider_act, Shops_act, Worker_info_act
from action import Order_of_books_act, Production_act, Salary_act, Supply_act
from action import Order_to_worker_report, Client_and_class_report
from tabs import Tabs


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tabs = Tabs(self)
        self.setCentralWidget(self.tabs)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
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
        reportsMenu.addAction(Order_to_worker_report(self, self.tabs))
        reportsMenu.addAction(Client_and_class_report(self, self.tabs))
        # QueryMenu = menubar.addMenu('&Запросы')

        # self.showFullScreen()

        self.setWindowTitle('База данных "Книготорговая организация"')

        self.showMaximized()
        # self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
