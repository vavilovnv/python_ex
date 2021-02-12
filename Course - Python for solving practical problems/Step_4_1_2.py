# Текст задания: https://stepik.org/lesson/245883/step/6?unit=218100

# В видео мы нашли хорошую статью, которая находится по ссылке https://eax.me/python-matplotlib/, она может быть вам
# полезна. Воспользуемся первым примером оттуда.
# Вам необходимо переместить легенду (подписи к графикам) из правого верхнего в левый нижний угол. Исправьте ровно одну
# строку в этой программе (не меняя ничего другого) и сдайте исправленный исходный код программы. Пожалуйста,
# используйте одинарные кавычки и расстановку пробелов в том же стиле, в котором написан пример.

import matplotlib as mpl
import matplotlib.pyplot as plt
import math

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 10, -1.5, 1.5])

plt.title('Sine & Cosine')
plt.xlabel('x')
plt.ylabel('F(x)')

xs = []
sin_vals = []
cos_vals = []

x = 0.0
while x < 10.0:
    sin_vals += [ math.sin(x) ]
    cos_vals += [ math.cos(x) ]
    xs += [x]
    x += 0.1

plt.plot(xs, sin_vals, color = 'blue', linestyle = 'solid',
         label = 'sin(x)')
plt.plot(xs, cos_vals, color = 'red', linestyle = 'dashed',
         label = 'cos(x)')

plt.legend(loc = 'lower left')
plt.show()



