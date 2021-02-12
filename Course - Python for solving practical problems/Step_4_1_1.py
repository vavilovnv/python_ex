# Текст задания: https://stepik.org/lesson/245883/step/2?unit=218100

# Это задание необходимо для того, чтобы проверить, что у вас все хорошо с библиотекой matplotlib.
# Создайте и запустите следующий файл. Откройте файл trigan.png и выберите, значение какой функции больше в точке x = 6.
# У вас всего одна попытка ответить на этот вопрос, будьте внимательны!

import matplotlib as mpl
import matplotlib.pyplot as plt
import math

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 10, -1.5, 1.5])

plt.title('Sin & Cos')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)

xs, sin_vals, cos_vals, x = [], [], [], 0.0
while x < 10.0:
    sin_vals += [math.sin(3 * x)]
    cos_vals += [math.cos(x)]
    xs += [x]
    x += 0.1

plt.plot(xs, sin_vals, color = 'blue', linestyle = 'solid', label = 'sin(3x)')
plt.plot(xs, cos_vals, color = 'red', linestyle = 'dashed', label = 'cos(x)')

plt.legend(loc = 'upper right')
# fig.savefig('trigan.png')
plt.show()



