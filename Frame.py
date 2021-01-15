from PySide6.QtWidgets import *
from enum import Enum
from Stylesheet import GuiColor


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
                           + str(color.value) + (" border-radius: 5px;" if border_radius else "") +
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
