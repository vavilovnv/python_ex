# Построить и вывести гистограмму

from numpy import *
n = random.randn(100000)

from pylab import *
fig, axes = subplots(1, 2, figsize = (12, 4))

axes[0].hist(n)
axes[0].set_title('Default histogram')
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative = True, bins = 50)
axes[1].set_title('Cumulative detailed histogram')
axes[1].set_xlim((min(n), max(n)))