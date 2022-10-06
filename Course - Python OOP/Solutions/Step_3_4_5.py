# Условие задачи https://stepik.org/lesson/701989/step/5?unit=702090

class NewList:

    def __init__(self, lst=[]):
        self.lst = lst[::]

    def get_list(self):
        return self.lst

    @staticmethod
    def sub_lists(list1, list2):
        list2, new_list = [str(i) for i in list2], []
        for i in list1:
            if str(i) not in list2:
                new_list.append(i)
            else:
                list2.remove(str(i))
        return new_list

    def __sub__(self, other):
        list2 = other
        if isinstance(other, NewList):
            list2 = other.get_list()
        return NewList(self.sub_lists(self.lst, list2))

    def __rsub__(self, other):
        return NewList(self.sub_lists(other, self.lst))
