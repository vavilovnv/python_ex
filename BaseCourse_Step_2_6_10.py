# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой,
# содержащей только строку "end" (без кавычек)
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы
# на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

import copy

s, sp =  input(), []

while s != 'end':
    sp.append([int(i) for i in s.split()])
    s = input()

sp1 = copy.deepcopy(sp)

for i in range(len(sp)):
    for j in range(len(sp[i])):
        sp1[i][j] = sp[i - 1][j] + sp[i - len(sp) + 1][j] + sp[i][j - 1] + sp[i][j - len(sp[i]) + 1]

for i in sp1:
    for j in i:
        print(j, end=' ')
    print()