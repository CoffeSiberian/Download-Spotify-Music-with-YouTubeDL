from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtCore import QStandardPaths, QDir
from PySide6.QtGui import QIcon

from views.main_Window import MainWindow

from functions.jsonedit import getValue, saveValue
import webbrowser

from controllers.main_controller_download_menu import MainWindowFormdownload
from controllers.main_controller_spotify_api import MainWindowQDialogApi
from controllers.main_controller_download_location import MainWindowQDialogdownloadLocation
from controllers.main_controller_about import MainWindowAbout
from functions.path import FILE_PATH


class MainWindowForm(QMainWindow, MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.defaultPath()
        self.setWindowIcon(QIcon(f'{FILE_PATH}/assets/icons/img.ico'))
        self.downloadPlayList.clicked.connect(
            lambda: self.opendownloadPlayList(self.downloadPlayList))
        self.downloadTrack.clicked.connect(
            lambda: self.opendownloadPlayList(self.downloadTrack))
        self.gitHub.clicked.connect(lambda: webbrowser.open(
            'https://github.com/CoffeSiberian/Download-Spotify-Music-with-YouTubeDL'))
        self.actionSpotify_API_KEY.triggered.connect(self.openSpotifyApiCfg)
        self.actiondownload_Location.triggered.connect(
            self.opendownloadLocation)
        self.actionHelp.triggered.connect(self.openAbout)
        self.actionExit.triggered.connect(self.close)

    def opendownloadPlayList(self, buttonObj: QPushButton):
        self.w = MainWindowFormdownload(buttonObj.objectName())
        self.w.show()

    def openSpotifyApiCfg(self):
        self.w = MainWindowQDialogApi()
        self.w.show()

    def opendownloadLocation(self):
        self.w = MainWindowQDialogdownloadLocation()
        self.w.show()

    def openAbout(self):
        self.w = MainWindowAbout()
        self.w.show()

    def defaultPath(self):
        if getValue()[2] == '':
            dir = QDir.fromNativeSeparators(
                QStandardPaths.writableLocation(QStandardPaths.DownloadLocation))
            saveValue('dir', dir)
