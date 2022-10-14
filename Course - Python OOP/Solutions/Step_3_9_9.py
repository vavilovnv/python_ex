# Условие задачи https://stepik.org/lesson/701994/step/9?auth=login&unit=702095

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
            

class Stack:

    def __init__(self):
        self.top = None
        self.__count = 0

    @staticmethod
    def check_index(idx, count):
        if not (isinstance(idx, int) and 0 <= idx < count):
            raise IndexError('неверный индекс')

    def __len__(self):
        return self.__count

    def push_back(self, obj):
        if not isinstance(obj, StackObj):
            return
        if self.__count == 0:
            self.top = obj
        else:
            root = self.__getitem__(self.__count - 1, False)
            root.next = obj
        self.__count += 1

    def push_front(self, obj):
        if not isinstance(obj, StackObj):
            return
        if self.__count == 0:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj
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

    def __getitem__(self, idx, get_data=True):
        self.check_index(idx, self.__count)
        if idx == 0:
            return self.top.data if get_data else self.top
        count, root = 0, self.top
        while count < idx:
            count += 1
            root = root.next
        return root.data if get_data else root

    def __setitem__(self, idx, value):
        self.check_index(idx, self.__count)
        if idx == 0:
            next = self.top.next
            self.top.data = value
            self.next = next
        else:
            root = self.__getitem__(idx, False)
            prev = self.__getitem__(idx - 1, False)
            next = root.next
            root.data = value
            root.next, prev.next = next, root

    def __iter__(self):
        for i in range(len(self)):
            yield self.__getitem__(i, False)
