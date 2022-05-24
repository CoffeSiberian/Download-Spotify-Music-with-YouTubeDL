from PySide6.QtWidgets import QDialog

from views.main_spotify_api import SpotifyConfig

class MainWindowQDialogApi(QDialog, SpotifyConfig):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)