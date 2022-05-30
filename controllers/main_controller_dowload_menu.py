from PySide6.QtWidgets import QDialog

from views.main_dowload_menu import DowloadMenuLink
from controllers.main_controller_dowload import MainWindowFormDowloadBar
from functions.jsonedit import configEdit
from functions.spotifyapi import spotifyPlay
from functions.youtubeapi import youtube

class MainWindowFormDowload(QDialog, DowloadMenuLink):

    def __init__(self, buttonObj) -> None:
        super().__init__()
        self.__buttonObj = buttonObj
        self.setupUi(self)
        self.__values = configEdit.getValue()
        self.__api = spotifyPlay(self.__values[0], self.__values[1])
        self.__yt_dl = youtube()
        self.dowload_menu_dowload_botton.clicked.connect(self.getUrl)
        self.dowload_menu_cancel_botton.clicked.connect(self.close)
    
    def getUrl(self):
        url = self.textobox_link.text()
        getId = self.splitURL(url)
        if getId:
            self.w = MainWindowFormDowloadBar(getId, self.__api, self.__yt_dl, self.__values[2], self.__buttonObj)
            self.w.show()
            self.w.checkTrackOrPlayList()
            self.close()
        else:
            pass

    '''
    download functions
    '''
    def splitURL(self, url) -> str: #get id from url playlist or track
        try:
            start = url.split(sep='?')[0]
            return start.split(sep='/')[4]
        except IndexError:
            return False