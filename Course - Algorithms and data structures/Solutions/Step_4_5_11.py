# Условие задачи https://stepik.org/lesson/124568/step/11?unit=756159

"""
Jump search
Реализуйте алгоритм поиска прыжками(Jump search).

Входные данные

В первой строке входных данных содержатся натуральные числа N и K (1 ≤ N,
K ≤ 100000).
Во второй строке задаются N элементов первого массива, отсортированного по
возрастанию. 
В третьей строке – K элементов второго массива.

Элементы обоих массивов - целые числа, каждое из которых по модулю не
превосходит 10^9.

Выходные данные

Требуется для каждого из K чисел вывести в отдельную строку "YES", если это
число встречается в первом массиве, и "NO" в противном случае.
"""

def jump_search(iterable, x):
    len_iterable = len(iterable)
    n = int(pow(len_iterable, 0.5))
    right, left = 0, n
    while left + 1 < len_iterable:
        if iterable[left] >= x:
            break
        right, left = left, min(len_iterable - 1, left + n)
    return ['YES', 'NO'][x in iterable[right: left + 1]]


def main():
    n, k = map(int, input().split())
    lst1 = [int(i) for i in input().split()]
    lst2 = [int(i) for i in input().split()]
    print(*[jump_search(lst1, x) for x in lst2], sep='\n')


if __name__ == '__main__':
    main()
