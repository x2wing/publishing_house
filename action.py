from PyQt5.QtWidgets import QMainWindow, qApp, QApplication, QFileDialog, \
    QWidget, \
    QAction, QMdiArea, QMdiSubWindow, QTabWidget


from forms import Book, Class, Clients, Provider, Shops, Worker_info
from rel_forms import Order_of_books, Production, Salary, Supply
from db import Order_to_worker, Client_and_class

class C_Action(QAction):
    def __init__(self, mdi: QMdiArea = None, name: str = 'Default', parent=None, ):
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



class Action(QAction):
    def __init__(self, name:str, parent, tabs):
        super(Action, self).__init__(name, parent)
        self.tabs = tabs

    def set_params(self, shortcut: str,  cls=None):
        self.setShortcut(shortcut)

        self.cls = cls
        self.triggered.connect(self.act)

    def act(self):
        # print(dir(self))
        obj = self.cls()
        self.tabs.add_tab(obj, obj.name)

        # print(dir(self))

class Book_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Книги', parent, tabs)
        self.set_params(shortcut='Ctrl+B', cls=Book)

class Class_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Класс обслуживания', parent, tabs)
        self.set_params(shortcut='Ctrl+K', cls=Class)

class Clients_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Клиенты', parent, tabs)
        self.set_params(shortcut='Ctrl+L', cls=Clients)

class Provider_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Поставщики', parent, tabs)
        self.set_params(shortcut='Ctrl+P', cls=Provider)

class Shops_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Магазины', parent, tabs)
        self.set_params(shortcut='Ctrl+S', cls=Shops)

class Worker_info_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Информация о сотрудниках', parent, tabs)
        self.set_params(shortcut='Ctrl+W', cls=Worker_info)


class Order_of_books_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Заказы', parent, tabs)
        self.set_params(shortcut='Ctrl+O', cls=Order_of_books)


class Production_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Книги в заказе', parent, tabs)
        self.set_params(shortcut='Ctrl+R', cls=Production)

class Salary_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Зарплата', parent, tabs)
        self.set_params(shortcut='Ctrl+R', cls=Salary)


class Supply_act(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Поставки', parent, tabs)
        self.set_params(shortcut='Ctrl+U', cls=Supply)


class Order_to_worker_report(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Отчет Заказы по менеджерам', parent, tabs)
        self.set_params(shortcut='Ctrl+Z', cls=Order_to_worker)

    def act(self):
        self.cls()

class Client_and_class_report(Action):
    def __init__(self, parent, tabs):
        super().__init__('&Отчет Классы обслуживания клиентов', parent, tabs)
        self.set_params(shortcut='Ctrl+E', cls=Client_and_class)

    def act(self):
        self.cls()


# class Open_action(C_Action):
#     def __init__(self, parent):
#         super(Open_action, self).__init__(name='&Open', parent=parent)
#         self.set_params(shortcut='Ctrl+O')
#
#     def act(self):
#         import os
#         description = 'Загрузить hdf5'  # заголовок окна диалога
#         default_path = os.path.dirname(os.path.abspath(__file__))  # дефолтный путь диалогового окна
#         filter = "Таблицы hdf5  (*.hdf5)"  # фильтр расширения
#         # получаем путь к файлу
#         path, _ = QFileDialog.getOpenFileName(None, description, default_path, filter)


class Exit_act(C_Action):
    def __init__(self, parent):
        super(Exit_act, self).__init__(name='&Exit', parent=parent)
        self.set_params(shortcut='Ctrl+Q')

    def act(self):
        qApp.quit()