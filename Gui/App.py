from PySide6.QtWidgets import *
from Stylesheet import *
from HeaderFrame import HeaderFrame
from BodyFrame import BodyFrame
from Frame import Frame


class App(Frame):
    def __init__(self):
        super().__init__(content_margins=False)

        # main frame
        self.main_frame = Frame(color=GuiColor.DARK_PRIMARY, border_radius=False, content_margins=False)
        self.add_widget(self.main_frame)

        # body frame
        self.body_frame = BodyFrame()
        self.main_frame.add_widget(self.body_frame)
