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
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length'))
        block_size = 1024
        progress_bar = tqdm.tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(f'{dirt}/music/{playListName}/{nameFile} - {remaining}.mp3', 'wb') as file:
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

    def queryYTurl(id, api, yt_dl, dirt, cmd) -> bool: #get url music from youtube_dl
        js = api.getTracksPlaylist(id)
        playListName = main_f.fileNameCheck(js[1])
        music_list = js[0]
        main_f.createMusicFolder(dirt)
        main_f.createFolderList(dirt, playListName)
        music_count = len(music_list)
        suple = 0
        for r in music_list:
            suple += 1
            name = f'{r[0]} - {r[1]}'
            url_download = yt_dl.search(name)['entries'][0]['url']
            os.system(cmd) #only for terminal app
            try:
                main_f.download(url_download, name, playListName, f'[{suple} - {music_count}]', dirt)
                if suple == music_count:
                    return True
            except KeyboardInterrupt:
                return False
    
    def createDownloadLog():
        pass

    def createFolderList(dirt, nameFolder) -> bool:
        if os.path.exists(f'{dirt}/music/{nameFolder}') == False:
            os.mkdir(f'{dirt}/music/{nameFolder}')
        return True

    def createMusicFolder(dirt) -> bool:
        if os.path.exists(f'{dirt}/music') == False:
            os.mkdir(f'{dirt}/music')
        return True
    
    def removeMusic(name) -> bool:
        pass