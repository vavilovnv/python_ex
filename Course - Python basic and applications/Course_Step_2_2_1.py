# Текст задания: https://stepik.org/lesson/24466/step/5?unit=6773

import datetime

d = input().split()
date = datetime.date(int(d[0]), int(d[1]), int(d[2])) + datetime.timedelta(int(input()))
print(date.year, date.month, date.day)