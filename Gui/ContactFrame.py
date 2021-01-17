from TextLabel import TextLabel
from ImageRounder import mask_image
from Frame import *


class ContactFrame(Frame):
    def __init__(self):
        super().__init__(color=GuiColor.DARK_PRIMARY, layout=LayoutDirection.HORIZONTAL, content_margins=False)
        self.setStyleSheet(self.styleSheet() +
                           " QFrame:hover {"
                           + GuiColor.DARK_PRIMARY_HOVER.value +
                           "}")
        self.setFixedWidth(250)

        # account picture
        self.account_picture_label = QLabel("")
        self.account_picture_label.setStyleSheet("border-radius: 25px; "
                                                 "max-width: 50px; "
                                                 "max-height: 50px; ")
        self.pixmap = mask_image(open("Gui/icons/vitalik.png", "rb").read(), "png", 50)
        self.account_picture_label.setPixmap(self.pixmap)
        self.add_widget(self.account_picture_label)

        # user info layout
        self.user_info_frame = Frame()
        self.add_widget(self.user_info_frame)

        # name label
        self.name_label = TextLabel("Vitalik Buterin")
        self.user_info_frame.add_widget(self.name_label)

        # username label
        self.username_label = TextLabel("@vitalik")
        self.user_info_frame.add_widget(self.username_label)

        # # score label
        # self.score_label = TextLabel("Score: 76")
        # self.user_info_frame.add_widget(self.score_label)
