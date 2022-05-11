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

    def download(url, name_file, remaining, dirt) -> None:
        name_file = main_f.fileNameCheck(name_file)
        print(f'Downloading... {name_file} | {remaining}')
        print('')
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length'))
        block_size = 1024
        progress_bar = tqdm.tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(f'{dirt}/music/{name_file} - {remaining}.mp3', 'wb') as file:
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

    def queryYTurl(id, api, yt_dl, dirt, cmd) -> None: #get url music from youtube_dl
        music_list = api.getTracksPlaylist(id)
        music_count = len(music_list)
        suple = 0
        for r in music_list:
            suple += 1
            name = f'{r[0]} - {r[1]}'
            url_download = yt_dl.search(name)['entries'][0]['url']
            os.system(cmd) #only for terminal app
            main_f.download(url_download, name, f'[{suple} - {music_count}]', dirt)