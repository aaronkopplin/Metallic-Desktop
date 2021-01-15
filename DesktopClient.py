import sys
import os
from PySide6 import QtWidgets, QtCore, QtGui
from PIL import Image
import re
from image_rounder import mask_image
from Profile import Profile

class MetallicDesktopClient(QtWidgets.QMainWindow):
    def __init__(self):
        super(MetallicDesktopClient, self).__init__()
        os.system("pyside6-uic Gui.ui > Gui.py")
        from Gui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
        self.show()

    def configure(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.minimize_button.clicked.connect(self.minimize)
        self.ui.maximize_button.clicked.connect(self.maximize)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.dragable_frame.mouseMoveEvent = self.moveWindow

        self.profile_layout = QtWidgets.QGridLayout()
        self.profile_layout.addWidget(QtWidgets.QLabel("test"), 0, 0)
        self.ui.view_profile_page.setLayout(self.profile_layout)
        print("hello world")
        # pixmap = mask_image(open("icons/vitalik.png", "rb").read(), "png", 50)
        # self.ui.v_label.setPixmap(pixmap)
        # self.ui.payment_avi_2.setPixmap(pixmap)
        #
        # im1 = Image.open(r'icons/profilepic.jpg')
        # im1.save(r'icons/profilepic.png')
        #
        # profile_pixmap = mask_image(open("icons/profilepic.png", "rb").read(), "png", 130)
        # self.ui.profile_label.setPixmap(profile_pixmap)
        #
        # profile_pixmap = mask_image(open("icons/profilepic.png", "rb").read(), "png", 50)
        # self.ui.payment_avi.setPixmap(profile_pixmap)

        # self.profile = ProfileWidget(self.ui.view_profile_page)


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        if self.isMaximized():
            self.minimize()
        
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def minimize(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.main_frame.setStyleSheet(re.sub("border-radius: 0px;", "border-radius: 10px;", self.ui.main_frame.styleSheet()))
        else:
            self.showMinimized()

    def maximize(self):
        self.ui.main_frame.setStyleSheet(re.sub("border-radius: 10px;", "border-radius: 0px;", self.ui.main_frame.styleSheet()))
        self.showMaximized()


app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('icons/logo.jpeg'))
client = MetallicDesktopClient()
sys.exit(app.exec_())