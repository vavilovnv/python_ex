# Условие задачи https://stepik.org/lesson/306286/step/10?unit=756168

"""
Палиндром
Палиндром - это строка, которая читается одинаково как справа налево, так и
слева направо. 

На вход программы поступает набор заглавных латинских букв. Разрешается
переставлять буквы, а также удалять некоторые буквы. Требуется из данных букв
по указанным правилам составить палиндром наибольшей длины, а если таких
палиндромов несколько, то выбрать первый из них в алфавитном порядке.

Входные данные
В первой строке входных данных содержится число N (1 ≤ N ≤ 10^5).
Во второй строке задается последовательность из N заглавных латинских букв
(буквы записаны без пробелов).

Выходные данные
В единственной строке выходных данных выведите искомый палиндром.
"""

from collections import Counter

def main(lst):
    odds = [i for i in lst if i[1] % 2 != 0]
    odd = min(odds, key=lambda x: x[0]) if odds else (1, 0)
    res, mid = [], ''
    for i in lst:
        a, b = divmod(i[1], 2)
        res.append(i[0] * a)
        if i[0] == odd[0]:
            mid = i[0] * b
    res.sort()
    print(''.join(res) + mid + ''.join(res[::-1]))


if __name__ == '__main__':
    input()
    main(sorted(Counter(input()).items(), key=lambda x: (-x[1], x[0])))
