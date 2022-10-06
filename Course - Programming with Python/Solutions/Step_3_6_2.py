# Текст задания: https://stepik.org/lesson/3378/step/3?unit=961

# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.

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

