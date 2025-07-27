# -*- coding: utf-8 -*-

import requests

url = 'https://api.github.com/'
headers = {'User-Agent': 'MyPythonApp/1.0','user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36'}

def get_response(url: str=url, headers: dict=headers) ->requests.Response:
    try:
        r = requests.get(url, headers)
        if r.status_code==200:
            print(f"successful: {r.status_code}")
            return r
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    except ConnectionError:
        print("Connection error")
    

def info_response(resp: requests.Response ) ->None:
    print(resp.headers['content-type'])
    print(resp.encoding)

def print_json_response(resp: requests.Response) -> None:
    if 'application/json' in resp.headers['content-type'].lower():
        try:
            data = resp.json()
            print(f"key{'':30} \t \tvalue")
            for k, v in data.items():
                print(f"{k:30.20} ===> \t{v}")
        except ValueError:
            print("Response contet invalid JSON")
    else:
        print("Response is not JSON")


e = get_response()
info_response(e)
print_json_response(e)

