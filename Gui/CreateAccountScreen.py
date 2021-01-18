from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *
from Frame import *
from Stylesheet import GuiColor
from TextLabel import TextLabel
from GuiButton import GuiButton
import pyqrcode
from pyqrcode import QRCode


class WaitForActivationFrame(Frame):
    def __init__(self):
        super().__init__(color=GuiColor.DARK_PRIMARY, content_margins=False)
        self.container = Frame(color=GuiColor.LIGHT_SECONDARY)
        self.add_widget(self.container)
        self.layout.setAlignment(self.container, Qt.AlignCenter)

        # activate label
        self.activate_label = TextLabel(text="3. Wait for transaction to process", font_size=20, bold=True)
        self.container.add_widget(self.activate_label)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        self.message_label = TextLabel("• Transactions usually take 15-30 seconds.\n\n• Your account will be created once "
                                       "your payment is received.\n\n• Any funds left over from the transaction will be "
                                       "saved in\n  your account balance.\n\n• If that username is already taken you will "
                                       "be prompted to\n  choose a new one.\n")
        self.container.add_widget(self.message_label)

        self.verify_account_button = GuiButton("Click me to create your account!")
        self.verify_account_button.setStyleSheet(GuiColor.NONE.value + " border: 0px; color: rgb(23, 198, 82); ")
        self.container.add_widget(self.verify_account_button)

        # vertical spacer
        self.add_spacer(SpacerDirection.VERTICAL)


class ActivateAccountFrame(Frame):
    def __init__(self,
                 receive_address: str,
                 copy_to_clipboard_method,
                 cost_to_create_account):
        super().__init__(color=GuiColor.DARK_PRIMARY, content_margins=False)
        self.container = Frame(color=GuiColor.LIGHT_SECONDARY)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.add_widget(self.container)
        self.layout.setAlignment(self.container, Qt.AlignTop)

        # activate label
        self.activate_label = TextLabel(text="2. Activate account", font_size=20, bold=True)
        self.container.add_widget(self.activate_label)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # activate account label
        print(cost_to_create_account)
        self.activate_account_label = TextLabel("• Accounts cost X Eth to create. This payment covers\n   the transaction "
                                                "fees associated with writing data\n   to the blockchain.\n\n• Please fund "
                                                "your account with X Eth to proceed.")
        self.container.add_widget(self.activate_account_label)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # address label
        self.your_public_address_label = TextLabel("• Your public address:")
        self.container.add_widget(self.your_public_address_label)

        # public receive address label
        self.receive_address_button = GuiButton(receive_address)
        self.receive_address_button.setContentsMargins(0, 0, 0, 0)
        self.receive_address_button.setToolTip("Click to copy to clipboard")
        self.receive_address_button.clicked.connect(copy_to_clipboard_method(receive_address))
        self.container.add_widget(self.receive_address_button)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # create a qr code
        self.container.add_widget(TextLabel("• You can also scan this QR code with your Ethereum\n   wallet app."))
        self.qr = QRCode(receive_address)

        # save the qr code as a png
        self.qr.png("Gui/QRCodes/QRCode.png", scale=8)

        # create a label to hold the QR code
        self.qr_label = TextLabel("")
        self.container.add_widget(self.qr_label)
        self.qr_label.setPixmap(QPixmap("Gui/QRCodes/QRCode.png"))


class CreateAccountFrame(Frame):
    def __init__(self, list_of_existing_accounts: list):
        super().__init__(color=GuiColor.DARK_PRIMARY, content_margins=False)
        self.list_of_existing_accounts = list_of_existing_accounts
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.container = Frame(color=GuiColor.LIGHT_SECONDARY)
        self.add_widget(self.container)
        self.layout.setAlignment(self.container, Qt.AlignCenter)

        # login label
        self.create_account_label = TextLabel(text="1. Pick a username", font_size=20, bold=True)
        self.container.add_widget(self.create_account_label)

        # add a little vertical spacing
        self.container.add_widget(TextLabel(""))

        # inform the user what characters are allowed
        self.container.add_widget(TextLabel("• Letters numbers and underscores are\n  allowed.\n\n• A \"@\" will be "
                                            "appended to the front\n  of your username.\n\n• Usernames must be "
                                            "less than 32\n  characters long.\n"))

        # username
        self.username_label = TextLabel("Username")
        self.container.add_widget(self.username_label)
        self.username = QLineEdit()
        self.username.textChanged.connect(self.text_changed)
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

        # vertical spacer
        self.add_spacer(SpacerDirection.VERTICAL)

    def text_changed(self):
        print(self.list_of_existing_accounts)


class CreateAccountScreen(Frame):
    def __init__(self,
                 receive_address: str,
                 copy_to_clipboard,
                 list_of_existing_accounts: list,
                 cost_to_create_account):
        super().__init__(content_margins=False,
                         color=GuiColor.DARK_PRIMARY,
                         border_radius=False)

        # container for both create and activate account
        self.container = Frame(layout=LayoutDirection.HORIZONTAL, content_margins=False)
        self.add_widget(self.container)

        # go back button container
        self.go_back_frame = Frame(content_margins=False)
        self.go_back_frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.container.add_widget(self.go_back_frame)

        # go back button
        self.login_button = GuiButton("Go back")
        self.login_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.go_back_frame.add_widget(self.login_button)
        self.go_back_frame.add_spacer(spacer_direction=SpacerDirection.VERTICAL)

        # spacer item
        self.container.add_spacer(SpacerDirection.HORIZONTAL)

        # create account
        self.create_account = CreateAccountFrame(list_of_existing_accounts)
        self.container.add_widget(self.create_account)

        # activate account
        self.activate_account = ActivateAccountFrame(receive_address, copy_to_clipboard, cost_to_create_account)
        self.container.add_widget(self.activate_account)

        # wait for account to activate
        self.wait_for_activation = WaitForActivationFrame()
        self.container.add_widget(self.wait_for_activation)

        # spacer item
        self.container.add_spacer(SpacerDirection.HORIZONTAL)

        # vertical spacer
        self.add_spacer(SpacerDirection.VERTICAL)


