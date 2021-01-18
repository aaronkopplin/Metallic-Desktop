import glob
from PySide6.QtWidgets import *
from Frame import Frame
from App import App
from Stylesheet import GuiColor
from LoginScreen import LoginScreen
from CreateAccountScreen import CreateAccountScreen
from ActivateAccountScreen import ActivateAccountScreen
from HeaderFrame import HeaderFrame


class MainWindow(QMainWindow):
    def __init__(self,
                 create_account_method,
                 login_method,
                 wallet_exists: bool,
                 receive_address: str,
                 copy_to_clipboard,
                 list_of_existing_accounts,
                 cost_to_create_account):
        super().__init__(None)

        # method calls
        self.create_account_method = create_account_method
        self.login_method = login_method

        self.setMinimumWidth(1100)
        self.setMinimumHeight(600)
        self.setWindowTitle("Metallic")
        self.setContentsMargins(0, 0, 0, 0)

        # frame to handle login and app
        self.frame = Frame(content_margins=True, color=GuiColor.DARK_PRIMARY, border_radius=False)
        self.setCentralWidget(self.frame)

        self.title_bar = HeaderFrame(self.width, 50)
        self.frame.add_widget(self.title_bar)

        # stack
        self.stack = QStackedWidget()
        self.frame.add_widget(self.stack)

        # login screen
        self.login_screen = LoginScreen(wallet_exists)
        self.stack.addWidget(self.login_screen)
        self.login_screen.create_account_button.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.login_screen.login_button.clicked.connect(self.login_event)
        self.stack.setCurrentIndex(0)

        # create account screen
        self.create_account_screen = CreateAccountScreen(receive_address,
                                                         copy_to_clipboard,
                                                         list_of_existing_accounts,
                                                         cost_to_create_account)
        self.stack.addWidget(self.create_account_screen)
        # self.create_account_screen.activate_account.activate_account_button.clicked.connect(self.create_account_event)
        self.create_account_screen.login_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        # app
        self.app = App()
        self.stack.addWidget(self.app)

    def login_event(self):
        # external backend behavior
        if self.login_method():
            # internal gui behavior
            self.stack.setCurrentIndex(3)

    def create_account_event(self):
        # internal gui behavior
        self.stack.setCurrentIndex(0)

        # back end behavior
        self.create_account_method()

    def create_account_username(self):
        return self.create_account_screen.username.text()

    def create_account_password(self):
        return self.create_account_screen.password.text()

    def create_account_confirm_password(self):
        return self.create_account_screen.confirm_password.text()

    def login_username(self):
        return self.login_screen.username.text()

    def login_password(self):
        return self.login_screen.password.text()
