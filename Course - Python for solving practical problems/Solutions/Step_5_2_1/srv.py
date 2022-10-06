# Текст задания: https://stepik.org/lesson/246231/step/3?unit=218435
#
# В этой задаче вам предстоит настроить и запустить веб-сервер. Создайте файл index.html с формой, в которой есть
# единственное текстовое поле ввода с именем INPUT_TEXT и кнопка отправить.
# Запустите скрипт, поднимающий веб-сервер с вашей формой, откройте страницу и введите слово Python (обязательно с
# большой буквы). У вас должна открыться страница, содержащая единственное число, введите его в качестве ответа.
#
# Скрипт для запуска http сервера

from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8080)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
