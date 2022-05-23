from PySide6.QtWidgets import QMainWindow
from views.main_Window import MainWindow

class MainWindowForm(QMainWindow, MainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)