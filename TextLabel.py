from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from Stylesheet import GuiColor


class TextLabel(QLabel):
    def __init__(self, text: str, alignment=Qt.AlignLeft, font_size=15, bold=False):
        super().__init__()
        self.setText(text)
        self.setStyleSheet(GuiColor.TEXT.value + " border-radius: 5px; font-size: " + str(font_size) + "px; "
                           + (" font-weight: bold; " if bold else ""))
        self.setAlignment(alignment)

