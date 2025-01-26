"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку, 
сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
- [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
- [1, 4, 3, 2] => "1-4"
- [1, 4] => "1,4"
"""

def solution(arr):
    res = []
    arr.sort()
    curr = curr_min = arr[0]
    for num in arr:
        if num - curr > 1:
            res.append(f"{curr_min}-{curr}" if curr_min != curr else str(curr))
            curr_min = num
        curr = num
    res.append(f"{curr_min}-{curr}" if curr_min != curr else str(curr))
    return ",".join(res)


"""
Написать стек с константным поиском максимального элемента.

push, pop, max должны работать за O(1).
"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append((item, item if not self.stack else max(item, self.stack[-1][1])))

    def pop(self):
        if self.stack:
            raise ValueError("Стек пустой")
        value, _ = self.stack.pop()
        return value

    def max(self):
        if self.stack:
            raise ValueError("Стек пустой")
        _, max_value = self.stack[-1][1]
        return max_value


"""
Написать очередь с константным поиском максимального элемента.

push, pop, max должны работать за O(1).

P.s. Задачи на интевью не было, но интерьювер заметил, что есть и такая.
"""

class MaxStack(object):
    def __init__(self):
        self.queue = []
        self.max = []

    def push(self, elem):
        if not self.max or self.max[-1] < elem:
            self.max.append(elem)
        self.queue.append(elem)

    def pop(self) -> int:
        if self.queue:
            m = self.queue.pop(0)
            if m == self.max[-1]:
                self.max.pop()
            return m
        raise Exception('Очередь пуста')

    def max(self) -> int:
        if self.max:
            return self.max[-1]
        raise Exception('Очередь пуста')
