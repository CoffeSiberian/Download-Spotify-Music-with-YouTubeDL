from PySide6.QtWidgets import QDialog

from views.main_dowload_menu import DowloadMenuLink
from functions.validations import Validations
from functions.spotifyapi import spotifyPlay
from functions.youtubeapi import youtube

import requests
import json

conf_d = open('./credentials.json')
load = json.load(conf_d)
api = spotifyPlay(load['client_id'], load['client_secret'])
yt_dl = youtube()

class MainWindowFormDowload(QDialog, DowloadMenuLink):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
    
    def getUrl(self):
        self.textobox_link.text

    '''
    download functions
    '''
    def download(self, url, nameFile, playListName, remaining, dirt) -> None:
        nameFile = Validations.fileNameCheck(nameFile)
        headers = {'content-type':'audio/webm', 'Range': 'bytes=0-'}
        response = requests.get(url=url, headers=headers ,stream=True)
        total_size = int(response.headers.get('content-length'))
        block_size = 1024
        with open(f'{dirt}/music/{playListName}/{remaining} - {nameFile}.mp3', 'wb') as file:
            for r in response.iter_content(block_size):
                file.write(r)

    def splitURL(self, url) -> str or bool: #get id from url playlist
        try:
            start = url.split(sep='?')[0]
            return start.split(sep='/')[4]
        except IndexError:
            return False

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
            except KeyboardInterrupt:
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