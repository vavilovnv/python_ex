# Текст задания: https://stepik.org/lesson/246231/step/3?unit=218435

# В этой задаче вам предстоит настроить и запустить веб-сервер. Создайте файл index.html с формой, в которой есть
# единственное текстовое поле ввода с именем INPUT_TEXT и кнопка отправить.
# В папке cgi-bin создайте скрипт со следующим содержанием:
#
# import cgi
#
# def ohash(s):
#     ans = 0
#     for c in s:
#         ans = ans * 123417 + ord(c)
#     return ans
#
# form = cgi.FieldStorage()
# text = form.getfirst("INPUT_TEXT", "не задано")
#
# print("Content-type: text/html\n")
# print("""<!DOCTYPE HTML>
#         <html>
#         <head>
#             <meta charset="utf-8">
#         </head>
#         <body>""")
#
# print("<h1>" + str(ohash(text)) + "</h1>")
#
# print("""</body>
#         </html>""")
# Запустите скрипт, поднимающий веб-сервер с вашей формой, откройте страницу и введите слово Python (обязательно с
# большой буквы). У вас должна открыться страница, содержащая единственное число, введите его в качестве ответа.
#
# Скрипт по отрисовке формы и выводу ответа.

import cgi

def ohash(s):
    ans = 0
    for c in s:
        ans = ans * 123417 + ord(c)
    return ans

form = cgi.FieldStorage()
text = form.getfirst("INPUT_TEXT", 'Не введено')

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html><head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>
            <form action="/cgi-bin/script.py">
                <input type="text" name="INPUT_TEXT">
                <input type="submit">
            </form>""")

if text != 'Не введено':
    print("<h1>" + str(ohash(text)) + "</h1>")

print("</body></html>")
