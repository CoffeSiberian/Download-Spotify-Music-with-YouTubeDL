import requests
from requests.structures import CaseInsensitiveDict
import base64
import json

class spotifyPlay:
    def __init__(self, clienId: str, clienSecret: str) -> None:
        self.__clienId = clienId
        self.__clienSecret = clienSecret
    
    @property
    def clienId(self) -> str:
        return self.__clienId

    @property
    def clienSecret(self) -> str:
        return self.__clienSecret

    def getBearer(self) -> tuple[str, int]: #code to access data (the code is temporary)
        concat = f'{self.clienId}:{self.clienSecret}'
        encoded = base64.b64encode(bytes(concat, "utf-8")).decode(("utf-8"))
        url = "https://accounts.spotify.com/api/token"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Basic {encoded}"
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = "grant_type=client_credentials"
        resp = requests.post(url, headers=headers, data=data)
        jsonLoads = json.loads(resp.content.decode("utf-8"))
        if resp.status_code != 200:
            return jsonLoads['error'], resp.status_code
        return jsonLoads['access_token'], resp.status_code

    def getPlaylist(self, id:str) -> tuple[dict, int]: #return dict playlist
        bearer = self.getBearer()
        if bearer[1] != 200:
            return bearer
        url = f'https://api.spotify.com/v1/playlists/{id}'
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {bearer[0]}"
        headers["Content-Type"] = "application/json"
        resp = requests.get(url, headers=headers)
        return resp.content.decode("utf-8"), resp.status_code
    
    def getTracksPlaylist(self, id:str) -> tuple[None | list, int, str]: #returns an list with song name and author [namePlayList][name, author]
        info = self.getPlaylist(id)
        if info[1] != 200: return None, info[1], self.errorMsj(info[0])

        infoConten = json.loads(info[0])
        playlist = infoConten['tracks']
        rescueTracks = []
        iterator = 0
        while True:
            if iterator == 100:
                if playlist['next'] == None:
                    break
                offsetUp = str(playlist['offset']+100)
                infoNext = self.getPlaylist(f'{id}/tracks?offset={offsetUp}&limit=100')
                if infoNext[1] != 200:
                    return None, infoNext[1], infoNext["error"]['message']

                playlist = json.loads(infoNext[0])
                iterator = 0
            try:
                name = playlist['items'][iterator]['track']['name']
                artists = playlist['items'][iterator]['track']['artists'][0]['name']
                rescueTracks.append([name, artists])
                iterator += 1
            except IndexError:
                break
            except TypeError:
                iterator += 1
        return rescueTracks, info[1], infoConten['name']
    
    def getTrack(self, id:str) -> tuple[str | None, int, str | None]:
        bearer = self.getBearer()
        if bearer[1] != 200:
            return None, bearer[1], self.errorMsj(bearer[0])

        url = f'https://api.spotify.com/v1/tracks/{id}'
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {bearer[0]}"
        headers["Content-Type"] = "application/json"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            return  None, resp.status_code, self.errorMsj(resp.content.decode("utf-8"))

        get_json = json.loads(resp.content)
        name = get_json['name']
        artists = get_json['artists'][0]['name']
        rescueTrack = f'{name} - {artists}'
        return rescueTrack, resp.status_code, None
    
    def errorMsj(self, error: str) -> str:
        msj = None
        try:
            loaded = json.loads(error)
            msj = loaded["error"]['message']
        except:
            try:
                loaded = json.loads(error)
                msj = loaded["error"]
            except: msj = error
        return msj