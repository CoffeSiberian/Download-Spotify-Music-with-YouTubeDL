import imp
from spotifyapi import *
import os
import pathlib
import tqdm
from beautifultable import BeautifulTable
from youtubeapi import *

dirt = str(pathlib.Path(__file__).parent.absolute())
conf_d = open(dirt+'/credentials.json')
load = json.load(conf_d)
os.system(load['systen_clear_cmd'])
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

def download(url, name_file) -> None:
    response = requests.get(url, stream=True)
    total_size= int(response.headers.get('content-length'))
    block_size = 1024
    progress_bar = tqdm.tqdm(total=total_size, unit='iB', unit_scale=True)
    with open('{name_file}.mp3', 'wb') as file:
        for r in response.iter_content(block_size):
            progress_bar.update(len(r))
            file.write(r)
    progress_bar.close()
    if total_size != 0 and progress_bar.n != total_size:
        print("ERROR, something went wrong")

def splitURL(url) -> str:
    return url.split(sep='/')[4]

def queryYTurl(id) -> str:
    for r in api.getTracksPlaylist(id):
        name = '{r[0]} - {r[1]}'
        url_download = yt_dl.search(name)[0]['url']
        download(url_download, name)

while True:
    buttonSelect = input(str('Ingresa un numero: '))
    if buttonSelect == 1:
        pass
    elif buttonSelect == 2:
        break