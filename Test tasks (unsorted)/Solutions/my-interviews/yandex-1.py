"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку, 
сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
- [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
- [1, 4, 3, 2] => "1-4"
- [1, 4] => "1,4"
"""

def group_out(g_start, g_end):
    if g_start == g_end:
        return str(g_end)
    return f'{g_start}-{g_end}'


def compress(l):
    if not l:
        return ''
    l = sorted(l)
    res, g_start, g_end = [], l[0], l[0]
    for n in l[1:]:
        if g_end == n-1:
            g_end = n
        else:
            res.append(group_out(g_start, g_end))
            g_start = n
            g_end = n
    res.append(group_out(g_start, g_end))
    return ','.join(res)


"""
Написать стек с константным поиском максимального элемента.

push, pop, max должны работать за O(1).
"""
class MaxStack(object):
    def __init__(self):
        self.stack = []
 
    def push(self, elem):
        if not self.stack:
            self.stack.append((elem, elem))
        else:
            m = max(self.stack[-1][1], elem)    
            self.stack.append((elem, m))        

    def pop(self) -> int:
        if self.stack:
            m = self.stack.pop()
            return m[0]
        raise Exception('Стек пустой')

    def max(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        raise Exception('Стек пустой')


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
