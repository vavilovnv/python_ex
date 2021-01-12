# Текст задания: https://stepik.org/lesson/3369/step/10?unit=952

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