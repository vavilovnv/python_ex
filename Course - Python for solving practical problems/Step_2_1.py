# Текст задания: https://stepik.org/lesson/245266/step/2?unit=217493

# Для решения этой задачи необходимо установить библиотеку xlrd, скачать файл
# https://stepik.org/media/attachments/lesson/245266/tab.xlsx и создать в папке с этим файлом скрипт со следующем
# содержанием:
# import xlrd
#
# wb = xlrd.open_workbook('tab.xlsx')
# sheet_names = wb.sheet_names()
# sh = wb.sheet_by_name(sheet_names[0])
# nmin = sh.row_values(6)[2]
# for rownum in range(7, 27):
#     temp = sh.row_values(rownum)
#     nmin = min(nmin, temp[2])
# print(nmin)

import xlrd
import requests
import wget

# wget.download('https://stepik.org/media/attachments/lesson/245266/tab.xlsx')
# wb = xlrd.open_workbook('tab.xlsx')

r = requests.get('https://stepik.org/media/attachments/lesson/245266/tab.xlsx')
wb = xlrd.open_workbook(file_contents=r.content)
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
nmin = sh.row_values(6)[2]
for rownum in range(7, 28):
    temp = sh.row_values(rownum)
    nmin = min(nmin, temp[2])
print(nmin)

# вариант реализации на pandas

# import pandas as pd
#
# wb = pd.read_excel('https://stepik.org/media/attachments/lesson/245266/tab.xlsx')
# print(min(wb.iloc[6, 2], wb.iloc[7:28, 2].min()))