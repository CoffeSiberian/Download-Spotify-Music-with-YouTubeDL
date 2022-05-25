from PySide6.QtWidgets import QDialog, QStyle, QLineEdit, QFileDialog, QMessageBox
from PySide6.QtCore import QStandardPaths, QDir

import json

from views.main_dowload_location import DowloadLocation

class MainWindowQDialogDowloadLocation(QDialog, DowloadLocation):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        dirt = self.getPath()
        self.lineEdit_location.setText(dirt)

        self._open_folder_action = self.lineEdit_location.addAction(
            qApp.style().standardIcon(QStyle.SP_DirOpenIcon), QLineEdit.TrailingPosition
        )

        self._open_folder_action.triggered.connect(self.on_open_folder)

        self.pushButton_save.clicked.connect(self.getTextAfterPushSave)

    def on_open_folder(self):

        dir_path = QFileDialog.getExistingDirectory(
            self, "Open Directory", QDir.homePath(), QFileDialog.ShowDirsOnly
        )

        if dir_path:
            dest_dir = QDir(dir_path)
            self.lineEdit_location.setText(QDir.fromNativeSeparators(dest_dir.path()))
    
    def getPath(self):
        if self.getNowData() == '':
            return QDir.fromNativeSeparators(
                    QStandardPaths.writableLocation(QStandardPaths.DownloadLocation))
        return self.getNowData()

    def getTextAfterPushSave(self):
        dir = self.lineEdit_location.text()
        with open('./credentials.json', 'r+') as r:
            data = json.load(r)
            data['dir'] = dir
            r.seek(0)
            json.dump(data, r, indent=4)
            r.truncate()
        QMessageBox.information(self, 'Saved!', 
        'Your modification was saved', 
        QMessageBox.Ok)
    
    def getNowData(self):
        data = json.load(open('./credentials.json'))
        client_id = data['dir']
        return client_id