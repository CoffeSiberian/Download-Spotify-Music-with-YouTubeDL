from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QIcon

from functions.jsonedit import saveValue, getValue

from views.main_spotify_api import SpotifyConfig

import webbrowser


class MainWindowQDialogApi(QDialog, SpotifyConfig):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        jdata = self.getNowData()
        self.lineEdit_client_id.setText(jdata[0])
        self.lineEdit_client_secret.setText(jdata[1])
        self.setModal(True)
        self.setWindowIcon(QIcon('./assets/icons/spotify.png'))
        self.pushButton_save.clicked.connect(self.getTextAfterPushSave)
        self.gitHub.clicked.connect(lambda: webbrowser.open(
            'https://github.com/CoffeSiberian/Download-Spotify-Music-with-YouTubeDL/blob/master/README.md'))

    def getTextAfterPushSave(self):
        clientId = self.lineEdit_client_id.text()
        clientSecret = self.lineEdit_client_secret.text()
        saveValue('client_id', clientId)
        saveValue('client_secret', clientSecret)
        QMessageBox.information(self, 'Saved!',
                                'Your modification was saved',
                                QMessageBox.Ok)
        self.close()

    def getNowData(self):
        data = getValue()
        return data[0], data[1]
