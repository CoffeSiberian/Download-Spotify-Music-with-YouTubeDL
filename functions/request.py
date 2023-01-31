from requests import Response, get, post
from requests.structures import CaseInsensitiveDict
from requests.exceptions import RequestException

def getData(url: str, headers: CaseInsensitiveDict, stream: bool = False) -> Response:
    try:
        data = get(url=url, headers=headers, stream=stream)
        return data
    except RequestException as err:
        return fakeResponseToError()

def postData(url: str, data: str, headers: CaseInsensitiveDict, stream: bool = False) -> Response:
    try:
        data = post(url=url, headers=headers, data=data, stream=stream)
        return data
    except RequestException as err:
        return fakeResponseToError()

def fakeResponseToError() -> Response:
    errorMsj = '{"error":"Connection error"}'
    fakeResponse = Response()
    fakeResponse.status_code = 504
    fakeResponse._content = bytes(errorMsj, "utf-8")
    return fakeResponse