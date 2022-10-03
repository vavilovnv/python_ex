"""
Стек - MaxEffective.

Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1). Для
пустого стека операция должна возвращать None. При этом push(x) и pop() также
должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит
100000. Далее идут команды по одной в строке. Команды могут быть следующих
видов:
push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для 
команды pop — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек
пустой, для команды get_max() напечатайте «None». Если происходит удаление из
пустого стека — напечатайте «error».

Пример 1
Ввод
10
pop
pop
push 4
push -5
push 7
pop
pop
get_max
pop
get_max
Вывод
error
error
4
None

Пример 2
Ввод
10
get_max
push -6
pop
pop
get_max
push 2
get_max
pop
push -2
push -6
Вывод
None
error
None
2
"""

class StackMaxEffective:

    def __init__(self):
        self.stack = []

    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
        else:
            self.stack.append(max(x, self.stack[-1]))

    def pop(self):
        if len(self.stack) == 0:
            print('error')
        else:
            self.stack.pop()

    def get_max(self):
        print('None' if len(self.stack) == 0 else self.stack[-1])


stack = StackMaxEffective()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'get_max':
        stack.get_max()
    if command[0] == 'push':
        stack.push(int(command[1]))
    if command[0] == 'pop':
        stack.pop()
