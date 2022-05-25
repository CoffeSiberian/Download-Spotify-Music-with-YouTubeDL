from PySide6.QtWidgets import QDialog, QMessageBox

from functions.jsonedit import configEdit

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
        configEdit.saveValue('client_id', clientId)
        configEdit.saveValue('client_secret', clientSecret)
        QMessageBox.information(self, 'Saved!', 
        'Your modification was saved', 
        QMessageBox.Ok)
    
    def getNowData(self):
        data = configEdit.getValue()
        return data[0], data[1]