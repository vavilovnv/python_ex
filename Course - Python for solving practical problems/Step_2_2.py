# Текст задания: https://stepik.org/lesson/245267/step/2?unit=217494

# Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал зарплаты для разных
# интересных ему профессий. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245267/salaries.xlsx.
# Выведите название региона с самой высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива
# после его упорядочивания) и, через пробел, название профессии с самой высокой средней зарплатой по всем регионам.

import xlrd
import requests
from statistics import mean, median

r = requests.get('https://stepik.org/media/attachments/lesson/245267/salaries.xlsx')
wb = xlrd.open_workbook(file_contents=r.content)
sh = wb.sheet_by_name(wb.sheet_names()[0])
msalary = 0
for rownum in range(2, sh.nrows):
    temp = median(sorted(sh.row_values(rownum)[1:]))
    if temp > msalary:
        msalary = temp
        region = sh.row_values(rownum)[0]
msalary = 0
for colnum in range(2, sh.ncols):
    temp = mean(sh.col_values(colnum)[1:])
    if temp > msalary:
        msalary = temp
        prof = sh.col_values(colnum)[0]
print(region, prof)
