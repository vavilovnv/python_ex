"""
Ограниченная очередь.

Астрологи объявили день очередей ограниченного размера. Тимофею нужно написать
класс MyQueueSized, который принимает параметр max_size, означающий
максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой
очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит
5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит
5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:
push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове
операций pop() или peek() для пустой очереди нужно вывести «None».

Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.

Пример 1
Ввод
8
2
peek
push 5
push 2
peek
size
size
push 1
size
Вывод
None
5
2
2
error
2

Пример 2
Ввод
10
1
push 1
size
push 3
size
push 1
pop
push 1
pop
push 3
push 3
Вывод
1
error
1
error
1
1
error
"""

class MyQueueSized:

    def __init__(self, max_size):
        self.queue = []
        self.size = 0
        self.max_size = max_size

    def push(self, x):
        if self.size < self.max_size:
            self.queue.append(x)
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.size == 0:
            print('None')
        else:
            print(self.queue[0])
            self.size -= 1
            self.queue = self.queue[1:]

    def get_size(self):
        print(self.size)

    def peek(self):
        if self.size == 0:
            print('None')
        else:
            print(self.queue[0])


n = int(input())
queue = MyQueueSized(int(input()))
for _ in range(n):
    command = input().split()
    if command[0] == 'peek':
        queue.peek()
    if command[0] == 'push':
        queue.push(int(command[1]))
    if command[0] == 'pop':
        queue.pop()
    if command[0] == 'size':
        queue.get_size()
