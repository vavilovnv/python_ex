# Условие задачи https://stepik.org/lesson/701984/step/9?unit=702085

class TreeObj:

    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__root = self.__left = self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.indx] == 1:
            if obj.left:
                return obj.left
        else:
            if obj.right:
                return obj.right
        return None

    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if not obj_next:
                break
            obj = obj_next

        return obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj
