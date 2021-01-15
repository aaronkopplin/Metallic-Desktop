from PySide6.QtWidgets import *
from NewGui.WindowEventButton import WindowEventButton


class HeaderFrame(QFrame):
    def __init__(self, width, height):
        super().__init__()
        self.button_width = 16
        self.setFixedHeight(height)

        # layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # label
        self.label = QLabel("Metallic")
        self.label.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        self.layout.addWidget(self.label)

        # minimize button
        self.minimize_button = WindowEventButton("yellow")
        self.layout.addWidget(self.minimize_button)

        # maximize button
        self.maximize_button = WindowEventButton("rgb(0, 255, 0)")
        self.layout.addWidget(self.maximize_button)

        # close button
        self.close_button = WindowEventButton("red")
        self.layout.addWidget(self.close_button)
