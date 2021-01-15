from PySide6.QtWidgets import *


class Profile(QFrame):
    def __init__(self, width, height):
        super(Profile, self).__init__()
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)
        self.setStyleSheet("background-color: yellow;")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.profile_picture = QLabel()
        self.profile_picture.setStyleSheet(
            '''
            min-height: 130px; 
            min-width: 130px; 
            border-radius: 65px; 
            background-color: yellow;
            '''
        )
        self.add