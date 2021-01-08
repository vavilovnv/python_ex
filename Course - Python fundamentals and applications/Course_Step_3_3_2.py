# Текст задания: https://stepik.org/lesson/24471/step/7?unit=6780

# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
# на которые есть ссылка.
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность
# символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за
# исключением случаев с относительными ссылками вида <a href="../some_path/index.html">.
# Сайты следует выводить в алфавитном порядке.

import requests
import re

pattern = r'(<a.*href[ ]?=[ ]? ?.)(http:\/\/|https:\/\/|ftp:\/\/)?([\w._-]*)'
text = requests.get(input().strip()).text # 'https://pastebin.com/raw/7543p0ns'

urls, urls_out = re.findall(pattern, text), set()
for url in urls:
    urls_out.add(url[2])

for url in sorted(urls_out):
    if url != '..':
        print(url)


