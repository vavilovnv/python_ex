# Условие задачи https://stepik.org/lesson/13240/step/8?auth=login&unit=3426

# Первая строка входа содержит число операций 1 ≤ n ≤ 10^5. Каждая из
# последующих nn строк задают операцию одного из следующих двух типов:
# Insert x, где x 0 ≤ x ≤ 10^9 — целое число;
# ExtractMax.
# Первая операция добавляет число x в очередь с приоритетами, вторая —
# извлекает максимальное число и выводит его.

class PriorityQueue:
    """Класс реализующий очередь с приоритетами на основе списка."""

    def __init__(self):
        self._queue = []
        self._size = 0

    def __swap_elements(self, i, j):
        self._queue[i], self._queue[j] = self._queue[j], self._queue[i]

    def __sift_up(self, i):
        """Просеивание элемента вверх по двоичному дереву."""
        while i - 1 >= 0 and self._queue[i] > self._queue[(i - 1) // 2]:
            self.__swap_elements(i, (i - 1) // 2)
            i = (i - 1) // 2

    def __sift_down(self, i):
        """Просеивание элемента вниз по двоичному дереву."""

        while 2 * i + 1 < self._size:
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if (right < self._size
                    and self._queue[right] > self._queue[left]):
                j = right
            if self._queue[i] >= self._queue[j]:
                break
            self.__swap_elements(i, j)
            i = j

    def insert(self, value):
        """Добавление элемента в очередь."""

        self._queue.append(int(value))
        self.__sift_up(self._size)
        self._size += 1

    def extractmax(self):
        """Получение максимального элемента из очереди."""

        max_value = self._queue[0]
        self._size -= 1
        self._queue[0] = self._queue[self._size]
        self._queue.pop(self._size)
        self.__sift_down(0)
        return max_value


def main():
    queue = PriorityQueue()
    for _ in range(int(input())):
        command = input().strip().split()
        if len(command) > 1:
            queue.__getattribute__(command[0].lower())(command[1])
        else:
            print(queue.__getattribute__(command[0].lower())())


if __name__ == '__main__':
    main()
