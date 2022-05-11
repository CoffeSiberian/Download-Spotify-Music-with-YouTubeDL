from spotifyapi import *
import os
import pathlib
import tqdm
from beautifultable import BeautifulTable
from youtubeapi import *
import time

dirt = str(pathlib.Path(__file__).parent.absolute())
conf_d = open(dirt+'/credentials.json')
load = json.load(conf_d)
cmd = load['systen_clear_cmd']
os.system(cmd)
api = spotifyPlay(load['client_id'], load['client_secret'])
yt_dl = youtube()
#5OOvspVe9Qzb9jcZrVLN9V
#0PCekXImFJ6K3EIIKDyfGH

#lobbyMenu
menu = BeautifulTable()
menu.columns.header = ['*','****** Descargar Musica de Spotify y YouTube ******'] 
menu.rows.append(['1', 'Descargar playlist Spotify'])
menu.rows.append(['2', 'Salir'])
menu.columns.alignment = BeautifulTable.ALIGN_LEFT

def fileNameCheck(str) -> str:
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

def download(url, name_file, remaining) -> None:
    os.system(cmd)
    name_file = fileNameCheck(name_file)
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

def splitURL(url) -> str:
    try:
        return url.split(sep='/')[4]
    except IndexError:
        return False

def queryYTurl(id) -> str:
    music_list = api.getTracksPlaylist(id)
    music_count = len(music_list)
    suple = 0
    for r in music_list:
        suple += 1
        name = f'{r[0]} - {r[1]}'
        url_download = yt_dl.search(name)['entries'][0]['url']
        download(url_download, name, f'[{suple} - {music_count}]')

while True:
    os.system(cmd)
    print(menu)
    textSelect = input(str('Ingresa un numero: '))
    if textSelect == '1':
        os.system(cmd)
        url = input(str('Ingresa la URL de la PlayList: '))
        validation = splitURL(url)
        if validation == False:
            print('Ingresa una URL valida')
            time.sleep(5)
        else:
            queryYTurl(validation)
    elif textSelect == '2':
        break