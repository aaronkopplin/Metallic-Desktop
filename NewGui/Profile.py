from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
from NewGui.Stylesheet import *
from NewGui.TextLabel import TextLabel
from NewGui.ImageRounder import mask_image
from NewGui.Frame import *


class Profile(Frame):
    def __init__(self, image, name, username, balance, score, age):
        super().__init__(color=GuiColor.DARK_PRIMARY)

        # profile picture
        self.profile_picture_label = QLabel()
        self.add_widget(self.profile_picture_label)
        self.pixmap = mask_image(open(image, "rb").read(), "png", 100)
        self.profile_picture_label.setPixmap(self.pixmap)
        self.profile_picture_label.setAlignment(Qt.AlignCenter)

        # name label
        self.name_label = TextLabel(name, Qt.AlignHCenter, 20)
        self.add_widget(self.name_label)

        # username label
        self.username_label = TextLabel(username, Qt.AlignHCenter)
        self.add_widget(self.username_label)

        # balance label
        self.balance_label = TextLabel("Balance: " + str(balance) + " Eth", Qt.AlignHCenter)
        self.add_widget(self.balance_label)

        # score label
        self.score_label = TextLabel("Score: " + str(score), Qt.AlignHCenter)
        self.add_widget(self.score_label)

        # account age label
        self.account_age_label = TextLabel("Account age: " + str(age), Qt.AlignHCenter)
        self.add_widget(self.account_age_label)

        # vertical spacer
        self.add_item(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Expanding))
