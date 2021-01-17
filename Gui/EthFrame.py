from TextLabel import TextLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from Frame import *
from GuiButton import GuiButton


class EthFrame(Frame):
    def __init__(self):
        super().__init__()
        self.layout.setContentsMargins(0, 0, 0, 0)

        # memo
        self.memo = QLineEdit()
        self.memo.setStyleSheet(GuiColor.DARK_PRIMARY.value)
        self.add_widget(self.memo)

        # eth frame
        self.eth_frame = Frame(layout=LayoutDirection.HORIZONTAL)
        self.add_widget(self.eth_frame)
        self.eth_label = TextLabel("0.00 Eth", Qt.AlignCenter, 20)
        self.eth_frame.add_widget(self.eth_label)

        # up down arrows
        self.up_down_frame = Frame()
        self.up_down_frame.layout.setContentsMargins(0, 0, 0, 0)
        self.eth_frame.add_widget(self.up_down_frame)

        # up arrow
        self.up_arrow = GuiButton()
        self.up_down_frame.add_widget(self.up_arrow)
        self.up_arrow.setIcon(QIcon("Gui/icons/up_arrow.png"))

        # down arrow
        self.down_arrow = GuiButton()
        self.up_down_frame.add_widget(self.down_arrow)
        self.down_arrow.setIcon(QIcon("Gui/icons/down_arrow.png"))

