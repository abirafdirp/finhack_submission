import requests
import json


def get(get_all=False):
    headers = {
        'Authorization': 'Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ=',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'grant_type': 'client_credentials'
    }

    r = requests.post(
        'https://api.finhacks.id/api/oauth/token',
        headers=headers,
        data=payload,
    )
    if not get_all:
        parsed = json.loads(r.text)
        print(parsed)
        r = parsed['access_token']
    return r


if __name__ == '__main__':
    r = get(get_all=True)
    parsed = json.loads(r.text)
    print(json.dumps(parsed, indent=4))
    print(r.headers)
