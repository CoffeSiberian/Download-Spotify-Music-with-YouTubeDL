from PySide6.QtWidgets import QDialog

from views.main_dowload_menu import DowloadMenuLink

class MainWindowFormDowload(QDialog, DowloadMenuLink):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)