from spotifyapi import *
from youtubeapi import *
from main_functions_cli import *

import os
import pathlib
from beautifultable import BeautifulTable
import time
import platform

osSystem = platform.system()

if osSystem == 'Linux' or osSystem == 'Darwin':
    cmd = 'clear'
elif osSystem == 'Windows':
    cmd = 'cls'

dirt = str(pathlib.Path(__file__).parent.absolute())
conf_d = open(dirt+'/credentials.json')
load = json.load(conf_d)
os.system(cmd)
if load['client_id'] == '' or load['client_secret'] == '':
    print('Please first write inside credentials.json your Spotify credentials (read README.md)')
    g = input(str(''))
api = spotifyPlay(load['client_id'], load['client_secret'])
yt_dl = youtube()

#lobbyMenu
menu = BeautifulTable()
menu.columns.header = ['*','****** Descargar Musica de Spotify y YouTube ******'] 
menu.rows.append(['1', 'Descargar playlist Spotify'])
menu.rows.append(['2', 'Descargar cancion Spotify'])
menu.rows.append(['3', 'Salir'])
menu.columns.alignment = BeautifulTable.ALIGN_LEFT

while True:
    os.system(cmd)
    print(menu)
    textSelect = input(str('Ingresa un numero: '))
    if textSelect == '1':
        os.system(cmd)
        print('Please make you playlist to public view for get data\n')
        url = input(str('Ingresa la URL de la PlayList: '))
        validation = main_f.splitURL(url)
        if validation == False:
            print('Ingresa una URL valida')
            time.sleep(5)
        else:
            main_f.queryYTurlPlaylist(validation, api, yt_dl, dirt, cmd)
            os.system(cmd)
            conf = input(str('Fin de la descarga. Presiona Intro '))
    elif textSelect == '2':
        os.system(cmd)
        url = input(str('Ingresa la URL de la cancion: '))
        validation = main_f.splitURL(url)
        if validation == False:
            print('Ingresa una URL valida')
            time.sleep(5)
        else:
            main_f.queryYTurlTrack(validation, api, yt_dl, dirt, cmd)
            os.system(cmd)
            conf = input(str('Fin de la descarga. Presiona Intro '))
    elif textSelect == '3':
        break