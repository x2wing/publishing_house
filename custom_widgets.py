
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLineEdit,
                             QApplication, QPushButton)
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

class TextBox(QLineEdit):
    def __init__(self, parent=None, regexp="^\\S+$"):
        #"^\\S+$" - символы без пробела
        super().__init__(parent)
        validator = QRegExpValidator(QRegExp(regexp))
        self.setValidator(validator)
