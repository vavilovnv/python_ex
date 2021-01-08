# Текст задания: https://stepik.org/lesson/24473/step/2?unit=6777

# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
# настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

import csv

with open('Crimes.csv') as f:
    reader = csv.reader(f)
    crimes = [row[5] for row in reader if '2015' in row[2]]

print(max(crimes, key = crimes.count))

