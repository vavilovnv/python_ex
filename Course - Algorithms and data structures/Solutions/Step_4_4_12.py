# Условие задачи https://stepik.org/lesson/290612/step/9?auth=login&unit=756158

"""
Приближенный двоичный поиск
Реализуйте алгоритм приближенного бинарного поиска.

Входные данные

В первой строке входных данных содержатся числа N и K (1 ≤ N, K ≤ 100000).
Во второй строке задаются N чисел первого массива, отсортированного по
неубыванию. 
В третьей строке – K чисел второго массива.

Каждое число в обоих массивах целое и по модулю не превосходит 2 x 10^9.

Выходные данные

Для каждого из K чисел выведите в отдельную строку число из первого массива,
наиболее близкое к данному. Если таких несколько, выведите меньшее из них.
"""

def approximation_binary_search(array, x):
    left, right = -1, len(array) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if array[mid] <= x:
            left = mid
        else:
            right = mid
    if abs(array[right] - x) < abs(array[left] - x):
        return array[right]
    return array[left]


def main():
    n, k = map(int, input().split())
    lst1 = [int(i) for i in input().split()]
    lst2 = [int(i) for i in input().split()]
    print(
        *[approximation_binary_search(lst1, number) for number in lst2],
        sep='\n'
    )


if __name__ == '__main__':
    main()
