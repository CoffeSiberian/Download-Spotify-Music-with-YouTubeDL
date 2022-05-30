from PySide6.QtWidgets import QDialog

from views.main_about import About

class MainWindowAbout(QDialog, About):
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)