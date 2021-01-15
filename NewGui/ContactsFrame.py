from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from NewGui.ContactFrame import ContactFrame
from NewGui.GuiButton import GuiButton
from NewGui.Frame import *


class ContactsFrame(Frame):
    def __init__(self):
        super().__init__(color=GuiColor.LIGHT_SECONDARY)
        self.setFixedWidth(300)

        # friends and world button
        self.button_frame = Frame(layout=LayoutDirection.HORIZONTAL, vertical_size_policy=QSizePolicy.Minimum)
        self.friends_button = GuiButton("")
        self.friends_button.setFixedWidth(50)
        self.friends_button.setIcon(QIcon("icons/contacts_icon.png"))
        self.button_frame.add_widget(self.friends_button)
        self.world_button = GuiButton("")
        self.world_button.setStyleSheet(GuiColor.LIGHT_SECONDARY.value + " border: 0px;")
        self.world_button.setFixedWidth(50)
        self.world_button.setIcon(QIcon("icons/globe_icon.png"))
        self.button_frame.add_widget(self.world_button)
        self.add_widget(self.button_frame)

        # search bar
        self.search_bar = QLineEdit()
        self.search_bar.setFixedHeight(20)
        self.search_bar.setStyleSheet(GuiColor.DARK_PRIMARY.value + " border-radius: 5px; " + GuiColor.TEXT.value + "QLineEdit[text=''] {color: red;}")
        self.add_widget(self.search_bar)

        # stack
        self.stack = QStackedWidget()
        self.add_widget(self.stack)

        # scroll area
        self.scroll_area = QScrollArea()
        self.stack.addWidget(self.scroll_area)
        self.scroll_area.setStyleSheet(GuiColor.DARK_PRIMARY.value + " border-radius: 5px;")

        self.scroll_frame = Frame()
        self.scroll_frame.add_widget(ContactFrame())
        self.scroll_frame.add_widget(ContactFrame())
        self.scroll_frame.add_widget(ContactFrame())
        self.scroll_frame.add_widget(ContactFrame())
        self.scroll_frame.add_widget(ContactFrame())
        self.scroll_frame.add_widget(ContactFrame())
        self.scroll_frame.add_widget(ContactFrame())
        self.scroll_frame.add_widget(ContactFrame())
        self.scroll_area.setWidget(self.scroll_frame)

        # add a vertical spacer
        self.scroll_frame.add_item(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))