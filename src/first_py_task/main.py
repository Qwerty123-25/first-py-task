# -*- coding: utf-8 -*-

import requests
import json

r = requests.get('https://api.github.com/user', auth=('user', 'pass')) #создаем запрос
s = r.json()


print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)


print(s['message'])
print(s['documentation_url'])
print(s['status'])
for k, v in s.items():
    print(f"{k}: {v}")
