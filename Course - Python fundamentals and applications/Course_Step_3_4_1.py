# Текст задания: https://stepik.org/lesson/24473/step/2?unit=6777

import csv

with open('Crimes.csv') as f:
    reader = csv.reader(f)
    crimes = [row[5] for row in reader if '2015' in row[2]]

print(max(crimes, key = crimes.count))

