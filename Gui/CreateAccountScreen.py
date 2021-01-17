from PySide6.QtWidgets import *
from Frame import *
from Stylesheet import GuiColor
from TextLabel import TextLabel
from GuiButton import GuiButton


class CreateAccountScreen(Frame):
    def __init__(self):
        super().__init__(content_margins=False,
                         color=GuiColor.DARK_PRIMARY,
                         border_radius=False)

        self.container = Frame(color=GuiColor.LIGHT_SECONDARY)
        self.container.setFixedWidth(250)
        self.add_widget(self.container)
        self.layout.setAlignment(self.container, Qt.AlignCenter)

        # vertical spacer
        self.container.add_spacer(SpacerDirection.VERTICAL)

        # login label
        self.create_account_label = TextLabel(text="Create Account", font_size=20, bold=True)
        self.container.add_widget(self.create_account_label)

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

        # confirm password
        self.confirm_password_label = TextLabel("Confirm Password")
        self.container.add_widget(self.confirm_password_label)
        self.confirm_password = QLineEdit()
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.container.add_widget(self.confirm_password)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # create account button
        self.create_account_button = GuiButton("Create Account")
        self.container.add_widget(self.create_account_button)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # already have an account? login
        self.login_button = GuiButton("Already have an account? Login")
        self.container.add_widget(self.login_button)

        # vertical spacer
        self.container.add_spacer(SpacerDirection.VERTICAL)
