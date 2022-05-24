import os

class Validations:

    def fileNameCheck(str) -> str: #checked incorrect character in filename
        lst = []
        strBlock = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|"]
        for r,char in enumerate(str):
            for i in strBlock:
                if char == i:
                    lst.append(r)
                    break
        list_str = list(str)
        if len(lst) == 0:
            return str
        for r in lst:
            list_str[r] = '_'
            name = ''.join(list_str)
        return name
        
    def downloadLog(dirt, playListName, remaining) -> None: #saved id of last track downloaded
        with open(f'{dirt}/music/{playListName}/log', 'w') as outfile:
            outfile.write(str(remaining))

    def readLog(dirt, playlistName) -> str or bool: #checks last download correct
        if os.path.exists(f'{dirt}/music/{playlistName}/log') == False:
            return False
        with open(f'{dirt}/music/{playlistName}/log') as file:
            return file.read()
    
    def createFolderList(dirt, nameFolder) -> bool:
        if os.path.exists(f'{dirt}/music/{nameFolder}') == False:
            os.mkdir(f'{dirt}/music/{nameFolder}')
        return True

    def createMusicFolder(dirt) -> bool:
        if os.path.exists(f'{dirt}/music') == False:
            os.mkdir(f'{dirt}/music')
        return True
    
    def removeFileMusic(dirt, playlistName, nameFile, remaining) -> None: #delete bad downloaded files (download not finish)
        os.remove(f'{dirt}/music/{playlistName}/[{remaining}] - {nameFile}.mp3')