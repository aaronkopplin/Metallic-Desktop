from PySide6.QtWidgets import *
from Stylesheet import GuiColor
from PySide6.QtGui import QIcon
from EthFrame import EthFrame
from GuiButton import GuiButton



class PaymentFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(GuiColor.LIGHT_SECONDARY.value)
        self.setFixedHeight(100)

        # layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # horizontal spacer
        self.layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))

        # receive button
        self.request_button = GuiButton("")
        self.request_button.setIcon(QIcon('icons/download_icon.png'))
        self.layout.addWidget(self.request_button)

        # horizontal spacer
        self.layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))

        # memo and eth dial
        self.eth_frame = EthFrame()
        self.layout.addWidget(self.eth_frame)

        # horizontal spacer
        self.layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))

        # sent button
        self.send_button = GuiButton("")
        self.send_button.setIcon(QIcon("icons/paper_plane_icon.png"))
        self.layout.addWidget(self.send_button)

        # horizontal spacer
        self.layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))
