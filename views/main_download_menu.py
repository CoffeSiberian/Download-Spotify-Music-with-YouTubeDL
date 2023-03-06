from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QFrame, QHBoxLayout,QLabel, 
    QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout
    )

class downloadMenuLink(object):
    def setupUi(self, dialog_menu_download_link):
        if not dialog_menu_download_link.objectName():
            dialog_menu_download_link.setObjectName(u"dialog_menu_download_link")
        dialog_menu_download_link.resize(400, 200)
        dialog_menu_download_link.setMinimumSize(QSize(0, 0))
        dialog_menu_download_link.setMaximumSize(QSize(400, 200))
        self.horizontalLayout_4 = QHBoxLayout(dialog_menu_download_link)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.background_frame_link = QFrame(dialog_menu_download_link)
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
        self.title_download_menu = QLabel(self.text_info_frame)
        self.title_download_menu.setObjectName(u"title_download_menu")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.title_download_menu.setFont(font)
        self.title_download_menu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_download_menu)


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
        self.horizontal_spacer_download_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontal_spacer_download_2)

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

        self.horizontal_spacer_download_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontal_spacer_download_3)


        self.horizontalLayout_3.addWidget(self.link_frame_2)


        self.verticalLayout_3.addWidget(self.link_frame)

        self.manu_download_options_frame = QFrame(self.background_frame_link)
        self.manu_download_options_frame.setObjectName(u"manu_download_options_frame")
        self.manu_download_options_frame.setFrameShape(QFrame.StyledPanel)
        self.manu_download_options_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.manu_download_options_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontal_spacer_download_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontal_spacer_download_1)

        self.download_menu_download_botton = QPushButton(self.manu_download_options_frame)
        self.download_menu_download_botton.setObjectName(u"download_menu_download_botton")
        self.download_menu_download_botton.setEnabled(True)
        self.download_menu_download_botton.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.download_menu_download_botton)

        self.download_menu_cancel_botton = QPushButton(self.manu_download_options_frame)
        self.download_menu_cancel_botton.setObjectName(u"download_menu_cancel_botton")
        self.download_menu_cancel_botton.setEnabled(True)
        self.download_menu_cancel_botton.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_2.addWidget(self.download_menu_cancel_botton)


        self.verticalLayout_3.addWidget(self.manu_download_options_frame)


        self.horizontalLayout_4.addWidget(self.background_frame_link)


        self.retranslateUi(dialog_menu_download_link)

        QMetaObject.connectSlotsByName(dialog_menu_download_link)

    def retranslateUi(self, dialog_menu_download_link):
        dialog_menu_download_link.setWindowTitle(QCoreApplication.translate("dialog_menu_download_link", u"Spotify Downloader", None))
        self.title_download_menu.setText(QCoreApplication.translate("dialog_menu_download_link", u"Paste your Spotify Link", None))
        self.link_icon.setText("")
        self.download_menu_download_botton.setText(QCoreApplication.translate("dialog_menu_download_link", u"Download", None))
        self.download_menu_cancel_botton.setText(QCoreApplication.translate("dialog_menu_download_link", u"Cancel", None))