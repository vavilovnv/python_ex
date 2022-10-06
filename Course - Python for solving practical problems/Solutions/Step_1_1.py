# Текст задания: https://stepik.org/lesson/209717/step/2?unit=183221

# Мы сохранили страницу с википедии про языки программирования и сохранили по адресу
# https://stepik.org/media/attachments/lesson/209717/1.html
# # Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++ (ответ должен быть
# одной из этих двух строк).

from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
print("C++" if html.count("C++") > html.count("Python") else "Python")