# Текст задания: https://stepik.org/lesson/416756/step/11?unit=406264

# Напишите программу, которая возводит квадратную матрицу в m-ую степень.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, затем
# натуральное число m.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

n = int(input())
mtx = [[int(j) for j in input().split(' ')] for i in range(n)]
temp, m = mtx[:], int(input())

for _ in range(m-1):
    new = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                new[i][j] += temp[i][x] * mtx[x][j]
    temp = new[:]

[print(*row) for row in new]

