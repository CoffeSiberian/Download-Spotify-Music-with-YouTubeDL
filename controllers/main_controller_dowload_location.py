from PySide6.QtWidgets import QDialog, QStyle, QLineEdit, QFileDialog, QMessageBox
from PySide6.QtCore import QStandardPaths, QDir
from PySide6.QtGui import QIcon

from functions.jsonedit import saveValue, getValue

from views.main_dowload_location import DowloadLocation

class MainWindowQDialogDowloadLocation(QDialog, DowloadLocation):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        dirt = self.getPath()
        self.setModal(True)
        self.setWindowIcon(QIcon('./assets/icons/downloading.png'))
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
        saveValue('dir', dir)
        QMessageBox.information(self, 'Saved!', 
        'Your modification was saved', 
        QMessageBox.Ok)
        self.close()
    
    def getNowData(self):
        data = getValue()
        return data[2]