from yt_dlp import YoutubeDL

class youtube:
    def __init__(self) -> None:
        self.__ytdl_options = {
        'format': 'bestaudio/best',
        'no_warnings': True,
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'logtostderr': False,
        'quiet': True
        }
        self.__ytdl = YoutubeDL(self.__ytdl_options)

    def findVideoInfoURL(self, url) -> list:
        vidinfo = self.__ytdl.extract_info(url, download=False)
        return vidinfo
    
    def search(self, find) -> list:
        vidinfo = self.__ytdl.extract_info(f'ytsearch:{find}', download=False)
        return vidinfo