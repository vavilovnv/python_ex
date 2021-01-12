# Текст задания: https://stepik.org/lesson/3378/step/3?unit=961

import requests

path = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('input.txt', 'r') as f:
    t = f.readline().strip()

while True:
    txt = requests.get(t).text.strip()
    sp = txt.split()
    if sp[0] == 'We':
        for line in txt.splitlines():
            print(line)
        break
    else:
        t = path + sp[0]
    print(s)
