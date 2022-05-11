from spotifyapi import *
from youtubeapi import *
from main_functions import *

import os
import pathlib
from beautifultable import BeautifulTable
import time

dirt = str(pathlib.Path(__file__).parent.absolute())
conf_d = open(dirt+'/credentials.json')
load = json.load(conf_d)
cmd = load['systen_clear_cmd']
os.system(cmd)
api = spotifyPlay(load['client_id'], load['client_secret'])
yt_dl = youtube()

#lobbyMenu
menu = BeautifulTable()
menu.columns.header = ['*','****** Descargar Musica de Spotify y YouTube ******'] 
menu.rows.append(['1', 'Descargar playlist Spotify'])
menu.rows.append(['2', 'Salir'])
menu.columns.alignment = BeautifulTable.ALIGN_LEFT

while True:
    os.system(cmd)
    print(menu)
    textSelect = input(str('Ingresa un numero: '))
    if textSelect == '1':
        os.system(cmd)
        url = input(str('Ingresa la URL de la PlayList: '))
        validation = main_f.splitURL(url)
        if validation == False:
            print('Ingresa una URL valida')
            time.sleep(5)
        else:
            main_f.queryYTurl(validation, api, yt_dl, dirt, cmd)
    elif textSelect == '2':
        break