# Текст задания: https://stepik.org/lesson/24471/step/6?unit=6780

import requests
import re


def geturl(url):
    print('Yes' if requests.get(url).status_code == 200 else 'No')


found, pattern = False, r'<a.*href="(.*)">'
docA, docB = (input().strip() for i in range(2))

urls = re.findall(pattern, requests.get(docA).text)
for url in urls:
    urls2 = re.findall(pattern, requests.get(url).text)
    if docB in urls2:
        geturl(docB)
        found = True
        break

if not found:
    print('No')
