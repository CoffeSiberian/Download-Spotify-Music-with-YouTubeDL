from PySide6.QtWidgets import QWidget

from views.main_dowload_menu import DowloadMenuLink

class MainWindowFormDowload(QWidget, DowloadMenuLink):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)