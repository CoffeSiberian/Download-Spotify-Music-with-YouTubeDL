from PySide6.QtWidgets import QDialog

from views.main_dowload_menu import DowloadMenuLink
from controllers.main_controller_dowload import MainWindowFormDowloadBar
from functions.jsonedit import configEdit
from functions.spotifyapi import spotifyPlay
from functions.youtubeapi import youtube

values = configEdit.getValue()
api = spotifyPlay(values[0], values[1])
yt_dl = youtube()

class MainWindowFormDowload(QDialog, DowloadMenuLink):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.dowload_menu_dowload_botton.clicked.connect(self.getUrl)
    
    def getUrl(self):
        url = self.textobox_link.text()
        getId = self.splitURL(url)
        if getId:
            self.w = MainWindowFormDowloadBar(getId, api, yt_dl, values[2])
            self.w.show()
            self.w.checkTrackOrPlayList()

        else:
            pass

    '''
    download functions
    '''
    def splitURL(self, url) -> str or bool: #get id from url playlist
        try:
            start = url.split(sep='?')[0]
            return start.split(sep='/')[4]
        except IndexError:
            return False