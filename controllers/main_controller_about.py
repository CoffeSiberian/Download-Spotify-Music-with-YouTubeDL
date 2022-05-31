from PySide6.QtWidgets import QDialog

from views.main_about import About

import webbrowser

class MainWindowAbout(QDialog, About):
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.gitHub.clicked.connect(lambda: webbrowser.open('https://github.com/CoffeSiberian'))