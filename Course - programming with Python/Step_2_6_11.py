# Текст задания: https://stepik.org/lesson/3369/step/11?unit=952

n = int(input())
sp = [[0 for j in range(n)] for i in range(n)]

x, d, s = 1, 0, 1,
di, dj = 0, 0 # координаты угловых точек
v = 0  # вектор 0 - слева направо, 1 - сверху вниз, 2 - справа налево, 3 - снизу вверх

while x <= n * n:
    d = n - s // 2 # расчет "приращения" от предыдущего x к текущему

    if v == 0:
        for j in range(dj, dj + d):
             sp[di][j] = x
             x += 1
        di += 1
        dj += d - 1
    elif v == 1:
        for i in range(di, di + d):
            sp[i][dj] = x
            x += 1
        di += d - 1
        dj -= 1
    elif v == 2:
        for j in range(dj, dj - d, -1):
            sp[di][j] = x
            x += 1
        di -= 1
        dj -= d - 1
    elif v == 3:
        for i in range(di, di - d, - 1):
            sp[i][dj] = x
            x += 1
        di -= d - 1
        dj += 1

    v = s % 4 # расчет дальнейшего направление
    s += 1 # увеличиваем шаг на единицу

for i in range(n):
    print(*sp[i])
