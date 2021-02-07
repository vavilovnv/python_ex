# Текст задания: https://stepik.org/lesson/245130/step/3?unit=217352

# Сейчас вам нужно установить библиотеку BeautifulSoup. Чтобы проверить, что всё установилось хорошо, необходимо
# запусить код, представленный ниже и сдать в качестве ответа то, что он выводит.

import requests
from bs4 import BeautifulSoup

text, cnt = requests.get('https://stepik.org/media/attachments/lesson/245130/6.html').text, 0
soup = BeautifulSoup(text, 'html.parser')

table = soup.find('table', attrs = {'class' : 'wikitable sortable'})
for tr in soup.find_all('tr'):
    cnt += 1
    for td in tr.find_all(['td', 'th']):
        cnt *= 2
print(cnt)

