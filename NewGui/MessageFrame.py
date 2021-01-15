from PySide6.QtWidgets import *
from NewGui.Stylesheet import GuiColor
from NewGui.Messgae import Message
from NewGui.Frame import *


class MessageFrame(Frame):
    def __init__(self):
        super().__init__(GuiColor.LIGHT_SECONDARY)

        # spacer
        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.add_item(self.spacer)

        # message
        self.message = Message()
        self.add_widget(self.message)
