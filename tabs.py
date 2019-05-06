import sys

from PyQt5.QtWidgets import QMainWindow, qApp, QApplication, QFileDialog, \
    QWidget, \
    QAction, QMdiArea, QMdiSubWindow, QTabWidget

class Tabs(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_widget =None
        self.setTabsClosable(True)
        self.setTabShape(QTabWidget.Rounded)
        self.tabCloseRequested.connect(self.tab_close)
        self.currentChanged.connect(self.tab_change)


    def tab_close(self, p):
        widget = self.widget(p)
        print(widget)
        del widget
        self.removeTab(p)
        self.current_widget = self.currentWidget()

    def tab_change(self, index):
        print('tab changed')
        print(self.currentIndex())
        print(self.currentWidget())
        if self.current_widget is not None:
            self.current_widget.del_model()
        # запоминаем текущий активный виджет
        self.current_widget = self.currentWidget()
        if self.current_widget is not None:
            self.current_widget.set_model()


    def add_tab(self, obj, title):
        print(self.currentIndex())
        print(self.currentWidget())
        cur_widget = self.currentWidget()
        if cur_widget is not None:
            cur_widget.del_model()
        self.addTab(obj, title)
        # переключение на новую вкладку
        self.setCurrentWidget(obj)
        self.current_widget = self.currentWidget()
        self.current_widget.set_model()
