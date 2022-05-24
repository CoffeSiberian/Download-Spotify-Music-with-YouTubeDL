from PySide6.QtWidgets import QMainWindow

from views.main_Window import MainWindow

from controllers.main_controller_dowload_menu import MainWindowFormDowload


class MainWindowForm(QMainWindow, MainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.dowloadPlayList.clicked.connect(self.openDowloadPlayList)
        self.dowloadTrack.clicked.connect(self.openDowloadPlayList)


    def openDowloadPlayList(self):
        self.w = MainWindowFormDowload()
        self.w.show()