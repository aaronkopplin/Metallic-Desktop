from PySide6.QtWidgets import *
from NewGui.Stylesheet import *


class ProfileStackFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(s_primary_color + " border-radius: 5px;")
        self.setFixedWidth(300)
