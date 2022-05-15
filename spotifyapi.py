import requests
from requests.structures import CaseInsensitiveDict
import base64
import json

class spotifyPlay:
    def __init__(self, clienId, clienSecret) -> None:
        self.__clienId = clienId
        self.__clienSecret = clienSecret
    
    @property
    def clienId(self) -> str:
        return self.__clienId

    @property
    def clienSecret(self) -> str:
        return self.__clienSecret

    def getBearer(self) -> str: #code to access data (the code is temporary)
        concat = f'{self.clienId}:{self.clienSecret}'
        encoded = base64.b64encode(bytes(concat, "utf-8")).decode(("utf-8"))
        url = "https://accounts.spotify.com/api/token"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Basic {encoded}"
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = "grant_type=client_credentials"
        resp = requests.post(url, headers=headers, data=data)
        jsonLoads = json.loads(resp.content.decode("utf-8"))
        return jsonLoads['access_token']

    def getPlaylist(self, id) -> dict: #return dict playlist
        url = f'https://api.spotify.com/v1/playlists/{id}'
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.getBearer()}"
        headers["Content-Type"] = "application/json"
        resp = requests.get(url, headers=headers)
        return resp.content
    
    def getTracksPlaylist(self, id) -> list: #returns an list with song name and author [namePlayList][name, author]
        get_json = json.loads(self.getPlaylist(id))
        try:
            playlist = get_json['tracks']
        except KeyError:
            return [get_json['error']['status'], get_json['error']['message']]
        rescueTracks = []
        iterator = 0
        while True:
            if iterator == 100:
                if playlist['next'] == None:
                    break
                offsetUp = str(playlist['offset']+100)
                playlist = json.loads(self.getPlaylist(f'{id}/tracks?offset={offsetUp}&limit=100'))
                iterator = 0
            try:
                name = playlist['items'][iterator]['track']['name']
                artists = playlist['items'][iterator]['track']['artists'][0]['name']
                rescueTracks.append([name, artists])
                iterator += 1
            except IndexError:
                break
        return rescueTracks, get_json['name']
    
    def getTrack(self, id) -> str:
        url = f'https://api.spotify.com/v1/tracks/{id}'
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.getBearer()}"
        headers["Content-Type"] = "application/json"
        resp = requests.get(url, headers=headers)
        get_json = json.loads(resp.content)
        name = get_json['name']
        artists = get_json['artists'][0]['name']
        rescueTrack = f'{name} - {artists}'
        return rescueTrack