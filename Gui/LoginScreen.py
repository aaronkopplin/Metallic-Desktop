from Frame import *
from Stylesheet import GuiColor
from TextLabel import TextLabel
from GuiButton import GuiButton


class LoginScreen(Frame):
    def __init__(self, wallet_exists: bool):
        super().__init__(content_margins=False,
                         border_radius=False)

        self.container = Frame(color=GuiColor.LIGHT_SECONDARY)
        self.container.setFixedWidth(250)
        self.add_widget(self.container)
        self.layout.setAlignment(self.container, Qt.AlignCenter)

        # vertical spacer
        self.container.add_spacer(SpacerDirection.VERTICAL)

        # login label
        self.login_label = TextLabel(text="Login", font_size=20, bold=True)
        self.container.add_widget(self.login_label)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # username
        self.username_label = TextLabel("Username")
        self.container.add_widget(self.username_label)
        self.username = QLineEdit()
        self.container.add_widget(self.username)

        # password
        self.password_label = TextLabel("Password")
        self.container.add_widget(self.password_label)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.container.add_widget(self.password)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # login button
        self.login_button = GuiButton("Login")
        self.container.add_widget(self.login_button)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # create account button
        self.create_account_button = GuiButton("Don't have an account?")
        self.container.add_widget(self.create_account_button)

        # hide create account option if there is a wallet on the machine
        if wallet_exists:
            self.create_account_button.hide()

        # vertical spacer
        self.container.add_spacer(SpacerDirection.VERTICAL)

