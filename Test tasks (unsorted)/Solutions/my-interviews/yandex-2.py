"""
В массиве символов нужно передвинуть в конец все пробелы с сохранением
исходного порядка непробелов.
Ограничение по памяти O(1). Ограничение по времени O(n).

Ввод:
arr = ['a', ' ', ' ', 'b', ' ', ' ', 'c']
Вывод:
arr = ['a', 'b', 'c', ' ', ' ', ' ', ' ']
"""

def solution(arr):
    left = 0
    for right in range(len(arr)) :
        if arr[right] != ' ':
            arr[left], arr[right] = arr[right], arr[left]
            left += 1


arr = ['a', ' ', ' ', 'b', ' ', ' ', 'c']
solution(arr)
assert arr == ['a', 'b', 'c', ' ', ' ', ' ', ' ']


"""
Есть основной произвольно задаваемый отрезок [A, B] и N произвольных дополнительных отрезков.
Необходимо вычислить общую длину основного отрезка на которой не происходит наложения доп. отрезков.

Пример
A = 15, B = 165
N1 = [37, 68]
N2 = [52, 74]
N3 = [118, 146]
N4 = [35, 44]
N5 = [37, 65]
N6 = [46, 74]

Ответ: 83
"""

# TC: O(n log n) SC: O(1)
# решение подойдет для float координат
def solution1(a, b, n):
    if not n:
        return b - a + 1
    n.sort(key=lambda x: x[0])
    res, l, r = 0, n[0][0], n[0][1]
    for i in range(1, len(n)):
        if r > n[i][0]:
            r = min(b, n[i][1])
        else:
            res += r - l
            l, r = max(a, n[i][0]), min(b, n[i][1])
    res += r - l
    return b - a - res

# TC: O(n) SC: O(n)
# решение не подойдет для float координат
def solution2(a, b, n):
    s = set(range(a, b))
    for i in n:
        s -= set(range(i[0], i[1]))
    return len(s)


a = 15
b = 165
n = [[37, 68], [52, 74], [118, 146], [35, 44], [37, 65], [46, 74]]
assert solution1(a, b, n) == 83
assert solution2(a, b, n) == 83