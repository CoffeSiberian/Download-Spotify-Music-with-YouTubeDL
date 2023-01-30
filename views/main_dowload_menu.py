from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout,QLabel, 
    QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout
    )

class DowloadMenuLink(object):
    def setupUi(self, dialog_menu_dowload_link):
        if not dialog_menu_dowload_link.objectName():
            dialog_menu_dowload_link.setObjectName(u"dialog_menu_dowload_link")
        dialog_menu_dowload_link.resize(400, 200)
        dialog_menu_dowload_link.setMinimumSize(QSize(0, 0))
        dialog_menu_dowload_link.setMaximumSize(QSize(400, 200))
        self.horizontalLayout_4 = QHBoxLayout(dialog_menu_dowload_link)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.background_frame_link = QFrame(dialog_menu_dowload_link)
        self.background_frame_link.setObjectName(u"background_frame_link")
        self.background_frame_link.setFrameShape(QFrame.StyledPanel)
        self.background_frame_link.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame_link)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.text_info_frame = QFrame(self.background_frame_link)
        self.text_info_frame.setObjectName(u"text_info_frame")
        self.text_info_frame.setFrameShape(QFrame.StyledPanel)
        self.text_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.text_info_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_dowload_menu = QLabel(self.text_info_frame)
        self.title_dowload_menu.setObjectName(u"title_dowload_menu")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.title_dowload_menu.setFont(font)
        self.title_dowload_menu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_dowload_menu)


        self.verticalLayout_3.addWidget(self.text_info_frame)

        self.link_frame = QFrame(self.background_frame_link)
        self.link_frame.setObjectName(u"link_frame")
        self.link_frame.setFrameShape(QFrame.StyledPanel)
        self.link_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.link_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.link_frame_2 = QFrame(self.link_frame)
        self.link_frame_2.setObjectName(u"link_frame_2")
        self.link_frame_2.setFrameShape(QFrame.StyledPanel)
        self.link_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.link_frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontal_spacer_dowload_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontal_spacer_dowload_2)

        self.link_icon = QLabel(self.link_frame_2)
        self.link_icon.setObjectName(u"link_icon")
        self.link_icon.setMinimumSize(QSize(30, 30))
        self.link_icon.setMaximumSize(QSize(30, 30))
        self.link_icon.setPixmap(QPixmap(u"assets/icons/link.png"))
        self.link_icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.link_icon)

        self.textobox_link = QLineEdit(self.link_frame_2)
        self.textobox_link.setObjectName(u"textobox_link")
        self.textobox_link.setMinimumSize(QSize(250, 30))
        self.textobox_link.setMaximumSize(QSize(250, 30))

        self.horizontalLayout.addWidget(self.textobox_link)

        self.horizontal_spacer_dowload_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontal_spacer_dowload_3)


        self.horizontalLayout_3.addWidget(self.link_frame_2)


        self.verticalLayout_3.addWidget(self.link_frame)

        self.manu_dowload_options_frame = QFrame(self.background_frame_link)
        self.manu_dowload_options_frame.setObjectName(u"manu_dowload_options_frame")
        self.manu_dowload_options_frame.setFrameShape(QFrame.StyledPanel)
        self.manu_dowload_options_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.manu_dowload_options_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontal_spacer_dowload_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontal_spacer_dowload_1)

        self.dowload_menu_dowload_botton = QPushButton(self.manu_dowload_options_frame)
        self.dowload_menu_dowload_botton.setObjectName(u"dowload_menu_dowload_botton")
        self.dowload_menu_dowload_botton.setEnabled(True)
        self.dowload_menu_dowload_botton.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.dowload_menu_dowload_botton)

        self.dowload_menu_cancel_botton = QPushButton(self.manu_dowload_options_frame)
        self.dowload_menu_cancel_botton.setObjectName(u"dowload_menu_cancel_botton")
        self.dowload_menu_cancel_botton.setEnabled(True)
        self.dowload_menu_cancel_botton.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.dowload_menu_cancel_botton)


        self.verticalLayout_3.addWidget(self.manu_dowload_options_frame)


        self.horizontalLayout_4.addWidget(self.background_frame_link)


        self.retranslateUi(dialog_menu_dowload_link)

        QMetaObject.connectSlotsByName(dialog_menu_dowload_link)

    def retranslateUi(self, dialog_menu_dowload_link):
        dialog_menu_dowload_link.setWindowTitle(QCoreApplication.translate("dialog_menu_dowload_link", u"Spotify Downloader", None))
        self.title_dowload_menu.setText(QCoreApplication.translate("dialog_menu_dowload_link", u"Paste your Spotify Link", None))
        self.link_icon.setText("")
        self.dowload_menu_dowload_botton.setText(QCoreApplication.translate("dialog_menu_dowload_link", u"Dowload", None))
        self.dowload_menu_cancel_botton.setText(QCoreApplication.translate("dialog_menu_dowload_link", u"Cancel", None))