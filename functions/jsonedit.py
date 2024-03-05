from os import path
import json
from PySide6.QtCore import QStandardPaths, QDir

DOCUMENT_PATH = QDir.fromNativeSeparators(
    QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
)
FILE_NAME = 'credentials_download_music_ytdlp.json'


def saveValue(key: str, value: str) -> None:
    with open(f'{DOCUMENT_PATH}/{FILE_NAME}', 'r+') as r:
        data = json.load(r)
        data[key] = value
        r.seek(0)
        json.dump(data, r, indent=4)
        r.truncate()


def getValue() -> tuple:
    if not path.isfile(f'{DOCUMENT_PATH}/{FILE_NAME}'):
        createJsonConfig()

    data = json.load(open(f'{DOCUMENT_PATH}/{FILE_NAME}'))
    client_id = data['client_id']
    client_secret = data['client_secret']
    dir = data['dir']
    return client_id, client_secret, dir


def createJsonConfig() -> None:
    with open(f'{DOCUMENT_PATH}/{FILE_NAME}', 'w') as r:
        data = {
            "client_id": "",
            "client_secret": "",
            "dir": ""
        }
        json.dump(data, r, indent=4)
