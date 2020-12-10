# Построить и вывести график

from pylab import *

t = linspace(0, 20, 500)
x = 24.8 * (cos(t) + cos(6.2 * t) / 6.2)
y = 24.8 * (sin(t) - sin(6.2 * t) / 6.2)

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()