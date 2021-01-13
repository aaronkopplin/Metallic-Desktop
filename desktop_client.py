import sys
import os
from PySide6 import QtWidgets, QtCore, QtGui
import PySide6
import re

class MetallicDesktopClient(QtWidgets.QMainWindow):
    def __init__(self):
        super(MetallicDesktopClient, self).__init__()
        os.system("pyside6-uic gui.ui > gui.py")
        from gui import Ui_MainWindow
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
client = MetallicDesktopClient()
sys.exit(app.exec_())