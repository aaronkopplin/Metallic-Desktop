# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1181, 653)
        MainWindow.setMinimumSize(QSize(0, 100))
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"QFrame#main_frame {\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 29, 127, 255), stop:1 rgba(13, 14, 66, 255));\n"
"	border-radius: 10px;\n"
"}")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dragable_frame = QFrame(self.main_frame)
        self.dragable_frame.setObjectName(u"dragable_frame")
        self.dragable_frame.setStyleSheet(u"border: none;")
        self.dragable_frame.setFrameShape(QFrame.StyledPanel)
        self.dragable_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dragable_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_4 = QFrame(self.dragable_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:white; \n"
"font-size: 20px; \n"
"font-weight: bold;\n"
"")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.frame = QFrame(self.dragable_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minimize_button = QPushButton(self.frame)
        self.minimize_button.setObjectName(u"minimize_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_button.sizePolicy().hasHeightForWidth())
        self.minimize_button.setSizePolicy(sizePolicy1)
        self.minimize_button.setMinimumSize(QSize(0, 0))
        self.minimize_button.setMaximumSize(QSize(16, 16))
        self.minimize_button.setSizeIncrement(QSize(0, 0))
        self.minimize_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(255, 255, 0)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 0, 155);\n"
"}")

        self.horizontalLayout.addWidget(self.minimize_button)

        self.maximize_button = QPushButton(self.frame)
        self.maximize_button.setObjectName(u"maximize_button")
        sizePolicy1.setHeightForWidth(self.maximize_button.sizePolicy().hasHeightForWidth())
        self.maximize_button.setSizePolicy(sizePolicy1)
        self.maximize_button.setMinimumSize(QSize(0, 0))
        self.maximize_button.setMaximumSize(QSize(16, 16))
        self.maximize_button.setSizeIncrement(QSize(0, 0))
        self.maximize_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 255, 0, 155);\n"
"}")

        self.horizontalLayout.addWidget(self.maximize_button)

        self.close_button = QPushButton(self.frame)
        self.close_button.setObjectName(u"close_button")
        sizePolicy1.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy1)
        self.close_button.setMinimumSize(QSize(0, 0))
        self.close_button.setMaximumSize(QSize(16, 16))
        self.close_button.setSizeIncrement(QSize(0, 0))
        self.close_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(255, 0, 0)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 0, 0, 155);\n"
"}")

        self.horizontalLayout.addWidget(self.close_button)


        self.horizontalLayout_6.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.dragable_frame)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_8 = QFrame(self.main_frame)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setMinimumSize(QSize(300, 0))
        self.frame_8.setMaximumSize(QSize(300, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgb(62, 51, 186); border-radius: 10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_17 = QFrame(self.frame_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.friends_button = QPushButton(self.frame_17)
        self.friends_button.setObjectName(u"friends_button")
        icon = QIcon()
        icon.addFile(u"friends_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.friends_button.setIcon(icon)

        self.horizontalLayout_15.addWidget(self.friends_button)

        self.globe_button = QPushButton(self.frame_17)
        self.globe_button.setObjectName(u"globe_button")
        icon1 = QIcon()
        icon1.addFile(u"globe_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.globe_button.setIcon(icon1)

        self.horizontalLayout_15.addWidget(self.globe_button)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.search_bar = QLineEdit(self.page_3)
        self.search_bar.setObjectName(u"search_bar")
        sizePolicy1.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy1)
        self.search_bar.setMinimumSize(QSize(262, 20))
        self.search_bar.setMaximumSize(QSize(244, 20))
        self.search_bar.setStyleSheet(u"background-color: white; border-radius: 5px; ")

        self.horizontalLayout_14.addWidget(self.search_bar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(10000, 16777215))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 262, 462))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 9, 0, 0)
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(262, 16777215))
        self.frame_6.setStyleSheet(u"background-color: white")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.v_label = QLabel(self.frame_6)
        self.v_label.setObjectName(u"v_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.v_label.sizePolicy().hasHeightForWidth())
        self.v_label.setSizePolicy(sizePolicy5)
        self.v_label.setMinimumSize(QSize(50, 50))
        self.v_label.setMaximumSize(QSize(50, 50))
        self.v_label.setStyleSheet(u"border-radius: 25px;\n"
"border: 2px;\n"
"border-color: red;\n"
"background-color: yellow;")

        self.horizontalLayout_8.addWidget(self.v_label)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy6)
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy7)
        self.label_5.setStyleSheet(u"font-size: 15px;")

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy7)
        self.label_6.setStyleSheet(u"color: grey;")

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: grey;")

        self.verticalLayout_7.addWidget(self.label_14)


        self.horizontalLayout_8.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_12.addLayout(self.verticalLayout_3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_19 = QFrame(self.main_frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"border: none;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_19)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setStyleSheet(u"background-color: rgb(62, 51, 186); \n"
"border-radius: 10px; \n"
"color: white; \n"
"font-size: 20px;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_8)

        self.frame_10 = QFrame(self.frame_19)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255); border-radius: 10px; border: none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.payments_scroll_area = QScrollArea(self.frame_10)
        self.payments_scroll_area.setObjectName(u"payments_scroll_area")
        self.payments_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 547, 400))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy8)
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setStyleSheet(u"color: grey;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy4.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy4)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.frame_9 = QFrame(self.frame_15)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(300, 0))
        self.frame_9.setMaximumSize(QSize(300, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgb(62, 51, 186);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy6.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy6)
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-size: 15px; color: white")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_9)

        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: grey;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_4)


        self.horizontalLayout_10.addWidget(self.frame_12)

        self.payment_avi = QLabel(self.frame_9)
        self.payment_avi.setObjectName(u"payment_avi")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.payment_avi.sizePolicy().hasHeightForWidth())
        self.payment_avi.setSizePolicy(sizePolicy9)
        self.payment_avi.setMaximumSize(QSize(50, 50))
        self.payment_avi.setStyleSheet(u"border-radius: 25px;\n"
"border: 2px;\n"
"border-color: red;\n"
"background-color: yellow;")

        self.horizontalLayout_10.addWidget(self.payment_avi)


        self.horizontalLayout_12.addWidget(self.frame_9)


        self.horizontalLayout_18.addWidget(self.frame_15)


        self.verticalLayout_17.addLayout(self.horizontalLayout_18)


        self.verticalLayout_4.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy10)
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setStyleSheet(u"color: grey;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy8.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy8)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_16)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy11)
        self.frame_13.setMinimumSize(QSize(300, 0))
        self.frame_13.setStyleSheet(u"background-color: rgb(62, 51, 186)")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.payment_avi_2 = QLabel(self.frame_13)
        self.payment_avi_2.setObjectName(u"payment_avi_2")
        sizePolicy9.setHeightForWidth(self.payment_avi_2.sizePolicy().hasHeightForWidth())
        self.payment_avi_2.setSizePolicy(sizePolicy9)
        self.payment_avi_2.setMaximumSize(QSize(50, 50))
        self.payment_avi_2.setStyleSheet(u"border-radius: 25px;\n"
"border: 2px;\n"
"border-color: red;\n"
"background-color: yellow;")

        self.horizontalLayout_11.addWidget(self.payment_avi_2)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy6.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy6)
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-size: 15px; color: white;")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: grey;")

        self.verticalLayout_11.addWidget(self.label_7)


        self.horizontalLayout_11.addWidget(self.frame_14)


        self.horizontalLayout_13.addWidget(self.frame_13)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_19.addWidget(self.frame_16)


        self.verticalLayout_18.addLayout(self.horizontalLayout_19)


        self.verticalLayout_4.addLayout(self.verticalLayout_18)

        self.payments_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_19.addWidget(self.payments_scroll_area)


        self.verticalLayout_9.addLayout(self.verticalLayout_19)


        self.verticalLayout_20.addWidget(self.frame_10)

        self.frame_18 = QFrame(self.frame_19)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 100))
        self.frame_18.setStyleSheet(u"background-color: rgb(62, 51, 186); border-radius: 10px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(18, 18, 18, 18)
        self.pushButton_4 = QPushButton(self.frame_18)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"download_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lineEdit = QLineEdit(self.frame_18)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 20))
        self.lineEdit.setStyleSheet(u"background-color: white; border-radius: 5px;")

        self.verticalLayout_14.addWidget(self.lineEdit)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:white; \n"
"font-size: 20px; \n"
"font-weight: bold;\n"
"")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_3)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton = QPushButton(self.frame_18)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy5)
        icon3 = QIcon()
        icon3.addFile(u"up_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.verticalLayout_15.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_18)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy5.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy5)
        icon4 = QIcon()
        icon4.addFile(u"down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon4)

        self.verticalLayout_15.addWidget(self.pushButton_2)


        self.horizontalLayout_16.addLayout(self.verticalLayout_15)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pushButton_3 = QPushButton(self.frame_18)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"paper_plane_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout_20.addWidget(self.frame_18)


        self.horizontalLayout_5.addWidget(self.frame_19)

        self.frame_5 = QFrame(self.main_frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy12)
        self.frame_5.setMinimumSize(QSize(300, 0))
        self.frame_5.setStyleSheet(u"background-color: rgb(62, 51, 186); border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy13)
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
        sizePolicy9.setHeightForWidth(self.profile_label.sizePolicy().hasHeightForWidth())
        self.profile_label.setSizePolicy(sizePolicy9)
        self.profile_label.setMaximumSize(QSize(130, 130))
        self.profile_label.setStyleSheet(u"border-radius: 65px;\n"
"border: 2px;\n"
"border-color: red;\n"
"background-color: yellow;")

        self.horizontalLayout_9.addWidget(self.profile_label)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.name_label = QLabel(self.frame_5)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setStyleSheet(u"font-size: 20px; color: white;")
        self.name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.name_label)

        self.username_label = QLabel(self.frame_5)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setStyleSheet(u"color: white;")
        self.username_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.username_label)

        self.balance_label = QLabel(self.frame_5)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setStyleSheet(u"color: white;")
        self.balance_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.balance_label)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: white;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.frame_2 = QFrame(self.main_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Metallic", None))
        self.minimize_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.friends_button.setText("")
        self.globe_button.setText("")
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.v_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Vitalik Buterin", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"@Viatlik", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Score: 78", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Vitalik Buterin", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Dec 12, 2020", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"You paid @vitalik 0.05 Eth", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Thanks for inventing Ethereum", None))
        self.payment_avi.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Dec 15, 2020", None))
        self.payment_avi_2.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"@vitalik paid you 1.00 Eth", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"The pleasure is all mine", None))
        self.pushButton_4.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"memo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0.00 Eth", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.profile_label.setText("")
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Aaron Kopplin", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"@aaronkopplin", None))
        self.balance_label.setText(QCoreApplication.translate("MainWindow", u"Balance: 0 Eth", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Score: 152", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Logged In", None))
    # retranslateUi

