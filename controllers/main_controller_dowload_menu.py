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
        getId = self.splitType(url)
        if getId:
            type = getId[1]
            self.w = MainWindowFormDowloadBar(getId[0], api, yt_dl, values[2], type.lower())
            self.w.show()
            self.w.checkTrackOrPlayList()
            self.close()
        else:
            pass

    '''
    download functions
    '''
    def splitURL(self, url, type) -> str: #get id from url playlist or track
        start = url.split(sep='?')[0]
        return start.split(sep='/')[4], type

    def splitType(self, url) -> str or bool: #get if the url is track or playlist
        try:
            start = url.split(sep='?')[0]
            return(self.splitURL(url, start.split(sep='/')[3]))
        except IndexError:
            return False