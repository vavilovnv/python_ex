# Текст задания: https://stepik.org/lesson/209723/step/4?unit=183223

# В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица. Просуммируйте все числа в
# ней и введите в качестве ответа одно число - эту сумму. Для доступа к ячейкам используйте возможности BeautifulSoup.

import requests
from bs4 import BeautifulSoup

text = requests.get('https://stepik.org/media/attachments/lesson/209723/3.html').text
soup = BeautifulSoup(text, 'html.parser')

table, count = soup.find('table'), 0
print(sum(int(td.text) for td in soup.find_all('td')))

