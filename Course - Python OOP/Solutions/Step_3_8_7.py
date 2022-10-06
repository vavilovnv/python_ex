# Условие задачи https://stepik.org/lesson/701993/step/7?auth=login&unit=702094

class Stack:

    def __init__(self):
        self.top = None
        self.__count = 0

    @staticmethod
    def check_index(idx, count):
        if not (isinstance(idx, int) and 0 <= idx < count):
            raise IndexError('неверный индекс')

    def push(self, obj):
        if not isinstance(obj, StackObj):
            return
        if self.__count == 0:
            self.top = obj
        else:
            root = self.__getitem__(self.__count - 1)
            root.next = obj
        self.__count += 1

    def pop(self):
        if self.__count == 1:
            obj = self.top
            self.top = None
        elif self.__count > 1:
            obj = self.__getitem__(self.__count - 1)
            prev = self.__getitem__(self.__count - 2)
            prev.next = None
        self.__count -= 1
        return obj

    def __getitem__(self, idx):
        self.check_index(idx, self.__count)
        if idx == 0:
            return self.top
        count, root = 0, self.top
        while count < idx:
            count += 1
            root = root.next
        return root

    def __setitem__(self, idx, value):
        self.check_index(idx, self.__count)
        if idx == 0:
            next = self.top.next
            self.top = value
            self.next = next
        else:
            root = self.__getitem__(idx)
            prev = self.__getitem__(idx - 1)
            next = root.next
            root = value
            root.next, prev.next = next, root


class StackObj:

    def __init__(self, data):
        self.__next = None
        self.data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj
