# Текст задания: https://stepik.org/lesson/245883/step/7?unit=218100

# Воспользуемся еще одним примером из статьи https://eax.me/python-matplotlib/:
# Вам необходимо сделать так, чтобы размер генерируемого изображения стал 1024 на 768. Исправьте ровно одну строку в
# этой программе (не меняя ничего другого) и сдайте исправленный исходный код программы. Пожалуйста, используйте
# одинарные кавычки и расстановку пробелов в том же стиле, в котором написан пример.

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

data_names = ['cafe', 'pharmacy', 'fuel', 'bank', 'waste_disposal',
              'atm', 'bench', 'parking', 'restaurant',
              'place_of_worship']
data_values = [9124, 8652, 7592, 7515, 7041, 6487, 6374, 6277,
               5092, 3629]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (1024 / dpi, 768 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.title('OpenStreetMap Point Types')

ax = plt.axes()
ax.yaxis.grid(True, zorder = 1)

xs = range(len(data_names))

plt.bar([x + 0.05 for x in xs], [ d * 0.9 for d in data_values],
        width = 0.2, color = 'red', alpha = 0.7, label = '2016',
        zorder = 2)
plt.bar([x + 0.3 for x in xs], data_values,
        width = 0.2, color = 'blue', alpha = 0.7, label = '2017',
        zorder = 2)
plt.xticks(xs, data_names)

fig.autofmt_xdate(rotation = 25)

plt.legend(loc='upper right')
plt.show()



