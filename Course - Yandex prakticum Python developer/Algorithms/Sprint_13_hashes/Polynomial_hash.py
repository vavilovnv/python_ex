"""
Полиномиальный хеш.

Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей
написать функцию, вычисляющую хеш строки s. В данной задаче необходимо
использовать в качестве значений отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:
h(s) = ((((s_1 * a + s_2)) * a + s_3) * a + ... + s_n-1) * a + s_n) % m

Формат ввода
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание, по которому
считается хеш.
Во второй строке дано число m (1 ≤ m ≤ 109) –— модуль.
В третьей строке дана строка s (0 ≤ |s| ≤ 106), состоящая из больших и
маленьких латинских букв.

Формат вывода
Выведите целое неотрицательное число –— хеш заданной строки.

Пример 1
Ввод
123
100003
a
Вывод
97

Пример 2
Ввод	
123
100003
hash
Вывод
6080

Пример 3
Ввод
123
100003
HaSH
Вывод
56156
"""

def calc(a, m, s):
    n = len(s)
    if n == 0:
        return 0
    d = {s[0]: ord(s[0])}
    res = d[s[0]]
    for i in range(1, n):
        if s[i] not in d:
            d[s[i]] = ord(s[i])
        res = (res * a + d[s[i]]) % m
    return res


print(calc(int(input()), int(input()), input()))
