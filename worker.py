import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
                             QApplication, QPushButton, QMessageBox)
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from db import DB_Worker, conn_params
from custom_widgets import TextBox

class Worker(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent, flags=QtCore.Qt.Dialog)

        self.initUI()

    def initUI(self):

        hbox = QVBoxLayout(self)

        
        self.WORKER_LAST_NAME = TextBox(self)
        self.WORKER_NAME = TextBox(self)
        self.WORKER_MIDDLE_NAME = TextBox(self)
        self.WORKER_PASSPORT_SERIES = TextBox(self)
        self.WORKER_PASSPORT_ID = TextBox(self)
        self.WORKER_POSITION_HELD = TextBox(self)
        self.WORKER_PLACE_OF_RESIDENT = TextBox(self)
        btn = QPushButton('Внести изменения')
        btn.clicked.connect(self.save_to_db)

        hbox.addWidget(self.WORKER_LAST_NAME)
        hbox.addWidget(self.WORKER_NAME)
        hbox.addWidget(self.WORKER_MIDDLE_NAME)
        hbox.addWidget(self.WORKER_PASSPORT_SERIES)
        hbox.addWidget(self.WORKER_PASSPORT_ID)
        hbox.addWidget(self.WORKER_POSITION_HELD)
        hbox.addWidget(self.WORKER_PLACE_OF_RESIDENT)
        hbox.addWidget(btn)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('worker_info')
        self.show()

    def save_to_db(self):

        data = dict(
            WORKER_LAST_NAME = self.WORKER_LAST_NAME.text(),
            WORKER_NAME = self.WORKER_NAME.text(),
            WORKER_MIDDLE_NAME = self.WORKER_MIDDLE_NAME.text(),
            WORKER_PASSPORT_SERIES = self.WORKER_PASSPORT_SERIES.text(),
            WORKER_PASSPORT_ID = self.WORKER_PASSPORT_ID.text(),
            WORKER_POSITION_HELD = self.WORKER_POSITION_HELD.text(),
            WORKER_PLACE_OF_RESIDENT = self.WORKER_PLACE_OF_RESIDENT.text())
        try:
            DB_Worker(conn_params).add_worker(data)
        except Exception as error:
            print(error)
        else:
            QMessageBox.information(self, 'Добавление записи', 'Запись успешно добалена в БД')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Worker()
    sys.exit(app.exec_())
