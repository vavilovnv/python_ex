# Условие задачи https://stepik.org/lesson/701988/step/6?unit=702089

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if isinstance(obj, ObjList):
            if not self.head:
                self.head = obj
            else:
                self.tail.next = obj
                obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):

        count, root = 0, self.head
        while root and count < indx:
            count += 1
            root = root.next
        if root:
            prev_obj = root.prev
            next_obj = root.next
            if prev_obj:
                prev_obj.next = next_obj
            else:
                self.head = next_obj
            if next_obj:
                next_obj.prev = prev_obj
            else:
                self.tail = prev_obj

    def __len__(self):
        count, root = 0, self.head
        while root:
            count += 1
            root = root.next
        return count

    def __call__(self, indx):
        count, root = 0, self.head
        while root and count < indx:
            count += 1
            root = root.next
        return root.data


class ObjList:

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj
