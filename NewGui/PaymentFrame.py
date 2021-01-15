from PySide6.QtWidgets import *
from NewGui.Stylesheet import *
from PySide6.QtGui import QIcon
from NewGui.EthFrame import EthFrame


class PaymentFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(s_primary_color)
        self.setFixedHeight(100)

        # layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # receive button
        self.request_button = QPushButton("")
        self.request_button.setStyleSheet("background-color: orange;")
        self.request_button.setIcon(QIcon('icons/download_icon.png'))
        self.layout.addWidget(self.request_button)

        # memo and eth dial
        self.eth_frame = EthFrame()
        self.layout.addWidget(self.eth_frame)

        # sent button
        self.send_button = QPushButton("")
        self.send_button.setIcon(QIcon("icons/paper_plane_icon.png"))
        self.layout.addWidget(self.send_button)
