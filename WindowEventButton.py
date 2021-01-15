import sys
from PySide6.QtWidgets import *


class WindowEventButton(QPushButton):
    def __init__(self, color):
        super().__init__("")
        self.setStyleSheet("background-color: " + color + "; border-radius: 8px;")
        self.button_width = 16
        self.setMaximumWidth(self.button_width)
        self.setMaximumHeight(self.button_width)

