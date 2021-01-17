from TextLabel import TextLabel
from PySide6.QtCore import Qt
from ImageRounder import mask_image
from Frame import *


class Message(Frame):
    def __init__(self):
        super().__init__(color=GuiColor.NONE, content_margins=False)
        self.setFixedHeight(100)

        # date label
        self.date_label = TextLabel("Dec 12, 2021", Qt.AlignHCenter)
        self.date_label.setFixedHeight(20)
        self.add_widget(self.date_label)

        # message content
        self.message_content = Frame(color=GuiColor.DARK_PRIMARY, layout=LayoutDirection.HORIZONTAL)
        self.add_widget(self.message_content)

        # move the message contents to the right
        self.resize_message_frame = Frame(layout=LayoutDirection.HORIZONTAL)
        self.resize_message_frame.setFixedHeight(75)
        self.resize_message_frame.layout.setContentsMargins(0, 0, 0, 0)
        self.add_widget(self.resize_message_frame)
        self.resize_message_frame.add_item(QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.resize_message_frame.add_widget(self.message_content)

        # message and memo frame
        self.message_and_memo = Frame()
        self.message_content.add_widget(self.message_and_memo)

        # message
        self.message = TextLabel("You paid @vitalik 0.005 Eth", Qt.AlignRight)
        self.message_and_memo.add_widget(self.message)

        # memo
        self.memo = TextLabel("Thanks for inventing Ethereum", Qt.AlignRight)
        self.message_and_memo.add_widget(self.memo)

        # picture
        self.picture = TextLabel("")
        self.picture.setStyleSheet("border-radius: 25px; "
                                   "max-height: 50px; "
                                   "max-width: 50px;")
        self.pixmap = mask_image(open("Gui/icons/profilepic.png", "rb").read(), "png", 50)
        self.picture.setPixmap(self.pixmap)
        self.message_content.add_widget(self.picture)




