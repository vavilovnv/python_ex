# Текст задания: https://stepik.org/lesson/416754/step/14?unit=406262

# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую
# и правую.
#
# Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой
# четверти.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые
# числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Элементы диагоналей не учитываются.

n = int(input())
mtx = [[int(i) for i in input().split(' ')] for _ in range(n)]
print('Верхняя четверть:', sum([mtx[i][j] for i in range(n) for j in range(n) if i < j and i < n-j-1]))
print('Правая четверть:', sum([mtx[i][j] for i in range(n) for j in range(n) if j > i > n-j-1]))
print('Нижняя четверть:', sum([mtx[i][j] for i in range(n) for j in range(n) if i > j and i > n-j-1]))
print('Левая четверть:', sum([mtx[i][j] for i in range(n) for j in range(n) if j < i < n-j-1]))

