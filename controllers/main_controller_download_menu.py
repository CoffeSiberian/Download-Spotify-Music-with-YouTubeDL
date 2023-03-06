from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QIcon

from views.main_download_menu import downloadMenuLink
from controllers.main_controller_download import MainWindowFormdownloadBar
from functions.jsonedit import getValue
from functions.spotifyapi import spotifyPlay
from functions.youtubeapi import youtube

class MainWindowFormdownload(QDialog, downloadMenuLink):

    def __init__(self, buttonObj: str) -> None:
        super().__init__()
        self.setupUi(self)
        self.__buttonObj = buttonObj
        self.__values = getValue()
        self.__api = spotifyPlay(self.__values[0], self.__values[1])
        self.__yt_dl = youtube()
        self.setModal(True)
        self.setWindowIcon(QIcon('./assets/icons/link.png'))
        self.download_menu_download_botton.clicked.connect(self.getUrl)
        self.download_menu_cancel_botton.clicked.connect(self.close)

    def messageBox(self, title: str, lowInfo: str, level: QMessageBox.Icon, details:str) -> None:
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        self.setWindowIcon(QIcon('./assets/icons/link.png'))
        msgBox.setText(lowInfo)
        msgBox.setIcon(level)
        msgBox.setDetailedText(details)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.detailedText()
        msgBox.exec()

    def getUrl(self) -> None:
        if self.checkConfig() == False:
            return
        url = self.textobox_link.text()
        getId = self.splitURL(url)
        if getId:
            self.w = MainWindowFormdownloadBar(getId, self.__api, self.__yt_dl, 
            self.__values[2], self.__buttonObj)
            self.close()
            self.w.show()
            self.w.checkTrackOrPlayList()
        else:
            self.messageBox('Invalid URL', 'The provided url is invalid', 
            QMessageBox.Icon.Warning, 'Invalid URL')

    def checkConfig(self) -> bool:
        if self.__values[0] == '' or self.__values[1] == '':
            self.close()
            self.messageBox('Not Found API', 'Settings your API key first', 
            QMessageBox.Icon.Warning, 'Go to settings and select the "Spotify API KEY" option')
            return False

    '''
    download functions
    '''
    def splitURL(self, url: str) -> str | bool: #get id from url playlist or track
        try:
            start = url.split(sep='?')[0]
            return start.split(sep='/')[4]
        except IndexError:
            return False