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

x, d, s= 0, 0, 1
while x < n * n:
    x = n * s - d
    d += (s+1)//2
    v = s % 4
    s += 1
    print(x)

# for i in range(n-1):
#     for j in range(n-1):
#         print(sp[i][j], end = ' ')
#     print()