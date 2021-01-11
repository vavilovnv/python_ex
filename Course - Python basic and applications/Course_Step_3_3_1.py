# Текст задания: https://stepik.org/lesson/24471/step/6?unit=6780

# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
# дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и
# из C в B можно перейти за один переход.
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документ

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
