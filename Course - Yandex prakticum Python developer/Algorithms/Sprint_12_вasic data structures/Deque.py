"""
Дек.

Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x), pop_back(),
pop_front() работали корректно. Но, если в деке было много элементов,
программа работала очень долго. Дело в том, что не все операции выполнялись за
O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
100000. Во второй строке записано число m — максимальный размер дека. Он не
превосходит 50000. В следующих n строках записана одна из команд:
push_back(value) – добавить элемент в конец дека. Если в деке уже находится
максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится
максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то
вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст,
то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных
запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример 1
Ввод
4
4
push_front 861
push_front -819
pop_back
pop_back
Вывод
861
-819

Пример 2
Ввод
7
10
push_front -855
push_front 0
pop_back
pop_back
push_back 844
pop_back
push_back 823
Вывод
-855
0
844

Пример 3
Ввод
6
6
push_front -201
push_back 959
push_back 102
push_front 20
pop_front
pop_back
Вывод
20
102
"""

from typing import Optional


class Deque:
    """Класс реализующий логику Дека на основе очереди на циклическом
    буфере. Если head и tail равны, то очередь пуста, в противном случае,
    т.к. очередь зациклена, head следует за tail."""

    def __init__(self, max_size: int) -> None:
        """Инициализация атрибутов класса Дек. Атрибуты сделаны приватными,
        чтобы в логику работы методов нельзя было вмешаться изменив значение
        какого-либо из атрибутов извне класса."""

        self.__head = self.__tail = 0  # Индексы начала и окончания очереди
        self.__size = 0  # Текущий размер очереди
        self.__values = [None] * max_size  # Список значений очереди
        self.__max_size = max_size  # Максимальный размер очереди

    def push_front(self, value: int) -> None:
        """Добавление элемента по индексу head. Циклически сдвигаем индекс
        head на предыдущую позицию. Увеличиваем текущий размер очереди."""

        if self.__size == self.__max_size:
            print('error')
            return
        self.__values[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.__max_size
        self.__size += 1

    def push_back(self, value: int) -> None:
        """Добавление элемента по индексу tail. Циклически сдвигаем индекс
        tail на следующую позицию. Увеличиваем текущий размер очереди."""

        if self.__size == self.__max_size:
            print('error')
            return
        self.__values[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def pop_front(self) -> Optional[int]:
        """Получение элемента по индексу head. Циклически сдвигаем индекс
        head на следующую позицию. Уменьшаем текущий размер очереди."""

        if self.__size != 0:
            value = self.__values[self.__head]
            self.__values[self.__head] = None
            self.__head = (self.__head + 1) % self.__max_size
            self.__size -= 1
            return value
        print('error')

    def pop_back(self) -> Optional[int]:
        """Получение элемента по индексу предшествующему tail. Циклически сдвигаем
        индекс tail на предыдущую позицию. Уменьшаем текущий размер очереди."""

        if self.__size != 0:
            value = self.__values[self.__tail - 1]
            self.__values[self.__tail - 1] = None
            self.__tail = (self.__tail - 1) % self.__max_size
            self.__size -= 1
            return value
        print('error')


def main():
    n, m = int(input()), int(input())
    deque = Deque(m)
    for _ in range(n):
        command = input().strip().split()
        func = getattr(deque, command[0])  # получаем атрибут-метод класса по имени
        if len(command) > 1:
            result = func(int(command[1]))
        else:
            result = func()
        if result is not None:
            print(result)


if __name__ == '__main__':
    main()
