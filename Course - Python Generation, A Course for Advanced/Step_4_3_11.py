# Текст задания: https://stepik.org/lesson/416753/step/11?unit=406261

# На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника
# Паскаля.
#
# Формат входных данных
# На вход программе подается число n (n ≥ 1).
#
# Формат выходных данных
# Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

from math import factorial


def pascal_triangle(n):
    for j in range(n):
        lst = []
        for i in range(j + 1):
            lst.append(int(factorial(j) / (factorial(i) * factorial(j - i))))
        print(*lst)


pascal_triangle(int(input()))
