"""
Стек - Max.

Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс должен поддерживать операции
push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое не
превосходит 10000. В следующих n строках идут команды. Команды могут быть
следующих видов:
push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для 
команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек
пустой, для команды get_max() напечатайте «None». Если происходит удаление из
пустого стека — напечатайте «error».

Пример 1
Ввод
8
get_max
push 7
pop
push -2
push -1
pop
get_max
get_max
Вывод
None
-2
-2

Пример 2
Ввод
7
get_max
pop
pop
pop
push 10
get_max
push -9
Вывод
None
error
error
error
10
"""

class StackMax:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            print('error')
        else:
            self.stack.pop()

    def get_max(self):
        print('None' if len(self.stack) == 0 else max(self.stack))


stack = StackMax()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'get_max':
        stack.get_max()
    if command[0] == 'push':
        stack.push(int(command[1]))
    if command[0] == 'pop':
        stack.pop()
