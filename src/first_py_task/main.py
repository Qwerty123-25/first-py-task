# -*- coding: utf-8 -*-

import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass')) #создаем запрос




print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)