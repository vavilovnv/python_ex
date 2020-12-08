# Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и
# посчитать число строк в нём.

import requests

with open('input.txt', 'r') as f:
    r = requests.get(f.readline().strip())
    print(len(r.text.splitlines()))