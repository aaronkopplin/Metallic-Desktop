from PySide6.QtWidgets import *
from NewGui.Stylesheet import GuiColor
from NewGui.MessageFrame import MessageFrame
from NewGui.PaymentFrame import PaymentFrame
from PySide6.QtCore import Qt
from NewGui.Frame import *


class MessagesFrame(Frame):
    def __init__(self):
        super().__init__(content_margins=False)

        # username label
        self.username_label = QLabel("Vitalik Buterin")
        self.username_label.setFixedHeight(50)
        self.username_label.setStyleSheet(GuiColor.LIGHT_SECONDARY.value + " font-size: 20px; " + GuiColor.TEXT.value)
        self.username_label.setAlignment(Qt.AlignCenter)
        self.add_widget(self.username_label)

        # message frame
        self.message_frame = MessageFrame()
        self.add_widget(self.message_frame)

        # payment frame
        self.payment_frame = PaymentFrame()
        self.add_widget(self.payment_frame)

