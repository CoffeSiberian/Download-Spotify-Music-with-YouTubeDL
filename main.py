from spotifyapi import *
import os
import pathlib

dirt = str(pathlib.Path(__file__).parent.absolute())
conf_d = open(dirt+'/credentials.json')
load = json.load(conf_d)

os.system(load['systen_clear_cmd'])

api = spotifyPlay(load['client_id'], load['client_secret'])
print(api.getTracksPlaylist('0PCekXImFJ6K3EIIKDyfGH'))