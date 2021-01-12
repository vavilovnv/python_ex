# Текст задания: https://stepik.org/lesson/3378/step/2?unit=961

import requests

with open('input.txt', 'r') as f:
    r = requests.get(f.readline().strip())
    print(len(r.text.splitlines()))