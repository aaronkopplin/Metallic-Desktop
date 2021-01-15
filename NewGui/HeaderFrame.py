from PySide6.QtCore import Qt
from NewGui.Frame import *
from NewGui.TextLabel import TextLabel


class HeaderFrame(Frame):
    def __init__(self, width, height):
        super().__init__(color=GuiColor.LIGHT_SECONDARY, layout=LayoutDirection.HORIZONTAL)
        self.button_width = 16
        self.setFixedHeight(height)

        # label
        self.label = TextLabel(text="Metallic", font_size=20, bold=True, alignment=Qt.AlignVCenter)
        self.add_widget(self.label)

