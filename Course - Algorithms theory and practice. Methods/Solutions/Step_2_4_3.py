# Текст задания: https://stepik.org/lesson/13230/step/9?unit=3416

# Упорядочите данные семь функций по возрастанию скорости роста (сверху —
# медленнее всего растущая функция, снизу — быстрее всего растущая).

import time
import math


def timed(f, *args, count_iter=100):
    """Функция рассчитывает минимальное время исполнения переданной
    функции за определенное количество итераций."""
    
    acc = float('inf')
    for i in range(count_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


if __name__ == '__main__':
    n = 5000
    print(timed(math.log, n, 5))
    print(timed(pow, n, 0.3))
    print(timed(math.sqrt, n))
    print(n * timed(math.log, n, 2))
    print(n * timed(pow, math.log(n, 2), 3))
    print(timed(pow, n, 3))
    print(timed(pow, 4, n))
