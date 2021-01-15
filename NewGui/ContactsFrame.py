from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from NewGui.ContactFrame import ContactFrame
from NewGui.Stylesheet import *


class ContactsFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(s_primary_color + " border-radius: 5px;")
        self.setFixedWidth(300)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # friends and world button
        self.button_frame = QFrame()
        self.button_frame.setStyleSheet("border-radius: 5px;")
        self.friends_group = QHBoxLayout()
        self.friends_button = QPushButton("")
        self.friends_button.setFixedWidth(50)
        self.friends_button.setIcon(QIcon("icons/contacts_icon.png"))
        self.friends_group.addWidget(self.friends_button)
        self.world_button = QPushButton("")
        self.world_button.setFixedWidth(50)
        self.world_button.setIcon(QIcon("icons/globe_icon.png"))
        self.friends_group.addWidget(self.world_button)
        self.button_frame.setLayout(self.friends_group)
        self.layout.addWidget(self.button_frame)

        # search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search")
        self.search_bar.setFixedHeight(20)
        self.search_bar.setStyleSheet(s_secondary_color + " border-radius: 5px;")
        self.layout.addWidget(self.search_bar)

        # stack
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet(s_secondary_color + " border-radius: 5px;")
        self.scroll_area_frame = QFrame()
        self.scroll_layout = QVBoxLayout()
        self.scroll_area.setLayout(self.scroll_layout)
        self.stack.addWidget(self.scroll_area)

        # add a contact
        self.contact = ContactFrame()
        self.scroll_layout.addWidget(self.contact)

        # add a vertical spacer
        self.scroll_layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))