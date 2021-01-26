# Текст задания: https://stepik.org/lesson/21975/step/2?adaptive=true&unit=5235

# Напишите программу, которая принимает на вход список чисел и число, после чего выводит все позиции, на которых это
# число встречается в переданном списке.
# Позиции в списке нумеруются с нуля.
# Если число x не найдено в списке, нужно вывести строку "None" (без кавычек, с большой буквы).
# Формат ввода:
# На первой строке содержатся значения списка -- целые числа, разделённые пробелом. На второй строке содержится целое
# число, позиции которого нужно найти.
# Формат вывода:
# Одна строка, в которой содержится слово "None" или через пробел перечислены числа -- позиции, на которых число x
# встречается в списке lst. Позиции должны быть выведены в порядке возрастания.

s, v = input().split(), input()

if v not in s:
    print('None')
else:
    for i in range(len(s)):
        if s[i] == v:
            print(i, end=' ')