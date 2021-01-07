# Текст задания: https://stepik.org/lesson/24476/step/3?unit=6781

import requests

api_url = "http://numbersapi.com/"
params = {
     'json': 'True'
}

with open('input.txt') as f:
    for line in f:
        number = line.strip()
        res = requests.get(api_url + number + '/math', params)
        print('Interesting' if res.json()['found'] == True else 'Boring')



