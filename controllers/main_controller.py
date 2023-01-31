from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtCore import QStandardPaths, QDir
from PySide6.QtGui import QIcon

from views.main_Window import MainWindow

from functions.jsonedit import configEdit
import webbrowser

from controllers.main_controller_dowload_menu import MainWindowFormDowload
from controllers.main_controller_spotify_api import MainWindowQDialogApi
from controllers.main_controller_dowload_location import MainWindowQDialogDowloadLocation
from controllers.main_controller_about import MainWindowAbout

class MainWindowForm(QMainWindow, MainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.defaultPath()
        self.setWindowIcon(QIcon('./assets/icons/img.ico'))
        self.dowloadPlayList.clicked.connect(lambda: self.openDowloadPlayList(self.dowloadPlayList))
        self.dowloadTrack.clicked.connect(lambda: self.openDowloadPlayList(self.dowloadTrack))
        self.gitHub.clicked.connect(lambda: webbrowser.open(
            'https://github.com/CoffeSiberian/Download-Spotify-Music-with-YouTubeDL'))
        self.actionSpotify_API_KEY.triggered.connect(self.openSpotifyApiCfg)
        self.actionDowload_Location.triggered.connect(self.openDowloadLocation)
        self.actionHelp.triggered.connect(self.openAbout)
        self.actionExit.triggered.connect(self.close)

    def openDowloadPlayList(self, buttonObj: QPushButton):
        self.w = MainWindowFormDowload(buttonObj.objectName())
        self.w.show()
    
    def openSpotifyApiCfg(self):
        self.w=MainWindowQDialogApi()
        self.w.show()
    
    def openDowloadLocation(self):
        self.w=MainWindowQDialogDowloadLocation()
        self.w.show()
    
    def openAbout(self):
        self.w=MainWindowAbout()
        self.w.show()
    
    def defaultPath(self):
        if configEdit.getValue()[2] == '':
            dir = QDir.fromNativeSeparators(
                    QStandardPaths.writableLocation(QStandardPaths.DownloadLocation))
            configEdit.saveValue('dir', dir)