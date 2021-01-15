import sys
import re
from PySide6.QtWidgets import *
from PySide6 import QtCore
from Stylesheet import *
from NewGui.HeaderFrame import HeaderFrame
from NewGui.BodyFrame import BodyFrame


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(930)
        self.setMinimumHeight(600)

        # remove grey title handle
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        # main frame
        self.main_frame = QFrame()
        self.main_frame.setStyleSheet(s_main_frame)
        self.setCentralWidget(self.main_frame)
        self.main_frame.setLayout(self.layout)

        # header frame
        self.header_frame = HeaderFrame(self.width, 50)
        self.header_frame.minimize_button.clicked.connect(self.minimize)
        self.header_frame.maximize_button.clicked.connect(self.maximize)
        self.header_frame.close_button.clicked.connect(self.close)
        self.header_frame.mouseMoveEvent = self.moveWindow
        self.layout.addWidget(self.header_frame, 0)

        # body frame
        self.body_frame = BodyFrame()
        self.layout.addWidget(self.body_frame)

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
            self.main_frame.setStyleSheet(
                re.sub("border-radius: 0px;", "border-radius: 10px;", self.main_frame.styleSheet()))
        else:
            self.showMinimized()

    def maximize(self):
        self.main_frame.setStyleSheet(
            re.sub("border-radius: 10px;", "border-radius: 0px;", self.main_frame.styleSheet()))
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication([])

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())