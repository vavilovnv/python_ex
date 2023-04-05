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
    curr = 0
    for i, v in enumerate(arr):
        if v != ' ':
            curr = i + 1
            break
    for i in range(curr + 1, len(arr)):
        if arr[i] != ' ':
            arr[curr], arr[i] = arr[i], arr[curr]
            curr += 1


arr = ['a', ' ', ' ', 'b', ' ', ' ', 'c']
solution(arr)
assert arr == ['a', 'b', 'c', ' ', ' ', ' ', ' ']
