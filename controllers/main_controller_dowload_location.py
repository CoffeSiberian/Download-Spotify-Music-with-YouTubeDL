from PySide6.QtWidgets import QDialog

from views.main_dowload_location import DowloadLocation

class MainWindowQDialogDowloadLocation(QDialog, DowloadLocation):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)