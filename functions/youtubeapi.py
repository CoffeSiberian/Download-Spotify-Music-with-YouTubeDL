from yt_dlp import YoutubeDL

class youtube:
    def __init__(self) -> None:
        self.ytdl_options = {
        'format': 'ba',
        'no_warnings': True,
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'logtostderr': False,
        'windows-filenames': True,
        'quiet': True
        }
        self.ytdl = YoutubeDL(self.ytdl_options)

    def findVideoInfoURL(self, url: str) -> tuple[dict, int]:
        '''
        Returns the video and an http code
        '''
        vidinfo = self.ytdl.extract_info(url, download=False)
        if vidinfo == None: return {"error":"Connection or search failed"}, 400
        return vidinfo, 200
    
    def search(self, find: str) -> tuple[dict, int]:
        '''
        Returns the first search result and an http code
        '''
        vidinfo = self.ytdl.extract_info(f'ytsearch:{find}', download=False)
        if vidinfo['entries'][0] == None: return {"error":"Connection or search failed"}, 400
        return vidinfo['entries'][0], 200