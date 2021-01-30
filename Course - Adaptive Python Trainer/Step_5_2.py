# Текст задания: https://stepik.org/lesson/21306/step/1?adaptive=true&unit=5109

# Напишите программу, которая выводит число в стиле LCD калькулятора.
# На вход программе подаётся последовательность цифр, которую нужно вывести на экран в специальном стиле.
# Размер всех цифр 4 символа в ширину и 7 символов в высоту. Между цифрами в выводе должен быть один пустой столбец.
# Перед первой цифрой не должно быть пробелов.
# Выведенные цифры должны быть обведены рамочкой, в углах которой находится символ x ("икс"), горизонтальная линия
# создаётся из символа - ("дефис"), а вертикальная -- из символа вертикальной черты: |.
# Формат ввода:
# Строка произвольной длины (минимум один символ), содержащая последовательность цифр.
# Формат вывода:
# 9 строк, содержащих цифры, записанные в указанном в задании формате.

def printline(n):
    print("x", end='')
    for i in range(len(n) * 5 - 1):
        print("-", end='')
    print("x")


n = input()
a1, a2, a3, a4, a5 = ' -- ', '|  |', '    ', '   |', '|   '
d = {'0': [a1, a2, a2, a3, a2, a2, a1], '1': [a3, a4, a4, a3, a4, a4, a3],
     '2': [a1, a4, a4, a1, a5, a5, a1], '3': [a1, a4, a4, a1, a4, a4, a1],
     '4': [a3, a2, a2, a1, a4, a4, a3], '5': [a1, a5, a5, a1, a4, a4, a1],
     '6': [a1, a5, a5, a1, a2, a2, a1], '7': [a1, a4, a4, a3, a4, a4, a3],
     '8': [a1, a2, a2, a1, a2, a2, a1], '9': [a1, a2, a2, a1, a4, a4, a1]}
printline(n)
for i in range(7):
    print('|', end='')
    for j in range(len(n)):
        print(d[n[j]][i], end='') if j == len(n)-1 else print(d[n[j]][i], end=' ')
    print('|')
printline(n)









