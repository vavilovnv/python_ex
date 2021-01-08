# Текст задания: https://stepik.org/lesson/24476/step/4?unit=6781

import requests
import json

client_id = 'fedf943c7c8fb509dafc'
client_secret = 'b918a9cd0701d7d1756cf058dde8c93f'

# запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# получаем токен
ans = json.loads(r.text)
token = ans["token"]

# запрос с заголовком, содержащий наш токен
headers = {"X-Xapp-Token" : token}
url_api = "https://api.artsy.net/api/artists/"
artists = {}

with open('input.txt') as f:
    for line in f:
        res = requests.get(url_api + line.strip(), headers=headers)
        res.encoding = 'utf-8'
        ans = json.loads(res.text)
        artists[ans['sortable_name']] = ans['birthday']




