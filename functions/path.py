import sys
from os import path


def resource_path() -> str:
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return base_path


FILE_PATH = resource_path()
