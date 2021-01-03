# Текст задания: https://stepik.org/lesson/24464/step/5?unit=6769

import itertools

def primes():
    x = 1
    while True:
        x += 1
        count = 0
        for i in range(1, x):
            if x % i == 0:
                count += 1
            if count == 2:
                break
        if count == 1:
            yield x

print(list(itertools.takewhile(lambda x : x <= 1000, primes())))