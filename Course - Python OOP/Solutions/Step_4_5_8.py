# Условие задачи https://stepik.org/lesson/701999/step/8?unit=702100

from abc import ABC, abstractmethod


class StackObj:

    def __init__(self, data):
        self._next = None
        self._data = data


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        """Метод для добавления в конец стека"""

    @abstractmethod
    def pop_back(self):
        """Метод для удаления элемента с конца стека"""


class Stack(StackInterface):

    def __init__(self):
        self._top = None
        self.__count = 0

    def push_back(self, obj):
        if not isinstance(obj, StackObj):
            return
        if self.__count == 0:
            self._top = obj
        else:
            root = self.__getitem__(self.__count - 1)
            root._next = obj
        self.__count += 1

    def pop_back(self):
        if self.__count == 1:
            obj = self._top
            self._top = None
        elif self.__count > 1:
            obj = self.__getitem__(self.__count - 1)
            prev = self.__getitem__(self.__count - 2)
            prev._next = None
        self.__count -= 1
        return obj

    def __getitem__(self, idx):
        if not (isinstance(idx, int) and 0 <= idx < self.__count):
            raise IndexError('неверный индекс')
        if idx == 0:
            return self._top
        count, root = 0, self._top
        while count < idx:
            count += 1
            root = root._next
        return root
