"""
E. Анаграммы
Даны две строки, состоящие из строчных латинских букв. Требуется определить,
являются ли эти строки анаграммами, т. е. отличаются ли они только порядком
следования символов.

Формат ввода
Входной файл содержит две строки строчных латинских символов, каждая не
длиннее 100 000 символов. Строки разделяются символом перевода строки.

Формат вывода
Выходной файл должен содержать единицу, если строки являются анаграммами, и
ноль в противном случае.

Пример 1
Ввод
qiu
iuq
Вывод
1

Пример 2
Ввод
zprl
zprc
Вывод
0

"""

if sorted(input()) == sorted(input()):
	print(1)
else:
	print(0)
