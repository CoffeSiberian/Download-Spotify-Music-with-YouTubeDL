from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool

from views.main_dowload import DowloadWindow
from functions.validations import Validations

import requests
import traceback
import sys

class WorkerSignals(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

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
            self.signals.finished.emit()  # Done

class MainWindowFormDowloadBar(QDialog, DowloadWindow):

    def __init__(self, getId, api, yt_dl, dir) -> None:
        self.__status = True
        super().__init__()
        self.setupUi(self)

        self.__getId = getId
        self.__api = api
        self.__yt_dl = yt_dl
        self.__dir = dir

        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_cancel.clicked.connect(self.statusChange)

        self.threadpool = QThreadPool() #we create the thread object for the download
    
    #Here we define the download status to false so that it is canceled
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, data):
        self.__status = data
    def statusChange(self, data=False):
        self.status = data
    #####

    def checkTrackOrPlayList(self) -> None: #We create the worker so that the download can proceed
        # Pass the function to execute
        worker = Worker(self.queryYTurlPlaylist, self.__getId, self.__api, self.__yt_dl, self.__dir)
        #worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.dowloadProgres)
        # Execute
        self.threadpool.start(worker)

    def download(self, url, nameFile, playListName, remaining, dirt, progress_callback) -> None:
        nameFile = Validations.fileNameCheck(nameFile)
        headers = {'content-type':'audio/webm', 'Range': 'bytes=0-'}
        filename = f'{remaining} - {nameFile}.mp3'
        response = requests.get(url=url, headers=headers ,stream=True)
        total_size = int(response.headers.get('content-length'))
        block_size = 1024
        dowloadedSize = 0
        self.track_name.setText(filename)
        self.progressBardowload.setRange(0, total_size)
        with open(f'{dirt}/music/{playListName}/{filename}', 'wb') as file:
            for r in response.iter_content(block_size):
                if self.__status == False:
                    break
                dowloadedSize+=len(r)
                progress_callback.emit(dowloadedSize)
                file.write(r)

    def dowloadProgres(self, bits) -> None: #set a progress bar status
        self.progressBardowload.setValue(bits)

    def thread_complete(self) -> None:
        QMessageBox.information(self, 'Download finished', 
        'Your download finished', 
        QMessageBox.Ok)
        self.pushButton_exit.setEnabled(True)
        if self.__status == False:
            self.pushButton_cancel.setEnabled(False)

    def queryYTurlPlaylist(self, id, api, yt_dl, dirt, progress_callback) -> bool: #get url music from youtube_dl
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
        self.pushButton_cancel.setEnabled(True)
        music_count = len(music_list)
        suple = 0
        if logRead == False:
            pass
        else:
            suple = int(logRead)

        for r in music_list[suple:]:
            if self.__status == False:
                break
            suple += 1
            name = f'{r[0]} - {r[1]}'
            url_download = yt_dl.search(name)['entries'][0]['url']
            try:
                self.download(url_download, name, playlistName, f'[{suple}]', dirt, progress_callback)
                Validations.downloadLog(dirt, playlistName, suple)
                if suple == music_count:
                    self.pushButton_cancel.setEnabled(False)
                    return True
            except:
                name = Validations.fileNameCheck(name)
                Validations.removeFileMusic(dirt, playlistName, name, suple)
                self.pushButton_cancel.setEnabled(False)
                return False

    def queryYTurlTrack(self, id, api, yt_dl, dirt, progress_callback) -> bool: #get url music from youtube_dl
        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download tracks)
        '''
        js = api.getTrack(id)
        trackName = Validations.fileNameCheck(js)
        nameFolder = 'manual_track'
        Validations.createMusicFolder(dirt)
        Validations.createFolderList(dirt, nameFolder)
        self.pushButton_cancel.setEnabled(True)
        url_download = yt_dl.search(trackName)['entries'][0]['url']
        try:
            self.download(url_download, trackName, nameFolder, '0', dirt, progress_callback)
            self.pushButton_cancel.setEnabled(False)
        except KeyboardInterrupt:
            name = Validations.fileNameCheck(name)
            Validations.removeFileMusic(dirt, nameFolder, name, '0')
            self.pushButton_cancel.setEnabled(False)
            return False