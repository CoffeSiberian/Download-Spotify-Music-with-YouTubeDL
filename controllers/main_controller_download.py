from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool
from PySide6.QtGui import QCloseEvent
from PySide6.QtGui import QIcon

from views.main_download import downloadWindow
from functions.validations import (
    fileNameCheck, createFolderList, createMusicFolder,
    downloadLog, readLog, removeFileMusic
)
from functions.spotifyapi import spotifyPlay
from functions.youtubeapi import youtube
from functions.request import getData
from functions.path import FILE_PATH

import traceback
import sys
import time


class WorkerSignals(QObject):

    finished = Signal(object)
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
    notFounds = Signal(str, str, object, bool)
    iteration = Signal(str, int)


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress
        # used to generate error messages
        self.kwargs['notFound'] = self.signals.notFounds
        # used to execute code after a download iteration is finished or not
        self.kwargs['iteration'] = self.signals.iteration

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # Return the result of the processing
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit(result)  # Done


class MainWindowFormdownloadBar(QDialog, downloadWindow):

    def __init__(self, getId: str, api: spotifyPlay, yt_dl: youtube, dir: str, buttonObj: str) -> None:
        self.__status = True
        super().__init__()
        self.setupUi(self)

        self.fromButton = buttonObj
        self.getId = getId
        self.api = api
        self.yt_dl = yt_dl
        self.dir = dir
        self.modalMessageBoxStatus = False

        self.setModal(True)
        self.setWindowIcon(QIcon(f'{FILE_PATH}/assets/icons/downloading.png'))
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_cancel.clicked.connect(self.statusChange)

        self.threadpool = QThreadPool()  # we create the thread object for the download

    # Here we define the download status to false so that it is canceled
    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, data: bool) -> None:
        self.__status = data

    def statusChange(self, data=False) -> None:
        self.status = data
    #####

    # events
    # stop download process on close window event
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.__status:
            return event.ignore()
        self.statusChange(False)

    def downloadProgres(self, bits: int) -> None:  # set a progress bar status
        self.progressBardownload.setValue(bits)

    # when the download thread ends, this function is executed
    def thread_complete(self, status: bool) -> None:
        if status:
            self.messageBox(
                'Download finished', 'Your download finished', QMessageBox.Icon.Information)
        self.pushButton_exit.setEnabled(True)
        self.pushButton_cancel.setEnabled(False)
    ####

    def messageBox(self, title: str, lowInfo: str, level: QMessageBox.Icon, changeStatus: bool = False):
        self.modalMessageBoxStatus = True
        self.statusChange(changeStatus)
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setWindowIcon(
            QIcon(f'{FILE_PATH}/assets/icons/downloading.png'))
        msgBox.setText(lowInfo)
        msgBox.setIcon(level)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()
        if msgBox.clickedButton() == msgBox.buttons()[0]:
            self.modalMessageBoxStatus = False

    def changeStatusdownload(self, filename: str, total_size: int):
        self.track_name.setText(filename)
        self.progressBardownload.setRange(0, total_size)
        self.pushButton_cancel.setEnabled(True)

    # We create the worker so that the download can proceed
    def checkTrackOrPlayList(self) -> None:
        # Pass the function to execute
        if self.fromButton == 'downloadPlayList':
            worker = Worker(self.queryYTurlPlaylist)
        elif self.fromButton == 'downloadTrack':
            worker = Worker(self.queryYTurlTrack)
        # worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.downloadProgres)
        worker.signals.notFounds.connect(self.messageBox)
        worker.signals.iteration.connect(self.changeStatusdownload)
        # Execute
        self.threadpool.start(worker)

    def download(
            self, url: str, nameFile: str, playListName: str, remaining: str, dirt: str,
            progress_callback: WorkerSignals, iteration: WorkerSignals) -> bool:

        nameFile = fileNameCheck(nameFile)
        filename = f'{remaining} - {nameFile}.mp3'

        # only get file headers info
        response = getData(url=url, stream=True)
        total_size = int(response.headers.get('content-length'))
        ############################

        # range use to more speed download
        headers = {'Accept': '*/*', 'Range': f'bytes=0-{total_size}'}
        getFileUrl = f'{url}&range=0-{total_size}'
        getFile = getData(url=getFileUrl, headers=headers, stream=True)
        #################################

        block_size = 1024
        downloadedSize = 0
        iteration.emit(filename, total_size)
        with open(f'{dirt}/music/{playListName}/{filename}', 'wb') as file:
            for r in getFile.iter_content(block_size):
                if not self.status:
                    return False
                downloadedSize += len(r)
                progress_callback.emit(downloadedSize)
                file.write(r)
        if total_size == downloadedSize:
            return True
        else:
            return False

    def queryYTurlPlaylist(
            self, progress_callback: WorkerSignals, notFound: WorkerSignals, iteration: WorkerSignals) -> bool:
        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download playlist)
        '''
        js = self.api.getTracksPlaylist(self.getId)
        if js[1] != 200:
            notFound.emit(str(js[1]), js[2], QMessageBox.Icon.Warning, False)
            return False
        playlistName = fileNameCheck(js[2])
        music_list = js[0]
        createMusicFolder(self.dir)
        createFolderList(self.dir, playlistName)
        logRead = readLog(self.dir, playlistName)
        music_count = len(music_list)
        suple = 0
        if logRead != False:
            suple = int(logRead)
            if music_count == suple:
                notFound.emit(
                    "Attention",
                    '''
You had already finished downloading this playlist.

If it's an error, delete the folder and try again.
''',
                    QMessageBox.Icon.Warning,
                    False)
                return False

        for r in music_list[suple:]:
            if self.status == False:
                break
            suple += 1
            name = f'{r[0]} - {r[1]}'
            search_yt, status_yt = self.yt_dl.search(name)

            if status_yt == 200:
                url_download = search_yt['url']
                download = self.download(
                    url_download, name, playlistName, f'[{suple}]', self.dir, progress_callback, iteration)
                if not download:
                    notFound.emit("400", "Connection issues",
                                  QMessageBox.Icon.Warning, False)
                    removeFileMusic(self.dir, playlistName, name, suple)
                else:
                    downloadLog(self.dir, playlistName, suple)
            else:
                notFound.emit(str(status_yt), search_yt
                              ["error"], QMessageBox.Icon.Warning, True)
                downloadLog(self.dir, playlistName, suple)
                while self.modalMessageBoxStatus:
                    time.sleep(0.5)

            if suple == music_count:
                self.statusChange(False)
                return True
        return False

    def queryYTurlTrack(
            self, progress_callback: WorkerSignals, notFound: WorkerSignals, iteration: WorkerSignals) -> bool:
        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download tracks)
        '''
        track, status, error_msj = self.api.getTrack(self.getId)
        if status != 200:
            notFound.emit(str(status), error_msj,
                          QMessageBox.Icon.Warning, False)
            return False

        trackName = fileNameCheck(track)
        nameFolder = 'manual_track'
        createMusicFolder(self.dir)
        createFolderList(self.dir, nameFolder)
        search_yt, status_yt = self.yt_dl.search(trackName)

        if status_yt == 200:
            url_download = search_yt['url']
            download = self.download(
                url_download, trackName, nameFolder, '[0]', self.dir, progress_callback, iteration)

            if not download:
                notFound.emit("400", "Connection issues",
                              QMessageBox.Icon.Warning, False)
                removeFileMusic(self.dir, nameFolder, trackName, '0')
                self.statusChange(False)
                return False
        else:
            notFound.emit(str(status_yt), search_yt
                          ["error"], QMessageBox.Icon.Warning, False)
            return False
        self.statusChange(False)
        return True
