from PySide6.QtCore import (
    QCoreApplication, QMetaObject, QRect,
    QSize, Qt
)
from PySide6.QtGui import (
    QAction, QCursor, QFont, QIcon, QPixmap
)
from PySide6.QtWidgets import (
    QCommandLinkButton, QFrame, QHBoxLayout,
    QLabel, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget
)
from functions.path import FILE_PATH


class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 430)
        MainWindow.setMinimumSize(QSize(540, 430))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(f"{FILE_PATH}/assets/icons/exit.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionSpotify_API_KEY = QAction(MainWindow)
        self.actionSpotify_API_KEY.setObjectName(u"actionSpotify_API_KEY")
        icon2 = QIcon()
        icon2.addFile(f"{FILE_PATH}/assets/icons/spotify.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionSpotify_API_KEY.setIcon(icon2)
        self.actiondownload_Location = QAction(MainWindow)
        self.actiondownload_Location.setObjectName(u"actiondownload_Location")
        icon3 = QIcon()
        icon3.addFile(f"{FILE_PATH}/assets/icons/downloading.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actiondownload_Location.setIcon(icon3)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.centralwidget)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.background_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.background_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.icon = QLabel(self.frame)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(50, 50))
        self.icon.setPixmap(QPixmap(f"{FILE_PATH}/assets/icons/img.ico"))
        self.icon.setScaledContents(True)
        self.icon.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.icon)

        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamilies([u"Broadway"])
        font1.setPointSize(14)
        self.title.setFont(font1)
        self.title.setCursor(QCursor(Qt.ArrowCursor))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setIndent(0)

        self.horizontalLayout_3.addWidget(self.title)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4.addWidget(self.frame)

        self.options_frame = QFrame(self.background_frame)
        self.options_frame.setObjectName(u"options_frame")
        self.options_frame.setFrameShape(QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.options_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.downloadPlayList = QPushButton(self.options_frame)
        self.downloadPlayList.setObjectName(u"downloadPlayList")
        self.downloadPlayList.setMinimumSize(QSize(150, 50))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.downloadPlayList.setFont(font2)
        self.downloadPlayList.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(f"{FILE_PATH}/assets/icons/playlist.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.downloadPlayList.setIcon(icon4)
        self.downloadPlayList.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.downloadPlayList)

        self.downloadTrack = QPushButton(self.options_frame)
        self.downloadTrack.setObjectName(u"downloadTrack")
        self.downloadTrack.setMinimumSize(QSize(150, 50))
        self.downloadTrack.setFont(font2)
        self.downloadTrack.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(f"{FILE_PATH}/assets/icons/music-note.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.downloadTrack.setIcon(icon5)
        self.downloadTrack.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.downloadTrack)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addWidget(self.options_frame)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.background_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.RightToLeft)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gitHub = QCommandLinkButton(self.frame_2)
        self.gitHub.setObjectName(u"gitHub")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gitHub.sizePolicy().hasHeightForWidth())
        self.gitHub.setSizePolicy(sizePolicy)
        self.gitHub.setMaximumSize(QSize(90, 50))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.gitHub.setFont(font3)
        self.gitHub.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(f"{FILE_PATH}/assets/icons/github.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.gitHub.setIcon(icon6)
        self.gitHub.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.gitHub)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.verticalLayout.addWidget(self.background_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuConfiguration = QMenu(self.menubar)
        self.menuConfiguration.setObjectName(u"menuConfiguration")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuConfiguration.addAction(self.actionSpotify_API_KEY)
        self.menuConfiguration.addAction(self.actiondownload_Location)
        self.menuHelp.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Download Spotify Music - By: SiberianCoffe", None))
        self.actionExit.setText(
            QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSpotify_API_KEY.setText(
            QCoreApplication.translate("MainWindow", u"Spotify API KEY", None))
        self.actiondownload_Location.setText(
            QCoreApplication.translate("MainWindow", u"Download Location", None))
        self.actionHelp.setText(
            QCoreApplication.translate("MainWindow", u"About", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate(
            "MainWindow", u"Download Spotify Music", None))
        self.downloadPlayList.setText(QCoreApplication.translate(
            "MainWindow", u"Download PlayList", None))
        self.downloadTrack.setText(QCoreApplication.translate(
            "MainWindow", u"Download Track", None))
        self.gitHub.setText(QCoreApplication.translate(
            "MainWindow", u"GitHub", None))
        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", u"File", None))
        self.menuConfiguration.setTitle(
            QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate(
            "MainWindow", u"About", None))
