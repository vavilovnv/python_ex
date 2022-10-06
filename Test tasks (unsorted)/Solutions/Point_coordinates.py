# На ввод подаются:
# - координаты вершин прямоугольника ABCD,
# - координаты точки Х внутри прямоугольника,
# - параметр b из уравнения прямой (y = kx + b), которая проходит через точку Х.
# Найти координаты точек пересечения прямой проходящей через точку Х и сторон прямоугольника ABCD.

import matplotlib.pyplot as plt

# ввод данных
p = {x: [*map(float, input(f'Координаты точки {x} прямоугольника ABCD: ').split())] for x in ['A', 'B', 'C', 'D']}
while True:
    t = [*map(float, input('Координаты точки Х в формате (x, y): ').split())]
    if t[0] > p['B'][0] or t[0] < p['A'][0]:
        print('Неверно задана координата X')
    elif t[1] > p['D'][1] or t[1] < p['A'][1]:
        print('Неверно задана координата Y')
    else:
        break
b = float(input('Значение параметра "b" для функции y = kx + b: '))
k = (t[1] - b) / t[0]

# определение координат точек пересечения
if k == 0:
    t1 = [p['A'][0], t[1]]
    t2 = [p['C'][0], t[1]]
else:
    dt1 = False
    for i in ('A', 'C'):
        z = [[round((p[i][1] - b), 2) / k, p[i][1]], [p[i][0], round(k * p[i][0] + b, 2)]]
        for j in range(len(z)):
            if p['A'][j] <= z[j][j] <= p['C'][j]:
                if dt1:
                    t2 = [z[j][0], z[j][1]]
                else:
                    t1, dt1 = [z[j][0], z[j][1]], True
print('Координаты точки 1:', t1)
print('Координаты точки 2:', t2)

# визуализация
z = '+' if b >= 0 else ''
points = ['A', 'B', 'C', 'D', 'A']
plt.plot([p[i][0] for i in points], [p[i][1] for i in points], label=f'y={round(k, 2)}x{z}{b}, x=({t[0]}, {t[1]})')
plt.xlabel('x', fontsize=10, color='blue')
plt.ylabel('y', fontsize=10, color='blue')
plt.grid(True)
plt.legend()

delta = 0.5
plt.plot((p['A'][0] - delta, 0, p['C'][0] + delta), ((p['A'][0] - delta) * k + b, b, (p['C'][0] + delta) * k + b))
plt.scatter(t[0], t[1], marker='s')

plt.scatter(t1[0], t1[1])
plt.scatter(t2[0], t2[1])

plt.show()
