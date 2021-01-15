from PySide6.QtWidgets import *
from NewGui.ContactsFrame import ContactsFrame
from NewGui.MessagesFrame import MessagesFrame
from NewGui.ProfileStackFrame import ProfileStackFrame


class BodyFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # contacts frame
        self.contacts_frame = ContactsFrame()
        self.layout.addWidget(self.contacts_frame)

        # messages frame
        self.messages_frame = MessagesFrame()
        self.layout.addWidget(self.messages_frame)

        # profile stack frame
        self.profile_stack_frame = ProfileStackFrame()
        self.layout.addWidget(self.profile_stack_frame)
