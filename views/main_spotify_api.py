from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor, QFont, QIcon, QPixmap
from PySide6.QtWidgets import (
    QCommandLinkButton, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout
)


class SpotifyConfig(object):
    def setupUi(self, main_spotify_api_dialog):
        if not main_spotify_api_dialog.objectName():
            main_spotify_api_dialog.setObjectName(u"main_spotify_api_dialog")
        main_spotify_api_dialog.resize(400, 300)
        main_spotify_api_dialog.setMinimumSize(QSize(400, 300))
        main_spotify_api_dialog.setMaximumSize(QSize(400, 300))
        self.horizontalLayout_5 = QHBoxLayout(main_spotify_api_dialog)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.background_frame_api = QFrame(main_spotify_api_dialog)
        self.background_frame_api.setObjectName(u"background_frame_api")
        self.background_frame_api.setFrameShape(QFrame.StyledPanel)
        self.background_frame_api.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.background_frame_api)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(self.background_frame_api)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.title_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title_frame_2 = QFrame(self.title_frame)
        self.title_frame_2.setObjectName(u"title_frame_2")
        self.title_frame_2.setMinimumSize(QSize(0, 50))
        self.title_frame_2.setFrameShape(QFrame.StyledPanel)
        self.title_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.title_frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4_title = QHBoxLayout()
        self.horizontalLayout_4_title.setObjectName(
            u"horizontalLayout_4_title")
        self.horizontalSpacer_2_title = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4_title.addItem(self.horizontalSpacer_2_title)

        self.img = QLabel(self.title_frame_2)
        self.img.setObjectName(u"img")
        self.img.setMinimumSize(QSize(30, 30))
        self.img.setMaximumSize(QSize(30, 30))
        self.img.setPixmap(QPixmap(u"assets/icons/spotify.png"))
        self.img.setScaledContents(True)

        self.horizontalLayout_4_title.addWidget(self.img)

        self.title_dialog = QLabel(self.title_frame_2)
        self.title_dialog.setObjectName(u"title_dialog")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        self.title_dialog.setFont(font)
        self.title_dialog.setAlignment(Qt.AlignCenter)
        self.title_dialog.setMargin(3)

        self.horizontalLayout_4_title.addWidget(self.title_dialog)

        self.horizontalSpacer_3_title = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4_title.addItem(self.horizontalSpacer_3_title)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4_title)

        self.verticalLayout_4.addWidget(self.title_frame_2)

        self.horizontalLayout_form = QHBoxLayout()
        self.horizontalLayout_form.setObjectName(u"horizontalLayout_form")
        self.verticalLayout_names = QVBoxLayout()
        self.verticalLayout_names.setObjectName(u"verticalLayout_names")
        self.client_id = QLabel(self.title_frame)
        self.client_id.setObjectName(u"client_id")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.client_id.setFont(font1)
        self.client_id.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_names.addWidget(self.client_id)

        self.client_secret = QLabel(self.title_frame)
        self.client_secret.setObjectName(u"client_secret")
        self.client_secret.setFont(font1)
        self.client_secret.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_names.addWidget(self.client_secret)

        self.horizontalLayout_form.addLayout(self.verticalLayout_names)

        self.verticalLayout_textbox = QVBoxLayout()
        self.verticalLayout_textbox.setObjectName(u"verticalLayout_textbox")
        self.lineEdit_client_id = QLineEdit(self.title_frame)
        self.lineEdit_client_id.setObjectName(u"lineEdit_client_id")
        self.lineEdit_client_id.setMinimumSize(QSize(250, 30))

        self.verticalLayout_textbox.addWidget(self.lineEdit_client_id)

        self.lineEdit_client_secret = QLineEdit(self.title_frame)
        self.lineEdit_client_secret.setObjectName(u"lineEdit_client_secret")
        self.lineEdit_client_secret.setMinimumSize(QSize(250, 30))
        self.lineEdit_client_secret.setEchoMode(QLineEdit.Password)

        self.verticalLayout_textbox.addWidget(self.lineEdit_client_secret)

        self.horizontalLayout_form.addLayout(self.verticalLayout_textbox)

        self.verticalLayout_4.addLayout(self.horizontalLayout_form)

        self.frame_save_botton = QFrame(self.title_frame)
        self.frame_save_botton.setObjectName(u"frame_save_botton")
        self.frame_save_botton.setFrameShape(QFrame.StyledPanel)
        self.frame_save_botton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_save_botton)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_save = QPushButton(self.frame_save_botton)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setEnabled(True)
        self.pushButton_save.setMinimumSize(QSize(90, 30))
        self.pushButton_save.setMaximumSize(QSize(90, 30))
        icon = QIcon()
        icon.addFile(u"assets/icons/diskette.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton_save)

        self.verticalLayout_4.addWidget(self.frame_save_botton)

        self.verticalLayout_5.addWidget(self.title_frame)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.boton_frame = QFrame(self.background_frame_api)
        self.boton_frame.setObjectName(u"boton_frame")
        self.boton_frame.setFrameShape(QFrame.StyledPanel)
        self.boton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.boton_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 6, 6)
        self.horizontalSpacer_boton = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_boton)

        self.gitHub = QCommandLinkButton(self.boton_frame)
        self.gitHub.setObjectName(u"gitHub")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gitHub.sizePolicy().hasHeightForWidth())
        self.gitHub.setSizePolicy(sizePolicy)
        self.gitHub.setMaximumSize(QSize(160, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.gitHub.setFont(font2)
        self.gitHub.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"assets/icons/question.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.gitHub.setIcon(icon1)
        self.gitHub.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.gitHub)

        self.verticalLayout_5.addWidget(self.boton_frame)

        self.horizontalLayout_5.addWidget(self.background_frame_api)

        self.retranslateUi(main_spotify_api_dialog)

        QMetaObject.connectSlotsByName(main_spotify_api_dialog)

    def retranslateUi(self, main_spotify_api_dialog):
        main_spotify_api_dialog.setWindowTitle(
            QCoreApplication.translate("main_spotify_api_dialog", u"API KEY", None))
        self.img.setText("")
        self.title_dialog.setText(QCoreApplication.translate(
            "main_spotify_api_dialog", u"Spotify API KEY", None))
        self.client_id.setText(QCoreApplication.translate(
            "main_spotify_api_dialog", u"Client ID", None))
        self.client_secret.setText(QCoreApplication.translate(
            "main_spotify_api_dialog", u"Client Secret", None))
        self.pushButton_save.setText(QCoreApplication.translate(
            "main_spotify_api_dialog", u"Save", None))
        self.gitHub.setText(QCoreApplication.translate(
            "main_spotify_api_dialog", u"How to get API KEY", None))
