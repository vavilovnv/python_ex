# Текст задания: https://stepik.org/lesson/209723/step/6?unit=183223

# В файле https://stepik.org/media/attachments/lesson/209723/5.html находится одна таблица. Просуммируйте все числа в
# ней. Теперь мы не только добавили разных тегов для изменения стиля отображения, но и сделали невалидный HTML-код
# (правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы). Невалидный HTML-код - не редкость в
# интернете, надо учиться работать и с этим.
# Вы можете исправить html-код или попробовать использовать нестандартный парсер html, такой как html5lib.

import requests
from bs4 import BeautifulSoup

text = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html').text
soup = BeautifulSoup(text, 'html.parser')

table, count = soup.find('table'), 0
print(sum(int(td.text) for td in soup.find_all('td')))

