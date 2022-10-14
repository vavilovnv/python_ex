# Условие задачи https://stepik.org/lesson/290612/step/9?auth=login&unit=756158

"""
Поиск-2
Даны два массива. Для каждого элемента второго массива определите, сколько раз
он встречается в первом массиве.

Входные данные
Первая строка входных данных содержит одно число N (1 ≤N ≤ 10^5) – количество
элементов в первом массиве.
Вторая строка содержит N целых упорядоченных по неубыванию чисел, не
превосходящих по модулю 10^9 – элементы первого массива.
Третья строка входных данных содержит одно число M (1 ≤M ≤ 10^5) – количество
элементов во втором массиве.
Четвертая строка содержит M целых чисел, не превосходящих по модулю 10^9 –
элементы второго массива.

Выходные данные
Выведите M чисел: для каждого элемента второго массива выведите, сколько раз
такое значение встречается в первом массиве.
"""

def left_binary_search(x, lst):
    if len(lst) == 0:
        return -1
    left, right = -1, len(lst) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if lst[mid] < x:
            left = mid
        else:
            right = mid
    if lst[right] == x:
        return right
    return -1


def right_binary_search(x, lst):
    if len(lst) == 0:
        return -1
    left, right = 0, len(lst)
    while left + 1 < right:
        mid = left + (right - left) // 2
        if lst[mid] <= x:
            left = mid
        else:
            right = mid
    if lst[left] == x:
        return left
    return -1


def main():
    n = int(input())
    lst1 = list(map(int, input().split()))
    m = int(input())
    lst2 = list(map(int, input().split()))
    for i in lst2:
        right, res = right_binary_search(i, lst1), 0
        if right != -1:
            left = left_binary_search(i, lst1)
            res = (right - left) + 1
            lst1 = lst1[left + 1:]
        print(res, end=' ')


if __name__ == '__main__':
    main()
