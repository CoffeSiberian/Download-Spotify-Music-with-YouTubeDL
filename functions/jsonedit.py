import json

def saveValue(key: str, value: str) -> None:
    with open('./credentials.json', 'r+') as r:
        data = json.load(r)
        data[key] = value
        r.seek(0)
        json.dump(data, r, indent=4)
        r.truncate()

def getValue() -> tuple:
    data = json.load(open('./credentials.json'))
    client_id = data['client_id']
    client_secret = data['client_secret']
    dir = data['dir']
    return client_id, client_secret, dir