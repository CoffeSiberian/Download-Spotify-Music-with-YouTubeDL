import os
import tqdm
import requests

class main_f:
    def fileNameCheck(str) -> str: #checked incorrect character in filename
        lst = []
        strBlock = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|"]
        for r,char in enumerate(str):
            for i in strBlock:
                if char == i:
                    lst.append(r)
                    break
        list_str = list(str)
        if len(lst) == 0:
            return str
        for r in lst:
            list_str[r] = '_'
            name = ''.join(list_str)
        return name

    def download(url, nameFile, playListName, remaining, dirt) -> None:
        nameFile = main_f.fileNameCheck(nameFile)
        print(f'Downloading... {nameFile} | {remaining}')
        print('Ctrl + c to cancel')
        print('')
        headers = {'content-type':'audio/webm', 'Range': 'bytes=0-'}
        response = requests.get(url=url, headers=headers ,stream=True)
        total_size = int(response.headers.get('content-length'))
        block_size = 1024
        progress_bar = tqdm.tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(f'{dirt}/music/{playListName}/{remaining} - {nameFile}.mp3', 'wb') as file:
            for r in response.iter_content(block_size):
                progress_bar.update(len(r))
                file.write(r)
        progress_bar.close()

    def splitURL(url) -> str or bool: #get id from url playlist
        try:
            start = url.split(sep='?')[0]
            return start.split(sep='/')[4]
        except IndexError:
            return False

    def queryYTurlPlaylist(id, api, yt_dl, dirt, cmd) -> bool: #get url music from youtube_dl
        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download playlist)
        '''
        js = api.getTracksPlaylist(id)
        playlistName = main_f.fileNameCheck(js[1])
        music_list = js[0]
        main_f.createMusicFolder(dirt)
        main_f.createFolderList(dirt, playlistName)
        logRead = main_f.readLog(dirt, playlistName)
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
            os.system(cmd) #only for terminal app
            try:
                main_f.download(url_download, name, playlistName, f'[{suple}]', dirt)
                main_f.downloadLog(dirt, playlistName, suple)
                if suple == music_count:
                    return True
            except KeyboardInterrupt:
                name = main_f.fileNameCheck(name)
                main_f.removeFileMusic(dirt, playlistName, name, suple)
                return False
    
    def queryYTurlTrack(id, api, yt_dl, dirt, cmd) -> bool: #get url music from youtube_dl
        '''
        get the link of the song in yt_dlp and 
        start downloading (this function is only used to download tracks)
        '''
        js = api.getTrack(id)
        trackName = main_f.fileNameCheck(js)
        nameFolder = 'manual_track'
        main_f.createMusicFolder(dirt)
        main_f.createFolderList(dirt, nameFolder)
        url_download = yt_dl.search(trackName)['entries'][0]['url']
        os.system(cmd) #only for terminal app
        try:
            main_f.download(url_download, trackName, nameFolder, '0', dirt)
        except KeyboardInterrupt:
            name = main_f.fileNameCheck(name)
            main_f.removeFileMusic(dirt, nameFolder, name, '0')
            return False

    def downloadLog(dirt, playListName, remaining) -> None: #saved id of last track downloaded
        with open(f'{dirt}/music/{playListName}/log', 'w') as outfile:
            outfile.write(str(remaining))

    def readLog(dirt, playlistName) -> str or bool: #checks last download correct
        if os.path.exists(f'{dirt}/music/{playlistName}/log') == False:
            return False
        with open(f'{dirt}/music/{playlistName}/log') as file:
            return file.read()
    
    def createFolderList(dirt, nameFolder) -> bool:
        if os.path.exists(f'{dirt}/music/{nameFolder}') == False:
            os.mkdir(f'{dirt}/music/{nameFolder}')
        return True

    def createMusicFolder(dirt) -> bool:
        if os.path.exists(f'{dirt}/music') == False:
            os.mkdir(f'{dirt}/music')
        return True
    
    def removeFileMusic(dirt, playlistName, nameFile, remaining) -> None: #delete bad downloaded files (download not finish)
        os.remove(f'{dirt}/music/{playlistName}/[{remaining}] - {nameFile}.mp3')