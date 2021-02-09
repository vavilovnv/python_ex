# Текст задания: https://stepik.org/lesson/245290/step/3?unit=217516

# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с
# указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта. Ему не
# удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным
# нулю). Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. Таблица
# доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx
# Вася составил раскладку по продуктам на один день (она на листе "Раскладка") с указанием названия продукта и его
# количества в граммах. Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов. Числа округлите
# до целых вниз и введите через пробел.

import xlrd

def download_file(url):
    import wget

    wget.download(url)
    return xlrd.open_workbook('trekking2.xlsx')

def get_file(url):
    import requests

    r = requests.get(url)
    return xlrd.open_workbook(file_contents=r.content)

download = False
url = 'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx'

if download:
    wb = download_file(url)
else:
    wb = get_file(url)
sh1, sh2 = wb.sheet_by_name(wb.sheet_names()[0]), wb.sheet_by_name(wb.sheet_names()[1])
res = [0, 0, 0, 0]
food = {sh1.row_values(i)[0]: [sh1.row_values(i)[j] for j in range(1,5)] for i in range(1, sh1.nrows)}
for i in range(1, sh2.nrows):
    key = sh2.row_values(i)[0]
    if key in food.keys():
        v = sh2.row_values(i)[1]
        for j in range(4):
            res[j] += v / 100 * food[key][j] if food[key][j] != "" else 0
print(*map(int, res))



