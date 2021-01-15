from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
from Stylesheet import GuiColor
from Profile import Profile


class ProfileStackFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(GuiColor.LIGHT_SECONDARY.value + " border-radius: 5px;")
        self.setFixedWidth(300)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # button group
        self.button_group_frame = QFrame()
        self.layout.addWidget(self.button_group_frame)
        self.button_group_layout = QHBoxLayout()
        self.button_group_frame.setLayout(self.button_group_layout)

        # my profile button
        self.my_profile_button = QPushButton("")
        self.button_group_layout.addWidget(self.my_profile_button)
        self.my_profile_button.setIcon(QIcon("icons/single_profile_icon.png"))
        self.my_profile_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        # other profile button
        self.other_profile_button = QPushButton("")
        self.button_group_layout.addWidget(self.other_profile_button)
        self.other_profile_button.setIcon(QIcon("icons/friends_icon.png"))
        self.other_profile_button.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        # stack
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # profile widget
        self.my_profile = Profile("icons/profilepic.png", "Aaron Kopplin", "@aaronkopplin", "0.0765", "143", "1 year 6 mos")
        self.stack.addWidget(self.my_profile)

        # other profile
        self.other_profile = Profile("icons/vitalik.png", "Test", "Test", "Test", "Test", "Test")
        self.stack.addWidget(self.other_profile)
