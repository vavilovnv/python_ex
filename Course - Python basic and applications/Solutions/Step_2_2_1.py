# Текст задания: https://stepik.org/lesson/24466/step/5?unit=6773

# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
# равное days.

import datetime

d = input().split()
date = datetime.date(int(d[0]), int(d[1]), int(d[2])) + datetime.timedelta(int(input()))
print(date.year, date.month, date.day)
