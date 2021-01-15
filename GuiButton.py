from PySide6.QtWidgets import *
from Stylesheet import GuiColor


class GuiButton(QPushButton):
    def __init__(self, text=""):
        super().__init__(text)
        self.setStyleSheet(GuiColor.LIGHT_SECONDARY.value + " border: 0px; ")
