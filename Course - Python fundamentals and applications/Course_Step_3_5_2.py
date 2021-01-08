# Текст задания: https://stepik.org/lesson/24476/step/4?unit=6781

import requests
import json

client_id = '...'
client_secret = '...'

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

with open('output.txt', 'w', encoding='utf-8') as f:
    for i in sorted(artists.items(), key=lambda x: (x[1], x[0])):
        f.writelines(i[0]+'\n')



