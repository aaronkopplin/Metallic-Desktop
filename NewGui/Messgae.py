from PySide6.QtWidgets import *
from NewGui.Stylesheet import *
from PySide6.QtCore import Qt
from NewGui.ImageRounder import mask_image


class Message(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # date label
        self.date_label = QLabel("Dec 12, 2021")
        self.date_label.setFixedHeight(20)
        self.date_label.setStyleSheet("color: grey; background-color: white")
        self.date_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.date_label)

        # body
        self.body = QFrame()
        self.body.setFixedHeight(75)
        self.layout.addWidget(self.body)
        self.body.setStyleSheet(s_primary_color)
        self.body_layout = QVBoxLayout()
        self.body.setContentsMargins(0, 0, 0, 0)
        self.body.setLayout(self.body_layout)

        # message content
        self.message_content = QFrame()
        self.body_layout.addWidget(self.message_content)
        self.message_content_layout = QHBoxLayout()
        self.message_content_layout.setContentsMargins(0, 0, 0, 0)
        self.message_content.setLayout(self.message_content_layout)

        # message and memo
        self.mesage_and_memo = QFrame()
        self.message_content_layout.addWidget(self.mesage_and_memo)
        self.mesage_and_memo_layout = QVBoxLayout()
        self.mesage_and_memo.setLayout(self.mesage_and_memo_layout)
        self.message = QLabel("You paid @vitalik 0.005 Eth")
        self.message.setStyleSheet("color: white;")
        self.message.setAlignment(Qt.AlignRight)
        self.mesage_and_memo_layout.addWidget(self.message)
        self.memo = QLabel("Thanks for inventing Ethereum")
        self.memo.setStyleSheet("color: grey;")
        self.memo.setAlignment(Qt.AlignRight)
        self.mesage_and_memo_layout.addWidget(self.memo)

        # picture
        self.picture = QLabel("")
        self.picture.setStyleSheet("border-radius: 25px; "
                                   "max-height: 50px; "
                                   "max-width: 50px;")
        self.pixmap = mask_image(open("icons/profilepic.png", "rb").read(), "png", 50)
        self.picture.setPixmap(self.pixmap)
        self.message_content_layout.addWidget(self.picture)

        # move the message contents to the right
        self.resize_message_frame = QFrame()
        self.layout.addWidget(self.resize_message_frame)
        self.resize_message_layout = QHBoxLayout()
        self.resize_message_layout.setContentsMargins(0, 0, 0, 0)
        self.resize_message_frame.setLayout(self.resize_message_layout)
        self.resize_message_layout.addSpacerItem(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.resize_message_layout.addWidget(self.body)


