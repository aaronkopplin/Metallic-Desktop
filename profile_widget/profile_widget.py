# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(282, 531)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(Frame)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(275, 130))
        self.frame_11.setMaximumSize(QSize(16777215, 130))
        self.frame_11.setSizeIncrement(QSize(0, 130))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.profile_label = QLabel(self.frame_11)
        self.profile_label.setObjectName(u"profile_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.profile_label.sizePolicy().hasHeightForWidth())
        self.profile_label.setSizePolicy(sizePolicy1)
        self.profile_label.setMaximumSize(QSize(130, 130))
        self.profile_label.setStyleSheet(u"border-radius: 65px;\n"
"background-color: yellow;\n"
"min-width: 130px;\n"
"min-height: 130px;\n"
"")

        self.horizontalLayout_9.addWidget(self.profile_label)


        self.verticalLayout.addWidget(self.frame_11)

        self.name_label = QLabel(Frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setStyleSheet(u"font-size: 20px; color: white;")
        self.name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.name_label)

        self.username_label = QLabel(Frame)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setStyleSheet(u"color: white;")
        self.username_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.username_label)

        self.balance_label = QLabel(Frame)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setStyleSheet(u"color: white;")
        self.balance_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.balance_label)

        self.label_13 = QLabel(Frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: white;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.verticalSpacer_4 = QSpacerItem(20, 329, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.profile_label.setText("")
        self.name_label.setText(QCoreApplication.translate("Frame", u"Aaron Kopplin", None))
        self.username_label.setText(QCoreApplication.translate("Frame", u"@aaronkopplin", None))
        self.balance_label.setText(QCoreApplication.translate("Frame", u"Balance: 0 Eth", None))
        self.label_13.setText(QCoreApplication.translate("Frame", u"Score: 152", None))
    # retranslateUi

