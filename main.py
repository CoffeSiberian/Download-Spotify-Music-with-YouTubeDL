from spotifyapi import *
from youtubeapi import *
from main_functions import *

import pathlib

dirt = str(pathlib.Path(__file__).parent.absolute())
conf_d = open(dirt+'/credentials.json')
load = json.load(conf_d)

if load['client_id'] == '' or load['client_secret'] == '':
    print('Please first write inside credentials.json your Spotify credentials (read README.md)')
    g = input(str(''))

#objects
api = spotifyPlay(load['client_id'], load['client_secret'])
yt_dl = youtube()