from typing import Tuple


def splitURL(url: str) -> str | bool:
    '''
    get id from url playlist or track
    '''
    try:
        start = url.split(sep='?')[0]
        return start.split(sep='/')[4]
    except IndexError:
        return False


def splitURLType(url: str) -> str | bool:
    '''
    get from url playlist or track
    '''
    try:
        return url.split(sep='/')[3]
    except IndexError:
        return False


def idAndType(url: str) -> Tuple[str, str] | bool:
    '''
    return splitURL and splitURLType in list or False with an error
    '''
    type = splitURLType(url)
    id = splitURL(url)
    if type != False:
        if id != False:
            if type == "intl-es":
                return ["track", url.split(sep='/')[5]]
            return [type, id]
    return False
