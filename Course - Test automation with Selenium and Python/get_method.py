import time
from selenium import webdriver

# инициализируем драйвер браузера
driver = webdriver.Chrome()

# чтобы увидеть, что происходит в браузере
time.sleep(5)

# Метод get открывает сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector позволяет находит нужный элемент на сайте, указав путь к нему
textarea = driver.find_element_by_css_selector(".textarea")

# Ввод текста в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Кнопка, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Команда нажатия на кнопку
submit_button.click()
time.sleep(5)

# закрываем окно браузера
driver.quit()
