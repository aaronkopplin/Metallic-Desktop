from PySide6.QtWidgets import *
from NewGui.Stylesheet import *
from NewGui.MessageFrame import MessageFrame
from NewGui.PaymentFrame import PaymentFrame
from PySide6.QtCore import Qt


class MessagesFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: none; border-radius: 5px;")

        # layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # username label
        self.username_label = QLabel("Vitalik Buterin")
        self.username_label.setFixedHeight(50)
        self.username_label.setStyleSheet(s_primary_color + " font-size: 25px; color: white; ")
        self.username_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.username_label)

        # message frame
        self.message_frame = MessageFrame()
        self.layout.addWidget(self.message_frame)

        # payment frame
        self.payment_frame = PaymentFrame()
        self.layout.addWidget(self.payment_frame)

