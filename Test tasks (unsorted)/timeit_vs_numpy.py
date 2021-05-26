# разница в скорости при использовании numpy
import timeit

# время извлечения квадрата до 10^6 степени
print(timeit.timeit("list(map(sqrt, range(100000)))", "from math import sqrt; a=[]", number=1))

# то же самое через numpy
print(timeit.timeit("np.sqrt(np.arange(100000))", "import numpy as np", number=1))

