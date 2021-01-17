from Frame import *
from Stylesheet import GuiColor
from TextLabel import TextLabel
from GuiButton import GuiButton


class ActivateAccountScreen(Frame):
    def __init__(self):
        super().__init__(content_margins=False,
                         color=GuiColor.DARK_PRIMARY,
                         border_radius=False)

        self.container = Frame()
        self.container.setFixedWidth(250)
        self.add_widget(self.container)
        self.layout.setAlignment(self.container, Qt.AlignCenter)

        # vertical spacer
        self.container.add_spacer(SpacerDirection.VERTICAL)

        # activate account label
        self.activate_account_label = TextLabel("Please sent X Eth to this account")
        self.container.add_widget(self.activate_account_label)

        # public receive address label
        self.receive_address_label = TextLabel("0x1233....")
        self.container.add_widget(self.receive_address_label)

        # activate account button
        self.activate_account_button = GuiButton("Activate Account")
        self.container.add_widget(self.activate_account_button)

        # vertical spacer
        self.container.add_spacer(SpacerDirection.VERTICAL)

