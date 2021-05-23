# текст задания: https://stepik.org/lesson/225311/step/8?unit=198054

# Допустим, Вы хотите строить матрицу признаков с помощью TF-IDF на биграммах токенов (N-граммах с N=2). Оцените,
# приблизительно, наибольшее количество уникальных биграмм в словаре для достаточно большой коллекции. Предполагайте,
# что в текстах используется 1000 уникальных токенов.

import math

N, nTokens = 2, 1000
print(math.factorial(nTokens) / math.factorial(nTokens - N))

