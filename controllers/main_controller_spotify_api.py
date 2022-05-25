from PySide6.QtWidgets import QDialog, QMessageBox
import json

from views.main_spotify_api import SpotifyConfig

class MainWindowQDialogApi(QDialog, SpotifyConfig):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        jdata = self.getNowData()
        self.lineEdit_client_id.setText(jdata[0])
        self.lineEdit_client_secret.setText(jdata[1])
        self.pushButton_save.clicked.connect(self.getTextAfterPushSave)

    def getTextAfterPushSave(self):
        clientId = self.lineEdit_client_id.text()
        clientSecret = self.lineEdit_client_secret.text()
        with open('./credentials.json', 'r+') as r:
            data = json.load(r)
            data['client_id'] = clientId
            data['client_secret'] = clientSecret
            r.seek(0)
            json.dump(data, r, indent=4)
            r.truncate()
        QMessageBox.information(self, 'Saved!', 
        'Your modification was saved', 
        QMessageBox.Ok)
    
    def getNowData(self):
        data = json.load(open('./credentials.json'))
        client_id = data['client_id']
        client_secret = data['client_secret']
        return client_id, client_secret