from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from enum import Enum
from Stylesheet import GuiColor


class SpacerDirection(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class LayoutDirection(Enum):
    VERTICAL = QVBoxLayout()
    HORIZONTAL = QHBoxLayout()


class Frame(QFrame):
    def __init__(self, color=GuiColor.NONE,
                 layout=LayoutDirection.VERTICAL,
                 content_margins=True,
                 horizontal_size_policy=QSizePolicy.Expanding,
                 vertical_size_policy=QSizePolicy.Expanding,
                 border_radius=True):
        super().__init__()
        self.setStyleSheet(" QFrame {"
                           + str(color.value) + (" border-radius: " + ("5" if border_radius else "0") + "px; ") +
                           "}")
        self.setSizePolicy(horizontal_size_policy, vertical_size_policy)

        # avoid copies
        if layout == LayoutDirection.VERTICAL:
            self.layout = QVBoxLayout()
        else:
            self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        if not content_margins:
            self.layout.setContentsMargins(0, 0, 0, 0)

    def add_widget(self, widget: QWidget):
        self.layout.addWidget(widget)

    def add_item(self, widget: QSpacerItem):
        self.layout.addItem(widget)

    def add_spacer(self, spacer_direction: SpacerDirection):
        if spacer_direction.value == SpacerDirection.VERTICAL.value:
            self.add_item(QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Expanding))
        else:
            self.add_item(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))
