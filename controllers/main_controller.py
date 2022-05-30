from PySide6.QtWidgets import QMainWindow

from views.main_Window import MainWindow

from controllers.main_controller_dowload_menu import MainWindowFormDowload
from controllers.main_controller_spotify_api import MainWindowQDialogApi
from controllers.main_controller_dowload_location import MainWindowQDialogDowloadLocation


class MainWindowForm(QMainWindow, MainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.dowloadPlayList.clicked.connect(lambda: self.openDowloadPlayList(self.dowloadPlayList))
        self.dowloadTrack.clicked.connect(lambda: self.openDowloadPlayList(self.dowloadTrack))
        self.actionSpotify_API_KEY.triggered.connect(self.openSpotifyApiCfg)
        self.actionDowload_Location.triggered.connect(self.openDowloadLocation)
        self.actionExit.triggered.connect(self.close)

    def openDowloadPlayList(self, buttonObj):
        self.w = MainWindowFormDowload(buttonObj.objectName())
        self.w.show()
    
    def openSpotifyApiCfg(self):
        self.w=MainWindowQDialogApi()
        self.w.show()
    
    def openDowloadLocation(self):
        self.w=MainWindowQDialogDowloadLocation()
        self.w.show()