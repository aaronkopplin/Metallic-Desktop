import sys
from PySide6.QtWidgets import *
from Stylesheet import *
from NewGui.HeaderFrame import HeaderFrame
from NewGui.BodyFrame import BodyFrame
from NewGui.Frame import Frame


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(930)
        self.setMinimumHeight(600)
        self.setWindowTitle("Metallic")
        self.setContentsMargins(0, 0, 0, 0)

        # main frame
        self.main_frame = Frame(color=GuiColor.DARK_PRIMARY, border_radius=False)
        self.setCentralWidget(self.main_frame)

        # header frame
        self.header_frame = HeaderFrame(self.width, 50)
        self.main_frame.add_widget(self.header_frame)

        # body frame
        self.body_frame = BodyFrame()
        self.main_frame.add_widget(self.body_frame)


if __name__ == '__main__':
    app = QApplication([])

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())