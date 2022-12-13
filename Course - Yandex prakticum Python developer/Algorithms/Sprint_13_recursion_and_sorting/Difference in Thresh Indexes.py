"""
Разность треш-индексов.

Гоша долго путешествовал и измерил площадь каждого из n островов Алгосов, но
ему этого мало! Теперь он захотел оценить, насколько разнообразными являются
острова в составе архипелага.

Для этого Гоша рассмотрел все пары островов (таких пар, напомним,
n * (n-1) / 2) и посчитал попарно разницу площадей между всеми островами.
Теперь он собирается упорядочить полученные разницы, чтобы взять k-ую по
порядку из них.

Помоги Гоше найти k-ю минимальную разницу между площадями эффективно.

Пояснения к примерам

Пример 1

Выпишем все пары площадей и найдём соответствующие разницы

|2 - 3| = 1
|3 - 4| = 1
|2 - 4| = 2
Так как нам нужна 2-я по величине разница, то ответ будет 1.

Пример 2

У нас есть два одинаковых элемента в массиве —– две единицы, поэтому
минимальная (первая) разница равна нулю.

Формат ввода
В первой строке записано натуральное число n –— количество островов в
архипелаге (2 ≤ n ≤ 100 000).

В следующей строке через пробел записаны n площадей островов — n натуральных
чисел, каждое из которых не превосходит 1 000 000.

В последней строке задано число k. Оно находится в диапазоне от 1 до 
n(n - 1) / 2.

Формат вывода
Выведите одно число –— k-ую минимальную разницу.

Пример 1
Ввод
3
2 3 4
2
Вывод
1

Пример 2
Ввод
3
1 3 1
1
Вывод
0

Пример 3
Ввод
3
1 3 5
3
Вывод
4
"""

def check_index(arr, half, k, n):
    left = count = 0
    for right in range(n):
        r_value, l_value = arr[right], arr[left]
        while r_value - l_value > half:
            left += 1
            l_value = arr[left]
        count += right - left
        if count >= k:
            return True
    return False


def get_k_min(n, lst, k):
    left, right = 0, lst[-1] - lst[0]
    while left < right:
        half = (left + right) // 2
        if check_index(lst, half, k, n):
            right = half
        else:
            left = half + 1
    return left


print(
    get_k_min(
        int(input()),
        sorted(list(map(int, input().split()))),
        int(input()))
    )