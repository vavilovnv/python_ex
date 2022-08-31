from collections import OrderedDict


class LRUCache:
    """Класс реализующий LRU cache на OrderedDict. Ёмкость кэша
    задается параметром capacity. Последний использованный (актуальный)
    элемент кэша всегда в конце словаря. При превышении емкости кэша
    удаляется первый элемент словаря."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.__cache = OrderedDict()
        self.__size = 0

    def pull(self, key):
        """Возвращает значение по ключу и "актуализирует" элемент
        словаря, перенося его в конец. Если указанного ключа в
        словаре нет, возвращает None."""

        if key not in self.__cache:
            return None
        else:
            self.__cache.move_to_end(key)
            self.__size = max(self.__size - 1, 0)
            return self.__cache[key]

    def push(self, key, value):
        """Добавляет ключ и значение в кэш и "актуализирует" элемент
        словаря, перенося его в конец. При превышении емкости кэша
        удаляется первый элемент из словаря."""

        self.__cache[key] = value
        self.__cache.move_to_end(key)
        self.__size = min(self.__size + 1, self.capacity)
        if len(self.__cache) > self.capacity:
            self.__cache.popitem(last=False)

    def size(self):
        """Возвращает текущую заполненность кэша."""

        return self.__size


def main():
    cache = LRUCache(2)
    cache.push(1, 1)
    print(cache.size())
    cache.push(2, 2)
    print(cache.size())
    cache.pull(1)
    print(cache.size())
    cache.push(3, 3)
    print(cache.size())
    cache.pull(2)
    print(cache.size())
    cache.push(4, 4)
    print(cache.size())
    cache.pull(1)
    print(cache.size())
    cache.pull(3)
    print(cache.size())
    cache.pull(4)
    print(cache.size())


if __name__ == '__main__':
    main()
