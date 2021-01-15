from PySide6.QtWidgets import *
from NewGui.Stylesheet import *
from NewGui.ImageRounder import mask_image


class ContactFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(s_primary_color)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(100)

        # layout
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # account picture
        self.account_picture_label = QLabel("")
        self.account_picture_label.setStyleSheet("border-radius: 25px; "
                                                 "max-width: 50px; "
                                                 "max-height: 50px; "
                                                 "background-color: red;")
        self.pixmap = mask_image(open("icons/vitalik.png", "rb").read(), "png", 50)
        self.account_picture_label.setPixmap(self.pixmap)
        self.layout.addWidget(self.account_picture_label)

        # user info layout
        self.user_info_frame = QFrame()
        self.user_info_layout = QVBoxLayout()
        self.user_info_layout.setContentsMargins(0, 0, 0, 0)
        self.user_info_frame.setLayout(self.user_info_layout)
        self.layout.addWidget(self.user_info_frame)

        # name label
        self.name_label = QLabel("Vitalik Buterin")
        self.user_info_layout.addWidget(self.name_label)

        # username label
        self.username_label = QLabel("@vitalik")
        self.user_info_layout.addWidget(self.username_label)

        # score label
        self.score_label = QLabel("Score: 76")
        self.user_info_layout.addWidget(self.score_label)

        # account age label
        self.account_age_label = QLabel("Account Age: 1 year 2 mos.")
        self.user_info_layout.addWidget(self.account_age_label)

