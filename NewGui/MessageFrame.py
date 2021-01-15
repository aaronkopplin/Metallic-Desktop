from PySide6.QtWidgets import *
from NewGui.Stylesheet import *
from NewGui.Messgae import Message


class MessageFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")

        # layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addSpacerItem(self.spacer)

        # message
        self.message = Message()
        self.layout.addWidget(self.message)