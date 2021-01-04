# Текст задания: https://stepik.org/lesson/24471/step/7?unit=6780

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


