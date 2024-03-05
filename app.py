import sys
from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainWindowForm

if __name__ == '__main__':
    app = QApplication()
    window = MainWindowForm()
    window.show()
    sys.exit(app.exec())
