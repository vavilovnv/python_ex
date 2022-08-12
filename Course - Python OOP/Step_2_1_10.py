# Условие задачи https://stepik.org/lesson/701983/step/10?unit=702084

class LinkedList:

    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if isinstance(obj, ObjList):
            if not self.head:
                self.head = obj
            else:
                self.tail.set_next(obj)
                obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.tail:
            prev_obj = self.tail.get_prev()
            if prev_obj:
                prev_obj.set_next(None)
            self.tail = prev_obj
            if not self.tail:
                self.head = None

    def get_data(self):
        lst, root = [], self.head
        while root:
            lst.append(root.get_data())
            root = root.get_next()
        return lst


class ObjList:

    def __init__(self, data):
        self.__next = self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
