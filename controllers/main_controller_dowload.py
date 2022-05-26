from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QThread

from views.main_dowload import DowloadWindow
from functions.validations import Validations

import requests
import threading

class MainWindowFormDowloadBar(QDialog, DowloadWindow):

    def __init__(self, getId, api, yt_dl, dir) -> None:
        super().__init__()
        self.setupUi(self)

        self.__getId = getId
        self.__api = api
        self.__yt_dl = yt_dl
        self.__dir = dir

    def checkTrackOrPlayList(self):
        d = threading.Thread(target=self.queryYTurlPlaylist, args=[self.__getId, self.__api, self.__yt_dl, self.__dir], name='Daemon')
        d.setDaemon
        d.start()

    def download(self, url, nameFile, playListName, remaining, dirt) -> None:
        nameFile = Validations.fileNameCheck(nameFile)
        headers = {'content-type':'audio/webm', 'Range': 'bytes=0-'}
        filename = f'{remaining} - {nameFile}.mp3'
        response = requests.get(url=url, headers=headers ,stream=True)
        total_size = int(response.headers.get('content-length'))
        block_size = 1024
        self.track_name.setText(filename)
        self.progressBardowload.setRange(0, total_size)
        with open(f'{dirt}/music/{playListName}/{filename}', 'wb') as file:
            for r in response.iter_content(block_size):
                self.progressBardowload.setValue(len(r))
                file.write(r)

    def queryYTurlPlaylist(self, id, api, yt_dl, dirt) -> bool: #get url music from youtube_dl
        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download playlist)
        '''
        js = api.getTracksPlaylist(id)
        playlistName = Validations.fileNameCheck(js[1])
        music_list = js[0]
        Validations.createMusicFolder(dirt)
        Validations.createFolderList(dirt, playlistName)
        logRead = Validations.readLog(dirt, playlistName)
        music_count = len(music_list)
        suple = 0
        if logRead == False:
            pass
        else:
            suple = int(logRead)

        for r in music_list[suple:]:
            suple += 1
            name = f'{r[0]} - {r[1]}'
            url_download = yt_dl.search(name)['entries'][0]['url']
            try:
                self.download(url_download, name, playlistName, f'[{suple}]', dirt)
                Validations.downloadLog(dirt, playlistName, suple)
                if suple == music_count:
                    return True
            except:
                name = Validations.fileNameCheck(name)
                Validations.removeFileMusic(dirt, playlistName, name, suple)
                return False

    def queryYTurlTrack(self, id, api, yt_dl, dirt) -> bool: #get url music from youtube_dl
        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download tracks)
        '''
        js = api.getTrack(id)
        trackName = Validations.fileNameCheck(js)
        nameFolder = 'manual_track'
        Validations.createMusicFolder(dirt)
        Validations.createFolderList(dirt, nameFolder)
        url_download = yt_dl.search(trackName)['entries'][0]['url']
        try:
            self.download(url_download, trackName, nameFolder, '0', dirt)
        except KeyboardInterrupt:
            name = Validations.fileNameCheck(name)
            Validations.removeFileMusic(dirt, nameFolder, name, '0')
            return False