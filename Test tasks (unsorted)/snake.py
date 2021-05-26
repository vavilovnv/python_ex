# Змейка
import numpy as np


def snake(rows, cols):
    a = np.array(range(1, rows * cols + 1)).reshape(rows, cols)
    a[1::2] = a[1::2, ::-1]
    return a


print(snake(5, 5))
