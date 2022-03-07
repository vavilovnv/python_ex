# Текст задания: https://stepik.org/lesson/416756/step/10?unit=406264

# Напишите программу, которая перемножает две матрицы.
#
# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы
# первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем
# элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

n, m = map(int, input().split(' '))
a = [[int(j) for j in input().split(' ')] for i in range(n)]
print()
m, k = map(int, input().split(' '))
b = [[int(j) for j in input().split(' ')] for i in range(m)]
c = [[0 for _ in range(n)] for i in range(k)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            c[i][j] += a[i][x] * b[x][j]

[print(*row) for row in c]

