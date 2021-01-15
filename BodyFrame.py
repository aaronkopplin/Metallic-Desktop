from ContactsFrame import ContactsFrame
from MessagesFrame import MessagesFrame
from ProfileStackFrame import ProfileStackFrame
from Frame import *


class BodyFrame(Frame):
    def __init__(self):
        super().__init__(layout=LayoutDirection.HORIZONTAL)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # contacts frame
        self.contacts_frame = ContactsFrame()
        self.add_widget(self.contacts_frame)

        # messages frame
        self.messages_frame = MessagesFrame()
        self.add_widget(self.messages_frame)

        # profile stack frame
        self.profile_stack_frame = ProfileStackFrame()
        self.add_widget(self.profile_stack_frame)
