"""
Списочная форма.

Вася просил Аллу помочь решить задачу. На этот раз по информатике.
Для неотрицательного целого числа X списочная форма – это массив его цифр
слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход
подается количество цифр числа Х, списочная форма неотрицательного числа Х и
неотрицательное число K. Числа К и Х не превосходят 10000.
Нужно вернуть списочную форму числа X + K.

Формат ввода
В первой строке — длина списочной формы числа X. На следующей строке — сама
списочная форма с цифрами записанными через пробел.
В последней строке записано число K, 0 ≤ K ≤ 10000.

Формат вывода
Выведите списочную форму числа X + K.

Пример 1
Ввод
4
1 2 0 0
34
Вывод
1 2 3 4
Пример 2
Ввод
2
9 5
17
Вывод
1 1 2
"""

n = int(input())
print(*list(str(int(''.join(input().split())) + int(input()))))
