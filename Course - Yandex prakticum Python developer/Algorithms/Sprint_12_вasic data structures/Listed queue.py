"""
Списочная очередь.

Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка. Помогите ему с реализацией. Очередь должна поддерживать
выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его. Если
очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
1000. В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.

Пример 1
Ввод
10
put -34
put -23
get
size
get
size
get
get
put 80
size
Вывод
-34
1
-23
0
error
error
1

Пример 2
Ввод
6
put -66
put 98
size
size
get
get
Вывод
2
2
-66
98

Пример 3
Ввод
9
get
size
put 74
get
size
put 90
size
size
size
Вывод
error
0
74
0
1
1
1

Примечания
Все операции должны выполняться за O(1).
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next_item = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self):
        if self.size == 0:
            print('error')
        else:
            print(self.head.value)
            self.head = self.head.next_item
            self.size -= 1

    def put(self, node):
        if self.size == 0:
            self.head = node
        elif self.size == 1:
            self.tail = node
            self.head.next_item = self.tail
        else:
            self.tail.next_item = node
            self.tail = self.tail.next_item
        self.size += 1

    def get_size(self):
        print(self.size)


queue = Queue()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'get':
        queue.get()
    if command[0] == 'put':
        queue.put(Node(int(command[1])))
    if command[0] == 'size':
        queue.get_size()
