# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла
# и закрученной по часовой стрелке, как показано в примере (здесь n=5):
# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# in progress

n = int(input())
sp = [[0 for j in range(n)] for i in range(n)]

x, d, s, = 0, 0, 1
vektor = 0  # 0 - слева направо
            # 1 - сверху вниз
            # 2 - справа налево
            # 3 - снизу вверх
otstup = 0
shag = 1
delta = 0

i, j, y, sm = n - 1,0, n-1, 0

x=0
while x<n*n:
    d = n - shag // 2
    x += d
    vektor = shag % 4
    shag += 1

    if vektor == 0:
         j -= d
    elif vektor == 1:
        i -= d
    elif vektor == 2:
        j += d
    elif vektor == 3:
        i += d

    print(x, i, j)

# for i in range(n-1):
#     for j in range(n-1):
#         print(sp[i][j], end = ' ')
#     print()