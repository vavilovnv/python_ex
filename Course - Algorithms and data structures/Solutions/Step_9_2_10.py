# Условие задачи https://stepik.org/lesson/306286/step/10?unit=756168

"""
Красивая гора.
Дан массив A из n целых чисел. Выведите YES, если массив является красивой
горой, иначе - NO.

Массив называется красивой горой, если с начала массива элементы строго
возрастают, а далее с какого-то момента строго убывают.

Иначе говоря, существует некоторое i (0 < i < n − 1), для которого выполняются
следующие условия:
A[0] <A[1] < ... < A[i − 1] < A[i] (сначала массива до i-го элемента строго
возрастает)
A[i] > A[i + 1]> ... > A[n − 1] (начиная с i-го элемента и до конца массива
строго убывает)
 
Входные данные:
В первой строке задается одно натуральное число n ≥ 3, не превосходящее 100.
Во второй строке вводятся n целых чисел, каждое из которых по модулю не
превосходит 100. 

Выходные данные.
Выведите YES, если массив является красивой горой, иначе - NO.
"""

from collections import Counter

def main(n, arr):
    res, left, right = 'NO', 0, n - 1
    while left <= right:
        mid = left + (right - left)
        if 0 < mid < n - 1 and arr[mid - 1] < arr[mid] > arr[mid + 1]:
            d1, d2 = Counter(arr[0: mid+1]), Counter(arr[mid: n])
            if max(d1.values()) == 1 and max(d2.values()) == 1:
                return 'YES'
            return res
        if mid < n - 1 and arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return res


if __name__ == '__main__':
    print(
        main(int(input()), list(map(int, input().split())))
    )
