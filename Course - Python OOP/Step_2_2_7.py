# Условие задачи https://stepik.org/lesson/701984/step/7?unit=702085

class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if not self.top:
            self.top = obj
        else:
            root = self.top
            while root.next:
                root = root.next
            root.next = obj

    def pop(self):
        if self.top:
            if not self.top.next:
                obj = self.top
                self.top = None
                return obj
            else:
                root = self.top
                while root:
                    if root.next.next:
                        root = root.next
                    else:
                        obj = root.next
                        root.next = None
                        return obj

    def get_data(self):
        lst = []
        root = self.top
        while root:
            lst.append(root.data)
            if root.next:
                root = root.next
            else:
                break
        return lst


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
