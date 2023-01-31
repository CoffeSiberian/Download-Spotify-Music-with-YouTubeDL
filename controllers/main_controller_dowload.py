from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool
from PySide6.QtGui import QCloseEvent
from PySide6.QtGui import QIcon, QIconEngine

from views.main_dowload import DowloadWindow
from functions.validations import Validations
from functions.spotifyapi import spotifyPlay
from functions.youtubeapi import youtube

import requests
import traceback
import sys

class WorkerSignals(QObject):

    finished = Signal(object)
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
    notFounds = Signal(str, str, object)
    iteration = Signal(str, int)

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress
        self.kwargs['notFound'] = self.signals.notFounds #used to generate error messages
        self.kwargs['iteration'] = self.signals.iteration #used to execute code after a download iteration is finished or not

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit(result)  # Done

class MainWindowFormDowloadBar(QDialog, DowloadWindow):

    def __init__(self, getId: str, api: spotifyPlay, yt_dl: youtube, dir: str, buttonObj: str) -> None:
        self.__status = True
        super().__init__()
        self.setupUi(self)

        self.__fromButton = buttonObj
        self.__getId = getId
        self.__api = api
        self.__yt_dl = yt_dl
        self.__dir = dir

        self.setModal(True)
        self.setWindowIcon(QIcon('./assets/icons/downloading.png'))
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_cancel.clicked.connect(self.statusChange)

        self.threadpool = QThreadPool() #we create the thread object for the download
    
    #Here we define the download status to false so that it is canceled
    @property
    def status(self) -> bool:
        return self.__status
    @status.setter
    def status(self, data: bool) -> None:
        self.__status = data
    def statusChange(self, data=False) -> None:
        self.status = data
    #####

    #events
    def closeEvent(self, event: QCloseEvent) -> None: #stop download process on close window event
        if self.__status:
            return event.ignore()
        self.statusChange(False)

    def dowloadProgres(self, bits) -> None: #set a progress bar status
        self.progressBardowload.setValue(bits)

    def thread_complete(self, status: bool) -> None: #when the download thread ends, this function is executed
        if status:
            self.messageBox('Download finished', 'Your download finished', QMessageBox.Icon.Information)
        self.pushButton_exit.setEnabled(True)
        self.pushButton_cancel.setEnabled(False)
    ####

    def messageBox(self, title: str, lowInfo: str, level: QMessageBox.Icon):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setWindowIcon(QIcon('./assets/icons/downloading.png'))
        msgBox.setText(lowInfo)
        msgBox.setIcon(level)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.statusChange(False)
        msgBox.exec()
    
    def changeStatusDowload(self, filename, total_size):
        self.track_name.setText(filename)
        self.progressBardowload.setRange(0, total_size)
        self.pushButton_cancel.setEnabled(True)

    def checkTrackOrPlayList(self) -> None: #We create the worker so that the download can proceed
        # Pass the function to execute
        if self.__fromButton == 'dowloadPlayList':
            worker = Worker(self.queryYTurlPlaylist, self.__getId, self.__api, self.__yt_dl, self.__dir)
        elif self.__fromButton == 'dowloadTrack':
            worker = Worker(self.queryYTurlTrack, self.__getId, self.__api, self.__yt_dl, self.__dir)
        #worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.dowloadProgres)
        worker.signals.notFounds.connect(self.messageBox)
        worker.signals.iteration.connect(self.changeStatusDowload)
        # Execute
        self.threadpool.start(worker)

    def download(
        self, url: str, nameFile: str, playListName: str, remaining: str, dirt: str, 
        progress_callback: WorkerSignals, iteration: WorkerSignals) -> bool:

        nameFile = Validations.fileNameCheck(nameFile)
        headers = {'content-type':'audio/webm', 'Range': 'bytes=0-'}
        filename = f'{remaining} - {nameFile}.mp3'
        response = requests.get(url=url, headers=headers , stream=True)
        total_size = int(response.headers.get('content-length'))
        block_size = 1024
        dowloadedSize = 0
        iteration.emit(filename, total_size)
        with open(f'{dirt}/music/{playListName}/{filename}', 'wb') as file:
            for r in response.iter_content(block_size):
                if not self.status: return False
                dowloadedSize+=len(r)
                progress_callback.emit(dowloadedSize)
                file.write(r)
        return True

    def queryYTurlPlaylist(
        self, id: str, api: spotifyPlay, yt_dl: youtube, dirt: str, 
        progress_callback: WorkerSignals, notFound: WorkerSignals, iteration: WorkerSignals) -> bool:

        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download playlist)
        '''
        js = api.getTracksPlaylist(id)
        if js[1] != 200:
            print(js[2])
            notFound.emit(str(js[1]), js[2], QMessageBox.Icon.Warning)
            return False
        playlistName = Validations.fileNameCheck(js[2])
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
            if self.status == False:
                break
            suple += 1
            name = f'{r[0]} - {r[1]}'
            url_download = yt_dl.search(name)['entries'][0]['url']
            try:
                if self.download(url_download, name, playlistName, f'[{suple}]', dirt, progress_callback, iteration):
                    Validations.downloadLog(dirt, playlistName, suple)
                else:
                    Validations.removeFileMusic(dirt, playlistName, name, suple)
                if suple == music_count:
                    self.statusChange(False)
                    return True
            except:
                name = Validations.fileNameCheck(name)
                Validations.removeFileMusic(dirt, playlistName, name, suple)
                return False

    def queryYTurlTrack(
        self, id: str, api: spotifyPlay, yt_dl: youtube, dirt: str, 
        progress_callback: WorkerSignals, notFound: WorkerSignals, iteration: WorkerSignals) -> bool:
        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download tracks)
        '''
        js = api.getTrack(id)
        if js[1] != 200:
            notFound.emit(str(js[1]), js[2], QMessageBox.Icon.Warning)
            return False
        trackName = Validations.fileNameCheck(js[0])
        nameFolder = 'manual_track'
        Validations.createMusicFolder(dirt)
        Validations.createFolderList(dirt, nameFolder)
        url_download = yt_dl.search(trackName)['entries'][0]['url']
        try:
            self.download(url_download, trackName, nameFolder, '0', dirt, progress_callback, iteration)
            self.statusChange(False)
            return True
        except:
            name = Validations.fileNameCheck(name)
            Validations.removeFileMusic(dirt, nameFolder, name, '0')
            return False