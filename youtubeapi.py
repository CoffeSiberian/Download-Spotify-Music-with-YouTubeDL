import youtube_dl

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
        self.__ytdl = youtube_dl.YoutubeDL(self.__ytdl_options)

    def findVideoInfoURL(self, url) -> str:
        vidinfo = self.__ytdl.extract_info(url, download=False)
        return vidinfo
    
    def search(self, find) -> str:
        vidinfo = self.__ytdl.extract_info(f"ytsearch:{find}", download=False)
        return vidinfo