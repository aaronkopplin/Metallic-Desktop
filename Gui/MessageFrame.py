from Messgae import Message
from Frame import *


class MessageFrame(Frame):
    def __init__(self):
        super().__init__(GuiColor.LIGHT_SECONDARY)

        # spacer
        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.add_item(self.spacer)

        # message
        self.message = Message()
        self.add_widget(self.message)
