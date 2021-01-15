from PySide6.QtWidgets import *
from NewGui.Stylesheet import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class EthFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: red;")
        self.setContentsMargins(0, 0, 0, 0)

        # layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # memo
        self.memo = QLineEdit()
        self.memo.setPlaceholderText("Memo")
        self.memo.setStyleSheet(s_secondary_color)
        self.layout.addWidget(self.memo)

        # eth frame
        self.eth_frame = QFrame()
        self.eth_frame.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.eth_frame)
        self.eth_frame_layout = QHBoxLayout()
        self.eth_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.eth_frame.setLayout(self.eth_frame_layout)
        self.eth_label = QLabel("0.00 Eth")
        self.eth_label.setStyleSheet("background-color: blue; color: white; font-size: 20px;")
        self.eth_label.setAlignment(Qt.AlignCenter)
        self.eth_frame_layout.addWidget(self.eth_label)

        # up down arrows
        self.up_down_frame = QFrame()
        self.up_down_frame.setContentsMargins(0, 0, 0, 0)
        self.up_down_frame.setStyleSheet("background-color: green;")
        self.eth_frame_layout.addWidget(self.up_down_frame)
        self.eth_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.up_down_frame_layout = QVBoxLayout()
        self.up_down_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.up_down_frame.setLayout(self.up_down_frame_layout)
        self.up_arrow = QPushButton()
        self.up_down_frame_layout.addWidget(self.up_arrow)
        self.up_arrow.setIcon(QIcon("icons/up_arrow.png"))
        self.down_arrow = QPushButton()
        self.up_down_frame_layout.addWidget(self.down_arrow)
        self.down_arrow.setIcon(QIcon("icons/down_arrow.png"))
