# Текст задания: https://stepik.org/lesson/245290/step/2?unit=217516

# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов
# с указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта. Ему не
# удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным
# нулю). Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. Таблица
# доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx
# Вася хочет минимизировать вес продуктов и для этого брать самые калорийные продукты. Помогите ему и упорядочите
# продукты по убыванию калорийности. В случае, если продукты имеют одинаковую калорийность - упорядочите их по названию.
# В качестве ответа необходимо сдать названия продуктов, по одному в строке.

import xlrd

def download_file(url):
    import wget

    wget.download(url)
    return xlrd.open_workbook('tab.xlsx')

def get_file(url):
    import requests

    r = requests.get(url)
    return xlrd.open_workbook(file_contents=r.content)

download = False
url = 'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx'

if download:
    wb = download_file(url)
else:
    wb = get_file(url)
sh = wb.sheet_by_name(wb.sheet_names()[0])
food = {sh.row_values(i)[0]: sh.row_values(i)[1] for i in range(1, sh.nrows)}
[print(i[0]) for i in sorted(food.items(), key=lambda item: (-item[1], item[0]))]



