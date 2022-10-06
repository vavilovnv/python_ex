# Текст задания: https://stepik.org/lesson/209719/step/2?unit=183222

# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python. В этой
# статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки, содержащиеся
# между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном порядке,
# разделяя пробелами.

import requests

text, d = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html').text, {}
ind = text.find("<code>")
while ind >= 0:
    text = text[ind + 6:]
    ind = text.find("</code>")
    if not ind == -1:
        if text[:ind] in d:
            d[text[:ind]] += 1
        else:
            d[text[:ind]] = 1
        text = text[ind + 7:]
    ind = text.find("<code>")

max = sorted(list(d.values()), reverse=True)[0]
print(*sorted([i for i,v in d.items() if v == max]))


