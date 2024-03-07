from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QCursor, QFont, QIcon, QPixmap
from PySide6.QtWidgets import (
    QCommandLinkButton, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout
)
from functions.path import FILE_PATH


class About(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(380, 425)
        about.setMinimumSize(QSize(380, 425))
        about.setMaximumSize(QSize(380, 425))
        self.verticalLayout = QVBoxLayout(about)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QFrame(about)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFrameShape(QFrame.StyledPanel)
        self.centralwidget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.info_used = QFrame(self.centralwidget)
        self.info_used.setObjectName(u"info_used")
        self.info_used.setFrameShape(QFrame.StyledPanel)
        self.info_used.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.info_used)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.info_used)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pythonico = QLabel(self.groupBox)
        self.pythonico.setObjectName(u"pythonico")
        self.pythonico.setMinimumSize(QSize(70, 70))
        self.pythonico.setMaximumSize(QSize(70, 70))
        self.pythonico.setPixmap(
            QPixmap(f"{FILE_PATH}/assets/icons/icons8-python-480.png"))
        self.pythonico.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.pythonico)

        self.pysideicon = QLabel(self.groupBox)
        self.pysideicon.setObjectName(u"pysideicon")
        self.pysideicon.setMinimumSize(QSize(70, 70))
        self.pysideicon.setMaximumSize(QSize(70, 70))
        self.pysideicon.setPixmap(
            QPixmap(f"{FILE_PATH}/assets/icons/pyside6.png"))
        self.pysideicon.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.pysideicon)

        self.spotifyicon = QLabel(self.groupBox)
        self.spotifyicon.setObjectName(u"spotifyicon")
        self.spotifyicon.setMinimumSize(QSize(70, 70))
        self.spotifyicon.setMaximumSize(QSize(70, 70))
        self.spotifyicon.setPixmap(
            QPixmap(f"{FILE_PATH}/assets/icons/spotify.png"))
        self.spotifyicon.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.spotifyicon)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.addWidget(self.groupBox)

        self.verticalLayout_6.addWidget(self.info_used)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.createby = QFrame(self.centralwidget)
        self.createby.setObjectName(u"createby")
        self.createby.setFrameShape(QFrame.StyledPanel)
        self.createby.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.createby)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_2 = QGroupBox(self.createby)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nickname_info = QLabel(self.groupBox_2)
        self.nickname_info.setObjectName(u"nickname_info")
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        self.nickname_info.setFont(font2)
        self.nickname_info.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.nickname_info)

        self.name_info = QLabel(self.groupBox_2)
        self.name_info.setObjectName(u"name_info")
        self.name_info.setFont(font2)
        self.name_info.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.name_info)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.nickname = QLabel(self.groupBox_2)
        self.nickname.setObjectName(u"nickname")
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(True)
        self.nickname.setFont(font3)

        self.verticalLayout_4.addWidget(self.nickname)

        self.name = QLabel(self.groupBox_2)
        self.name.setObjectName(u"name")
        font4 = QFont()
        font4.setItalic(False)
        self.name.setFont(font4)

        self.verticalLayout_4.addWidget(self.name)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.gitHub = QCommandLinkButton(self.groupBox_2)
        self.gitHub.setObjectName(u"gitHub")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gitHub.sizePolicy().hasHeightForWidth())
        self.gitHub.setSizePolicy(sizePolicy)
        self.gitHub.setMaximumSize(QSize(90, 50))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(9)
        font5.setBold(True)
        self.gitHub.setFont(font5)
        self.gitHub.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(f"{FILE_PATH}/assets/icons/github.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.gitHub.setIcon(icon)
        self.gitHub.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.gitHub)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6.addWidget(self.groupBox_2)

        self.verticalLayout_6.addWidget(self.createby)

        self.verticalLayout.addWidget(self.centralwidget)

        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        about.setWindowTitle(
            QCoreApplication.translate("about", u"About", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "about", u"what do we use?", None))
        self.pythonico.setText("")
        self.pysideicon.setText("")
        self.spotifyicon.setText("")
        self.label.setText(QCoreApplication.translate(
            "about", u"Python Ver. 3.10", None))
        self.label_2.setText(QCoreApplication.translate(
            "about", u"PySide6 Ver. 6.6", None))
        self.label_3.setText(QCoreApplication.translate(
            "about", u"Spotify Web API", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("about", u"Create By", None))
        self.nickname_info.setText(
            QCoreApplication.translate("about", u"Nickname:", None))
        self.name_info.setText(
            QCoreApplication.translate("about", u"Name:", None))
        self.nickname.setText(QCoreApplication.translate(
            "about", u"SiberianCoffe", None))
        self.name.setText(QCoreApplication.translate(
            "about", u"Fernando Garrido", None))
        self.gitHub.setText(
            QCoreApplication.translate("about", u"GitHub", None))
